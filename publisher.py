import json

from google.cloud import pubsub_v1

from config import app_config
from log import logger


def publish_message(message, project_id=app_config.GCP_PROJECT_ID,
                    topic_id=app_config.PUBSUB_TOPIC_ID):
    if app_config.TEST_ENV:
        logger.info(f"Skip publish message, this is test env, message: {message}")
        return

    # Initialize a PublisherClient
    publisher = pubsub_v1.PublisherClient()

    # Create the topic path
    topic_path = publisher.topic_path(project_id, topic_id)

    # Convert the message to bytes
    message_str = json.dumps(message)
    message_bytes = message_str.encode("utf-8")

    # Publish the message
    future = publisher.publish(topic_path, data=message_bytes)
    message_id = future.result()

    logger.info(f"Message published with ID: {message_id}, message: {message}")


if __name__ == "__main__":
    publish_message(app_config.GCP_PROJECT_ID, app_config.PUBSUB_TOPIC_ID, "test")
