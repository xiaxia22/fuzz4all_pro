# Class BasicStroke

**Source:** `java.desktop\java\awt\BasicStroke.html`

### Class Description

```java
public class
BasicStroke

extends
Object

implements
Stroke
```

The

BasicStroke

class defines a basic set of rendering
attributes for the outlines of graphics primitives, which are rendered
with a

Graphics2D

object that has its Stroke attribute set to
this

BasicStroke

.
The rendering attributes defined by

BasicStroke

describe
the shape of the mark made by a pen drawn along the outline of a

Shape

and the decorations applied at the ends and joins of
path segments of the

Shape

.
These rendering attributes include:

All attributes that specify measurements and distances controlling
the shape of the returned outline are measured in the same
coordinate system as the original unstroked

Shape

argument. When a

Graphics2D

object uses a

Stroke

object to redefine a path during the execution
of one of its

draw

methods, the geometry is supplied
in its original form before the

Graphics2D

transform
attribute is applied. Therefore, attributes such as the pen width
are interpreted in the user space coordinate system of the

Graphics2D

object and are subject to the scaling and
shearing effects of the user-space-to-device-space transform in that
particular

Graphics2D

.
For example, the width of a rendered shape's outline is determined
not only by the width attribute of this

BasicStroke

,
but also by the transform attribute of the

Graphics2D

object. Consider this code:

```java
// sets the Graphics2D object's Transform attribute
g2d.scale(10, 10);
// sets the Graphics2D object's Stroke attribute
g2d.setStroke(new BasicStroke(1.5f));
```

Assuming there are no other scaling transforms added to the

Graphics2D

object, the resulting line
will be approximately 15 pixels wide.
As the example code demonstrates, a floating-point line
offers better precision, especially when large transforms are
used with a

Graphics2D

object.
When a line is diagonal, the exact width depends on how the
rendering pipeline chooses which pixels to fill as it traces the
theoretical widened outline. The choice of which pixels to turn
on is affected by the antialiasing attribute because the
antialiasing rendering pipeline can choose to color
partially-covered pixels.

For more information on the user space coordinate system and the
rendering process, see the

Graphics2D

class comments.

**All Implemented Interfaces:** Stroke

---

### Field Details

#### @Native

public static final int JOIN_MITER

Joins path segments by extending their outside edges until
they meet.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int JOIN_ROUND

Joins path segments by rounding off the corner at a radius
of half the line width.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int JOIN_BEVEL

Joins path segments by connecting the outer corners of their
wide outlines with a straight segment.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int CAP_BUTT

Ends unclosed subpaths and dash segments with no added
decoration.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int CAP_ROUND

Ends unclosed subpaths and dash segments with a round
decoration that has a radius equal to half of the width
of the pen.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int CAP_SQUARE

Ends unclosed subpaths and dash segments with a square
projection that extends beyond the end of the segment
to a distance equal to half of the line width.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### @ConstructorProperties
({"lineWidth","endCap","lineJoin","miterLimit","dashArray","dashPhase"})
public BasicStroke​(float width,
int cap,
int join,
float miterlimit,
float[] dash,
float dash_phase)

Constructs a new

BasicStroke

with the specified
attributes.

**Parameters:**
- width

- the width of this

BasicStroke

. The
width must be greater than or equal to 0.0f. If width is
set to 0.0f, the stroke is rendered as the thinnest
possible line for the target device and the antialias
hint setting.
- cap

- the decoration of the ends of a

BasicStroke
- join

- the decoration applied where path segments meet
- miterlimit

- the limit to trim the miter join. The miterlimit
must be greater than or equal to 1.0f.
- dash

- the array representing the dashing pattern
- dash_phase

- the offset to start the dashing pattern

**Throws:**
- IllegalArgumentException

- if

width

is negative
- IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
- IllegalArgumentException

- if

miterlimit

is less
than 1 and

join

is JOIN_MITER
- IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER
- IllegalArgumentException

- if

dash_phase

is negative and

dash

is not

null
- IllegalArgumentException

- if the length of

dash

is zero
- IllegalArgumentException

- if dash lengths are all zero.

---

#### public BasicStroke​(float width,
int cap,
int join,
float miterlimit)

Constructs a solid

BasicStroke

with the specified
attributes.

**Parameters:**
- width

- the width of the

BasicStroke
- cap

- the decoration of the ends of a

BasicStroke
- join

- the decoration applied where path segments meet
- miterlimit

- the limit to trim the miter join

**Throws:**
- IllegalArgumentException

- if

width

is negative
- IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
- IllegalArgumentException

- if

miterlimit

is less
than 1 and

join

is JOIN_MITER
- IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

---

#### public BasicStroke​(float width,
int cap,
int join)

Constructs a solid

BasicStroke

with the specified
attributes. The

miterlimit

parameter is
unnecessary in cases where the default is allowable or the
line joins are not specified as JOIN_MITER.

**Parameters:**
- width

- the width of the

BasicStroke
- cap

- the decoration of the ends of a

BasicStroke
- join

- the decoration applied where path segments meet

**Throws:**
- IllegalArgumentException

- if

width

is negative
- IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
- IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

---

#### public BasicStroke​(float width)

Constructs a solid

BasicStroke

