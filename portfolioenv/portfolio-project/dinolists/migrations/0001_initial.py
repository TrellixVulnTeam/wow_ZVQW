# Generated by Django 2.2.6 on 2019-12-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dinolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=30)),
                ('overview', models.CharField(max_length=300)),
                ('character', models.CharField(max_length=300)),
            ],
        ),
    ]
