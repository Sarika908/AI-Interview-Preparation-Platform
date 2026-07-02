from django.shortcuts import render
from .ai import ask_interview_question, evaluate_answer
from interviews.models import InterviewSession
import re


def chatbot_home(request):

    category = request.GET.get("category", "Python")

    question = ask_interview_question(category)

    result = None

    if request.method == "POST":

        answer = request.POST.get("answer")

        result = evaluate_answer(question, answer)

        match = re.search(r"Score.*?(\d+)", result)

        score = int(match.group(1)) if match else 0

        if request.user.is_authenticated:

            InterviewSession.objects.create(
                user=request.user,
                category=category,
                question=question,
                answer=answer,
                feedback=result,
                score=score
            )

    return render(
        request,
        "chatbot/chatbot.html",
        {
            "question": question,
            "result": result,
            "category": category
        }
    )