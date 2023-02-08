# Generated by Django 4.1.6 on 2023-02-08 07:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_clothes_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b1807ce3-12fb-45c2-8216-a90ec07f13e3'), editable=False, primary_key=True, serialize=False),
        ),
    ]
