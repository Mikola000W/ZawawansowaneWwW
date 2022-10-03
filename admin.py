from django.contrib import admin

from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date','question_text']

class AnswerAdmin(admin.ModelAdmin):
    fields = ['answer_text','question']
    def get_answer(self,obj):
        return obj.answer.answer_text
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
