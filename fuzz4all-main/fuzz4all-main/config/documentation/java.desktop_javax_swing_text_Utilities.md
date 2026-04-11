# Class Utilities

**Source:** `java.desktop\javax\swing\text\Utilities.html`

### Class Description

```java
public class
Utilities

extends
Object
```

A collection of methods to deal with various text
related activities.

---

### Field Details

*No entries found.*

### Constructor Details

#### public Utilities()

*No description found.*

---

### Method Details

#### @Deprecated
(
since
="9")
public static final int drawTabbedText​(
Segment
s,
int x,
int y,

Graphics
g,

TabExpander
e,
int startOffset)

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique. This particular
implementation renders in a 1.1 style coordinate system
where ints are used and 72dpi is assumed.

**Parameters:**
- s

- the source of the text
- x

- the X origin >= 0
- y

- the Y origin >= 0
- g

- the graphics context
- e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
- startOffset

- starting offset of the text in the document >= 0

**Returns:**
- the X location at the end of the rendered text

---

#### public static final float drawTabbedText​(
Segment
s,
float x,
float y,

Graphics2D
g,

TabExpander
e,
int startOffset)

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique.

**Parameters:**
- s

- the source of the text
- x

- the X origin

>= 0
- y

- the Y origin

>= 0
- g

- the graphics context
- e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
- startOffset

- starting offset of the text in the document

>= 0

**Returns:**
- the X location at the end of the rendered text

**Since:**
- 9

---

#### @Deprecated
(
since
="9")
public static final int getTabbedTextWidth​(
Segment
s,

FontMetrics
metrics,
int x,

TabExpander
e,
int startOffset)

Determines the width of the given segment of text taking tabs
into consideration. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

**Parameters:**
- s

- the source of the text
- metrics

- the font metrics to use for the calculation
- x

- the X origin >= 0
- e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
- startOffset

- starting offset of the text in the document >= 0

**Returns:**
- the width of the text

---

#### public static final float getTabbedTextWidth​(
Segment
s,

FontMetrics
metrics,
float x,

TabExpander
e,
int startOffset)

Determines the width of the given segment of text taking tabs
into consideration.

**Parameters:**
- s

- the source of the text
- metrics

- the font metrics to use for the calculation
- x

- the X origin

>= 0
- e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
- startOffset

- starting offset of the text in the document

>= 0

**Returns:**
- the width of the text

**Since:**
- 9

---

#### @Deprecated
(
since
="9")
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

**Parameters:**
- s

- the source of the text
- metrics

- the font metrics to use for the calculation
- x0

- the starting view location representing the start
of the given text >= 0.
- x

- the target view location to translate to an
offset into the text >= 0.
- e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
- startOffset

- starting offset of the text in the document >= 0

**Returns:**
- the offset into the text >= 0

---

#### @Deprecated
(
since
="9")
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset,
boolean round)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

**Parameters:**
- s

- the source of the text
- metrics

- the font metrics to use for the calculation
- x0

- the starting view location representing the start
of the given text >= 0.
- x

- the target view location to translate to an
offset into the text >= 0.
- e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
- startOffset

- starting offset of the text in the document >= 0
- round

- whether or not to round

**Returns:**
- the offset into the text >= 0

---

#### public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
float x0,
float x,

TabExpander
e,
int startOffset,
boolean round)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

**Parameters:**
- s

- the source of the text
- metrics

- the font metrics to use for the calculation
- x0

- the starting view location representing the start
of the given text

>= 0

.
- x

- the target view location to translate to an
offset into the text

>= 0

.
- e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
- startOffset

- starting offset of the text in the document

>= 0
- round

- whether or not to round

**Returns:**
- the offset into the text

>= 0

**Since:**
- 9

---

#### @Deprecated
(
since
="9")
public static final int getBreakLocation​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset)

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

**Parameters:**
- s

- the source of the text
- metrics

- the font metrics to use for the calculation
- x0

- the starting view location representing the start
of the given text.
- x

- the target view location to translate to an
offset into the text.
- e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
- startOffset

- starting offset in the document of the text

**Returns:**
- the offset into the given text

---

#### public static final int getBreakLocation​(
Segment
s,

FontMetrics
metrics,
float x0,
float x,

TabExpander
e,
int startOffset)

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

**Parameters:**
- s

- the source of the text
- metrics

- the font metrics to use for the calculation
- x0

- the starting view location representing the start
of the given text.
- x

- the target view location to translate to an
offset into the text.
- e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
- startOffset

- starting offset in the document of the text

**Returns:**
- the offset into the given text

**Since:**
- 9

---

#### public static final int getRowStart​(
JTextComponent
c,
int offs)
throws
BadLocationException

Determines the starting row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:**
- c

- the editor
- offs

- the offset in the document >= 0

**Returns:**
- the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.

