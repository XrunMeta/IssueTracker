# Created by: Diaz Reza
import os
import sys
import requests
import json
from urllib.parse import urljoin

API_BASE_URL = "http://127.0.0.1:9988"
TTS_ENDPOINT = f"{API_BASE_URL}/tts"
UPLOAD_ENDPOINT = f"{API_BASE_URL}/upload"
OUTPUT_DIR = "output"

SUPPORTED_LANGUAGES = {
    "chinese": "zh-cn", "zh-cn": "zh-cn",
    "english": "en", "en": "en",
    "japanese": "ja", "ja": "ja",
    "korean": "ko", "ko": "ko",
    "spanish": "es", "es": "es",
    "german": "de", "de": "de",
    "french": "fr", "fr": "fr",
    "italian": "it", "it": "it",
    "turkish": "tr", "tr": "tr",
    "russian": "ru", "ru": "ru",
    "portuguese": "pt", "pt": "pt",
    "polish": "pl", "pl": "pl",
    "dutch": "nl", "nl": "nl",
    "arabic": "ar", "ar": "ar",
    "hungarian": "hu", "hu": "hu",
    "czech": "cs", "cs": "cs"
}

def normalize_language(lang):
    lang_key = lang.strip().lower()
    if lang_key not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language '{lang}'. Supported: {', '.join(SUPPORTED_LANGUAGES)}")
    return SUPPORTED_LANGUAGES[lang_key]

def upload_voice_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Voice file not found: {filepath}")
    with open(filepath, "rb") as f:
        response = requests.post(UPLOAD_ENDPOINT, files={"audio": f})
    data = response.json()
    if data["code"] != 0:
        raise RuntimeError(f"Failed to upload file: {data.get('msg')}")
    return data["data"]

def get_next_filename(base_name: str, extension: str = ".wav"):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    i = 1
    while True:
        filename = f"{base_name}_{i}{extension}"
        path = os.path.join(OUTPUT_DIR, filename)
        if not os.path.exists(path):
            return path

def synthesize(text, language, speed, voice, model=""):
    try:
        lang_code = normalize_language(language)
    except ValueError as e:
        print(str(e))
        return

    if os.path.isfile(voice):
        print(f"Uploading voice file: {voice}")
        voice = upload_voice_file(voice)

    data = {
        "text": text,
        "language": lang_code,
        "speed": speed,
        "voice": voice,
        "model": model
    }

    print(f"Requesting synthesis: {data}")
    response = requests.post(TTS_ENDPOINT, data=data)
    if response.status_code != 200:
        print("Error: Failed to call API.")
        print(response.text)
        return

    result = response.json()
    if result.get("code") != 0:
        print(f"Error from API: {result.get('msg')}")
        return

    audio_file = os.path.abspath(result["filename"])  # Ensures full path
    suffix_path = get_next_filename("voice_clone")
    try:
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Output file not found: {audio_file}")
        with open(audio_file, "rb") as f_in, open(suffix_path, "wb") as f_out:
            f_out.write(f_in.read())
        print(f"✅ Audio saved to: {suffix_path}")
    except Exception as e:
        print(f"❌ Failed to save audio: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python clone_api.py <text> <language> <speed> <voice_wav_or_model> [model]")
        sys.exit(1)

    text = sys.argv[1]
    language = sys.argv[2]
    speed = float(sys.argv[3])
    voice = sys.argv[4]
    model = sys.argv[5] if len(sys.argv) > 5 else ""

    synthesize(text, language, speed, voice, model)
