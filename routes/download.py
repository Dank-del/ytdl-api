from fastapi import APIRouter
import yt_dlp as youtube_dl

router = APIRouter()


@router.get("/video", tags=["download"])
async def download_video(video_url: str):
    ydl_opts = {
        "outtmpl": "%(id)s.%(ext)s", 
        "progress_hooks": [show_download_progress],
        "format": "bestvideo+bestaudio"
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(video_url, download=False)
        # ydl.download([video_url])

        # def iterFile():
        #     with open(ydl.prepare_filename(video_info), "rb") as f:
        #         yield from f
        # return responses.StreamingResponse(
        #     iterFile(), media_type="video/mp4"
        # )

@router.get("/ssyoutube", tags=["download"])
async def download_ss_youtube(video_url: str):
    import http.client
    import json
    conn = http.client.HTTPSConnection("ssyoutube.com")

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/json" 
    }
    
    
    payload = json.dumps({ "url": video_url })

    conn.request("POST", "/api/convert", payload, headersList) # type: ignore    
    response = conn.getresponse()
    result = response.read()
    return json.loads(result)


def show_download_progress(d):
    if d["status"] == "downloading":
        print(f"Download progress: {d['_percent_str']}")
