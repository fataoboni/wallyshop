# Generated by Django 4.2.3 on 2024-04-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wally', '0010_alter_commande_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='telephone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]