# Generated by Django 4.0.4 on 2022-04-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
