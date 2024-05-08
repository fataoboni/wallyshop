# Generated by Django 4.2.3 on 2024-04-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wally', '0008_remove_product_stock_stock_produit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='produits',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='statut',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='user',
        ),
        migrations.AddField(
            model_name='commande',
            name='infouser',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commande',
            name='items',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]