**Throws:**
- BadLocationException

- if the offset is out of range

---

#### public static final int getRowEnd​(
JTextComponent
c,
int offs)
throws
BadLocationException

Determines the ending row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:**
- c

- the editor
- offs

- the offset in the document >= 0

**Returns:**
- the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.

**Throws:**
- BadLocationException

- if the offset is out of range

---

#### @Deprecated
(
since
="9")
public static final int getPositionAbove​(
JTextComponent
c,
int offs,
int x)
throws
BadLocationException

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:**
- c

- the editor
- offs

- the offset in the document >= 0
- x

- the X coordinate >= 0

**Returns:**
- the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.

**Throws:**
- BadLocationException

- if the offset is out of range

---

#### public static final int getPositionAbove​(
JTextComponent
c,
int offs,
float x)
throws
BadLocationException

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:**
- c

- the editor
- offs

- the offset in the document

>= 0
- x

- the X coordinate

>= 0

**Returns:**
- the position

>= 0

if the request can be computed, otherwise
a value of -1 will be returned.

**Throws:**
- BadLocationException

- if the offset is out of range

**Since:**
- 9

---

#### @Deprecated
(
since
="9")
public static final int getPositionBelow​(
JTextComponent
c,
int offs,
int x)
throws
BadLocationException

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:**
- c

- the editor
- offs

- the offset in the document >= 0
- x

- the X coordinate >= 0

**Returns:**
- the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.

**Throws:**
- BadLocationException

- if the offset is out of range

---

#### public static final int getPositionBelow​(
JTextComponent
c,
int offs,
float x)
throws
BadLocationException

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:**
- c

- the editor
- offs

- the offset in the document

>= 0
- x

- the X coordinate

>= 0

**Returns:**
- the position

>= 0

if the request can be computed, otherwise
a value of -1 will be returned.

**Throws:**
- BadLocationException

- if the offset is out of range

**Since:**
- 9

---

#### public static final int getWordStart​(
JTextComponent
c,
int offs)
throws
BadLocationException

Determines the start of a word for the given model location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:**
- c

- the editor
- offs

- the offset in the document >= 0

**Returns:**
- the location in the model of the word start >= 0

**Throws:**
- BadLocationException

- if the offset is out of range

---

#### public static final int getWordEnd​(
JTextComponent
c,
int offs)
throws
BadLocationException

Determines the end of a word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:**
- c

- the editor
- offs

- the offset in the document >= 0

**Returns:**
- the location in the model of the word end >= 0

**Throws:**
- BadLocationException

- if the offset is out of range

---

#### public static final int getNextWord​(
JTextComponent
c,
int offs)
throws
BadLocationException

Determines the start of the next word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:**
- c

- the editor
- offs

- the offset in the document >= 0

**Returns:**
- the location in the model of the word start >= 0

**Throws:**
- BadLocationException

- if the offset is out of range

---

#### public static final int getPreviousWord​(
JTextComponent
c,
int offs)
throws
BadLocationException

Determine the start of the prev word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:**
- c

- the editor
- offs

- the offset in the document >= 0

**Returns:**
- the location in the model of the word start >= 0

**Throws:**
- BadLocationException

- if the offset is out of range

---

#### public static final
Element
getParagraphElement​(
JTextComponent
c,
int offs)

Determines the element to use for a paragraph/line.

**Parameters:**
- c

- the editor
- offs

- the starting offset in the document >= 0

**Returns:**
- the element

---

### Additional Sections

#### Class Utilities

java.lang.Object

- javax.swing.text.Utilities

javax.swing.text.Utilities

```java
public class
Utilities

extends
Object
```

A collection of methods to deal with various text
related activities.

public class

Utilities

extends

Object

A collection of methods to deal with various text
related activities.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Utilities

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static float

drawTabbedText

​(

Segment

s,
float x,
float y,

Graphics2D

g,

TabExpander

e,
int startOffset)

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique.

static int

drawTabbedText

​(

Segment

s,
int x,
int y,

Graphics

g,

TabExpander

e,
int startOffset)

Deprecated.

replaced by

drawTabbedText(Segment, float, float, Graphics2D, TabExpander, int)

static int

getBreakLocation

​(

Segment

s,

FontMetrics

metrics,
float x0,
float x,

TabExpander

e,
int startOffset)

Determine where to break the given text to fit
within the given span.

static int

getBreakLocation

​(

Segment

s,

FontMetrics

metrics,
int x0,
int x,

TabExpander

e,
int startOffset)

Deprecated.

replaced by

getBreakLocation(Segment, FontMetrics, float, float,
TabExpander, int)

static int

getNextWord

​(

JTextComponent

c,
int offs)

Determines the start of the next word for the given location.

static

Element

getParagraphElement

​(

JTextComponent

c,
int offs)

