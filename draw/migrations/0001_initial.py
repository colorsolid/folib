# Generated by Django 2.2.6 on 2019-11-28 03:37

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=50)),
                ('user_id', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='draw.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='DrawingBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('password', models.CharField(blank=True, default='', max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='draw.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='DrawingBoardGroup',
            fields=[
                ('name', models.CharField(default='--MAIN--', max_length=16)),
                ('board', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='draw.DrawingBoard')),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(default='#000', max_length=20)),
                ('coords', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=2), size=None)),
                ('thickness', models.IntegerField(default=1)),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='draw.Drawing')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='boards',
            field=models.ManyToManyField(to='draw.DrawingBoard'),
        ),
        migrations.AddField(
            model_name='artist',
            name='groups',
            field=models.ManyToManyField(to='draw.DrawingBoardGroup'),
        ),
    ]