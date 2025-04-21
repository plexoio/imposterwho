from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from admin_dashboard.models import MotivationalQuote, EmergencyQuiz
from .models import UserQuizProgress, UserFavoriteQuote

@login_required
def user_dashboard(request):
    quotes = MotivationalQuote.objects.filter(is_active=True)
    favorite_quotes = UserFavoriteQuote.objects.filter(user=request.user)
    user_quiz_progress = UserQuizProgress.objects.filter(user=request.user)
    completed_quizzes = EmergencyQuiz.objects.filter(id__in=user_quiz_progress.values('quiz'))

    quiz_scores = {}
    for quiz in completed_quizzes:
        total_questions = quiz.questions.count()
        correct_answers = user_quiz_progress.filter(quiz=quiz, is_correct=True).count()
        quiz_scores[quiz] = (correct_answers, total_questions)

    context = {
        'quotes': quotes,  
        'favorite_quotes': favorite_quotes,  
        'completed_quizzes': completed_quizzes, 
        'quiz_scores': quiz_scores,  
    }

    return render(request, 'user_dashboard.html', context)


@login_required
def remove_from_favorites(request, favorite_id):
    favorite = UserFavoriteQuote.objects.get(id=favorite_id, user=request.user)
    favorite.delete()
    return redirect('user_dashboard')