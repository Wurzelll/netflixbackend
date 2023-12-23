from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    if request.user.is_authenticated:
        return redirect('profile_page'),
    
    return render(request,'index.html', {}) 