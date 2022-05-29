from .models import Job, Candidate, Skill
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.

class SkillSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Skill

class JobSerializer(serializers.ModelSerializer):
    skills = SkillSerilizer(read_only=True, many=True)
    class Meta:
        model = Job
        fields = ['id', 'title', 'skills']

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id','title', 'name']