# Generated by Django 2.0.4 on 2018-05-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0021_delete_common'),
    ]

    operations = [
        migrations.CreateModel(
            name='common',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turb', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=30)),
            ],
        ),
    ]
