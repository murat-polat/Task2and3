from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Cafeteria Admin"
admin.site.site_title = "cafeteria Admin Area"

## Here we can add and manage new questions/choices in Django Admin site

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)