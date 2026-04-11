# Class FontMetrics

**Source:** `java.desktop\java\awt\FontMetrics.html`

### Class Description

```java
public abstract class
FontMetrics

extends
Object

implements
Serializable
```

The

FontMetrics

class defines a font metrics object, which
encapsulates information about the rendering of a particular font on a
particular screen.

Note to subclassers

: Since many of these methods form closed,
mutually recursive loops, you must take care that you implement
at least one of the methods in each such loop to prevent
infinite recursion when your subclass is used.
In particular, the following is the minimal suggested set of methods
to override in order to ensure correctness and prevent infinite
recursion (though other subsets are equally feasible):

- getAscent()

getLeading()

getMaxAdvance()

charWidth(char)

charsWidth(char[], int, int)

Note that the implementations of these methods are
inefficient, so they are usually overridden with more efficient
toolkit-specific implementations.

When an application asks to place a character at the position
(

x

,

y

), the character is placed so that its
reference point (shown as the dot in the accompanying image) is
put at that position. The reference point specifies a horizontal
line called the

baseline

of the character. In normal
printing, the baselines of characters should align.

In addition, every character in a font has an

ascent

, a

descent

, and an

advance width

. The ascent is the
amount by which the character ascends above the baseline. The
descent is the amount by which the character descends below the
baseline. The advance width indicates the position at which AWT
should place the next character.

An array of characters or a string can also have an ascent, a
descent, and an advance width. The ascent of the array is the
maximum ascent of any character in the array. The descent is the
maximum descent of any character in the array. The advance width
is the sum of the advance widths of each of the characters in the
character array. The advance of a

String

is the
distance along the baseline of the

String

. This
distance is the width that should be used for centering or
right-aligning the

String

.

Note that the advance of a

String

is not necessarily
the sum of the advances of its characters measured in isolation
because the width of a character can vary depending on its context.
For example, in Arabic text, the shape of a character can change
in order to connect to other characters. Also, in some scripts,
certain character sequences can be represented by a single shape,
called a

ligature

. Measuring characters individually does
not account for these transformations.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Font
font

The actual

Font

from which the font metrics are
created.
This cannot be null.

**See Also:**
- getFont()

---

### Constructor Details

#### protected FontMetrics​(
Font
font)

Creates a new

FontMetrics

object for finding out
height and width information about the specified

Font

and specific character glyphs in that

Font

.

**Parameters:**
- font

- the

Font

**See Also:**
- Font

---

### Method Details

#### public
Font
getFont()

Gets the

Font

described by this

FontMetrics

object.

**Returns:**
- the

Font

described by this

FontMetrics

object.

---

#### public
FontRenderContext
getFontRenderContext()

Gets the

FontRenderContext

used by this

FontMetrics

object to measure text.

Note that methods in this class which take a

Graphics

parameter measure text using the

FontRenderContext

of that

Graphics

object, and not this

FontRenderContext

**Returns:**
- the

FontRenderContext

used by this

FontMetrics

object.

**Since:**
- 1.6

---

#### public int getLeading()

Determines the

standard leading

of the

Font

described by this

FontMetrics

object. The standard leading, or
interline spacing, is the logical amount of space to be reserved
between the descent of one line of text and the ascent of the next
line. The height metric is calculated to include this extra space.

**Returns:**
- the standard leading of the

Font

.

**See Also:**
- getHeight()

,

getAscent()

,

getDescent()

---

#### public int getAscent()

Determines the

font ascent

of the

Font

described by this

FontMetrics

object. The font ascent
is the distance from the font's baseline to the top of most
alphanumeric characters. Some characters in the

Font

might extend above the font ascent line.

**Returns:**
- the font ascent of the

Font

.

**See Also:**
- getMaxAscent()

---

#### public int getDescent()

Determines the

font descent

of the

Font

described by this

FontMetrics

object. The font descent is the distance
from the font's baseline to the bottom of most alphanumeric
characters with descenders. Some characters in the

Font

might extend
below the font descent line.

**Returns:**
- the font descent of the

Font

.

**See Also:**
- getMaxDescent()

---

#### public int getHeight()

Gets the standard height of a line of text in this font. This
is the distance between the baseline of adjacent lines of text.
It is the sum of the leading + ascent + descent. Due to rounding
this may not be the same as getAscent() + getDescent() + getLeading().
There is no guarantee that lines of text spaced at this distance are
disjoint; such lines may overlap if some characters overshoot
either the standard ascent or the standard descent metric.

**Returns:**
- the standard height of the font.

**See Also:**
- getLeading()

,

getAscent()

,

getDescent()

---

#### public int getMaxAscent()

Determines the maximum ascent of the

Font

described by this

FontMetrics

object. No character
extends further above the font's baseline than this height.

**Returns:**
- the maximum ascent of any character in the

Font

.

**See Also:**
- getAscent()

---

#### public int getMaxDescent()

Determines the maximum descent of the

Font

described by this

FontMetrics

object. No character
extends further below the font's baseline than this height.

**Returns:**
- the maximum descent of any character in the

Font

.

**See Also:**
- getDescent()

---

#### @Deprecated

public int getMaxDecent()

For backward compatibility only.

**Returns:**
- the maximum descent of any character in the

Font

.

**See Also:**
- getMaxDescent()

---

#### public int getMaxAdvance()

Gets the maximum advance width of any character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is
not necessarily the sum of the advances of its characters.

**Returns:**
- the maximum advance width of any character
in the

Font

, or

-1

if the
maximum advance width is not known.

---

#### public int charWidth​(int codePoint)

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

This method doesn't validate the specified character to be a
valid Unicode code point. The caller must validate the
character value using

Character.isValidCodePoint

if necessary.

**Parameters:**
- codePoint

- the character (Unicode code point) to be measured

**Returns:**
- the advance width of the specified character
in the

Font

described by this

FontMetrics

object.

**See Also:**
- charsWidth(char[], int, int)

,

stringWidth(String)

---

#### public int charWidth​(char ch)

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

Note:

This method cannot handle

supplementary
characters

. To support all Unicode characters, including
supplementary characters, use the

charWidth(int)

method.

**Parameters:**
- ch

- the character to be measured

**Returns:**
- the advance width of the specified character
in the

Font

described by this

FontMetrics

object.

**See Also:**
- charsWidth(char[], int, int)

,

stringWidth(String)

---

#### public int stringWidth​(
String
str)

Returns the total advance width for showing the specified

String

in this

Font

. The advance
is the distance from the leftmost point to the rightmost point
on the string's baseline.

Note that the advance of a

String

is
not necessarily the sum of the advances of its characters.

**Parameters:**
- str

- the

String

to be measured

**Returns:**
- the advance width of the specified

String

in the

Font

described by this

FontMetrics

.

**Throws:**
- NullPointerException

- if str is null.

**See Also:**
- bytesWidth(byte[], int, int)

,

charsWidth(char[], int, int)

,

getStringBounds(String, Graphics)

---

#### public int charsWidth​(char[] data,
int off,
int len)

Returns the total advance width for showing the specified array
of characters in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

**Parameters:**
- data

- the array of characters to be measured
- off

- the start offset of the characters in the array
- len

- the number of characters to be measured from the array

**Returns:**
- the advance width of the subarray of the specified

char

array in the font described by
this

FontMetrics

object.

**Throws:**
- NullPointerException

- if

data

is null.
- IndexOutOfBoundsException

- if the

off

and

len

arguments index characters outside
the bounds of the

data

array.

**See Also:**
- charWidth(int)

,

charWidth(char)

,

bytesWidth(byte[], int, int)

,

stringWidth(String)

---

#### public int bytesWidth​(byte[] data,
int off,
int len)

Returns the total advance width for showing the specified array
of bytes in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

**Parameters:**
- data

- the array of bytes to be measured
- off

- the start offset of the bytes in the array
- len

- the number of bytes to be measured from the array

**Returns:**
- the advance width of the subarray of the specified

byte

array in the

Font

described by
this

FontMetrics

object.

**Throws:**
- NullPointerException

- if

data

is null.
- IndexOutOfBoundsException

- if the

off

and

len

arguments index bytes outside
the bounds of the

data

array.

**See Also:**
- charsWidth(char[], int, int)

,

stringWidth(String)

---

#### public int[] getWidths()

Gets the advance widths of the first 256 characters in the

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

**Returns:**
- an array storing the advance widths of the
characters in the

Font

described by this

FontMetrics

object.

---

#### public boolean hasUniformLineMetrics()

Checks to see if the

Font

has uniform line metrics. A
composite font may consist of several different fonts to cover
various character sets. In such cases, the

FontLineMetrics

objects are not uniform.
Different fonts may have a different ascent, descent, metrics and
so on. This information is sometimes necessary for line
measuring and line breaking.

**Returns:**
- true

if the font has uniform line metrics;

false

otherwise.

**See Also:**
- Font.hasUniformLineMetrics()

---

#### public
LineMetrics
getLineMetrics​(
String
str,

Graphics
context)

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

**Parameters:**
- str

- the specified

String
- context

- the specified

Graphics

context

**Returns:**
- a

LineMetrics

object created with the
specified

String

and

Graphics

context.

**See Also:**
- Font.getLineMetrics(String, FontRenderContext)

