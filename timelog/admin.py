from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import TimeLog
# Register your models here.


class TimeLogAdmin(ImportExportModelAdmin):
    list_display = ('user_id', 'date', 'time', 'CI_CO')
    list_filter = ('user_id', 'date', 'CI_CO')
    search_fields = ('user_id', 'date', 'CI_CO')


admin.site.register(TimeLog, TimeLogAdmin)
#  return f'{self.user_id} | {self.CI_CO} | {self.date} | {self.time}'


# class NoteAdmin(admin.ModelAdmin):
#     '''
#         Admin View for Note
#     '''
#     list_display = ('id', 'title', 'slug', 'date_added')
#     list_filter = ('title', 'date_added')
#     search_fields = ('title', 'body')
#     prepopulated_fields = {'slug': ('title',)}


# admin.site.register(Note, NoteAdmin)
