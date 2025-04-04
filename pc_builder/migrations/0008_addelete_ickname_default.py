# Generated by Django 4.2.19 on 2025-02-17 10:26

from django.db import migrations, models
import pc_builder.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pc_builder', '0007_add_nickname_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 사용중인 닉네임입니다.'}, max_length=15, null=True, unique=True, validators=[pc_builder.validators.validate_no_special_characters]),
        ),
    ]
