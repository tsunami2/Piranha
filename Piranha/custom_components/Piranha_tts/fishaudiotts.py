# custom_components/fish_audio_wyoming/fishaudiotts.py

import logging
from homeassistant.components.tts import Provider

_LOGGER = logging.getLogger(__name__)

FISH_AUDIO_API_URL = "https://api.fish.audio/tts"

class FishAudioTTSEngine(Provider):
    def __init__(self, hass, api_key, voice_model_id):
        """Initialize the Fish Audio TTS Engine."""
        self.hass = hass
        self.name = "FishAudioWyoming"
        self.supported_languages = ["en"]
        self.default_language = "en"
        self.supported_options = []
        self.api_key = api_key
        self.voice_model_id = voice_model_id

    def get_tts_audio(self, message, language, options=None):
        """Fetch TTS audio from Fish Audio API."""
        if not self.api_key or not self.voice_model_id:
            _LOGGER.error("API Key or Voice Model ID not configured!")
            return None, None

        payload = {
            "text": message,
            "voice_model_id": self.voice_model_id
        }
        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = requests.post(FISH_AUDIO_API_URL, json=payload, headers=headers)
        
        if response.status_code == 200:
            return "mp3", response.content
        else:
            _LOGGER.error("Failed to fetch TTS audio: %s", response.text)
            return None, None