---

#### public
LineMetrics
getLineMetrics​(
String
str,
int beginIndex,
int limit,

Graphics
context)

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

**Parameters:**
- str

- the specified

String
- beginIndex

- the initial offset of

str
- limit

- the end offset of

str
- context

- the specified

Graphics

context

**Returns:**
- a

LineMetrics

object created with the
specified

String

and

Graphics

context.

**See Also:**
- Font.getLineMetrics(String, int, int, FontRenderContext)

---

#### public
LineMetrics
getLineMetrics​(char[] chars,
int beginIndex,
int limit,

Graphics
context)

Returns the

LineMetrics

object for the specified
character array in the specified

Graphics

context.

**Parameters:**
- chars

- the specified character array
- beginIndex

- the initial offset of

chars
- limit

- the end offset of

chars
- context

- the specified

Graphics

context

**Returns:**
- a

LineMetrics

object created with the
specified character array and

Graphics

context.

**See Also:**
- Font.getLineMetrics(char[], int, int, FontRenderContext)

---

#### public
LineMetrics
getLineMetrics​(
CharacterIterator
ci,
int beginIndex,
int limit,

Graphics
context)

Returns the

LineMetrics

object for the specified

CharacterIterator

in the specified

Graphics

context.

**Parameters:**
- ci

- the specified

CharacterIterator
- beginIndex

- the initial offset in

ci
- limit

- the end index of

ci
- context

- the specified

Graphics

context

**Returns:**
- a

LineMetrics

object created with the
specified arguments.

**See Also:**
- Font.getLineMetrics(CharacterIterator, int, int, FontRenderContext)

---

#### public
Rectangle2D
getStringBounds​(
String
str,

Graphics
context)

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:**
- str

- the specified

String
- context

- the specified

Graphics

context

**Returns:**
- a

Rectangle2D

that is the bounding box of the
specified

String

in the specified

Graphics

context.

**See Also:**
- Font.getStringBounds(String, FontRenderContext)

---

#### public
Rectangle2D
getStringBounds​(
String
str,
int beginIndex,
int limit,

Graphics
context)

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:**
- str

- the specified

String
- beginIndex

- the offset of the beginning of

str
- limit

- the end offset of

str
- context

- the specified

Graphics

context

**Returns:**
- a

Rectangle2D

that is the bounding box of the
specified

String

in the specified

Graphics

context.

**See Also:**
- Font.getStringBounds(String, int, int, FontRenderContext)

---

#### public
Rectangle2D
getStringBounds​(char[] chars,
int beginIndex,
int limit,

Graphics
context)

Returns the bounds of the specified array of characters
in the specified

Graphics

context.
The bounds is used to layout the

String

created with the specified array of characters,

beginIndex

and

limit

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:**
- chars

- an array of characters
- beginIndex

- the initial offset of the array of
characters
- limit

- the end offset of the array of characters
- context

- the specified

Graphics

context

**Returns:**
- a

Rectangle2D

that is the bounding box of the
specified character array in the specified

Graphics

context.

**See Also:**
- Font.getStringBounds(char[], int, int, FontRenderContext)

---

#### public
Rectangle2D
getStringBounds​(
CharacterIterator
ci,
int beginIndex,
int limit,

Graphics
context)

Returns the bounds of the characters indexed in the specified

CharacterIterator

in the
specified

Graphics

context.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:**
- ci

- the specified

CharacterIterator
- beginIndex

- the initial offset in

ci
- limit

- the end index of

ci
- context

- the specified

Graphics

context

**Returns:**
- a

Rectangle2D

that is the bounding box of the
characters indexed in the specified

CharacterIterator

in the specified

Graphics

context.

**See Also:**
- Font.getStringBounds(CharacterIterator, int, int, FontRenderContext)

---

#### public
Rectangle2D
getMaxCharBounds​(
Graphics
context)

Returns the bounds for the character with the maximum bounds
in the specified

Graphics

context.

**Parameters:**
- context

- the specified

Graphics

context

**Returns:**
- a

Rectangle2D

that is the
bounding box for the character with the maximum bounds.

**See Also:**
- Font.getMaxCharBounds(FontRenderContext)

---

#### public
String
toString()

Returns a representation of this

FontMetrics

object's values as a

String

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a

String

representation of this

FontMetrics

object.

---

### Additional Sections

#### Class FontMetrics

java.lang.Object

- java.awt.FontMetrics

java.awt.FontMetrics

**All Implemented Interfaces:** Serializable

```java
public abstract class
FontMetrics

extends
Object

implements
Serializable
```

The

FontMetrics

class defines a font metrics object, which
encapsulates information about the rendering of a particular font on a
particular screen.

Note to subclassers

: Since many of these methods form closed,
mutually recursive loops, you must take care that you implement
at least one of the methods in each such loop to prevent
infinite recursion when your subclass is used.
In particular, the following is the minimal suggested set of methods
to override in order to ensure correctness and prevent infinite
recursion (though other subsets are equally feasible):

- getAscent()

getLeading()

getMaxAdvance()

charWidth(char)

charsWidth(char[], int, int)

Note that the implementations of these methods are
inefficient, so they are usually overridden with more efficient
toolkit-specific implementations.

When an application asks to place a character at the position
(

x

,

y

), the character is placed so that its
reference point (shown as the dot in the accompanying image) is
put at that position. The reference point specifies a horizontal
line called the

baseline

of the character. In normal
printing, the baselines of characters should align.

In addition, every character in a font has an

ascent

, a

descent

, and an

advance width

. The ascent is the
amount by which the character ascends above the baseline. The
descent is the amount by which the character descends below the
baseline. The advance width indicates the position at which AWT
should place the next character.

An array of characters or a string can also have an ascent, a
descent, and an advance width. The ascent of the array is the
maximum ascent of any character in the array. The descent is the
maximum descent of any character in the array. The advance width
is the sum of the advance widths of each of the characters in the
character array. The advance of a

String

is the
distance along the baseline of the

String

. This
distance is the width that should be used for centering or
right-aligning the

String

.

Note that the advance of a

String

is not necessarily
the sum of the advances of its characters measured in isolation
because the width of a character can vary depending on its context.
For example, in Arabic text, the shape of a character can change
in order to connect to other characters. Also, in some scripts,
certain character sequences can be represented by a single shape,
called a

ligature

. Measuring characters individually does
not account for these transformations.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

**Since:** 1.0
**See Also:** Font

,

Serialized Form

public abstract class

FontMetrics

extends

Object

implements

Serializable

The

FontMetrics

class defines a font metrics object, which
encapsulates information about the rendering of a particular font on a
particular screen.

Note to subclassers

: Since many of these methods form closed,
mutually recursive loops, you must take care that you implement
at least one of the methods in each such loop to prevent
infinite recursion when your subclass is used.
In particular, the following is the minimal suggested set of methods
to override in order to ensure correctness and prevent infinite
recursion (though other subsets are equally feasible):

- getAscent()

getLeading()

getMaxAdvance()

charWidth(char)

charsWidth(char[], int, int)

Note that the implementations of these methods are
inefficient, so they are usually overridden with more efficient
toolkit-specific implementations.

When an application asks to place a character at the position
(

x

,

y

), the character is placed so that its
reference point (shown as the dot in the accompanying image) is
put at that position. The reference point specifies a horizontal
line called the

baseline

of the character. In normal
printing, the baselines of characters should align.

In addition, every character in a font has an

ascent

, a

descent

, and an

advance width

. The ascent is the
amount by which the character ascends above the baseline. The
descent is the amount by which the character descends below the
baseline. The advance width indicates the position at which AWT
should place the next character.

An array of characters or a string can also have an ascent, a
descent, and an advance width. The ascent of the array is the
maximum ascent of any character in the array. The descent is the
maximum descent of any character in the array. The advance width
is the sum of the advance widths of each of the characters in the
character array. The advance of a

String

is the
distance along the baseline of the

String

. This
distance is the width that should be used for centering or
right-aligning the

String

.

Note that the advance of a

String

is not necessarily
the sum of the advances of its characters measured in isolation
because the width of a character can vary depending on its context.
For example, in Arabic text, the shape of a character can change
in order to connect to other characters. Also, in some scripts,
certain character sequences can be represented by a single shape,
called a

ligature

. Measuring characters individually does
not account for these transformations.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

Note to subclassers

: Since many of these methods form closed,
mutually recursive loops, you must take care that you implement
at least one of the methods in each such loop to prevent
infinite recursion when your subclass is used.
In particular, the following is the minimal suggested set of methods
to override in order to ensure correctness and prevent infinite
recursion (though other subsets are equally feasible):

- getAscent()

getLeading()

getMaxAdvance()

charWidth(char)

charsWidth(char[], int, int)

Note that the implementations of these methods are
inefficient, so they are usually overridden with more efficient
toolkit-specific implementations.

When an application asks to place a character at the position
(

x

,

y

), the character is placed so that its
reference point (shown as the dot in the accompanying image) is
put at that position. The reference point specifies a horizontal
line called the

baseline

of the character. In normal
printing, the baselines of characters should align.

In addition, every character in a font has an

ascent

, a

descent

, and an

advance width

