from django.shortcuts import render
from  .models import Topic

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')


def all_topics(requst):
    topics = Topic.objects.order_by('date_added')
    return render(requst, 'learning_logs/all_topics.html', {'topics': topics})
