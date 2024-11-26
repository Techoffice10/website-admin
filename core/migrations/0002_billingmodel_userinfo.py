# Generated by Django 5.1.3 on 2024-11-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_address', models.CharField(max_length=255)),
                ('billing_to', models.CharField(max_length=255)),
                ('service_type', models.CharField(max_length=255)),
                ('bill_description', models.CharField(max_length=255)),
                ('ticket_id', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('emailed', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=3)),
                ('comments', models.CharField(default='No Comments', max_length=255)),
                ('invoice_no', models.IntegerField(blank=True, default=None, null=True)),
                ('invoice_date', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('node', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=100)),
                ('ext_no', models.CharField(max_length=50)),
                ('port_ip', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('power_broker_id', models.CharField(max_length=50)),
                ('applied_rating_id', models.CharField(max_length=50)),
                ('user_creation_date', models.DateField()),
                ('suspended_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('history', models.TextField(blank=True, null=True)),
            ],
        ),
    ]