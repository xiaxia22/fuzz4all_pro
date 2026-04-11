# Class GlyphMetrics

**Source:** `java.desktop\java\awt\font\GlyphMetrics.html`

### Class Description

```java
public final class
GlyphMetrics

extends
Object
```

The

GlyphMetrics

class represents information for a
single glyph. A glyph is the visual representation of one or more
characters. Many different glyphs can be used to represent a single
character or combination of characters.

GlyphMetrics

instances are produced by

Font

and are applicable
to a specific glyph in a particular

Font

.

Glyphs are either STANDARD, LIGATURE, COMBINING, or COMPONENT.

- STANDARD glyphs are commonly used to represent single characters.

LIGATURE glyphs are used to represent sequences of characters.

COMPONENT glyphs in a

GlyphVector

do not correspond to a
particular character in a text model. Instead, COMPONENT glyphs are
added for typographical reasons, such as Arabic justification.

COMBINING glyphs embellish STANDARD or LIGATURE glyphs, such
as accent marks. Carets do not appear before COMBINING glyphs.

Other metrics available through

GlyphMetrics

are the
components of the advance, the visual bounds, and the left and right
side bearings.

Glyphs for a rotated font, or obtained from a

GlyphVector

which has applied a rotation to the glyph, can have advances that
contain both X and Y components. Usually the advance only has one
component.

The advance of a glyph is the distance from the glyph's origin to the
origin of the next glyph along the baseline, which is either vertical
or horizontal. Note that, in a

GlyphVector

,
the distance from a glyph to its following glyph might not be the
glyph's advance, because of kerning or other positioning adjustments.

The bounds is the smallest rectangle that completely contains the
outline of the glyph. The bounds rectangle is relative to the
glyph's origin. The left-side bearing is the distance from the glyph
origin to the left of its bounds rectangle. If the left-side bearing is
negative, part of the glyph is drawn to the left of its origin. The
right-side bearing is the distance from the right side of the bounds
rectangle to the next glyph origin (the origin plus the advance). If
negative, part of the glyph is drawn to the right of the next glyph's
origin. Note that the bounds does not necessarily enclose all the pixels
affected when rendering the glyph, because of rasterization and pixel
adjustment effects.

Although instances of

GlyphMetrics

can be directly
constructed, they are almost always obtained from a

GlyphVector

. Once constructed,

GlyphMetrics

objects are immutable.

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

**See Also:** Font

,

GlyphVector

---

### Field Details

#### public static final byte STANDARD

Indicates a glyph that represents a single standard
character.

**See Also:**
- Constant Field Values

---

#### public static final byte LIGATURE

Indicates a glyph that represents multiple characters
as a ligature, for example 'fi' or 'ffi'. It is followed by
filler glyphs for the remaining characters. Filler and combining
glyphs can be intermixed to control positioning of accent marks
on the logically preceding ligature.

**See Also:**
- Constant Field Values

---

#### public static final byte COMBINING

Indicates a glyph that represents a combining character,
such as an umlaut. There is no caret position between this glyph
and the preceding glyph.

**See Also:**
- Constant Field Values

---

#### public static final byte COMPONENT

Indicates a glyph with no corresponding character in the
backing store. The glyph is associated with the character
represented by the logically preceding non-component glyph. This
is used for kashida justification or other visual modifications to
existing glyphs. There is no caret position between this glyph
and the preceding glyph.

**See Also:**
- Constant Field Values

---

#### public static final byte WHITESPACE

Indicates a glyph with no visual representation. It can
be added to the other code values to indicate an invisible glyph.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public GlyphMetrics​(float advance,

Rectangle2D
bounds,
byte glyphType)

Constructs a

GlyphMetrics

object.

**Parameters:**
- advance

- the advance width of the glyph
- bounds

- the black box bounds of the glyph
- glyphType

- the type of the glyph

---

#### public GlyphMetrics​(boolean horizontal,
float advanceX,
float advanceY,

Rectangle2D
bounds,
byte glyphType)

Constructs a

GlyphMetrics

object.

**Parameters:**
- horizontal

- if true, metrics are for a horizontal baseline,
otherwise they are for a vertical baseline
- advanceX

- the X-component of the glyph's advance
- advanceY

- the Y-component of the glyph's advance
- bounds

- the visual bounds of the glyph
- glyphType

- the type of the glyph

**Since:**
- 1.4

---

### Method Details

#### public float getAdvance()

Returns the advance of the glyph along the baseline (either
horizontal or vertical).

**Returns:**
- the advance of the glyph

---

#### public float getAdvanceX()

Returns the x-component of the advance of the glyph.

**Returns:**
- the x-component of the advance of the glyph

**Since:**
- 1.4

---

#### public float getAdvanceY()

Returns the y-component of the advance of the glyph.

**Returns:**
- the y-component of the advance of the glyph

**Since:**
- 1.4

---

#### public
Rectangle2D
getBounds2D()

