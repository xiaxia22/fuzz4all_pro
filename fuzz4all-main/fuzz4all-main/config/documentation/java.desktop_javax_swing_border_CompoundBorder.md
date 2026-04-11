# Class CompoundBorder

**Source:** `java.desktop\javax\swing\border\CompoundBorder.html`

### Class Description

```java
public class
CompoundBorder

extends
AbstractBorder
```

A composite Border class used to compose two Border objects
into a single border by nesting an inside Border object within
the insets of an outside Border object.

For example, this class may be used to add blank margin space
to a component with an existing decorative border:

```java
Border border = comp.getBorder();
Border margin = new EmptyBorder(10,10,10,10);
comp.setBorder(new CompoundBorder(border, margin));
```

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

#### protected
Border
outsideBorder

The outside border.

---

#### protected
Border
insideBorder

The inside border.

---

### Constructor Details

#### public CompoundBorder()

Creates a compound border with null outside and inside borders.

---

#### @ConstructorProperties
({"outsideBorder","insideBorder"})
public CompoundBorder​(
Border
outsideBorder,

Border
insideBorder)

Creates a compound border with the specified outside and
inside borders. Either border may be null.

**Parameters:**
- outsideBorder

- the outside border
- insideBorder

- the inside border to be nested

---

### Method Details

#### public boolean isBorderOpaque()

Returns whether or not the compound border is opaque.

**Specified by:**
- isBorderOpaque

in interface

Border

**Overrides:**
- isBorderOpaque

in class

AbstractBorder

**Returns:**
- true

if the inside and outside borders
are each either

null

or opaque;
or

false

otherwise

---

#### public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)

Paints the compound border by painting the outside border
with the specified position and size and then painting the
inside border at the specified position and size offset by
the insets of the outside border.

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
Border
getOutsideBorder()

Returns the outside border object.

**Returns:**
- the outside

Border

object

---

#### public
Border
getInsideBorder()

Returns the inside border object.

**Returns:**
- the inside

Border

object

---

### Additional Sections

#### Class CompoundBorder

java.lang.Object

- javax.swing.border.AbstractBorder
- - javax.swing.border.CompoundBorder

javax.swing.border.AbstractBorder

- javax.swing.border.CompoundBorder

javax.swing.border.CompoundBorder

**All Implemented Interfaces:** Serializable

,

Border

**Direct Known Subclasses:** BorderUIResource.CompoundBorderUIResource

```java
public class
CompoundBorder

extends
AbstractBorder
```

A composite Border class used to compose two Border objects
into a single border by nesting an inside Border object within
the insets of an outside Border object.

For example, this class may be used to add blank margin space
to a component with an existing decorative border:

```java
Border border = comp.getBorder();
Border margin = new EmptyBorder(10,10,10,10);
comp.setBorder(new CompoundBorder(border, margin));
```

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

CompoundBorder

extends

AbstractBorder

A composite Border class used to compose two Border objects
into a single border by nesting an inside Border object within
the insets of an outside Border object.

For example, this class may be used to add blank margin space
to a component with an existing decorative border:

```java
Border border = comp.getBorder();
Border margin = new EmptyBorder(10,10,10,10);
comp.setBorder(new CompoundBorder(border, margin));
```

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

Border border = comp.getBorder();
Border margin = new EmptyBorder(10,10,10,10);
comp.setBorder(new CompoundBorder(border, margin));

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

protected

Border

insideBorder

The inside border.

protected

Border

outsideBorder

The outside border.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CompoundBorder

()

Creates a compound border with null outside and inside borders.

CompoundBorder

​(

Border

outsideBorder,

Border

insideBorder)

Creates a compound border with the specified outside and
inside borders.

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

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

Border

getInsideBorder

()

Returns the inside border object.

Border

getOutsideBorder

()

Returns the outside border object.

boolean

isBorderOpaque

()

Returns whether or not the compound border is opaque.

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

Paints the compound border by painting the outside border
with the specified position and size and then painting the
inside border at the specified position and size offset by
the insets of the outside border.

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

protected

Border

insideBorder

The inside border.

protected

Border

outsideBorder

The outside border.

---

#### Field Summary

The inside border.

The outside border.

Constructor Summary

Constructors

Constructor

Description

CompoundBorder

()

Creates a compound border with null outside and inside borders.

CompoundBorder

​(

Border

outsideBorder,

Border

insideBorder)

Creates a compound border with the specified outside and
inside borders.

---

#### Constructor Summary

Creates a compound border with null outside and inside borders.

Creates a compound border with the specified outside and
inside borders.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

Border

getInsideBorder

()

Returns the inside border object.

Border

getOutsideBorder

()

Returns the outside border object.

boolean

isBorderOpaque

()

Returns whether or not the compound border is opaque.

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

Paints the compound border by painting the outside border
with the specified position and size and then painting the
inside border at the specified position and size offset by
the insets of the outside border.

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