with the specified
line width and with default values for the cap and join
styles.

**Parameters:**
- width

- the width of the

BasicStroke

**Throws:**
- IllegalArgumentException

- if

width

is negative

---

#### public BasicStroke()

Constructs a new

BasicStroke

with defaults for all
attributes.
The default attributes are a solid line of width 1.0, CAP_SQUARE,
JOIN_MITER, a miter limit of 10.0.

---

### Method Details

#### public
Shape
createStrokedShape​(
Shape
s)

Returns a

Shape

whose interior defines the
stroked outline of a specified

Shape

.

**Specified by:**
- createStrokedShape

in interface

Stroke

**Parameters:**
- s

- the

Shape

boundary be stroked

**Returns:**
- the

Shape

of the stroked outline.

---

#### public float getLineWidth()

Returns the line width. Line width is represented in user space,
which is the default-coordinate space used by Java 2D. See the

Graphics2D

class comments for more information on
the user space coordinate system.

**Returns:**
- the line width of this

BasicStroke

.

**See Also:**
- Graphics2D

---

#### public int getEndCap()

Returns the end cap style.

**Returns:**
- the end cap style of this

BasicStroke

as one
of the static

int

values that define possible end cap
styles.

---

#### public int getLineJoin()

Returns the line join style.

**Returns:**
- the line join style of the

BasicStroke

as one
of the static

int

values that define possible line
join styles.

---

#### public float getMiterLimit()

Returns the limit of miter joins.

**Returns:**
- the limit of miter joins of the

BasicStroke

.

---

#### public float[] getDashArray()

Returns the array representing the lengths of the dash segments.
Alternate entries in the array represent the user space lengths
of the opaque and transparent segments of the dashes.
As the pen moves along the outline of the

Shape

to be stroked, the user space
distance that the pen travels is accumulated. The distance
value is used to index into the dash array.
The pen is opaque when its current cumulative distance maps
to an even element of the dash array and transparent otherwise.

**Returns:**
- the dash array.

---

#### public float getDashPhase()

Returns the current dash phase.
The dash phase is a distance specified in user coordinates that
represents an offset into the dashing pattern. In other words, the dash
phase defines the point in the dashing pattern that will correspond to
the beginning of the stroke.

**Returns:**
- the dash phase as a

float

value.

---

#### public int hashCode()

Returns the hashcode for this stroke.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this stroke.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Tests if a specified object is equal to this

BasicStroke

by first testing if it is a

BasicStroke

and then comparing
its width, join, cap, miter limit, dash, and dash phase attributes with
those of this

BasicStroke

.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the specified object to compare to this

BasicStroke

**Returns:**
- true

if the width, join, cap, miter limit, dash, and
dash phase are the same for both objects;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class BasicStroke

java.lang.Object

- java.awt.BasicStroke

java.awt.BasicStroke

**All Implemented Interfaces:** Stroke

```java
public class
BasicStroke

extends
Object

implements
Stroke
```

The

BasicStroke

class defines a basic set of rendering
attributes for the outlines of graphics primitives, which are rendered
with a

Graphics2D

object that has its Stroke attribute set to
this

BasicStroke

.
The rendering attributes defined by

BasicStroke

describe
the shape of the mark made by a pen drawn along the outline of a

Shape

and the decorations applied at the ends and joins of
path segments of the

Shape

.
These rendering attributes include:

All attributes that specify measurements and distances controlling
the shape of the returned outline are measured in the same
coordinate system as the original unstroked

Shape

argument. When a

Graphics2D

object uses a

Stroke

object to redefine a path during the execution
of one of its

draw

methods, the geometry is supplied
in its original form before the

Graphics2D

transform
attribute is applied. Therefore, attributes such as the pen width
are interpreted in the user space coordinate system of the

Graphics2D

object and are subject to the scaling and
shearing effects of the user-space-to-device-space transform in that
particular

Graphics2D

.
For example, the width of a rendered shape's outline is determined
not only by the width attribute of this

BasicStroke

,
but also by the transform attribute of the

Graphics2D

object. Consider this code:

```java
// sets the Graphics2D object's Transform attribute
g2d.scale(10, 10);
// sets the Graphics2D object's Stroke attribute
g2d.setStroke(new BasicStroke(1.5f));
```

Assuming there are no other scaling transforms added to the

Graphics2D

object, the resulting line
will be approximately 15 pixels wide.
As the example code demonstrates, a floating-point line
offers better precision, especially when large transforms are
used with a

Graphics2D

object.
When a line is diagonal, the exact width depends on how the
rendering pipeline chooses which pixels to fill as it traces the
theoretical widened outline. The choice of which pixels to turn
on is affected by the antialiasing attribute because the
antialiasing rendering pipeline can choose to color
partially-covered pixels.

For more information on the user space coordinate system and the
rendering process, see the

Graphics2D

class comments.

**See Also:** Graphics2D

public class

BasicStroke

extends

Object

implements

Stroke

The

BasicStroke

class defines a basic set of rendering
attributes for the outlines of graphics primitives, which are rendered
with a

Graphics2D

object that has its Stroke attribute set to
this

BasicStroke

.
The rendering attributes defined by

BasicStroke

describe
the shape of the mark made by a pen drawn along the outline of a

Shape

