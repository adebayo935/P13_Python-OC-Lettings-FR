# Generated by Django 3.2.7 on 2021-09-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='letting',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]