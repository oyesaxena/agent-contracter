from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

    
    GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY"
    )

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "gemini-2.5-flash"
    )

    CONFIDENCE_THRESHOLD = float(
        os.getenv(
            "CONFIDENCE_THRESHOLD",
            0.8
        )
    )

settings = Settings()