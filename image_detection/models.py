from django.db import models

class DetectionHistory(models.Model):
    image = models.ImageField(upload_to='detections/')
    predictions = models.JSONField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"Detection at {self.uploaded_at}"