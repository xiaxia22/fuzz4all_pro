# Class LineMetrics

**Source:** `java.desktop\java\awt\font\LineMetrics.html`

### Class Description

```java
public abstract class
LineMetrics

extends
Object
```

The

LineMetrics

class allows access to the
metrics needed to layout characters along a line
and to layout of a set of lines. A

LineMetrics

object encapsulates the measurement information associated
with a run of text.

Fonts can have different metrics for different ranges of
characters. The

getLineMetrics

methods of

Font

take some text as an argument
and return a

LineMetrics

object describing the
metrics of the initial number of characters in that text, as
returned by

getNumChars()

.

---

### Field Details

*No entries found.*

### Constructor Details

#### public LineMetrics()

*No description found.*

---

### Method Details

#### public abstract int getNumChars()

Returns the number of characters (

char

values) in the text whose
metrics are encapsulated by this

LineMetrics

object.

**Returns:**
- the number of characters (

char

values) in the text with which
this

LineMetrics

was created.

---

#### public abstract float getAscent()

Returns the ascent of the text. The ascent
is the distance from the baseline
to the ascender line. The ascent usually represents the
the height of the capital letters of the text. Some characters
can extend above the ascender line.

**Returns:**
- the ascent of the text.

---

#### public abstract float getDescent()

Returns the descent of the text. The descent
is the distance from the baseline
to the descender line. The descent usually represents
the distance to the bottom of lower case letters like
'p'. Some characters can extend below the descender
line.

**Returns:**
- the descent of the text.

---

#### public abstract float getLeading()

Returns the leading of the text. The
leading is the recommended
distance from the bottom of the descender line to the
top of the next line.

**Returns:**
- the leading of the text.

---

#### public abstract float getHeight()

Returns the height of the text. The
height is equal to the sum of the ascent, the
descent and the leading.

**Returns:**
- the height of the text.

---

#### public abstract int getBaselineIndex()

Returns the baseline index of the text.
The index is one of

ROMAN_BASELINE

,

CENTER_BASELINE

,

HANGING_BASELINE

.

**Returns:**
- the baseline of the text.

---

#### public abstract float[] getBaselineOffsets()

Returns the baseline offsets of the text,
relative to the baseline of the text. The
offsets are indexed by baseline index. For
example, if the baseline index is

CENTER_BASELINE

then

offsets[HANGING_BASELINE]

is usually
negative,

offsets[CENTER_BASELINE]

is zero, and

offsets[ROMAN_BASELINE]

is usually positive.

**Returns:**
- the baseline offsets of the text.

---

#### public abstract float getStrikethroughOffset()

Returns the position of the strike-through line
relative to the baseline.

**Returns:**
- the position of the strike-through line.

---

#### public abstract float getStrikethroughThickness()

Returns the thickness of the strike-through line.

**Returns:**
- the thickness of the strike-through line.

---

#### public abstract float getUnderlineOffset()

Returns the position of the underline relative to
the baseline.

**Returns:**
- the position of the underline.

---

#### public abstract float getUnderlineThickness()

Returns the thickness of the underline.

**Returns:**
- the thickness of the underline.

---

### Additional Sections

#### Class LineMetrics

java.lang.Object

- java.awt.font.LineMetrics

java.awt.font.LineMetrics

```java
public abstract class
LineMetrics

extends
Object
```

The

LineMetrics

class allows access to the
metrics needed to layout characters along a line
and to layout of a set of lines. A

LineMetrics

object encapsulates the measurement information associated
with a run of text.

Fonts can have different metrics for different ranges of
characters. The

getLineMetrics

methods of

Font

take some text as an argument
and return a

LineMetrics

object describing the
metrics of the initial number of characters in that text, as
returned by

getNumChars()

.

public abstract class

LineMetrics

extends

Object

The

LineMetrics

class allows access to the
metrics needed to layout characters along a line
and to layout of a set of lines. A

LineMetrics

object encapsulates the measurement information associated
with a run of text.

Fonts can have different metrics for different ranges of
characters. The

getLineMetrics

methods of

Font

take some text as an argument
and return a

LineMetrics

object describing the
metrics of the initial number of characters in that text, as
returned by

getNumChars()

.

Fonts can have different metrics for different ranges of
characters. The

