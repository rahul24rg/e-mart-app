from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    completed=models.BooleanField(default=False)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer_id):
        return Orders.objects.filter(customer=customer_id).order_by('-date')
