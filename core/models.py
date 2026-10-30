from django.db import models
class ContactRequest(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    organization=models.CharField(max_length=200,blank=True)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.name} — {self.created_at:%Y-%m-%d}'
