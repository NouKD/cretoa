from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from Action.action import Action

# Register your models here.

class ContactAdmin(Action):
    list_display = ('nom', 'email', 'tel','date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['date_add']
    list_per_page = 15
    fieldsets = [('Info Contact', {'fields': ['nom', 'email', 'tel', 'message']}),
                 ('Standard', {'fields': ['status']})
                 ]


class NewsLetterAdmin(Action):
    list_display = ('id', 'email', 'date_add', 'date_update', 'status')
    list_filter = ('id', )
    search_fields = ('email', )
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    ordering = ['id', 'email']
    list_per_page = 10
    fieldsets = [('Info NewsLetter', {'fields': ['email']}),
                 ('Standare', {'fields': ['status']})
                 ]

class SocialAccountAdmin(Action):
    list_display = ('nom', 'lien', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['lien']
    ordering = ['nom']
    list_per_page = 10

    fieldsets = [
        ('Info SocialAccount', {
            'fields': ['nom', 'lien', 'icon']
        }),
        ('Standare', {
            'fields': ['status']
        })
    ]


class SiteInfoAdmin(Action):
    list_display = ('image_view', 'tel', 'adresse', 'email', 'date_add','date_update', 'status')
    list_filter = ('email', )
    search_fields = ('email', )
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    ordering = ['email']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['email', 'tel', 'adresse', 'image', 'map_url']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def image_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.logo.url))


class PresentationAdmin(Action):
    list_display = ('images_view', 'titre', 'date_add','date_update', 'status')
    list_filter = ('titre', )
    search_fields = ('titre', )
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    fieldsets = [('Info Presentation', {'fields': ['titre', 'description', 'image']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class TeamAdmin(Action):
    list_display = ('images_view', 'titre', 'statu', 'date_add','date_update', 'status')
    list_filter = ('titre', )
    search_fields = ('titre', )
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    fieldsets = [('Info Presentation', {'fields': ['titre', 'statu', 'image']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
_register(models.NewsLetter, NewsLetterAdmin)
_register(models.SocialAccount, SocialAccountAdmin)
_register(models.Presentation, PresentationAdmin)
_register(models.SiteInfo, SiteInfoAdmin)
_register(models.Team, TeamAdmin)