getLineMetrics

methods of

Font

take some text as an argument
and return a

LineMetrics

object describing the
metrics of the initial number of characters in that text, as
returned by

getNumChars()

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LineMetrics

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract float

getAscent

()

Returns the ascent of the text.

abstract int

getBaselineIndex

()

Returns the baseline index of the text.

abstract float[]

getBaselineOffsets

()

Returns the baseline offsets of the text,
relative to the baseline of the text.

abstract float

getDescent

()

Returns the descent of the text.

abstract float

getHeight

()

Returns the height of the text.

abstract float

getLeading

()

Returns the leading of the text.

abstract int

getNumChars

()

Returns the number of characters (

char

values) in the text whose
metrics are encapsulated by this

LineMetrics

object.

abstract float

getStrikethroughOffset

()

Returns the position of the strike-through line
relative to the baseline.

abstract float

getStrikethroughThickness

()

Returns the thickness of the strike-through line.

abstract float

getUnderlineOffset

()

Returns the position of the underline relative to
the baseline.

abstract float

getUnderlineThickness

()

Returns the thickness of the underline.

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

LineMetrics

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

abstract float

getAscent

()

Returns the ascent of the text.

abstract int

getBaselineIndex

()

Returns the baseline index of the text.

abstract float[]

getBaselineOffsets

()

Returns the baseline offsets of the text,
relative to the baseline of the text.

abstract float

getDescent

()

Returns the descent of the text.

abstract float

getHeight

()

Returns the height of the text.

abstract float

getLeading

()

Returns the leading of the text.

abstract int

getNumChars

()

Returns the number of characters (

char

values) in the text whose
metrics are encapsulated by this

LineMetrics

object.

abstract float

getStrikethroughOffset

()

Returns the position of the strike-through line
relative to the baseline.

abstract float

getStrikethroughThickness

()

Returns the thickness of the strike-through line.

abstract float

getUnderlineOffset

()

Returns the position of the underline relative to
the baseline.

abstract float

getUnderlineThickness

()

Returns the thickness of the underline.

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

Returns the ascent of the text.

Returns the baseline index of the text.

Returns the baseline offsets of the text,
relative to the baseline of the text.

Returns the descent of the text.

Returns the height of the text.

Returns the leading of the text.

Returns the number of characters (

char

values) in the text whose
metrics are encapsulated by this

LineMetrics

object.

Returns the position of the strike-through line
relative to the baseline.

Returns the thickness of the strike-through line.

Returns the position of the underline relative to
the baseline.

Returns the thickness of the underline.

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

- LineMetrics

```java
public LineMetrics()
```

============ METHOD DETAIL ==========

- Method Detail

- getNumChars

```java
public abstract int getNumChars()
```

Returns the number of characters (

char

values) in the text whose
metrics are encapsulated by this

LineMetrics

object.

**Returns:** the number of characters (

char

values) in the text with which
this

LineMetrics

was created.

- getAscent

```java
public abstract float getAscent()
```

Returns the ascent of the text. The ascent
is the distance from the baseline
to the ascender line. The ascent usually represents the
the height of the capital letters of the text. Some characters
can extend above the ascender line.

**Returns:** the ascent of the text.

- getDescent

```java
public abstract float getDescent()
```

Returns the descent of the text. The descent
is the distance from the baseline
to the descender line. The descent usually represents
the distance to the bottom of lower case letters like
'p'. Some characters can extend below the descender
line.

**Returns:** the descent of the text.

- getLeading

```java
public abstract float getLeading()
```

Returns the leading of the text. The
leading is the recommended
distance from the bottom of the descender line to the
top of the next line.

**Returns:** the leading of the text.

- getHeight

```java
public abstract float getHeight()
```

Returns the height of the text. The
height is equal to the sum of the ascent, the
descent and the leading.

**Returns:** the height of the text.

- getBaselineIndex

```java
public abstract int getBaselineIndex()
```

Returns the baseline index of the text.
The index is one of

ROMAN_BASELINE

,

CENTER_BASELINE

,

HANGING_BASELINE

.

**Returns:** the baseline of the text.

- getBaselineOffsets

```java
public abstract float[] getBaselineOffsets()
```

