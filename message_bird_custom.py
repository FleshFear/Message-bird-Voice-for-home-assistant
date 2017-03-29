"""
MessageBird platform for notify component.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/notify.message_bird/
"""
import logging

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.notify import (
    ATTR_TARGET, ATTR_TITLE, PLATFORM_SCHEMA, BaseNotificationService)
from homeassistant.const import CONF_API_KEY, CONF_SENDER, CONF_METHOD, CONF_CUSTOMIZE

REQUIREMENTS = ['messagebird==1.2.0']

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Optional(CONF_SENDER, default='HA'):
        vol.All(cv.string, vol.Match(r"^(\+?[1-9]\d{1,14}|\w{1,11})$")),
    vol.Optional(CONF_METHOD, default='en-GB'),
    vol.Optional(CONF_CUSTOMIZE, default='female'):
        vol.All(cv.string, vol.Match(r"^(\+?[1-9]\d{1,14}|\w{1,11})$")),
})


# pylint: disable=unused-argument
def get_service(hass, config, discovery_info=None):
    """Get the MessageBird notification service."""
    import messagebird

    client = messagebird.Client(config[CONF_API_KEY])
    try:
        # validates the api key
        client.balance()
    except messagebird.client.ErrorException:
        _LOGGER.error('The specified MessageBird API key is invalid.')
        return None

    return MessageBirdNotificationService(config.get(CONF_SENDER), client, config.get(CONF_METHOD), config.get(CONF_CUSTOMIZE))


class MessageBirdNotificationService(BaseNotificationService):
    """Implement the notification service for MessageBird."""

    def __init__(self, sender, client, method, customize):
        """Initialize the service."""
        self.sender = sender
        self.client = client
        self.method = method
        self.customize = customize

    def send_message(self, message=None, **kwargs):
        """Send a message to a specified target."""
        from messagebird.client import ErrorException

        targets = kwargs.get(ATTR_TARGET)
        title = kwargs.get(ATTR_TITLE)
        if not targets:
            _LOGGER.error('No target specified.')
            return

        for target in targets:
            try:
                self.client.voice_message_create(self.sender,
                                           target,
                                           message,
                                           {'reference': 'HA'})
            except ErrorException as exception:
                _LOGGER.error('Failed to notify %s: %s', target, exception)
                continue
