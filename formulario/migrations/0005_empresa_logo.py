# Generated by Django 5.1.4 on 2024-12-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0004_alter_criterioinclusion_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/empresa/logo'),
        ),
    ]