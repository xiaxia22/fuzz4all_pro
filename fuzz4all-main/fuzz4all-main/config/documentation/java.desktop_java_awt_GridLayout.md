# Class GridLayout

**Source:** `java.desktop\java\awt\GridLayout.html`

### Class Description

```java
public class
GridLayout

extends
Object

implements
LayoutManager
,
Serializable
```

The

GridLayout

class is a layout manager that
lays out a container's components in a rectangular grid.
The container is divided into equal-sized rectangles,
and one component is placed in each rectangle.
For example, the following is an applet that lays out six buttons
into three rows and two columns:

```java
import java.awt.*;
import java.applet.Applet;
public class ButtonGrid extends Applet {
public void init() {
setLayout(new GridLayout(3,2));
add(new Button("1"));
add(new Button("2"));
add(new Button("3"));
add(new Button("4"));
add(new Button("5"));
add(new Button("6"));
}
}
```

If the container's

ComponentOrientation

property is horizontal
and left-to-right, the above example produces the output shown in Figure 1.
If the container's

ComponentOrientation

property is horizontal
and right-to-left, the example produces the output shown in Figure 2.

Figures

Figure 1: Horizontal, Left-to-Right

Figure 2: Horizontal, Right-to-Left

When both the number of rows and the number of columns have
been set to non-zero values, either by a constructor or
by the

setRows

and

setColumns

methods, the number of
columns specified is ignored. Instead, the number of
columns is determined from the specified number of rows
and the total number of components in the layout. So, for
example, if three rows and two columns have been specified
and nine components are added to the layout, they will
be displayed as three rows of three columns. Specifying
the number of columns affects the layout only when the
number of rows is set to zero.

**All Implemented Interfaces:** LayoutManager

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public GridLayout()

Creates a grid layout with a default of one column per component,
in a single row.

**Since:**
- 1.1

---

#### public GridLayout​(int rows,
int cols)

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

**Parameters:**
- rows

- the rows, with the value zero meaning
any number of rows.
- cols

- the columns, with the value zero meaning
any number of columns.

---

#### public GridLayout​(int rows,
int cols,
int hgap,
int vgap)

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

In addition, the horizontal and vertical gaps are set to the
specified values. Horizontal gaps are placed between each
of the columns. Vertical gaps are placed between each of
the rows.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

All

GridLayout

constructors defer to this one.

**Parameters:**
- rows

- the rows, with the value zero meaning
any number of rows
- cols

- the columns, with the value zero meaning
any number of columns
- hgap

- the horizontal gap
- vgap

- the vertical gap

**Throws:**
- IllegalArgumentException

- if the value of both

rows

and

cols

is
set to zero

---

### Method Details

#### public int getRows()

Gets the number of rows in this layout.

**Returns:**
- the number of rows in this layout

**Since:**
- 1.1

---

#### public void setRows​(int rows)

Sets the number of rows in this layout to the specified value.

**Parameters:**
- rows

- the number of rows in this layout

**Throws:**
- IllegalArgumentException

- if the value of both

rows

and

cols

is set to zero

**Since:**
- 1.1

---

#### public int getColumns()

Gets the number of columns in this layout.

**Returns:**
- the number of columns in this layout

**Since:**
- 1.1

---

#### public void setColumns​(int cols)

Sets the number of columns in this layout to the specified value.
Setting the number of columns has no affect on the layout
if the number of rows specified by a constructor or by
the

setRows

method is non-zero. In that case, the number
of columns displayed in the layout is determined by the total
number of components and the number of rows specified.

**Parameters:**
- cols

- the number of columns in this layout

**Throws:**
- IllegalArgumentException

- if the value of both

rows

and

cols

is set to zero

**Since:**
- 1.1

---

#### public int getHgap()

Gets the horizontal gap between components.

**Returns:**
- the horizontal gap between components

**Since:**
- 1.1

---

#### public void setHgap​(int hgap)

Sets the horizontal gap between components to the specified value.

**Parameters:**
- hgap

- the horizontal gap between components

**Since:**
- 1.1

---

#### public int getVgap()

Gets the vertical gap between components.

**Returns:**
- the vertical gap between components

