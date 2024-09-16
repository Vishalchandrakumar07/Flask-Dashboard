from application import db, app
from application.models import IncomeExpenses

with app.app_context():
    # Create all tables
    db.create_all()

    # Create entries to add to the database
    entry1 = IncomeExpenses(type="income", amount=4000, category="salary")
    entry2 = IncomeExpenses(type="expense", amount=3000, category="rent")
    entry3 = IncomeExpenses(type="expense", amount=2000, category="feeding")
    entry4 = IncomeExpenses(type="income", amount=7000, category="salary")

    # Add entries to the session
    db.session.add(entry1)
    db.session.add(entry2)
    db.session.add(entry3)
    db.session.add(entry4)

    # Commit the changes to the database
    db.session.commit()

    # Query all entries and print them
    entries = IncomeExpenses.query.all()

    for entry in entries:
        print(f"{entry.type}, {entry.category}, {entry.amount}, {entry.date}")
