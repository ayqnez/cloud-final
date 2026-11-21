"""Create the local Compose environment once, with independent random credentials."""

import secrets
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECRET_FIELDS = {"SECRET_KEY", "DB_PASSWORD", "POSTGRES_PASSWORD", "GRAFANA_ADMIN_PASSWORD"}


def random_credential() -> str:
    while True:
        value = secrets.token_urlsafe(48)
        if any(c.isupper() for c in value) and any(c.islower() for c in value) and any(c.isdigit() for c in value):
            return value


def main() -> None:
    template = (ROOT / ".env.example").read_text(encoding="utf-8").splitlines()
    lines = []
    for line in template:
        key, sep, _ = line.partition("=")
        lines.append(f"{key}={random_credential()}" if sep and key in SECRET_FIELDS else line)
    try:
        with (ROOT / ".env").open("x", encoding="utf-8") as env_file:
            env_file.write("\n".join(lines) + "\n")
    except FileExistsError:
        print("Using the existing .env.")
    else:
        print("Created .env for local development.")


if __name__ == "__main__":
    main()
