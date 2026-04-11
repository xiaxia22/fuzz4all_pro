# Class GlyphJustificationInfo

**Source:** `java.desktop\java\awt\font\GlyphJustificationInfo.html`

### Class Description

```java
public final class
GlyphJustificationInfo

extends
Object
```

The

GlyphJustificationInfo

class represents information
about the justification properties of a glyph. A glyph is the visual
representation of one or more characters. Many different glyphs can
be used to represent a single character or combination of characters.
The four justification properties represented by

GlyphJustificationInfo

are weight, priority, absorb and
limit.

Weight is the overall 'weight' of the glyph in the line. Generally it is
proportional to the size of the font. Glyphs with larger weight are
allocated a correspondingly larger amount of the change in space.

Priority determines the justification phase in which this glyph is used.
All glyphs of the same priority are examined before glyphs of the next
priority. If all the change in space can be allocated to these glyphs
without exceeding their limits, then glyphs of the next priority are not
examined. There are four priorities, kashida, whitespace, interchar,
and none. KASHIDA is the first priority examined. NONE is the last
priority examined.

Absorb determines whether a glyph absorbs all change in space. Within a
given priority, some glyphs may absorb all the change in space. If any of
these glyphs are present, no glyphs of later priority are examined.

Limit determines the maximum or minimum amount by which the glyph can
change. Left and right sides of the glyph can have different limits.

Each

GlyphJustificationInfo

represents two sets of
metrics, which are

growing

and

shrinking

. Growing
metrics are used when the glyphs on a line are to be
spread apart to fit a larger width. Shrinking metrics are used when
the glyphs are to be moved together to fit a smaller width.

---

### Field Details

#### public static final int PRIORITY_KASHIDA

The highest justification priority.

**See Also:**
- Constant Field Values

---

#### public static final int PRIORITY_WHITESPACE

The second highest justification priority.

**See Also:**
- Constant Field Values

---

#### public static final int PRIORITY_INTERCHAR

The second lowest justification priority.

**See Also:**
- Constant Field Values

---

#### public static final int PRIORITY_NONE

The lowest justification priority.

**See Also:**
- Constant Field Values

---

#### public final float weight

The weight of this glyph.

---

#### public final int growPriority

The priority level of this glyph as it is growing.

---

#### public final boolean growAbsorb

If

true

, this glyph absorbs all extra
space at this and lower priority levels when it grows.

---

#### public final float growLeftLimit

The maximum amount by which the left side of this glyph can grow.

---

#### public final float growRightLimit

The maximum amount by which the right side of this glyph can grow.

---

#### public final int shrinkPriority

The priority level of this glyph as it is shrinking.

---

#### public final boolean shrinkAbsorb

If

true

,this glyph absorbs all remaining shrinkage at
this and lower priority levels as it shrinks.

---

#### public final float shrinkLeftLimit

The maximum amount by which the left side of this glyph can shrink
(a positive number).

---

#### public final float shrinkRightLimit

The maximum amount by which the right side of this glyph can shrink
(a positive number).

---

### Constructor Details

#### public GlyphJustificationInfo​(float weight,
boolean growAbsorb,
int growPriority,
float growLeftLimit,
float growRightLimit,
boolean shrinkAbsorb,
int shrinkPriority,
float shrinkLeftLimit,
float shrinkRightLimit)

Constructs information about the justification properties of a
glyph.

**Parameters:**
- weight

- the weight of this glyph when allocating space. Must be non-negative.
- growAbsorb

- if

true

this glyph absorbs
all extra space at this priority and lower priority levels when it
grows
- growPriority

- the priority level of this glyph when it
grows
- growLeftLimit

- the maximum amount by which the left side of this
glyph can grow. Must be non-negative.
- growRightLimit

- the maximum amount by which the right side of this
glyph can grow. Must be non-negative.
- shrinkAbsorb

- if

true

, this glyph absorbs all
remaining shrinkage at this and lower priority levels when it
shrinks
- shrinkPriority

- the priority level of this glyph when
it shrinks
- shrinkLeftLimit

- the maximum amount by which the left side of this
glyph can shrink. Must be non-negative.
- shrinkRightLimit

