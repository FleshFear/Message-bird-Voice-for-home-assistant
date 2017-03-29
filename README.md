# Message-bird-Voice-for-home-assistant

This is a custom component for home assistant, modified from the original component for message bird. This will add the ability to make voice messages to your phone. Calling you with the predefiende message.

## Installation

follow the setup from the original [message bird component](https://home-assistant.io/components/notify.message_bird/) for home assistant.

Download the message_bird_custom.py and put in your custom component folder
```
custom_components/notify
```

And add the configuration into your configuration.yaml
```
# Example configuration.yaml entry
notify:
  - name: NOTIFIER_NAME
    platform: message_bird_custom
    api_key: YOUR_API_KEY
```

Configuration variables:

- **api_key** (Required): Enter the API key for MessageBird. Go to https://www.messagebird.com/ to retrieve your API key.

- **name** (Optional): Setting the optional parameter name allows multiple notifiers to be created. The default value is notify. The notifier will bind to the service notify.NOTIFIER_NAME.

- **sender** (Optional): Setting the optional parameter sender. This will be the sender of the SMS. It may be either a telephone number (e.g. +4915112345678) or a text with a maximum length of 11 characters. Defaults to HA.

- **method** (Optional): Setting the optional parameter method, will change langauge of the message spoken in the call, only need in voice calls. Supported langauges: nl-nl, de-de, en-gb, en-us, es-es, fr-fr, ru-ru, zh-cn, en-au, es-mx, es-us, fr-ca, is-is, it-it, ja-jp, ko-kr, pl-pl, pt-br, ro-ro. Default is en-gb.

- **customize** (Optional): Setting the optional parameter method, will set the gender of the voice calling. Possible options is male, or female. Default is female

## Usage

MessageBird is a notify platform and thus can be controlled by calling the notify service [as described here](https://home-assistant.io/components/notify/). It will send a notification to the specified mobile phone number(s).

```
{
  "message": "A message for many people",
  "title": "voice",
  "target": [ "+49123456789", "+43123456789" ]
}
```

- **title** (Optional): Setting the title to voice, will send you'r message as a text-to-speach phone call to the specified targets. The default is nothing and will send as a text.
