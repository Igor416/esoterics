from rest_framework.serializers import ModelSerializer

from user.models import Master

class MasterSerializer(ModelSerializer):
  class Meta:
    exclude = ['user']
    model = Master
    
  def to_representation(self, instance):
    r = super().to_representation(instance)
    r['hours'] = list()
    for key in [*r.keys()]:
      if key.endswith('_hours'):
        val = r.pop(key)
        hours = []
        for el in val.split(','):
          if '-' in el:
            start, end = list(map(int, el.split('-')))
            hours.extend(range(start, end + 1))
          else:
            hours.append(int(el))
        r['hours'].append(hours)
    return r