- the maximum amount by which the right side
of this glyph can shrink. Must be non-negative.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class GlyphJustificationInfo

java.lang.Object

- java.awt.font.GlyphJustificationInfo

java.awt.font.GlyphJustificationInfo

```java
public final class
GlyphJustificationInfo

extends
Object
```

The

GlyphJustificationInfo

class represents information
about the justification properties of a glyph. A glyph is the visual
representation of one or more characters. Many different glyphs can
be used to represent a single character or combination of characters.
The four justification properties represented by

GlyphJustificationInfo

are weight, priority, absorb and
limit.

Weight is the overall 'weight' of the glyph in the line. Generally it is
proportional to the size of the font. Glyphs with larger weight are
allocated a correspondingly larger amount of the change in space.

Priority determines the justification phase in which this glyph is used.
All glyphs of the same priority are examined before glyphs of the next
priority. If all the change in space can be allocated to these glyphs
without exceeding their limits, then glyphs of the next priority are not
examined. There are four priorities, kashida, whitespace, interchar,
and none. KASHIDA is the first priority examined. NONE is the last
priority examined.

Absorb determines whether a glyph absorbs all change in space. Within a
given priority, some glyphs may absorb all the change in space. If any of
these glyphs are present, no glyphs of later priority are examined.

Limit determines the maximum or minimum amount by which the glyph can
change. Left and right sides of the glyph can have different limits.

Each

GlyphJustificationInfo

represents two sets of
metrics, which are

growing

and

shrinking

. Growing
metrics are used when the glyphs on a line are to be
spread apart to fit a larger width. Shrinking metrics are used when
the glyphs are to be moved together to fit a smaller width.

public final class

GlyphJustificationInfo

extends

Object

The

GlyphJustificationInfo

class represents information
about the justification properties of a glyph. A glyph is the visual
representation of one or more characters. Many different glyphs can
be used to represent a single character or combination of characters.
The four justification properties represented by

GlyphJustificationInfo

are weight, priority, absorb and
limit.

Weight is the overall 'weight' of the glyph in the line. Generally it is
proportional to the size of the font. Glyphs with larger weight are
allocated a correspondingly larger amount of the change in space.

Priority determines the justification phase in which this glyph is used.
All glyphs of the same priority are examined before glyphs of the next
priority. If all the change in space can be allocated to these glyphs
without exceeding their limits, then glyphs of the next priority are not
examined. There are four priorities, kashida, whitespace, interchar,
and none. KASHIDA is the first priority examined. NONE is the last
priority examined.

Absorb determines whether a glyph absorbs all change in space. Within a
given priority, some glyphs may absorb all the change in space. If any of
these glyphs are present, no glyphs of later priority are examined.

Limit determines the maximum or minimum amount by which the glyph can
change. Left and right sides of the glyph can have different limits.

Each

GlyphJustificationInfo

represents two sets of
metrics, which are

growing

and

shrinking

. Growing
metrics are used when the glyphs on a line are to be
spread apart to fit a larger width. Shrinking metrics are used when
the glyphs are to be moved together to fit a smaller width.

Weight is the overall 'weight' of the glyph in the line. Generally it is
proportional to the size of the font. Glyphs with larger weight are
allocated a correspondingly larger amount of the change in space.

Priority determines the justification phase in which this glyph is used.
All glyphs of the same priority are examined before glyphs of the next
priority. If all the change in space can be allocated to these glyphs
without exceeding their limits, then glyphs of the next priority are not
examined. There are four priorities, kashida, whitespace, interchar,
and none. KASHIDA is the first priority examined. NONE is the last
priority examined.

Absorb determines whether a glyph absorbs all change in space. Within a
given priority, some glyphs may absorb all the change in space. If any of
these glyphs are present, no glyphs of later priority are examined.

Limit determines the maximum or minimum amount by which the glyph can
change. Left and right sides of the glyph can have different limits.

Each

GlyphJustificationInfo

represents two sets of
metrics, which are

growing

and

shrinking

. Growing
metrics are used when the glyphs on a line are to be
spread apart to fit a larger width. Shrinking metrics are used when
the glyphs are to be moved together to fit a smaller width.

