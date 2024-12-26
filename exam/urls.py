from django.urls import path
from . import views
from    rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('exams',views.ExamViewset,basename='exams')
router.register('students',views.StudentViewset)


reviews_router = routers.NestedDefaultRouter(router,'exams',lookup='exam')
reviews_router.register('reviews',views.RiviewViewset,basename='exam-review')

questions_router = routers.NestedDefaultRouter(router,'exams',lookup='exam')
questions_router.register('questions',views.QuestionViewset,basename='exam-question')


urlpatterns = router.urls + reviews_router.urls + questions_router.urls