from rest_framework.serializers import ModelSerializer

from user.models import MatrixRequest

class MatrixRequestSerializer(ModelSerializer):
  class Meta:
    fields = '__all__'
    model = MatrixRequest
    extra_kwargs = {
      'user': {'write_only': True}
    }