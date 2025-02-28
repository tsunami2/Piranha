# custom_components/fish_audio_wyoming/config_flow.py

import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class FishAudioConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Fish Audio Wyoming TTS."""

    VERSION = 1
    
    async def async_step_user(self, user_input=None):
        """Handle the initial step where users enter API key and voice model ID."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title="Fish Audio Wyoming TTS", data=user_input)

        data_schema = vol.Schema({
            vol.Required("api_key"): str,
            vol.Required("voice_model_id"): str,
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)
