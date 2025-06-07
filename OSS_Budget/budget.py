import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.budget_limit = None

    def set_budget(self, limit):  
        self.budget_limit = limit
        print(f"예산이 {limit}원으로 설정되었습니다.\n")

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
        
        if self.budget_limit is not None:
            total = sum(e.amount for e in self.expenses)
            if total > self.budget_limit:
                print("예산을 초과했습니다\n")
            else:
                print(f" 현재 총 지출: {total}원 / 예산: {self.budget_limit}원\n")
        else:
            print()
    

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


