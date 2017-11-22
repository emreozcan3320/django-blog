from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    # After a while when we want to list our post, we face a problem because title return as a post object.
    # to overcome that problem we define __str__ function.
    def __str__(self):
        return self.title
