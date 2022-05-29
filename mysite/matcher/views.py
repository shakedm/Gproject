from django.shortcuts import render

# Create your views here.
from .serializers import Job, JobSerializer, CandidateSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (AllowAny,)

    @action(detail=True)
    def candidates(self, request, pk=None):
        job = self.get_object()
        candidates_pull = []
        for skill in job.skills.all():
            for candidate in skill.candidate_set.all():
                if candidate not in candidates_pull:
                    candidates_pull.append(candidate)

        return Response(CandidateSerializer(candidates_pull, many=True).data)