# Generated by Django 5.0.7 on 2024-08-04 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0013_question_title_alter_question_choicea_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女'), ('O', '其他')], max_length=1)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
