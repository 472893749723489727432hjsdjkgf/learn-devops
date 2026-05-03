import yt_dlp
import os
import asyncio
from fastapi import HTTPException, status

class ScClient:
    def __init__(self, url: str):
        self.url = url
        self.opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            
           
            'outtmpl': '../content/%(title)s.%(ext)s',
            

            'postprocessors': [
                {'key': 'FFmpegMetadata'},
                {'key': 'EmbedThumbnail'},
            ],
            
            'writethumbnail': True,
            'quiet': True,
            'no_warnings': True,
            
        }

    async def install_video(self) -> str:
        loop = asyncio.get_running_loop()

        def download():
            try: 
                with yt_dlp.YoutubeDL(self.opts) as ydl:
                    info = ydl.extract_info(self.url, download=False)
                    

                    file_path = ydl.prepare_filename(info)
                    
                    ydl.download([self.url])
                    
                    return file_path
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Ошибка при скачивании YouTube: {str(e)}"
                )

        print(f"Start video download: {self.url}")
        path = await loop.run_in_executor(None, download)
        print(f"Video ready: {path}")
        return path

