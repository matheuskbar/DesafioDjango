# Generated by Django 3.2.4 on 2021-09-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]