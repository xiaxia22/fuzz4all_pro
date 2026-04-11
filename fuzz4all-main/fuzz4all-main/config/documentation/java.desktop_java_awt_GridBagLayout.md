# Class GridBagLayout

**Source:** `java.desktop\java\awt\GridBagLayout.html`

### Class Description

```java
public class
GridBagLayout

extends
Object

implements
LayoutManager2
,
Serializable
```

The

GridBagLayout

class is a flexible layout
manager that aligns components vertically, horizontally or along their
baseline without requiring that the components be of the same size.
Each

GridBagLayout

object maintains a dynamic,
rectangular grid of cells, with each component occupying
one or more cells, called its

display area

.

Each component managed by a

GridBagLayout

is associated with
an instance of

GridBagConstraints

. The constraints object
specifies where a component's display area should be located on the grid
and how the component should be positioned within its display area. In
addition to its constraints object, the

GridBagLayout

also
considers each component's minimum and preferred sizes in order to
determine a component's size.

The overall orientation of the grid depends on the container's

ComponentOrientation

property. For horizontal left-to-right
orientations, grid coordinate (0,0) is in the upper left corner of the
container with x increasing to the right and y increasing downward. For
horizontal right-to-left orientations, grid coordinate (0,0) is in the upper
right corner of the container with x increasing to the left and y
increasing downward.

To use a grid bag layout effectively, you must customize one or more
of the

GridBagConstraints

objects that are associated
with its components. You customize a

GridBagConstraints

object by setting one or more of its instance variables:

Each row may have a baseline; the baseline is determined by the
components in that row that have a valid baseline and are aligned
along the baseline (the component's anchor value is one of

BASELINE

,

BASELINE_LEADING

or

BASELINE_TRAILING

).
If none of the components in the row has a valid baseline, the row
does not have a baseline.

If a component spans rows it is aligned either to the baseline of
the start row (if the baseline-resize behavior is

CONSTANT_ASCENT

) or the end row (if the baseline-resize behavior
is

CONSTANT_DESCENT

). The row that the component is
aligned to is called the

prevailing row

.

The following figure shows a baseline layout and includes a
component that spans rows:

Baseline Layout

This layout consists of three components:

- A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Because the second button and the panel share the same prevailing row,
they are both aligned along their baseline.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
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

#### protected static final int MAXGRIDSIZE

This field is no longer used to reserve arrays and kept for backward
compatibility. Previously, this was
the maximum number of grid positions (both horizontal and
vertical) that could be laid out by the grid bag layout.
Current implementation doesn't impose any limits
on the size of a grid.

**See Also:**
- Constant Field Values

---

#### protected static final int MINSIZE

The smallest grid that can be laid out by the grid bag layout.

**See Also:**
- Constant Field Values

---

#### protected static final int PREFERREDSIZE

The preferred grid size that can be laid out by the grid bag layout.

**See Also:**
- Constant Field Values

---

#### protected
Hashtable
<
Component
,​
GridBagConstraints
> comptable

This hashtable maintains the association between
a component and its gridbag constraints.
The Keys in

comptable

are the components and the
values are the instances of

GridBagConstraints

.

**See Also:**
- GridBagConstraints

---

#### protected
GridBagConstraints
defaultConstraints

This field holds a gridbag constraints instance
containing the default values, so if a component
does not have gridbag constraints associated with
it, then the component will be assigned a
copy of the

defaultConstraints

.

**See Also:**
- getConstraints(Component)

,

setConstraints(Component, GridBagConstraints)

,

lookupConstraints(Component)

---

#### protected
GridBagLayoutInfo
layoutInfo

This field holds the layout information
for the gridbag. The information in this field
is based on the most recent validation of the
gridbag.
If

layoutInfo

is

null

this indicates that there are no components in
the gridbag or if there are components, they have
not yet been validated.

**See Also:**
- getLayoutInfo(Container, int)

---

#### public int[] columnWidths

This field holds the overrides to the column minimum
width. If this field is non-

null

the values are
applied to the gridbag after all of the minimum columns
widths have been calculated.
If columnWidths has more elements than the number of
columns, columns are added to the gridbag to match
the number of elements in columnWidth.

**See Also:**
- getLayoutDimensions()

---

#### public int[] rowHeights

This field holds the overrides to the row minimum
heights. If this field is non-

null

the values are
applied to the gridbag after all of the minimum row
heights have been calculated.
If

rowHeights

has more elements than the number of
rows, rows are added to the gridbag to match
the number of elements in

rowHeights

.

**See Also:**
- getLayoutDimensions()

---

#### public double[] columnWeights

This field holds the overrides to the column weights.
If this field is non-

null

the values are
applied to the gridbag after all of the columns
weights have been calculated.
If

columnWeights[i] >

weight for column i, then
column i is assigned the weight in

columnWeights[i]

.
If

columnWeights

has more elements than the number
of columns, the excess elements are ignored - they do
not cause more columns to be created.

---

#### public double[] rowWeights

This field holds the overrides to the row weights.
If this field is non-

null

the values are
applied to the gridbag after all of the rows
weights have been calculated.
If

rowWeights[i] >

weight for row i, then
row i is assigned the weight in

rowWeights[i]

.
If

rowWeights

has more elements than the number
of rows, the excess elements are ignored - they do
not cause more rows to be created.

---

### Constructor Details

#### public GridBagLayout()

Creates a grid bag layout manager.

---

### Method Details

#### public void setConstraints​(
Component
comp,

GridBagConstraints
constraints)

Sets the constraints for the specified component in this layout.

**Parameters:**
- comp

- the component to be modified
- constraints

- the constraints to be applied

---

#### public
GridBagConstraints
getConstraints​(
Component
comp)

Gets the constraints for the specified component. A copy of
the actual

GridBagConstraints

object is returned.

**Parameters:**
- comp

- the component to be queried

**Returns:**
- the constraint for the specified component in this
grid bag layout; a copy of the actual constraint
object is returned

---

#### protected
GridBagConstraints
lookupConstraints​(
Component
comp)

Retrieves the constraints for the specified component.
The return value is not a copy, but is the actual

GridBagConstraints

object used by the layout mechanism.

If

comp

is not in the

GridBagLayout

,
a set of default

GridBagConstraints

are returned.
A

comp

value of

null

is invalid
and returns

null

.

**Parameters:**
- comp

- the component to be queried

**Returns:**
- the constraints for the specified component

---

#### public
Point
getLayoutOrigin()

Determines the origin of the layout area, in the graphics coordinate
space of the target container. This value represents the pixel
coordinates of the top-left corner of the layout area regardless of
the

ComponentOrientation

value of the container. This
is distinct from the grid origin given by the cell coordinates (0,0).
Most applications do not call this method directly.

**Returns:**
- the graphics origin of the cell in the top-left
corner of the layout grid

**See Also:**
- ComponentOrientation

**Since:**
- 1.1

---

#### public int[][] getLayoutDimensions()

Determines column widths and row heights for the layout grid.

Most applications do not call this method directly.

**Returns:**
- an array of two arrays, containing the widths
of the layout columns and
the heights of the layout rows

**Since:**
- 1.1

---

#### public double[][] getLayoutWeights()

Determines the weights of the layout grid's columns and rows.
Weights are used to calculate how much a given column or row
stretches beyond its preferred size, if the layout has extra
room to fill.

Most applications do not call this method directly.

**Returns:**
- an array of two arrays, representing the
horizontal weights of the layout columns
and the vertical weights of the layout rows

**Since:**
- 1.1

---

#### public
Point
location​(int x,
int y)

Determines which cell in the layout grid contains the point
specified by

(x, y)

. Each cell is identified
by its column index (ranging from 0 to the number of columns
minus 1) and its row index (ranging from 0 to the number of
rows minus 1).

If the

(x, y)

point lies
outside the grid, the following rules are used.
The column index is returned as zero if

x

lies to the
left of the layout for a left-to-right container or to the right of
the layout for a right-to-left container. The column index is returned
as the number of columns if

x

lies
to the right of the layout in a left-to-right container or to the left
in a right-to-left container.
The row index is returned as zero if

y

lies above the
layout, and as the number of rows if

y

lies
below the layout. The orientation of a container is determined by its

ComponentOrientation

property.

**Parameters:**
- x

- the

x

coordinate of a point
- y

- the

y

coordinate of a point

**Returns:**
- an ordered pair of indexes that indicate which cell
in the layout grid contains the point
(

x

,

y

).

**See Also:**
- ComponentOrientation

**Since:**
- 1.1

---

#### public void addLayoutComponent​(
String
name,

Component
comp)

Has no effect, since this layout manager does not use a per-component string.

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

#### public void addLayoutComponent​(
Component
comp,

Object
constraints)

Adds the specified component to the layout, using the specified

constraints

object. Note that constraints
are mutable and are, therefore, cloned when cached.

**Specified by:**
- addLayoutComponent

in interface

LayoutManager2

**Parameters:**
- comp

- the component to be added
- constraints

- an object that determines how
the component is added to the layout

**Throws:**
- IllegalArgumentException

- if

constraints

is not a

GridBagConstraint

---

#### public void removeLayoutComponent​(
Component
comp)

Removes the specified component from this layout.

Most applications do not call this method directly.

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

Determines the preferred size of the

parent

container using this grid bag layout.

Most applications do not call this method directly.

**Specified by:**
- preferredLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the container in which to do the layout

**Returns:**
- the preferred size of the

parent

container

**See Also:**
- Container.getPreferredSize()

---

#### public
Dimension
minimumLayoutSize​(
Container
parent)

Determines the minimum size of the

parent

container
using this grid bag layout.

Most applications do not call this method directly.

**Specified by:**
- minimumLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the container in which to do the layout

**Returns:**
- the minimum size of the

parent

container

**See Also:**
- Container.doLayout()

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

- the container which needs to be laid out

**Returns:**
- the maximum dimensions for this layout

**See Also:**
- Container

,

minimumLayoutSize(Container)

,

preferredLayoutSize(Container)

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
- the value

