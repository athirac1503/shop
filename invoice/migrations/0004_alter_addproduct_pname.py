# Generated by Django 3.2.13 on 2022-08-17 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20220816_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='pname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
