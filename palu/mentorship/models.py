from django.db import models
from users.models import User

class MentorSchedule(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal = models.DateField()
    jam = models.TimeField()

    class Meta:
        unique_together = ('mentor', 'tanggal', 'jam')

    def _str_(self):
        return f"{self.mentor.email} - {self.tanggal} {self.jam}"

class MentorshipRequest(models.Model):
    STATUS_CHOICES = [
        ("waiting", "Waiting"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("finished", "Finished"),
    ]
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentor_requests")
    mahasiswa = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mahasiswa_requests")
    tanggal = models.DateField()
    jam = models.TimeField()
    topik = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="waiting")
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.mahasiswa.email} → {self.mentor.email} ({self.status})"