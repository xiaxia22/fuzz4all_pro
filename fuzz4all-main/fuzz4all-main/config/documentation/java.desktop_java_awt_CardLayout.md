# Class CardLayout

**Source:** `java.desktop\java\awt\CardLayout.html`

### Class Description

```java
public class
CardLayout

extends
Object

implements
LayoutManager2
,
Serializable
```

A

CardLayout

object is a layout manager for a
container. It treats each component in the container as a card.
Only one card is visible at a time, and the container acts as
a stack of cards. The first component added to a

CardLayout

object is the visible component when the
container is first displayed.

The ordering of cards is determined by the container's own internal
ordering of its component objects.

CardLayout

defines a set of methods that allow an application to flip
through these cards sequentially, or to show a specified card.
The

addLayoutComponent(java.awt.Component, java.lang.Object)

method can be used to associate a string identifier with a given card
for fast random access.

**All Implemented Interfaces:** LayoutManager

,

LayoutManager2

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CardLayout()

Creates a new card layout with gaps of size zero.

---

#### public CardLayout​(int hgap,
int vgap)

Creates a new card layout with the specified horizontal and
vertical gaps. The horizontal gaps are placed at the left and
right edges. The vertical gaps are placed at the top and bottom
edges.

**Parameters:**
- hgap

- the horizontal gap.
- vgap

- the vertical gap.

---

### Method Details

#### public int getHgap()

Gets the horizontal gap between components.

**Returns:**
- the horizontal gap between components.

**See Also:**
- setHgap(int)

,

getVgap()

**Since:**
- 1.1

---

#### public void setHgap​(int hgap)

Sets the horizontal gap between components.

**Parameters:**
- hgap

- the horizontal gap between components.

**See Also:**
- getHgap()

,

setVgap(int)

**Since:**
- 1.1

---

#### public int getVgap()

Gets the vertical gap between components.

**Returns:**
- the vertical gap between components.

**See Also:**
- setVgap(int)

,

getHgap()

---

#### public void setVgap​(int vgap)

Sets the vertical gap between components.

**Parameters:**
- vgap

- the vertical gap between components.

**See Also:**
- getVgap()

,

setHgap(int)

**Since:**
- 1.1

---

#### public void addLayoutComponent​(
Component
comp,

Object
constraints)

Adds the specified component to this card layout's internal
table of names. The object specified by

constraints

must be a string. The card layout stores this string as a key-value
pair that can be used for random access to a particular card.
By calling the

show

method, an application can
display the component with the specified name.

**Specified by:**
- addLayoutComponent

in interface

LayoutManager2

**Parameters:**
- comp

- the component to be added.
- constraints

- a tag that identifies a particular
card in the layout.

**Throws:**
- IllegalArgumentException

- if the constraint is not a string.

**See Also:**
- show(java.awt.Container, java.lang.String)

---

#### @Deprecated

public void addLayoutComponent​(
String
name,

Component
comp)

Description copied from interface:

LayoutManager

**Specified by:**
- addLayoutComponent

in interface

LayoutManager

**Parameters:**
- name

- the string to be associated with the component
- comp

- the component to be added

---

#### public void removeLayoutComponent​(
Component
comp)

Removes the specified component from the layout.
If the card was visible on top, the next card underneath it is shown.

**Specified by:**
- removeLayoutComponent

in interface

LayoutManager

**Parameters:**
- comp

- the component to be removed.

**See Also:**
- Container.remove(java.awt.Component)

,

Container.removeAll()

---

#### public
Dimension
preferredLayoutSize​(
Container
parent)

Determines the preferred size of the container argument using
this card layout.

**Specified by:**
- preferredLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the parent container in which to do the layout

**Returns:**
- the preferred dimensions to lay out the subcomponents
of the specified container

**See Also:**
- Container.getPreferredSize()

,

minimumLayoutSize(java.awt.Container)

---

#### public
Dimension
minimumLayoutSize​(
Container
parent)

