# Generated by Django 4.1.7 on 2023-03-27 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_package_package_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ok - 1 star'), (2, 'Average - 2 star'), (3, 'Fine - 3 star'), (4, 'Good - 4 star'), (5, 'Excellent - 5 star')], default=1),
        ),
    ]