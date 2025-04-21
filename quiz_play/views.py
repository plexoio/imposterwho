from django.shortcuts import render, get_object_or_404, redirect
from admin_dashboard.models import EmergencyQuiz
from django.contrib.auth.decorators import login_required

@login_required
def quiz_list(request):
    quizzes = EmergencyQuiz.objects.filter(is_active=True)
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

@login_required
def start_quiz(request, quiz_id):
    # Más adelante implementarás esta vista con lógica de preguntas
    quiz = get_object_or_404(EmergencyQuiz, id=quiz_id)
    return redirect('quiz_list')  # Por ahora redirecciona de vuelta
