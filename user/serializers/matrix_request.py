from rest_framework.serializers import ModelSerializer

from user.models import MatrixRequest

class MatrixRequestSerializer(ModelSerializer):
  class Meta:
    fields = '__all__'
    model = MatrixRequest
    
  def to_representation(self, instance):
    r = super().to_representation(instance)
    r.pop('user')
    return r