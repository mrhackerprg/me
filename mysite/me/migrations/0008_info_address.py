# Generated by Django 3.2.3 on 2021-05-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0007_remove_info_addres'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
