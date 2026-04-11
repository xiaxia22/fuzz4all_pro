# Class NumericShaper

**Source:** `java.desktop\java\awt\font\NumericShaper.html`

### Class Description

```java
public final class
NumericShaper

extends
Object

implements
Serializable
```

The

NumericShaper

class is used to convert Latin-1 (European)
digits to other Unicode decimal digits. Users of this class will
primarily be people who wish to present data using
national digit shapes, but find it more convenient to represent the
data internally using Latin-1 (European) digits. This does not
interpret the deprecated numeric shape selector character (U+206E).

Instances of

NumericShaper

are typically applied
as attributes to text with the

NUMERIC_SHAPING

attribute
of the

TextAttribute

class.
For example, this code snippet causes a

TextLayout

to
shape European digits to Arabic in an Arabic context:

```java
Map map = new HashMap();
map.put(TextAttribute.NUMERIC_SHAPING,
NumericShaper.getContextualShaper(NumericShaper.ARABIC));
FontRenderContext frc = ...;
TextLayout layout = new TextLayout(text, map, frc);
layout.draw(g2d, x, y);
```

It is also possible to perform numeric shaping explicitly using instances
of

NumericShaper

, as this code snippet demonstrates:

```java
char[] text = ...;
// shape all EUROPEAN digits (except zero) to ARABIC digits
NumericShaper shaper = NumericShaper.getShaper(NumericShaper.ARABIC);
shaper.shape(text, start, count);

// shape European digits to ARABIC digits if preceding text is Arabic, or
// shape European digits to TAMIL digits if preceding text is Tamil, or
// leave European digits alone if there is no preceding text, or
// preceding text is neither Arabic nor Tamil
NumericShaper shaper =
NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);
shaper.shape(text, start, count);
```

Bit mask- and enum-based Unicode ranges

This class supports two different programming interfaces to
represent Unicode ranges for script-specific digits: bit
mask-based ones, such as

NumericShaper.ARABIC

, and
enum-based ones, such as

NumericShaper.Range.ARABIC

.
Multiple ranges can be specified by ORing bit mask-based constants,
such as:

```java
NumericShaper.ARABIC | NumericShaper.TAMIL
```

or creating a

Set

with the

NumericShaper.Range

constants, such as:

```java
EnumSet.of(NumericShaper.Range.ARABIC, NumericShaper.Range.TAMIL)
```

The enum-based ranges are a super set of the bit mask-based ones.

If the two interfaces are mixed (including serialization),
Unicode range values are mapped to their counterparts where such
mapping is possible, such as

NumericShaper.Range.ARABIC

from/to

NumericShaper.ARABIC

. If any unmappable range
values are specified, such as

NumericShaper.Range.BALINESE

,
those ranges are ignored.

Decimal Digits Precedence

A Unicode range may have more than one set of decimal digits. If
multiple decimal digits sets are specified for the same Unicode
range, one of the sets will take precedence as follows.

NumericShaper constants precedence

Unicode Range

NumericShaper

Constants

Precedence

Arabic

NumericShaper.ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.Range.ARABIC

NumericShaper.Range.EASTERN_ARABIC

NumericShaper.Range.EASTERN_ARABIC

Tai Tham

NumericShaper.Range.TAI_THAM_HORA

NumericShaper.Range.TAI_THAM_THAM

NumericShaper.Range.TAI_THAM_THAM

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int EUROPEAN

Identifies the Latin-1 (European) and extended range, and
Latin-1 (European) decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int ARABIC

Identifies the ARABIC range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int EASTERN_ARABIC

Identifies the ARABIC range and ARABIC_EXTENDED decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int DEVANAGARI

Identifies the DEVANAGARI range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int BENGALI

Identifies the BENGALI range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int GURMUKHI

Identifies the GURMUKHI range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int GUJARATI

Identifies the GUJARATI range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int ORIYA

Identifies the ORIYA range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int TAMIL

Identifies the TAMIL range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int TELUGU

Identifies the TELUGU range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int KANNADA

Identifies the KANNADA range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int MALAYALAM

Identifies the MALAYALAM range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int THAI

Identifies the THAI range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int LAO

Identifies the LAO range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int TIBETAN

Identifies the TIBETAN range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int MYANMAR

Identifies the MYANMAR range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int ETHIOPIC

Identifies the ETHIOPIC range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int KHMER

Identifies the KHMER range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int MONGOLIAN

Identifies the MONGOLIAN range and decimal base.

**See Also:**
- Constant Field Values

---

#### public static final int ALL_RANGES

Identifies all ranges, for full contextual shaping.

This constant specifies all of the bit mask-based
ranges. Use

EnumSet.allOf(NumericShaper.Range.class)

to
specify all of the enum-based ranges.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
NumericShaper
getShaper​(int singleRange)

Returns a shaper for the provided unicode range. All
Latin-1 (EUROPEAN) digits are converted
to the corresponding decimal unicode digits.

**Parameters:**
- singleRange

- the specified Unicode range

**Returns:**
- a non-contextual numeric shaper

**Throws:**
- IllegalArgumentException

- if the range is not a single range

---

#### public static
NumericShaper
getShaper​(
NumericShaper.Range
singleRange)

Returns a shaper for the provided Unicode
range. All Latin-1 (EUROPEAN) digits are converted to the
corresponding decimal digits of the specified Unicode range.

**Parameters:**
- singleRange

- the Unicode range given by a

NumericShaper.Range

constant.

**Returns:**
- a non-contextual

NumericShaper

.

**Throws:**
- NullPointerException

- if

singleRange

is

null

**Since:**
- 1.7

---

#### public static
NumericShaper
getContextualShaper​(int ranges)

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits are converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, such as,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper assumes EUROPEAN as the starting context, that is, if
EUROPEAN digits are encountered before any strong directional
text in the string, the context is presumed to be EUROPEAN, and
so the digits will not shape.

**Parameters:**
- ranges

- the specified Unicode ranges

**Returns:**
- a shaper for the specified ranges

---

#### public static
NumericShaper
getContextualShaper​(
Set
<
NumericShaper.Range
> ranges)

Returns a contextual shaper for the provided Unicode
range(s). The Latin-1 (EUROPEAN) digits are converted to the
decimal digits corresponding to the range of the preceding
text, if the range is one of the provided ranges.

The shaper assumes EUROPEAN as the starting context, that
is, if EUROPEAN digits are encountered before any strong
directional text in the string, the context is presumed to be
EUROPEAN, and so the digits will not shape.

**Parameters:**
- ranges

- the specified Unicode ranges

**Returns:**
- a contextual shaper for the specified ranges

**Throws:**
- NullPointerException

- if

ranges

is

null

.

**Since:**
- 1.7

---

#### public static
NumericShaper
getContextualShaper​(int ranges,
int defaultContext)

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits will be converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, for example,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper uses defaultContext as the starting context.

**Parameters:**
- ranges

- the specified Unicode ranges
- defaultContext

- the starting context, such as

NumericShaper.EUROPEAN

**Returns:**
- a shaper for the specified Unicode ranges.

**Throws:**
- IllegalArgumentException

- if the specified

defaultContext

is not a single valid range.

---

#### public static
NumericShaper
getContextualShaper​(
Set
<
NumericShaper.Range
> ranges,

NumericShaper.Range
defaultContext)

Returns a contextual shaper for the provided Unicode range(s).
The Latin-1 (EUROPEAN) digits will be converted to the decimal
digits corresponding to the range of the preceding text, if the
range is one of the provided ranges. The shaper uses

defaultContext

as the starting context.

**Parameters:**
- ranges

- the specified Unicode ranges
- defaultContext

- the starting context, such as

NumericShaper.Range.EUROPEAN

**Returns:**
- a contextual shaper for the specified Unicode ranges.

**Throws:**
- NullPointerException

- if

ranges

or

defaultContext

is

null

**Since:**
- 1.7

---

#### public void shape​(char[] text,
int start,
int count)

Converts the digits in the text that occur between start and
start + count.

**Parameters:**
- text

- an array of characters to convert
- start

- the index into

text

to start
converting
- count

- the number of characters in

text

to convert

**Throws:**
- IndexOutOfBoundsException

- if start or start + count is
out of bounds
- NullPointerException

- if text is null

---

#### public void shape​(char[] text,
int start,
int count,
int context)

Converts the digits in the text that occur between start and
start + count, using the provided context.
Context is ignored if the shaper is not a contextual shaper.

**Parameters:**
- text

- an array of characters
- start

- the index into

text

to start
converting
- count

- the number of characters in

text

to convert
- context

- the context to which to convert the
characters, such as

NumericShaper.EUROPEAN

**Throws:**
- IndexOutOfBoundsException

- if start or start + count is
out of bounds
- NullPointerException

- if text is null
- IllegalArgumentException

- if this is a contextual shaper
and the specified

