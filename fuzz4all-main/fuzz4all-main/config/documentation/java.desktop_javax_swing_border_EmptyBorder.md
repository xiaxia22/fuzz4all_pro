# Class EmptyBorder

**Source:** `java.desktop\javax\swing\border\EmptyBorder.html`

### Class Description

```java
public class
EmptyBorder

extends
AbstractBorder

implements
Serializable
```

A class which provides an empty, transparent border which
takes up space but does no drawing.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

Border

---

### Field Details

#### protected int left

The left inset of the border.

---

#### protected int right

The right inset of the border.

---

#### protected int top

The top inset of the border.

---

#### protected int bottom

The bottom inset of the border.

---

### Constructor Details

#### public EmptyBorder​(int top,
int left,
int bottom,
int right)

Creates an empty border with the specified insets.

**Parameters:**
- top

- the top inset of the border
- left

- the left inset of the border
- bottom

- the bottom inset of the border
- right

- the right inset of the border

---

#### @ConstructorProperties
("borderInsets")
public EmptyBorder​(
Insets
borderInsets)

Creates an empty border with the specified insets.

**Parameters:**
- borderInsets

- the insets of the border

---

### Method Details

#### public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)

Does no drawing by default.

**Specified by:**
- paintBorder

in interface

Border

**Overrides:**
- paintBorder

in class

AbstractBorder

**Parameters:**
- c

- the component for which this border is being painted
- g

- the paint graphics
- x

- the x position of the painted border
- y

- the y position of the painted border
- width

- the width of the painted border
- height

- the height of the painted border

---

#### public
Insets
getBorderInsets​(
Component
c,

Insets
insets)

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:**
- getBorderInsets

in class

AbstractBorder

**Parameters:**
- c

- the component for which this border insets value applies
- insets

- the object to be reinitialized

**Returns:**
- the

insets

object

---

#### public
Insets
getBorderInsets()

Returns the insets of the border.

**Returns:**
- an

Insets

object containing the insets from top, left,
bottom and right

**Since:**
- 1.3

---

#### public boolean isBorderOpaque()

Returns whether or not the border is opaque.
Returns false by default.

**Specified by:**
- isBorderOpaque

in interface

Border

**Overrides:**
- isBorderOpaque

in class

AbstractBorder

**Returns:**
- false

---

### Additional Sections

#### Class EmptyBorder

java.lang.Object

- javax.swing.border.AbstractBorder
- - javax.swing.border.EmptyBorder

javax.swing.border.AbstractBorder

- javax.swing.border.EmptyBorder

javax.swing.border.EmptyBorder

**All Implemented Interfaces:** Serializable

,

Border

**Direct Known Subclasses:** BorderUIResource.EmptyBorderUIResource

,

MatteBorder

```java
public class
EmptyBorder

extends
AbstractBorder

implements
Serializable
```

A class which provides an empty, transparent border which
takes up space but does no drawing.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public class

EmptyBorder

extends

AbstractBorder

implements

Serializable

A class which provides an empty, transparent border which
takes up space but does no drawing.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

bottom

The bottom inset of the border.

protected int

left

The left inset of the border.

protected int

right

The right inset of the border.

protected int

top

The top inset of the border.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EmptyBorder

​(int top,
int left,
int bottom,
int right)

Creates an empty border with the specified insets.

EmptyBorder

​(

Insets

borderInsets)

Creates an empty border with the specified insets.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Insets

getBorderInsets

()

Returns the insets of the border.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

boolean

isBorderOpaque

()

Returns whether or not the border is opaque.

void

paintBorder

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Does no drawing by default.

- Methods declared in class javax.swing.border.

AbstractBorder

getBaseline

,

getBaselineResizeBehavior

,

getBorderInsets

,

getInteriorRectangle

,

getInteriorRectangle

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

protected int

bottom

The bottom inset of the border.

protected int

left

The left inset of the border.

protected int

right

The right inset of the border.

protected int

top

The top inset of the border.

---

#### Field Summary

The bottom inset of the border.

The left inset of the border.

The right inset of the border.

The top inset of the border.

Constructor Summary

Constructors

Constructor

Description

EmptyBorder

​(int top,
int left,
int bottom,
int right)

Creates an empty border with the specified insets.

EmptyBorder

​(

Insets

borderInsets)

Creates an empty border with the specified insets.

---

#### Constructor Summary

Creates an empty border with the specified insets.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Insets

getBorderInsets

()

Returns the insets of the border.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

boolean

isBorderOpaque

()

Returns whether or not the border is opaque.

void

paintBorder

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Does no drawing by default.

- Methods declared in class javax.swing.border.

AbstractBorder

getBaseline

,

getBaselineResizeBehavior

,

getBorderInsets

,

getInteriorRectangle

,

getInteriorRectangle

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

Returns the insets of the border.

Reinitialize the insets parameter with this Border's current Insets.