Determines the element to use for a paragraph/line.

static int

getPositionAbove

​(

JTextComponent

c,
int offs,
float x)

Determines the position in the model that is closest to the given
view location in the row above.

static int

getPositionAbove

​(

JTextComponent

c,
int offs,
int x)

Deprecated.

replaced by

getPositionAbove(JTextComponent, int, float)

static int

getPositionBelow

​(

JTextComponent

c,
int offs,
float x)

Determines the position in the model that is closest to the given
view location in the row below.

static int

getPositionBelow

​(

JTextComponent

c,
int offs,
int x)

Deprecated.

replaced by

getPositionBelow(JTextComponent, int, float)

static int

getPreviousWord

​(

JTextComponent

c,
int offs)

Determine the start of the prev word for the given location.

static int

getRowEnd

​(

JTextComponent

c,
int offs)

Determines the ending row model position of the row that contains
the specified model position.

static int

getRowStart

​(

JTextComponent

c,
int offs)

Determines the starting row model position of the row that contains
the specified model position.

static int

getTabbedTextOffset

​(

Segment

s,

FontMetrics

metrics,
float x0,
float x,

TabExpander

e,
int startOffset,
boolean round)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

static int

getTabbedTextOffset

​(

Segment

s,

FontMetrics

metrics,
int x0,
int x,

TabExpander

e,
int startOffset)

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

static int

getTabbedTextOffset

​(

Segment

s,

FontMetrics

metrics,
int x0,
int x,

TabExpander

e,
int startOffset,
boolean round)

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

static float

getTabbedTextWidth

​(

Segment

s,

FontMetrics

metrics,
float x,

TabExpander

e,
int startOffset)

Determines the width of the given segment of text taking tabs
into consideration.

static int

getTabbedTextWidth

​(

Segment

s,

FontMetrics

metrics,
int x,

TabExpander

e,
int startOffset)

Deprecated.

replaced by

getTabbedTextWidth(Segment, FontMetrics, float, TabExpander, int)

static int

getWordEnd

​(

JTextComponent

c,
int offs)

Determines the end of a word for the given location.

static int

getWordStart

​(

JTextComponent

c,
int offs)

Determines the start of a word for the given model location.

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

Utilities

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static float

drawTabbedText

​(

Segment

s,
float x,
float y,

Graphics2D

g,

TabExpander

e,
int startOffset)

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique.

static int

drawTabbedText

​(

Segment

s,
int x,
int y,

Graphics

g,

TabExpander

e,
int startOffset)

Deprecated.

replaced by

drawTabbedText(Segment, float, float, Graphics2D, TabExpander, int)

static int

getBreakLocation

​(

Segment

s,

FontMetrics

metrics,
float x0,
float x,

TabExpander

e,
int startOffset)

Determine where to break the given text to fit
within the given span.

static int

getBreakLocation

​(

Segment

s,

FontMetrics

metrics,
int x0,
int x,

TabExpander

e,
int startOffset)

Deprecated.

replaced by

getBreakLocation(Segment, FontMetrics, float, float,
TabExpander, int)

static int

getNextWord

​(

JTextComponent

c,
int offs)

Determines the start of the next word for the given location.

static

Element

getParagraphElement

​(

JTextComponent

c,
int offs)

Determines the element to use for a paragraph/line.

static int

getPositionAbove

​(

JTextComponent

c,
int offs,
float x)

Determines the position in the model that is closest to the given
view location in the row above.

static int

getPositionAbove

​(

JTextComponent

c,
int offs,
int x)

Deprecated.

replaced by

getPositionAbove(JTextComponent, int, float)

static int

getPositionBelow

​(

JTextComponent

c,
int offs,
float x)

Determines the position in the model that is closest to the given
view location in the row below.

static int

getPositionBelow

​(

JTextComponent

c,
int offs,
int x)

Deprecated.

replaced by

getPositionBelow(JTextComponent, int, float)

static int

getPreviousWord

​(

JTextComponent

c,
int offs)

Determine the start of the prev word for the given location.

static int

getRowEnd

​(

JTextComponent

c,
int offs)

Determines the ending row model position of the row that contains
the specified model position.

static int

getRowStart

​(

JTextComponent

c,
int offs)

Determines the starting row model position of the row that contains
the specified model position.

static int

getTabbedTextOffset

​(

Segment

s,

FontMetrics

metrics,
float x0,
float x,

TabExpander

e,
int startOffset,
boolean round)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

static int

getTabbedTextOffset

​(

Segment

s,

FontMetrics

metrics,
int x0,
int x,

TabExpander

e,
int startOffset)

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

static int

getTabbedTextOffset

​(

Segment

s,

FontMetrics

metrics,
int x0,
int x,

TabExpander

e,
int startOffset,
boolean round)

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

static float

getTabbedTextWidth

