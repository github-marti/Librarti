# Generated by Django 3.0.2 on 2020-01-28 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200127_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='id',
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='books.Book'),
        ),
    ]
