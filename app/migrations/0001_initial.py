# Generated by Django 3.0.1 on 2020-05-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quality', models.CharField(max_length=30)),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodAmmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.CharField(max_length=30)),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fooditems',
            fields=[
                ('name', models.IntegerField(primary_key=True, serialize=False)),
                ('Quality', models.CharField(max_length=30)),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodMaxmam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.FileField(blank=True, upload_to='profile_pice/')),
                ('Booking', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('name', models.IntegerField(primary_key=True, serialize=False)),
                ('foodname', models.FileField(blank=True, upload_to='profile_pice/')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Total', models.CharField(max_length=30)),
                ('Booking', models.CharField(max_length=30)),
                ('Date', models.DateField(auto_now_add=True)),
                ('discount', models.CharField(max_length=30)),
            ],
        ),
    ]
