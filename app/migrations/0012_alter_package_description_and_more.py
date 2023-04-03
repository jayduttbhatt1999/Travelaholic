# Generated by Django 4.1.7 on 2023-04-01 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_booking_packbook_package_package_airport_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='package_price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='packbook',
            name='ispackage_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ispackage_name', to='app.package'),
        ),
    ]