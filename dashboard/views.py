from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from interviews.models import InterviewSession
from django.db.models import Avg


@login_required
def dashboard(request):

    sessions = InterviewSession.objects.filter(user=request.user)

    total_interviews = sessions.count()

    average_score = sessions.aggregate(
        Avg("score")
    )["score__avg"]

    if average_score is None:
        average_score = 0

    recent_sessions = sessions.order_by("-created_at")[:5]

    category_scores = {}

    for session in sessions:
        category_scores.setdefault(session.category, []).append(session.score)

    best_category = "N/A"
    highest_avg = 0

    for category, scores in category_scores.items():
        avg = sum(scores) / len(scores)
        if avg > highest_avg:
            highest_avg = avg
            best_category = category

    context = {
        "total_interviews": total_interviews,
        "average_score": round(average_score, 2),
        "best_category": best_category,
        "recent_sessions": recent_sessions,
    }

    return render(request, "dashboard/dashboard.html", context)