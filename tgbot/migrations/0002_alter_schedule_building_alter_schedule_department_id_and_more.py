# Generated by Django 5.0 on 2024-03-14 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='building',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='department_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='department_name',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='department_parent_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='employee_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='faculty_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='faculty_name',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='group_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='group_language',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='lesson_pair',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='lesson_pair_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='room',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='subject_date',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='subject_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
