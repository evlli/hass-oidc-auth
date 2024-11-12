from aiohttp import web
from homeassistant.components.http import HomeAssistantView
from homeassistant.core import HomeAssistant, callback
import logging

_LOGGER = logging.getLogger(__name__)

@callback
def async_register_view(hass: HomeAssistant) -> None:
    """Make sure callback view is registered."""
    if not hass.data.get(DATA_VIEW_REGISTERED, False):
        hass.http.register_view(OAuth2AuthorizeCallbackView())  # type: ignore
        hass.data[DATA_VIEW_REGISTERED] = True


