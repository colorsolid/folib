# Generated by Django 2.2.6 on 2019-11-28 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawing',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='draw.DrawingBoard'),
        ),
    ]