Returns the baseline offsets of the text,
relative to the baseline of the text. The
offsets are indexed by baseline index. For
example, if the baseline index is

CENTER_BASELINE

then

offsets[HANGING_BASELINE]

is usually
negative,

offsets[CENTER_BASELINE]

is zero, and

offsets[ROMAN_BASELINE]

is usually positive.

**Returns:** the baseline offsets of the text.

- getStrikethroughOffset

```java
public abstract float getStrikethroughOffset()
```

Returns the position of the strike-through line
relative to the baseline.

**Returns:** the position of the strike-through line.

- getStrikethroughThickness

```java
public abstract float getStrikethroughThickness()
```

Returns the thickness of the strike-through line.

**Returns:** the thickness of the strike-through line.

- getUnderlineOffset

```java
public abstract float getUnderlineOffset()
```

Returns the position of the underline relative to
the baseline.

**Returns:** the position of the underline.

- getUnderlineThickness

```java
public abstract float getUnderlineThickness()
```

Returns the thickness of the underline.

**Returns:** the thickness of the underline.

Constructor Detail

- LineMetrics

```java
public LineMetrics()
```

---

#### Constructor Detail

LineMetrics

```java
public LineMetrics()
```

---

#### LineMetrics

public LineMetrics()

Method Detail

- getNumChars

```java
public abstract int getNumChars()
```

Returns the number of characters (

char

values) in the text whose
metrics are encapsulated by this

LineMetrics

object.

**Returns:** the number of characters (

char

values) in the text with which
this

LineMetrics

was created.

- getAscent

```java
public abstract float getAscent()
```

Returns the ascent of the text. The ascent
is the distance from the baseline
to the ascender line. The ascent usually represents the
the height of the capital letters of the text. Some characters
can extend above the ascender line.

**Returns:** the ascent of the text.

- getDescent

```java
public abstract float getDescent()
```

Returns the descent of the text. The descent
is the distance from the baseline
to the descender line. The descent usually represents
the distance to the bottom of lower case letters like
'p'. Some characters can extend below the descender
line.

**Returns:** the descent of the text.

- getLeading

```java
public abstract float getLeading()
```

Returns the leading of the text. The
leading is the recommended
distance from the bottom of the descender line to the
top of the next line.

**Returns:** the leading of the text.

- getHeight

```java
public abstract float getHeight()
```

Returns the height of the text. The
height is equal to the sum of the ascent, the
descent and the leading.

**Returns:** the height of the text.

- getBaselineIndex

```java
public abstract int getBaselineIndex()
```

Returns the baseline index of the text.
The index is one of

ROMAN_BASELINE

,

CENTER_BASELINE

,

HANGING_BASELINE

.

**Returns:** the baseline of the text.

- getBaselineOffsets

```java
public abstract float[] getBaselineOffsets()
```

Returns the baseline offsets of the text,
relative to the baseline of the text. The
offsets are indexed by baseline index. For
example, if the baseline index is

CENTER_BASELINE

then

offsets[HANGING_BASELINE]

is usually
negative,

offsets[CENTER_BASELINE]

is zero, and

offsets[ROMAN_BASELINE]

is usually positive.

**Returns:** the baseline offsets of the text.

- getStrikethroughOffset

```java
public abstract float getStrikethroughOffset()
```

Returns the position of the strike-through line
relative to the baseline.

**Returns:** the position of the strike-through line.

- getStrikethroughThickness

```java
public abstract float getStrikethroughThickness()
```

Returns the thickness of the strike-through line.

**Returns:** the thickness of the strike-through line.

- getUnderlineOffset

```java
public abstract float getUnderlineOffset()
```

Returns the position of the underline relative to
the baseline.

**Returns:** the position of the underline.

- getUnderlineThickness

```java
public abstract float getUnderlineThickness()
```

Returns the thickness of the underline.

**Returns:** the thickness of the underline.

---

#### Method Detail

getNumChars

```java
public abstract int getNumChars()
```

Returns the number of characters (

char

values) in the text whose
metrics are encapsulated by this

LineMetrics

object.

**Returns:** the number of characters (

char

values) in the text with which
this

LineMetrics

was created.

---

#### getNumChars

public abstract int getNumChars()

Returns the number of characters (

char

values) in the text whose
metrics are encapsulated by this