0.5f

to indicate centered

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
- the value

0.5f

to indicate centered

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

Lays out the specified container using this grid bag layout.
This method reshapes components in the specified container in
order to satisfy the constraints of this

GridBagLayout

object.

Most applications do not call this method directly.

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

Returns a string representation of this grid bag layout's values.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this grid bag layout.

---

#### protected
GridBagLayoutInfo
getLayoutInfo​(
Container
parent,
int sizeflag)

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This requires three passes through the
set of children:

- Figure out the dimensions of the layout grid.

Determine which cells the components occupy.

Distribute the weights and min sizes among the rows/columns.

This also caches the minsizes for all the children when they are
first encountered (so subsequent loops don't need to ask again).

This method should only be used internally by

GridBagLayout

.

**Parameters:**
- parent

- the layout container
- sizeflag

- either

PREFERREDSIZE

or

MINSIZE

**Returns:**
- the

GridBagLayoutInfo

for the set of children

**Since:**
- 1.4

---

#### protected
GridBagLayoutInfo
GetLayoutInfo​(
Container
parent,
int sizeflag)

This method is obsolete and supplied for backwards
compatibility only; new code should call

getLayoutInfo

instead.

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This method is the same
as

getLayoutInfo

; refer to

getLayoutInfo

description for details.

**Parameters:**
- parent

- the layout container
- sizeflag

- either

PREFERREDSIZE

or

MINSIZE

**Returns:**
- the

GridBagLayoutInfo

for the set of children

---

#### protected void adjustForGravity​(
GridBagConstraints
constraints,

Rectangle
r)

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.
This method should only be used internally by

GridBagLayout

.

**Parameters:**
- constraints

- the constraints to be applied
- r

- the

Rectangle

to be adjusted

**Since:**
- 1.4

---

#### protected void AdjustForGravity​(
GridBagConstraints
constraints,

Rectangle
r)

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

This method is obsolete and supplied for backwards
compatibility only; new code should call

adjustForGravity

instead.
This method is the same as

adjustForGravity

**Parameters:**
- constraints

- the constraints to be applied
- r

- the

Rectangle

to be adjusted

---

#### protected
Dimension
getMinSize​(
Container
parent,

GridBagLayoutInfo
info)

Figures out the minimum size of the
parent based on the information from

getLayoutInfo

.
This method should only be used internally by

GridBagLayout

.

**Parameters:**
- parent

- the layout container
- info

- the layout info for this parent

**Returns:**
- a

Dimension

object containing the
minimum size

**Since:**
- 1.4

---

#### protected
Dimension
GetMinSize​(
Container
parent,

GridBagLayoutInfo
info)

This method is obsolete and supplied for backwards
compatibility only; new code should call

getMinSize

instead.
This method is the same as

getMinSize

**Parameters:**
- parent

- the layout container
- info

- the layout info for this parent

**Returns:**
- a

Dimension

object containing the
minimum size

---

#### protected void arrangeGrid​(
Container
parent)

Lays out the grid.
This method should only be used internally by

GridBagLayout

.

**Parameters:**
- parent

- the layout container

**Since:**
- 1.4

---

#### protected void ArrangeGrid​(
Container
parent)

This method is obsolete and supplied for backwards
compatibility only; new code should call

arrangeGrid

instead.
This method is the same as

arrangeGrid

**Parameters:**
- parent

- the layout container

---

### Additional Sections

#### Class GridBagLayout

java.lang.Object

- java.awt.GridBagLayout

java.awt.GridBagLayout

**All Implemented Interfaces:** LayoutManager

,

LayoutManager2

,

Serializable

```java
public class
GridBagLayout

extends
Object

implements
LayoutManager2
,
Serializable
```

The

GridBagLayout

class is a flexible layout
manager that aligns components vertically, horizontally or along their
baseline without requiring that the components be of the same size.
Each

GridBagLayout

object maintains a dynamic,
rectangular grid of cells, with each component occupying
one or more cells, called its

display area

.

Each component managed by a

GridBagLayout

is associated with
an instance of

GridBagConstraints

. The constraints object
specifies where a component's display area should be located on the grid
and how the component should be positioned within its display area. In
addition to its constraints object, the

GridBagLayout

also
considers each component's minimum and preferred sizes in order to
determine a component's size.

The overall orientation of the grid depends on the container's

ComponentOrientation

property. For horizontal left-to-right
orientations, grid coordinate (0,0) is in the upper left corner of the
container with x increasing to the right and y increasing downward. For
horizontal right-to-left orientations, grid coordinate (0,0) is in the upper
right corner of the container with x increasing to the left and y
increasing downward.

To use a grid bag layout effectively, you must customize one or more
of the

GridBagConstraints

objects that are associated
with its components. You customize a

GridBagConstraints

object by setting one or more of its instance variables:

Each row may have a baseline; the baseline is determined by the
components in that row that have a valid baseline and are aligned
along the baseline (the component's anchor value is one of

BASELINE

,

BASELINE_LEADING

or

BASELINE_TRAILING

).
If none of the components in the row has a valid baseline, the row
does not have a baseline.

If a component spans rows it is aligned either to the baseline of
the start row (if the baseline-resize behavior is

CONSTANT_ASCENT

) or the end row (if the baseline-resize behavior
is

CONSTANT_DESCENT

). The row that the component is
aligned to is called the

prevailing row

.

The following figure shows a baseline layout and includes a
component that spans rows:

Baseline Layout

This layout consists of three components:

- A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Because the second button and the panel share the same prevailing row,
they are both aligned along their baseline.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

**Since:** 1.0
**See Also:** GridBagConstraints

,

GridBagLayoutInfo

,

ComponentOrientation

,

Serialized Form

public class

GridBagLayout

extends

Object

implements

LayoutManager2

,

Serializable

The

GridBagLayout

class is a flexible layout
manager that aligns components vertically, horizontally or along their
baseline without requiring that the components be of the same size.
Each

GridBagLayout

object maintains a dynamic,
rectangular grid of cells, with each component occupying
one or more cells, called its

display area

.

Each component managed by a

GridBagLayout

is associated with
an instance of

GridBagConstraints

. The constraints object
specifies where a component's display area should be located on the grid
and how the component should be positioned within its display area. In
addition to its constraints object, the

GridBagLayout

also
considers each component's minimum and preferred sizes in order to
determine a component's size.

The overall orientation of the grid depends on the container's

ComponentOrientation

property. For horizontal left-to-right
orientations, grid coordinate (0,0) is in the upper left corner of the
container with x increasing to the right and y increasing downward. For
horizontal right-to-left orientations, grid coordinate (0,0) is in the upper
right corner of the container with x increasing to the left and y
increasing downward.

To use a grid bag layout effectively, you must customize one or more
of the

GridBagConstraints

objects that are associated
with its components. You customize a

GridBagConstraints

object by setting one or more of its instance variables:

Each row may have a baseline; the baseline is determined by the
components in that row that have a valid baseline and are aligned
along the baseline (the component's anchor value is one of

BASELINE

,

BASELINE_LEADING

or

BASELINE_TRAILING

).
If none of the components in the row has a valid baseline, the row
does not have a baseline.

If a component spans rows it is aligned either to the baseline of
the start row (if the baseline-resize behavior is

CONSTANT_ASCENT

) or the end row (if the baseline-resize behavior
is

CONSTANT_DESCENT

). The row that the component is
aligned to is called the

prevailing row

.

The following figure shows a baseline layout and includes a
component that spans rows:

Baseline Layout

This layout consists of three components:

- A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Because the second button and the panel share the same prevailing row,
they are both aligned along their baseline.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

Each component managed by a

GridBagLayout

is associated with
an instance of

GridBagConstraints

. The constraints object
specifies where a component's display area should be located on the grid
and how the component should be positioned within its display area. In
addition to its constraints object, the

GridBagLayout

also
considers each component's minimum and preferred sizes in order to
determine a component's size.

The overall orientation of the grid depends on the container's

ComponentOrientation

property. For horizontal left-to-right
orientations, grid coordinate (0,0) is in the upper left corner of the
container with x increasing to the right and y increasing downward. For
horizontal right-to-left orientations, grid coordinate (0,0) is in the upper
right corner of the container with x increasing to the left and y
increasing downward.

To use a grid bag layout effectively, you must customize one or more
of the

GridBagConstraints

objects that are associated
with its components. You customize a

GridBagConstraints

object by setting one or more of its instance variables:

Each row may have a baseline; the baseline is determined by the
components in that row that have a valid baseline and are aligned
along the baseline (the component's anchor value is one of

BASELINE

,

BASELINE_LEADING

or

BASELINE_TRAILING

).
If none of the components in the row has a valid baseline, the row
does not have a baseline.

If a component spans rows it is aligned either to the baseline of
the start row (if the baseline-resize behavior is

CONSTANT_ASCENT

) or the end row (if the baseline-resize behavior
is

CONSTANT_DESCENT

). The row that the component is
aligned to is called the

prevailing row

.

The following figure shows a baseline layout and includes a
component that spans rows:

Baseline Layout

This layout consists of three components:

- A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Because the second button and the panel share the same prevailing row,
they are both aligned along their baseline.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

The overall orientation of the grid depends on the container's

ComponentOrientation

property. For horizontal left-to-right
orientations, grid coordinate (0,0) is in the upper left corner of the
container with x increasing to the right and y increasing downward. For
horizontal right-to-left orientations, grid coordinate (0,0) is in the upper
right corner of the container with x increasing to the left and y
increasing downward.

To use a grid bag layout effectively, you must customize one or more
of the

GridBagConstraints

objects that are associated
with its components. You customize a

GridBagConstraints

object by setting one or more of its instance variables:

Each row may have a baseline; the baseline is determined by the
components in that row that have a valid baseline and are aligned
along the baseline (the component's anchor value is one of

BASELINE

,

BASELINE_LEADING

or

BASELINE_TRAILING

).
If none of the components in the row has a valid baseline, the row
does not have a baseline.

