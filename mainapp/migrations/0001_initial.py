# Generated by Django 3.1.7 on 2021-05-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=10)),
                ('repeat_password', models.CharField(max_length=10)),
            ],
        ),
    ]
