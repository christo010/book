from django.db import models

# Create your models here.

class employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    salary=models.IntegerField()
    email=models.EmailField(null=True)
    def __str__(self):
        return self.name


class studeny(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=20)
    email=models.EmailField(unique=True,null=True)

    def __str__(self):
        return self.name
    

class emp(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    salary=models.PositiveIntegerField()
    contact=models.IntegerField()


class bookdb(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    year=models.PositiveIntegerField()
    genere=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class personal(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(null=True)
    course=models.CharField(max_length=20)
    
class studentdb(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    place=models.CharField(max_length=20)

    def __str__(self):
        return self.name

   