Priority determines the justification phase in which this glyph is used.
All glyphs of the same priority are examined before glyphs of the next
priority. If all the change in space can be allocated to these glyphs
without exceeding their limits, then glyphs of the next priority are not
examined. There are four priorities, kashida, whitespace, interchar,
and none. KASHIDA is the first priority examined. NONE is the last
priority examined.

Absorb determines whether a glyph absorbs all change in space. Within a
given priority, some glyphs may absorb all the change in space. If any of
these glyphs are present, no glyphs of later priority are examined.

Limit determines the maximum or minimum amount by which the glyph can
change. Left and right sides of the glyph can have different limits.

Each

GlyphJustificationInfo

represents two sets of
metrics, which are

growing

and

shrinking

. Growing
metrics are used when the glyphs on a line are to be
spread apart to fit a larger width. Shrinking metrics are used when
the glyphs are to be moved together to fit a smaller width.

Absorb determines whether a glyph absorbs all change in space. Within a
given priority, some glyphs may absorb all the change in space. If any of
these glyphs are present, no glyphs of later priority are examined.

Limit determines the maximum or minimum amount by which the glyph can
change. Left and right sides of the glyph can have different limits.

Each

GlyphJustificationInfo

represents two sets of
metrics, which are

growing

and

shrinking

. Growing
metrics are used when the glyphs on a line are to be
spread apart to fit a larger width. Shrinking metrics are used when
the glyphs are to be moved together to fit a smaller width.

Limit determines the maximum or minimum amount by which the glyph can
change. Left and right sides of the glyph can have different limits.

Each

GlyphJustificationInfo

represents two sets of
metrics, which are

growing

and

shrinking

. Growing
metrics are used when the glyphs on a line are to be
spread apart to fit a larger width. Shrinking metrics are used when
the glyphs are to be moved together to fit a smaller width.

Each

GlyphJustificationInfo

represents two sets of
metrics, which are

growing

and

shrinking

. Growing
metrics are used when the glyphs on a line are to be
spread apart to fit a larger width. Shrinking metrics are used when
the glyphs are to be moved together to fit a smaller width.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

boolean

growAbsorb

If

true

, this glyph absorbs all extra
space at this and lower priority levels when it grows.

float

growLeftLimit

The maximum amount by which the left side of this glyph can grow.

int

growPriority

The priority level of this glyph as it is growing.

float

growRightLimit

The maximum amount by which the right side of this glyph can grow.

static int

PRIORITY_INTERCHAR

The second lowest justification priority.

static int

PRIORITY_KASHIDA

The highest justification priority.

static int

PRIORITY_NONE

The lowest justification priority.

static int

PRIORITY_WHITESPACE

The second highest justification priority.

boolean

shrinkAbsorb

If

true

,this glyph absorbs all remaining shrinkage at
this and lower priority levels as it shrinks.

float

shrinkLeftLimit

The maximum amount by which the left side of this glyph can shrink
(a positive number).

int

shrinkPriority

The priority level of this glyph as it is shrinking.

float

shrinkRightLimit

The maximum amount by which the right side of this glyph can shrink
(a positive number).

float

weight

The weight of this glyph.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GlyphJustificationInfo

​(float weight,
boolean growAbsorb,
int growPriority,
float growLeftLimit,
float growRightLimit,
boolean shrinkAbsorb,
int shrinkPriority,
float shrinkLeftLimit,
float shrinkRightLimit)

Constructs information about the justification properties of a
glyph.

========== METHOD SUMMARY ===========

- Method Summary

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

boolean

growAbsorb

If

true

, this glyph absorbs all extra
space at this and lower priority levels when it grows.

float

growLeftLimit

The maximum amount by which the left side of this glyph can grow.

int

growPriority

The priority level of this glyph as it is growing.

float

growRightLimit

The maximum amount by which the right side of this glyph can grow.

static int

PRIORITY_INTERCHAR

The second lowest justification priority.

static int

PRIORITY_KASHIDA

The highest justification priority.

static int

PRIORITY_NONE

The lowest justification priority.

static int

PRIORITY_WHITESPACE

The second highest justification priority.

boolean

shrinkAbsorb

If

true

,this glyph absorbs all remaining shrinkage at
this and lower priority levels as it shrinks.

float

