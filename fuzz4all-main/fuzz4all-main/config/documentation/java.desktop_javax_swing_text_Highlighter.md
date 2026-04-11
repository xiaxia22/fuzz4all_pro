# Interface Highlighter

**Source:** `java.desktop\javax\swing\text\Highlighter.html`

### Class Description

```java
public interface
Highlighter
```

An interface for an object that allows one to mark up the background
with colored areas.

**All Known Implementing Classes:** BasicTextUI.BasicHighlighter

,

DefaultHighlighter

,

LayeredHighlighter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void install​(
JTextComponent
c)

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface.

**Parameters:**
- c

- the JTextComponent editor

---

#### void deinstall​(
JTextComponent
c)

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

**Parameters:**
- c

- the JTextComponent editor

---

#### void paint​(
Graphics
g)

Renders the highlights.

**Parameters:**
- g

- the graphics context.

---

#### Object
addHighlight​(int p0,
int p1,

Highlighter.HighlightPainter
p)
throws
BadLocationException

Adds a highlight to the view. Returns a tag that can be used
to refer to the highlight.

**Parameters:**
- p0

- the beginning of the range >= 0
- p1

- the end of the range >= p0
- p

- the painter to use for the actual highlighting

**Returns:**
- an object that refers to the highlight

**Throws:**
- BadLocationException

- for an invalid range specification

---

#### void removeHighlight​(
Object
tag)

Removes a highlight from the view.

**Parameters:**
- tag

- which highlight to remove

---

#### void removeAllHighlights()

Removes all highlights this highlighter is responsible for.

---

#### void changeHighlight​(
Object
tag,
int p0,
int p1)
throws
BadLocationException

Changes the given highlight to span a different portion of
the document. This may be more efficient than a remove/add
when a selection is expanding/shrinking (such as a sweep
with a mouse) by damaging only what changed.

**Parameters:**
- tag

- which highlight to change
- p0

- the beginning of the range >= 0
- p1

- the end of the range >= p0

**Throws:**
- BadLocationException

- for an invalid range specification

---

#### Highlighter.Highlight
[] getHighlights()

Fetches the current list of highlights.

**Returns:**
- the highlight list

---

### Additional Sections

#### Interface Highlighter

**All Known Implementing Classes:** BasicTextUI.BasicHighlighter

,

DefaultHighlighter

,

LayeredHighlighter

```java
public interface
Highlighter
```

An interface for an object that allows one to mark up the background
with colored areas.

public interface

Highlighter

An interface for an object that allows one to mark up the background
with colored areas.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

Highlighter.Highlight

A highlight.

static interface

Highlighter.HighlightPainter

Highlight renderer.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

addHighlight

​(int p0,
int p1,

Highlighter.HighlightPainter

p)

Adds a highlight to the view.

void

changeHighlight

​(

Object

tag,
int p0,
int p1)

Changes the given highlight to span a different portion of
the document.

void

deinstall

​(

JTextComponent

c)

Called when the UI is being removed from the
interface of a JTextComponent.

Highlighter.Highlight

[]

getHighlights

()

Fetches the current list of highlights.

void

install

​(

JTextComponent

c)

Called when the UI is being installed into the
interface of a JTextComponent.

void

paint

​(

Graphics

g)

Renders the highlights.

void

removeAllHighlights

()

Removes all highlights this highlighter is responsible for.

void

removeHighlight

​(

Object

tag)

Removes a highlight from the view.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

Highlighter.Highlight

A highlight.

static interface

Highlighter.HighlightPainter

Highlight renderer.

---

#### Nested Class Summary

A highlight.

Highlight renderer.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

addHighlight

​(int p0,
int p1,

Highlighter.HighlightPainter

p)

Adds a highlight to the view.

void

changeHighlight

​(

Object

tag,
int p0,
int p1)

Changes the given highlight to span a different portion of
the document.

void

deinstall

​(

JTextComponent

c)

Called when the UI is being removed from the
interface of a JTextComponent.

Highlighter.Highlight

[]

getHighlights

()

Fetches the current list of highlights.

void

install

​(

JTextComponent

c)

Called when the UI is being installed into the
interface of a JTextComponent.

void

paint

​(

Graphics

g)

Renders the highlights.

void

removeAllHighlights

()

Removes all highlights this highlighter is responsible for.

void

removeHighlight

​(

Object

tag)

Removes a highlight from the view.

---

#### Method Summary

Adds a highlight to the view.

Changes the given highlight to span a different portion of
the document.

Called when the UI is being removed from the
interface of a JTextComponent.

Fetches the current list of highlights.

Called when the UI is being installed into the
interface of a JTextComponent.

Renders the highlights.

Removes all highlights this highlighter is responsible for.

Removes a highlight from the view.

============ METHOD DETAIL ==========

- Method Detail

- install

```java
void install​(
JTextComponent
c)
```

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface.

**Parameters:** c

- the JTextComponent editor

- deinstall

```java
void deinstall​(
JTextComponent
c)
```

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

**Parameters:** c

- the JTextComponent editor

- paint

```java
void paint​(
Graphics
g)
```

Renders the highlights.

**Parameters:** g

- the graphics context.

- addHighlight

```java
Object
addHighlight​(int p0,
int p1,

Highlighter.HighlightPainter
p)
throws
BadLocationException
```

