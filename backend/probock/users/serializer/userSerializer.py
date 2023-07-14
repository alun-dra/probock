from rest_framework import serializers
from users.models.user import User
from users.models.range import Range

class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Range
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    range_id = RangeSerializer()

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        # Verificar que los campos obligatorios no estén vacíos
        required_fields = ['name', 'last_name', 'email', 'password']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError(f"El campo {field} es obligatorio.")         

    def validate_email(self, value):
        # Validar que el email no esté en uso por otro usuario
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está en uso.")
        return value

    def validate_password(self, value):
        # Validar que la contraseña tenga al menos 4 caracteres
        if len(value) < 4:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return value
