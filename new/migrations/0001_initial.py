# Generated by Django 2.2.14 on 2021-01-12 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Jag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('end_time', models.DateField()),
                ('ph', models.ImageField(blank=True, upload_to='static/')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.Todo')),
            ],
        ),
    ]
