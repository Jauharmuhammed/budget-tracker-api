from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Income, Expense, IncomeCategory, ExpenseCategory, ExpenseAccount


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'date', 'user')
    list_filter = ('category', 'date', 'user')
    search_fields = ('amount', 'category__name', '', 'user__username')
    readonly_fields = ('created_date', 'modified_date')

    fieldsets = (
        (None, {
            'fields': ('amount', 'category', 'account', 'date', 'note')
        }),
        ('Audit Information', {
            'fields': ('created_date', 'modified_date'),
            'classes': ('collapse',),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'account', 'date')
    list_filter = ('category', 'account', 'date', 'user')
    search_fields = ('amount', 'category__name', 'account__name', 'note', 'user__username')
    readonly_fields = ('created_date', 'modified_date')

    fieldsets = (
        (None, {
            'fields': ('amount', 'category', 'account', 'date', '', 'user')
        }),
        ('Audit Information', {
            'fields': ('created_date', 'modified_date'),
            'classes': ('collapse',),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(IncomeCategory, ExpenseCategory, ExpenseAccount)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')
    readonly_fields = ('created_date', 'modified_date')

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Audit Information', {
            'fields': ('created_date', 'modified_date'),
            'classes': ('collapse',),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
