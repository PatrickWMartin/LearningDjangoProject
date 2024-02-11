from django.shortcuts import render
from  .models import Topic

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')


def topics(requst):
    topics = Topic.objects.order_by('date_added')
    return render(requst, 'learning_logs/topics.html', {'topics': topics})
