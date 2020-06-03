from django.urls import path
from . import views

app_name = 'freelance'

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name = 'register'),
    path('', views.index, name='index'),
    path('logout/',views.logout_view,name='logout'),
    path('post_job/', views.PostJobFormView.as_view(), name='post_job'),
    path('post_project/', views.PostProjectFormView.as_view(),name='post_project'),
    path('jobs/', views.JobsListView.as_view(), name='jobs'),
    path('projects/', views.ProjectsListView.as_view(), name='projects'),
    path('login/', views.LoginFormView.as_view(), name = 'login'),
    path('posted_jobs/', views.PostedJobsListView.as_view(), name='posted_jobs'),
    path('jobs/<int:pk>/',views.JobApplicationView.as_view(), name='job_appl'),
    path('projects/<int:pk>/',views.ProjectApplicationView.as_view(), name='project_bid'),
    

]
