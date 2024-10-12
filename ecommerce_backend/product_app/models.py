from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
   # image = models.ImageField(upload_to = 'img',  blank = True, null=True, default='')
    description = models.TextField()
    num_of_prod_on_stock = models.IntegerField()
    date_enrolled = models.DateTimeField(auto_now=True) 
    

    def __str__(self):
        return self.title



class ProImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "images")
    image = models.ImageField(upload_to="img", default="", null=True, blank=True)
    def __str__(self):
        return f"{self.product.id} - {self.product.title}"
