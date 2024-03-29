"""URLs for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.all_topics, name='topics'),
    path('topics/<int:topic_id>', views.topic, name='topic'),
    path('newtopic', views.new_topic, name='new_topic'),
    path('newentry/<int:topic_id>', views.new_entry, name='new_entry'),
    path('editentry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