Calculates the minimum size for the specified panel.

**Specified by:**
- minimumLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the parent container in which to do the layout

**Returns:**
- the minimum dimensions required to lay out the
subcomponents of the specified container

**See Also:**
- Container.doLayout()

,

preferredLayoutSize(java.awt.Container)

---

#### public
Dimension
maximumLayoutSize​(
Container
target)

Returns the maximum dimensions for this layout given the components
in the specified target container.

**Specified by:**
- maximumLayoutSize

in interface

LayoutManager2

**Parameters:**
- target

- the component which needs to be laid out

**Returns:**
- the maximum size of the container

**See Also:**
- Container

,

minimumLayoutSize(java.awt.Container)

,

preferredLayoutSize(java.awt.Container)

---

#### public float getLayoutAlignmentX​(
Container
parent)

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Specified by:**
- getLayoutAlignmentX

in interface

LayoutManager2

**Parameters:**
- parent

- the target container

**Returns:**
- the x-axis alignment preference

---

#### public float getLayoutAlignmentY​(
Container
parent)

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Specified by:**
- getLayoutAlignmentY

in interface

LayoutManager2

**Parameters:**
- parent

- the target container

**Returns:**
- the y-axis alignment preference

---

#### public void invalidateLayout​(
Container
target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

**Specified by:**
- invalidateLayout

in interface

LayoutManager2

**Parameters:**
- target

- the target container

---

#### public void layoutContainer​(
Container
parent)

Lays out the specified container using this card layout.

Each component in the

parent

container is reshaped
to be the size of the container, minus space for surrounding
insets, horizontal gaps, and vertical gaps.

**Specified by:**
- layoutContainer

in interface

LayoutManager

**Parameters:**
- parent

- the parent container in which to do the layout

**See Also:**
- Container.doLayout()

---

#### public void first​(
Container
parent)

Flips to the first card of the container.

**Parameters:**
- parent

- the parent container in which to do the layout

**See Also:**
- last(java.awt.Container)

---

#### public void next​(
Container
parent)

Flips to the next card of the specified container. If the
currently visible card is the last one, this method flips to the
first card in the layout.

**Parameters:**
- parent

- the parent container in which to do the layout

**See Also:**
- previous(java.awt.Container)

---

#### public void previous​(
Container
parent)

Flips to the previous card of the specified container. If the
currently visible card is the first one, this method flips to the
last card in the layout.

**Parameters:**
- parent

- the parent container in which to do the layout

**See Also:**
- next(java.awt.Container)

---

#### public void last​(
Container
parent)

Flips to the last card of the container.

**Parameters:**
- parent

- the parent container in which to do the layout

**See Also:**
- first(java.awt.Container)

---

#### public void show​(
Container
parent,

String
name)

Flips to the component that was added to this layout with the
specified

name

, using

addLayoutComponent

.
If no such component exists, then nothing happens.

**Parameters:**
- parent

- the parent container in which to do the layout
- name

- the component name

**See Also:**
- addLayoutComponent(java.awt.Component, java.lang.Object)

---

#### public
String
toString()

Returns a string representation of the state of this card layout.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this card layout.

---

### Additional Sections

#### Class CardLayout

java.lang.Object

- java.awt.CardLayout

java.awt.CardLayout

**All Implemented Interfaces:** LayoutManager

,

LayoutManager2

,

Serializable

```java
public class
CardLayout

extends
Object

implements
LayoutManager2
,
Serializable
```

A

CardLayout

object is a layout manager for a
container. It treats each component in the container as a card.
Only one card is visible at a time, and the container acts as
a stack of cards. The first component added to a

CardLayout

object is the visible component when the
container is first displayed.

The ordering of cards is determined by the container's own internal
ordering of its component objects.

CardLayout

defines a set of methods that allow an application to flip
through these cards sequentially, or to show a specified card.
The

addLayoutComponent(java.awt.Component, java.lang.Object)

method can be used to associate a string identifier with a given card
for fast random access.

