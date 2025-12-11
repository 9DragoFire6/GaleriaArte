from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario

users = User.objects.all()
print(f'Total users: {users.count()}')
for u in users:
    try:
        perfil = u.perfil
        print(f'User: {u.username}, Email: {u.email}, Staff: {u.is_staff}, Superuser: {u.is_superuser}, Tipo: {perfil.tipo_usuario}')
    except PerfilUsuario.DoesNotExist:
        print(f'User: {u.username}, Email: {u.email}, Staff: {u.is_staff}, Superuser: {u.is_superuser}, Tipo: NO PROFILE')
