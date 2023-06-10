# Generated by Django 4.2.1 on 2023-06-08 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.CharField(max_length=2)),
                ('number', models.CharField(max_length=9)),
                ('tb_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phones',
                'db_table': 'tb_phone',
            },
        ),
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=2)),
                ('tb_personid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
            ],
            options={
                'verbose_name': 'Costumer',
                'verbose_name_plural': 'Costumers',
                'db_table': 'tb_costumer',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('street_avenue', models.CharField(max_length=40)),
                ('number', models.IntegerField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('uf', models.CharField(max_length=2)),
                ('additional_information', models.CharField(max_length=50)),
                ('tb_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'db_table': 'tb_address',
            },
        ),
    ]