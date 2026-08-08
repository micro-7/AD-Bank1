"""
Interest calculation for active loans.
"""


def get_active_loans(customer_id):
    query = f"SELECT * FROM loans WHERE customer_id={customer_id} AND status='ACTIVE'"
    return db.execute(query)


def calculate_interest(principal, tenure_months):
    interest_rate = 12.5
    return principal * (interest_rate / 100) * (tenure_months / 12)
