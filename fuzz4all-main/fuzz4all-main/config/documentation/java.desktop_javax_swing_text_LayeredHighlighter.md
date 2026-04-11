# Class LayeredHighlighter

**Source:** `java.desktop\javax\swing\text\LayeredHighlighter.html`

### Class Description

```java
public abstract class
LayeredHighlighter

extends
Object

implements
Highlighter
```

**All Implemented Interfaces:** Highlighter

---

### Field Details

*No entries found.*

### Constructor Details

#### public LayeredHighlighter()

*No description found.*

---

### Method Details

#### public abstract void paintLayeredHighlights​(
Graphics
g,
int p0,
int p1,

Shape
viewBounds,

JTextComponent
editor,

View
view)

When leaf Views (such as LabelView) are rendering they should
call into this method. If a highlight is in the given region it will
be drawn immediately.

**Parameters:**
- g

- Graphics used to draw
- p0

- starting offset of view
- p1

- ending offset of view
- viewBounds

- Bounds of View
- editor

- JTextComponent
- view

- View instance being rendered

---

### Additional Sections

#### Class LayeredHighlighter

java.lang.Object

- javax.swing.text.LayeredHighlighter

javax.swing.text.LayeredHighlighter

**All Implemented Interfaces:** Highlighter

**Direct Known Subclasses:** DefaultHighlighter

```java
public abstract class
LayeredHighlighter

extends
Object

implements
Highlighter
```

**See Also:** Highlighter

public abstract class

LayeredHighlighter

extends

Object

implements

Highlighter

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

LayeredHighlighter.LayerPainter

Layered highlight renderer.

- Nested classes/interfaces declared in interface javax.swing.text.

Highlighter

Highlighter.Highlight

,

Highlighter.HighlightPainter

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LayeredHighlighter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

paintLayeredHighlights

​(

Graphics

g,
int p0,
int p1,

Shape

viewBounds,

JTextComponent

editor,

View

view)

When leaf Views (such as LabelView) are rendering they should
call into this method.

- Methods declared in class java.lang.

Object

clone

,

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

- Methods declared in interface javax.swing.text.

Highlighter

addHighlight

,

changeHighlight

,

deinstall

,

getHighlights

,

install

,

paint

,

removeAllHighlights

,

removeHighlight

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

LayeredHighlighter.LayerPainter

Layered highlight renderer.

- Nested classes/interfaces declared in interface javax.swing.text.

Highlighter

Highlighter.Highlight

,

Highlighter.HighlightPainter

---

#### Nested Class Summary

Layered highlight renderer.

Nested classes/interfaces declared in interface javax.swing.text.

Highlighter

Highlighter.Highlight

,

Highlighter.HighlightPainter

---

#### Nested classes/interfaces declared in interface javax.swing.text. Highlighter

Constructor Summary

Constructors

Constructor

Description

LayeredHighlighter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

paintLayeredHighlights

​(

Graphics

g,
int p0,
int p1,

Shape

viewBounds,

JTextComponent

editor,

View

view)

When leaf Views (such as LabelView) are rendering they should
call into this method.

- Methods declared in class java.lang.

Object

clone

,

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

- Methods declared in interface javax.swing.text.

Highlighter

addHighlight

,

changeHighlight

,

deinstall

,

getHighlights

,

install

,

paint

,

removeAllHighlights

,

removeHighlight

---

#### Method Summary

When leaf Views (such as LabelView) are rendering they should
call into this method.

Methods declared in class java.lang.

Object

clone

,

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

Methods declared in interface javax.swing.text.

Highlighter

addHighlight

,

changeHighlight

,

deinstall

,

getHighlights

,

install

,

paint

,

removeAllHighlights

,

removeHighlight

---

#### Methods declared in interface javax.swing.text. Highlighter

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LayeredHighlighter

```java
public LayeredHighlighter()
```

============ METHOD DETAIL ==========

- Method Detail

- paintLayeredHighlights

```java
public abstract void paintLayeredHighlights​(
Graphics
g,
int p0,
int p1,

Shape
viewBounds,

JTextComponent
editor,

View
view)
```

When leaf Views (such as LabelView) are rendering they should
call into this method. If a highlight is in the given region it will
be drawn immediately.

**Parameters:** g

- Graphics used to draw
**Parameters:** p0

- starting offset of view
**Parameters:** p1

- ending offset of view
**Parameters:** viewBounds

- Bounds of View
**Parameters:** editor

- JTextComponent
**Parameters:** view

- View instance being rendered

Constructor Detail

- LayeredHighlighter

```java
public LayeredHighlighter()
```

---

#### Constructor Detail

LayeredHighlighter

```java
public LayeredHighlighter()
```

---

#### LayeredHighlighter

public LayeredHighlighter()

Method Detail

- paintLayeredHighlights

```java
public abstract void paintLayeredHighlights​(
Graphics
g,
int p0,
int p1,

Shape
viewBounds,

JTextComponent
editor,

View
view)
```

When leaf Views (such as LabelView) are rendering they should
call into this method. If a highlight is in the given region it will
be drawn immediately.

**Parameters:** g

- Graphics used to draw
**Parameters:** p0

- starting offset of view
**Parameters:** p1

- ending offset of view
**Parameters:** viewBounds

- Bounds of View
**Parameters:** editor

- JTextComponent
**Parameters:** view

- View instance being rendered

---

#### Method Detail

paintLayeredHighlights

```java
public abstract void paintLayeredHighlights​(
Graphics
g,
int p0,
int p1,

Shape
viewBounds,

JTextComponent
editor,

View
view)
```

When leaf Views (such as LabelView) are rendering they should
call into this method. If a highlight is in the given region it will
be drawn immediately.

**Parameters:** g

- Graphics used to draw
**Parameters:** p0

- starting offset of view
**Parameters:** p1

- ending offset of view
**Parameters:** viewBounds

- Bounds of View
**Parameters:** editor

- JTextComponent
**Parameters:** view

- View instance being rendered

---

#### paintLayeredHighlights

public abstract void paintLayeredHighlights​(

Graphics

g,
int p0,
int p1,

Shape

viewBounds,

JTextComponent

editor,

View

view)

When leaf Views (such as LabelView) are rendering they should
call into this method. If a highlight is in the given region it will
be drawn immediately.

---

