from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

INCOMES = (
    ('Earned', 'Earned'),
    ('Passive', 'Passive'),
    ('Portfolio', 'Portfolio'),
)

BILLS = (
  ('Essential', 'Essential'),
  ('Nonessential', 'Nonessential'),
)

EXPENSES = (
  ('Essential', 'Essential'),
  ('Nonessential', 'Nonessential'),
)

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)

#     def __str__(self):
#         return self.username

class Income(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=255, 
        choices=INCOMES, 
        default=INCOMES[0][0]
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Income for {self.user.username}"

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=255, 
        choices=BILLS, 
        default=BILLS[0][0]
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField('Expense Date')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=255, 
        choices=EXPENSES, 
        default=EXPENSES[0][0]
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.user.username}"
    
    class Meta:
        ordering = ['-date']

class FinancialHealth(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=50)
    recommendations = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Financial Health for {self.user.username}"

class Location(models.Model):
    state = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.state}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
