from django.db import models

class User(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def _str_(self):
        return self.nama


#from django.db import models
#from django.contrib.auth.hashers import make_password, check_password
#from django.contrib.auth.models import AbstractUser
#from django.db import models

# Nama class ini HARUS sama dengan yang kamu tulis di AUTH_USER_MODEL
#class User(models.Model):
#    ROLE_CHOICES = (
#        ('mahasiswa', 'Mahasiswa'),
# #       ('alumni', 'Alumni'),
#    )
#
#    nama = models.CharField(max_length=150)
#    nim = models.CharField(max_length=20, unique=True)
#    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='mahasiswa')
#    email = models.EmailField(unique=True)
#    password = models.CharField(max_length=255)  # akan menyimpan hash
#
 #   def set_password(self, raw_password):
#        self.password = make_password(raw_password)
#        self.save()

 #   def check_password(self, raw_password):
#        return check_password(raw_password, self.password)

 #   def str(self):
#        return f"{self.nama} ({self.email})"