# Generated by Django 2.1.7 on 2019-02-15 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190215_0155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nama_kategory',
            new_name='nama_kategori',
        ),
    ]
