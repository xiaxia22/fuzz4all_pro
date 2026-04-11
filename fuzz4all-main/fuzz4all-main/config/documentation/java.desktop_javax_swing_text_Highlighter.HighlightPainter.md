# Interface Highlighter.HighlightPainter

**Source:** `java.desktop\javax\swing\text\Highlighter.HighlightPainter.html`

### Class Description

```java
public static interface
Highlighter.HighlightPainter
```

Highlight renderer.

**All Known Implementing Classes:** DefaultHighlighter.DefaultHighlightPainter

,

LayeredHighlighter.LayerPainter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void paint​(
Graphics
g,
int p0,
int p1,

Shape
bounds,

JTextComponent
c)

Renders the highlight.

**Parameters:**
- g

- the graphics context
- p0

- the starting offset in the model >= 0
- p1

- the ending offset in the model >= p0
- bounds

- the bounding box for the highlight
- c

- the editor

---

### Additional Sections

#### Interface Highlighter.HighlightPainter

**All Known Implementing Classes:** DefaultHighlighter.DefaultHighlightPainter

,

LayeredHighlighter.LayerPainter

**Enclosing interface:** Highlighter

```java
public static interface
Highlighter.HighlightPainter
```

Highlight renderer.

public static interface

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

void

paint

​(

Graphics

g,
int p0,
int p1,

Shape

bounds,

JTextComponent

c)

Renders the highlight.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

paint

​(

Graphics

g,
int p0,
int p1,

Shape

bounds,

JTextComponent

c)

Renders the highlight.

---

#### Method Summary

Renders the highlight.

============ METHOD DETAIL ==========

- Method Detail

- paint

```java
void paint​(
Graphics
g,
int p0,
int p1,

Shape
bounds,

JTextComponent
c)
```

Renders the highlight.

**Parameters:** g

- the graphics context
**Parameters:** p0

- the starting offset in the model >= 0
**Parameters:** p1

- the ending offset in the model >= p0
**Parameters:** bounds

- the bounding box for the highlight
**Parameters:** c

- the editor

Method Detail

- paint

```java
void paint​(
Graphics
g,
int p0,
int p1,

Shape
bounds,

JTextComponent
c)
```

Renders the highlight.

**Parameters:** g

- the graphics context
**Parameters:** p0

- the starting offset in the model >= 0
**Parameters:** p1

- the ending offset in the model >= p0
**Parameters:** bounds

- the bounding box for the highlight
**Parameters:** c

- the editor

---

#### Method Detail

paint

```java
void paint​(
Graphics
g,
int p0,
int p1,

Shape
bounds,

JTextComponent
c)
```

Renders the highlight.

**Parameters:** g

- the graphics context
**Parameters:** p0

- the starting offset in the model >= 0
**Parameters:** p1

- the ending offset in the model >= p0
**Parameters:** bounds

- the bounding box for the highlight
**Parameters:** c

- the editor

---

#### paint

void paint​(

Graphics

g,
int p0,
int p1,

Shape

bounds,

JTextComponent

c)

Renders the highlight.

---

