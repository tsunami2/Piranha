# custom_components/fish_audio_wyoming/__init__.py

import logging
import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional("api_key"): cv.string,
        vol.Optional("host", default="127.0.0.1"): cv.string,
        vol.Optional("port", default=10200): cv.port,
    })
}, extra=vol.ALLOW_EXTRA)

def setup(hass: HomeAssistant, config: dict):
    """Set up the Fish Audio Wyoming TTS component."""
    hass.data[DOMAIN] = config.get(DOMAIN, {})
    _LOGGER.info("Fish Audio Wyoming TTS component loaded.")
    return True

def setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Fish Audio Wyoming TTS from a config entry."""
    hass.data[DOMAIN] = entry.data
    _LOGGER.info("Fish Audio Wyoming TTS configured through UI.")
    return True