shrinkLeftLimit

The maximum amount by which the left side of this glyph can shrink
(a positive number).

int

shrinkPriority

The priority level of this glyph as it is shrinking.

float

shrinkRightLimit

The maximum amount by which the right side of this glyph can shrink
(a positive number).

float

weight

The weight of this glyph.

---

#### Field Summary

If

true

, this glyph absorbs all extra
space at this and lower priority levels when it grows.

The maximum amount by which the left side of this glyph can grow.

The priority level of this glyph as it is growing.

The maximum amount by which the right side of this glyph can grow.

The second lowest justification priority.

The highest justification priority.

The lowest justification priority.

The second highest justification priority.

If

true

,this glyph absorbs all remaining shrinkage at
this and lower priority levels as it shrinks.

The maximum amount by which the left side of this glyph can shrink
(a positive number).

The priority level of this glyph as it is shrinking.

The maximum amount by which the right side of this glyph can shrink
(a positive number).

The weight of this glyph.

Constructor Summary

Constructors

Constructor

Description

GlyphJustificationInfo

​(float weight,
boolean growAbsorb,
int growPriority,
float growLeftLimit,
float growRightLimit,
boolean shrinkAbsorb,
int shrinkPriority,
float shrinkLeftLimit,
float shrinkRightLimit)

Constructs information about the justification properties of a
glyph.

---

#### Constructor Summary

Constructs information about the justification properties of a
glyph.

Method Summary

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

- PRIORITY_KASHIDA

```java
public static final int PRIORITY_KASHIDA
```

The highest justification priority.

**See Also:** Constant Field Values

- PRIORITY_WHITESPACE

```java
public static final int PRIORITY_WHITESPACE
```

The second highest justification priority.

**See Also:** Constant Field Values

- PRIORITY_INTERCHAR

```java
public static final int PRIORITY_INTERCHAR
```

The second lowest justification priority.

**See Also:** Constant Field Values

- PRIORITY_NONE

```java
public static final int PRIORITY_NONE
```

The lowest justification priority.

**See Also:** Constant Field Values

- weight

```java
public final float weight
```

The weight of this glyph.

- growPriority

```java
public final int growPriority
```

The priority level of this glyph as it is growing.

- growAbsorb

```java
public final boolean growAbsorb
```

If

true

, this glyph absorbs all extra
space at this and lower priority levels when it grows.

- growLeftLimit

```java
public final float growLeftLimit
```

The maximum amount by which the left side of this glyph can grow.

- growRightLimit

```java
public final float growRightLimit
```

The maximum amount by which the right side of this glyph can grow.

- shrinkPriority

```java
public final int shrinkPriority
```

The priority level of this glyph as it is shrinking.

- shrinkAbsorb

```java
public final boolean shrinkAbsorb
```

If

true

,this glyph absorbs all remaining shrinkage at
this and lower priority levels as it shrinks.

- shrinkLeftLimit

```java
public final float shrinkLeftLimit
```

The maximum amount by which the left side of this glyph can shrink
(a positive number).

- shrinkRightLimit

```java
public final float shrinkRightLimit
```

The maximum amount by which the right side of this glyph can shrink
(a positive number).

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GlyphJustificationInfo

```java
public GlyphJustificationInfo​(float weight,
boolean growAbsorb,
int growPriority,
float growLeftLimit,
float growRightLimit,
boolean shrinkAbsorb,
int shrinkPriority,
float shrinkLeftLimit,
float shrinkRightLimit)
```

Constructs information about the justification properties of a
glyph.

**Parameters:** weight

- the weight of this glyph when allocating space. Must be non-negative.
**Parameters:** growAbsorb

- if

true

this glyph absorbs
all extra space at this priority and lower priority levels when it
grows
**Parameters:** growPriority

- the priority level of this glyph when it
grows
**Parameters:** growLeftLimit

- the maximum amount by which the left side of this
glyph can grow. Must be non-negative.
**Parameters:** growRightLimit

- the maximum amount by which the right side of this
glyph can grow. Must be non-negative.
**Parameters:** shrinkAbsorb

- if

true

, this glyph absorbs all
remaining shrinkage at this and lower priority levels when it
shrinks
**Parameters:** shrinkPriority

