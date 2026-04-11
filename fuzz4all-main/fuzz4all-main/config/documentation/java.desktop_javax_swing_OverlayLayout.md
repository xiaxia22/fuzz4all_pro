# Class OverlayLayout

**Source:** `java.desktop\javax\swing\OverlayLayout.html`

### Class Description

```java
public class
OverlayLayout

extends
Object

implements
LayoutManager2
,
Serializable
```

A layout manager to arrange components over the top
of each other. The requested size of the container
will be the largest requested size of the children,
taking alignment needs into consideration.

The alignment is based upon what is needed to properly
fit the children in the allocation area. The children
will be placed such that their alignment points are all
on top of each other.

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

**All Implemented Interfaces:** LayoutManager

,

LayoutManager2

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### @ConstructorProperties
("target")
public OverlayLayout​(
Container
target)

Constructs a layout manager that performs overlay
arrangement of the children. The layout manager
created is dedicated to the given container.

**Parameters:**
- target

- the container to do layout against

---

### Method Details

#### public final
Container
getTarget()

Returns the container that uses this layout manager.

**Returns:**
- the container that uses this layout manager

**Since:**
- 1.6

---

#### public void invalidateLayout​(
Container
target)

Indicates a child has changed its layout related information,
which causes any cached calculations to be flushed.

**Specified by:**
- invalidateLayout

in interface

LayoutManager2

**Parameters:**
- target

- the container

---

#### public void addLayoutComponent​(
String
name,

Component
comp)

Adds the specified component to the layout. Used by
this class to know when to invalidate layout.

**Specified by:**
- addLayoutComponent

in interface

LayoutManager

**Parameters:**
- name

- the name of the component
- comp

- the component to be added

---

#### public void removeLayoutComponent​(
Component
comp)

Removes the specified component from the layout. Used by
this class to know when to invalidate layout.

**Specified by:**
- removeLayoutComponent

in interface

LayoutManager

**Parameters:**
- comp

- the component to remove

---

#### public void addLayoutComponent​(
Component
comp,

Object
constraints)

Adds the specified component to the layout, using the specified
constraint object. Used by this class to know when to invalidate
layout.

**Specified by:**
- addLayoutComponent

in interface

LayoutManager2

**Parameters:**
- comp

- the component to be added
- constraints

- where/how the component is added to the layout.

---

#### public
Dimension
preferredLayoutSize​(
Container
target)

Returns the preferred dimensions for this layout given the components
in the specified target container. Recomputes the layout if it
has been invalidated. Factors in the current inset setting returned
by getInsets().

**Specified by:**
- preferredLayoutSize

in interface

LayoutManager

**Parameters:**
- target

- the component which needs to be laid out

**Returns:**
- a Dimension object containing the preferred dimensions

**See Also:**
- minimumLayoutSize(java.awt.Container)

---

#### public
Dimension
minimumLayoutSize​(
Container
target)

Returns the minimum dimensions needed to lay out the components
contained in the specified target container. Recomputes the layout
if it has been invalidated, and factors in the current inset setting.

**Specified by:**
- minimumLayoutSize

in interface

LayoutManager

**Parameters:**
- target

- the component which needs to be laid out

**Returns:**
- a Dimension object containing the minimum dimensions

**See Also:**
- preferredLayoutSize(java.awt.Container)

---

#### public
Dimension
maximumLayoutSize​(
Container
target)

Returns the maximum dimensions needed to lay out the components
contained in the specified target container. Recomputes the
layout if it has been invalidated, and factors in the inset setting
returned by

getInset

.

**Specified by:**
- maximumLayoutSize

in interface

LayoutManager2

**Parameters:**
- target

- the component that needs to be laid out

**Returns:**
- a

Dimension

object containing the maximum
dimensions

**See Also:**
- preferredLayoutSize(java.awt.Container)

---

#### public float getLayoutAlignmentX​(
Container
target)

Returns the alignment along the x axis for the container.

**Specified by:**
- getLayoutAlignmentX

in interface

LayoutManager2

**Parameters:**
- target

- the container

