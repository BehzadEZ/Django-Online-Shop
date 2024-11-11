from django.db import models

# Create your models here.



class slider(models.Model):
    imagename=models.ImageField(upload_to="media")
    title_img=models.CharField(max_length=200)

class advimgage(models.Model):
    advertize_image=models.ImageField(upload_to="media")
    title_adv_img=models.CharField(max_length=200)
