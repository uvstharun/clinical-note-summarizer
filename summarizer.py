import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# -------------------------------------------------------
# STEP 1: DEFINE THE OUTPUT SCHEMA
# -------------------------------------------------------

class DischargeSummary(BaseModel):
    chief_complaint: str = Field(description="The primary reason for admission in one sentence")
    primary_diagnosis: str = Field(description="The main discharge diagnosis")
    all_diagnoses: list[str] = Field(description="All diagnoses listed at discharge")
    key_procedures: list[str] = Field(description="Major procedures performed during the stay")
    discharge_medications: list[str] = Field(description="Complete list of medications at discharge with doses")
    new_medications: list[str] = Field(description="Medications that were newly started during this admission")
    changed_medications: list[str] = Field(description="Medications whose dose or frequency was changed")
    follow_up: list[str] = Field(description="Follow-up appointments and referrals")
    hospital_days: int = Field(description="Total number of days in hospital")
    discharge_condition: str = Field(description="Patient condition at discharge")
    clinical_summary: str = Field(description="2-3 sentence plain English summary of the hospital course")

# -------------------------------------------------------
# STEP 2: SET UP LANGCHAIN COMPONENTS
# -------------------------------------------------------


llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    max_tokens=2048
)

# The output parser — automatically handles JSON parsing and Pydantic validation
parser = PydanticOutputParser(pydantic_object=DischargeSummary)

# The prompt template — {format_instructions} is automatically filled by the parser
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a clinical documentation specialist with expertise in 
reading and summarizing hospital discharge summaries.

Extract structured information from the discharge summary provided.
Be precise and complete. Do not add information not present in the note.
For medications include the full dose and frequency.
For diagnoses use the exact terms from the note.

{format_instructions}"""),
    ("human", "Please summarize this discharge summary:\n\n{note}")
])

# -------------------------------------------------------
# STEP 3: BUILD THE CHAIN
# -------------------------------------------------------

chain = prompt | llm | parser


# -------------------------------------------------------
# STEP 4: THE SUMMARIZER FUNCTION
# -------------------------------------------------------

def summarize_note(discharge_note: str) -> DischargeSummary:
    """Take a discharge summary and return structured data."""
    result = chain.invoke({
        "note": discharge_note,
        "format_instructions": parser.get_format_instructions()
    })
    return result

