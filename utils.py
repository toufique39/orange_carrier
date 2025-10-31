import requests
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

def play_audio_from_url(url: str):
    """Download and play audio from OrangeCarrier link"""
    try:
        print(f"🎧 Playing audio from: {url}")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            audio = AudioSegment.from_file(BytesIO(response.content), format="wav")
            play(audio)
        else:
            print("❌ Failed to fetch audio. Status:", response.status_code)
    except Exception as e:
        print("⚠️ Error playing audio:", e)