Returns the bounds of the glyph. This is the bounding box of the glyph outline.
Because of rasterization and pixel alignment effects, it does not necessarily
enclose the pixels that are affected when rendering the glyph.

**Returns:**
- a

Rectangle2D

that is the bounds of the glyph.

---

#### public float getLSB()

Returns the left (top) side bearing of the glyph.

This is the distance from 0, 0 to the left (top) of the glyph
bounds. If the bounds of the glyph is to the left of (above) the
origin, the LSB is negative.

**Returns:**
- the left side bearing of the glyph.

---

#### public float getRSB()

Returns the right (bottom) side bearing of the glyph.

This is the distance from the right (bottom) of the glyph bounds to
the advance. If the bounds of the glyph is to the right of (below)
the advance, the RSB is negative.

**Returns:**
- the right side bearing of the glyph.

---

#### public int getType()

Returns the raw glyph type code.

**Returns:**
- the raw glyph type code.

---

#### public boolean isStandard()

Returns

true

if this is a standard glyph.

**Returns:**
- true

if this is a standard glyph;

false

otherwise.

---

#### public boolean isLigature()

Returns

true

if this is a ligature glyph.

**Returns:**
- true

if this is a ligature glyph;

false

otherwise.

---

#### public boolean isCombining()

Returns

true

if this is a combining glyph.

**Returns:**
- true

if this is a combining glyph;

false

otherwise.

---

#### public boolean isComponent()

Returns

true

if this is a component glyph.

**Returns:**
- true

if this is a component glyph;

false

otherwise.

---

#### public boolean isWhitespace()

Returns

true

if this is a whitespace glyph.

**Returns:**
- true

if this is a whitespace glyph;

false

otherwise.

---

### Additional Sections

#### Class GlyphMetrics

java.lang.Object

- java.awt.font.GlyphMetrics

java.awt.font.GlyphMetrics

```java
public final class
GlyphMetrics

extends
Object
```

The

GlyphMetrics

class represents information for a
single glyph. A glyph is the visual representation of one or more
characters. Many different glyphs can be used to represent a single
character or combination of characters.

GlyphMetrics

instances are produced by

Font

and are applicable
to a specific glyph in a particular

Font

.

Glyphs are either STANDARD, LIGATURE, COMBINING, or COMPONENT.

- STANDARD glyphs are commonly used to represent single characters.

LIGATURE glyphs are used to represent sequences of characters.

COMPONENT glyphs in a

GlyphVector

do not correspond to a
particular character in a text model. Instead, COMPONENT glyphs are
added for typographical reasons, such as Arabic justification.

COMBINING glyphs embellish STANDARD or LIGATURE glyphs, such
as accent marks. Carets do not appear before COMBINING glyphs.

Other metrics available through

GlyphMetrics

are the
components of the advance, the visual bounds, and the left and right
side bearings.

Glyphs for a rotated font, or obtained from a

GlyphVector

which has applied a rotation to the glyph, can have advances that
contain both X and Y components. Usually the advance only has one
component.

The advance of a glyph is the distance from the glyph's origin to the
origin of the next glyph along the baseline, which is either vertical
or horizontal. Note that, in a

GlyphVector

,
the distance from a glyph to its following glyph might not be the
glyph's advance, because of kerning or other positioning adjustments.

The bounds is the smallest rectangle that completely contains the
outline of the glyph. The bounds rectangle is relative to the
glyph's origin. The left-side bearing is the distance from the glyph
origin to the left of its bounds rectangle. If the left-side bearing is
negative, part of the glyph is drawn to the left of its origin. The
right-side bearing is the distance from the right side of the bounds
rectangle to the next glyph origin (the origin plus the advance). If
negative, part of the glyph is drawn to the right of the next glyph's
origin. Note that the bounds does not necessarily enclose all the pixels
affected when rendering the glyph, because of rasterization and pixel
adjustment effects.

Although instances of

GlyphMetrics

can be directly
constructed, they are almost always obtained from a

GlyphVector

. Once constructed,

GlyphMetrics

objects are immutable.

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

**See Also:** Font

,

GlyphVector

public final class

GlyphMetrics

extends

Object

The

GlyphMetrics

class represents information for a
single glyph. A glyph is the visual representation of one or more
characters. Many different glyphs can be used to represent a single
character or combination of characters.

GlyphMetrics

instances are produced by

Font

and are applicable
to a specific glyph in a particular

Font

.

Glyphs are either STANDARD, LIGATURE, COMBINING, or COMPONENT.

- STANDARD glyphs are commonly used to represent single characters.

LIGATURE glyphs are used to represent sequences of characters.

COMPONENT glyphs in a

GlyphVector

do not correspond to a
particular character in a text model. Instead, COMPONENT glyphs are
added for typographical reasons, such as Arabic justification.

COMBINING glyphs embellish STANDARD or LIGATURE glyphs, such
as accent marks. Carets do not appear before COMBINING glyphs.

Other metrics available through

GlyphMetrics

are the
components of the advance, the visual bounds, and the left and right
side bearings.

