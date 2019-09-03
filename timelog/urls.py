from django.urls import path


from . import views

urlpatterns = [
    path('', views.TimeLogListView.as_view(), name='home'),
    path('timelog/new/', views.TimeLogCreateView.as_view(), name='timelog_new'),
]
