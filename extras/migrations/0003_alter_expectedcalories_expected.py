# Generated by Django 4.2.2 on 2023-06-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0002_alter_expectedcalories_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expectedcalories',
            name='expected',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]