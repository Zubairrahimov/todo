# Generated by Django 4.2.5 on 2023-09-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