**Returns:**
- the alignment >= 0.0f && <= 1.0f

---

#### public float getLayoutAlignmentY​(
Container
target)

Returns the alignment along the y axis for the container.

**Specified by:**
- getLayoutAlignmentY

in interface

LayoutManager2

**Parameters:**
- target

- the container

**Returns:**
- the alignment >= 0.0f && <= 1.0f

---

#### public void layoutContainer​(
Container
target)

Called by the AWT when the specified container needs to be laid out.

**Specified by:**
- layoutContainer

in interface

LayoutManager

**Parameters:**
- target

- the container to lay out

**Throws:**
- AWTError

- if the target isn't the container specified to the
constructor

---

### Additional Sections

#### Class OverlayLayout

java.lang.Object

- javax.swing.OverlayLayout

javax.swing.OverlayLayout

**All Implemented Interfaces:** LayoutManager

,

LayoutManager2

,

Serializable

```java
public class
OverlayLayout

extends
Object

implements
LayoutManager2
,
Serializable
```

A layout manager to arrange components over the top
of each other. The requested size of the container
will be the largest requested size of the children,
taking alignment needs into consideration.

The alignment is based upon what is needed to properly
fit the children in the allocation area. The children
will be placed such that their alignment points are all
on top of each other.

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

**Since:** 1.2
**See Also:** Serialized Form

public class

OverlayLayout

extends

Object

implements

LayoutManager2

,

Serializable

A layout manager to arrange components over the top
of each other. The requested size of the container
will be the largest requested size of the children,
taking alignment needs into consideration.

The alignment is based upon what is needed to properly
fit the children in the allocation area. The children
will be placed such that their alignment points are all
on top of each other.

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

OverlayLayout

​(

Container

target)

Constructs a layout manager that performs overlay
arrangement of the children.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addLayoutComponent

​(

Component

comp,

Object

constraints)

Adds the specified component to the layout, using the specified
constraint object.

void

addLayoutComponent

​(

String

name,

Component

comp)

Adds the specified component to the layout.

float

getLayoutAlignmentX

​(

Container

target)

Returns the alignment along the x axis for the container.

float

getLayoutAlignmentY

​(

Container

target)

Returns the alignment along the y axis for the container.

Container

getTarget

()

Returns the container that uses this layout manager.

void

invalidateLayout

​(

Container

target)

Indicates a child has changed its layout related information,
which causes any cached calculations to be flushed.

void

layoutContainer

​(

Container

target)

Called by the AWT when the specified container needs to be laid out.

Dimension

maximumLayoutSize

​(

Container

target)

Returns the maximum dimensions needed to lay out the components
contained in the specified target container.

Dimension

minimumLayoutSize

​(

Container

target)

Returns the minimum dimensions needed to lay out the components
contained in the specified target container.

Dimension

preferredLayoutSize

​(

Container

target)

Returns the preferred dimensions for this layout given the components
in the specified target container.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

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

OverlayLayout

​(

Container

target)

Constructs a layout manager that performs overlay
arrangement of the children.

---

#### Constructor Summary

Constructs a layout manager that performs overlay
arrangement of the children.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addLayoutComponent

​(

Component

comp,

Object

constraints)

Adds the specified component to the layout, using the specified
constraint object.

void

addLayoutComponent

​(

String

name,

Component

comp)

Adds the specified component to the layout.

float

getLayoutAlignmentX

​(

Container

target)

Returns the alignment along the x axis for the container.

float

getLayoutAlignmentY

​(

Container

target)

Returns the alignment along the y axis for the container.

Container

getTarget

()

Returns the container that uses this layout manager.

void

invalidateLayout

​(

Container

target)

Indicates a child has changed its layout related information,
which causes any cached calculations to be flushed.

void

layoutContainer

​(

Container

target)

Called by the AWT when the specified container needs to be laid out.

Dimension

maximumLayoutSize

​(

Container

target)

Returns the maximum dimensions needed to lay out the components
contained in the specified target container.

Dimension

minimumLayoutSize

​(

Container

target)

Returns the minimum dimensions needed to lay out the components
contained in the specified target container.

