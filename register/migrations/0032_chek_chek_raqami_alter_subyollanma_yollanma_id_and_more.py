# Generated by Django 4.2.1 on 2023-09-09 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0031_chek_vaqt_joylashtirish_kelish_vaqti_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chek',
            name='chek_raqami',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subyollanma',
            name='yollanma_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.yollanma'),
        ),
        migrations.AlterField(
            model_name='tolov',
            name='subyollanma_idlar',
            field=models.ManyToManyField(blank=True, default=[], null=True, to='register.subyollanma'),
        ),
    ]
