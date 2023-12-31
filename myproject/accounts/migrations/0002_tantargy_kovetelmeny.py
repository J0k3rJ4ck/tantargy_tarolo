# Generated by Django 4.2.4 on 2023-08-04 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tantargy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=200)),
                ('felhasznalo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kovetelmeny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leiras', models.TextField()),
                ('statusz', models.BooleanField(default=False)),
                ('tantargy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kovetelmenyek', to='accounts.tantargy')),
            ],
        ),
    ]
