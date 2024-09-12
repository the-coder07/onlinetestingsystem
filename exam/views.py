from django.shortcuts import render
from django.http import HttpResponse

def testpaper(request):
    q="who develope python?"
    a="thosmas edition "
    b="alebert einstein"
    c="guiddo van rossum"
    d="Omprakash"
    d1={'q':q,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exam/show_test.html',d1)
    return res
def testresult(request):
    s="test result"
    return HttpResponse(s)