LineMetrics

object.

getAscent

```java
public abstract float getAscent()
```

Returns the ascent of the text. The ascent
is the distance from the baseline
to the ascender line. The ascent usually represents the
the height of the capital letters of the text. Some characters
can extend above the ascender line.

**Returns:** the ascent of the text.

---

#### getAscent

public abstract float getAscent()

Returns the ascent of the text. The ascent
is the distance from the baseline
to the ascender line. The ascent usually represents the
the height of the capital letters of the text. Some characters
can extend above the ascender line.

getDescent

```java
public abstract float getDescent()
```

Returns the descent of the text. The descent
is the distance from the baseline
to the descender line. The descent usually represents
the distance to the bottom of lower case letters like
'p'. Some characters can extend below the descender
line.

**Returns:** the descent of the text.

---

#### getDescent

public abstract float getDescent()

Returns the descent of the text. The descent
is the distance from the baseline
to the descender line. The descent usually represents
the distance to the bottom of lower case letters like
'p'. Some characters can extend below the descender
line.

getLeading

```java
public abstract float getLeading()
```

Returns the leading of the text. The
leading is the recommended
distance from the bottom of the descender line to the
top of the next line.

**Returns:** the leading of the text.

---

#### getLeading

public abstract float getLeading()

Returns the leading of the text. The
leading is the recommended
distance from the bottom of the descender line to the
top of the next line.

getHeight

```java
public abstract float getHeight()
```

Returns the height of the text. The
height is equal to the sum of the ascent, the
descent and the leading.

**Returns:** the height of the text.

---

#### getHeight

public abstract float getHeight()

Returns the height of the text. The
height is equal to the sum of the ascent, the
descent and the leading.

getBaselineIndex

```java
public abstract int getBaselineIndex()
```

Returns the baseline index of the text.
The index is one of

ROMAN_BASELINE

,

CENTER_BASELINE

,

HANGING_BASELINE

.

**Returns:** the baseline of the text.

---

#### getBaselineIndex

public abstract int getBaselineIndex()

Returns the baseline index of the text.
The index is one of

ROMAN_BASELINE

,

CENTER_BASELINE

,

HANGING_BASELINE

.

getBaselineOffsets

```java
public abstract float[] getBaselineOffsets()
```

Returns the baseline offsets of the text,
relative to the baseline of the text. The
offsets are indexed by baseline index. For
example, if the baseline index is

CENTER_BASELINE

then

offsets[HANGING_BASELINE]

is usually
negative,

offsets[CENTER_BASELINE]

is zero, and

offsets[ROMAN_BASELINE]

is usually positive.

**Returns:** the baseline offsets of the text.

---

#### getBaselineOffsets

public abstract float[] getBaselineOffsets()

Returns the baseline offsets of the text,
relative to the baseline of the text. The
offsets are indexed by baseline index. For
example, if the baseline index is

CENTER_BASELINE

then

offsets[HANGING_BASELINE]

is usually
negative,

offsets[CENTER_BASELINE]

is zero, and

offsets[ROMAN_BASELINE]

is usually positive.

getStrikethroughOffset

```java
public abstract float getStrikethroughOffset()
```

Returns the position of the strike-through line
relative to the baseline.

**Returns:** the position of the strike-through line.

---

#### getStrikethroughOffset

public abstract float getStrikethroughOffset()

Returns the position of the strike-through line
relative to the baseline.

getStrikethroughThickness

```java
public abstract float getStrikethroughThickness()
```

Returns the thickness of the strike-through line.

**Returns:** the thickness of the strike-through line.

---

#### getStrikethroughThickness

public abstract float getStrikethroughThickness()

Returns the thickness of the strike-through line.

getUnderlineOffset

```java
public abstract float getUnderlineOffset()
```

Returns the position of the underline relative to
the baseline.

**Returns:** the position of the underline.

---

#### getUnderlineOffset

public abstract float getUnderlineOffset()

Returns the position of the underline relative to
the baseline.

getUnderlineThickness

```java
public abstract float getUnderlineThickness()
```

Returns the thickness of the underline.

**Returns:** the thickness of the underline.

---

#### getUnderlineThickness

public abstract float getUnderlineThickness()

Returns the thickness of the underline.

---

