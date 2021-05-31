# Generated by Django 3.2.3 on 2021-05-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lastname', models.CharField(max_length=150)),
                ('bio', models.TextField()),
                ('birth', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('e_email', models.CharField(max_length=150)),
                ('website', models.CharField(max_length=150)),
            ],
        ),
    ]