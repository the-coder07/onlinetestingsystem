from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
def greeting(request):
    menu="""
    <a href="http://localhost:8000/testapp/">Home</a>
    <a href="http://localhost:8000/testapp/about/">About</a>
    <a href="http://localhost:8000/testapp/contacts/">Contacts</a>
    """
    s="<h1>hello world this is my first django project</h1>"
    s=menu+s
    return HttpResponse(s)
def about(request):
    menu="""
     <a href="http://localhost:8000/testapp/">Home</a>
    <a href="http://localhost:8000/testapp/about/">About</a>
    <a href="http://localhost:8000/testapp/contacts/">Contacts</a>
    """
    s="<h1>about Page</h1>"
    s=menu+s
    return HttpResponse(s)
def contacts(request):
    menu="""
    <a href="http://localhost:8000/testapp/">Home</a>
    <a href="http://localhost:8000/testapp/about/">About</a>
    <a href="http://localhost:8000/testapp/contacts/">Contacts</a>
    """
    s="<h1>contacts Page</h1>"
    s=menu+s
    return HttpResponse(s)
