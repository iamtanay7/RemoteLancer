from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm,PostJobForm,PostProjectForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Jobs,Projects
from django.views import generic
# Create your views here.

@method_decorator(login_required,name='dispatch')
class JobsListView(generic.ListView):
    template_name = 'freelance/jobs.html'
    context_object_name = 'all_jobs'

    def get_queryset(self):
        return Jobs.objects.all()


@method_decorator(login_required,name='dispatch')
class JobApplicationView(generic.detail.DetailView):
    model = Jobs
    template_name = 'freelance/job_appl.html'


@method_decorator(login_required,name='dispatch')
class ProjectsListView(generic.ListView):
    template_name = 'freelance/projects.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Projects.objects.all()


@method_decorator(login_required,name='dispatch')
class ProjectApplicationView(generic.detail.DetailView):
    model = Projects
    template_name = 'freelance/project_bid.html'


@method_decorator(login_required,name='dispatch')
class PostedJobsListView(generic.ListView):
    template_name = 'freelance/posted_jobs.html'
    context_object_name = 'posted_jobs'

    def get_queryset(self):
        return Jobs.objects.filter(author=self.request.user.username)



def index(request):
    return render(request,'freelance/index.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'freelance/registration_form.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('freelance:index')
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.username = username
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('freelance:index')

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required,name='dispatch')
class PostJobFormView(View):
    form_class = PostJobForm
    template_name = 'freelance/post_job.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            title = form.cleaned_data['title']
            domain = form.cleaned_data['domain']
            job_desc = form.cleaned_data['job_desc']
            job.title = title
            job.domain = domain
            job.author = request.user.username
            job.job_desc = job_desc
            job.save()
            return redirect('freelance:index')
        return render(request, self.template_name, {
            'form': form,
            'errormsg':'Invalid form. Please refill',
        })

@method_decorator(login_required,name='dispatch')
class PostProjectFormView(View):
    form_class = PostProjectForm
    template_name = 'freelance/post_project.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            title = form.cleaned_data['title']
            domain = form.cleaned_data['domain']
            project_desc = form.cleaned_data['project_desc']
            project.title = title
            project.domain = domain
            project.author = request.user.username
            project.project_desc = project_desc
            project.save()
            return redirect('freelance:index')
        return render(request, self.template_name, {
            'form': form,
            'errormsg':'Invalid form. Please refill',
        })


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'freelance/login.html'
    def get(self, request):
        if request.user.username:
            return redirect('freelance:index')
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('freelance:index')



        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('freelance:index')