Glyphs for a rotated font, or obtained from a

GlyphVector

which has applied a rotation to the glyph, can have advances that
contain both X and Y components. Usually the advance only has one
component.

The advance of a glyph is the distance from the glyph's origin to the
origin of the next glyph along the baseline, which is either vertical
or horizontal. Note that, in a

GlyphVector

,
the distance from a glyph to its following glyph might not be the
glyph's advance, because of kerning or other positioning adjustments.

The bounds is the smallest rectangle that completely contains the
outline of the glyph. The bounds rectangle is relative to the
glyph's origin. The left-side bearing is the distance from the glyph
origin to the left of its bounds rectangle. If the left-side bearing is
negative, part of the glyph is drawn to the left of its origin. The
right-side bearing is the distance from the right side of the bounds
rectangle to the next glyph origin (the origin plus the advance). If
negative, part of the glyph is drawn to the right of the next glyph's
origin. Note that the bounds does not necessarily enclose all the pixels
affected when rendering the glyph, because of rasterization and pixel
adjustment effects.

Although instances of

GlyphMetrics

can be directly
constructed, they are almost always obtained from a

GlyphVector

. Once constructed,

GlyphMetrics

objects are immutable.

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

Glyphs are either STANDARD, LIGATURE, COMBINING, or COMPONENT.

- STANDARD glyphs are commonly used to represent single characters.

LIGATURE glyphs are used to represent sequences of characters.

COMPONENT glyphs in a

GlyphVector

do not correspond to a
particular character in a text model. Instead, COMPONENT glyphs are
added for typographical reasons, such as Arabic justification.

COMBINING glyphs embellish STANDARD or LIGATURE glyphs, such
as accent marks. Carets do not appear before COMBINING glyphs.

Other metrics available through

GlyphMetrics

are the
components of the advance, the visual bounds, and the left and right
side bearings.

Glyphs for a rotated font, or obtained from a

GlyphVector

which has applied a rotation to the glyph, can have advances that
contain both X and Y components. Usually the advance only has one
component.

The advance of a glyph is the distance from the glyph's origin to the
origin of the next glyph along the baseline, which is either vertical
or horizontal. Note that, in a

GlyphVector

,
the distance from a glyph to its following glyph might not be the
glyph's advance, because of kerning or other positioning adjustments.

The bounds is the smallest rectangle that completely contains the
outline of the glyph. The bounds rectangle is relative to the
glyph's origin. The left-side bearing is the distance from the glyph
origin to the left of its bounds rectangle. If the left-side bearing is
negative, part of the glyph is drawn to the left of its origin. The
right-side bearing is the distance from the right side of the bounds
rectangle to the next glyph origin (the origin plus the advance). If
negative, part of the glyph is drawn to the right of the next glyph's
origin. Note that the bounds does not necessarily enclose all the pixels
affected when rendering the glyph, because of rasterization and pixel
adjustment effects.

Although instances of

GlyphMetrics

can be directly
constructed, they are almost always obtained from a

GlyphVector

. Once constructed,

GlyphMetrics

objects are immutable.

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

STANDARD glyphs are commonly used to represent single characters.

LIGATURE glyphs are used to represent sequences of characters.

COMPONENT glyphs in a

GlyphVector

do not correspond to a
particular character in a text model. Instead, COMPONENT glyphs are
added for typographical reasons, such as Arabic justification.

COMBINING glyphs embellish STANDARD or LIGATURE glyphs, such
as accent marks. Carets do not appear before COMBINING glyphs.

Other metrics available through

GlyphMetrics

are the
components of the advance, the visual bounds, and the left and right
side bearings.

Glyphs for a rotated font, or obtained from a

GlyphVector

which has applied a rotation to the glyph, can have advances that
contain both X and Y components. Usually the advance only has one
component.

The advance of a glyph is the distance from the glyph's origin to the
origin of the next glyph along the baseline, which is either vertical
or horizontal. Note that, in a

GlyphVector

,
the distance from a glyph to its following glyph might not be the
glyph's advance, because of kerning or other positioning adjustments.

The bounds is the smallest rectangle that completely contains the
outline of the glyph. The bounds rectangle is relative to the
glyph's origin. The left-side bearing is the distance from the glyph
origin to the left of its bounds rectangle. If the left-side bearing is
negative, part of the glyph is drawn to the left of its origin. The
right-side bearing is the distance from the right side of the bounds
rectangle to the next glyph origin (the origin plus the advance). If
negative, part of the glyph is drawn to the right of the next glyph's
origin. Note that the bounds does not necessarily enclose all the pixels
affected when rendering the glyph, because of rasterization and pixel
adjustment effects.

Although instances of

GlyphMetrics

can be directly
constructed, they are almost always obtained from a

GlyphVector

. Once constructed,

GlyphMetrics

objects are immutable.

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

Glyphs for a rotated font, or obtained from a

GlyphVector

which has applied a rotation to the glyph, can have advances that
contain both X and Y components. Usually the advance only has one
component.

