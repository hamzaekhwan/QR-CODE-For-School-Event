from rest_framework import serializers



from .models import *


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = "__all__"