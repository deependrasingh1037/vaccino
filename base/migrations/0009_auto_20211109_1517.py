# Generated by Django 2.2.1 on 2021-11-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20211109_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccdetails',
            name='date1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vaccdetails',
            name='date2',
            field=models.DateField(blank=True, null=True),
        ),
    ]