and the decorations applied at the ends and joins of
path segments of the

Shape

.
These rendering attributes include:

All attributes that specify measurements and distances controlling
the shape of the returned outline are measured in the same
coordinate system as the original unstroked

Shape

argument. When a

Graphics2D

object uses a

Stroke

object to redefine a path during the execution
of one of its

draw

methods, the geometry is supplied
in its original form before the

Graphics2D

transform
attribute is applied. Therefore, attributes such as the pen width
are interpreted in the user space coordinate system of the

Graphics2D

object and are subject to the scaling and
shearing effects of the user-space-to-device-space transform in that
particular

Graphics2D

.
For example, the width of a rendered shape's outline is determined
not only by the width attribute of this

BasicStroke

,
but also by the transform attribute of the

Graphics2D

object. Consider this code:

```java
// sets the Graphics2D object's Transform attribute
g2d.scale(10, 10);
// sets the Graphics2D object's Stroke attribute
g2d.setStroke(new BasicStroke(1.5f));
```

Assuming there are no other scaling transforms added to the

Graphics2D

object, the resulting line
will be approximately 15 pixels wide.
As the example code demonstrates, a floating-point line
offers better precision, especially when large transforms are
used with a

Graphics2D

object.
When a line is diagonal, the exact width depends on how the
rendering pipeline chooses which pixels to fill as it traces the
theoretical widened outline. The choice of which pixels to turn
on is affected by the antialiasing attribute because the
antialiasing rendering pipeline can choose to color
partially-covered pixels.

For more information on the user space coordinate system and the
rendering process, see the

Graphics2D

class comments.

// sets the Graphics2D object's Transform attribute
g2d.scale(10, 10);
// sets the Graphics2D object's Stroke attribute
g2d.setStroke(new BasicStroke(1.5f));

For more information on the user space coordinate system and the
rendering process, see the

Graphics2D

class comments.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CAP_BUTT

Ends unclosed subpaths and dash segments with no added
decoration.

static int

CAP_ROUND

Ends unclosed subpaths and dash segments with a round
decoration that has a radius equal to half of the width
of the pen.

static int

CAP_SQUARE

Ends unclosed subpaths and dash segments with a square
projection that extends beyond the end of the segment
to a distance equal to half of the line width.

static int

JOIN_BEVEL

Joins path segments by connecting the outer corners of their
wide outlines with a straight segment.

static int

JOIN_MITER

Joins path segments by extending their outside edges until
they meet.

static int

JOIN_ROUND

Joins path segments by rounding off the corner at a radius
of half the line width.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicStroke

()

Constructs a new

BasicStroke

with defaults for all
attributes.

BasicStroke

​(float width)

Constructs a solid

BasicStroke

with the specified
line width and with default values for the cap and join
styles.

BasicStroke

​(float width,
int cap,
int join)

Constructs a solid

BasicStroke

with the specified
attributes.

BasicStroke

​(float width,
int cap,
int join,
float miterlimit)

Constructs a solid

BasicStroke

with the specified
attributes.

BasicStroke

​(float width,
int cap,
int join,
float miterlimit,
float[] dash,
float dash_phase)

Constructs a new

BasicStroke

with the specified
attributes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Shape

createStrokedShape

​(

Shape

s)

Returns a

Shape

whose interior defines the
stroked outline of a specified

Shape

.

boolean

equals

​(

Object

obj)

Tests if a specified object is equal to this

BasicStroke

by first testing if it is a

BasicStroke

and then comparing
its width, join, cap, miter limit, dash, and dash phase attributes with
those of this

BasicStroke

.

float[]

getDashArray

()

Returns the array representing the lengths of the dash segments.

float

getDashPhase

()

Returns the current dash phase.

int

getEndCap

()

Returns the end cap style.

int

getLineJoin

()

Returns the line join style.

float

getLineWidth

()

Returns the line width.

float

getMiterLimit

()

Returns the limit of miter joins.

int

hashCode

()

Returns the hashcode for this stroke.

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

CAP_BUTT

Ends unclosed subpaths and dash segments with no added
decoration.

static int

CAP_ROUND

Ends unclosed subpaths and dash segments with a round
decoration that has a radius equal to half of the width
of the pen.

static int

CAP_SQUARE

Ends unclosed subpaths and dash segments with a square
projection that extends beyond the end of the segment
to a distance equal to half of the line width.

static int

JOIN_BEVEL

Joins path segments by connecting the outer corners of their
wide outlines with a straight segment.

static int

JOIN_MITER

Joins path segments by extending their outside edges until
they meet.

static int

JOIN_ROUND

Joins path segments by rounding off the corner at a radius
of half the line width.

---

#### Field Summary

Ends unclosed subpaths and dash segments with no added
decoration.

Ends unclosed subpaths and dash segments with a round
decoration that has a radius equal to half of the width
of the pen.

Ends unclosed subpaths and dash segments with a square
projection that extends beyond the end of the segment
to a distance equal to half of the line width.

Joins path segments by connecting the outer corners of their
wide outlines with a straight segment.

Joins path segments by extending their outside edges until
they meet.

Joins path segments by rounding off the corner at a radius
of half the line width.

Constructor Summary

Constructors

Constructor

Description

BasicStroke

()

Constructs a new

