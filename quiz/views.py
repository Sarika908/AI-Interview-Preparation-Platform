from django.shortcuts import render
from .models import Question


def quiz_home(request):

    questions = Question.objects.all()

    score = None

    if request.method == "POST":

        score = 0

        for q in questions:

            answer = request.POST.get(str(q.id))

            if answer == q.correct_answer:
                score += 1

    return render(
        request,
        "quiz/quiz.html",
        {
            "questions": questions,
            "score": score,
        },
    )