**Since:**
- 1.1

---

#### public void setVgap​(int vgap)

Sets the vertical gap between components to the specified value.

**Parameters:**
- vgap

- the vertical gap between components

**Since:**
- 1.1

---

#### public void addLayoutComponent​(
String
name,

Component
comp)

Adds the specified component with the specified name to the layout.

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

Removes the specified component from the layout.

**Specified by:**
- removeLayoutComponent

in interface

LayoutManager

**Parameters:**
- comp

- the component to be removed

---

#### public
Dimension
preferredLayoutSize​(
Container
parent)

Determines the preferred size of the container argument using
this grid layout.

The preferred width of a grid layout is the largest preferred
width of all of the components in the container times the number of
columns, plus the horizontal padding times the number of columns
minus one, plus the left and right insets of the target container.

The preferred height of a grid layout is the largest preferred
height of all of the components in the container times the number of
rows, plus the vertical padding times the number of rows minus one,
plus the top and bottom insets of the target container.

**Specified by:**
- preferredLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the container in which to do the layout

**Returns:**
- the preferred dimensions to lay out the
subcomponents of the specified container

**See Also:**
- minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

---

#### public
Dimension
minimumLayoutSize​(
Container
parent)

Determines the minimum size of the container argument using this
grid layout.

The minimum width of a grid layout is the largest minimum width
of all of the components in the container times the number of columns,
plus the horizontal padding times the number of columns minus one,
plus the left and right insets of the target container.

The minimum height of a grid layout is the largest minimum height
of all of the components in the container times the number of rows,
plus the vertical padding times the number of rows minus one, plus
the top and bottom insets of the target container.

**Specified by:**
- minimumLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the container in which to do the layout

**Returns:**
- the minimum dimensions needed to lay out the
subcomponents of the specified container

**See Also:**
- preferredLayoutSize(java.awt.Container)

,

Container.doLayout()

---

#### public void layoutContainer​(
Container
parent)

Lays out the specified container using this layout.

This method reshapes the components in the specified target
container in order to satisfy the constraints of the

GridLayout

object.

The grid layout manager determines the size of individual
components by dividing the free space in the container into
equal-sized portions according to the number of rows and columns
in the layout. The container's free space equals the container's
size minus any insets and any specified horizontal or vertical
gap. All components in a grid layout are given the same size.

**Specified by:**
- layoutContainer

in interface

LayoutManager

**Parameters:**
- parent

- the container in which to do the layout

**See Also:**
- Container

,

Container.doLayout()

---

#### public
String
toString()

Returns the string representation of this grid layout's values.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this grid layout

---

### Additional Sections

#### Class GridLayout

java.lang.Object

- java.awt.GridLayout

java.awt.GridLayout

**All Implemented Interfaces:** LayoutManager

,

Serializable

```java
public class
GridLayout

extends
Object

implements
LayoutManager
,
Serializable
```

The

GridLayout

class is a layout manager that
lays out a container's components in a rectangular grid.
The container is divided into equal-sized rectangles,
and one component is placed in each rectangle.
For example, the following is an applet that lays out six buttons
into three rows and two columns:

```java
import java.awt.*;
import java.applet.Applet;
public class ButtonGrid extends Applet {
public void init() {
setLayout(new GridLayout(3,2));
add(new Button("1"));
add(new Button("2"));
add(new Button("3"));
add(new Button("4"));
add(new Button("5"));
add(new Button("6"));
}
}
```

If the container's

ComponentOrientation

property is horizontal
and left-to-right, the above example produces the output shown in Figure 1.
If the container's

ComponentOrientation

property is horizontal
and right-to-left, the example produces the output shown in Figure 2.

Figures

Figure 1: Horizontal, Left-to-Right

Figure 2: Horizontal, Right-to-Left

When both the number of rows and the number of columns have
been set to non-zero values, either by a constructor or
by the

setRows

and

setColumns

methods, the number of
columns specified is ignored. Instead, the number of
columns is determined from the specified number of rows
and the total number of components in the layout. So, for
example, if three rows and two columns have been specified
and nine components are added to the layout, they will
be displayed as three rows of three columns. Specifying
the number of columns affects the layout only when the
number of rows is set to zero.

