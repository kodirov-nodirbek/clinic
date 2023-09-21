# Generated by Django 4.2.1 on 2023-08-24 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0028_alter_bemor_sharif'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubYollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('matn', models.TextField()),
                ('narx', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='yollanma',
            name='narx',
        ),
        migrations.RemoveField(
            model_name='yollanma',
            name='xulosa_shablon_id',
        ),
        migrations.AddField(
            model_name='yollanma',
            name='footer_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='yollanma',
            name='header_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='XulosaShablon',
        ),
        migrations.AddField(
            model_name='subyollanma',
            name='yollanma_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.yollanma'),
        ),
        migrations.AddField(
            model_name='tolov',
            name='subyollanma_idlar',
            field=models.ManyToManyField(blank=True, null=True, to='register.subyollanma'),
        ),
    ]
