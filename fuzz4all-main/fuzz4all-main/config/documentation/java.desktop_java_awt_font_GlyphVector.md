# Class GlyphVector

**Source:** `java.desktop\java\awt\font\GlyphVector.html`

### Class Description

```java
public abstract class
GlyphVector

extends
Object

implements
Cloneable
```

A

GlyphVector

object is a collection of glyphs
containing geometric information for the placement of each glyph
in a transformed coordinate space which corresponds to the
device on which the

GlyphVector

is ultimately
displayed.

The

GlyphVector

does not attempt any interpretation of
the sequence of glyphs it contains. Relationships between adjacent
glyphs in sequence are solely used to determine the placement of
the glyphs in the visual coordinate space.

Instances of

GlyphVector

are created by a

Font

.

In a text processing application that can cache intermediate
representations of text, creation and subsequent caching of a

GlyphVector

for use during rendering is the fastest
method to present the visual representation of characters to a user.

A

GlyphVector

is associated with exactly one

Font

, and can provide data useful only in relation to
this

Font

. In addition, metrics obtained from a

GlyphVector

are not generally geometrically scalable
since the pixelization and spacing are dependent on grid-fitting
algorithms within a

Font

. To facilitate accurate
measurement of a

GlyphVector

and its component
glyphs, you must specify a scaling transform, anti-alias mode, and
fractional metrics mode when creating the

GlyphVector

.
These characteristics can be derived from the destination device.

For each glyph in the

GlyphVector

, you can obtain:

- the position of the glyph

the transform associated with the glyph

the metrics of the glyph in the context of the

GlyphVector

. The metrics of the glyph may be
different under different transforms, application specified
rendering hints, and the specific instance of the glyph within
the

GlyphVector

.

Altering the data used to create the

GlyphVector

does not
alter the state of the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

**All Implemented Interfaces:** Cloneable

---

### Field Details

#### public static final int FLAG_HAS_TRANSFORMS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
per-glyph transforms.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int FLAG_HAS_POSITION_ADJUSTMENTS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
position adjustments. When this is true, the glyph positions don't match the
accumulated default advances of the glyphs (for example, if kerning has been done).

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int FLAG_RUN_RTL

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a right-to-left run direction. This refers to the glyph-to-char mapping and does
not imply that the visual locations of the glyphs are necessarily in this order,
although generally they will be.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int FLAG_COMPLEX_GLYPHS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a complex glyph-to-char mapping (one that does not map glyphs to chars one-to-one in
strictly ascending or descending order matching the run direction).

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int FLAG_MASK

A mask for supported flags from getLayoutFlags. Only bits covered by the mask
should be tested.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

### Constructor Details

#### public GlyphVector()

*No description found.*

---

### Method Details

#### public abstract
Font
getFont()

Returns the

Font

associated with this

GlyphVector

.

**Returns:**
- Font

used to create this

GlyphVector

.

**See Also:**
- Font

---

#### public abstract
FontRenderContext
getFontRenderContext()

Returns the

FontRenderContext

associated with this

GlyphVector

.

**Returns:**
- FontRenderContext

used to create this

GlyphVector

.

**See Also:**
- FontRenderContext

,

Font

---

#### public abstract void performDefaultLayout()

Assigns default positions to each glyph in this

GlyphVector

. This can destroy information
generated during initial layout of this

GlyphVector

.

---

#### public abstract int getNumGlyphs()

Returns the number of glyphs in this

GlyphVector

.

**Returns:**
- number of glyphs in this

GlyphVector

.

---

#### public abstract int getGlyphCode​(int glyphIndex)

Returns the glyphcode of the specified glyph.
This return value is meaningless to anything other
than the

Font

object that created this

GlyphVector

.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve the
glyphcode.

**Returns:**
- the glyphcode of the glyph at the specified

glyphIndex

.

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the
number of glyphs in this

GlyphVector

---

#### public abstract int[] getGlyphCodes​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)

Returns an array of glyphcodes for the specified glyphs.
The contents of this return value are meaningless to anything other
than the

Font

used to create this

GlyphVector

. This method is used
for convenience and performance when processing glyphcodes.
If no array is passed in, a new array is created.

**Parameters:**
- beginGlyphIndex

- the index into this

GlyphVector

at which to start retrieving glyphcodes
- numEntries

- the number of glyphcodes to retrieve
- codeReturn

- the array that receives the glyphcodes and is
then returned

**Returns:**
- an array of glyphcodes for the specified glyphs.

**Throws:**
- IllegalArgumentException

- if

numEntries

is
less than 0
- IndexOutOfBoundsException

- if

beginGlyphIndex

is less than 0
- IndexOutOfBoundsException

- if the sum of

beginGlyphIndex

and

numEntries

is
greater than the number of glyphs in this

GlyphVector

---

#### public int getGlyphCharIndex​(int glyphIndex)

Returns the character index of the specified glyph.
The character index is the index of the first logical
character represented by the glyph. The default
implementation assumes a one-to-one, left-to-right mapping
of glyphs to characters.

**Parameters:**
- glyphIndex

- the index of the glyph

**Returns:**
- the index of the first character represented by the glyph

**Since:**
- 1.4

---

#### public int[] getGlyphCharIndices​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)

Returns the character indices of the specified glyphs.
The character index is the index of the first logical
character represented by the glyph. Indices are returned
in glyph order. The default implementation invokes
getGlyphCharIndex for each glyph, and subclassers will probably
want to override this implementation for performance reasons.
Use this method for convenience and performance
in processing of glyphcodes. If no array is passed in,
a new array is created.

**Parameters:**
- beginGlyphIndex

- the index of the first glyph
- numEntries

- the number of glyph indices
- codeReturn

- the array into which to return the character indices

**Returns:**
- an array of character indices, one per glyph.

**Since:**
- 1.4

---

#### public abstract
Rectangle2D
getLogicalBounds()

Returns the logical bounds of this

GlyphVector

.
This method is used when positioning this

GlyphVector

in relation to visually adjacent

GlyphVector

objects.

**Returns:**
- a

Rectangle2D

that is the logical bounds of this

GlyphVector

.

---

#### public abstract
Rectangle2D
getVisualBounds()

Returns the visual bounds of this

GlyphVector

The visual bounds is the bounding box of the outline of this

GlyphVector

. Because of rasterization and
alignment of pixels, it is possible that this box does not
enclose all pixels affected by rendering this

GlyphVector

.

**Returns:**
- a

Rectangle2D

that is the bounding box
of this

GlyphVector

.

---

#### public
Rectangle
getPixelBounds​(
FontRenderContext
renderFRC,
float x,
float y)

Returns the pixel bounds of this

GlyphVector

when
rendered in a graphics with the given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds,
offset to x, y and rounded out to the next integer value (i.e. returns an
integer rectangle which encloses the visual bounds) and
ignores the FRC. Subclassers should override this method.

**Parameters:**
- renderFRC

- the

FontRenderContext

of the

Graphics

.
- x

- the x-coordinate at which to render this

GlyphVector

.
- y

- the y-coordinate at which to render this

GlyphVector

.

**Returns:**
- a

Rectangle

bounding the pixels that would be affected.

**Since:**
- 1.4

---

#### public abstract
Shape
getOutline()

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

.

**Returns:**
- a

Shape

that is the outline of this

GlyphVector

.

---

#### public abstract
Shape
getOutline​(float x,
float y)

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

when
rendered at x, y.

**Parameters:**
- x

- the X coordinate of this

GlyphVector

.
- y

- the Y coordinate of this

GlyphVector

.

**Returns:**
- a

Shape

that is the outline of this

GlyphVector

when rendered at the specified
coordinates.

---

#### public abstract
Shape
getGlyphOutline​(int glyphIndex)

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

.
The outline returned by this method is positioned around the
origin of each individual glyph.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector

**Returns:**
- a

Shape

that is the outline of the glyph
at the specified

glyphIndex

of this

GlyphVector

.

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

---

#### public
Shape
getGlyphOutline​(int glyphIndex,
float x,
float y)

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

, offset to x, y.
The outline returned by this method is positioned around the
origin of each individual glyph.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector
- x

- the X coordinate of the location of this

GlyphVector
- y

- the Y coordinate of the location of this

GlyphVector

**Returns:**
- a

Shape

that is the outline of the glyph
at the specified

glyphIndex

of this

GlyphVector

when rendered at the specified
coordinates.

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

**Since:**
- 1.4

---

#### public abstract
Point2D
getGlyphPosition​(int glyphIndex)

Returns the position of the specified glyph relative to the
origin of this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method returns the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector

**Returns:**
- a

Point2D

object that is the position of the glyph
at the specified

glyphIndex

.

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than the number of glyphs
in this

GlyphVector

**See Also:**
- setGlyphPosition(int, java.awt.geom.Point2D)

---

#### public abstract void setGlyphPosition​(int glyphIndex,

Point2D
newPos)

Sets the position of the specified glyph within this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method sets the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector
- newPos

- the

Point2D

at which to position the
glyph at the specified

glyphIndex

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than the number of glyphs
in this

GlyphVector

**See Also:**
- getGlyphPosition(int)

---

#### public abstract
AffineTransform
getGlyphTransform​(int glyphIndex)

Returns the transform of the specified glyph within this

GlyphVector

. The transform is relative to the
glyph position. If no special transform has been applied,

null

can be returned. A null return indicates
an identity transform.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector

**Returns:**
- an

AffineTransform

that is the transform of
the glyph at the specified

glyphIndex

.

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

**See Also:**
- setGlyphTransform(int, java.awt.geom.AffineTransform)

---

#### public abstract void setGlyphTransform​(int glyphIndex,

AffineTransform
newTX)

Sets the transform of the specified glyph within this

GlyphVector

. The transform is relative to the glyph
position. A

null

argument for

newTX

indicates that no special transform is applied for the specified
glyph.
This method can be used to rotate, mirror, translate and scale the
glyph. Adding a transform can result in significant performance changes.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector
- newTX

- the new transform of the glyph at

glyphIndex

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

**See Also:**
- getGlyphTransform(int)

---

#### public int getLayoutFlags()

Returns flags describing the global state of the GlyphVector.
Flags not described below are reserved. The default
implementation returns 0 (meaning false) for the position adjustments,
transforms, rtl, and complex flags.
Subclassers should override this method, and make sure
it correctly describes the GlyphVector and corresponds
to the results of related calls.

**Returns:**
- an int containing the flags describing the state

**See Also:**
- FLAG_HAS_POSITION_ADJUSTMENTS

,