BasicStroke

with defaults for all
attributes.

BasicStroke

​(float width)

Constructs a solid

BasicStroke

with the specified
line width and with default values for the cap and join
styles.

BasicStroke

​(float width,
int cap,
int join)

Constructs a solid

BasicStroke

with the specified
attributes.

BasicStroke

​(float width,
int cap,
int join,
float miterlimit)

Constructs a solid

BasicStroke

with the specified
attributes.

BasicStroke

​(float width,
int cap,
int join,
float miterlimit,
float[] dash,
float dash_phase)

Constructs a new

BasicStroke

with the specified
attributes.

---

#### Constructor Summary

Constructs a new

BasicStroke

with defaults for all
attributes.

Constructs a solid

BasicStroke

with the specified
line width and with default values for the cap and join
styles.

Constructs a solid

BasicStroke

with the specified
attributes.

Constructs a new

BasicStroke

with the specified
attributes.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Shape

createStrokedShape

​(

Shape

s)

Returns a

Shape

whose interior defines the
stroked outline of a specified

Shape

.

boolean

equals

​(

Object

obj)

Tests if a specified object is equal to this

BasicStroke

by first testing if it is a

BasicStroke

and then comparing
its width, join, cap, miter limit, dash, and dash phase attributes with
those of this

BasicStroke

.

float[]

getDashArray

()

Returns the array representing the lengths of the dash segments.

float

getDashPhase

()

Returns the current dash phase.

int

getEndCap

()

Returns the end cap style.

int

getLineJoin

()

Returns the line join style.

float

getLineWidth

()

Returns the line width.

float

getMiterLimit

()

Returns the limit of miter joins.

int

hashCode

()

Returns the hashcode for this stroke.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a

Shape

whose interior defines the
stroked outline of a specified

Shape

.

Tests if a specified object is equal to this

BasicStroke

by first testing if it is a

BasicStroke

and then comparing
its width, join, cap, miter limit, dash, and dash phase attributes with
those of this

BasicStroke

.

Returns the array representing the lengths of the dash segments.

Returns the current dash phase.

Returns the end cap style.

Returns the line join style.

Returns the line width.

Returns the limit of miter joins.

Returns the hashcode for this stroke.

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

- JOIN_MITER

```java
@Native

public static final int JOIN_MITER
```

Joins path segments by extending their outside edges until
they meet.

**See Also:** Constant Field Values

- JOIN_ROUND

```java
@Native

public static final int JOIN_ROUND
```

Joins path segments by rounding off the corner at a radius
of half the line width.

**See Also:** Constant Field Values

- JOIN_BEVEL

```java
@Native

public static final int JOIN_BEVEL
```

Joins path segments by connecting the outer corners of their
wide outlines with a straight segment.

**See Also:** Constant Field Values

- CAP_BUTT

```java
@Native

public static final int CAP_BUTT
```

Ends unclosed subpaths and dash segments with no added
decoration.

**See Also:** Constant Field Values

- CAP_ROUND

```java
@Native

public static final int CAP_ROUND
```

Ends unclosed subpaths and dash segments with a round
decoration that has a radius equal to half of the width
of the pen.

**See Also:** Constant Field Values

- CAP_SQUARE

```java
@Native

public static final int CAP_SQUARE
```

Ends unclosed subpaths and dash segments with a square
projection that extends beyond the end of the segment
to a distance equal to half of the line width.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicStroke

```java
@ConstructorProperties
({"lineWidth","endCap","lineJoin","miterLimit","dashArray","dashPhase"})
public BasicStroke​(float width,
int cap,
int join,
float miterlimit,
float[] dash,
float dash_phase)
```

Constructs a new

BasicStroke

with the specified
attributes.

**Parameters:** width

- the width of this

BasicStroke

. The
width must be greater than or equal to 0.0f. If width is
set to 0.0f, the stroke is rendered as the thinnest
possible line for the target device and the antialias
hint setting.
**Parameters:** cap

- the decoration of the ends of a

BasicStroke
**Parameters:** join

- the decoration applied where path segments meet
**Parameters:** miterlimit

- the limit to trim the miter join. The miterlimit
must be greater than or equal to 1.0f.
**Parameters:** dash

- the array representing the dashing pattern
**Parameters:** dash_phase

- the offset to start the dashing pattern
**Throws:** IllegalArgumentException

- if

width

is negative
**Throws:** IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
**Throws:** IllegalArgumentException

- if

miterlimit

is less
than 1 and

join

is JOIN_MITER
**Throws:** IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER
**Throws:** IllegalArgumentException

- if

dash_phase

is negative and

dash

is not

null
**Throws:** IllegalArgumentException

- if the length of

dash

is zero
**Throws:** IllegalArgumentException

- if dash lengths are all zero.

- BasicStroke

```java
public BasicStroke​(float width,
int cap,
int join,
float miterlimit)
```

Constructs a solid

BasicStroke

with the specified
attributes.

**Parameters:** width

- the width of the

BasicStroke
**Parameters:** cap

- the decoration of the ends of a

BasicStroke
**Parameters:** join

- the decoration applied where path segments meet
**Parameters:** miterlimit

- the limit to trim the miter join
**Throws:** IllegalArgumentException

- if

width

