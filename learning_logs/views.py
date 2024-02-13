from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')


def all_topics(requst):
    topics = Topic.objects.order_by('date_added')
    return render(requst, 'learning_logs/all_topics.html', {'topics': topics})


def topic(request, topic_id):
    topic_object = Topic.objects.get(id=topic_id)
    entries = topic_object.entry_set.order_by('-date_added')
    return render(request, 'learning_logs/topic.html',
                  {'topic': topic_object, 'entries': entries})


def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    else:
        form = TopicForm()

    return render(request, 'learning_logs/new_topic.html', {'form': form})


def new_entry(request, topic_id):
    topic_object = Topic.objects.get(id=topic_id)

    if request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic_object
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    else:
        form = EntryForm()

    return render(request, 'learning_logs/new_entry.html', {'form': form})
