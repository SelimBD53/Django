from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    return HttpResponse('''
                        <a href = '/first_app/about/'>About </a>
                        <a href = '/second_app/courses/'>Courses</a>
                        <a href = '/second_app/feedback/'>Feedback</a>
                        <h1>This is Contact Page.</h1>
                        ''')

def about(request):
    return HttpResponse('''
                        <a href = '/first_app/contact/'>Contact </a>
                        <a href = '/second_app/courses/'>Courses</a>
                        <a href = '/second_app/feedback/'>Feedback</a>
                        <h1>This is About Page.</h1>
                        ''')


