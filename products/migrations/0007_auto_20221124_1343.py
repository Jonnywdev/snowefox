# Generated by Django 3.2 on 2022-11-24 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
        ('products', '0006_club_sport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clubs', to='clubs.club', verbose_name='Club'),
        ),
        migrations.DeleteModel(
            name='Club',
        ),
    ]
