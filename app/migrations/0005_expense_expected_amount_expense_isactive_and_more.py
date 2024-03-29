# Generated by Django 4.2.1 on 2024-01-22 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_income_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='expected_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='expenseaccount',
            name='icon',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expenseaccount',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='expenseaccount',
            name='isDefault',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expenseaccount',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expensecategory',
            name='icon',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expensecategory',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='expensecategory',
            name='isDefault',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expensecategory',
            name='level',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expensecategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='app.expensecategory'),
        ),
        migrations.AddField(
            model_name='income',
            name='expected_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='income',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='incomecategory',
            name='icon',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incomecategory',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='incomecategory',
            name='isDefault',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='expense',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.expenseaccount'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.expensecategory'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expenseaccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expensecategory',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='expensecategory',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expensecategory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='income',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.expenseaccount'),
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.incomecategory'),
        ),
        migrations.AlterField(
            model_name='income',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='incomecategory',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='incomecategory',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incomecategory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
