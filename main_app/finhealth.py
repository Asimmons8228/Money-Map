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


  financial_health_score = (needs_score + savings_score + nonessential_score + essential_score) / 4 

  recommendations = get_recommendation(needs_score, nonessential_score, essential_score, savings_score)

  if financial_health_score == 100:
    financial_health_grade = 'A+'
  elif 95 <= financial_health_score < 100:
    financial_health_grade = 'A'
  elif 90 <= financial_health_score < 95:
    financial_health_grade = 'A-'
  elif 85 <= financial_health_score < 90:
    financial_health_grade = 'B+'
  elif 80 <= financial_health_score < 85:
    financial_health_grade = 'B'
  elif 75 <= financial_health_score < 80:
    financial_health_grade = 'C+'
  elif 70 <= financial_health_score < 75:
    financial_health_grade = 'C'
  elif 65 <= financial_health_score < 70:
    financial_health_grade = 'D+'
  elif 60 <= financial_health_score < 65:
    financial_health_grade = 'D'
  elif 0 <= financial_health_score < 60:
    financial_health_grade = 'F'
  else:
    financial_health_grade = 'Not Specified!'
  
  
  return  {
        'finhealth': finhealth,
        'bills': bills,
        'monthly_bills': monthly_bills,
        'yearly_bills': yearly_bills,
        'income': income,
        'yearly_income': yearly_income,
        'monthly_income': monthly_income,
        'rounded_monthly_income': rounded_monthly_income,
        'expenses': expenses,
        'total_expenses': total_expenses,
        'yearly_estimated_expenses': yearly_estimated_expenses,
        'needs_percent': needs_percent,
        'savings_percent': savings_percent,
        'nonessential_percent': nonessential_percent,
        'essential_percent': essential_percent,
        'financial_health_grade': financial_health_grade,
        'financial_health_score': financial_health_score,
        'needs_score': needs_score,
        'savings_score': savings_score,
        'nonessential_score': nonessential_score,
        'essential_score': essential_score,
        'needs_recommendation': recommendations[0],
        'nonessential_recommendation': recommendations[1],
        'essential_recommendation': recommendations[2],
        'savings_recommendation': recommendations[3],
        'non_essential_spending': non_essential_spending,
        'essential_spending': essential_spending,
        "savings": savings,
        'full_name': full_name,
    }
def calculate_score(percent, score_ranges):
    for lower, upper, score in score_ranges:
        if lower <= percent <= upper:
            return score

savings_ranges = [
    (30, 100, 100),
    (25, 30, 95),
    (20, 25, 90),
    (17, 20, 85),
    (15, 17, 80),
    (13, 15, 75),
    (11, 13, 70),
    (9, 11, 65),
    (7, 9, 60),
    (4, 7, 55),
    (1, 4, 50),
]

essential_ranges = [
    (0, 30, 100),
    (30, 35, 95),
    (35, 40, 90),
    (40, 45, 85),
    (45, 50, 80),
    (50, 60, 75),
    (60, 65, 70),
    (65, 70, 65),
    (70, 75, 60),
    (75, 80, 55),
    (80, 100, 50),
]

nonessential_ranges = [
    (0, 15, 100),
    (15, 17, 95),
    (17, 19, 90),
    (19, 21, 85),
    (21, 23, 80),
    (23, 25, 75),
    (25, 27, 70),
    (27, 29, 65),
    (29, 30, 60),
    (30, 32, 55),
    (32, 100, 50),
]
needs_ranges = [
    (0, 50, 100),
    (50, 55, 95),
    (55, 60, 90),
    (60, 65, 85),
    (65, 70, 80),
    (70, 75, 75),
    (75, 80, 70),
    (80, 85, 65),
    (85, 90, 60),
    (90, 95, 55),
    (95, 100, 50),
]

