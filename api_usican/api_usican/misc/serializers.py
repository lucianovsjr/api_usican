from rest_framework import serializers


class BaseRegisterSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        if self.instance:
            if not data.get("active", False) and not self.instance.active:
                raise serializers.ValidationError(
                    {
                        "message": f"usican.error.{self.instance.get_model()}.active_is_false"
                    }
                )

        return data
