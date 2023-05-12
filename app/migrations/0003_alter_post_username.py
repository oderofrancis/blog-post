# Generated by Django 4.0 on 2023-05-12 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
