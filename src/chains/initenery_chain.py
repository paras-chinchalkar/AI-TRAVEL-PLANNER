from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

# Initialize the LLM
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

# Define the prompt template correctly
itenery_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a very helpful travel assistant. Create a trip itinerary for {city} based on the user's preferences: {interests}. Provide a brief, bulleted itinerary."),
    ("human", "Create an itinerary for my day trip!")
])

def generate_itinerary(city:str,intrests:str) -> str:
    response=llm.invoke(
        itenery_prompt.format_messages(city=city, interests=" , ".join(intrests))
    )
    return response.content