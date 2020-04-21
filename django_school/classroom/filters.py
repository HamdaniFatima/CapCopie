import django_filters
from classroom.models import Quiz, Profile, Student, Capteur

class CasesFilter (django_filters.FilterSet):
    class Meta:
        model = Quiz
        fields = [ 'subject',]



class ExpertsFilter (django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['interests']






class CapteurFilter (django_filters.FilterSet):
    class Meta:
        model = Capteur
        fields = [ 'type_evt',]
