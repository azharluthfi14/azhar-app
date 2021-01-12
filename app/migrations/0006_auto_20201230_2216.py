# Generated by Django 3.1.1 on 2020-12-30 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201230_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine_classification',
            name='user',
        ),
        migrations.AddField(
            model_name='wine_classification',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=88),
            preserve_default=False,
        ),
    ]
