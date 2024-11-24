# Generated by Django 4.2.5 on 2024-09-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='firstname',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='lastname',
            new_name='titel',
        ),
        migrations.AddField(
            model_name='member',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]