is negative
**Throws:** IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
**Throws:** IllegalArgumentException

- if

miterlimit

is less
than 1 and

join

is JOIN_MITER
**Throws:** IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

- BasicStroke

```java
public BasicStroke​(float width,
int cap,
int join)
```

Constructs a solid

BasicStroke

with the specified
attributes. The

miterlimit

parameter is
unnecessary in cases where the default is allowable or the
line joins are not specified as JOIN_MITER.

**Parameters:** width

- the width of the

BasicStroke
**Parameters:** cap

- the decoration of the ends of a

BasicStroke
**Parameters:** join

- the decoration applied where path segments meet
**Throws:** IllegalArgumentException

- if

width

is negative
**Throws:** IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
**Throws:** IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

- BasicStroke

```java
public BasicStroke​(float width)
```

Constructs a solid

BasicStroke

with the specified
line width and with default values for the cap and join
styles.

**Parameters:** width

- the width of the

BasicStroke
**Throws:** IllegalArgumentException

- if

width

is negative

- BasicStroke

```java
public BasicStroke()
```

Constructs a new

BasicStroke

with defaults for all
attributes.
The default attributes are a solid line of width 1.0, CAP_SQUARE,
JOIN_MITER, a miter limit of 10.0.

============ METHOD DETAIL ==========

- Method Detail

- createStrokedShape

```java
public
Shape
createStrokedShape​(
Shape
s)
```

Returns a

Shape

whose interior defines the
stroked outline of a specified

Shape

.

**Specified by:** createStrokedShape

in interface

Stroke
**Parameters:** s

- the

Shape

boundary be stroked
**Returns:** the

Shape

of the stroked outline.

- getLineWidth

```java
public float getLineWidth()
```

Returns the line width. Line width is represented in user space,
which is the default-coordinate space used by Java 2D. See the

Graphics2D

class comments for more information on
the user space coordinate system.

**Returns:** the line width of this

BasicStroke

.
**See Also:** Graphics2D

- getEndCap

```java
public int getEndCap()
```

Returns the end cap style.

**Returns:** the end cap style of this

BasicStroke

as one
of the static

int

values that define possible end cap
styles.

- getLineJoin

```java
public int getLineJoin()
```

Returns the line join style.

**Returns:** the line join style of the

BasicStroke

as one
of the static

int

values that define possible line
join styles.

- getMiterLimit

```java
public float getMiterLimit()
```

Returns the limit of miter joins.

**Returns:** the limit of miter joins of the

BasicStroke

.

- getDashArray

```java
public float[] getDashArray()
```

Returns the array representing the lengths of the dash segments.
Alternate entries in the array represent the user space lengths
of the opaque and transparent segments of the dashes.
As the pen moves along the outline of the

Shape

to be stroked, the user space
distance that the pen travels is accumulated. The distance
value is used to index into the dash array.
The pen is opaque when its current cumulative distance maps
to an even element of the dash array and transparent otherwise.

**Returns:** the dash array.

- getDashPhase

```java
public float getDashPhase()
```

Returns the current dash phase.
The dash phase is a distance specified in user coordinates that
represents an offset into the dashing pattern. In other words, the dash
phase defines the point in the dashing pattern that will correspond to
the beginning of the stroke.

**Returns:** the dash phase as a

float

value.

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this stroke.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this stroke.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Tests if a specified object is equal to this

BasicStroke

by first testing if it is a

BasicStroke

and then comparing
its width, join, cap, miter limit, dash, and dash phase attributes with
those of this

BasicStroke

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the specified object to compare to this

BasicStroke
**Returns:** true

if the width, join, cap, miter limit, dash, and
dash phase are the same for both objects;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

Field Detail

- JOIN_MITER

```java
@Native

public static final int JOIN_MITER
```

Joins path segments by extending their outside edges until
they meet.

**See Also:** Constant Field Values

- JOIN_ROUND

```java
@Native

public static final int JOIN_ROUND
```

Joins path segments by rounding off the corner at a radius
of half the line width.

**See Also:** Constant Field Values

- JOIN_BEVEL

```java
@Native

public static final int JOIN_BEVEL
```

Joins path segments by connecting the outer corners of their
wide outlines with a straight segment.

**See Also:** Constant Field Values

- CAP_BUTT

```java
@Native

public static final int CAP_BUTT
```

Ends unclosed subpaths and dash segments with no added
decoration.

**See Also:** Constant Field Values

- CAP_ROUND

```java
@Native

public static final int CAP_ROUND
```

Ends unclosed subpaths and dash segments with a round
decoration that has a radius equal to half of the width
of the pen.

**See Also:** Constant Field Values

- CAP_SQUARE

```java
@Native

public static final int CAP_SQUARE
```

Ends unclosed subpaths and dash segments with a square
projection that extends beyond the end of the segment
to a distance equal to half of the line width.

**See Also:** Constant Field Values

---

#### Field Detail

JOIN_MITER

```java
@Native

public static final int JOIN_MITER
```

Joins path segments by extending their outside edges until
they meet.

**See Also:** Constant Field Values

---

#### JOIN_MITER

@Native

public static final int JOIN_MITER

Joins path segments by extending their outside edges until
they meet.

JOIN_ROUND

```java
@Native

public static final int JOIN_ROUND
```

