from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import FileUpload
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
import os, mimetypes

def home(request):
	allUsers = User.objects.all()
	#print(request.user.id)
	
	count = 0
	if request.user.id:

		media_root = settings.MEDIA_ROOT
		folder_path = os.path.join(media_root, request.user.username)
		for filename in os.listdir(folder_path):
			filePath = os.path.join(folder_path, filename)
			count = wordCount(filePath)
			#downloadFile = downloadF(filePath)
			#print(filePath)

	return render(request, 'assignment1/home.html', {'allUsers':allUsers, 'wordCount':count})

def about(request):
	return render(request, 'assignment1/about.html')

def aboutContent(request):
	return render(request, 'assignment1/aboutContent.html')

def education(request):
	return render(request, 'assignment1/education.html')

def workExp(request):
	return render(request, 'assignment1/workExp.html')

def skills(request):
	return render(request, 'assignment1/skills.html')

def achievements(request):
	return render(request, 'assignment1/achievements.html')

def wordCount(filePath):
	count = 0
	with open(filePath, 'r') as f:
		for line in f.readlines():
			#print(type(str(line))
			line = str(line)
			wordCount = line.split(' ')
			count+=len(wordCount)

	return count

def downloadF(request):

	if request.user.id:

		media_root = settings.MEDIA_ROOT
		folder_path = os.path.join(media_root, request.user.username)
		for filename in os.listdir(folder_path):
			filePath = os.path.join(folder_path, filename)

		with open(filePath, 'rb') as fh:
			mime_type, _ = mimetypes.guess_type(filePath)
			response = HttpResponse(fh.read(), content_type=mime_type)
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filePath)
			return response

def register(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST, request.FILES)
		if form.is_valid():
			
			file = request.FILES['document']
			username = request.POST['username']

			if file.name.endswith('.txt'):
				fs = FileSystemStorage()
				filename = fs.save(username + '/' + file.name, file)
				file_url = fs.url(filename)

			else:
				messages.error(request, "File must be .txt")
				form = UserRegisterForm()
				return render(request, 'assignment1/registration.html', {'form':form})
			

			#doc = FileUpload(file=file, uname=username)
			#doc.save()

			#doc = FileUpload.objects.create(file = newPath)
			#doc.save()

			#wordCnt = wordCount(request.FILES['document'])
			#messages.success(request, f('WordCount in Uploaded file is: {wordCount}'))
			#form.wordCount = wordCnt
			form.save()
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, 'assignment1/registration.html', {'form':form})

def profile(request):
	return render(request, 'assignment1/profile.html')

