from rest_framework import serializers

from companies.models import Employee, Task
from accounts.models import User, User_Groups, Group, Group_Permissions

from django.contrib.auth.models import Permission

class EmployeesSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'email'
        )

    def get_name(self,obj) -> any:
        return obj.user.name
    def get_email(self,obj) -> any:
        return obj.user.email
        
class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'email',
            'groups'
        )

    def get_name(self,obj) -> any:
        return obj.user.name
    def get_email(self,obj) -> any:
        return obj.user.email
    def get_groups(self,obj) -> None:
        groupsDb = User_Groups.objects.filter(user_id=obj.user.id).all()
        groupsData = []

        for group in groupsDb:
            groupsData.append({
                "id":group.group.id,
                "name":group.group.name
            })
        return groupsData
    
class GroupsSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'permissions'
        )

    def get_permissions(self,obj) -> list:
        groups = Group_Permissions.objects.filter(group_id=obj.id).all()
        permissions = []

        for group in groups:
            permissions.append({
                "id":group.permission.id,
                "label":group.permission.name,
                "codename":group.permission.codename
            })
        return permissions

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            'id',
            'name',
            'codename'
        )

class TasksSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'due_date',
            'created_at',
            'status'
        )

    def get_status(self,obj) -> any:
        return obj.status.name

class TaskSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    employee = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'due_date',
            'created_at',
            'status',
            'employee'
        )

    def get_status(self,obj) -> any:
        return obj.status.name
    def get_employee(self,obj) -> EmployeesSerializer:
        return EmployeesSerializer(obj.employee).data
    def update(self, instance, validated_data) -> any:
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.status_id = validated_data.get('status_id',instance.status_id)
        instance.employee_id = validated_data.get('employee_id',instance.employee_id)
        instance.due_date = validated_data.get('due_date',instance.due_date)
        
        instance.save()

        return instance