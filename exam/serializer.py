from .models import *
from rest_framework import serializers
from core.models import User  


class QuestionSerializer(serializers.ModelSerializer):
    correct_answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id','title','option_a','option_b','option_c','option_d','correct_answer']

    def get_correct_answer(self, obj):
        user = self.context['request'].user
        if user.is_staff:  
            return obj.correct_answer
        return None

class ExamSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True,read_only=True)
    class Meta:
        model = Exam
        fields = ['id','title','level','question']

class AnswerSwerilizer(serializers.ModelSerializer):
     class Meta:
        model = Answer
        fields = ['id','student','question','answer']
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','student','description',"date","exam"]

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Student
        fields = ['id','user', 'enrolling_date', 'grade']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract user data
        user = User.objects.create(**user_data)  # Create the User instance
        student = Student.objects.create(user=user, **validated_data)  # Create Student linked to User
        return student

