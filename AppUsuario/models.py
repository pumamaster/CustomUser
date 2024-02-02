from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):

    def create_user(self,email,username,nombres,password=None):
        if not email:
            raise ValueError('Se necesita un correo electrónico')
        
        user=self.model(
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,email,nombres,password):
        user=self.create_user(
            email,
            username=username,
            nombres=nombres,
            password=password
        )

        user.usuario_administrador=True
        user.save()
        return user

class Usuario(AbstractBaseUser):

    username=models.CharField('Nombre de usuario', unique=True, max_length=100)
    email=models.EmailField('Correo electrónico', unique=True, max_length=100)
    nombres=models.CharField('Nombres', blank=True, null=True, max_length=100)
    apellidos=models.CharField('Apellidos', blank=True, null=True, max_length=100)
    imagen=models.ImageField('Imagen de perfil', upload_to='perfil/', blank=True, null=True)
    usuario_activo=models.BooleanField(default=True)
    usuario_administrador=models.BooleanField(default=False)
    objects=UsuarioManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email', 'nombres']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador