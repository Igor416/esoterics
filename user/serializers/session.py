from rest_framework.serializers import ModelSerializer

from user.models import Session

class SessionSerializer(ModelSerializer):
  class Meta:
    exclude = ['id']
    model = Session
    
  def to_representation(self, instance):
    r = super().to_representation(instance)
    r['id'] = str(instance.id)
    return r