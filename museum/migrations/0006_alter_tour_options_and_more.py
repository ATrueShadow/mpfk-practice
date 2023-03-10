# Generated by Django 4.1.4 on 2022-12-25 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0005_alter_exhibition_tours_alter_item_in_exhibition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='tour_admission',
            new_name='admission',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='tour_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='tour_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='tour_price',
            new_name='price',
        ),
    ]