**Since:** 1.0
**See Also:** Serialized Form

public class

GridLayout

extends

Object

implements

LayoutManager

,

Serializable

The

GridLayout

class is a layout manager that
lays out a container's components in a rectangular grid.
The container is divided into equal-sized rectangles,
and one component is placed in each rectangle.
For example, the following is an applet that lays out six buttons
into three rows and two columns:

```java
import java.awt.*;
import java.applet.Applet;
public class ButtonGrid extends Applet {
public void init() {
setLayout(new GridLayout(3,2));
add(new Button("1"));
add(new Button("2"));
add(new Button("3"));
add(new Button("4"));
add(new Button("5"));
add(new Button("6"));
}
}
```

If the container's

ComponentOrientation

property is horizontal
and left-to-right, the above example produces the output shown in Figure 1.
If the container's

ComponentOrientation

property is horizontal
and right-to-left, the example produces the output shown in Figure 2.

Figures

Figure 1: Horizontal, Left-to-Right

Figure 2: Horizontal, Right-to-Left

When both the number of rows and the number of columns have
been set to non-zero values, either by a constructor or
by the

setRows

and

setColumns

methods, the number of
columns specified is ignored. Instead, the number of
columns is determined from the specified number of rows
and the total number of components in the layout. So, for
example, if three rows and two columns have been specified
and nine components are added to the layout, they will
be displayed as three rows of three columns. Specifying
the number of columns affects the layout only when the
number of rows is set to zero.

import java.awt.*;
import java.applet.Applet;
public class ButtonGrid extends Applet {
public void init() {
setLayout(new GridLayout(3,2));
add(new Button("1"));
add(new Button("2"));
add(new Button("3"));
add(new Button("4"));
add(new Button("5"));
add(new Button("6"));
}
}

If the container's

ComponentOrientation

property is horizontal
and left-to-right, the above example produces the output shown in Figure 1.
If the container's

ComponentOrientation

property is horizontal
and right-to-left, the example produces the output shown in Figure 2.

Figures

Figure 1: Horizontal, Left-to-Right

Figure 2: Horizontal, Right-to-Left

When both the number of rows and the number of columns have
been set to non-zero values, either by a constructor or
by the

setRows

and

setColumns

methods, the number of
columns specified is ignored. Instead, the number of
columns is determined from the specified number of rows
and the total number of components in the layout. So, for
example, if three rows and two columns have been specified
and nine components are added to the layout, they will
be displayed as three rows of three columns. Specifying
the number of columns affects the layout only when the
number of rows is set to zero.

When both the number of rows and the number of columns have
been set to non-zero values, either by a constructor or
by the

setRows

and

setColumns

methods, the number of
columns specified is ignored. Instead, the number of
columns is determined from the specified number of rows
and the total number of components in the layout. So, for
example, if three rows and two columns have been specified
and nine components are added to the layout, they will
be displayed as three rows of three columns. Specifying
the number of columns affects the layout only when the
number of rows is set to zero.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GridLayout

()

Creates a grid layout with a default of one column per component,
in a single row.

GridLayout

​(int rows,
int cols)

Creates a grid layout with the specified number of rows and
columns.

GridLayout

​(int rows,
int cols,
int hgap,
int vgap)

Creates a grid layout with the specified number of rows and
columns.

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

String

name,

Component

comp)

Adds the specified component with the specified name to the layout.

int

getColumns

()

Gets the number of columns in this layout.

int

getHgap

()

Gets the horizontal gap between components.

int

getRows

()

Gets the number of rows in this layout.

int

getVgap

()

Gets the vertical gap between components.

void

layoutContainer

​(

Container

parent)

Lays out the specified container using this layout.

Dimension

minimumLayoutSize

​(

Container

parent)

Determines the minimum size of the container argument using this
grid layout.

Dimension

preferredLayoutSize

​(

Container

parent)

Determines the preferred size of the container argument using
this grid layout.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

void

setColumns

​(int cols)

Sets the number of columns in this layout to the specified value.

void

setHgap

​(int hgap)

