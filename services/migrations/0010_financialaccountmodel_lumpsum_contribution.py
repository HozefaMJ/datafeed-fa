# Generated by Django 4.2.3 on 2023-07-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_financialaccountmodel_premium_holiday_commencement_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialaccountmodel',
            name='lumpsum_contribution',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
