# Class AbstractBorder

**Source:** `java.desktop\javax\swing\border\AbstractBorder.html`

### Class Description

```java
public abstract class
AbstractBorder

extends
Object

implements
Border
,
Serializable
```

A class that implements an empty border with no size.
This provides a convenient base class from which other border
classes can be easily derived.

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

*No entries found.*

### Constructor Details

#### public AbstractBorder()

*No description found.*

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

This default implementation does no painting.

**Specified by:**
- paintBorder

in interface

Border

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
c)

This default implementation returns a new

Insets

object
that is initialized by the

getBorderInsets(Component,Insets)

method.
By default the

top

,

left

,

bottom

,
and

right

fields are set to

0

.

**Specified by:**
- getBorderInsets

in interface

Border

**Parameters:**
- c

- the component for which this border insets value applies

**Returns:**
- a new

Insets

object

---

#### public
Insets
getBorderInsets​(
Component
c,

Insets
insets)

Reinitializes the insets parameter with this Border's current Insets.

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

#### public boolean isBorderOpaque()

This default implementation returns false.

**Specified by:**
- isBorderOpaque

in interface

Border

**Returns:**
- false

---

#### public
Rectangle
getInteriorRectangle​(
Component
c,
int x,
int y,
int width,
int height)

This convenience method calls the static method.

**Parameters:**
- c

- the component for which this border is being computed
- x

- the x position of the border
- y

- the y position of the border
- width

- the width of the border
- height

- the height of the border

**Returns:**
- a

Rectangle

containing the interior coordinates

---

#### public static
Rectangle
getInteriorRectangle​(
Component
c,

Border
b,
int x,
int y,
int width,
int height)

Returns a rectangle using the arguments minus the
insets of the border. This is useful for determining the area
that components should draw in that will not intersect the border.

**Parameters:**
- c

- the component for which this border is being computed
- b

- the

Border

object
- x

- the x position of the border
- y

- the y position of the border
- width

- the width of the border
- height

- the height of the border

**Returns:**
- a

Rectangle

containing the interior coordinates

---

#### public int getBaseline​(
Component
c,
int width,
int height)

Returns the baseline. A return value less than 0 indicates the border
does not have a reasonable baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

**Parameters:**
- c

-

Component

baseline is being requested for
- width

- the width to get the baseline for
- height

- the height to get the baseline for

**Returns:**
- the baseline or < 0 indicating there is no reasonable
baseline

**Throws:**
- IllegalArgumentException

- if width or height is < 0

**See Also:**
- Component.getBaseline(int,int)

,

Component.getBaselineResizeBehavior()

**Since:**
- 1.6

---

#### public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
Component
c)

Returns an enum indicating how the baseline of a component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

, subclasses that support
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

**Parameters:**
- c

-

Component

to return baseline resize behavior for

**Returns:**
- an enum indicating how the baseline changes as the border is
resized

**See Also:**
- Component.getBaseline(int,int)

,

Component.getBaselineResizeBehavior()

**Since:**
- 1.6

---

### Additional Sections

#### Class AbstractBorder

java.lang.Object

- javax.swing.border.AbstractBorder

javax.swing.border.AbstractBorder

**All Implemented Interfaces:** Serializable

,

Border

**Direct Known Subclasses:** BasicBorders.ButtonBorder

,

BasicBorders.FieldBorder

,

BasicBorders.MarginBorder

,

BasicBorders.MenuBarBorder

,

BevelBorder

,

CompoundBorder

,

EmptyBorder

,

EtchedBorder

,

LineBorder

,

MetalBorders.ButtonBorder

,

MetalBorders.Flush3DBorder

,

MetalBorders.InternalFrameBorder

,

MetalBorders.MenuBarBorder

,

MetalBorders.MenuItemBorder

,

MetalBorders.OptionDialogBorder

,

MetalBorders.PaletteBorder

,

MetalBorders.PopupMenuBorder

,

MetalBorders.ScrollPaneBorder

,

MetalBorders.TableHeaderBorder

,

MetalBorders.ToolBarBorder

,

StrokeBorder

,

TitledBorder

```java
public abstract class
AbstractBorder

extends
Object

implements
Border
,
Serializable
```

A class that implements an empty border with no size.
This provides a convenient base class from which other border
classes can be easily derived.

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

public abstract class

AbstractBorder

extends

Object

implements

Border

,

Serializable

A class that implements an empty border with no size.
This provides a convenient base class from which other border
classes can be easily derived.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractBorder

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getBaseline

​(

Component

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

Component

c)

Returns an enum indicating how the baseline of a component
changes as the size changes.

Insets

getBorderInsets

​(

Component

c)

This default implementation returns a new

Insets

object
that is initialized by the

getBorderInsets(Component,Insets)

method.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitializes the insets parameter with this Border's current Insets.

Rectangle

getInteriorRectangle

​(

Component

c,
int x,
int y,
int width,
int height)

This convenience method calls the static method.

static

Rectangle

getInteriorRectangle

