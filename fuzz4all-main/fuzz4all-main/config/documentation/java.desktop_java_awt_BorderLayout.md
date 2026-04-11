# Class BorderLayout

**Source:** `java.desktop\java\awt\BorderLayout.html`

### Class Description

```java
public class
BorderLayout

extends
Object

implements
LayoutManager2
,
Serializable
```

A border layout lays out a container, arranging and resizing
its components to fit in five regions:
north, south, east, west, and center.
Each region may contain no more than one component, and
is identified by a corresponding constant:

NORTH

,

SOUTH

,

EAST

,

WEST

, and

CENTER

. When adding a
component to a container with a border layout, use one of these
five constants, for example:

```java
Panel p = new Panel();
p.setLayout(new BorderLayout());
p.add(new Button("Okay"), BorderLayout.SOUTH);
```

As a convenience,

BorderLayout

interprets the
absence of a string specification the same as the constant

CENTER

:

```java
Panel p2 = new Panel();
p2.setLayout(new BorderLayout());
p2.add(new TextArea()); // Same as p.add(new TextArea(), BorderLayout.CENTER);
```

In addition,

BorderLayout

supports the relative
positioning constants,

PAGE_START

,

PAGE_END

,

LINE_START

, and

LINE_END

.
In a container whose

ComponentOrientation

is set to

ComponentOrientation.LEFT_TO_RIGHT

, these constants map to

NORTH

,

SOUTH

,

WEST

, and

EAST

, respectively.

For compatibility with previous releases,

BorderLayout

also includes the relative positioning constants

BEFORE_FIRST_LINE

,

AFTER_LAST_LINE

,

BEFORE_LINE_BEGINS

and

AFTER_LINE_ENDS

. These are equivalent to

PAGE_START

,

PAGE_END

,

LINE_START

and

LINE_END

respectively. For
consistency with the relative positioning constants used by other
components, the latter constants are preferred.

Mixing both absolute and relative positioning constants can lead to
unpredictable results. If
you use both types, the relative constants will take precedence.
For example, if you add components using both the

NORTH

and

PAGE_START

constants in a container whose
orientation is

LEFT_TO_RIGHT

, only the

PAGE_START

will be laid out.

NOTE: Currently,

BorderLayout

does not support vertical
orientations. The

isVertical

setting on the container's

ComponentOrientation

is not respected.

The components are laid out according to their
preferred sizes and the constraints of the container's size.
The

NORTH

and

SOUTH

components may
be stretched horizontally; the

EAST

and

WEST

components may be stretched vertically;
the

CENTER

component may stretch both horizontally
and vertically to fill any space left over.

Here is an example of five buttons in an applet laid out using
the

BorderLayout

layout manager:

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

**All Implemented Interfaces:** LayoutManager

,

LayoutManager2

,

Serializable

---

### Field Details

#### public static final
String
NORTH

The north layout constraint (top of container).

**See Also:**
- Constant Field Values

---

#### public static final
String
SOUTH

The south layout constraint (bottom of container).

**See Also:**
- Constant Field Values

---

#### public static final
String
EAST

The east layout constraint (right side of container).

**See Also:**
- Constant Field Values

---

#### public static final
String
WEST

The west layout constraint (left side of container).

**See Also:**
- Constant Field Values

---

#### public static final
String
CENTER

The center layout constraint (middle of container).

**See Also:**
- Constant Field Values

---

#### public static final
String
BEFORE_FIRST_LINE

Synonym for PAGE_START. Exists for compatibility with previous
versions. PAGE_START is preferred.

**See Also:**
- PAGE_START

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final
String
AFTER_LAST_LINE

Synonym for PAGE_END. Exists for compatibility with previous
versions. PAGE_END is preferred.

**See Also:**
- PAGE_END

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final
String
BEFORE_LINE_BEGINS

Synonym for LINE_START. Exists for compatibility with previous
versions. LINE_START is preferred.

**See Also:**
- LINE_START

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final
String
AFTER_LINE_ENDS

Synonym for LINE_END. Exists for compatibility with previous
versions. LINE_END is preferred.

**See Also:**
- LINE_END

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final
String
PAGE_START

The component comes before the first line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to NORTH.

**See Also:**
- Component.getComponentOrientation()

,

Constant Field Values

**Since:**
- 1.4

---

#### public static final
String
PAGE_END

The component comes after the last line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to SOUTH.

**See Also:**
- Component.getComponentOrientation()

,

Constant Field Values

**Since:**
- 1.4

---

#### public static final
String
LINE_START

The component goes at the beginning of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to WEST.

**See Also:**
- Component.getComponentOrientation()

,

Constant Field Values

**Since:**
- 1.4

---

#### public static final
String
LINE_END

The component goes at the end of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to EAST.

**See Also:**
- Component.getComponentOrientation()

,

Constant Field Values

**Since:**
- 1.4

---

### Constructor Details

#### public BorderLayout()

Constructs a new border layout with
no gaps between components.

---

#### public BorderLayout​(int hgap,
int vgap)

Constructs a border layout with the specified gaps
between components.
The horizontal gap is specified by

hgap

and the vertical gap is specified by

vgap

.

**Parameters:**
- hgap

- the horizontal gap.
- vgap

- the vertical gap.

---

### Method Details

#### public int getHgap()

Returns the horizontal gap between components.

**Returns:**
- the horizontal gap between components

**Since:**
- 1.1

---

#### public void setHgap​(int hgap)

Sets the horizontal gap between components.

**Parameters:**
- hgap

- the horizontal gap between components

**Since:**
- 1.1

---

#### public int getVgap()

Returns the vertical gap between components.

**Returns:**
- the vertical gap between components

**Since:**
- 1.1

---

#### public void setVgap​(int vgap)

Sets the vertical gap between components.

**Parameters:**
- vgap

- the vertical gap between components

**Since:**
- 1.1

---

#### public void addLayoutComponent​(
Component
comp,

Object
constraints)

Adds the specified component to the layout, using the specified
constraint object. For border layouts, the constraint must be
one of the following constants:

NORTH

,

SOUTH

,

EAST

,

WEST

, or

CENTER

.

Most applications do not call this method directly. This method
is called when a component is added to a container using the

Container.add

method with the same argument types.

**Specified by:**
- addLayoutComponent

in interface

LayoutManager2

**Parameters:**
- comp

- the component to be added.
- constraints

- an object that specifies how and where
the component is added to the layout.

**Throws:**
- IllegalArgumentException

- if the constraint object is not
a string, or if it not one of the five specified constants.

**See Also:**
- Container.add(java.awt.Component, java.lang.Object)

**Since:**
- 1.1

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

