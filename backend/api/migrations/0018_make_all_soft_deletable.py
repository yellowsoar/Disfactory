# Generated by Django 2.2.10 on 2020-04-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200426_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reportrecord',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]