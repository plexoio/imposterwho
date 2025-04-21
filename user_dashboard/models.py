from django.db import models
from django.conf import settings
from admin_dashboard.models import MotivationalQuote, EmergencyQuiz, QuizQuestion, QuizAnswer 


class UserQuizProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(EmergencyQuiz, on_delete=models.CASCADE)
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(QuizAnswer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user.username} - {self.quiz.title} - Question {self.question.order}"

class UserFavoriteQuote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quote = models.ForeignKey(MotivationalQuote, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user.username} - Favorite Quote: {self.quote.text[:50]}..."