Joins path segments by rounding off the corner at a radius
of half the line width.

**See Also:** Constant Field Values

---

#### JOIN_ROUND

@Native

public static final int JOIN_ROUND

Joins path segments by rounding off the corner at a radius
of half the line width.

JOIN_BEVEL

```java
@Native

public static final int JOIN_BEVEL
```

Joins path segments by connecting the outer corners of their
wide outlines with a straight segment.

**See Also:** Constant Field Values

---

#### JOIN_BEVEL

@Native

public static final int JOIN_BEVEL

Joins path segments by connecting the outer corners of their
wide outlines with a straight segment.

CAP_BUTT

```java
@Native

public static final int CAP_BUTT
```

Ends unclosed subpaths and dash segments with no added
decoration.

**See Also:** Constant Field Values

---

#### CAP_BUTT

@Native

public static final int CAP_BUTT

Ends unclosed subpaths and dash segments with no added
decoration.

CAP_ROUND

```java
@Native

public static final int CAP_ROUND
```

Ends unclosed subpaths and dash segments with a round
decoration that has a radius equal to half of the width
of the pen.

**See Also:** Constant Field Values

---

#### CAP_ROUND

@Native

public static final int CAP_ROUND

Ends unclosed subpaths and dash segments with a round
decoration that has a radius equal to half of the width
of the pen.

CAP_SQUARE

```java
@Native

public static final int CAP_SQUARE
```

Ends unclosed subpaths and dash segments with a square
projection that extends beyond the end of the segment
to a distance equal to half of the line width.

**See Also:** Constant Field Values

---

#### CAP_SQUARE

@Native

public static final int CAP_SQUARE

Ends unclosed subpaths and dash segments with a square
projection that extends beyond the end of the segment
to a distance equal to half of the line width.

Constructor Detail

- BasicStroke

```java
@ConstructorProperties
({"lineWidth","endCap","lineJoin","miterLimit","dashArray","dashPhase"})
public BasicStroke​(float width,
int cap,
int join,
float miterlimit,
float[] dash,
float dash_phase)
```

Constructs a new

BasicStroke

with the specified
attributes.

**Parameters:** width

- the width of this

BasicStroke

. The
width must be greater than or equal to 0.0f. If width is
set to 0.0f, the stroke is rendered as the thinnest
possible line for the target device and the antialias
hint setting.
**Parameters:** cap

- the decoration of the ends of a

BasicStroke
**Parameters:** join

- the decoration applied where path segments meet
**Parameters:** miterlimit

- the limit to trim the miter join. The miterlimit
must be greater than or equal to 1.0f.
**Parameters:** dash

- the array representing the dashing pattern
**Parameters:** dash_phase

- the offset to start the dashing pattern
**Throws:** IllegalArgumentException

- if

width

is negative
**Throws:** IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
**Throws:** IllegalArgumentException

- if

miterlimit

is less
than 1 and

join

is JOIN_MITER
**Throws:** IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER
**Throws:** IllegalArgumentException

- if

dash_phase

is negative and

dash

is not

null
**Throws:** IllegalArgumentException

- if the length of

dash

is zero
**Throws:** IllegalArgumentException

- if dash lengths are all zero.

- BasicStroke

```java
public BasicStroke​(float width,
int cap,
int join,
float miterlimit)
```

Constructs a solid

BasicStroke

with the specified
attributes.

**Parameters:** width

- the width of the

BasicStroke
**Parameters:** cap

- the decoration of the ends of a

BasicStroke
**Parameters:** join

- the decoration applied where path segments meet
**Parameters:** miterlimit

- the limit to trim the miter join
**Throws:** IllegalArgumentException

- if

width

is negative
**Throws:** IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
**Throws:** IllegalArgumentException

- if

miterlimit

is less
than 1 and

join

is JOIN_MITER
**Throws:** IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

- BasicStroke

```java
public BasicStroke​(float width,
int cap,
int join)
```

Constructs a solid

BasicStroke

with the specified
attributes. The

miterlimit

parameter is
unnecessary in cases where the default is allowable or the
line joins are not specified as JOIN_MITER.

**Parameters:** width

- the width of the

BasicStroke
**Parameters:** cap

- the decoration of the ends of a

BasicStroke
**Parameters:** join

- the decoration applied where path segments meet
**Throws:** IllegalArgumentException

- if

width

is negative
**Throws:** IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
**Throws:** IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

- BasicStroke

```java
public BasicStroke​(float width)
```

Constructs a solid

BasicStroke

with the specified
line width and with default values for the cap and join
styles.

**Parameters:** width

- the width of the

BasicStroke
**Throws:** IllegalArgumentException

- if

width

is negative

- BasicStroke

```java
public BasicStroke()
```

Constructs a new

BasicStroke

with defaults for all
attributes.
The default attributes are a solid line of width 1.0, CAP_SQUARE,
JOIN_MITER, a miter limit of 10.0.

---

#### Constructor Detail

BasicStroke

```java
@ConstructorProperties
({"lineWidth","endCap","lineJoin","miterLimit","dashArray","dashPhase"})
public BasicStroke​(float width,
int cap,
int join,
float miterlimit,
float[] dash,
float dash_phase)
```

Constructs a new

BasicStroke

