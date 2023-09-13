# Generated by Django 4.0 on 2023-03-13 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20230310_0755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagem',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='imagens',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='video_youtube',
        ),
        migrations.AddField(
            model_name='imagem',
            name='descricao',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='projeto',
            name='nome',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens/'),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='projeto',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='portfolio.projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(blank=True, default=''),
        ),
    ]