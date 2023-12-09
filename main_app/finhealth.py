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

  non_essential_spending = (total_nonessential_bills + total_nonessential_expenses) * 12
  essential_spending = (total_essential_bills + total_essential_expenses) * 12
  savings = yearly_income - (yearly_bills + yearly_estimated_expenses)

  needs_percent = (yearly_bills + yearly_estimated_expenses) / yearly_income * 100
  savings_percent = ((yearly_income - (yearly_bills + yearly_estimated_expenses)) / yearly_income) * 100
  nonessential_percent = (non_essential_spending / yearly_income) * 100
  essential_percent = (essential_spending / yearly_income) * 100

  needs_score = calculate_score(needs_percent, needs_ranges)
  essential_score = calculate_score(essential_percent, essential_ranges)
  nonessential_score = calculate_score(nonessential_percent, nonessential_ranges)
  savings_score= calculate_score( savings_percent, savings_ranges) 