- the priority level of this glyph when
it shrinks
**Parameters:** shrinkLeftLimit

- the maximum amount by which the left side of this
glyph can shrink. Must be non-negative.
**Parameters:** shrinkRightLimit

- the maximum amount by which the right side
of this glyph can shrink. Must be non-negative.

Field Detail

- PRIORITY_KASHIDA

```java
public static final int PRIORITY_KASHIDA
```

The highest justification priority.

**See Also:** Constant Field Values

- PRIORITY_WHITESPACE

```java
public static final int PRIORITY_WHITESPACE
```

The second highest justification priority.

**See Also:** Constant Field Values

- PRIORITY_INTERCHAR

```java
public static final int PRIORITY_INTERCHAR
```

The second lowest justification priority.

**See Also:** Constant Field Values

- PRIORITY_NONE

```java
public static final int PRIORITY_NONE
```

The lowest justification priority.

**See Also:** Constant Field Values

- weight

```java
public final float weight
```

The weight of this glyph.

- growPriority

```java
public final int growPriority
```

The priority level of this glyph as it is growing.

- growAbsorb

```java
public final boolean growAbsorb
```

If

true

, this glyph absorbs all extra
space at this and lower priority levels when it grows.

- growLeftLimit

```java
public final float growLeftLimit
```

The maximum amount by which the left side of this glyph can grow.

- growRightLimit

```java
public final float growRightLimit
```

The maximum amount by which the right side of this glyph can grow.

- shrinkPriority

```java
public final int shrinkPriority
```

The priority level of this glyph as it is shrinking.

- shrinkAbsorb

```java
public final boolean shrinkAbsorb
```

If

true

,this glyph absorbs all remaining shrinkage at
this and lower priority levels as it shrinks.

- shrinkLeftLimit

```java
public final float shrinkLeftLimit
```

The maximum amount by which the left side of this glyph can shrink
(a positive number).

- shrinkRightLimit

```java
public final float shrinkRightLimit
```

The maximum amount by which the right side of this glyph can shrink
(a positive number).

---

#### Field Detail

PRIORITY_KASHIDA

```java
public static final int PRIORITY_KASHIDA
```

The highest justification priority.

**See Also:** Constant Field Values

---

#### PRIORITY_KASHIDA

public static final int PRIORITY_KASHIDA

The highest justification priority.

PRIORITY_WHITESPACE

```java
public static final int PRIORITY_WHITESPACE
```

The second highest justification priority.

**See Also:** Constant Field Values

---

#### PRIORITY_WHITESPACE

public static final int PRIORITY_WHITESPACE

The second highest justification priority.

PRIORITY_INTERCHAR

```java
public static final int PRIORITY_INTERCHAR
```

The second lowest justification priority.

**See Also:** Constant Field Values

---

#### PRIORITY_INTERCHAR

public static final int PRIORITY_INTERCHAR

The second lowest justification priority.

PRIORITY_NONE

```java
public static final int PRIORITY_NONE
```

The lowest justification priority.

**See Also:** Constant Field Values

---

#### PRIORITY_NONE

public static final int PRIORITY_NONE

The lowest justification priority.

weight

```java
public final float weight
```

The weight of this glyph.

---

#### weight

public final float weight

The weight of this glyph.

growPriority

```java
public final int growPriority
```

The priority level of this glyph as it is growing.

---

#### growPriority

public final int growPriority

The priority level of this glyph as it is growing.

growAbsorb

```java
public final boolean growAbsorb
```

If

true

, this glyph absorbs all extra
space at this and lower priority levels when it grows.

---

#### growAbsorb

public final boolean growAbsorb

If

true

, this glyph absorbs all extra
space at this and lower priority levels when it grows.

growLeftLimit

```java
public final float growLeftLimit
```

The maximum amount by which the left side of this glyph can grow.

---

#### growLeftLimit

public final float growLeftLimit

The maximum amount by which the left side of this glyph can grow.

growRightLimit

```java
public final float growRightLimit
```

The maximum amount by which the right side of this glyph can grow.

---

#### growRightLimit

public final float growRightLimit

The maximum amount by which the right side of this glyph can grow.

shrinkPriority

