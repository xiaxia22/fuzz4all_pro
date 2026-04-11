# Class SpringLayout

**Source:** `java.desktop\javax\swing\SpringLayout.html`

### Class Description

```java
public class
SpringLayout

extends
Object

implements
LayoutManager2
```

A

SpringLayout

lays out the children of its associated container
according to a set of constraints.
See

How to Use SpringLayout

in

The Java Tutorial

for examples of using

SpringLayout

.

Each constraint,
represented by a

Spring

object,
controls the vertical or horizontal distance
between two component edges.
The edges can belong to
any child of the container,
or to the container itself.
For example,
the allowable width of a component
can be expressed using a constraint
that controls the distance between the west (left) and east (right)
edges of the component.
The allowable

y

coordinates for a component
can be expressed by constraining the distance between
the north (top) edge of the component
and the north edge of its container.

Every child of a

SpringLayout

-controlled container,
as well as the container itself,
has exactly one set of constraints
associated with it.
These constraints are represented by
a

SpringLayout.Constraints

object.
By default,

SpringLayout

creates constraints
that make their associated component
have the minimum, preferred, and maximum sizes
returned by the component's

Component.getMinimumSize()

,

Component.getPreferredSize()

, and

Component.getMaximumSize()

methods. The

x

and

y

positions are initially not
constrained, so that until you constrain them the

Component

will be positioned at 0,0 relative to the

Insets

of the
parent

Container

.

You can change
a component's constraints in several ways.
You can
use one of the

putConstraint

methods
to establish a spring
linking the edges of two components within the same container.
Or you can get the appropriate

SpringLayout.Constraints

object using

getConstraints

and then modify one or more of its springs.
Or you can get the spring for a particular edge of a component
using

getConstraint

,
and modify it.
You can also associate
your own

SpringLayout.Constraints

object
with a component by specifying the constraints object
when you add the component to its container
(using

Container.add(Component, Object)

).

The

Spring

object representing each constraint
has a minimum, preferred, maximum, and current value.
The current value of the spring
is somewhere between the minimum and maximum values,
according to the formula given in the

Spring.sum(javax.swing.Spring, javax.swing.Spring)

method description.
When the minimum, preferred, and maximum values are the same,
the current value is always equal to them;
this inflexible spring is called a

strut

.
You can create struts using the factory method

Spring.constant(int)

.
The

Spring

class also provides factory methods
for creating other kinds of springs,
including springs that depend on other springs.

In a

SpringLayout

, the position of each edge is dependent on
the position of just one other edge. If a constraint is subsequently added
to create a new binding for an edge, the previous binding is discarded
and the edge remains dependent on a single edge.
Springs should only be attached
between edges of the container and its immediate children; the behavior
of the

SpringLayout

when presented with constraints linking
the edges of components from different containers (either internal or
external) is undefined.

SpringLayout vs. Other Layout Managers

Note:

Unlike many layout managers,

SpringLayout

doesn't automatically set the location of
the components it manages.
If you hand-code a GUI that uses

SpringLayout

,
remember to initialize component locations by constraining the west/east
and north/south locations.

Depending on the constraints you use,
you may also need to set the size of the container explicitly.

Despite the simplicity of

SpringLayout

,
it can emulate the behavior of most other layout managers.
For some features,
such as the line breaking provided by

FlowLayout

,
you'll need to
create a special-purpose subclass of the

Spring

class.

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

---

### Field Details

#### public static final
String
NORTH

Specifies the top edge of a component's bounding rectangle.

**See Also:**
- Constant Field Values

---

#### public static final
String
SOUTH

Specifies the bottom edge of a component's bounding rectangle.

**See Also:**
- Constant Field Values

---

#### public static final
String
EAST

Specifies the right edge of a component's bounding rectangle.

**See Also:**
- Constant Field Values

---

#### public static final
String
WEST

Specifies the left edge of a component's bounding rectangle.

**See Also:**
- Constant Field Values

---

#### public static final
String
HORIZONTAL_CENTER

Specifies the horizontal center of a component's bounding rectangle.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final
String
VERTICAL_CENTER

Specifies the vertical center of a component's bounding rectangle.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final
String
BASELINE

Specifies the baseline of a component.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final
String
WIDTH

Specifies the width of a component's bounding rectangle.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

#### public static final
String
HEIGHT

Specifies the height of a component's bounding rectangle.

**See Also:**
- Constant Field Values

**Since:**
- 1.6

---

### Constructor Details

#### public SpringLayout()

Constructs a new

SpringLayout

.

---

### Method Details

#### public void addLayoutComponent​(
String
name,

Component
c)

Has no effect,
since this layout manager does not
use a per-component string.

**Specified by:**
- addLayoutComponent

in interface

LayoutManager

**Parameters:**
- name

- the string to be associated with the component
- c

- the component to be added

---

#### public void removeLayoutComponent​(
Component
c)

Removes the constraints associated with the specified component.

**Specified by:**
- removeLayoutComponent

in interface

LayoutManager

**Parameters:**
- c

- the component being removed from the container

---

#### public void addLayoutComponent​(
Component
component,

Object
constraints)

If

constraints

is an instance of

SpringLayout.Constraints

,
associates the constraints with the specified component.

**Specified by:**
- addLayoutComponent

in interface

LayoutManager2

**Parameters:**
- component

- the component being added
- constraints

- the component's constraints

**See Also:**
- SpringLayout.Constraints

---

#### public float getLayoutAlignmentX​(
Container
p)

Returns 0.5f (centered).

**Specified by:**
- getLayoutAlignmentX

in interface

LayoutManager2

**Parameters:**
- p

- the target container

**Returns:**
- the x-axis alignment preference

---

#### public float getLayoutAlignmentY​(
Container
p)

Returns 0.5f (centered).

**Specified by:**
- getLayoutAlignmentY

in interface

LayoutManager2

**Parameters:**
- p

- the target container

**Returns:**
- the y-axis alignment preference

---

#### public void putConstraint​(
String
e1,

Component
c1,
int pad,

String
e2,

Component
c2)

Links edge

e1

of component

c1

to
edge

e2

of component

c2

,
with a fixed distance between the edges. This
constraint will cause the assignment

```java
value(e1, c1) = value(e2, c2) + pad
```

to take place during all subsequent layout operations.

**Parameters:**
- e1

- the edge of the dependent
- c1

- the component of the dependent
- pad

- the fixed distance between dependent and anchor
- e2

- the edge of the anchor
- c2

- the component of the anchor

**See Also:**
- putConstraint(String, Component, Spring, String, Component)

---

#### public void putConstraint​(
String
e1,

Component
c1,

Spring
s,

String
e2,

Component
c2)

Links edge

e1

of component

c1

