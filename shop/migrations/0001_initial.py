# Generated by Django 2.1.7 on 2019-02-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='shop/static/images')),
                ('nama', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=25)),
                ('deskripsi', models.TextField(max_length=600)),
            ],
        ),
    ]
