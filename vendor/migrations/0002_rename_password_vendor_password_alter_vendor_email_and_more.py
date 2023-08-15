# Generated by Django 4.2.3 on 2023-08-15 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='Password',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='first_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='last_name',
            field=models.CharField(max_length=43),
        ),
    ]