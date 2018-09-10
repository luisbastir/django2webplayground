from django.urls import path
from .views import ThreadDetail, ThreadList, add_message, start_thread

messenger_patterns = ([
  path("", ThreadList.as_view(), "list"),
  path("thread/<int:pk>/", ThreadDetail.as_view(), "detail"),
  path("thread/<int:pk>/add/", add_message, "add"),
  path("thread/start/<username>/start/", start_thread, "start"),
], "messenger")