to
edge

e2

of component

c2

. As edge

(e2, c2)

changes value, edge

(e1, c1)

will
be calculated by taking the (spring) sum of

(e2, c2)

and

s

.
Each edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.HORIZONTAL_CENTER

or

SpringLayout.BASELINE

.

**Parameters:**
- e1

- the edge of the dependent
- c1

- the component of the dependent
- s

- the spring linking dependent and anchor
- e2

- the edge of the anchor
- c2

- the component of the anchor

**See Also:**
- putConstraint(String, Component, int, String, Component)

,

NORTH

,

SOUTH

,

EAST

,

WEST

,

VERTICAL_CENTER

,

HORIZONTAL_CENTER

,

BASELINE

---

#### public
SpringLayout.Constraints
getConstraints​(
Component
c)

Returns the constraints for the specified component.
Note that,
unlike the

GridBagLayout

getConstraints

method,
this method does not clone constraints.
If no constraints
have been associated with this component,
this method
returns a default constraints object positioned at
0,0 relative to the parent's Insets and its width/height
constrained to the minimum, maximum, and preferred sizes of the
component. The size characteristics
are not frozen at the time this method is called;
instead this method returns a constraints object
whose characteristics track the characteristics
of the component as they change.

**Parameters:**
- c

- the component whose constraints will be returned

**Returns:**
- the constraints for the specified component

---

#### public
Spring
getConstraint​(
String
edgeName,

Component
c)

Returns the spring controlling the distance between
the specified edge of
the component and the top or left edge of its parent. This
method, instead of returning the current binding for the
edge, returns a proxy that tracks the characteristics
of the edge even if the edge is subsequently rebound.
Proxies are intended to be used in builder environments
where it is useful to allow the user to define the
constraints for a layout in any order. Proxies do, however,
provide the means to create cyclic dependencies amongst
the constraints of a layout. Such cycles are detected
internally by

SpringLayout

so that
the layout operation always terminates.

**Parameters:**
- edgeName

- must be one of

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.HORIZONTAL_CENTER

or

SpringLayout.BASELINE
- c

- the component whose edge spring is desired

**Returns:**
- a proxy for the spring controlling the distance between the
specified edge and the top or left edge of its parent

**See Also:**
- NORTH

,

SOUTH

,

EAST

,

WEST

,

VERTICAL_CENTER

,

HORIZONTAL_CENTER

,

BASELINE

---

### Additional Sections

#### Class SpringLayout

java.lang.Object

- javax.swing.SpringLayout

javax.swing.SpringLayout

**All Implemented Interfaces:** LayoutManager

,

LayoutManager2

```java
public class
SpringLayout

extends
Object

implements
LayoutManager2
```

A

SpringLayout

lays out the children of its associated container
according to a set of constraints.
See

How to Use SpringLayout

in

The Java Tutorial

for examples of using

SpringLayout

.

Each constraint,
represented by a

Spring

object,
controls the vertical or horizontal distance
between two component edges.
The edges can belong to
any child of the container,
or to the container itself.
For example,
the allowable width of a component
can be expressed using a constraint
that controls the distance between the west (left) and east (right)
edges of the component.
The allowable

y

coordinates for a component
can be expressed by constraining the distance between
the north (top) edge of the component
and the north edge of its container.

Every child of a

SpringLayout

-controlled container,
as well as the container itself,
has exactly one set of constraints
associated with it.
These constraints are represented by
a

SpringLayout.Constraints

object.
By default,

SpringLayout

creates constraints
that make their associated component
have the minimum, preferred, and maximum sizes
returned by the component's

Component.getMinimumSize()

,

Component.getPreferredSize()

, and

Component.getMaximumSize()

methods. The

x

and

y

positions are initially not
constrained, so that until you constrain them the

Component

will be positioned at 0,0 relative to the

Insets

of the
parent

Container

.

You can change
a component's constraints in several ways.
You can
use one of the

putConstraint

methods
to establish a spring
linking the edges of two components within the same container.
Or you can get the appropriate

SpringLayout.Constraints

object using

getConstraints

and then modify one or more of its springs.
Or you can get the spring for a particular edge of a component
using

getConstraint

,
and modify it.
You can also associate
your own

SpringLayout.Constraints

object
with a component by specifying the constraints object
when you add the component to its container
(using

Container.add(Component, Object)

).

The

Spring

object representing each constraint
has a minimum, preferred, maximum, and current value.
The current value of the spring
is somewhere between the minimum and maximum values,
according to the formula given in the

Spring.sum(javax.swing.Spring, javax.swing.Spring)

method description.
When the minimum, preferred, and maximum values are the same,
the current value is always equal to them;
this inflexible spring is called a

strut

.
You can create struts using the factory method

Spring.constant(int)

.
The

Spring

class also provides factory methods
for creating other kinds of springs,
including springs that depend on other springs.

In a

SpringLayout

, the position of each edge is dependent on
the position of just one other edge. If a constraint is subsequently added
to create a new binding for an edge, the previous binding is discarded
and the edge remains dependent on a single edge.
Springs should only be attached
between edges of the container and its immediate children; the behavior
of the

SpringLayout

when presented with constraints linking
the edges of components from different containers (either internal or
external) is undefined.

SpringLayout vs. Other Layout Managers

Note:

Unlike many layout managers,

SpringLayout

doesn't automatically set the location of
the components it manages.
If you hand-code a GUI that uses

SpringLayout

,
remember to initialize component locations by constraining the west/east
and north/south locations.

Depending on the constraints you use,
you may also need to set the size of the container explicitly.

Despite the simplicity of

SpringLayout

,
it can emulate the behavior of most other layout managers.
For some features,
such as the line breaking provided by

FlowLayout

,
you'll need to
create a special-purpose subclass of the

Spring

class.

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

**Since:** 1.4
**See Also:** Spring

,

SpringLayout.Constraints

public class

SpringLayout

extends

Object

implements

LayoutManager2

A

SpringLayout

lays out the children of its associated container
according to a set of constraints.
See

How to Use SpringLayout

in

The Java Tutorial

for examples of using

SpringLayout

.

Each constraint,
represented by a

Spring

object,
controls the vertical or horizontal distance
between two component edges.
The edges can belong to
any child of the container,
or to the container itself.
For example,
the allowable width of a component
can be expressed using a constraint
that controls the distance between the west (left) and east (right)
edges of the component.
The allowable

y

coordinates for a component
can be expressed by constraining the distance between
the north (top) edge of the component
and the north edge of its container.

Every child of a

SpringLayout

-controlled container,
as well as the container itself,
has exactly one set of constraints
associated with it.
These constraints are represented by
a

SpringLayout.Constraints

object.
By default,

SpringLayout

