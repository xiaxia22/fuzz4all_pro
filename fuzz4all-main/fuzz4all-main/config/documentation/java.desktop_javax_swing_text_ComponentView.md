# Class ComponentView

**Source:** `java.desktop\javax\swing\text\ComponentView.html`

### Class Description

```java
public class
ComponentView

extends
View
```

Component decorator that implements the view interface. The
entire element is used to represent the component. This acts
as a gateway from the display-only View implementations to
interactive lightweight components (ie it allows components
to be embedded into the View hierarchy).

The component is placed relative to the text baseline
according to the value returned by

Component.getAlignmentY

. For Swing components
this value can be conveniently set using the method

JComponent.setAlignmentY

. For example, setting
a value of

0.75

will cause 75 percent of the
component to be above the baseline, and 25 percent of the
component to be below the baseline.

This class is implemented to do the extra work necessary to
work properly in the presence of multiple threads (i.e. from
asynchronous notification of model changes for example) by
ensuring that all component access is done on the event thread.

The component used is determined by the return value of the
createComponent method. The default implementation of this
method is to return the component held as an attribute of
the element (by calling StyleConstants.getComponent). A
limitation of this behavior is that the component cannot
be used by more than one text component (i.e. with a shared
model). Subclasses can remove this constraint by implementing
the createComponent to actually create a component based upon
some kind of specification contained in the attributes. The
ObjectView class in the html package is an example of a
ComponentView implementation that supports multiple component
views of a shared model.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public ComponentView​(
Element
elem)

Creates a new ComponentView object.

**Parameters:**
- elem

- the element to decorate

---

### Method Details

#### protected
Component
createComponent()

Create the component that is associated with
this view. This will be called when it has
been determined that a new component is needed.
This would result from a call to setParent or
as a result of being notified that attributes
have changed.

**Returns:**
- the component that is associated with
this view

---

#### public final
Component
getComponent()

Fetch the component associated with the view.

**Returns:**
- the component associated with the view

---

#### public void paint​(
Graphics
g,

Shape
a)

The real paint behavior occurs naturally from the association
that the component has with its parent container (the same
container hosting this view). This is implemented to do nothing.

**Specified by:**
- paint

in class

View

**Parameters:**
- g

- the graphics context
- a

- the shape

**See Also:**
- View.paint(java.awt.Graphics, java.awt.Shape)

---

#### public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis. This is implemented to return the value
returned by Component.getPreferredSize along the
axis of interest.

**Specified by:**
- getPreferredSpan

in class

View

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**Throws:**
- IllegalArgumentException

- for an invalid axis

**See Also:**
- View.getPreferredSpan(int)

---

#### public float getMinimumSpan​(int axis)

Determines the minimum span for this view along an
axis. This is implemented to return the value
returned by Component.getMinimumSize along the
axis of interest.

**Overrides:**
- getMinimumSpan

in class

View

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**Throws:**
- IllegalArgumentException

- for an invalid axis

**See Also:**
- View.getPreferredSpan(int)

---

#### public float getMaximumSpan​(int axis)

Determines the maximum span for this view along an
axis. This is implemented to return the value
returned by Component.getMaximumSize along the
axis of interest.

**Overrides:**
- getMaximumSpan

in class

View

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**Throws:**
- IllegalArgumentException

- for an invalid axis

**See Also:**
- View.getPreferredSpan(int)

---

#### public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment of the
embedded component.

**Overrides:**
- getAlignment

in class

View

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the desired alignment. This should be a value
between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin. An alignment of 0.5 would be the
center of the view.

---

#### public void setParent​(
View
p)

Sets the parent for a child view.
The parent calls this on the child to tell it who its
parent is, giving the view access to things like
the hosting Container. The superclass behavior is
executed, followed by a call to createComponent if
the parent view parameter is non-null and a component
has not yet been created. The embedded components parent
is then set to the value returned by

getContainer

.
If the parent view parameter is null, this view is being
cleaned up, thus the component is removed from its parent.

The changing of the component hierarchy will
touch the component lock, which is the one thing
that is not safe from the View hierarchy. Therefore,
this functionality is executed immediately if on the
event thread, or is queued on the event queue if
called from another thread (notification of change
from an asynchronous update).

**Overrides:**
- setParent

in class

View

**Parameters:**
- p

- the parent

---

#### public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException

Provides a mapping from the coordinate space of the model to
that of the view.

**Specified by:**
- modelToView

