from application import app, db
from flask import render_template, flash, redirect, url_for, get_flashed_messages
from application.form import UserInputForm
from application.models import IncomeExpenses
from sqlalchemy import func


@app.route("/")
def index():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    return render_template("index.html", title="index", entries=entries)


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    form = UserInputForm()
    if form.validate_on_submit():
        entry = IncomeExpenses(
            type=form.type.data, amount=form.amount.data, category=form.category.data
        )
        db.session.add(entry)
        db.session.commit()
        flash("Successful entry", "success")
        return redirect(url_for("index"))

    return render_template("add.html", title="add", form=form)


@app.route("/delete/<int:entry_id>")
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for("index"))


@app.route("/dashboard")
def dashboard():
    # Get total income and expenses
    income = (
        db.session.query(func.sum(IncomeExpenses.amount))
        .filter(IncomeExpenses.type == "income")
        .scalar()
        or 0
    )
    expenses = (
        db.session.query(func.sum(IncomeExpenses.amount))
        .filter(IncomeExpenses.type == "expense")
        .scalar()
        or 0
    )

    # Get data for chart
    categories = (
        db.session.query(IncomeExpenses.category, func.sum(IncomeExpenses.amount))
        .group_by(IncomeExpenses.category)
        .all()
    )

    return render_template(
        "dashboard.html", income=income, expenses=expenses, categories=categories
    )