Removes the specified component from this border layout. This
method is called when a container calls its

remove

or

removeAll

methods. Most applications do not call this
method directly.

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
Component
getLayoutComponent​(
Object
constraints)

Gets the component that was added using the given constraint

**Parameters:**
- constraints

- the desired constraint, one of

CENTER

,

NORTH

,

SOUTH

,

WEST

,

EAST

,

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END

**Returns:**
- the component at the given location, or

null

if
the location is empty

**Throws:**
- IllegalArgumentException

- if the constraint object is
not one of the nine specified constants

**See Also:**
- addLayoutComponent(java.awt.Component, java.lang.Object)

**Since:**
- 1.5

---

#### public
Component
getLayoutComponent​(
Container
target,

Object
constraints)

Returns the component that corresponds to the given constraint location
based on the target

Container

's component orientation.
Components added with the relative constraints

PAGE_START

,

PAGE_END

,

LINE_START

, and

LINE_END

take precedence over components added with the explicit constraints

NORTH

,

SOUTH

,

WEST

, and

EAST

.
The

Container

's component orientation is used to determine the location of components
added with

LINE_START

and

LINE_END

.

**Parameters:**
- constraints

- the desired absolute position, one of

CENTER

,

NORTH

,

SOUTH

,

EAST

,

WEST
- target

- the

Container

used to obtain
the constraint location based on the target

Container

's component orientation.

**Returns:**
- the component at the given location, or

null

if
the location is empty

**Throws:**
- IllegalArgumentException

- if the constraint object is
not one of the five specified constants
- NullPointerException

- if the target parameter is null

**See Also:**
- addLayoutComponent(java.awt.Component, java.lang.Object)

**Since:**
- 1.5

---

#### public
Object
getConstraints​(
Component
comp)

Gets the constraints for the specified component

**Parameters:**
- comp

- the component to be queried

**Returns:**
- the constraint for the specified component,
or null if component is null or is not present
in this layout

**See Also:**
- addLayoutComponent(java.awt.Component, java.lang.Object)

**Since:**
- 1.5

---

#### public
Dimension
minimumLayoutSize​(
Container
target)

Determines the minimum size of the

target

container
using this layout manager.

This method is called when a container calls its

getMinimumSize

method. Most applications do not call
this method directly.

**Specified by:**
- minimumLayoutSize

in interface

LayoutManager

**Parameters:**
- target

- the container in which to do the layout.

**Returns:**
- the minimum dimensions needed to lay out the subcomponents
of the specified container.

**See Also:**
- Container

,

preferredLayoutSize(java.awt.Container)

,

Container.getMinimumSize()

---

#### public
Dimension
preferredLayoutSize​(
Container
target)

Determines the preferred size of the

target

container using this layout manager, based on the components
in the container.

Most applications do not call this method directly. This method
is called when a container calls its

getPreferredSize

method.

**Specified by:**
- preferredLayoutSize

in interface

LayoutManager

**Parameters:**
- target

- the container in which to do the layout.

**Returns:**
- the preferred dimensions to lay out the subcomponents
of the specified container.

**See Also:**
- Container

,

minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

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
target)

Lays out the container argument using this border layout.

This method actually reshapes the components in the specified
container in order to satisfy the constraints of this

BorderLayout

object. The

NORTH

and

SOUTH

components, if any, are placed at
the top and bottom of the container, respectively. The

WEST

and

EAST

components are
then placed on the left and right, respectively. Finally,
the

CENTER

object is placed in any remaining
space in the middle.

Most applications do not call this method directly. This method
is called when a container calls its

doLayout

method.

**Specified by:**
- layoutContainer

in interface

LayoutManager

**Parameters:**
- target

- the container in which to do the layout.

**See Also:**
- Container

,

Container.doLayout()

---

#### public
String
toString()

Returns a string representation of the state of this border layout.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this border layout.

---

### Additional Sections

#### Class BorderLayout

java.lang.Object

- java.awt.BorderLayout

java.awt.BorderLayout

**All Implemented Interfaces:** LayoutManager

,

LayoutManager2

,

Serializable

```java
public class
BorderLayout

extends
Object

implements
LayoutManager2
,
Serializable
```

A border layout lays out a container, arranging and resizing
its components to fit in five regions:
north, south, east, west, and center.
Each region may contain no more than one component, and
is identified by a corresponding constant:

NORTH

,

SOUTH

,

EAST

,

WEST

, and

CENTER

. When adding a
component to a container with a border layout, use one of these
five constants, for example:

```java
Panel p = new Panel();
p.setLayout(new BorderLayout());
p.add(new Button("Okay"), BorderLayout.SOUTH);
```

As a convenience,

BorderLayout

interprets the
absence of a string specification the same as the constant

CENTER

:

```java
Panel p2 = new Panel();
p2.setLayout(new BorderLayout());
p2.add(new TextArea()); // Same as p.add(new TextArea(), BorderLayout.CENTER);
```

In addition,

BorderLayout

supports the relative
positioning constants,

PAGE_START

,

PAGE_END

,

LINE_START

, and

LINE_END

.
In a container whose

ComponentOrientation

is set to

ComponentOrientation.LEFT_TO_RIGHT

, these constants map to

NORTH

,

SOUTH

,

WEST

, and

EAST

, respectively.

For compatibility with previous releases,

BorderLayout

also includes the relative positioning constants

BEFORE_FIRST_LINE

,

AFTER_LAST_LINE

,

BEFORE_LINE_BEGINS

and

AFTER_LINE_ENDS

. These are equivalent to

PAGE_START

,

PAGE_END

,

LINE_START

and

LINE_END

respectively. For
consistency with the relative positioning constants used by other
components, the latter constants are preferred.

Mixing both absolute and relative positioning constants can lead to
unpredictable results. If
you use both types, the relative constants will take precedence.
For example, if you add components using both the

NORTH

and

PAGE_START

constants in a container whose
orientation is

LEFT_TO_RIGHT

, only the

PAGE_START

will be laid out.

NOTE: Currently,

BorderLayout

does not support vertical
orientations. The

isVertical

setting on the container's

ComponentOrientation

is not respected.

The components are laid out according to their
preferred sizes and the constraints of the container's size.
The

NORTH

and

SOUTH

components may
be stretched horizontally; the

EAST

and

WEST

components may be stretched vertically;
the

CENTER

component may stretch both horizontally
and vertically to fill any space left over.

Here is an example of five buttons in an applet laid out using
the

BorderLayout

layout manager:

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

**Since:** 1.0
**See Also:** Container.add(String, Component)

,

ComponentOrientation

,

Serialized Form

public class

BorderLayout

extends

Object

implements