creates constraints
that make their associated component
have the minimum, preferred, and maximum sizes
returned by the component's

Component.getMinimumSize()

,

Component.getPreferredSize()

, and

Component.getMaximumSize()

methods. The

x

and

y

positions are initially not
constrained, so that until you constrain them the

Component

will be positioned at 0,0 relative to the

Insets

of the
parent

Container

.

You can change
a component's constraints in several ways.
You can
use one of the

putConstraint

methods
to establish a spring
linking the edges of two components within the same container.
Or you can get the appropriate

SpringLayout.Constraints

object using

getConstraints

and then modify one or more of its springs.
Or you can get the spring for a particular edge of a component
using

getConstraint

,
and modify it.
You can also associate
your own

SpringLayout.Constraints

object
with a component by specifying the constraints object
when you add the component to its container
(using

Container.add(Component, Object)

).

The

Spring

object representing each constraint
has a minimum, preferred, maximum, and current value.
The current value of the spring
is somewhere between the minimum and maximum values,
according to the formula given in the

Spring.sum(javax.swing.Spring, javax.swing.Spring)

method description.
When the minimum, preferred, and maximum values are the same,
the current value is always equal to them;
this inflexible spring is called a

strut

.
You can create struts using the factory method

Spring.constant(int)

.
The

Spring

class also provides factory methods
for creating other kinds of springs,
including springs that depend on other springs.

In a

SpringLayout

, the position of each edge is dependent on
the position of just one other edge. If a constraint is subsequently added
to create a new binding for an edge, the previous binding is discarded
and the edge remains dependent on a single edge.
Springs should only be attached
between edges of the container and its immediate children; the behavior
of the

SpringLayout

when presented with constraints linking
the edges of components from different containers (either internal or
external) is undefined.

SpringLayout vs. Other Layout Managers

Note:

Unlike many layout managers,

SpringLayout

doesn't automatically set the location of
the components it manages.
If you hand-code a GUI that uses

SpringLayout

,
remember to initialize component locations by constraining the west/east
and north/south locations.

Depending on the constraints you use,
you may also need to set the size of the container explicitly.

Despite the simplicity of

SpringLayout

,
it can emulate the behavior of most other layout managers.
For some features,
such as the line breaking provided by

FlowLayout

,
you'll need to
create a special-purpose subclass of the

Spring

class.

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

Each constraint,
represented by a

Spring

object,
controls the vertical or horizontal distance
between two component edges.
The edges can belong to
any child of the container,
or to the container itself.
For example,
the allowable width of a component
can be expressed using a constraint
that controls the distance between the west (left) and east (right)
edges of the component.
The allowable

y

coordinates for a component
can be expressed by constraining the distance between
the north (top) edge of the component
and the north edge of its container.

Every child of a

SpringLayout

-controlled container,
as well as the container itself,
has exactly one set of constraints
associated with it.
These constraints are represented by
a

SpringLayout.Constraints

object.
By default,

SpringLayout

creates constraints
that make their associated component
have the minimum, preferred, and maximum sizes
returned by the component's

Component.getMinimumSize()

,

Component.getPreferredSize()

, and

Component.getMaximumSize()

methods. The

x

and

y

positions are initially not
constrained, so that until you constrain them the

Component

will be positioned at 0,0 relative to the

Insets

of the
parent

Container

.

You can change
a component's constraints in several ways.
You can
use one of the

putConstraint

methods
to establish a spring
linking the edges of two components within the same container.
Or you can get the appropriate

SpringLayout.Constraints

object using

getConstraints

and then modify one or more of its springs.
Or you can get the spring for a particular edge of a component
using

getConstraint

,
and modify it.
You can also associate
your own

SpringLayout.Constraints

object
with a component by specifying the constraints object
when you add the component to its container
(using

Container.add(Component, Object)

).

The

Spring

object representing each constraint
has a minimum, preferred, maximum, and current value.
The current value of the spring
is somewhere between the minimum and maximum values,
according to the formula given in the

Spring.sum(javax.swing.Spring, javax.swing.Spring)

method description.
When the minimum, preferred, and maximum values are the same,
the current value is always equal to them;
this inflexible spring is called a

strut

.
You can create struts using the factory method

Spring.constant(int)

.
The

Spring

class also provides factory methods
for creating other kinds of springs,
including springs that depend on other springs.

In a

SpringLayout

, the position of each edge is dependent on
the position of just one other edge. If a constraint is subsequently added
to create a new binding for an edge, the previous binding is discarded
and the edge remains dependent on a single edge.
Springs should only be attached
between edges of the container and its immediate children; the behavior
of the

SpringLayout

when presented with constraints linking
the edges of components from different containers (either internal or
external) is undefined.

SpringLayout vs. Other Layout Managers

Note:

Unlike many layout managers,

SpringLayout

doesn't automatically set the location of
the components it manages.
If you hand-code a GUI that uses

SpringLayout

,
remember to initialize component locations by constraining the west/east
and north/south locations.

Depending on the constraints you use,
you may also need to set the size of the container explicitly.

Despite the simplicity of

SpringLayout

,
it can emulate the behavior of most other layout managers.
For some features,
such as the line breaking provided by

FlowLayout

,
you'll need to
create a special-purpose subclass of the

Spring

class.

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

Every child of a

SpringLayout

-controlled container,
as well as the container itself,
has exactly one set of constraints
associated with it.
These constraints are represented by
a

SpringLayout.Constraints

object.
By default,

SpringLayout

creates constraints
that make their associated component
have the minimum, preferred, and maximum sizes
returned by the component's

Component.getMinimumSize()

,

Component.getPreferredSize()

, and

Component.getMaximumSize()

methods. The

x

and

y

positions are initially not
constrained, so that until you constrain them the

Component

will be positioned at 0,0 relative to the

Insets

of the
parent

Container

.

You can change
a component's constraints in several ways.
You can
use one of the

putConstraint

methods
to establish a spring
linking the edges of two components within the same container.
Or you can get the appropriate

SpringLayout.Constraints

object using

getConstraints

and then modify one or more of its springs.
Or you can get the spring for a particular edge of a component
using

getConstraint

,
and modify it.
You can also associate
your own

SpringLayout.Constraints

object
with a component by specifying the constraints object
when you add the component to its container
(using

Container.add(Component, Object)

).

The

Spring

object representing each constraint
has a minimum, preferred, maximum, and current value.
The current value of the spring
is somewhere between the minimum and maximum values,
according to the formula given in the

Spring.sum(javax.swing.Spring, javax.swing.Spring)

method description.
When the minimum, preferred, and maximum values are the same,
the current value is always equal to them;
this inflexible spring is called a

strut

.
You can create struts using the factory method

Spring.constant(int)

.
The

