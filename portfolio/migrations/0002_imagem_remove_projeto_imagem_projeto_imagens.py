# Generated by Django 4.0 on 2023-03-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagens/')),
            ],
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='imagem',
        ),
        migrations.AddField(
            model_name='projeto',
            name='imagens',
            field=models.ManyToManyField(to='portfolio.Imagem'),
        ),
    ]
