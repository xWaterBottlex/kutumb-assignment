# Generated by Django 3.0.6 on 2020-05-20 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_auto_20200520_1512'),
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Company.Company'),
        ),
    ]
