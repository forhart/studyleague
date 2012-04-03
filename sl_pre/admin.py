from sl_pre.models import Student,Author,Stream,Subject,Chapter,Semester,Note

from django.contrib import admin



class NoteAdmin(admin.ModelAdmin):
    list_filter = ('subject','author','semester','stream')
    prepopulated_fields = {"slug":('title',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","age","gender")

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title','semester')
    list_filter = ('streams','semester')
    prepopulated_fields = {'slug':('title',)}

class StreamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}

class SemesterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}

class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}

#class ChapterAdmin(admin.modelAdmin):
#    list_filter = ('subject')

admin.site.register(Student)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Stream,StreamAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Semester,SemesterAdmin)

#admin.site.register(Note)
#Here when we use NoteAdmin to configure admin page use following code
admin.site.register(Note,NoteAdmin)