Returns whether or not the border is opaque.

Does no drawing by default.

Methods declared in class javax.swing.border.

AbstractBorder

getBaseline

,

getBaselineResizeBehavior

,

getBorderInsets

,

getInteriorRectangle

,

getInteriorRectangle

---

#### Methods declared in class javax.swing.border. AbstractBorder

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

- left

```java
protected int left
```

The left inset of the border.

- right

```java
protected int right
```

The right inset of the border.

- top

```java
protected int top
```

The top inset of the border.

- bottom

```java
protected int bottom
```

The bottom inset of the border.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- EmptyBorder

```java
public EmptyBorder​(int top,
int left,
int bottom,
int right)
```

Creates an empty border with the specified insets.

**Parameters:** top

- the top inset of the border
**Parameters:** left

- the left inset of the border
**Parameters:** bottom

- the bottom inset of the border
**Parameters:** right

- the right inset of the border

- EmptyBorder

```java
@ConstructorProperties
("borderInsets")
public EmptyBorder​(
Insets
borderInsets)
```

Creates an empty border with the specified insets.

**Parameters:** borderInsets

- the insets of the border

============ METHOD DETAIL ==========

- Method Detail

- paintBorder

```java
public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Does no drawing by default.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

AbstractBorder
**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

- getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c,

Insets
insets)
```

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

- getBorderInsets

```java
public
Insets
getBorderInsets()
```

Returns the insets of the border.

**Returns:** an

Insets

object containing the insets from top, left,
bottom and right
**Since:** 1.3

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque.
Returns false by default.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** false

Field Detail

- left

```java
protected int left
```

The left inset of the border.

- right

```java
protected int right
```

The right inset of the border.

- top

```java
protected int top
```

The top inset of the border.

- bottom

```java
protected int bottom
```

The bottom inset of the border.

---

#### Field Detail

left

```java
protected int left
```

The left inset of the border.

---

#### left

protected int left

The left inset of the border.

right

```java
protected int right
```

The right inset of the border.

---

#### right

protected int right

The right inset of the border.

top

```java
protected int top
```

The top inset of the border.

---

#### top

protected int top

The top inset of the border.

bottom

```java
protected int bottom
```

The bottom inset of the border.

---

#### bottom

protected int bottom

The bottom inset of the border.

Constructor Detail

- EmptyBorder

```java
public EmptyBorder​(int top,
int left,
int bottom,
int right)
```

Creates an empty border with the specified insets.

**Parameters:** top

- the top inset of the border
**Parameters:** left

- the left inset of the border
**Parameters:** bottom

- the bottom inset of the border
**Parameters:** right

- the right inset of the border

- EmptyBorder

```java
@ConstructorProperties
("borderInsets")
public EmptyBorder​(
Insets
borderInsets)
```

Creates an empty border with the specified insets.

**Parameters:** borderInsets

- the insets of the border

---

#### Constructor Detail

EmptyBorder

```java
public EmptyBorder​(int top,
int left,
int bottom,
int right)
```

Creates an empty border with the specified insets.

**Parameters:** top

- the top inset of the border
**Parameters:** left

- the left inset of the border
**Parameters:** bottom

- the bottom inset of the border
**Parameters:** right

- the right inset of the border

---

#### EmptyBorder

public EmptyBorder​(int top,
int left,
int bottom,
int right)

Creates an empty border with the specified insets.

EmptyBorder

```java
@ConstructorProperties
("borderInsets")
public EmptyBorder​(
Insets
borderInsets)
```

Creates an empty border with the specified insets.

**Parameters:** borderInsets

- the insets of the border

---

#### EmptyBorder

@ConstructorProperties

("borderInsets")
public EmptyBorder​(

Insets

borderInsets)

Creates an empty border with the specified insets.

Method Detail

- paintBorder

```java
public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Does no drawing by default.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

AbstractBorder
**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

- getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c,

Insets
insets)
```

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

- getBorderInsets

```java
public
Insets
getBorderInsets()
```

Returns the insets of the border.

**Returns:** an

Insets

object containing the insets from top, left,
bottom and right
**Since:** 1.3

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque.
Returns false by default.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** false

---

#### Method Detail

paintBorder

```java
public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Does no drawing by default.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

AbstractBorder
**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

---

#### paintBorder

public void paintBorder​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Does no drawing by default.

getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c,

Insets
insets)
```

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

---

#### getBorderInsets

public

Insets

getBorderInsets​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

getBorderInsets

```java
public
Insets
getBorderInsets()
```

Returns the insets of the border.

**Returns:** an

Insets

object containing the insets from top, left,
bottom and right
**Since:** 1.3

---

#### getBorderInsets

public

Insets

getBorderInsets()

Returns the insets of the border.

isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque.
Returns false by default.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** false

---

#### isBorderOpaque

public boolean isBorderOpaque()

Returns whether or not the border is opaque.
Returns false by default.

---