**Since:** 1.0
**See Also:** Container

,

Serialized Form

public class

CardLayout

extends

Object

implements

LayoutManager2

,

Serializable

A

CardLayout

object is a layout manager for a
container. It treats each component in the container as a card.
Only one card is visible at a time, and the container acts as
a stack of cards. The first component added to a

CardLayout

object is the visible component when the
container is first displayed.

The ordering of cards is determined by the container's own internal
ordering of its component objects.

CardLayout

defines a set of methods that allow an application to flip
through these cards sequentially, or to show a specified card.
The

addLayoutComponent(java.awt.Component, java.lang.Object)

method can be used to associate a string identifier with a given card
for fast random access.

The ordering of cards is determined by the container's own internal
ordering of its component objects.

CardLayout

defines a set of methods that allow an application to flip
through these cards sequentially, or to show a specified card.
The

addLayoutComponent(java.awt.Component, java.lang.Object)

method can be used to associate a string identifier with a given card
for fast random access.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CardLayout

()

Creates a new card layout with gaps of size zero.

CardLayout

​(int hgap,
int vgap)

Creates a new card layout with the specified horizontal and
vertical gaps.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

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

Adds the specified component to this card layout's internal
table of names.

void

addLayoutComponent

​(

String

name,

Component

comp)

Deprecated.

replaced by

addLayoutComponent(Component, Object)

.

void

first

​(

Container

parent)

Flips to the first card of the container.

int

getHgap

()

Gets the horizontal gap between components.

float

getLayoutAlignmentX

​(

Container

parent)

Returns the alignment along the x axis.

float

getLayoutAlignmentY

​(

Container

parent)

Returns the alignment along the y axis.

int

getVgap

()

Gets the vertical gap between components.

void

invalidateLayout

