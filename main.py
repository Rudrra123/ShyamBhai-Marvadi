from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from models import FormRequest
from pdf_generator import create_pdf
from excel_generator import create_excel
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# ===== CORS =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== Serve Static UI =====
# Make sure your HTML file is inside: static/index.html
app.mount("/", StaticFiles(directory="Static", html=True), name="static")


# ===== PDF API =====
@app.post("/pdf")
def pdf(req: FormRequest):

    create_pdf(
        rows=req.rows,
        total=req.total,
        header=req.header
    )

    return FileResponse(
        "output.pdf",
        media_type="application/pdf",
        filename="measurement.pdf"
    )


# ===== EXCEL API =====
@app.post("/excel")
def excel(req: FormRequest):

    create_excel(req.rows, req.total)

    return FileResponse(
        "output.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="measurement.xlsx"
    )
