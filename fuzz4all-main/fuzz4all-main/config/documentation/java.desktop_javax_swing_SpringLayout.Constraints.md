# Class SpringLayout.Constraints

**Source:** `java.desktop\javax\swing\SpringLayout.Constraints.html`

### Class Description

```java
public static class
SpringLayout.Constraints

extends
Object
```

A

Constraints

object holds the
constraints that govern the way a component's size and position
change in a container controlled by a

SpringLayout

.
A

Constraints

object is
like a

Rectangle

, in that it
has

x

,

y

,

width

, and

height

properties.
In the

Constraints

object, however,
these properties have

Spring

values instead of integers.
In addition,
a

Constraints

object
can be manipulated as four edges
-- north, south, east, and west --
using the

constraint

property.

The following formulas are always true
for a

Constraints

object (here WEST and

x

are synonyms, as are and NORTH and

y

):

```java
EAST = WEST + WIDTH
SOUTH = NORTH + HEIGHT
HORIZONTAL_CENTER = WEST + WIDTH/2
VERTICAL_CENTER = NORTH + HEIGHT/2
ABSOLUTE_BASELINE = NORTH + RELATIVE_BASELINE*
```

For example, if you have specified the WIDTH and WEST (X) location
the EAST is calculated as WEST + WIDTH. If you instead specified
the WIDTH and EAST locations the WEST (X) location is then calculated
as EAST - WIDTH.

[RELATIVE_BASELINE is a private constraint that is set automatically when
the SpringLayout.Constraints(Component) constructor is called or when
a constraints object is registered with a SpringLayout object.]

Note

: In this document,
operators represent methods
in the

Spring

class.
For example, "a + b" is equal to

Spring.sum(a, b)

,
and "a - b" is equal to

Spring.sum(a, Spring.minus(b))

.
See the

Spring API documentation

for further details
of spring arithmetic.

Because a

Constraints

object's properties --
representing its edges, size, and location -- can all be set
independently and yet are interrelated,
a

Constraints

object can become

over-constrained

.
For example, if the

WEST

,

WIDTH

and

EAST

edges are all set, steps must be taken to ensure that
the first of the formulas above holds. To do this, the

Constraints

object throws away the

least recently set

constraint so as to make the formulas hold.

**Enclosing class:** SpringLayout

---

### Field Details

*No entries found.*

### Constructor Details

#### public Constraints()

Creates an empty

Constraints

object.

---

#### public Constraints​(
Spring
x,

Spring
y)

Creates a

Constraints

object with the
specified values for its

x

and

y

properties.
The

height

and

width

springs
have

null

values.

**Parameters:**
- x

- the spring controlling the component's

x

value
- y

- the spring controlling the component's

y

value

---

#### public Constraints​(
Spring
x,

Spring
y,

Spring
width,

Spring
height)

Creates a

Constraints

object with the
specified values for its

x

,

y

,

width

,
and

height

properties.
Note: If the

SpringLayout

class
encounters

null

values in the

Constraints

object of a given component,
it replaces them with suitable defaults.

**Parameters:**
- x

- the spring value for the

x

property
- y

- the spring value for the

y

property
- width

- the spring value for the

width

property
- height

- the spring value for the

height

property

---

#### public Constraints​(
Component
c)

Creates a

Constraints

object with
suitable

x

,

y

,

width

and

height

springs for component,

c

.
The

x

and

y

springs are constant
springs initialised with the component's location at
the time this method is called. The

width

and

height

springs are special springs, created by
the

Spring.width()

and

Spring.height()

methods, which track the size characteristics of the component
when they change.

**Parameters:**
- c

- the component whose characteristics will be reflected by this Constraints object

**Throws:**
- NullPointerException

- if

c

is null.

**Since:**
- 1.5

---

### Method Details

#### public void setX​(
Spring
x)

Sets the

x

property,
which controls the

x

value
of a component's location.

**Parameters:**
- x

- the spring controlling the

x

value
of a component's location

**See Also:**
- getX()

,

SpringLayout.Constraints

---

#### public
Spring
getX()

Returns the value of the

x

property.

**Returns:**
- the spring controlling the

x

value
of a component's location

**See Also:**
- setX(javax.swing.Spring)

,

SpringLayout.Constraints

---

#### public void setY​(
Spring
y)

Sets the

y

property,
which controls the

y

value
of a component's location.

**Parameters:**
- y

- the spring controlling the

y

value
of a component's location

**See Also:**
- getY()

,

