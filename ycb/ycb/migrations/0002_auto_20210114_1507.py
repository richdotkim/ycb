# Generated by Django 3.1.2 on 2021-01-14 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ycb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(blank=True),
        ),
    ]