. The ascent is the
amount by which the character ascends above the baseline. The
descent is the amount by which the character descends below the
baseline. The advance width indicates the position at which AWT
should place the next character.

An array of characters or a string can also have an ascent, a
descent, and an advance width. The ascent of the array is the
maximum ascent of any character in the array. The descent is the
maximum descent of any character in the array. The advance width
is the sum of the advance widths of each of the characters in the
character array. The advance of a

String

is the
distance along the baseline of the

String

. This
distance is the width that should be used for centering or
right-aligning the

String

.

Note that the advance of a

String

is not necessarily
the sum of the advances of its characters measured in isolation
because the width of a character can vary depending on its context.
For example, in Arabic text, the shape of a character can change
in order to connect to other characters. Also, in some scripts,
certain character sequences can be represented by a single shape,
called a

ligature

. Measuring characters individually does
not account for these transformations.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

getAscent()

getLeading()

getMaxAdvance()

charWidth(char)

charsWidth(char[], int, int)

Note that the implementations of these methods are
inefficient, so they are usually overridden with more efficient
toolkit-specific implementations.

When an application asks to place a character at the position
(

x

,

y

), the character is placed so that its
reference point (shown as the dot in the accompanying image) is
put at that position. The reference point specifies a horizontal
line called the

baseline

of the character. In normal
printing, the baselines of characters should align.

In addition, every character in a font has an

ascent

, a

descent

, and an

advance width

. The ascent is the
amount by which the character ascends above the baseline. The
descent is the amount by which the character descends below the
baseline. The advance width indicates the position at which AWT
should place the next character.

An array of characters or a string can also have an ascent, a
descent, and an advance width. The ascent of the array is the
maximum ascent of any character in the array. The descent is the
maximum descent of any character in the array. The advance width
is the sum of the advance widths of each of the characters in the
character array. The advance of a

String

is the
distance along the baseline of the

String

. This
distance is the width that should be used for centering or
right-aligning the

String

.

Note that the advance of a

String

is not necessarily
the sum of the advances of its characters measured in isolation
because the width of a character can vary depending on its context.
For example, in Arabic text, the shape of a character can change
in order to connect to other characters. Also, in some scripts,
certain character sequences can be represented by a single shape,
called a

ligature

. Measuring characters individually does
not account for these transformations.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

When an application asks to place a character at the position
(

x

,

y

), the character is placed so that its
reference point (shown as the dot in the accompanying image) is
put at that position. The reference point specifies a horizontal
line called the

baseline

of the character. In normal
printing, the baselines of characters should align.

In addition, every character in a font has an

ascent

, a

descent

, and an

advance width

. The ascent is the
amount by which the character ascends above the baseline. The
descent is the amount by which the character descends below the
baseline. The advance width indicates the position at which AWT
should place the next character.

An array of characters or a string can also have an ascent, a
descent, and an advance width. The ascent of the array is the
maximum ascent of any character in the array. The descent is the
maximum descent of any character in the array. The advance width
is the sum of the advance widths of each of the characters in the
character array. The advance of a

String

is the
distance along the baseline of the

String

. This
distance is the width that should be used for centering or
right-aligning the

String

.

Note that the advance of a

String

is not necessarily
the sum of the advances of its characters measured in isolation
because the width of a character can vary depending on its context.
For example, in Arabic text, the shape of a character can change
in order to connect to other characters. Also, in some scripts,
certain character sequences can be represented by a single shape,
called a

ligature

. Measuring characters individually does
not account for these transformations.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

In addition, every character in a font has an

ascent

, a

descent

, and an

advance width

. The ascent is the
amount by which the character ascends above the baseline. The
descent is the amount by which the character descends below the
baseline. The advance width indicates the position at which AWT
should place the next character.

An array of characters or a string can also have an ascent, a
descent, and an advance width. The ascent of the array is the
maximum ascent of any character in the array. The descent is the
maximum descent of any character in the array. The advance width
is the sum of the advance widths of each of the characters in the
character array. The advance of a

String

is the
distance along the baseline of the

String

. This
distance is the width that should be used for centering or
right-aligning the

String

.

Note that the advance of a

String

is not necessarily
the sum of the advances of its characters measured in isolation
because the width of a character can vary depending on its context.
For example, in Arabic text, the shape of a character can change
in order to connect to other characters. Also, in some scripts,
certain character sequences can be represented by a single shape,
called a

ligature

. Measuring characters individually does
not account for these transformations.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

An array of characters or a string can also have an ascent, a
descent, and an advance width. The ascent of the array is the
maximum ascent of any character in the array. The descent is the
maximum descent of any character in the array. The advance width
is the sum of the advance widths of each of the characters in the
character array. The advance of a

String

is the
distance along the baseline of the

String

. This
distance is the width that should be used for centering or
right-aligning the

String

.

Note that the advance of a

String

is not necessarily
the sum of the advances of its characters measured in isolation
because the width of a character can vary depending on its context.
For example, in Arabic text, the shape of a character can change
in order to connect to other characters. Also, in some scripts,
certain character sequences can be represented by a single shape,
called a

ligature

. Measuring characters individually does
not account for these transformations.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

Note that the advance of a

String

is not necessarily
the sum of the advances of its characters measured in isolation
because the width of a character can vary depending on its context.
For example, in Arabic text, the shape of a character can change
in order to connect to other characters. Also, in some scripts,
certain character sequences can be represented by a single shape,
called a

ligature

. Measuring characters individually does
not account for these transformations.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

Font metrics are baseline-relative, meaning that they are
generally independent of the rotation applied to the font (modulo
possible grid hinting effects). See

Font

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Font

font

The actual

Font

from which the font metrics are
created.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

FontMetrics

​(

Font

font)

Creates a new

FontMetrics

object for finding out
height and width information about the specified

Font

and specific character glyphs in that

Font

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

bytesWidth

​(byte[] data,
int off,
int len)

Returns the total advance width for showing the specified array
of bytes in this

Font

.

int

charsWidth

​(char[] data,
int off,
int len)

Returns the total advance width for showing the specified array
of characters in this

Font

.

int

charWidth

​(char ch)

Returns the advance width of the specified character in this

Font

.

int

charWidth

​(int codePoint)

Returns the advance width of the specified character in this

Font

.

int

getAscent

()

Determines the

font ascent

of the

Font

described by this

FontMetrics

object.

int

getDescent

()

Determines the

font descent

of the

Font

described by this

FontMetrics

object.

Font

getFont

()

Gets the

Font

described by this

FontMetrics

object.

FontRenderContext

getFontRenderContext

()

Gets the

FontRenderContext

used by this

FontMetrics

object to measure text.

int

getHeight

()

Gets the standard height of a line of text in this font.

int

getLeading

()

Determines the

standard leading

of the

Font

described by this

FontMetrics

object.

LineMetrics

getLineMetrics

​(char[] chars,
int beginIndex,
int limit,

Graphics

context)

Returns the

LineMetrics

object for the specified
character array in the specified

Graphics

context.

LineMetrics

getLineMetrics

​(

String

str,
int beginIndex,
int limit,

Graphics

context)

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

LineMetrics

getLineMetrics

​(

String

str,

Graphics

context)

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

LineMetrics

getLineMetrics

​(

CharacterIterator

ci,
int beginIndex,
int limit,

Graphics

context)

Returns the

LineMetrics

object for the specified

CharacterIterator

in the specified

Graphics

context.

int

getMaxAdvance

()

Gets the maximum advance width of any character in this

Font

.

int

getMaxAscent

()

Determines the maximum ascent of the

Font

described by this

FontMetrics

object.

Rectangle2D

getMaxCharBounds

​(

Graphics

context)

Returns the bounds for the character with the maximum bounds
in the specified

Graphics

context.

int

getMaxDecent

()

Deprecated.

As of JDK version 1.1.1,
replaced by

getMaxDescent()

.

int

getMaxDescent

()

Determines the maximum descent of the

Font

described by this

FontMetrics

object.

Rectangle2D

getStringBounds

​(char[] chars,
int beginIndex,
int limit,

Graphics

context)

Returns the bounds of the specified array of characters
in the specified

Graphics

context.

Rectangle2D

getStringBounds

​(

String

str,
int beginIndex,
int limit,

Graphics

context)

Returns the bounds of the specified

String

in the
specified

Graphics

context.

Rectangle2D

getStringBounds

​(

String

str,

Graphics

context)

Returns the bounds of the specified

String

in the
specified

Graphics

context.

Rectangle2D

getStringBounds

​(

CharacterIterator

ci,
int beginIndex,
int limit,

Graphics

context)

Returns the bounds of the characters indexed in the specified

CharacterIterator

in the
specified

Graphics

context.

int[]

getWidths

()

Gets the advance widths of the first 256 characters in the

Font

.

boolean

hasUniformLineMetrics

()

Checks to see if the

Font

has uniform line metrics.

int

stringWidth

​(

String

str)

Returns the total advance width for showing the specified

String

in this

Font

.

String

toString

()

Returns a representation of this

FontMetrics

object's values as a

String

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

protected

Font

font

The actual

Font

from which the font metrics are
created.

---

#### Field Summary

The actual

Font

from which the font metrics are
created.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

FontMetrics

​(

Font

font)

Creates a new

