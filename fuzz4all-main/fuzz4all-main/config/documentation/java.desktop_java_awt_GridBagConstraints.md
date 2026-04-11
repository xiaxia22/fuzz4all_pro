# Class GridBagConstraints

**Source:** `java.desktop\java\awt\GridBagConstraints.html`

### Class Description

```java
public class
GridBagConstraints

extends
Object

implements
Cloneable
,
Serializable
```

The

GridBagConstraints

class specifies constraints
for components that are laid out using the

GridBagLayout

class.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public static final int RELATIVE

Specifies that this component is the next-to-last component in its
column or row (

gridwidth

,

gridheight

),
or that this component be placed next to the previously added
component (

gridx

,

gridy

).

**See Also:**
- gridwidth

,

gridheight

,

gridx

,

gridy

,

Constant Field Values

---

#### public static final int REMAINDER

Specifies that this component is the
last component in its column or row.

**See Also:**
- Constant Field Values

---

#### public static final int NONE

Do not resize the component.

**See Also:**
- Constant Field Values

---

#### public static final int BOTH

Resize the component both horizontally and vertically.

**See Also:**
- Constant Field Values

---

#### public static final int HORIZONTAL

Resize the component horizontally but not vertically.

**See Also:**
- Constant Field Values

---

#### public static final int VERTICAL

Resize the component vertically but not horizontally.

**See Also:**
- Constant Field Values

---

#### public static final int CENTER

Put the component in the center of its display area.

**See Also:**
- Constant Field Values

---

#### public static final int NORTH

Put the component at the top of its display area,
centered horizontally.

**See Also:**
- Constant Field Values

---

#### public static final int NORTHEAST

Put the component at the top-right corner of its display area.

**See Also:**
- Constant Field Values

---

#### public static final int EAST

Put the component on the right side of its display area,
centered vertically.

**See Also:**
- Constant Field Values

---

#### public static final int SOUTHEAST

Put the component at the bottom-right corner of its display area.

**See Also:**
- Constant Field Values

---

#### public static final int SOUTH

Put the component at the bottom of its display area, centered
horizontally.

**See Also:**
- Constant Field Values

---

#### public static final int SOUTHWEST

Put the component at the bottom-left corner of its display area.

**See Also:**
- Constant Field Values

---

#### public static final int WEST

Put the component on the left side of its display area,
centered vertically.

**See Also:**
- Constant Field Values

---

#### public static final int NORTHWEST

Put the component at the top-left corner of its display area.

**See Also:**
- Constant Field Values

---

#### public static final int PAGE_START

Place the component centered along the edge of its display area
associated with the start of a page for the current

ComponentOrientation

. Equal to NORTH for horizontal
orientations.

**See Also:**
- Constant Field Values

---

#### public static final int PAGE_END

Place the component centered along the edge of its display area
associated with the end of a page for the current

ComponentOrientation

. Equal to SOUTH for horizontal
orientations.

**See Also:**
- Constant Field Values

---

#### public static final int LINE_START

Place the component centered along the edge of its display area where
lines of text would normally begin for the current

ComponentOrientation

. Equal to WEST for horizontal,
left-to-right orientations and EAST for horizontal, right-to-left
orientations.

**See Also:**
- Constant Field Values

---

#### public static final int LINE_END

Place the component centered along the edge of its display area where
lines of text would normally end for the current

ComponentOrientation

. Equal to EAST for horizontal,
left-to-right orientations and WEST for horizontal, right-to-left
orientations.

**See Also:**
- Constant Field Values

---

#### public static final int FIRST_LINE_START

Place the component in the corner of its display area where
the first line of text on a page would normally begin for the current

ComponentOrientation

. Equal to NORTHWEST for horizontal,
left-to-right orientations and NORTHEAST for horizontal, right-to-left
orientations.

**See Also:**
- Constant Field Values

---

#### public static final int FIRST_LINE_END

Place the component in the corner of its display area where
the first line of text on a page would normally end for the current

ComponentOrientation

. Equal to NORTHEAST for horizontal,
left-to-right orientations and NORTHWEST for horizontal, right-to-left
orientations.

**See Also:**
- Constant Field Values

---

#### public static final int LAST_LINE_START

Place the component in the corner of its display area where
the last line of text on a page would normally start for the current

ComponentOrientation

. Equal to SOUTHWEST for horizontal,
left-to-right orientations and SOUTHEAST for horizontal, right-to-left
orientations.

**See Also:**
- Constant Field Values

---

#### public static final int LAST_LINE_END

Place the component in the corner of its display area where
the last line of text on a page would normally end for the current

ComponentOrientation

. Equal to SOUTHEAST for horizontal,
left-to-right orientations and SOUTHWEST for horizontal, right-to-left
orientations.

**See Also:**
- Constant Field Values

---

#### public static final int BASELINE

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered and
vertically aligned along the baseline of the prevailing row.
If the component does not have a baseline it will be vertically
centered.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final int BASELINE_LEADING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
aligned along the baseline of the prevailing row. If the
component does not have a baseline it will be vertically
centered.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final int BASELINE_TRAILING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is aligned along the baseline of the prevailing
row. If the component does not have a baseline it will be
vertically centered.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final int ABOVE_BASELINE

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final int ABOVE_BASELINE_LEADING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its bottom edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final int ABOVE_BASELINE_TRAILING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final int BELOW_BASELINE

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final int BELOW_BASELINE_LEADING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its top edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final int BELOW_BASELINE_TRAILING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public int gridx

Specifies the cell containing the leading edge of the component's
display area, where the first cell in a row has

gridx=0

.
The leading edge of a component's display area is its left edge for
a horizontal, left-to-right container and its right edge for a
horizontal, right-to-left container.
The value

RELATIVE

specifies that the component be placed
immediately following the component that was added to the container
just before this component was added.

The default value is

RELATIVE

.

gridx

should be a non-negative value.

**See Also:**
- clone()

,

gridy

,

ComponentOrientation

---

#### public int gridy

Specifies the cell at the top of the component's display area,
where the topmost cell has

gridy=0

. The value

RELATIVE

specifies that the component be placed just
below the component that was added to the container just before
this component was added.

The default value is

RELATIVE

.

gridy

should be a non-negative value.

**See Also:**
- clone()

,

gridx

---

#### public int gridwidth

Specifies the number of cells in a row for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridx

to the last
cell in the row.
Use

RELATIVE

to specify that the component's
display area will be from

gridx

to the next
to the last one in its row.

gridwidth

should be non-negative and the default
value is 1.

**See Also:**
- clone()

,

gridheight

---

#### public int gridheight

Specifies the number of cells in a column for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridy

to the last
cell in the column.
Use

RELATIVE

to specify that the component's
display area will be from

gridy

to the next
to the last one in its column.

gridheight

should be a non-negative value and the
default value is 1.

**See Also:**
- clone()

,

gridwidth

---

#### public double weightx

Specifies how to distribute extra horizontal space.

The grid bag layout manager calculates the weight of a column to
be the maximum

weightx

of all the components in a
column. If the resulting layout is smaller horizontally than the area
it needs to fill, the extra space is distributed to each column in
proportion to its weight. A column that has a weight of zero receives
no extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the left and right edges.

The default value of this field is

0

.

weightx

should be a non-negative value.

**See Also:**
- clone()

,

weighty

---

#### public double weighty

Specifies how to distribute extra vertical space.

The grid bag layout manager calculates the weight of a row to be
the maximum

weighty

of all the components in a row.
If the resulting layout is smaller vertically than the area it
needs to fill, the extra space is distributed to each row in
proportion to its weight. A row that has a weight of zero receives no
extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the top and bottom edges.

The default value of this field is

0

.

weighty

should be a non-negative value.

**See Also:**
- clone()

,

weightx

---

#### public int anchor

This field is used when the component is smaller than its
display area. It determines where, within the display area, to
place the component.

There are three kinds of possible values: orientation
relative, baseline relative and absolute. Orientation relative
values are interpreted relative to the container's component
orientation property, baseline relative values are interpreted
relative to the baseline and absolute values are not. The
absolute values are:

CENTER

,

NORTH

,

NORTHEAST

,

EAST

,

SOUTHEAST

,

SOUTH

,

SOUTHWEST

,

WEST

, and

NORTHWEST

.
The orientation relative values are:

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END

,

FIRST_LINE_START

,

FIRST_LINE_END

,

LAST_LINE_START

and

LAST_LINE_END

. The
baseline relative values are:

BASELINE

,

BASELINE_LEADING

,

BASELINE_TRAILING

,

ABOVE_BASELINE

,

ABOVE_BASELINE_LEADING

,

ABOVE_BASELINE_TRAILING

,

BELOW_BASELINE

,

BELOW_BASELINE_LEADING

,
and

BELOW_BASELINE_TRAILING

.
The default value is

CENTER

.

**See Also:**
- clone()

,

ComponentOrientation

---

#### public int fill

This field is used when the component's display area is larger
than the component's requested size. It determines whether to
resize the component, and if so, how.