FLAG_HAS_TRANSFORMS

,

FLAG_RUN_RTL

,

FLAG_COMPLEX_GLYPHS

,

FLAG_MASK

**Since:**
- 1.4

---

#### public abstract float[] getGlyphPositions​(int beginGlyphIndex,
int numEntries,
float[] positionReturn)

Returns an array of glyph positions for the specified glyphs.
This method is used for convenience and performance when
processing glyph positions.
If no array is passed in, a new array is created.
Even numbered array entries beginning with position zero are the X
coordinates of the glyph numbered

beginGlyphIndex + position/2

.
Odd numbered array entries beginning with position one are the Y
coordinates of the glyph numbered

beginGlyphIndex + (position-1)/2

.
If

beginGlyphIndex

equals the number of glyphs in
this

GlyphVector

, this method gets the position after
the last glyph and this position is used to define the advance of
the entire

GlyphVector

.

**Parameters:**
- beginGlyphIndex

- the index at which to begin retrieving
glyph positions
- numEntries

- the number of glyphs to retrieve
- positionReturn

- the array that receives the glyph positions
and is then returned.

**Returns:**
- an array of glyph positions specified by

beginGlyphIndex

and

numEntries

.

**Throws:**
- IllegalArgumentException

- if

numEntries

is
less than 0
- IndexOutOfBoundsException

- if

beginGlyphIndex

is less than 0
- IndexOutOfBoundsException

- if the sum of

beginGlyphIndex

and

numEntries

is greater than the number of glyphs in this

GlyphVector

plus one

---

#### public abstract
Shape
getGlyphLogicalBounds​(int glyphIndex)

Returns the logical bounds of the specified glyph within this

GlyphVector

.
These logical bounds have a total of four edges, with two edges
parallel to the baseline under the glyph's transform and the other two
edges are shared with adjacent glyphs if they are present. This
method is useful for hit-testing of the specified glyph,
positioning of a caret at the leading or trailing edge of a glyph,
and for drawing a highlight region around the specified glyph.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its logical
bounds

**Returns:**
- a

Shape

that is the logical bounds of the
glyph at the specified

glyphIndex

.

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

**See Also:**
- getGlyphVisualBounds(int)

---

#### public abstract
Shape
getGlyphVisualBounds​(int glyphIndex)

Returns the visual bounds of the specified glyph within the

GlyphVector

.
The bounds returned by this method is positioned around the
origin of each individual glyph.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its visual
bounds

**Returns:**
- a

Shape

that is the visual bounds of the
glyph at the specified

glyphIndex

.

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

**See Also:**
- getGlyphLogicalBounds(int)

---

#### public
Rectangle
getGlyphPixelBounds​(int index,

FontRenderContext
renderFRC,
float x,
float y)

Returns the pixel bounds of the glyph at index when this

GlyphVector

is rendered in a

Graphics

with the
given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds of the glyph,
offset to x, y and rounded out to the next integer value, and
ignores the FRC. Subclassers should override this method.

**Parameters:**
- index

- the index of the glyph.
- renderFRC

- the

FontRenderContext

of the

Graphics

.
- x

- the X position at which to render this

GlyphVector

.
- y

- the Y position at which to render this

GlyphVector

.

**Returns:**
- a

Rectangle

bounding the pixels that would be affected.

**Since:**
- 1.4

---

#### public abstract
GlyphMetrics
getGlyphMetrics​(int glyphIndex)

Returns the metrics of the glyph at the specified index into
this

GlyphVector

.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its metrics

**Returns:**
- a

GlyphMetrics

object that represents the
metrics of the glyph at the specified

glyphIndex

into this

GlyphVector

.

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

---

#### public abstract
GlyphJustificationInfo
getGlyphJustificationInfo​(int glyphIndex)

Returns the justification information for the glyph at
the specified index into this

GlyphVector

.

**Parameters:**
- glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its
justification properties

**Returns:**
- a

GlyphJustificationInfo

object that
represents the justification properties of the glyph at the
specified

glyphIndex

into this

GlyphVector

.

**Throws:**
- IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

---

#### public abstract boolean equals​(
GlyphVector
set)

Tests if the specified

GlyphVector

exactly
equals this

GlyphVector

.

**Parameters:**
- set

- the specified

GlyphVector

to test

**Returns:**
- true

if the specified

GlyphVector

equals this

GlyphVector

;

false

otherwise.

---

### Additional Sections

#### Class GlyphVector

java.lang.Object

- java.awt.font.GlyphVector

java.awt.font.GlyphVector

**All Implemented Interfaces:** Cloneable

```java
public abstract class
GlyphVector

extends
Object

implements
Cloneable
```

A

GlyphVector

object is a collection of glyphs
containing geometric information for the placement of each glyph
in a transformed coordinate space which corresponds to the
device on which the

GlyphVector

is ultimately
displayed.

The

GlyphVector

does not attempt any interpretation of
the sequence of glyphs it contains. Relationships between adjacent
glyphs in sequence are solely used to determine the placement of
the glyphs in the visual coordinate space.

Instances of

GlyphVector

are created by a

Font

.

In a text processing application that can cache intermediate
representations of text, creation and subsequent caching of a

GlyphVector

for use during rendering is the fastest
method to present the visual representation of characters to a user.

A

GlyphVector

is associated with exactly one

Font

, and can provide data useful only in relation to
this

Font

. In addition, metrics obtained from a

GlyphVector

are not generally geometrically scalable
since the pixelization and spacing are dependent on grid-fitting
algorithms within a

Font

. To facilitate accurate
measurement of a

GlyphVector

and its component
glyphs, you must specify a scaling transform, anti-alias mode, and
fractional metrics mode when creating the

GlyphVector

.
These characteristics can be derived from the destination device.

For each glyph in the

GlyphVector

, you can obtain:

- the position of the glyph

the transform associated with the glyph

the metrics of the glyph in the context of the

GlyphVector

. The metrics of the glyph may be
different under different transforms, application specified
rendering hints, and the specific instance of the glyph within
the

GlyphVector

.

Altering the data used to create the

GlyphVector

does not
alter the state of the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

**See Also:** Font

,

GlyphMetrics

,

TextLayout

public abstract class

GlyphVector

extends

Object

implements

Cloneable

A

GlyphVector

object is a collection of glyphs
containing geometric information for the placement of each glyph
in a transformed coordinate space which corresponds to the
device on which the

GlyphVector

is ultimately
displayed.

The

GlyphVector

does not attempt any interpretation of
the sequence of glyphs it contains. Relationships between adjacent
glyphs in sequence are solely used to determine the placement of
the glyphs in the visual coordinate space.

Instances of

GlyphVector

are created by a

Font

.

In a text processing application that can cache intermediate
representations of text, creation and subsequent caching of a

GlyphVector

for use during rendering is the fastest
method to present the visual representation of characters to a user.

A

GlyphVector

is associated with exactly one

Font

, and can provide data useful only in relation to
this

Font

. In addition, metrics obtained from a

GlyphVector

are not generally geometrically scalable
since the pixelization and spacing are dependent on grid-fitting
algorithms within a

Font

. To facilitate accurate
measurement of a

GlyphVector

and its component
glyphs, you must specify a scaling transform, anti-alias mode, and
fractional metrics mode when creating the

GlyphVector

.
These characteristics can be derived from the destination device.

For each glyph in the

GlyphVector

, you can obtain:

- the position of the glyph

the transform associated with the glyph

the metrics of the glyph in the context of the

GlyphVector

. The metrics of the glyph may be
different under different transforms, application specified
rendering hints, and the specific instance of the glyph within
the

GlyphVector

.

Altering the data used to create the

GlyphVector

does not
alter the state of the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

The

GlyphVector

does not attempt any interpretation of
the sequence of glyphs it contains. Relationships between adjacent
glyphs in sequence are solely used to determine the placement of
the glyphs in the visual coordinate space.

Instances of

GlyphVector

are created by a

Font

.

In a text processing application that can cache intermediate
representations of text, creation and subsequent caching of a

GlyphVector

for use during rendering is the fastest
method to present the visual representation of characters to a user.

A

GlyphVector

is associated with exactly one

Font

, and can provide data useful only in relation to
this

Font

. In addition, metrics obtained from a

GlyphVector

are not generally geometrically scalable
since the pixelization and spacing are dependent on grid-fitting
algorithms within a

Font

. To facilitate accurate
measurement of a

GlyphVector

and its component
glyphs, you must specify a scaling transform, anti-alias mode, and
fractional metrics mode when creating the

GlyphVector

.
These characteristics can be derived from the destination device.

For each glyph in the

GlyphVector

, you can obtain:

- the position of the glyph

the transform associated with the glyph

the metrics of the glyph in the context of the

GlyphVector

. The metrics of the glyph may be
different under different transforms, application specified
rendering hints, and the specific instance of the glyph within
the

GlyphVector

.

Altering the data used to create the

GlyphVector

does not
alter the state of the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

Instances of

GlyphVector

are created by a

Font

.

In a text processing application that can cache intermediate
representations of text, creation and subsequent caching of a

GlyphVector

for use during rendering is the fastest
method to present the visual representation of characters to a user.

A

GlyphVector

is associated with exactly one

Font

, and can provide data useful only in relation to
this

Font

. In addition, metrics obtained from a

GlyphVector

are not generally geometrically scalable
since the pixelization and spacing are dependent on grid-fitting
algorithms within a

Font

. To facilitate accurate
measurement of a

GlyphVector

and its component
glyphs, you must specify a scaling transform, anti-alias mode, and
fractional metrics mode when creating the

GlyphVector

.
These characteristics can be derived from the destination device.

For each glyph in the

GlyphVector

, you can obtain:

- the position of the glyph

the transform associated with the glyph

the metrics of the glyph in the context of the

GlyphVector

. The metrics of the glyph may be
different under different transforms, application specified
rendering hints, and the specific instance of the glyph within
the

GlyphVector

.

Altering the data used to create the

GlyphVector

does not
alter the state of the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

In a text processing application that can cache intermediate
representations of text, creation and subsequent caching of a

GlyphVector

for use during rendering is the fastest
method to present the visual representation of characters to a user.

A

GlyphVector

is associated with exactly one

Font

, and can provide data useful only in relation to
this

Font

. In addition, metrics obtained from a

GlyphVector

are not generally geometrically scalable
since the pixelization and spacing are dependent on grid-fitting
algorithms within a

Font

. To facilitate accurate
measurement of a

GlyphVector

and its component
glyphs, you must specify a scaling transform, anti-alias mode, and
fractional metrics mode when creating the

