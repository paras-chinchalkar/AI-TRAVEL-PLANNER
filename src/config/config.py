import os
from dotenv import load_dotenv

# Load local .env when present
load_dotenv()

# Prefer environment variable, but when running on Streamlit Cloud users often
# store secrets in `st.secrets`. Try to read from environment first, then
# gracefully fall back to Streamlit secrets (if available).
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
try:
	if not GROQ_API_KEY:
		import streamlit as _st

		# _st.secrets behaves like a dict; use .get to avoid KeyError
		GROQ_API_KEY = _st.secrets.get("GROQ_API_KEY")
except Exception:
	# If Streamlit isn't available (e.g., during tests or import-time on CI),
	# just ignore — the code that needs the key will handle a missing value.
	pass

