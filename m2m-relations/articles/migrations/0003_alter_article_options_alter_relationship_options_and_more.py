# Generated by Django 5.0.3 on 2024-03-20 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_relationship'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='relationship',
            options={'ordering': ['-is_main', 'tag__tag'], 'verbose_name': 'Связь', 'verbose_name_plural': 'Связи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='articles.Relationship', to='articles.tag', verbose_name='Раздел'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='статья'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='тег'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=100, verbose_name='Тег'),
        ),
    ]
