from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=175)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

class Employee(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

class TaskStatus(models.Model):
    name = models.CharField(max_length=155)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'companies_task_status' #Para especificar o nome da tabela

class Task(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    due_date = models.DateTimeField(null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    