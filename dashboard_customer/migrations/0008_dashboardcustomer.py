# Generated by Django 4.1 on 2022-12-03 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '__first__'),
        ('dashboard_driver', '__first__'),
        ('dashboard_customer', '0007_remove_review_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.customer')),
                ('order', models.ManyToManyField(blank=True, to='dashboard_driver.order')),
            ],
        ),
    ]
