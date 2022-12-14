# Generated by Django 4.1.1 on 2022-09-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('status', models.CharField(choices=[('done', 'DONE'), ('ongoing', 'ONGOING'), ('cancelled', 'CANCELLED')], max_length=10)),
                ('priority', models.CharField(choices=[('U', 'unset'), ('H', 'High'), ('L', 'Low')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
