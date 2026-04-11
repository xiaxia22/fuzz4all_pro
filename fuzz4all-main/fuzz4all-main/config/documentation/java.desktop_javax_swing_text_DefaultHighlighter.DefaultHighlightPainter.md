# Class DefaultHighlighter.DefaultHighlightPainter

**Source:** `java.desktop\javax\swing\text\DefaultHighlighter.DefaultHighlightPainter.html`

### Class Description

```java
public static class
DefaultHighlighter.DefaultHighlightPainter

extends
LayeredHighlighter.LayerPainter
```

Simple highlight painter that fills a highlighted area with
a solid color.

**All Implemented Interfaces:** Highlighter.HighlightPainter

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultHighlightPainter​(
Color
c)

Constructs a new highlight painter. If

c

is null,
the JTextComponent will be queried for its selection color.

**Parameters:**
- c

- the color for the highlight

---

### Method Details

#### public
Color
getColor()

Returns the color of the highlight.

**Returns:**
- the color

---

#### public void paint​(
Graphics
g,
int offs0,
int offs1,

Shape
bounds,

JTextComponent
c)

Paints a highlight.

**Parameters:**
- g

- the graphics context
- offs0

- the starting model offset >= 0
- offs1

- the ending model offset >= offs1
- bounds

- the bounding box for the highlight
- c

- the editor

---

#### public
Shape
paintLayer​(
Graphics
g,
int offs0,
int offs1,

Shape
bounds,

JTextComponent
c,

View
view)

Paints a portion of a highlight.

**Specified by:**
- paintLayer

in class

LayeredHighlighter.LayerPainter

**Parameters:**
- g

- the graphics context
- offs0

- the starting model offset >= 0
- offs1

- the ending model offset >= offs1
- bounds

- the bounding box of the view, which is not
necessarily the region to paint.
- c

- the editor
- view

- View painting for

**Returns:**
- region drawing occurred in

---

### Additional Sections

#### Class DefaultHighlighter.DefaultHighlightPainter

java.lang.Object

- javax.swing.text.LayeredHighlighter.LayerPainter
- - javax.swing.text.DefaultHighlighter.DefaultHighlightPainter

javax.swing.text.LayeredHighlighter.LayerPainter

- javax.swing.text.DefaultHighlighter.DefaultHighlightPainter

javax.swing.text.DefaultHighlighter.DefaultHighlightPainter

**All Implemented Interfaces:** Highlighter.HighlightPainter

**Enclosing class:** DefaultHighlighter

```java
public static class
DefaultHighlighter.DefaultHighlightPainter

extends
LayeredHighlighter.LayerPainter
```

Simple highlight painter that fills a highlighted area with
a solid color.

public static class

DefaultHighlighter.DefaultHighlightPainter

extends

LayeredHighlighter.LayerPainter

Simple highlight painter that fills a highlighted area with
a solid color.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultHighlightPainter

​(

Color

c)

Constructs a new highlight painter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Color

getColor

()

Returns the color of the highlight.

void

paint

​(

Graphics

g,
int offs0,
int offs1,

Shape

bounds,

JTextComponent

c)

Paints a highlight.

Shape

paintLayer

​(

Graphics

g,
int offs0,
int offs1,

Shape

bounds,

JTextComponent

c,

View

view)

Paints a portion of a highlight.

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

Constructor Summary

Constructors

Constructor

Description

DefaultHighlightPainter

​(

Color

c)

Constructs a new highlight painter.

---

#### Constructor Summary

Constructs a new highlight painter.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Color

getColor

()

Returns the color of the highlight.

void

paint

​(

Graphics

g,
int offs0,
int offs1,

Shape

bounds,

JTextComponent

c)

Paints a highlight.

Shape

paintLayer

​(

Graphics

g,
int offs0,
int offs1,

Shape

bounds,

JTextComponent

c,

View

view)

Paints a portion of a highlight.

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

---

#### Method Summary

Returns the color of the highlight.

Paints a highlight.

Paints a portion of a highlight.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultHighlightPainter

```java
public DefaultHighlightPainter​(
Color
c)
```

Constructs a new highlight painter. If

c

is null,
the JTextComponent will be queried for its selection color.

**Parameters:** c

- the color for the highlight

============ METHOD DETAIL ==========

- Method Detail

- getColor

```java
public
Color
getColor()
```

Returns the color of the highlight.

**Returns:** the color

- paint

```java
public void paint​(
Graphics
g,
int offs0,
int offs1,

Shape
bounds,

JTextComponent
c)
```

