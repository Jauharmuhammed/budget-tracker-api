# Generated by Django 4.2.1 on 2024-01-22 03:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_expense_expected_amount_expense_isactive_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='expenseaccount',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='expenseaccount',
            old_name='isDefault',
            new_name='is_default',
        ),
        migrations.RenameField(
            model_name='expensecategory',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='expensecategory',
            old_name='isDefault',
            new_name='is_default',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='incomecategory',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='incomecategory',
            old_name='isDefault',
            new_name='is_default',
        ),
        migrations.AddField(
            model_name='expense',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
