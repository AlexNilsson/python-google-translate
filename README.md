# multitrans
Translate multiple strings to multiple languages wrapping the Google Translate service.

## Install
```
pip install multitrans
```

## Format
```python
from multitrans import translate

result = translate( strings, to_languages, from_language )
```

## Examples
```python
from multitrans import translate

# translate one string to one language
a = translate('en fin stol','en','sv')

# translate multiple strings to one language
b = translate(['en stol','två soffor','tre fönster'],['en'],'sv')

# translate multiple strings to multiple languages
c = translate(['stol','soffa','fönster'],['en','da'],'sv')

print(a)
# {'en': ['a nice chair']}
print(b)
# {'en': ['a chair', 'two sofas', 'three windows']}
print(c)
# {'en': ['chair', 'couch', 'window'], 'da': ['stol', 'sofa', 'vindue']}
```

## Languages
Languages are represented by its two-char-code according to ISO 639-1\
A full list of all codes can be found here: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

Some examples follow below:

```
locales = {
  'af': 'Afrikaans',
  'ar': 'Arabic',
  'az': 'Azerbaijani',
  'be': 'Belarusian',
  'bg': 'Bulgarian',
  'bn': 'Bengali',
  'bs': 'Bosnian',
  'ca': 'Catalan',
  'ceb': 'Cebuano',
  'cs': 'Czech',
  'cy': 'Welsh',
  'da': 'Danish',
  'de': 'German',
  'el': 'Greek',
  'en': 'English',
  'eo': 'Esperanto',
  'es': 'Spanish',
  'et': 'Estonian',
  'eu': 'Basque',
  'fa': 'Persian',
  'fi': 'Finnish',
  'fr': 'French',
  'ga': 'Irish',
  'gl': 'Galician',
  'gu': 'Gujarati',
  'ha': 'Hausa',
  'hi': 'Hindi',
  'hr': 'Croatian',
  'ht': 'Haitian Creole',
  'hu': 'Hungarian',
  'hy': 'Armenian',
  'id': 'Indonesian',
  'ig': 'Igbo',
  'is': 'Icelandic',
  'it': 'Italian',
  'iw': 'Hebrew',
  'ja': 'Japanese',
  'jw': 'Javanese',
  'ka': 'Georgian',
  'kk': 'Kazakh',
  'km': 'Khmer',
  'kn': 'Kannada',
  'ko': 'Korean',
  'la': 'Latin',
  'lo': 'Lao',
  'lt': 'Lithuanian',
  'lv': 'Latvian',
  'mg': 'Malagasy',
  'mi': 'Maori',
  'mk': 'Macedonian',
  'ml': 'Malayalam',
  'mn': 'Mongolian',
  'mr': 'Marathi',
  'ms': 'Malay',
  'mt': 'Maltese',
  'my': 'Myanmar (Burmese)',
  'ne': 'Nepali',
  'nl': 'Dutch',
  'no': 'Norwegian',
  'ny': 'Chichewa',
  'pa': 'Punjabi',
  'pl': 'Polish',
  'pt': 'Portuguese',
  'ro': 'Romanian',
  'ru': 'Russian',
  'si': 'Sinhala',
  'sk': 'Slovak',
  'sl': 'Slovenian',
  'so': 'Somali',
  'sq': 'Albanian',
  'sr': 'Serbian',
  'st': 'Sesotho',
  'su': 'Sundanese',
  'sv': 'Swedish',
  'sw': 'Swahili',
  'ta': 'Tamil',
  'te': 'Telugu',
  'tg': 'Tajik',
  'th': 'Thai',
  'tl': 'Filipino',
  'tr': 'Turkish',
  'uk': 'Ukrainian',
  'ur': 'Urdu',
  'uz': 'Uzbek',
  'vi': 'Vietnamese',
  'yi': 'Yiddish',
  'yo': 'Yoruba',
  'zh': 'Chinese',
  'zu': 'Zulu'
  }
```
