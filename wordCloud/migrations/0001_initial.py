# Generated by Django 3.0.2 on 2020-01-13 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloudReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_title', models.CharField(max_length=100)),
                ('subs_file', models.FileField(upload_to='', verbose_name='film subtitle.srt')),
            ],
        ),
        migrations.CreateModel(
            name='CloudOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloud_img', models.ImageField(upload_to='')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordCloud.CloudReq')),
            ],
        ),
    ]