​(

Segment

s,

FontMetrics

metrics,
float x,

TabExpander

e,
int startOffset)

Determines the width of the given segment of text taking tabs
into consideration.

static int

getTabbedTextWidth

​(

Segment

s,

FontMetrics

metrics,
int x,

TabExpander

e,
int startOffset)

Deprecated.

replaced by

getTabbedTextWidth(Segment, FontMetrics, float, TabExpander, int)

static int

getWordEnd

​(

JTextComponent

c,
int offs)

Determines the end of a word for the given location.

static int

getWordStart

​(

JTextComponent

c,
int offs)

Determines the start of a word for the given model location.

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

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique.

Deprecated.

replaced by

drawTabbedText(Segment, float, float, Graphics2D, TabExpander, int)

Determine where to break the given text to fit
within the given span.

Deprecated.

replaced by

getBreakLocation(Segment, FontMetrics, float, float,
TabExpander, int)

Determines the start of the next word for the given location.

Determines the element to use for a paragraph/line.

Determines the position in the model that is closest to the given
view location in the row above.

Deprecated.

replaced by

getPositionAbove(JTextComponent, int, float)

Determines the position in the model that is closest to the given
view location in the row below.

Deprecated.

replaced by

getPositionBelow(JTextComponent, int, float)

Determine the start of the prev word for the given location.

Determines the ending row model position of the row that contains
the specified model position.

Determines the starting row model position of the row that contains
the specified model position.

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

Determines the width of the given segment of text taking tabs
into consideration.

Deprecated.

replaced by

getTabbedTextWidth(Segment, FontMetrics, float, TabExpander, int)

Determines the end of a word for the given location.

Determines the start of a word for the given model location.

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

- Utilities

```java
public Utilities()
```

============ METHOD DETAIL ==========

- Method Detail

- drawTabbedText

```java
@Deprecated
(
since
="9")
public static final int drawTabbedText​(
Segment
s,
int x,
int y,

Graphics
g,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

drawTabbedText(Segment, float, float, Graphics2D, TabExpander, int)

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique. This particular
implementation renders in a 1.1 style coordinate system
where ints are used and 72dpi is assumed.

**Parameters:** s

- the source of the text
**Parameters:** x

- the X origin >= 0
**Parameters:** y

- the Y origin >= 0
**Parameters:** g

- the graphics context
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Returns:** the X location at the end of the rendered text

- drawTabbedText

```java
public static final float drawTabbedText​(
Segment
s,
float x,
float y,

Graphics2D
g,

TabExpander
e,
int startOffset)
```

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique.

**Parameters:** s

- the source of the text
**Parameters:** x

- the X origin

>= 0
**Parameters:** y

- the Y origin

>= 0
**Parameters:** g

- the graphics context
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document

>= 0
**Returns:** the X location at the end of the rendered text
**Since:** 9

- getTabbedTextWidth

```java
@Deprecated
(
since
="9")
public static final int getTabbedTextWidth​(
Segment
s,

FontMetrics
metrics,
int x,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

getTabbedTextWidth(Segment, FontMetrics, float, TabExpander, int)

Determines the width of the given segment of text taking tabs
into consideration. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x

- the X origin >= 0
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Returns:** the width of the text

- getTabbedTextWidth

```java
public static final float getTabbedTextWidth​(
Segment
s,

FontMetrics
metrics,
float x,

TabExpander
e,
int startOffset)
```

Determines the width of the given segment of text taking tabs
into consideration.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x

- the X origin

>= 0
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document

>= 0
**Returns:** the width of the text
**Since:** 9

- getTabbedTextOffset

```java
@Deprecated
(
since
="9")
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text >= 0.
**Parameters:** x

- the target view location to translate to an
offset into the text >= 0.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Returns:** the offset into the text >= 0

- getTabbedTextOffset

```java
@Deprecated
(
since
="9")
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset,
boolean round)
```

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text >= 0.
**Parameters:** x

- the target view location to translate to an
offset into the text >= 0.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Parameters:** round

- whether or not to round
**Returns:** the offset into the text >= 0

- getTabbedTextOffset

```java
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
float x0,
float x,

TabExpander
e,
int startOffset,
boolean round)
```

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text

>= 0

.
**Parameters:** x

- the target view location to translate to an
offset into the text

>= 0

.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document

>= 0
**Parameters:** round

- whether or not to round
**Returns:** the offset into the text

>= 0
**Since:** 9

- getBreakLocation

```java
@Deprecated
(
since
="9")
public static final int getBreakLocation​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

getBreakLocation(Segment, FontMetrics, float, float,
TabExpander, int)

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text.
**Parameters:** x

- the target view location to translate to an
offset into the text.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset in the document of the text
**Returns:** the offset into the given text

- getBreakLocation

