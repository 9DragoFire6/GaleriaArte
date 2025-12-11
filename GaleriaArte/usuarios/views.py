from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import RegistroForm
from .models import PerfilUsuario
from album.models import ObraArte

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            tipo_usuario = form.cleaned_data.get('tipo_usuario')
            
            # Crear perfil de usuario
            PerfilUsuario.objects.create(user=user, tipo_usuario=tipo_usuario)
            
            # Asignar permisos según el tipo de usuario
            if tipo_usuario == 'administrador':
                user.is_staff = True
                user.is_active = True
                user.save()
                
                # Crear grupo AdministradorArte con permisos específicos
                grupo_admin, created = Group.objects.get_or_create(name='AdministradorArte')
                
                if created:
                    # Obtener el ContentType de ObraArte
                    content_type = ContentType.objects.get_for_model(ObraArte)
                    
                    # Asignar permisos de añadir, eliminar, modificar y ver obras
                    permisos = Permission.objects.filter(
                        content_type=content_type,
                        codename__in=['add_obraarte', 'delete_obraarte', 'change_obraarte', 'view_obraarte']
                    )
                    grupo_admin.permissions.set(permisos)
                
                user.groups.add(grupo_admin)
            else:
                grupo_espectador, created = Group.objects.get_or_create(name='Espectadores')
                user.groups.add(grupo_espectador)
            
            messages.success(request, f'Cuenta creada exitosamente para {user.username}')
            return redirect('login')
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

@ensure_csrf_cookie
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            
            # Redirigir según el tipo de usuario
            try:
                perfil = user.perfil
                if perfil.tipo_usuario == 'administrador':
                    return redirect('/admin/')
                else:
                    return redirect('index')  # Espectadores van al inicio
            except PerfilUsuario.DoesNotExist:
                return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            form = AuthenticationForm()
            return render(request, 'usuarios/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente')
    return redirect('index')
