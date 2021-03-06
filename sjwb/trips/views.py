from django.shortcuts import render, redirect, get_object_or_404
#建立首頁
from trips.models import Post, Like, Tag, Comment
from .forms import PostForm, post_comment_form
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

def home(request):
	post_list = Post.objects.all()
	return render(request, 'home.html', {
		'post_list': post_list,
		})

def area(request):
	url = request.build_absolute_uri()
	count = 0
	area_ID = ''
	d = False
	for s in url:
		if s == '=':
			d = True
		elif s.isdigit() and d == True:
			area_ID+=str(s)
		count+=1
	post_list = Post.objects.filter(area=area_ID).order_by('-created_date')
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
	area_title = AREA_CHOICES[int(area_ID)-1][1]
	return render(request, 'area.html', {'post_list': post_list,'area_title':area_title})

def attraction(request):
	post = Post.objects.filter(category=1).order_by('-created_date')
	user = request.user
	art_comment = []
	for po in post:
		if po.comment_set.all():
			art_comment.append(po.comment_set.all())
		else:
			art_comment.append([])
	post_list = zip(post, art_comment)
	comment_form = post_comment_form()
	return render(request, 'attraction.html', {
		'post_list': post_list,
		'user':user,
		})

def accomodation(request):
	post = Post.objects.filter(category=2).order_by('-created_date')
	user = request.user
	art_comment = []
	for po in post:
		if po.comment_set.all():
			art_comment.append(po.comment_set.all())
		else:
			art_comment.append([])
	post_list = zip(post, art_comment)
	comment_form = post_comment_form()
	return render(request, 'accomodation.html', {
		'post_list': post_list,
		'user':user,
		})


def restaurant(request):
	post = Post.objects.filter(category=3).order_by('-created_date')
	user = request.user
	art_comment = []
	for po in post:
		if po.comment_set.all():
			art_comment.append(po.comment_set.all())
		else:
			art_comment.append([])
	post_list = zip(post, art_comment)
	comment_form = post_comment_form()
	return render(request, 'restaurant.html', {
		'post_list': post_list,
		'user':user,
		})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post':post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form':form})

def post_delete(request, pk):
	post = Post.objects.get(pk=pk)
	post.delete()
	return redirect('/')

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST,request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_edit.html', {'form': form})

def login(request):
	if request.user.is_authenticated:
		return redirect('/home/')
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username = username, password = password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return redirect('/home/')
	else:
		return render(request, 'login.html', locals())

def logout(request):
	auth.logout(request)
	return redirect('/home/')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print("Errors", form.errors)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, 'registration/register.html', {'form':form})
	else:
		form = UserCreationForm()
		context = {'form':form}
		return render(request, 'registration/register.html', context)

def like_post(request):
	user = request.user
	if request.method == 'POST':
		pk = request.POST.get('post_pk')
		post = Post.objects.get(pk=pk)

		if user in post.liked.all():
			post.liked.remove(user)
		else:
			post.liked.add(user)

	return HttpResponse()

def post_serialized_view(request):
	data = list(Post.objects.values())
	return JsonResponse(data, safe=False)

def post_new_comment(request, post_id): 
	the_post = Post.objects.get(pk=post_id)
	if request.method =="POST":
		comment_form = post_comment_form(request.POST or None)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.comment_post = the_post
			new_comment.save()
			messages.success(request, "成功新增留言")
			return redirect('/attraction')
		else:
			return redirect('/attraction')