FontMetrics

object for finding out
height and width information about the specified

Font

and specific character glyphs in that

Font

.

---

#### Constructor Summary

Creates a new

FontMetrics

object for finding out
height and width information about the specified

Font

and specific character glyphs in that

Font

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

bytesWidth

​(byte[] data,
int off,
int len)

Returns the total advance width for showing the specified array
of bytes in this

Font

.

int

charsWidth

​(char[] data,
int off,
int len)

Returns the total advance width for showing the specified array
of characters in this

Font

.

int

charWidth

​(char ch)

Returns the advance width of the specified character in this

Font

.

int

charWidth

​(int codePoint)

Returns the advance width of the specified character in this

Font

.

int

getAscent

()

Determines the

font ascent

of the

Font

described by this

FontMetrics

object.

int

getDescent

()

Determines the

font descent

of the

Font

described by this

FontMetrics

object.

Font

getFont

()

Gets the

Font

described by this

FontMetrics

object.

FontRenderContext

getFontRenderContext

()

Gets the

FontRenderContext

used by this

FontMetrics

object to measure text.

int

getHeight

()

Gets the standard height of a line of text in this font.

int

getLeading

()

Determines the

standard leading

of the

Font

described by this

FontMetrics

object.

LineMetrics

getLineMetrics

​(char[] chars,
int beginIndex,
int limit,

Graphics

context)

Returns the

LineMetrics

object for the specified
character array in the specified

Graphics

context.

LineMetrics

getLineMetrics

​(

String

str,
int beginIndex,
int limit,

Graphics

context)

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

LineMetrics

getLineMetrics

​(

String

str,

Graphics

context)

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

LineMetrics

getLineMetrics

​(

CharacterIterator

ci,
int beginIndex,
int limit,

Graphics

context)

Returns the

LineMetrics

object for the specified

CharacterIterator

in the specified

Graphics

context.

int

getMaxAdvance

()

Gets the maximum advance width of any character in this

Font

.

int

getMaxAscent

()

Determines the maximum ascent of the

Font

described by this

FontMetrics

object.

Rectangle2D

getMaxCharBounds

​(

Graphics

context)

Returns the bounds for the character with the maximum bounds
in the specified

Graphics

context.

int

getMaxDecent

()

Deprecated.

As of JDK version 1.1.1,
replaced by

getMaxDescent()

.

int

getMaxDescent

()

Determines the maximum descent of the

Font

described by this

FontMetrics

object.

Rectangle2D

getStringBounds

​(char[] chars,
int beginIndex,
int limit,

Graphics

context)

Returns the bounds of the specified array of characters
in the specified

Graphics

context.

Rectangle2D

getStringBounds

​(

String

str,
int beginIndex,
int limit,

Graphics

context)

Returns the bounds of the specified

String

in the
specified

Graphics

context.

Rectangle2D

getStringBounds

​(

String

str,

Graphics

context)

Returns the bounds of the specified

String

in the
specified

Graphics

context.

Rectangle2D

getStringBounds

​(

CharacterIterator

ci,
int beginIndex,
int limit,

Graphics

context)

Returns the bounds of the characters indexed in the specified

CharacterIterator

in the
specified

Graphics

context.

int[]

getWidths

()

Gets the advance widths of the first 256 characters in the

Font

.

boolean

hasUniformLineMetrics

()

Checks to see if the

Font

has uniform line metrics.

int

stringWidth

​(

String

str)

Returns the total advance width for showing the specified

String

in this

Font

.

String

toString

()

Returns a representation of this

FontMetrics

object's values as a

String

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the total advance width for showing the specified array
of bytes in this

Font

.

Returns the total advance width for showing the specified array
of characters in this

Font

.

Returns the advance width of the specified character in this

Font

.

Determines the

font ascent

of the

Font

described by this

FontMetrics

object.

Determines the

font descent

of the

Font

described by this

FontMetrics

object.

Gets the

Font

described by this

FontMetrics

object.

Gets the

FontRenderContext

used by this

FontMetrics

object to measure text.

Gets the standard height of a line of text in this font.

Determines the

standard leading

of the

Font

described by this

FontMetrics

object.

Returns the

LineMetrics

object for the specified
character array in the specified

Graphics

context.

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

Returns the

LineMetrics

object for the specified

CharacterIterator

in the specified

Graphics

context.

Gets the maximum advance width of any character in this

Font

.

Determines the maximum ascent of the

Font

described by this

FontMetrics

object.

Returns the bounds for the character with the maximum bounds
in the specified

Graphics

context.

Deprecated.

As of JDK version 1.1.1,
replaced by

getMaxDescent()

.

Determines the maximum descent of the

Font

described by this

FontMetrics

object.

Returns the bounds of the specified array of characters
in the specified

Graphics

context.

Returns the bounds of the specified

String

in the
specified

Graphics

context.

Returns the bounds of the characters indexed in the specified

CharacterIterator

in the
specified

Graphics

context.

Gets the advance widths of the first 256 characters in the

Font

.

Checks to see if the

Font

has uniform line metrics.

Returns the total advance width for showing the specified

String

in this

Font

.

Returns a representation of this

FontMetrics

object's values as a

String

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- font

```java
protected
Font
font
```

The actual

Font

from which the font metrics are
created.
This cannot be null.

**See Also:** getFont()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FontMetrics

```java
protected FontMetrics​(
Font
font)
```

Creates a new

FontMetrics

object for finding out
height and width information about the specified

Font

and specific character glyphs in that

Font

.

**Parameters:** font

- the

Font
**See Also:** Font

============ METHOD DETAIL ==========

- Method Detail

- getFont

```java
public
Font
getFont()
```

Gets the

Font

described by this

FontMetrics

object.

**Returns:** the

Font

described by this

FontMetrics

object.

- getFontRenderContext

```java
public
FontRenderContext
getFontRenderContext()
```

Gets the

FontRenderContext

used by this

FontMetrics

object to measure text.

Note that methods in this class which take a

Graphics

parameter measure text using the

FontRenderContext

of that

Graphics

object, and not this

FontRenderContext

**Returns:** the

FontRenderContext

used by this

FontMetrics

object.
**Since:** 1.6

- getLeading

```java
public int getLeading()
```

Determines the

standard leading

of the

Font

described by this

FontMetrics

object. The standard leading, or
interline spacing, is the logical amount of space to be reserved
between the descent of one line of text and the ascent of the next
line. The height metric is calculated to include this extra space.

**Returns:** the standard leading of the

Font

.
**See Also:** getHeight()

,

getAscent()

,

getDescent()

- getAscent

```java
public int getAscent()
```

Determines the

font ascent

of the

Font

described by this

FontMetrics

object. The font ascent
is the distance from the font's baseline to the top of most
alphanumeric characters. Some characters in the

Font

might extend above the font ascent line.

**Returns:** the font ascent of the

Font

.
**See Also:** getMaxAscent()

- getDescent

```java
public int getDescent()
```

Determines the

font descent

of the

Font

described by this

FontMetrics

object. The font descent is the distance
from the font's baseline to the bottom of most alphanumeric
characters with descenders. Some characters in the

Font

might extend
below the font descent line.

**Returns:** the font descent of the

Font

.
**See Also:** getMaxDescent()

- getHeight

```java
public int getHeight()
```

Gets the standard height of a line of text in this font. This
is the distance between the baseline of adjacent lines of text.
It is the sum of the leading + ascent + descent. Due to rounding
this may not be the same as getAscent() + getDescent() + getLeading().
There is no guarantee that lines of text spaced at this distance are
disjoint; such lines may overlap if some characters overshoot
either the standard ascent or the standard descent metric.

**Returns:** the standard height of the font.
**See Also:** getLeading()

,

getAscent()

,

getDescent()

- getMaxAscent

```java
public int getMaxAscent()
```

Determines the maximum ascent of the

Font

described by this

FontMetrics

object. No character
extends further above the font's baseline than this height.

**Returns:** the maximum ascent of any character in the

Font

.
**See Also:** getAscent()

- getMaxDescent

```java
public int getMaxDescent()
```

Determines the maximum descent of the

Font

described by this

FontMetrics

object. No character
extends further below the font's baseline than this height.

**Returns:** the maximum descent of any character in the

Font

.
**See Also:** getDescent()

- getMaxDecent

```java
@Deprecated

public int getMaxDecent()
```

Deprecated.

As of JDK version 1.1.1,
replaced by

getMaxDescent()

.

For backward compatibility only.

**Returns:** the maximum descent of any character in the

Font

.
**See Also:** getMaxDescent()

- getMaxAdvance

```java
public int getMaxAdvance()
```

Gets the maximum advance width of any character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is
not necessarily the sum of the advances of its characters.

**Returns:** the maximum advance width of any character
in the

Font

, or

-1

if the
maximum advance width is not known.

- charWidth

```java
public int charWidth​(int codePoint)
```

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

This method doesn't validate the specified character to be a
valid Unicode code point. The caller must validate the
character value using

Character.isValidCodePoint

if necessary.

**Parameters:** codePoint

- the character (Unicode code point) to be measured
**Returns:** the advance width of the specified character
in the

Font

described by this

FontMetrics

object.
**See Also:** charsWidth(char[], int, int)

