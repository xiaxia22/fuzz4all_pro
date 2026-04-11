# Class DefaultEditorKit

**Source:** `java.desktop\javax\swing\text\DefaultEditorKit.html`

### Class Description

```java
public class
DefaultEditorKit

extends
EditorKit
```

This is the set of things needed by a text component
to be a reasonably functioning editor for some

type

of text document. This implementation provides a default
implementation which treats text as plain text and
provides a minimal set of actions for a simple editor.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public static final
String
EndOfLineStringProperty

When reading a document if a CRLF is encountered a property
with this name is added and the value will be "\r\n".

**See Also:**
- Constant Field Values

---

#### public static final
String
insertContentAction

Name of the action to place content into the associated
document. If there is a selection, it is removed before
the new content is added.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
insertBreakAction

Name of the action to place a line/paragraph break into
the document. If there is a selection, it is removed before
the break is added.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
insertTabAction

Name of the action to place a tab character into
the document. If there is a selection, it is removed before
the tab is added.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
deletePrevCharAction

Name of the action to delete the character of content that
precedes the current caret position.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
deleteNextCharAction

Name of the action to delete the character of content that
follows the current caret position.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
deleteNextWordAction

Name of the action to delete the word that
follows the beginning of the selection.

**See Also:**
- getActions()

,

JTextComponent.getSelectionStart()

,

Constant Field Values

**Since:**
- 1.6

---

#### public static final
String
deletePrevWordAction

Name of the action to delete the word that
precedes the beginning of the selection.

**See Also:**
- getActions()

,

JTextComponent.getSelectionStart()

,

Constant Field Values

**Since:**
- 1.6

---

#### public static final
String
readOnlyAction

Name of the action to set the editor into read-only
mode.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
writableAction

Name of the action to set the editor into writeable
mode.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
cutAction

Name of the action to cut the selected region
and place the contents into the system clipboard.

**See Also:**
- JTextComponent.cut()

,

getActions()

,

Constant Field Values

---

#### public static final
String
copyAction

Name of the action to copy the selected region
and place the contents into the system clipboard.

**See Also:**
- JTextComponent.copy()

,

getActions()

,

Constant Field Values

---

#### public static final
String
pasteAction

Name of the action to paste the contents of the
system clipboard into the selected region, or before the
caret if nothing is selected.

**See Also:**
- JTextComponent.paste()

,

getActions()

,

Constant Field Values

---

#### public static final
String
beepAction

Name of the action to create a beep.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
pageUpAction

Name of the action to page up vertically.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
pageDownAction

Name of the action to page down vertically.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
forwardAction

Name of the Action for moving the caret
logically forward one position.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
backwardAction

Name of the Action for moving the caret
logically backward one position.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionForwardAction

Name of the Action for extending the selection
by moving the caret logically forward one position.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionBackwardAction

Name of the Action for extending the selection
by moving the caret logically backward one position.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
upAction

Name of the Action for moving the caret
logically upward one position.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
downAction

Name of the Action for moving the caret
logically downward one position.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionUpAction

Name of the Action for moving the caret
logically upward one position, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionDownAction

Name of the Action for moving the caret
logically downward one position, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
beginWordAction

Name of the

Action

for moving the caret
to the beginning of a word.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
endWordAction

Name of the Action for moving the caret
to the end of a word.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionBeginWordAction

Name of the

Action

for moving the caret
to the beginning of a word, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionEndWordAction

Name of the Action for moving the caret
to the end of a word, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
previousWordAction

Name of the

Action

for moving the caret to the
beginning of the previous word.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
nextWordAction

Name of the

Action

for moving the caret to the
beginning of the next word.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionPreviousWordAction

Name of the

Action

for moving the selection to the
beginning of the previous word, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionNextWordAction

Name of the

Action

for moving the selection to the
beginning of the next word, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
beginLineAction

Name of the

Action

for moving the caret
to the beginning of a line.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
endLineAction

Name of the

Action

for moving the caret
to the end of a line.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionBeginLineAction

Name of the

Action

for moving the caret
to the beginning of a line, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionEndLineAction

Name of the

Action

for moving the caret
to the end of a line, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
beginParagraphAction

Name of the

Action

for moving the caret
to the beginning of a paragraph.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
endParagraphAction

Name of the

Action

for moving the caret
to the end of a paragraph.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionBeginParagraphAction

Name of the

Action

for moving the caret
to the beginning of a paragraph, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionEndParagraphAction

Name of the

Action

for moving the caret
to the end of a paragraph, extending the selection.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
beginAction

Name of the

Action

for moving the caret
to the beginning of the document.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
endAction

Name of the

Action

for moving the caret
to the end of the document.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionBeginAction

Name of the

Action

for moving the caret
to the beginning of the document.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectionEndAction

Name of the Action for moving the caret
to the end of the document.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectWordAction

Name of the Action for selecting a word around the caret.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectLineAction

Name of the Action for selecting a line around the caret.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectParagraphAction

Name of the Action for selecting a paragraph around the caret.

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
selectAllAction

Name of the Action for selecting the entire document

**See Also:**
- getActions()

,

Constant Field Values

---

#### public static final
String
defaultKeyTypedAction

Name of the action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

**See Also:**
- getActions()

,

Constant Field Values

---

### Constructor Details

#### public DefaultEditorKit()

default constructor for DefaultEditorKit

---

### Method Details

#### public
String
getContentType()

Gets the MIME type of the data that this
kit represents support for. The default
is

text/plain

.

**Specified by:**
- getContentType

in class

EditorKit

**Returns:**
- the type

---

#### public
ViewFactory
getViewFactory()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. The default is to have the UI produce the
factory, so this method has no implementation.

**Specified by:**
- getViewFactory

in class

EditorKit

**Returns:**
- the view factory

---

#### public
Action
[] getActions()

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

**Specified by:**
- getActions

in class

EditorKit

**Returns:**
- the command list

---

#### public
Caret
createCaret()

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

**Specified by:**
- createCaret

in class

EditorKit

**Returns:**
- the caret

---

#### public
Document
createDefaultDocument()

Creates an uninitialized text storage model (PlainDocument)
that is appropriate for this type of editor.

**Specified by:**
- createDefaultDocument

in class

EditorKit

**Returns:**
- the model

---

#### public void read​(
InputStream
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Specified by:**
- read

in class

EditorKit

**Parameters:**
- in

- The stream to read from
- doc

- The destination for the insertion.
- pos

- The location in the document to place the
content >=0.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### public void write​(
OutputStream
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

**Specified by:**
- write

in class

EditorKit

**Parameters:**
- out

- The stream to write to
- doc

- The source for the write.
- pos

- The location in the document to fetch the
content >=0.
- len

- The amount to write out >=0.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### public void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException

Inserts content from the given stream, which will be
treated as plain text.

**Specified by:**
- read

in class

EditorKit

**Parameters:**
- in

- The stream to read from
- doc

- The destination for the insertion.
- pos

- The location in the document to place the
content >=0.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### public void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException

Writes content from a document to the given stream
as plain text.

**Specified by:**
- write

in class

EditorKit

**Parameters:**
- out

- The stream to write to
- doc

- The source for the write.
- pos

- The location in the document to fetch the
content from >=0.
- len

- The amount to write out >=0.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos is not within 0 and
the length of the document.

---

### Additional Sections

#### Class DefaultEditorKit

java.lang.Object

- javax.swing.text.EditorKit
- - javax.swing.text.DefaultEditorKit

javax.swing.text.EditorKit

- javax.swing.text.DefaultEditorKit

javax.swing.text.DefaultEditorKit

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** StyledEditorKit

```java
public class
DefaultEditorKit

extends
EditorKit
```