LayoutManager2

,

Serializable

A border layout lays out a container, arranging and resizing
its components to fit in five regions:
north, south, east, west, and center.
Each region may contain no more than one component, and
is identified by a corresponding constant:

NORTH

,

SOUTH

,

EAST

,

WEST

, and

CENTER

. When adding a
component to a container with a border layout, use one of these
five constants, for example:

```java
Panel p = new Panel();
p.setLayout(new BorderLayout());
p.add(new Button("Okay"), BorderLayout.SOUTH);
```

As a convenience,

BorderLayout

interprets the
absence of a string specification the same as the constant

CENTER

:

```java
Panel p2 = new Panel();
p2.setLayout(new BorderLayout());
p2.add(new TextArea()); // Same as p.add(new TextArea(), BorderLayout.CENTER);
```

In addition,

BorderLayout

supports the relative
positioning constants,

PAGE_START

,

PAGE_END

,

LINE_START

, and

LINE_END

.
In a container whose

ComponentOrientation

is set to

ComponentOrientation.LEFT_TO_RIGHT

, these constants map to

NORTH

,

SOUTH

,

WEST

, and

EAST

, respectively.

For compatibility with previous releases,

BorderLayout

also includes the relative positioning constants

BEFORE_FIRST_LINE

,

AFTER_LAST_LINE

,

BEFORE_LINE_BEGINS

and

AFTER_LINE_ENDS

. These are equivalent to

PAGE_START

,

PAGE_END

,

LINE_START

and

LINE_END

respectively. For
consistency with the relative positioning constants used by other
components, the latter constants are preferred.

Mixing both absolute and relative positioning constants can lead to
unpredictable results. If
you use both types, the relative constants will take precedence.
For example, if you add components using both the

NORTH

and

PAGE_START

constants in a container whose
orientation is

LEFT_TO_RIGHT

, only the

PAGE_START

will be laid out.

NOTE: Currently,

BorderLayout

does not support vertical
orientations. The

isVertical

setting on the container's

ComponentOrientation

is not respected.

The components are laid out according to their
preferred sizes and the constraints of the container's size.
The

NORTH

and

SOUTH

components may
be stretched horizontally; the

EAST

and

WEST

components may be stretched vertically;
the

CENTER

component may stretch both horizontally
and vertically to fill any space left over.

Here is an example of five buttons in an applet laid out using
the

BorderLayout

layout manager:

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

Panel p = new Panel();
p.setLayout(new BorderLayout());
p.add(new Button("Okay"), BorderLayout.SOUTH);

Panel p2 = new Panel();
p2.setLayout(new BorderLayout());
p2.add(new TextArea()); // Same as p.add(new TextArea(), BorderLayout.CENTER);

In addition,

BorderLayout

supports the relative
positioning constants,

PAGE_START

,

PAGE_END

,

LINE_START

, and

LINE_END

.
In a container whose

ComponentOrientation

is set to

ComponentOrientation.LEFT_TO_RIGHT

, these constants map to

NORTH

,

SOUTH

,

WEST

, and

EAST

, respectively.

For compatibility with previous releases,

BorderLayout

also includes the relative positioning constants

BEFORE_FIRST_LINE

,

AFTER_LAST_LINE

,

BEFORE_LINE_BEGINS

and

AFTER_LINE_ENDS

. These are equivalent to

PAGE_START

,

PAGE_END

,

LINE_START

and

LINE_END

respectively. For
consistency with the relative positioning constants used by other
components, the latter constants are preferred.

Mixing both absolute and relative positioning constants can lead to
unpredictable results. If
you use both types, the relative constants will take precedence.
For example, if you add components using both the

NORTH

and

PAGE_START

constants in a container whose
orientation is

LEFT_TO_RIGHT

, only the

PAGE_START

will be laid out.

NOTE: Currently,

BorderLayout

does not support vertical
orientations. The

isVertical

setting on the container's

ComponentOrientation

is not respected.

The components are laid out according to their
preferred sizes and the constraints of the container's size.
The

NORTH

and

SOUTH

components may
be stretched horizontally; the

EAST

and

WEST

components may be stretched vertically;
the

CENTER

component may stretch both horizontally
and vertically to fill any space left over.

Here is an example of five buttons in an applet laid out using
the

BorderLayout

layout manager:

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

For compatibility with previous releases,

BorderLayout

also includes the relative positioning constants

BEFORE_FIRST_LINE

,

AFTER_LAST_LINE

,

BEFORE_LINE_BEGINS

and

AFTER_LINE_ENDS

. These are equivalent to

PAGE_START

,

PAGE_END

,

LINE_START

and

LINE_END

respectively. For
consistency with the relative positioning constants used by other
components, the latter constants are preferred.

Mixing both absolute and relative positioning constants can lead to
unpredictable results. If
you use both types, the relative constants will take precedence.
For example, if you add components using both the

NORTH

and

PAGE_START

constants in a container whose
orientation is

LEFT_TO_RIGHT

, only the

PAGE_START

will be laid out.

NOTE: Currently,

BorderLayout

does not support vertical
orientations. The

isVertical

setting on the container's

ComponentOrientation

is not respected.

The components are laid out according to their
preferred sizes and the constraints of the container's size.
The

NORTH

and

SOUTH

components may
be stretched horizontally; the

EAST

and

WEST

components may be stretched vertically;
the

CENTER

component may stretch both horizontally
and vertically to fill any space left over.

Here is an example of five buttons in an applet laid out using
the

BorderLayout

layout manager:

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

Mixing both absolute and relative positioning constants can lead to
unpredictable results. If
you use both types, the relative constants will take precedence.
For example, if you add components using both the

NORTH

and

PAGE_START

constants in a container whose
orientation is

LEFT_TO_RIGHT

, only the

PAGE_START

will be laid out.

NOTE: Currently,

BorderLayout

does not support vertical
orientations. The

isVertical

setting on the container's

ComponentOrientation

is not respected.

The components are laid out according to their
preferred sizes and the constraints of the container's size.
The

NORTH

and

SOUTH

components may
be stretched horizontally; the

EAST

and

WEST

components may be stretched vertically;
the

CENTER

component may stretch both horizontally
and vertically to fill any space left over.

Here is an example of five buttons in an applet laid out using
the

BorderLayout

layout manager:

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

NOTE: Currently,

BorderLayout

does not support vertical
orientations. The

isVertical

setting on the container's

ComponentOrientation

is not respected.

The components are laid out according to their
preferred sizes and the constraints of the container's size.
The

NORTH

and

SOUTH

components may
be stretched horizontally; the

EAST

and

WEST

components may be stretched vertically;
the

CENTER

