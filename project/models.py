from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import SlugField
import datetime
from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()

class Project(models.Model):
  STATUS = (
    ('done','DONE'),
    ('ongoing','ONGOING'),
    ('cancelled','CANCELLED'),
    )
  PRIORITY=(('U','unset'),('H','High'), ('L','Low'),)

  title = models.CharField(max_length=200)
  slug=models.SlugField(unique=True)
  description = models.TextField()
  deadline = models.DateField()
  status = models.CharField(max_length=10,choices=STATUS)
  priority = models.CharField(max_length=10,choices=PRIORITY)
  assigned_to = models.ManyToManyField(User)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ('title',)

  @property
  def is_deadline(self):
    return datetime.date.today() > self.deadline

  @property
  def time_to_complete(self):
    # Checking if the deadline has passed.
    return -1 if self.is_deadline else (self.deadline-self.created_at).days

  def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

  def __str__(self):
    return self.title