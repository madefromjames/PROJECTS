# Generated by Django 4.2.11 on 2024-09-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='Content_Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
