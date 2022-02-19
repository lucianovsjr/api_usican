from rest_framework import serializers


class BaseRegisterSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        if not data["active"] and not self.instance.active:
            raise serializers.ValidationError(
                {"message": f"usican.error.{self.instance.get_model()}.active_is_false"}
            )

        return data
