from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django import forms
import uuid

# Create your views here.

class NewStory(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    newstory = forms.CharField(label='New story', min_length=10, max_length=120,widget=forms.Textarea)

    

stories = []
next_entry = 1
def homepage(request):
    return render(request, 'addStory/homepage.html',{
        'stories' : stories
    })

def add(request):
    return render(request, 'addStory/add.html',{
        'form' : NewStory()

    })


def addentry(request):
    global next_entry
    if request.method == 'POST':
        form = NewStory(request.POST)
        if form.is_valid():
            newstory = form.cleaned_data['newstory']
            username = form.cleaned_data['username']
            stories.append(f'ID{next_entry} - {username.capitalize()} shared a story : " {newstory} "')
            next_entry +=1
        else:
            return redirect('add')
    return redirect('homepage')

def entry(request, id):
    try:
        entry = stories[id-1]
        return JsonResponse({'id': id, 'entry': entry})
    except IndexError:
        return JsonResponse({'error': 'Entry not found'})
    

