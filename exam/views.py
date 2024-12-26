from django.shortcuts import render
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.exceptions import NotFound
from rest_framework.mixins import *
from rest_framework.permissions import IsAuthenticated




class ExamViewset(ModelViewSet):
    serializer_class = ExamSerializer

    def get_queryset(self):
        queryset = Exam.objects.all()
        level = self.request.query_params.get('level')
        if  level is not None :
            queryset =  Exam.objects.filter(level__iexact=level)

        return queryset
    
    
class RiviewViewset(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        exam_pk = self.kwargs['exam_pk']
        if exam_pk:
           if not Exam.objects.filter(pk=exam_pk).exists():
                raise NotFound(f"Exam with id {exam_pk} does not exist.")
           return Review.objects.filter(exam_id=exam_pk)
        return Review.objects.all()
    

class StudentViewset(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer
    
class QuestionViewset(ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        exam_id = self.kwargs['exam_pk']
        return Question.objects.filter(exam_id=exam_id)
    


# @api_view(['GET'])
# def exams_filters(request,level):
#     exam = Exam.objects.filter(level=level)
#     serializer = ExamSerializer(exam, many=True)
#     return Response(serializer.data)
    