Sets the horizontal gap between components to the specified value.

void

setRows

​(int rows)

Sets the number of rows in this layout to the specified value.

void

setVgap

​(int vgap)

Sets the vertical gap between components to the specified value.

String

toString

()

Returns the string representation of this grid layout's values.

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

GridLayout

()

Creates a grid layout with a default of one column per component,
in a single row.

GridLayout

​(int rows,
int cols)

Creates a grid layout with the specified number of rows and
columns.

GridLayout

​(int rows,
int cols,
int hgap,
int vgap)

Creates a grid layout with the specified number of rows and
columns.

---

#### Constructor Summary

Creates a grid layout with a default of one column per component,
in a single row.

Creates a grid layout with the specified number of rows and
columns.

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

String

name,

Component

comp)

Adds the specified component with the specified name to the layout.

int

getColumns

()

Gets the number of columns in this layout.

int

getHgap

()

Gets the horizontal gap between components.

int

getRows

()

Gets the number of rows in this layout.

int

getVgap

()

Gets the vertical gap between components.

void

layoutContainer

​(

Container

parent)

Lays out the specified container using this layout.

Dimension

minimumLayoutSize

​(

Container

parent)

Determines the minimum size of the container argument using this
grid layout.

Dimension

preferredLayoutSize

​(

Container

parent)

Determines the preferred size of the container argument using
this grid layout.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

void

setColumns

​(int cols)

Sets the number of columns in this layout to the specified value.

void

setHgap

​(int hgap)

Sets the horizontal gap between components to the specified value.

void

setRows

​(int rows)

Sets the number of rows in this layout to the specified value.

void

setVgap

​(int vgap)

Sets the vertical gap between components to the specified value.

String

toString

()

Returns the string representation of this grid layout's values.

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

Adds the specified component with the specified name to the layout.

Gets the number of columns in this layout.

Gets the horizontal gap between components.

Gets the number of rows in this layout.

Gets the vertical gap between components.

Lays out the specified container using this layout.

Determines the minimum size of the container argument using this
grid layout.

Determines the preferred size of the container argument using
this grid layout.

Removes the specified component from the layout.

Sets the number of columns in this layout to the specified value.

Sets the horizontal gap between components to the specified value.

Sets the number of rows in this layout to the specified value.

Sets the vertical gap between components to the specified value.

Returns the string representation of this grid layout's values.

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

- GridLayout

```java
public GridLayout()
```

Creates a grid layout with a default of one column per component,
in a single row.

**Since:** 1.1

- GridLayout

```java
public GridLayout​(int rows,
int cols)
```

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

**Parameters:** rows

- the rows, with the value zero meaning
any number of rows.
**Parameters:** cols

- the columns, with the value zero meaning
any number of columns.

- GridLayout

```java
public GridLayout​(int rows,
int cols,
int hgap,
int vgap)
```

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

In addition, the horizontal and vertical gaps are set to the
specified values. Horizontal gaps are placed between each
of the columns. Vertical gaps are placed between each of
the rows.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

All

GridLayout

constructors defer to this one.

**Parameters:** rows

- the rows, with the value zero meaning
any number of rows
**Parameters:** cols

- the columns, with the value zero meaning
any number of columns
**Parameters:** hgap

- the horizontal gap
**Parameters:** vgap

- the vertical gap
**Throws:** IllegalArgumentException

- if the value of both

rows

and

cols

is
set to zero

============ METHOD DETAIL ==========

- Method Detail

- getRows

```java
public int getRows()
```

Gets the number of rows in this layout.

**Returns:** the number of rows in this layout
**Since:** 1.1

- setRows

```java
public void setRows​(int rows)
```

Sets the number of rows in this layout to the specified value.

**Parameters:** rows

- the number of rows in this layout
**Throws:** IllegalArgumentException

- if the value of both

rows

and

cols

is set to zero
**Since:** 1.1

- getColumns

```java
public int getColumns()
```

Gets the number of columns in this layout.

**Returns:** the number of columns in this layout
**Since:** 1.1

- setColumns

```java
public void setColumns​(int cols)
```

