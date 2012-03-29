from dbtest.models import Stream,Subject,Semester
from django.contrib import admin



#class Admin(admin.ModelAdmin):
#    list_filter = ('subject','author','semester','stream')

#class AuthorAdmin(admin.ModelAdmin):
#    list_display = ("first_name","last_name","age","gender")

#class ChapterAdmin(admin.modelAdmin):
#    list_filter = ('subject')

class SubjectAdmin(admin.ModelAdmin):
    list_filter = ('streams',)
    list_display = ['title','semester']
    search_fields = ["title",'streams__title'] #implement this in every model

admin.site.register(Stream)
admin.site.register(Subject,SubjectAdmin)

admin.site.register(Semester)

#admin.site.register(Note)
#Here when we use NoteAdmin to configure admin page use following code
#admin.site.register(Note,NoteAdmin)
