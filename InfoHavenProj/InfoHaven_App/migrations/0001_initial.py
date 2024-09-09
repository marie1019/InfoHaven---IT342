# Generated by Django 4.2.5 on 2023-10-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('Member_ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Fname', models.CharField(max_length=50)),
                ('Lname', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Contact_Details', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Type', models.IntegerField(default=0)),
            ],
        ),
    ]