component may stretch both horizontally
and vertically to fill any space left over.

Here is an example of five buttons in an applet laid out using
the

BorderLayout

layout manager:

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

The components are laid out according to their
preferred sizes and the constraints of the container's size.
The

NORTH

and

SOUTH

components may
be stretched horizontally; the

EAST

and

WEST

components may be stretched vertically;
the

CENTER

component may stretch both horizontally
and vertically to fill any space left over.

Here is an example of five buttons in an applet laid out using
the

BorderLayout

layout manager:

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

Here is an example of five buttons in an applet laid out using
the

BorderLayout

layout manager:

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

The code for this applet is as follows:

```java
import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}
```

import java.awt.*;
import java.applet.Applet;

public class buttonDir extends Applet {
public void init() {
setLayout(new BorderLayout());
add(new Button("North"), BorderLayout.NORTH);
add(new Button("South"), BorderLayout.SOUTH);
add(new Button("East"), BorderLayout.EAST);
add(new Button("West"), BorderLayout.WEST);
add(new Button("Center"), BorderLayout.CENTER);
}
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

AFTER_LAST_LINE

Synonym for PAGE_END.

static

String

AFTER_LINE_ENDS

Synonym for LINE_END.

static

String

BEFORE_FIRST_LINE

Synonym for PAGE_START.

static

String

BEFORE_LINE_BEGINS

Synonym for LINE_START.

static

String

CENTER

The center layout constraint (middle of container).

static

String

EAST

The east layout constraint (right side of container).

static

String

LINE_END

The component goes at the end of the line direction for the
layout.

static

String

LINE_START

The component goes at the beginning of the line direction for the
layout.

static

String

NORTH

The north layout constraint (top of container).

static

String

PAGE_END

The component comes after the last line of the layout's content.

static

String

PAGE_START

The component comes before the first line of the layout's content.

static

String

SOUTH

The south layout constraint (bottom of container).

static

String

WEST

The west layout constraint (left side of container).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BorderLayout

()

Constructs a new border layout with
no gaps between components.

BorderLayout

​(int hgap,
int vgap)

Constructs a border layout with the specified gaps
between components.

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

Adds the specified component to the layout, using the specified
constraint object.

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

Object

getConstraints

​(

Component

comp)

Gets the constraints for the specified component

int

getHgap

()

Returns the horizontal gap between components.

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

Component

getLayoutComponent

​(

Container

target,

Object

constraints)

Returns the component that corresponds to the given constraint location
based on the target

Container

's component orientation.

Component

getLayoutComponent

​(

Object

constraints)

Gets the component that was added using the given constraint

int

getVgap

()

Returns the vertical gap between components.

void

invalidateLayout

​(

Container

target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

void

layoutContainer

​(

Container

target)

Lays out the container argument using this border layout.

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

target)

Determines the minimum size of the

target

container
using this layout manager.

Dimension

preferredLayoutSize

​(

Container

target)

Determines the preferred size of the

target

container using this layout manager, based on the components
in the container.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from this border layout.

void

setHgap

​(int hgap)

Sets the horizontal gap between components.

void

setVgap

​(int vgap)

Sets the vertical gap between components.

String

toString

()

Returns a string representation of the state of this border layout.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

AFTER_LAST_LINE

Synonym for PAGE_END.

static

String

AFTER_LINE_ENDS

Synonym for LINE_END.

static

String

BEFORE_FIRST_LINE

Synonym for PAGE_START.

static

String

BEFORE_LINE_BEGINS

Synonym for LINE_START.

static

String

CENTER

The center layout constraint (middle of container).

static

String

EAST

The east layout constraint (right side of container).

static

String

LINE_END

The component goes at the end of the line direction for the
layout.

static

String

LINE_START

The component goes at the beginning of the line direction for the
layout.

static

String

NORTH

The north layout constraint (top of container).

static

String

PAGE_END

The component comes after the last line of the layout's content.

static

String

PAGE_START

The component comes before the first line of the layout's content.

static

String

SOUTH

The south layout constraint (bottom of container).

static

String

WEST

The west layout constraint (left side of container).

---

#### Field Summary

Synonym for PAGE_END.

Synonym for LINE_END.

Synonym for PAGE_START.

Synonym for LINE_START.

The center layout constraint (middle of container).

The east layout constraint (right side of container).

The component goes at the end of the line direction for the
layout.

The component goes at the beginning of the line direction for the
layout.

The north layout constraint (top of container).

The component comes after the last line of the layout's content.

The component comes before the first line of the layout's content.

The south layout constraint (bottom of container).

The west layout constraint (left side of container).

Constructor Summary

Constructors

Constructor

Description

BorderLayout

()

Constructs a new border layout with
no gaps between components.

BorderLayout

​(int hgap,
int vgap)

Constructs a border layout with the specified gaps
between components.

---

#### Constructor Summary

Constructs a new border layout with
no gaps between components.

Constructs a border layout with the specified gaps
between components.

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

Adds the specified component to the layout, using the specified
constraint object.

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

Object

getConstraints

​(

Component

comp)

Gets the constraints for the specified component

int

getHgap

()

Returns the horizontal gap between components.

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

Component

getLayoutComponent

​(

Container

target,

Object

constraints)

Returns the component that corresponds to the given constraint location
based on the target

Container

's component orientation.

Component

getLayoutComponent

​(

Object

constraints)

Gets the component that was added using the given constraint

int

getVgap

()

Returns the vertical gap between components.

void

invalidateLayout

​(

Container

target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

void

layoutContainer

​(

Container

target)

Lays out the container argument using this border layout.

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

target)

Determines the minimum size of the

target

container
using this layout manager.

Dimension

preferredLayoutSize

​(

Container

target)

Determines the preferred size of the

target

container using this layout manager, based on the components
in the container.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from this border layout.

void

setHgap

​(int hgap)

Sets the horizontal gap between components.

void

setVgap

​(int vgap)

Sets the vertical gap between components.

String

toString

()

Returns a string representation of the state of this border layout.

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

Adds the specified component to the layout, using the specified
constraint object.

Deprecated.

replaced by

addLayoutComponent(Component, Object)

.

Gets the constraints for the specified component

Returns the horizontal gap between components.

Returns the alignment along the x axis.

Returns the alignment along the y axis.

Returns the component that corresponds to the given constraint location
based on the target

Container

's component orientation.

Gets the component that was added using the given constraint

Returns the vertical gap between components.

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

Lays out the container argument using this border layout.

Returns the maximum dimensions for this layout given the components
in the specified target container.

Determines the minimum size of the

target

container
using this layout manager.

Determines the preferred size of the

target

container using this layout manager, based on the components
in the container.

Removes the specified component from this border layout.

Sets the horizontal gap between components.

Sets the vertical gap between components.

Returns a string representation of the state of this border layout.

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

============ FIELD DETAIL ===========

- Field Detail

- NORTH

```java
public static final
String
NORTH
```

The north layout constraint (top of container).

**See Also:** Constant Field Values

- SOUTH

```java
public static final
String
SOUTH
```

The south layout constraint (bottom of container).

**See Also:** Constant Field Values

- EAST

```java
public static final
String
EAST
```

The east layout constraint (right side of container).

**See Also:** Constant Field Values

- WEST

```java
public static final
String
WEST
```

The west layout constraint (left side of container).

**See Also:** Constant Field Values

- CENTER

```java
public static final
String
CENTER
```

The center layout constraint (middle of container).

**See Also:** Constant Field Values

- BEFORE_FIRST_LINE

```java
public static final
String
BEFORE_FIRST_LINE
```

Synonym for PAGE_START. Exists for compatibility with previous
versions. PAGE_START is preferred.

**Since:** 1.2
**See Also:** PAGE_START

,

Constant Field Values

- AFTER_LAST_LINE

```java
public static final
String
AFTER_LAST_LINE
```

Synonym for PAGE_END. Exists for compatibility with previous
versions. PAGE_END is preferred.

**Since:** 1.2
**See Also:** PAGE_END

,

Constant Field Values

- BEFORE_LINE_BEGINS

```java
public static final
String
BEFORE_LINE_BEGINS
```

Synonym for LINE_START. Exists for compatibility with previous
versions. LINE_START is preferred.

**Since:** 1.2
**See Also:** LINE_START

,

Constant Field Values

- AFTER_LINE_ENDS

```java
public static final
String
AFTER_LINE_ENDS
```

Synonym for LINE_END. Exists for compatibility with previous
versions. LINE_END is preferred.

**Since:** 1.2
**See Also:** LINE_END

,

Constant Field Values

- PAGE_START

```java
public static final
String
PAGE_START
```

The component comes before the first line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to NORTH.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

- PAGE_END

```java
public static final
String
PAGE_END
```

The component comes after the last line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to SOUTH.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

- LINE_START

```java
public static final
String
LINE_START
```

The component goes at the beginning of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to WEST.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

- LINE_END

```java
public static final
String
LINE_END
```

The component goes at the end of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to EAST.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BorderLayout

```java
public BorderLayout()
```

Constructs a new border layout with
no gaps between components.

- BorderLayout

```java
public BorderLayout​(int hgap,
int vgap)
```

Constructs a border layout with the specified gaps
between components.
The horizontal gap is specified by

hgap

and the vertical gap is specified by

vgap

.

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

Returns the horizontal gap between components.

**Returns:** the horizontal gap between components
**Since:** 1.1

- setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components.

**Parameters:** hgap

- the horizontal gap between components
**Since:** 1.1

- getVgap

```java
public int getVgap()
```

Returns the vertical gap between components.

**Returns:** the vertical gap between components
**Since:** 1.1

- setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components.

**Parameters:** vgap

- the vertical gap between components
**Since:** 1.1

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified
constraint object. For border layouts, the constraint must be
one of the following constants:

NORTH

,

SOUTH

,

EAST

,

WEST

, or

CENTER

.

Most applications do not call this method directly. This method
is called when a component is added to a container using the

Container.add

method with the same argument types.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added.
**Parameters:** constraints

- an object that specifies how and where
the component is added to the layout.
**Throws:** IllegalArgumentException

- if the constraint object is not
a string, or if it not one of the five specified constants.
**Since:** 1.1
**See Also:** Container.add(java.awt.Component, java.lang.Object)

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

Removes the specified component from this border layout. This
method is called when a container calls its

remove

or

removeAll

methods. Most applications do not call this
method directly.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to be removed.
**See Also:** Container.remove(java.awt.Component)

,

Container.removeAll()

- getLayoutComponent

```java
public
Component
getLayoutComponent​(
Object
constraints)
```

Gets the component that was added using the given constraint

**Parameters:** constraints

- the desired constraint, one of

CENTER

,

NORTH

,

SOUTH

,

WEST

,

EAST

,

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END
**Returns:** the component at the given location, or

null

if
the location is empty
**Throws:** IllegalArgumentException

- if the constraint object is
not one of the nine specified constants
**Since:** 1.5
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

- getLayoutComponent

```java
public
Component
getLayoutComponent​(
Container
target,

Object
constraints)
```

Returns the component that corresponds to the given constraint location
based on the target

Container

's component orientation.
Components added with the relative constraints

PAGE_START

,

PAGE_END

,

LINE_START

, and

LINE_END

take precedence over components added with the explicit constraints

NORTH

,

SOUTH

,

WEST

, and

EAST

.
The

Container

's component orientation is used to determine the location of components
added with

LINE_START

and

LINE_END

.

**Parameters:** constraints

- the desired absolute position, one of

CENTER

,

NORTH

,

SOUTH

,

EAST

,

WEST
**Parameters:** target

- the

Container

used to obtain
the constraint location based on the target

Container

's component orientation.
**Returns:** the component at the given location, or

null

if
the location is empty
**Throws:** IllegalArgumentException

- if the constraint object is
not one of the five specified constants
**Throws:** NullPointerException

- if the target parameter is null
**Since:** 1.5
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

- getConstraints

```java
public
Object
getConstraints​(
Component
comp)
```

Gets the constraints for the specified component

**Parameters:** comp

- the component to be queried
**Returns:** the constraint for the specified component,
or null if component is null or is not present
in this layout
**Since:** 1.5
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
target)
```

Determines the minimum size of the

target

container
using this layout manager.

This method is called when a container calls its

getMinimumSize

method. Most applications do not call
this method directly.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container in which to do the layout.
**Returns:** the minimum dimensions needed to lay out the subcomponents
of the specified container.
**See Also:** Container

,

preferredLayoutSize(java.awt.Container)

,

Container.getMinimumSize()

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
target)
```

