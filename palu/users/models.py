from django.db import models

class User(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20, unique=True)
    
    ROLE_CHOICES = [
        ("mahasiswa", "Mahasiswa"),
        ("alumni", "Alumni"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="mahasiswa"
    )

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nama