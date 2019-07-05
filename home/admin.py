from django.contrib import admin

from home.models import Student , Teacher, Marks,Library
from home.models import Section,teacher1,library1,Book

#from .models import student
#from account.models import AccInfo

# Register your models here.

# admin.site.register(Student)
# admin.site.register(Teacher)
# admin.site.register(Marks)
# admin.site.register(Library)
# admin.site.register(Section)
# admin.site.register(teacher1)
# admin.site.register(library1)
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('student_name','id')
    list_filter=('student_name','timestamp','department')
    fields=('student_name','department')

@admin.register(teacher1)
class teacher1Admin(admin.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(library1)
class library1Admin(admin.ModelAdmin):
    pass        
