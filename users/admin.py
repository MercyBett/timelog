from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()




class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'password')
    list_display_links = ('id', 'name', 'email', 'password')
    search_fields = ('name', 'email',)
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
      email=obj.email
      obj.delete()


    def get_queryset(self, request):
        return super().get_queryset(request)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request,  **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request,  **kwargs)


admin.site.register(User,UserAdmin)

