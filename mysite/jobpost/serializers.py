from rest_framework import serializers
from .models import JobPost



class JobPostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = JobPost
        #fields = ('jobtitle','jobdescription','category','company','user')
        fields = '__all__'