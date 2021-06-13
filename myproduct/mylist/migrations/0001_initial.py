# Generated by Django 3.2.4 on 2021-06-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.CharField(max_length=10)),
                ('product_name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(blank=True, default='', max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='mylist/images')),
            ],
        ),
    ]