SpringLayout.Constraints

---

#### public
Spring
getY()

Returns the value of the

y

property.

**Returns:**
- the spring controlling the

y

value
of a component's location

**See Also:**
- setY(javax.swing.Spring)

,

SpringLayout.Constraints

---

#### public void setWidth​(
Spring
width)

Sets the

width

property,
which controls the width of a component.

**Parameters:**
- width

- the spring controlling the width of this

Constraints

object

**See Also:**
- getWidth()

,

SpringLayout.Constraints

---

#### public
Spring
getWidth()

Returns the value of the

width

property.

**Returns:**
- the spring controlling the width of a component

**See Also:**
- setWidth(javax.swing.Spring)

,

SpringLayout.Constraints

---

#### public void setHeight​(
Spring
height)

Sets the

height

property,
which controls the height of a component.

**Parameters:**
- height

- the spring controlling the height of this

Constraints

object

**See Also:**
- getHeight()

,

SpringLayout.Constraints

---

#### public
Spring
getHeight()

Returns the value of the

height

property.

**Returns:**
- the spring controlling the height of a component

**See Also:**
- setHeight(javax.swing.Spring)

,

SpringLayout.Constraints

---

#### public void setConstraint​(
String
edgeName,

Spring
s)

Sets the spring controlling the specified edge.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,
no action is taken. For a

null

edge, a

NullPointerException

is thrown.

Note:

This method can affect

x

and

y

values
previously set for this

Constraints

.

**Parameters:**
- edgeName

- the edge to be set
- s

- the spring controlling the specified edge

**Throws:**
- NullPointerException

- if

edgeName

is

null

**See Also:**
- getConstraint(java.lang.String)

,

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

,

SpringLayout.HEIGHT

,

SpringLayout.Constraints

---

#### public
Spring
getConstraint​(
String
edgeName)

Returns the value of the specified edge, which may be
a derived value, or even

null

.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,

null

will be returned. Throws

NullPointerException

for a

null

edge.

**Parameters:**
- edgeName

- the edge whose value
is to be returned

**Returns:**
- the spring controlling the specified edge, may be

null

**Throws:**
- NullPointerException

- if

edgeName

is

null

**See Also:**
- setConstraint(java.lang.String, javax.swing.Spring)

,

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

,

SpringLayout.HEIGHT

,

SpringLayout.Constraints

---

### Additional Sections

#### Class SpringLayout.Constraints

java.lang.Object

- javax.swing.SpringLayout.Constraints

javax.swing.SpringLayout.Constraints

**Enclosing class:** SpringLayout

```java
public static class
SpringLayout.Constraints

extends
Object
```

A

Constraints

object holds the
constraints that govern the way a component's size and position
change in a container controlled by a

SpringLayout

.
A

Constraints

object is
like a

Rectangle

, in that it
has

x

,

y

,

width

, and

height

properties.
In the

Constraints

object, however,
these properties have

Spring

values instead of integers.
In addition,
a

Constraints

object
can be manipulated as four edges
-- north, south, east, and west --
using the

constraint

property.

The following formulas are always true
for a

Constraints

object (here WEST and

x

are synonyms, as are and NORTH and

y

):

```java
EAST = WEST + WIDTH
SOUTH = NORTH + HEIGHT
HORIZONTAL_CENTER = WEST + WIDTH/2
VERTICAL_CENTER = NORTH + HEIGHT/2
ABSOLUTE_BASELINE = NORTH + RELATIVE_BASELINE*
```

For example, if you have specified the WIDTH and WEST (X) location
the EAST is calculated as WEST + WIDTH. If you instead specified
the WIDTH and EAST locations the WEST (X) location is then calculated
as EAST - WIDTH.

[RELATIVE_BASELINE is a private constraint that is set automatically when
the SpringLayout.Constraints(Component) constructor is called or when
a constraints object is registered with a SpringLayout object.]

Note

: In this document,
operators represent methods
in the

Spring

class.
For example, "a + b" is equal to

Spring.sum(a, b)

,
and "a - b" is equal to

Spring.sum(a, Spring.minus(b))

.
See the

Spring API documentation

for further details
of spring arithmetic.

Because a

Constraints

object's properties --
representing its edges, size, and location -- can all be set
independently and yet are interrelated,
a

Constraints

object can become

over-constrained

.
For example, if the

WEST

,

WIDTH

and

EAST

edges are all set, steps must be taken to ensure that
the first of the formulas above holds. To do this, the

Constraints

object throws away the

