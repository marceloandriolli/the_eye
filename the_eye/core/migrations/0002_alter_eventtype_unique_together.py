# Generated by Django 3.2.7 on 2021-09-15 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventtype',
            unique_together={('category', 'name')},
        ),
    ]
