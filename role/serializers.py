from rest_framework import serializers
from role.models import Role  # Asegúrate de importar el modelo Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'description']  # Añade otros campos si son necesarios