from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class QuoteType(models.Model):
    """Quote types"""

    name = models.CharField(max_length=100, unique=True)  # Ej: "Genérico"
    slug = models.SlugField(unique=True)  # Ej: "generic", "programming"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class MotivationalQuote(models.Model):
    """Motivational quotes"""

    text = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    quote_type = models.ForeignKey(
        QuoteType, on_delete=models.CASCADE, related_name="motivational_quotes"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text[:50]}... ({self.quote_type})"


class EmergencyQuiz(models.Model):
    """Parent quiz information"""

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        QuoteType, on_delete=models.CASCADE, related_name="quiz_categories"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    """Question for the quiz"""

    quiz = models.ForeignKey(
        EmergencyQuiz, on_delete=models.CASCADE, related_name="questions"
    )
    question_text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quiz.title} - {self.question_text[:50]}..."


class QuizAnswer(models.Model):
    """Related awnser for the quiz"""

    question = models.ForeignKey(
        QuizQuestion, on_delete=models.CASCADE, related_name="answers"
    )
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.question_text[:30]} - {self.answer_text}"