least recently set

constraint so as to make the formulas hold.

**Since:** 1.4

public static class

SpringLayout.Constraints

extends

Object

A

Constraints

object holds the
constraints that govern the way a component's size and position
change in a container controlled by a

SpringLayout

.
A

Constraints

object is
like a

Rectangle

, in that it
has

x

,

y

,

width

, and

height

properties.
In the

Constraints

object, however,
these properties have

Spring

values instead of integers.
In addition,
a

Constraints

object
can be manipulated as four edges
-- north, south, east, and west --
using the

constraint

property.

The following formulas are always true
for a

Constraints

object (here WEST and

x

are synonyms, as are and NORTH and

y

):

```java
EAST = WEST + WIDTH
SOUTH = NORTH + HEIGHT
HORIZONTAL_CENTER = WEST + WIDTH/2
VERTICAL_CENTER = NORTH + HEIGHT/2
ABSOLUTE_BASELINE = NORTH + RELATIVE_BASELINE*
```

For example, if you have specified the WIDTH and WEST (X) location
the EAST is calculated as WEST + WIDTH. If you instead specified
the WIDTH and EAST locations the WEST (X) location is then calculated
as EAST - WIDTH.

[RELATIVE_BASELINE is a private constraint that is set automatically when
the SpringLayout.Constraints(Component) constructor is called or when
a constraints object is registered with a SpringLayout object.]

Note

: In this document,
operators represent methods
in the

Spring

class.
For example, "a + b" is equal to

Spring.sum(a, b)

,
and "a - b" is equal to

Spring.sum(a, Spring.minus(b))

.
See the

Spring API documentation

for further details
of spring arithmetic.

Because a

Constraints

object's properties --
representing its edges, size, and location -- can all be set
independently and yet are interrelated,
a

Constraints

object can become

over-constrained

.
For example, if the

WEST

,

WIDTH

and

EAST

edges are all set, steps must be taken to ensure that
the first of the formulas above holds. To do this, the

Constraints

object throws away the

least recently set

constraint so as to make the formulas hold.

The following formulas are always true
for a

Constraints

object (here WEST and

x

are synonyms, as are and NORTH and

y

):

```java
EAST = WEST + WIDTH
SOUTH = NORTH + HEIGHT
HORIZONTAL_CENTER = WEST + WIDTH/2
VERTICAL_CENTER = NORTH + HEIGHT/2
ABSOLUTE_BASELINE = NORTH + RELATIVE_BASELINE*
```

For example, if you have specified the WIDTH and WEST (X) location
the EAST is calculated as WEST + WIDTH. If you instead specified
the WIDTH and EAST locations the WEST (X) location is then calculated
as EAST - WIDTH.

[RELATIVE_BASELINE is a private constraint that is set automatically when
the SpringLayout.Constraints(Component) constructor is called or when
a constraints object is registered with a SpringLayout object.]

Note

: In this document,
operators represent methods
in the

Spring

class.
For example, "a + b" is equal to

Spring.sum(a, b)

,
and "a - b" is equal to

Spring.sum(a, Spring.minus(b))

.
See the

Spring API documentation

for further details
of spring arithmetic.

Because a

Constraints

object's properties --
representing its edges, size, and location -- can all be set
independently and yet are interrelated,
a

Constraints

object can become

over-constrained

.
For example, if the

WEST

,

WIDTH

and

EAST

edges are all set, steps must be taken to ensure that
the first of the formulas above holds. To do this, the

Constraints

object throws away the

least recently set

constraint so as to make the formulas hold.

EAST = WEST + WIDTH
SOUTH = NORTH + HEIGHT
HORIZONTAL_CENTER = WEST + WIDTH/2
VERTICAL_CENTER = NORTH + HEIGHT/2
ABSOLUTE_BASELINE = NORTH + RELATIVE_BASELINE*

For example, if you have specified the WIDTH and WEST (X) location
the EAST is calculated as WEST + WIDTH. If you instead specified
the WIDTH and EAST locations the WEST (X) location is then calculated
as EAST - WIDTH.

[RELATIVE_BASELINE is a private constraint that is set automatically when
the SpringLayout.Constraints(Component) constructor is called or when
a constraints object is registered with a SpringLayout object.]

Note

: In this document,
operators represent methods
in the

Spring

class.
For example, "a + b" is equal to

Spring.sum(a, b)

,
and "a - b" is equal to

Spring.sum(a, Spring.minus(b))

.
See the

Spring API documentation

