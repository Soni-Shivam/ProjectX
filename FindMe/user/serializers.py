from rest_framework import serializers
from .models import CustomUser

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    skills_offered = SkillSerializer(many=True, read_only=True)
    skills_wanted = SkillSerializer(many=True, read_only=True)

    skills_offered_ids = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True, write_only=True, required=False
    )
    skills_wanted_ids = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = CustomUser
        fields = (
            'id', 'email', 'name', 'bio',
            'skills_offered', 'skills_wanted',
            'skills_offered_ids', 'skills_wanted_ids',
            'availability', 'location', 'profile_photo', 'is_private'
        )

    def update(self, instance, validated_data):
        offered_ids = validated_data.pop('skills_offered_ids', None)
        wanted_ids = validated_data.pop('skills_wanted_ids', None)

        instance = super().update(instance, validated_data)

        if offered_ids is not None:
            instance.skills_offered.set(offered_ids)
        if wanted_ids is not None:
            instance.skills_wanted.set(wanted_ids)

        return instance