This is the set of things needed by a text component
to be a reasonably functioning editor for some

type

of text document. This implementation provides a default
implementation which treats text as plain text and
provides a minimal set of actions for a simple editor.

**See Also:** Serialized Form

public class

DefaultEditorKit

extends

EditorKit

This is the set of things needed by a text component
to be a reasonably functioning editor for some

type

of text document. This implementation provides a default
implementation which treats text as plain text and
provides a minimal set of actions for a simple editor.

Note that

EndOfLineStringProperty

is set
on the

Document

using the

get/putProperty

methods. Subclasses may override this behavior.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

DefaultEditorKit.BeepAction

Creates a beep.

static class

DefaultEditorKit.CopyAction

Copies the selected region and place its contents
into the system clipboard.

static class

DefaultEditorKit.CutAction

Cuts the selected region and place its contents
into the system clipboard.

static class

DefaultEditorKit.DefaultKeyTypedAction

The action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

static class

DefaultEditorKit.InsertBreakAction

Places a line/paragraph break into the document.

static class

DefaultEditorKit.InsertContentAction

Places content into the associated document.

static class

DefaultEditorKit.InsertTabAction

Places a tab character into the document.

static class

DefaultEditorKit.PasteAction

Pastes the contents of the system clipboard into the
selected region, or before the caret if nothing is
selected.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

backwardAction

Name of the Action for moving the caret
logically backward one position.

static

String

beepAction

Name of the action to create a beep.

static

String

beginAction

Name of the

Action

for moving the caret
to the beginning of the document.

static

String

beginLineAction

Name of the

Action

for moving the caret
to the beginning of a line.

static

String

beginParagraphAction

Name of the

Action

for moving the caret
to the beginning of a paragraph.

static

String

beginWordAction

Name of the

Action

for moving the caret
to the beginning of a word.

static

String

copyAction

Name of the action to copy the selected region
and place the contents into the system clipboard.

static

String

cutAction

Name of the action to cut the selected region
and place the contents into the system clipboard.

static

String

defaultKeyTypedAction

Name of the action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

static

String

deleteNextCharAction

Name of the action to delete the character of content that
follows the current caret position.

static

String

deleteNextWordAction

Name of the action to delete the word that
follows the beginning of the selection.

static

String

deletePrevCharAction

Name of the action to delete the character of content that
precedes the current caret position.

static

String

deletePrevWordAction

Name of the action to delete the word that
precedes the beginning of the selection.

static

String

downAction

Name of the Action for moving the caret
logically downward one position.

static

String

endAction

Name of the

Action

for moving the caret
to the end of the document.

static

String

endLineAction

Name of the

Action

for moving the caret
to the end of a line.

static

String

EndOfLineStringProperty

When reading a document if a CRLF is encountered a property
with this name is added and the value will be "\r\n".

static

String

endParagraphAction

Name of the

Action

for moving the caret
to the end of a paragraph.

static

String

endWordAction

Name of the Action for moving the caret
to the end of a word.

static

String

forwardAction

Name of the Action for moving the caret
logically forward one position.

static

String

insertBreakAction

Name of the action to place a line/paragraph break into
the document.

static

String

insertContentAction

Name of the action to place content into the associated
document.

static

String

insertTabAction

Name of the action to place a tab character into
the document.

static

String

nextWordAction

Name of the

Action

for moving the caret to the
beginning of the next word.

static

String

pageDownAction

Name of the action to page down vertically.

static

String

pageUpAction

Name of the action to page up vertically.

static

String

pasteAction

Name of the action to paste the contents of the
system clipboard into the selected region, or before the
caret if nothing is selected.

static

String

previousWordAction

Name of the

Action

for moving the caret to the
beginning of the previous word.

static

String

readOnlyAction

Name of the action to set the editor into read-only
mode.

static

String

selectAllAction

Name of the Action for selecting the entire document

static

String

selectionBackwardAction

Name of the Action for extending the selection
by moving the caret logically backward one position.

static

String

selectionBeginAction

Name of the

Action

for moving the caret
to the beginning of the document.

static

String

selectionBeginLineAction

Name of the

Action

for moving the caret
to the beginning of a line, extending the selection.

static

String

selectionBeginParagraphAction

Name of the

Action

for moving the caret
to the beginning of a paragraph, extending the selection.

static

String

selectionBeginWordAction

Name of the

Action

for moving the caret
to the beginning of a word, extending the selection.

static

String

selectionDownAction

Name of the Action for moving the caret
logically downward one position, extending the selection.

static

String

selectionEndAction

Name of the Action for moving the caret
to the end of the document.

static

String

selectionEndLineAction

Name of the

Action

for moving the caret
to the end of a line, extending the selection.

static

String

selectionEndParagraphAction

Name of the

Action

for moving the caret
to the end of a paragraph, extending the selection.

static

String

selectionEndWordAction

Name of the Action for moving the caret
to the end of a word, extending the selection.

static

String

selectionForwardAction

Name of the Action for extending the selection
by moving the caret logically forward one position.

static

String

selectionNextWordAction

Name of the

Action

for moving the selection to the
beginning of the next word, extending the selection.

static

String

selectionPreviousWordAction

Name of the

Action

for moving the selection to the
beginning of the previous word, extending the selection.

static

String

selectionUpAction

Name of the Action for moving the caret
logically upward one position, extending the selection.

static

String

selectLineAction

Name of the Action for selecting a line around the caret.

static

String

selectParagraphAction

Name of the Action for selecting a paragraph around the caret.

static

String

selectWordAction

Name of the Action for selecting a word around the caret.

static

String

upAction

Name of the Action for moving the caret
logically upward one position.

static

String

writableAction

Name of the action to set the editor into writeable
mode.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultEditorKit

()

default constructor for DefaultEditorKit

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Caret

createCaret

()

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

Document

createDefaultDocument

()

Creates an uninitialized text storage model (PlainDocument)
that is appropriate for this type of editor.

Action

[]

getActions

()

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

String

getContentType

()

Gets the MIME type of the data that this
kit represents support for.

ViewFactory

getViewFactory

()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

void

read

​(

InputStream

in,

Document

doc,
int pos)

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

void

read

​(

Reader

in,

Document

doc,
int pos)

Inserts content from the given stream, which will be
treated as plain text.

void

write

​(

OutputStream

out,

Document

doc,
int pos,
int len)

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

void

write

​(

Writer

out,

Document

doc,
int pos,
int len)

Writes content from a document to the given stream
as plain text.

- Methods declared in class javax.swing.text.

EditorKit

clone

,

deinstall

,

install

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

DefaultEditorKit.BeepAction

Creates a beep.

static class

DefaultEditorKit.CopyAction

Copies the selected region and place its contents
into the system clipboard.

static class

DefaultEditorKit.CutAction

Cuts the selected region and place its contents
into the system clipboard.

static class

DefaultEditorKit.DefaultKeyTypedAction

The action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

static class

DefaultEditorKit.InsertBreakAction

Places a line/paragraph break into the document.

static class

DefaultEditorKit.InsertContentAction

Places content into the associated document.

static class

DefaultEditorKit.InsertTabAction

Places a tab character into the document.

static class

DefaultEditorKit.PasteAction

Pastes the contents of the system clipboard into the
selected region, or before the caret if nothing is
selected.

---

#### Nested Class Summary

Creates a beep.

Copies the selected region and place its contents
into the system clipboard.

Cuts the selected region and place its contents
into the system clipboard.

The action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

Places a line/paragraph break into the document.

Places content into the associated document.

Places a tab character into the document.

Pastes the contents of the system clipboard into the
selected region, or before the caret if nothing is
selected.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

backwardAction

Name of the Action for moving the caret
logically backward one position.