Spring

class also provides factory methods
for creating other kinds of springs,
including springs that depend on other springs.

In a

SpringLayout

, the position of each edge is dependent on
the position of just one other edge. If a constraint is subsequently added
to create a new binding for an edge, the previous binding is discarded
and the edge remains dependent on a single edge.
Springs should only be attached
between edges of the container and its immediate children; the behavior
of the

SpringLayout

when presented with constraints linking
the edges of components from different containers (either internal or
external) is undefined.

SpringLayout vs. Other Layout Managers

Note:

Unlike many layout managers,

SpringLayout

doesn't automatically set the location of
the components it manages.
If you hand-code a GUI that uses

SpringLayout

,
remember to initialize component locations by constraining the west/east
and north/south locations.

Depending on the constraints you use,
you may also need to set the size of the container explicitly.

Despite the simplicity of

SpringLayout

,
it can emulate the behavior of most other layout managers.
For some features,
such as the line breaking provided by

FlowLayout

,
you'll need to
create a special-purpose subclass of the

Spring

class.

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

You can change
a component's constraints in several ways.
You can
use one of the

putConstraint

methods
to establish a spring
linking the edges of two components within the same container.
Or you can get the appropriate

SpringLayout.Constraints

object using

getConstraints

and then modify one or more of its springs.
Or you can get the spring for a particular edge of a component
using

getConstraint

,
and modify it.
You can also associate
your own

SpringLayout.Constraints

object
with a component by specifying the constraints object
when you add the component to its container
(using

Container.add(Component, Object)

).

The

Spring

object representing each constraint
has a minimum, preferred, maximum, and current value.
The current value of the spring
is somewhere between the minimum and maximum values,
according to the formula given in the

Spring.sum(javax.swing.Spring, javax.swing.Spring)

method description.
When the minimum, preferred, and maximum values are the same,
the current value is always equal to them;
this inflexible spring is called a

strut

.
You can create struts using the factory method

Spring.constant(int)

.
The

Spring

class also provides factory methods
for creating other kinds of springs,
including springs that depend on other springs.

In a

SpringLayout

, the position of each edge is dependent on
the position of just one other edge. If a constraint is subsequently added
to create a new binding for an edge, the previous binding is discarded
and the edge remains dependent on a single edge.
Springs should only be attached
between edges of the container and its immediate children; the behavior
of the

SpringLayout

when presented with constraints linking
the edges of components from different containers (either internal or
external) is undefined.

SpringLayout vs. Other Layout Managers

Note:

Unlike many layout managers,

SpringLayout

doesn't automatically set the location of
the components it manages.
If you hand-code a GUI that uses

SpringLayout

,
remember to initialize component locations by constraining the west/east
and north/south locations.

Depending on the constraints you use,
you may also need to set the size of the container explicitly.

Despite the simplicity of

SpringLayout

,
it can emulate the behavior of most other layout managers.
For some features,
such as the line breaking provided by

FlowLayout

,
you'll need to
create a special-purpose subclass of the

Spring

class.

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

The

Spring

object representing each constraint
has a minimum, preferred, maximum, and current value.
The current value of the spring
is somewhere between the minimum and maximum values,
according to the formula given in the

Spring.sum(javax.swing.Spring, javax.swing.Spring)

method description.
When the minimum, preferred, and maximum values are the same,
the current value is always equal to them;
this inflexible spring is called a

strut

.
You can create struts using the factory method

Spring.constant(int)

.
The

Spring

class also provides factory methods
for creating other kinds of springs,
including springs that depend on other springs.

In a

SpringLayout

, the position of each edge is dependent on
the position of just one other edge. If a constraint is subsequently added
to create a new binding for an edge, the previous binding is discarded
and the edge remains dependent on a single edge.
Springs should only be attached
between edges of the container and its immediate children; the behavior
of the

SpringLayout

when presented with constraints linking
the edges of components from different containers (either internal or
external) is undefined.

SpringLayout vs. Other Layout Managers

Note:

Unlike many layout managers,

SpringLayout

doesn't automatically set the location of
the components it manages.
If you hand-code a GUI that uses

SpringLayout

,
remember to initialize component locations by constraining the west/east
and north/south locations.

Depending on the constraints you use,
you may also need to set the size of the container explicitly.

Despite the simplicity of

SpringLayout

,
it can emulate the behavior of most other layout managers.
For some features,
such as the line breaking provided by

FlowLayout

,
you'll need to
create a special-purpose subclass of the

Spring

class.

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

In a

SpringLayout

, the position of each edge is dependent on
the position of just one other edge. If a constraint is subsequently added
to create a new binding for an edge, the previous binding is discarded
and the edge remains dependent on a single edge.
Springs should only be attached
between edges of the container and its immediate children; the behavior
of the

SpringLayout

when presented with constraints linking
the edges of components from different containers (either internal or
external) is undefined.

SpringLayout vs. Other Layout Managers

Note:

Unlike many layout managers,

SpringLayout

doesn't automatically set the location of
the components it manages.
If you hand-code a GUI that uses

SpringLayout

,
remember to initialize component locations by constraining the west/east
and north/south locations.

Depending on the constraints you use,
you may also need to set the size of the container explicitly.

Despite the simplicity of

SpringLayout

,
it can emulate the behavior of most other layout managers.
For some features,
such as the line breaking provided by

FlowLayout

,
you'll need to
create a special-purpose subclass of the

Spring

class.

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

---

#### SpringLayout vs. Other Layout Managers

Depending on the constraints you use,
you may also need to set the size of the container explicitly.

Despite the simplicity of

SpringLayout

,
it can emulate the behavior of most other layout managers.
For some features,
such as the line breaking provided by

FlowLayout

,
you'll need to
create a special-purpose subclass of the

Spring

class.

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

SpringLayout

also provides a way to solve
many of the difficult layout
problems that cannot be solved by nesting combinations
of

Box

es. That said,

SpringLayout

honors the

LayoutManager2

contract correctly and so can be nested with
other layout managers -- a technique that can be preferable to
creating the constraints implied by the other layout managers.

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

The asymptotic complexity of the layout operation of a

SpringLayout

is linear in the number of constraints (and/or components).

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

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SpringLayout.Constraints

A

Constraints

object holds the
constraints that govern the way a component's size and position
change in a container controlled by a

SpringLayout

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

BASELINE

Specifies the baseline of a component.

static

String

EAST

Specifies the right edge of a component's bounding rectangle.

static

String

HEIGHT

Specifies the height of a component's bounding rectangle.

static

String

HORIZONTAL_CENTER

Specifies the horizontal center of a component's bounding rectangle.

static

String

NORTH

Specifies the top edge of a component's bounding rectangle.

static

String

SOUTH

