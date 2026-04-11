# Class RTFEditorKit

**Source:** `java.desktop\javax\swing\text\rtf\RTFEditorKit.html`

### Class Description

```java
public class
RTFEditorKit

extends
StyledEditorKit
```

This is the default implementation of RTF editing
functionality. The RTF support was not written by the
Swing team. In the future we hope to improve the support
provided.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RTFEditorKit()

Constructs an RTFEditorKit.

---

### Method Details

#### public
String
getContentType()

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/rtf

.

**Overrides:**
- getContentType

in class

DefaultEditorKit

**Returns:**
- the type

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

Insert content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Overrides:**
- read

in class

DefaultEditorKit

**Parameters:**
- in

- The stream to read from
- doc

- The destination for the insertion.
- pos

- The location in the document to place the
content.

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

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

**Overrides:**
- write

in class

DefaultEditorKit

**Parameters:**
- out

- The stream to write to
- doc

- The source for the write.
- pos

- The location in the document to fetch the
content.
- len

- The amount to write out.

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

Insert content from the given stream, which will be
treated as plain text.

**Overrides:**
- read

in class

DefaultEditorKit

**Parameters:**
- in

- The stream to read from
- doc

- The destination for the insertion.
- pos

- The location in the document to place the
content.

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

Write content from a document to the given stream
as plain text.

**Overrides:**
- write

in class

DefaultEditorKit

**Parameters:**
- out

- The stream to write to
- doc

- The source for the write.
- pos

- The location in the document to fetch the
content.
- len

- The amount to write out.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

### Additional Sections

#### Class RTFEditorKit

java.lang.Object

- javax.swing.text.EditorKit
- - javax.swing.text.DefaultEditorKit
- - javax.swing.text.StyledEditorKit
- - javax.swing.text.rtf.RTFEditorKit

javax.swing.text.EditorKit

- javax.swing.text.DefaultEditorKit
- - javax.swing.text.StyledEditorKit
- - javax.swing.text.rtf.RTFEditorKit

javax.swing.text.DefaultEditorKit

- javax.swing.text.StyledEditorKit
- - javax.swing.text.rtf.RTFEditorKit

javax.swing.text.StyledEditorKit

- javax.swing.text.rtf.RTFEditorKit

javax.swing.text.rtf.RTFEditorKit

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
RTFEditorKit

