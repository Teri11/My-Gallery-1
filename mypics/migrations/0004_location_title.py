# Generated by Django 3.2.5 on 2021-07-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypics', '0003_auto_20210703_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='title',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