Specifies the bottom edge of a component's bounding rectangle.

static

String

VERTICAL_CENTER

Specifies the vertical center of a component's bounding rectangle.

static

String

WEST

Specifies the left edge of a component's bounding rectangle.

static

String

WIDTH

Specifies the width of a component's bounding rectangle.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SpringLayout

()

Constructs a new

SpringLayout

.

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

component,

Object

constraints)

If

constraints

is an instance of

SpringLayout.Constraints

,
associates the constraints with the specified component.

void

addLayoutComponent

​(

String

name,

Component

c)

Has no effect,
since this layout manager does not
use a per-component string.

Spring

getConstraint

​(

String

edgeName,

Component

c)

Returns the spring controlling the distance between
the specified edge of
the component and the top or left edge of its parent.

SpringLayout.Constraints

getConstraints

​(

Component

c)

Returns the constraints for the specified component.

float

getLayoutAlignmentX

​(

Container

p)

Returns 0.5f (centered).

float

getLayoutAlignmentY

​(

Container

p)

Returns 0.5f (centered).

void

putConstraint

​(

String

e1,

Component

c1,
int pad,

String

e2,

Component

c2)

Links edge

e1

of component

c1

to
edge

e2

of component

c2

,
with a fixed distance between the edges.

void

putConstraint

​(

String

e1,

Component

c1,

Spring

s,

String

e2,

Component

c2)

Links edge

e1

of component

c1

to
edge

e2

of component

c2

.

void

removeLayoutComponent

​(

Component

c)

Removes the constraints associated with the specified component.

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

- Methods declared in interface java.awt.

LayoutManager

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

- Methods declared in interface java.awt.

LayoutManager2

invalidateLayout

,

maximumLayoutSize

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SpringLayout.Constraints

A

Constraints

object holds the
constraints that govern the way a component's size and position
change in a container controlled by a

SpringLayout

.

---

#### Nested Class Summary

A

Constraints

object holds the
constraints that govern the way a component's size and position
change in a container controlled by a

SpringLayout

.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

BASELINE

Specifies the baseline of a component.

static

String

EAST

Specifies the right edge of a component's bounding rectangle.

static

String

HEIGHT

Specifies the height of a component's bounding rectangle.

static

String

HORIZONTAL_CENTER

Specifies the horizontal center of a component's bounding rectangle.

static

String

NORTH

Specifies the top edge of a component's bounding rectangle.

static

String

SOUTH

Specifies the bottom edge of a component's bounding rectangle.

static

String

VERTICAL_CENTER

Specifies the vertical center of a component's bounding rectangle.

static

String

WEST

Specifies the left edge of a component's bounding rectangle.

static

String

WIDTH

Specifies the width of a component's bounding rectangle.

---

#### Field Summary

Specifies the baseline of a component.

Specifies the right edge of a component's bounding rectangle.

Specifies the height of a component's bounding rectangle.

Specifies the horizontal center of a component's bounding rectangle.

Specifies the top edge of a component's bounding rectangle.

Specifies the bottom edge of a component's bounding rectangle.

Specifies the vertical center of a component's bounding rectangle.

Specifies the left edge of a component's bounding rectangle.

Specifies the width of a component's bounding rectangle.

Constructor Summary

Constructors

Constructor

Description

SpringLayout

()

Constructs a new

SpringLayout

.

---

#### Constructor Summary

Constructs a new

SpringLayout

.

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

component,

Object

constraints)

If

constraints

is an instance of

SpringLayout.Constraints

,
associates the constraints with the specified component.

void

addLayoutComponent

​(

String

name,

Component

c)

Has no effect,
since this layout manager does not
use a per-component string.

Spring

getConstraint

​(

String

edgeName,

Component

c)

Returns the spring controlling the distance between
the specified edge of
the component and the top or left edge of its parent.

SpringLayout.Constraints

getConstraints

​(

Component

c)

Returns the constraints for the specified component.

float

getLayoutAlignmentX

​(

Container

p)

Returns 0.5f (centered).

float

getLayoutAlignmentY

​(

Container

p)

Returns 0.5f (centered).

void

putConstraint

​(

String

e1,

Component

c1,
int pad,

String

e2,

Component

c2)

Links edge

e1

of component

c1

to
edge

e2

of component

c2

,
with a fixed distance between the edges.

void

putConstraint

​(

String

e1,

Component

c1,

Spring

s,

String

e2,

Component

c2)

Links edge

e1

of component

c1

to
edge

e2

of component

c2

.

void

removeLayoutComponent

​(

Component

c)

Removes the constraints associated with the specified component.

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

- Methods declared in interface java.awt.

LayoutManager

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

- Methods declared in interface java.awt.

LayoutManager2

invalidateLayout

,

maximumLayoutSize

---

#### Method Summary

If

constraints

is an instance of

SpringLayout.Constraints

,
associates the constraints with the specified component.

Has no effect,
since this layout manager does not
use a per-component string.

Returns the spring controlling the distance between
the specified edge of
the component and the top or left edge of its parent.

Returns the constraints for the specified component.

Returns 0.5f (centered).

Links edge

e1

of component

c1

to
edge

e2

of component

c2

,
with a fixed distance between the edges.

Links edge

e1

of component

c1

to
edge

e2

of component

c2

.

Removes the constraints associated with the specified component.

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

Methods declared in interface java.awt.

LayoutManager

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

---

#### Methods declared in interface java.awt. LayoutManager

Methods declared in interface java.awt.

LayoutManager2

invalidateLayout

,

maximumLayoutSize

---

#### Methods declared in interface java.awt. LayoutManager2

============ FIELD DETAIL ===========

- Field Detail

- NORTH

```java
public static final
String
NORTH
```

Specifies the top edge of a component's bounding rectangle.

**See Also:** Constant Field Values

- SOUTH

```java
public static final
String
SOUTH
```

Specifies the bottom edge of a component's bounding rectangle.

**See Also:** Constant Field Values

- EAST

```java
public static final
String
EAST
```

Specifies the right edge of a component's bounding rectangle.

**See Also:** Constant Field Values

- WEST

```java
public static final
String
WEST
```

Specifies the left edge of a component's bounding rectangle.

**See Also:** Constant Field Values

- HORIZONTAL_CENTER

```java
public static final
String
HORIZONTAL_CENTER
```

Specifies the horizontal center of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

- VERTICAL_CENTER

```java
public static final
String
VERTICAL_CENTER
```

Specifies the vertical center of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

- BASELINE

```java
public static final
String
BASELINE
```

Specifies the baseline of a component.

**Since:** 1.6
**See Also:** Constant Field Values

- WIDTH

```java
public static final
String
WIDTH
```

Specifies the width of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

- HEIGHT