Paints a highlight.

**Parameters:** g

- the graphics context
**Parameters:** offs0

- the starting model offset >= 0
**Parameters:** offs1

- the ending model offset >= offs1
**Parameters:** bounds

- the bounding box for the highlight
**Parameters:** c

- the editor

- paintLayer

```java
public
Shape
paintLayer​(
Graphics
g,
int offs0,
int offs1,

Shape
bounds,

JTextComponent
c,

View
view)
```

Paints a portion of a highlight.

**Specified by:** paintLayer

in class

LayeredHighlighter.LayerPainter
**Parameters:** g

- the graphics context
**Parameters:** offs0

- the starting model offset >= 0
**Parameters:** offs1

- the ending model offset >= offs1
**Parameters:** bounds

- the bounding box of the view, which is not
necessarily the region to paint.
**Parameters:** c

- the editor
**Parameters:** view

- View painting for
**Returns:** region drawing occurred in

Constructor Detail

- DefaultHighlightPainter

```java
public DefaultHighlightPainter​(
Color
c)
```

Constructs a new highlight painter. If

c

is null,
the JTextComponent will be queried for its selection color.

**Parameters:** c

- the color for the highlight

---

#### Constructor Detail

DefaultHighlightPainter

```java
public DefaultHighlightPainter​(
Color
c)
```

Constructs a new highlight painter. If

c

is null,
the JTextComponent will be queried for its selection color.

**Parameters:** c

- the color for the highlight

---

#### DefaultHighlightPainter

public DefaultHighlightPainter​(

Color

c)

Constructs a new highlight painter. If

c

is null,
the JTextComponent will be queried for its selection color.

Method Detail

- getColor

```java
public
Color
getColor()
```

Returns the color of the highlight.

**Returns:** the color

- paint

```java
public void paint​(
Graphics
g,
int offs0,
int offs1,

Shape
bounds,

JTextComponent
c)
```

Paints a highlight.

**Parameters:** g

- the graphics context
**Parameters:** offs0

- the starting model offset >= 0
**Parameters:** offs1

- the ending model offset >= offs1
**Parameters:** bounds

- the bounding box for the highlight
**Parameters:** c

- the editor

- paintLayer

```java
public
Shape
paintLayer​(
Graphics
g,
int offs0,
int offs1,

Shape
bounds,

JTextComponent
c,

View
view)
```

Paints a portion of a highlight.

**Specified by:** paintLayer

in class

LayeredHighlighter.LayerPainter
**Parameters:** g

- the graphics context
**Parameters:** offs0

- the starting model offset >= 0
**Parameters:** offs1

- the ending model offset >= offs1
**Parameters:** bounds

- the bounding box of the view, which is not
necessarily the region to paint.
**Parameters:** c

- the editor
**Parameters:** view

- View painting for
**Returns:** region drawing occurred in

---

#### Method Detail

getColor

```java
public
Color
getColor()
```

Returns the color of the highlight.

**Returns:** the color

---

#### getColor

public

Color

getColor()

Returns the color of the highlight.

paint

```java
public void paint​(
Graphics
g,
int offs0,
int offs1,

Shape
bounds,

JTextComponent
c)
```

Paints a highlight.

**Parameters:** g

- the graphics context
**Parameters:** offs0

- the starting model offset >= 0
**Parameters:** offs1

- the ending model offset >= offs1
**Parameters:** bounds

- the bounding box for the highlight
**Parameters:** c

- the editor

---

#### paint

public void paint​(

Graphics

g,
int offs0,
int offs1,

Shape

bounds,

JTextComponent

c)

Paints a highlight.

paintLayer

```java
public
Shape
paintLayer​(
Graphics
g,
int offs0,
int offs1,

Shape
bounds,

JTextComponent
c,

View
view)
```

Paints a portion of a highlight.

**Specified by:** paintLayer

in class

LayeredHighlighter.LayerPainter
**Parameters:** g

- the graphics context
**Parameters:** offs0

- the starting model offset >= 0
**Parameters:** offs1

- the ending model offset >= offs1
**Parameters:** bounds

- the bounding box of the view, which is not
necessarily the region to paint.
**Parameters:** c

- the editor
**Parameters:** view

- View painting for
**Returns:** region drawing occurred in

---

#### paintLayer

public

Shape

paintLayer​(

Graphics

g,
int offs0,
int offs1,

Shape

bounds,

JTextComponent

c,

View

view)

Paints a portion of a highlight.

---

