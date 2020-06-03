from django.db import models

# Create your models here.
class Jobs(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    job_desc=models.CharField(max_length=2000)
    domain=models.CharField(max_length=50)

class Projects(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    project_desc = models.CharField(max_length=2000)
    domain=models.CharField(max_length=50)

class Job_application(models.Model):
    job_id=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    applicant_username=models.CharField(max_length=50)
    hourly_rate=models.IntegerField(default=0)
    is_accepted = models.BooleanField(default=False)
    appl_desc = models.CharField(max_length=2000)

class Project_bid(models.Model):
    project_id=models.ForeignKey(Projects,on_delete=models.CASCADE)
    bidder_username = models.CharField(max_length=50)
    bid_amount = models.IntegerField(default=0)
    is_accepted = models.BooleanField(default=False)
    bid_desc = models.CharField(max_length=2000)