```java
public static final
String
HEIGHT
```

Specifies the height of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SpringLayout

```java
public SpringLayout()
```

Constructs a new

SpringLayout

.

============ METHOD DETAIL ==========

- Method Detail

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
c)
```

Has no effect,
since this layout manager does not
use a per-component string.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the string to be associated with the component
**Parameters:** c

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
c)
```

Removes the constraints associated with the specified component.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** c

- the component being removed from the container

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
component,

Object
constraints)
```

If

constraints

is an instance of

SpringLayout.Constraints

,
associates the constraints with the specified component.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** component

- the component being added
**Parameters:** constraints

- the component's constraints
**See Also:** SpringLayout.Constraints

- getLayoutAlignmentX

```java
public float getLayoutAlignmentX​(
Container
p)
```

Returns 0.5f (centered).

**Specified by:** getLayoutAlignmentX

in interface

LayoutManager2
**Parameters:** p

- the target container
**Returns:** the x-axis alignment preference

- getLayoutAlignmentY

```java
public float getLayoutAlignmentY​(
Container
p)
```

Returns 0.5f (centered).

**Specified by:** getLayoutAlignmentY

in interface

LayoutManager2
**Parameters:** p

- the target container
**Returns:** the y-axis alignment preference

- putConstraint

```java
public void putConstraint​(
String
e1,

Component
c1,
int pad,

String
e2,

Component
c2)
```

Links edge

e1

of component

c1

to
edge

e2

of component

c2

,
with a fixed distance between the edges. This
constraint will cause the assignment

```java
value(e1, c1) = value(e2, c2) + pad
```

to take place during all subsequent layout operations.

**Parameters:** e1

- the edge of the dependent
**Parameters:** c1

- the component of the dependent
**Parameters:** pad

- the fixed distance between dependent and anchor
**Parameters:** e2

- the edge of the anchor
**Parameters:** c2

- the component of the anchor
**See Also:** putConstraint(String, Component, Spring, String, Component)

- putConstraint

```java
public void putConstraint​(
String
e1,

Component
c1,

Spring
s,

String
e2,

Component
c2)
```

Links edge

e1

of component

c1

to
edge

e2

of component

c2

. As edge

(e2, c2)

changes value, edge

(e1, c1)

will
be calculated by taking the (spring) sum of

(e2, c2)

and

s

.
Each edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.HORIZONTAL_CENTER

or

SpringLayout.BASELINE

.

**Parameters:** e1

- the edge of the dependent
**Parameters:** c1

- the component of the dependent
**Parameters:** s

- the spring linking dependent and anchor
**Parameters:** e2

- the edge of the anchor
**Parameters:** c2

- the component of the anchor
**See Also:** putConstraint(String, Component, int, String, Component)

,

NORTH

,

SOUTH

,

EAST

,

WEST

,

VERTICAL_CENTER

,

HORIZONTAL_CENTER

,

BASELINE

- getConstraints

```java
public
SpringLayout.Constraints
getConstraints​(
Component
c)
```

Returns the constraints for the specified component.
Note that,
unlike the

GridBagLayout

getConstraints

method,
this method does not clone constraints.
If no constraints
have been associated with this component,
this method
returns a default constraints object positioned at
0,0 relative to the parent's Insets and its width/height
constrained to the minimum, maximum, and preferred sizes of the
component. The size characteristics
are not frozen at the time this method is called;
instead this method returns a constraints object
whose characteristics track the characteristics
of the component as they change.

**Parameters:** c

- the component whose constraints will be returned
**Returns:** the constraints for the specified component

- getConstraint

```java
public
Spring
getConstraint​(
String
edgeName,

Component
c)
```

Returns the spring controlling the distance between
the specified edge of
the component and the top or left edge of its parent. This
method, instead of returning the current binding for the
edge, returns a proxy that tracks the characteristics
of the edge even if the edge is subsequently rebound.
Proxies are intended to be used in builder environments
where it is useful to allow the user to define the
constraints for a layout in any order. Proxies do, however,
provide the means to create cyclic dependencies amongst
the constraints of a layout. Such cycles are detected
internally by

SpringLayout

so that
the layout operation always terminates.

**Parameters:** edgeName

- must be one of

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.HORIZONTAL_CENTER

or

SpringLayout.BASELINE
**Parameters:** c

- the component whose edge spring is desired
**Returns:** a proxy for the spring controlling the distance between the
specified edge and the top or left edge of its parent
**See Also:** NORTH

,

SOUTH

,

EAST

,

WEST

,

VERTICAL_CENTER

,

HORIZONTAL_CENTER

,

BASELINE

Field Detail

- NORTH

```java
public static final
String
NORTH
```

Specifies the top edge of a component's bounding rectangle.

**See Also:** Constant Field Values

- SOUTH

```java
public static final
String
SOUTH
```

Specifies the bottom edge of a component's bounding rectangle.

**See Also:** Constant Field Values

- EAST

```java
public static final
String
EAST
```

Specifies the right edge of a component's bounding rectangle.

**See Also:** Constant Field Values

- WEST

```java
public static final
String
WEST
```

Specifies the left edge of a component's bounding rectangle.

**See Also:** Constant Field Values

- HORIZONTAL_CENTER

```java
public static final
String
HORIZONTAL_CENTER
```

Specifies the horizontal center of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

- VERTICAL_CENTER

```java
public static final
String
VERTICAL_CENTER
```

Specifies the vertical center of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

- BASELINE

```java
public static final
String
BASELINE
```

Specifies the baseline of a component.

**Since:** 1.6
**See Also:** Constant Field Values

- WIDTH

```java
public static final
String
WIDTH
```

Specifies the width of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

- HEIGHT

```java
public static final
String
HEIGHT
```

Specifies the height of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### Field Detail

NORTH

```java
public static final
String
NORTH
```

Specifies the top edge of a component's bounding rectangle.

**See Also:** Constant Field Values

---

#### NORTH

public static final

String

NORTH

Specifies the top edge of a component's bounding rectangle.

SOUTH

```java
public static final
String
SOUTH
```

Specifies the bottom edge of a component's bounding rectangle.

**See Also:** Constant Field Values

---

#### SOUTH

public static final

String

SOUTH

Specifies the bottom edge of a component's bounding rectangle.

EAST

```java
public static final
String
EAST
```

Specifies the right edge of a component's bounding rectangle.

**See Also:** Constant Field Values

---

#### EAST

public static final

String

EAST

Specifies the right edge of a component's bounding rectangle.

WEST

```java
public static final
String
WEST
```

Specifies the left edge of a component's bounding rectangle.

**See Also:** Constant Field Values

---

#### WEST

public static final

String

WEST

Specifies the left edge of a component's bounding rectangle.

HORIZONTAL_CENTER

```java
public static final
String
HORIZONTAL_CENTER
```

Specifies the horizontal center of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### HORIZONTAL_CENTER

public static final

String

HORIZONTAL_CENTER

Specifies the horizontal center of a component's bounding rectangle.

VERTICAL_CENTER

```java
public static final
String
VERTICAL_CENTER
```

Specifies the vertical center of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### VERTICAL_CENTER

public static final

String

VERTICAL_CENTER

Specifies the vertical center of a component's bounding rectangle.

BASELINE

```java
public static final
String
BASELINE
```

Specifies the baseline of a component.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### BASELINE

public static final

String

BASELINE

Specifies the baseline of a component.

WIDTH

```java
public static final
String
WIDTH
```

Specifies the width of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### WIDTH

public static final

String

WIDTH

Specifies the width of a component's bounding rectangle.

HEIGHT

```java
public static final
String
HEIGHT
```

Specifies the height of a component's bounding rectangle.

**Since:** 1.6
**See Also:** Constant Field Values

---

#### HEIGHT

public static final

String

HEIGHT

Specifies the height of a component's bounding rectangle.

Constructor Detail

- SpringLayout

```java
public SpringLayout()
```

Constructs a new

SpringLayout

.

---

#### Constructor Detail

SpringLayout

```java
public SpringLayout()
```

Constructs a new

SpringLayout

.

---

#### SpringLayout

public SpringLayout()

Constructs a new

SpringLayout

.

Method Detail

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
c)
```

