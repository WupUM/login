# Generated by Django 4.0.1 on 2022-06-30 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_test1_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test1',
            old_name='User_id',
            new_name='user',
        ),
    ]