# Class DefaultHighlighter

**Source:** `java.desktop\javax\swing\text\DefaultHighlighter.html`

### Class Description

```java
public class
DefaultHighlighter

extends
LayeredHighlighter
```

Implements the Highlighter interfaces. Implements a simple highlight
painter that renders in a solid color.

**All Implemented Interfaces:** Highlighter

---

### Field Details

#### public static final
LayeredHighlighter.LayerPainter
DefaultPainter

Default implementation of LayeredHighlighter.LayerPainter that can
be used for painting highlights.

As of 1.4 this field is final.

---

### Constructor Details

#### public DefaultHighlighter()

Creates a new DefaultHighlighther object.

---

### Method Details

#### public void paint​(
Graphics
g)

Renders the highlights.

**Parameters:**
- g

- the graphics context

---

#### public void install​(
JTextComponent
c)

Called when the UI is being installed into the
interface of a JTextComponent. Installs the editor, and
removes any existing highlights.

**Parameters:**
- c

- the editor component

**See Also:**
- Highlighter.install(javax.swing.text.JTextComponent)

---

#### public void deinstall​(
JTextComponent
c)

Called when the UI is being removed from the interface of
a JTextComponent.

**Parameters:**
- c

- the component

**See Also:**
- Highlighter.deinstall(javax.swing.text.JTextComponent)

---

#### public
Object
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

- the start offset of the range to highlight >= 0
- p1

- the end offset of the range to highlight >= p0
- p

- the painter to use to actually render the highlight

**Returns:**
- an object that can be used as a tag
to refer to the highlight

**Throws:**
- BadLocationException

- if the specified location is invalid

---

#### public void removeHighlight​(
Object
tag)

Removes a highlight from the view.

**Parameters:**
- tag

- the reference to the highlight

---

#### public void removeAllHighlights()

Removes all highlights.

---

#### public void changeHighlight​(
Object
tag,
int p0,
int p1)
throws
BadLocationException

Changes a highlight.

**Parameters:**
- tag

- the highlight tag
- p0

- the beginning of the range >= 0
- p1

- the end of the range >= p0

**Throws:**
- BadLocationException

- if the specified location is invalid

---

#### public
Highlighter.Highlight
[] getHighlights()

Makes a copy of the highlights. Does not actually clone each highlight,
but only makes references to them.

**Returns:**
- the copy

**See Also:**
- Highlighter.getHighlights()

---

#### public void paintLayeredHighlights​(
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

**Specified by:**
- paintLayeredHighlights

in class

LayeredHighlighter

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

#### public void setDrawsLayeredHighlights​(boolean newValue)

If true, highlights are drawn as the Views draw the text. That is
the Views will call into

paintLayeredHighlight

which
will result in a rectangle being drawn before the text is drawn
(if the offsets are in a highlighted region that is). For this to
work the painter supplied must be an instance of
LayeredHighlightPainter.

**Parameters:**
- newValue

- the new value

---

#### public boolean getDrawsLayeredHighlights()

Return the draw layered highlights.

**Returns:**
- the draw layered highlights

---

### Additional Sections

#### Class DefaultHighlighter

java.lang.Object

- javax.swing.text.LayeredHighlighter
- - javax.swing.text.DefaultHighlighter

javax.swing.text.LayeredHighlighter

- javax.swing.text.DefaultHighlighter

javax.swing.text.DefaultHighlighter

**All Implemented Interfaces:** Highlighter

**Direct Known Subclasses:** BasicTextUI.BasicHighlighter

```java
public class
DefaultHighlighter

extends
LayeredHighlighter
```

Implements the Highlighter interfaces. Implements a simple highlight
painter that renders in a solid color.

**See Also:** Highlighter

public class

DefaultHighlighter

extends

LayeredHighlighter

Implements the Highlighter interfaces. Implements a simple highlight
painter that renders in a solid color.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

DefaultHighlighter.DefaultHighlightPainter

Simple highlight painter that fills a highlighted area with
a solid color.

- Nested classes/interfaces declared in class javax.swing.text.

LayeredHighlighter

LayeredHighlighter.LayerPainter

- Nested classes/interfaces declared in interface javax.swing.text.

Highlighter

Highlighter.Highlight

,

Highlighter.HighlightPainter

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

LayeredHighlighter.LayerPainter

DefaultPainter

Default implementation of LayeredHighlighter.LayerPainter that can
be used for painting highlights.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultHighlighter

()

Creates a new DefaultHighlighther object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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

Changes a highlight.

void

deinstall

