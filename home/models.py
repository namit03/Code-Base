from django.db import models

# Create your models here.

class Student(models.Model):
    student_name=models.CharField('Student Name',max_length =30, null=True)
    dept = (
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )

    
    department=models.CharField('Department',choices=dept, blank=True, null=True, max_length = 30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name    
    

class Teacher(models.Model):
    teacher_id = models.AutoField(verbose_name = "ID",primary_key = True)
    teacher_name = models.CharField(verbose_name = "Teacher Name",max_length = 30)

class Marks(models.Model):
    sub1 = models.IntegerField(verbose_name = "Subject 1")
    sub2 = models.IntegerField(verbose_name = "Subject 2")
    sub3 = models.IntegerField(verbose_name = "Subject 3")

class Library(models.Model):
    sut = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    # sut = models.ForeignKey('Student',on_delete=models.CASCADE )   
    
class Section(models.Model):
    section = models.CharField('Section',max_length=20,null=False)
    advisor = models.OneToOneField('Teacher',on_delete=models.SET_NULL,null=True)
    students = models.ManyToManyField('Student',null=False)
    def __str__(self):
        return self.section

class teacher1(models.Model):
    teacher1=models.CharField('Teacher Name',max_length=100,null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teacher1

class library1(models.Model):
    library_name=models.CharField('library',null=True,max_length=30)
    books=models.ManyToManyField('Book',null=True)
    def __str__(self):
        return self.library_name

class Book(models.Model):
    book=models.CharField('Book',max_length=30,null=True)
    def __str__(self):
        return self.book
    

