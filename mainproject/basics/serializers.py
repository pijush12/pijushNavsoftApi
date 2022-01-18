from rest_framework import serializers
from basics.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('StudentId','StudentName','Roll','Department')