​(

JTextComponent

c)

Called when the UI is being removed from the interface of
a JTextComponent.

boolean

getDrawsLayeredHighlights

()

Return the draw layered highlights.

Highlighter.Highlight

[]

getHighlights

()

Makes a copy of the highlights.

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

void

removeAllHighlights

()

Removes all highlights.

void

removeHighlight

​(

Object

tag)

Removes a highlight from the view.

void

setDrawsLayeredHighlights

​(boolean newValue)

If true, highlights are drawn as the Views draw the text.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

DefaultHighlighter.DefaultHighlightPainter

Simple highlight painter that fills a highlighted area with
a solid color.

- Nested classes/interfaces declared in class javax.swing.text.

LayeredHighlighter

LayeredHighlighter.LayerPainter

- Nested classes/interfaces declared in interface javax.swing.text.

Highlighter

Highlighter.Highlight

,

Highlighter.HighlightPainter

---

#### Nested Class Summary

Simple highlight painter that fills a highlighted area with
a solid color.

Nested classes/interfaces declared in class javax.swing.text.

LayeredHighlighter

LayeredHighlighter.LayerPainter

---

#### Nested classes/interfaces declared in class javax.swing.text. LayeredHighlighter

Nested classes/interfaces declared in interface javax.swing.text.

Highlighter

Highlighter.Highlight

,

Highlighter.HighlightPainter

---

#### Nested classes/interfaces declared in interface javax.swing.text. Highlighter

Field Summary

Fields

Modifier and Type

Field

Description

static

LayeredHighlighter.LayerPainter

DefaultPainter

Default implementation of LayeredHighlighter.LayerPainter that can
be used for painting highlights.

---

#### Field Summary

Default implementation of LayeredHighlighter.LayerPainter that can
be used for painting highlights.

Constructor Summary

Constructors

Constructor

Description

DefaultHighlighter

()

Creates a new DefaultHighlighther object.

---

#### Constructor Summary

Creates a new DefaultHighlighther object.

Method Summary

All Methods

Instance Methods

Concrete Methods

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

Changes a highlight.

void

deinstall

​(

JTextComponent

c)

Called when the UI is being removed from the interface of
a JTextComponent.

boolean

getDrawsLayeredHighlights

()

Return the draw layered highlights.

Highlighter.Highlight

[]

getHighlights

()

Makes a copy of the highlights.

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

void

removeAllHighlights

()

Removes all highlights.

void

removeHighlight

​(

Object

tag)

Removes a highlight from the view.

void

setDrawsLayeredHighlights

​(boolean newValue)

If true, highlights are drawn as the Views draw the text.

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

Adds a highlight to the view.

Changes a highlight.

Called when the UI is being removed from the interface of
a JTextComponent.

Return the draw layered highlights.

Makes a copy of the highlights.

Called when the UI is being installed into the
interface of a JTextComponent.

Renders the highlights.

When leaf Views (such as LabelView) are rendering they should
call into this method.

Removes all highlights.

Removes a highlight from the view.

If true, highlights are drawn as the Views draw the text.

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

============ FIELD DETAIL ===========

- Field Detail

- DefaultPainter

```java
public static final
LayeredHighlighter.LayerPainter
DefaultPainter
```

Default implementation of LayeredHighlighter.LayerPainter that can
be used for painting highlights.

As of 1.4 this field is final.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultHighlighter

```java
public DefaultHighlighter()
```

Creates a new DefaultHighlighther object.

============ METHOD DETAIL ==========

- Method Detail

- paint

```java
public void paint​(
Graphics
g)
```

Renders the highlights.

**Parameters:** g

- the graphics context

- install

```java
public void install​(
JTextComponent
c)
```

Called when the UI is being installed into the
interface of a JTextComponent. Installs the editor, and
removes any existing highlights.

**Parameters:** c

- the editor component
**See Also:** Highlighter.install(javax.swing.text.JTextComponent)

- deinstall

```java
public void deinstall​(
JTextComponent
c)
```

Called when the UI is being removed from the interface of
a JTextComponent.

**Parameters:** c

- the component
**See Also:** Highlighter.deinstall(javax.swing.text.JTextComponent)

- addHighlight

