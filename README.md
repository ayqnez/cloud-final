# Club events

Club events is Ayan Kassen's CSS4005 project. Each item is a club event with a title and description. An event can have an attachment, such as a poster or agenda. The local stack runs the course FastAPI application with PostgreSQL 17.6 and stores attachments in a Docker volume.

## Run locally

Install Docker with Compose and Python 3, then run these commands from the repository root.

```powershell
python scripts/init_local.py
docker compose up -d --build --wait
```

Open [Club events](http://127.0.0.1:8000/) or use the [interactive API](http://127.0.0.1:8000/docs) to create an event. The [readiness check](http://127.0.0.1:8000/readyz) checks both PostgreSQL and attachment storage. To create and read an event in PowerShell, run

```powershell
$event = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/items -ContentType application/json -Body '{"title":"Board Game Night","description":"A club meetup for new members."}'
Invoke-RestMethod "http://127.0.0.1:8000/api/items/$($event.id)"
```

The setup script generates separate credentials in the Git-ignored `.env` and preserves them on subsequent runs. The API connects as `app_rw`. PostgreSQL is reachable within the Compose network. To stop the project and retain events and attachments, run `docker compose down`. Start it again with `docker compose up -d --wait`. Change `APP_PORT` in `.env` if another application uses port 8000.

## Development

- `/info` reports the app name, owner, version and database engine.
- `/metrics` exposes Prometheus metrics. The optional `docker compose --profile monitoring up -d` starts the supplied Prometheus and Grafana configuration.
- `POST /api/admin/check-password` checks the configured local application policy. The minimum is 14 characters and a symbol is optional.
- To run the course tests in a Python virtual environment, install `requirements-dev.txt`, then run `python -m pytest -q` and `ruff check .`.

[Course template](https://github.com/weeebdev-edu/css4005-final-project) · [Assignment](https://weeebdev-edu.github.io/css4005/pdfs/final-project.pdf)
