# Generated by Django 4.2.10 on 2025-03-08 07:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('asset_type', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('acquisition_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('maintenance', 'Under Maintenance'), ('retired', 'Retired')], default='active', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assets',
                'ordering': ['-created_at'],
            },
        ),
    ]
