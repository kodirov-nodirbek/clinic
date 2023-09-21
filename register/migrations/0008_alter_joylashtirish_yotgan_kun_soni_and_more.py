# Generated by Django 4.2.1 on 2023-06-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_alter_joylashtirish_yotgan_kun_soni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joylashtirish',
            name='yotgan_kun_soni',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tolov',
            name='xulosa_holati',
            field=models.CharField(blank=True, choices=[('Topshirilyapti', 'Topshirilyapti'), ('Kutyapti', 'Kutyapti'), ('Kiritildi', 'Kiritildi')], max_length=30, null=True),
        ),
    ]
