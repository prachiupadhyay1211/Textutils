from http.client import HTTPResponse  # I have created this file - Prachi
from django.http import HttpResponse
from django.shortcuts import render


#  code for 1st part (just opening website-codewithharry)
# from django.http import HttpResponse
#
# def index(request):
#      return HttpResponse('''<h1>Harry</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">code with Harry</a>''')
# def about(request):
#      return HttpResponse("About Harry")

# code for laying of pipeline
def index(request):
    # return HttpResponse("Home")

    return render(request, 'index.html')
    # render has many variables, one is dict also & so for that we have written earlier return render(request,'index.html',params)


def analyze(request):
    # GET THE TEXT
    djtext = (request.POST.get('text', 'default'))
    print(djtext)
    # request.GET.get   --> give value you write else give default value

    # CHECK CHECKBOX VALUES
    removepun = request.POST.get('removepunc', 'off')
    print(removepun)

    fullcaps = request.POST.get('fullcaps','off')

    newlineremover = request.POST.get('newlineremover','off')

    spaceremover = request.POST.get('spaceremover','off')

    charcount = request.POST.get('charcount','off')


    # Analyzing text
    # return HttpResponse("rempun <a href='/'>back<a/>")     --> this is used when we simply analyzing from inde.html        # back button

    # now we made diff template for analyzing so now we use return render for it
    # CHECK WHICH CHECKBOX IS ON
    if (removepun == "on"):
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if(fullcaps == 'on'):
         analyzed=""
         for char in djtext:
             analyzed = analyzed + char.upper()
         params = {'purpose':'Change to Uppercase', 'analyzed_text' : analyzed}
         # return render(request, 'analyze.html', params)
         djtext = analyzed

    if(newlineremover == 'on'):
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params ={'purpose': 'Remove Newline', 'analyzed_text' : analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if(spaceremover == 'on'):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Space Remover', 'analyzed_text':analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if(charcount == 'on'):
        analyzed=""
        count_dict = {}
        for char in djtext:
            count_dict[char] = count_dict.get(char,0)+1
        analyzed = str(count_dict)           # for easily displaying we need to convert it into str as displaying dict need to handle it differently.
        params = {'purpose':'Char Count', 'analyzed_text':analyzed}
        # return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")

    if(removepun != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcount != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)


# def capitalizefirst(request):
#      return HttpResponse("capfirst <a href='/'>back<a/>")
# def newlineremove(request):
#      return HttpResponse("newline remover <a href='/'>back<a/>")
#
# def spaceremove(request):
#      return HttpResponse("space remover <a href='/'>back<a/>")
#
# def capitalizefirst(request):
#      return HttpResponse("capfirst <a href='/'>back<a/>")
#
# def charcount(request):
#      return HttpResponse("charcount <a href='/'>back<a/>")

# <a href='/'>back<a/>   (for back button)