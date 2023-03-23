# Generated by Django 4.1.7 on 2023-03-21 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_provider', models.CharField(max_length=25, verbose_name='Provider name')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='provider',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.provider'),
        ),
    ]