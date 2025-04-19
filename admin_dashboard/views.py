from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MotivationalQuote, QuizQuestion


def admin_dashboard(request):
    # if not request.user.is_authenticated or not request.user.is_owner:
    #     return redirect('home')  # o mostrar error 403

    quotes = MotivationalQuote.objects.all()
    quizzes = QuizQuestion.objects.all()

    return render(request, './admin_dashboard.html', {
        'quotes': quotes,
        'quizzes': quizzes,
    })
