from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import (
    MotivationalQuote, EmergencyQuiz, QuoteType, 
    QuizQuestion, QuizAnswer
)
from .forms import (
    CategoryForm, MotivationalQuoteForm, EmergencyQuizForm,
    QuizQuestionForm, QuizAnswerForm, QuizAnswerInlineFormSet
)

@login_required
def admin_dashboard(request):
    # Obtener todos los datos para mostrar en el dashboard
    quotes = MotivationalQuote.objects.all().select_related('quote_type')
    quizzes = EmergencyQuiz.objects.all().select_related('category')
    quote_types = QuoteType.objects.all()
    
    # Instanciar formularios vacíos para agregar nuevos elementos
    category_form = CategoryForm()
    quote_form = MotivationalQuoteForm()
    quiz_form = EmergencyQuizForm()
    
    return render(request, 'admin_dashboard.html', {
        'motivational_quotes': quotes,
        'quizzes': quizzes,
        'quote_types': quote_types,
        'category_form': category_form,
        'quote_form': quote_form,
        'quiz_form': quiz_form,
    })

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
        else:
            messages.error(request, 'Error adding category.')
    return redirect('manager')

@login_required
def edit_category(request, category_id):
    category = get_object_or_404(QuoteType, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
        else:
            messages.error(request, 'Error updating category.')
    return redirect('manager')

# @login_required
# def delete_category(request, category_id):
#     if request.method == 'POST':
#         category = get_object_or_404(QuoteType, id=category_id)
#         category.delete()
#         messages.success(request, 'Categoría eliminada exitosamente.')
#     return redirect('manager')

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = MotivationalQuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Motivational quote successfully added.')
        else:
            messages.error(request, 'Error adding motivational quote.')
    return redirect('manager')

@login_required
def edit_quote(request, quote_id):
    quote = get_object_or_404(MotivationalQuote, id=quote_id)
    if request.method == 'POST':
        form = MotivationalQuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            messages.success(request, 'Motivational quote successfully updated.')
        else:
            messages.error(request, 'Error updating motivational quote.')
    return redirect('manager')

# @login_required
# def delete_quote(request, quote_id):
#     if request.method == 'POST':
#         quote = get_object_or_404(MotivationalQuote, id=quote_id)
#         quote.delete()
#         messages.success(request, 'Cita motivacional eliminada exitosamente.')
#     return redirect('manager')

@login_required
def add_quiz(request):
    if request.method == 'POST':
        form = EmergencyQuizForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Emergency quiz added successfully.')
        else:
            messages.error(request, 'Error adding emergency quiz.')
    return redirect('manager')

@login_required
def edit_quiz(request, quiz_id):
    quiz = get_object_or_404(EmergencyQuiz, id=quiz_id)
    if request.method == 'POST':
        form = EmergencyQuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            messages.success(request, 'Emergency quiz successfully updated.')
        else:
            messages.error(request, 'Error updating emergency quiz.')
    return redirect('manager')

# @login_required
# def delete_quiz(request, quiz_id):
#     if request.method == 'POST':
#         quiz = get_object_or_404(EmergencyQuiz, id=quiz_id)
#         quiz.delete()
#         messages.success(request, 'Quiz de emergencia eliminado exitosamente.')
#     return redirect('manager')

@login_required
def manage_quiz_questions(request, quiz_id):
    quiz = get_object_or_404(EmergencyQuiz, id=quiz_id)
    questions = QuizQuestion.objects.filter(quiz=quiz).order_by('order')
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_question':
            question_form = QuizQuestionForm(request.POST)
            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.quiz = quiz
                question.save()
                messages.success(request, 'Question added successfully.')
            else:
                messages.error(request, 'Error adding question.')
        
        elif action == 'edit_question':
            question_id = request.POST.get('question_id')
            question = get_object_or_404(QuizQuestion, id=question_id)
            question_form = QuizQuestionForm(request.POST, instance=question)
            if question_form.is_valid():
                question_form.save()
                messages.success(request, 'Question updated successfully.')
            else:
                messages.error(request, 'Error updating question.')
        
        return redirect('manage_quiz_questions', quiz_id=quiz_id)
    
    question_form = QuizQuestionForm()
    
    return render(request, 'manage_quiz_questions.html', {
        'quiz': quiz,
        'questions': questions,
        'question_form': question_form,
    })

@login_required
def delete_question(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(QuizQuestion, id=question_id)
        quiz_id = question.quiz.id
        question.delete()
        messages.success(request, 'Question successfully deleted.')
    return redirect('manage_quiz_questions', quiz_id=quiz_id)

@login_required
def manage_question_answers(request, question_id):
    question = get_object_or_404(QuizQuestion, id=question_id)
    answers = QuizAnswer.objects.filter(question=question)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_answer':
            answer_form = QuizAnswerForm(request.POST)
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.question = question
                answer.save()
                messages.success(request, 'Answer added successfully.')
            else:
                messages.error(request, 'Error adding answer.')
        
        elif action == 'edit_answer':
            answer_id = request.POST.get('answer_id')
            answer = get_object_or_404(QuizAnswer, id=answer_id)
            answer_form = QuizAnswerForm(request.POST, instance=answer)
            if answer_form.is_valid():
                answer_form.save()
                messages.success(request, 'Response updated successfully.')
            else:
                messages.error(request, 'Error updating response.')
        
        elif action == 'save_answers':
            formset = QuizAnswerInlineFormSet(request.POST, instance=question)
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Answers updated successfully.')
            else:
                messages.error(request, 'Error updating responses.')
        
        return redirect('manage_question_answers', question_id=question_id)
    
    answer_form = QuizAnswerForm()
    formset = QuizAnswerInlineFormSet(instance=question)
    
    return render(request, 'manage_question_answers.html', {
        'question': question,
        'answers': answers,
        'answer_form': answer_form,
        'formset': formset,
    })

@login_required
def delete_answer(request, answer_id):
    if request.method == 'POST':
        answer = get_object_or_404(QuizAnswer, id=answer_id)
        question_id = answer.question.id
        answer.delete()
        messages.success(request, 'Reply successfully deleted.')
    return redirect('manage_question_answers', question_id=question_id)

@login_required
def delete_object(request, type, pk):
    if request.method == 'POST':
        model_map = {
            'category': QuoteType,
            'quote': MotivationalQuote,
            'quiz': EmergencyQuiz,
        }
        model = model_map.get(type)
        if model:
            obj = get_object_or_404(model, pk=pk)
            obj.delete()
            messages.success(request, f'{type.capitalize()} successfully deleted.')
        else:
            messages.error(request, 'Invalid type.')
    return redirect('manager')