The following values are valid for

fill

:

- NONE

: Do not resize the component.

HORIZONTAL

: Make the component wide enough to fill
its display area horizontally, but do not change its height.

VERTICAL

: Make the component tall enough to fill its
display area vertically, but do not change its width.

BOTH

: Make the component fill its display area
entirely.

The default value is

NONE

.

**See Also:**
- clone()

---

#### public
Insets
insets

This field specifies the external padding of the component, the
minimum amount of space between the component and the edges of its
display area.

The default value is

new Insets(0, 0, 0, 0)

.

**See Also:**
- clone()

---

#### public int ipadx

This field specifies the internal padding of the component, how much
space to add to the minimum width of the component. The width of
the component is at least its minimum width plus

ipadx

pixels.

The default value is

0

.

**See Also:**
- clone()

,

ipady

---

#### public int ipady

This field specifies the internal padding, that is, how much
space to add to the minimum height of the component. The height of
the component is at least its minimum height plus

ipady

pixels.

The default value is 0.

**See Also:**
- clone()

,

ipadx

---

### Constructor Details

#### public GridBagConstraints()

Creates a

GridBagConstraint

object with
all of its fields set to their default value.

---

#### public GridBagConstraints​(int gridx,
int gridy,
int gridwidth,
int gridheight,
double weightx,
double weighty,
int anchor,
int fill,

Insets
insets,
int ipadx,
int ipady)

Creates a

GridBagConstraints

object with
all of its fields set to the passed-in arguments.

Note: Because the use of this constructor hinders readability
of source code, this constructor should only be used by
automatic source code generation tools.

**Parameters:**
- gridx

- The initial gridx value.
- gridy

- The initial gridy value.
- gridwidth

- The initial gridwidth value.
- gridheight

- The initial gridheight value.
- weightx

- The initial weightx value.
- weighty

- The initial weighty value.
- anchor

- The initial anchor value.
- fill

- The initial fill value.
- insets

- The initial insets value.
- ipadx

- The initial ipadx value.
- ipady

- The initial ipady value.

**See Also:**
- gridx

,

gridy

,

gridwidth

,

gridheight

,

weightx

,

weighty

,

anchor

,

fill

,

insets

,

ipadx

,

ipady

**Since:**
- 1.2

---

### Method Details

#### public
Object
clone()

Creates a copy of this grid bag constraint.

**Overrides:**
- clone

in class

Object

**Returns:**
- a copy of this grid bag constraint

**See Also:**
- Cloneable

---

### Additional Sections

#### Class GridBagConstraints

java.lang.Object

- java.awt.GridBagConstraints

java.awt.GridBagConstraints

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
GridBagConstraints

extends
Object

