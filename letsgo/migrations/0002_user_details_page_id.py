# Generated by Django 3.1.7 on 2021-05-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsgo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='page_id',
            field=models.IntegerField(default=0),
        ),
    ]