context

is not a single valid
range.

---

#### public void shape​(char[] text,
int start,
int count,

NumericShaper.Range
context)

Converts the digits in the text that occur between

start

and

start + count

, using the provided

context

.

Context

is ignored if the shaper is not a
contextual shaper.

**Parameters:**
- text

- a

char

array
- start

- the index into

text

to start converting
- count

- the number of

char

s in

text

to convert
- context

- the context to which to convert the characters,
such as

NumericShaper.Range.EUROPEAN

**Throws:**
- IndexOutOfBoundsException

- if

start

or

start + count

is out of bounds
- NullPointerException

- if

text

or

context

is null

**Since:**
- 1.7

---

#### public boolean isContextual()

Returns a

boolean

indicating whether or not
this shaper shapes contextually.

**Returns:**
- true

if this shaper is contextual;

false

otherwise.

---

#### public int getRanges()

Returns an

int

that ORs together the values for
all the ranges that will be shaped.

For example, to check if a shaper shapes to Arabic, you would use the
following:

if ((shaper.getRanges() & shaper.ARABIC) != 0) &#123; ...

Note that this method supports only the bit mask-based
ranges. Call

getRangeSet()

for the enum-based ranges.

**Returns:**
- the values for all the ranges to be shaped.

---

#### public
Set
<
NumericShaper.Range
> getRangeSet()

Returns a

Set

representing all the Unicode ranges in
this

NumericShaper

that will be shaped.

**Returns:**
- all the Unicode ranges to be shaped.

**Since:**
- 1.7

---

#### public int hashCode()

Returns a hash code for this shaper.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- this shaper's hash code.

**See Also:**
- Object.hashCode()

---

#### public boolean equals​(
Object
o)

Returns

true

if the specified object is an instance of

NumericShaper

and shapes identically to this one,
regardless of the range representations, the bit mask or the
enum. For example, the following code produces

"true"

.

```java
NumericShaper ns1 = NumericShaper.getShaper(NumericShaper.ARABIC);
NumericShaper ns2 = NumericShaper.getShaper(NumericShaper.Range.ARABIC);
System.out.println(ns1.equals(ns2));
```

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the specified object to compare to this

NumericShaper

**Returns:**
- true

if

o

is an instance
of

NumericShaper

and shapes in the same way;

false

otherwise.

**See Also:**
- Object.equals(java.lang.Object)

---

#### public
String
toString()

Returns a

String

that describes this shaper. This method
is used for debugging purposes only.

**Overrides:**
- toString

in class

Object

**Returns:**
- a

String

describing this shaper.

---

### Additional Sections

#### Class NumericShaper

java.lang.Object

- java.awt.font.NumericShaper

java.awt.font.NumericShaper

**All Implemented Interfaces:** Serializable

```java
public final class
NumericShaper

extends
Object

implements
Serializable
```

The

NumericShaper

class is used to convert Latin-1 (European)
digits to other Unicode decimal digits. Users of this class will
primarily be people who wish to present data using
national digit shapes, but find it more convenient to represent the
data internally using Latin-1 (European) digits. This does not
interpret the deprecated numeric shape selector character (U+206E).

Instances of

NumericShaper

are typically applied
as attributes to text with the

NUMERIC_SHAPING

attribute
of the

TextAttribute

class.
For example, this code snippet causes a

TextLayout

to
shape European digits to Arabic in an Arabic context:

```java
Map map = new HashMap();
map.put(TextAttribute.NUMERIC_SHAPING,
NumericShaper.getContextualShaper(NumericShaper.ARABIC));
FontRenderContext frc = ...;
TextLayout layout = new TextLayout(text, map, frc);
layout.draw(g2d, x, y);
```

It is also possible to perform numeric shaping explicitly using instances
of

NumericShaper

, as this code snippet demonstrates:

```java
char[] text = ...;
// shape all EUROPEAN digits (except zero) to ARABIC digits
NumericShaper shaper = NumericShaper.getShaper(NumericShaper.ARABIC);
shaper.shape(text, start, count);

// shape European digits to ARABIC digits if preceding text is Arabic, or
// shape European digits to TAMIL digits if preceding text is Tamil, or
// leave European digits alone if there is no preceding text, or
// preceding text is neither Arabic nor Tamil
NumericShaper shaper =
NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);
shaper.shape(text, start, count);
```

Bit mask- and enum-based Unicode ranges

This class supports two different programming interfaces to
represent Unicode ranges for script-specific digits: bit
mask-based ones, such as

NumericShaper.ARABIC

, and
enum-based ones, such as

NumericShaper.Range.ARABIC

.
Multiple ranges can be specified by ORing bit mask-based constants,
such as:

```java
NumericShaper.ARABIC | NumericShaper.TAMIL
```

or creating a

Set

with the

NumericShaper.Range

constants, such as:

```java
EnumSet.of(NumericShaper.Range.ARABIC, NumericShaper.Range.TAMIL)
```

The enum-based ranges are a super set of the bit mask-based ones.

If the two interfaces are mixed (including serialization),
Unicode range values are mapped to their counterparts where such
mapping is possible, such as

NumericShaper.Range.ARABIC

from/to

NumericShaper.ARABIC

. If any unmappable range
values are specified, such as

NumericShaper.Range.BALINESE

,
those ranges are ignored.

Decimal Digits Precedence

A Unicode range may have more than one set of decimal digits. If
multiple decimal digits sets are specified for the same Unicode
range, one of the sets will take precedence as follows.

NumericShaper constants precedence

Unicode Range

NumericShaper

Constants

Precedence

Arabic

NumericShaper.ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.Range.ARABIC

NumericShaper.Range.EASTERN_ARABIC

NumericShaper.Range.EASTERN_ARABIC

Tai Tham

NumericShaper.Range.TAI_THAM_HORA

NumericShaper.Range.TAI_THAM_THAM

NumericShaper.Range.TAI_THAM_THAM

**Since:** 1.4
**See Also:** Serialized Form

public final class

NumericShaper

extends

Object

implements

Serializable

The

NumericShaper

class is used to convert Latin-1 (European)
digits to other Unicode decimal digits. Users of this class will
primarily be people who wish to present data using
national digit shapes, but find it more convenient to represent the
data internally using Latin-1 (European) digits. This does not
interpret the deprecated numeric shape selector character (U+206E).

Instances of

NumericShaper

are typically applied
as attributes to text with the

NUMERIC_SHAPING

attribute
of the

TextAttribute

class.
For example, this code snippet causes a

TextLayout

to
shape European digits to Arabic in an Arabic context:

```java
Map map = new HashMap();
map.put(TextAttribute.NUMERIC_SHAPING,
NumericShaper.getContextualShaper(NumericShaper.ARABIC));
FontRenderContext frc = ...;
TextLayout layout = new TextLayout(text, map, frc);
layout.draw(g2d, x, y);
```

It is also possible to perform numeric shaping explicitly using instances
of

NumericShaper

, as this code snippet demonstrates:

```java
char[] text = ...;
// shape all EUROPEAN digits (except zero) to ARABIC digits
NumericShaper shaper = NumericShaper.getShaper(NumericShaper.ARABIC);
shaper.shape(text, start, count);

// shape European digits to ARABIC digits if preceding text is Arabic, or
// shape European digits to TAMIL digits if preceding text is Tamil, or
// leave European digits alone if there is no preceding text, or
// preceding text is neither Arabic nor Tamil
NumericShaper shaper =
NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);
shaper.shape(text, start, count);
```

Bit mask- and enum-based Unicode ranges

This class supports two different programming interfaces to
represent Unicode ranges for script-specific digits: bit
mask-based ones, such as

NumericShaper.ARABIC

, and
enum-based ones, such as

NumericShaper.Range.ARABIC

.
Multiple ranges can be specified by ORing bit mask-based constants,
such as:

```java
NumericShaper.ARABIC | NumericShaper.TAMIL
```

or creating a

Set

with the

NumericShaper.Range

constants, such as:

```java
EnumSet.of(NumericShaper.Range.ARABIC, NumericShaper.Range.TAMIL)
```

The enum-based ranges are a super set of the bit mask-based ones.

If the two interfaces are mixed (including serialization),
Unicode range values are mapped to their counterparts where such
mapping is possible, such as

NumericShaper.Range.ARABIC

from/to

NumericShaper.ARABIC

. If any unmappable range
values are specified, such as

NumericShaper.Range.BALINESE

,
those ranges are ignored.

Decimal Digits Precedence

A Unicode range may have more than one set of decimal digits. If
multiple decimal digits sets are specified for the same Unicode
range, one of the sets will take precedence as follows.

NumericShaper constants precedence

Unicode Range

NumericShaper

Constants

Precedence

Arabic

NumericShaper.ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.Range.ARABIC

NumericShaper.Range.EASTERN_ARABIC

NumericShaper.Range.EASTERN_ARABIC