The advance of a glyph is the distance from the glyph's origin to the
origin of the next glyph along the baseline, which is either vertical
or horizontal. Note that, in a

GlyphVector

,
the distance from a glyph to its following glyph might not be the
glyph's advance, because of kerning or other positioning adjustments.

The bounds is the smallest rectangle that completely contains the
outline of the glyph. The bounds rectangle is relative to the
glyph's origin. The left-side bearing is the distance from the glyph
origin to the left of its bounds rectangle. If the left-side bearing is
negative, part of the glyph is drawn to the left of its origin. The
right-side bearing is the distance from the right side of the bounds
rectangle to the next glyph origin (the origin plus the advance). If
negative, part of the glyph is drawn to the right of the next glyph's
origin. Note that the bounds does not necessarily enclose all the pixels
affected when rendering the glyph, because of rasterization and pixel
adjustment effects.

Although instances of

GlyphMetrics

can be directly
constructed, they are almost always obtained from a

GlyphVector

. Once constructed,

GlyphMetrics

objects are immutable.

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

The advance of a glyph is the distance from the glyph's origin to the
origin of the next glyph along the baseline, which is either vertical
or horizontal. Note that, in a

GlyphVector

,
the distance from a glyph to its following glyph might not be the
glyph's advance, because of kerning or other positioning adjustments.

The bounds is the smallest rectangle that completely contains the
outline of the glyph. The bounds rectangle is relative to the
glyph's origin. The left-side bearing is the distance from the glyph
origin to the left of its bounds rectangle. If the left-side bearing is
negative, part of the glyph is drawn to the left of its origin. The
right-side bearing is the distance from the right side of the bounds
rectangle to the next glyph origin (the origin plus the advance). If
negative, part of the glyph is drawn to the right of the next glyph's
origin. Note that the bounds does not necessarily enclose all the pixels
affected when rendering the glyph, because of rasterization and pixel
adjustment effects.

Although instances of

GlyphMetrics

can be directly
constructed, they are almost always obtained from a

GlyphVector

. Once constructed,

GlyphMetrics

objects are immutable.

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

The bounds is the smallest rectangle that completely contains the
outline of the glyph. The bounds rectangle is relative to the
glyph's origin. The left-side bearing is the distance from the glyph
origin to the left of its bounds rectangle. If the left-side bearing is
negative, part of the glyph is drawn to the left of its origin. The
right-side bearing is the distance from the right side of the bounds
rectangle to the next glyph origin (the origin plus the advance). If
negative, part of the glyph is drawn to the right of the next glyph's
origin. Note that the bounds does not necessarily enclose all the pixels
affected when rendering the glyph, because of rasterization and pixel
adjustment effects.

Although instances of

GlyphMetrics

can be directly
constructed, they are almost always obtained from a

GlyphVector

. Once constructed,

GlyphMetrics

objects are immutable.

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

Although instances of

GlyphMetrics

can be directly
constructed, they are almost always obtained from a

GlyphVector

. Once constructed,

GlyphMetrics

objects are immutable.

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

Example

:

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

Querying a

Font

for glyph information

```java
Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();
```

Font font = ...;
int glyphIndex = ...;
GlyphMetrics metrics = GlyphVector.getGlyphMetrics(glyphIndex);
int isStandard = metrics.isStandard();
float glyphAdvance = metrics.getAdvance();

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static byte

COMBINING

Indicates a glyph that represents a combining character,
such as an umlaut.

static byte

COMPONENT

Indicates a glyph with no corresponding character in the
backing store.

static byte

LIGATURE

Indicates a glyph that represents multiple characters
as a ligature, for example 'fi' or 'ffi'.

static byte

STANDARD

Indicates a glyph that represents a single standard
character.

static byte

WHITESPACE

Indicates a glyph with no visual representation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GlyphMetrics

​(boolean horizontal,
float advanceX,
float advanceY,

Rectangle2D

bounds,
byte glyphType)

Constructs a

GlyphMetrics

object.

GlyphMetrics

​(float advance,

Rectangle2D

bounds,
byte glyphType)

Constructs a

GlyphMetrics

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float

getAdvance

()

Returns the advance of the glyph along the baseline (either
horizontal or vertical).

float

getAdvanceX

()

Returns the x-component of the advance of the glyph.

float

getAdvanceY

()

Returns the y-component of the advance of the glyph.

Rectangle2D

getBounds2D

()

Returns the bounds of the glyph.

float

getLSB

()

Returns the left (top) side bearing of the glyph.

float

getRSB

()

Returns the right (bottom) side bearing of the glyph.

int

getType

()

Returns the raw glyph type code.

boolean

isCombining

()

Returns

true

if this is a combining glyph.

boolean

isComponent

()

Returns

true

if this is a component glyph.

boolean

isLigature

()

Returns

true

if this is a ligature glyph.

boolean

isStandard

()

Returns

true

if this is a standard glyph.

boolean

isWhitespace

()

Returns

true

if this is a whitespace glyph.

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

Field Summary

