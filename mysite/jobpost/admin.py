from django.contrib import admin
from .models import JobPost, Category, Company



class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id','jobtitle','created_at','category')
    list_display_links = ('id','jobtitle')
    search_fields = ('jobtitle','jobdescription')
    list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id','title')
    search_fields = ('title',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')
    list_display_links = ('id','company_name')
    search_fields = ('company_name',)

admin.site.register(JobPost,JobPostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Company,CompanyAdmin)