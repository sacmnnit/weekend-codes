from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings as django_settings
from django.http import HttpResponse
from django.template.context_processors import csrf  
# Create your views here.


def home(request):
	csrf_token = (csrf(request)['csrf_token'])
	print(csrf_token)
	return render(request,'WocLanding/home.html',{'csrf_token':csrf_token})

def test(request):
	return render(request,'test/test.html',{})


def contact(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	message = request.POST.get('message')
	to_user = [django_settings.EMAIL_HOST_USER]
	from_user = django_settings.EMAIL_HOST_USER
	subject = 'message from woc event'
	message = 'There is a message from '+name+ 'Email : '+email+' Message is : '+message
	send_mail(subject,message,from_user,to_user,fail_silently=False)

	return HttpResponse('success')