Fields

Modifier and Type

Field

Description

static byte

COMBINING

Indicates a glyph that represents a combining character,
such as an umlaut.

static byte

COMPONENT

Indicates a glyph with no corresponding character in the
backing store.

static byte

LIGATURE

Indicates a glyph that represents multiple characters
as a ligature, for example 'fi' or 'ffi'.

static byte

STANDARD

Indicates a glyph that represents a single standard
character.

static byte

WHITESPACE

Indicates a glyph with no visual representation.

---

#### Field Summary

Indicates a glyph that represents a combining character,
such as an umlaut.

Indicates a glyph with no corresponding character in the
backing store.

Indicates a glyph that represents multiple characters
as a ligature, for example 'fi' or 'ffi'.

Indicates a glyph that represents a single standard
character.

Indicates a glyph with no visual representation.

Constructor Summary

Constructors

Constructor

Description

GlyphMetrics

​(boolean horizontal,
float advanceX,
float advanceY,

Rectangle2D

bounds,
byte glyphType)

Constructs a

GlyphMetrics

object.

GlyphMetrics

​(float advance,

Rectangle2D

bounds,
byte glyphType)

Constructs a

GlyphMetrics

object.

---

#### Constructor Summary

Constructs a

GlyphMetrics

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float

getAdvance

()

Returns the advance of the glyph along the baseline (either
horizontal or vertical).

float

getAdvanceX

()

Returns the x-component of the advance of the glyph.

float

getAdvanceY

()

Returns the y-component of the advance of the glyph.

Rectangle2D

getBounds2D

()

Returns the bounds of the glyph.

float

getLSB

()

Returns the left (top) side bearing of the glyph.

float

getRSB

()

Returns the right (bottom) side bearing of the glyph.

int

getType

()

Returns the raw glyph type code.

boolean

isCombining

()

Returns

true

if this is a combining glyph.

boolean

isComponent

()

Returns

true

if this is a component glyph.

boolean

isLigature

()

Returns

true

if this is a ligature glyph.

boolean

isStandard

()

Returns

true

if this is a standard glyph.

boolean

isWhitespace

()

Returns

true

if this is a whitespace glyph.

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

Returns the advance of the glyph along the baseline (either
horizontal or vertical).

Returns the x-component of the advance of the glyph.

Returns the y-component of the advance of the glyph.

Returns the bounds of the glyph.

Returns the left (top) side bearing of the glyph.

Returns the right (bottom) side bearing of the glyph.

Returns the raw glyph type code.

Returns

true

if this is a combining glyph.

Returns

true

if this is a component glyph.

Returns

true

if this is a ligature glyph.

Returns

true

if this is a standard glyph.

Returns

true

if this is a whitespace glyph.

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

- STANDARD

```java
public static final byte STANDARD
```

Indicates a glyph that represents a single standard
character.

**See Also:** Constant Field Values

- LIGATURE

```java
public static final byte LIGATURE
```

Indicates a glyph that represents multiple characters
as a ligature, for example 'fi' or 'ffi'. It is followed by
filler glyphs for the remaining characters. Filler and combining
glyphs can be intermixed to control positioning of accent marks
on the logically preceding ligature.

**See Also:** Constant Field Values

- COMBINING

```java
public static final byte COMBINING
```

Indicates a glyph that represents a combining character,
such as an umlaut. There is no caret position between this glyph
and the preceding glyph.

**See Also:** Constant Field Values

- COMPONENT

```java
public static final byte COMPONENT
```

Indicates a glyph with no corresponding character in the
backing store. The glyph is associated with the character
represented by the logically preceding non-component glyph. This
is used for kashida justification or other visual modifications to
existing glyphs. There is no caret position between this glyph
and the preceding glyph.

**See Also:** Constant Field Values

- WHITESPACE

```java
public static final byte WHITESPACE
```

Indicates a glyph with no visual representation. It can
be added to the other code values to indicate an invisible glyph.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GlyphMetrics

```java
public GlyphMetrics​(float advance,

Rectangle2D
bounds,
byte glyphType)
```

Constructs a

GlyphMetrics

object.

**Parameters:** advance

- the advance width of the glyph
**Parameters:** bounds

- the black box bounds of the glyph
**Parameters:** glyphType

- the type of the glyph

- GlyphMetrics

```java
public GlyphMetrics​(boolean horizontal,
float advanceX,
float advanceY,

Rectangle2D
bounds,
byte glyphType)
```

Constructs a

GlyphMetrics

object.

**Parameters:** horizontal

- if true, metrics are for a horizontal baseline,
otherwise they are for a vertical baseline
**Parameters:** advanceX

- the X-component of the glyph's advance
**Parameters:** advanceY

- the Y-component of the glyph's advance
**Parameters:** bounds

- the visual bounds of the glyph
**Parameters:** glyphType

- the type of the glyph
**Since:** 1.4

============ METHOD DETAIL ==========

- Method Detail

- getAdvance

```java
public float getAdvance()
```

