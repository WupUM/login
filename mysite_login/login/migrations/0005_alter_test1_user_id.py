# Generated by Django 4.0.1 on 2022-06-25 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_test1_q1_test1_q2_test1_q3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test1',
            name='User_id',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='User_id', to='login.user'),
        ),
    ]