static

String

beepAction

Name of the action to create a beep.

static

String

beginAction

Name of the

Action

for moving the caret
to the beginning of the document.

static

String

beginLineAction

Name of the

Action

for moving the caret
to the beginning of a line.

static

String

beginParagraphAction

Name of the

Action

for moving the caret
to the beginning of a paragraph.

static

String

beginWordAction

Name of the

Action

for moving the caret
to the beginning of a word.

static

String

copyAction

Name of the action to copy the selected region
and place the contents into the system clipboard.

static

String

cutAction

Name of the action to cut the selected region
and place the contents into the system clipboard.

static

String

defaultKeyTypedAction

Name of the action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

static

String

deleteNextCharAction

Name of the action to delete the character of content that
follows the current caret position.

static

String

deleteNextWordAction

Name of the action to delete the word that
follows the beginning of the selection.

static

String

deletePrevCharAction

Name of the action to delete the character of content that
precedes the current caret position.

static

String

deletePrevWordAction

Name of the action to delete the word that
precedes the beginning of the selection.

static

String

downAction

Name of the Action for moving the caret
logically downward one position.

static

String

endAction

Name of the

Action

for moving the caret
to the end of the document.

static

String

endLineAction

Name of the

Action

for moving the caret
to the end of a line.

static

String

EndOfLineStringProperty

When reading a document if a CRLF is encountered a property
with this name is added and the value will be "\r\n".

static

String

endParagraphAction

Name of the

Action

for moving the caret
to the end of a paragraph.

static

String

endWordAction

Name of the Action for moving the caret
to the end of a word.

static

String

forwardAction

Name of the Action for moving the caret
logically forward one position.

static

String

insertBreakAction

Name of the action to place a line/paragraph break into
the document.

static

String

insertContentAction

Name of the action to place content into the associated
document.

static

String

insertTabAction

Name of the action to place a tab character into
the document.

static

String

nextWordAction

Name of the

Action

for moving the caret to the
beginning of the next word.

static

String

pageDownAction

Name of the action to page down vertically.

static

String

pageUpAction

Name of the action to page up vertically.

static

String

pasteAction

Name of the action to paste the contents of the
system clipboard into the selected region, or before the
caret if nothing is selected.

static

String

previousWordAction

Name of the

Action

for moving the caret to the
beginning of the previous word.

static

String

readOnlyAction

Name of the action to set the editor into read-only
mode.

static

String

selectAllAction

Name of the Action for selecting the entire document

static

String

selectionBackwardAction

Name of the Action for extending the selection
by moving the caret logically backward one position.

static

String

selectionBeginAction

Name of the

Action

for moving the caret
to the beginning of the document.

static

String

selectionBeginLineAction

Name of the

Action

for moving the caret
to the beginning of a line, extending the selection.

static

String

selectionBeginParagraphAction

Name of the

Action

for moving the caret
to the beginning of a paragraph, extending the selection.

static

String

selectionBeginWordAction

Name of the

Action

for moving the caret
to the beginning of a word, extending the selection.

static

String

selectionDownAction

Name of the Action for moving the caret
logically downward one position, extending the selection.

static

String

selectionEndAction

Name of the Action for moving the caret
to the end of the document.

static

String

selectionEndLineAction

Name of the

Action

for moving the caret
to the end of a line, extending the selection.

static

String

selectionEndParagraphAction

Name of the

Action

for moving the caret
to the end of a paragraph, extending the selection.

static

String

selectionEndWordAction

Name of the Action for moving the caret
to the end of a word, extending the selection.

static

String

selectionForwardAction

Name of the Action for extending the selection
by moving the caret logically forward one position.

static

String

selectionNextWordAction

Name of the

Action

for moving the selection to the
beginning of the next word, extending the selection.

static

String

selectionPreviousWordAction

Name of the

Action

for moving the selection to the
beginning of the previous word, extending the selection.

static

String

selectionUpAction

Name of the Action for moving the caret
logically upward one position, extending the selection.

static

String

selectLineAction

Name of the Action for selecting a line around the caret.

static

String

selectParagraphAction

Name of the Action for selecting a paragraph around the caret.

static

String

selectWordAction

Name of the Action for selecting a word around the caret.

static

String

upAction

Name of the Action for moving the caret
logically upward one position.

static

String

writableAction

Name of the action to set the editor into writeable
mode.

---

#### Field Summary

Name of the Action for moving the caret
logically backward one position.

Name of the action to create a beep.

Name of the

Action

for moving the caret
to the beginning of the document.

Name of the

Action

for moving the caret
to the beginning of a line.

Name of the

Action

for moving the caret
to the beginning of a paragraph.

Name of the

Action

for moving the caret
to the beginning of a word.

Name of the action to copy the selected region
and place the contents into the system clipboard.

Name of the action to cut the selected region
and place the contents into the system clipboard.

Name of the action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

Name of the action to delete the character of content that
follows the current caret position.

Name of the action to delete the word that
follows the beginning of the selection.

Name of the action to delete the character of content that
precedes the current caret position.

Name of the action to delete the word that
precedes the beginning of the selection.

Name of the Action for moving the caret
logically downward one position.

Name of the

Action

for moving the caret
to the end of the document.

Name of the

Action

for moving the caret
to the end of a line.

When reading a document if a CRLF is encountered a property
with this name is added and the value will be "\r\n".

Name of the

Action

for moving the caret
to the end of a paragraph.

Name of the Action for moving the caret
to the end of a word.

Name of the Action for moving the caret
logically forward one position.

Name of the action to place a line/paragraph break into
the document.

Name of the action to place content into the associated
document.

Name of the action to place a tab character into
the document.

Name of the

Action

for moving the caret to the
beginning of the next word.

Name of the action to page down vertically.

Name of the action to page up vertically.

Name of the action to paste the contents of the
system clipboard into the selected region, or before the
caret if nothing is selected.

Name of the

Action

for moving the caret to the
beginning of the previous word.

Name of the action to set the editor into read-only
mode.

Name of the Action for selecting the entire document

Name of the Action for extending the selection
by moving the caret logically backward one position.

Name of the

Action

for moving the caret
to the beginning of a line, extending the selection.

Name of the

Action

for moving the caret
to the beginning of a paragraph, extending the selection.

Name of the

Action

for moving the caret
to the beginning of a word, extending the selection.

Name of the Action for moving the caret
logically downward one position, extending the selection.

Name of the Action for moving the caret
to the end of the document.

Name of the

Action

for moving the caret
to the end of a line, extending the selection.

Name of the

Action

for moving the caret
to the end of a paragraph, extending the selection.

Name of the Action for moving the caret
to the end of a word, extending the selection.

Name of the Action for extending the selection
by moving the caret logically forward one position.

Name of the

Action

for moving the selection to the
beginning of the next word, extending the selection.

Name of the

Action

for moving the selection to the
beginning of the previous word, extending the selection.

Name of the Action for moving the caret
logically upward one position, extending the selection.

Name of the Action for selecting a line around the caret.

Name of the Action for selecting a paragraph around the caret.

Name of the Action for selecting a word around the caret.

Name of the Action for moving the caret
logically upward one position.

Name of the action to set the editor into writeable
mode.

Constructor Summary

Constructors

Constructor

Description

DefaultEditorKit

()

default constructor for DefaultEditorKit

---

#### Constructor Summary

default constructor for DefaultEditorKit

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Caret

createCaret

()

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

Document

createDefaultDocument

()

Creates an uninitialized text storage model (PlainDocument)
that is appropriate for this type of editor.

Action

[]

getActions

()

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

String

getContentType

()

Gets the MIME type of the data that this
kit represents support for.

ViewFactory

getViewFactory

()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

void

read