Sets the number of columns in this layout to the specified value.
Setting the number of columns has no affect on the layout
if the number of rows specified by a constructor or by
the

setRows

method is non-zero. In that case, the number
of columns displayed in the layout is determined by the total
number of components and the number of rows specified.

**Parameters:** cols

- the number of columns in this layout
**Throws:** IllegalArgumentException

- if the value of both

rows

and

cols

is set to zero
**Since:** 1.1

- getHgap

```java
public int getHgap()
```

Gets the horizontal gap between components.

**Returns:** the horizontal gap between components
**Since:** 1.1

- setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components to the specified value.

**Parameters:** hgap

- the horizontal gap between components
**Since:** 1.1

- getVgap

```java
public int getVgap()
```

Gets the vertical gap between components.

**Returns:** the vertical gap between components
**Since:** 1.1

- setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components to the specified value.

**Parameters:** vgap

- the vertical gap between components
**Since:** 1.1

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Adds the specified component with the specified name to the layout.

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

Removes the specified component from the layout.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to be removed

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Determines the preferred size of the container argument using
this grid layout.

The preferred width of a grid layout is the largest preferred
width of all of the components in the container times the number of
columns, plus the horizontal padding times the number of columns
minus one, plus the left and right insets of the target container.

The preferred height of a grid layout is the largest preferred
height of all of the components in the container times the number of
rows, plus the vertical padding times the number of rows minus one,
plus the top and bottom insets of the target container.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the preferred dimensions to lay out the
subcomponents of the specified container
**See Also:** minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Determines the minimum size of the container argument using this
grid layout.

The minimum width of a grid layout is the largest minimum width
of all of the components in the container times the number of columns,
plus the horizontal padding times the number of columns minus one,
plus the left and right insets of the target container.

The minimum height of a grid layout is the largest minimum height
of all of the components in the container times the number of rows,
plus the vertical padding times the number of rows minus one, plus
the top and bottom insets of the target container.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the minimum dimensions needed to lay out the
subcomponents of the specified container
**See Also:** preferredLayoutSize(java.awt.Container)

,

Container.doLayout()

- layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Lays out the specified container using this layout.

This method reshapes the components in the specified target
container in order to satisfy the constraints of the

GridLayout

object.

The grid layout manager determines the size of individual
components by dividing the free space in the container into
equal-sized portions according to the number of rows and columns
in the layout. The container's free space equals the container's
size minus any insets and any specified horizontal or vertical
gap. All components in a grid layout are given the same size.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**See Also:** Container

,

Container.doLayout()

- toString

```java
public
String
toString()
```

Returns the string representation of this grid layout's values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this grid layout

Constructor Detail

- GridLayout

```java
public GridLayout()
```

Creates a grid layout with a default of one column per component,
in a single row.

**Since:** 1.1

- GridLayout

```java
public GridLayout​(int rows,
int cols)
```

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

**Parameters:** rows

- the rows, with the value zero meaning
any number of rows.
**Parameters:** cols

- the columns, with the value zero meaning
any number of columns.

- GridLayout

```java
public GridLayout​(int rows,
int cols,
int hgap,
int vgap)
```

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

In addition, the horizontal and vertical gaps are set to the
specified values. Horizontal gaps are placed between each
of the columns. Vertical gaps are placed between each of
the rows.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

All

GridLayout

constructors defer to this one.

**Parameters:** rows

- the rows, with the value zero meaning
any number of rows
**Parameters:** cols

- the columns, with the value zero meaning
any number of columns
**Parameters:** hgap

- the horizontal gap
**Parameters:** vgap

- the vertical gap
**Throws:** IllegalArgumentException

- if the value of both

rows

and

cols

is
set to zero

---

#### Constructor Detail

GridLayout

```java
public GridLayout()
```

Creates a grid layout with a default of one column per component,
in a single row.

**Since:** 1.1

---

#### GridLayout

public GridLayout()

Creates a grid layout with a default of one column per component,
in a single row.

GridLayout

```java
public GridLayout​(int rows,
int cols)
```

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

**Parameters:** rows

- the rows, with the value zero meaning
any number of rows.
**Parameters:** cols

- the columns, with the value zero meaning
any number of columns.