If a component spans rows it is aligned either to the baseline of
the start row (if the baseline-resize behavior is

CONSTANT_ASCENT

) or the end row (if the baseline-resize behavior
is

CONSTANT_DESCENT

). The row that the component is
aligned to is called the

prevailing row

.

The following figure shows a baseline layout and includes a
component that spans rows:

Baseline Layout

This layout consists of three components:

- A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Because the second button and the panel share the same prevailing row,
they are both aligned along their baseline.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

To use a grid bag layout effectively, you must customize one or more
of the

GridBagConstraints

objects that are associated
with its components. You customize a

GridBagConstraints

object by setting one or more of its instance variables:

Each row may have a baseline; the baseline is determined by the
components in that row that have a valid baseline and are aligned
along the baseline (the component's anchor value is one of

BASELINE

,

BASELINE_LEADING

or

BASELINE_TRAILING

).
If none of the components in the row has a valid baseline, the row
does not have a baseline.

If a component spans rows it is aligned either to the baseline of
the start row (if the baseline-resize behavior is

CONSTANT_ASCENT

) or the end row (if the baseline-resize behavior
is

CONSTANT_DESCENT

). The row that the component is
aligned to is called the

prevailing row

.

The following figure shows a baseline layout and includes a
component that spans rows:

Baseline Layout

This layout consists of three components:

- A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Because the second button and the panel share the same prevailing row,
they are both aligned along their baseline.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

Absolute Values

Orientation Relative Values

Baseline Relative Values

GridBagConstraints.NORTH

GridBagConstraints.SOUTH

GridBagConstraints.WEST

GridBagConstraints.EAST

GridBagConstraints.NORTHWEST

GridBagConstraints.NORTHEAST

GridBagConstraints.SOUTHWEST

GridBagConstraints.SOUTHEAST

GridBagConstraints.CENTER

(the default)

GridBagConstraints.PAGE_START

GridBagConstraints.PAGE_END

GridBagConstraints.LINE_START

GridBagConstraints.LINE_END

GridBagConstraints.FIRST_LINE_START

GridBagConstraints.FIRST_LINE_END

GridBagConstraints.LAST_LINE_START

GridBagConstraints.LAST_LINE_END

GridBagConstraints.BASELINE

GridBagConstraints.BASELINE_LEADING

GridBagConstraints.BASELINE_TRAILING

GridBagConstraints.ABOVE_BASELINE

GridBagConstraints.ABOVE_BASELINE_LEADING

GridBagConstraints.ABOVE_BASELINE_TRAILING

GridBagConstraints.BELOW_BASELINE

GridBagConstraints.BELOW_BASELINE_LEADING

GridBagConstraints.BELOW_BASELINE_TRAILING

Each row may have a baseline; the baseline is determined by the
components in that row that have a valid baseline and are aligned
along the baseline (the component's anchor value is one of

BASELINE

,

BASELINE_LEADING

or

BASELINE_TRAILING

).
If none of the components in the row has a valid baseline, the row
does not have a baseline.

If a component spans rows it is aligned either to the baseline of
the start row (if the baseline-resize behavior is

CONSTANT_ASCENT

) or the end row (if the baseline-resize behavior
is

CONSTANT_DESCENT

). The row that the component is
aligned to is called the

prevailing row

.

The following figure shows a baseline layout and includes a
component that spans rows:

Baseline Layout

This layout consists of three components:

- A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Because the second button and the panel share the same prevailing row,
they are both aligned along their baseline.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

If a component spans rows it is aligned either to the baseline of
the start row (if the baseline-resize behavior is

CONSTANT_ASCENT

) or the end row (if the baseline-resize behavior
is

CONSTANT_DESCENT

). The row that the component is
aligned to is called the

prevailing row

.

The following figure shows a baseline layout and includes a
component that spans rows:

Baseline Layout

This layout consists of three components:

- A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Because the second button and the panel share the same prevailing row,
they are both aligned along their baseline.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

The following figure shows a baseline layout and includes a
component that spans rows:

Baseline Layout

This layout consists of three components:

- A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Because the second button and the panel share the same prevailing row,
they are both aligned along their baseline.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

A panel that starts in row 0 and ends in row 1. The panel
has a baseline-resize behavior of

CONSTANT_DESCENT

and has
an anchor of

BASELINE

. As the baseline-resize behavior
is

CONSTANT_DESCENT

the prevailing row for the panel is
row 1.

Two buttons, each with a baseline-resize behavior of

CENTER_OFFSET

and an anchor of

BASELINE

.

Components positioned using one of the baseline-relative values resize
differently than when positioned using an absolute or orientation-relative
value. How components change is dictated by how the baseline of the
prevailing row changes. The baseline is anchored to the
bottom of the display area if any components with the same prevailing row
have a baseline-resize behavior of

CONSTANT_DESCENT

,
otherwise the baseline is anchored to the top of the display area.
The following rules dictate the resize behavior:

- Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

If you position a component along the baseline, but the
component does not have a valid baseline, it will be vertically centered
in its space. Similarly if you have positioned a component relative
to the baseline and none of the components in the row have a valid
baseline the component is vertically centered.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

Resizable components positioned above the baseline can only
grow as tall as the baseline. For example, if the baseline is at 100
and anchored at the top, a resizable component positioned above the
baseline can never grow more than 100 units.

Similarly, resizable components positioned below the baseline can
only grow as high as the difference between the display height and the
baseline.

Resizable components positioned on the baseline with a
baseline-resize behavior of

OTHER

are only resized if
the baseline at the resized size fits within the display area. If
the baseline is such that it does not fit within the display area
the component is not resized.

Components positioned on the baseline that do not have a
baseline-resize behavior of

OTHER

can only grow as tall as

display height - baseline + baseline of component

.

The following figures show ten components (all buttons)
managed by a grid bag layout. Figure 2 shows the layout for a horizontal,
left-to-right container and Figure 3 shows the layout for a horizontal,
right-to-left container.

Figures

Figure 2: Horizontal, Left-to-Right

Figure 3: Horizontal, Right-to-Left

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

Each of the ten components has the

fill

field
of its associated

GridBagConstraints

object
set to

GridBagConstraints.BOTH

.
In addition, the components have the following non-default constraints:

- Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

Button1, Button2, Button3:

weightx = 1.0

Button4:

weightx = 1.0

,

gridwidth = GridBagConstraints.REMAINDER

Button5:

gridwidth = GridBagConstraints.REMAINDER

Button6:

gridwidth = GridBagConstraints.RELATIVE

Button7:

gridwidth = GridBagConstraints.REMAINDER

Button8:

gridheight = 2

,

weighty = 1.0

Button9, Button 10:

gridwidth = GridBagConstraints.REMAINDER

Here is the code that implements the example shown above:

```java
import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}
```

import java.awt.*;
import java.util.*;
import java.applet.Applet;

