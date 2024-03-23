from django.db import models
from django.contrib.auth.models import User


class IncomeCategory(models.Model):
    name = models.CharField(max_length=128)
    icon = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    note = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=128)
    icon = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    parent_category = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.RESTRICT)
    level = models.PositiveIntegerField()

    note = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ExpenseAccount(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    note = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    name = models.CharField(max_length=256)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    expected_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.RESTRICT)
    account = models.ForeignKey(ExpenseAccount, on_delete=models.RESTRICT)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    note = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Income of {self.amount} on {self.date}"


class Expense(models.Model):
    name = models.CharField(max_length=256)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    expected_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.RESTRICT)
    account = models.ForeignKey(ExpenseAccount, on_delete=models.RESTRICT)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    note = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Expense of {self.amount} on {self.date}"