---

#### GridLayout

public GridLayout​(int rows,
int cols)

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

GridLayout

```java
public GridLayout​(int rows,
int cols,
int hgap,
int vgap)
```

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

In addition, the horizontal and vertical gaps are set to the
specified values. Horizontal gaps are placed between each
of the columns. Vertical gaps are placed between each of
the rows.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

All

GridLayout

constructors defer to this one.

**Parameters:** rows

- the rows, with the value zero meaning
any number of rows
**Parameters:** cols

- the columns, with the value zero meaning
any number of columns
**Parameters:** hgap

- the horizontal gap
**Parameters:** vgap

- the vertical gap
**Throws:** IllegalArgumentException

- if the value of both

rows

and

cols

is
set to zero

---

#### GridLayout

public GridLayout​(int rows,
int cols,
int hgap,
int vgap)

Creates a grid layout with the specified number of rows and
columns. All components in the layout are given equal size.

In addition, the horizontal and vertical gaps are set to the
specified values. Horizontal gaps are placed between each
of the columns. Vertical gaps are placed between each of
the rows.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

All

GridLayout

constructors defer to this one.

In addition, the horizontal and vertical gaps are set to the
specified values. Horizontal gaps are placed between each
of the columns. Vertical gaps are placed between each of
the rows.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

All

GridLayout

constructors defer to this one.

One, but not both, of

rows

and

cols

can
be zero, which means that any number of objects can be placed in a
row or in a column.

All

GridLayout

constructors defer to this one.

All

GridLayout

constructors defer to this one.

Method Detail

- getRows

```java
public int getRows()
```

Gets the number of rows in this layout.

**Returns:** the number of rows in this layout
**Since:** 1.1

- setRows

```java
public void setRows​(int rows)
```

Sets the number of rows in this layout to the specified value.

**Parameters:** rows

- the number of rows in this layout
**Throws:** IllegalArgumentException

- if the value of both

rows

and

cols

is set to zero
**Since:** 1.1

- getColumns

```java
public int getColumns()
```

Gets the number of columns in this layout.

**Returns:** the number of columns in this layout
**Since:** 1.1

- setColumns

```java
public void setColumns​(int cols)
```

Sets the number of columns in this layout to the specified value.
Setting the number of columns has no affect on the layout
if the number of rows specified by a constructor or by
the

setRows

method is non-zero. In that case, the number
of columns displayed in the layout is determined by the total
number of components and the number of rows specified.

**Parameters:** cols

- the number of columns in this layout
**Throws:** IllegalArgumentException

- if the value of both

rows

and

cols

is set to zero
**Since:** 1.1

- getHgap

```java
public int getHgap()
```

Gets the horizontal gap between components.

**Returns:** the horizontal gap between components
**Since:** 1.1

- setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components to the specified value.

**Parameters:** hgap

- the horizontal gap between components
**Since:** 1.1

- getVgap

```java
public int getVgap()
```

Gets the vertical gap between components.

**Returns:** the vertical gap between components
**Since:** 1.1

- setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components to the specified value.

**Parameters:** vgap

- the vertical gap between components
**Since:** 1.1

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Adds the specified component with the specified name to the layout.

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

Removes the specified component from the layout.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to be removed

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Determines the preferred size of the container argument using
this grid layout.

The preferred width of a grid layout is the largest preferred
width of all of the components in the container times the number of
columns, plus the horizontal padding times the number of columns
minus one, plus the left and right insets of the target container.

The preferred height of a grid layout is the largest preferred
height of all of the components in the container times the number of
rows, plus the vertical padding times the number of rows minus one,
plus the top and bottom insets of the target container.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the preferred dimensions to lay out the
subcomponents of the specified container
**See Also:** minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Determines the minimum size of the container argument using this
grid layout.

The minimum width of a grid layout is the largest minimum width
of all of the components in the container times the number of columns,
plus the horizontal padding times the number of columns minus one,
plus the left and right insets of the target container.

The minimum height of a grid layout is the largest minimum height
of all of the components in the container times the number of rows,
plus the vertical padding times the number of rows minus one, plus
the top and bottom insets of the target container.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the minimum dimensions needed to lay out the
subcomponents of the specified container
**See Also:** preferredLayoutSize(java.awt.Container)