for further details
of spring arithmetic.

Because a

Constraints

object's properties --
representing its edges, size, and location -- can all be set
independently and yet are interrelated,
a

Constraints

object can become

over-constrained

.
For example, if the

WEST

,

WIDTH

and

EAST

edges are all set, steps must be taken to ensure that
the first of the formulas above holds. To do this, the

Constraints

object throws away the

least recently set

constraint so as to make the formulas hold.

[RELATIVE_BASELINE is a private constraint that is set automatically when
the SpringLayout.Constraints(Component) constructor is called or when
a constraints object is registered with a SpringLayout object.]

Note

: In this document,
operators represent methods
in the

Spring

class.
For example, "a + b" is equal to

Spring.sum(a, b)

,
and "a - b" is equal to

Spring.sum(a, Spring.minus(b))

.
See the

Spring API documentation

for further details
of spring arithmetic.

Because a

Constraints

object's properties --
representing its edges, size, and location -- can all be set
independently and yet are interrelated,
a

Constraints

object can become

over-constrained

.
For example, if the

WEST

,

WIDTH

and

EAST

edges are all set, steps must be taken to ensure that
the first of the formulas above holds. To do this, the

Constraints

object throws away the

least recently set

constraint so as to make the formulas hold.

Note

: In this document,
operators represent methods
in the

Spring

class.
For example, "a + b" is equal to

Spring.sum(a, b)

,
and "a - b" is equal to

Spring.sum(a, Spring.minus(b))

.
See the

Spring API documentation

for further details
of spring arithmetic.

Because a

Constraints

object's properties --
representing its edges, size, and location -- can all be set
independently and yet are interrelated,
a

Constraints

object can become

over-constrained

.
For example, if the

WEST

,

WIDTH

and

EAST

edges are all set, steps must be taken to ensure that
the first of the formulas above holds. To do this, the

Constraints

object throws away the

least recently set

constraint so as to make the formulas hold.

Because a

Constraints

object's properties --
representing its edges, size, and location -- can all be set
independently and yet are interrelated,
a

Constraints

object can become

over-constrained

.
For example, if the

WEST

,

WIDTH

and

EAST

edges are all set, steps must be taken to ensure that
the first of the formulas above holds. To do this, the

Constraints

object throws away the

least recently set

constraint so as to make the formulas hold.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Constraints

()

Creates an empty

Constraints

object.

Constraints

​(

Component

c)

Creates a

Constraints

object with
suitable

x

,

y

,

width

and

height

springs for component,

c

.

Constraints

​(

Spring

x,

Spring

y)

Creates a

Constraints

object with the
specified values for its

x

and

y

properties.

Constraints

​(

Spring

x,

Spring

y,

Spring

width,

Spring

height)

Creates a

Constraints

object with the
specified values for its

x

,

y

,

width

,
and

height

properties.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Spring

getConstraint

​(

String

edgeName)

Returns the value of the specified edge, which may be
a derived value, or even

null

.

Spring

getHeight

()

Returns the value of the

height

property.

Spring

getWidth

()

Returns the value of the

width

property.

Spring

getX

()

Returns the value of the

x

property.

Spring

getY

()

Returns the value of the

y

property.

void

setConstraint

​(

String

edgeName,

Spring

s)

Sets the spring controlling the specified edge.

void

setHeight

​(

Spring

height)

Sets the

height

property,
which controls the height of a component.

void

setWidth

​(

Spring

width)

Sets the

width

property,
which controls the width of a component.

void

setX

​(

Spring

x)

Sets the

x

property,
which controls the

x

value
of a component's location.

void

setY

​(

Spring

y)

Sets the

y

property,
which controls the

y

value
of a component's location.

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

Constraints

()

Creates an empty

Constraints

object.

Constraints

​(

Component

c)

Creates a

Constraints

object with
suitable

x

,

y

,

width

and

height

springs for component,

c

.

Constraints

​(

Spring

x,

Spring

y)

Creates a

Constraints

object with the
specified values for its

x

and

y

properties.

Constraints

​(

Spring

x,

Spring

y,

Spring

width,

Spring

height)

Creates a

Constraints

object with the
specified values for its

x

,

y

,

width

,
and

height

properties.

---

#### Constructor Summary

Creates an empty

Constraints

object.

Creates a

Constraints

object with
suitable

x

,

y

,

width

and

height

springs for component,

c

.

Creates a

Constraints

object with the
specified values for its

x

and

y

properties.

Creates a

Constraints

object with the
specified values for its

