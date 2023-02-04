# Generated by Django 4.1.6 on 2023-02-03 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0004_alter_comentario_post_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='usuario_comentario',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
