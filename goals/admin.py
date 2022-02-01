from django.contrib import admin

from goals.models import Goal, GoalCategory, Board


class BoardAdmin(admin.ModelAdmin):
    list_display = ("title", "created")


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("board", "title", "user", "created", "updated")
    search_fields = ("title", "user")


class GoalAdmin(admin.ModelAdmin):
    list_display = ("category", "title", "user", "created", "updated")
    search_fields = ("title", "user")


admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Board, BoardAdmin)