,

stringWidth(String)

- charWidth

```java
public int charWidth​(char ch)
```

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

Note:

This method cannot handle

supplementary
characters

. To support all Unicode characters, including
supplementary characters, use the

charWidth(int)

method.

**Parameters:** ch

- the character to be measured
**Returns:** the advance width of the specified character
in the

Font

described by this

FontMetrics

object.
**See Also:** charsWidth(char[], int, int)

,

stringWidth(String)

- stringWidth

```java
public int stringWidth​(
String
str)
```

Returns the total advance width for showing the specified

String

in this

Font

. The advance
is the distance from the leftmost point to the rightmost point
on the string's baseline.

Note that the advance of a

String

is
not necessarily the sum of the advances of its characters.

**Parameters:** str

- the

String

to be measured
**Returns:** the advance width of the specified

String

in the

Font

described by this

FontMetrics

.
**Throws:** NullPointerException

- if str is null.
**See Also:** bytesWidth(byte[], int, int)

,

charsWidth(char[], int, int)

,

getStringBounds(String, Graphics)

- charsWidth

```java
public int charsWidth​(char[] data,
int off,
int len)
```

Returns the total advance width for showing the specified array
of characters in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

**Parameters:** data

- the array of characters to be measured
**Parameters:** off

- the start offset of the characters in the array
**Parameters:** len

- the number of characters to be measured from the array
**Returns:** the advance width of the subarray of the specified

char

array in the font described by
this

FontMetrics

object.
**Throws:** NullPointerException

- if

data

is null.
**Throws:** IndexOutOfBoundsException

- if the

off

and

len

arguments index characters outside
the bounds of the

data

array.
**See Also:** charWidth(int)

,

charWidth(char)

,

bytesWidth(byte[], int, int)

,

stringWidth(String)

- bytesWidth

```java
public int bytesWidth​(byte[] data,
int off,
int len)
```

Returns the total advance width for showing the specified array
of bytes in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

**Parameters:** data

- the array of bytes to be measured
**Parameters:** off

- the start offset of the bytes in the array
**Parameters:** len

- the number of bytes to be measured from the array
**Returns:** the advance width of the subarray of the specified

byte

array in the

Font

described by
this

FontMetrics

object.
**Throws:** NullPointerException

- if

data

is null.
**Throws:** IndexOutOfBoundsException

- if the

off

and

len

arguments index bytes outside
the bounds of the

data

array.
**See Also:** charsWidth(char[], int, int)

,

stringWidth(String)

- getWidths

```java
public int[] getWidths()
```

Gets the advance widths of the first 256 characters in the

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

**Returns:** an array storing the advance widths of the
characters in the

Font

described by this

FontMetrics

object.

- hasUniformLineMetrics

```java
public boolean hasUniformLineMetrics()
```

Checks to see if the

Font

has uniform line metrics. A
composite font may consist of several different fonts to cover
various character sets. In such cases, the

FontLineMetrics

objects are not uniform.
Different fonts may have a different ascent, descent, metrics and
so on. This information is sometimes necessary for line
measuring and line breaking.

**Returns:** true

if the font has uniform line metrics;

false

otherwise.
**See Also:** Font.hasUniformLineMetrics()

- getLineMetrics

```java
public
LineMetrics
getLineMetrics​(
String
str,

Graphics
context)
```

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

**Parameters:** str

- the specified

String
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified

String

and

Graphics

context.
**See Also:** Font.getLineMetrics(String, FontRenderContext)

- getLineMetrics

```java
public
LineMetrics
getLineMetrics​(
String
str,
int beginIndex,
int limit,

Graphics
context)
```

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

**Parameters:** str

- the specified

String
**Parameters:** beginIndex

- the initial offset of

str
**Parameters:** limit

- the end offset of

str
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified

String

and

Graphics

context.
**See Also:** Font.getLineMetrics(String, int, int, FontRenderContext)

- getLineMetrics

```java
public
LineMetrics
getLineMetrics​(char[] chars,
int beginIndex,
int limit,

Graphics
context)
```

Returns the

LineMetrics

object for the specified
character array in the specified

Graphics

context.

**Parameters:** chars

- the specified character array
**Parameters:** beginIndex

- the initial offset of

chars
**Parameters:** limit

- the end offset of

chars
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified character array and

Graphics

context.
**See Also:** Font.getLineMetrics(char[], int, int, FontRenderContext)

- getLineMetrics

```java
public
LineMetrics
getLineMetrics​(
CharacterIterator
ci,
int beginIndex,
int limit,

Graphics
context)
```

Returns the

LineMetrics

object for the specified

CharacterIterator

in the specified

Graphics

context.

**Parameters:** ci

- the specified

CharacterIterator
**Parameters:** beginIndex

- the initial offset in

ci
**Parameters:** limit

- the end index of

ci
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified arguments.
**See Also:** Font.getLineMetrics(CharacterIterator, int, int, FontRenderContext)

- getStringBounds

```java
public
Rectangle2D
getStringBounds​(
String
str,

Graphics
context)
```

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** str

- the specified

String
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
specified

String

in the specified

Graphics

context.
**See Also:** Font.getStringBounds(String, FontRenderContext)

- getStringBounds

```java
public
Rectangle2D
getStringBounds​(
String
str,
int beginIndex,
int limit,

Graphics
context)
```

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** str

- the specified

String
**Parameters:** beginIndex

- the offset of the beginning of

str
**Parameters:** limit

- the end offset of

str
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
specified

String

in the specified

Graphics

context.
**See Also:** Font.getStringBounds(String, int, int, FontRenderContext)

- getStringBounds

```java
public
Rectangle2D
getStringBounds​(char[] chars,
int beginIndex,
int limit,

Graphics
context)
```

Returns the bounds of the specified array of characters
in the specified

Graphics

context.
The bounds is used to layout the

String

created with the specified array of characters,

beginIndex

and

limit

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** chars

- an array of characters
**Parameters:** beginIndex

- the initial offset of the array of
characters
**Parameters:** limit

- the end offset of the array of characters
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
specified character array in the specified

Graphics

context.
**See Also:** Font.getStringBounds(char[], int, int, FontRenderContext)

- getStringBounds

```java
public
Rectangle2D
getStringBounds​(
CharacterIterator
ci,
int beginIndex,
int limit,

Graphics
context)
```

Returns the bounds of the characters indexed in the specified

CharacterIterator

in the
specified

Graphics

context.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** ci

- the specified

CharacterIterator
**Parameters:** beginIndex

- the initial offset in

ci
**Parameters:** limit

- the end index of

ci
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
characters indexed in the specified

CharacterIterator

in the specified

Graphics

context.
**See Also:** Font.getStringBounds(CharacterIterator, int, int, FontRenderContext)

- getMaxCharBounds

```java
public
Rectangle2D
getMaxCharBounds​(
Graphics
context)
```

Returns the bounds for the character with the maximum bounds
in the specified

Graphics

context.

**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the
bounding box for the character with the maximum bounds.
**See Also:** Font.getMaxCharBounds(FontRenderContext)

- toString

```java
public
String
toString()
```

Returns a representation of this

FontMetrics

object's values as a

String

.

**Overrides:** toString

in class

Object
**Returns:** a

String

representation of this

FontMetrics

object.

Field Detail

- font

```java
protected
Font
font
```

The actual

Font

from which the font metrics are
created.
This cannot be null.

**See Also:** getFont()

---

#### Field Detail

font

```java
protected
Font
font
```

The actual

Font

from which the font metrics are
created.
This cannot be null.

**See Also:** getFont()

---

#### font

protected

Font

font

The actual

Font

from which the font metrics are
created.
This cannot be null.

Constructor Detail

- FontMetrics

```java
protected FontMetrics​(
Font
font)
```

Creates a new

FontMetrics

object for finding out
height and width information about the specified

Font

and specific character glyphs in that

Font

.

**Parameters:** font

- the

Font
**See Also:** Font

---

#### Constructor Detail

FontMetrics

```java
protected FontMetrics​(
Font
font)
```

Creates a new

FontMetrics

object for finding out
height and width information about the specified

Font

and specific character glyphs in that

Font

.

**Parameters:** font

- the

Font
**See Also:** Font

---

#### FontMetrics

protected FontMetrics​(

Font

font)

Creates a new

FontMetrics

object for finding out
height and width information about the specified

Font

and specific character glyphs in that

Font

.

Method Detail

- getFont

```java
public
Font
getFont()
```

Gets the

Font

described by this

FontMetrics

object.

**Returns:** the

Font

described by this

FontMetrics

object.

- getFontRenderContext

```java
public
FontRenderContext
getFontRenderContext()
```

Gets the

FontRenderContext

used by this

FontMetrics

object to measure text.

Note that methods in this class which take a

Graphics

parameter measure text using the

FontRenderContext

of that

Graphics

object, and not this

FontRenderContext

**Returns:** the

FontRenderContext

used by this

FontMetrics

object.
**Since:** 1.6

- getLeading

```java
public int getLeading()
```

Determines the

standard leading

of the

Font

described by this

FontMetrics

object. The standard leading, or
interline spacing, is the logical amount of space to be reserved
between the descent of one line of text and the ascent of the next
line. The height metric is calculated to include this extra space.