Dimension

preferredLayoutSize

​(

Container

target)

Returns the preferred dimensions for this layout given the components
in the specified target container.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

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

Adds the specified component to the layout, using the specified
constraint object.

Adds the specified component to the layout.

Returns the alignment along the x axis for the container.

Returns the alignment along the y axis for the container.

Returns the container that uses this layout manager.

Indicates a child has changed its layout related information,
which causes any cached calculations to be flushed.

Called by the AWT when the specified container needs to be laid out.

Returns the maximum dimensions needed to lay out the components
contained in the specified target container.

Returns the minimum dimensions needed to lay out the components
contained in the specified target container.

Returns the preferred dimensions for this layout given the components
in the specified target container.

Removes the specified component from the layout.

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

- OverlayLayout

```java
@ConstructorProperties
("target")
public OverlayLayout​(
Container
target)
```

Constructs a layout manager that performs overlay
arrangement of the children. The layout manager
created is dedicated to the given container.

**Parameters:** target

- the container to do layout against

============ METHOD DETAIL ==========

- Method Detail

- getTarget

```java
public final
Container
getTarget()
```

Returns the container that uses this layout manager.

**Returns:** the container that uses this layout manager
**Since:** 1.6

- invalidateLayout

```java
public void invalidateLayout​(
Container
target)
```

Indicates a child has changed its layout related information,
which causes any cached calculations to be flushed.

**Specified by:** invalidateLayout

in interface

LayoutManager2
**Parameters:** target

- the container

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Adds the specified component to the layout. Used by
this class to know when to invalidate layout.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the name of the component
**Parameters:** comp

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout. Used by
this class to know when to invalidate layout.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to remove

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified
constraint object. Used by this class to know when to invalidate
layout.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- where/how the component is added to the layout.

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
target)
```

Returns the preferred dimensions for this layout given the components
in the specified target container. Recomputes the layout if it
has been invalidated. Factors in the current inset setting returned
by getInsets().

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** target

- the component which needs to be laid out
**Returns:** a Dimension object containing the preferred dimensions
**See Also:** minimumLayoutSize(java.awt.Container)

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
target)
```

Returns the minimum dimensions needed to lay out the components
contained in the specified target container. Recomputes the layout
if it has been invalidated, and factors in the current inset setting.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** target

- the component which needs to be laid out
**Returns:** a Dimension object containing the minimum dimensions
**See Also:** preferredLayoutSize(java.awt.Container)

- maximumLayoutSize

```java
public
Dimension
maximumLayoutSize​(
Container
target)
```

Returns the maximum dimensions needed to lay out the components
contained in the specified target container. Recomputes the
layout if it has been invalidated, and factors in the inset setting
returned by

getInset

.

**Specified by:** maximumLayoutSize

in interface

LayoutManager2
**Parameters:** target

- the component that needs to be laid out
**Returns:** a

Dimension

object containing the maximum
dimensions
**See Also:** preferredLayoutSize(java.awt.Container)

- getLayoutAlignmentX

```java
public float getLayoutAlignmentX​(
Container
target)
```

Returns the alignment along the x axis for the container.

**Specified by:** getLayoutAlignmentX

in interface

LayoutManager2
**Parameters:** target

- the container
**Returns:** the alignment >= 0.0f && <= 1.0f

- getLayoutAlignmentY

```java
public float getLayoutAlignmentY​(
Container
target)
```

Returns the alignment along the y axis for the container.

**Specified by:** getLayoutAlignmentY

in interface

LayoutManager2
**Parameters:** target

- the container
**Returns:** the alignment >= 0.0f && <= 1.0f

- layoutContainer

```java
public void layoutContainer​(
Container
target)
```

Called by the AWT when the specified container needs to be laid out.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** target

- the container to lay out
**Throws:** AWTError

- if the target isn't the container specified to the
constructor

Constructor Detail

- OverlayLayout

```java
@ConstructorProperties
("target")
public OverlayLayout​(
Container
target)
```

Constructs a layout manager that performs overlay
arrangement of the children. The layout manager
created is dedicated to the given container.