with the specified
attributes.

**Parameters:** width

- the width of this

BasicStroke

. The
width must be greater than or equal to 0.0f. If width is
set to 0.0f, the stroke is rendered as the thinnest
possible line for the target device and the antialias
hint setting.
**Parameters:** cap

- the decoration of the ends of a

BasicStroke
**Parameters:** join

- the decoration applied where path segments meet
**Parameters:** miterlimit

- the limit to trim the miter join. The miterlimit
must be greater than or equal to 1.0f.
**Parameters:** dash

- the array representing the dashing pattern
**Parameters:** dash_phase

- the offset to start the dashing pattern
**Throws:** IllegalArgumentException

- if

width

is negative
**Throws:** IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
**Throws:** IllegalArgumentException

- if

miterlimit

is less
than 1 and

join

is JOIN_MITER
**Throws:** IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER
**Throws:** IllegalArgumentException

- if

dash_phase

is negative and

dash

is not

null
**Throws:** IllegalArgumentException

- if the length of

dash

is zero
**Throws:** IllegalArgumentException

- if dash lengths are all zero.

---

#### BasicStroke

@ConstructorProperties

({"lineWidth","endCap","lineJoin","miterLimit","dashArray","dashPhase"})
public BasicStroke​(float width,
int cap,
int join,
float miterlimit,
float[] dash,
float dash_phase)

Constructs a new

BasicStroke

with the specified
attributes.

BasicStroke

```java
public BasicStroke​(float width,
int cap,
int join,
float miterlimit)
```

Constructs a solid

BasicStroke

with the specified
attributes.

**Parameters:** width

- the width of the

BasicStroke
**Parameters:** cap

- the decoration of the ends of a

BasicStroke
**Parameters:** join

- the decoration applied where path segments meet
**Parameters:** miterlimit

- the limit to trim the miter join
**Throws:** IllegalArgumentException

- if

width

is negative
**Throws:** IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
**Throws:** IllegalArgumentException

- if

miterlimit

is less
than 1 and

join

is JOIN_MITER
**Throws:** IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

---

#### BasicStroke

public BasicStroke​(float width,
int cap,
int join,
float miterlimit)

Constructs a solid

BasicStroke

with the specified
attributes.

BasicStroke

```java
public BasicStroke​(float width,
int cap,
int join)
```

Constructs a solid

BasicStroke

with the specified
attributes. The

miterlimit

parameter is
unnecessary in cases where the default is allowable or the
line joins are not specified as JOIN_MITER.

**Parameters:** width

- the width of the

BasicStroke
**Parameters:** cap

- the decoration of the ends of a

BasicStroke
**Parameters:** join

- the decoration applied where path segments meet
**Throws:** IllegalArgumentException

- if

width

is negative
**Throws:** IllegalArgumentException

- if

cap

is not either
CAP_BUTT, CAP_ROUND or CAP_SQUARE
**Throws:** IllegalArgumentException

- if

join

is not
either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

---

#### BasicStroke

public BasicStroke​(float width,
int cap,
int join)

Constructs a solid

BasicStroke

with the specified
attributes. The

miterlimit

parameter is
unnecessary in cases where the default is allowable or the
line joins are not specified as JOIN_MITER.

BasicStroke

```java
public BasicStroke​(float width)
```

Constructs a solid

BasicStroke

with the specified
line width and with default values for the cap and join
styles.

**Parameters:** width

- the width of the

BasicStroke
**Throws:** IllegalArgumentException

- if

width

is negative

---

#### BasicStroke

public BasicStroke​(float width)

Constructs a solid

BasicStroke

with the specified
line width and with default values for the cap and join
styles.

BasicStroke

```java
public BasicStroke()
```

Constructs a new

BasicStroke

with defaults for all
attributes.
The default attributes are a solid line of width 1.0, CAP_SQUARE,
JOIN_MITER, a miter limit of 10.0.

---

#### BasicStroke

public BasicStroke()

Constructs a new

BasicStroke

with defaults for all
attributes.
The default attributes are a solid line of width 1.0, CAP_SQUARE,
JOIN_MITER, a miter limit of 10.0.

Method Detail

- createStrokedShape

```java
public
Shape
createStrokedShape​(
Shape
s)
```

Returns a

Shape

whose interior defines the
stroked outline of a specified

Shape

.

**Specified by:** createStrokedShape

in interface

Stroke
**Parameters:** s

- the

Shape

boundary be stroked
**Returns:** the

Shape

of the stroked outline.

- getLineWidth

```java
public float getLineWidth()
```

Returns the line width. Line width is represented in user space,
which is the default-coordinate space used by Java 2D. See the

Graphics2D

class comments for more information on
the user space coordinate system.

**Returns:** the line width of this

BasicStroke

.
**See Also:** Graphics2D

- getEndCap

```java
public int getEndCap()
```

Returns the end cap style.

**Returns:** the end cap style of this

BasicStroke

as one
of the static

int

values that define possible end cap
styles.

- getLineJoin

```java
public int getLineJoin()
```

Returns the line join style.

**Returns:** the line join style of the

BasicStroke

as one
of the static

int

values that define possible line
join styles.

- getMiterLimit

```java
public float getMiterLimit()
```

Returns the limit of miter joins.