**Returns:** the standard leading of the

Font

.
**See Also:** getHeight()

,

getAscent()

,

getDescent()

- getAscent

```java
public int getAscent()
```

Determines the

font ascent

of the

Font

described by this

FontMetrics

object. The font ascent
is the distance from the font's baseline to the top of most
alphanumeric characters. Some characters in the

Font

might extend above the font ascent line.

**Returns:** the font ascent of the

Font

.
**See Also:** getMaxAscent()

- getDescent

```java
public int getDescent()
```

Determines the

font descent

of the

Font

described by this

FontMetrics

object. The font descent is the distance
from the font's baseline to the bottom of most alphanumeric
characters with descenders. Some characters in the

Font

might extend
below the font descent line.

**Returns:** the font descent of the

Font

.
**See Also:** getMaxDescent()

- getHeight

```java
public int getHeight()
```

Gets the standard height of a line of text in this font. This
is the distance between the baseline of adjacent lines of text.
It is the sum of the leading + ascent + descent. Due to rounding
this may not be the same as getAscent() + getDescent() + getLeading().
There is no guarantee that lines of text spaced at this distance are
disjoint; such lines may overlap if some characters overshoot
either the standard ascent or the standard descent metric.

**Returns:** the standard height of the font.
**See Also:** getLeading()

,

getAscent()

,

getDescent()

- getMaxAscent

```java
public int getMaxAscent()
```

Determines the maximum ascent of the

Font

described by this

FontMetrics

object. No character
extends further above the font's baseline than this height.

**Returns:** the maximum ascent of any character in the

Font

.
**See Also:** getAscent()

- getMaxDescent

```java
public int getMaxDescent()
```

Determines the maximum descent of the

Font

described by this

FontMetrics

object. No character
extends further below the font's baseline than this height.

**Returns:** the maximum descent of any character in the

Font

.
**See Also:** getDescent()

- getMaxDecent

```java
@Deprecated

public int getMaxDecent()
```

Deprecated.

As of JDK version 1.1.1,
replaced by

getMaxDescent()

.

For backward compatibility only.

**Returns:** the maximum descent of any character in the

Font

.
**See Also:** getMaxDescent()

- getMaxAdvance

```java
public int getMaxAdvance()
```

Gets the maximum advance width of any character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is
not necessarily the sum of the advances of its characters.

**Returns:** the maximum advance width of any character
in the

Font

, or

-1

if the
maximum advance width is not known.

- charWidth

```java
public int charWidth​(int codePoint)
```

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

This method doesn't validate the specified character to be a
valid Unicode code point. The caller must validate the
character value using

Character.isValidCodePoint

if necessary.

**Parameters:** codePoint

- the character (Unicode code point) to be measured
**Returns:** the advance width of the specified character
in the

Font

described by this

FontMetrics

object.
**See Also:** charsWidth(char[], int, int)

,

stringWidth(String)

- charWidth

```java
public int charWidth​(char ch)
```

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

Note:

This method cannot handle

supplementary
characters

. To support all Unicode characters, including
supplementary characters, use the

charWidth(int)

method.

**Parameters:** ch

- the character to be measured
**Returns:** the advance width of the specified character
in the

Font

described by this

FontMetrics

object.
**See Also:** charsWidth(char[], int, int)

,

stringWidth(String)

- stringWidth

```java
public int stringWidth​(
String
str)
```

Returns the total advance width for showing the specified

String

in this

Font

. The advance
is the distance from the leftmost point to the rightmost point
on the string's baseline.

Note that the advance of a

String

is
not necessarily the sum of the advances of its characters.

**Parameters:** str

- the

String

to be measured
**Returns:** the advance width of the specified

String

in the

Font

described by this

FontMetrics

.
**Throws:** NullPointerException

- if str is null.
**See Also:** bytesWidth(byte[], int, int)

,

charsWidth(char[], int, int)

,

getStringBounds(String, Graphics)

- charsWidth

```java
public int charsWidth​(char[] data,
int off,
int len)
```

Returns the total advance width for showing the specified array
of characters in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

**Parameters:** data

- the array of characters to be measured
**Parameters:** off

- the start offset of the characters in the array
**Parameters:** len

- the number of characters to be measured from the array
**Returns:** the advance width of the subarray of the specified

char

array in the font described by
this

FontMetrics

object.
**Throws:** NullPointerException

- if

data

is null.
**Throws:** IndexOutOfBoundsException

- if the

off

and

len

arguments index characters outside
the bounds of the

data

array.
**See Also:** charWidth(int)

,

charWidth(char)

,

bytesWidth(byte[], int, int)

,

stringWidth(String)

- bytesWidth

```java
public int bytesWidth​(byte[] data,
int off,
int len)
```

Returns the total advance width for showing the specified array
of bytes in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

**Parameters:** data

- the array of bytes to be measured
**Parameters:** off

- the start offset of the bytes in the array
**Parameters:** len

- the number of bytes to be measured from the array
**Returns:** the advance width of the subarray of the specified

byte

array in the

Font

described by
this

FontMetrics

object.
**Throws:** NullPointerException

- if

data

is null.
**Throws:** IndexOutOfBoundsException

- if the

off

and

len

arguments index bytes outside
the bounds of the

data

array.
**See Also:** charsWidth(char[], int, int)

,

stringWidth(String)

- getWidths

```java
public int[] getWidths()
```

Gets the advance widths of the first 256 characters in the

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

**Returns:** an array storing the advance widths of the
characters in the

Font

described by this

FontMetrics

object.

- hasUniformLineMetrics

```java
public boolean hasUniformLineMetrics()
```

Checks to see if the

Font

has uniform line metrics. A
composite font may consist of several different fonts to cover
various character sets. In such cases, the

FontLineMetrics

objects are not uniform.
Different fonts may have a different ascent, descent, metrics and
so on. This information is sometimes necessary for line
measuring and line breaking.

**Returns:** true

if the font has uniform line metrics;

false

otherwise.
**See Also:** Font.hasUniformLineMetrics()

- getLineMetrics

```java
public
LineMetrics
getLineMetrics​(
String
str,

Graphics
context)
```

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

**Parameters:** str

- the specified

String
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified

String

and

Graphics

context.
**See Also:** Font.getLineMetrics(String, FontRenderContext)

- getLineMetrics

```java
public
LineMetrics
getLineMetrics​(
String
str,
int beginIndex,
int limit,

Graphics
context)
```

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

**Parameters:** str

- the specified

String
**Parameters:** beginIndex

- the initial offset of

str
**Parameters:** limit

- the end offset of

str
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified

String

and

Graphics

context.
**See Also:** Font.getLineMetrics(String, int, int, FontRenderContext)

- getLineMetrics

```java
public
LineMetrics
getLineMetrics​(char[] chars,
int beginIndex,
int limit,

Graphics
context)
```

Returns the

LineMetrics

object for the specified
character array in the specified

Graphics

context.

**Parameters:** chars

- the specified character array
**Parameters:** beginIndex

- the initial offset of

chars
**Parameters:** limit

- the end offset of

chars
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified character array and

Graphics

context.
**See Also:** Font.getLineMetrics(char[], int, int, FontRenderContext)

- getLineMetrics

```java
public
LineMetrics
getLineMetrics​(
CharacterIterator
ci,
int beginIndex,
int limit,

Graphics
context)
```

Returns the

LineMetrics

object for the specified

CharacterIterator

in the specified

Graphics

context.

**Parameters:** ci

- the specified

CharacterIterator
**Parameters:** beginIndex

- the initial offset in

ci
**Parameters:** limit

- the end index of

ci
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified arguments.
**See Also:** Font.getLineMetrics(CharacterIterator, int, int, FontRenderContext)

- getStringBounds

```java
public
Rectangle2D
getStringBounds​(
String
str,

Graphics
context)
```

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** str

- the specified

String
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
specified

String

in the specified

Graphics

context.
**See Also:** Font.getStringBounds(String, FontRenderContext)

- getStringBounds

```java
public
Rectangle2D
getStringBounds​(
String
str,
int beginIndex,
int limit,

Graphics
context)
```

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** str

- the specified

String
**Parameters:** beginIndex

- the offset of the beginning of

str
**Parameters:** limit

- the end offset of

str
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
specified

String

in the specified

Graphics

context.
**See Also:** Font.getStringBounds(String, int, int, FontRenderContext)

- getStringBounds

```java
public
Rectangle2D
getStringBounds​(char[] chars,
int beginIndex,
int limit,

Graphics
context)
```

Returns the bounds of the specified array of characters
in the specified

Graphics

context.
The bounds is used to layout the

String

created with the specified array of characters,

beginIndex

and

limit

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** chars

- an array of characters
**Parameters:** beginIndex

- the initial offset of the array of
characters
**Parameters:** limit

- the end offset of the array of characters
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
specified character array in the specified

Graphics

context.
**See Also:** Font.getStringBounds(char[], int, int, FontRenderContext)

- getStringBounds

```java
public
Rectangle2D
getStringBounds​(
CharacterIterator
ci,
int beginIndex,
int limit,

Graphics
context)
```

Returns the bounds of the characters indexed in the specified

CharacterIterator

in the
specified

