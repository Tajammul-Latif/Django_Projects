# Generated by Django 4.2.7 on 2023-12-04 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='MyImage')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