in class

View

**Parameters:**
- pos

- the position to convert >=0
- a

- the allocated region to render into
- b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward

**Returns:**
- the bounding box of the given position is returned

**Throws:**
- BadLocationException

- if the given position does not
represent a valid location in the associated document

**See Also:**
- View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:**
- viewToModel

in class

View

**Parameters:**
- x

- the X coordinate >=0
- y

- the Y coordinate >=0
- a

- the allocated region to render into
- bias

- the returned bias

**Returns:**
- the location within the model that best represents
the given point in the view

**See Also:**
- View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

### Additional Sections

#### Class ComponentView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.ComponentView

javax.swing.text.View

- javax.swing.text.ComponentView

javax.swing.text.ComponentView

**All Implemented Interfaces:** SwingConstants

**Direct Known Subclasses:** FormView

,

ObjectView

```java
public class
ComponentView

extends
View
```

Component decorator that implements the view interface. The
entire element is used to represent the component. This acts
as a gateway from the display-only View implementations to
interactive lightweight components (ie it allows components
to be embedded into the View hierarchy).

The component is placed relative to the text baseline
according to the value returned by

Component.getAlignmentY

. For Swing components
this value can be conveniently set using the method

JComponent.setAlignmentY

. For example, setting
a value of

0.75

will cause 75 percent of the
component to be above the baseline, and 25 percent of the
component to be below the baseline.

This class is implemented to do the extra work necessary to
work properly in the presence of multiple threads (i.e. from
asynchronous notification of model changes for example) by
ensuring that all component access is done on the event thread.

The component used is determined by the return value of the
createComponent method. The default implementation of this
method is to return the component held as an attribute of
the element (by calling StyleConstants.getComponent). A
limitation of this behavior is that the component cannot
be used by more than one text component (i.e. with a shared
model). Subclasses can remove this constraint by implementing
the createComponent to actually create a component based upon
some kind of specification contained in the attributes. The
ObjectView class in the html package is an example of a
ComponentView implementation that supports multiple component
views of a shared model.

public class

ComponentView

extends

View

Component decorator that implements the view interface. The
entire element is used to represent the component. This acts
as a gateway from the display-only View implementations to
interactive lightweight components (ie it allows components
to be embedded into the View hierarchy).

The component is placed relative to the text baseline
according to the value returned by

Component.getAlignmentY

. For Swing components
this value can be conveniently set using the method

JComponent.setAlignmentY

. For example, setting
a value of

0.75

will cause 75 percent of the
component to be above the baseline, and 25 percent of the
component to be below the baseline.

This class is implemented to do the extra work necessary to
work properly in the presence of multiple threads (i.e. from
asynchronous notification of model changes for example) by
ensuring that all component access is done on the event thread.

The component used is determined by the return value of the
createComponent method. The default implementation of this
method is to return the component held as an attribute of
the element (by calling StyleConstants.getComponent). A
limitation of this behavior is that the component cannot
be used by more than one text component (i.e. with a shared
model). Subclasses can remove this constraint by implementing
the createComponent to actually create a component based upon
some kind of specification contained in the attributes. The
ObjectView class in the html package is an example of a
ComponentView implementation that supports multiple component
views of a shared model.

The component is placed relative to the text baseline
according to the value returned by

Component.getAlignmentY

. For Swing components
this value can be conveniently set using the method

JComponent.setAlignmentY

. For example, setting
a value of

0.75

will cause 75 percent of the
component to be above the baseline, and 25 percent of the
component to be below the baseline.

This class is implemented to do the extra work necessary to
work properly in the presence of multiple threads (i.e. from
asynchronous notification of model changes for example) by
ensuring that all component access is done on the event thread.

The component used is determined by the return value of the
createComponent method. The default implementation of this
method is to return the component held as an attribute of
the element (by calling StyleConstants.getComponent). A
limitation of this behavior is that the component cannot
be used by more than one text component (i.e. with a shared
model). Subclasses can remove this constraint by implementing
the createComponent to actually create a component based upon
some kind of specification contained in the attributes. The
ObjectView class in the html package is an example of a
ComponentView implementation that supports multiple component
views of a shared model.

This class is implemented to do the extra work necessary to
work properly in the presence of multiple threads (i.e. from
asynchronous notification of model changes for example) by
ensuring that all component access is done on the event thread.