implements
Cloneable
,
Serializable
```

The

GridBagConstraints

class specifies constraints
for components that are laid out using the

GridBagLayout

class.

**Since:** 1.0
**See Also:** GridBagLayout

,

Serialized Form

public class

GridBagConstraints

extends

Object

implements

Cloneable

,

Serializable

The

GridBagConstraints

class specifies constraints
for components that are laid out using the

GridBagLayout

class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ABOVE_BASELINE

Possible value for the

anchor

field.

static int

ABOVE_BASELINE_LEADING

Possible value for the

anchor

field.

static int

ABOVE_BASELINE_TRAILING

Possible value for the

anchor

field.

int

anchor

This field is used when the component is smaller than its
display area.

static int

BASELINE

Possible value for the

anchor

field.

static int

BASELINE_LEADING

Possible value for the

anchor

field.

static int

BASELINE_TRAILING

Possible value for the

anchor

field.

static int

BELOW_BASELINE

Possible value for the

anchor

field.

static int

BELOW_BASELINE_LEADING

Possible value for the

anchor

field.

static int

BELOW_BASELINE_TRAILING

Possible value for the

anchor

field.

static int

BOTH

Resize the component both horizontally and vertically.

static int

CENTER

Put the component in the center of its display area.

static int

EAST

Put the component on the right side of its display area,
centered vertically.

int

fill

This field is used when the component's display area is larger
than the component's requested size.

static int

FIRST_LINE_END

Place the component in the corner of its display area where
the first line of text on a page would normally end for the current

ComponentOrientation

.

static int

FIRST_LINE_START

Place the component in the corner of its display area where
the first line of text on a page would normally begin for the current

ComponentOrientation

.

int

gridheight

Specifies the number of cells in a column for the component's
display area.

int

gridwidth

Specifies the number of cells in a row for the component's
display area.

int

gridx

Specifies the cell containing the leading edge of the component's
display area, where the first cell in a row has

gridx=0

.

int

gridy

Specifies the cell at the top of the component's display area,
where the topmost cell has

gridy=0

.

static int

HORIZONTAL

Resize the component horizontally but not vertically.

Insets

insets

This field specifies the external padding of the component, the
minimum amount of space between the component and the edges of its
display area.

int

ipadx

This field specifies the internal padding of the component, how much
space to add to the minimum width of the component.

int

ipady

This field specifies the internal padding, that is, how much
space to add to the minimum height of the component.

static int

LAST_LINE_END

Place the component in the corner of its display area where
the last line of text on a page would normally end for the current

ComponentOrientation

.

static int

LAST_LINE_START

Place the component in the corner of its display area where
the last line of text on a page would normally start for the current

ComponentOrientation

.

static int

LINE_END

Place the component centered along the edge of its display area where
lines of text would normally end for the current

ComponentOrientation

.

static int

LINE_START

Place the component centered along the edge of its display area where
lines of text would normally begin for the current

ComponentOrientation

.

static int

NONE

Do not resize the component.

static int

NORTH

Put the component at the top of its display area,
centered horizontally.

static int

NORTHEAST

Put the component at the top-right corner of its display area.

static int

NORTHWEST

Put the component at the top-left corner of its display area.

static int

PAGE_END

Place the component centered along the edge of its display area
associated with the end of a page for the current

ComponentOrientation

.

static int

PAGE_START

Place the component centered along the edge of its display area
associated with the start of a page for the current

ComponentOrientation

.

static int

RELATIVE

Specifies that this component is the next-to-last component in its
column or row (

gridwidth

,

gridheight

),
or that this component be placed next to the previously added
component (

gridx

,

gridy

).

static int

REMAINDER

Specifies that this component is the
last component in its column or row.

static int

SOUTH

Put the component at the bottom of its display area, centered
horizontally.

static int

SOUTHEAST

Put the component at the bottom-right corner of its display area.

static int

SOUTHWEST

Put the component at the bottom-left corner of its display area.

static int

VERTICAL

Resize the component vertically but not horizontally.

double

weightx

Specifies how to distribute extra horizontal space.

double

weighty

Specifies how to distribute extra vertical space.

static int

WEST

Put the component on the left side of its display area,
centered vertically.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GridBagConstraints

()

Creates a

GridBagConstraint

object with
all of its fields set to their default value.

GridBagConstraints

​(int gridx,
int gridy,
int gridwidth,
int gridheight,
double weightx,
double weighty,
int anchor,
int fill,

Insets

insets,
int ipadx,
int ipady)

Creates a

GridBagConstraints

object with
all of its fields set to the passed-in arguments.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of this grid bag constraint.

- Methods declared in class java.lang.

Object

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

static int

ABOVE_BASELINE

Possible value for the

anchor

field.

static int

ABOVE_BASELINE_LEADING

Possible value for the

anchor

field.

static int

ABOVE_BASELINE_TRAILING

Possible value for the

anchor

field.

int

anchor

This field is used when the component is smaller than its
display area.

static int

BASELINE

Possible value for the

anchor

field.

static int

BASELINE_LEADING

Possible value for the

anchor

field.

static int

BASELINE_TRAILING

Possible value for the

anchor

field.

static int

BELOW_BASELINE

Possible value for the

anchor

field.

static int

BELOW_BASELINE_LEADING

Possible value for the

anchor

field.

static int

BELOW_BASELINE_TRAILING

Possible value for the

anchor

field.

static int

BOTH

Resize the component both horizontally and vertically.

static int

CENTER

Put the component in the center of its display area.

static int

EAST

Put the component on the right side of its display area,
centered vertically.

int

fill

This field is used when the component's display area is larger
than the component's requested size.

static int

FIRST_LINE_END

Place the component in the corner of its display area where
the first line of text on a page would normally end for the current

ComponentOrientation

.

static int

FIRST_LINE_START

Place the component in the corner of its display area where
the first line of text on a page would normally begin for the current

ComponentOrientation

.

int

gridheight

Specifies the number of cells in a column for the component's
display area.

int

gridwidth

Specifies the number of cells in a row for the component's
display area.

int

gridx

Specifies the cell containing the leading edge of the component's
display area, where the first cell in a row has

gridx=0

.

int

gridy

Specifies the cell at the top of the component's display area,
where the topmost cell has

gridy=0

.

static int

HORIZONTAL

Resize the component horizontally but not vertically.

Insets

insets

This field specifies the external padding of the component, the
minimum amount of space between the component and the edges of its
display area.

int

ipadx

This field specifies the internal padding of the component, how much
space to add to the minimum width of the component.

int

ipady

This field specifies the internal padding, that is, how much
space to add to the minimum height of the component.

static int

LAST_LINE_END

Place the component in the corner of its display area where
the last line of text on a page would normally end for the current

ComponentOrientation

.

static int

LAST_LINE_START

Place the component in the corner of its display area where
the last line of text on a page would normally start for the current

ComponentOrientation

.

static int

LINE_END

Place the component centered along the edge of its display area where
lines of text would normally end for the current

ComponentOrientation

.

static int

LINE_START

Place the component centered along the edge of its display area where
lines of text would normally begin for the current

ComponentOrientation

.

static int

NONE

Do not resize the component.

static int

NORTH

Put the component at the top of its display area,
centered horizontally.

static int

NORTHEAST

Put the component at the top-right corner of its display area.

static int

NORTHWEST

Put the component at the top-left corner of its display area.

static int

PAGE_END

Place the component centered along the edge of its display area
associated with the end of a page for the current

ComponentOrientation

.

static int

PAGE_START

Place the component centered along the edge of its display area
associated with the start of a page for the current

ComponentOrientation

.

static int

RELATIVE

Specifies that this component is the next-to-last component in its
column or row (

gridwidth

,

gridheight

),
or that this component be placed next to the previously added
component (

gridx

,

gridy

).

static int

REMAINDER

Specifies that this component is the
last component in its column or row.

static int

SOUTH

Put the component at the bottom of its display area, centered
horizontally.

static int

SOUTHEAST

Put the component at the bottom-right corner of its display area.

static int

SOUTHWEST

Put the component at the bottom-left corner of its display area.

static int

VERTICAL

Resize the component vertically but not horizontally.

double

weightx

Specifies how to distribute extra horizontal space.

double

weighty

Specifies how to distribute extra vertical space.

static int

WEST

Put the component on the left side of its display area,
centered vertically.

---

#### Field Summary

Possible value for the

anchor

field.

This field is used when the component is smaller than its
display area.

Resize the component both horizontally and vertically.

Put the component in the center of its display area.

Put the component on the right side of its display area,
centered vertically.

This field is used when the component's display area is larger
than the component's requested size.

Place the component in the corner of its display area where
the first line of text on a page would normally end for the current

ComponentOrientation

.

Place the component in the corner of its display area where
the first line of text on a page would normally begin for the current

ComponentOrientation

.

Specifies the number of cells in a column for the component's
display area.

Specifies the number of cells in a row for the component's
display area.

Specifies the cell containing the leading edge of the component's
display area, where the first cell in a row has

gridx=0

.

Specifies the cell at the top of the component's display area,
where the topmost cell has

gridy=0

.

Resize the component horizontally but not vertically.

This field specifies the external padding of the component, the
minimum amount of space between the component and the edges of its
display area.

This field specifies the internal padding of the component, how much
space to add to the minimum width of the component.

This field specifies the internal padding, that is, how much
space to add to the minimum height of the component.

Place the component in the corner of its display area where
the last line of text on a page would normally end for the current

ComponentOrientation

.

Place the component in the corner of its display area where
the last line of text on a page would normally start for the current

ComponentOrientation

.

Place the component centered along the edge of its display area where
lines of text would normally end for the current

ComponentOrientation

.

Place the component centered along the edge of its display area where
lines of text would normally begin for the current

ComponentOrientation

.

Do not resize the component.

Put the component at the top of its display area,
centered horizontally.

Put the component at the top-right corner of its display area.

Put the component at the top-left corner of its display area.

Place the component centered along the edge of its display area
associated with the end of a page for the current

ComponentOrientation

.

Place the component centered along the edge of its display area
associated with the start of a page for the current

ComponentOrientation

.

Specifies that this component is the next-to-last component in its
column or row (

gridwidth

,

gridheight

),
or that this component be placed next to the previously added
component (

gridx

,

gridy

).

Specifies that this component is the
last component in its column or row.

Put the component at the bottom of its display area, centered
horizontally.

Put the component at the bottom-right corner of its display area.

Put the component at the bottom-left corner of its display area.

Resize the component vertically but not horizontally.

Specifies how to distribute extra horizontal space.

Specifies how to distribute extra vertical space.

Put the component on the left side of its display area,
centered vertically.

Constructor Summary

Constructors

Constructor

Description

GridBagConstraints

()

Creates a

GridBagConstraint

object with
all of its fields set to their default value.

GridBagConstraints

​(int gridx,
int gridy,
int gridwidth,
int gridheight,
double weightx,
double weighty,
int anchor,
int fill,

Insets

insets,
int ipadx,
int ipady)

Creates a

GridBagConstraints

object with
all of its fields set to the passed-in arguments.

---

#### Constructor Summary

Creates a

GridBagConstraint

object with
all of its fields set to their default value.

Creates a

GridBagConstraints

object with
all of its fields set to the passed-in arguments.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of this grid bag constraint.

- Methods declared in class java.lang.

Object

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

Creates a copy of this grid bag constraint.

Methods declared in class java.lang.

Object

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

- RELATIVE

```java
public static final int RELATIVE
```

Specifies that this component is the next-to-last component in its
column or row (

gridwidth

,

gridheight

),
or that this component be placed next to the previously added
component (

gridx

,

gridy

).

**See Also:** gridwidth

,

gridheight

,

gridx

,

gridy

,

Constant Field Values

- REMAINDER

```java
public static final int REMAINDER
```

Specifies that this component is the
last component in its column or row.

**See Also:** Constant Field Values

- NONE

```java
public static final int NONE
```

Do not resize the component.

**See Also:** Constant Field Values

- BOTH

```java
public static final int BOTH
```

Resize the component both horizontally and vertically.

**See Also:** Constant Field Values

- HORIZONTAL

```java
public static final int HORIZONTAL
```

Resize the component horizontally but not vertically.

**See Also:** Constant Field Values

- VERTICAL

```java
public static final int VERTICAL
```

Resize the component vertically but not horizontally.

**See Also:** Constant Field Values

- CENTER

```java
public static final int CENTER
```

Put the component in the center of its display area.

**See Also:** Constant Field Values

- NORTH

```java
public static final int NORTH
```

Put the component at the top of its display area,
centered horizontally.

**See Also:** Constant Field Values

- NORTHEAST

```java
public static final int NORTHEAST
```

Put the component at the top-right corner of its display area.

**See Also:** Constant Field Values

- EAST

```java
public static final int EAST
```

Put the component on the right side of its display area,
centered vertically.

**See Also:** Constant Field Values

- SOUTHEAST

```java
public static final int SOUTHEAST
```

Put the component at the bottom-right corner of its display area.

**See Also:** Constant Field Values

- SOUTH

```java
public static final int SOUTH
```

Put the component at the bottom of its display area, centered
horizontally.

**See Also:** Constant Field Values

- SOUTHWEST

```java
public static final int SOUTHWEST
```

Put the component at the bottom-left corner of its display area.

**See Also:** Constant Field Values

- WEST

```java
public static final int WEST
```

Put the component on the left side of its display area,
centered vertically.

**See Also:** Constant Field Values

- NORTHWEST

```java
public static final int NORTHWEST
```

Put the component at the top-left corner of its display area.

**See Also:** Constant Field Values

- PAGE_START

```java
public static final int PAGE_START
```

Place the component centered along the edge of its display area
associated with the start of a page for the current

ComponentOrientation

. Equal to NORTH for horizontal
orientations.

**See Also:** Constant Field Values

- PAGE_END

```java
public static final int PAGE_END
```

Place the component centered along the edge of its display area
associated with the end of a page for the current

ComponentOrientation

. Equal to SOUTH for horizontal
orientations.

**See Also:** Constant Field Values

- LINE_START

```java
public static final int LINE_START
```

Place the component centered along the edge of its display area where
lines of text would normally begin for the current

ComponentOrientation

. Equal to WEST for horizontal,
left-to-right orientations and EAST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- LINE_END

```java
public static final int LINE_END
```

Place the component centered along the edge of its display area where
lines of text would normally end for the current

ComponentOrientation

. Equal to EAST for horizontal,
left-to-right orientations and WEST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- FIRST_LINE_START

```java
public static final int FIRST_LINE_START
```

Place the component in the corner of its display area where
the first line of text on a page would normally begin for the current

ComponentOrientation

. Equal to NORTHWEST for horizontal,
left-to-right orientations and NORTHEAST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- FIRST_LINE_END

```java
public static final int FIRST_LINE_END
```

Place the component in the corner of its display area where
the first line of text on a page would normally end for the current

ComponentOrientation

. Equal to NORTHEAST for horizontal,
left-to-right orientations and NORTHWEST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- LAST_LINE_START

```java
public static final int LAST_LINE_START
```

Place the component in the corner of its display area where
the last line of text on a page would normally start for the current

ComponentOrientation

. Equal to SOUTHWEST for horizontal,
left-to-right orientations and SOUTHEAST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- LAST_LINE_END

```java
public static final int LAST_LINE_END
```

Place the component in the corner of its display area where
the last line of text on a page would normally end for the current

ComponentOrientation

. Equal to SOUTHEAST for horizontal,
left-to-right orientations and SOUTHWEST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- BASELINE

```java
public static final int BASELINE
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered and
vertically aligned along the baseline of the prevailing row.
If the component does not have a baseline it will be vertically
centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BASELINE_LEADING

