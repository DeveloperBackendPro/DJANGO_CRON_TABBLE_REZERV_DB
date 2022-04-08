from django.db import models



class ContactMessage(models.Model):
    name = models.CharField(blank=True, max_length=255)
    message = models.TextField(blank=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
