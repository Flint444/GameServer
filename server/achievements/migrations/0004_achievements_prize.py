# Generated by Django 4.1.2 on 2022-10-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0003_rename_getachievements_userachievements'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='prize',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]