x

,

y

,

width

,
and

height

properties.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Spring

getConstraint

​(

String

edgeName)

Returns the value of the specified edge, which may be
a derived value, or even

null

.

Spring

getHeight

()

Returns the value of the

height

property.

Spring

getWidth

()

Returns the value of the

width

property.

Spring

getX

()

Returns the value of the

x

property.

Spring

getY

()

Returns the value of the

y

property.

void

setConstraint

​(

String

edgeName,

Spring

s)

Sets the spring controlling the specified edge.

void

setHeight

​(

Spring

height)

Sets the

height

property,
which controls the height of a component.

void

setWidth

​(

Spring

width)

Sets the

width

property,
which controls the width of a component.

void

setX

​(

Spring

x)

Sets the

x

property,
which controls the

x

value
of a component's location.

void

setY

​(

Spring

y)

Sets the

y

property,
which controls the

y

value
of a component's location.

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

Returns the value of the specified edge, which may be
a derived value, or even

null

.

Returns the value of the

height

property.

Returns the value of the

width

property.

Returns the value of the

x

property.

Returns the value of the

y

property.

Sets the spring controlling the specified edge.

Sets the

height

property,
which controls the height of a component.

Sets the

width

property,
which controls the width of a component.

Sets the

x

property,
which controls the

x

value
of a component's location.

Sets the

y

property,
which controls the

y

value
of a component's location.

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

- Constraints

```java
public Constraints()
```

Creates an empty

Constraints

object.

- Constraints

```java
public Constraints​(
Spring
x,

Spring
y)
```

Creates a

Constraints

object with the
specified values for its

x

and

y

properties.
The

height

and

width

springs
have

null

values.

**Parameters:** x

- the spring controlling the component's

x

value
**Parameters:** y

- the spring controlling the component's

y

value

- Constraints

```java
public Constraints​(
Spring
x,

Spring
y,

Spring
width,

Spring
height)
```

Creates a

Constraints

object with the
specified values for its

x

,

y

,

width

,
and

height

properties.
Note: If the

SpringLayout

class
encounters

null

values in the

Constraints

object of a given component,
it replaces them with suitable defaults.

**Parameters:** x

- the spring value for the

x

property
**Parameters:** y

- the spring value for the

y

property
**Parameters:** width

- the spring value for the

width

property
**Parameters:** height

- the spring value for the

height

property

- Constraints

```java
public Constraints​(
Component
c)
```

Creates a

Constraints

object with
suitable

x

,

y

,

width

and

height

springs for component,

c

.
The

x

and

y

springs are constant
springs initialised with the component's location at
the time this method is called. The

width

and

height

springs are special springs, created by
the

Spring.width()

and

Spring.height()

methods, which track the size characteristics of the component
when they change.

**Parameters:** c

- the component whose characteristics will be reflected by this Constraints object
**Throws:** NullPointerException

- if

c

is null.
**Since:** 1.5

============ METHOD DETAIL ==========

- Method Detail

- setX

```java
public void setX​(
Spring
x)
```

Sets the

x

property,
which controls the

x

value
of a component's location.

**Parameters:** x

- the spring controlling the

x

value
of a component's location
**See Also:** getX()

,

SpringLayout.Constraints

- getX

```java
public
Spring
getX()
```

Returns the value of the

x

property.

**Returns:** the spring controlling the

x

value
of a component's location
**See Also:** setX(javax.swing.Spring)

,

SpringLayout.Constraints

- setY

```java
public void setY​(
Spring
y)
```

Sets the

y

property,
which controls the

y

value
of a component's location.

**Parameters:** y

- the spring controlling the

y

value
of a component's location
**See Also:** getY()

,

SpringLayout.Constraints

- getY

```java
public
Spring
getY()
```

Returns the value of the

y

property.

**Returns:** the spring controlling the

y

value
of a component's location
**See Also:** setY(javax.swing.Spring)

,

SpringLayout.Constraints

- setWidth

```java
public void setWidth​(
Spring
width)
```

Sets the

width

property,
which controls the width of a component.

**Parameters:** width

- the spring controlling the width of this

Constraints

object
**See Also:** getWidth()

,

SpringLayout.Constraints

- getWidth

```java
public
Spring
getWidth()
```

Returns the value of the

width

property.

**Returns:** the spring controlling the width of a component
**See Also:** setWidth(javax.swing.Spring)

,

SpringLayout.Constraints

- setHeight

```java
public void setHeight​(
Spring
height)
```

