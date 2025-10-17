from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# ✅ permite conexiunea dintre frontend și backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔑 introduce cheia ta OpenAI
client = OpenAI(api_key="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")  # <-- înlocuiește cu cheia ta

class SymptomRequest(BaseModel):
    symptom: str

@app.post("/analyze")
async def analyze_symptom(data: SymptomRequest):
    prompt = f"""
    The user reports the following symptom: {data.symptom}.
    Provide 3 to 5 possible causes ranked from most to least likely.
    Answer in JSON like this:

    {{
      "summary": "short explanation",
      "possible_causes": [
        {{"condition": "Condition 1", "likelihood": "High"}},
        {{"condition": "Condition 2", "likelihood": "Medium"}}
      ]
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return {"result": response.choices[0].message.content}
