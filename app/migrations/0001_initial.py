# Generated by Django 4.0 on 2023-05-10 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('page', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]