​(

InputStream

in,

Document

doc,
int pos)

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

void

read

​(

Reader

in,

Document

doc,
int pos)

Inserts content from the given stream, which will be
treated as plain text.

void

write

​(

OutputStream

out,

Document

doc,
int pos,
int len)

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

void

write

​(

Writer

out,

Document

doc,
int pos,
int len)

Writes content from a document to the given stream
as plain text.

- Methods declared in class javax.swing.text.

EditorKit

clone

,

deinstall

,

install

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

Creates an uninitialized text storage model (PlainDocument)
that is appropriate for this type of editor.

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

Gets the MIME type of the data that this
kit represents support for.

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

Inserts content from the given stream, which will be
treated as plain text.

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

Writes content from a document to the given stream
as plain text.

Methods declared in class javax.swing.text.

EditorKit

clone

,

deinstall

,

install

---

#### Methods declared in class javax.swing.text. EditorKit

Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- EndOfLineStringProperty

```java
public static final
String
EndOfLineStringProperty
```

When reading a document if a CRLF is encountered a property
with this name is added and the value will be "\r\n".

**See Also:** Constant Field Values

- insertContentAction

```java
public static final
String
insertContentAction
```

Name of the action to place content into the associated
document. If there is a selection, it is removed before
the new content is added.

**See Also:** getActions()

,

Constant Field Values

- insertBreakAction

```java
public static final
String
insertBreakAction
```

Name of the action to place a line/paragraph break into
the document. If there is a selection, it is removed before
the break is added.

**See Also:** getActions()

,

Constant Field Values

- insertTabAction

```java
public static final
String
insertTabAction
```

Name of the action to place a tab character into
the document. If there is a selection, it is removed before
the tab is added.

**See Also:** getActions()

,

Constant Field Values

- deletePrevCharAction

```java
public static final
String
deletePrevCharAction
```

Name of the action to delete the character of content that
precedes the current caret position.

**See Also:** getActions()

,

Constant Field Values

- deleteNextCharAction

```java
public static final
String
deleteNextCharAction
```

Name of the action to delete the character of content that
follows the current caret position.

**See Also:** getActions()

,

Constant Field Values

- deleteNextWordAction

```java
public static final
String
deleteNextWordAction
```

Name of the action to delete the word that
follows the beginning of the selection.

**Since:** 1.6
**See Also:** getActions()

,

JTextComponent.getSelectionStart()

,

Constant Field Values

- deletePrevWordAction

```java
public static final
String
deletePrevWordAction
```

Name of the action to delete the word that
precedes the beginning of the selection.

**Since:** 1.6
**See Also:** getActions()

,

JTextComponent.getSelectionStart()

,

Constant Field Values

- readOnlyAction

```java
public static final
String
readOnlyAction
```

Name of the action to set the editor into read-only
mode.

**See Also:** getActions()

,

Constant Field Values

- writableAction

```java
public static final
String
writableAction
```

Name of the action to set the editor into writeable
mode.

**See Also:** getActions()

,

Constant Field Values

- cutAction

```java
public static final
String
cutAction
```

Name of the action to cut the selected region
and place the contents into the system clipboard.

**See Also:** JTextComponent.cut()

,

getActions()

,

Constant Field Values

- copyAction

```java
public static final
String
copyAction
```

Name of the action to copy the selected region
and place the contents into the system clipboard.

**See Also:** JTextComponent.copy()

,

getActions()

,

Constant Field Values

- pasteAction

```java
public static final
String
pasteAction
```

Name of the action to paste the contents of the
system clipboard into the selected region, or before the
caret if nothing is selected.

**See Also:** JTextComponent.paste()

,

getActions()

,

Constant Field Values

- beepAction

```java
public static final
String
beepAction
```

Name of the action to create a beep.

**See Also:** getActions()

,

Constant Field Values

- pageUpAction

```java
public static final
String
pageUpAction
```

Name of the action to page up vertically.

**See Also:** getActions()

,

Constant Field Values

- pageDownAction

```java
public static final
String
pageDownAction
```

Name of the action to page down vertically.

**See Also:** getActions()

,

Constant Field Values

- forwardAction

```java
public static final
String
forwardAction
```

Name of the Action for moving the caret
logically forward one position.

**See Also:** getActions()

,

Constant Field Values

- backwardAction

```java
public static final
String
backwardAction
```

Name of the Action for moving the caret
logically backward one position.

**See Also:** getActions()

,

Constant Field Values

- selectionForwardAction

```java
public static final
String
selectionForwardAction
```

Name of the Action for extending the selection
by moving the caret logically forward one position.

**See Also:** getActions()

,

Constant Field Values

- selectionBackwardAction

```java
public static final
String
selectionBackwardAction
```

Name of the Action for extending the selection
by moving the caret logically backward one position.

**See Also:** getActions()

,

Constant Field Values

- upAction

```java
public static final
String
upAction
```

Name of the Action for moving the caret
logically upward one position.

**See Also:** getActions()

,

Constant Field Values

- downAction

```java
public static final
String
downAction
```

Name of the Action for moving the caret
logically downward one position.

**See Also:** getActions()

,

Constant Field Values

- selectionUpAction

```java
public static final
String
selectionUpAction
```

Name of the Action for moving the caret
logically upward one position, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionDownAction

```java
public static final
String
selectionDownAction
```

Name of the Action for moving the caret
logically downward one position, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- beginWordAction

```java
public static final
String
beginWordAction
```

Name of the

Action

for moving the caret
to the beginning of a word.

**See Also:** getActions()

,

Constant Field Values

- endWordAction

```java
public static final
String
endWordAction
```

Name of the Action for moving the caret
to the end of a word.

**See Also:** getActions()

,

Constant Field Values

- selectionBeginWordAction

```java
public static final
String
selectionBeginWordAction
```

Name of the

Action

for moving the caret
to the beginning of a word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionEndWordAction

```java
public static final
String
selectionEndWordAction
```

Name of the Action for moving the caret
to the end of a word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- previousWordAction

```java
public static final
String
previousWordAction
```

Name of the

Action

for moving the caret to the
beginning of the previous word.

**See Also:** getActions()

,

Constant Field Values

- nextWordAction

```java
public static final
String
nextWordAction
```

Name of the

Action

for moving the caret to the
beginning of the next word.

**See Also:** getActions()

,

Constant Field Values

- selectionPreviousWordAction

```java
public static final
String
selectionPreviousWordAction
```

Name of the

Action

for moving the selection to the
beginning of the previous word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionNextWordAction

```java
public static final
String
selectionNextWordAction
```

Name of the

Action

for moving the selection to the
beginning of the next word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- beginLineAction

```java
public static final
String
beginLineAction
```

Name of the

Action

for moving the caret
to the beginning of a line.

**See Also:** getActions()

,

Constant Field Values

- endLineAction

```java
public static final
String
endLineAction
```

Name of the

Action

for moving the caret
to the end of a line.

**See Also:** getActions()

,

Constant Field Values

- selectionBeginLineAction

```java
public static final
String
selectionBeginLineAction
```

Name of the

Action

for moving the caret
to the beginning of a line, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionEndLineAction

```java
public static final
String
selectionEndLineAction
```

Name of the

Action

for moving the caret
to the end of a line, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- beginParagraphAction

```java
public static final
String
beginParagraphAction
```

Name of the

Action

for moving the caret
to the beginning of a paragraph.

**See Also:** getActions()

,

Constant Field Values

- endParagraphAction

```java
public static final
String
endParagraphAction
```

Name of the

Action

for moving the caret
to the end of a paragraph.

**See Also:** getActions()

,

Constant Field Values

- selectionBeginParagraphAction

```java
public static final
String
selectionBeginParagraphAction
```

Name of the

Action

