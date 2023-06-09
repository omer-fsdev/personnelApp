from rest_framework import serializers
from .models import Department, Personnel


class DepartmentSerializer(serializers.ModelSerializer):
    personnel_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        # fields = "__all__"
        fields = ["id", "name", "personnel_count"]

    def get_personnel_count(self, obj):
        return obj.personnel.count()


from django.utils.timezone import now


class PersonnelSerializer(serializers.ModelSerializer):
    create_user_id = serializers.IntegerField(required=False)
    create_user = serializers.StringRelatedField()
    days_until_now = serializers.SerializerMethodField()

    class Meta:
        model = Personnel
        fields = "__all__"

    def create(self, validate_data):
        validate_data["create_user_id"] = self.context["request"].user.id
        instance = Personnel.objects.create(**validate_data)
        return instance

    def get_days_until_now(self, obj):
        return (now() - obj.start_date).days


class DepartmentPersonnelSerializer(serializers.ModelSerializer):
    personnel = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ["id", "name", "personnel"]

    def get_personnel(self, obj):
        personnel_queryset = obj.personnel.all()
        personnel_data = [
            {
                "id": personnel.id,
                "first_name": personnel.first_name,
                "last_name": personnel.last_name,
            }
            for personnel in personnel_queryset
        ]
        return personnel_data
