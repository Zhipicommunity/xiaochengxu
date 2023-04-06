from datetime import datetime

from django.db import models


# # Create your models here.
# class Counters(models.Model):
#     id = models.AutoField
#     count = models.IntegerField(max_length=11, default=0)
#     createdAt = models.DateTimeField(default=datetime.now(), )
#     updatedAt = models.DateTimeField(default=datetime.now(),)

#     def __str__(self):
#         return self.title

#     class Meta:
#         db_table = 'Counters'  # 数据库表名
class UsersInfo(models.Model):
    id=models.AutoField
    username=models.CharField(max_length=64)
    userpwd=models.IntegerField(max_length=11)
    fabuneirong=models.CharField()
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(),)

    class My_sql:
        db_data='usersinfo'
