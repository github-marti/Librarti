# Generated by Django 3.0.2 on 2020-01-28 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200127_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
        migrations.RemoveField(
            model_name='book',
            name='thoughts',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.CharField(choices=[('☆☆☆☆☆', 'No stars'), ('★☆☆☆☆', 'One star'), ('★★☆☆☆', 'Two stars'), ('★★★☆☆', 'Three stars'), ('★★★★☆', 'Four stars'), ('★★★★★', 'Five stars')], default='☆☆☆☆☆', max_length=255)),
                ('thoughts', models.CharField(blank=True, max_length=10000, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
    ]