```java
public static final int getBreakLocation​(
Segment
s,

FontMetrics
metrics,
float x0,
float x,

TabExpander
e,
int startOffset)
```

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text.
**Parameters:** x

- the target view location to translate to an
offset into the text.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset in the document of the text
**Returns:** the offset into the given text
**Since:** 9

- getRowStart

```java
public static final int getRowStart​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the starting row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

- getRowEnd

```java
public static final int getRowEnd​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the ending row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

- getPositionAbove

```java
@Deprecated
(
since
="9")
public static final int getPositionAbove​(
JTextComponent
c,
int offs,
int x)
throws
BadLocationException
```

Deprecated.

replaced by

getPositionAbove(JTextComponent, int, float)

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Parameters:** x

- the X coordinate >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

- getPositionAbove

```java
public static final int getPositionAbove​(
JTextComponent
c,
int offs,
float x)
throws
BadLocationException
```

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document

>= 0
**Parameters:** x

- the X coordinate

>= 0
**Returns:** the position

>= 0

if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range
**Since:** 9

- getPositionBelow

```java
@Deprecated
(
since
="9")
public static final int getPositionBelow​(
JTextComponent
c,
int offs,
int x)
throws
BadLocationException
```

Deprecated.

replaced by

getPositionBelow(JTextComponent, int, float)

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Parameters:** x

- the X coordinate >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

- getPositionBelow

```java
public static final int getPositionBelow​(
JTextComponent
c,
int offs,
float x)
throws
BadLocationException
```

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document

>= 0
**Parameters:** x

- the X coordinate

>= 0
**Returns:** the position

>= 0

if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range
**Since:** 9

- getWordStart

```java
public static final int getWordStart​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the start of a word for the given model location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word start >= 0
**Throws:** BadLocationException

- if the offset is out of range

- getWordEnd

```java
public static final int getWordEnd​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the end of a word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word end >= 0
**Throws:** BadLocationException

- if the offset is out of range

- getNextWord

```java
public static final int getNextWord​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the start of the next word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word start >= 0
**Throws:** BadLocationException

- if the offset is out of range

- getPreviousWord

```java
public static final int getPreviousWord​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determine the start of the prev word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word start >= 0
**Throws:** BadLocationException

- if the offset is out of range

- getParagraphElement

```java
public static final
Element
getParagraphElement​(
JTextComponent
c,
int offs)
```

Determines the element to use for a paragraph/line.

**Parameters:** c

- the editor
**Parameters:** offs

- the starting offset in the document >= 0
**Returns:** the element

Constructor Detail

- Utilities

```java
public Utilities()
```

---

#### Constructor Detail

Utilities

```java
public Utilities()
```

---

#### Utilities

public Utilities()

Method Detail

- drawTabbedText

```java
@Deprecated
(
since
="9")
public static final int drawTabbedText​(
Segment
s,
int x,
int y,

Graphics
g,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

drawTabbedText(Segment, float, float, Graphics2D, TabExpander, int)

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique. This particular
implementation renders in a 1.1 style coordinate system
where ints are used and 72dpi is assumed.

**Parameters:** s

- the source of the text
**Parameters:** x

- the X origin >= 0
**Parameters:** y

- the Y origin >= 0
**Parameters:** g

- the graphics context
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Returns:** the X location at the end of the rendered text

- drawTabbedText

```java
public static final float drawTabbedText​(
Segment
s,
float x,
float y,

Graphics2D
g,

TabExpander
e,
int startOffset)
```

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique.

**Parameters:** s

- the source of the text
**Parameters:** x

- the X origin

>= 0
**Parameters:** y

- the Y origin

>= 0
**Parameters:** g

- the graphics context
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document

>= 0
**Returns:** the X location at the end of the rendered text
**Since:** 9

- getTabbedTextWidth

```java
@Deprecated
(
since
="9")
public static final int getTabbedTextWidth​(
Segment
s,

FontMetrics
metrics,
int x,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

getTabbedTextWidth(Segment, FontMetrics, float, TabExpander, int)

Determines the width of the given segment of text taking tabs
into consideration. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x

- the X origin >= 0
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Returns:** the width of the text

- getTabbedTextWidth

```java
public static final float getTabbedTextWidth​(
Segment
s,

FontMetrics
metrics,
float x,

TabExpander
e,
int startOffset)
```

Determines the width of the given segment of text taking tabs
into consideration.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x

- the X origin

>= 0
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document

>= 0
**Returns:** the width of the text
**Since:** 9

- getTabbedTextOffset

```java
@Deprecated
(
since
="9")
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text >= 0.
**Parameters:** x

- the target view location to translate to an
offset into the text >= 0.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Returns:** the offset into the text >= 0

- getTabbedTextOffset

```java
@Deprecated
(
since
="9")
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset,
boolean round)
```

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text >= 0.
**Parameters:** x

- the target view location to translate to an
offset into the text >= 0.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Parameters:** round

- whether or not to round
**Returns:** the offset into the text >= 0

- getTabbedTextOffset

```java
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
float x0,
float x,