```java
public
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

- the start offset of the range to highlight >= 0
**Parameters:** p1

- the end offset of the range to highlight >= p0
**Parameters:** p

- the painter to use to actually render the highlight
**Returns:** an object that can be used as a tag
to refer to the highlight
**Throws:** BadLocationException

- if the specified location is invalid

- removeHighlight

```java
public void removeHighlight​(
Object
tag)
```

Removes a highlight from the view.

**Parameters:** tag

- the reference to the highlight

- removeAllHighlights

```java
public void removeAllHighlights()
```

Removes all highlights.

- changeHighlight

```java
public void changeHighlight​(
Object
tag,
int p0,
int p1)
throws
BadLocationException
```

Changes a highlight.

**Parameters:** tag

- the highlight tag
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Throws:** BadLocationException

- if the specified location is invalid

- getHighlights

```java
public
Highlighter.Highlight
[] getHighlights()
```

Makes a copy of the highlights. Does not actually clone each highlight,
but only makes references to them.

**Returns:** the copy
**See Also:** Highlighter.getHighlights()

- paintLayeredHighlights

```java
public void paintLayeredHighlights​(
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

**Specified by:** paintLayeredHighlights

in class

LayeredHighlighter
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

- setDrawsLayeredHighlights

```java
public void setDrawsLayeredHighlights​(boolean newValue)
```

If true, highlights are drawn as the Views draw the text. That is
the Views will call into

paintLayeredHighlight

which
will result in a rectangle being drawn before the text is drawn
(if the offsets are in a highlighted region that is). For this to
work the painter supplied must be an instance of
LayeredHighlightPainter.

**Parameters:** newValue

- the new value

- getDrawsLayeredHighlights

```java
public boolean getDrawsLayeredHighlights()
```

Return the draw layered highlights.

**Returns:** the draw layered highlights

Field Detail

- DefaultPainter

```java
public static final
LayeredHighlighter.LayerPainter
DefaultPainter
```

Default implementation of LayeredHighlighter.LayerPainter that can
be used for painting highlights.

As of 1.4 this field is final.

---

#### Field Detail

DefaultPainter

```java
public static final
LayeredHighlighter.LayerPainter
DefaultPainter
```

Default implementation of LayeredHighlighter.LayerPainter that can
be used for painting highlights.

As of 1.4 this field is final.

---

#### DefaultPainter

public static final

LayeredHighlighter.LayerPainter

DefaultPainter

Default implementation of LayeredHighlighter.LayerPainter that can
be used for painting highlights.

As of 1.4 this field is final.

As of 1.4 this field is final.

Constructor Detail

- DefaultHighlighter

```java
public DefaultHighlighter()
```

Creates a new DefaultHighlighther object.

---

#### Constructor Detail

DefaultHighlighter

```java
public DefaultHighlighter()
```

Creates a new DefaultHighlighther object.

---

#### DefaultHighlighter

public DefaultHighlighter()

Creates a new DefaultHighlighther object.

Method Detail

- paint

```java
public void paint​(
Graphics
g)
```

Renders the highlights.

**Parameters:** g

- the graphics context

- install

```java
public void install​(
JTextComponent
c)
```

Called when the UI is being installed into the
interface of a JTextComponent. Installs the editor, and
removes any existing highlights.

**Parameters:** c

- the editor component
**See Also:** Highlighter.install(javax.swing.text.JTextComponent)

- deinstall

```java
public void deinstall​(
JTextComponent
c)
```

Called when the UI is being removed from the interface of
a JTextComponent.

**Parameters:** c

- the component
**See Also:** Highlighter.deinstall(javax.swing.text.JTextComponent)

- addHighlight

```java
public
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

- the start offset of the range to highlight >= 0
**Parameters:** p1

- the end offset of the range to highlight >= p0
**Parameters:** p

- the painter to use to actually render the highlight
**Returns:** an object that can be used as a tag
to refer to the highlight
**Throws:** BadLocationException

- if the specified location is invalid

- removeHighlight

```java
public void removeHighlight​(
Object
tag)
```

Removes a highlight from the view.

**Parameters:** tag

- the reference to the highlight

- removeAllHighlights

```java
public void removeAllHighlights()
```

Removes all highlights.

- changeHighlight

```java
public void changeHighlight​(
Object
tag,
int p0,
int p1)
throws
BadLocationException
```

Changes a highlight.

**Parameters:** tag

- the highlight tag
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Throws:** BadLocationException

- if the specified location is invalid

- getHighlights

```java
public
Highlighter.Highlight
[] getHighlights()
```

Makes a copy of the highlights. Does not actually clone each highlight,
but only makes references to them.

**Returns:** the copy
**See Also:** Highlighter.getHighlights()

- paintLayeredHighlights

```java
public void paintLayeredHighlights​(
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

**Specified by:** paintLayeredHighlights

in class

LayeredHighlighter
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

- setDrawsLayeredHighlights

```java
public void setDrawsLayeredHighlights​(boolean newValue)
```

If true, highlights are drawn as the Views draw the text. That is
the Views will call into

paintLayeredHighlight

which
will result in a rectangle being drawn before the text is drawn
(if the offsets are in a highlighted region that is). For this to
work the painter supplied must be an instance of
LayeredHighlightPainter.

**Parameters:** newValue

- the new value

- getDrawsLayeredHighlights

```java
public boolean getDrawsLayeredHighlights()
```

Return the draw layered highlights.

**Returns:** the draw layered highlights

---

#### Method Detail

paint

```java
public void paint​(
Graphics
g)
```

Renders the highlights.

**Parameters:** g

- the graphics context

---

#### paint

public void paint​(

Graphics

g)

Renders the highlights.

install

```java
public void install​(
JTextComponent
c)
```

Called when the UI is being installed into the
interface of a JTextComponent. Installs the editor, and
removes any existing highlights.

**Parameters:** c

- the editor component
**See Also:** Highlighter.install(javax.swing.text.JTextComponent)

---

#### install

public void install​(

JTextComponent

c)

Called when the UI is being installed into the
interface of a JTextComponent. Installs the editor, and
removes any existing highlights.

deinstall

```java
public void deinstall​(
JTextComponent
c)
```

Called when the UI is being removed from the interface of
a JTextComponent.

**Parameters:** c

- the component
**See Also:** Highlighter.deinstall(javax.swing.text.JTextComponent)

---

#### deinstall

public void deinstall​(

JTextComponent

c)

Called when the UI is being removed from the interface of
a JTextComponent.

addHighlight

```java
public
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

- the start offset of the range to highlight >= 0
**Parameters:** p1

- the end offset of the range to highlight >= p0
**Parameters:** p

- the painter to use to actually render the highlight
**Returns:** an object that can be used as a tag
to refer to the highlight
**Throws:** BadLocationException

- if the specified location is invalid

---

#### addHighlight

public

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
public void removeHighlight​(
Object
tag)
```

Removes a highlight from the view.

**Parameters:** tag

- the reference to the highlight

---

#### removeHighlight

public void removeHighlight​(

Object

tag)

Removes a highlight from the view.

removeAllHighlights

```java
public void removeAllHighlights()
```

Removes all highlights.

---

#### removeAllHighlights

public void removeAllHighlights()

Removes all highlights.

changeHighlight

```java
public void changeHighlight​(
Object
tag,
int p0,
int p1)
throws
BadLocationException
```

Changes a highlight.

**Parameters:** tag

- the highlight tag
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Throws:** BadLocationException

- if the specified location is invalid

---

#### changeHighlight

public void changeHighlight​(

Object

tag,
int p0,
int p1)
throws

BadLocationException

Changes a highlight.

getHighlights

```java
public
Highlighter.Highlight
[] getHighlights()
```

Makes a copy of the highlights. Does not actually clone each highlight,
but only makes references to them.

**Returns:** the copy
**See Also:** Highlighter.getHighlights()

---

#### getHighlights

public

Highlighter.Highlight

[] getHighlights()

Makes a copy of the highlights. Does not actually clone each highlight,
but only makes references to them.

paintLayeredHighlights

```java
public void paintLayeredHighlights​(
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

**Specified by:** paintLayeredHighlights

in class

LayeredHighlighter
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

public void paintLayeredHighlights​(

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

setDrawsLayeredHighlights

```java
public void setDrawsLayeredHighlights​(boolean newValue)
```

If true, highlights are drawn as the Views draw the text. That is
the Views will call into

paintLayeredHighlight

which
will result in a rectangle being drawn before the text is drawn
(if the offsets are in a highlighted region that is). For this to
work the painter supplied must be an instance of
LayeredHighlightPainter.

**Parameters:** newValue

- the new value

---

#### setDrawsLayeredHighlights

public void setDrawsLayeredHighlights​(boolean newValue)

If true, highlights are drawn as the Views draw the text. That is
the Views will call into

paintLayeredHighlight

which
will result in a rectangle being drawn before the text is drawn
(if the offsets are in a highlighted region that is). For this to
work the painter supplied must be an instance of
LayeredHighlightPainter.

getDrawsLayeredHighlights

```java
public boolean getDrawsLayeredHighlights()
```

Return the draw layered highlights.

**Returns:** the draw layered highlights

---

#### getDrawsLayeredHighlights

public boolean getDrawsLayeredHighlights()

Return the draw layered highlights.

---