Sets the

height

property,
which controls the height of a component.

**Parameters:** height

- the spring controlling the height of this

Constraints

object
**See Also:** getHeight()

,

SpringLayout.Constraints

- getHeight

```java
public
Spring
getHeight()
```

Returns the value of the

height

property.

**Returns:** the spring controlling the height of a component
**See Also:** setHeight(javax.swing.Spring)

,

SpringLayout.Constraints

- setConstraint

```java
public void setConstraint​(
String
edgeName,

Spring
s)
```

Sets the spring controlling the specified edge.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,
no action is taken. For a

null

edge, a

NullPointerException

is thrown.

Note:

This method can affect

x

and

y

values
previously set for this

Constraints

.

**Parameters:** edgeName

- the edge to be set
**Parameters:** s

- the spring controlling the specified edge
**Throws:** NullPointerException

- if

edgeName

is

null
**See Also:** getConstraint(java.lang.String)

,

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

,

SpringLayout.HEIGHT

,

SpringLayout.Constraints

- getConstraint

```java
public
Spring
getConstraint​(
String
edgeName)
```

Returns the value of the specified edge, which may be
a derived value, or even

null

.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,

null

will be returned. Throws

NullPointerException

for a

null

edge.

**Parameters:** edgeName

- the edge whose value
is to be returned
**Returns:** the spring controlling the specified edge, may be

null
**Throws:** NullPointerException

- if

edgeName

is

null
**See Also:** setConstraint(java.lang.String, javax.swing.Spring)

,

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

,

SpringLayout.HEIGHT

,

SpringLayout.Constraints

Constructor Detail

- Constraints

```java
public Constraints()
```

Creates an empty

Constraints

object.

- Constraints

```java
public Constraints​(
Spring
x,

Spring
y)
```

Creates a

Constraints

object with the
specified values for its

x

and

y

properties.
The

height

and

width

springs
have

null

values.

**Parameters:** x

- the spring controlling the component's

x

value
**Parameters:** y

- the spring controlling the component's

y

value

- Constraints

```java
public Constraints​(
Spring
x,

Spring
y,

Spring
width,

Spring
height)
```

Creates a

Constraints

object with the
specified values for its

x

,

y

,

width

,
and

height

properties.
Note: If the

SpringLayout

class
encounters

null

values in the

Constraints

object of a given component,
it replaces them with suitable defaults.

**Parameters:** x

- the spring value for the

x

property
**Parameters:** y

- the spring value for the

y

property
**Parameters:** width

- the spring value for the

width

property
**Parameters:** height

- the spring value for the

height

property

- Constraints

```java
public Constraints​(
Component
c)
```

Creates a

Constraints

object with
suitable

x

,

y

,

width

and

height

springs for component,

c

.
The

x

and

y

springs are constant
springs initialised with the component's location at
the time this method is called. The

width

and

height

springs are special springs, created by
the

Spring.width()

and

Spring.height()

methods, which track the size characteristics of the component
when they change.

**Parameters:** c

- the component whose characteristics will be reflected by this Constraints object
**Throws:** NullPointerException

- if

c

is null.
**Since:** 1.5

---

#### Constructor Detail

Constraints

```java
public Constraints()
```

Creates an empty

Constraints

object.

---

#### Constraints

public Constraints()

Creates an empty

Constraints

object.

Constraints

```java
public Constraints​(
Spring
x,

Spring
y)
```

Creates a

Constraints

object with the
specified values for its

x

and

y

properties.
The

height

and

width

springs
have

null

values.

**Parameters:** x

- the spring controlling the component's

x

value
**Parameters:** y

- the spring controlling the component's

y

value

---

#### Constraints

public Constraints​(

Spring

x,

Spring

y)

Creates a

Constraints

object with the
specified values for its

x

and

y

properties.
The

height

and

width

springs
have

null

values.

Constraints

```java
public Constraints​(
Spring
x,

Spring
y,

Spring
width,

Spring
height)
```

Creates a

Constraints

object with the
specified values for its

x

,

y

,

width

,
and

height

properties.
Note: If the

SpringLayout

class
encounters

null

values in the

Constraints

object of a given component,
it replaces them with suitable defaults.

**Parameters:** x

- the spring value for the

x

property
**Parameters:** y

- the spring value for the

y

property
**Parameters:** width

- the spring value for the

width

property
**Parameters:** height

- the spring value for the

height

property

---

#### Constraints

public Constraints​(

Spring

x,

Spring

y,

Spring

width,

Spring

height)