TabExpander
e,
int startOffset,
boolean round)
```

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text

>= 0

.
**Parameters:** x

- the target view location to translate to an
offset into the text

>= 0

.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document

>= 0
**Parameters:** round

- whether or not to round
**Returns:** the offset into the text

>= 0
**Since:** 9

- getBreakLocation

```java
@Deprecated
(
since
="9")
public static final int getBreakLocation​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

getBreakLocation(Segment, FontMetrics, float, float,
TabExpander, int)

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text.
**Parameters:** x

- the target view location to translate to an
offset into the text.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset in the document of the text
**Returns:** the offset into the given text

- getBreakLocation

```java
public static final int getBreakLocation​(
Segment
s,

FontMetrics
metrics,
float x0,
float x,

TabExpander
e,
int startOffset)
```

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text.
**Parameters:** x

- the target view location to translate to an
offset into the text.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset in the document of the text
**Returns:** the offset into the given text
**Since:** 9

- getRowStart

```java
public static final int getRowStart​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the starting row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

- getRowEnd

```java
public static final int getRowEnd​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the ending row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

- getPositionAbove

```java
@Deprecated
(
since
="9")
public static final int getPositionAbove​(
JTextComponent
c,
int offs,
int x)
throws
BadLocationException
```

Deprecated.

replaced by

getPositionAbove(JTextComponent, int, float)

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Parameters:** x

- the X coordinate >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

- getPositionAbove

```java
public static final int getPositionAbove​(
JTextComponent
c,
int offs,
float x)
throws
BadLocationException
```

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document

>= 0
**Parameters:** x

- the X coordinate

>= 0
**Returns:** the position

>= 0

if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range
**Since:** 9

- getPositionBelow

```java
@Deprecated
(
since
="9")
public static final int getPositionBelow​(
JTextComponent
c,
int offs,
int x)
throws
BadLocationException
```

Deprecated.

replaced by

getPositionBelow(JTextComponent, int, float)

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Parameters:** x

- the X coordinate >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

- getPositionBelow

```java
public static final int getPositionBelow​(
JTextComponent
c,
int offs,
float x)
throws
BadLocationException
```

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document

>= 0
**Parameters:** x

- the X coordinate

>= 0
**Returns:** the position

>= 0

if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range
**Since:** 9

- getWordStart

```java
public static final int getWordStart​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the start of a word for the given model location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word start >= 0
**Throws:** BadLocationException

- if the offset is out of range

- getWordEnd

```java
public static final int getWordEnd​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the end of a word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word end >= 0
**Throws:** BadLocationException

- if the offset is out of range

- getNextWord

```java
public static final int getNextWord​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the start of the next word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word start >= 0
**Throws:** BadLocationException

- if the offset is out of range

- getPreviousWord

```java
public static final int getPreviousWord​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determine the start of the prev word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word start >= 0
**Throws:** BadLocationException

- if the offset is out of range

- getParagraphElement

```java
public static final
Element
getParagraphElement​(
JTextComponent
c,
int offs)
```

Determines the element to use for a paragraph/line.

**Parameters:** c

- the editor
**Parameters:** offs

- the starting offset in the document >= 0
**Returns:** the element

---

#### Method Detail

drawTabbedText

