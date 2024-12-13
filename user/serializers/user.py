from rest_framework.serializers import ModelSerializer

from user.models import User

class UserSerializer(ModelSerializer):
  class Meta:
    exclude = ['last_action']
    model = User
    
  def to_representation(self, instance):
    r = super().to_representation(instance)
    r['firstName'] = r.pop('first_name')
    r['lastName'] = r.pop('last_name')
    r.pop('language_code')
    r['referralLink'] = f'https://t.me/matrix_md_bot/main?startapp={instance.referral_link.id}' if hasattr(instance, 'referral_link') else None
    return r