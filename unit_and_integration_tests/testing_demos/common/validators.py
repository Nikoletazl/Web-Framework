from django.core.exceptions import ValidationError


def validate_only_letters(value):
    invalid_chars = [ch for ch in value if not ch.isalpha]
    if invalid_chars:
        raise ValidationError(f'Value must contain only letters, but contains: {invalid_chars}')