Graphics

context.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** ci

- the specified

CharacterIterator
**Parameters:** beginIndex

- the initial offset in

ci
**Parameters:** limit

- the end index of

ci
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
characters indexed in the specified

CharacterIterator

in the specified

Graphics

context.
**See Also:** Font.getStringBounds(CharacterIterator, int, int, FontRenderContext)

- getMaxCharBounds

```java
public
Rectangle2D
getMaxCharBounds​(
Graphics
context)
```

Returns the bounds for the character with the maximum bounds
in the specified

Graphics

context.

**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the
bounding box for the character with the maximum bounds.
**See Also:** Font.getMaxCharBounds(FontRenderContext)

- toString

```java
public
String
toString()
```

Returns a representation of this

FontMetrics

object's values as a

String

.

**Overrides:** toString

in class

Object
**Returns:** a

String

representation of this

FontMetrics

object.

---

#### Method Detail

getFont

```java
public
Font
getFont()
```

Gets the

Font

described by this

FontMetrics

object.

**Returns:** the

Font

described by this

FontMetrics

object.

---

#### getFont

public

Font

getFont()

Gets the

Font

described by this

FontMetrics

object.

getFontRenderContext

```java
public
FontRenderContext
getFontRenderContext()
```

Gets the

FontRenderContext

used by this

FontMetrics

object to measure text.

Note that methods in this class which take a

Graphics

parameter measure text using the

FontRenderContext

of that

Graphics

object, and not this

FontRenderContext

**Returns:** the

FontRenderContext

used by this

FontMetrics

object.
**Since:** 1.6

---

#### getFontRenderContext

public

FontRenderContext

getFontRenderContext()

Gets the

FontRenderContext

used by this

FontMetrics

object to measure text.

Note that methods in this class which take a

Graphics

parameter measure text using the

FontRenderContext

of that

Graphics

object, and not this

FontRenderContext

Note that methods in this class which take a

Graphics

parameter measure text using the

FontRenderContext

of that

Graphics

object, and not this

FontRenderContext

getLeading

```java
public int getLeading()
```

Determines the

standard leading

of the

Font

described by this

FontMetrics

object. The standard leading, or
interline spacing, is the logical amount of space to be reserved
between the descent of one line of text and the ascent of the next
line. The height metric is calculated to include this extra space.

**Returns:** the standard leading of the

Font

.
**See Also:** getHeight()

,

getAscent()

,

getDescent()

---

#### getLeading

public int getLeading()

Determines the

standard leading

of the

Font

described by this

FontMetrics

object. The standard leading, or
interline spacing, is the logical amount of space to be reserved
between the descent of one line of text and the ascent of the next
line. The height metric is calculated to include this extra space.

getAscent

```java
public int getAscent()
```

Determines the

font ascent

of the

Font

described by this

FontMetrics

object. The font ascent
is the distance from the font's baseline to the top of most
alphanumeric characters. Some characters in the

Font

might extend above the font ascent line.

**Returns:** the font ascent of the

Font

.
**See Also:** getMaxAscent()

---

#### getAscent

public int getAscent()

Determines the

font ascent

of the

Font

described by this

FontMetrics

object. The font ascent
is the distance from the font's baseline to the top of most
alphanumeric characters. Some characters in the

Font

might extend above the font ascent line.

getDescent

```java
public int getDescent()
```

Determines the

font descent

of the

Font

described by this

FontMetrics

object. The font descent is the distance
from the font's baseline to the bottom of most alphanumeric
characters with descenders. Some characters in the

Font

might extend
below the font descent line.

**Returns:** the font descent of the

Font

.
**See Also:** getMaxDescent()

---

#### getDescent

public int getDescent()

Determines the

font descent

of the

Font

described by this

FontMetrics

object. The font descent is the distance
from the font's baseline to the bottom of most alphanumeric
characters with descenders. Some characters in the

Font

might extend
below the font descent line.

getHeight

```java
public int getHeight()
```

Gets the standard height of a line of text in this font. This
is the distance between the baseline of adjacent lines of text.
It is the sum of the leading + ascent + descent. Due to rounding
this may not be the same as getAscent() + getDescent() + getLeading().
There is no guarantee that lines of text spaced at this distance are
disjoint; such lines may overlap if some characters overshoot
either the standard ascent or the standard descent metric.

**Returns:** the standard height of the font.
**See Also:** getLeading()

,

getAscent()

,

getDescent()

---

#### getHeight

public int getHeight()

Gets the standard height of a line of text in this font. This
is the distance between the baseline of adjacent lines of text.
It is the sum of the leading + ascent + descent. Due to rounding
this may not be the same as getAscent() + getDescent() + getLeading().
There is no guarantee that lines of text spaced at this distance are
disjoint; such lines may overlap if some characters overshoot
either the standard ascent or the standard descent metric.

getMaxAscent

```java
public int getMaxAscent()
```

Determines the maximum ascent of the

Font

described by this

FontMetrics

object. No character
extends further above the font's baseline than this height.

**Returns:** the maximum ascent of any character in the

Font

.
**See Also:** getAscent()

---

#### getMaxAscent

public int getMaxAscent()

Determines the maximum ascent of the

Font

described by this

FontMetrics

object. No character
extends further above the font's baseline than this height.

getMaxDescent

```java
public int getMaxDescent()
```

Determines the maximum descent of the

Font

described by this

FontMetrics

object. No character
extends further below the font's baseline than this height.

**Returns:** the maximum descent of any character in the

Font

.
**See Also:** getDescent()

---

#### getMaxDescent

public int getMaxDescent()

Determines the maximum descent of the

Font

described by this

FontMetrics

object. No character
extends further below the font's baseline than this height.

getMaxDecent

```java
@Deprecated

public int getMaxDecent()
```

Deprecated.

As of JDK version 1.1.1,
replaced by

getMaxDescent()

.

For backward compatibility only.

**Returns:** the maximum descent of any character in the

Font

.
**See Also:** getMaxDescent()

---

#### getMaxDecent

@Deprecated

public int getMaxDecent()

For backward compatibility only.

getMaxAdvance

```java
public int getMaxAdvance()
```

Gets the maximum advance width of any character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is
not necessarily the sum of the advances of its characters.

**Returns:** the maximum advance width of any character
in the

Font

, or

-1

if the
maximum advance width is not known.

---

#### getMaxAdvance

public int getMaxAdvance()

Gets the maximum advance width of any character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is
not necessarily the sum of the advances of its characters.

charWidth

```java
public int charWidth​(int codePoint)
```

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

This method doesn't validate the specified character to be a
valid Unicode code point. The caller must validate the
character value using

Character.isValidCodePoint

if necessary.

**Parameters:** codePoint

- the character (Unicode code point) to be measured
**Returns:** the advance width of the specified character
in the

Font

described by this

FontMetrics

object.
**See Also:** charsWidth(char[], int, int)

,

stringWidth(String)

---

#### charWidth

public int charWidth​(int codePoint)

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

This method doesn't validate the specified character to be a
valid Unicode code point. The caller must validate the
character value using

Character.isValidCodePoint

if necessary.

This method doesn't validate the specified character to be a
valid Unicode code point. The caller must validate the
character value using

Character.isValidCodePoint

if necessary.

charWidth

```java
public int charWidth​(char ch)
```

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

Note:

This method cannot handle

supplementary
characters

. To support all Unicode characters, including
supplementary characters, use the

charWidth(int)

method.

**Parameters:** ch

- the character to be measured
**Returns:** the advance width of the specified character
in the

Font

described by this

FontMetrics

object.
**See Also:** charsWidth(char[], int, int)

,

stringWidth(String)

---

#### charWidth

public int charWidth​(char ch)

Returns the advance width of the specified character in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

Note:

This method cannot handle

supplementary
characters

. To support all Unicode characters, including
supplementary characters, use the

charWidth(int)

method.

Note:

This method cannot handle

supplementary
characters

. To support all Unicode characters, including
supplementary characters, use the

charWidth(int)

method.

stringWidth

```java
public int stringWidth​(
String
str)
```

Returns the total advance width for showing the specified

String

in this

Font

. The advance
is the distance from the leftmost point to the rightmost point
on the string's baseline.

Note that the advance of a

String

is
not necessarily the sum of the advances of its characters.

**Parameters:** str

- the

String

to be measured
**Returns:** the advance width of the specified

String

in the

Font

described by this

FontMetrics

.
**Throws:** NullPointerException

- if str is null.
**See Also:** bytesWidth(byte[], int, int)

,

charsWidth(char[], int, int)

,

getStringBounds(String, Graphics)

---

#### stringWidth

public int stringWidth​(

String

str)

Returns the total advance width for showing the specified

String

in this

Font

. The advance
is the distance from the leftmost point to the rightmost point
on the string's baseline.

Note that the advance of a

String

is
not necessarily the sum of the advances of its characters.

Note that the advance of a

String

is
not necessarily the sum of the advances of its characters.

charsWidth

```java
public int charsWidth​(char[] data,
int off,
int len)
```

Returns the total advance width for showing the specified array
of characters in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

**Parameters:** data

- the array of characters to be measured
**Parameters:** off

- the start offset of the characters in the array
**Parameters:** len

