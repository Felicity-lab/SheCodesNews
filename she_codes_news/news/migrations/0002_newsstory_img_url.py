# Generated by Django 3.0.8 on 2020-08-01 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
