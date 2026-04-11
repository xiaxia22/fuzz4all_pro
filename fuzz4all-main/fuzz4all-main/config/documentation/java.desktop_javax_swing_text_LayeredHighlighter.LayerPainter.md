# Class LayeredHighlighter.LayerPainter

**Source:** `java.desktop\javax\swing\text\LayeredHighlighter.LayerPainter.html`

### Class Description

```java
public abstract static class
LayeredHighlighter.LayerPainter

extends
Object

implements
Highlighter.HighlightPainter
```

Layered highlight renderer.

**All Implemented Interfaces:** Highlighter.HighlightPainter

---

### Field Details

*No entries found.*

### Constructor Details

#### public LayerPainter()

*No description found.*

---

### Method Details

#### public abstract
Shape
paintLayer​(
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

**Returns:**
- a shape

---

### Additional Sections

#### Class LayeredHighlighter.LayerPainter

java.lang.Object

- javax.swing.text.LayeredHighlighter.LayerPainter

javax.swing.text.LayeredHighlighter.LayerPainter

**All Implemented Interfaces:** Highlighter.HighlightPainter

**Direct Known Subclasses:** DefaultHighlighter.DefaultHighlightPainter

**Enclosing class:** LayeredHighlighter

```java
public abstract static class
LayeredHighlighter.LayerPainter

extends
Object

implements
Highlighter.HighlightPainter
```

Layered highlight renderer.

public abstract static class

LayeredHighlighter.LayerPainter

extends

Object

implements

Highlighter.HighlightPainter

Layered highlight renderer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LayerPainter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Shape

paintLayer

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

Highlighter.HighlightPainter

paint

Constructor Summary

Constructors

Constructor

Description

LayerPainter

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

abstract

Shape

paintLayer

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

Highlighter.HighlightPainter

paint

---

#### Method Summary

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

Highlighter.HighlightPainter

paint

---

#### Methods declared in interface javax.swing.text. Highlighter.HighlightPainter

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LayerPainter

```java
public LayerPainter()
```

============ METHOD DETAIL ==========

- Method Detail

- paintLayer

```java
public abstract
Shape
paintLayer​(
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
**Returns:** a shape

Constructor Detail

- LayerPainter

```java
public LayerPainter()
```

---

#### Constructor Detail

LayerPainter

```java
public LayerPainter()
```

---

#### LayerPainter

public LayerPainter()

Method Detail

- paintLayer

```java
public abstract
Shape
paintLayer​(
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
**Returns:** a shape

---

#### Method Detail

paintLayer

```java
public abstract
Shape
paintLayer​(
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
**Returns:** a shape

---

#### paintLayer

public abstract

Shape

paintLayer​(

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

---

