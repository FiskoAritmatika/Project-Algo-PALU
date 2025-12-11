from django.db import models
from django.shortcuts import render, redirect
from users.decorators import user_login_required
from users.models import User
from .models import ChatMessage, Conversation
from .utils import get_or_create_conversation

@user_login_required
def private_chat(request, user_id):
    current_user = User.objects.get(id=request.session["user_id"])
    other_user = User.objects.get(id=user_id)

    conversation = get_or_create_conversation(current_user, other_user)

    if request.method == "POST":
        message = request.POST.get("message")
        if message.strip():
            ChatMessage.objects.create(
                conversation=conversation,
                sender=current_user,
                message=message
            )
        return redirect("private_chat", user_id=other_user.id)

    messages_list = ChatMessage.objects.filter(conversation=conversation)

    conversations = Conversation.objects.filter(
        models.Q(user1=current_user) | models.Q(user2=current_user)
    ).annotate(
        last_message_time=models.Max("chatmessage__created_at")
    ).order_by("-last_message_time")

    chat_partners = []

    for conv in conversations:
        if conv.user1 == current_user:
            other = conv.user2
        else:
            other = conv.user1

        last_msg = ChatMessage.objects.filter(conversation=conv).order_by("-created_at").first()

        chat_partners.append({
            "user": other,
            "last_message": last_msg.message if last_msg else "",
            "last_time": last_msg.created_at if last_msg else None,
        })

    return render(request, "chat/index.html", {
        "messages": messages_list,
        "other_user": other_user,
        "current_user": current_user,
        "chat_partners": chat_partners,
    })

    
@user_login_required
def inbox(request):
    current_user = User.objects.get(id=request.session["user_id"])

    # Ambil semua conversation yang melibatkan user saat ini
    conversations = Conversation.objects.filter(
        models.Q(user1=current_user) | models.Q(user2=current_user)
    ).annotate(
        last_message_time=models.Max("chatmessage__created_at")
    ).order_by("-last_message_time")

    chat_partners = []

    for conv in conversations:
        # Tentukan siapa lawan bicara
        if conv.user1 == current_user:
            other = conv.user2
        else:
            other = conv.user1

        # Ambil pesan terakhir
        last_msg = ChatMessage.objects.filter(conversation=conv).order_by("-created_at").first()

        chat_partners.append({
            "user": other,
            "last_message": last_msg.message if last_msg else "",
            "last_time": last_msg.created_at if last_msg else None,
        })

    return render(request, "chat/inbox.html", {
        "chat_partners": chat_partners
    })
