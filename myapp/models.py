from django.db import models


class Dashdetail(models.Model):
  title = models.CharField(max_length=225)
  due_number = models.IntegerField()
  due_amount = models.IntegerField()
  year_income = models.IntegerField()
  month_income = models.IntegerField()
  daily_income = models.IntegerField()
  month_profit = models.IntegerField()
  year_expense = models.IntegerField()
  month_expense = models.IntegerField()
  total_student = models.IntegerField()
  total_parent = models.IntegerField()
  total_boys = models.IntegerField()
  total_girl = models.IntegerField()
  
  def __str__(self):
    return self.title