GlyphVector

.
These characteristics can be derived from the destination device.

For each glyph in the

GlyphVector

, you can obtain:

- the position of the glyph

the transform associated with the glyph

the metrics of the glyph in the context of the

GlyphVector

. The metrics of the glyph may be
different under different transforms, application specified
rendering hints, and the specific instance of the glyph within
the

GlyphVector

.

Altering the data used to create the

GlyphVector

does not
alter the state of the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

A

GlyphVector

is associated with exactly one

Font

, and can provide data useful only in relation to
this

Font

. In addition, metrics obtained from a

GlyphVector

are not generally geometrically scalable
since the pixelization and spacing are dependent on grid-fitting
algorithms within a

Font

. To facilitate accurate
measurement of a

GlyphVector

and its component
glyphs, you must specify a scaling transform, anti-alias mode, and
fractional metrics mode when creating the

GlyphVector

.
These characteristics can be derived from the destination device.

For each glyph in the

GlyphVector

, you can obtain:

- the position of the glyph

the transform associated with the glyph

the metrics of the glyph in the context of the

GlyphVector

. The metrics of the glyph may be
different under different transforms, application specified
rendering hints, and the specific instance of the glyph within
the

GlyphVector

.

Altering the data used to create the

GlyphVector

does not
alter the state of the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

For each glyph in the

GlyphVector

, you can obtain:

- the position of the glyph

the transform associated with the glyph

the metrics of the glyph in the context of the

GlyphVector

. The metrics of the glyph may be
different under different transforms, application specified
rendering hints, and the specific instance of the glyph within
the

GlyphVector

.

Altering the data used to create the

GlyphVector

does not
alter the state of the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

the position of the glyph

the transform associated with the glyph

the metrics of the glyph in the context of the

GlyphVector

. The metrics of the glyph may be
different under different transforms, application specified
rendering hints, and the specific instance of the glyph within
the

GlyphVector

.

Altering the data used to create the

GlyphVector

does not
alter the state of the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

Methods are provided to adjust the positions of the glyphs
within the

GlyphVector

. These methods are most
appropriate for applications that are performing justification
operations for the presentation of the glyphs.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

Methods are provided to transform individual glyphs within the

GlyphVector

. These methods are primarily useful for
special effects.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

Methods are provided to return both the visual, logical, and pixel bounds
of the entire

GlyphVector

or of individual glyphs within
the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

Methods are provided to return a

Shape

for the

GlyphVector

, and for individual glyphs within the

GlyphVector

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

FLAG_COMPLEX_GLYPHS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a complex glyph-to-char mapping (one that does not map glyphs to chars one-to-one in
strictly ascending or descending order matching the run direction).

static int

FLAG_HAS_POSITION_ADJUSTMENTS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
position adjustments.

static int

FLAG_HAS_TRANSFORMS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
per-glyph transforms.

static int

FLAG_MASK

A mask for supported flags from getLayoutFlags.

static int

FLAG_RUN_RTL

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a right-to-left run direction.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GlyphVector

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract boolean

equals

​(

GlyphVector

set)

Tests if the specified

GlyphVector

exactly
equals this

GlyphVector

.

abstract

Font

getFont

()

Returns the

Font

associated with this

GlyphVector

.

abstract

FontRenderContext

getFontRenderContext

()

Returns the

FontRenderContext

associated with this

GlyphVector

.

int

getGlyphCharIndex

​(int glyphIndex)

Returns the character index of the specified glyph.

int[]

getGlyphCharIndices

​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)

Returns the character indices of the specified glyphs.

abstract int

getGlyphCode

​(int glyphIndex)

Returns the glyphcode of the specified glyph.

abstract int[]

getGlyphCodes

​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)

Returns an array of glyphcodes for the specified glyphs.

abstract

GlyphJustificationInfo

getGlyphJustificationInfo

​(int glyphIndex)

Returns the justification information for the glyph at
the specified index into this

GlyphVector

.

abstract

Shape

getGlyphLogicalBounds

​(int glyphIndex)

Returns the logical bounds of the specified glyph within this

GlyphVector

.

abstract

GlyphMetrics

getGlyphMetrics

​(int glyphIndex)

Returns the metrics of the glyph at the specified index into
this

GlyphVector

.

abstract

Shape

getGlyphOutline

​(int glyphIndex)

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

.

Shape

getGlyphOutline

​(int glyphIndex,
float x,
float y)

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

, offset to x, y.

Rectangle

getGlyphPixelBounds

​(int index,

FontRenderContext

renderFRC,
float x,
float y)

Returns the pixel bounds of the glyph at index when this

GlyphVector

is rendered in a

Graphics

with the
given

FontRenderContext

at the given location.

abstract

Point2D

getGlyphPosition

​(int glyphIndex)

Returns the position of the specified glyph relative to the
origin of this

GlyphVector

.

abstract float[]

getGlyphPositions

​(int beginGlyphIndex,
int numEntries,
float[] positionReturn)

Returns an array of glyph positions for the specified glyphs.

abstract

AffineTransform

getGlyphTransform

​(int glyphIndex)

Returns the transform of the specified glyph within this

GlyphVector

.

abstract

Shape

getGlyphVisualBounds

​(int glyphIndex)

Returns the visual bounds of the specified glyph within the

GlyphVector

.

int

getLayoutFlags

()

Returns flags describing the global state of the GlyphVector.

abstract

Rectangle2D

getLogicalBounds

()

Returns the logical bounds of this

GlyphVector

.

abstract int

getNumGlyphs

()

Returns the number of glyphs in this

GlyphVector

.

abstract

Shape

getOutline

()

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

.

abstract

Shape

getOutline

​(float x,
float y)

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

when
rendered at x, y.

Rectangle

getPixelBounds

​(

FontRenderContext

renderFRC,
float x,
float y)

Returns the pixel bounds of this

GlyphVector

when
rendered in a graphics with the given

FontRenderContext

at the given location.

abstract

Rectangle2D

getVisualBounds

()

Returns the visual bounds of this

GlyphVector

The visual bounds is the bounding box of the outline of this

GlyphVector

.

abstract void

performDefaultLayout

()

Assigns default positions to each glyph in this

GlyphVector

.

abstract void

setGlyphPosition

​(int glyphIndex,

Point2D

newPos)

Sets the position of the specified glyph within this

GlyphVector

.

abstract void

setGlyphTransform

​(int glyphIndex,

AffineTransform

newTX)

Sets the transform of the specified glyph within this

GlyphVector

.

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

static int

FLAG_COMPLEX_GLYPHS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a complex glyph-to-char mapping (one that does not map glyphs to chars one-to-one in
strictly ascending or descending order matching the run direction).

static int

FLAG_HAS_POSITION_ADJUSTMENTS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
position adjustments.

static int

FLAG_HAS_TRANSFORMS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
per-glyph transforms.

static int

FLAG_MASK

A mask for supported flags from getLayoutFlags.

static int

FLAG_RUN_RTL

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a right-to-left run direction.

---

#### Field Summary

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a complex glyph-to-char mapping (one that does not map glyphs to chars one-to-one in
strictly ascending or descending order matching the run direction).

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
position adjustments.

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
per-glyph transforms.

A mask for supported flags from getLayoutFlags.

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a right-to-left run direction.

Constructor Summary

Constructors

Constructor

Description

GlyphVector

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract boolean

equals

​(

GlyphVector

set)

Tests if the specified

GlyphVector

exactly
equals this

GlyphVector

.

abstract

Font

getFont

()

Returns the

Font

associated with this

GlyphVector

.

abstract

FontRenderContext

getFontRenderContext

()

Returns the

FontRenderContext

associated with this

GlyphVector

.

int

getGlyphCharIndex

​(int glyphIndex)

Returns the character index of the specified glyph.

int[]

getGlyphCharIndices

​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)

Returns the character indices of the specified glyphs.

abstract int

getGlyphCode

​(int glyphIndex)

Returns the glyphcode of the specified glyph.

abstract int[]

getGlyphCodes

​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)

Returns an array of glyphcodes for the specified glyphs.

abstract

GlyphJustificationInfo

getGlyphJustificationInfo

​(int glyphIndex)

Returns the justification information for the glyph at
the specified index into this

GlyphVector

.

abstract

Shape

getGlyphLogicalBounds

​(int glyphIndex)

Returns the logical bounds of the specified glyph within this

GlyphVector

.

abstract

GlyphMetrics

getGlyphMetrics

​(int glyphIndex)

Returns the metrics of the glyph at the specified index into
this

GlyphVector

.

abstract

Shape

getGlyphOutline

​(int glyphIndex)

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

.

Shape

getGlyphOutline

​(int glyphIndex,
float x,
float y)

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

, offset to x, y.

Rectangle

getGlyphPixelBounds

​(int index,

FontRenderContext

renderFRC,
float x,
float y)

Returns the pixel bounds of the glyph at index when this

GlyphVector

is rendered in a

Graphics

with the
given

FontRenderContext

at the given location.

abstract

Point2D

getGlyphPosition

​(int glyphIndex)

Returns the position of the specified glyph relative to the
origin of this

GlyphVector

.

abstract float[]

getGlyphPositions

​(int beginGlyphIndex,
int numEntries,
float[] positionReturn)

Returns an array of glyph positions for the specified glyphs.

abstract

AffineTransform

getGlyphTransform

​(int glyphIndex)

Returns the transform of the specified glyph within this

GlyphVector

.

abstract

Shape

getGlyphVisualBounds

​(int glyphIndex)

Returns the visual bounds of the specified glyph within the

GlyphVector

.

int

getLayoutFlags

()

Returns flags describing the global state of the GlyphVector.

abstract

Rectangle2D

getLogicalBounds

()

Returns the logical bounds of this

GlyphVector

.

abstract int

getNumGlyphs

()

Returns the number of glyphs in this

GlyphVector

.

abstract

Shape

getOutline

()

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

.

abstract

Shape

getOutline

​(float x,
float y)

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

when
rendered at x, y.

Rectangle

getPixelBounds

​(

FontRenderContext

renderFRC,
float x,
float y)

Returns the pixel bounds of this

GlyphVector

when
rendered in a graphics with the given

FontRenderContext

at the given location.

abstract

Rectangle2D

getVisualBounds

()

Returns the visual bounds of this

GlyphVector

The visual bounds is the bounding box of the outline of this

GlyphVector

.

abstract void

performDefaultLayout

()

Assigns default positions to each glyph in this

GlyphVector

.

abstract void

setGlyphPosition