Determines the preferred size of the

target

container using this layout manager, based on the components
in the container.

Most applications do not call this method directly. This method
is called when a container calls its

getPreferredSize

method.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container in which to do the layout.
**Returns:** the preferred dimensions to lay out the subcomponents
of the specified container.
**See Also:** Container

,

minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

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
target)
```

Lays out the container argument using this border layout.

This method actually reshapes the components in the specified
container in order to satisfy the constraints of this

BorderLayout

object. The

NORTH

and

SOUTH

components, if any, are placed at
the top and bottom of the container, respectively. The

WEST

and

EAST

components are
then placed on the left and right, respectively. Finally,
the

CENTER

object is placed in any remaining
space in the middle.

Most applications do not call this method directly. This method
is called when a container calls its

doLayout

method.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** target

- the container in which to do the layout.
**See Also:** Container

,

Container.doLayout()

- toString

```java
public
String
toString()
```

Returns a string representation of the state of this border layout.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this border layout.

Field Detail

- NORTH

```java
public static final
String
NORTH
```

The north layout constraint (top of container).

**See Also:** Constant Field Values

- SOUTH

```java
public static final
String
SOUTH
```

The south layout constraint (bottom of container).

**See Also:** Constant Field Values

- EAST

```java
public static final
String
EAST
```

The east layout constraint (right side of container).

**See Also:** Constant Field Values

- WEST

```java
public static final
String
WEST
```

The west layout constraint (left side of container).

**See Also:** Constant Field Values

- CENTER

```java
public static final
String
CENTER
```

The center layout constraint (middle of container).

**See Also:** Constant Field Values

- BEFORE_FIRST_LINE

```java
public static final
String
BEFORE_FIRST_LINE
```

Synonym for PAGE_START. Exists for compatibility with previous
versions. PAGE_START is preferred.

**Since:** 1.2
**See Also:** PAGE_START

,

Constant Field Values

- AFTER_LAST_LINE

```java
public static final
String
AFTER_LAST_LINE
```

Synonym for PAGE_END. Exists for compatibility with previous
versions. PAGE_END is preferred.

**Since:** 1.2
**See Also:** PAGE_END

,

Constant Field Values

- BEFORE_LINE_BEGINS

```java
public static final
String
BEFORE_LINE_BEGINS
```

Synonym for LINE_START. Exists for compatibility with previous
versions. LINE_START is preferred.

**Since:** 1.2
**See Also:** LINE_START

,

Constant Field Values

- AFTER_LINE_ENDS

```java
public static final
String
AFTER_LINE_ENDS
```

Synonym for LINE_END. Exists for compatibility with previous
versions. LINE_END is preferred.

**Since:** 1.2
**See Also:** LINE_END

,

Constant Field Values

- PAGE_START

```java
public static final
String
PAGE_START
```

The component comes before the first line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to NORTH.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

- PAGE_END

```java
public static final
String
PAGE_END
```

The component comes after the last line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to SOUTH.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

- LINE_START

```java
public static final
String
LINE_START
```

The component goes at the beginning of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to WEST.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

- LINE_END

```java
public static final
String
LINE_END
```

The component goes at the end of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to EAST.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

---

#### Field Detail

NORTH

```java
public static final
String
NORTH
```

The north layout constraint (top of container).

**See Also:** Constant Field Values

---

#### NORTH

public static final

String

NORTH

The north layout constraint (top of container).

SOUTH

```java
public static final
String
SOUTH
```

The south layout constraint (bottom of container).

**See Also:** Constant Field Values

---

#### SOUTH

public static final

String

SOUTH

The south layout constraint (bottom of container).

EAST

```java
public static final
String
EAST
```

The east layout constraint (right side of container).

**See Also:** Constant Field Values

---

#### EAST

public static final

String

EAST

The east layout constraint (right side of container).

WEST

```java
public static final
String
WEST
```

The west layout constraint (left side of container).

**See Also:** Constant Field Values

---

#### WEST

public static final

String

WEST

The west layout constraint (left side of container).

CENTER

```java
public static final
String
CENTER
```

The center layout constraint (middle of container).

**See Also:** Constant Field Values

---

#### CENTER

public static final

String

CENTER

The center layout constraint (middle of container).

BEFORE_FIRST_LINE

```java
public static final
String
BEFORE_FIRST_LINE
```

Synonym for PAGE_START. Exists for compatibility with previous
versions. PAGE_START is preferred.

**Since:** 1.2
**See Also:** PAGE_START

,

Constant Field Values

---

#### BEFORE_FIRST_LINE

public static final

String

BEFORE_FIRST_LINE

Synonym for PAGE_START. Exists for compatibility with previous
versions. PAGE_START is preferred.

AFTER_LAST_LINE

```java
public static final
String
AFTER_LAST_LINE
```

Synonym for PAGE_END. Exists for compatibility with previous
versions. PAGE_END is preferred.

**Since:** 1.2
**See Also:** PAGE_END

,

Constant Field Values

---

#### AFTER_LAST_LINE

public static final

String

AFTER_LAST_LINE

Synonym for PAGE_END. Exists for compatibility with previous
versions. PAGE_END is preferred.

BEFORE_LINE_BEGINS

```java
public static final
String
BEFORE_LINE_BEGINS
```

Synonym for LINE_START. Exists for compatibility with previous
versions. LINE_START is preferred.

**Since:** 1.2
**See Also:** LINE_START

,

Constant Field Values

---

#### BEFORE_LINE_BEGINS

public static final

String

BEFORE_LINE_BEGINS

Synonym for LINE_START. Exists for compatibility with previous
versions. LINE_START is preferred.

AFTER_LINE_ENDS

```java
public static final
String
AFTER_LINE_ENDS
```

Synonym for LINE_END. Exists for compatibility with previous
versions. LINE_END is preferred.

**Since:** 1.2
**See Also:** LINE_END

,

Constant Field Values

---

#### AFTER_LINE_ENDS

public static final

String

AFTER_LINE_ENDS

Synonym for LINE_END. Exists for compatibility with previous
versions. LINE_END is preferred.

PAGE_START

```java
public static final
String
PAGE_START
```

The component comes before the first line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to NORTH.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

---

#### PAGE_START

public static final

String

PAGE_START

The component comes before the first line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to NORTH.

PAGE_END

```java
public static final
String
PAGE_END
```

The component comes after the last line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to SOUTH.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

---

#### PAGE_END

public static final

String

PAGE_END

The component comes after the last line of the layout's content.
For Western, left-to-right and top-to-bottom orientations, this is
equivalent to SOUTH.

LINE_START

```java
public static final
String
LINE_START
```

The component goes at the beginning of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to WEST.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

---

#### LINE_START

public static final

String

LINE_START

The component goes at the beginning of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to WEST.

LINE_END

```java
public static final
String
LINE_END
```

The component goes at the end of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to EAST.

**Since:** 1.4
**See Also:** Component.getComponentOrientation()

,

Constant Field Values

---

#### LINE_END

public static final

String

LINE_END

The component goes at the end of the line direction for the
layout. For Western, left-to-right and top-to-bottom orientations,
this is equivalent to EAST.

Constructor Detail

- BorderLayout

```java
public BorderLayout()
```

Constructs a new border layout with
no gaps between components.

- BorderLayout

```java
public BorderLayout​(int hgap,
int vgap)
```

Constructs a border layout with the specified gaps
between components.
The horizontal gap is specified by

hgap

and the vertical gap is specified by

vgap

.

**Parameters:** hgap

- the horizontal gap.
**Parameters:** vgap

- the vertical gap.

---

#### Constructor Detail

BorderLayout

```java
public BorderLayout()
```

Constructs a new border layout with
no gaps between components.

---

#### BorderLayout

public BorderLayout()

Constructs a new border layout with
no gaps between components.

BorderLayout

```java
public BorderLayout​(int hgap,
int vgap)
```

Constructs a border layout with the specified gaps
between components.
The horizontal gap is specified by

hgap

and the vertical gap is specified by

vgap

.

**Parameters:** hgap

- the horizontal gap.
**Parameters:** vgap

- the vertical gap.

---

#### BorderLayout

public BorderLayout​(int hgap,
int vgap)

Constructs a border layout with the specified gaps
between components.
The horizontal gap is specified by

hgap

and the vertical gap is specified by

vgap

.

Method Detail

- getHgap

```java
public int getHgap()
```

Returns the horizontal gap between components.

**Returns:** the horizontal gap between components
**Since:** 1.1

- setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components.

**Parameters:** hgap

- the horizontal gap between components
**Since:** 1.1

- getVgap

```java
public int getVgap()
```

Returns the vertical gap between components.

**Returns:** the vertical gap between components
**Since:** 1.1

- setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components.

**Parameters:** vgap

- the vertical gap between components
**Since:** 1.1

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified
constraint object. For border layouts, the constraint must be
one of the following constants:

NORTH

,

SOUTH

,

EAST

,

WEST

, or

CENTER

.

Most applications do not call this method directly. This method
is called when a component is added to a container using the

Container.add

method with the same argument types.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added.
**Parameters:** constraints

- an object that specifies how and where
the component is added to the layout.
**Throws:** IllegalArgumentException

- if the constraint object is not
a string, or if it not one of the five specified constants.
**Since:** 1.1
**See Also:** Container.add(java.awt.Component, java.lang.Object)

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

Removes the specified component from this border layout. This
method is called when a container calls its

remove

or

removeAll

methods. Most applications do not call this
method directly.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to be removed.
**See Also:** Container.remove(java.awt.Component)

,

Container.removeAll()

- getLayoutComponent

```java
public
Component
getLayoutComponent​(
Object
constraints)
```

Gets the component that was added using the given constraint

**Parameters:** constraints

- the desired constraint, one of

CENTER

,

NORTH

,

SOUTH

,

WEST

,

EAST

,

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END
**Returns:** the component at the given location, or

null

if
the location is empty
**Throws:** IllegalArgumentException

- if the constraint object is
not one of the nine specified constants
**Since:** 1.5
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

- getLayoutComponent

```java
public
Component
getLayoutComponent​(
Container
target,

Object
constraints)
```

Returns the component that corresponds to the given constraint location
based on the target

Container

's component orientation.
Components added with the relative constraints

PAGE_START

,

PAGE_END

,

LINE_START

, and

LINE_END

take precedence over components added with the explicit constraints

NORTH

,

SOUTH

,

WEST

, and

EAST

.
The

Container

's component orientation is used to determine the location of components
added with

LINE_START

and

LINE_END

.

**Parameters:** constraints

- the desired absolute position, one of

CENTER

,

NORTH

,

SOUTH

,

EAST

,

WEST
**Parameters:** target

- the

Container

used to obtain
the constraint location based on the target

Container

's component orientation.
**Returns:** the component at the given location, or

null

if
the location is empty
**Throws:** IllegalArgumentException

- if the constraint object is
not one of the five specified constants
**Throws:** NullPointerException

- if the target parameter is null
**Since:** 1.5
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

- getConstraints

```java
public
Object
getConstraints​(
Component
comp)
```

Gets the constraints for the specified component

**Parameters:** comp

- the component to be queried
**Returns:** the constraint for the specified component,
or null if component is null or is not present
in this layout
**Since:** 1.5
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
target)
```

