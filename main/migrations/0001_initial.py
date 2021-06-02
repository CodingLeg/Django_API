# Generated by Django 3.2 on 2021-05-22 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpName', models.CharField(default='Java', max_length=100, unique=True)),
                ('subscribe', models.CharField(default='okay', max_length=100)),
                ('role', models.CharField(default='user', max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='manager', max_length=100)),
                ('group', models.CharField(default='Java', max_length=100)),
                ('messages', models.CharField(default='Welcome', max_length=100)),
                ('grp_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.group')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='user', max_length=100)),
                ('gpName', models.CharField(default='Java', max_length=100)),
                ('grp_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.group')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
