from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Income, Expense, IncomeCategory, ExpenseCategory, ExpenseAccount


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'account', 'category', 'date')
    list_filter = ('category', 'account', 'date')
    search_fields = ('amount', 'category__name', '', 'user__username')
    readonly_fields = ('created_date', 'modified_date')

    fieldsets = (
        (None, {
            'fields': ('name', 'amount', 'expected_amount', 'category', 'account', 'date', 'note')
        }),
        ('Audit Information', {
            'fields': ('created_date', 'modified_date'),
            'classes': ('collapse',),
        }),
    )

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super().save_model(request, obj, form, change)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'category', 'account', 'date')
    list_filter = ('category', 'account', 'date')
    search_fields = ('amount', 'category__name',
                     'account__name', 'note', 'user__username')
    readonly_fields = ('created_date', 'modified_date')

    fieldsets = (
        (None, {
            'fields': ('name', 'amount', 'expected_amount', 'category', 'account', 'date', 'note')
        }),
        ('Audit Information', {
            'fields': ('created_date', 'modified_date'),
            'classes': ('collapse',),
        }),
    )

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super().save_model(request, obj, form, change)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'is_default', 'user')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')
    readonly_fields = ('created_date', 'modified_date')

    fieldsets = (
        (None, {
            'fields': ('name', 'icon', 'is_active', 'is_default', 'note')
        }),
        ('Audit Information', {
            'fields': ('created_date', 'modified_date'),
            'classes': ('collapse',),
        }),
    )


class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', "is_default", 'user')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')
    readonly_fields = ('created_date', 'modified_date')

    fieldsets = (
        (None, {
            'fields': ('name', 'icon', 'is_active', 'is_default', 'note')
        }),
        ('Audit Information', {
            'fields': ('created_date', 'modified_date'),
            'classes': ('collapse',),
        }),
    )


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'level',
                    'is_active', "is_default", 'user')
    list_filter = ('parent_category', 'level', 'user',)
    search_fields = ('name', 'user__username')
    readonly_fields = ('created_date', 'modified_date')

    fieldsets = (
        (None, {
            'fields': ('name', 'parent_category', 'level', 'icon', 'is_active', 'is_default', 'note')
        }),
        ('Audit Information', {
            'fields': ('created_date', 'modified_date'),
            'classes': ('collapse',),
        }),
    )


admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseAccount, AccountAdmin)
admin.site.register(IncomeCategory, IncomeCategoryAdmin)
admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
