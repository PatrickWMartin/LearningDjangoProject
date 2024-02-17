from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')


@login_required
def all_topics(requst):
    topics = Topic.objects.order_by('date_added')
    return render(requst, 'learning_logs/all_topics.html', {'topics': topics})


@login_required
def topic(request, topic_id):
    topic_object = Topic.objects.get(id=topic_id)
    entries = topic_object.entry_set.order_by('-date_added')
    return render(request, 'learning_logs/topic.html',
                  {'topic': topic_object, 'entries': entries})


@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    else:
        form = TopicForm()

    return render(request, 'learning_logs/new_topic.html', {'form': form})


@login_required
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

    return render(request, 'learning_logs/new_entry.html', {'topic': topic_object, 'form': form})


@login_required
def edit_entry(request, entry_id):
    entry_object = Entry.objects.get(id=entry_id)
    topic = entry_object.topic

    if request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    else:
        form = EntryForm()

    context = {'entry': entry_object, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
