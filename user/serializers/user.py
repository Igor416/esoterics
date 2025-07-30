from rest_framework.serializers import ModelSerializer

from user.models import User

class UserSerializer(ModelSerializer):
  class Meta:
    exclude = ['last_action', 'language_code', 'created']
    model = User
    
  def to_representation(self, instance):
    r = super().to_representation(instance)
    r['firstName'] = r.pop('first_name')
    r['lastName'] = r.pop('last_name')
    return r