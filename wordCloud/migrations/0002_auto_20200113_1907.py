# Generated by Django 3.0.2 on 2020-01-13 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordCloud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cloudreq',
            old_name='subs_file',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='cloudreq',
            old_name='film_title',
            new_name='title',
        ),
        migrations.DeleteModel(
            name='CloudOut',
        ),
    ]