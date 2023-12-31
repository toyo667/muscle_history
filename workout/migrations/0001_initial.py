# Generated by Django 5.0 on 2023-12-31 02:41

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('feel', models.CharField(choices=[('best', '最高！'), ('better', 'いい感じ'), ('normal', '普通'), ('bad', '良くはない'), ('so_bad', '悪い'), ('cannot', '無理')], max_length=64, verbose_name='コンディション')),
                ('order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'ワークアウトセッションのコンディション',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TrainingArea',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('training_area', models.CharField(choices=[('arm', '腕'), ('back', '背中'), ('chest', '胸'), ('leg', '脚'), ('abdominal', '腹')], max_length=64, verbose_name='トレーニング部位')),
                ('order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'トレーニング部位',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='WorkoutFeeling',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('feel', models.CharField(choices=[('too_easy', '簡単すぎ'), ('easy', '簡単'), ('normal', '普通'), ('hard', 'きつい'), ('too_hard', 'キツすぎ'), ('cannot', '無理')], max_length=64, verbose_name='ワークアウト感想')),
                ('order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'ワークアウト時の感想',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='WorkoutItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('training_name', models.CharField(max_length=64, verbose_name='トレーニング種目')),
                ('category', models.ManyToManyField(to='workout.trainingarea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'トレーニング種目',
            },
        ),
        migrations.CreateModel(
            name='WorkoutSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='トレーニング開始日時')),
                ('finished_at', models.DateTimeField(null=True, verbose_name='トレーニング終了日時')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.condition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ワークアウトセッション',
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rep_count', models.IntegerField(verbose_name='レップ数')),
                ('set_count', models.IntegerField(verbose_name='セット数')),
                ('weight_kg', models.FloatField(verbose_name='重さ(kg)')),
                ('trained_at', models.DateTimeField(auto_now_add=True, verbose_name='トレーニング日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('feeling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.workoutfeeling')),
                ('training_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.workoutitem')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.workoutsession')),
            ],
            options={
                'verbose_name': 'ワークアウト',
                'ordering': ['-trained_at'],
            },
        ),
    ]