```java
public final int shrinkPriority
```

The priority level of this glyph as it is shrinking.

---

#### shrinkPriority

public final int shrinkPriority

The priority level of this glyph as it is shrinking.

shrinkAbsorb

```java
public final boolean shrinkAbsorb
```

If

true

,this glyph absorbs all remaining shrinkage at
this and lower priority levels as it shrinks.

---

#### shrinkAbsorb

public final boolean shrinkAbsorb

If

true

,this glyph absorbs all remaining shrinkage at
this and lower priority levels as it shrinks.

shrinkLeftLimit

```java
public final float shrinkLeftLimit
```

The maximum amount by which the left side of this glyph can shrink
(a positive number).

---

#### shrinkLeftLimit

public final float shrinkLeftLimit

The maximum amount by which the left side of this glyph can shrink
(a positive number).

shrinkRightLimit

```java
public final float shrinkRightLimit
```

The maximum amount by which the right side of this glyph can shrink
(a positive number).

---

#### shrinkRightLimit

public final float shrinkRightLimit

The maximum amount by which the right side of this glyph can shrink
(a positive number).

Constructor Detail

- GlyphJustificationInfo

```java
public GlyphJustificationInfo​(float weight,
boolean growAbsorb,
int growPriority,
float growLeftLimit,
float growRightLimit,
boolean shrinkAbsorb,
int shrinkPriority,
float shrinkLeftLimit,
float shrinkRightLimit)
```

Constructs information about the justification properties of a
glyph.

**Parameters:** weight

- the weight of this glyph when allocating space. Must be non-negative.
**Parameters:** growAbsorb

- if

true

this glyph absorbs
all extra space at this priority and lower priority levels when it
grows
**Parameters:** growPriority

- the priority level of this glyph when it
grows
**Parameters:** growLeftLimit

- the maximum amount by which the left side of this
glyph can grow. Must be non-negative.
**Parameters:** growRightLimit

- the maximum amount by which the right side of this
glyph can grow. Must be non-negative.
**Parameters:** shrinkAbsorb

- if

true

, this glyph absorbs all
remaining shrinkage at this and lower priority levels when it
shrinks
**Parameters:** shrinkPriority

- the priority level of this glyph when
it shrinks
**Parameters:** shrinkLeftLimit

- the maximum amount by which the left side of this
glyph can shrink. Must be non-negative.
**Parameters:** shrinkRightLimit

- the maximum amount by which the right side
of this glyph can shrink. Must be non-negative.

---

#### Constructor Detail

GlyphJustificationInfo

```java
public GlyphJustificationInfo​(float weight,
boolean growAbsorb,
int growPriority,
float growLeftLimit,
float growRightLimit,
boolean shrinkAbsorb,
int shrinkPriority,
float shrinkLeftLimit,
float shrinkRightLimit)
```

Constructs information about the justification properties of a
glyph.

**Parameters:** weight

- the weight of this glyph when allocating space. Must be non-negative.
**Parameters:** growAbsorb

- if

true

this glyph absorbs
all extra space at this priority and lower priority levels when it
grows
**Parameters:** growPriority

- the priority level of this glyph when it
grows
**Parameters:** growLeftLimit

- the maximum amount by which the left side of this
glyph can grow. Must be non-negative.
**Parameters:** growRightLimit

- the maximum amount by which the right side of this
glyph can grow. Must be non-negative.
**Parameters:** shrinkAbsorb

- if

true

, this glyph absorbs all
remaining shrinkage at this and lower priority levels when it
shrinks
**Parameters:** shrinkPriority

- the priority level of this glyph when
it shrinks
**Parameters:** shrinkLeftLimit

- the maximum amount by which the left side of this
glyph can shrink. Must be non-negative.
**Parameters:** shrinkRightLimit

- the maximum amount by which the right side
of this glyph can shrink. Must be non-negative.

---

#### GlyphJustificationInfo

public GlyphJustificationInfo​(float weight,
boolean growAbsorb,
int growPriority,
float growLeftLimit,
float growRightLimit,
boolean shrinkAbsorb,
int shrinkPriority,
float shrinkLeftLimit,
float shrinkRightLimit)

Constructs information about the justification properties of a
glyph.

---

