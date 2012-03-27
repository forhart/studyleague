from sl_pre.models import User,Author,Stream,Subject,Semester,Note

from django.contrib import admin



class NoteAdmin(admin.ModelAdmin):
    list_filter = ('subject','author','semester','stream')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","age","gender")

admin.site.register(User)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Stream)
admin.site.register(Subject)
admin.site.register(Semester)

#admin.site.register(Note)
#Here when we use NoteAdmin to configure admin page use following code
admin.site.register(Note,NoteAdmin)