Returns the advance of the glyph along the baseline (either
horizontal or vertical).

**Returns:** the advance of the glyph

- getAdvanceX

```java
public float getAdvanceX()
```

Returns the x-component of the advance of the glyph.

**Returns:** the x-component of the advance of the glyph
**Since:** 1.4

- getAdvanceY

```java
public float getAdvanceY()
```

Returns the y-component of the advance of the glyph.

**Returns:** the y-component of the advance of the glyph
**Since:** 1.4

- getBounds2D

```java
public
Rectangle2D
getBounds2D()
```

Returns the bounds of the glyph. This is the bounding box of the glyph outline.
Because of rasterization and pixel alignment effects, it does not necessarily
enclose the pixels that are affected when rendering the glyph.

**Returns:** a

Rectangle2D

that is the bounds of the glyph.

- getLSB

```java
public float getLSB()
```

Returns the left (top) side bearing of the glyph.

This is the distance from 0, 0 to the left (top) of the glyph
bounds. If the bounds of the glyph is to the left of (above) the
origin, the LSB is negative.

**Returns:** the left side bearing of the glyph.

- getRSB

```java
public float getRSB()
```

Returns the right (bottom) side bearing of the glyph.

This is the distance from the right (bottom) of the glyph bounds to
the advance. If the bounds of the glyph is to the right of (below)
the advance, the RSB is negative.

**Returns:** the right side bearing of the glyph.

- getType

```java
public int getType()
```

Returns the raw glyph type code.

**Returns:** the raw glyph type code.

- isStandard

```java
public boolean isStandard()
```

Returns

true

if this is a standard glyph.

**Returns:** true

if this is a standard glyph;

false

otherwise.

- isLigature

```java
public boolean isLigature()
```

Returns

true

if this is a ligature glyph.

**Returns:** true

if this is a ligature glyph;

false

otherwise.

- isCombining

```java
public boolean isCombining()
```

Returns

true

if this is a combining glyph.

**Returns:** true

if this is a combining glyph;

false

otherwise.

- isComponent

```java
public boolean isComponent()
```

Returns

true

if this is a component glyph.

**Returns:** true

if this is a component glyph;

false

otherwise.

- isWhitespace

```java
public boolean isWhitespace()
```

Returns

true

if this is a whitespace glyph.

**Returns:** true

if this is a whitespace glyph;

false

otherwise.

Field Detail

- STANDARD

```java
public static final byte STANDARD
```

Indicates a glyph that represents a single standard
character.

**See Also:** Constant Field Values

- LIGATURE

```java
public static final byte LIGATURE
```

Indicates a glyph that represents multiple characters
as a ligature, for example 'fi' or 'ffi'. It is followed by
filler glyphs for the remaining characters. Filler and combining
glyphs can be intermixed to control positioning of accent marks
on the logically preceding ligature.

**See Also:** Constant Field Values

- COMBINING

```java
public static final byte COMBINING
```

Indicates a glyph that represents a combining character,
such as an umlaut. There is no caret position between this glyph
and the preceding glyph.

**See Also:** Constant Field Values

- COMPONENT

```java
public static final byte COMPONENT
```

Indicates a glyph with no corresponding character in the
backing store. The glyph is associated with the character
represented by the logically preceding non-component glyph. This
is used for kashida justification or other visual modifications to
existing glyphs. There is no caret position between this glyph
and the preceding glyph.

**See Also:** Constant Field Values

- WHITESPACE

```java
public static final byte WHITESPACE
```

Indicates a glyph with no visual representation. It can
be added to the other code values to indicate an invisible glyph.

**See Also:** Constant Field Values

---

#### Field Detail

STANDARD

```java
public static final byte STANDARD
```

Indicates a glyph that represents a single standard
character.

**See Also:** Constant Field Values

---

#### STANDARD

public static final byte STANDARD

Indicates a glyph that represents a single standard
character.

LIGATURE

```java
public static final byte LIGATURE
```

Indicates a glyph that represents multiple characters
as a ligature, for example 'fi' or 'ffi'. It is followed by
filler glyphs for the remaining characters. Filler and combining
glyphs can be intermixed to control positioning of accent marks
on the logically preceding ligature.

**See Also:** Constant Field Values

---

#### LIGATURE

public static final byte LIGATURE

Indicates a glyph that represents multiple characters
as a ligature, for example 'fi' or 'ffi'. It is followed by
filler glyphs for the remaining characters. Filler and combining
glyphs can be intermixed to control positioning of accent marks
on the logically preceding ligature.

COMBINING

```java
public static final byte COMBINING
```

Indicates a glyph that represents a combining character,
such as an umlaut. There is no caret position between this glyph
and the preceding glyph.

**See Also:** Constant Field Values

---

#### COMBINING

public static final byte COMBINING

Indicates a glyph that represents a combining character,
such as an umlaut. There is no caret position between this glyph
and the preceding glyph.

COMPONENT

```java
public static final byte COMPONENT
```