,

Container.doLayout()

- layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Lays out the specified container using this layout.

This method reshapes the components in the specified target
container in order to satisfy the constraints of the

GridLayout

object.

The grid layout manager determines the size of individual
components by dividing the free space in the container into
equal-sized portions according to the number of rows and columns
in the layout. The container's free space equals the container's
size minus any insets and any specified horizontal or vertical
gap. All components in a grid layout are given the same size.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**See Also:** Container

,

Container.doLayout()

- toString

```java
public
String
toString()
```

Returns the string representation of this grid layout's values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this grid layout

---

#### Method Detail

getRows

```java
public int getRows()
```

Gets the number of rows in this layout.

**Returns:** the number of rows in this layout
**Since:** 1.1

---

#### getRows

public int getRows()

Gets the number of rows in this layout.

setRows

```java
public void setRows​(int rows)
```

Sets the number of rows in this layout to the specified value.

**Parameters:** rows

- the number of rows in this layout
**Throws:** IllegalArgumentException

- if the value of both

rows

and

cols

is set to zero
**Since:** 1.1

---

#### setRows

public void setRows​(int rows)

Sets the number of rows in this layout to the specified value.

getColumns

```java
public int getColumns()
```

Gets the number of columns in this layout.

**Returns:** the number of columns in this layout
**Since:** 1.1

---

#### getColumns

public int getColumns()

Gets the number of columns in this layout.

setColumns

```java
public void setColumns​(int cols)
```

Sets the number of columns in this layout to the specified value.
Setting the number of columns has no affect on the layout
if the number of rows specified by a constructor or by
the

setRows

method is non-zero. In that case, the number
of columns displayed in the layout is determined by the total
number of components and the number of rows specified.

**Parameters:** cols

- the number of columns in this layout
**Throws:** IllegalArgumentException

- if the value of both

rows

and

cols

is set to zero
**Since:** 1.1

---

#### setColumns

public void setColumns​(int cols)

Sets the number of columns in this layout to the specified value.
Setting the number of columns has no affect on the layout
if the number of rows specified by a constructor or by
the

setRows

method is non-zero. In that case, the number
of columns displayed in the layout is determined by the total
number of components and the number of rows specified.

getHgap

```java
public int getHgap()
```

Gets the horizontal gap between components.

**Returns:** the horizontal gap between components
**Since:** 1.1

---

#### getHgap

public int getHgap()

Gets the horizontal gap between components.

setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components to the specified value.

**Parameters:** hgap

- the horizontal gap between components
**Since:** 1.1

---

#### setHgap

public void setHgap​(int hgap)

Sets the horizontal gap between components to the specified value.

getVgap

```java
public int getVgap()
```

Gets the vertical gap between components.

**Returns:** the vertical gap between components
**Since:** 1.1

---

#### getVgap

public int getVgap()

Gets the vertical gap between components.

setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components to the specified value.

**Parameters:** vgap

- the vertical gap between components
**Since:** 1.1

---

#### setVgap

public void setVgap​(int vgap)

Sets the vertical gap between components to the specified value.

addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Adds the specified component with the specified name to the layout.

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

Adds the specified component with the specified name to the layout.

removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to be removed

---

#### removeLayoutComponent

public void removeLayoutComponent​(

Component

comp)

Removes the specified component from the layout.

preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Determines the preferred size of the container argument using
this grid layout.

The preferred width of a grid layout is the largest preferred
width of all of the components in the container times the number of
columns, plus the horizontal padding times the number of columns
minus one, plus the left and right insets of the target container.

The preferred height of a grid layout is the largest preferred
height of all of the components in the container times the number of
rows, plus the vertical padding times the number of rows minus one,
plus the top and bottom insets of the target container.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the preferred dimensions to lay out the
subcomponents of the specified container
**See Also:** minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

---

#### preferredLayoutSize

public

Dimension

preferredLayoutSize​(

Container

parent)

Determines the preferred size of the container argument using
this grid layout.

