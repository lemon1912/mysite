#coding=utf-8
# Register your models here.

from django.contrib import admin
from  models import Question,Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets中每个元组的第一个元素是字段集的标题
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    #---------------------------------------------------------
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #添加Question的时候可以在同一个界面添加Choice
    inlines = [ChoiceInline]

    #fields = ['question_text','pub_date']
    # list_display = ('question_text','pub_date')

    #was_published_recently是自定义函数
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #添加搜索功能
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text','votes')



admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)