#i have created this file-shivansh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyser(request):
    djtext = request.POST.get('text', 'no text available')
    punc = request.POST.get('punc', 'off')
    upper = request.POST.get('upper', 'off')
    nline = request.POST.get('nlineremove', 'off')
    space = request.POST.get('xspaceremove', 'off')
    count = request.POST.get('charcount', 'off')
    tchar = len(djtext)

    if punc == 'on':
        analysed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for c in djtext:
            if c not in punctuations:
                analysed = analysed + c
        param = {"purpose": "Removal of Punctuations", 'analysed_text': analysed}
        djtext = analysed

    if upper == 'on':
        analysed = ""
        for c in djtext:
            analysed = analysed + c.upper()
        param = {"purpose": "Changed to upper text", 'analysed_text': analysed}
        djtext = analysed

    if nline == 'on':
        analysed = ""
        for c in djtext:
            if c != '\n' and c != '\r':
                analysed = analysed + c
        param = {"purpose": "After removing newlines", 'analysed_text': analysed}
        djtext = analysed

    if space == 'on':
        analysed = ""
        for i in range(0, len(djtext)):
            if djtext[i] ==' ' and djtext[i+1] == ' ':
                continue
            else:
                analysed = analysed + djtext[i]
        param = {"purpose": "After removing extra spaces", 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyser.html', param)
    if count == 'on':
        analysed = djtext + '\nAnd number of characters typed are:' + str(tchar)
        param = {"purpose": "Number of characters typed:", 'analysed_text': analysed}

    if(punc != 'on' and upper != 'on' and nline != 'on' and space != 'on' and count != 'on'):
        return HttpResponse('<h3>please atleast choose one option</h3><br><button type="button"><a href="/">Move to main page</a></button>')
    else:
        return render(request, 'analyser.html', param)

