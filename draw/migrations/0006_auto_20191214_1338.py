# Generated by Django 2.2.6 on 2019-12-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0005_auto_20191210_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='end_index',
            field=models.IntegerField(default=-1),
        ),
    ]