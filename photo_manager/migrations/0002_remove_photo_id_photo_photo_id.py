# Generated by Django 4.1 on 2022-10-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='id',
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
