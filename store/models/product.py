from django.db import models
from .catrogry import Cateogrie

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200,null=True,default='')
    image = models.ImageField(upload_to='uploads/products')
    cateogry=models.ForeignKey(Cateogrie,on_delete=models.CASCADE)


    @staticmethod
    def getProductsByID(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_poduct():
        return Product.objects.all()

    @staticmethod
    def get_all_poduct_byID(cateogry_id):
       if cateogry_id:
          return Product.objects.filter(cateogry=cateogry_id)
       else:
           return Product.get_all_poduct();