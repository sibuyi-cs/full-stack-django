from django.contrib import admin
from .models import Topics,Article,Comment

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('id','pk')
    list_display=('tittle','topic','created_at')

class TopicsAdmin(admin.ModelAdmin):
    readonly_fields=('id','pk')
class CommentAdmin(admin.ModelAdmin):
    list_display=('author','post','text')


admin.site.register(Topics,TopicsAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)