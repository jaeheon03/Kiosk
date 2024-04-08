from django.db import models
from django.contrib.postgres.fields import ArrayField  


class EvaluationIntChoices(models.IntegerChoices):
    one = 1, '1'
    two = 2, '2'
    three = 3, '3'
    four = 4, '4'
    five = 5, '5'


class Menu(models.Model):
    name = models.CharField(max_length=50)
    cafe = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
class Size(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)

class Temperature(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    temperature = models.CharField(max_length=50)

class Option(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    option = models.CharField(max_length=50)


class Review(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    evaluation = models.IntegerField(choices=EvaluationIntChoices.choices)  # 수정
    created_dt = models.DateField("CREATE DATE", auto_now_add=True)
    modify_dt = models.DateField("MODIFY DATE", auto_now=True)

    class Meta:
        ordering = ('-modify_dt',)

    def __str__(self) -> str:
        return self.content

class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, null=True)
    temperature = models.CharField(max_length=50, null=True)
    option = models.CharField(max_length=50, null=True) 
    created_dt = models.DateField("CREATE DATE", auto_now_add=True)
    modify_dt = models.DateField("MODIFY DATE", auto_now=True)

    class Meta:
        ordering = ('created_dt',)

    def __str__(self) -> str:
        return self.menu.name