​(int glyphIndex,

Point2D

newPos)

Sets the position of the specified glyph within this

GlyphVector

.

abstract void

setGlyphTransform

​(int glyphIndex,

AffineTransform

newTX)

Sets the transform of the specified glyph within this

GlyphVector

.

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

Tests if the specified

GlyphVector

exactly
equals this

GlyphVector

.

Returns the

Font

associated with this

GlyphVector

.

Returns the

FontRenderContext

associated with this

GlyphVector

.

Returns the character index of the specified glyph.

Returns the character indices of the specified glyphs.

Returns the glyphcode of the specified glyph.

Returns an array of glyphcodes for the specified glyphs.

Returns the justification information for the glyph at
the specified index into this

GlyphVector

.

Returns the logical bounds of the specified glyph within this

GlyphVector

.

Returns the metrics of the glyph at the specified index into
this

GlyphVector

.

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

.

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

, offset to x, y.

Returns the pixel bounds of the glyph at index when this

GlyphVector

is rendered in a

Graphics

with the
given

FontRenderContext

at the given location.

Returns the position of the specified glyph relative to the
origin of this

GlyphVector

.

Returns an array of glyph positions for the specified glyphs.

Returns the transform of the specified glyph within this

GlyphVector

.

Returns the visual bounds of the specified glyph within the

GlyphVector

.

Returns flags describing the global state of the GlyphVector.

Returns the logical bounds of this

GlyphVector

.

Returns the number of glyphs in this

GlyphVector

.

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

.

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

when
rendered at x, y.

Returns the pixel bounds of this

GlyphVector

when
rendered in a graphics with the given

FontRenderContext

at the given location.

Returns the visual bounds of this

GlyphVector

The visual bounds is the bounding box of the outline of this

GlyphVector

.

Assigns default positions to each glyph in this

GlyphVector

.

Sets the position of the specified glyph within this

GlyphVector

.

Sets the transform of the specified glyph within this

GlyphVector

.

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

- FLAG_HAS_TRANSFORMS

```java
public static final int FLAG_HAS_TRANSFORMS
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
per-glyph transforms.

**Since:** 1.4
**See Also:** Constant Field Values

- FLAG_HAS_POSITION_ADJUSTMENTS

```java
public static final int FLAG_HAS_POSITION_ADJUSTMENTS
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
position adjustments. When this is true, the glyph positions don't match the
accumulated default advances of the glyphs (for example, if kerning has been done).

**Since:** 1.4
**See Also:** Constant Field Values

- FLAG_RUN_RTL

```java
public static final int FLAG_RUN_RTL
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a right-to-left run direction. This refers to the glyph-to-char mapping and does
not imply that the visual locations of the glyphs are necessarily in this order,
although generally they will be.

**Since:** 1.4
**See Also:** Constant Field Values

- FLAG_COMPLEX_GLYPHS

```java
public static final int FLAG_COMPLEX_GLYPHS
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a complex glyph-to-char mapping (one that does not map glyphs to chars one-to-one in
strictly ascending or descending order matching the run direction).

**Since:** 1.4
**See Also:** Constant Field Values

- FLAG_MASK

```java
public static final int FLAG_MASK
```

A mask for supported flags from getLayoutFlags. Only bits covered by the mask
should be tested.

**Since:** 1.4
**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GlyphVector

```java
public GlyphVector()
```

============ METHOD DETAIL ==========

- Method Detail

- getFont

```java
public abstract
Font
getFont()
```

Returns the

Font

associated with this

GlyphVector

.

**Returns:** Font

used to create this

GlyphVector

.
**See Also:** Font

- getFontRenderContext

```java
public abstract
FontRenderContext
getFontRenderContext()
```

Returns the

FontRenderContext

associated with this

GlyphVector

.

**Returns:** FontRenderContext

used to create this

GlyphVector

.
**See Also:** FontRenderContext

,

Font

- performDefaultLayout

```java
public abstract void performDefaultLayout()
```

Assigns default positions to each glyph in this

GlyphVector

. This can destroy information
generated during initial layout of this

GlyphVector

.

- getNumGlyphs

```java
public abstract int getNumGlyphs()
```

Returns the number of glyphs in this

GlyphVector

.

**Returns:** number of glyphs in this

GlyphVector

.

- getGlyphCode

```java
public abstract int getGlyphCode​(int glyphIndex)
```

Returns the glyphcode of the specified glyph.
This return value is meaningless to anything other
than the

Font

object that created this

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve the
glyphcode.
**Returns:** the glyphcode of the glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the
number of glyphs in this

GlyphVector

- getGlyphCodes

```java
public abstract int[] getGlyphCodes​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)
```

Returns an array of glyphcodes for the specified glyphs.
The contents of this return value are meaningless to anything other
than the

Font

used to create this

GlyphVector

. This method is used
for convenience and performance when processing glyphcodes.
If no array is passed in, a new array is created.

**Parameters:** beginGlyphIndex

- the index into this

GlyphVector

at which to start retrieving glyphcodes
**Parameters:** numEntries

- the number of glyphcodes to retrieve
**Parameters:** codeReturn

- the array that receives the glyphcodes and is
then returned
**Returns:** an array of glyphcodes for the specified glyphs.
**Throws:** IllegalArgumentException

- if

numEntries

is
less than 0
**Throws:** IndexOutOfBoundsException

- if

beginGlyphIndex

is less than 0
**Throws:** IndexOutOfBoundsException

- if the sum of

beginGlyphIndex

and

numEntries

is
greater than the number of glyphs in this

GlyphVector

- getGlyphCharIndex

```java
public int getGlyphCharIndex​(int glyphIndex)
```

Returns the character index of the specified glyph.
The character index is the index of the first logical
character represented by the glyph. The default
implementation assumes a one-to-one, left-to-right mapping
of glyphs to characters.

**Parameters:** glyphIndex

- the index of the glyph
**Returns:** the index of the first character represented by the glyph
**Since:** 1.4

- getGlyphCharIndices

```java
public int[] getGlyphCharIndices​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)
```

Returns the character indices of the specified glyphs.
The character index is the index of the first logical
character represented by the glyph. Indices are returned
in glyph order. The default implementation invokes
getGlyphCharIndex for each glyph, and subclassers will probably
want to override this implementation for performance reasons.
Use this method for convenience and performance
in processing of glyphcodes. If no array is passed in,
a new array is created.

**Parameters:** beginGlyphIndex

- the index of the first glyph
**Parameters:** numEntries

- the number of glyph indices
**Parameters:** codeReturn

- the array into which to return the character indices
**Returns:** an array of character indices, one per glyph.
**Since:** 1.4

- getLogicalBounds

```java
public abstract
Rectangle2D
getLogicalBounds()
```

Returns the logical bounds of this

GlyphVector

.
This method is used when positioning this

GlyphVector

in relation to visually adjacent

GlyphVector

objects.

**Returns:** a

Rectangle2D

that is the logical bounds of this

GlyphVector

.

- getVisualBounds

```java
public abstract
Rectangle2D
getVisualBounds()
```

Returns the visual bounds of this

GlyphVector

The visual bounds is the bounding box of the outline of this

GlyphVector

. Because of rasterization and
alignment of pixels, it is possible that this box does not
enclose all pixels affected by rendering this

GlyphVector

.

**Returns:** a

Rectangle2D

that is the bounding box
of this

GlyphVector

.

- getPixelBounds

```java
public
Rectangle
getPixelBounds​(
FontRenderContext
renderFRC,
float x,
float y)
```

Returns the pixel bounds of this

GlyphVector

when
rendered in a graphics with the given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds,
offset to x, y and rounded out to the next integer value (i.e. returns an
integer rectangle which encloses the visual bounds) and
ignores the FRC. Subclassers should override this method.

**Parameters:** renderFRC

- the

FontRenderContext

of the

Graphics

.
**Parameters:** x

- the x-coordinate at which to render this

GlyphVector

.
**Parameters:** y

- the y-coordinate at which to render this

GlyphVector

.
**Returns:** a

Rectangle

bounding the pixels that would be affected.
**Since:** 1.4

- getOutline

```java
public abstract
Shape
getOutline()
```

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

.

**Returns:** a

Shape

that is the outline of this

GlyphVector

.

- getOutline

```java
public abstract
Shape
getOutline​(float x,
float y)
```

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

when
rendered at x, y.

**Parameters:** x

- the X coordinate of this

GlyphVector

.
**Parameters:** y

- the Y coordinate of this

GlyphVector

.
**Returns:** a

Shape

that is the outline of this

GlyphVector

when rendered at the specified
coordinates.

- getGlyphOutline

```java
public abstract
Shape
getGlyphOutline​(int glyphIndex)
```

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

.
The outline returned by this method is positioned around the
origin of each individual glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Returns:** a

Shape

that is the outline of the glyph
at the specified

glyphIndex

of this

GlyphVector

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

- getGlyphOutline

```java
public
Shape
getGlyphOutline​(int glyphIndex,
float x,
float y)
```

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

, offset to x, y.
The outline returned by this method is positioned around the
origin of each individual glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Parameters:** x

- the X coordinate of the location of this

GlyphVector
**Parameters:** y

- the Y coordinate of the location of this

GlyphVector
**Returns:** a

Shape

that is the outline of the glyph
at the specified

glyphIndex

of this

GlyphVector

when rendered at the specified
coordinates.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**Since:** 1.4

- getGlyphPosition

```java
public abstract
Point2D
getGlyphPosition​(int glyphIndex)
```

Returns the position of the specified glyph relative to the
origin of this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method returns the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Returns:** a

Point2D

object that is the position of the glyph
at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than the number of glyphs
in this

GlyphVector
**See Also:** setGlyphPosition(int, java.awt.geom.Point2D)

- setGlyphPosition

```java
public abstract void setGlyphPosition​(int glyphIndex,

Point2D
newPos)
```

Sets the position of the specified glyph within this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method sets the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Parameters:** newPos

- the

Point2D

at which to position the
glyph at the specified

glyphIndex
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than the number of glyphs
in this

GlyphVector
**See Also:** getGlyphPosition(int)

- getGlyphTransform

```java
public abstract
AffineTransform
getGlyphTransform​(int glyphIndex)
```

Returns the transform of the specified glyph within this

GlyphVector

. The transform is relative to the
glyph position. If no special transform has been applied,

null

can be returned. A null return indicates
an identity transform.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Returns:** an

AffineTransform

that is the transform of
the glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** setGlyphTransform(int, java.awt.geom.AffineTransform)

- setGlyphTransform

