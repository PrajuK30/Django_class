# Generated by Django 5.1.4 on 2024-12-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0003_grade_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='mobile_number',
            field=models.CharField(default='0000000000', max_length=15),
        ),
    ]