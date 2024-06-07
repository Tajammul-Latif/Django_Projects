from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.

admin.site.register(Receipe)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_rank', 'total_marks', 'date_of_report_card_generation']
    
    def total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student = obj.student)
        return subject_marks.aggregate(marks = Sum('marks'))

admin.site.register(ReportCard, )