Determines the minimum size of the

target

container
using this layout manager.

This method is called when a container calls its

getMinimumSize

method. Most applications do not call
this method directly.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container in which to do the layout.
**Returns:** the minimum dimensions needed to lay out the subcomponents
of the specified container.
**See Also:** Container

,

preferredLayoutSize(java.awt.Container)

,

Container.getMinimumSize()

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
target)
```

Determines the preferred size of the

target

container using this layout manager, based on the components
in the container.

Most applications do not call this method directly. This method
is called when a container calls its

getPreferredSize

method.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container in which to do the layout.
**Returns:** the preferred dimensions to lay out the subcomponents
of the specified container.
**See Also:** Container

,

minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

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
target)
```

Lays out the container argument using this border layout.

This method actually reshapes the components in the specified
container in order to satisfy the constraints of this

BorderLayout

object. The

NORTH

and

SOUTH

components, if any, are placed at
the top and bottom of the container, respectively. The

WEST

and

EAST

components are
then placed on the left and right, respectively. Finally,
the

CENTER

object is placed in any remaining
space in the middle.

Most applications do not call this method directly. This method
is called when a container calls its

doLayout

method.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** target

- the container in which to do the layout.
**See Also:** Container

,

Container.doLayout()

- toString

```java
public
String
toString()
```

