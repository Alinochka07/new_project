# Generated by Django 3.2.7 on 2021-10-14 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20211012_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.IntegerField(default=0, verbose_name='Скидка %'),
        ),
    ]