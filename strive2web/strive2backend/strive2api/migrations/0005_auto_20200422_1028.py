# Generated by Django 3.0.4 on 2020-04-22 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strive2api', '0004_auto_20200422_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='scorer_cate',
        ),
        migrations.AddField(
            model_name='unit',
            name='scorer_major_cate',
            field=models.CharField(choices=[('基层', '基层'), ('机关', '机关'), ('领导', '领导')], default='基层', max_length=20, verbose_name='评分身份'),
            preserve_default=False,
        ),
    ]