​(

Container

target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

void

last

​(

Container

parent)

Flips to the last card of the container.

void

layoutContainer

​(

Container

parent)

Lays out the specified container using this card layout.

Dimension

maximumLayoutSize

​(

Container

target)

Returns the maximum dimensions for this layout given the components
in the specified target container.

Dimension

minimumLayoutSize

​(

Container

parent)

Calculates the minimum size for the specified panel.

void

next

​(

Container

parent)

Flips to the next card of the specified container.

Dimension

preferredLayoutSize

​(

Container

parent)

Determines the preferred size of the container argument using
this card layout.

void

previous

​(

Container

parent)

Flips to the previous card of the specified container.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

void

setHgap

​(int hgap)

Sets the horizontal gap between components.

void

setVgap

​(int vgap)

Sets the vertical gap between components.

void

show

​(

Container

parent,

String

name)

Flips to the component that was added to this layout with the
specified

name

, using

addLayoutComponent

.

String

toString

()

Returns a string representation of the state of this card layout.

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

Constructor Summary

Constructors

Constructor

Description

CardLayout

()

Creates a new card layout with gaps of size zero.

CardLayout

​(int hgap,
int vgap)

Creates a new card layout with the specified horizontal and
vertical gaps.

---

#### Constructor Summary

Creates a new card layout with gaps of size zero.

Creates a new card layout with the specified horizontal and
vertical gaps.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

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

Adds the specified component to this card layout's internal
table of names.

void

addLayoutComponent

​(

String

name,

Component

comp)

Deprecated.

replaced by

addLayoutComponent(Component, Object)

.

void

first

​(

Container

parent)

Flips to the first card of the container.

int

getHgap

()

Gets the horizontal gap between components.

float

getLayoutAlignmentX

​(

Container

parent)

Returns the alignment along the x axis.

float

getLayoutAlignmentY

​(

Container

parent)

Returns the alignment along the y axis.

int

getVgap

()

Gets the vertical gap between components.

void

invalidateLayout

​(

Container

target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

void

last

​(

Container

parent)

Flips to the last card of the container.

void

layoutContainer

​(

Container

parent)

Lays out the specified container using this card layout.

Dimension

maximumLayoutSize

​(

Container

target)

Returns the maximum dimensions for this layout given the components
in the specified target container.

Dimension

minimumLayoutSize

​(

Container

parent)

Calculates the minimum size for the specified panel.

void

next

​(

Container

parent)

Flips to the next card of the specified container.

Dimension

preferredLayoutSize

​(

Container

parent)

Determines the preferred size of the container argument using
this card layout.

void

previous

​(

Container

parent)

Flips to the previous card of the specified container.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

void

setHgap

​(int hgap)

Sets the horizontal gap between components.

void

setVgap

​(int vgap)

Sets the vertical gap between components.

void

show

​(

Container

parent,

String

name)

Flips to the component that was added to this layout with the
specified

name

, using

addLayoutComponent

.

String

toString

()

Returns a string representation of the state of this card layout.

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

Adds the specified component to this card layout's internal
table of names.

Deprecated.

replaced by

addLayoutComponent(Component, Object)

.

Flips to the first card of the container.

Gets the horizontal gap between components.

Returns the alignment along the x axis.

Returns the alignment along the y axis.

Gets the vertical gap between components.

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

Flips to the last card of the container.

Lays out the specified container using this card layout.

Returns the maximum dimensions for this layout given the components
in the specified target container.

Calculates the minimum size for the specified panel.

Flips to the next card of the specified container.

Determines the preferred size of the container argument using
this card layout.

Flips to the previous card of the specified container.

Removes the specified component from the layout.

Sets the horizontal gap between components.

Sets the vertical gap between components.

Flips to the component that was added to this layout with the
specified

name

, using

addLayoutComponent

.

Returns a string representation of the state of this card layout.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CardLayout

```java
public CardLayout()
```

Creates a new card layout with gaps of size zero.

- CardLayout

```java
public CardLayout​(int hgap,
int vgap)
```

Creates a new card layout with the specified horizontal and
vertical gaps. The horizontal gaps are placed at the left and
right edges. The vertical gaps are placed at the top and bottom
edges.

**Parameters:** hgap

- the horizontal gap.
**Parameters:** vgap

- the vertical gap.

============ METHOD DETAIL ==========

- Method Detail

- getHgap

```java
public int getHgap()
```

Gets the horizontal gap between components.

**Returns:** the horizontal gap between components.
**Since:** 1.1
**See Also:** setHgap(int)

,

getVgap()

- setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components.

**Parameters:** hgap

- the horizontal gap between components.
**Since:** 1.1
**See Also:** getHgap()

,

setVgap(int)

- getVgap

```java
public int getVgap()
```

Gets the vertical gap between components.

**Returns:** the vertical gap between components.
**See Also:** setVgap(int)

,

getHgap()

- setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components.

**Parameters:** vgap

- the vertical gap between components.
**Since:** 1.1
**See Also:** getVgap()

,

setHgap(int)

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to this card layout's internal
table of names. The object specified by

constraints

must be a string. The card layout stores this string as a key-value
pair that can be used for random access to a particular card.
By calling the

show

method, an application can
display the component with the specified name.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added.
**Parameters:** constraints

- a tag that identifies a particular
card in the layout.
**Throws:** IllegalArgumentException

- if the constraint is not a string.
**See Also:** show(java.awt.Container, java.lang.String)

- addLayoutComponent

```java
@Deprecated

public void addLayoutComponent​(
String
name,

Component
comp)
```

Deprecated.

replaced by

addLayoutComponent(Component, Object)

.

Description copied from interface:

LayoutManager

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the string to be associated with the component
**Parameters:** comp

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.
If the card was visible on top, the next card underneath it is shown.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to be removed.
**See Also:** Container.remove(java.awt.Component)

,

Container.removeAll()

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Determines the preferred size of the container argument using
this card layout.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the parent container in which to do the layout
**Returns:** the preferred dimensions to lay out the subcomponents
of the specified container
**See Also:** Container.getPreferredSize()

,

minimumLayoutSize(java.awt.Container)

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Calculates the minimum size for the specified panel.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the parent container in which to do the layout
**Returns:** the minimum dimensions required to lay out the
subcomponents of the specified container
**See Also:** Container.doLayout()

,

preferredLayoutSize(java.awt.Container)

- maximumLayoutSize

```java
public
Dimension
maximumLayoutSize​(
Container
target)
```

Returns the maximum dimensions for this layout given the components
in the specified target container.

**Specified by:** maximumLayoutSize

in interface

LayoutManager2
**Parameters:** target

- the component which needs to be laid out
**Returns:** the maximum size of the container
**See Also:** Container

,

minimumLayoutSize(java.awt.Container)

,

preferredLayoutSize(java.awt.Container)

- getLayoutAlignmentX

```java
public float getLayoutAlignmentX​(
Container
parent)
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Specified by:** getLayoutAlignmentX

in interface

LayoutManager2
**Parameters:** parent

- the target container
**Returns:** the x-axis alignment preference

- getLayoutAlignmentY

```java
public float getLayoutAlignmentY​(
Container
parent)
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Specified by:** getLayoutAlignmentY

in interface

LayoutManager2
**Parameters:** parent

- the target container
**Returns:** the y-axis alignment preference

- invalidateLayout

```java
public void invalidateLayout​(
Container
target)
```

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

**Specified by:** invalidateLayout

in interface

LayoutManager2
**Parameters:** target

- the target container

- layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Lays out the specified container using this card layout.

Each component in the

parent

container is reshaped
to be the size of the container, minus space for surrounding
insets, horizontal gaps, and vertical gaps.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the parent container in which to do the layout
**See Also:** Container.doLayout()

- first

```java
public void first​(
Container
parent)
```

Flips to the first card of the container.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** last(java.awt.Container)

- next

```java
public void next​(
Container
parent)
```

Flips to the next card of the specified container. If the
currently visible card is the last one, this method flips to the
first card in the layout.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** previous(java.awt.Container)

- previous

```java
public void previous​(
Container
parent)
```

Flips to the previous card of the specified container. If the
currently visible card is the first one, this method flips to the
last card in the layout.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** next(java.awt.Container)

- last

```java
public void last​(
Container
parent)
```

Flips to the last card of the container.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** first(java.awt.Container)

- show

```java
public void show​(
Container
parent,

String
name)
```

Flips to the component that was added to this layout with the
specified

name

, using

addLayoutComponent

.
If no such component exists, then nothing happens.

**Parameters:** parent

- the parent container in which to do the layout
**Parameters:** name

- the component name
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of the state of this card layout.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this card layout.

Constructor Detail

- CardLayout

```java
public CardLayout()
```

Creates a new card layout with gaps of size zero.

- CardLayout

```java
public CardLayout​(int hgap,
int vgap)
```

Creates a new card layout with the specified horizontal and
vertical gaps. The horizontal gaps are placed at the left and
right edges. The vertical gaps are placed at the top and bottom
edges.

**Parameters:** hgap

- the horizontal gap.
**Parameters:** vgap

- the vertical gap.

---

#### Constructor Detail

CardLayout

```java
public CardLayout()
```

Creates a new card layout with gaps of size zero.

---

#### CardLayout

public CardLayout()

Creates a new card layout with gaps of size zero.

CardLayout

```java
public CardLayout​(int hgap,
int vgap)
```

Creates a new card layout with the specified horizontal and
vertical gaps. The horizontal gaps are placed at the left and
right edges. The vertical gaps are placed at the top and bottom
edges.

**Parameters:** hgap

- the horizontal gap.
**Parameters:** vgap

- the vertical gap.

---

#### CardLayout

public CardLayout​(int hgap,
int vgap)

Creates a new card layout with the specified horizontal and
vertical gaps. The horizontal gaps are placed at the left and
right edges. The vertical gaps are placed at the top and bottom
edges.

Method Detail

- getHgap

```java
public int getHgap()
```

Gets the horizontal gap between components.

**Returns:** the horizontal gap between components.
**Since:** 1.1
**See Also:** setHgap(int)

,

getVgap()

- setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components.

**Parameters:** hgap

- the horizontal gap between components.
**Since:** 1.1
**See Also:** getHgap()

,

setVgap(int)

- getVgap

```java
public int getVgap()
```

Gets the vertical gap between components.

**Returns:** the vertical gap between components.
**See Also:** setVgap(int)

,

getHgap()

- setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components.

**Parameters:** vgap

- the vertical gap between components.
**Since:** 1.1
**See Also:** getVgap()

,

setHgap(int)

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to this card layout's internal
table of names. The object specified by

constraints

must be a string. The card layout stores this string as a key-value
pair that can be used for random access to a particular card.
By calling the

show

method, an application can
display the component with the specified name.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added.
**Parameters:** constraints

- a tag that identifies a particular
card in the layout.
**Throws:** IllegalArgumentException

- if the constraint is not a string.
**See Also:** show(java.awt.Container, java.lang.String)

- addLayoutComponent

```java
@Deprecated

public void addLayoutComponent​(
String
name,

Component
comp)
```

Deprecated.

replaced by

addLayoutComponent(Component, Object)

.

Description copied from interface:

LayoutManager

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the string to be associated with the component
**Parameters:** comp

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.
If the card was visible on top, the next card underneath it is shown.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to be removed.
**See Also:** Container.remove(java.awt.Component)

,

Container.removeAll()

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Determines the preferred size of the container argument using
this card layout.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the parent container in which to do the layout
**Returns:** the preferred dimensions to lay out the subcomponents
of the specified container
**See Also:** Container.getPreferredSize()

,

minimumLayoutSize(java.awt.Container)

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Calculates the minimum size for the specified panel.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the parent container in which to do the layout
**Returns:** the minimum dimensions required to lay out the
subcomponents of the specified container
**See Also:** Container.doLayout()

,

preferredLayoutSize(java.awt.Container)

- maximumLayoutSize

```java
public
Dimension
maximumLayoutSize​(
Container
target)
```

Returns the maximum dimensions for this layout given the components
in the specified target container.

**Specified by:** maximumLayoutSize

in interface

LayoutManager2
**Parameters:** target

- the component which needs to be laid out
**Returns:** the maximum size of the container
**See Also:** Container

,

minimumLayoutSize(java.awt.Container)

,

preferredLayoutSize(java.awt.Container)

- getLayoutAlignmentX

```java
public float getLayoutAlignmentX​(
Container
parent)
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Specified by:** getLayoutAlignmentX

in interface

LayoutManager2
**Parameters:** parent

- the target container
**Returns:** the x-axis alignment preference

- getLayoutAlignmentY

```java
public float getLayoutAlignmentY​(
Container
parent)
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Specified by:** getLayoutAlignmentY

in interface

LayoutManager2
**Parameters:** parent

- the target container
**Returns:** the y-axis alignment preference

- invalidateLayout

```java
public void invalidateLayout​(
Container
target)
```

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

**Specified by:** invalidateLayout

in interface

LayoutManager2
**Parameters:** target

- the target container

- layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Lays out the specified container using this card layout.

Each component in the

parent

container is reshaped
to be the size of the container, minus space for surrounding
insets, horizontal gaps, and vertical gaps.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the parent container in which to do the layout
**See Also:** Container.doLayout()

- first

```java
public void first​(
Container
parent)
```

Flips to the first card of the container.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** last(java.awt.Container)

- next

```java
public void next​(
Container
parent)
```

Flips to the next card of the specified container. If the
currently visible card is the last one, this method flips to the
first card in the layout.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** previous(java.awt.Container)

- previous

```java
public void previous​(
Container
parent)
```

Flips to the previous card of the specified container. If the
currently visible card is the first one, this method flips to the
last card in the layout.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** next(java.awt.Container)

- last

```java
public void last​(
Container
parent)
```

Flips to the last card of the container.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** first(java.awt.Container)

- show

```java
public void show​(
Container
parent,

String
name)
```

Flips to the component that was added to this layout with the
specified

name

, using

addLayoutComponent

.
If no such component exists, then nothing happens.

**Parameters:** parent

- the parent container in which to do the layout
**Parameters:** name

- the component name
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of the state of this card layout.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this card layout.

---

#### Method Detail

getHgap

```java
public int getHgap()
```

Gets the horizontal gap between components.

**Returns:** the horizontal gap between components.
**Since:** 1.1
**See Also:** setHgap(int)

,

getVgap()

---

#### getHgap

public int getHgap()

Gets the horizontal gap between components.

setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components.

**Parameters:** hgap

- the horizontal gap between components.
**Since:** 1.1
**See Also:** getHgap()

,

setVgap(int)

---

#### setHgap

public void setHgap​(int hgap)

Sets the horizontal gap between components.

getVgap

```java
public int getVgap()
```

Gets the vertical gap between components.

**Returns:** the vertical gap between components.
**See Also:** setVgap(int)

,

getHgap()

---

#### getVgap

public int getVgap()

Gets the vertical gap between components.

setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components.

**Parameters:** vgap

- the vertical gap between components.
**Since:** 1.1
**See Also:** getVgap()

,

setHgap(int)

---

#### setVgap

public void setVgap​(int vgap)

Sets the vertical gap between components.

addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to this card layout's internal
table of names. The object specified by

constraints

must be a string. The card layout stores this string as a key-value
pair that can be used for random access to a particular card.
By calling the

show

method, an application can
display the component with the specified name.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added.
**Parameters:** constraints

- a tag that identifies a particular
card in the layout.
**Throws:** IllegalArgumentException

- if the constraint is not a string.
**See Also:** show(java.awt.Container, java.lang.String)

---

#### addLayoutComponent

public void addLayoutComponent​(

Component

comp,

Object

constraints)

Adds the specified component to this card layout's internal
table of names. The object specified by

constraints

must be a string. The card layout stores this string as a key-value
pair that can be used for random access to a particular card.
By calling the

show

method, an application can
display the component with the specified name.

addLayoutComponent

```java
@Deprecated

public void addLayoutComponent​(
String
name,

Component
comp)
```

Deprecated.

replaced by

addLayoutComponent(Component, Object)

.

Description copied from interface:

LayoutManager

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the string to be associated with the component
**Parameters:** comp

- the component to be added

---

#### addLayoutComponent

@Deprecated

public void addLayoutComponent​(

String

name,

Component

comp)

Description copied from interface:

LayoutManager

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.
If the card was visible on top, the next card underneath it is shown.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to be removed.
**See Also:** Container.remove(java.awt.Component)

,

Container.removeAll()

---

#### removeLayoutComponent

public void removeLayoutComponent​(

Component

comp)

Removes the specified component from the layout.
If the card was visible on top, the next card underneath it is shown.

preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Determines the preferred size of the container argument using
this card layout.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the parent container in which to do the layout
**Returns:** the preferred dimensions to lay out the subcomponents
of the specified container
**See Also:** Container.getPreferredSize()

,

minimumLayoutSize(java.awt.Container)

---

#### preferredLayoutSize

public

Dimension

preferredLayoutSize​(

Container

parent)

Determines the preferred size of the container argument using
this card layout.

minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Calculates the minimum size for the specified panel.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the parent container in which to do the layout
**Returns:** the minimum dimensions required to lay out the
subcomponents of the specified container
**See Also:** Container.doLayout()

,

preferredLayoutSize(java.awt.Container)

---

#### minimumLayoutSize

public

Dimension

minimumLayoutSize​(

Container

parent)

Calculates the minimum size for the specified panel.

maximumLayoutSize

```java
public
Dimension
maximumLayoutSize​(
Container
target)
```

Returns the maximum dimensions for this layout given the components
in the specified target container.

**Specified by:** maximumLayoutSize

in interface

LayoutManager2
**Parameters:** target

- the component which needs to be laid out
**Returns:** the maximum size of the container
**See Also:** Container

,

minimumLayoutSize(java.awt.Container)

,

preferredLayoutSize(java.awt.Container)

---

#### maximumLayoutSize

public

Dimension

maximumLayoutSize​(

Container

target)

Returns the maximum dimensions for this layout given the components
in the specified target container.

getLayoutAlignmentX

```java
public float getLayoutAlignmentX​(
Container
parent)
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Specified by:** getLayoutAlignmentX

in interface

LayoutManager2
**Parameters:** parent

- the target container
**Returns:** the x-axis alignment preference

---

#### getLayoutAlignmentX

public float getLayoutAlignmentX​(

Container

parent)

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

getLayoutAlignmentY

```java
public float getLayoutAlignmentY​(
Container
parent)
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Specified by:** getLayoutAlignmentY

in interface

LayoutManager2
**Parameters:** parent

- the target container
**Returns:** the y-axis alignment preference

---

#### getLayoutAlignmentY

public float getLayoutAlignmentY​(

Container

parent)

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

invalidateLayout

```java
public void invalidateLayout​(
Container
target)
```

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

**Specified by:** invalidateLayout

in interface

LayoutManager2
**Parameters:** target

- the target container

---

#### invalidateLayout

public void invalidateLayout​(

Container

target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Lays out the specified container using this card layout.

Each component in the

parent

container is reshaped
to be the size of the container, minus space for surrounding
insets, horizontal gaps, and vertical gaps.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the parent container in which to do the layout
**See Also:** Container.doLayout()

---

#### layoutContainer

public void layoutContainer​(

Container

parent)

Lays out the specified container using this card layout.

Each component in the

parent

container is reshaped
to be the size of the container, minus space for surrounding
insets, horizontal gaps, and vertical gaps.

Each component in the

parent

container is reshaped
to be the size of the container, minus space for surrounding
insets, horizontal gaps, and vertical gaps.

first

```java
public void first​(
Container
parent)
```

Flips to the first card of the container.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** last(java.awt.Container)

---

#### first

public void first​(

Container

parent)

Flips to the first card of the container.

next

```java
public void next​(
Container
parent)
```

Flips to the next card of the specified container. If the
currently visible card is the last one, this method flips to the
first card in the layout.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** previous(java.awt.Container)

---

#### next

public void next​(

Container

parent)

Flips to the next card of the specified container. If the
currently visible card is the last one, this method flips to the
first card in the layout.

previous

```java
public void previous​(
Container
parent)
```

Flips to the previous card of the specified container. If the
currently visible card is the first one, this method flips to the
last card in the layout.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** next(java.awt.Container)

---

#### previous

public void previous​(

Container

parent)

Flips to the previous card of the specified container. If the
currently visible card is the first one, this method flips to the
last card in the layout.

last

```java
public void last​(
Container
parent)
```

Flips to the last card of the container.

**Parameters:** parent

- the parent container in which to do the layout
**See Also:** first(java.awt.Container)

---

#### last

public void last​(

Container

parent)

Flips to the last card of the container.

show

```java
public void show​(
Container
parent,

String
name)
```

Flips to the component that was added to this layout with the
specified

name

, using

addLayoutComponent

.
If no such component exists, then nothing happens.

**Parameters:** parent

- the parent container in which to do the layout
**Parameters:** name

- the component name
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

---

#### show

public void show​(

Container

parent,

String

name)

Flips to the component that was added to this layout with the
specified

name

, using

addLayoutComponent

.
If no such component exists, then nothing happens.

toString

```java
public
String
toString()
```

Returns a string representation of the state of this card layout.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this card layout.

---

#### toString

public

String

toString()

Returns a string representation of the state of this card layout.

---

