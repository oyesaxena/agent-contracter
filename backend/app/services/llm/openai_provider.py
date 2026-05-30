from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from app.core.config import settings

llm = ChatGoogleGenerativeAI(
    model=settings.MODEL_NAME,
    google_api_key=settings.GOOGLE_API_KEY,
    temperature=0
)