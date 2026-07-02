from django.shortcuts import render
from .models import InterviewSession


def history(request):

    sessions = InterviewSession.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "interviews/history.html",
        {"sessions": sessions}
    )