# htranslate

Translate text into h-binary.

## Usage

```py
from htranslate import translate_to_h, translate_from_h

print(translate_to_h("Hello!"))
print(translate_from_h("HhhHhhh HHhhHhH HHhHHhh HHhHHhh HHhHHHH HhhhhH"))

print(translate_to_h("Hello!", delimiter="."))
print(translate_from_h("HhhHhhh.HHhhHhH.HHhHHhh.HHhHHhh.HHhHHHH.HhhhhH", delimiter="."))
```