Has no effect,
since this layout manager does not
use a per-component string.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the string to be associated with the component
**Parameters:** c

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
c)
```

Removes the constraints associated with the specified component.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** c

- the component being removed from the container

- addLayoutComponent

```java
public void addLayoutComponent​(
Component
component,

Object
constraints)
```

If

constraints

is an instance of

SpringLayout.Constraints

,
associates the constraints with the specified component.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** component

- the component being added
**Parameters:** constraints

- the component's constraints
**See Also:** SpringLayout.Constraints

- getLayoutAlignmentX

```java
public float getLayoutAlignmentX​(
Container
p)
```

Returns 0.5f (centered).

**Specified by:** getLayoutAlignmentX

in interface

LayoutManager2
**Parameters:** p

- the target container
**Returns:** the x-axis alignment preference

- getLayoutAlignmentY

```java
public float getLayoutAlignmentY​(
Container
p)
```

Returns 0.5f (centered).

**Specified by:** getLayoutAlignmentY

in interface

LayoutManager2
**Parameters:** p

- the target container
**Returns:** the y-axis alignment preference

- putConstraint

```java
public void putConstraint​(
String
e1,

Component
c1,
int pad,

String
e2,

Component
c2)
```

Links edge

e1

of component

c1

to
edge

e2

of component

c2

,
with a fixed distance between the edges. This
constraint will cause the assignment

```java
value(e1, c1) = value(e2, c2) + pad
```

to take place during all subsequent layout operations.

**Parameters:** e1

- the edge of the dependent
**Parameters:** c1

- the component of the dependent
**Parameters:** pad

- the fixed distance between dependent and anchor
**Parameters:** e2

- the edge of the anchor
**Parameters:** c2

- the component of the anchor
**See Also:** putConstraint(String, Component, Spring, String, Component)

- putConstraint

```java
public void putConstraint​(
String
e1,

Component
c1,

Spring
s,

String
e2,

Component
c2)
```

Links edge

e1

of component

c1

to
edge

e2

of component

c2

. As edge

(e2, c2)

changes value, edge

(e1, c1)

will
be calculated by taking the (spring) sum of

(e2, c2)

and

s

.
Each edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.HORIZONTAL_CENTER

or

SpringLayout.BASELINE

.

**Parameters:** e1

- the edge of the dependent
**Parameters:** c1

- the component of the dependent
**Parameters:** s

- the spring linking dependent and anchor
**Parameters:** e2

- the edge of the anchor
**Parameters:** c2

- the component of the anchor
**See Also:** putConstraint(String, Component, int, String, Component)

,

NORTH

,

SOUTH

,

EAST

,

WEST

,

VERTICAL_CENTER

,

HORIZONTAL_CENTER

,

BASELINE

- getConstraints

```java
public
SpringLayout.Constraints
getConstraints​(
Component
c)
```

Returns the constraints for the specified component.
Note that,
unlike the

GridBagLayout

getConstraints

method,
this method does not clone constraints.
If no constraints
have been associated with this component,
this method
returns a default constraints object positioned at
0,0 relative to the parent's Insets and its width/height
constrained to the minimum, maximum, and preferred sizes of the
component. The size characteristics
are not frozen at the time this method is called;
instead this method returns a constraints object
whose characteristics track the characteristics
of the component as they change.

**Parameters:** c

- the component whose constraints will be returned
**Returns:** the constraints for the specified component

- getConstraint

```java
public
Spring
getConstraint​(
String
edgeName,

Component
c)
```

Returns the spring controlling the distance between
the specified edge of
the component and the top or left edge of its parent. This
method, instead of returning the current binding for the
edge, returns a proxy that tracks the characteristics
of the edge even if the edge is subsequently rebound.
Proxies are intended to be used in builder environments
where it is useful to allow the user to define the
constraints for a layout in any order. Proxies do, however,
provide the means to create cyclic dependencies amongst
the constraints of a layout. Such cycles are detected
internally by

SpringLayout

so that
the layout operation always terminates.

**Parameters:** edgeName

- must be one of

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.HORIZONTAL_CENTER

or

SpringLayout.BASELINE
**Parameters:** c

- the component whose edge spring is desired
**Returns:** a proxy for the spring controlling the distance between the
specified edge and the top or left edge of its parent
**See Also:** NORTH

,

SOUTH

,

EAST

,

WEST

,

VERTICAL_CENTER

,

HORIZONTAL_CENTER

,

BASELINE

---

#### Method Detail

addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
c)
```

Has no effect,
since this layout manager does not
use a per-component string.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the string to be associated with the component
**Parameters:** c

- the component to be added

---

#### addLayoutComponent

public void addLayoutComponent​(

String

name,

Component

c)

Has no effect,
since this layout manager does not
use a per-component string.

removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
c)
```

Removes the constraints associated with the specified component.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** c

- the component being removed from the container

---

#### removeLayoutComponent

public void removeLayoutComponent​(

Component

c)

Removes the constraints associated with the specified component.

addLayoutComponent

```java
public void addLayoutComponent​(
Component
component,

Object
constraints)
```

If

constraints

is an instance of

SpringLayout.Constraints

,
associates the constraints with the specified component.

**Specified by:** addLayoutComponent

in interface

LayoutManager2
**Parameters:** component

- the component being added
**Parameters:** constraints

- the component's constraints
**See Also:** SpringLayout.Constraints

---

#### addLayoutComponent

public void addLayoutComponent​(

Component

component,

Object

constraints)

If

constraints

is an instance of

SpringLayout.Constraints

,
associates the constraints with the specified component.

getLayoutAlignmentX

```java
public float getLayoutAlignmentX​(
Container
p)
```

Returns 0.5f (centered).

**Specified by:** getLayoutAlignmentX

in interface

LayoutManager2
**Parameters:** p

- the target container
**Returns:** the x-axis alignment preference

---

#### getLayoutAlignmentX

public float getLayoutAlignmentX​(

Container

p)

Returns 0.5f (centered).

getLayoutAlignmentY

```java
public float getLayoutAlignmentY​(
Container
p)
```

Returns 0.5f (centered).

**Specified by:** getLayoutAlignmentY

in interface

LayoutManager2
**Parameters:** p

- the target container
**Returns:** the y-axis alignment preference

---

#### getLayoutAlignmentY

public float getLayoutAlignmentY​(

Container

p)

Returns 0.5f (centered).

putConstraint

```java
public void putConstraint​(
String
e1,

Component
c1,
int pad,

String
e2,

Component
c2)
```

Links edge

e1

of component

c1

to
edge

e2

of component

c2

,
with a fixed distance between the edges. This
constraint will cause the assignment

```java
value(e1, c1) = value(e2, c2) + pad
```

to take place during all subsequent layout operations.

**Parameters:** e1

- the edge of the dependent
**Parameters:** c1

- the component of the dependent
**Parameters:** pad

- the fixed distance between dependent and anchor
**Parameters:** e2

- the edge of the anchor
**Parameters:** c2

- the component of the anchor
**See Also:** putConstraint(String, Component, Spring, String, Component)

---

#### putConstraint

public void putConstraint​(

String

e1,

Component

c1,
int pad,

String

e2,

Component

c2)

Links edge

e1

of component

c1

to
edge

e2

of component

c2

,
with a fixed distance between the edges. This
constraint will cause the assignment

```java
value(e1, c1) = value(e2, c2) + pad
```

to take place during all subsequent layout operations.

value(e1, c1) = value(e2, c2) + pad

putConstraint

```java
public void putConstraint​(
String
e1,

Component
c1,

Spring
s,

String
e2,

Component
c2)
```

Links edge

e1

of component

c1

to
edge

e2

of component

c2

. As edge

(e2, c2)

changes value, edge

(e1, c1)

will
be calculated by taking the (spring) sum of

(e2, c2)

and

s

.
Each edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.HORIZONTAL_CENTER

or

SpringLayout.BASELINE

.

**Parameters:** e1

- the edge of the dependent
**Parameters:** c1

- the component of the dependent
**Parameters:** s

- the spring linking dependent and anchor
**Parameters:** e2

- the edge of the anchor
**Parameters:** c2

- the component of the anchor
**See Also:** putConstraint(String, Component, int, String, Component)

,

NORTH

,

SOUTH

,

EAST

,

WEST

,

VERTICAL_CENTER

,

HORIZONTAL_CENTER

,

BASELINE

---

#### putConstraint

public void putConstraint​(

String

e1,

Component

c1,

Spring

s,

String

e2,

Component

c2)

Links edge

e1

of component

c1

to
edge

e2

of component

c2

. As edge

(e2, c2)

changes value, edge

(e1, c1)

will
be calculated by taking the (spring) sum of

(e2, c2)

and

s

.
Each edge must have one of the following values:

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.HORIZONTAL_CENTER

or

SpringLayout.BASELINE

.

getConstraints

```java
public
SpringLayout.Constraints
getConstraints​(
Component
c)
```

Returns the constraints for the specified component.
Note that,
unlike the

GridBagLayout

getConstraints

method,
this method does not clone constraints.
If no constraints
have been associated with this component,
this method
returns a default constraints object positioned at
0,0 relative to the parent's Insets and its width/height
constrained to the minimum, maximum, and preferred sizes of the
component. The size characteristics
are not frozen at the time this method is called;
instead this method returns a constraints object
whose characteristics track the characteristics
of the component as they change.

**Parameters:** c

- the component whose constraints will be returned
**Returns:** the constraints for the specified component

---

#### getConstraints

public

SpringLayout.Constraints

getConstraints​(

Component

c)

Returns the constraints for the specified component.
Note that,
unlike the

GridBagLayout

getConstraints

method,
this method does not clone constraints.
If no constraints
have been associated with this component,
this method
returns a default constraints object positioned at
0,0 relative to the parent's Insets and its width/height
constrained to the minimum, maximum, and preferred sizes of the
component. The size characteristics
are not frozen at the time this method is called;
instead this method returns a constraints object
whose characteristics track the characteristics
of the component as they change.

getConstraint

```java
public
Spring
getConstraint​(
String
edgeName,

Component
c)
```

Returns the spring controlling the distance between
the specified edge of
the component and the top or left edge of its parent. This
method, instead of returning the current binding for the
edge, returns a proxy that tracks the characteristics
of the edge even if the edge is subsequently rebound.
Proxies are intended to be used in builder environments
where it is useful to allow the user to define the
constraints for a layout in any order. Proxies do, however,
provide the means to create cyclic dependencies amongst
the constraints of a layout. Such cycles are detected
internally by

SpringLayout

so that
the layout operation always terminates.

**Parameters:** edgeName

- must be one of

SpringLayout.NORTH

,

SpringLayout.SOUTH

,

SpringLayout.EAST

,

SpringLayout.WEST

,

SpringLayout.VERTICAL_CENTER

,

SpringLayout.HORIZONTAL_CENTER

or

SpringLayout.BASELINE
**Parameters:** c

- the component whose edge spring is desired
**Returns:** a proxy for the spring controlling the distance between the
specified edge and the top or left edge of its parent
**See Also:** NORTH

,

SOUTH

,

EAST

,

WEST

,

VERTICAL_CENTER

,

HORIZONTAL_CENTER

,

BASELINE

---

#### getConstraint

public

Spring

getConstraint​(

String

edgeName,

Component

c)

Returns the spring controlling the distance between
the specified edge of
the component and the top or left edge of its parent. This
method, instead of returning the current binding for the
edge, returns a proxy that tracks the characteristics
of the edge even if the edge is subsequently rebound.
Proxies are intended to be used in builder environments
where it is useful to allow the user to define the
constraints for a layout in any order. Proxies do, however,
provide the means to create cyclic dependencies amongst
the constraints of a layout. Such cycles are detected
internally by

SpringLayout

so that
the layout operation always terminates.

---

