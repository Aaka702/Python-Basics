from collections import defaultdict
import heapq

class ExpenseManager:
    def __init__(self):
        self.expenses = defaultdict(int)
        self.loans = defaultdict(int)

    def add_expense(self, payer, amount, *recipients):
        per_person_share = amount // len(recipients)
        for recipient in recipients:
            self.expenses[payer] -= per_person_share
            self.expenses[recipient] += per_person_share

    def add_loan(self, lender, borrower, amount):
        self.loans[lender] -= amount
        self.loans[borrower] += amount

    def reconcile_loans(self):
        result = []
        for lender, borrower, amount in self.loans:
            result.append((lender, borrower, amount))
