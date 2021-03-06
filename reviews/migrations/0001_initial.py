# Generated by Django 3.2.5 on 2021-07-20 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arts.art')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.review')),
            ],
            options={
                'db_table': 'reviewimages',
            },
        ),
    ]
