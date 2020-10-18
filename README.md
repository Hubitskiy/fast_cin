1. Run command docker-compose up --build
2. Add Package /app/core/db/migrations/ to PYTHONPATH - > export PYTHONPATH='/app/core/db/migrations': $PYTHONPATH
3. RUN migrations alembic upgrade head