Indicates a glyph with no corresponding character in the
backing store. The glyph is associated with the character
represented by the logically preceding non-component glyph. This
is used for kashida justification or other visual modifications to
existing glyphs. There is no caret position between this glyph
and the preceding glyph.

**See Also:** Constant Field Values

---

#### COMPONENT

public static final byte COMPONENT

Indicates a glyph with no corresponding character in the
backing store. The glyph is associated with the character
represented by the logically preceding non-component glyph. This
is used for kashida justification or other visual modifications to
existing glyphs. There is no caret position between this glyph
and the preceding glyph.

WHITESPACE

```java
public static final byte WHITESPACE
```

Indicates a glyph with no visual representation. It can
be added to the other code values to indicate an invisible glyph.

**See Also:** Constant Field Values

---

#### WHITESPACE

public static final byte WHITESPACE

Indicates a glyph with no visual representation. It can
be added to the other code values to indicate an invisible glyph.

Constructor Detail

- GlyphMetrics

```java
public GlyphMetrics​(float advance,

Rectangle2D
bounds,
byte glyphType)
```

Constructs a

GlyphMetrics

object.

**Parameters:** advance

- the advance width of the glyph
**Parameters:** bounds

- the black box bounds of the glyph
**Parameters:** glyphType

- the type of the glyph

- GlyphMetrics

```java
public GlyphMetrics​(boolean horizontal,
float advanceX,
float advanceY,

Rectangle2D
bounds,
byte glyphType)
```

Constructs a

GlyphMetrics

object.

**Parameters:** horizontal

- if true, metrics are for a horizontal baseline,
otherwise they are for a vertical baseline
**Parameters:** advanceX

- the X-component of the glyph's advance
**Parameters:** advanceY

- the Y-component of the glyph's advance
**Parameters:** bounds

- the visual bounds of the glyph
**Parameters:** glyphType

- the type of the glyph
**Since:** 1.4

---

#### Constructor Detail

GlyphMetrics

```java
public GlyphMetrics​(float advance,

Rectangle2D
bounds,
byte glyphType)
```

Constructs a

GlyphMetrics

object.

**Parameters:** advance

- the advance width of the glyph
**Parameters:** bounds

- the black box bounds of the glyph
**Parameters:** glyphType

- the type of the glyph

---

#### GlyphMetrics

public GlyphMetrics​(float advance,

Rectangle2D

bounds,
byte glyphType)

Constructs a

GlyphMetrics

object.

GlyphMetrics

```java
public GlyphMetrics​(boolean horizontal,
float advanceX,
float advanceY,

Rectangle2D
bounds,
byte glyphType)
```

Constructs a

GlyphMetrics

object.

**Parameters:** horizontal

- if true, metrics are for a horizontal baseline,
otherwise they are for a vertical baseline
**Parameters:** advanceX

- the X-component of the glyph's advance
**Parameters:** advanceY

- the Y-component of the glyph's advance
**Parameters:** bounds

- the visual bounds of the glyph
**Parameters:** glyphType

- the type of the glyph
**Since:** 1.4

---

#### GlyphMetrics

public GlyphMetrics​(boolean horizontal,
float advanceX,
float advanceY,

Rectangle2D

bounds,
byte glyphType)

Constructs a

GlyphMetrics

object.

Method Detail

- getAdvance

```java
public float getAdvance()
```

Returns the advance of the glyph along the baseline (either
horizontal or vertical).

**Returns:** the advance of the glyph

- getAdvanceX

```java
public float getAdvanceX()
```

Returns the x-component of the advance of the glyph.

**Returns:** the x-component of the advance of the glyph
**Since:** 1.4

- getAdvanceY

```java
public float getAdvanceY()
```

Returns the y-component of the advance of the glyph.

**Returns:** the y-component of the advance of the glyph
**Since:** 1.4

- getBounds2D

```java
public
Rectangle2D
getBounds2D()
```

Returns the bounds of the glyph. This is the bounding box of the glyph outline.
Because of rasterization and pixel alignment effects, it does not necessarily
enclose the pixels that are affected when rendering the glyph.

**Returns:** a

Rectangle2D

that is the bounds of the glyph.

- getLSB

```java
public float getLSB()
```

Returns the left (top) side bearing of the glyph.

This is the distance from 0, 0 to the left (top) of the glyph
bounds. If the bounds of the glyph is to the left of (above) the
origin, the LSB is negative.

**Returns:** the left side bearing of the glyph.

- getRSB

```java
public float getRSB()
```

Returns the right (bottom) side bearing of the glyph.

This is the distance from the right (bottom) of the glyph bounds to
the advance. If the bounds of the glyph is to the right of (below)
the advance, the RSB is negative.

**Returns:** the right side bearing of the glyph.

- getType

```java
public int getType()
```

Returns the raw glyph type code.

**Returns:** the raw glyph type code.

- isStandard

```java
public boolean isStandard()
```

Returns

true

if this is a standard glyph.

**Returns:** true

if this is a standard glyph;

false

otherwise.

