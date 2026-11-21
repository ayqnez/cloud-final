from app.security import check_password
from scripts import init_local


def test_local_database_passwords_and_existing_env(tmp_path, monkeypatch):
    monkeypatch.setattr(init_local, "ROOT", tmp_path)
    (tmp_path / ".env.example").write_text("DB_PASSWORD=\nPOSTGRES_PASSWORD=\n", encoding="utf-8")

    init_local.main()
    env_path = tmp_path / ".env"
    original = env_path.read_bytes()
    fields = dict(line.split("=", 1) for line in original.decode().splitlines())
    for key in ("DB_PASSWORD", "POSTGRES_PASSWORD"):
        assert check_password(fields[key], min_length=14, require_symbol=False)["ok"]
    assert fields["DB_PASSWORD"] != fields["POSTGRES_PASSWORD"]

    init_local.main()
    assert env_path.read_bytes() == original
