from rest_framework import serializers
from user.models import User, Student, Teacher, Admin, StudentGroup
from rest_framework.response import Response

class StudentCreateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only = True, source='user.password')
    gender = serializers.CharField(source = 'user.gender')
    birthday = serializers.DateField(source = 'user.birthday')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    email = serializers.CharField(source = 'user.email')
    phone = serializers.CharField(source = 'user.phone')
    name = serializers.CharField(source = 'studentgroup.name')

    class Meta:
        model = Student
        fields = ('username', 'password', 'gender', 'birthday', 'first_name', 'last_name', 'email', 'phone','name')

    def create(self, validated_data):
        user = validated_data.pop('user')
        users = User.objects.create(username=user['username'], first_name = user['first_name'],
            email = user['email'], gender= user['gender'],   birthday = user['birthday'],
            last_name = user['last_name'],  phone = user['phone']
        )
        users.set_password(user['password'])
        users.has_profile_true()
        users.save()
        student = Student(**validated_data)

        student.user = users
        student.save()
        group = StudentGroup.objects.filter(id = validated_data['studentgroup']['name'])[0]
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
        if user.get('username'):
            instance.user.username = user['username']
            instance.user.save()
        if user.get('password'):
            instance.user.set_password(user['password'])
            instance.user.save()
        if user.get('gender'):
            instance.user.gender = user['gender']
            instance.user.save()
        if user.get('birthday'):
            instance.user.birthday = user['birthday']
            instance.user.save()
        if user.get('first_name'):
            instance.user.firts_name = user['first_name']
            instance.user.save()
        if user.get('last_name'):
            instance.user.last_name = user['last_name']
            instance.user.save()
        if user.get('email'):
            instance.user.email = user['email']
            instance.user.save()
        if user.get('phone'):
            instance.user.phone = user['phone']
            instance.user.save()
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
        users = User.objects.create(
            username = user['username'],
            gender = user['gender'],
            birthday = user['birthday'],
            first_name = user['first_name'],
            last_name = user['last_name'],
            email = user['email'],
            phone = user['phone'],
            )
        
        users.set_password(user['password'])
        users.has_profile_true()
        users.save()

        teacher = Teacher(**validated_data)
        teacher.user = user
        teacher.save()

        return teacher

    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        if user.get('username'):
            instance.user.username = user['username']
            instance.user.save()
        if user.get('password'):
            instance.user.set_password(user['password'])
            instance.user.save()
        if user.get('gender'):
            instance.user.gender = user['gender']
            instance.user.save()
        if user.get('birthday'):
            instance.user.birthday = user['birthday']
            instance.user.save()
        if user.get('first_name'):
            instance.user.firts_name = user['first_name']
            instance.user.save()
        if user.get('last_name'):
            instance.user.last_name = user['last_name']
            instance.user.save()
        if user.get('email'):
            instance.user.email = user['email']
            instance.user.save()
        if user.get('phone'):
            instance.user.phone = user['phone']
            instance.user.save()
        return instance


