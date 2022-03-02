from django.contrib import admin
from django1.web.models import Todo, Category


@admin.register(Todo)
class ToDoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
