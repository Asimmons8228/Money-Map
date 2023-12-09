from .models import Bill, Income, Expense, FinancialHealth



def get_finhealth(user):
  finhealth= FinancialHealth.objects.filter(user=user)
  bills= Bill.objects.filter(user=user)
  monthly_bills = sum(bill.amount for bill in bills)
  yearly_bills = monthly_bills * 12
  essential_bills = Bill.objects.filter(user = user, category='Essential')
  nonessential_bills = Bill.objects.filter(user = user, category = 'Nonessential')
  total_essential_bills = sum(bill.amount for bill in essential_bills)
  total_nonessential_bills = sum(bill.amount for bill in nonessential_bills) 
  first_name = user.first_name
  last_name = user.last_name
  full_name = first_name + ' ' + last_name

  income= Income.objects.filter(user= user)
  yearly_income= sum(income.amount for income in income)
  monthly_income= yearly_income / 12
  rounded_monthly_income = round(monthly_income, 2)

  expenses= Expense.objects.filter(user= user)
  total_expenses = sum(expense.amount for expense in expenses)
  yearly_estimated_expenses = total_expenses * 12
  essential_expenses = Expense.objects.filter(user =  user, category='Essential')
  nonessential_expenses = Expense.objects.filter(user =  user, category = 'Nonessential')
  total_essential_expenses = sum(expense.amount for expense in essential_expenses)
  total_nonessential_expenses = sum(expense.amount for expense in nonessential_expenses)
