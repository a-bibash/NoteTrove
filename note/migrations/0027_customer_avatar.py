# Generated by Django 4.2.3 on 2023-10-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0026_alter_room_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to='static/images'),
        ),
    ]
