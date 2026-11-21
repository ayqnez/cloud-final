"""Password policy checker, used by the security checks of the project."""

import string

# fmt: off
COMMON_PASSWORDS = {
    "password", "password1", "password123", "123456", "12345678", "123456789",
    "qwerty", "qwerty123", "admin", "admin123", "letmein", "welcome", "welcome1",
    "iloveyou", "monkey", "dragon", "football", "abc123", "111111", "postgres",
    "mysql", "root", "changeme", "secret", "passw0rd", "p@ssw0rd", "narxoz",
}
# fmt: on


def check_password(password: str, min_length: int = 14, require_symbol: bool = False) -> dict:
    rules = {
        "min_length": len(password) >= min_length,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "not_common": password.lower() not in COMMON_PASSWORDS,
    }
    meets_base_rules = all(rules.values())
    rules["has_symbol"] = any(c in string.punctuation for c in password)
    return {
        "ok": meets_base_rules and (not require_symbol or rules["has_symbol"]),
        "min_length": min_length,
        "require_symbol": require_symbol,
        "rules": rules,
    }
