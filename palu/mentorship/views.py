from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import MentorshipRequest, MentorSchedule
from users.models import User

def get_logged_in_user(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return None
    return User.objects.filter(id=user_id).first()

def indexMentorship(request):
    user = get_logged_in_user(request)

    if not user:
        return redirect("login")

    if user.role == "mahasiswa":
        mentors = User.objects.filter(role="alumni")

        mentorship_request = MentorshipRequest.objects.filter(
            mahasiswa=user
        ).exclude(status="finished").first()

        if request.method == "POST" and not mentorship_request:
            mentor_id = request.POST.get("mentor_id")
            tanggal = request.POST.get("tanggal")
            jam = request.POST.get("jam")
            topik = request.POST.get("topik")

            mentor = get_object_or_404(User, id=mentor_id, role="alumni")

            bentrok = MentorSchedule.objects.filter(
                mentor=mentor,
                tanggal=tanggal,
                jam=jam
            ).exists()

            if bentrok:
                messages.error(request, "Jadwal mentor tidak tersedia.")
                return redirect("mentorship")

            MentorshipRequest.objects.create(
                mentor=mentor,
                mahasiswa=user,
                tanggal=tanggal,
                jam=jam,
                topik=topik,
                status="waiting"
            )

            MentorSchedule.objects.create(
                mentor=mentor,
                tanggal=tanggal,
                jam=jam
            )

            messages.success(request, "Mentorship berhasil diajukan.")
            return redirect("mentorship")

        return render(request, "mentorship/mahasiswa/index.html", {
            "mentors": mentors,
            "request_data": mentorship_request
        })

    mentorship_requests = MentorshipRequest.objects.filter(
        mentor=user
    ).order_by("-created_at")

    return render(request, "mentorship/alumni/index.html", {
        "requests": mentorship_requests
    })


def approve_mentorship(request, request_id):
    user = get_logged_in_user(request)

    if not user or user.role != "alumni":
        return redirect("login")

    mentorship = get_object_or_404(
        MentorshipRequest,
        id=request_id,
        mentor=user
    )

    mentorship.status = "approved"
    mentorship.save()

    messages.success(request, "Mentorship disetujui.")
    return redirect("mentorship")


def reject_mentorship(request, request_id):
    user = get_logged_in_user(request)

    if not user or user.role != "alumni":
        return redirect("login")

    mentorship = get_object_or_404(
        MentorshipRequest,
        id=request_id,
        mentor=user
    )

    MentorSchedule.objects.filter(
        mentor=mentorship.mentor,
        tanggal=mentorship.tanggal,
        jam=mentorship.jam
    ).delete()

    mentorship.status = "rejected"
    mentorship.save()

    messages.info(request, "Mentorship ditolak.")
    return redirect("mentorship")

def finish_mentorship(request, request_id):
    user = get_logged_in_user(request)

    if not user or user.role != "alumni":
        return redirect("login")

    mentorship = get_object_or_404(
        MentorshipRequest,
        id=request_id,
        mentor=user,
        status="approved"
    )

    mentorship.status = "finished"
    mentorship.save()

    messages.success(request, "Sesi mentorship telah diselesaikan.")
    return redirect("mentorship")