from django.shortcuts import render
from django.http import HttpResponse
from .models import JobPost, Category,Company
from rest_framework import generics, viewsets
from .serializers import JobPostSerializer




def job_list(request):
    jobposts = JobPost.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'jobposts':jobposts,
        'title':'Job List',
        'categories':categories,
    }
    return render(request,template_name = 'jobpost/index.html',context=context)

def job_category(request,category_id):
    jobposts = JobPost.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request,'jobpost/category.html',{'jobposts':jobposts,'categories':categories, 'category':category})

def companies_list(request):
    company_name = Company.objects.all()
    context = {
        'company_name':company_name,

    }

class JobPostViewSet(viewsets.ModelViewSet):
   queryset = JobPost.objects.all()
   serializer_class = JobPostSerializer

class JobPostAPIView(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobPostAPIUpdate(generics.UpdateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobPostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