public class GridBagEx1 extends Applet {

protected void makebutton(String name,
GridBagLayout gridbag,
GridBagConstraints c) {
Button button = new Button(name);
gridbag.setConstraints(button, c);
add(button);
}

public void init() {
GridBagLayout gridbag = new GridBagLayout();
GridBagConstraints c = new GridBagConstraints();

setFont(new Font("SansSerif", Font.PLAIN, 14));
setLayout(gridbag);

c.fill = GridBagConstraints.BOTH;
c.weightx = 1.0;
makebutton("Button1", gridbag, c);
makebutton("Button2", gridbag, c);
makebutton("Button3", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button4", gridbag, c);

c.weightx = 0.0; //reset to the default
makebutton("Button5", gridbag, c); //another row

c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last in row
makebutton("Button6", gridbag, c);

c.gridwidth = GridBagConstraints.REMAINDER; //end row
makebutton("Button7", gridbag, c);

c.gridwidth = 1; //reset to the default
c.gridheight = 2;
c.weighty = 1.0;
makebutton("Button8", gridbag, c);

c.weighty = 0.0; //reset to the default
c.gridwidth = GridBagConstraints.REMAINDER; //end row
c.gridheight = 1; //reset to the default
makebutton("Button9", gridbag, c);
makebutton("Button10", gridbag, c);

setSize(300, 100);
}

public static void main(String args[]) {
Frame f = new Frame("GridBag Layout Example");
GridBagEx1 ex1 = new GridBagEx1();

ex1.init();

f.add("Center", ex1);
f.pack();
f.setSize(f.getPreferredSize());
f.show();
}
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

double[]

columnWeights

This field holds the overrides to the column weights.

int[]

columnWidths

This field holds the overrides to the column minimum
width.

protected

Hashtable

<

Component

,​

GridBagConstraints

>

comptable

This hashtable maintains the association between
a component and its gridbag constraints.

protected

GridBagConstraints

defaultConstraints

This field holds a gridbag constraints instance
containing the default values, so if a component
does not have gridbag constraints associated with
it, then the component will be assigned a
copy of the

defaultConstraints

.

protected

GridBagLayoutInfo

layoutInfo

This field holds the layout information
for the gridbag.

protected static int

MAXGRIDSIZE

This field is no longer used to reserve arrays and kept for backward
compatibility.

protected static int

MINSIZE

The smallest grid that can be laid out by the grid bag layout.

protected static int

PREFERREDSIZE

The preferred grid size that can be laid out by the grid bag layout.

int[]

rowHeights

This field holds the overrides to the row minimum
heights.

double[]

rowWeights

This field holds the overrides to the row weights.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GridBagLayout

()

Creates a grid bag layout manager.

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

constraints

object.

void

addLayoutComponent

​(

String

name,

Component

comp)

Has no effect, since this layout manager does not use a per-component string.

protected void

adjustForGravity

​(

GridBagConstraints

constraints,

Rectangle

r)

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

protected void

AdjustForGravity

​(

GridBagConstraints

constraints,

Rectangle

r)

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

protected void

arrangeGrid

​(

Container

parent)

Lays out the grid.

protected void

ArrangeGrid

​(

Container

parent)

This method is obsolete and supplied for backwards
compatibility only; new code should call

arrangeGrid

instead.

GridBagConstraints

getConstraints

​(

Component

comp)

Gets the constraints for the specified component.

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

int[][]

getLayoutDimensions

()

Determines column widths and row heights for the layout grid.

protected

GridBagLayoutInfo

getLayoutInfo

​(

Container

parent,
int sizeflag)

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children.

protected

GridBagLayoutInfo

GetLayoutInfo

​(

Container

parent,
int sizeflag)

This method is obsolete and supplied for backwards
compatibility only; new code should call

getLayoutInfo

instead.

Point

getLayoutOrigin

()

Determines the origin of the layout area, in the graphics coordinate
space of the target container.

double[][]

getLayoutWeights

()

Determines the weights of the layout grid's columns and rows.

protected

Dimension

getMinSize

​(

Container

parent,

GridBagLayoutInfo

info)

Figures out the minimum size of the
parent based on the information from

getLayoutInfo

.

protected

Dimension

GetMinSize

​(

Container

parent,

GridBagLayoutInfo

info)

This method is obsolete and supplied for backwards
compatibility only; new code should call

getMinSize

instead.

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

parent)

Lays out the specified container using this grid bag layout.

Point

location

​(int x,
int y)

Determines which cell in the layout grid contains the point
specified by

(x, y)

.

protected

GridBagConstraints

lookupConstraints

​(

Component

comp)

Retrieves the constraints for the specified component.

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

Determines the minimum size of the

parent

container
using this grid bag layout.

Dimension

preferredLayoutSize

​(

Container

parent)

Determines the preferred size of the

parent

container using this grid bag layout.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from this layout.

void

setConstraints

​(

Component

comp,

GridBagConstraints

constraints)

Sets the constraints for the specified component in this layout.

String

toString

()

Returns a string representation of this grid bag layout's values.

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

double[]

columnWeights

This field holds the overrides to the column weights.

int[]

columnWidths

This field holds the overrides to the column minimum
width.

protected

Hashtable

<

Component

,​

GridBagConstraints

>

comptable

This hashtable maintains the association between
a component and its gridbag constraints.

protected

GridBagConstraints

defaultConstraints

This field holds a gridbag constraints instance
containing the default values, so if a component
does not have gridbag constraints associated with
it, then the component will be assigned a
copy of the

defaultConstraints

.

protected

GridBagLayoutInfo

layoutInfo

This field holds the layout information
for the gridbag.

protected static int

MAXGRIDSIZE

This field is no longer used to reserve arrays and kept for backward
compatibility.

protected static int

MINSIZE

The smallest grid that can be laid out by the grid bag layout.

protected static int

PREFERREDSIZE

The preferred grid size that can be laid out by the grid bag layout.

int[]

rowHeights

This field holds the overrides to the row minimum
heights.

double[]

rowWeights

This field holds the overrides to the row weights.

---

#### Field Summary

This field holds the overrides to the column weights.

This field holds the overrides to the column minimum
width.

This hashtable maintains the association between
a component and its gridbag constraints.

This field holds a gridbag constraints instance
containing the default values, so if a component
does not have gridbag constraints associated with
it, then the component will be assigned a
copy of the

defaultConstraints

.

This field holds the layout information
for the gridbag.

This field is no longer used to reserve arrays and kept for backward
compatibility.

The smallest grid that can be laid out by the grid bag layout.

The preferred grid size that can be laid out by the grid bag layout.

This field holds the overrides to the row minimum
heights.

This field holds the overrides to the row weights.

Constructor Summary

Constructors

Constructor

Description

GridBagLayout

()

Creates a grid bag layout manager.

---

#### Constructor Summary

Creates a grid bag layout manager.

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

constraints

object.

void

addLayoutComponent

​(

String

name,

Component

comp)

Has no effect, since this layout manager does not use a per-component string.

protected void

adjustForGravity

​(

GridBagConstraints

constraints,

Rectangle

r)

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

protected void

AdjustForGravity

​(

GridBagConstraints

constraints,

Rectangle

r)

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

protected void

arrangeGrid

​(

Container

parent)

Lays out the grid.

protected void

ArrangeGrid

​(

Container

parent)

This method is obsolete and supplied for backwards
compatibility only; new code should call

arrangeGrid

instead.

GridBagConstraints

getConstraints

​(

Component

comp)

Gets the constraints for the specified component.

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

int[][]

getLayoutDimensions

()

Determines column widths and row heights for the layout grid.

protected

GridBagLayoutInfo

getLayoutInfo

​(

Container

parent,
int sizeflag)

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children.

protected

GridBagLayoutInfo

GetLayoutInfo

​(

Container

parent,
int sizeflag)

This method is obsolete and supplied for backwards
compatibility only; new code should call

getLayoutInfo

instead.

Point

getLayoutOrigin

()

Determines the origin of the layout area, in the graphics coordinate
space of the target container.

double[][]

getLayoutWeights

()

Determines the weights of the layout grid's columns and rows.

protected

Dimension

getMinSize

​(

Container

parent,

GridBagLayoutInfo

info)

Figures out the minimum size of the
parent based on the information from

getLayoutInfo

.

protected

Dimension

GetMinSize

​(

Container

parent,

GridBagLayoutInfo

info)

This method is obsolete and supplied for backwards
compatibility only; new code should call

getMinSize

instead.

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

parent)

Lays out the specified container using this grid bag layout.

Point

location

​(int x,
int y)

Determines which cell in the layout grid contains the point
specified by

(x, y)

.

protected

GridBagConstraints

lookupConstraints

​(

Component

comp)

Retrieves the constraints for the specified component.

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

Determines the minimum size of the

parent

container
using this grid bag layout.

Dimension

preferredLayoutSize

​(

Container

parent)

Determines the preferred size of the

parent

container using this grid bag layout.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from this layout.

void

setConstraints

​(

Component

comp,

GridBagConstraints

constraints)

Sets the constraints for the specified component in this layout.

String

toString

()

Returns a string representation of this grid bag layout's values.

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

constraints

object.

Has no effect, since this layout manager does not use a per-component string.

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

Lays out the grid.

This method is obsolete and supplied for backwards
compatibility only; new code should call

arrangeGrid

instead.

Gets the constraints for the specified component.

Returns the alignment along the x axis.

Returns the alignment along the y axis.

Determines column widths and row heights for the layout grid.

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children.

This method is obsolete and supplied for backwards
compatibility only; new code should call

getLayoutInfo

instead.

Determines the origin of the layout area, in the graphics coordinate
space of the target container.

Determines the weights of the layout grid's columns and rows.

Figures out the minimum size of the
parent based on the information from

getLayoutInfo

.

This method is obsolete and supplied for backwards
compatibility only; new code should call

getMinSize

instead.

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

Lays out the specified container using this grid bag layout.

Determines which cell in the layout grid contains the point
specified by

(x, y)

.

Retrieves the constraints for the specified component.

Returns the maximum dimensions for this layout given the components
in the specified target container.

Determines the minimum size of the

parent

container
using this grid bag layout.

Determines the preferred size of the

parent

container using this grid bag layout.

Removes the specified component from this layout.

Sets the constraints for the specified component in this layout.

Returns a string representation of this grid bag layout's values.

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

- MAXGRIDSIZE

```java
protected static final int MAXGRIDSIZE
```

This field is no longer used to reserve arrays and kept for backward
compatibility. Previously, this was
the maximum number of grid positions (both horizontal and
vertical) that could be laid out by the grid bag layout.
Current implementation doesn't impose any limits
on the size of a grid.

**See Also:** Constant Field Values

- MINSIZE

```java
protected static final int MINSIZE
```

The smallest grid that can be laid out by the grid bag layout.

**See Also:** Constant Field Values

- PREFERREDSIZE

```java
protected static final int PREFERREDSIZE
```

The preferred grid size that can be laid out by the grid bag layout.

**See Also:** Constant Field Values

- comptable

```java
protected
Hashtable
<
Component
,​
GridBagConstraints
> comptable
```

This hashtable maintains the association between
a component and its gridbag constraints.
The Keys in

comptable

are the components and the
values are the instances of

GridBagConstraints

.

**See Also:** GridBagConstraints

- defaultConstraints

```java
protected
GridBagConstraints
defaultConstraints
```

This field holds a gridbag constraints instance
containing the default values, so if a component
does not have gridbag constraints associated with
it, then the component will be assigned a
copy of the

defaultConstraints

.

**See Also:** getConstraints(Component)

,

setConstraints(Component, GridBagConstraints)

,

lookupConstraints(Component)

- layoutInfo

```java
protected
GridBagLayoutInfo
layoutInfo
```

This field holds the layout information
for the gridbag. The information in this field
is based on the most recent validation of the
gridbag.
If

layoutInfo

is

null

this indicates that there are no components in
the gridbag or if there are components, they have
not yet been validated.

**See Also:** getLayoutInfo(Container, int)

- columnWidths

```java
public int[] columnWidths
```

This field holds the overrides to the column minimum
width. If this field is non-

null

the values are
applied to the gridbag after all of the minimum columns
widths have been calculated.
If columnWidths has more elements than the number of
columns, columns are added to the gridbag to match
the number of elements in columnWidth.

**See Also:** getLayoutDimensions()

- rowHeights

```java
public int[] rowHeights
```

This field holds the overrides to the row minimum
heights. If this field is non-

null

the values are
applied to the gridbag after all of the minimum row
heights have been calculated.
If

rowHeights

has more elements than the number of
rows, rows are added to the gridbag to match
the number of elements in

rowHeights

.

**See Also:** getLayoutDimensions()

- columnWeights

```java
public double[] columnWeights
```

This field holds the overrides to the column weights.
If this field is non-

null

the values are
applied to the gridbag after all of the columns
weights have been calculated.
If

columnWeights[i] >

weight for column i, then
column i is assigned the weight in

columnWeights[i]

.
If

columnWeights

has more elements than the number
of columns, the excess elements are ignored - they do
not cause more columns to be created.

- rowWeights

