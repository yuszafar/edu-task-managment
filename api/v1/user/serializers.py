from rest_framework import serializers
from users.models import User, Student, Teacher, Admin, StudentGroup


class StudentCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only = True, source='user.password')
    gender = serializers.CharField(source = 'user.gender')
    birthday = serializers.DateField(source = 'user.birthday')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    email = serializers.CharField(source = 'user.email')
    phone = serializers.CharField(source = 'user.phone')
    class Meta:
        model = Student
        fields = ('username', 'password', 'gender', 'birthday', 'first_name', 'last_name', 'email', 'phone')

    def create(self, validated_data):
        user = validated_data.pop('user')
        user = User.objects.create(username=user['username'], first_name = user['first_name'],
            email = user['email'], gender= user['gender'],   birthday = user['birthday'],
            last_name = user['last_name'],  phone = user['phone']
        )
        user.set_password('password')
        user.has_profile_true()
        user.save()
        student = Student(**validated_data)
        student.user = user
        student.save()
        return student

class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class StudentGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('name', 'owner', 'description',)
    
    def create(self, validated_data):
        group = StudentGroup(**validated_data)
        group.status = True
        group.save()

        return group

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
        user = User.objects.create(
            username = user['username'],
            gender = user['gender'],
            birthday = user['birthday'],
            first_name = user['first_name'],
            last_name = user['last_name'],
            email = user['email'],
            phone = user['phone'],
            )
        
        user.set_password('password')
        user.has_profile_true()
        user.save()

        teacher = Teacher(**validated_data)
        teacher.user = user
        teacher.save()

        return teacher
