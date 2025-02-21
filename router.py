from fastapi import HTTPException, UploadFile, File, APIRouter
from research_summarizer import research_paper_summarizer

router = APIRouter()

@router.post("/Research_paper_summarizer")
def summarizer(file: UploadFile = File(...)):
    try:
        print("Inside Router")
        response=research_paper_summarizer(file)
        print("response", response)
        return response
    except Exception as e:
        print("failed at research_paper_summarizer")
        print(str(e))
        raise HTTPException(**e.__dict__)