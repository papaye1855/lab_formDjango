from django.db import models

# Create your models here.

class Todo(models.Model):
    img = models.FileField(upload_to="static/images/todos/",blank=True,null=True)
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    isCompleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titre

    
    @property
    def imageUrl(self) -> str:
        if(str(self.img).startswith("/static")):
            return str(self.img).replace("/static/images/todos/","")
        return str(self.img).replace("static/images/todos/","")