```java
public static final int BASELINE_LEADING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
aligned along the baseline of the prevailing row. If the
component does not have a baseline it will be vertically
centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BASELINE_TRAILING

```java
public static final int BASELINE_TRAILING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is aligned along the baseline of the prevailing
row. If the component does not have a baseline it will be
vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- ABOVE_BASELINE

```java
public static final int ABOVE_BASELINE
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- ABOVE_BASELINE_LEADING

```java
public static final int ABOVE_BASELINE_LEADING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its bottom edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- ABOVE_BASELINE_TRAILING

```java
public static final int ABOVE_BASELINE_TRAILING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BELOW_BASELINE

```java
public static final int BELOW_BASELINE
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BELOW_BASELINE_LEADING

```java
public static final int BELOW_BASELINE_LEADING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its top edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BELOW_BASELINE_TRAILING

```java
public static final int BELOW_BASELINE_TRAILING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- gridx

```java
public int gridx
```

Specifies the cell containing the leading edge of the component's
display area, where the first cell in a row has

gridx=0

.
The leading edge of a component's display area is its left edge for
a horizontal, left-to-right container and its right edge for a
horizontal, right-to-left container.
The value

RELATIVE

specifies that the component be placed
immediately following the component that was added to the container
just before this component was added.

The default value is

RELATIVE

.

gridx

should be a non-negative value.

**See Also:** clone()

,

gridy

,

ComponentOrientation

- gridy

```java
public int gridy
```

Specifies the cell at the top of the component's display area,
where the topmost cell has

gridy=0

. The value

RELATIVE

specifies that the component be placed just
below the component that was added to the container just before
this component was added.

The default value is

RELATIVE

.

gridy

should be a non-negative value.

**See Also:** clone()

,

gridx

- gridwidth

```java
public int gridwidth
```

Specifies the number of cells in a row for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridx

to the last
cell in the row.
Use

RELATIVE

to specify that the component's
display area will be from

gridx

to the next
to the last one in its row.

gridwidth

should be non-negative and the default
value is 1.

**See Also:** clone()

,

gridheight

- gridheight

```java
public int gridheight
```

Specifies the number of cells in a column for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridy

to the last
cell in the column.
Use

RELATIVE

to specify that the component's
display area will be from

gridy

to the next
to the last one in its column.

gridheight

should be a non-negative value and the
default value is 1.

**See Also:** clone()

,

gridwidth

- weightx

```java
public double weightx
```

Specifies how to distribute extra horizontal space.

The grid bag layout manager calculates the weight of a column to
be the maximum

weightx

of all the components in a
column. If the resulting layout is smaller horizontally than the area
it needs to fill, the extra space is distributed to each column in
proportion to its weight. A column that has a weight of zero receives
no extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the left and right edges.

The default value of this field is

0

.

weightx

should be a non-negative value.

**See Also:** clone()

,

weighty

- weighty

```java
public double weighty
```

Specifies how to distribute extra vertical space.

The grid bag layout manager calculates the weight of a row to be
the maximum

weighty

of all the components in a row.
If the resulting layout is smaller vertically than the area it
needs to fill, the extra space is distributed to each row in
proportion to its weight. A row that has a weight of zero receives no
extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the top and bottom edges.

The default value of this field is

0

.

weighty

should be a non-negative value.

**See Also:** clone()

,

weightx

- anchor

```java
public int anchor
```

This field is used when the component is smaller than its
display area. It determines where, within the display area, to
place the component.

There are three kinds of possible values: orientation
relative, baseline relative and absolute. Orientation relative
values are interpreted relative to the container's component
orientation property, baseline relative values are interpreted
relative to the baseline and absolute values are not. The
absolute values are:

CENTER

,

NORTH

,

NORTHEAST

,

EAST

,

SOUTHEAST

,

SOUTH

,

SOUTHWEST

,

WEST

, and

NORTHWEST

.
The orientation relative values are:

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END

,

FIRST_LINE_START

,

FIRST_LINE_END

,

LAST_LINE_START

and

LAST_LINE_END

. The
baseline relative values are:

BASELINE

,

BASELINE_LEADING

,

BASELINE_TRAILING

,

ABOVE_BASELINE

,

ABOVE_BASELINE_LEADING

,

ABOVE_BASELINE_TRAILING

,

BELOW_BASELINE

,

BELOW_BASELINE_LEADING

,
and

BELOW_BASELINE_TRAILING

.
The default value is

CENTER

.

**See Also:** clone()

,

ComponentOrientation

- fill

```java
public int fill
```

This field is used when the component's display area is larger
than the component's requested size. It determines whether to
resize the component, and if so, how.

The following values are valid for

fill

:

- NONE

: Do not resize the component.

HORIZONTAL

: Make the component wide enough to fill
its display area horizontally, but do not change its height.

VERTICAL

: Make the component tall enough to fill its
display area vertically, but do not change its width.

BOTH

: Make the component fill its display area
entirely.

The default value is

NONE

.

**See Also:** clone()

- insets

```java
public
Insets
insets
```

This field specifies the external padding of the component, the
minimum amount of space between the component and the edges of its
display area.

The default value is

new Insets(0, 0, 0, 0)

.

**See Also:** clone()

- ipadx

```java
public int ipadx
```

This field specifies the internal padding of the component, how much
space to add to the minimum width of the component. The width of
the component is at least its minimum width plus

ipadx

pixels.

The default value is

0

.

**See Also:** clone()

,

ipady

- ipady

```java
public int ipady
```

This field specifies the internal padding, that is, how much
space to add to the minimum height of the component. The height of
the component is at least its minimum height plus

ipady

pixels.

The default value is 0.

**See Also:** clone()

,

ipadx

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GridBagConstraints

```java
public GridBagConstraints()
```

Creates a

GridBagConstraint

object with
all of its fields set to their default value.

- GridBagConstraints

```java
public GridBagConstraints​(int gridx,
int gridy,
int gridwidth,
int gridheight,
double weightx,
double weighty,
int anchor,
int fill,

Insets
insets,
int ipadx,
int ipady)
```

Creates a

GridBagConstraints

object with
all of its fields set to the passed-in arguments.

Note: Because the use of this constructor hinders readability
of source code, this constructor should only be used by
automatic source code generation tools.

**Parameters:** gridx

- The initial gridx value.
**Parameters:** gridy

- The initial gridy value.
**Parameters:** gridwidth

- The initial gridwidth value.
**Parameters:** gridheight

- The initial gridheight value.
**Parameters:** weightx

- The initial weightx value.
**Parameters:** weighty

- The initial weighty value.
**Parameters:** anchor

- The initial anchor value.
**Parameters:** fill

- The initial fill value.
**Parameters:** insets

- The initial insets value.
**Parameters:** ipadx

- The initial ipadx value.
**Parameters:** ipady

- The initial ipady value.
**Since:** 1.2
**See Also:** gridx

,

gridy

,

gridwidth

,

gridheight

,

weightx

,

weighty

,

anchor

,

fill

,

insets

,

ipadx

,

ipady

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Creates a copy of this grid bag constraint.

**Overrides:** clone

in class

Object
**Returns:** a copy of this grid bag constraint
**See Also:** Cloneable

Field Detail

- RELATIVE

```java
public static final int RELATIVE
```

Specifies that this component is the next-to-last component in its
column or row (

gridwidth

,

gridheight

),
or that this component be placed next to the previously added
component (

gridx

,

gridy

).

**See Also:** gridwidth

,

gridheight

,

gridx

,

gridy

,

Constant Field Values

- REMAINDER

```java
public static final int REMAINDER
```

Specifies that this component is the
last component in its column or row.

**See Also:** Constant Field Values

- NONE

```java
public static final int NONE
```

Do not resize the component.

**See Also:** Constant Field Values

- BOTH

```java
public static final int BOTH
```

Resize the component both horizontally and vertically.

**See Also:** Constant Field Values

- HORIZONTAL

```java
public static final int HORIZONTAL
```

Resize the component horizontally but not vertically.

**See Also:** Constant Field Values

- VERTICAL

```java
public static final int VERTICAL
```

Resize the component vertically but not horizontally.

**See Also:** Constant Field Values

- CENTER

```java
public static final int CENTER
```

Put the component in the center of its display area.

**See Also:** Constant Field Values

- NORTH

```java
public static final int NORTH
```

Put the component at the top of its display area,
centered horizontally.

**See Also:** Constant Field Values

- NORTHEAST

```java
public static final int NORTHEAST
```

