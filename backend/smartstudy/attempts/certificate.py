from reportlab.pdfgen import canvas
from django.http import HttpResponse


def generate_certificate(user, quiz, score):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 750, "Certificate of Completion")
    p.drawString(100, 700, f"This certifies that {user.username}")
    p.drawString(100, 650, f"completed the quiz '{quiz.title}'")
    p.drawString(100, 600, f"Score: {score}")

    p.showPage()
    p.save()

    return response