from sl_pre.models import Student,Author,Stream,Subject,Chapter,Semester,Note,SubChapter
from studyleague import settings
from django.contrib import admin

#Following class is to embbed Dojo's editor
#add Media=CommonMedia in every AdminClass to enable it. 

#class CommonMedia:
#    js = (
#        '/site_media/dojo-toolkit/dojo/dojo.js',
#        '/site_media/js/editor.js',
#        )
#    css = {
#        'all':('/site_media/css/editor.css',),
#        }

class NoteAdmin(admin.ModelAdmin):
    list_filter = ('subject','author','semester','stream')
    prepopulated_fields = {"slug":('title',)}
 #   Media = CommonMedia

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","age","gender")
#    Media = CommonMedia

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title','semester')
    list_filter = ('streams','semester')
    prepopulated_fields = {'slug':('title',)}
#    Media = CommonMedia #this brings dojo's editor in admin panel

class StreamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
#    Media = CommonMedia

class SemesterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
    
class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
#    Media=CommonMedia

class SubChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
#    Media = CommonMedia
#    list_filter = ('chapter',)

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
admin.site.register(SubChapter,SubChapterAdmin)