Put the component at the top-right corner of its display area.

**See Also:** Constant Field Values

- EAST

```java
public static final int EAST
```

Put the component on the right side of its display area,
centered vertically.

**See Also:** Constant Field Values

- SOUTHEAST

```java
public static final int SOUTHEAST
```

Put the component at the bottom-right corner of its display area.

**See Also:** Constant Field Values

- SOUTH

```java
public static final int SOUTH
```

Put the component at the bottom of its display area, centered
horizontally.

**See Also:** Constant Field Values

- SOUTHWEST

```java
public static final int SOUTHWEST
```

Put the component at the bottom-left corner of its display area.

**See Also:** Constant Field Values

- WEST

```java
public static final int WEST
```

Put the component on the left side of its display area,
centered vertically.

**See Also:** Constant Field Values

- NORTHWEST

```java
public static final int NORTHWEST
```

Put the component at the top-left corner of its display area.

**See Also:** Constant Field Values

- PAGE_START

```java
public static final int PAGE_START
```

Place the component centered along the edge of its display area
associated with the start of a page for the current

ComponentOrientation

. Equal to NORTH for horizontal
orientations.

**See Also:** Constant Field Values

- PAGE_END

```java
public static final int PAGE_END
```

Place the component centered along the edge of its display area
associated with the end of a page for the current

ComponentOrientation

. Equal to SOUTH for horizontal
orientations.

**See Also:** Constant Field Values

- LINE_START

```java
public static final int LINE_START
```

Place the component centered along the edge of its display area where
lines of text would normally begin for the current

ComponentOrientation

. Equal to WEST for horizontal,
left-to-right orientations and EAST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- LINE_END

```java
public static final int LINE_END
```

Place the component centered along the edge of its display area where
lines of text would normally end for the current

ComponentOrientation

. Equal to EAST for horizontal,
left-to-right orientations and WEST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- FIRST_LINE_START

```java
public static final int FIRST_LINE_START
```

Place the component in the corner of its display area where
the first line of text on a page would normally begin for the current

ComponentOrientation

. Equal to NORTHWEST for horizontal,
left-to-right orientations and NORTHEAST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- FIRST_LINE_END

```java
public static final int FIRST_LINE_END
```

Place the component in the corner of its display area where
the first line of text on a page would normally end for the current

ComponentOrientation

. Equal to NORTHEAST for horizontal,
left-to-right orientations and NORTHWEST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- LAST_LINE_START

```java
public static final int LAST_LINE_START
```

Place the component in the corner of its display area where
the last line of text on a page would normally start for the current

ComponentOrientation

. Equal to SOUTHWEST for horizontal,
left-to-right orientations and SOUTHEAST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- LAST_LINE_END

```java
public static final int LAST_LINE_END
```

Place the component in the corner of its display area where
the last line of text on a page would normally end for the current

ComponentOrientation

. Equal to SOUTHEAST for horizontal,
left-to-right orientations and SOUTHWEST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

- BASELINE

```java
public static final int BASELINE
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered and
vertically aligned along the baseline of the prevailing row.
If the component does not have a baseline it will be vertically
centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BASELINE_LEADING

```java
public static final int BASELINE_LEADING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
aligned along the baseline of the prevailing row. If the
component does not have a baseline it will be vertically
centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BASELINE_TRAILING

```java
public static final int BASELINE_TRAILING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is aligned along the baseline of the prevailing
row. If the component does not have a baseline it will be
vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- ABOVE_BASELINE

```java
public static final int ABOVE_BASELINE
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- ABOVE_BASELINE_LEADING

```java
public static final int ABOVE_BASELINE_LEADING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its bottom edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- ABOVE_BASELINE_TRAILING

```java
public static final int ABOVE_BASELINE_TRAILING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BELOW_BASELINE

```java
public static final int BELOW_BASELINE
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BELOW_BASELINE_LEADING

```java
public static final int BELOW_BASELINE_LEADING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its top edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- BELOW_BASELINE_TRAILING

