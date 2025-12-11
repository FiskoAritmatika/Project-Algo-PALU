from .models import Conversation

def get_or_create_conversation(user1, user2):
    # Ini biar urutannya sama terus = u1, u2 berdasarkan id
    if user1.id < user2.id:
        u1, u2 = user1, user2
    else:
        u1, u2 = user2, user1

    # Cari wadah, kalo ada ambil, kalo belom bikin
    conv, created = Conversation.objects.get_or_create(
        # Pengurutan yang diatas tadi dimasukin ke parameter
        user1=u1,
        user2=u2
    )
    return conv