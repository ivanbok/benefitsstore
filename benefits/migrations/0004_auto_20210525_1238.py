# Generated by Django 3.1.2 on 2021-05-25 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0003_employeeuser_benefits'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedemptionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityRedeemed', models.IntegerField()),
                ('redemptionDateTime', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benefits.employeeuser')),
                ('buyerCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benefits.company')),
                ('listingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benefits.benefits')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benefits.benefitsprovidercompany')),
            ],
        ),
        migrations.RemoveField(
            model_name='transactionhistory',
            name='is_active',
        ),
        migrations.DeleteModel(
            name='TransactionHistoryArchived',
        ),
    ]