**Returns:** the limit of miter joins of the

BasicStroke

.

- getDashArray

```java
public float[] getDashArray()
```

Returns the array representing the lengths of the dash segments.
Alternate entries in the array represent the user space lengths
of the opaque and transparent segments of the dashes.
As the pen moves along the outline of the

Shape

to be stroked, the user space
distance that the pen travels is accumulated. The distance
value is used to index into the dash array.
The pen is opaque when its current cumulative distance maps
to an even element of the dash array and transparent otherwise.

**Returns:** the dash array.

- getDashPhase

```java
public float getDashPhase()
```

Returns the current dash phase.
The dash phase is a distance specified in user coordinates that
represents an offset into the dashing pattern. In other words, the dash
phase defines the point in the dashing pattern that will correspond to
the beginning of the stroke.

**Returns:** the dash phase as a

float

value.

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this stroke.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this stroke.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Tests if a specified object is equal to this

BasicStroke

by first testing if it is a

BasicStroke

and then comparing
its width, join, cap, miter limit, dash, and dash phase attributes with
those of this

BasicStroke

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the specified object to compare to this

BasicStroke
**Returns:** true

if the width, join, cap, miter limit, dash, and
dash phase are the same for both objects;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

createStrokedShape

```java
public
Shape
createStrokedShape​(
Shape
s)
```

Returns a

Shape

whose interior defines the
stroked outline of a specified

Shape

.

**Specified by:** createStrokedShape

in interface

Stroke
**Parameters:** s

- the

Shape

boundary be stroked
**Returns:** the

Shape

of the stroked outline.

---

#### createStrokedShape

public

Shape

createStrokedShape​(

Shape

s)

Returns a

Shape

whose interior defines the
stroked outline of a specified

Shape

.

getLineWidth

```java
public float getLineWidth()
```

Returns the line width. Line width is represented in user space,
which is the default-coordinate space used by Java 2D. See the

Graphics2D

class comments for more information on
the user space coordinate system.

**Returns:** the line width of this

BasicStroke

.
**See Also:** Graphics2D

---

#### getLineWidth

public float getLineWidth()

Returns the line width. Line width is represented in user space,
which is the default-coordinate space used by Java 2D. See the

Graphics2D

class comments for more information on
the user space coordinate system.

getEndCap

```java
public int getEndCap()
```

Returns the end cap style.

**Returns:** the end cap style of this

BasicStroke

as one
of the static

int

values that define possible end cap
styles.

---

#### getEndCap

public int getEndCap()

Returns the end cap style.

getLineJoin

```java
public int getLineJoin()
```

Returns the line join style.

**Returns:** the line join style of the

BasicStroke

as one
of the static

int

values that define possible line
join styles.

---

#### getLineJoin

public int getLineJoin()

Returns the line join style.

getMiterLimit

```java
public float getMiterLimit()
```

Returns the limit of miter joins.

**Returns:** the limit of miter joins of the

BasicStroke

.

---

#### getMiterLimit

public float getMiterLimit()

Returns the limit of miter joins.

getDashArray

```java
public float[] getDashArray()
```

Returns the array representing the lengths of the dash segments.
Alternate entries in the array represent the user space lengths
of the opaque and transparent segments of the dashes.
As the pen moves along the outline of the

Shape

to be stroked, the user space
distance that the pen travels is accumulated. The distance
value is used to index into the dash array.
The pen is opaque when its current cumulative distance maps
to an even element of the dash array and transparent otherwise.

**Returns:** the dash array.

---

#### getDashArray

public float[] getDashArray()

Returns the array representing the lengths of the dash segments.
Alternate entries in the array represent the user space lengths
of the opaque and transparent segments of the dashes.
As the pen moves along the outline of the

Shape

to be stroked, the user space
distance that the pen travels is accumulated. The distance
value is used to index into the dash array.
The pen is opaque when its current cumulative distance maps
to an even element of the dash array and transparent otherwise.

getDashPhase

```java
public float getDashPhase()
```

Returns the current dash phase.
The dash phase is a distance specified in user coordinates that
represents an offset into the dashing pattern. In other words, the dash
phase defines the point in the dashing pattern that will correspond to
the beginning of the stroke.

**Returns:** the dash phase as a

float

value.

---

#### getDashPhase

public float getDashPhase()

Returns the current dash phase.
The dash phase is a distance specified in user coordinates that
represents an offset into the dashing pattern. In other words, the dash
phase defines the point in the dashing pattern that will correspond to
the beginning of the stroke.

hashCode

```java
public int hashCode()
```

Returns the hashcode for this stroke.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this stroke.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hashcode for this stroke.

equals

```java
public boolean equals​(
Object
obj)
```

Tests if a specified object is equal to this

BasicStroke

by first testing if it is a

BasicStroke

and then comparing
its width, join, cap, miter limit, dash, and dash phase attributes with
those of this

BasicStroke

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the specified object to compare to this

BasicStroke
**Returns:** true

if the width, join, cap, miter limit, dash, and
dash phase are the same for both objects;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Tests if a specified object is equal to this

BasicStroke

by first testing if it is a

BasicStroke

and then comparing
its width, join, cap, miter limit, dash, and dash phase attributes with
those of this

BasicStroke

.

---

