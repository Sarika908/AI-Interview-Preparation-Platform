from django.shortcuts import render, redirect
from .forms import ResumeForm
from .parser import read_pdf, read_docx
from .ai import analyze_resume


def upload_resume(request):

    if not request.user.is_authenticated:
        return redirect("login")

    result = None

    if request.method == "POST":

        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():

            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            path = resume.resume.path

            if path.endswith(".pdf"):
                text = read_pdf(path)

            elif path.endswith(".docx"):
                text = read_docx(path)

            else:
                text = ""

            result = analyze_resume(text)

            return render(
                request,
                "resume/result.html",
                {"result": result}
            )

    else:
        form = ResumeForm()

    return render(
        request,
        "resume/upload.html",
        {"form": form}
    )