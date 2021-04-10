from django.db import models


class Cateogrie(models.Model):
    name=models.CharField(max_length=20)

    @staticmethod
    def get_all_cateogries():
       return Cateogrie.objects.all()


    def __str__(self):
        return self.name