```java
public static final int BELOW_BASELINE_TRAILING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

- gridx

```java
public int gridx
```

Specifies the cell containing the leading edge of the component's
display area, where the first cell in a row has

gridx=0

.
The leading edge of a component's display area is its left edge for
a horizontal, left-to-right container and its right edge for a
horizontal, right-to-left container.
The value

RELATIVE

specifies that the component be placed
immediately following the component that was added to the container
just before this component was added.

The default value is

RELATIVE

.

gridx

should be a non-negative value.

**See Also:** clone()

,

gridy

,

ComponentOrientation

- gridy

```java
public int gridy
```

Specifies the cell at the top of the component's display area,
where the topmost cell has

gridy=0

. The value

RELATIVE

specifies that the component be placed just
below the component that was added to the container just before
this component was added.

The default value is

RELATIVE

.

gridy

should be a non-negative value.

**See Also:** clone()

,

gridx

- gridwidth

```java
public int gridwidth
```

Specifies the number of cells in a row for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridx

to the last
cell in the row.
Use

RELATIVE

to specify that the component's
display area will be from

gridx

to the next
to the last one in its row.

gridwidth

should be non-negative and the default
value is 1.

**See Also:** clone()

,

gridheight

- gridheight

```java
public int gridheight
```

Specifies the number of cells in a column for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridy

to the last
cell in the column.
Use

RELATIVE

to specify that the component's
display area will be from

gridy

to the next
to the last one in its column.

gridheight

should be a non-negative value and the
default value is 1.

**See Also:** clone()

,

gridwidth

- weightx

```java
public double weightx
```

Specifies how to distribute extra horizontal space.

The grid bag layout manager calculates the weight of a column to
be the maximum

weightx

of all the components in a
column. If the resulting layout is smaller horizontally than the area
it needs to fill, the extra space is distributed to each column in
proportion to its weight. A column that has a weight of zero receives
no extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the left and right edges.

The default value of this field is

0

.

weightx

should be a non-negative value.

**See Also:** clone()

,

weighty

- weighty

```java
public double weighty
```

Specifies how to distribute extra vertical space.

The grid bag layout manager calculates the weight of a row to be
the maximum

weighty

of all the components in a row.
If the resulting layout is smaller vertically than the area it
needs to fill, the extra space is distributed to each row in
proportion to its weight. A row that has a weight of zero receives no
extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the top and bottom edges.

The default value of this field is

0

.

weighty

should be a non-negative value.

**See Also:** clone()

,

weightx

- anchor

```java
public int anchor
```

This field is used when the component is smaller than its
display area. It determines where, within the display area, to
place the component.

There are three kinds of possible values: orientation
relative, baseline relative and absolute. Orientation relative
values are interpreted relative to the container's component
orientation property, baseline relative values are interpreted
relative to the baseline and absolute values are not. The
absolute values are:

CENTER

,

NORTH

,

NORTHEAST

,

EAST

,

SOUTHEAST

,

SOUTH

,

SOUTHWEST

,

WEST

, and

NORTHWEST

.
The orientation relative values are:

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END

,

FIRST_LINE_START

,

FIRST_LINE_END

,

LAST_LINE_START

and

LAST_LINE_END

. The
baseline relative values are:

BASELINE

,

BASELINE_LEADING

,

BASELINE_TRAILING

,

ABOVE_BASELINE

,

ABOVE_BASELINE_LEADING

,

ABOVE_BASELINE_TRAILING

,

BELOW_BASELINE

,

BELOW_BASELINE_LEADING

,
and

BELOW_BASELINE_TRAILING

.
The default value is

CENTER

.

**See Also:** clone()

,

ComponentOrientation

- fill

```java
public int fill
```

This field is used when the component's display area is larger
than the component's requested size. It determines whether to
resize the component, and if so, how.

The following values are valid for

fill

:

- NONE

: Do not resize the component.

HORIZONTAL

: Make the component wide enough to fill
its display area horizontally, but do not change its height.

VERTICAL

: Make the component tall enough to fill its
display area vertically, but do not change its width.

BOTH

: Make the component fill its display area
entirely.

The default value is

NONE

.

**See Also:** clone()

- insets

```java
public
Insets
insets
```

This field specifies the external padding of the component, the
minimum amount of space between the component and the edges of its
display area.

The default value is

new Insets(0, 0, 0, 0)

.

**See Also:** clone()

- ipadx

```java
public int ipadx
```

This field specifies the internal padding of the component, how much
space to add to the minimum width of the component. The width of
the component is at least its minimum width plus

ipadx

pixels.

The default value is

0

.

**See Also:** clone()

,

ipady

- ipady

```java
public int ipady
```

This field specifies the internal padding, that is, how much
space to add to the minimum height of the component. The height of
the component is at least its minimum height plus

ipady

pixels.

The default value is 0.

**See Also:** clone()

,

ipadx

---

#### Field Detail

RELATIVE

```java
public static final int RELATIVE
```

Specifies that this component is the next-to-last component in its
column or row (

gridwidth

,

gridheight

),
or that this component be placed next to the previously added
component (

gridx

,

gridy

).

**See Also:** gridwidth

,

gridheight

,

gridx

,

gridy

,

Constant Field Values

---

#### RELATIVE

public static final int RELATIVE

Specifies that this component is the next-to-last component in its
column or row (

gridwidth

,

gridheight

),
or that this component be placed next to the previously added
component (

gridx

,

gridy

).

REMAINDER

```java
public static final int REMAINDER
```

Specifies that this component is the
last component in its column or row.

**See Also:** Constant Field Values

---

#### REMAINDER

public static final int REMAINDER

Specifies that this component is the
last component in its column or row.

NONE

```java
public static final int NONE
```

Do not resize the component.

**See Also:** Constant Field Values

---

#### NONE

public static final int NONE

Do not resize the component.

BOTH

```java
public static final int BOTH
```

Resize the component both horizontally and vertically.

**See Also:** Constant Field Values

---

#### BOTH

public static final int BOTH

Resize the component both horizontally and vertically.

HORIZONTAL

```java
public static final int HORIZONTAL
```

Resize the component horizontally but not vertically.

**See Also:** Constant Field Values

---

#### HORIZONTAL

public static final int HORIZONTAL

Resize the component horizontally but not vertically.

VERTICAL

```java
public static final int VERTICAL
```

Resize the component vertically but not horizontally.

**See Also:** Constant Field Values

---

#### VERTICAL

public static final int VERTICAL

Resize the component vertically but not horizontally.

CENTER

```java
public static final int CENTER
```

Put the component in the center of its display area.

**See Also:** Constant Field Values

---

#### CENTER

public static final int CENTER

Put the component in the center of its display area.

NORTH

```java
public static final int NORTH
```

Put the component at the top of its display area,
centered horizontally.

**See Also:** Constant Field Values

---

#### NORTH

public static final int NORTH

Put the component at the top of its display area,
centered horizontally.

NORTHEAST

```java
public static final int NORTHEAST
```

Put the component at the top-right corner of its display area.

**See Also:** Constant Field Values

---

#### NORTHEAST

public static final int NORTHEAST

Put the component at the top-right corner of its display area.

EAST

```java
public static final int EAST
```

Put the component on the right side of its display area,
centered vertically.

**See Also:** Constant Field Values

---

#### EAST

public static final int EAST

Put the component on the right side of its display area,
centered vertically.

SOUTHEAST

```java
public static final int SOUTHEAST
```

Put the component at the bottom-right corner of its display area.

**See Also:** Constant Field Values

---

#### SOUTHEAST

public static final int SOUTHEAST

Put the component at the bottom-right corner of its display area.

SOUTH

```java
public static final int SOUTH
```

Put the component at the bottom of its display area, centered
horizontally.

**See Also:** Constant Field Values

---

#### SOUTH

public static final int SOUTH

Put the component at the bottom of its display area, centered
horizontally.

SOUTHWEST

```java
public static final int SOUTHWEST
```

Put the component at the bottom-left corner of its display area.

**See Also:** Constant Field Values

---

#### SOUTHWEST

public static final int SOUTHWEST

Put the component at the bottom-left corner of its display area.

WEST

```java
public static final int WEST
```

Put the component on the left side of its display area,
centered vertically.

**See Also:** Constant Field Values

---

#### WEST

public static final int WEST

Put the component on the left side of its display area,
centered vertically.

NORTHWEST

```java
public static final int NORTHWEST
```

Put the component at the top-left corner of its display area.

**See Also:** Constant Field Values

---

#### NORTHWEST

public static final int NORTHWEST

Put the component at the top-left corner of its display area.

PAGE_START

```java
public static final int PAGE_START
```

Place the component centered along the edge of its display area
associated with the start of a page for the current

ComponentOrientation

. Equal to NORTH for horizontal
orientations.

**See Also:** Constant Field Values

---

#### PAGE_START

public static final int PAGE_START

Place the component centered along the edge of its display area
associated with the start of a page for the current

ComponentOrientation

. Equal to NORTH for horizontal
orientations.

PAGE_END

```java
public static final int PAGE_END
```

Place the component centered along the edge of its display area
associated with the end of a page for the current

ComponentOrientation

. Equal to SOUTH for horizontal
orientations.

**See Also:** Constant Field Values

---

#### PAGE_END

public static final int PAGE_END

Place the component centered along the edge of its display area
associated with the end of a page for the current

ComponentOrientation

. Equal to SOUTH for horizontal
orientations.

LINE_START

```java
public static final int LINE_START
```

Place the component centered along the edge of its display area where
lines of text would normally begin for the current

ComponentOrientation

. Equal to WEST for horizontal,
left-to-right orientations and EAST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

---

#### LINE_START

public static final int LINE_START

Place the component centered along the edge of its display area where
lines of text would normally begin for the current

ComponentOrientation

. Equal to WEST for horizontal,
left-to-right orientations and EAST for horizontal, right-to-left
orientations.

LINE_END

```java
public static final int LINE_END
```

Place the component centered along the edge of its display area where
lines of text would normally end for the current

ComponentOrientation

. Equal to EAST for horizontal,
left-to-right orientations and WEST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

---

#### LINE_END

public static final int LINE_END

Place the component centered along the edge of its display area where
lines of text would normally end for the current

ComponentOrientation

. Equal to EAST for horizontal,
left-to-right orientations and WEST for horizontal, right-to-left
orientations.

FIRST_LINE_START

```java
public static final int FIRST_LINE_START
```

Place the component in the corner of its display area where
the first line of text on a page would normally begin for the current

ComponentOrientation

. Equal to NORTHWEST for horizontal,
left-to-right orientations and NORTHEAST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

---

#### FIRST_LINE_START

public static final int FIRST_LINE_START

Place the component in the corner of its display area where
the first line of text on a page would normally begin for the current

ComponentOrientation

. Equal to NORTHWEST for horizontal,
left-to-right orientations and NORTHEAST for horizontal, right-to-left
orientations.

FIRST_LINE_END

```java
public static final int FIRST_LINE_END
```

Place the component in the corner of its display area where
the first line of text on a page would normally end for the current

ComponentOrientation

. Equal to NORTHEAST for horizontal,
left-to-right orientations and NORTHWEST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

---

#### FIRST_LINE_END

public static final int FIRST_LINE_END

Place the component in the corner of its display area where
the first line of text on a page would normally end for the current

ComponentOrientation

. Equal to NORTHEAST for horizontal,
left-to-right orientations and NORTHWEST for horizontal, right-to-left
orientations.

LAST_LINE_START

```java
public static final int LAST_LINE_START
```

Place the component in the corner of its display area where
the last line of text on a page would normally start for the current

ComponentOrientation

. Equal to SOUTHWEST for horizontal,
left-to-right orientations and SOUTHEAST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

---

#### LAST_LINE_START

public static final int LAST_LINE_START

Place the component in the corner of its display area where
the last line of text on a page would normally start for the current

ComponentOrientation

. Equal to SOUTHWEST for horizontal,
left-to-right orientations and SOUTHEAST for horizontal, right-to-left
orientations.

LAST_LINE_END

```java
public static final int LAST_LINE_END
```

Place the component in the corner of its display area where
the last line of text on a page would normally end for the current

ComponentOrientation

. Equal to SOUTHEAST for horizontal,
left-to-right orientations and SOUTHWEST for horizontal, right-to-left
orientations.

**See Also:** Constant Field Values

---

#### LAST_LINE_END

public static final int LAST_LINE_END

Place the component in the corner of its display area where
the last line of text on a page would normally end for the current

ComponentOrientation

. Equal to SOUTHEAST for horizontal,
left-to-right orientations and SOUTHWEST for horizontal, right-to-left
orientations.

BASELINE

```java
public static final int BASELINE
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered and
vertically aligned along the baseline of the prevailing row.
If the component does not have a baseline it will be vertically
centered.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### BASELINE

public static final int BASELINE

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered and
vertically aligned along the baseline of the prevailing row.
If the component does not have a baseline it will be vertically
centered.

BASELINE_LEADING

```java
public static final int BASELINE_LEADING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
aligned along the baseline of the prevailing row. If the
component does not have a baseline it will be vertically
centered.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### BASELINE_LEADING

public static final int BASELINE_LEADING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
aligned along the baseline of the prevailing row. If the
component does not have a baseline it will be vertically
centered.

BASELINE_TRAILING

```java
public static final int BASELINE_TRAILING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is aligned along the baseline of the prevailing
row. If the component does not have a baseline it will be
vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### BASELINE_TRAILING

public static final int BASELINE_TRAILING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is aligned along the baseline of the prevailing
row. If the component does not have a baseline it will be
vertically centered.

ABOVE_BASELINE

```java
public static final int ABOVE_BASELINE
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### ABOVE_BASELINE

public static final int ABOVE_BASELINE

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

ABOVE_BASELINE_LEADING

```java
public static final int ABOVE_BASELINE_LEADING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its bottom edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### ABOVE_BASELINE_LEADING

