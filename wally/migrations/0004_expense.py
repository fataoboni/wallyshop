# Generated by Django 5.0.3 on 2024-04-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wally', '0003_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
