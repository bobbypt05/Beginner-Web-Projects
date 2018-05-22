from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import SignUpModel

def login(request):
	return render(request,'loginpage.html')

def homepage(request):
	return render(request,'base.html')

def signup(request):
    if request.method == 'POST':
    	form = SignUpModel(request.POST)

    	if form.is_valid():
    		new_req = SignUpModel(username = request.POST['Fusername'], first_name = request.POST['Mfirst_name'], last_name = request.POST['Mlast_name'],
    		 email = request.POST['Memail'], password1 = request.POST['Mpassword1'], password2 = request.POST['Mpassword2'])

    		new_req.save()
    		return redirect('home')
    	else:
    		form = SignUpModel()

    	context = {'form': form}

    	return(request,'base.html',context)





#if request.method == "POST":
#		form = videoForm(request.POST)
#
#		if form.is_valid():
#			new_req = video(title=request.POST['videoName'],description=request.POST['videoDescription'])
#			new_req.save()
#			return redirect('index')
#	else:
#		form = videoForm()		
#
#	context = {'form' : form}
#
#	return render(request, 'videorequest.html',context)