# Generated by Django 4.2.1 on 2023-06-02 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('resume', models.TextField()),
                ('rank', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
