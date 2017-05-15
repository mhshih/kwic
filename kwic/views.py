from django import forms

class WordForm(forms.Form):
    word=forms.CharField(max_length=100)


from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    if request.method=='POST':
        form=WordForm(request.POST)
        if form.is_valid():
            word=form.cleaned_data['word']
            return HttpResponse(word)
    else:
        return render(request,'template.htm',{'form':WordForm})