Tai Tham

NumericShaper.Range.TAI_THAM_HORA

NumericShaper.Range.TAI_THAM_THAM

NumericShaper.Range.TAI_THAM_THAM

Instances of

NumericShaper

are typically applied
as attributes to text with the

NUMERIC_SHAPING

attribute
of the

TextAttribute

class.
For example, this code snippet causes a

TextLayout

to
shape European digits to Arabic in an Arabic context:

```java
Map map = new HashMap();
map.put(TextAttribute.NUMERIC_SHAPING,
NumericShaper.getContextualShaper(NumericShaper.ARABIC));
FontRenderContext frc = ...;
TextLayout layout = new TextLayout(text, map, frc);
layout.draw(g2d, x, y);
```

It is also possible to perform numeric shaping explicitly using instances
of

NumericShaper

, as this code snippet demonstrates:

```java
char[] text = ...;
// shape all EUROPEAN digits (except zero) to ARABIC digits
NumericShaper shaper = NumericShaper.getShaper(NumericShaper.ARABIC);
shaper.shape(text, start, count);

// shape European digits to ARABIC digits if preceding text is Arabic, or
// shape European digits to TAMIL digits if preceding text is Tamil, or
// leave European digits alone if there is no preceding text, or
// preceding text is neither Arabic nor Tamil
NumericShaper shaper =
NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);
shaper.shape(text, start, count);
```

Bit mask- and enum-based Unicode ranges

This class supports two different programming interfaces to
represent Unicode ranges for script-specific digits: bit
mask-based ones, such as

NumericShaper.ARABIC

, and
enum-based ones, such as

NumericShaper.Range.ARABIC

.
Multiple ranges can be specified by ORing bit mask-based constants,
such as:

```java
NumericShaper.ARABIC | NumericShaper.TAMIL
```

or creating a

Set

with the

NumericShaper.Range

constants, such as:

```java
EnumSet.of(NumericShaper.Range.ARABIC, NumericShaper.Range.TAMIL)
```

The enum-based ranges are a super set of the bit mask-based ones.

If the two interfaces are mixed (including serialization),
Unicode range values are mapped to their counterparts where such
mapping is possible, such as

NumericShaper.Range.ARABIC

from/to

NumericShaper.ARABIC

. If any unmappable range
values are specified, such as

NumericShaper.Range.BALINESE

,
those ranges are ignored.

Decimal Digits Precedence

A Unicode range may have more than one set of decimal digits. If
multiple decimal digits sets are specified for the same Unicode
range, one of the sets will take precedence as follows.

NumericShaper constants precedence

Unicode Range

NumericShaper

Constants

Precedence

Arabic

NumericShaper.ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.Range.ARABIC

NumericShaper.Range.EASTERN_ARABIC

NumericShaper.Range.EASTERN_ARABIC

Tai Tham

NumericShaper.Range.TAI_THAM_HORA

NumericShaper.Range.TAI_THAM_THAM

NumericShaper.Range.TAI_THAM_THAM

Map map = new HashMap();
map.put(TextAttribute.NUMERIC_SHAPING,
NumericShaper.getContextualShaper(NumericShaper.ARABIC));
FontRenderContext frc = ...;
TextLayout layout = new TextLayout(text, map, frc);
layout.draw(g2d, x, y);

char[] text = ...;
// shape all EUROPEAN digits (except zero) to ARABIC digits
NumericShaper shaper = NumericShaper.getShaper(NumericShaper.ARABIC);
shaper.shape(text, start, count);

// shape European digits to ARABIC digits if preceding text is Arabic, or
// shape European digits to TAMIL digits if preceding text is Tamil, or
// leave European digits alone if there is no preceding text, or
// preceding text is neither Arabic nor Tamil
NumericShaper shaper =
NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);
shaper.shape(text, start, count);

Bit mask- and enum-based Unicode ranges

This class supports two different programming interfaces to
represent Unicode ranges for script-specific digits: bit
mask-based ones, such as

NumericShaper.ARABIC

, and
enum-based ones, such as

NumericShaper.Range.ARABIC

.
Multiple ranges can be specified by ORing bit mask-based constants,
such as:

```java
NumericShaper.ARABIC | NumericShaper.TAMIL
```

or creating a

Set

with the

NumericShaper.Range

constants, such as:

```java
EnumSet.of(NumericShaper.Range.ARABIC, NumericShaper.Range.TAMIL)
```

The enum-based ranges are a super set of the bit mask-based ones.

If the two interfaces are mixed (including serialization),
Unicode range values are mapped to their counterparts where such
mapping is possible, such as

NumericShaper.Range.ARABIC

from/to

NumericShaper.ARABIC

. If any unmappable range
values are specified, such as

NumericShaper.Range.BALINESE

,
those ranges are ignored.

Decimal Digits Precedence

A Unicode range may have more than one set of decimal digits. If
multiple decimal digits sets are specified for the same Unicode
range, one of the sets will take precedence as follows.

NumericShaper constants precedence

Unicode Range

NumericShaper

Constants

Precedence

Arabic

NumericShaper.ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.Range.ARABIC

NumericShaper.Range.EASTERN_ARABIC

NumericShaper.Range.EASTERN_ARABIC

Tai Tham

NumericShaper.Range.TAI_THAM_HORA

NumericShaper.Range.TAI_THAM_THAM

NumericShaper.Range.TAI_THAM_THAM

NumericShaper.ARABIC | NumericShaper.TAMIL

EnumSet.of(NumericShaper.Range.ARABIC, NumericShaper.Range.TAMIL)

If the two interfaces are mixed (including serialization),
Unicode range values are mapped to their counterparts where such
mapping is possible, such as

NumericShaper.Range.ARABIC

from/to

NumericShaper.ARABIC

. If any unmappable range
values are specified, such as

NumericShaper.Range.BALINESE

,
those ranges are ignored.

Decimal Digits Precedence

A Unicode range may have more than one set of decimal digits. If
multiple decimal digits sets are specified for the same Unicode
range, one of the sets will take precedence as follows.

NumericShaper constants precedence

Unicode Range

NumericShaper

Constants

Precedence

Arabic

NumericShaper.ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.Range.ARABIC

NumericShaper.Range.EASTERN_ARABIC

NumericShaper.Range.EASTERN_ARABIC

Tai Tham

NumericShaper.Range.TAI_THAM_HORA

NumericShaper.Range.TAI_THAM_THAM

NumericShaper.Range.TAI_THAM_THAM

Decimal Digits Precedence

A Unicode range may have more than one set of decimal digits. If
multiple decimal digits sets are specified for the same Unicode
range, one of the sets will take precedence as follows.

NumericShaper constants precedence

Unicode Range

NumericShaper

Constants

Precedence

Arabic

NumericShaper.ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.EASTERN_ARABIC

NumericShaper.Range.ARABIC

NumericShaper.Range.EASTERN_ARABIC

NumericShaper.Range.EASTERN_ARABIC

Tai Tham

NumericShaper.Range.TAI_THAM_HORA

NumericShaper.Range.TAI_THAM_THAM

NumericShaper.Range.TAI_THAM_THAM

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

NumericShaper.Range

A

NumericShaper.Range

represents a Unicode range of a
script having its own decimal digits.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ALL_RANGES

Identifies all ranges, for full contextual shaping.

static int

ARABIC

Identifies the ARABIC range and decimal base.

static int

BENGALI

Identifies the BENGALI range and decimal base.

static int

DEVANAGARI

Identifies the DEVANAGARI range and decimal base.

static int

EASTERN_ARABIC

Identifies the ARABIC range and ARABIC_EXTENDED decimal base.

static int

ETHIOPIC

Identifies the ETHIOPIC range and decimal base.

static int

EUROPEAN

Identifies the Latin-1 (European) and extended range, and
Latin-1 (European) decimal base.

static int

GUJARATI

Identifies the GUJARATI range and decimal base.

static int

GURMUKHI

Identifies the GURMUKHI range and decimal base.

static int

KANNADA

Identifies the KANNADA range and decimal base.

static int

KHMER

Identifies the KHMER range and decimal base.

static int

LAO

Identifies the LAO range and decimal base.

static int

MALAYALAM

Identifies the MALAYALAM range and decimal base.

static int

MONGOLIAN

Identifies the MONGOLIAN range and decimal base.

static int

MYANMAR

Identifies the MYANMAR range and decimal base.

static int

ORIYA

Identifies the ORIYA range and decimal base.

static int

TAMIL

Identifies the TAMIL range and decimal base.

static int

TELUGU

Identifies the TELUGU range and decimal base.

static int

THAI

Identifies the THAI range and decimal base.

static int

TIBETAN

Identifies the TIBETAN range and decimal base.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Returns

true

if the specified object is an instance of

NumericShaper

and shapes identically to this one,
regardless of the range representations, the bit mask or the
enum.

