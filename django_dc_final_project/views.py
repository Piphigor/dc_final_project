# -*- coding: utf-8 -*-
from collections import defaultdict

from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Avg

from .models import Student, Subject, Score
from .forms import StudentForm, SubjectForm, ScoreForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        scores = Score.objects.all()
        student_scores = defaultdict(dict)

        subjects = Subject.objects.all()
        for score in scores:
            subject_name = score.subject.name
            student_scores[score.student][subject_name] = score.value

        score_statistics = [
            {
                'subject': subject,
                'avg_score': f'{scores.filter(subject__name=subject).aggregate(Avg("value"))["value__avg"] or 0:.1f}',
            }
            for subject in subjects
        ]

        student_statistics = [
            {
                'student': student,
                'scores': [f'{scores.get(subject.name, 0):.1f}' for subject in subjects],
                'avg_score': f'{sum(scores.values()) / len(scores):.1f}' if scores else 0
            }
            for student, scores in student_scores.items()
        ]

        if student_statistics:
            best_student = max(student_statistics, key=lambda x: x['avg_score'])
            worst_student = min(student_statistics, key=lambda x: x['avg_score'])
        else:
            best_student = worst_student = None

        context.update(
            {
                'subjects': subjects,
                'student_statistics': student_statistics,
                'score_statistics': score_statistics,
                'best_student': best_student,
                'worst_student': worst_student,
                'students': Student.objects.all(),
                'scores': scores,
            }
        )
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        subjects = Subject.objects.all()
        for subject in subjects:
            Score.objects.create(student=self.object, subject=subject, value=0)
        return response


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('index')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('index')


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        students = Student.objects.all()
        for student in students:
            Score.objects.create(student=student, subject=self.object, value=0)
        return response


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_form.html'
    success_url = reverse_lazy('index')


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subject_confirm_delete.html'
    success_url = reverse_lazy('index')


class ScoreCreateView(CreateView):
    model = Score
    form_class = ScoreForm
    template_name = 'score_form.html'
    success_url = reverse_lazy('index')


class ScoreUpdateView(UpdateView):
    model = Score
    form_class = ScoreForm
    template_name = 'score_form.html'
    success_url = reverse_lazy('index')


class ScoreDeleteView(DeleteView):
    model = Score
    template_name = 'score_confirm_delete.html'
    success_url = reverse_lazy('index')