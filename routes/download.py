from fastapi import APIRouter
import yt_dlp as youtube_dl

router = APIRouter()


@router.get("/video", tags=["download"])
async def download_video(video_url: str):
    ydl_opts = {"outtmpl": "%(id)s.%(ext)s", "progress_hooks": [
        show_download_progress]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(video_url, download=False)
        # ydl.download([video_url])

        # def iterFile():
        #     with open(ydl.prepare_filename(video_info), "rb") as f:
        #         yield from f
        # return responses.StreamingResponse(
        #     iterFile(), media_type="video/mp4"
        # )


def show_download_progress(d):
    if d["status"] == "downloading":
        print(f"Download progress: {d['_percent_str']}")
