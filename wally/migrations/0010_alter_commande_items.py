# Generated by Django 4.2.3 on 2024-04-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wally', '0009_remove_commande_produits_remove_commande_statut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='items',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