extends
StyledEditorKit
```

This is the default implementation of RTF editing
functionality. The RTF support was not written by the
Swing team. In the future we hope to improve the support
provided.

**See Also:** Serialized Form

public class

RTFEditorKit

extends

StyledEditorKit

This is the default implementation of RTF editing
functionality. The RTF support was not written by the
Swing team. In the future we hope to improve the support
provided.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.text.

StyledEditorKit

StyledEditorKit.AlignmentAction

,

StyledEditorKit.BoldAction

,

StyledEditorKit.FontFamilyAction

,

StyledEditorKit.FontSizeAction

,

StyledEditorKit.ForegroundAction

,

StyledEditorKit.ItalicAction

,

StyledEditorKit.StyledTextAction

,

StyledEditorKit.UnderlineAction

- Nested classes/interfaces declared in class javax.swing.text.

DefaultEditorKit

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.text.

DefaultEditorKit

backwardAction

,

beepAction

,

beginAction

,

beginLineAction

,

beginParagraphAction

,

beginWordAction

,

copyAction

,

cutAction

,

defaultKeyTypedAction

,

deleteNextCharAction

,

deleteNextWordAction

,

deletePrevCharAction

,

deletePrevWordAction

,

downAction

,

endAction

,

endLineAction

,

EndOfLineStringProperty

,

endParagraphAction

,

endWordAction

,

forwardAction

,

insertBreakAction

,

insertContentAction

,

insertTabAction

,

nextWordAction

,

pageDownAction

,

pageUpAction

,

pasteAction

,

previousWordAction

,

readOnlyAction

,

selectAllAction

,

selectionBackwardAction

,

selectionBeginAction

,

selectionBeginLineAction

,

selectionBeginParagraphAction

,

selectionBeginWordAction

,

selectionDownAction

,

selectionEndAction

,

selectionEndLineAction

,

selectionEndParagraphAction

,

selectionEndWordAction

,

selectionForwardAction

,

selectionNextWordAction

,

selectionPreviousWordAction

,

selectionUpAction

,

selectLineAction

,

selectParagraphAction

,

selectWordAction

,

upAction

,

writableAction

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RTFEditorKit

()

Constructs an RTFEditorKit.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getContentType

()

Get the MIME type of the data that this
kit represents support for.

void

read

​(

InputStream

in,

Document

doc,
int pos)

Insert content from the given stream which is expected
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

Insert content from the given stream, which will be
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

Write content from a document to the given stream
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

Write content from a document to the given stream
as plain text.

- Methods declared in class javax.swing.text.

StyledEditorKit

clone

,

createDefaultDocument

,

createInputAttributes

,

deinstall

,

getActions

,

getCharacterAttributeRun

,

getInputAttributes

,

getViewFactory

,

install

- Methods declared in class javax.swing.text.

DefaultEditorKit

createCaret

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

- Nested classes/interfaces declared in class javax.swing.text.

StyledEditorKit

StyledEditorKit.AlignmentAction

,

StyledEditorKit.BoldAction

,

StyledEditorKit.FontFamilyAction

,

StyledEditorKit.FontSizeAction

,

StyledEditorKit.ForegroundAction

,

StyledEditorKit.ItalicAction

,

StyledEditorKit.StyledTextAction

,

StyledEditorKit.UnderlineAction

- Nested classes/interfaces declared in class javax.swing.text.

DefaultEditorKit

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.text.

StyledEditorKit

StyledEditorKit.AlignmentAction

,

StyledEditorKit.BoldAction

,

StyledEditorKit.FontFamilyAction

,

StyledEditorKit.FontSizeAction

,

StyledEditorKit.ForegroundAction

,

StyledEditorKit.ItalicAction

,

StyledEditorKit.StyledTextAction

,

StyledEditorKit.UnderlineAction

---

#### Nested classes/interfaces declared in class javax.swing.text. StyledEditorKit

Nested classes/interfaces declared in class javax.swing.text.

DefaultEditorKit

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

---

#### Nested classes/interfaces declared in class javax.swing.text. DefaultEditorKit

Field Summary

- Fields declared in class javax.swing.text.

DefaultEditorKit

backwardAction

,

beepAction

,

beginAction

,

beginLineAction

,

beginParagraphAction

,

beginWordAction

,

copyAction

,

cutAction

,

defaultKeyTypedAction

,

deleteNextCharAction

,

deleteNextWordAction

,

deletePrevCharAction

,

deletePrevWordAction

,

downAction

,

endAction

,

endLineAction

,

EndOfLineStringProperty

,

endParagraphAction

,

endWordAction

,

forwardAction

,

insertBreakAction

,

insertContentAction

,

insertTabAction

,

nextWordAction

,

pageDownAction

,

pageUpAction

,

pasteAction

,

previousWordAction

,

readOnlyAction

,

selectAllAction

,

selectionBackwardAction

,

selectionBeginAction

,

selectionBeginLineAction

,

selectionBeginParagraphAction

,

selectionBeginWordAction

,

selectionDownAction

,

selectionEndAction

,

selectionEndLineAction

,

selectionEndParagraphAction

,

selectionEndWordAction

,

selectionForwardAction

,

selectionNextWordAction

,

selectionPreviousWordAction

,

selectionUpAction

,

selectLineAction

,

selectParagraphAction

,

selectWordAction

,

upAction

,

writableAction

---

#### Field Summary

Fields declared in class javax.swing.text.

DefaultEditorKit

backwardAction

,

beepAction

,

beginAction

,

beginLineAction

,

beginParagraphAction

,

beginWordAction

,

copyAction

,

cutAction

,

defaultKeyTypedAction

,

deleteNextCharAction

,

deleteNextWordAction

,

deletePrevCharAction

,

deletePrevWordAction

,

downAction

,

endAction

,

endLineAction

,

EndOfLineStringProperty

,

endParagraphAction

,

endWordAction

,

forwardAction

,

insertBreakAction

,

insertContentAction

,

insertTabAction

,

nextWordAction

,

pageDownAction

,

pageUpAction

,

pasteAction

,

previousWordAction

,

readOnlyAction

,

selectAllAction

,

selectionBackwardAction

,

selectionBeginAction

,

selectionBeginLineAction

,

selectionBeginParagraphAction

,

selectionBeginWordAction

,

selectionDownAction

,

selectionEndAction

,

selectionEndLineAction

,

selectionEndParagraphAction

,

selectionEndWordAction

,

selectionForwardAction

,

selectionNextWordAction

,

selectionPreviousWordAction

,

selectionUpAction

,

selectLineAction

,

selectParagraphAction

,

selectWordAction

,

upAction

,

writableAction

---

#### Fields declared in class javax.swing.text. DefaultEditorKit

Constructor Summary

Constructors

Constructor

Description

RTFEditorKit

()

Constructs an RTFEditorKit.

---

#### Constructor Summary

Constructs an RTFEditorKit.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getContentType

()

Get the MIME type of the data that this
kit represents support for.

void

read

​(

InputStream

in,

Document

doc,
int pos)

Insert content from the given stream which is expected
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

Insert content from the given stream, which will be
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

Write content from a document to the given stream
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

Write content from a document to the given stream
as plain text.

- Methods declared in class javax.swing.text.

StyledEditorKit

clone

,

createDefaultDocument

,

createInputAttributes

,

deinstall

,

getActions

,

getCharacterAttributeRun

,

getInputAttributes

,

getViewFactory

,

install

- Methods declared in class javax.swing.text.

DefaultEditorKit

createCaret

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

Get the MIME type of the data that this
kit represents support for.

Insert content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

Insert content from the given stream, which will be
treated as plain text.

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

Write content from a document to the given stream
as plain text.

Methods declared in class javax.swing.text.

StyledEditorKit

clone

,

createDefaultDocument

,

createInputAttributes

,

deinstall

,

getActions

,

getCharacterAttributeRun

,

getInputAttributes

,

getViewFactory

,

install

---

#### Methods declared in class javax.swing.text. StyledEditorKit

Methods declared in class javax.swing.text.

DefaultEditorKit

createCaret

---

#### Methods declared in class javax.swing.text. DefaultEditorKit

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RTFEditorKit

```java
public RTFEditorKit()
```

Constructs an RTFEditorKit.

============ METHOD DETAIL ==========

- Method Detail

- getContentType

```java
public
String
getContentType()
```

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/rtf

.

**Overrides:** getContentType

in class

DefaultEditorKit
**Returns:** the type

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

Insert content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Overrides:** read

in class

DefaultEditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content.
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

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

**Overrides:** write

in class

DefaultEditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.
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

Insert content from the given stream, which will be
treated as plain text.

**Overrides:** read

in class

DefaultEditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content.
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

Write content from a document to the given stream
as plain text.

**Overrides:** write

in class

DefaultEditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

Constructor Detail

- RTFEditorKit

```java
public RTFEditorKit()
```

Constructs an RTFEditorKit.

---

#### Constructor Detail

RTFEditorKit

```java
public RTFEditorKit()
```

Constructs an RTFEditorKit.

---

#### RTFEditorKit

public RTFEditorKit()

Constructs an RTFEditorKit.

Method Detail

- getContentType

```java
public
String
getContentType()
```

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/rtf

.

**Overrides:** getContentType

in class

DefaultEditorKit
**Returns:** the type

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

Insert content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Overrides:** read

in class

DefaultEditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content.
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

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

**Overrides:** write

in class

DefaultEditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.
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

Insert content from the given stream, which will be
treated as plain text.

**Overrides:** read

in class

DefaultEditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content.
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

Write content from a document to the given stream
as plain text.

**Overrides:** write

in class

DefaultEditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### Method Detail

getContentType

```java
public
String
getContentType()
```

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/rtf

.

**Overrides:** getContentType

in class

DefaultEditorKit
**Returns:** the type

---

#### getContentType

public

String

getContentType()

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/rtf

.

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

Insert content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Overrides:** read

in class

DefaultEditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content.
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

Insert content from the given stream which is expected
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

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

**Overrides:** write

in class

DefaultEditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.
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

Write content from a document to the given stream
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

Insert content from the given stream, which will be
treated as plain text.

**Overrides:** read

in class

DefaultEditorKit
**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content.
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

Insert content from the given stream, which will be
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

Write content from a document to the given stream
as plain text.

**Overrides:** write

in class

DefaultEditorKit
**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

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

Write content from a document to the given stream
as plain text.

---

