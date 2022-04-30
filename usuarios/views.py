from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == 'POST':
        print('Usuário cadastrado!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def dashboard(request):
    pass

def logout(request):
    pass