# Generated by Django 4.2.3 on 2024-03-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0004_rename_mobile_contact_us_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='name',
        ),
        migrations.AddField(
            model_name='images',
            name='username',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='xrayimages',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chest_ct',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
