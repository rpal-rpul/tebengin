# Generated by Django 4.1 on 2022-12-02 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '__first__'),
        ('dashboard_customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.customer'),
        ),
        migrations.AlterField(
            model_name='review',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.driver'),
        ),
    ]
