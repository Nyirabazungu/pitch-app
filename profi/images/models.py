from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    user_name = models.CharField(max_length =30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Bio = models.CharField(max_length=300)
    profile_image = models.ImageField(upload_to='Images/', blank=True)
    
   
    def __str__(self):
        return self.user_name

    # class Meta:
    #     ordering = ['profile']


    def save_profile(self):
         self.save()  
         
    def delete_profile(self):
         self.delete()  

    def display_profile(self):
         self.display()

    def update_profile(self):
         self.update()  

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(user_name__icontains=search_term)
        return profiles       

    

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length =70)
    image = models.ImageField(upload_to = 'images/')
    caption= models.TextField()
   

    def __str__(self):
        return self.title

      

    def save_images(self):
         self.save()  
         
    
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images   

    def delete_image(self):
        self.delete()    

 
       
class Comments(models.Model):
    comment = models.CharField(max_length = 300)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

class Like(models.Model):
    likes= models.IntegerField(default=0)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.likes





    







    
