# Generated by Django 3.2.7 on 2021-10-06 03:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=2, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]