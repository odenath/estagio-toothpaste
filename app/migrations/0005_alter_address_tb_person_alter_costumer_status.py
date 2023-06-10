# Generated by Django 4.2.1 on 2023-06-08 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_tb_personid_costumer_tb_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='tb_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person', unique=True),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