Adds a highlight to the view. Returns a tag that can be used
to refer to the highlight.

**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Parameters:** p

- the painter to use for the actual highlighting
**Returns:** an object that refers to the highlight
**Throws:** BadLocationException

- for an invalid range specification

- removeHighlight

```java
void removeHighlight​(
Object
tag)
```

Removes a highlight from the view.

**Parameters:** tag

- which highlight to remove

- removeAllHighlights

```java
void removeAllHighlights()
```

Removes all highlights this highlighter is responsible for.

- changeHighlight

```java
void changeHighlight​(
Object
tag,
int p0,
int p1)
throws
BadLocationException
```

Changes the given highlight to span a different portion of
the document. This may be more efficient than a remove/add
when a selection is expanding/shrinking (such as a sweep
with a mouse) by damaging only what changed.

**Parameters:** tag

- which highlight to change
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Throws:** BadLocationException

- for an invalid range specification

- getHighlights

```java
Highlighter.Highlight
[] getHighlights()
```

Fetches the current list of highlights.

**Returns:** the highlight list

Method Detail

- install

```java
void install​(
JTextComponent
c)
```

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface.

**Parameters:** c

- the JTextComponent editor

- deinstall

```java
void deinstall​(
JTextComponent
c)
```

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

**Parameters:** c

- the JTextComponent editor

- paint

```java
void paint​(
Graphics
g)
```

Renders the highlights.

**Parameters:** g

- the graphics context.

- addHighlight

```java
Object
addHighlight​(int p0,
int p1,

Highlighter.HighlightPainter
p)
throws
BadLocationException
```

Adds a highlight to the view. Returns a tag that can be used
to refer to the highlight.

**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Parameters:** p

- the painter to use for the actual highlighting
**Returns:** an object that refers to the highlight
**Throws:** BadLocationException

- for an invalid range specification

- removeHighlight

```java
void removeHighlight​(
Object
tag)
```

Removes a highlight from the view.

**Parameters:** tag

- which highlight to remove

- removeAllHighlights

```java
void removeAllHighlights()
```

Removes all highlights this highlighter is responsible for.

- changeHighlight

```java
void changeHighlight​(
Object
tag,
int p0,
int p1)
throws
BadLocationException
```

Changes the given highlight to span a different portion of
the document. This may be more efficient than a remove/add
when a selection is expanding/shrinking (such as a sweep
with a mouse) by damaging only what changed.

**Parameters:** tag

- which highlight to change
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Throws:** BadLocationException

- for an invalid range specification

- getHighlights

```java
Highlighter.Highlight
[] getHighlights()
```

Fetches the current list of highlights.

**Returns:** the highlight list

---

#### Method Detail

install

```java
void install​(
JTextComponent
c)
```

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface.

**Parameters:** c

- the JTextComponent editor

---

#### install

void install​(

JTextComponent

c)

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface.

deinstall

```java
void deinstall​(
JTextComponent
c)
```

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

**Parameters:** c

- the JTextComponent editor

---

#### deinstall

void deinstall​(

JTextComponent

c)

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

paint

```java
void paint​(
Graphics
g)
```

Renders the highlights.

**Parameters:** g

- the graphics context.

---

#### paint

void paint​(

Graphics

g)

Renders the highlights.

addHighlight

```java
Object
addHighlight​(int p0,
int p1,

Highlighter.HighlightPainter
p)
throws
BadLocationException
```

Adds a highlight to the view. Returns a tag that can be used
to refer to the highlight.

**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Parameters:** p

- the painter to use for the actual highlighting
**Returns:** an object that refers to the highlight
**Throws:** BadLocationException

- for an invalid range specification

---

#### addHighlight

Object

addHighlight​(int p0,
int p1,

Highlighter.HighlightPainter

p)
throws

BadLocationException

Adds a highlight to the view. Returns a tag that can be used
to refer to the highlight.

removeHighlight

```java
void removeHighlight​(
Object
tag)
```

Removes a highlight from the view.

**Parameters:** tag

- which highlight to remove

---

#### removeHighlight

void removeHighlight​(

Object

tag)

Removes a highlight from the view.

removeAllHighlights

```java
void removeAllHighlights()
```

Removes all highlights this highlighter is responsible for.

---

#### removeAllHighlights

void removeAllHighlights()

Removes all highlights this highlighter is responsible for.

changeHighlight

```java
void changeHighlight​(
Object
tag,
int p0,
int p1)
throws
BadLocationException
```

Changes the given highlight to span a different portion of
the document. This may be more efficient than a remove/add
when a selection is expanding/shrinking (such as a sweep
with a mouse) by damaging only what changed.

**Parameters:** tag

- which highlight to change
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Throws:** BadLocationException

- for an invalid range specification

---

#### changeHighlight

void changeHighlight​(

Object

tag,
int p0,
int p1)
throws

BadLocationException

Changes the given highlight to span a different portion of
the document. This may be more efficient than a remove/add
when a selection is expanding/shrinking (such as a sweep
with a mouse) by damaging only what changed.

getHighlights

```java
Highlighter.Highlight
[] getHighlights()
```

Fetches the current list of highlights.

**Returns:** the highlight list

---

#### getHighlights

Highlighter.Highlight

[] getHighlights()

Fetches the current list of highlights.

---

