from django.contrib import admin
from tgbot.models import AbsentStudents, Schedule, BotUser, ScheduleChecked

# Register your models here.


class AbsentStudentsAdmin(admin.ModelAdmin):
    # Display only `name` and `description` fields
    list_display = ('group_name', 'student_name',
                    'subject_name', 'subject_date')
    # readonly_fields = ('created_at',)  # Make the `created_at` field read-only
    # ordering = ('created_at',)  # Order instances by `created_at` field (ascending)


class BotUserAdmin(admin.ModelAdmin):
    list_display = ('bot_id', 'username', 'first_name', 'last_name')


class CheckedInline(admin.StackedInline):
    model = ScheduleChecked
    fields = ['id', 'group_name',
              'subject_name', 'employee_name', 'subject_date']
    extra = 0
    can_delete = True
    can_add = False


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name', 'group_language',
                    'subject_name', 'employee_name', 'subject_date', 'checked')
    list_editable = ('checked',)
    search_fields = ["id", "group_name", "group_language",
                     "department_name", "employee_name", "subject_date", "subject_name"]
    inlines = (CheckedInline,)


class ScheduleCheckedAdmin(admin.ModelAdmin):
    list_display = ('id', 'schedule_id', 'group_name',
                    'subject_name', 'employee_name', 'subject_date')
    list_editable = ('subject_name',)
    search_fields = ["subject_name", "id"]


admin.site.register(AbsentStudents, AbsentStudentsAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(BotUser, BotUserAdmin)
admin.site.register(ScheduleChecked, ScheduleCheckedAdmin)
