from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Users must have an email'))

        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)

        return user
    
class User(AbstractBaseUser):
    """
    User model
    """
    PERSON_TYPE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    person_type = models.CharField(max_length=2, null=True, blank=True, choices=PERSON_TYPE_CHOICES)

    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    document = models.CharField(max_length=14, null=True, blank=True)  # CPF: 11 caracteres, CNPJ: 14 caracteres
    document_number = models.CharField(max_length=20, null=True, blank=True)  # Número Documento
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Valor da dívida ativa
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Valor do empréstimo solicitado
    
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_verified(self):
        return self.is_active

    @property
    def is_staff(self):
        return self.is_admin
    

