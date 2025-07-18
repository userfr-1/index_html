from django.db import models

# Create your models here.

#country jadval bor uni title bor,created_ed,updated_ed, jadval region title,image,created_ed,update_ed,region countryga foreign key,ushbularni darsdagidak chiqarberiladi,
# navbar, components, list code
#md boostrap 5,2 chsiiga kiriladi ,.
class Country(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Region(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.title