```java
public double[] rowWeights
```

This field holds the overrides to the row weights.
If this field is non-

null

the values are
applied to the gridbag after all of the rows
weights have been calculated.
If

rowWeights[i] >

weight for row i, then
row i is assigned the weight in

rowWeights[i]

.
If

rowWeights

has more elements than the number
of rows, the excess elements are ignored - they do
not cause more rows to be created.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GridBagLayout

```java
public GridBagLayout()
```

Creates a grid bag layout manager.

============ METHOD DETAIL ==========

- Method Detail

- setConstraints

```java
public void setConstraints​(
Component
comp,

GridBagConstraints
constraints)
```

Sets the constraints for the specified component in this layout.

**Parameters:** comp

- the component to be modified
**Parameters:** constraints

- the constraints to be applied

- getConstraints

```java
public
GridBagConstraints
getConstraints​(
Component
comp)
```

Gets the constraints for the specified component. A copy of
the actual

GridBagConstraints

object is returned.

**Parameters:** comp

- the component to be queried
**Returns:** the constraint for the specified component in this
grid bag layout; a copy of the actual constraint
object is returned

- lookupConstraints

```java
protected
GridBagConstraints
lookupConstraints​(
Component
comp)
```

Retrieves the constraints for the specified component.
The return value is not a copy, but is the actual

GridBagConstraints

object used by the layout mechanism.

If

comp

is not in the

GridBagLayout

,
a set of default

GridBagConstraints

are returned.
A

comp

value of

null

is invalid
and returns

null

.

**Parameters:** comp

- the component to be queried
**Returns:** the constraints for the specified component

- getLayoutOrigin

```java
public
Point
getLayoutOrigin()
```

Determines the origin of the layout area, in the graphics coordinate
space of the target container. This value represents the pixel
coordinates of the top-left corner of the layout area regardless of
the

ComponentOrientation

value of the container. This
is distinct from the grid origin given by the cell coordinates (0,0).
Most applications do not call this method directly.

**Returns:** the graphics origin of the cell in the top-left
corner of the layout grid
**Since:** 1.1
**See Also:** ComponentOrientation

- getLayoutDimensions

```java
public int[][] getLayoutDimensions()
```

Determines column widths and row heights for the layout grid.

Most applications do not call this method directly.

**Returns:** an array of two arrays, containing the widths
of the layout columns and
the heights of the layout rows
**Since:** 1.1

- getLayoutWeights

```java
public double[][] getLayoutWeights()
```

Determines the weights of the layout grid's columns and rows.
Weights are used to calculate how much a given column or row
stretches beyond its preferred size, if the layout has extra
room to fill.

Most applications do not call this method directly.

**Returns:** an array of two arrays, representing the
horizontal weights of the layout columns
and the vertical weights of the layout rows
**Since:** 1.1

- location

```java
public
Point
location​(int x,
int y)
```

Determines which cell in the layout grid contains the point
specified by

(x, y)

. Each cell is identified
by its column index (ranging from 0 to the number of columns
minus 1) and its row index (ranging from 0 to the number of
rows minus 1).

If the

(x, y)

point lies
outside the grid, the following rules are used.
The column index is returned as zero if

x

lies to the
left of the layout for a left-to-right container or to the right of
the layout for a right-to-left container. The column index is returned
as the number of columns if

x

lies
to the right of the layout in a left-to-right container or to the left
in a right-to-left container.
The row index is returned as zero if

y

lies above the
layout, and as the number of rows if

y

lies
below the layout. The orientation of a container is determined by its

ComponentOrientation

property.

**Parameters:** x

- the

x

coordinate of a point
**Parameters:** y

- the

y

coordinate of a point
**Returns:** an ordered pair of indexes that indicate which cell
in the layout grid contains the point
(

x

,

y

).
**Since:** 1.1
**See Also:** ComponentOrientation

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Has no effect, since this layout manager does not use a per-component string.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the string to be associated with the component
**Parameters:** comp

- the component to be added

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified

constraints

object. Note that constraints
are mutable and are, therefore, cloned when cached.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object that determines how
the component is added to the layout
**Throws:** IllegalArgumentException

- if

constraints

is not a

GridBagConstraint

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from this layout.

Most applications do not call this method directly.

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

Determines the preferred size of the

parent

container using this grid bag layout.

Most applications do not call this method directly.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the preferred size of the

parent

container
**See Also:** Container.getPreferredSize()

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Determines the minimum size of the

parent

container
using this grid bag layout.

Most applications do not call this method directly.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the minimum size of the

parent

container
**See Also:** Container.doLayout()

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

- the container which needs to be laid out
**Returns:** the maximum dimensions for this layout
**See Also:** Container

,

minimumLayoutSize(Container)

,

preferredLayoutSize(Container)

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
**Returns:** the value

0.5f

to indicate centered

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
**Returns:** the value

0.5f

to indicate centered

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

Lays out the specified container using this grid bag layout.
This method reshapes components in the specified container in
order to satisfy the constraints of this

GridBagLayout

object.

Most applications do not call this method directly.

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

Returns a string representation of this grid bag layout's values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this grid bag layout.

- getLayoutInfo

```java
protected
GridBagLayoutInfo
getLayoutInfo​(
Container
parent,
int sizeflag)
```

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This requires three passes through the
set of children:

- Figure out the dimensions of the layout grid.

Determine which cells the components occupy.

Distribute the weights and min sizes among the rows/columns.

