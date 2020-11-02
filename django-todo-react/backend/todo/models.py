# todo/models.py

from django.db import models
# Create your models here.

# add this
class Todo(models.Model):
  title = models.CharField(max_length=120)
  priority = models.IntegerField(choices=((1, ("week")),(2, ("Strong"))),
                                default=1)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  due_date = models.DateField()

  def _str_(self):
    return self.title