for moving the caret
to the beginning of a paragraph, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionEndParagraphAction

```java
public static final
String
selectionEndParagraphAction
```

Name of the

Action

for moving the caret
to the end of a paragraph, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- beginAction

```java
public static final
String
beginAction
```

Name of the

Action

for moving the caret
to the beginning of the document.

**See Also:** getActions()

,

Constant Field Values

- endAction

```java
public static final
String
endAction
```

Name of the

Action

for moving the caret
to the end of the document.

**See Also:** getActions()

,

Constant Field Values

- selectionBeginAction

```java
public static final
String
selectionBeginAction
```

Name of the

Action

for moving the caret
to the beginning of the document.

**See Also:** getActions()

,

Constant Field Values

- selectionEndAction

```java
public static final
String
selectionEndAction
```

Name of the Action for moving the caret
to the end of the document.

**See Also:** getActions()

,

Constant Field Values

- selectWordAction

```java
public static final
String
selectWordAction
```

Name of the Action for selecting a word around the caret.

**See Also:** getActions()

,

Constant Field Values

- selectLineAction

```java
public static final
String
selectLineAction
```

Name of the Action for selecting a line around the caret.

**See Also:** getActions()

,

Constant Field Values

- selectParagraphAction

```java
public static final
String
selectParagraphAction
```

Name of the Action for selecting a paragraph around the caret.

**See Also:** getActions()

,

Constant Field Values

- selectAllAction

```java
public static final
String
selectAllAction
```

Name of the Action for selecting the entire document

**See Also:** getActions()

,

Constant Field Values

- defaultKeyTypedAction

```java
public static final
String
defaultKeyTypedAction
```

Name of the action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

**See Also:** getActions()

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultEditorKit

```java
public DefaultEditorKit()
```

default constructor for DefaultEditorKit

============ METHOD DETAIL ==========

- Method Detail

- getContentType

```java
public
String
getContentType()
```

Gets the MIME type of the data that this
kit represents support for. The default
is

text/plain

.

**Specified by:** getContentType

in class

EditorKit
**Returns:** the type

- getViewFactory

```java
public
ViewFactory
getViewFactory()
```

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. The default is to have the UI produce the
factory, so this method has no implementation.

**Specified by:** getViewFactory

in class

EditorKit
**Returns:** the view factory

- getActions

```java
public
Action
[] getActions()
```

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

**Specified by:** getActions

in class

EditorKit
**Returns:** the command list

- createCaret

```java
public
Caret
createCaret()
```

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

**Specified by:** createCaret

in class

EditorKit
**Returns:** the caret

- createDefaultDocument

```java
public
Document
createDefaultDocument()
```

Creates an uninitialized text storage model (PlainDocument)
that is appropriate for this type of editor.

**Specified by:** createDefaultDocument

in class

EditorKit
**Returns:** the model

- read

