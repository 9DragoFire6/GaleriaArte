"""
Script para crear usuarios de prueba para el sistema de autenticación
Ejecutar con: Get-Content crear_usuarios_prueba.py | python manage.py shell
"""

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from usuarios.models import PerfilUsuario
from album.models import ObraArte

# Eliminar usuarios de prueba si ya existen
User.objects.filter(username__in=['admin_galeria', 'espectador_galeria']).delete()

# Crear grupo AdministradorArte con permisos específicos
grupo_admin, created = Group.objects.get_or_create(name='AdministradorArte')

if created or not grupo_admin.permissions.exists():
    # Obtener el ContentType de ObraArte
    content_type = ContentType.objects.get_for_model(ObraArte)
    
    # Asignar permisos de añadir, eliminar, modificar y ver obras
    permisos = Permission.objects.filter(
        content_type=content_type,
        codename__in=['add_obraarte', 'delete_obraarte', 'change_obraarte', 'view_obraarte']
    )
    grupo_admin.permissions.set(permisos)

# Crear grupo Espectadores
grupo_espectador, _ = Group.objects.get_or_create(name='Espectadores')

# Crear usuario Administrador
admin_user = User.objects.create_user(
    username='admin_galeria',
    email='admin@galeria.com',
    password='Admin2024!',
    first_name='Carlos',
    last_name='Administrador',
    is_staff=True,
    is_active=True
)
PerfilUsuario.objects.create(user=admin_user, tipo_usuario='administrador')
admin_user.groups.add(grupo_admin)

# Crear usuario Espectador
espectador_user = User.objects.create_user(
    username='espectador_galeria',
    email='espectador@galeria.com',
    password='Espectador2024!',
    first_name='María',
    last_name='Espectadora',
    is_active=True
)
PerfilUsuario.objects.create(user=espectador_user, tipo_usuario='espectador')
espectador_user.groups.add(grupo_espectador)

print("=" * 60)
print("USUARIOS DE PRUEBA CREADOS EXITOSAMENTE")
print("=" * 60)
print("\n📋 CREDENCIALES DE ACCESO:\n")
print("👨‍💼 ADMINISTRADOR:")
print("   Usuario:    admin_galeria")
print("   Contraseña: Admin2024!")
print("   Email:      admin@galeria.com")
print("   Tipo:       Staff (NO Superusuario)")
print("   Grupo:      AdministradorArte")
print("   Permisos:   Añadir, Eliminar, Modificar y Ver Obras")
print("   Acceso:     Panel de Django Admin (/admin/)")
print("\n👁️  ESPECTADOR:")
print("   Usuario:    espectador_galeria")
print("   Contraseña: Espectador2024!")
print("   Email:      espectador@galeria.com")
print("   Tipo:       Usuario estándar")
print("   Grupo:      Espectadores")
print("   Permisos:   Solo visualización")
print("   Acceso:     Página de inicio (/)")
print("\n" + "=" * 60)
print("✅ Los usuarios están listos para usar")
print("=" * 60)
