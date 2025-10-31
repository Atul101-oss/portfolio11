from django.db import models

# Create your models here.
class DIP_work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    in_progress = models.BooleanField(default=False)

    def __str__(self):
        return self.title