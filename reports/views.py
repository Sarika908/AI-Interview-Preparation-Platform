from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def interview_report(request):

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="Interview_Report.pdf"'

    doc = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Interview Preparation Platform</b>", styles["Title"]))
    story.append(Paragraph("Interview Report", styles["Heading2"]))
    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("Candidate: {}".format(request.user.username), styles["BodyText"]))
    story.append(Paragraph("Average Score: 8.5 / 10", styles["BodyText"]))
    story.append(Paragraph("Best Category: Python", styles["BodyText"]))
    story.append(Paragraph("Completed Interviews: 12", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(
        "Congratulations! Continue practicing coding and technical interviews to improve your performance.",
        styles["BodyText"]
    ))

    doc.build(story)

    return response