from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import QuoteType, MotivationalQuote, EmergencyQuiz, QuizQuestion, QuizAnswer

class CategoryForm(forms.ModelForm):
    class Meta:
        model = QuoteType
        fields = ['name']
        labels = {
            'name': 'Nombre de la categoría',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar', css_class='btn-primary')
        )

class MotivationalQuoteForm(forms.ModelForm):
    class Meta:
        model = MotivationalQuote
        fields = ['text', 'author', 'quote_type', 'is_active']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'text': 'Texto de la cita',
            'author': 'Autor (opcional)',
            'quote_type': 'Categoría',
            'is_active': 'Activa'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'text',
            Row(
                Column('author', css_class='form-group col-md-6'),
                Column('quote_type', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Field('is_active'),
            Submit('submit', 'Guardar Cita', css_class='btn-primary')
        )

class EmergencyQuizForm(forms.ModelForm):
    class Meta:
        model = EmergencyQuiz
        fields = ['title', 'description', 'category', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'title': 'Título del Quiz',
            'description': 'Descripción',
            'category': 'Categoría',
            'is_active': 'Activo'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'title',
            'description',
            Row(
                Column('category', css_class='form-group col-md-6'),
                Column(Field('is_active', wrapper_class='form-check'), css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar Quiz', css_class='btn-primary')
        )

class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['question_text', 'order']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 3}),
            'order': forms.NumberInput(attrs={'min': 0})
        }
        labels = {
            'question_text': 'Texto de la pregunta',
            'order': 'Orden de visualización'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'question_text',
            Row(
                Column('order', css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar Pregunta', css_class='btn-primary')
        )

class QuizAnswerForm(forms.ModelForm):
    class Meta:
        model = QuizAnswer
        fields = ['answer_text', 'is_correct']
        labels = {
            'answer_text': 'Texto de la respuesta',
            'is_correct': '¿Es correcta?'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('answer_text', css_class='form-group col-md-9'),
                Column(Field('is_correct', wrapper_class='form-check'), css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar Respuesta', css_class='btn-primary')
        )

class QuizAnswerInlineFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Submit('submit', 'Guardar Respuestas', css_class='btn-primary')
        )