from django.contrib.auth import get_user_model, login, logout,authenticate
from django.shortcuts import render, redirect

# Create your views here.

User = get_user_model()



def inscrire(request):
    if request.method == "POST":
        username = request.POST.get("username")
        # username = request.POST.get("first_name")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)

        login(request, user)
        return redirect('index')
    return render(request, 'compte/inscrire.html')

def connexion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate (username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'compte/connexion.html')

def deconnect(request):
        logout(request)
        return redirect('index')
