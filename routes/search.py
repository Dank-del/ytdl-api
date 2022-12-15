from fastapi import APIRouter
from youtube_search import YoutubeSearch
import typing

router = APIRouter()

@router.get("/video", tags=["search"])
async def search_video(search_terms: str, max_results: typing.Optional[int] = None) -> YoutubeSearch:
    return YoutubeSearch(search_terms, max_results=max_results)