```java
public void read​(
InputStream
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Specified by:** read

in class

EditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- write

```java
public void write​(
OutputStream
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

**Specified by:** write

in class

EditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content >=0.
**Parameters:** len

- The amount to write out >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- read

```java
public void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream, which will be
treated as plain text.

**Specified by:** read

in class

EditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- write

```java
public void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
as plain text.

**Specified by:** write

in class

EditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content from >=0.
**Parameters:** len

- The amount to write out >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos is not within 0 and
the length of the document.

Field Detail

- EndOfLineStringProperty

```java
public static final
String
EndOfLineStringProperty
```

When reading a document if a CRLF is encountered a property
with this name is added and the value will be "\r\n".

**See Also:** Constant Field Values

- insertContentAction

```java
public static final
String
insertContentAction
```

Name of the action to place content into the associated
document. If there is a selection, it is removed before
the new content is added.

**See Also:** getActions()

,

Constant Field Values

- insertBreakAction

```java
public static final
String
insertBreakAction
```

Name of the action to place a line/paragraph break into
the document. If there is a selection, it is removed before
the break is added.

**See Also:** getActions()

,

Constant Field Values

- insertTabAction

```java
public static final
String
insertTabAction
```

Name of the action to place a tab character into
the document. If there is a selection, it is removed before
the tab is added.

**See Also:** getActions()

,

Constant Field Values

- deletePrevCharAction

```java
public static final
String
deletePrevCharAction
```

Name of the action to delete the character of content that
precedes the current caret position.

**See Also:** getActions()

,

Constant Field Values

- deleteNextCharAction

```java
public static final
String
deleteNextCharAction
```

Name of the action to delete the character of content that
follows the current caret position.

**See Also:** getActions()

,

Constant Field Values

- deleteNextWordAction

```java
public static final
String
deleteNextWordAction
```

Name of the action to delete the word that
follows the beginning of the selection.

**Since:** 1.6
**See Also:** getActions()

,

JTextComponent.getSelectionStart()

,

Constant Field Values

- deletePrevWordAction

```java
public static final
String
deletePrevWordAction
```

Name of the action to delete the word that
precedes the beginning of the selection.

**Since:** 1.6
**See Also:** getActions()

,

JTextComponent.getSelectionStart()

,

Constant Field Values

- readOnlyAction

```java
public static final
String
readOnlyAction
```

Name of the action to set the editor into read-only
mode.

**See Also:** getActions()

,

Constant Field Values

- writableAction

```java
public static final
String
writableAction
```

Name of the action to set the editor into writeable
mode.

**See Also:** getActions()

,

Constant Field Values

- cutAction

```java
public static final
String
cutAction
```

Name of the action to cut the selected region
and place the contents into the system clipboard.

**See Also:** JTextComponent.cut()

,

getActions()

,

Constant Field Values

- copyAction

```java
public static final
String
copyAction
```

Name of the action to copy the selected region
and place the contents into the system clipboard.

**See Also:** JTextComponent.copy()

,

getActions()

,

Constant Field Values

- pasteAction

```java
public static final
String
pasteAction
```

Name of the action to paste the contents of the
system clipboard into the selected region, or before the
caret if nothing is selected.

**See Also:** JTextComponent.paste()

,

getActions()

,

Constant Field Values

- beepAction

```java
public static final
String
beepAction
```

Name of the action to create a beep.

**See Also:** getActions()

,

Constant Field Values

- pageUpAction

```java
public static final
String
pageUpAction
```

Name of the action to page up vertically.

**See Also:** getActions()

,

Constant Field Values

- pageDownAction

```java
public static final
String
pageDownAction
```

Name of the action to page down vertically.

**See Also:** getActions()

,

Constant Field Values

- forwardAction

```java
public static final
String
forwardAction
```

Name of the Action for moving the caret
logically forward one position.

**See Also:** getActions()

,

Constant Field Values

- backwardAction

```java
public static final
String
backwardAction
```

Name of the Action for moving the caret
logically backward one position.

**See Also:** getActions()

,

Constant Field Values

- selectionForwardAction

```java
public static final
String
selectionForwardAction
```

Name of the Action for extending the selection
by moving the caret logically forward one position.

**See Also:** getActions()

,

Constant Field Values

- selectionBackwardAction

```java
public static final
String
selectionBackwardAction
```

Name of the Action for extending the selection
by moving the caret logically backward one position.

**See Also:** getActions()

,

Constant Field Values

- upAction

```java
public static final
String
upAction
```

Name of the Action for moving the caret
logically upward one position.

**See Also:** getActions()

,

Constant Field Values

- downAction

```java
public static final
String
downAction
```

Name of the Action for moving the caret
logically downward one position.

**See Also:** getActions()

,

Constant Field Values

- selectionUpAction

```java
public static final
String
selectionUpAction
```

Name of the Action for moving the caret
logically upward one position, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionDownAction

```java
public static final
String
selectionDownAction
```

Name of the Action for moving the caret
logically downward one position, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- beginWordAction

```java
public static final
String
beginWordAction
```

Name of the

Action

for moving the caret
to the beginning of a word.

**See Also:** getActions()

,

Constant Field Values

- endWordAction

```java
public static final
String
endWordAction
```

Name of the Action for moving the caret
to the end of a word.

**See Also:** getActions()

,

Constant Field Values

- selectionBeginWordAction

```java
public static final
String
selectionBeginWordAction
```

Name of the

Action

for moving the caret
to the beginning of a word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionEndWordAction

```java
public static final
String
selectionEndWordAction
```

Name of the Action for moving the caret
to the end of a word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- previousWordAction

```java
public static final
String
previousWordAction
```

Name of the

Action

for moving the caret to the
beginning of the previous word.

**See Also:** getActions()

,

Constant Field Values

- nextWordAction

```java
public static final
String
nextWordAction
```

Name of the

Action

for moving the caret to the
beginning of the next word.

**See Also:** getActions()

,

Constant Field Values

- selectionPreviousWordAction

```java
public static final
String
selectionPreviousWordAction
```

Name of the

Action

for moving the selection to the
beginning of the previous word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionNextWordAction

```java
public static final
String
selectionNextWordAction
```

Name of the

Action

for moving the selection to the
beginning of the next word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- beginLineAction

```java
public static final
String
beginLineAction
```

Name of the

Action

for moving the caret
to the beginning of a line.

**See Also:** getActions()

,

Constant Field Values

- endLineAction

```java
public static final
String
endLineAction
```

Name of the

Action

for moving the caret
to the end of a line.

**See Also:** getActions()

,

Constant Field Values

- selectionBeginLineAction

```java
public static final
String
selectionBeginLineAction
```

Name of the

Action

for moving the caret
to the beginning of a line, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionEndLineAction

```java
public static final
String
selectionEndLineAction
```

Name of the

Action

for moving the caret
to the end of a line, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- beginParagraphAction

```java
public static final
String
beginParagraphAction
```

Name of the

Action

for moving the caret
to the beginning of a paragraph.

**See Also:** getActions()

,

Constant Field Values

- endParagraphAction

```java
public static final
String
endParagraphAction
```

Name of the

Action

for moving the caret
to the end of a paragraph.

**See Also:** getActions()

,

Constant Field Values

- selectionBeginParagraphAction

```java
public static final
String
selectionBeginParagraphAction
```

Name of the

Action

for moving the caret
to the beginning of a paragraph, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- selectionEndParagraphAction

```java
public static final
String
selectionEndParagraphAction
```

Name of the

Action

for moving the caret
to the end of a paragraph, extending the selection.

**See Also:** getActions()

,

Constant Field Values

- beginAction

```java
public static final
String
beginAction
```

Name of the

Action

for moving the caret
to the beginning of the document.

**See Also:** getActions()

,

Constant Field Values

- endAction

```java
public static final
String
endAction
```

Name of the

Action

for moving the caret
to the end of the document.

**See Also:** getActions()

,

Constant Field Values

- selectionBeginAction

```java
public static final
String
selectionBeginAction
```

Name of the

Action

for moving the caret
to the beginning of the document.

**See Also:** getActions()

,

Constant Field Values

- selectionEndAction

```java
public static final
String
selectionEndAction
```

Name of the Action for moving the caret
to the end of the document.

**See Also:** getActions()

,

Constant Field Values

- selectWordAction

```java
public static final
String
selectWordAction
```

Name of the Action for selecting a word around the caret.

**See Also:** getActions()

,

Constant Field Values

- selectLineAction

```java
public static final
String
selectLineAction
```

Name of the Action for selecting a line around the caret.

**See Also:** getActions()

,

Constant Field Values

- selectParagraphAction

```java
public static final
String
selectParagraphAction
```

Name of the Action for selecting a paragraph around the caret.

**See Also:** getActions()

,

Constant Field Values

- selectAllAction

```java
public static final
String
selectAllAction
```

Name of the Action for selecting the entire document

**See Also:** getActions()

,

Constant Field Values

- defaultKeyTypedAction

```java
public static final
String
defaultKeyTypedAction
```

Name of the action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

**See Also:** getActions()

,

Constant Field Values

---

#### Field Detail

EndOfLineStringProperty

```java
public static final
String
EndOfLineStringProperty
```

When reading a document if a CRLF is encountered a property
with this name is added and the value will be "\r\n".

**See Also:** Constant Field Values

---

#### EndOfLineStringProperty

public static final

String

EndOfLineStringProperty

When reading a document if a CRLF is encountered a property
with this name is added and the value will be "\r\n".

insertContentAction

```java
public static final
String
insertContentAction
```

Name of the action to place content into the associated
document. If there is a selection, it is removed before
the new content is added.

**See Also:** getActions()

,

Constant Field Values

---

#### insertContentAction

public static final

String

insertContentAction

Name of the action to place content into the associated
document. If there is a selection, it is removed before
the new content is added.

insertBreakAction

```java
public static final
String
insertBreakAction
```

Name of the action to place a line/paragraph break into
the document. If there is a selection, it is removed before
the break is added.

**See Also:** getActions()

,

Constant Field Values

---

#### insertBreakAction

public static final

String

insertBreakAction

Name of the action to place a line/paragraph break into
the document. If there is a selection, it is removed before
the break is added.

insertTabAction

```java
public static final
String
insertTabAction
```

Name of the action to place a tab character into
the document. If there is a selection, it is removed before
the tab is added.

**See Also:** getActions()

,

Constant Field Values

---

#### insertTabAction

public static final

String

insertTabAction

Name of the action to place a tab character into
the document. If there is a selection, it is removed before
the tab is added.

deletePrevCharAction

```java
public static final
String
deletePrevCharAction
```

Name of the action to delete the character of content that
precedes the current caret position.

**See Also:** getActions()

,

Constant Field Values

---

#### deletePrevCharAction

public static final

String

deletePrevCharAction

Name of the action to delete the character of content that
precedes the current caret position.

deleteNextCharAction

```java
public static final
String
deleteNextCharAction
```

Name of the action to delete the character of content that
follows the current caret position.

**See Also:** getActions()

,

Constant Field Values

---

#### deleteNextCharAction

public static final

String

deleteNextCharAction

Name of the action to delete the character of content that
follows the current caret position.

deleteNextWordAction

```java
public static final
String
deleteNextWordAction
```

Name of the action to delete the word that
follows the beginning of the selection.

**Since:** 1.6
**See Also:** getActions()

,

JTextComponent.getSelectionStart()

,

Constant Field Values

---

#### deleteNextWordAction

public static final

String

deleteNextWordAction

Name of the action to delete the word that
follows the beginning of the selection.

deletePrevWordAction

```java
public static final
String
deletePrevWordAction
```

Name of the action to delete the word that
precedes the beginning of the selection.

**Since:** 1.6
**See Also:** getActions()

,

JTextComponent.getSelectionStart()

,

Constant Field Values

---

#### deletePrevWordAction

public static final

String

deletePrevWordAction

Name of the action to delete the word that
precedes the beginning of the selection.

readOnlyAction

```java
public static final
String
readOnlyAction
```

Name of the action to set the editor into read-only
mode.

**See Also:** getActions()

,

Constant Field Values

---

#### readOnlyAction

public static final

String

readOnlyAction

Name of the action to set the editor into read-only
mode.

writableAction

```java
public static final
String
writableAction
```

Name of the action to set the editor into writeable
mode.

**See Also:** getActions()

,

Constant Field Values

---

#### writableAction

public static final

String

writableAction

Name of the action to set the editor into writeable
mode.

cutAction

```java
public static final
String
cutAction
```

Name of the action to cut the selected region
and place the contents into the system clipboard.

**See Also:** JTextComponent.cut()

,

getActions()

,

Constant Field Values

---

#### cutAction

public static final

String

cutAction

Name of the action to cut the selected region
and place the contents into the system clipboard.

copyAction

```java
public static final
String
copyAction
```

Name of the action to copy the selected region
and place the contents into the system clipboard.

**See Also:** JTextComponent.copy()

,

getActions()

,

Constant Field Values

---

#### copyAction

public static final

String

copyAction

Name of the action to copy the selected region
and place the contents into the system clipboard.

pasteAction

```java
public static final
String
pasteAction
```

Name of the action to paste the contents of the
system clipboard into the selected region, or before the
caret if nothing is selected.

**See Also:** JTextComponent.paste()

,

getActions()

,

Constant Field Values

---

#### pasteAction

public static final

String

pasteAction

Name of the action to paste the contents of the
system clipboard into the selected region, or before the
caret if nothing is selected.

beepAction

```java
public static final
String
beepAction
```

Name of the action to create a beep.

**See Also:** getActions()

,

Constant Field Values

---

#### beepAction

public static final

String

beepAction

Name of the action to create a beep.

pageUpAction

```java
public static final
String
pageUpAction
```

Name of the action to page up vertically.

**See Also:** getActions()

,

Constant Field Values

---

#### pageUpAction

public static final

String

pageUpAction

Name of the action to page up vertically.

pageDownAction

```java
public static final
String
pageDownAction
```

Name of the action to page down vertically.

**See Also:** getActions()

,

Constant Field Values

---

#### pageDownAction

public static final

String

pageDownAction

Name of the action to page down vertically.

forwardAction

```java
public static final
String
forwardAction
```

Name of the Action for moving the caret
logically forward one position.

**See Also:** getActions()

,

Constant Field Values

---

#### forwardAction

public static final

String

forwardAction

Name of the Action for moving the caret
logically forward one position.

backwardAction

```java
public static final
String
backwardAction
```

Name of the Action for moving the caret
logically backward one position.

**See Also:** getActions()

,

Constant Field Values

---

#### backwardAction

public static final

String

backwardAction

Name of the Action for moving the caret
logically backward one position.

selectionForwardAction

```java
public static final
String
selectionForwardAction
```

Name of the Action for extending the selection
by moving the caret logically forward one position.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionForwardAction

public static final

String

selectionForwardAction

Name of the Action for extending the selection
by moving the caret logically forward one position.

selectionBackwardAction

```java
public static final
String
selectionBackwardAction
```

Name of the Action for extending the selection
by moving the caret logically backward one position.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionBackwardAction

public static final

String

selectionBackwardAction

Name of the Action for extending the selection
by moving the caret logically backward one position.

upAction

```java
public static final
String
upAction
```

Name of the Action for moving the caret
logically upward one position.

**See Also:** getActions()

,

Constant Field Values

---

#### upAction

public static final

String

upAction

Name of the Action for moving the caret
logically upward one position.

downAction

```java
public static final
String
downAction
```

Name of the Action for moving the caret
logically downward one position.

**See Also:** getActions()

,

Constant Field Values

---

#### downAction

public static final

String

downAction

Name of the Action for moving the caret
logically downward one position.

selectionUpAction

```java
public static final
String
selectionUpAction
```

Name of the Action for moving the caret
logically upward one position, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionUpAction

public static final

String

selectionUpAction

Name of the Action for moving the caret
logically upward one position, extending the selection.

selectionDownAction

```java
public static final
String
selectionDownAction
```

Name of the Action for moving the caret
logically downward one position, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionDownAction

public static final

String

selectionDownAction

Name of the Action for moving the caret
logically downward one position, extending the selection.

beginWordAction

```java
public static final
String
beginWordAction
```

Name of the

Action

for moving the caret
to the beginning of a word.

**See Also:** getActions()

,

Constant Field Values

---

#### beginWordAction

public static final

String

beginWordAction

Name of the

Action

for moving the caret
to the beginning of a word.

endWordAction

```java
public static final
String
endWordAction
```

Name of the Action for moving the caret
to the end of a word.

**See Also:** getActions()

,

Constant Field Values

---

#### endWordAction

public static final

String

endWordAction

Name of the Action for moving the caret
to the end of a word.

selectionBeginWordAction

```java
public static final
String
selectionBeginWordAction
```

Name of the

Action

for moving the caret
to the beginning of a word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionBeginWordAction

public static final

String

selectionBeginWordAction

Name of the

Action

for moving the caret
to the beginning of a word, extending the selection.

selectionEndWordAction

```java
public static final
String
selectionEndWordAction
```

Name of the Action for moving the caret
to the end of a word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionEndWordAction

public static final

String

selectionEndWordAction

Name of the Action for moving the caret
to the end of a word, extending the selection.

previousWordAction

```java
public static final
String
previousWordAction
```

Name of the

Action

for moving the caret to the
beginning of the previous word.

**See Also:** getActions()

,

Constant Field Values

---

#### previousWordAction

public static final

String

previousWordAction

Name of the

Action

for moving the caret to the
beginning of the previous word.

nextWordAction

```java
public static final
String
nextWordAction
```

Name of the

Action

for moving the caret to the
beginning of the next word.

**See Also:** getActions()

,

Constant Field Values

---

#### nextWordAction

public static final

String

nextWordAction

Name of the

Action

for moving the caret to the
beginning of the next word.

selectionPreviousWordAction

```java
public static final
String
selectionPreviousWordAction
```

Name of the

Action

for moving the selection to the
beginning of the previous word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionPreviousWordAction

public static final

String

selectionPreviousWordAction

Name of the

Action

for moving the selection to the
beginning of the previous word, extending the selection.

selectionNextWordAction

```java
public static final
String
selectionNextWordAction
```

Name of the

Action

for moving the selection to the
beginning of the next word, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionNextWordAction

public static final

String

selectionNextWordAction

Name of the

Action

for moving the selection to the
beginning of the next word, extending the selection.

beginLineAction

```java
public static final
String
beginLineAction
```

Name of the

Action

for moving the caret
to the beginning of a line.

**See Also:** getActions()

,

Constant Field Values

---

#### beginLineAction

public static final

String

beginLineAction

Name of the

Action

for moving the caret
to the beginning of a line.

endLineAction

```java
public static final
String
endLineAction
```

Name of the

Action

for moving the caret
to the end of a line.

**See Also:** getActions()

,

Constant Field Values

---

#### endLineAction

public static final

String

endLineAction

Name of the

Action

for moving the caret
to the end of a line.

selectionBeginLineAction

```java
public static final
String
selectionBeginLineAction
```

Name of the

Action

for moving the caret
to the beginning of a line, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionBeginLineAction

public static final

String

selectionBeginLineAction

Name of the

Action

for moving the caret
to the beginning of a line, extending the selection.

selectionEndLineAction

```java
public static final
String
selectionEndLineAction
```

Name of the

Action

for moving the caret
to the end of a line, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionEndLineAction

public static final

String

selectionEndLineAction

Name of the

Action

for moving the caret
to the end of a line, extending the selection.

beginParagraphAction

```java
public static final
String
beginParagraphAction
```

Name of the

Action

for moving the caret
to the beginning of a paragraph.

**See Also:** getActions()

,

Constant Field Values

---

#### beginParagraphAction

public static final

String

beginParagraphAction

Name of the

Action

for moving the caret
to the beginning of a paragraph.

endParagraphAction

```java
public static final
String
endParagraphAction
```

Name of the

Action

for moving the caret
to the end of a paragraph.

**See Also:** getActions()

,

Constant Field Values

---

#### endParagraphAction

public static final

String

endParagraphAction

Name of the

Action

for moving the caret
to the end of a paragraph.

selectionBeginParagraphAction

```java
public static final
String
selectionBeginParagraphAction
```

Name of the

Action

for moving the caret
to the beginning of a paragraph, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionBeginParagraphAction

public static final

String

selectionBeginParagraphAction

Name of the

Action

for moving the caret
to the beginning of a paragraph, extending the selection.

selectionEndParagraphAction

```java
public static final
String
selectionEndParagraphAction
```

Name of the

Action

for moving the caret
to the end of a paragraph, extending the selection.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionEndParagraphAction

public static final

String

selectionEndParagraphAction

Name of the

Action

for moving the caret
to the end of a paragraph, extending the selection.

beginAction

```java
public static final
String
beginAction
```

Name of the

Action

for moving the caret
to the beginning of the document.

**See Also:** getActions()

,

Constant Field Values

---

#### beginAction

public static final

String

beginAction

Name of the

Action

for moving the caret
to the beginning of the document.

endAction

```java
public static final
String
endAction
```

Name of the

Action

for moving the caret
to the end of the document.

**See Also:** getActions()

,

Constant Field Values

---

#### endAction

public static final

String

endAction

Name of the

Action

for moving the caret
to the end of the document.

selectionBeginAction

```java
public static final
String
selectionBeginAction
```

Name of the

Action

for moving the caret
to the beginning of the document.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionBeginAction

public static final

String

selectionBeginAction

Name of the

Action

for moving the caret
to the beginning of the document.

selectionEndAction

```java
public static final
String
selectionEndAction
```

Name of the Action for moving the caret
to the end of the document.

**See Also:** getActions()

,

Constant Field Values

---

#### selectionEndAction

public static final

String

selectionEndAction

Name of the Action for moving the caret
to the end of the document.

selectWordAction

```java
public static final
String
selectWordAction
```

Name of the Action for selecting a word around the caret.

**See Also:** getActions()

,

Constant Field Values

---

#### selectWordAction

public static final

String

selectWordAction

Name of the Action for selecting a word around the caret.

selectLineAction

```java
public static final
String
selectLineAction
```

Name of the Action for selecting a line around the caret.

**See Also:** getActions()

,

Constant Field Values

---

#### selectLineAction

public static final

String

selectLineAction

Name of the Action for selecting a line around the caret.

selectParagraphAction

```java
public static final
String
selectParagraphAction
```

Name of the Action for selecting a paragraph around the caret.

**See Also:** getActions()

,

Constant Field Values

---

#### selectParagraphAction

public static final

String

selectParagraphAction

Name of the Action for selecting a paragraph around the caret.

selectAllAction

```java
public static final
String
selectAllAction
```

Name of the Action for selecting the entire document

**See Also:** getActions()

,

Constant Field Values

---

#### selectAllAction

public static final

String

selectAllAction

Name of the Action for selecting the entire document

defaultKeyTypedAction

```java
public static final
String
defaultKeyTypedAction
```

Name of the action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

**See Also:** getActions()

,

Constant Field Values

---

#### defaultKeyTypedAction

public static final

String

defaultKeyTypedAction

Name of the action that is executed by default if
a

key typed event

is received and there
is no keymap entry.

Constructor Detail

- DefaultEditorKit

```java
public DefaultEditorKit()
```

default constructor for DefaultEditorKit

---

#### Constructor Detail

DefaultEditorKit

```java
public DefaultEditorKit()
```

default constructor for DefaultEditorKit

---

#### DefaultEditorKit

public DefaultEditorKit()

default constructor for DefaultEditorKit

Method Detail

- getContentType

```java
public
String
getContentType()
```

Gets the MIME type of the data that this
kit represents support for. The default
is

text/plain

.

**Specified by:** getContentType

in class

EditorKit
**Returns:** the type

- getViewFactory

```java
public
ViewFactory
getViewFactory()
```

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. The default is to have the UI produce the
factory, so this method has no implementation.

**Specified by:** getViewFactory

in class

EditorKit
**Returns:** the view factory

- getActions

```java
public
Action
[] getActions()
```

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

**Specified by:** getActions

in class

EditorKit
**Returns:** the command list

- createCaret

```java
public
Caret
createCaret()
```

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

**Specified by:** createCaret

in class

EditorKit
**Returns:** the caret

- createDefaultDocument

```java
public
Document
createDefaultDocument()
```

Creates an uninitialized text storage model (PlainDocument)
that is appropriate for this type of editor.

**Specified by:** createDefaultDocument

in class

EditorKit
**Returns:** the model

- read

```java
public void read​(
InputStream
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Specified by:** read

in class

EditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- write

```java
public void write​(
OutputStream
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

**Specified by:** write

in class

EditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content >=0.
**Parameters:** len

- The amount to write out >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- read

```java
public void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream, which will be
treated as plain text.

**Specified by:** read

in class

EditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- write

```java
public void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
as plain text.

**Specified by:** write

in class

EditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content from >=0.
**Parameters:** len

- The amount to write out >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos is not within 0 and
the length of the document.

---

#### Method Detail

getContentType

```java
public
String
getContentType()
```

Gets the MIME type of the data that this
kit represents support for. The default
is

text/plain

.

**Specified by:** getContentType

in class

EditorKit
**Returns:** the type

---

#### getContentType

public

String

getContentType()

Gets the MIME type of the data that this
kit represents support for. The default
is

text/plain

.

getViewFactory

```java
public
ViewFactory
getViewFactory()
```

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. The default is to have the UI produce the
factory, so this method has no implementation.

**Specified by:** getViewFactory

in class

EditorKit
**Returns:** the view factory

---

#### getViewFactory

public

ViewFactory

getViewFactory()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. The default is to have the UI produce the
factory, so this method has no implementation.

getActions

```java
public
Action
[] getActions()
```

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

**Specified by:** getActions

in class

EditorKit
**Returns:** the command list

---

#### getActions

public

Action

[] getActions()

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

createCaret

```java
public
Caret
createCaret()
```

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

**Specified by:** createCaret

in class

EditorKit
**Returns:** the caret

---

#### createCaret

public

Caret

createCaret()

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

createDefaultDocument

```java
public
Document
createDefaultDocument()
```

Creates an uninitialized text storage model (PlainDocument)
that is appropriate for this type of editor.

**Specified by:** createDefaultDocument

in class

EditorKit
**Returns:** the model

---

#### createDefaultDocument

public

Document

createDefaultDocument()

Creates an uninitialized text storage model (PlainDocument)
that is appropriate for this type of editor.

read

```java
public void read​(
InputStream
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Specified by:** read

in class

EditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### read

public void read​(

InputStream

in,

Document

doc,
int pos)
throws

IOException

,

BadLocationException

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

write

```java
public void write​(
OutputStream
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

**Specified by:** write

in class

EditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content >=0.
**Parameters:** len

- The amount to write out >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### write

public void write​(

OutputStream

out,

Document

doc,
int pos,
int len)
throws

IOException

,

BadLocationException

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

read

```java
public void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream, which will be
treated as plain text.

**Specified by:** read

in class

EditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### read

public void read​(

Reader

in,

Document

doc,
int pos)
throws

IOException

,

BadLocationException

Inserts content from the given stream, which will be
treated as plain text.

write

```java
public void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
as plain text.

**Specified by:** write

in class

EditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content from >=0.
**Parameters:** len

- The amount to write out >=0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos is not within 0 and
the length of the document.

---

#### write

public void write​(

Writer

out,

Document

doc,
int pos,
int len)
throws

IOException

,

BadLocationException

Writes content from a document to the given stream
as plain text.

---

