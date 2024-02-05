# Generated by Django 5.0.1 on 2024-02-05 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('todolist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.todoitem')),
            ],
        ),
    ]
