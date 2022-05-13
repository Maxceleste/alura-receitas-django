from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receitas

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')

        if senhas_diferentes(senha, senha2):
            messages.error(request, 'As senhas estão diferentes.')
            return redirect('cadastro')

        if email_ja_cadastrado(email):
            messages.error(request, 'Usuário já existe')
            return redirect('cadastro')

        if usuario_ja_cadastrado(nome):
            messages.error(request, 'Usuário já existe')
            return redirect('cadastro')
        
        user = User.objects.create_user(username = nome, email = email, password = senha)
        user.save()

        messages.success(request, 'Usuário cadastrado')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Prencha todos os campos.')
            return redirect('login')

        if email_ja_cadastrado(email):
            nome = User.objects.filter(email=email).values_list('username', flat = True)[0]
            user = auth.authenticate(request, username = nome, password = senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Informações inválidas')
                return redirect('login')
        else:
            messages.error(request, 'E-mail não cadastrado')
            return redirect('login')

    return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        lista_receitas = Receitas.objects.order_by('-date_receita').filter(pessoa=id)

        dados = {
            'receitas' : lista_receitas,
        }

        return render(request, 'usuarios/dashboard.html', dados)
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

        user = get_object_or_404(User, pk = request.user.id)

        receita = Receitas.objects.create(pessoa=user, nome_receita=nome_receita,
        ingredientes=ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo,
        rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)

        receita.save()


        return redirect('dashboard')
    
    else:
        return render(request, 'usuarios/cria_receita.html')


def campo_vazio(campo):
    '''
    Função que retorna True ou False se o campo como argumento estiver vazio.
    '''
    return not campo.strip()

def senhas_diferentes(senha1, senha2):
    '''
    Função que retorna True ou False se as duas senhas são diferentes.
    '''
    return senha1 != senha2

def email_ja_cadastrado(email):
    '''
    Função que retorna True ou False se o email já está cadastrado no banco.
    '''
    return User.objects.filter(email=email).exists()

def usuario_ja_cadastrado(user):
    '''
    Função que retorna True ou Flase se o usuário já estiver cadastrado no banco
    '''
    return User.objects.filter(username=user).exists()
    