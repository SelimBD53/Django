from django.shortcuts import render
from django.http import HttpResponse


def courses(request):
    return HttpResponse('''
                        <a href = '/second_app/feedback/'>Feedback</a>
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/first_app/about/'>About</a>
                        <h1>This is Courses Page.</h1>
                        ''')


def feedback(request):
    return HttpResponse('''
                        <a href = '/second_app/courses/'>Courses</a>
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/first_app/about/'>About</a>
                        <h1>This is Feedback Page.</h1>
                        ''')