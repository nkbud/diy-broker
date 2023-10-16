import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    """
    event = {
      "a": "John",
      "b": "Doe",
    }
    """
    logger.info("EVENT: " + event)
    
    return {
        "statusCode": 200,
        "headers"   : {
            "Content-Type": "application/json"
        },
        "body"      : json.dumps({
            "Message": ""
        })
    }

if __name__ == "__main__":
    pass
