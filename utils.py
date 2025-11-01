import requests
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

def play_audio_from_url(url: str):
    """
    ✅ Download and play audio directly from OrangeCarrier live call link.
    Supports both .wav and .mp3.
    """
    try:
        print(f"🎧 Fetching audio from: {url}")
        response = requests.get(url, timeout=15)

        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            # Determine format automatically
            if 'wav' in content_type or url.endswith('.wav'):
                fmt = 'wav'
            elif 'mpeg' in content_type or url.endswith('.mp3'):
                fmt = 'mp3'
            else:
                fmt = 'wav'  # fallback format

            # Convert and play audio
            audio = AudioSegment.from_file(BytesIO(response.content), format=fmt)
            print("▶️ Playing audio now...")
            play(audio)
        else:
            print(f"❌ Failed to fetch audio. HTTP {response.status_code}")

    except Exception as e:
        print(f"⚠️ Error playing audio: {e}")
