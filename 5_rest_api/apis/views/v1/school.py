from rest_framework import viewsets
from django.db.models import Count, OuterRef, Subquery

from apis.models import School, Classroom, Teacher, Student
from apis.serializers import SchoolSerializer, ClassroomSerializer
from apis.filters import SchoolFilter, ClassroomFilter


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter

    def get_queryset(self):
        teacher_sq = Teacher.objects.filter(
            classrooms__school=OuterRef('pk')
        ).values('classrooms__school').annotate(
            count=Count('id', distinct=True)
        ).values('count')

        student_sq = Student.objects.filter(
            classroom__school=OuterRef('pk')
        ).values('classroom__school').annotate(
            count=Count('id')
        ).values('count')

        school_queryset = School.objects.all().annotate(
            classroom_count=Count('classrooms'),
            teacher_count=Subquery(teacher_sq),
            student_count=Subquery(student_sq)
        )
        return school_queryset



class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filterset_class = ClassroomFilter