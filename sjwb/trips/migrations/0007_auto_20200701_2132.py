# Generated by Django 3.0.7 on 2020-07-01 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_auto_20200701_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='area',
            field=models.IntegerField(choices=[(1, '基隆市'), (2, '台北市'), (3, '新北市'), (4, '桃園市'), (5, '新竹縣'), (6, '新竹市'), (7, '苗栗縣'), (8, '南投縣'), (9, '台中市'), (10, '彰化縣'), (11, '雲林縣'), (12, '嘉義縣'), (13, '嘉義市'), (14, '台南市'), (15, '高雄市'), (16, '屏東縣'), (17, '台東縣'), (18, '宜蘭縣'), (19, '花蓮縣'), (20, '澎湖縣'), (21, '金門縣'), (22, '連江縣')], default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.IntegerField(choices=[(1, '景點'), (2, '住宿'), (3, '餐廳')], default=1, max_length=2),
        ),
    ]