```java
@Deprecated
(
since
="9")
public static final int drawTabbedText​(
Segment
s,
int x,
int y,

Graphics
g,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

drawTabbedText(Segment, float, float, Graphics2D, TabExpander, int)

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique. This particular
implementation renders in a 1.1 style coordinate system
where ints are used and 72dpi is assumed.

**Parameters:** s

- the source of the text
**Parameters:** x

- the X origin >= 0
**Parameters:** y

- the Y origin >= 0
**Parameters:** g

- the graphics context
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Returns:** the X location at the end of the rendered text

---

#### drawTabbedText

@Deprecated

(

since

="9")
public static final int drawTabbedText​(

Segment

s,
int x,
int y,

Graphics

g,

TabExpander

e,
int startOffset)

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique. This particular
implementation renders in a 1.1 style coordinate system
where ints are used and 72dpi is assumed.

drawTabbedText

```java
public static final float drawTabbedText​(
Segment
s,
float x,
float y,

Graphics2D
g,

TabExpander
e,
int startOffset)
```

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique.

**Parameters:** s

- the source of the text
**Parameters:** x

- the X origin

>= 0
**Parameters:** y

- the Y origin

>= 0
**Parameters:** g

- the graphics context
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document

>= 0
**Returns:** the X location at the end of the rendered text
**Since:** 9

---

#### drawTabbedText

public static final float drawTabbedText​(

Segment

s,
float x,
float y,

Graphics2D

g,

TabExpander

e,
int startOffset)

Draws the given text, expanding any tabs that are contained
using the given tab expansion technique.

getTabbedTextWidth

```java
@Deprecated
(
since
="9")
public static final int getTabbedTextWidth​(
Segment
s,

FontMetrics
metrics,
int x,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

getTabbedTextWidth(Segment, FontMetrics, float, TabExpander, int)

Determines the width of the given segment of text taking tabs
into consideration. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x

- the X origin >= 0
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Returns:** the width of the text

---

#### getTabbedTextWidth

@Deprecated

(

since

="9")
public static final int getTabbedTextWidth​(

Segment

s,

FontMetrics

metrics,
int x,

TabExpander

e,
int startOffset)

Determines the width of the given segment of text taking tabs
into consideration. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

getTabbedTextWidth

```java
public static final float getTabbedTextWidth​(
Segment
s,

FontMetrics
metrics,
float x,

TabExpander
e,
int startOffset)
```

Determines the width of the given segment of text taking tabs
into consideration.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x

- the X origin

>= 0
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document

>= 0
**Returns:** the width of the text
**Since:** 9

---

#### getTabbedTextWidth

public static final float getTabbedTextWidth​(

Segment

s,

FontMetrics

metrics,
float x,

TabExpander

e,
int startOffset)

Determines the width of the given segment of text taking tabs
into consideration.

getTabbedTextOffset

```java
@Deprecated
(
since
="9")
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text >= 0.
**Parameters:** x

- the target view location to translate to an
offset into the text >= 0.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Returns:** the offset into the text >= 0

---

#### getTabbedTextOffset

@Deprecated

(

since

="9")
public static final int getTabbedTextOffset​(

Segment

s,

FontMetrics

metrics,
int x0,
int x,

TabExpander

e,
int startOffset)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system. This is implemented in a 1.1 style coordinate
system where ints are used and 72dpi is assumed.

getTabbedTextOffset

```java
@Deprecated
(
since
="9")
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset,
boolean round)
```

Deprecated.

replaced by

getTabbedTextOffset(Segment, FontMetrics, float, float,
TabExpander, int, boolean)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text >= 0.
**Parameters:** x

- the target view location to translate to an
offset into the text >= 0.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document >= 0
**Parameters:** round

- whether or not to round
**Returns:** the offset into the text >= 0

---

#### getTabbedTextOffset

@Deprecated

(

since

="9")
public static final int getTabbedTextOffset​(

Segment

s,

FontMetrics

metrics,
int x0,
int x,

TabExpander

e,
int startOffset,
boolean round)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

getTabbedTextOffset

```java
public static final int getTabbedTextOffset​(
Segment
s,

FontMetrics
metrics,
float x0,
float x,

TabExpander
e,
int startOffset,
boolean round)
```

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text

>= 0

.
**Parameters:** x

- the target view location to translate to an
offset into the text

>= 0

.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset of the text in the document

>= 0
**Parameters:** round

- whether or not to round
**Returns:** the offset into the text

>= 0
**Since:** 9

---

#### getTabbedTextOffset

public static final int getTabbedTextOffset​(

Segment

s,

FontMetrics

metrics,
float x0,
float x,

TabExpander

e,
int startOffset,
boolean round)

Determines the relative offset into the given text that
best represents the given span in the view coordinate
system.

getBreakLocation

```java
@Deprecated
(
since
="9")
public static final int getBreakLocation​(
Segment
s,

FontMetrics
metrics,
int x0,
int x,

TabExpander
e,
int startOffset)
```

Deprecated.

replaced by

getBreakLocation(Segment, FontMetrics, float, float,
TabExpander, int)

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text.
**Parameters:** x

- the target view location to translate to an
offset into the text.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset in the document of the text
**Returns:** the offset into the given text

---

#### getBreakLocation

@Deprecated

(

since

="9")
public static final int getBreakLocation​(

Segment

s,

FontMetrics

metrics,
int x0,
int x,

TabExpander

e,
int startOffset)

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

getBreakLocation

```java
public static final int getBreakLocation​(
Segment
s,

FontMetrics
metrics,
float x0,
float x,

TabExpander
e,
int startOffset)
```

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

**Parameters:** s

- the source of the text
**Parameters:** metrics

- the font metrics to use for the calculation
**Parameters:** x0

- the starting view location representing the start
of the given text.
**Parameters:** x

- the target view location to translate to an
offset into the text.
**Parameters:** e

- how to expand the tabs. If this value is null,
tabs will be expanded as a space character.
**Parameters:** startOffset

- starting offset in the document of the text
**Returns:** the offset into the given text
**Since:** 9

---

#### getBreakLocation

public static final int getBreakLocation​(

Segment

s,

FontMetrics

metrics,
float x0,
float x,

TabExpander

e,
int startOffset)

Determine where to break the given text to fit
within the given span. This tries to find a word boundary.

getRowStart

```java
public static final int getRowStart​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the starting row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

