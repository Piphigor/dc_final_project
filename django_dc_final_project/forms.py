from django import forms
from .models import Student, Subject, Score

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'email']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['student', 'subject', 'value']