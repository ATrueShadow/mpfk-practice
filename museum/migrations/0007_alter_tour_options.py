# Generated by Django 4.1.4 on 2022-12-25 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0006_alter_tour_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'ordering': ['date']},
        ),
    ]