# Generated by Django 3.2.3 on 2022-04-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0019_rename_hotels_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='distance',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]