- isLigature

```java
public boolean isLigature()
```

Returns

true

if this is a ligature glyph.

**Returns:** true

if this is a ligature glyph;

false

otherwise.

- isCombining

```java
public boolean isCombining()
```

Returns

true

if this is a combining glyph.

**Returns:** true

if this is a combining glyph;

false

otherwise.

- isComponent

```java
public boolean isComponent()
```

Returns

true

if this is a component glyph.

**Returns:** true

if this is a component glyph;

false

otherwise.

- isWhitespace

```java
public boolean isWhitespace()
```

Returns

true

if this is a whitespace glyph.

**Returns:** true

if this is a whitespace glyph;

false

otherwise.

---

#### Method Detail

getAdvance

```java
public float getAdvance()
```

Returns the advance of the glyph along the baseline (either
horizontal or vertical).

**Returns:** the advance of the glyph

---

#### getAdvance

public float getAdvance()

Returns the advance of the glyph along the baseline (either
horizontal or vertical).

getAdvanceX

```java
public float getAdvanceX()
```

Returns the x-component of the advance of the glyph.

**Returns:** the x-component of the advance of the glyph
**Since:** 1.4

---

#### getAdvanceX

public float getAdvanceX()

Returns the x-component of the advance of the glyph.

getAdvanceY

```java
public float getAdvanceY()
```

Returns the y-component of the advance of the glyph.

**Returns:** the y-component of the advance of the glyph
**Since:** 1.4

---

#### getAdvanceY

public float getAdvanceY()

Returns the y-component of the advance of the glyph.

getBounds2D

```java
public
Rectangle2D
getBounds2D()
```

Returns the bounds of the glyph. This is the bounding box of the glyph outline.
Because of rasterization and pixel alignment effects, it does not necessarily
enclose the pixels that are affected when rendering the glyph.

**Returns:** a

Rectangle2D

that is the bounds of the glyph.

---

#### getBounds2D

public

Rectangle2D

getBounds2D()

Returns the bounds of the glyph. This is the bounding box of the glyph outline.
Because of rasterization and pixel alignment effects, it does not necessarily
enclose the pixels that are affected when rendering the glyph.

getLSB

```java
public float getLSB()
```

Returns the left (top) side bearing of the glyph.

This is the distance from 0, 0 to the left (top) of the glyph
bounds. If the bounds of the glyph is to the left of (above) the
origin, the LSB is negative.

**Returns:** the left side bearing of the glyph.

---

#### getLSB

public float getLSB()

Returns the left (top) side bearing of the glyph.

This is the distance from 0, 0 to the left (top) of the glyph
bounds. If the bounds of the glyph is to the left of (above) the
origin, the LSB is negative.

This is the distance from 0, 0 to the left (top) of the glyph
bounds. If the bounds of the glyph is to the left of (above) the
origin, the LSB is negative.

getRSB

```java
public float getRSB()
```

Returns the right (bottom) side bearing of the glyph.

This is the distance from the right (bottom) of the glyph bounds to
the advance. If the bounds of the glyph is to the right of (below)
the advance, the RSB is negative.

**Returns:** the right side bearing of the glyph.

---

#### getRSB

public float getRSB()

Returns the right (bottom) side bearing of the glyph.

This is the distance from the right (bottom) of the glyph bounds to
the advance. If the bounds of the glyph is to the right of (below)
the advance, the RSB is negative.

This is the distance from the right (bottom) of the glyph bounds to
the advance. If the bounds of the glyph is to the right of (below)
the advance, the RSB is negative.

getType

```java
public int getType()
```

Returns the raw glyph type code.

**Returns:** the raw glyph type code.

---

#### getType

public int getType()

Returns the raw glyph type code.

isStandard

```java
public boolean isStandard()
```

Returns

true

if this is a standard glyph.

**Returns:** true

if this is a standard glyph;

false

otherwise.

---

#### isStandard

public boolean isStandard()

Returns

true

if this is a standard glyph.

isLigature

```java
public boolean isLigature()
```

Returns

true

if this is a ligature glyph.

**Returns:** true

if this is a ligature glyph;

false

otherwise.

---

#### isLigature

public boolean isLigature()

Returns

true

if this is a ligature glyph.

isCombining

```java
public boolean isCombining()
```

Returns

true

if this is a combining glyph.

**Returns:** true

if this is a combining glyph;

false

otherwise.

---

#### isCombining

public boolean isCombining()

Returns

true

if this is a combining glyph.

isComponent

```java
public boolean isComponent()
```

Returns

true

if this is a component glyph.

**Returns:** true

if this is a component glyph;

false

otherwise.

---

#### isComponent

public boolean isComponent()

Returns

true

if this is a component glyph.

isWhitespace

```java
public boolean isWhitespace()
```

Returns

true

if this is a whitespace glyph.

**Returns:** true

if this is a whitespace glyph;

false

otherwise.

---

#### isWhitespace

public boolean isWhitespace()

Returns

true

if this is a whitespace glyph.

---

