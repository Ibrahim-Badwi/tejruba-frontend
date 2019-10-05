from rest_framework import serializers

from .models import CustomUser, Settings


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('notify_when_reply', 'notify_when_comment')


class CustomUserSerializer(serializers.ModelSerializer):
    settings = SettingsSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 
                   'birth_date', 'bio', 'country','job', 'settings')
        read_only_fields = ('id', 'date_joined', 'last_login')