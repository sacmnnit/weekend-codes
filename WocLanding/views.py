from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request,'WocLanding/index.html',{})

def test(request):
	return render(request,'test/test.html',{})