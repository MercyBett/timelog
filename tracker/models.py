from django.db import models
# from users.models import User
from project.models import Project
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class ProjectTracker(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField(blank=True,db_index=True)
  total_time = models.DecimalField(max_digits=8,decimal_places=2,default=0)

  class Meta:
    unique_together = ('user', 'project',)

  @property
  def total_time(self):
    self.total_time = self.end_time - self.start_time

  def __str__(self):
    return f'{self.user} tracking {self.project}'