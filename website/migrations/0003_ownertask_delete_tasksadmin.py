# Generated by Django 4.1.5 on 2023-01-04 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_tasksadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fk_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.tasks')),
            ],
        ),
        migrations.DeleteModel(
            name='TasksAdmin',
        ),
    ]
