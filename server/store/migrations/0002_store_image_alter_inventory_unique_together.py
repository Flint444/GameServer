# Generated by Django 4.1.2 on 2022-10-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together={('title', 'nickname')},
        ),
    ]
