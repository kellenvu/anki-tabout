# Anki Cloze TabOut Add-on

Streamline your Anki workflow by enabling the Tab key to jump outside Cloze deletions (`{{c1::text}}`). When your cursor is positioned directly before a closing `}}`, pressing Tab moves it to just after the braces.

![](https://github.com/kellenvu/anki-tabout/blob/main/demo.gif)

## Features

- **Tab Out of Clozes**: Moves the cursor to the position after `}}` if immediately to the right of the cursor.

- **Default Behavior**: If not next to `}}`, Tab moves to the next field as usual.

## Installation

1. Download and install the add-on.

1. Restart Anki to activate.

## Usage

Place the cursor right before `}}` in a Cloze deletion and press **Tab** to jump outside the braces. Otherwise, Tab follows Anki’s default behavior.

## How to Test Locally

1. Copy the directory located at `src/tabout` to your clipboard.

1. In Anki, go to `Tools > Add-ons > View Files`. Past the directory in the place where the add-ons are.

1. Restart Anki.

## License

GNU AGPL, version 3 or later.