Returns a string representation of the state of this border layout.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this border layout.

---

#### Method Detail

getHgap

```java
public int getHgap()
```

Returns the horizontal gap between components.

**Returns:** the horizontal gap between components
**Since:** 1.1

---

#### getHgap

public int getHgap()

Returns the horizontal gap between components.

setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components.

**Parameters:** hgap

- the horizontal gap between components
**Since:** 1.1

---

#### setHgap

public void setHgap​(int hgap)

Sets the horizontal gap between components.

getVgap

```java
public int getVgap()
```

Returns the vertical gap between components.

**Returns:** the vertical gap between components
**Since:** 1.1

---

#### getVgap

public int getVgap()

Returns the vertical gap between components.

setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components.

**Parameters:** vgap

- the vertical gap between components
**Since:** 1.1

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

Adds the specified component to the layout, using the specified
constraint object. For border layouts, the constraint must be
one of the following constants:

NORTH

,

SOUTH

,

EAST

,

WEST

, or

CENTER

.

Most applications do not call this method directly. This method
is called when a component is added to a container using the

Container.add

method with the same argument types.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added.
**Parameters:** constraints

- an object that specifies how and where
the component is added to the layout.
**Throws:** IllegalArgumentException

- if the constraint object is not
a string, or if it not one of the five specified constants.
**Since:** 1.1
**See Also:** Container.add(java.awt.Component, java.lang.Object)

