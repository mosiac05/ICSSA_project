# Generated by Django 3.0.7 on 2020-06-15 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ICSSA_app', '0003_auto_20200615_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExecutivePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ExecutiveTenure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.CreateModel(
            name='PollQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('running_hours', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('old', 'Old')], default='inactive', max_length=15)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ICSSA_app.Level')),
            ],
        ),
        migrations.CreateModel(
            name='PollParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ICSSA_app.PollChoice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ICSSA_app.PollQuestion')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ICSSA_app.Student')),
            ],
        ),
        migrations.AddField(
            model_name='pollchoice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ICSSA_app.PollQuestion'),
        ),
        migrations.CreateModel(
            name='ExecutiveMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ICSSA_app.Student')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ICSSA_app.ExecutivePost')),
                ('tenure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ICSSA_app.ExecutiveTenure')),
            ],
        ),
    ]
