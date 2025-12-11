from django.db import models
from users.models import User

class Conversation(models.Model):
    # Bikin wadah chat
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conv_user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conv_user2")

    class Meta:
        # Gaboleh ada 2 conv yang sama antar user1 sama user2
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"{self.user1.nama} & {self.user2.nama}"
      
class ChatMessage(models.Model):
    # Setiap chat message harus terhubung ke satu conversation
    # Ini juga biar ChatMessage tau siapa yang lagi ngobrol
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=False, blank=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']