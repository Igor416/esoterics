from rest_framework.serializers import ModelSerializer

from user.models import MatrixRequest

class MatrixRequestSerializer(ModelSerializer):
  class Meta:
    exclude = ['user']
    model = MatrixRequest