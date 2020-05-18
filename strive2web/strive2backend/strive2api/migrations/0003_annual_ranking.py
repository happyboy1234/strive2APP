# Generated by Django 3.0.4 on 2020-04-20 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strive2api', '0002_auto_20200417_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annual_ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年份')),
                ('s1_score', models.IntegerField(default=0, verbose_name='第一季度积分')),
                ('s2_score', models.IntegerField(default=0, verbose_name='第二季度积分')),
                ('s3_score', models.IntegerField(default=0, verbose_name='第三季度积分')),
                ('s4_score', models.IntegerField(default=0, verbose_name='第四季度积分')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annual_rankings', to='strive2api.Unit', verbose_name='年度排名')),
            ],
        ),
    ]