Creates a

Constraints

object with the
specified values for its

x

,

y

,

width

,
and

height

properties.
Note: If the

SpringLayout

class
encounters

null

values in the

Constraints

object of a given component,
it replaces them with suitable defaults.

Constraints

```java
public Constraints​(
Component
c)
```

Creates a

Constraints

object with
suitable

x

,

y

,

width

and

height

springs for component,

c

.
The

x

and

y

springs are constant
springs initialised with the component's location at
the time this method is called. The

width

and

height

springs are special springs, created by
the

Spring.width()

and

Spring.height()

methods, which track the size characteristics of the component
when they change.

**Parameters:** c

- the component whose characteristics will be reflected by this Constraints object
**Throws:** NullPointerException

- if

c

is null.
**Since:** 1.5

---

#### Constraints

public Constraints​(

Component

c)

Creates a

Constraints

object with
suitable

x

,

y

,

width

and

height

springs for component,

c

.
The

x

and

y

springs are constant
springs initialised with the component's location at
the time this method is called. The

width

and

height

springs are special springs, created by
the

Spring.width()

and

Spring.height()

methods, which track the size characteristics of the component
when they change.

Method Detail

- setX

```java
public void setX​(
Spring
x)
```

Sets the

x

property,
which controls the

x

value
of a component's location.

**Parameters:** x

- the spring controlling the

x

value
of a component's location
**See Also:** getX()

,

SpringLayout.Constraints

- getX

```java
public
Spring
getX()
```

Returns the value of the

x

property.

**Returns:** the spring controlling the

x

value
of a component's location
**See Also:** setX(javax.swing.Spring)

,

SpringLayout.Constraints

- setY

```java
public void setY​(
Spring
y)
```

Sets the

y

property,
which controls the

y

value
of a component's location.

**Parameters:** y

- the spring controlling the

y

value
of a component's location
**See Also:** getY()

,

SpringLayout.Constraints

- getY

```java
public
Spring
getY()
```

Returns the value of the

y

property.

**Returns:** the spring controlling the

y

value
of a component's location
**See Also:** setY(javax.swing.Spring)

,

SpringLayout.Constraints

- setWidth

```java
public void setWidth​(
Spring
width)
```

Sets the

width

property,
which controls the width of a component.

**Parameters:** width

- the spring controlling the width of this

Constraints

object
**See Also:** getWidth()

,

SpringLayout.Constraints

- getWidth

```java
public
Spring
getWidth()
```

Returns the value of the

width

property.

**Returns:** the spring controlling the width of a component
**See Also:** setWidth(javax.swing.Spring)

,

SpringLayout.Constraints

- setHeight

```java
public void setHeight​(
Spring
height)
```

Sets the

height

property,
which controls the height of a component.

**Parameters:** height

- the spring controlling the height of this

Constraints

object
**See Also:** getHeight()

,

SpringLayout.Constraints

- getHeight

```java
public
Spring
getHeight()
```

Returns the value of the

height

property.

**Returns:** the spring controlling the height of a component
**See Also:** setHeight(javax.swing.Spring)

,

SpringLayout.Constraints

- setConstraint

```java
public void setConstraint​(
String
edgeName,

Spring
s)
```

Sets the spring controlling the specified edge.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,
no action is taken. For a

null

edge, a

NullPointerException

is thrown.

Note:

This method can affect

x

and

y

values
previously set for this

Constraints

.

**Parameters:** edgeName

- the edge to be set
**Parameters:** s

- the spring controlling the specified edge
**Throws:** NullPointerException

- if

edgeName

is

null
**See Also:** getConstraint(java.lang.String)

,

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

,

SpringLayout.HEIGHT

,

SpringLayout.Constraints

- getConstraint

```java
public
Spring
getConstraint​(
String
edgeName)
```

Returns the value of the specified edge, which may be
a derived value, or even

null

.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,

null

will be returned. Throws

NullPointerException

for a

null

edge.

**Parameters:** edgeName

- the edge whose value
is to be returned
**Returns:** the spring controlling the specified edge, may be

null
**Throws:** NullPointerException

- if

edgeName

is

null
**See Also:** setConstraint(java.lang.String, javax.swing.Spring)

,

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

,

SpringLayout.HEIGHT

,

SpringLayout.Constraints

---

#### Method Detail

setX

```java
public void setX​(
Spring
x)
```

Sets the

x

property,
which controls the

x

value
of a component's location.

**Parameters:** x

- the spring controlling the

