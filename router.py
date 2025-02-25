from fastapi import HTTPException, UploadFile, File, APIRouter, Form
from research_summarizer import research_paper_summarizer_pdf, research_paper_summarizer_web

router = APIRouter()

@router.post("/Research_paper_summarizer_pdf")
def summarizer(file: UploadFile = File(...)):
    try:
        print("Inside Router")
        response=research_paper_summarizer_pdf(file)
        print("response", response)
        return response
    except Exception as e:
        print("failed at research_paper_summarizer_pdfrouter")
        print(str(e))
        raise HTTPException(**e.__dict__)
    
@router.post("/Research_paper_summarizer_web")
def summarizer(sitelink: str = Form(...)):
    try:
        print("Inside Router")
        response=research_paper_summarizer_web(sitelink)
        print("response", response)
        return response
    except Exception as e:
        print("failed at research_paper_summarizer_webrouter")
        print(str(e))
        raise HTTPException(**e.__dict__)