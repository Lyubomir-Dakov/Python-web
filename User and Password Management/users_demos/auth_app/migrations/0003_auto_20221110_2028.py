# Generated by Django 3.2.16 on 2022-11-10 18:28

from django.db import migrations, models
import users_demos.auth_app.managers


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_auto_20221110_1900'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
                ('objects', users_demos.auth_app.managers.AppUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]