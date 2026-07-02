import time

from django.shortcuts import render

from .forms import CodeForm


QUESTION = """
Write a Python function to find the factorial of a number.
"""


def coding_test(request):

    result = ""

    runtime = 0

    if request.method == "POST":

        form = CodeForm(request.POST)

        if form.is_valid():

            code = form.cleaned_data["code"]

            start = time.time()

            try:

                exec(code)

                result = "Program Executed Successfully"

            except Exception as e:

                result = str(e)

            runtime = round(time.time() - start, 5)

    else:

        form = CodeForm()

    return render(
        request,
        "coding/editor.html",
        {
            "form": form,
            "question": QUESTION,
            "result": result,
            "runtime": runtime
        }
    )