static

NumericShaper

getContextualShaper

​(int ranges)

Returns a contextual shaper for the provided unicode range(s).

static

NumericShaper

getContextualShaper

​(int ranges,
int defaultContext)

Returns a contextual shaper for the provided unicode range(s).

static

NumericShaper

getContextualShaper

​(

Set

<

NumericShaper.Range

> ranges)

Returns a contextual shaper for the provided Unicode
range(s).

static

NumericShaper

getContextualShaper

​(

Set

<

NumericShaper.Range

> ranges,

NumericShaper.Range

defaultContext)

Returns a contextual shaper for the provided Unicode range(s).

int

getRanges

()

Returns an

int

that ORs together the values for
all the ranges that will be shaped.

Set

<

NumericShaper.Range

>

getRangeSet

()

Returns a

Set

representing all the Unicode ranges in
this

NumericShaper

that will be shaped.

static

NumericShaper

getShaper

​(int singleRange)

Returns a shaper for the provided unicode range.

static

NumericShaper

getShaper

​(

NumericShaper.Range

singleRange)

Returns a shaper for the provided Unicode
range.

int

hashCode

()

Returns a hash code for this shaper.

boolean

isContextual

()

Returns a

boolean

indicating whether or not
this shaper shapes contextually.

void

shape

​(char[] text,
int start,
int count)

Converts the digits in the text that occur between start and
start + count.

void

shape

​(char[] text,
int start,
int count,
int context)

Converts the digits in the text that occur between start and
start + count, using the provided context.

void

shape

​(char[] text,
int start,
int count,

NumericShaper.Range

context)

Converts the digits in the text that occur between

start

and

start + count

, using the provided

context

.

String

toString

()

Returns a

String

that describes this shaper.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

NumericShaper.Range

A

NumericShaper.Range

represents a Unicode range of a
script having its own decimal digits.

---

#### Nested Class Summary

A

NumericShaper.Range

represents a Unicode range of a
script having its own decimal digits.

Field Summary

Fields

Modifier and Type

Field

Description

static int

ALL_RANGES

Identifies all ranges, for full contextual shaping.

static int

ARABIC

Identifies the ARABIC range and decimal base.

static int

BENGALI

Identifies the BENGALI range and decimal base.

static int

DEVANAGARI

Identifies the DEVANAGARI range and decimal base.

static int

EASTERN_ARABIC

Identifies the ARABIC range and ARABIC_EXTENDED decimal base.

static int

ETHIOPIC

Identifies the ETHIOPIC range and decimal base.

static int

EUROPEAN

Identifies the Latin-1 (European) and extended range, and
Latin-1 (European) decimal base.

static int

GUJARATI

Identifies the GUJARATI range and decimal base.

static int

GURMUKHI

Identifies the GURMUKHI range and decimal base.

static int

KANNADA

Identifies the KANNADA range and decimal base.

static int

KHMER

Identifies the KHMER range and decimal base.

static int

LAO

Identifies the LAO range and decimal base.

static int

MALAYALAM

Identifies the MALAYALAM range and decimal base.

static int

MONGOLIAN

Identifies the MONGOLIAN range and decimal base.

static int

MYANMAR

Identifies the MYANMAR range and decimal base.

static int

ORIYA

Identifies the ORIYA range and decimal base.

static int

TAMIL

Identifies the TAMIL range and decimal base.

static int

TELUGU

Identifies the TELUGU range and decimal base.

static int

THAI

Identifies the THAI range and decimal base.

static int

TIBETAN

Identifies the TIBETAN range and decimal base.

---

#### Field Summary

Identifies all ranges, for full contextual shaping.

Identifies the ARABIC range and decimal base.

Identifies the BENGALI range and decimal base.

Identifies the DEVANAGARI range and decimal base.

Identifies the ARABIC range and ARABIC_EXTENDED decimal base.

Identifies the ETHIOPIC range and decimal base.

Identifies the Latin-1 (European) and extended range, and
Latin-1 (European) decimal base.

Identifies the GUJARATI range and decimal base.

Identifies the GURMUKHI range and decimal base.

Identifies the KANNADA range and decimal base.

Identifies the KHMER range and decimal base.

Identifies the LAO range and decimal base.

Identifies the MALAYALAM range and decimal base.

Identifies the MONGOLIAN range and decimal base.

Identifies the MYANMAR range and decimal base.

Identifies the ORIYA range and decimal base.

Identifies the TAMIL range and decimal base.

Identifies the TELUGU range and decimal base.

Identifies the THAI range and decimal base.

Identifies the TIBETAN range and decimal base.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Returns

true

if the specified object is an instance of

NumericShaper

and shapes identically to this one,
regardless of the range representations, the bit mask or the
enum.

static

NumericShaper

getContextualShaper

​(int ranges)

Returns a contextual shaper for the provided unicode range(s).

static

NumericShaper

getContextualShaper

​(int ranges,
int defaultContext)

Returns a contextual shaper for the provided unicode range(s).

static

NumericShaper

getContextualShaper

​(

Set

<

NumericShaper.Range

> ranges)

Returns a contextual shaper for the provided Unicode
range(s).

static

NumericShaper

getContextualShaper

​(

Set

<

NumericShaper.Range

> ranges,

NumericShaper.Range

defaultContext)

Returns a contextual shaper for the provided Unicode range(s).

int

getRanges

()

Returns an

int

that ORs together the values for
all the ranges that will be shaped.

Set

<

NumericShaper.Range

>

getRangeSet

()

Returns a

Set

representing all the Unicode ranges in
this

NumericShaper

that will be shaped.

static

NumericShaper

getShaper

​(int singleRange)

Returns a shaper for the provided unicode range.

static

NumericShaper

getShaper

​(

NumericShaper.Range

singleRange)

Returns a shaper for the provided Unicode
range.

int

hashCode

()

Returns a hash code for this shaper.

boolean

isContextual

()

Returns a

boolean

indicating whether or not
this shaper shapes contextually.

void

shape

​(char[] text,
int start,
int count)

Converts the digits in the text that occur between start and
start + count.

void

shape

​(char[] text,
int start,
int count,
int context)

Converts the digits in the text that occur between start and
start + count, using the provided context.

void

shape

​(char[] text,
int start,
int count,

NumericShaper.Range

context)

Converts the digits in the text that occur between

start

and

start + count

, using the provided

context

.

String

toString

()

Returns a

String

that describes this shaper.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Returns

true

if the specified object is an instance of

NumericShaper

and shapes identically to this one,
regardless of the range representations, the bit mask or the
enum.

Returns a contextual shaper for the provided unicode range(s).

Returns a contextual shaper for the provided Unicode
range(s).

Returns a contextual shaper for the provided Unicode range(s).

Returns an

int

that ORs together the values for
all the ranges that will be shaped.

Returns a

Set

representing all the Unicode ranges in
this

NumericShaper

that will be shaped.

Returns a shaper for the provided unicode range.

Returns a shaper for the provided Unicode
range.

Returns a hash code for this shaper.

Returns a

boolean

indicating whether or not
this shaper shapes contextually.

Converts the digits in the text that occur between start and
start + count.

Converts the digits in the text that occur between start and
start + count, using the provided context.

Converts the digits in the text that occur between

start

and

start + count

, using the provided

context

.

Returns a

String

that describes this shaper.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- EUROPEAN

```java
public static final int EUROPEAN
```

Identifies the Latin-1 (European) and extended range, and
Latin-1 (European) decimal base.

**See Also:** Constant Field Values

- ARABIC

```java
public static final int ARABIC
```

Identifies the ARABIC range and decimal base.

**See Also:** Constant Field Values

- EASTERN_ARABIC

```java
public static final int EASTERN_ARABIC
```

Identifies the ARABIC range and ARABIC_EXTENDED decimal base.

**See Also:** Constant Field Values

- DEVANAGARI

```java
public static final int DEVANAGARI
```

Identifies the DEVANAGARI range and decimal base.

**See Also:** Constant Field Values

- BENGALI

```java
public static final int BENGALI
```

Identifies the BENGALI range and decimal base.

**See Also:** Constant Field Values

- GURMUKHI

```java
public static final int GURMUKHI
```

Identifies the GURMUKHI range and decimal base.

**See Also:** Constant Field Values

- GUJARATI

```java
public static final int GUJARATI
```

Identifies the GUJARATI range and decimal base.

**See Also:** Constant Field Values

- ORIYA

```java
public static final int ORIYA
```

Identifies the ORIYA range and decimal base.

**See Also:** Constant Field Values

- TAMIL

```java
public static final int TAMIL
```

Identifies the TAMIL range and decimal base.

**See Also:** Constant Field Values

- TELUGU

```java
public static final int TELUGU
```

Identifies the TELUGU range and decimal base.

**See Also:** Constant Field Values

- KANNADA

