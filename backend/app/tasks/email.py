import logging

from app.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(name="tasks.send_email")
def send_email(to_email: str, subject: str, body: str) -> dict[str, str]:
    logger.info(
        "send_email task received",
        extra={
            "to_email": to_email,
            "subject": subject,
        },
    )
    return {"status": "queued", "to_email": to_email, "subject": subject}
