import os
from fastapi import APIRouter, HTTPException
from app.services.scraper import WebScraper
from app.services.processor import TextAnalyzer
from app.models.request import ScrapeRequest
from app.models.response import AnalysisResponse


router = APIRouter()

@router.post("/analyze/", response_model=AnalysisResponse)
async def analyze_text(scrape_request: ScrapeRequest):
    try:
        scraper = WebScraper(scrape_request.url)
        article_text = scraper.extract_article_text()

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        stopwords_dir = os.path.join(BASE_DIR,'assets', 'StopWords')
        master_dict_dir = os.path.join(BASE_DIR,'assets', 'MasterDictionary')
        analyzer = TextAnalyzer(stopwords_dir, master_dict_dir)
        analysis_result = analyzer.analyze_text(article_text)

        return AnalysisResponse(**analysis_result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
