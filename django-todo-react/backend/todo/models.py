# todo/models.py

from django.db import models
# Create your models here.

class Categorize(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return "%s %s" % (self.name)



class Todo(models.Model):
  title = models.CharField(max_length=120)
  priority = models.IntegerField(choices=((1, ("low")),(2, ("high"))),
                                default=1)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  due_date = models.DateField()
  categorize = models.ForeignKey(Categorize, on_delete=models.CASCADE)


  def _str_(self):
    return self.title

