from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from summarizer import summarize_note, DischargeSummary

load_dotenv()

app = FastAPI(title="Clinical Note Summarizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------
# REQUEST MODEL
# -------------------------------------------------------

class NoteRequest(BaseModel):
    note: str

# -------------------------------------------------------
# CACHE
# -------------------------------------------------------

summary_cache = {}

# -------------------------------------------------------
# ENDPOINTS
# -------------------------------------------------------

@app.get("/")
def root():
    return {"status": "Clinical Note Summarizer API is running"}


@app.post("/summarize", response_model=DischargeSummary)
def summarize(request: NoteRequest):
    # Use first 100 chars as cache key
    cache_key = request.note[:100]

    if cache_key in summary_cache:
        print("Cache hit")
        return summary_cache[cache_key]

    result = summarize_note(request.note)
    summary_cache[cache_key] = result
    return result