x

value
of a component's location
**See Also:** getX()

,

SpringLayout.Constraints

---

#### setX

public void setX​(

Spring

x)

Sets the

x

property,
which controls the

x

value
of a component's location.

getX

```java
public
Spring
getX()
```

Returns the value of the

x

property.

**Returns:** the spring controlling the

x

value
of a component's location
**See Also:** setX(javax.swing.Spring)

,

SpringLayout.Constraints

---

#### getX

public

Spring

getX()

Returns the value of the

x

property.

setY

```java
public void setY​(
Spring
y)
```

Sets the

y

property,
which controls the

y

value
of a component's location.

**Parameters:** y

- the spring controlling the

y

value
of a component's location
**See Also:** getY()

,

SpringLayout.Constraints

---

#### setY

public void setY​(

Spring

y)

Sets the

y

property,
which controls the

y

value
of a component's location.

getY

```java
public
Spring
getY()
```

Returns the value of the

y

property.

**Returns:** the spring controlling the

y

value
of a component's location
**See Also:** setY(javax.swing.Spring)

,

SpringLayout.Constraints

---

#### getY

public

Spring

getY()

Returns the value of the

y

property.

setWidth

```java
public void setWidth​(
Spring
width)
```

Sets the

width

property,
which controls the width of a component.

**Parameters:** width

- the spring controlling the width of this

Constraints

object
**See Also:** getWidth()

,

SpringLayout.Constraints

---

#### setWidth

public void setWidth​(

Spring

width)

Sets the

width

property,
which controls the width of a component.

getWidth

```java
public
Spring
getWidth()
```

Returns the value of the

width

property.

**Returns:** the spring controlling the width of a component
**See Also:** setWidth(javax.swing.Spring)

,

SpringLayout.Constraints

---

#### getWidth

public

Spring

getWidth()

Returns the value of the

width

property.

setHeight

```java
public void setHeight​(
Spring
height)
```

Sets the

height

property,
which controls the height of a component.

**Parameters:** height

- the spring controlling the height of this

Constraints

object
**See Also:** getHeight()

,

SpringLayout.Constraints

---

#### setHeight

public void setHeight​(

Spring

height)

Sets the

height

property,
which controls the height of a component.

getHeight

```java
public
Spring
getHeight()
```

Returns the value of the

height

property.

**Returns:** the spring controlling the height of a component
**See Also:** setHeight(javax.swing.Spring)

,

SpringLayout.Constraints

---

#### getHeight

public

Spring

getHeight()

Returns the value of the

height

property.

setConstraint

```java
public void setConstraint​(
String
edgeName,

Spring
s)
```

Sets the spring controlling the specified edge.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,
no action is taken. For a

null

edge, a

NullPointerException

is thrown.

Note:

This method can affect

x

and

y

values
previously set for this

Constraints

.

**Parameters:** edgeName

- the edge to be set
**Parameters:** s

- the spring controlling the specified edge
**Throws:** NullPointerException

- if

edgeName

is

null
**See Also:** getConstraint(java.lang.String)

,

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

,

SpringLayout.HEIGHT

,

SpringLayout.Constraints

---

#### setConstraint

public void setConstraint​(

String

edgeName,

Spring

s)

Sets the spring controlling the specified edge.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,
no action is taken. For a

null

edge, a

NullPointerException

is thrown.

Note:

This method can affect

x

and

y

values
previously set for this

Constraints

.

Note:

This method can affect

x

and

y

values
previously set for this

Constraints

.

getConstraint

```java
public
Spring
getConstraint​(
String
edgeName)
```

Returns the value of the specified edge, which may be
a derived value, or even

null

.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,

null

will be returned. Throws

NullPointerException

for a

null

edge.

**Parameters:** edgeName

- the edge whose value
is to be returned
**Returns:** the spring controlling the specified edge, may be

null
**Throws:** NullPointerException

- if

edgeName

is

null
**See Also:** setConstraint(java.lang.String, javax.swing.Spring)

,

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

,

SpringLayout.HEIGHT

,

SpringLayout.Constraints

---

#### getConstraint

public

Spring

getConstraint​(

String

edgeName)

Returns the value of the specified edge, which may be
a derived value, or even

null

.
The edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.HORIZONTAL_CENTER

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.BASELINE

,

SpringLayout.WIDTH

or

SpringLayout.HEIGHT

.
For any other

String

value passed as the edge,

null

will be returned. Throws

NullPointerException

for a

null

edge.

---