```java
public abstract void setGlyphTransform​(int glyphIndex,

AffineTransform
newTX)
```

Sets the transform of the specified glyph within this

GlyphVector

. The transform is relative to the glyph
position. A

null

argument for

newTX

indicates that no special transform is applied for the specified
glyph.
This method can be used to rotate, mirror, translate and scale the
glyph. Adding a transform can result in significant performance changes.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Parameters:** newTX

- the new transform of the glyph at

glyphIndex
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** getGlyphTransform(int)

- getLayoutFlags

```java
public int getLayoutFlags()
```

Returns flags describing the global state of the GlyphVector.
Flags not described below are reserved. The default
implementation returns 0 (meaning false) for the position adjustments,
transforms, rtl, and complex flags.
Subclassers should override this method, and make sure
it correctly describes the GlyphVector and corresponds
to the results of related calls.

**Returns:** an int containing the flags describing the state
**Since:** 1.4
**See Also:** FLAG_HAS_POSITION_ADJUSTMENTS

,

FLAG_HAS_TRANSFORMS

,

FLAG_RUN_RTL

,

FLAG_COMPLEX_GLYPHS

,

FLAG_MASK

- getGlyphPositions

```java
public abstract float[] getGlyphPositions​(int beginGlyphIndex,
int numEntries,
float[] positionReturn)
```

Returns an array of glyph positions for the specified glyphs.
This method is used for convenience and performance when
processing glyph positions.
If no array is passed in, a new array is created.
Even numbered array entries beginning with position zero are the X
coordinates of the glyph numbered

beginGlyphIndex + position/2

.
Odd numbered array entries beginning with position one are the Y
coordinates of the glyph numbered

beginGlyphIndex + (position-1)/2

.
If

beginGlyphIndex

equals the number of glyphs in
this

GlyphVector

, this method gets the position after
the last glyph and this position is used to define the advance of
the entire

GlyphVector

.

**Parameters:** beginGlyphIndex

- the index at which to begin retrieving
glyph positions
**Parameters:** numEntries

- the number of glyphs to retrieve
**Parameters:** positionReturn

- the array that receives the glyph positions
and is then returned.
**Returns:** an array of glyph positions specified by

beginGlyphIndex

and

numEntries

.
**Throws:** IllegalArgumentException

- if

numEntries

is
less than 0
**Throws:** IndexOutOfBoundsException

- if

beginGlyphIndex

is less than 0
**Throws:** IndexOutOfBoundsException

- if the sum of

beginGlyphIndex

and

numEntries

is greater than the number of glyphs in this

GlyphVector

plus one

- getGlyphLogicalBounds

```java
public abstract
Shape
getGlyphLogicalBounds​(int glyphIndex)
```

Returns the logical bounds of the specified glyph within this

GlyphVector

.
These logical bounds have a total of four edges, with two edges
parallel to the baseline under the glyph's transform and the other two
edges are shared with adjacent glyphs if they are present. This
method is useful for hit-testing of the specified glyph,
positioning of a caret at the leading or trailing edge of a glyph,
and for drawing a highlight region around the specified glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its logical
bounds
**Returns:** a

Shape

that is the logical bounds of the
glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** getGlyphVisualBounds(int)

- getGlyphVisualBounds

```java
public abstract
Shape
getGlyphVisualBounds​(int glyphIndex)
```

Returns the visual bounds of the specified glyph within the

GlyphVector

.
The bounds returned by this method is positioned around the
origin of each individual glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its visual
bounds
**Returns:** a

Shape

that is the visual bounds of the
glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** getGlyphLogicalBounds(int)

- getGlyphPixelBounds

```java
public
Rectangle
getGlyphPixelBounds​(int index,

FontRenderContext
renderFRC,
float x,
float y)
```

Returns the pixel bounds of the glyph at index when this

GlyphVector

is rendered in a

Graphics

with the
given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds of the glyph,
offset to x, y and rounded out to the next integer value, and
ignores the FRC. Subclassers should override this method.

**Parameters:** index

- the index of the glyph.
**Parameters:** renderFRC

- the

FontRenderContext

of the

Graphics

.
**Parameters:** x

- the X position at which to render this

GlyphVector

.
**Parameters:** y

- the Y position at which to render this

GlyphVector

.
**Returns:** a

Rectangle

bounding the pixels that would be affected.
**Since:** 1.4

- getGlyphMetrics

```java
public abstract
GlyphMetrics
getGlyphMetrics​(int glyphIndex)
```

Returns the metrics of the glyph at the specified index into
this

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its metrics
**Returns:** a

GlyphMetrics

object that represents the
metrics of the glyph at the specified

glyphIndex

into this

GlyphVector

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

- getGlyphJustificationInfo

```java
public abstract
GlyphJustificationInfo
getGlyphJustificationInfo​(int glyphIndex)
```

Returns the justification information for the glyph at
the specified index into this

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its
justification properties
**Returns:** a

GlyphJustificationInfo

object that
represents the justification properties of the glyph at the
specified

glyphIndex

into this

GlyphVector

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

- equals

```java
public abstract boolean equals​(
GlyphVector
set)
```

Tests if the specified

GlyphVector

exactly
equals this

GlyphVector

.

**Parameters:** set

- the specified

GlyphVector

to test
**Returns:** true

if the specified

GlyphVector

equals this

GlyphVector

;

false

otherwise.

Field Detail

- FLAG_HAS_TRANSFORMS

```java
public static final int FLAG_HAS_TRANSFORMS
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
per-glyph transforms.

**Since:** 1.4
**See Also:** Constant Field Values

- FLAG_HAS_POSITION_ADJUSTMENTS

```java
public static final int FLAG_HAS_POSITION_ADJUSTMENTS
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
position adjustments. When this is true, the glyph positions don't match the
accumulated default advances of the glyphs (for example, if kerning has been done).

**Since:** 1.4
**See Also:** Constant Field Values

- FLAG_RUN_RTL

```java
public static final int FLAG_RUN_RTL
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a right-to-left run direction. This refers to the glyph-to-char mapping and does
not imply that the visual locations of the glyphs are necessarily in this order,
although generally they will be.

**Since:** 1.4
**See Also:** Constant Field Values

- FLAG_COMPLEX_GLYPHS

```java
public static final int FLAG_COMPLEX_GLYPHS
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a complex glyph-to-char mapping (one that does not map glyphs to chars one-to-one in
strictly ascending or descending order matching the run direction).

**Since:** 1.4
**See Also:** Constant Field Values

- FLAG_MASK

```java
public static final int FLAG_MASK
```

A mask for supported flags from getLayoutFlags. Only bits covered by the mask
should be tested.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### Field Detail

FLAG_HAS_TRANSFORMS

```java
public static final int FLAG_HAS_TRANSFORMS
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
per-glyph transforms.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### FLAG_HAS_TRANSFORMS

public static final int FLAG_HAS_TRANSFORMS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
per-glyph transforms.

FLAG_HAS_POSITION_ADJUSTMENTS

```java
public static final int FLAG_HAS_POSITION_ADJUSTMENTS
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
position adjustments. When this is true, the glyph positions don't match the
accumulated default advances of the glyphs (for example, if kerning has been done).

**Since:** 1.4
**See Also:** Constant Field Values

---

#### FLAG_HAS_POSITION_ADJUSTMENTS

public static final int FLAG_HAS_POSITION_ADJUSTMENTS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
position adjustments. When this is true, the glyph positions don't match the
accumulated default advances of the glyphs (for example, if kerning has been done).

FLAG_RUN_RTL

