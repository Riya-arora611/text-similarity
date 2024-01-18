from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import numpy as np 
from fastapi.middleware.cors import CORSMiddleware
from src.utils import process_text
import uvicorn
import json
import datetime as dt

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "Text similarity API"

@app.post('/text-similarity')
async def process_text_similarity(request: Request):
    try:
        record_json = await request.json()

        if "text1" and "text2" in record_json:
            text1 = record_json["text1"]
            text2 = record_json["text2"]

            # Call the process_text function to compute similarity
            similarity_result = process_text(text1, text2)
            print("Text similarity result:", similarity_result)

            # Convert float32 to regular float
            similarity_result = float(similarity_result)

            # Return the result in dictionary format
            result_dict = {"similarity_score": similarity_result}
            return JSONResponse(result_dict)
        else:
            return JSONResponse({"error": "Missing 'text1' or 'text2' in the request data"})
    except Exception as e:
        return JSONResponse({"error": str(e)})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)