public static final int ABOVE_BASELINE_LEADING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its bottom edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

ABOVE_BASELINE_TRAILING

```java
public static final int ABOVE_BASELINE_TRAILING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### ABOVE_BASELINE_TRAILING

public static final int ABOVE_BASELINE_TRAILING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its bottom edge touches
the baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

BELOW_BASELINE

```java
public static final int BELOW_BASELINE
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### BELOW_BASELINE

public static final int BELOW_BASELINE

Possible value for the

anchor

field. Specifies
that the component should be horizontally centered. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

BELOW_BASELINE_LEADING

```java
public static final int BELOW_BASELINE_LEADING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its top edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### BELOW_BASELINE_LEADING

public static final int BELOW_BASELINE_LEADING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
leading edge. For components with a left-to-right orientation,
the leading edge is the left edge. Vertically the component is
positioned so that its top edge touches the baseline of the
starting row. If the starting row does not have a baseline it
will be vertically centered.

BELOW_BASELINE_TRAILING

```java
public static final int BELOW_BASELINE_TRAILING
```

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### BELOW_BASELINE_TRAILING

public static final int BELOW_BASELINE_TRAILING

Possible value for the

anchor

field. Specifies
that the component should be horizontally placed along the
trailing edge. For components with a left-to-right
orientation, the trailing edge is the right edge. Vertically
the component is positioned so that its top edge touches the
baseline of the starting row. If the starting row does not
have a baseline it will be vertically centered.

gridx

```java
public int gridx
```

Specifies the cell containing the leading edge of the component's
display area, where the first cell in a row has

gridx=0

.
The leading edge of a component's display area is its left edge for
a horizontal, left-to-right container and its right edge for a
horizontal, right-to-left container.
The value

RELATIVE

specifies that the component be placed
immediately following the component that was added to the container
just before this component was added.

The default value is

RELATIVE

.

gridx

should be a non-negative value.

**See Also:** clone()

,

gridy

,

ComponentOrientation

---

#### gridx

public int gridx

Specifies the cell containing the leading edge of the component's
display area, where the first cell in a row has

gridx=0

.
The leading edge of a component's display area is its left edge for
a horizontal, left-to-right container and its right edge for a
horizontal, right-to-left container.
The value

RELATIVE

specifies that the component be placed
immediately following the component that was added to the container
just before this component was added.

The default value is

RELATIVE

.

gridx

should be a non-negative value.

The default value is

RELATIVE

.

gridx

should be a non-negative value.

gridy

```java
public int gridy
```

Specifies the cell at the top of the component's display area,
where the topmost cell has

gridy=0

. The value

RELATIVE

specifies that the component be placed just
below the component that was added to the container just before
this component was added.

The default value is

RELATIVE

.

gridy

should be a non-negative value.

**See Also:** clone()

,

gridx

---

#### gridy

public int gridy

Specifies the cell at the top of the component's display area,
where the topmost cell has

gridy=0

. The value

RELATIVE

specifies that the component be placed just
below the component that was added to the container just before
this component was added.

The default value is

RELATIVE

.

gridy

should be a non-negative value.

The default value is

RELATIVE

.

gridy

should be a non-negative value.

gridwidth

```java
public int gridwidth
```

Specifies the number of cells in a row for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridx

to the last
cell in the row.
Use

RELATIVE

to specify that the component's
display area will be from

gridx

to the next
to the last one in its row.

gridwidth

should be non-negative and the default
value is 1.

**See Also:** clone()

,

gridheight

---

#### gridwidth

public int gridwidth

Specifies the number of cells in a row for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridx

to the last
cell in the row.
Use

RELATIVE

to specify that the component's
display area will be from

gridx

to the next
to the last one in its row.

gridwidth

should be non-negative and the default
value is 1.

Use

REMAINDER

to specify that the component's
display area will be from

gridx

to the last
cell in the row.
Use

RELATIVE

to specify that the component's
display area will be from

gridx

to the next
to the last one in its row.

gridwidth

should be non-negative and the default
value is 1.

gridwidth

should be non-negative and the default
value is 1.

gridheight

```java
public int gridheight
```

Specifies the number of cells in a column for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridy

to the last
cell in the column.
Use

RELATIVE

to specify that the component's
display area will be from

gridy

to the next
to the last one in its column.

gridheight

should be a non-negative value and the
default value is 1.

**See Also:** clone()

,

gridwidth

---

#### gridheight

public int gridheight

Specifies the number of cells in a column for the component's
display area.

Use

REMAINDER

to specify that the component's
display area will be from

gridy

to the last
cell in the column.
Use

RELATIVE

to specify that the component's
display area will be from

gridy

to the next
to the last one in its column.

gridheight

should be a non-negative value and the
default value is 1.

Use

REMAINDER

to specify that the component's
display area will be from

gridy

to the last
cell in the column.
Use

RELATIVE

to specify that the component's
display area will be from

gridy

to the next
to the last one in its column.

gridheight

should be a non-negative value and the
default value is 1.

gridheight

should be a non-negative value and the
default value is 1.

weightx

```java
public double weightx
```

Specifies how to distribute extra horizontal space.

The grid bag layout manager calculates the weight of a column to
be the maximum

weightx

of all the components in a
column. If the resulting layout is smaller horizontally than the area
it needs to fill, the extra space is distributed to each column in
proportion to its weight. A column that has a weight of zero receives
no extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the left and right edges.

The default value of this field is

0

.

weightx

should be a non-negative value.

**See Also:** clone()

,

weighty

---

#### weightx

public double weightx

Specifies how to distribute extra horizontal space.

The grid bag layout manager calculates the weight of a column to
be the maximum

weightx

of all the components in a
column. If the resulting layout is smaller horizontally than the area
it needs to fill, the extra space is distributed to each column in
proportion to its weight. A column that has a weight of zero receives
no extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the left and right edges.

The default value of this field is

0

.

weightx

should be a non-negative value.

The grid bag layout manager calculates the weight of a column to
be the maximum

weightx

of all the components in a
column. If the resulting layout is smaller horizontally than the area
it needs to fill, the extra space is distributed to each column in
proportion to its weight. A column that has a weight of zero receives
no extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the left and right edges.

The default value of this field is

0

.

weightx

should be a non-negative value.

If all the weights are zero, all the extra space appears between
the grids of the cell and the left and right edges.

The default value of this field is

0

.

weightx

should be a non-negative value.

The default value of this field is

0

.

weightx

should be a non-negative value.

weighty

```java
public double weighty
```

Specifies how to distribute extra vertical space.

The grid bag layout manager calculates the weight of a row to be
the maximum

weighty

of all the components in a row.
If the resulting layout is smaller vertically than the area it
needs to fill, the extra space is distributed to each row in
proportion to its weight. A row that has a weight of zero receives no
extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the top and bottom edges.

The default value of this field is

0

.

weighty

should be a non-negative value.

**See Also:** clone()

,

weightx

---

#### weighty

public double weighty

Specifies how to distribute extra vertical space.

The grid bag layout manager calculates the weight of a row to be
the maximum

weighty

of all the components in a row.
If the resulting layout is smaller vertically than the area it
needs to fill, the extra space is distributed to each row in
proportion to its weight. A row that has a weight of zero receives no
extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the top and bottom edges.

The default value of this field is

0

.

weighty

should be a non-negative value.

The grid bag layout manager calculates the weight of a row to be
the maximum

weighty

of all the components in a row.
If the resulting layout is smaller vertically than the area it
needs to fill, the extra space is distributed to each row in
proportion to its weight. A row that has a weight of zero receives no
extra space.

If all the weights are zero, all the extra space appears between
the grids of the cell and the top and bottom edges.

The default value of this field is

0

.

weighty

should be a non-negative value.

If all the weights are zero, all the extra space appears between
the grids of the cell and the top and bottom edges.

The default value of this field is

0

.

weighty

should be a non-negative value.

The default value of this field is

0

.

weighty

should be a non-negative value.

anchor

```java
public int anchor
```

This field is used when the component is smaller than its
display area. It determines where, within the display area, to
place the component.

There are three kinds of possible values: orientation
relative, baseline relative and absolute. Orientation relative
values are interpreted relative to the container's component
orientation property, baseline relative values are interpreted
relative to the baseline and absolute values are not. The
absolute values are:

CENTER

,

NORTH

,

NORTHEAST

,

EAST

,

SOUTHEAST

,

SOUTH

,

SOUTHWEST

,

WEST

, and

NORTHWEST

.
The orientation relative values are:

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END

,

FIRST_LINE_START

,

FIRST_LINE_END

,

LAST_LINE_START

and

LAST_LINE_END

. The
baseline relative values are:

BASELINE

,

BASELINE_LEADING

,

BASELINE_TRAILING

,

ABOVE_BASELINE

,

ABOVE_BASELINE_LEADING

,

ABOVE_BASELINE_TRAILING

,

BELOW_BASELINE

,

BELOW_BASELINE_LEADING

,
and

BELOW_BASELINE_TRAILING

.
The default value is

CENTER

.

**See Also:** clone()

,

ComponentOrientation

---

#### anchor

public int anchor

This field is used when the component is smaller than its
display area. It determines where, within the display area, to
place the component.

There are three kinds of possible values: orientation
relative, baseline relative and absolute. Orientation relative
values are interpreted relative to the container's component
orientation property, baseline relative values are interpreted
relative to the baseline and absolute values are not. The
absolute values are:

CENTER

,

NORTH

,

NORTHEAST

,

EAST

,

SOUTHEAST

,

SOUTH

,

SOUTHWEST

,

WEST

, and

NORTHWEST

.
The orientation relative values are:

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END

,

FIRST_LINE_START

,

FIRST_LINE_END

,

LAST_LINE_START

and

LAST_LINE_END

. The
baseline relative values are:

BASELINE

,

BASELINE_LEADING

,

BASELINE_TRAILING

,

ABOVE_BASELINE

,

ABOVE_BASELINE_LEADING

,

ABOVE_BASELINE_TRAILING

,

BELOW_BASELINE

,

BELOW_BASELINE_LEADING

,
and

BELOW_BASELINE_TRAILING

.
The default value is

CENTER

.

There are three kinds of possible values: orientation
relative, baseline relative and absolute. Orientation relative
values are interpreted relative to the container's component
orientation property, baseline relative values are interpreted
relative to the baseline and absolute values are not. The
absolute values are:

CENTER

,

NORTH

,

NORTHEAST

,

EAST

,

SOUTHEAST

,

SOUTH

,

SOUTHWEST

,

WEST

, and

NORTHWEST

.
The orientation relative values are:

PAGE_START

,

PAGE_END

,

LINE_START

,

LINE_END

,

FIRST_LINE_START

,

FIRST_LINE_END

,

LAST_LINE_START

and

LAST_LINE_END

. The
baseline relative values are:

BASELINE

,

BASELINE_LEADING

,

BASELINE_TRAILING

,

ABOVE_BASELINE

,

ABOVE_BASELINE_LEADING

,

ABOVE_BASELINE_TRAILING

,

BELOW_BASELINE

,

BELOW_BASELINE_LEADING

,
and

BELOW_BASELINE_TRAILING

.
The default value is

CENTER

.

fill

```java
public int fill
```

This field is used when the component's display area is larger
than the component's requested size. It determines whether to
resize the component, and if so, how.

The following values are valid for

fill

:

- NONE

: Do not resize the component.

HORIZONTAL

: Make the component wide enough to fill
its display area horizontally, but do not change its height.

VERTICAL

: Make the component tall enough to fill its
display area vertically, but do not change its width.

BOTH

: Make the component fill its display area
entirely.

The default value is

NONE

.

**See Also:** clone()

---

#### fill

public int fill

This field is used when the component's display area is larger
than the component's requested size. It determines whether to
resize the component, and if so, how.

The following values are valid for

fill

:

- NONE

: Do not resize the component.

HORIZONTAL

: Make the component wide enough to fill
its display area horizontally, but do not change its height.

VERTICAL

: Make the component tall enough to fill its
display area vertically, but do not change its width.

BOTH

: Make the component fill its display area
entirely.

The default value is

NONE

.

The following values are valid for

fill

:

- NONE

: Do not resize the component.

HORIZONTAL

: Make the component wide enough to fill
its display area horizontally, but do not change its height.

VERTICAL

: Make the component tall enough to fill its
display area vertically, but do not change its width.

BOTH

: Make the component fill its display area
entirely.

The default value is

NONE

.

NONE

: Do not resize the component.

HORIZONTAL

: Make the component wide enough to fill
its display area horizontally, but do not change its height.

VERTICAL

: Make the component tall enough to fill its
display area vertically, but do not change its width.

BOTH

: Make the component fill its display area
entirely.

The default value is

NONE

.

insets

```java
public
Insets
insets
```

This field specifies the external padding of the component, the
minimum amount of space between the component and the edges of its
display area.

The default value is

new Insets(0, 0, 0, 0)

.

**See Also:** clone()

---

#### insets

public

Insets

insets

This field specifies the external padding of the component, the
minimum amount of space between the component and the edges of its
display area.

The default value is

new Insets(0, 0, 0, 0)

.

The default value is

new Insets(0, 0, 0, 0)

.

ipadx

```java
public int ipadx
```

This field specifies the internal padding of the component, how much
space to add to the minimum width of the component. The width of
the component is at least its minimum width plus

ipadx

pixels.

The default value is

0

.

**See Also:** clone()

,

ipady

---

#### ipadx

public int ipadx

This field specifies the internal padding of the component, how much
space to add to the minimum width of the component. The width of
the component is at least its minimum width plus

ipadx

pixels.

The default value is

0

.

The default value is

0

.

ipady

```java
public int ipady
```

This field specifies the internal padding, that is, how much
space to add to the minimum height of the component. The height of
the component is at least its minimum height plus

ipady

pixels.

The default value is 0.

**See Also:** clone()

,

ipadx

---

#### ipady

public int ipady

This field specifies the internal padding, that is, how much
space to add to the minimum height of the component. The height of
the component is at least its minimum height plus

ipady

pixels.

The default value is 0.

The default value is 0.

Constructor Detail

- GridBagConstraints

```java
public GridBagConstraints()
```

Creates a

GridBagConstraint

object with
all of its fields set to their default value.

- GridBagConstraints

```java
public GridBagConstraints​(int gridx,
int gridy,
int gridwidth,
int gridheight,
double weightx,
double weighty,
int anchor,
int fill,

Insets
insets,
int ipadx,
int ipady)
```

Creates a

GridBagConstraints

object with
all of its fields set to the passed-in arguments.

Note: Because the use of this constructor hinders readability
of source code, this constructor should only be used by
automatic source code generation tools.

**Parameters:** gridx

- The initial gridx value.
**Parameters:** gridy

- The initial gridy value.
**Parameters:** gridwidth

- The initial gridwidth value.
**Parameters:** gridheight

- The initial gridheight value.
**Parameters:** weightx

- The initial weightx value.
**Parameters:** weighty

- The initial weighty value.
**Parameters:** anchor

- The initial anchor value.
**Parameters:** fill

- The initial fill value.
**Parameters:** insets

- The initial insets value.
**Parameters:** ipadx

- The initial ipadx value.
**Parameters:** ipady

- The initial ipady value.
**Since:** 1.2
**See Also:** gridx

,

gridy

,

gridwidth

,

gridheight

,

weightx

,

weighty

,

anchor

,

fill

,

insets

,

ipadx

,

ipady

---

#### Constructor Detail

GridBagConstraints

```java
public GridBagConstraints()
```

Creates a

GridBagConstraint

object with
all of its fields set to their default value.

---

#### GridBagConstraints

public GridBagConstraints()

Creates a

GridBagConstraint

object with
all of its fields set to their default value.

GridBagConstraints

```java
public GridBagConstraints​(int gridx,
int gridy,
int gridwidth,
int gridheight,
double weightx,
double weighty,
int anchor,
int fill,

Insets
insets,
int ipadx,
int ipady)
```

Creates a

GridBagConstraints

object with
all of its fields set to the passed-in arguments.

Note: Because the use of this constructor hinders readability
of source code, this constructor should only be used by
automatic source code generation tools.

**Parameters:** gridx

- The initial gridx value.
**Parameters:** gridy

- The initial gridy value.
**Parameters:** gridwidth

- The initial gridwidth value.
**Parameters:** gridheight

- The initial gridheight value.
**Parameters:** weightx

- The initial weightx value.
**Parameters:** weighty

- The initial weighty value.
**Parameters:** anchor

- The initial anchor value.
**Parameters:** fill

- The initial fill value.
**Parameters:** insets

- The initial insets value.
**Parameters:** ipadx

- The initial ipadx value.
**Parameters:** ipady

- The initial ipady value.
**Since:** 1.2
**See Also:** gridx

,

gridy

,

gridwidth

,

gridheight

,

weightx

,

weighty

,

anchor

,

fill

,

insets

,

ipadx

,

ipady

---

#### GridBagConstraints

public GridBagConstraints​(int gridx,
int gridy,
int gridwidth,
int gridheight,
double weightx,
double weighty,
int anchor,
int fill,

Insets

insets,
int ipadx,
int ipady)

Creates a

GridBagConstraints

object with
all of its fields set to the passed-in arguments.

Note: Because the use of this constructor hinders readability
of source code, this constructor should only be used by
automatic source code generation tools.

Method Detail

- clone

```java
public
Object
clone()
```

Creates a copy of this grid bag constraint.

**Overrides:** clone

in class

Object
**Returns:** a copy of this grid bag constraint
**See Also:** Cloneable

---

#### Method Detail

clone

```java
public
Object
clone()
```

Creates a copy of this grid bag constraint.

**Overrides:** clone

in class

Object
**Returns:** a copy of this grid bag constraint
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a copy of this grid bag constraint.

---

