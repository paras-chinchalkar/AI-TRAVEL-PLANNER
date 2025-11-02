from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY


# Prompt template (kept at module-level)
itenery_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a very helpful travel assistant. Create a trip itinerary for {city} based on the user's preferences: {interests}. Provide a brief, bulleted itinerary.",
    ),
    ("human", "Create an itinerary for my day trip!"),
])


def get_llm() -> ChatGroq:
    """Lazily construct and return a ChatGroq client.

    This avoids creating the client at import time (which fails in environments
    where GROQ_API_KEY isn't set). If the key is missing we raise a clear
    RuntimeError with instructions for the deploy environment.
    """
    if not GROQ_API_KEY:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Please set the GROQ_API_KEY environment variable or add it to your Streamlit secrets/.env."
        )

    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0.7,
    )


def generate_itinerary(city: str, intrests: list[str]) -> str:
    """Return a generated itinerary for `city` using user's `intrests`.

    The LLM is instantiated lazily so import-time failures are avoided.
    """
    llm = get_llm()
    # format the prompt messages and invoke the model
    response = llm.invoke(
        itenery_prompt.format_messages(city=city, interests=" , ".join(intrests))
    )
    return response.content