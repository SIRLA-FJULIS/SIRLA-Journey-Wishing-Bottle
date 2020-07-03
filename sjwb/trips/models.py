from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
	title = models.CharField(max_length=200, help_text='<font color="red">*必填</font>')
	text = models.TextField(help_text='<font color="red">*必填</font>')

	AREA_CHOICES=((1,'基隆市'),
		(2,'台北市'),
		(3,'新北市'),
		(4,'桃園市'),
		(5,'新竹縣'),
		(6, '新竹市'),
		(7, '苗栗縣'),
		(8, '南投縣'),
		(9, '台中市'),
		(10, '彰化縣'),
		(11, '雲林縣'),
		(12, '嘉義縣'),
		(13, '嘉義市'),
		(14, '台南市'),
		(15, '高雄市'),
		(16, '屏東縣'),
		(17, '台東縣'),
		(18, '宜蘭縣'),
		(19, '花蓮縣'),
		(20, '澎湖縣'),	
		(21, '金門縣'),
		(22, '連江縣'),)
	area = models.IntegerField(max_length=100, choices=AREA_CHOICES, default=1)

	CHOICES=((1,'景點'),(2,'住宿'),(3,'餐廳'))
	category = models.IntegerField(max_length=2, choices=CHOICES, default=1)
	
	location = models.CharField(max_length=100, help_text='<font color="red">*必填</font>')
	phone_number = models.CharField(max_length=12,blank=True, null=True, help_text='類型是住宿或餐廳才要填')
	tag = models.CharField(max_length=10,blank=True, null=True)
	photo = models.ImageField(upload_to='img/',blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True) 
	liked = models.ManyToManyField(User,default=None,blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	@property
	def num_likes(self):
		return self.liked.all().count()
	

	def __str__(self):
		return self.title
'''
author 			作者
title			標題
text 			介紹景點的內容
area 			地區選擇
category		類別
location 		地點
phone_number 	電話
tag				標籤
photo			照片(格式是圖片網址)
created_date
published_date
'''
LIKE_CHOICES=(
	('Like','Like'),
	('Unlike','Unlike'),
	)


class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	value = models.CharField(choices=LIKE_CHOICES,default='Like', max_length=10)

	def __str__(self):
		return self.post