---

#### addLayoutComponent

public void addLayoutComponent​(

Component

comp,

Object

constraints)

Adds the specified component to the layout, using the specified
constraint object. For border layouts, the constraint must be
one of the following constants:

NORTH

,

SOUTH

,

EAST

,

WEST

, or

CENTER

.

Most applications do not call this method directly. This method
is called when a component is added to a container using the

Container.add

method with the same argument types.

Most applications do not call this method directly. This method
is called when a component is added to a container using the

Container.add

method with the same argument types.

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

Removes the specified component from this border layout. This
method is called when a container calls its

remove

or

removeAll

methods. Most applications do not call this
method directly.

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

Removes the specified component from this border layout. This
method is called when a container calls its

remove

or

removeAll

methods. Most applications do not call this
method directly.

getLayoutComponent

```java
public
Component
getLayoutComponent​(
Object
constraints)
```

Gets the component that was added using the given constraint

**Parameters:** constraints

- the desired constraint, one of

CENTER

,

NORTH

,

SOUTH

,

WEST

,

EAST

,

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END
**Returns:** the component at the given location, or

null

if
the location is empty
**Throws:** IllegalArgumentException

- if the constraint object is
not one of the nine specified constants
**Since:** 1.5
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

---

#### getLayoutComponent

public

Component

getLayoutComponent​(

Object

constraints)

Gets the component that was added using the given constraint

getLayoutComponent

```java
public
Component
getLayoutComponent​(
Container
target,

Object
constraints)
```

Returns the component that corresponds to the given constraint location
based on the target

Container

's component orientation.
Components added with the relative constraints

PAGE_START

,

PAGE_END

,

LINE_START

, and

LINE_END

take precedence over components added with the explicit constraints

NORTH

,

SOUTH

,

WEST

, and

EAST

.
The

Container

's component orientation is used to determine the location of components
added with

LINE_START

and

LINE_END

.

**Parameters:** constraints

- the desired absolute position, one of

CENTER

,

NORTH

,

SOUTH

,

EAST

,

WEST
**Parameters:** target

- the

Container

used to obtain
the constraint location based on the target

Container

's component orientation.
**Returns:** the component at the given location, or

null

if
the location is empty
**Throws:** IllegalArgumentException

- if the constraint object is
not one of the five specified constants
**Throws:** NullPointerException

- if the target parameter is null
**Since:** 1.5
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

---

#### getLayoutComponent

public

Component

getLayoutComponent​(

Container

target,

Object

constraints)

Returns the component that corresponds to the given constraint location
based on the target

Container

's component orientation.
Components added with the relative constraints

PAGE_START

,

PAGE_END

,

LINE_START

, and

LINE_END

take precedence over components added with the explicit constraints

NORTH

,

SOUTH

,

WEST

, and

EAST

.
The

Container

's component orientation is used to determine the location of components
added with

LINE_START

and

LINE_END

.

getConstraints

```java
public
Object
getConstraints​(
Component
comp)
```

Gets the constraints for the specified component

**Parameters:** comp

- the component to be queried
**Returns:** the constraint for the specified component,
or null if component is null or is not present
in this layout
**Since:** 1.5
**See Also:** addLayoutComponent(java.awt.Component, java.lang.Object)

---

#### getConstraints

public

Object

getConstraints​(

Component

comp)

Gets the constraints for the specified component

minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
target)
```

Determines the minimum size of the

target

container
using this layout manager.

This method is called when a container calls its

getMinimumSize

method. Most applications do not call
this method directly.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container in which to do the layout.
**Returns:** the minimum dimensions needed to lay out the subcomponents
of the specified container.
**See Also:** Container

,

preferredLayoutSize(java.awt.Container)

,

Container.getMinimumSize()

---

#### minimumLayoutSize

public

Dimension

minimumLayoutSize​(

Container

target)

Determines the minimum size of the

target

container
using this layout manager.

This method is called when a container calls its

getMinimumSize

method. Most applications do not call
this method directly.

This method is called when a container calls its

getMinimumSize

method. Most applications do not call
this method directly.

preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
target)
```

Determines the preferred size of the

target

container using this layout manager, based on the components
in the container.

Most applications do not call this method directly. This method
is called when a container calls its

getPreferredSize

method.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container in which to do the layout.
**Returns:** the preferred dimensions to lay out the subcomponents
of the specified container.
**See Also:** Container

,

minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

---

#### preferredLayoutSize

public

Dimension

preferredLayoutSize​(

Container

target)

Determines the preferred size of the

target

container using this layout manager, based on the components
in the container.

Most applications do not call this method directly. This method
is called when a container calls its

getPreferredSize

method.

Most applications do not call this method directly. This method
is called when a container calls its

getPreferredSize

method.

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
target)
```

Lays out the container argument using this border layout.

This method actually reshapes the components in the specified
container in order to satisfy the constraints of this

BorderLayout

object. The

NORTH

and

SOUTH

components, if any, are placed at
the top and bottom of the container, respectively. The

WEST

and

EAST

components are
then placed on the left and right, respectively. Finally,
the

CENTER

object is placed in any remaining
space in the middle.

Most applications do not call this method directly. This method
is called when a container calls its

doLayout

method.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** target

- the container in which to do the layout.
**See Also:** Container

,

Container.doLayout()

---

#### layoutContainer

public void layoutContainer​(

Container

target)

Lays out the container argument using this border layout.

This method actually reshapes the components in the specified
container in order to satisfy the constraints of this

BorderLayout

object. The

NORTH

and

SOUTH

components, if any, are placed at
the top and bottom of the container, respectively. The

WEST

and

EAST

components are
then placed on the left and right, respectively. Finally,
the

CENTER

object is placed in any remaining
space in the middle.

Most applications do not call this method directly. This method
is called when a container calls its

doLayout

method.

This method actually reshapes the components in the specified
container in order to satisfy the constraints of this

BorderLayout

object. The

NORTH

and

SOUTH

components, if any, are placed at
the top and bottom of the container, respectively. The

WEST

and

EAST

components are
then placed on the left and right, respectively. Finally,
the

CENTER

object is placed in any remaining
space in the middle.

Most applications do not call this method directly. This method
is called when a container calls its

doLayout

method.

Most applications do not call this method directly. This method
is called when a container calls its

doLayout

method.

toString

```java
public
String
toString()
```

Returns a string representation of the state of this border layout.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this border layout.

---

#### toString

public

String

toString()

Returns a string representation of the state of this border layout.

---

