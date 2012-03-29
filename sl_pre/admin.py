from sl_pre.models import Student,Author,Stream,Subject,Chapter,Semester,Note

from django.contrib import admin



class NoteAdmin(admin.ModelAdmin):
    list_filter = ('subject','author','semester','stream')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","age","gender")

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title','semester')
    list_filter = ('streams','semester')

#class ChapterAdmin(admin.modelAdmin):
#    list_filter = ('subject')

admin.site.register(Student)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Stream)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Chapter)
admin.site.register(Semester)

#admin.site.register(Note)
#Here when we use NoteAdmin to configure admin page use following code
admin.site.register(Note,NoteAdmin)
