from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    user_name = models.CharField(max_length =30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Profile= models.ImageField(upload_to = 'images/')
    Bio= models.TextField()
    profile_image = models.ImageField(upload_to='profiles/', blank=True)
   
   
 
    

    def __str__(self):
        return self.user_name

    # class Meta:
    #     ordering = ['profile']


    def save_profile(self):
         self.save()  
         
    def delete_profile(self):
         self.save()  

    def display_profile(self):
         self.save()

    def update_profile(self):
         self.save()  

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
    image = models.ImageField(upload_to = 'gramys/')
    title = models.CharField(max_length =70)
    caption= models.TextField()
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile)
   

    def __str__(self):
        return self.title

      

    def save_images(self):
         self.save()  
         
    def delete_images(self):
         self.save()  

    def display_images(self):
         self.save()

    def update_images(self):
         self.save()     

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images    

 
       
class Comments(models.Model):
    comment = models.CharField(max_length = 300)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()





    







    
