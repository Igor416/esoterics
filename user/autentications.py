from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import User

class MyJWTAuthentication(JWTAuthentication):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.user_model = User
    
  def get_user(self, validated_token):
    user = super().get_user(validated_token)
    user.is_authenticated = True
    return user