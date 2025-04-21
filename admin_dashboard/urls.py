from django.urls import path
from . import views

urlpatterns = [
    # Dashboard principal
    path("dashboard/", views.admin_dashboard, name="manager"),
    # URLs para categorías (QuoteType)
    path("categories/add/", views.add_category, name="add_category"),
    path(
        "categories/edit/<int:category_id>/", views.edit_category, name="edit_category"
    ),
    # path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    # URLs para citas motivacionales (MotivationalQuote)
    path("quotes/add/", views.add_quote, name="add_quote"),
    path("quotes/edit/<int:quote_id>/", views.edit_quote, name="edit_quote"),
    # path('quotes/delete/<int:quote_id>/', views.delete_quote, name='delete_quote'),
    # URLs para quizzes de emergencia (EmergencyQuiz)
    path("quizzes/add/", views.add_quiz, name="add_quiz"),
    path("quizzes/edit/<int:quiz_id>/", views.edit_quiz, name="edit_quiz"),
    # path('quizzes/delete/<int:quiz_id>/', views.delete_quiz, name='delete_quiz'),
    # URLs para gestión de preguntas del quiz (QuizQuestion)
    path(
        "quizzes/<int:quiz_id>/questions/",
        views.manage_quiz_questions,
        name="manage_quiz_questions",
    ),
    path(
        "questions/delete/<int:question_id>/",
        views.delete_question,
        name="delete_question",
    ),
    # URLs para gestión de respuestas del quiz (QuizAnswer)
    path(
        "questions/<int:question_id>/answers/",
        views.manage_question_answers,
        name="manage_question_answers",
    ),
    path("answers/delete/<int:answer_id>/", views.delete_answer, name="delete_answer"),
    # urls.py
    path(
        "dashboard/delete/<str:type>/<int:pk>/",
        views.delete_object,
        name="delete_object",
    ),
]
