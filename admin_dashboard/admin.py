from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import (
    QuoteType,
    MotivationalQuote,
    EmergencyQuiz,
    QuizQuestion,
    QuizAnswer
)

@admin.register(QuoteType)
class QuoteTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MotivationalQuote)
class MotivationalQuoteAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ('short_text', 'author', 'quote_type', 'is_active', 'created_at')
    list_filter = ('quote_type', 'is_active')
    search_fields = ('text', 'author')

    def short_text(self, obj):
        return obj.text[:50] + '...'


@admin.register(EmergencyQuiz)
class EmergencyQuizAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('title', 'category', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('title',)


@admin.register(QuizQuestion)
class QuizQuestionAdmin(SummernoteModelAdmin):
    summernote_fields = ('question_text',)
    list_display = ('short_question', 'quiz', 'order')
    search_fields = ('question_text',)

    def short_question(self, obj):
        return obj.question_text[:50] + '...'


@admin.register(QuizAnswer)
class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('answer_text',)
