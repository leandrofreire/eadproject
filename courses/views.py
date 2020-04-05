from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourse


# Create your views here.

def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)


def detalhe(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/detalhe.html'
    return render(request, template_name, context)
