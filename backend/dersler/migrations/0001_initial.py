# Generated by Django 3.2.13 on 2022-05-12 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('all_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dersler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinif_adi', models.CharField(max_length=100)),
                ('ders_sorumlusu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='all_users.akademisyen')),
            ],
        ),
    ]
