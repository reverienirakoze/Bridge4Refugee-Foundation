from django.shortcuts import render

# Define the views for each page
def who_we_are_view(request):
    return render(request, 'who_we_are/whoweare.html')

def contribute_view(request):
    return render(request, 'contribute/contribute.html')

def get_involved_view(request):
    return render(request, 'get_involved/getinvolved.html')

def news_stories_view(request):
    return render(request, 'news_stories/newsstories.html')

def our_work(request):
    return render(request, 'ourteam/our_work.html')
def home_view(request):
    return render(request, 'ourteam/ourteam.html')