The preferred width of a grid layout is the largest preferred
width of all of the components in the container times the number of
columns, plus the horizontal padding times the number of columns
minus one, plus the left and right insets of the target container.

The preferred height of a grid layout is the largest preferred
height of all of the components in the container times the number of
rows, plus the vertical padding times the number of rows minus one,
plus the top and bottom insets of the target container.

The preferred width of a grid layout is the largest preferred
width of all of the components in the container times the number of
columns, plus the horizontal padding times the number of columns
minus one, plus the left and right insets of the target container.

The preferred height of a grid layout is the largest preferred
height of all of the components in the container times the number of
rows, plus the vertical padding times the number of rows minus one,
plus the top and bottom insets of the target container.

The preferred height of a grid layout is the largest preferred
height of all of the components in the container times the number of
rows, plus the vertical padding times the number of rows minus one,
plus the top and bottom insets of the target container.

minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Determines the minimum size of the container argument using this
grid layout.

The minimum width of a grid layout is the largest minimum width
of all of the components in the container times the number of columns,
plus the horizontal padding times the number of columns minus one,
plus the left and right insets of the target container.

The minimum height of a grid layout is the largest minimum height
of all of the components in the container times the number of rows,
plus the vertical padding times the number of rows minus one, plus
the top and bottom insets of the target container.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the minimum dimensions needed to lay out the
subcomponents of the specified container
**See Also:** preferredLayoutSize(java.awt.Container)

,

Container.doLayout()

---

#### minimumLayoutSize

public

Dimension

minimumLayoutSize​(

Container

parent)

Determines the minimum size of the container argument using this
grid layout.

The minimum width of a grid layout is the largest minimum width
of all of the components in the container times the number of columns,
plus the horizontal padding times the number of columns minus one,
plus the left and right insets of the target container.

The minimum height of a grid layout is the largest minimum height
of all of the components in the container times the number of rows,
plus the vertical padding times the number of rows minus one, plus
the top and bottom insets of the target container.

The minimum width of a grid layout is the largest minimum width
of all of the components in the container times the number of columns,
plus the horizontal padding times the number of columns minus one,
plus the left and right insets of the target container.

The minimum height of a grid layout is the largest minimum height
of all of the components in the container times the number of rows,
plus the vertical padding times the number of rows minus one, plus
the top and bottom insets of the target container.

The minimum height of a grid layout is the largest minimum height
of all of the components in the container times the number of rows,
plus the vertical padding times the number of rows minus one, plus
the top and bottom insets of the target container.

layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Lays out the specified container using this layout.

This method reshapes the components in the specified target
container in order to satisfy the constraints of the

GridLayout

object.

The grid layout manager determines the size of individual
components by dividing the free space in the container into
equal-sized portions according to the number of rows and columns
in the layout. The container's free space equals the container's
size minus any insets and any specified horizontal or vertical
gap. All components in a grid layout are given the same size.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**See Also:** Container

,

Container.doLayout()

---

#### layoutContainer

public void layoutContainer​(

Container

parent)

Lays out the specified container using this layout.

This method reshapes the components in the specified target
container in order to satisfy the constraints of the

GridLayout

object.

The grid layout manager determines the size of individual
components by dividing the free space in the container into
equal-sized portions according to the number of rows and columns
in the layout. The container's free space equals the container's
size minus any insets and any specified horizontal or vertical
gap. All components in a grid layout are given the same size.

This method reshapes the components in the specified target
container in order to satisfy the constraints of the

GridLayout

object.

The grid layout manager determines the size of individual
components by dividing the free space in the container into
equal-sized portions according to the number of rows and columns
in the layout. The container's free space equals the container's
size minus any insets and any specified horizontal or vertical
gap. All components in a grid layout are given the same size.

The grid layout manager determines the size of individual
components by dividing the free space in the container into
equal-sized portions according to the number of rows and columns
in the layout. The container's free space equals the container's
size minus any insets and any specified horizontal or vertical
gap. All components in a grid layout are given the same size.

toString

```java
public
String
toString()
```

Returns the string representation of this grid layout's values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this grid layout

---

#### toString

public

String

toString()

Returns the string representation of this grid layout's values.

---

