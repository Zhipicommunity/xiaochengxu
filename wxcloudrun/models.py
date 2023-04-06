from django.db import models


# Create your models here.
# class Counters(models.Model):
#     id = models.AutoField
#     count = models.IntegerField(max_length=11, default=0)
#     createdAt = models.DateTimeField(default=datetime.now(), )
#     updatedAt = models.DateTimeField(default=datetime.now(),)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         db_table = 'counter'  # 数据库表名
# # class UsersInfo(models.Model):
#     id=models.AutoField
#     usersname=models.CharField(max_length=64)
#     userspwd=models.IntegerField(max_length=11)
#     neirong=models.CharField()
#     createdAt = models.DateTimeField(default=datetime.now(), )
#     updatedAt = models.DateTimeField(default=datetime.now(),)
#
#     class My_sql:
#         db_data='usersinfo'

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # 其他字段

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