Reinitialize the insets parameter with this Border's current Insets.

Returns the inside border object.

Returns the outside border object.

Returns whether or not the compound border is opaque.

Paints the compound border by painting the outside border
with the specified position and size and then painting the
inside border at the specified position and size offset by
the insets of the outside border.

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

- outsideBorder

```java
protected
Border
outsideBorder
```

The outside border.

- insideBorder

```java
protected
Border
insideBorder
```

The inside border.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CompoundBorder

```java
public CompoundBorder()
```

Creates a compound border with null outside and inside borders.

- CompoundBorder

```java
@ConstructorProperties
({"outsideBorder","insideBorder"})
public CompoundBorder​(
Border
outsideBorder,

Border
insideBorder)
```

Creates a compound border with the specified outside and
inside borders. Either border may be null.

**Parameters:** outsideBorder

- the outside border
**Parameters:** insideBorder

- the inside border to be nested

============ METHOD DETAIL ==========

- Method Detail

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the compound border is opaque.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

if the inside and outside borders
are each either

null

or opaque;
or

false

otherwise

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

Paints the compound border by painting the outside border
with the specified position and size and then painting the
inside border at the specified position and size offset by
the insets of the outside border.

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

- getOutsideBorder

```java
public
Border
getOutsideBorder()
```

Returns the outside border object.

**Returns:** the outside

Border

object

- getInsideBorder

```java
public
Border
getInsideBorder()
```

Returns the inside border object.

**Returns:** the inside

Border

object

Field Detail

- outsideBorder

```java
protected
Border
outsideBorder
```

The outside border.

- insideBorder

```java
protected
Border
insideBorder
```

The inside border.

---

#### Field Detail

outsideBorder

```java
protected
Border
outsideBorder
```

The outside border.

---

#### outsideBorder

protected

Border

outsideBorder

The outside border.

insideBorder

```java
protected
Border
insideBorder
```

The inside border.

---

#### insideBorder

protected

Border

insideBorder

The inside border.

Constructor Detail

- CompoundBorder

```java
public CompoundBorder()
```

Creates a compound border with null outside and inside borders.

- CompoundBorder

```java
@ConstructorProperties
({"outsideBorder","insideBorder"})
public CompoundBorder​(
Border
outsideBorder,

Border
insideBorder)
```

Creates a compound border with the specified outside and
inside borders. Either border may be null.

**Parameters:** outsideBorder

- the outside border
**Parameters:** insideBorder

- the inside border to be nested

---

#### Constructor Detail

CompoundBorder

```java
public CompoundBorder()
```

Creates a compound border with null outside and inside borders.

---

#### CompoundBorder

public CompoundBorder()

Creates a compound border with null outside and inside borders.

CompoundBorder

```java
@ConstructorProperties
({"outsideBorder","insideBorder"})
public CompoundBorder​(
Border
outsideBorder,

Border
insideBorder)
```

Creates a compound border with the specified outside and
inside borders. Either border may be null.

**Parameters:** outsideBorder

- the outside border
**Parameters:** insideBorder

- the inside border to be nested

---

#### CompoundBorder

@ConstructorProperties

({"outsideBorder","insideBorder"})
public CompoundBorder​(

Border

outsideBorder,

Border

insideBorder)

Creates a compound border with the specified outside and
inside borders. Either border may be null.

Method Detail

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the compound border is opaque.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

if the inside and outside borders
are each either

null

or opaque;
or

false

otherwise

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

Paints the compound border by painting the outside border
with the specified position and size and then painting the
inside border at the specified position and size offset by
the insets of the outside border.

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

- getOutsideBorder

```java
public
Border
getOutsideBorder()
```

Returns the outside border object.

**Returns:** the outside

Border

object

- getInsideBorder

```java
public
Border
getInsideBorder()
```

Returns the inside border object.

**Returns:** the inside

Border

object

---

#### Method Detail

isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the compound border is opaque.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

if the inside and outside borders
are each either

null

or opaque;
or

false

otherwise

---

#### isBorderOpaque

public boolean isBorderOpaque()

Returns whether or not the compound border is opaque.

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

Paints the compound border by painting the outside border
with the specified position and size and then painting the
inside border at the specified position and size offset by
the insets of the outside border.

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

Paints the compound border by painting the outside border
with the specified position and size and then painting the
inside border at the specified position and size offset by
the insets of the outside border.

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

getOutsideBorder

```java
public
Border
getOutsideBorder()
```

Returns the outside border object.

**Returns:** the outside

Border

object

---

#### getOutsideBorder

public

Border

getOutsideBorder()

Returns the outside border object.

getInsideBorder

```java
public
Border
getInsideBorder()
```

Returns the inside border object.

**Returns:** the inside

Border

object

---

#### getInsideBorder

public

Border

getInsideBorder()

Returns the inside border object.

---

