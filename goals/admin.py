from django.contrib import admin

from goals.models import Goal, GoalCategory


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated')


class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated')



admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(Goal, GoalAdmin)