```java
public static final int KANNADA
```

Identifies the KANNADA range and decimal base.

**See Also:** Constant Field Values

- MALAYALAM

```java
public static final int MALAYALAM
```

Identifies the MALAYALAM range and decimal base.

**See Also:** Constant Field Values

- THAI

```java
public static final int THAI
```

Identifies the THAI range and decimal base.

**See Also:** Constant Field Values

- LAO

```java
public static final int LAO
```

Identifies the LAO range and decimal base.

**See Also:** Constant Field Values

- TIBETAN

```java
public static final int TIBETAN
```

Identifies the TIBETAN range and decimal base.

**See Also:** Constant Field Values

- MYANMAR

```java
public static final int MYANMAR
```

Identifies the MYANMAR range and decimal base.

**See Also:** Constant Field Values

- ETHIOPIC

```java
public static final int ETHIOPIC
```

Identifies the ETHIOPIC range and decimal base.

**See Also:** Constant Field Values

- KHMER

```java
public static final int KHMER
```

Identifies the KHMER range and decimal base.

**See Also:** Constant Field Values

- MONGOLIAN

```java
public static final int MONGOLIAN
```

Identifies the MONGOLIAN range and decimal base.

**See Also:** Constant Field Values

- ALL_RANGES

```java
public static final int ALL_RANGES
```

Identifies all ranges, for full contextual shaping.

This constant specifies all of the bit mask-based
ranges. Use

EnumSet.allOf(NumericShaper.Range.class)

to
specify all of the enum-based ranges.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getShaper

```java
public static
NumericShaper
getShaper​(int singleRange)
```

Returns a shaper for the provided unicode range. All
Latin-1 (EUROPEAN) digits are converted
to the corresponding decimal unicode digits.

**Parameters:** singleRange

- the specified Unicode range
**Returns:** a non-contextual numeric shaper
**Throws:** IllegalArgumentException

- if the range is not a single range

- getShaper

```java
public static
NumericShaper
getShaper​(
NumericShaper.Range
singleRange)
```

Returns a shaper for the provided Unicode
range. All Latin-1 (EUROPEAN) digits are converted to the
corresponding decimal digits of the specified Unicode range.

**Parameters:** singleRange

- the Unicode range given by a

NumericShaper.Range

constant.
**Returns:** a non-contextual

NumericShaper

.
**Throws:** NullPointerException

- if

singleRange

is

null
**Since:** 1.7

- getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(int ranges)
```

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits are converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, such as,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper assumes EUROPEAN as the starting context, that is, if
EUROPEAN digits are encountered before any strong directional
text in the string, the context is presumed to be EUROPEAN, and
so the digits will not shape.

**Parameters:** ranges

- the specified Unicode ranges
**Returns:** a shaper for the specified ranges

- getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(
Set
<
NumericShaper.Range
> ranges)
```

Returns a contextual shaper for the provided Unicode
range(s). The Latin-1 (EUROPEAN) digits are converted to the
decimal digits corresponding to the range of the preceding
text, if the range is one of the provided ranges.

The shaper assumes EUROPEAN as the starting context, that
is, if EUROPEAN digits are encountered before any strong
directional text in the string, the context is presumed to be
EUROPEAN, and so the digits will not shape.

**Parameters:** ranges

- the specified Unicode ranges
**Returns:** a contextual shaper for the specified ranges
**Throws:** NullPointerException

- if

ranges

is

null

.
**Since:** 1.7

- getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(int ranges,
int defaultContext)
```

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits will be converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, for example,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper uses defaultContext as the starting context.

**Parameters:** ranges

- the specified Unicode ranges
**Parameters:** defaultContext

- the starting context, such as

NumericShaper.EUROPEAN
**Returns:** a shaper for the specified Unicode ranges.
**Throws:** IllegalArgumentException

- if the specified

defaultContext

is not a single valid range.

- getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(
Set
<
NumericShaper.Range
> ranges,

NumericShaper.Range
defaultContext)
```

Returns a contextual shaper for the provided Unicode range(s).
The Latin-1 (EUROPEAN) digits will be converted to the decimal
digits corresponding to the range of the preceding text, if the
range is one of the provided ranges. The shaper uses

defaultContext

as the starting context.

**Parameters:** ranges

- the specified Unicode ranges
**Parameters:** defaultContext

- the starting context, such as

NumericShaper.Range.EUROPEAN
**Returns:** a contextual shaper for the specified Unicode ranges.
**Throws:** NullPointerException

- if

ranges

or

defaultContext

is

null
**Since:** 1.7

- shape

```java
public void shape​(char[] text,
int start,
int count)
```

Converts the digits in the text that occur between start and
start + count.

**Parameters:** text

- an array of characters to convert
**Parameters:** start

- the index into

text

to start
converting
**Parameters:** count

- the number of characters in

text

to convert
**Throws:** IndexOutOfBoundsException

- if start or start + count is
out of bounds
**Throws:** NullPointerException

- if text is null

- shape

```java
public void shape​(char[] text,
int start,
int count,
int context)
```

Converts the digits in the text that occur between start and
start + count, using the provided context.
Context is ignored if the shaper is not a contextual shaper.

**Parameters:** text

- an array of characters
**Parameters:** start

- the index into

text

to start
converting
**Parameters:** count

- the number of characters in

text

to convert
**Parameters:** context

- the context to which to convert the
characters, such as

NumericShaper.EUROPEAN
**Throws:** IndexOutOfBoundsException

- if start or start + count is
out of bounds
**Throws:** NullPointerException

- if text is null
**Throws:** IllegalArgumentException

- if this is a contextual shaper
and the specified

context

is not a single valid
range.

- shape

```java
public void shape​(char[] text,
int start,
int count,

NumericShaper.Range
context)
```

Converts the digits in the text that occur between

start

and

start + count

, using the provided

context

.

Context

is ignored if the shaper is not a
contextual shaper.

**Parameters:** text

- a

char

array
**Parameters:** start

- the index into

text

to start converting
**Parameters:** count

- the number of

char

s in

text

to convert
**Parameters:** context

- the context to which to convert the characters,
such as

NumericShaper.Range.EUROPEAN
**Throws:** IndexOutOfBoundsException

- if

start

or

start + count

is out of bounds
**Throws:** NullPointerException

- if

text

or

context

is null
**Since:** 1.7

- isContextual

```java
public boolean isContextual()
```

Returns a

boolean

indicating whether or not
this shaper shapes contextually.

**Returns:** true

if this shaper is contextual;

false

otherwise.

- getRanges

```java
public int getRanges()
```

Returns an

int

that ORs together the values for
all the ranges that will be shaped.

For example, to check if a shaper shapes to Arabic, you would use the
following:

if ((shaper.getRanges() & shaper.ARABIC) != 0) &#123; ...

Note that this method supports only the bit mask-based
ranges. Call

getRangeSet()

for the enum-based ranges.

**Returns:** the values for all the ranges to be shaped.

- getRangeSet

```java
public
Set
<
NumericShaper.Range
> getRangeSet()
```

Returns a

Set

representing all the Unicode ranges in
this

NumericShaper

that will be shaped.

**Returns:** all the Unicode ranges to be shaped.
**Since:** 1.7

- hashCode

```java
public int hashCode()
```

Returns a hash code for this shaper.

**Overrides:** hashCode

in class

Object
**Returns:** this shaper's hash code.
**See Also:** Object.hashCode()

- equals

```java
public boolean equals​(
Object
o)
```

Returns

true

if the specified object is an instance of

NumericShaper

and shapes identically to this one,
regardless of the range representations, the bit mask or the
enum. For example, the following code produces

"true"

.

```java
NumericShaper ns1 = NumericShaper.getShaper(NumericShaper.ARABIC);
NumericShaper ns2 = NumericShaper.getShaper(NumericShaper.Range.ARABIC);
System.out.println(ns1.equals(ns2));
```

**Overrides:** equals

in class

Object
**Parameters:** o

- the specified object to compare to this

NumericShaper
**Returns:** true

if

o

is an instance
of

NumericShaper

and shapes in the same way;

false