The component used is determined by the return value of the
createComponent method. The default implementation of this
method is to return the component held as an attribute of
the element (by calling StyleConstants.getComponent). A
limitation of this behavior is that the component cannot
be used by more than one text component (i.e. with a shared
model). Subclasses can remove this constraint by implementing
the createComponent to actually create a component based upon
some kind of specification contained in the attributes. The
ObjectView class in the html package is an example of a
ComponentView implementation that supports multiple component
views of a shared model.

The component used is determined by the return value of the
createComponent method. The default implementation of this
method is to return the component held as an attribute of
the element (by calling StyleConstants.getComponent). A
limitation of this behavior is that the component cannot
be used by more than one text component (i.e. with a shared
model). Subclasses can remove this constraint by implementing
the createComponent to actually create a component based upon
some kind of specification contained in the attributes. The
ObjectView class in the html package is an example of a
ComponentView implementation that supports multiple component
views of a shared model.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ComponentView

​(

Element

elem)

Creates a new ComponentView object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Component

createComponent

()

Create the component that is associated with
this view.

float

getAlignment

​(int axis)

Determines the desired alignment for this view along an
axis.

Component

getComponent

()

Fetch the component associated with the view.

float

getMaximumSpan

​(int axis)

Determines the maximum span for this view along an
axis.

float

getMinimumSpan

​(int axis)

Determines the minimum span for this view along an
axis.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the coordinate space of the model to
that of the view.

void

paint

​(

Graphics

g,

Shape

a)

The real paint behavior occurs naturally from the association
that the component has with its parent container (the same
container hosting this view).

void

setParent

​(

View

p)

Sets the parent for a child view.

int

viewToModel