- the number of characters to be measured from the array
**Returns:** the advance width of the subarray of the specified

char

array in the font described by
this

FontMetrics

object.
**Throws:** NullPointerException

- if

data

is null.
**Throws:** IndexOutOfBoundsException

- if the

off

and

len

arguments index characters outside
the bounds of the

data

array.
**See Also:** charWidth(int)

,

charWidth(char)

,

bytesWidth(byte[], int, int)

,

stringWidth(String)

---

#### charsWidth

public int charsWidth​(char[] data,
int off,
int len)

Returns the total advance width for showing the specified array
of characters in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

bytesWidth

```java
public int bytesWidth​(byte[] data,
int off,
int len)
```

Returns the total advance width for showing the specified array
of bytes in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

**Parameters:** data

- the array of bytes to be measured
**Parameters:** off

- the start offset of the bytes in the array
**Parameters:** len

- the number of bytes to be measured from the array
**Returns:** the advance width of the subarray of the specified

byte

array in the

Font

described by
this

FontMetrics

object.
**Throws:** NullPointerException

- if

data

is null.
**Throws:** IndexOutOfBoundsException

- if the

off

and

len

arguments index bytes outside
the bounds of the

data

array.
**See Also:** charsWidth(char[], int, int)

,

stringWidth(String)

---

#### bytesWidth

public int bytesWidth​(byte[] data,
int off,
int len)

Returns the total advance width for showing the specified array
of bytes in this

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
string's baseline. The advance of a

String

is not necessarily the sum of the advances of its characters.
This is equivalent to measuring a

String

of the
characters in the specified range.

getWidths

```java
public int[] getWidths()
```

Gets the advance widths of the first 256 characters in the

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

**Returns:** an array storing the advance widths of the
characters in the

Font

described by this

FontMetrics

object.

---

#### getWidths

public int[] getWidths()

Gets the advance widths of the first 256 characters in the

Font

. The advance is the
distance from the leftmost point to the rightmost point on the
character's baseline. Note that the advance of a

String

is not necessarily the sum of the advances
of its characters.

hasUniformLineMetrics

```java
public boolean hasUniformLineMetrics()
```

Checks to see if the

Font

has uniform line metrics. A
composite font may consist of several different fonts to cover
various character sets. In such cases, the

FontLineMetrics

objects are not uniform.
Different fonts may have a different ascent, descent, metrics and
so on. This information is sometimes necessary for line
measuring and line breaking.

**Returns:** true

if the font has uniform line metrics;

false

otherwise.
**See Also:** Font.hasUniformLineMetrics()

---

#### hasUniformLineMetrics

public boolean hasUniformLineMetrics()

Checks to see if the

Font

has uniform line metrics. A
composite font may consist of several different fonts to cover
various character sets. In such cases, the

FontLineMetrics

objects are not uniform.
Different fonts may have a different ascent, descent, metrics and
so on. This information is sometimes necessary for line
measuring and line breaking.

getLineMetrics

```java
public
LineMetrics
getLineMetrics​(
String
str,

Graphics
context)
```

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

**Parameters:** str

- the specified

String
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified

String

and

Graphics

context.
**See Also:** Font.getLineMetrics(String, FontRenderContext)

---

#### getLineMetrics

public

LineMetrics

getLineMetrics​(

String

str,

Graphics

context)

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

getLineMetrics

```java
public
LineMetrics
getLineMetrics​(
String
str,
int beginIndex,
int limit,

Graphics
context)
```

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

**Parameters:** str

- the specified

String
**Parameters:** beginIndex

- the initial offset of

str
**Parameters:** limit

- the end offset of

str
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified

String

and

Graphics

context.
**See Also:** Font.getLineMetrics(String, int, int, FontRenderContext)

---

#### getLineMetrics

public

LineMetrics

getLineMetrics​(

String

str,
int beginIndex,
int limit,

Graphics

context)

Returns the

LineMetrics

object for the specified

String

in the specified

Graphics

context.

getLineMetrics

```java
public
LineMetrics
getLineMetrics​(char[] chars,
int beginIndex,
int limit,

Graphics
context)
```

Returns the

LineMetrics

object for the specified
character array in the specified

Graphics

context.

**Parameters:** chars

- the specified character array
**Parameters:** beginIndex

- the initial offset of

chars
**Parameters:** limit

- the end offset of

chars
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified character array and

Graphics

context.
**See Also:** Font.getLineMetrics(char[], int, int, FontRenderContext)

---

#### getLineMetrics

public

LineMetrics

getLineMetrics​(char[] chars,
int beginIndex,
int limit,

Graphics

context)

Returns the

LineMetrics

object for the specified
character array in the specified

Graphics

context.

getLineMetrics

```java
public
LineMetrics
getLineMetrics​(
CharacterIterator
ci,
int beginIndex,
int limit,

Graphics
context)
```

Returns the

LineMetrics

object for the specified

CharacterIterator

in the specified

Graphics

context.

**Parameters:** ci

- the specified

CharacterIterator
**Parameters:** beginIndex

- the initial offset in

ci
**Parameters:** limit

- the end index of

ci
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

LineMetrics

object created with the
specified arguments.
**See Also:** Font.getLineMetrics(CharacterIterator, int, int, FontRenderContext)

---

#### getLineMetrics

public

LineMetrics

getLineMetrics​(

CharacterIterator

ci,
int beginIndex,
int limit,

Graphics

context)

Returns the

LineMetrics

object for the specified

CharacterIterator

in the specified

Graphics

context.

getStringBounds

```java
public
Rectangle2D
getStringBounds​(
String
str,

Graphics
context)
```

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** str

- the specified

String
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
specified

String

in the specified

Graphics

context.
**See Also:** Font.getStringBounds(String, FontRenderContext)

---

#### getStringBounds

public

Rectangle2D

getStringBounds​(

String

str,

Graphics

context)

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

getStringBounds

```java
public
Rectangle2D
getStringBounds​(
String
str,
int beginIndex,
int limit,

Graphics
context)
```

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** str

- the specified

String
**Parameters:** beginIndex

- the offset of the beginning of

str
**Parameters:** limit

- the end offset of

str
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
specified

String

in the specified

Graphics

context.
**See Also:** Font.getStringBounds(String, int, int, FontRenderContext)

---

#### getStringBounds

public

Rectangle2D

getStringBounds​(

String

str,
int beginIndex,
int limit,

Graphics

context)

Returns the bounds of the specified

String

in the
specified

Graphics

context. The bounds is used
to layout the

String

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

getStringBounds

```java
public
Rectangle2D
getStringBounds​(char[] chars,
int beginIndex,
int limit,

Graphics
context)
```

Returns the bounds of the specified array of characters
in the specified

Graphics

context.
The bounds is used to layout the

String

created with the specified array of characters,

beginIndex

and

limit

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** chars

- an array of characters
**Parameters:** beginIndex

- the initial offset of the array of
characters
**Parameters:** limit

- the end offset of the array of characters
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
specified character array in the specified

Graphics

context.
**See Also:** Font.getStringBounds(char[], int, int, FontRenderContext)

---

#### getStringBounds

public

Rectangle2D

getStringBounds​(char[] chars,
int beginIndex,
int limit,

Graphics

context)

Returns the bounds of the specified array of characters
in the specified

Graphics

context.
The bounds is used to layout the

String

created with the specified array of characters,

beginIndex

and

limit

.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

getStringBounds

```java
public
Rectangle2D
getStringBounds​(
CharacterIterator
ci,
int beginIndex,
int limit,

Graphics
context)
```

Returns the bounds of the characters indexed in the specified

CharacterIterator

in the
specified

Graphics

context.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

**Parameters:** ci

- the specified

CharacterIterator
**Parameters:** beginIndex

- the initial offset in

ci
**Parameters:** limit

- the end index of

ci
**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the bounding box of the
characters indexed in the specified

CharacterIterator

in the specified

Graphics

context.
**See Also:** Font.getStringBounds(CharacterIterator, int, int, FontRenderContext)

---

#### getStringBounds

public

Rectangle2D

getStringBounds​(

CharacterIterator

ci,
int beginIndex,
int limit,

Graphics

context)

Returns the bounds of the characters indexed in the specified

CharacterIterator

in the
specified

Graphics

context.

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

Note: The returned bounds is in baseline-relative coordinates
(see

class notes

).

getMaxCharBounds

```java
public
Rectangle2D
getMaxCharBounds​(
Graphics
context)
```

Returns the bounds for the character with the maximum bounds
in the specified

Graphics

context.

**Parameters:** context

- the specified

Graphics

context
**Returns:** a

Rectangle2D

that is the
bounding box for the character with the maximum bounds.
**See Also:** Font.getMaxCharBounds(FontRenderContext)

---

#### getMaxCharBounds

public

Rectangle2D

getMaxCharBounds​(

Graphics

context)

Returns the bounds for the character with the maximum bounds
in the specified

Graphics

context.

toString

```java
public
String
toString()
```

Returns a representation of this

FontMetrics

object's values as a

String

.

**Overrides:** toString

in class

Object
**Returns:** a

String

representation of this

FontMetrics

object.

---

#### toString

public

String

toString()

Returns a representation of this

FontMetrics

object's values as a

String

.

---

