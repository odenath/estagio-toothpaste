# Generated by Django 4.2.1 on 2023-05-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_usuario_uf_usuario_birthdate_usuario_cnpj_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Phone',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cro_number',
            field=models.CharField(max_length=8),
        ),
    ]
