# Generated by Django 5.1.6 on 2025-02-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_coin_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='image',
            field=models.ImageField(default='Error 404', upload_to='image/'),
        ),
    ]
