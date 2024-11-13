# Anki Cloze TabOut Add-on

Easily tab out of Cloze deletions (e.g., `{{c1::text}}`) within Anki's editor.

This add-on simplifies navigation while editing Cloze cards by enabling the Tab key to move the cursor outside of closing double curly braces (`}}`). With this feature, if your cursor is directly before a `}}`, pressing Tab will move the cursor to the position after the closing braces, streamlining the card creation process.

![](https://github.com/kellenvu/anki-tabout/blob/main/demo.gif)

## Features

- **Tab Out of Cloze Deletions**: Automatically moves the cursor to the position after the closing `}}` when pressing Tab if positioned just before `}}`.

- **Default Behavior**: If the cursor is not before `}}`, the default Tab behavior (moving to the next text field) is preserved.

## Installation

1. Download and install the add-on.

2. Restart Anki to activate the TabOut functionality.

## Usage

The add-on is enabled by default. To use it:

1. Position the cursor within a Cloze deletion, just before the closing `}}`.

2. Press the **Tab** key to move the cursor to the position immediately after `}}`.

If the cursor is not directly before a `}}`, pressing **Tab** will move to the next editable field, following Anki's default behavior.

## Notes

- This add-on is currently designed specifically for Cloze deletions and supports tabbing out of `{{c1::...}}`-style syntax in Anki.
  
## License

This add-on is licensed under the GNU AGPL, version 3 or later.

Enhance your Anki workflow by easily tabbing out of Cloze deletions and focusing on what matters: creating effective flashcards!
