from celery import Celery


app = Celery(
    'celery_tasks',
    broker="redis://fast_cin_redis:6379/0",
)
