from sl_pre.models import Student,Stream,Subject,Chapter,Semester,Topic,TopicTheory,TopicSolved,TopicUnsolved,TopicVideo
from sl_pre.models import SubjectTestPaper
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

#class NoteAdmin(admin.ModelAdmin):
#    list_filter = ('subject','author','semester','stream')
#    prepopulated_fields = {"slug":('title',)}
#   Media = CommonMedia

#class AuthorAdmin(admin.ModelAdmin):
#    list_display = ("first_name","last_name","age","gender")
#    Media = CommonMedia

class SubjectTestPaperAdmin(admin.ModelAdmin):
    list_display        = ('title','Subject')
    prepopulated_fields = { "slug":("title",)}
    search_fields       = [ 'title' ]   

class SubjectTestPaperInline(admin.TabularInline):
    model = SubjectTestPaper
    prepopulated_fields = {'slug':('title',)}
    extra = 1

  

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title','semester','numOfChapters')
    list_filter = ('streams','semester')
    prepopulated_fields = {'slug':('title',)}
    filter_horizontal = ('streams',)
    inlines = [SubjectTestPaperInline,]
   
#    Media = CommonMedia #this brings dojo's editor in admin panel

class StreamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
#    Media = CommonMedia

class SemesterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
    

    
#    Media=CommonMedia



#Following two classes are added to add links to pdf on the subchapter pad itself. 

class TopicTheoryAdmin(admin.ModelAdmin):
    list_display        = ('title','Topic')
    prepopulated_fields = { "slug":("title",)}
    search_fields       = [ 'title' ] 

class TopicTheoryInline(admin.TabularInline):
    model = TopicTheory
    prepopulated_fields = { "slug":("title",)}
    extra = 1
    
class TopicSolvedAdmin(admin.ModelAdmin):
    list_display        = ('title','topic')
    prepopulated_fields = { "slug":("title",)}
    search_fields       = [ 'title' ] 
    
class TopicSolvedInline(admin.TabularInline):
    model = TopicSolved
    prepopulated_fields = {'slug':('title',)}
    extra = 1

class TopicUnSolvedAdmin(admin.ModelAdmin):
    list_display        = ('title','Topic')
    prepopulated_fields = { "slug":("title",)}
    search_fields       = [ 'title' ] 
    
class TopicUnsolvedInline(admin.TabularInline):
    model = TopicUnsolved
    prepopulated_fields = {'slug':('title',)}
    extra = 1

class TopicVideoAdmin(admin.ModelAdmin):
    list_display        = ('title','Topic')
    prepopulated_fields = { "slug":("title",)}
    search_fields       = [ 'title' ] 
    
class TopicVideoInline(admin.TabularInline):
    model = TopicVideo
    prepopulated_fields = {'slug':('title',)}
    extra = 1
    

class TopicAdmin(admin.ModelAdmin):
    list_display=('title','chapter',)   #change this variable name to lowercase
    list_filter = ('chapter','chapter__subject','chapter__subject__streams','chapter__subject__semester')
    prepopulated_fields = {"slug":('title',)}
    search_fields = ['title' ]
    inlines = [TopicSolvedInline,TopicUnsolvedInline,TopicVideoInline,TopicTheoryInline]

class TopicInline(admin.TabularInline):
    model = Topic
    exclude =         ('description',)
    prepopulated_fields = {'slug':('title',)}


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title','subject','numOfTopics',)
    prepopulated_fields = {"slug":('title',)}
    inlines = [ TopicInline , ]
    list_filter = ['subject__streams','subject__semester']



admin.site.register(Student)
#admin.site.register(Author,AuthorAdmin)
admin.site.register(Stream,StreamAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Semester,SemesterAdmin)

#admin.site.register(Note)
#Here when we use NoteAdmin to configure admin page use following code
#admin.site.register(Note,NoteAdmin)
admin.site.register(Topic,TopicAdmin)