```java
public static final int FLAG_RUN_RTL
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a right-to-left run direction. This refers to the glyph-to-char mapping and does
not imply that the visual locations of the glyphs are necessarily in this order,
although generally they will be.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### FLAG_RUN_RTL

public static final int FLAG_RUN_RTL

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a right-to-left run direction. This refers to the glyph-to-char mapping and does
not imply that the visual locations of the glyphs are necessarily in this order,
although generally they will be.

FLAG_COMPLEX_GLYPHS

```java
public static final int FLAG_COMPLEX_GLYPHS
```

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a complex glyph-to-char mapping (one that does not map glyphs to chars one-to-one in
strictly ascending or descending order matching the run direction).

**Since:** 1.4
**See Also:** Constant Field Values

---

#### FLAG_COMPLEX_GLYPHS

public static final int FLAG_COMPLEX_GLYPHS

A flag used with getLayoutFlags that indicates that this

GlyphVector

has
a complex glyph-to-char mapping (one that does not map glyphs to chars one-to-one in
strictly ascending or descending order matching the run direction).

FLAG_MASK

```java
public static final int FLAG_MASK
```

A mask for supported flags from getLayoutFlags. Only bits covered by the mask
should be tested.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### FLAG_MASK

public static final int FLAG_MASK

A mask for supported flags from getLayoutFlags. Only bits covered by the mask
should be tested.

Constructor Detail

- GlyphVector

```java
public GlyphVector()
```

---

#### Constructor Detail

GlyphVector

```java
public GlyphVector()
```

---

#### GlyphVector

public GlyphVector()

Method Detail

- getFont

```java
public abstract
Font
getFont()
```

Returns the

Font

associated with this

GlyphVector

.

**Returns:** Font

used to create this

GlyphVector

.
**See Also:** Font

- getFontRenderContext

```java
public abstract
FontRenderContext
getFontRenderContext()
```

Returns the

FontRenderContext

associated with this

GlyphVector

.

**Returns:** FontRenderContext

used to create this

GlyphVector

.
**See Also:** FontRenderContext

,

Font

- performDefaultLayout

```java
public abstract void performDefaultLayout()
```

Assigns default positions to each glyph in this

GlyphVector

. This can destroy information
generated during initial layout of this

GlyphVector

.

- getNumGlyphs

```java
public abstract int getNumGlyphs()
```

Returns the number of glyphs in this

GlyphVector

.

**Returns:** number of glyphs in this

GlyphVector

.

- getGlyphCode

```java
public abstract int getGlyphCode​(int glyphIndex)
```

Returns the glyphcode of the specified glyph.
This return value is meaningless to anything other
than the

Font

object that created this

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve the
glyphcode.
**Returns:** the glyphcode of the glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the
number of glyphs in this

GlyphVector

- getGlyphCodes

```java
public abstract int[] getGlyphCodes​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)
```

Returns an array of glyphcodes for the specified glyphs.
The contents of this return value are meaningless to anything other
than the

Font

used to create this

GlyphVector

. This method is used
for convenience and performance when processing glyphcodes.
If no array is passed in, a new array is created.

**Parameters:** beginGlyphIndex

- the index into this

GlyphVector

at which to start retrieving glyphcodes
**Parameters:** numEntries

- the number of glyphcodes to retrieve
**Parameters:** codeReturn

- the array that receives the glyphcodes and is
then returned
**Returns:** an array of glyphcodes for the specified glyphs.
**Throws:** IllegalArgumentException

- if

numEntries

is
less than 0
**Throws:** IndexOutOfBoundsException

- if

beginGlyphIndex

is less than 0
**Throws:** IndexOutOfBoundsException

- if the sum of

beginGlyphIndex

and

numEntries

is
greater than the number of glyphs in this

GlyphVector

- getGlyphCharIndex

```java
public int getGlyphCharIndex​(int glyphIndex)
```

Returns the character index of the specified glyph.
The character index is the index of the first logical
character represented by the glyph. The default
implementation assumes a one-to-one, left-to-right mapping
of glyphs to characters.

**Parameters:** glyphIndex

- the index of the glyph
**Returns:** the index of the first character represented by the glyph
**Since:** 1.4

- getGlyphCharIndices

```java
public int[] getGlyphCharIndices​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)
```

Returns the character indices of the specified glyphs.
The character index is the index of the first logical
character represented by the glyph. Indices are returned
in glyph order. The default implementation invokes
getGlyphCharIndex for each glyph, and subclassers will probably
want to override this implementation for performance reasons.
Use this method for convenience and performance
in processing of glyphcodes. If no array is passed in,
a new array is created.

**Parameters:** beginGlyphIndex

- the index of the first glyph
**Parameters:** numEntries

- the number of glyph indices
**Parameters:** codeReturn

- the array into which to return the character indices
**Returns:** an array of character indices, one per glyph.
**Since:** 1.4

- getLogicalBounds

```java
public abstract
Rectangle2D
getLogicalBounds()
```

Returns the logical bounds of this

GlyphVector

.
This method is used when positioning this

GlyphVector

in relation to visually adjacent

GlyphVector

objects.

**Returns:** a

Rectangle2D

that is the logical bounds of this

GlyphVector

.

- getVisualBounds

```java
public abstract
Rectangle2D
getVisualBounds()
```

Returns the visual bounds of this

GlyphVector

The visual bounds is the bounding box of the outline of this

GlyphVector

. Because of rasterization and
alignment of pixels, it is possible that this box does not
enclose all pixels affected by rendering this

GlyphVector

.

**Returns:** a

Rectangle2D

that is the bounding box
of this

GlyphVector

.

- getPixelBounds

```java
public
Rectangle
getPixelBounds​(
FontRenderContext
renderFRC,
float x,
float y)
```

Returns the pixel bounds of this

GlyphVector

when
rendered in a graphics with the given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds,
offset to x, y and rounded out to the next integer value (i.e. returns an
integer rectangle which encloses the visual bounds) and
ignores the FRC. Subclassers should override this method.

**Parameters:** renderFRC

- the

FontRenderContext

of the

Graphics

.
**Parameters:** x

- the x-coordinate at which to render this

GlyphVector

.
**Parameters:** y

- the y-coordinate at which to render this

GlyphVector

.
**Returns:** a

Rectangle

bounding the pixels that would be affected.
**Since:** 1.4

- getOutline

```java
public abstract
Shape
getOutline()
```

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

.

**Returns:** a

Shape

that is the outline of this

GlyphVector

.

- getOutline

```java
public abstract
Shape
getOutline​(float x,
float y)
```

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

when
rendered at x, y.

**Parameters:** x

- the X coordinate of this

GlyphVector

.
**Parameters:** y

- the Y coordinate of this

GlyphVector

.
**Returns:** a

Shape

that is the outline of this

GlyphVector

when rendered at the specified
coordinates.

- getGlyphOutline

```java
public abstract
Shape
getGlyphOutline​(int glyphIndex)
```

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

.
The outline returned by this method is positioned around the
origin of each individual glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Returns:** a

Shape

that is the outline of the glyph
at the specified

glyphIndex

of this

GlyphVector

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

- getGlyphOutline

```java
public
Shape
getGlyphOutline​(int glyphIndex,
float x,
float y)
```

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

, offset to x, y.
The outline returned by this method is positioned around the
origin of each individual glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Parameters:** x

- the X coordinate of the location of this

GlyphVector
**Parameters:** y

- the Y coordinate of the location of this

GlyphVector
**Returns:** a

Shape

that is the outline of the glyph
at the specified

glyphIndex

of this

GlyphVector

when rendered at the specified
coordinates.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**Since:** 1.4

- getGlyphPosition

```java
public abstract
Point2D
getGlyphPosition​(int glyphIndex)
```

Returns the position of the specified glyph relative to the
origin of this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method returns the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Returns:** a

Point2D

object that is the position of the glyph
at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than the number of glyphs
in this

GlyphVector
**See Also:** setGlyphPosition(int, java.awt.geom.Point2D)

- setGlyphPosition

```java
public abstract void setGlyphPosition​(int glyphIndex,

Point2D
newPos)
```

Sets the position of the specified glyph within this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method sets the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Parameters:** newPos

- the

Point2D

at which to position the
glyph at the specified

glyphIndex
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than the number of glyphs
in this

GlyphVector
**See Also:** getGlyphPosition(int)

- getGlyphTransform

```java
public abstract
AffineTransform
getGlyphTransform​(int glyphIndex)
```

Returns the transform of the specified glyph within this

GlyphVector

. The transform is relative to the
glyph position. If no special transform has been applied,

null

can be returned. A null return indicates
an identity transform.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Returns:** an

AffineTransform

that is the transform of
the glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** setGlyphTransform(int, java.awt.geom.AffineTransform)

- setGlyphTransform

```java
public abstract void setGlyphTransform​(int glyphIndex,

AffineTransform
newTX)
```

Sets the transform of the specified glyph within this

GlyphVector

. The transform is relative to the glyph
position. A

null

argument for

newTX

indicates that no special transform is applied for the specified
glyph.
This method can be used to rotate, mirror, translate and scale the
glyph. Adding a transform can result in significant performance changes.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Parameters:** newTX

- the new transform of the glyph at

glyphIndex
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** getGlyphTransform(int)

- getLayoutFlags

```java
public int getLayoutFlags()
```

Returns flags describing the global state of the GlyphVector.
Flags not described below are reserved. The default
implementation returns 0 (meaning false) for the position adjustments,
transforms, rtl, and complex flags.
Subclassers should override this method, and make sure
it correctly describes the GlyphVector and corresponds
to the results of related calls.

**Returns:** an int containing the flags describing the state
**Since:** 1.4
**See Also:** FLAG_HAS_POSITION_ADJUSTMENTS

,

FLAG_HAS_TRANSFORMS

,

FLAG_RUN_RTL

,

FLAG_COMPLEX_GLYPHS

,

FLAG_MASK

- getGlyphPositions

```java
public abstract float[] getGlyphPositions​(int beginGlyphIndex,
int numEntries,
float[] positionReturn)
```

Returns an array of glyph positions for the specified glyphs.
This method is used for convenience and performance when
processing glyph positions.
If no array is passed in, a new array is created.
Even numbered array entries beginning with position zero are the X
coordinates of the glyph numbered

beginGlyphIndex + position/2

.
Odd numbered array entries beginning with position one are the Y
coordinates of the glyph numbered

beginGlyphIndex + (position-1)/2

.
If

beginGlyphIndex

equals the number of glyphs in
this

GlyphVector

, this method gets the position after
the last glyph and this position is used to define the advance of
the entire

GlyphVector

.

**Parameters:** beginGlyphIndex

- the index at which to begin retrieving
glyph positions
**Parameters:** numEntries

- the number of glyphs to retrieve
**Parameters:** positionReturn

- the array that receives the glyph positions
and is then returned.
**Returns:** an array of glyph positions specified by

beginGlyphIndex

and

numEntries

.
**Throws:** IllegalArgumentException

- if

numEntries

is
less than 0
**Throws:** IndexOutOfBoundsException

- if

beginGlyphIndex

is less than 0
**Throws:** IndexOutOfBoundsException

- if the sum of

beginGlyphIndex

and

numEntries

is greater than the number of glyphs in this

GlyphVector

plus one

- getGlyphLogicalBounds

```java
public abstract
Shape
getGlyphLogicalBounds​(int glyphIndex)
```

Returns the logical bounds of the specified glyph within this

GlyphVector

.
These logical bounds have a total of four edges, with two edges
parallel to the baseline under the glyph's transform and the other two
edges are shared with adjacent glyphs if they are present. This
method is useful for hit-testing of the specified glyph,
positioning of a caret at the leading or trailing edge of a glyph,
and for drawing a highlight region around the specified glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its logical
bounds
**Returns:** a

Shape

that is the logical bounds of the
glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** getGlyphVisualBounds(int)

- getGlyphVisualBounds

```java
public abstract
Shape
getGlyphVisualBounds​(int glyphIndex)
```

Returns the visual bounds of the specified glyph within the

GlyphVector

.
The bounds returned by this method is positioned around the
origin of each individual glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its visual
bounds
**Returns:** a

Shape

that is the visual bounds of the
glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** getGlyphLogicalBounds(int)

- getGlyphPixelBounds

```java
public
Rectangle
getGlyphPixelBounds​(int index,

FontRenderContext
renderFRC,
float x,
float y)
```

Returns the pixel bounds of the glyph at index when this

GlyphVector

is rendered in a

Graphics

with the
given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds of the glyph,
offset to x, y and rounded out to the next integer value, and
ignores the FRC. Subclassers should override this method.

**Parameters:** index

- the index of the glyph.
**Parameters:** renderFRC

- the

FontRenderContext

of the

Graphics

.
**Parameters:** x

- the X position at which to render this

GlyphVector

.
**Parameters:** y

- the Y position at which to render this

GlyphVector

.
**Returns:** a

Rectangle

bounding the pixels that would be affected.
**Since:** 1.4

- getGlyphMetrics

```java
public abstract
GlyphMetrics
getGlyphMetrics​(int glyphIndex)
```

Returns the metrics of the glyph at the specified index into
this

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its metrics
**Returns:** a

GlyphMetrics

object that represents the
metrics of the glyph at the specified

glyphIndex

into this

GlyphVector

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

- getGlyphJustificationInfo

```java
public abstract
GlyphJustificationInfo
getGlyphJustificationInfo​(int glyphIndex)
```

Returns the justification information for the glyph at
the specified index into this

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its
justification properties
**Returns:** a

GlyphJustificationInfo

object that
represents the justification properties of the glyph at the
specified

glyphIndex

into this

GlyphVector

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

- equals

```java
public abstract boolean equals​(
GlyphVector
set)
```

Tests if the specified

GlyphVector

exactly
equals this

GlyphVector

.

**Parameters:** set

- the specified

GlyphVector

to test
**Returns:** true

if the specified

GlyphVector

equals this

GlyphVector

;

false

otherwise.

---

#### Method Detail

getFont

```java
public abstract
Font
getFont()
```

Returns the

Font

associated with this

GlyphVector

.

**Returns:** Font

used to create this

GlyphVector

.
**See Also:** Font

---

#### getFont

public abstract

Font

getFont()

Returns the

Font

associated with this

GlyphVector

.

getFontRenderContext

```java
public abstract
FontRenderContext
getFontRenderContext()
```

Returns the

FontRenderContext

associated with this

GlyphVector

.

**Returns:** FontRenderContext

used to create this

GlyphVector

.
**See Also:** FontRenderContext

,

Font

---

#### getFontRenderContext

public abstract

FontRenderContext

getFontRenderContext()

Returns the

FontRenderContext

associated with this

GlyphVector

.

performDefaultLayout

```java
public abstract void performDefaultLayout()
```

Assigns default positions to each glyph in this

GlyphVector

. This can destroy information
generated during initial layout of this

GlyphVector

.

---

#### performDefaultLayout

public abstract void performDefaultLayout()

Assigns default positions to each glyph in this

GlyphVector

. This can destroy information
generated during initial layout of this

GlyphVector

.

getNumGlyphs

```java
public abstract int getNumGlyphs()
```

Returns the number of glyphs in this

GlyphVector

.

**Returns:** number of glyphs in this

GlyphVector

.

---

#### getNumGlyphs

public abstract int getNumGlyphs()

Returns the number of glyphs in this

GlyphVector

.

getGlyphCode

```java
public abstract int getGlyphCode​(int glyphIndex)
```

Returns the glyphcode of the specified glyph.
This return value is meaningless to anything other
than the

Font

object that created this

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve the
glyphcode.
**Returns:** the glyphcode of the glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the
number of glyphs in this

GlyphVector

---

#### getGlyphCode

public abstract int getGlyphCode​(int glyphIndex)

Returns the glyphcode of the specified glyph.
This return value is meaningless to anything other
than the

Font

object that created this

GlyphVector

.

getGlyphCodes

```java
public abstract int[] getGlyphCodes​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)
```

Returns an array of glyphcodes for the specified glyphs.
The contents of this return value are meaningless to anything other
than the

Font

used to create this

GlyphVector

. This method is used
for convenience and performance when processing glyphcodes.
If no array is passed in, a new array is created.

**Parameters:** beginGlyphIndex

- the index into this

GlyphVector

at which to start retrieving glyphcodes
**Parameters:** numEntries

- the number of glyphcodes to retrieve
**Parameters:** codeReturn

- the array that receives the glyphcodes and is
then returned
**Returns:** an array of glyphcodes for the specified glyphs.
**Throws:** IllegalArgumentException

- if

numEntries

is
less than 0
**Throws:** IndexOutOfBoundsException

- if

beginGlyphIndex

is less than 0
**Throws:** IndexOutOfBoundsException

- if the sum of

beginGlyphIndex

and

numEntries

is
greater than the number of glyphs in this

GlyphVector

---

#### getGlyphCodes

public abstract int[] getGlyphCodes​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)

Returns an array of glyphcodes for the specified glyphs.
The contents of this return value are meaningless to anything other
than the

Font

used to create this

GlyphVector

. This method is used
for convenience and performance when processing glyphcodes.
If no array is passed in, a new array is created.

getGlyphCharIndex

```java
public int getGlyphCharIndex​(int glyphIndex)
```

Returns the character index of the specified glyph.
The character index is the index of the first logical
character represented by the glyph. The default
implementation assumes a one-to-one, left-to-right mapping
of glyphs to characters.

**Parameters:** glyphIndex

- the index of the glyph
**Returns:** the index of the first character represented by the glyph
**Since:** 1.4

---

#### getGlyphCharIndex

public int getGlyphCharIndex​(int glyphIndex)

Returns the character index of the specified glyph.
The character index is the index of the first logical
character represented by the glyph. The default
implementation assumes a one-to-one, left-to-right mapping
of glyphs to characters.

getGlyphCharIndices

```java
public int[] getGlyphCharIndices​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)
```

Returns the character indices of the specified glyphs.
The character index is the index of the first logical
character represented by the glyph. Indices are returned
in glyph order. The default implementation invokes
getGlyphCharIndex for each glyph, and subclassers will probably
want to override this implementation for performance reasons.
Use this method for convenience and performance
in processing of glyphcodes. If no array is passed in,
a new array is created.

**Parameters:** beginGlyphIndex

- the index of the first glyph
**Parameters:** numEntries

- the number of glyph indices
**Parameters:** codeReturn

- the array into which to return the character indices
**Returns:** an array of character indices, one per glyph.
**Since:** 1.4

---

#### getGlyphCharIndices

public int[] getGlyphCharIndices​(int beginGlyphIndex,
int numEntries,
int[] codeReturn)

Returns the character indices of the specified glyphs.
The character index is the index of the first logical
character represented by the glyph. Indices are returned
in glyph order. The default implementation invokes
getGlyphCharIndex for each glyph, and subclassers will probably
want to override this implementation for performance reasons.
Use this method for convenience and performance
in processing of glyphcodes. If no array is passed in,
a new array is created.

getLogicalBounds

```java
public abstract
Rectangle2D
getLogicalBounds()
```

Returns the logical bounds of this

GlyphVector

.
This method is used when positioning this

GlyphVector

in relation to visually adjacent

GlyphVector

objects.

**Returns:** a

Rectangle2D

that is the logical bounds of this

GlyphVector

.

---

#### getLogicalBounds

public abstract

Rectangle2D

getLogicalBounds()

Returns the logical bounds of this

GlyphVector

.
This method is used when positioning this

GlyphVector

in relation to visually adjacent

GlyphVector

objects.

getVisualBounds

```java
public abstract
Rectangle2D
getVisualBounds()
```

Returns the visual bounds of this

GlyphVector

The visual bounds is the bounding box of the outline of this

GlyphVector

. Because of rasterization and
alignment of pixels, it is possible that this box does not
enclose all pixels affected by rendering this

GlyphVector

.

**Returns:** a

Rectangle2D

that is the bounding box
of this

GlyphVector

.

---

#### getVisualBounds

public abstract

Rectangle2D

getVisualBounds()

Returns the visual bounds of this

GlyphVector

The visual bounds is the bounding box of the outline of this

GlyphVector

. Because of rasterization and
alignment of pixels, it is possible that this box does not
enclose all pixels affected by rendering this

GlyphVector

.

getPixelBounds

```java
public
Rectangle
getPixelBounds​(
FontRenderContext
renderFRC,
float x,
float y)
```

Returns the pixel bounds of this

GlyphVector

when
rendered in a graphics with the given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds,
offset to x, y and rounded out to the next integer value (i.e. returns an
integer rectangle which encloses the visual bounds) and
ignores the FRC. Subclassers should override this method.

**Parameters:** renderFRC

- the

FontRenderContext

of the

Graphics

.
**Parameters:** x

- the x-coordinate at which to render this

GlyphVector

.
**Parameters:** y

- the y-coordinate at which to render this

GlyphVector

.
**Returns:** a

Rectangle

bounding the pixels that would be affected.
**Since:** 1.4

---

#### getPixelBounds

public

Rectangle

getPixelBounds​(

FontRenderContext

renderFRC,
float x,
float y)

Returns the pixel bounds of this

GlyphVector

when
rendered in a graphics with the given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds,
offset to x, y and rounded out to the next integer value (i.e. returns an
integer rectangle which encloses the visual bounds) and
ignores the FRC. Subclassers should override this method.

getOutline

```java
public abstract
Shape
getOutline()
```

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

.

**Returns:** a

Shape

that is the outline of this

GlyphVector

.

---

#### getOutline

public abstract

Shape

getOutline()

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

.

getOutline

```java
public abstract
Shape
getOutline​(float x,
float y)
```

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

when
rendered at x, y.

**Parameters:** x

- the X coordinate of this

GlyphVector

.
**Parameters:** y

- the Y coordinate of this

GlyphVector

.
**Returns:** a

Shape

that is the outline of this

GlyphVector

when rendered at the specified
coordinates.

---

#### getOutline

public abstract

Shape

getOutline​(float x,
float y)

Returns a

Shape

whose interior corresponds to the
visual representation of this

GlyphVector

when
rendered at x, y.

getGlyphOutline

```java
public abstract
Shape
getGlyphOutline​(int glyphIndex)
```

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

.
The outline returned by this method is positioned around the
origin of each individual glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Returns:** a

Shape

that is the outline of the glyph
at the specified

glyphIndex

of this

GlyphVector

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

---

#### getGlyphOutline

public abstract

Shape

getGlyphOutline​(int glyphIndex)

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

.
The outline returned by this method is positioned around the
origin of each individual glyph.

getGlyphOutline

```java
public
Shape
getGlyphOutline​(int glyphIndex,
float x,
float y)
```

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

, offset to x, y.
The outline returned by this method is positioned around the
origin of each individual glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Parameters:** x

- the X coordinate of the location of this

GlyphVector
**Parameters:** y

- the Y coordinate of the location of this

GlyphVector
**Returns:** a

Shape

that is the outline of the glyph
at the specified

glyphIndex

of this

GlyphVector

when rendered at the specified
coordinates.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**Since:** 1.4

---

#### getGlyphOutline

public

Shape

getGlyphOutline​(int glyphIndex,
float x,
float y)

Returns a

Shape

whose interior corresponds to the
visual representation of the specified glyph
within this

GlyphVector

, offset to x, y.
The outline returned by this method is positioned around the
origin of each individual glyph.

getGlyphPosition

```java
public abstract
Point2D
getGlyphPosition​(int glyphIndex)
```

Returns the position of the specified glyph relative to the
origin of this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method returns the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Returns:** a

Point2D

object that is the position of the glyph
at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than the number of glyphs
in this

GlyphVector
**See Also:** setGlyphPosition(int, java.awt.geom.Point2D)

---

#### getGlyphPosition

public abstract

Point2D

getGlyphPosition​(int glyphIndex)

Returns the position of the specified glyph relative to the
origin of this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method returns the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

setGlyphPosition

```java
public abstract void setGlyphPosition​(int glyphIndex,

Point2D
newPos)
```

Sets the position of the specified glyph within this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method sets the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Parameters:** newPos

- the

Point2D

at which to position the
glyph at the specified

glyphIndex
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than the number of glyphs
in this

GlyphVector
**See Also:** getGlyphPosition(int)

---

#### setGlyphPosition

public abstract void setGlyphPosition​(int glyphIndex,

Point2D

newPos)

Sets the position of the specified glyph within this

GlyphVector

.
If

glyphIndex

equals the number of glyphs in
this

GlyphVector

, this method sets the position after
the last glyph. This position is used to define the advance of
the entire

GlyphVector

.

getGlyphTransform

```java
public abstract
AffineTransform
getGlyphTransform​(int glyphIndex)
```

Returns the transform of the specified glyph within this

GlyphVector

. The transform is relative to the
glyph position. If no special transform has been applied,

null

can be returned. A null return indicates
an identity transform.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Returns:** an

AffineTransform

that is the transform of
the glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** setGlyphTransform(int, java.awt.geom.AffineTransform)

---

#### getGlyphTransform

public abstract

AffineTransform

getGlyphTransform​(int glyphIndex)

Returns the transform of the specified glyph within this

GlyphVector

. The transform is relative to the
glyph position. If no special transform has been applied,

null

can be returned. A null return indicates
an identity transform.

setGlyphTransform

```java
public abstract void setGlyphTransform​(int glyphIndex,

AffineTransform
newTX)
```

Sets the transform of the specified glyph within this

GlyphVector

. The transform is relative to the glyph
position. A

null

argument for

newTX

indicates that no special transform is applied for the specified
glyph.
This method can be used to rotate, mirror, translate and scale the
glyph. Adding a transform can result in significant performance changes.

**Parameters:** glyphIndex

- the index into this

GlyphVector
**Parameters:** newTX

- the new transform of the glyph at

glyphIndex
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** getGlyphTransform(int)

---

#### setGlyphTransform

public abstract void setGlyphTransform​(int glyphIndex,

AffineTransform

newTX)

Sets the transform of the specified glyph within this

GlyphVector

. The transform is relative to the glyph
position. A

null

argument for

newTX

indicates that no special transform is applied for the specified
glyph.
This method can be used to rotate, mirror, translate and scale the
glyph. Adding a transform can result in significant performance changes.

getLayoutFlags

```java
public int getLayoutFlags()
```

Returns flags describing the global state of the GlyphVector.
Flags not described below are reserved. The default
implementation returns 0 (meaning false) for the position adjustments,
transforms, rtl, and complex flags.
Subclassers should override this method, and make sure
it correctly describes the GlyphVector and corresponds
to the results of related calls.

**Returns:** an int containing the flags describing the state
**Since:** 1.4
**See Also:** FLAG_HAS_POSITION_ADJUSTMENTS

,

FLAG_HAS_TRANSFORMS

,

FLAG_RUN_RTL

,

FLAG_COMPLEX_GLYPHS

,

FLAG_MASK

---

#### getLayoutFlags

public int getLayoutFlags()

Returns flags describing the global state of the GlyphVector.
Flags not described below are reserved. The default
implementation returns 0 (meaning false) for the position adjustments,
transforms, rtl, and complex flags.
Subclassers should override this method, and make sure
it correctly describes the GlyphVector and corresponds
to the results of related calls.

getGlyphPositions

```java
public abstract float[] getGlyphPositions​(int beginGlyphIndex,
int numEntries,
float[] positionReturn)
```

Returns an array of glyph positions for the specified glyphs.
This method is used for convenience and performance when
processing glyph positions.
If no array is passed in, a new array is created.
Even numbered array entries beginning with position zero are the X
coordinates of the glyph numbered

beginGlyphIndex + position/2

.
Odd numbered array entries beginning with position one are the Y
coordinates of the glyph numbered

beginGlyphIndex + (position-1)/2

.
If

beginGlyphIndex

equals the number of glyphs in
this

GlyphVector

, this method gets the position after
the last glyph and this position is used to define the advance of
the entire

GlyphVector

.

**Parameters:** beginGlyphIndex

- the index at which to begin retrieving
glyph positions
**Parameters:** numEntries

- the number of glyphs to retrieve
**Parameters:** positionReturn

- the array that receives the glyph positions
and is then returned.
**Returns:** an array of glyph positions specified by

beginGlyphIndex

and

numEntries

.
**Throws:** IllegalArgumentException

- if

numEntries

is
less than 0
**Throws:** IndexOutOfBoundsException

- if

beginGlyphIndex

is less than 0
**Throws:** IndexOutOfBoundsException

- if the sum of

beginGlyphIndex

and

numEntries

is greater than the number of glyphs in this

GlyphVector

plus one

---

#### getGlyphPositions

public abstract float[] getGlyphPositions​(int beginGlyphIndex,
int numEntries,
float[] positionReturn)

Returns an array of glyph positions for the specified glyphs.
This method is used for convenience and performance when
processing glyph positions.
If no array is passed in, a new array is created.
Even numbered array entries beginning with position zero are the X
coordinates of the glyph numbered

beginGlyphIndex + position/2

.
Odd numbered array entries beginning with position one are the Y
coordinates of the glyph numbered

beginGlyphIndex + (position-1)/2

.
If

beginGlyphIndex

equals the number of glyphs in
this

GlyphVector

, this method gets the position after
the last glyph and this position is used to define the advance of
the entire

GlyphVector

.

getGlyphLogicalBounds

```java
public abstract
Shape
getGlyphLogicalBounds​(int glyphIndex)
```

Returns the logical bounds of the specified glyph within this

GlyphVector

.
These logical bounds have a total of four edges, with two edges
parallel to the baseline under the glyph's transform and the other two
edges are shared with adjacent glyphs if they are present. This
method is useful for hit-testing of the specified glyph,
positioning of a caret at the leading or trailing edge of a glyph,
and for drawing a highlight region around the specified glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its logical
bounds
**Returns:** a

Shape

that is the logical bounds of the
glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** getGlyphVisualBounds(int)

---

#### getGlyphLogicalBounds

public abstract

Shape

getGlyphLogicalBounds​(int glyphIndex)

Returns the logical bounds of the specified glyph within this

GlyphVector

.
These logical bounds have a total of four edges, with two edges
parallel to the baseline under the glyph's transform and the other two
edges are shared with adjacent glyphs if they are present. This
method is useful for hit-testing of the specified glyph,
positioning of a caret at the leading or trailing edge of a glyph,
and for drawing a highlight region around the specified glyph.

getGlyphVisualBounds

```java
public abstract
Shape
getGlyphVisualBounds​(int glyphIndex)
```

Returns the visual bounds of the specified glyph within the

GlyphVector

.
The bounds returned by this method is positioned around the
origin of each individual glyph.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its visual
bounds
**Returns:** a

Shape

that is the visual bounds of the
glyph at the specified

glyphIndex

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector
**See Also:** getGlyphLogicalBounds(int)

---

#### getGlyphVisualBounds

public abstract

Shape

getGlyphVisualBounds​(int glyphIndex)

Returns the visual bounds of the specified glyph within the

GlyphVector

.
The bounds returned by this method is positioned around the
origin of each individual glyph.

getGlyphPixelBounds

```java
public
Rectangle
getGlyphPixelBounds​(int index,

FontRenderContext
renderFRC,
float x,
float y)
```

Returns the pixel bounds of the glyph at index when this

GlyphVector

is rendered in a

Graphics

with the
given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds of the glyph,
offset to x, y and rounded out to the next integer value, and
ignores the FRC. Subclassers should override this method.

**Parameters:** index

- the index of the glyph.
**Parameters:** renderFRC

- the

FontRenderContext

of the

Graphics

.
**Parameters:** x

- the X position at which to render this

GlyphVector

.
**Parameters:** y

- the Y position at which to render this

GlyphVector

.
**Returns:** a

Rectangle

bounding the pixels that would be affected.
**Since:** 1.4

---

#### getGlyphPixelBounds

public

Rectangle

getGlyphPixelBounds​(int index,

FontRenderContext

renderFRC,
float x,
float y)

Returns the pixel bounds of the glyph at index when this

GlyphVector

is rendered in a

Graphics

with the
given

FontRenderContext

at the given location. The
renderFRC need not be the same as the

FontRenderContext

of this

GlyphVector

, and can be null. If it is null, the

FontRenderContext

of this

GlyphVector

is used. The default implementation returns the visual bounds of the glyph,
offset to x, y and rounded out to the next integer value, and
ignores the FRC. Subclassers should override this method.

getGlyphMetrics

```java
public abstract
GlyphMetrics
getGlyphMetrics​(int glyphIndex)
```

Returns the metrics of the glyph at the specified index into
this

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its metrics
**Returns:** a

GlyphMetrics

object that represents the
metrics of the glyph at the specified

glyphIndex

into this

GlyphVector

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

---

#### getGlyphMetrics

public abstract

GlyphMetrics

getGlyphMetrics​(int glyphIndex)

Returns the metrics of the glyph at the specified index into
this

GlyphVector

.

getGlyphJustificationInfo

```java
public abstract
GlyphJustificationInfo
getGlyphJustificationInfo​(int glyphIndex)
```

Returns the justification information for the glyph at
the specified index into this

GlyphVector

.

**Parameters:** glyphIndex

- the index into this

GlyphVector

that corresponds to the glyph from which to retrieve its
justification properties
**Returns:** a

GlyphJustificationInfo

object that
represents the justification properties of the glyph at the
specified

glyphIndex

into this

GlyphVector

.
**Throws:** IndexOutOfBoundsException

- if

glyphIndex

is less than 0 or greater than or equal to the number
of glyphs in this

GlyphVector

---

#### getGlyphJustificationInfo

public abstract

GlyphJustificationInfo

getGlyphJustificationInfo​(int glyphIndex)

Returns the justification information for the glyph at
the specified index into this

GlyphVector

.

equals

```java
public abstract boolean equals​(
GlyphVector
set)
```

Tests if the specified

GlyphVector

exactly
equals this

GlyphVector

.

**Parameters:** set

- the specified

GlyphVector

to test
**Returns:** true

if the specified

GlyphVector

equals this

GlyphVector

;

false

otherwise.

---

#### equals

public abstract boolean equals​(

GlyphVector

set)

Tests if the specified

GlyphVector

exactly
equals this

GlyphVector

.

---

