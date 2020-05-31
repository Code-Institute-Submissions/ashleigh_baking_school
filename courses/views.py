from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Course, Category

def all_courses(request):
    """ A view to show all courses, including sorting and search queries """

    courses = Course.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            courses = courses.filter(category__title__in=categories)
            categories = Category.objects.filter(title__in=categories)

    context = {
        'courses': courses,
        'current_categories': category,
    }
    return render(request, 'courses/courses.html', context)

def course(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    content = {
        'course' : course
    }
    return render(request, 'courses/individual_course.html', content)