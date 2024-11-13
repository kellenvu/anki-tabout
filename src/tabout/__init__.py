from aqt import mw
from aqt.editor import Editor
from aqt import gui_hooks

def custom_tab_behavior(editor: Editor):
    """Overrides the Tab key behavior to allow tabbing out of cloze deletions in Anki editor.

    This function injects JavaScript into Anki's editor to check if the cursor
    is immediately before a closing double curly brace `}}`, which is used in cloze
    deletions (e.g., `{{c1::text}}`). If `}}` is immediately to the right of the cursor,
    pressing Tab will move the cursor to the position after `}}`. If not, the default
    Tab behavior is preserved, allowing movement to the next text field.

    Args:
        editor (Editor): The current Anki editor instance where the JavaScript
            behavior is applied.
    """
    js_code = """
    document.addEventListener("keydown", function(event) {

        if (event.key === "Tab") {
            let selection = document.activeElement.shadowRoot.getSelection();
            if (selection && selection.focusNode) {

                let currentText = selection.focusNode.textContent;  // Get the text content of the active field
                let cursorPos = selection.focusOffset;  // Get the current cursor position
                
                // Check if immediately to the right is '}}'
                let textAfterCursor = currentText.slice(cursorPos);  // Text from cursor to end
                if (textAfterCursor.startsWith("}}")) {
                
                    event.preventDefault();  // Prevent default tab behavior only if '}}' is immediately to the right
                    
                    // Move the cursor to right after the '}}'
                    let range = document.createRange();
                    range.setStart(selection.focusNode, cursorPos + 2);  // Move 2 characters right
                    range.collapse(true);  // Collapse range to the new cursor position
                    selection.removeAllRanges();
                    selection.addRange(range);
                }
            }
        }
    });
    """
    editor.web.eval(js_code)


def on_editor_did_init(editor: Editor):
    """Attaches the custom Tab key behavior to the Anki editor instance.

    This function applies `custom_tab_behavior` to the editor upon initialization,
    enabling the custom Tab key handling for cloze deletions.

    Args:
        editor (Editor): The current Anki editor instance.
    """
    custom_tab_behavior(editor)


# Attach the hook to Anki's editor initialization
gui_hooks.editor_did_init.append(on_editor_did_init)