This also caches the minsizes for all the children when they are
first encountered (so subsequent loops don't need to ask again).

This method should only be used internally by

GridBagLayout

.

**Parameters:** parent

- the layout container
**Parameters:** sizeflag

- either

PREFERREDSIZE

or

MINSIZE
**Returns:** the

GridBagLayoutInfo

for the set of children
**Since:** 1.4

- GetLayoutInfo

```java
protected
GridBagLayoutInfo
GetLayoutInfo​(
Container
parent,
int sizeflag)
```

This method is obsolete and supplied for backwards
compatibility only; new code should call

getLayoutInfo

instead.

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This method is the same
as

getLayoutInfo

; refer to

getLayoutInfo

description for details.

**Parameters:** parent

- the layout container
**Parameters:** sizeflag

- either

PREFERREDSIZE

or

MINSIZE
**Returns:** the

GridBagLayoutInfo

for the set of children

- adjustForGravity

```java
protected void adjustForGravity​(
GridBagConstraints
constraints,

Rectangle
r)
```

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.
This method should only be used internally by

GridBagLayout

.

**Parameters:** constraints

- the constraints to be applied
**Parameters:** r

- the

Rectangle

to be adjusted
**Since:** 1.4

- AdjustForGravity

```java
protected void AdjustForGravity​(
GridBagConstraints
constraints,

Rectangle
r)
```

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

This method is obsolete and supplied for backwards
compatibility only; new code should call

adjustForGravity

instead.
This method is the same as

adjustForGravity

**Parameters:** constraints

- the constraints to be applied
**Parameters:** r

- the

Rectangle

to be adjusted

- getMinSize

```java
protected
Dimension
getMinSize​(
Container
parent,

GridBagLayoutInfo
info)
```

Figures out the minimum size of the
parent based on the information from

getLayoutInfo

.
This method should only be used internally by

GridBagLayout

.

**Parameters:** parent

- the layout container
**Parameters:** info

- the layout info for this parent
**Returns:** a

Dimension

object containing the
minimum size
**Since:** 1.4

- GetMinSize

```java
protected
Dimension
GetMinSize​(
Container
parent,

GridBagLayoutInfo
info)
```

This method is obsolete and supplied for backwards
compatibility only; new code should call

getMinSize

instead.
This method is the same as

getMinSize

**Parameters:** parent

- the layout container
**Parameters:** info

- the layout info for this parent
**Returns:** a

Dimension

object containing the
minimum size

- arrangeGrid

```java
protected void arrangeGrid​(
Container
parent)
```

Lays out the grid.
This method should only be used internally by

GridBagLayout

.

**Parameters:** parent

- the layout container
**Since:** 1.4

- ArrangeGrid

```java
protected void ArrangeGrid​(
Container
parent)
```

This method is obsolete and supplied for backwards
compatibility only; new code should call

arrangeGrid

instead.
This method is the same as

arrangeGrid

**Parameters:** parent

- the layout container

Field Detail

- MAXGRIDSIZE

```java
protected static final int MAXGRIDSIZE
```

This field is no longer used to reserve arrays and kept for backward
compatibility. Previously, this was
the maximum number of grid positions (both horizontal and
vertical) that could be laid out by the grid bag layout.
Current implementation doesn't impose any limits
on the size of a grid.

**See Also:** Constant Field Values

- MINSIZE

```java
protected static final int MINSIZE
```

The smallest grid that can be laid out by the grid bag layout.

**See Also:** Constant Field Values

- PREFERREDSIZE

```java
protected static final int PREFERREDSIZE
```

The preferred grid size that can be laid out by the grid bag layout.

**See Also:** Constant Field Values

- comptable

```java
protected
Hashtable
<
Component
,​
GridBagConstraints
> comptable
```

This hashtable maintains the association between
a component and its gridbag constraints.
The Keys in

comptable

are the components and the
values are the instances of

GridBagConstraints

.

**See Also:** GridBagConstraints

- defaultConstraints

```java
protected
GridBagConstraints
defaultConstraints
```

This field holds a gridbag constraints instance
containing the default values, so if a component
does not have gridbag constraints associated with
it, then the component will be assigned a
copy of the

defaultConstraints

.

**See Also:** getConstraints(Component)

,

setConstraints(Component, GridBagConstraints)

,

lookupConstraints(Component)

- layoutInfo

```java
protected
GridBagLayoutInfo
layoutInfo
```

This field holds the layout information
for the gridbag. The information in this field
is based on the most recent validation of the
gridbag.
If

layoutInfo

is

null

this indicates that there are no components in
the gridbag or if there are components, they have
not yet been validated.

**See Also:** getLayoutInfo(Container, int)

- columnWidths

```java
public int[] columnWidths
```

This field holds the overrides to the column minimum
width. If this field is non-

null

the values are
applied to the gridbag after all of the minimum columns
widths have been calculated.
If columnWidths has more elements than the number of
columns, columns are added to the gridbag to match
the number of elements in columnWidth.

**See Also:** getLayoutDimensions()

- rowHeights

```java
public int[] rowHeights
```

This field holds the overrides to the row minimum
heights. If this field is non-

null

the values are
applied to the gridbag after all of the minimum row
heights have been calculated.
If

rowHeights

has more elements than the number of
rows, rows are added to the gridbag to match
the number of elements in

rowHeights

.

**See Also:** getLayoutDimensions()

- columnWeights

```java
public double[] columnWeights
```

This field holds the overrides to the column weights.
If this field is non-

null

the values are
applied to the gridbag after all of the columns
weights have been calculated.
If

columnWeights[i] >

weight for column i, then
column i is assigned the weight in

columnWeights[i]

.
If

columnWeights

has more elements than the number
of columns, the excess elements are ignored - they do
not cause more columns to be created.

- rowWeights

```java
public double[] rowWeights
```

This field holds the overrides to the row weights.
If this field is non-

null

the values are
applied to the gridbag after all of the rows
weights have been calculated.
If

rowWeights[i] >

weight for row i, then
row i is assigned the weight in

rowWeights[i]

.
If

rowWeights

has more elements than the number
of rows, the excess elements are ignored - they do
not cause more rows to be created.

---

#### Field Detail

MAXGRIDSIZE

```java
protected static final int MAXGRIDSIZE
```

This field is no longer used to reserve arrays and kept for backward
compatibility. Previously, this was
the maximum number of grid positions (both horizontal and
vertical) that could be laid out by the grid bag layout.
Current implementation doesn't impose any limits
on the size of a grid.

**See Also:** Constant Field Values

---

#### MAXGRIDSIZE

protected static final int MAXGRIDSIZE

This field is no longer used to reserve arrays and kept for backward
compatibility. Previously, this was
the maximum number of grid positions (both horizontal and
vertical) that could be laid out by the grid bag layout.
Current implementation doesn't impose any limits
on the size of a grid.

MINSIZE

```java
protected static final int MINSIZE
```

The smallest grid that can be laid out by the grid bag layout.

**See Also:** Constant Field Values

---

#### MINSIZE

protected static final int MINSIZE

The smallest grid that can be laid out by the grid bag layout.

PREFERREDSIZE

```java
protected static final int PREFERREDSIZE
```

The preferred grid size that can be laid out by the grid bag layout.

**See Also:** Constant Field Values

---

#### PREFERREDSIZE

protected static final int PREFERREDSIZE

The preferred grid size that can be laid out by the grid bag layout.

comptable

```java
protected
Hashtable
<
Component
,​
GridBagConstraints
> comptable
```

This hashtable maintains the association between
a component and its gridbag constraints.
The Keys in

comptable

are the components and the
values are the instances of

GridBagConstraints

.

**See Also:** GridBagConstraints

---

#### comptable

protected

Hashtable

<

Component

,​

GridBagConstraints

> comptable

This hashtable maintains the association between
a component and its gridbag constraints.
The Keys in

comptable

are the components and the
values are the instances of

GridBagConstraints

.

defaultConstraints

```java
protected
GridBagConstraints
defaultConstraints
```

This field holds a gridbag constraints instance
containing the default values, so if a component
does not have gridbag constraints associated with
it, then the component will be assigned a
copy of the

defaultConstraints

.

**See Also:** getConstraints(Component)

,

setConstraints(Component, GridBagConstraints)

,

lookupConstraints(Component)

---

#### defaultConstraints

protected

GridBagConstraints

defaultConstraints

This field holds a gridbag constraints instance
containing the default values, so if a component
does not have gridbag constraints associated with
it, then the component will be assigned a
copy of the

defaultConstraints

.

layoutInfo

```java
protected
GridBagLayoutInfo
layoutInfo
```

This field holds the layout information
for the gridbag. The information in this field
is based on the most recent validation of the
gridbag.
If

layoutInfo

is

null

this indicates that there are no components in
the gridbag or if there are components, they have
not yet been validated.

**See Also:** getLayoutInfo(Container, int)

---

#### layoutInfo

protected

GridBagLayoutInfo

layoutInfo

This field holds the layout information
for the gridbag. The information in this field
is based on the most recent validation of the
gridbag.
If

layoutInfo

is

null

this indicates that there are no components in
the gridbag or if there are components, they have
not yet been validated.

columnWidths

```java
public int[] columnWidths
```

This field holds the overrides to the column minimum
width. If this field is non-

null

the values are
applied to the gridbag after all of the minimum columns
widths have been calculated.
If columnWidths has more elements than the number of
columns, columns are added to the gridbag to match
the number of elements in columnWidth.

**See Also:** getLayoutDimensions()

---

#### columnWidths

public int[] columnWidths

This field holds the overrides to the column minimum
width. If this field is non-

null

the values are
applied to the gridbag after all of the minimum columns
widths have been calculated.
If columnWidths has more elements than the number of
columns, columns are added to the gridbag to match
the number of elements in columnWidth.

rowHeights

```java
public int[] rowHeights
```

This field holds the overrides to the row minimum
heights. If this field is non-

null

the values are
applied to the gridbag after all of the minimum row
heights have been calculated.
If

rowHeights

has more elements than the number of
rows, rows are added to the gridbag to match
the number of elements in

rowHeights

.

**See Also:** getLayoutDimensions()

---

#### rowHeights

public int[] rowHeights

This field holds the overrides to the row minimum
heights. If this field is non-

null

the values are
applied to the gridbag after all of the minimum row
heights have been calculated.
If

rowHeights

has more elements than the number of
rows, rows are added to the gridbag to match
the number of elements in

rowHeights

.

columnWeights

```java
public double[] columnWeights
```

This field holds the overrides to the column weights.
If this field is non-

null

the values are
applied to the gridbag after all of the columns
weights have been calculated.
If

columnWeights[i] >

weight for column i, then
column i is assigned the weight in

columnWeights[i]

.
If

columnWeights

has more elements than the number
of columns, the excess elements are ignored - they do
not cause more columns to be created.

---

#### columnWeights

public double[] columnWeights

This field holds the overrides to the column weights.
If this field is non-

null

the values are
applied to the gridbag after all of the columns
weights have been calculated.
If

columnWeights[i] >

weight for column i, then
column i is assigned the weight in

columnWeights[i]

.
If

columnWeights

has more elements than the number
of columns, the excess elements are ignored - they do
not cause more columns to be created.

rowWeights

```java
public double[] rowWeights
```

This field holds the overrides to the row weights.
If this field is non-

null

the values are
applied to the gridbag after all of the rows
weights have been calculated.
If

rowWeights[i] >

weight for row i, then
row i is assigned the weight in

rowWeights[i]

.
If

rowWeights

has more elements than the number
of rows, the excess elements are ignored - they do
not cause more rows to be created.

---

#### rowWeights

public double[] rowWeights

This field holds the overrides to the row weights.
If this field is non-

null

the values are
applied to the gridbag after all of the rows
weights have been calculated.
If

rowWeights[i] >

weight for row i, then
row i is assigned the weight in

rowWeights[i]

.
If

rowWeights

has more elements than the number
of rows, the excess elements are ignored - they do
not cause more rows to be created.

Constructor Detail

- GridBagLayout

```java
public GridBagLayout()
```

Creates a grid bag layout manager.

---

#### Constructor Detail

GridBagLayout

```java
public GridBagLayout()
```

Creates a grid bag layout manager.

---

#### GridBagLayout

public GridBagLayout()

Creates a grid bag layout manager.

Method Detail

- setConstraints

```java
public void setConstraints​(
Component
comp,

GridBagConstraints
constraints)
```

Sets the constraints for the specified component in this layout.

**Parameters:** comp

- the component to be modified
**Parameters:** constraints

- the constraints to be applied

- getConstraints

```java
public
GridBagConstraints
getConstraints​(
Component
comp)
```

Gets the constraints for the specified component. A copy of
the actual

GridBagConstraints

object is returned.

**Parameters:** comp

- the component to be queried
**Returns:** the constraint for the specified component in this
grid bag layout; a copy of the actual constraint
object is returned

- lookupConstraints

```java
protected
GridBagConstraints
lookupConstraints​(
Component
comp)
```

Retrieves the constraints for the specified component.
The return value is not a copy, but is the actual

GridBagConstraints

object used by the layout mechanism.

If

comp

is not in the

GridBagLayout

,
a set of default

GridBagConstraints

are returned.
A

comp

value of

null

is invalid
and returns

null

.

**Parameters:** comp

- the component to be queried
**Returns:** the constraints for the specified component

- getLayoutOrigin

```java
public
Point
getLayoutOrigin()
```

Determines the origin of the layout area, in the graphics coordinate
space of the target container. This value represents the pixel
coordinates of the top-left corner of the layout area regardless of
the

ComponentOrientation

value of the container. This
is distinct from the grid origin given by the cell coordinates (0,0).
Most applications do not call this method directly.

**Returns:** the graphics origin of the cell in the top-left
corner of the layout grid
**Since:** 1.1
**See Also:** ComponentOrientation

- getLayoutDimensions

```java
public int[][] getLayoutDimensions()
```

Determines column widths and row heights for the layout grid.

Most applications do not call this method directly.

**Returns:** an array of two arrays, containing the widths
of the layout columns and
the heights of the layout rows
**Since:** 1.1

- getLayoutWeights

```java
public double[][] getLayoutWeights()
```

Determines the weights of the layout grid's columns and rows.
Weights are used to calculate how much a given column or row
stretches beyond its preferred size, if the layout has extra
room to fill.

Most applications do not call this method directly.

**Returns:** an array of two arrays, representing the
horizontal weights of the layout columns
and the vertical weights of the layout rows
**Since:** 1.1

- location

```java
public
Point
location​(int x,
int y)
```

Determines which cell in the layout grid contains the point
specified by

(x, y)

. Each cell is identified
by its column index (ranging from 0 to the number of columns
minus 1) and its row index (ranging from 0 to the number of
rows minus 1).

If the

(x, y)

point lies
outside the grid, the following rules are used.
The column index is returned as zero if

x

lies to the
left of the layout for a left-to-right container or to the right of
the layout for a right-to-left container. The column index is returned
as the number of columns if

x

lies
to the right of the layout in a left-to-right container or to the left
in a right-to-left container.
The row index is returned as zero if

y

lies above the
layout, and as the number of rows if

y

lies
below the layout. The orientation of a container is determined by its

ComponentOrientation

property.

**Parameters:** x

- the

x

coordinate of a point
**Parameters:** y

- the

y

coordinate of a point
**Returns:** an ordered pair of indexes that indicate which cell
in the layout grid contains the point
(

x

,

y

).
**Since:** 1.1
**See Also:** ComponentOrientation

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Has no effect, since this layout manager does not use a per-component string.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the string to be associated with the component
**Parameters:** comp

- the component to be added

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified

constraints

object. Note that constraints
are mutable and are, therefore, cloned when cached.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object that determines how
the component is added to the layout
**Throws:** IllegalArgumentException

- if

constraints

is not a

GridBagConstraint

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from this layout.

Most applications do not call this method directly.

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

Determines the preferred size of the

parent

container using this grid bag layout.

Most applications do not call this method directly.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the preferred size of the

parent

container
**See Also:** Container.getPreferredSize()

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Determines the minimum size of the

parent

container
using this grid bag layout.

Most applications do not call this method directly.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the minimum size of the

parent

container
**See Also:** Container.doLayout()

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

- the container which needs to be laid out
**Returns:** the maximum dimensions for this layout
**See Also:** Container

,

minimumLayoutSize(Container)

,

preferredLayoutSize(Container)

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
**Returns:** the value

0.5f

to indicate centered

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
**Returns:** the value

0.5f

to indicate centered

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

Lays out the specified container using this grid bag layout.
This method reshapes components in the specified container in
order to satisfy the constraints of this

GridBagLayout

object.

Most applications do not call this method directly.

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

Returns a string representation of this grid bag layout's values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this grid bag layout.

- getLayoutInfo

```java
protected
GridBagLayoutInfo
getLayoutInfo​(
Container
parent,
int sizeflag)
```

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This requires three passes through the
set of children:

- Figure out the dimensions of the layout grid.

Determine which cells the components occupy.

Distribute the weights and min sizes among the rows/columns.

This also caches the minsizes for all the children when they are
first encountered (so subsequent loops don't need to ask again).

This method should only be used internally by

GridBagLayout

.

**Parameters:** parent

- the layout container
**Parameters:** sizeflag

- either

PREFERREDSIZE

or

MINSIZE
**Returns:** the

GridBagLayoutInfo

for the set of children
**Since:** 1.4

- GetLayoutInfo

```java
protected
GridBagLayoutInfo
GetLayoutInfo​(
Container
parent,
int sizeflag)
```

This method is obsolete and supplied for backwards
compatibility only; new code should call

getLayoutInfo

instead.

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This method is the same
as

getLayoutInfo

; refer to

getLayoutInfo

description for details.

**Parameters:** parent

- the layout container
**Parameters:** sizeflag

- either

PREFERREDSIZE

or

MINSIZE
**Returns:** the

GridBagLayoutInfo

for the set of children

- adjustForGravity

```java
protected void adjustForGravity​(
GridBagConstraints
constraints,

Rectangle
r)
```

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.
This method should only be used internally by

GridBagLayout

.

**Parameters:** constraints

- the constraints to be applied
**Parameters:** r

- the

Rectangle

to be adjusted
**Since:** 1.4

- AdjustForGravity

```java
protected void AdjustForGravity​(
GridBagConstraints
constraints,

Rectangle
r)
```

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

This method is obsolete and supplied for backwards
compatibility only; new code should call

adjustForGravity

instead.
This method is the same as

adjustForGravity

**Parameters:** constraints

- the constraints to be applied
**Parameters:** r

- the

Rectangle

to be adjusted

- getMinSize

```java
protected
Dimension
getMinSize​(
Container
parent,

GridBagLayoutInfo
info)
```

Figures out the minimum size of the
parent based on the information from

getLayoutInfo

.
This method should only be used internally by

GridBagLayout

.

**Parameters:** parent

- the layout container
**Parameters:** info

- the layout info for this parent
**Returns:** a

Dimension

object containing the
minimum size
**Since:** 1.4

- GetMinSize

```java
protected
Dimension
GetMinSize​(
Container
parent,

GridBagLayoutInfo
info)
```

This method is obsolete and supplied for backwards
compatibility only; new code should call

getMinSize

instead.
This method is the same as

getMinSize

**Parameters:** parent

- the layout container
**Parameters:** info

- the layout info for this parent
**Returns:** a

Dimension

object containing the
minimum size

- arrangeGrid

```java
protected void arrangeGrid​(
Container
parent)
```

Lays out the grid.
This method should only be used internally by

GridBagLayout

.

**Parameters:** parent

- the layout container
**Since:** 1.4

- ArrangeGrid

```java
protected void ArrangeGrid​(
Container
parent)
```

This method is obsolete and supplied for backwards
compatibility only; new code should call

arrangeGrid

instead.
This method is the same as

arrangeGrid

**Parameters:** parent

- the layout container

---

#### Method Detail

setConstraints

```java
public void setConstraints​(
Component
comp,

GridBagConstraints
constraints)
```

Sets the constraints for the specified component in this layout.

**Parameters:** comp

- the component to be modified
**Parameters:** constraints

- the constraints to be applied

---

#### setConstraints

public void setConstraints​(

Component

comp,

GridBagConstraints

constraints)

Sets the constraints for the specified component in this layout.

getConstraints

```java
public
GridBagConstraints
getConstraints​(
Component
comp)
```

Gets the constraints for the specified component. A copy of
the actual

GridBagConstraints

object is returned.

**Parameters:** comp

- the component to be queried
**Returns:** the constraint for the specified component in this
grid bag layout; a copy of the actual constraint
object is returned

---

#### getConstraints

public

GridBagConstraints

getConstraints​(

Component

comp)

Gets the constraints for the specified component. A copy of
the actual

GridBagConstraints

object is returned.

lookupConstraints

```java
protected
GridBagConstraints
lookupConstraints​(
Component
comp)
```

Retrieves the constraints for the specified component.
The return value is not a copy, but is the actual

GridBagConstraints

object used by the layout mechanism.

If

comp

is not in the

GridBagLayout

,
a set of default

GridBagConstraints

are returned.
A

comp

value of

null

is invalid
and returns

null

.

**Parameters:** comp

- the component to be queried
**Returns:** the constraints for the specified component

---

#### lookupConstraints

protected

GridBagConstraints

lookupConstraints​(

Component

comp)

Retrieves the constraints for the specified component.
The return value is not a copy, but is the actual

GridBagConstraints

object used by the layout mechanism.

If

comp

is not in the

GridBagLayout

,
a set of default

GridBagConstraints

are returned.
A

comp

value of

null

is invalid
and returns

null

.

If

comp

is not in the

GridBagLayout

,
a set of default

GridBagConstraints

are returned.
A

comp

value of

null

is invalid
and returns

null

.

getLayoutOrigin

```java
public
Point
getLayoutOrigin()
```

Determines the origin of the layout area, in the graphics coordinate
space of the target container. This value represents the pixel
coordinates of the top-left corner of the layout area regardless of
the

ComponentOrientation

value of the container. This
is distinct from the grid origin given by the cell coordinates (0,0).
Most applications do not call this method directly.

**Returns:** the graphics origin of the cell in the top-left
corner of the layout grid
**Since:** 1.1
**See Also:** ComponentOrientation

---

#### getLayoutOrigin

public

Point

getLayoutOrigin()

Determines the origin of the layout area, in the graphics coordinate
space of the target container. This value represents the pixel
coordinates of the top-left corner of the layout area regardless of
the

ComponentOrientation

value of the container. This
is distinct from the grid origin given by the cell coordinates (0,0).
Most applications do not call this method directly.

getLayoutDimensions

```java
public int[][] getLayoutDimensions()
```

Determines column widths and row heights for the layout grid.

Most applications do not call this method directly.

**Returns:** an array of two arrays, containing the widths
of the layout columns and
the heights of the layout rows
**Since:** 1.1

---

#### getLayoutDimensions

public int[][] getLayoutDimensions()

Determines column widths and row heights for the layout grid.

Most applications do not call this method directly.

Most applications do not call this method directly.

getLayoutWeights

```java
public double[][] getLayoutWeights()
```

Determines the weights of the layout grid's columns and rows.
Weights are used to calculate how much a given column or row
stretches beyond its preferred size, if the layout has extra
room to fill.

Most applications do not call this method directly.

**Returns:** an array of two arrays, representing the
horizontal weights of the layout columns
and the vertical weights of the layout rows
**Since:** 1.1

---

#### getLayoutWeights

public double[][] getLayoutWeights()

Determines the weights of the layout grid's columns and rows.
Weights are used to calculate how much a given column or row
stretches beyond its preferred size, if the layout has extra
room to fill.

Most applications do not call this method directly.

Most applications do not call this method directly.

location

```java
public
Point
location​(int x,
int y)
```

Determines which cell in the layout grid contains the point
specified by

(x, y)

. Each cell is identified
by its column index (ranging from 0 to the number of columns
minus 1) and its row index (ranging from 0 to the number of
rows minus 1).

If the

(x, y)

point lies
outside the grid, the following rules are used.
The column index is returned as zero if

x

lies to the
left of the layout for a left-to-right container or to the right of
the layout for a right-to-left container. The column index is returned
as the number of columns if

x

lies
to the right of the layout in a left-to-right container or to the left
in a right-to-left container.
The row index is returned as zero if

y

lies above the
layout, and as the number of rows if

y

lies
below the layout. The orientation of a container is determined by its

ComponentOrientation

property.

**Parameters:** x

- the

x

coordinate of a point
**Parameters:** y

- the

y

coordinate of a point
**Returns:** an ordered pair of indexes that indicate which cell
in the layout grid contains the point
(

x

,

y

).
**Since:** 1.1
**See Also:** ComponentOrientation

---

#### location

public

Point

location​(int x,
int y)

Determines which cell in the layout grid contains the point
specified by

(x, y)

. Each cell is identified
by its column index (ranging from 0 to the number of columns
minus 1) and its row index (ranging from 0 to the number of
rows minus 1).

If the

(x, y)

point lies
outside the grid, the following rules are used.
The column index is returned as zero if

x

lies to the
left of the layout for a left-to-right container or to the right of
the layout for a right-to-left container. The column index is returned
as the number of columns if

x

lies
to the right of the layout in a left-to-right container or to the left
in a right-to-left container.
The row index is returned as zero if

y

lies above the
layout, and as the number of rows if

y

lies
below the layout. The orientation of a container is determined by its

ComponentOrientation

property.

If the

(x, y)

point lies
outside the grid, the following rules are used.
The column index is returned as zero if

x

lies to the
left of the layout for a left-to-right container or to the right of
the layout for a right-to-left container. The column index is returned
as the number of columns if

x

lies
to the right of the layout in a left-to-right container or to the left
in a right-to-left container.
The row index is returned as zero if

y

lies above the
layout, and as the number of rows if

y

lies
below the layout. The orientation of a container is determined by its

ComponentOrientation

property.

addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Has no effect, since this layout manager does not use a per-component string.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the string to be associated with the component
**Parameters:** comp

- the component to be added

---

#### addLayoutComponent

public void addLayoutComponent​(

String

name,

Component

comp)

Has no effect, since this layout manager does not use a per-component string.

addLayoutComponent

```java
public void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified

constraints

object. Note that constraints
are mutable and are, therefore, cloned when cached.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object that determines how
the component is added to the layout
**Throws:** IllegalArgumentException

- if

constraints

is not a

GridBagConstraint

---

#### addLayoutComponent

public void addLayoutComponent​(

Component

comp,

Object

constraints)

Adds the specified component to the layout, using the specified

constraints

object. Note that constraints
are mutable and are, therefore, cloned when cached.

removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from this layout.

Most applications do not call this method directly.

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

Removes the specified component from this layout.

Most applications do not call this method directly.

Most applications do not call this method directly.

preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Determines the preferred size of the

parent

container using this grid bag layout.

Most applications do not call this method directly.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the preferred size of the

parent

container
**See Also:** Container.getPreferredSize()

---

#### preferredLayoutSize

public

Dimension

preferredLayoutSize​(

Container

parent)

Determines the preferred size of the

parent

container using this grid bag layout.

Most applications do not call this method directly.

Most applications do not call this method directly.

minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Determines the minimum size of the

parent

container
using this grid bag layout.

Most applications do not call this method directly.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the container in which to do the layout
**Returns:** the minimum size of the

parent

container
**See Also:** Container.doLayout()

---

#### minimumLayoutSize

public

Dimension

minimumLayoutSize​(

Container

parent)

Determines the minimum size of the

parent

container
using this grid bag layout.

Most applications do not call this method directly.

Most applications do not call this method directly.

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

- the container which needs to be laid out
**Returns:** the maximum dimensions for this layout
**See Also:** Container

,

minimumLayoutSize(Container)

,

preferredLayoutSize(Container)

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
**Returns:** the value

0.5f

to indicate centered

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
**Returns:** the value

0.5f

to indicate centered

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

Lays out the specified container using this grid bag layout.
This method reshapes components in the specified container in
order to satisfy the constraints of this

GridBagLayout

object.

Most applications do not call this method directly.

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

Lays out the specified container using this grid bag layout.
This method reshapes components in the specified container in
order to satisfy the constraints of this

GridBagLayout

object.

Most applications do not call this method directly.

Most applications do not call this method directly.

toString

```java
public
String
toString()
```

Returns a string representation of this grid bag layout's values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this grid bag layout.

---

#### toString

public

String

toString()

Returns a string representation of this grid bag layout's values.

getLayoutInfo

```java
protected
GridBagLayoutInfo
getLayoutInfo​(
Container
parent,
int sizeflag)
```

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This requires three passes through the
set of children:

- Figure out the dimensions of the layout grid.

Determine which cells the components occupy.

Distribute the weights and min sizes among the rows/columns.

This also caches the minsizes for all the children when they are
first encountered (so subsequent loops don't need to ask again).

This method should only be used internally by

GridBagLayout

.

**Parameters:** parent

- the layout container
**Parameters:** sizeflag

- either

PREFERREDSIZE

or

MINSIZE
**Returns:** the

GridBagLayoutInfo

for the set of children
**Since:** 1.4

---

#### getLayoutInfo

protected

GridBagLayoutInfo

getLayoutInfo​(

Container

parent,
int sizeflag)

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This requires three passes through the
set of children:

- Figure out the dimensions of the layout grid.

Determine which cells the components occupy.

Distribute the weights and min sizes among the rows/columns.

This also caches the minsizes for all the children when they are
first encountered (so subsequent loops don't need to ask again).

This method should only be used internally by

GridBagLayout

.

Figure out the dimensions of the layout grid.

Determine which cells the components occupy.

Distribute the weights and min sizes among the rows/columns.

This method should only be used internally by

GridBagLayout

.

GetLayoutInfo

```java
protected
GridBagLayoutInfo
GetLayoutInfo​(
Container
parent,
int sizeflag)
```

This method is obsolete and supplied for backwards
compatibility only; new code should call

getLayoutInfo

instead.

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This method is the same
as

getLayoutInfo

; refer to

getLayoutInfo

description for details.

**Parameters:** parent

- the layout container
**Parameters:** sizeflag

- either

PREFERREDSIZE

or

MINSIZE
**Returns:** the

GridBagLayoutInfo

for the set of children

---

#### GetLayoutInfo

protected

GridBagLayoutInfo

GetLayoutInfo​(

Container

parent,
int sizeflag)

This method is obsolete and supplied for backwards
compatibility only; new code should call

getLayoutInfo

instead.

Fills in an instance of

GridBagLayoutInfo

for the
current set of managed children. This method is the same
as

getLayoutInfo

; refer to

getLayoutInfo

description for details.

adjustForGravity

```java
protected void adjustForGravity​(
GridBagConstraints
constraints,

Rectangle
r)
```

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.
This method should only be used internally by

GridBagLayout

.

**Parameters:** constraints

- the constraints to be applied
**Parameters:** r

- the

Rectangle

to be adjusted
**Since:** 1.4

---

#### adjustForGravity

protected void adjustForGravity​(

GridBagConstraints

constraints,

Rectangle

r)

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.
This method should only be used internally by

GridBagLayout

.

AdjustForGravity

```java
protected void AdjustForGravity​(
GridBagConstraints
constraints,

Rectangle
r)
```

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

This method is obsolete and supplied for backwards
compatibility only; new code should call

adjustForGravity

instead.
This method is the same as

adjustForGravity

**Parameters:** constraints

- the constraints to be applied
**Parameters:** r

- the

Rectangle

to be adjusted

---

#### AdjustForGravity

protected void AdjustForGravity​(

GridBagConstraints

constraints,

Rectangle

r)

Adjusts the x, y, width, and height fields to the correct
values depending on the constraint geometry and pads.

This method is obsolete and supplied for backwards
compatibility only; new code should call

adjustForGravity

instead.
This method is the same as

adjustForGravity

This method is obsolete and supplied for backwards
compatibility only; new code should call

adjustForGravity

instead.
This method is the same as

adjustForGravity

getMinSize

```java
protected
Dimension
getMinSize​(
Container
parent,

GridBagLayoutInfo
info)
```

Figures out the minimum size of the
parent based on the information from

getLayoutInfo

.
This method should only be used internally by

GridBagLayout

.

**Parameters:** parent

- the layout container
**Parameters:** info

- the layout info for this parent
**Returns:** a

Dimension

object containing the
minimum size
**Since:** 1.4

---

#### getMinSize

protected

Dimension

getMinSize​(

Container

parent,

GridBagLayoutInfo

info)

Figures out the minimum size of the
parent based on the information from

getLayoutInfo

.
This method should only be used internally by

GridBagLayout

.

GetMinSize

```java
protected
Dimension
GetMinSize​(
Container
parent,

GridBagLayoutInfo
info)
```

This method is obsolete and supplied for backwards
compatibility only; new code should call

getMinSize

instead.
This method is the same as

getMinSize

**Parameters:** parent

- the layout container
**Parameters:** info

- the layout info for this parent
**Returns:** a

Dimension

object containing the
minimum size

---

#### GetMinSize

protected

Dimension

GetMinSize​(

Container

parent,

GridBagLayoutInfo

info)

This method is obsolete and supplied for backwards
compatibility only; new code should call

getMinSize

instead.
This method is the same as

getMinSize

arrangeGrid

```java
protected void arrangeGrid​(
Container
parent)
```

Lays out the grid.
This method should only be used internally by

GridBagLayout

.

**Parameters:** parent

- the layout container
**Since:** 1.4

---

#### arrangeGrid

protected void arrangeGrid​(

Container

parent)

Lays out the grid.
This method should only be used internally by

GridBagLayout

.

ArrangeGrid

```java
protected void ArrangeGrid​(
Container
parent)
```

This method is obsolete and supplied for backwards
compatibility only; new code should call

arrangeGrid

instead.
This method is the same as

arrangeGrid

**Parameters:** parent

- the layout container

---

#### ArrangeGrid

protected void ArrangeGrid​(

Container

parent)

This method is obsolete and supplied for backwards
compatibility only; new code should call

arrangeGrid

instead.
This method is the same as

arrangeGrid

---

