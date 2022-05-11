# Generated by Django 4.0.3 on 2022-05-11 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receitas', '0004_receitas_foto_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receitas',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