​(float x,
float y,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

changedUpdate

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

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

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Field Summary

Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

---

#### Fields declared in class javax.swing.text. View

Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Fields declared in interface javax.swing. SwingConstants

Constructor Summary

Constructors

Constructor

Description

ComponentView

​(

Element

elem)

Creates a new ComponentView object.

---

#### Constructor Summary

Creates a new ComponentView object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Component

createComponent

()

Create the component that is associated with
this view.

float

getAlignment

​(int axis)

Determines the desired alignment for this view along an
axis.

Component

getComponent

()

Fetch the component associated with the view.

float

getMaximumSpan

​(int axis)

Determines the maximum span for this view along an
axis.

float

getMinimumSpan

​(int axis)

Determines the minimum span for this view along an
axis.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the coordinate space of the model to
that of the view.

void

paint

​(

Graphics

g,

Shape

a)

The real paint behavior occurs naturally from the association
that the component has with its parent container (the same
container hosting this view).

void

setParent

​(

View

p)

Sets the parent for a child view.

int

viewToModel

​(float x,
float y,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

changedUpdate

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

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

Create the component that is associated with
this view.

Determines the desired alignment for this view along an
axis.

Fetch the component associated with the view.

Determines the maximum span for this view along an
axis.

Determines the minimum span for this view along an
axis.

Determines the preferred span for this view along an
axis.

Provides a mapping from the coordinate space of the model to
that of the view.

The real paint behavior occurs naturally from the association
that the component has with its parent container (the same
container hosting this view).

Sets the parent for a child view.

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

Methods declared in class javax.swing.text.

View

append

,

breakView

,

changedUpdate

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

---

#### Methods declared in class javax.swing.text. View

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

- ComponentView

```java
public ComponentView​(
Element
elem)
```

Creates a new ComponentView object.

**Parameters:** elem

- the element to decorate

============ METHOD DETAIL ==========

- Method Detail

- createComponent

```java
protected
Component
createComponent()
```

Create the component that is associated with
this view. This will be called when it has
been determined that a new component is needed.
This would result from a call to setParent or
as a result of being notified that attributes
have changed.

**Returns:** the component that is associated with
this view

- getComponent

```java
public final
Component
getComponent()
```

Fetch the component associated with the view.

**Returns:** the component associated with the view

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

The real paint behavior occurs naturally from the association
that the component has with its parent container (the same
container hosting this view). This is implemented to do nothing.

**Specified by:** paint

in class

View
**Parameters:** g

- the graphics context
**Parameters:** a

- the shape
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis. This is implemented to return the value
returned by Component.getPreferredSize along the
axis of interest.

**Specified by:** getPreferredSpan

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an
axis. This is implemented to return the value
returned by Component.getMinimumSize along the
axis of interest.

**Overrides:** getMinimumSpan

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis. This is implemented to return the value
returned by Component.getMaximumSize along the
axis of interest.

**Overrides:** getMaximumSpan

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment of the
embedded component.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the desired alignment. This should be a value
between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin. An alignment of 0.5 would be the
center of the view.

- setParent

```java
public void setParent​(
View
p)
```

Sets the parent for a child view.
The parent calls this on the child to tell it who its
parent is, giving the view access to things like
the hosting Container. The superclass behavior is
executed, followed by a call to createComponent if
the parent view parameter is non-null and a component
has not yet been created. The embedded components parent
is then set to the value returned by

getContainer

.
If the parent view parameter is null, this view is being
cleaned up, thus the component is removed from its parent.

The changing of the component hierarchy will
touch the component lock, which is the one thing
that is not safe from the View hierarchy. Therefore,
this functionality is executed immediately if on the
event thread, or is queued on the event queue if
called from another thread (notification of change
from an asynchronous update).

**Overrides:** setParent

in class

View
**Parameters:** p

- the parent

- modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the coordinate space of the model to
that of the view.

**Specified by:** modelToView

in class

View
**Parameters:** pos

- the position to convert >=0
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position is returned
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- viewToModel

```java
public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate >=0
**Parameters:** y

- the Y coordinate >=0
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents
the given point in the view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

Constructor Detail

- ComponentView

```java
public ComponentView​(
Element
elem)
```

Creates a new ComponentView object.

**Parameters:** elem

- the element to decorate

---

#### Constructor Detail

ComponentView

```java
public ComponentView​(
Element
elem)
```

Creates a new ComponentView object.

**Parameters:** elem

- the element to decorate

---

#### ComponentView

public ComponentView​(

Element

elem)

Creates a new ComponentView object.

Method Detail

- createComponent

```java
protected
Component
createComponent()
```

Create the component that is associated with
this view. This will be called when it has
been determined that a new component is needed.
This would result from a call to setParent or
as a result of being notified that attributes
have changed.

**Returns:** the component that is associated with
this view

- getComponent

```java
public final
Component
getComponent()
```

Fetch the component associated with the view.

**Returns:** the component associated with the view

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

The real paint behavior occurs naturally from the association
that the component has with its parent container (the same
container hosting this view). This is implemented to do nothing.

**Specified by:** paint

in class

View
**Parameters:** g

- the graphics context
**Parameters:** a

- the shape
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis. This is implemented to return the value
returned by Component.getPreferredSize along the
axis of interest.

**Specified by:** getPreferredSpan

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an
axis. This is implemented to return the value
returned by Component.getMinimumSize along the
axis of interest.

**Overrides:** getMinimumSpan

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis. This is implemented to return the value
returned by Component.getMaximumSize along the
axis of interest.

**Overrides:** getMaximumSpan

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment of the
embedded component.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the desired alignment. This should be a value
between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin. An alignment of 0.5 would be the
center of the view.

- setParent

```java
public void setParent​(
View
p)
```

Sets the parent for a child view.
The parent calls this on the child to tell it who its
parent is, giving the view access to things like
the hosting Container. The superclass behavior is
executed, followed by a call to createComponent if
the parent view parameter is non-null and a component
has not yet been created. The embedded components parent
is then set to the value returned by

getContainer

.
If the parent view parameter is null, this view is being
cleaned up, thus the component is removed from its parent.

The changing of the component hierarchy will
touch the component lock, which is the one thing
that is not safe from the View hierarchy. Therefore,
this functionality is executed immediately if on the
event thread, or is queued on the event queue if
called from another thread (notification of change
from an asynchronous update).

**Overrides:** setParent

in class

View
**Parameters:** p

- the parent

- modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the coordinate space of the model to
that of the view.

**Specified by:** modelToView

in class

View
**Parameters:** pos

- the position to convert >=0
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position is returned
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- viewToModel

```java
public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate >=0
**Parameters:** y

- the Y coordinate >=0
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents
the given point in the view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### Method Detail

createComponent

```java
protected
Component
createComponent()
```

Create the component that is associated with
this view. This will be called when it has
been determined that a new component is needed.
This would result from a call to setParent or
as a result of being notified that attributes
have changed.

**Returns:** the component that is associated with
this view

---

#### createComponent

protected

Component

createComponent()

Create the component that is associated with
this view. This will be called when it has
been determined that a new component is needed.
This would result from a call to setParent or
as a result of being notified that attributes
have changed.

getComponent

```java
public final
Component
getComponent()
```

Fetch the component associated with the view.

**Returns:** the component associated with the view

---

#### getComponent

public final

Component

getComponent()

Fetch the component associated with the view.

paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

The real paint behavior occurs naturally from the association
that the component has with its parent container (the same
container hosting this view). This is implemented to do nothing.

**Specified by:** paint

in class

View
**Parameters:** g

- the graphics context
**Parameters:** a

- the shape
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

---

#### paint

public void paint​(

Graphics

g,

Shape

a)

The real paint behavior occurs naturally from the association
that the component has with its parent container (the same
container hosting this view). This is implemented to do nothing.

getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis. This is implemented to return the value
returned by Component.getPreferredSize along the
axis of interest.

**Specified by:** getPreferredSpan

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

---

#### getPreferredSpan

public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis. This is implemented to return the value
returned by Component.getPreferredSize along the
axis of interest.

getMinimumSpan

```java
public float getMinimumSpan​(int axis)
```

Determines the minimum span for this view along an
axis. This is implemented to return the value
returned by Component.getMinimumSize along the
axis of interest.

**Overrides:** getMinimumSpan

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

---

#### getMinimumSpan

public float getMinimumSpan​(int axis)

Determines the minimum span for this view along an
axis. This is implemented to return the value
returned by Component.getMinimumSize along the
axis of interest.

getMaximumSpan

```java
public float getMaximumSpan​(int axis)
```

Determines the maximum span for this view along an
axis. This is implemented to return the value
returned by Component.getMaximumSize along the
axis of interest.

**Overrides:** getMaximumSpan

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >=0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**Throws:** IllegalArgumentException

- for an invalid axis
**See Also:** View.getPreferredSpan(int)

---

#### getMaximumSpan

public float getMaximumSpan​(int axis)

Determines the maximum span for this view along an
axis. This is implemented to return the value
returned by Component.getMaximumSize along the
axis of interest.

getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment of the
embedded component.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the desired alignment. This should be a value
between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin. An alignment of 0.5 would be the
center of the view.

---

#### getAlignment

public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment of the
embedded component.

setParent

```java
public void setParent​(
View
p)
```

Sets the parent for a child view.
The parent calls this on the child to tell it who its
parent is, giving the view access to things like
the hosting Container. The superclass behavior is
executed, followed by a call to createComponent if
the parent view parameter is non-null and a component
has not yet been created. The embedded components parent
is then set to the value returned by

getContainer

.
If the parent view parameter is null, this view is being
cleaned up, thus the component is removed from its parent.

The changing of the component hierarchy will
touch the component lock, which is the one thing
that is not safe from the View hierarchy. Therefore,
this functionality is executed immediately if on the
event thread, or is queued on the event queue if
called from another thread (notification of change
from an asynchronous update).

**Overrides:** setParent

in class

View
**Parameters:** p

- the parent

---

#### setParent

public void setParent​(

View

p)

Sets the parent for a child view.
The parent calls this on the child to tell it who its
parent is, giving the view access to things like
the hosting Container. The superclass behavior is
executed, followed by a call to createComponent if
the parent view parameter is non-null and a component
has not yet been created. The embedded components parent
is then set to the value returned by

getContainer

.
If the parent view parameter is null, this view is being
cleaned up, thus the component is removed from its parent.

The changing of the component hierarchy will
touch the component lock, which is the one thing
that is not safe from the View hierarchy. Therefore,
this functionality is executed immediately if on the
event thread, or is queued on the event queue if
called from another thread (notification of change
from an asynchronous update).

The changing of the component hierarchy will
touch the component lock, which is the one thing
that is not safe from the View hierarchy. Therefore,
this functionality is executed immediately if on the
event thread, or is queued on the event queue if
called from another thread (notification of change
from an asynchronous update).

modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the coordinate space of the model to
that of the view.

**Specified by:** modelToView

in class

View
**Parameters:** pos

- the position to convert >=0
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position is returned
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### modelToView

public

Shape

modelToView​(int pos,

Shape

a,

Position.Bias

b)
throws

BadLocationException

Provides a mapping from the coordinate space of the model to
that of the view.

Position.Bias.Forward

Position.Bias.Backward

viewToModel

```java
public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate >=0
**Parameters:** y

- the Y coordinate >=0
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents
the given point in the view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### viewToModel

public int viewToModel​(float x,
float y,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

---

