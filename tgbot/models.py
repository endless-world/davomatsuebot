from datetime import datetime
from django.db import models
# from django.core.exceptions import DoesNotExist


class BotUser(models.Model):
    bot_id = models.BigIntegerField()
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'BOT USER'
        verbose_name_plural = 'BOT USERS'


class AbsentStudents(models.Model):
    subject_schedule = models.IntegerField(default=None)
    group_id = models.IntegerField(default=None)
    group_name = models.CharField(max_length=250, default=None)
    group_language = models.CharField(max_length=250, default=None)
    subject_name = models.CharField(max_length=250, default=None)
    subject_id = models.IntegerField(default=None)
    subject_type = models.CharField(max_length=250, default=None)
    subject_date = models.CharField(max_length=250, default=None)
    subject_date_tmp = models.IntegerField(default=None)
    student_id = models.IntegerField(default=None)
    student_name = models.CharField(max_length=250, default=None)
    employee_id = models.IntegerField(default=None)
    employee_name = models.CharField(max_length=250, default=None)
    education_year = models.CharField(max_length=250, default=None)
    semester = models.CharField(max_length=250, default=None)
    lesson_pair_id = models.IntegerField(default=None)
    lesson_pair = models.CharField(max_length=250, default=None)
    absent_off = models.IntegerField(default=None)

    class Meta:
        verbose_name = 'ABSENT STUDENTS'
        verbose_name_plural = 'ABSENT STUDENTS'


class Schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    subject_id = models.IntegerField(default=None, null=True, blank=True)
    subject_name = models.CharField(max_length=250, default=None)
    subject_type = models.CharField(max_length=250, default=None)
    subject_date = models.CharField(max_length=250, default=None)
    subject_date_tmp = models.IntegerField(default=None)
    semester = models.CharField(max_length=250, default=None)
    education_year = models.CharField(max_length=250, default=None)
    group_id = models.IntegerField(default=None, null=True, blank=True)
    group_name = models.CharField(max_length=250, default=None)
    group_language = models.CharField(
        max_length=250, default=None, null=True, blank=True)
    lesson_pair_id = models.IntegerField(default=None, null=True, blank=True)
    lesson_pair = models.CharField(
        max_length=250, default=None, null=True, blank=True)
    employee_id = models.IntegerField(default=None, null=True, blank=True)
    employee_name = models.CharField(max_length=250, default=None)
    faculty_id = models.IntegerField(default=None, null=True, blank=True)
    faculty_name = models.CharField(
        max_length=250, default=None, null=True, blank=True)
    department_id = models.IntegerField(default=None, null=True, blank=True)
    department_name = models.CharField(
        max_length=250, default=None, null=True, blank=True)
    department_parent_id = models.IntegerField(
        default=None, null=True, blank=True)
    building = models.CharField(
        max_length=250, default=None, null=True, blank=True)
    room = models.CharField(
        max_length=250, default=None, null=True, blank=True)
    checked = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'SCHEDULE'
        verbose_name_plural = 'SCHEDULES'


class ScheduleChecked(models.Model):
    id = models.IntegerField(primary_key=True)
    schedule = models.ForeignKey(Schedule, models.CASCADE)
    subject_name = models.CharField(max_length=250, default=None)
    subject_type = models.CharField(max_length=250, default=None)
    subject_date = models.CharField(max_length=250, default=None)
    subject_date_tmp = models.IntegerField(default=None)
    semester = models.CharField(max_length=250, default=None)
    education_year = models.CharField(max_length=250, default=None)
    group_name = models.CharField(max_length=250, default=None)
    lesson_pair = models.CharField(max_length=250, default=None)
    employee_name = models.CharField(max_length=250, default=None)

    def save(self, *args, **kwargs):
        try:
            self.schedule.checked = True
            self.schedule.save()
            print("Saving schedule", self.schedule.id)
        except Schedule.DoesNotExist:
            # print(f"{self.schedule.id} - Schedule does not exist")
            Schedule.objects.create(
                id=self.schedule_id,
                subject_name=self.subject_name,
                subject_type=self.subject_type,
                subject_date=self.subject_date,
                subject_date_tmp=self.subject_date_tmp,
                semester=self.semester,
                education_year=self.education_year,
                group_name=self.group_name,
                lesson_pair=self.lesson_pair,
                employee_name=self.employee_name,
                checked=True)

        return super().save(*args, **kwargs)

        # if not created:
        #     # Handle potential case where Schedule doesn't exist
        #     Schedule.objects.create(
        #         id=self.schedule.id,
        #         subject_name= self.subject_name,
        #         subject_type= self.subject_type,
        #         subject_date= self.subject_date,
        #         subject_date_tmp= self.subject_date_tmp,
        #         semester= self.semester,
        #         education_year= self.education_year,
        #         group_name= self.group_name,
        #         lesson_pair= self.lesson_pair,
        #         employee_name= self.employee_name,
        #         checked= True
        #         )

    class Meta:
        verbose_name = 'CHECKED SCHEDULE'
        verbose_name_plural = 'CHECKED SCHEDULES'