**Parameters:** target

- the container to do layout against

---

#### Constructor Detail

OverlayLayout

```java
@ConstructorProperties
("target")
public OverlayLayout​(
Container
target)
```

Constructs a layout manager that performs overlay
arrangement of the children. The layout manager
created is dedicated to the given container.

**Parameters:** target

- the container to do layout against

---

#### OverlayLayout

@ConstructorProperties

("target")
public OverlayLayout​(

Container

target)

Constructs a layout manager that performs overlay
arrangement of the children. The layout manager
created is dedicated to the given container.

Method Detail

- getTarget

```java
public final
Container
getTarget()
```

Returns the container that uses this layout manager.

**Returns:** the container that uses this layout manager
**Since:** 1.6

- invalidateLayout

```java
public void invalidateLayout​(
Container
target)
```

Indicates a child has changed its layout related information,
which causes any cached calculations to be flushed.

**Specified by:** invalidateLayout

in interface

LayoutManager2
**Parameters:** target

- the container

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Adds the specified component to the layout. Used by
this class to know when to invalidate layout.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the name of the component
**Parameters:** comp

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout. Used by
this class to know when to invalidate layout.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to remove

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified
constraint object. Used by this class to know when to invalidate
layout.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- where/how the component is added to the layout.

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
target)
```

Returns the preferred dimensions for this layout given the components
in the specified target container. Recomputes the layout if it
has been invalidated. Factors in the current inset setting returned
by getInsets().

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** target

- the component which needs to be laid out
**Returns:** a Dimension object containing the preferred dimensions
**See Also:** minimumLayoutSize(java.awt.Container)

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
target)
```

Returns the minimum dimensions needed to lay out the components
contained in the specified target container. Recomputes the layout
if it has been invalidated, and factors in the current inset setting.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** target

- the component which needs to be laid out
**Returns:** a Dimension object containing the minimum dimensions
**See Also:** preferredLayoutSize(java.awt.Container)

- maximumLayoutSize

```java
public
Dimension
maximumLayoutSize​(
Container
target)
```

Returns the maximum dimensions needed to lay out the components
contained in the specified target container. Recomputes the
layout if it has been invalidated, and factors in the inset setting
returned by

getInset

.

**Specified by:** maximumLayoutSize

in interface

LayoutManager2
**Parameters:** target

- the component that needs to be laid out
**Returns:** a

Dimension

object containing the maximum
dimensions
**See Also:** preferredLayoutSize(java.awt.Container)

- getLayoutAlignmentX

```java
public float getLayoutAlignmentX​(
Container
target)
```

Returns the alignment along the x axis for the container.

**Specified by:** getLayoutAlignmentX

in interface

LayoutManager2
**Parameters:** target

- the container
**Returns:** the alignment >= 0.0f && <= 1.0f

- getLayoutAlignmentY

```java
public float getLayoutAlignmentY​(
Container
target)
```

Returns the alignment along the y axis for the container.

**Specified by:** getLayoutAlignmentY

in interface

LayoutManager2
**Parameters:** target

- the container
**Returns:** the alignment >= 0.0f && <= 1.0f

- layoutContainer

```java
public void layoutContainer​(
Container
target)
```

Called by the AWT when the specified container needs to be laid out.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** target

- the container to lay out
**Throws:** AWTError

- if the target isn't the container specified to the
constructor

---

#### Method Detail

getTarget

```java
public final
Container
getTarget()
```

Returns the container that uses this layout manager.

**Returns:** the container that uses this layout manager
**Since:** 1.6

---

#### getTarget

public final

Container

getTarget()

Returns the container that uses this layout manager.

invalidateLayout

```java
public void invalidateLayout​(
Container
target)
```

Indicates a child has changed its layout related information,
which causes any cached calculations to be flushed.

**Specified by:** invalidateLayout

in interface

LayoutManager2
**Parameters:** target

- the container

---

#### invalidateLayout

public void invalidateLayout​(

Container

target)

Indicates a child has changed its layout related information,
which causes any cached calculations to be flushed.

addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Adds the specified component to the layout. Used by
this class to know when to invalidate layout.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the name of the component
**Parameters:** comp

- the component to be added

---

#### addLayoutComponent

public void addLayoutComponent​(

String

name,

Component

comp)

Adds the specified component to the layout. Used by
this class to know when to invalidate layout.

removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout. Used by
this class to know when to invalidate layout.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to remove

---

#### removeLayoutComponent

public void removeLayoutComponent​(

Component

comp)

Removes the specified component from the layout. Used by
this class to know when to invalidate layout.

addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified
constraint object. Used by this class to know when to invalidate
layout.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- where/how the component is added to the layout.

---

#### addLayoutComponent

public void addLayoutComponent​(

Component

comp,

Object

constraints)

Adds the specified component to the layout, using the specified
constraint object. Used by this class to know when to invalidate
layout.

preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
target)
```

Returns the preferred dimensions for this layout given the components
in the specified target container. Recomputes the layout if it
has been invalidated. Factors in the current inset setting returned
by getInsets().

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** target

- the component which needs to be laid out
**Returns:** a Dimension object containing the preferred dimensions
**See Also:** minimumLayoutSize(java.awt.Container)

---

#### preferredLayoutSize

public

Dimension

preferredLayoutSize​(

Container

target)

Returns the preferred dimensions for this layout given the components
in the specified target container. Recomputes the layout if it
has been invalidated. Factors in the current inset setting returned
by getInsets().

minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
target)
```

Returns the minimum dimensions needed to lay out the components
contained in the specified target container. Recomputes the layout
if it has been invalidated, and factors in the current inset setting.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** target

- the component which needs to be laid out
**Returns:** a Dimension object containing the minimum dimensions
**See Also:** preferredLayoutSize(java.awt.Container)

---

#### minimumLayoutSize

public

Dimension

minimumLayoutSize​(

Container

target)

Returns the minimum dimensions needed to lay out the components
contained in the specified target container. Recomputes the layout
if it has been invalidated, and factors in the current inset setting.

maximumLayoutSize

```java
public
Dimension
maximumLayoutSize​(
Container
target)
```

Returns the maximum dimensions needed to lay out the components
contained in the specified target container. Recomputes the
layout if it has been invalidated, and factors in the inset setting
returned by

getInset

.

**Specified by:** maximumLayoutSize

in interface

LayoutManager2
**Parameters:** target

- the component that needs to be laid out
**Returns:** a

Dimension

object containing the maximum
dimensions
**See Also:** preferredLayoutSize(java.awt.Container)

---

#### maximumLayoutSize

public

Dimension

maximumLayoutSize​(

Container

target)

Returns the maximum dimensions needed to lay out the components
contained in the specified target container. Recomputes the
layout if it has been invalidated, and factors in the inset setting
returned by

getInset

.

getLayoutAlignmentX

```java
public float getLayoutAlignmentX​(
Container
target)
```

Returns the alignment along the x axis for the container.

**Specified by:** getLayoutAlignmentX

in interface

LayoutManager2
**Parameters:** target

- the container
**Returns:** the alignment >= 0.0f && <= 1.0f

---

#### getLayoutAlignmentX

public float getLayoutAlignmentX​(

Container

target)

Returns the alignment along the x axis for the container.

getLayoutAlignmentY

```java
public float getLayoutAlignmentY​(
Container
target)
```

Returns the alignment along the y axis for the container.

**Specified by:** getLayoutAlignmentY

in interface

LayoutManager2
**Parameters:** target

- the container
**Returns:** the alignment >= 0.0f && <= 1.0f

---

#### getLayoutAlignmentY

public float getLayoutAlignmentY​(

Container

target)

Returns the alignment along the y axis for the container.

layoutContainer

```java
public void layoutContainer​(
Container
target)
```

Called by the AWT when the specified container needs to be laid out.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** target

- the container to lay out
**Throws:** AWTError

- if the target isn't the container specified to the
constructor

---

#### layoutContainer

public void layoutContainer​(

Container

target)

Called by the AWT when the specified container needs to be laid out.

---

