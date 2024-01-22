from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "get_organizations",
        "date",
        "image",
    )
    readonly_fields = ("image_preview",)

    def get_organizations(self, obj):
        return " | \n".join(
            [organization.title for organization in obj.organizations.all()]
        )
