from rest_framework import serializers
from user.models import User, Student, Teacher, Admin, StudentGroup
import datetime
class StudentCreateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only = True, source='user.password')
    gender = serializers.CharField(source = 'user.gender')
    birthday = serializers.DateField(source = 'user.birthday')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    email = serializers.CharField(source = 'user.email')
    phone = serializers.CharField(source = 'user.phone')
    group_id = serializers.IntegerField(source = 'studentgroup.id', label='id')

    class Meta:
        model = Student
        fields = ('username', 'password', 'gender', 'birthday', 'first_name', 'last_name', 'email', 'phone','group_id', 'education_start_date')

    def create(self, validated_data):
        user = validated_data.pop('user')
        users = User.objects.create(**user)
        users.set_password(user['password'])
        users.has_profile_true()
        users.save()
        student = Student(**validated_data)
        student.education_start_date = datetime.date.today()
        student.user = users
        student.save()
        group = StudentGroup.objects.filter(id = validated_data['studentgroup']['id'])[0]
        group.student.add(student.id)
        group.save()
        return student
    
class StudentUpdateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only = True, source='user.password')
    gender = serializers.CharField(source = 'user.gender')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    email = serializers.CharField(source = 'user.email')
    phone = serializers.CharField(source = 'user.phone')
    birthday = serializers.DateField(source = 'user.birthday')
    
    class Meta:
        model = Student
        fields = ('username', 'password', 'gender', 'birthday', 'first_name', 'last_name', 'email', 'phone')

    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        #for User Update
        for attr, value in user.items():
            setattr(instance.user, attr, value)
        if user.get('password'):
            instance.user.set_password(user['password'])
        #for Student Update
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.user.save()
        instance.save()

        return instance




class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class StudentGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('name', 'owner', 'description', 'student')

class StudentGroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'

class TeacherCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only = True, source='user.password')
    gender = serializers.CharField(source = 'user.gender')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    email = serializers.CharField(source = 'user.email')
    phone = serializers.CharField(source = 'user.phone')
    birthday = serializers.DateField(source = 'user.birthday')
    
    class Meta:
        model = Teacher
        fields = ('username', 'password', 'gender', 'birthday', 'first_name', 'last_name', 'email', 'phone')

    def create(self, validated_data):
        user = validated_data.pop('user')
        users = User.objects.create(**user)
        
        users.set_password(user['password'])
        users.has_profile_true()
        users.save()

        teacher = Teacher(**validated_data)
        teacher.user = users
        teacher.save()

        return teacher

    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        #for User Update
        for attr, value in user.items():
            setattr(instance.user, attr, value)
        if user.get('password'):
            instance.user.set_password(user['password'])
        #for Student Update
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.user.save()
        instance.save()

        return instance



