from django.shortcuts import render
from .models import Story

# Define the views for each page
def who_we_are_view(request):
    return render(request, 'who_we_are/whoweare.html')

def contribute_view(request):
    return render(request, 'contribute/contribute.html')

def get_involved_view(request):
    return render(request, 'get_involved/getinvolved.html')

def home_view(request):
    return render(request, 'news_stories/newsstories.html')

def our_work_view(request):
    return render(request, 'our_work/ourwork.html')

def news_stories(request):
    stories = Story.objects.all()
    return render(request, 'newsstories.html', {'stories': stories})

def story_list(request):
    stories = Story.objects.all()  # Get all stories from the database
    return render(request, 'your_template_name.html', {'stories': stories})