# Generated by Django 4.2.1 on 2023-06-18 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_alter_tolov_tolangan_sana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tolov',
            name='tolangan_sana',
            field=models.DateField(blank=True, null=True),
        ),
    ]