​(

Component

c,

Border

b,
int x,
int y,
int width,
int height)

Returns a rectangle using the arguments minus the
insets of the border.

boolean

isBorderOpaque

()

This default implementation returns false.

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

This default implementation does no painting.

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

AbstractBorder

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getBaseline

​(

Component

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

Component

c)

Returns an enum indicating how the baseline of a component
changes as the size changes.

Insets

getBorderInsets

​(

Component

c)

This default implementation returns a new

Insets

object
that is initialized by the

getBorderInsets(Component,Insets)

method.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitializes the insets parameter with this Border's current Insets.

Rectangle

getInteriorRectangle

​(

Component

c,
int x,
int y,
int width,
int height)

This convenience method calls the static method.

static

Rectangle

getInteriorRectangle

​(

Component

c,

Border

b,
int x,
int y,
int width,
int height)

Returns a rectangle using the arguments minus the
insets of the border.

boolean

isBorderOpaque

()

This default implementation returns false.

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

This default implementation does no painting.

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

Returns the baseline.

Returns an enum indicating how the baseline of a component
changes as the size changes.

This default implementation returns a new

Insets

object
that is initialized by the

getBorderInsets(Component,Insets)

method.

Reinitializes the insets parameter with this Border's current Insets.

This convenience method calls the static method.

Returns a rectangle using the arguments minus the
insets of the border.

This default implementation returns false.

This default implementation does no painting.

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

- AbstractBorder

```java
public AbstractBorder()
```

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

This default implementation does no painting.

**Specified by:** paintBorder

in interface

Border
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
c)
```

This default implementation returns a new

Insets

object
that is initialized by the

getBorderInsets(Component,Insets)

method.
By default the

top

,

left

,

bottom

,
and

right

fields are set to

0

.

**Specified by:** getBorderInsets

in interface

Border
**Parameters:** c

- the component for which this border insets value applies
**Returns:** a new

Insets

object

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

Reinitializes the insets parameter with this Border's current Insets.

**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

This default implementation returns false.

**Specified by:** isBorderOpaque

in interface

Border
**Returns:** false

- getInteriorRectangle

```java
public
Rectangle
getInteriorRectangle​(
Component
c,
int x,
int y,
int width,
int height)
```

This convenience method calls the static method.

**Parameters:** c

- the component for which this border is being computed
**Parameters:** x

- the x position of the border
**Parameters:** y

- the y position of the border
**Parameters:** width

- the width of the border
**Parameters:** height

- the height of the border
**Returns:** a

Rectangle

containing the interior coordinates

- getInteriorRectangle

```java
public static
Rectangle
getInteriorRectangle​(
Component
c,

Border
b,
int x,
int y,
int width,
int height)
```

Returns a rectangle using the arguments minus the
insets of the border. This is useful for determining the area
that components should draw in that will not intersect the border.

**Parameters:** c

- the component for which this border is being computed
**Parameters:** b

- the

Border

object
**Parameters:** x

- the x position of the border
**Parameters:** y

- the y position of the border
**Parameters:** width

- the width of the border
**Parameters:** height

- the height of the border
**Returns:** a

Rectangle

containing the interior coordinates

- getBaseline

```java
public int getBaseline​(
Component
c,
int width,
int height)
```

Returns the baseline. A return value less than 0 indicates the border
does not have a reasonable baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

**Parameters:** c

-

Component

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** the baseline or < 0 indicating there is no reasonable
baseline
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** Component.getBaseline(int,int)

,

Component.getBaselineResizeBehavior()

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
Component
c)
```

Returns an enum indicating how the baseline of a component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

, subclasses that support
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

**Parameters:** c

-

Component

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the border is
resized
**Since:** 1.6
**See Also:** Component.getBaseline(int,int)

,

Component.getBaselineResizeBehavior()

Constructor Detail

- AbstractBorder

```java
public AbstractBorder()
```

---

#### Constructor Detail

AbstractBorder

```java
public AbstractBorder()
```

---

#### AbstractBorder

public AbstractBorder()

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

This default implementation does no painting.

**Specified by:** paintBorder

in interface

