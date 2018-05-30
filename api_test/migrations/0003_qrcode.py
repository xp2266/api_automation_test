# Generated by Django 2.0.2 on 2018-05-30 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0002_auto_20180529_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.CharField(blank=True, max_length=1024, null=True, verbose_name='图片地址')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Robot', verbose_name='机器人')),
            ],
            options={
                'verbose_name': '二维码管理',
                'verbose_name_plural': '二维码管理',
            },
        ),
    ]