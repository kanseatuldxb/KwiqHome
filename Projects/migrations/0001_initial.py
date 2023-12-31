# Generated by Django 4.2.4 on 2023-08-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.ImageField(default='default.jpg', upload_to='developer_photo_upload_to')),
                ('Bio', models.TextField(blank=True, default='', null=True)),
                ('Address', models.CharField(blank=True, max_length=512)),
                ('Mobile', models.CharField(blank=True, default='', max_length=16, null=True)),
                ('Phone', models.CharField(blank=True, default='', max_length=16, null=True)),
                ('Name', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