Border
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
c)
```

This default implementation returns a new

Insets

object
that is initialized by the

getBorderInsets(Component,Insets)

method.
By default the

top

,

left

,

bottom

,
and

right

fields are set to

0

.

**Specified by:** getBorderInsets

in interface

Border
**Parameters:** c

- the component for which this border insets value applies
**Returns:** a new

Insets

object

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

Reinitializes the insets parameter with this Border's current Insets.

**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

This default implementation returns false.

**Specified by:** isBorderOpaque

in interface

Border
**Returns:** false

- getInteriorRectangle

```java
public
Rectangle
getInteriorRectangle​(
Component
c,
int x,
int y,
int width,
int height)
```

This convenience method calls the static method.

**Parameters:** c

- the component for which this border is being computed
**Parameters:** x

- the x position of the border
**Parameters:** y

- the y position of the border
**Parameters:** width

- the width of the border
**Parameters:** height

- the height of the border
**Returns:** a

Rectangle

containing the interior coordinates

- getInteriorRectangle

```java
public static
Rectangle
getInteriorRectangle​(
Component
c,

Border
b,
int x,
int y,
int width,
int height)
```

Returns a rectangle using the arguments minus the
insets of the border. This is useful for determining the area
that components should draw in that will not intersect the border.

**Parameters:** c

- the component for which this border is being computed
**Parameters:** b

- the

Border

object
**Parameters:** x

- the x position of the border
**Parameters:** y

- the y position of the border
**Parameters:** width

- the width of the border
**Parameters:** height

- the height of the border
**Returns:** a

Rectangle

containing the interior coordinates

- getBaseline

```java
public int getBaseline​(
Component
c,
int width,
int height)
```

Returns the baseline. A return value less than 0 indicates the border
does not have a reasonable baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

**Parameters:** c

-

Component

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** the baseline or < 0 indicating there is no reasonable
baseline
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** Component.getBaseline(int,int)

,

Component.getBaselineResizeBehavior()

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
Component
c)
```

Returns an enum indicating how the baseline of a component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

, subclasses that support
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

**Parameters:** c

-

Component

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the border is
resized
**Since:** 1.6
**See Also:** Component.getBaseline(int,int)

,

Component.getBaselineResizeBehavior()

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

This default implementation does no painting.

**Specified by:** paintBorder

in interface

Border
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

This default implementation does no painting.

getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c)
```

This default implementation returns a new

Insets

object
that is initialized by the

getBorderInsets(Component,Insets)

method.
By default the

top

,

left

,

bottom

,
and

right

fields are set to

0

.

**Specified by:** getBorderInsets

in interface

Border
**Parameters:** c

- the component for which this border insets value applies
**Returns:** a new

Insets

object

---

#### getBorderInsets

public

Insets

getBorderInsets​(

Component

c)

This default implementation returns a new

Insets

object
that is initialized by the

getBorderInsets(Component,Insets)

method.
By default the

top

,

left

,

bottom

,
and

right

fields are set to

0

.

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

Reinitializes the insets parameter with this Border's current Insets.

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

Reinitializes the insets parameter with this Border's current Insets.

isBorderOpaque

```java
public boolean isBorderOpaque()
```

This default implementation returns false.

**Specified by:** isBorderOpaque

in interface

Border
**Returns:** false

---

#### isBorderOpaque

public boolean isBorderOpaque()

This default implementation returns false.

getInteriorRectangle

```java
public
Rectangle
getInteriorRectangle​(
Component
c,
int x,
int y,
int width,
int height)
```

This convenience method calls the static method.

**Parameters:** c

- the component for which this border is being computed
**Parameters:** x

- the x position of the border
**Parameters:** y

- the y position of the border
**Parameters:** width

- the width of the border
**Parameters:** height

- the height of the border
**Returns:** a

Rectangle

containing the interior coordinates

---

#### getInteriorRectangle

public

Rectangle

getInteriorRectangle​(

Component

c,
int x,
int y,
int width,
int height)

This convenience method calls the static method.

getInteriorRectangle

```java
public static
Rectangle
getInteriorRectangle​(
Component
c,

Border
b,
int x,
int y,
int width,
int height)
```

Returns a rectangle using the arguments minus the
insets of the border. This is useful for determining the area
that components should draw in that will not intersect the border.

**Parameters:** c

- the component for which this border is being computed
**Parameters:** b

- the

Border

object
**Parameters:** x

- the x position of the border
**Parameters:** y

- the y position of the border
**Parameters:** width

- the width of the border
**Parameters:** height

- the height of the border
**Returns:** a

Rectangle

containing the interior coordinates

---

#### getInteriorRectangle

public static

Rectangle

getInteriorRectangle​(

Component

c,

Border

b,
int x,
int y,
int width,
int height)

Returns a rectangle using the arguments minus the
insets of the border. This is useful for determining the area
that components should draw in that will not intersect the border.

getBaseline

```java
public int getBaseline​(
Component
c,
int width,
int height)
```

Returns the baseline. A return value less than 0 indicates the border
does not have a reasonable baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

**Parameters:** c

-

Component

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** the baseline or < 0 indicating there is no reasonable
baseline
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** Component.getBaseline(int,int)

,

Component.getBaselineResizeBehavior()

---

#### getBaseline

public int getBaseline​(

Component

c,
int width,
int height)

Returns the baseline. A return value less than 0 indicates the border
does not have a reasonable baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
Component
c)
```

Returns an enum indicating how the baseline of a component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

, subclasses that support
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

**Parameters:** c

-

Component

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the border is
resized
**Since:** 1.6
**See Also:** Component.getBaseline(int,int)

,

Component.getBaselineResizeBehavior()

---

#### getBaselineResizeBehavior

public

Component.BaselineResizeBehavior

getBaselineResizeBehavior​(

Component

c)

Returns an enum indicating how the baseline of a component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

, subclasses that support
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

The default implementation returns

BaselineResizeBehavior.OTHER

, subclasses that support
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

---

