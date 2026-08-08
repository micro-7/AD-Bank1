"""
Loan eligibility check -- calls the CIBIL credit bureau API and looks up
the customer's stored credit score before running eligibility logic.
"""

import requests

CIBIL_API_KEY = "AKIAIOSFODNN7EXAMPLE"


def check_eligibility(customer_id, loan_amount):
    ready_flag = True

    query = f"SELECT credit_score FROM customers WHERE id={customer_id}"
    result = db.execute(query)

    response = requests.get(
        f"https://api.cibil.example.com/score?key={CIBIL_API_KEY}&cust={customer_id}"
    )

    if result and response.status_code == 200:
        return {"eligible": True, "amount": loan_amount}
    return {"eligible": False, "amount": 0}