otherwise.
**See Also:** Object.equals(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a

String

that describes this shaper. This method
is used for debugging purposes only.

**Overrides:** toString

in class

Object
**Returns:** a

String

describing this shaper.

Field Detail

- EUROPEAN

```java
public static final int EUROPEAN
```

Identifies the Latin-1 (European) and extended range, and
Latin-1 (European) decimal base.

**See Also:** Constant Field Values

- ARABIC

```java
public static final int ARABIC
```

Identifies the ARABIC range and decimal base.

**See Also:** Constant Field Values

- EASTERN_ARABIC

```java
public static final int EASTERN_ARABIC
```

Identifies the ARABIC range and ARABIC_EXTENDED decimal base.

**See Also:** Constant Field Values

- DEVANAGARI

```java
public static final int DEVANAGARI
```

Identifies the DEVANAGARI range and decimal base.

**See Also:** Constant Field Values

- BENGALI

```java
public static final int BENGALI
```

Identifies the BENGALI range and decimal base.

**See Also:** Constant Field Values

- GURMUKHI

```java
public static final int GURMUKHI
```

Identifies the GURMUKHI range and decimal base.

**See Also:** Constant Field Values

- GUJARATI

```java
public static final int GUJARATI
```

Identifies the GUJARATI range and decimal base.

**See Also:** Constant Field Values

- ORIYA

```java
public static final int ORIYA
```

Identifies the ORIYA range and decimal base.

**See Also:** Constant Field Values

- TAMIL

```java
public static final int TAMIL
```

Identifies the TAMIL range and decimal base.

**See Also:** Constant Field Values

- TELUGU

```java
public static final int TELUGU
```

Identifies the TELUGU range and decimal base.

**See Also:** Constant Field Values

- KANNADA

```java
public static final int KANNADA
```

Identifies the KANNADA range and decimal base.

**See Also:** Constant Field Values

- MALAYALAM

```java
public static final int MALAYALAM
```

Identifies the MALAYALAM range and decimal base.

**See Also:** Constant Field Values

- THAI

```java
public static final int THAI
```

Identifies the THAI range and decimal base.

**See Also:** Constant Field Values

- LAO

```java
public static final int LAO
```

Identifies the LAO range and decimal base.

**See Also:** Constant Field Values

- TIBETAN

```java
public static final int TIBETAN
```

Identifies the TIBETAN range and decimal base.

**See Also:** Constant Field Values

- MYANMAR

```java
public static final int MYANMAR
```

Identifies the MYANMAR range and decimal base.

**See Also:** Constant Field Values

- ETHIOPIC

```java
public static final int ETHIOPIC
```

Identifies the ETHIOPIC range and decimal base.

**See Also:** Constant Field Values

- KHMER

```java
public static final int KHMER
```

Identifies the KHMER range and decimal base.

**See Also:** Constant Field Values

- MONGOLIAN

```java
public static final int MONGOLIAN
```

Identifies the MONGOLIAN range and decimal base.

**See Also:** Constant Field Values

- ALL_RANGES

```java
public static final int ALL_RANGES
```

Identifies all ranges, for full contextual shaping.

This constant specifies all of the bit mask-based
ranges. Use

EnumSet.allOf(NumericShaper.Range.class)

to
specify all of the enum-based ranges.

**See Also:** Constant Field Values

---

#### Field Detail

EUROPEAN

```java
public static final int EUROPEAN
```

Identifies the Latin-1 (European) and extended range, and
Latin-1 (European) decimal base.

**See Also:** Constant Field Values

---

#### EUROPEAN

public static final int EUROPEAN

Identifies the Latin-1 (European) and extended range, and
Latin-1 (European) decimal base.

ARABIC

```java
public static final int ARABIC
```

Identifies the ARABIC range and decimal base.

**See Also:** Constant Field Values

---

#### ARABIC

public static final int ARABIC

Identifies the ARABIC range and decimal base.

EASTERN_ARABIC

```java
public static final int EASTERN_ARABIC
```

Identifies the ARABIC range and ARABIC_EXTENDED decimal base.

**See Also:** Constant Field Values

---

#### EASTERN_ARABIC

public static final int EASTERN_ARABIC

Identifies the ARABIC range and ARABIC_EXTENDED decimal base.

DEVANAGARI

```java
public static final int DEVANAGARI
```

Identifies the DEVANAGARI range and decimal base.

**See Also:** Constant Field Values

---

#### DEVANAGARI

public static final int DEVANAGARI

Identifies the DEVANAGARI range and decimal base.

BENGALI

```java
public static final int BENGALI
```

Identifies the BENGALI range and decimal base.

**See Also:** Constant Field Values

---

#### BENGALI

public static final int BENGALI

Identifies the BENGALI range and decimal base.

GURMUKHI

```java
public static final int GURMUKHI
```

Identifies the GURMUKHI range and decimal base.

**See Also:** Constant Field Values

---

#### GURMUKHI

public static final int GURMUKHI

Identifies the GURMUKHI range and decimal base.

GUJARATI

```java
public static final int GUJARATI
```

Identifies the GUJARATI range and decimal base.

**See Also:** Constant Field Values

---

#### GUJARATI

public static final int GUJARATI

Identifies the GUJARATI range and decimal base.

ORIYA

```java
public static final int ORIYA
```

Identifies the ORIYA range and decimal base.

**See Also:** Constant Field Values

---

#### ORIYA

public static final int ORIYA

Identifies the ORIYA range and decimal base.

TAMIL

```java
public static final int TAMIL
```

Identifies the TAMIL range and decimal base.

**See Also:** Constant Field Values

---

#### TAMIL

public static final int TAMIL

Identifies the TAMIL range and decimal base.

TELUGU

```java
public static final int TELUGU
```

Identifies the TELUGU range and decimal base.

**See Also:** Constant Field Values

---

#### TELUGU

public static final int TELUGU

Identifies the TELUGU range and decimal base.

KANNADA

```java
public static final int KANNADA
```

Identifies the KANNADA range and decimal base.

**See Also:** Constant Field Values

---

#### KANNADA

public static final int KANNADA

Identifies the KANNADA range and decimal base.

MALAYALAM

```java
public static final int MALAYALAM
```

Identifies the MALAYALAM range and decimal base.

**See Also:** Constant Field Values

---

#### MALAYALAM

public static final int MALAYALAM

Identifies the MALAYALAM range and decimal base.

THAI

```java
public static final int THAI
```

Identifies the THAI range and decimal base.

**See Also:** Constant Field Values

---

#### THAI

public static final int THAI

Identifies the THAI range and decimal base.

LAO

```java
public static final int LAO
```

Identifies the LAO range and decimal base.

**See Also:** Constant Field Values

---

#### LAO

public static final int LAO

Identifies the LAO range and decimal base.

TIBETAN

```java
public static final int TIBETAN
```

Identifies the TIBETAN range and decimal base.

**See Also:** Constant Field Values

---

#### TIBETAN

public static final int TIBETAN

Identifies the TIBETAN range and decimal base.

MYANMAR

```java
public static final int MYANMAR
```

Identifies the MYANMAR range and decimal base.

**See Also:** Constant Field Values

---

#### MYANMAR

public static final int MYANMAR

Identifies the MYANMAR range and decimal base.

ETHIOPIC

```java
public static final int ETHIOPIC
```

Identifies the ETHIOPIC range and decimal base.

**See Also:** Constant Field Values

---

#### ETHIOPIC

public static final int ETHIOPIC

Identifies the ETHIOPIC range and decimal base.

KHMER

```java
public static final int KHMER
```

Identifies the KHMER range and decimal base.

**See Also:** Constant Field Values

---

#### KHMER

public static final int KHMER

Identifies the KHMER range and decimal base.

MONGOLIAN

```java
public static final int MONGOLIAN
```

Identifies the MONGOLIAN range and decimal base.

**See Also:** Constant Field Values

---

#### MONGOLIAN

public static final int MONGOLIAN

Identifies the MONGOLIAN range and decimal base.

ALL_RANGES

```java
public static final int ALL_RANGES
```

Identifies all ranges, for full contextual shaping.

This constant specifies all of the bit mask-based
ranges. Use

EnumSet.allOf(NumericShaper.Range.class)

to
specify all of the enum-based ranges.

**See Also:** Constant Field Values

---

#### ALL_RANGES

public static final int ALL_RANGES

Identifies all ranges, for full contextual shaping.

This constant specifies all of the bit mask-based
ranges. Use

EnumSet.allOf(NumericShaper.Range.class)

to
specify all of the enum-based ranges.

This constant specifies all of the bit mask-based
ranges. Use

EnumSet.allOf(NumericShaper.Range.class)

to
specify all of the enum-based ranges.

Method Detail

- getShaper

```java
public static
NumericShaper
getShaper​(int singleRange)
```

Returns a shaper for the provided unicode range. All
Latin-1 (EUROPEAN) digits are converted
to the corresponding decimal unicode digits.

**Parameters:** singleRange

- the specified Unicode range
**Returns:** a non-contextual numeric shaper
**Throws:** IllegalArgumentException

- if the range is not a single range

- getShaper

```java
public static
NumericShaper
getShaper​(
NumericShaper.Range
singleRange)
```

Returns a shaper for the provided Unicode
range. All Latin-1 (EUROPEAN) digits are converted to the
corresponding decimal digits of the specified Unicode range.

**Parameters:** singleRange

- the Unicode range given by a

NumericShaper.Range

constant.
**Returns:** a non-contextual

NumericShaper

.
**Throws:** NullPointerException

- if

singleRange

is

null
**Since:** 1.7

- getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(int ranges)
```

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits are converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, such as,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper assumes EUROPEAN as the starting context, that is, if
EUROPEAN digits are encountered before any strong directional
text in the string, the context is presumed to be EUROPEAN, and
so the digits will not shape.

**Parameters:** ranges

- the specified Unicode ranges
**Returns:** a shaper for the specified ranges

- getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(
Set
<
NumericShaper.Range
> ranges)
```

Returns a contextual shaper for the provided Unicode
range(s). The Latin-1 (EUROPEAN) digits are converted to the
decimal digits corresponding to the range of the preceding
text, if the range is one of the provided ranges.

The shaper assumes EUROPEAN as the starting context, that
is, if EUROPEAN digits are encountered before any strong
directional text in the string, the context is presumed to be
EUROPEAN, and so the digits will not shape.

**Parameters:** ranges

- the specified Unicode ranges
**Returns:** a contextual shaper for the specified ranges
**Throws:** NullPointerException

- if

ranges

is

null

.
**Since:** 1.7

- getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(int ranges,
int defaultContext)
```

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits will be converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, for example,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper uses defaultContext as the starting context.

**Parameters:** ranges

- the specified Unicode ranges
**Parameters:** defaultContext

- the starting context, such as

NumericShaper.EUROPEAN
**Returns:** a shaper for the specified Unicode ranges.
**Throws:** IllegalArgumentException

- if the specified

defaultContext

is not a single valid range.

- getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(
Set
<
NumericShaper.Range
> ranges,

NumericShaper.Range
defaultContext)
```

Returns a contextual shaper for the provided Unicode range(s).
The Latin-1 (EUROPEAN) digits will be converted to the decimal
digits corresponding to the range of the preceding text, if the
range is one of the provided ranges. The shaper uses

defaultContext

as the starting context.

**Parameters:** ranges

- the specified Unicode ranges
**Parameters:** defaultContext

- the starting context, such as

NumericShaper.Range.EUROPEAN
**Returns:** a contextual shaper for the specified Unicode ranges.
**Throws:** NullPointerException

- if

ranges

or

defaultContext

is

null
**Since:** 1.7

- shape

```java
public void shape​(char[] text,
int start,
int count)
```

Converts the digits in the text that occur between start and
start + count.

**Parameters:** text

- an array of characters to convert
**Parameters:** start

- the index into

text

to start
converting
**Parameters:** count

- the number of characters in

text

to convert
**Throws:** IndexOutOfBoundsException

- if start or start + count is
out of bounds
**Throws:** NullPointerException

- if text is null

- shape

```java
public void shape​(char[] text,
int start,
int count,
int context)
```

Converts the digits in the text that occur between start and
start + count, using the provided context.
Context is ignored if the shaper is not a contextual shaper.

**Parameters:** text

- an array of characters
**Parameters:** start

- the index into

text

to start
converting
**Parameters:** count

- the number of characters in

text

to convert
**Parameters:** context

- the context to which to convert the
characters, such as

NumericShaper.EUROPEAN
**Throws:** IndexOutOfBoundsException

- if start or start + count is
out of bounds
**Throws:** NullPointerException

- if text is null
**Throws:** IllegalArgumentException

- if this is a contextual shaper
and the specified

context

is not a single valid
range.

- shape

```java
public void shape​(char[] text,
int start,
int count,

NumericShaper.Range
context)
```

Converts the digits in the text that occur between

start

and

start + count

, using the provided

context

.

Context

is ignored if the shaper is not a
contextual shaper.

**Parameters:** text

- a

char

array
**Parameters:** start

- the index into

text

to start converting
**Parameters:** count

- the number of

char

s in

text

to convert
**Parameters:** context

- the context to which to convert the characters,
such as

NumericShaper.Range.EUROPEAN
**Throws:** IndexOutOfBoundsException

- if

start

or

start + count

is out of bounds
**Throws:** NullPointerException

- if

text

or

context

is null
**Since:** 1.7

- isContextual

```java
public boolean isContextual()
```

Returns a

boolean

indicating whether or not
this shaper shapes contextually.

**Returns:** true

if this shaper is contextual;

false

otherwise.

- getRanges

```java
public int getRanges()
```

Returns an

int

that ORs together the values for
all the ranges that will be shaped.

For example, to check if a shaper shapes to Arabic, you would use the
following:

if ((shaper.getRanges() & shaper.ARABIC) != 0) &#123; ...

Note that this method supports only the bit mask-based
ranges. Call

getRangeSet()

for the enum-based ranges.

**Returns:** the values for all the ranges to be shaped.

- getRangeSet

```java
public
Set
<
NumericShaper.Range
> getRangeSet()
```

Returns a

Set

representing all the Unicode ranges in
this

NumericShaper

that will be shaped.

**Returns:** all the Unicode ranges to be shaped.
**Since:** 1.7

- hashCode

```java
public int hashCode()
```

Returns a hash code for this shaper.

**Overrides:** hashCode

in class

Object
**Returns:** this shaper's hash code.
**See Also:** Object.hashCode()

- equals

```java
public boolean equals​(
Object
o)
```

Returns

true

if the specified object is an instance of

NumericShaper

and shapes identically to this one,
regardless of the range representations, the bit mask or the
enum. For example, the following code produces

"true"

.

```java
NumericShaper ns1 = NumericShaper.getShaper(NumericShaper.ARABIC);
NumericShaper ns2 = NumericShaper.getShaper(NumericShaper.Range.ARABIC);
System.out.println(ns1.equals(ns2));
```

**Overrides:** equals

in class

Object
**Parameters:** o

- the specified object to compare to this

NumericShaper
**Returns:** true

if

o

is an instance
of

NumericShaper

and shapes in the same way;

false

otherwise.
**See Also:** Object.equals(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a

String

that describes this shaper. This method
is used for debugging purposes only.

**Overrides:** toString

in class

Object
**Returns:** a

String

describing this shaper.

---

#### Method Detail

getShaper

```java
public static
NumericShaper
getShaper​(int singleRange)
```

Returns a shaper for the provided unicode range. All
Latin-1 (EUROPEAN) digits are converted
to the corresponding decimal unicode digits.

**Parameters:** singleRange

- the specified Unicode range
**Returns:** a non-contextual numeric shaper
**Throws:** IllegalArgumentException

- if the range is not a single range

---

#### getShaper

public static

NumericShaper

getShaper​(int singleRange)

Returns a shaper for the provided unicode range. All
Latin-1 (EUROPEAN) digits are converted
to the corresponding decimal unicode digits.

getShaper

```java
public static
NumericShaper
getShaper​(
NumericShaper.Range
singleRange)
```

Returns a shaper for the provided Unicode
range. All Latin-1 (EUROPEAN) digits are converted to the
corresponding decimal digits of the specified Unicode range.

**Parameters:** singleRange

- the Unicode range given by a

NumericShaper.Range

constant.
**Returns:** a non-contextual

NumericShaper

.
**Throws:** NullPointerException

- if

singleRange

is

null
**Since:** 1.7

---

#### getShaper

public static

NumericShaper

getShaper​(

NumericShaper.Range

singleRange)

Returns a shaper for the provided Unicode
range. All Latin-1 (EUROPEAN) digits are converted to the
corresponding decimal digits of the specified Unicode range.

getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(int ranges)
```

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits are converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, such as,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper assumes EUROPEAN as the starting context, that is, if
EUROPEAN digits are encountered before any strong directional
text in the string, the context is presumed to be EUROPEAN, and
so the digits will not shape.

**Parameters:** ranges

- the specified Unicode ranges
**Returns:** a shaper for the specified ranges

---

#### getContextualShaper

public static

NumericShaper

getContextualShaper​(int ranges)

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits are converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, such as,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper assumes EUROPEAN as the starting context, that is, if
EUROPEAN digits are encountered before any strong directional
text in the string, the context is presumed to be EUROPEAN, and
so the digits will not shape.

getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(
Set
<
NumericShaper.Range
> ranges)
```

Returns a contextual shaper for the provided Unicode
range(s). The Latin-1 (EUROPEAN) digits are converted to the
decimal digits corresponding to the range of the preceding
text, if the range is one of the provided ranges.

The shaper assumes EUROPEAN as the starting context, that
is, if EUROPEAN digits are encountered before any strong
directional text in the string, the context is presumed to be
EUROPEAN, and so the digits will not shape.

**Parameters:** ranges

- the specified Unicode ranges
**Returns:** a contextual shaper for the specified ranges
**Throws:** NullPointerException

- if

ranges

is

null

.
**Since:** 1.7

---

#### getContextualShaper

public static

NumericShaper

getContextualShaper​(

Set

<

NumericShaper.Range

> ranges)

Returns a contextual shaper for the provided Unicode
range(s). The Latin-1 (EUROPEAN) digits are converted to the
decimal digits corresponding to the range of the preceding
text, if the range is one of the provided ranges.

The shaper assumes EUROPEAN as the starting context, that
is, if EUROPEAN digits are encountered before any strong
directional text in the string, the context is presumed to be
EUROPEAN, and so the digits will not shape.

The shaper assumes EUROPEAN as the starting context, that
is, if EUROPEAN digits are encountered before any strong
directional text in the string, the context is presumed to be
EUROPEAN, and so the digits will not shape.

getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(int ranges,
int defaultContext)
```

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits will be converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, for example,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper uses defaultContext as the starting context.

**Parameters:** ranges

- the specified Unicode ranges
**Parameters:** defaultContext

- the starting context, such as

NumericShaper.EUROPEAN
**Returns:** a shaper for the specified Unicode ranges.
**Throws:** IllegalArgumentException

- if the specified

defaultContext

is not a single valid range.

---

#### getContextualShaper

public static

NumericShaper

getContextualShaper​(int ranges,
int defaultContext)

Returns a contextual shaper for the provided unicode range(s).
Latin-1 (EUROPEAN) digits will be converted to the decimal digits
corresponding to the range of the preceding text, if the
range is one of the provided ranges. Multiple ranges are
represented by or-ing the values together, for example,

NumericShaper.ARABIC | NumericShaper.THAI

. The
shaper uses defaultContext as the starting context.

getContextualShaper

```java
public static
NumericShaper
getContextualShaper​(
Set
<
NumericShaper.Range
> ranges,

NumericShaper.Range
defaultContext)
```

Returns a contextual shaper for the provided Unicode range(s).
The Latin-1 (EUROPEAN) digits will be converted to the decimal
digits corresponding to the range of the preceding text, if the
range is one of the provided ranges. The shaper uses

defaultContext

as the starting context.

**Parameters:** ranges

- the specified Unicode ranges
**Parameters:** defaultContext

- the starting context, such as

NumericShaper.Range.EUROPEAN
**Returns:** a contextual shaper for the specified Unicode ranges.
**Throws:** NullPointerException

- if

ranges

or

defaultContext

is

null
**Since:** 1.7

---

#### getContextualShaper

public static

NumericShaper

getContextualShaper​(

Set

<

NumericShaper.Range

> ranges,

NumericShaper.Range

defaultContext)

Returns a contextual shaper for the provided Unicode range(s).
The Latin-1 (EUROPEAN) digits will be converted to the decimal
digits corresponding to the range of the preceding text, if the
range is one of the provided ranges. The shaper uses

defaultContext

as the starting context.

shape

```java
public void shape​(char[] text,
int start,
int count)
```

Converts the digits in the text that occur between start and
start + count.

**Parameters:** text

- an array of characters to convert
**Parameters:** start

- the index into

text

to start
converting
**Parameters:** count

- the number of characters in

text

to convert
**Throws:** IndexOutOfBoundsException

- if start or start + count is
out of bounds
**Throws:** NullPointerException

- if text is null

---

#### shape

public void shape​(char[] text,
int start,
int count)

Converts the digits in the text that occur between start and
start + count.

shape

```java
public void shape​(char[] text,
int start,
int count,
int context)
```

Converts the digits in the text that occur between start and
start + count, using the provided context.
Context is ignored if the shaper is not a contextual shaper.

**Parameters:** text

- an array of characters
**Parameters:** start

- the index into

text

to start
converting
**Parameters:** count

- the number of characters in

text

to convert
**Parameters:** context

- the context to which to convert the
characters, such as

NumericShaper.EUROPEAN
**Throws:** IndexOutOfBoundsException

- if start or start + count is
out of bounds
**Throws:** NullPointerException

- if text is null
**Throws:** IllegalArgumentException

- if this is a contextual shaper
and the specified

context

is not a single valid
range.

---

#### shape

public void shape​(char[] text,
int start,
int count,
int context)

Converts the digits in the text that occur between start and
start + count, using the provided context.
Context is ignored if the shaper is not a contextual shaper.

shape

```java
public void shape​(char[] text,
int start,
int count,

NumericShaper.Range
context)
```

Converts the digits in the text that occur between

start

and

start + count

, using the provided

context

.

Context

is ignored if the shaper is not a
contextual shaper.

**Parameters:** text

- a

char

array
**Parameters:** start

- the index into

text

to start converting
**Parameters:** count

- the number of

char

s in

text

to convert
**Parameters:** context

- the context to which to convert the characters,
such as

NumericShaper.Range.EUROPEAN
**Throws:** IndexOutOfBoundsException

- if

start

or

start + count

is out of bounds
**Throws:** NullPointerException

- if

text

or

context

is null
**Since:** 1.7

---

#### shape

public void shape​(char[] text,
int start,
int count,

NumericShaper.Range

context)

Converts the digits in the text that occur between

start

and

start + count

, using the provided

context

.

Context

is ignored if the shaper is not a
contextual shaper.

isContextual

```java
public boolean isContextual()
```

Returns a

boolean

indicating whether or not
this shaper shapes contextually.

**Returns:** true

if this shaper is contextual;

false

otherwise.

---

#### isContextual

public boolean isContextual()

Returns a

boolean

indicating whether or not
this shaper shapes contextually.

getRanges

```java
public int getRanges()
```

Returns an

int

that ORs together the values for
all the ranges that will be shaped.

For example, to check if a shaper shapes to Arabic, you would use the
following:

if ((shaper.getRanges() & shaper.ARABIC) != 0) &#123; ...

Note that this method supports only the bit mask-based
ranges. Call

getRangeSet()

for the enum-based ranges.

**Returns:** the values for all the ranges to be shaped.

---

#### getRanges

public int getRanges()

Returns an

int

that ORs together the values for
all the ranges that will be shaped.

For example, to check if a shaper shapes to Arabic, you would use the
following:

if ((shaper.getRanges() & shaper.ARABIC) != 0) &#123; ...

Note that this method supports only the bit mask-based
ranges. Call

getRangeSet()

for the enum-based ranges.

For example, to check if a shaper shapes to Arabic, you would use the
following:

if ((shaper.getRanges() & shaper.ARABIC) != 0) &#123; ...

Note that this method supports only the bit mask-based
ranges. Call

getRangeSet()

for the enum-based ranges.

Note that this method supports only the bit mask-based
ranges. Call

getRangeSet()

for the enum-based ranges.

getRangeSet

```java
public
Set
<
NumericShaper.Range
> getRangeSet()
```

Returns a

Set

representing all the Unicode ranges in
this

NumericShaper

that will be shaped.

**Returns:** all the Unicode ranges to be shaped.
**Since:** 1.7

---

#### getRangeSet

public

Set

<

NumericShaper.Range

> getRangeSet()

Returns a

Set

representing all the Unicode ranges in
this

NumericShaper

that will be shaped.

hashCode

```java
public int hashCode()
```

Returns a hash code for this shaper.

**Overrides:** hashCode

in class

Object
**Returns:** this shaper's hash code.
**See Also:** Object.hashCode()

---

#### hashCode

public int hashCode()

Returns a hash code for this shaper.

equals

```java
public boolean equals​(
Object
o)
```

Returns

true

if the specified object is an instance of

NumericShaper

and shapes identically to this one,
regardless of the range representations, the bit mask or the
enum. For example, the following code produces

"true"

.

```java
NumericShaper ns1 = NumericShaper.getShaper(NumericShaper.ARABIC);
NumericShaper ns2 = NumericShaper.getShaper(NumericShaper.Range.ARABIC);
System.out.println(ns1.equals(ns2));
```

**Overrides:** equals

in class

Object
**Parameters:** o

- the specified object to compare to this

NumericShaper
**Returns:** true

if

o

is an instance
of

NumericShaper

and shapes in the same way;

false

otherwise.
**See Also:** Object.equals(java.lang.Object)

---

#### equals

public boolean equals​(

Object

o)

Returns

true

if the specified object is an instance of

NumericShaper

and shapes identically to this one,
regardless of the range representations, the bit mask or the
enum. For example, the following code produces

"true"

.

```java
NumericShaper ns1 = NumericShaper.getShaper(NumericShaper.ARABIC);
NumericShaper ns2 = NumericShaper.getShaper(NumericShaper.Range.ARABIC);
System.out.println(ns1.equals(ns2));
```

NumericShaper ns1 = NumericShaper.getShaper(NumericShaper.ARABIC);
NumericShaper ns2 = NumericShaper.getShaper(NumericShaper.Range.ARABIC);
System.out.println(ns1.equals(ns2));

toString

```java
public
String
toString()
```

Returns a

String

that describes this shaper. This method
is used for debugging purposes only.

**Overrides:** toString

in class

Object
**Returns:** a

String

describing this shaper.

---

#### toString

public

String

toString()

Returns a

String

that describes this shaper. This method
is used for debugging purposes only.

---

