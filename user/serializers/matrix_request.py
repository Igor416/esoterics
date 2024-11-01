from rest_framework.serializers import ModelSerializer

from user.models import MatrixRequest

class MatrixRequestSerializer(ModelSerializer):
  class Meta:
    fields = '__all__'
    model = MatrixRequest
    
  def to_representation(self, instance):
    r = super().to_representation(instance)
    if instance.paired:
      r['paired'] = super().to_representation(MatrixRequest.objects.get(id=instance.paired.id))
    r.pop('user')
    return r