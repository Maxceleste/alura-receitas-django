from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')

        if senha != senha2:
            print('As senhas estão diferentes.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('Usuário já existe')
            return redirect('cadastro')
        
        user = User.objects.create_user(username = nome, email = email, password = senha)
        user.save()

        print('Usuário cadastrado')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == '' or senha == '':
            print('Prencha todos os campos.')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat = True)[0]
            user = auth.authenticate(request, username = nome, password = senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso!')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

def cria_receita(request):

    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']    

        

        return redirect('dashboard')
    
    else:
        return render(request, 'usuarios/cria_receita.html')

