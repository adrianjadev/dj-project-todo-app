# Generated by Django 4.2.5 on 2023-09-21 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_alter_todoitem_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
