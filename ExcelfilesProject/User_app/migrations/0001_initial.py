# Generated by Django 3.1.7 on 2021-03-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files_Data',
            fields=[
                ('fdid', models.AutoField(primary_key=True, serialize=False)),
                ('excel_file', models.FileField(upload_to='')),
            ],
        ),
    ]
