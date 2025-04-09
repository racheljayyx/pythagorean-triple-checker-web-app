from django.shortcuts import render
from django.http import HttpResponse

def triple_checker(request):
    return HttpResponse("Welcome to the Pythagorean Triple Checker!")