---

#### getRowStart

public static final int getRowStart​(

JTextComponent

c,
int offs)
throws

BadLocationException

Determines the starting row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

getRowEnd

```java
public static final int getRowEnd​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the ending row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

---

#### getRowEnd

public static final int getRowEnd​(

JTextComponent

c,
int offs)
throws

BadLocationException

Determines the ending row model position of the row that contains
the specified model position. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

getPositionAbove

```java
@Deprecated
(
since
="9")
public static final int getPositionAbove​(
JTextComponent
c,
int offs,
int x)
throws
BadLocationException
```

Deprecated.

replaced by

getPositionAbove(JTextComponent, int, float)

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Parameters:** x

- the X coordinate >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

---

#### getPositionAbove

@Deprecated

(

since

="9")
public static final int getPositionAbove​(

JTextComponent

c,
int offs,
int x)
throws

BadLocationException

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

getPositionAbove

```java
public static final int getPositionAbove​(
JTextComponent
c,
int offs,
float x)
throws
BadLocationException
```

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document

>= 0
**Parameters:** x

- the X coordinate

>= 0
**Returns:** the position

>= 0

if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range
**Since:** 9

---

#### getPositionAbove

public static final int getPositionAbove​(

JTextComponent

c,
int offs,
float x)
throws

BadLocationException

Determines the position in the model that is closest to the given
view location in the row above. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

getPositionBelow

```java
@Deprecated
(
since
="9")
public static final int getPositionBelow​(
JTextComponent
c,
int offs,
int x)
throws
BadLocationException
```

Deprecated.

replaced by

getPositionBelow(JTextComponent, int, float)

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Parameters:** x

- the X coordinate >= 0
**Returns:** the position >= 0 if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range

---

#### getPositionBelow

@Deprecated

(

since

="9")
public static final int getPositionBelow​(

JTextComponent

c,
int offs,
int x)
throws

BadLocationException

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

getPositionBelow

```java
public static final int getPositionBelow​(
JTextComponent
c,
int offs,
float x)
throws
BadLocationException
```

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document

>= 0
**Parameters:** x

- the X coordinate

>= 0
**Returns:** the position

>= 0

if the request can be computed, otherwise
a value of -1 will be returned.
**Throws:** BadLocationException

- if the offset is out of range
**Since:** 9

---

#### getPositionBelow

public static final int getPositionBelow​(

JTextComponent

c,
int offs,
float x)
throws

BadLocationException

Determines the position in the model that is closest to the given
view location in the row below. The component given must have a
size to compute the result. If the component doesn't have a size
a value of -1 will be returned.

getWordStart

```java
public static final int getWordStart​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the start of a word for the given model location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word start >= 0
**Throws:** BadLocationException

- if the offset is out of range

---

#### getWordStart

public static final int getWordStart​(

JTextComponent

c,
int offs)
throws

BadLocationException

Determines the start of a word for the given model location.
Uses BreakIterator.getWordInstance() to actually get the words.

getWordEnd

```java
public static final int getWordEnd​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the end of a word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word end >= 0
**Throws:** BadLocationException

- if the offset is out of range

---

#### getWordEnd

public static final int getWordEnd​(

JTextComponent

c,
int offs)
throws

BadLocationException

Determines the end of a word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

getNextWord

```java
public static final int getNextWord​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determines the start of the next word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word start >= 0
**Throws:** BadLocationException

- if the offset is out of range

---

#### getNextWord

public static final int getNextWord​(

JTextComponent

c,
int offs)
throws

BadLocationException

Determines the start of the next word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

getPreviousWord

```java
public static final int getPreviousWord​(
JTextComponent
c,
int offs)
throws
BadLocationException
```

Determine the start of the prev word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

**Parameters:** c

- the editor
**Parameters:** offs

- the offset in the document >= 0
**Returns:** the location in the model of the word start >= 0
**Throws:** BadLocationException

- if the offset is out of range

---

#### getPreviousWord

public static final int getPreviousWord​(

JTextComponent

c,
int offs)
throws

BadLocationException

Determine the start of the prev word for the given location.
Uses BreakIterator.getWordInstance() to actually get the words.

getParagraphElement

```java
public static final
Element
getParagraphElement​(
JTextComponent
c,
int offs)
```

Determines the element to use for a paragraph/line.

**Parameters:** c

- the editor
**Parameters:** offs

- the starting offset in the document >= 0
**Returns:** the element

---

#### getParagraphElement

public static final

Element

getParagraphElement​(

JTextComponent

c,
int offs)

Determines the element to use for a paragraph/line.

---

