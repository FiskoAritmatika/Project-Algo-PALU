from django.contrib import admin
from .models import Conversation, ChatMessage

# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user1', 'user2')
    search_fields = ('id',)

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'sender', 'message', 'created_at')
    search_fields = ('id',)