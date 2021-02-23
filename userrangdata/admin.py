# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from . import models


class UserRankResource(resources.ModelResource):
    class Meta:
        model = models.UserRank
        fields = (
                    'rank',
                    'name',
                    'user_url',
                    'network',
                    'last',
                    'trades',
                    'total_return',
                )

class UserRankAdmin(ImportExportModelAdmin):

    list_display = (
        'rank',
        'name',
        'user_url',
        'network',
        'last',
        'trades',
        'total_return',
    )
    resource_class = UserRankResource

    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.UserRank, UserRankAdmin)
