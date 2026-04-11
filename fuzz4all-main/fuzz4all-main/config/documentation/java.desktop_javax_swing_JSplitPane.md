# Class JSplitPane

**Source:** `java.desktop\javax\swing\JSplitPane.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI")
public class
JSplitPane

extends
JComponent

implements
Accessible
```

JSplitPane

is used to divide two (and only two)

Component

s. The two

Component

s
are graphically divided based on the look and feel
implementation, and the two

Component

s can then be
interactively resized by the user.
Information on using

JSplitPane

is in

How to Use Split Panes

in

The Java Tutorial

.

The two

Component

s in a split pane can be aligned
left to right using

JSplitPane.HORIZONTAL_SPLIT

, or top to bottom using

JSplitPane.VERTICAL_SPLIT

.
The preferred way to change the size of the

Component

s
is to invoke

setDividerLocation

where

location

is either
the new x or y position, depending on the orientation of the

JSplitPane

.

To resize the

Component

s to their preferred sizes invoke

resetToPreferredSizes

.

When the user is resizing the

Component

s the minimum
size of the

Components

is used to determine the
maximum/minimum position the

Component

s
can be set to. If the minimum size of the two
components is greater than the size of the split pane the divider
will not allow you to resize it. To alter the minimum size of a

JComponent

, see

JComponent.setMinimumSize(java.awt.Dimension)

.

When the user resizes the split pane the new space is distributed between
the two components based on the

resizeWeight

property.
A value of 0,
the default, indicates the right/bottom component gets all the space,
where as a value of 1 indicates the left/top component gets all the space.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

#### public static final int VERTICAL_SPLIT

Vertical split indicates the

Component

s are
split along the y axis. For example the two

Component

s will be split one on top of the other.

**See Also:**
- Constant Field Values

---

#### public static final int HORIZONTAL_SPLIT

Horizontal split indicates the

Component

s are
split along the x axis. For example the two

Component

s will be split one to the left of the
other.

**See Also:**
- Constant Field Values

---

#### public static final
String
LEFT

Used to add a

Component

to the left of the other

Component

.

**See Also:**
- Constant Field Values

---

#### public static final
String
RIGHT

Used to add a

Component

to the right of the other

Component

.

**See Also:**
- Constant Field Values

---

#### public static final
String
TOP

Used to add a

Component

above the other

Component

.

**See Also:**
- Constant Field Values

---

#### public static final
String
BOTTOM

Used to add a

Component

below the other

Component

.

**See Also:**
- Constant Field Values

---

#### public static final
String
DIVIDER

Used to add a

Component

that will represent the divider.

**See Also:**
- Constant Field Values

---

#### public static final
String
ORIENTATION_PROPERTY

Bound property name for orientation (horizontal or vertical).

**See Also:**
- Constant Field Values

---

#### public static final
String
CONTINUOUS_LAYOUT_PROPERTY

Bound property name for continuousLayout.

**See Also:**
- Constant Field Values

---

#### public static final
String
DIVIDER_SIZE_PROPERTY

Bound property name for border.

**See Also:**
- Constant Field Values

---

#### public static final
String
ONE_TOUCH_EXPANDABLE_PROPERTY

Bound property for oneTouchExpandable.

**See Also:**
- Constant Field Values

---

#### public static final
String
LAST_DIVIDER_LOCATION_PROPERTY

Bound property for lastLocation.

**See Also:**
- Constant Field Values

---

#### public static final
String
DIVIDER_LOCATION_PROPERTY

Bound property for the dividerLocation.

**See Also:**
- Constant Field Values

**Since:**
- 1.3

---

#### public static final
String
RESIZE_WEIGHT_PROPERTY

Bound property for weight.

**See Also:**
- Constant Field Values

**Since:**
- 1.3

---

#### protected int orientation

How the views are split.

---

#### protected boolean continuousLayout

Whether or not the views are continuously redisplayed while
resizing.

---

#### protected
Component
leftComponent

The left or top component.

---

#### protected
Component
rightComponent

The right or bottom component.

---

#### protected int dividerSize

Size of the divider.

---

#### protected boolean oneTouchExpandable

Is a little widget provided to quickly expand/collapse the
split pane?

---

#### protected int lastDividerLocation

Previous location of the split pane.

---

### Constructor Details

#### public JSplitPane()

Creates a new

JSplitPane

configured to arrange the child
components side-by-side horizontally, using two buttons for the components.

---

#### @ConstructorProperties
("orientation")
public JSplitPane​(int newOrientation)

Creates a new

JSplitPane

configured with the
specified orientation.

**Parameters:**
- newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

**Throws:**
- IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT.

---

#### public JSplitPane​(int newOrientation,
boolean newContinuousLayout)

Creates a new

JSplitPane

with the specified
orientation and redrawing style.

**Parameters:**
- newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
- newContinuousLayout

- a boolean, true for the components to
redraw continuously as the divider changes position, false
to wait until the divider position stops changing to redraw

**Throws:**
- IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT

---

#### public JSplitPane​(int newOrientation,

Component
newLeftComponent,

Component
newRightComponent)

Creates a new

JSplitPane

with the specified
orientation and the specified components.

**Parameters:**
- newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
- newLeftComponent

- the

Component

that will
appear on the left
of a horizontally-split pane, or at the top of a
vertically-split pane
- newRightComponent

- the

Component

that will
appear on the right
of a horizontally-split pane, or at the bottom of a
vertically-split pane

**Throws:**
- IllegalArgumentException

- if

orientation

is not one of: HORIZONTAL_SPLIT or VERTICAL_SPLIT

---

#### public JSplitPane​(int newOrientation,
boolean newContinuousLayout,

Component
newLeftComponent,

Component
newRightComponent)

Creates a new

JSplitPane

with the specified
orientation and
redrawing style, and with the specified components.

**Parameters:**
- newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
- newContinuousLayout

- a boolean, true for the components to
redraw continuously as the divider changes position, false
to wait until the divider position stops changing to redraw
- newLeftComponent

- the

Component

that will
appear on the left
of a horizontally-split pane, or at the top of a
vertically-split pane
- newRightComponent

- the

Component

that will
appear on the right
of a horizontally-split pane, or at the bottom of a
vertically-split pane

**Throws:**
- IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT

---

### Method Details

#### public void setUI​(
SplitPaneUI
ui)

Sets the L&F object that renders this component.

**Parameters:**
- ui

- the

SplitPaneUI

L&F object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The L&F object that renders this component.")
public
SplitPaneUI
getUI()

Returns the

SplitPaneUI

that is providing the
current look and feel.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

SplitPaneUI

object that renders this component

---

#### public void updateUI()

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:**
- updateUI

in class

JComponent

**See Also:**
- JComponent.updateUI()

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="A string that specifies the name of the L&F class.")
public
String
getUIClassID()

Returns the name of the L&F class that renders this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "SplitPaneUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### @BeanProperty
(
description
="The size of the divider.")
public void setDividerSize​(int newSize)

Sets the size of the divider.

**Parameters:**
- newSize

- an integer giving the size of the divider in pixels

---

#### public int getDividerSize()

Returns the size of the divider.

**Returns:**
- an integer giving the size of the divider in pixels

---

#### public void setLeftComponent​(
Component
comp)

Sets the component to the left (or above) the divider.

**Parameters:**
- comp

- the

Component

to display in that position

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="The component to the left (or above) the divider.")
public
Component
getLeftComponent()

Returns the component to the left (or above) the divider.

**Returns:**
- the

Component

displayed in that position

---

#### @BeanProperty
(
bound
=false,

description
="The component above, or to the left of the divider.")
public void setTopComponent​(
Component
comp)

Sets the component above, or to the left of the divider.

**Parameters:**
- comp

- the

Component

to display in that position

---

#### public
Component
getTopComponent()

Returns the component above, or to the left of the divider.

**Returns:**
- the

Component

displayed in that position

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="The component to the right (or below) the divider.")
public void setRightComponent​(
Component
comp)

Sets the component to the right (or below) the divider.

**Parameters:**
- comp

- the

Component

to display in that position

---

#### public
Component
getRightComponent()

Returns the component to the right (or below) the divider.

**Returns:**
- the

Component

displayed in that position

---

#### @BeanProperty
(
bound
=false,

description
="The component below, or to the right of the divider.")
public void setBottomComponent​(
Component
comp)

Sets the component below, or to the right of the divider.

**Parameters:**
- comp

- the

Component

to display in that position

---

#### public
Component
getBottomComponent()

Returns the component below, or to the right of the divider.

**Returns:**
- the

Component

displayed in that position

---

#### @BeanProperty
(
description
="UI widget on the divider to quickly expand/collapse the divider.")
public void setOneTouchExpandable​(boolean newValue)

Sets the value of the

oneTouchExpandable

property,
which must be

true

for the

JSplitPane

to provide a UI widget
on the divider to quickly expand/collapse the divider.
The default value of this property is

false

.
Some look and feels might not support one-touch expanding;
they will ignore this property.

**Parameters:**
- newValue

-

true

to specify that the split pane should provide a
collapse/expand widget

**See Also:**
- isOneTouchExpandable()

---

#### public boolean isOneTouchExpandable()

Gets the

oneTouchExpandable

property.

**Returns:**
- the value of the

oneTouchExpandable

property

**See Also:**
- setOneTouchExpandable(boolean)

---

#### @BeanProperty
(
description
="The last location the divider was at.")
public void setLastDividerLocation​(int newLastLocation)

Sets the last location the divider was at to

newLastLocation

.

**Parameters:**
- newLastLocation

- an integer specifying the last divider location
in pixels, from the left (or upper) edge of the pane to the
left (or upper) edge of the divider

---

#### public int getLastDividerLocation()

Returns the last location the divider was at.

**Returns:**
- an integer specifying the last divider location as a count
of pixels from the left (or upper) edge of the pane to the
left (or upper) edge of the divider

---

#### @BeanProperty
(
enumerationValues
={"JSplitPane.HORIZONTAL_SPLIT","JSplitPane.VERTICAL_SPLIT"},

description
="The orientation, or how the splitter is divided.")
public void setOrientation​(int orientation)

Sets the orientation, or how the splitter is divided. The options
are:

- JSplitPane.VERTICAL_SPLIT (above/below orientation of components)

JSplitPane.HORIZONTAL_SPLIT (left/right orientation of components)

**Parameters:**
- orientation

- an integer specifying the orientation

**Throws:**
- IllegalArgumentException

- if orientation is not one of:
HORIZONTAL_SPLIT or VERTICAL_SPLIT.

---

#### public int getOrientation()

Returns the orientation.

**Returns:**
- an integer giving the orientation

**See Also:**
- setOrientation(int)

---

#### @BeanProperty
(
description
="Whether the child components are continuously redisplayed and laid out during user intervention.")
public void setContinuousLayout​(boolean newContinuousLayout)

Sets the value of the

continuousLayout

property,
which must be

true

for the child components
to be continuously
redisplayed and laid out during user intervention.
The default value of this property is look and feel dependent.
Some look and feels might not support continuous layout;
they will ignore this property.

**Parameters:**
- newContinuousLayout

-

true

if the components
should continuously be redrawn as the divider changes position

**See Also:**
- isContinuousLayout()

---

#### public boolean isContinuousLayout()

Gets the

continuousLayout

property.

**Returns:**
- the value of the

continuousLayout

property

**See Also:**
- setContinuousLayout(boolean)

---

#### @BeanProperty
(
description
="Specifies how to distribute extra space when the split pane resizes.")
public void setResizeWeight​(double value)

Specifies how to distribute extra space when the size of the split pane
changes. A value of 0, the default,
indicates the right/bottom component gets all the extra space (the
left/top component acts fixed), where as a value of 1 specifies the
left/top component gets all the extra space (the right/bottom component
acts fixed). Specifically, the left/top component gets (weight * diff)
extra space and the right/bottom component gets (1 - weight) * diff
extra space.

**Parameters:**
- value

- as described above

**Throws:**
- IllegalArgumentException

- if

value

is < 0 or > 1

**Since:**
- 1.3

---

#### public double getResizeWeight()

Returns the number that determines how extra space is distributed.

**Returns:**
- how extra space is to be distributed on a resize of the
split pane

**Since:**
- 1.3

---

#### public void resetToPreferredSizes()

Lays out the

JSplitPane

layout based on the preferred size
of the children components. This will likely result in changing
the divider location.

---

#### @BeanProperty
(
description
="The location of the divider.")
public void setDividerLocation​(double proportionalLocation)

Sets the divider location as a percentage of the

JSplitPane

's size.

This method is implemented in terms of

setDividerLocation(int)

.
This method immediately changes the size of the split pane based on
its current size. If the split pane is not correctly realized and on
screen, this method will have no effect (new divider location will
become (current size * proportionalLocation) which is 0).

**Parameters:**
- proportionalLocation

- a double-precision floating point value
that specifies a percentage, from zero (top/left) to 1.0
(bottom/right)

**Throws:**
- IllegalArgumentException

- if the specified location is < 0
or > 1.0

---

#### @BeanProperty
(
description
="The location of the divider.")
public void setDividerLocation​(int location)

Sets the location of the divider. This is passed off to the
look and feel implementation, and then listeners are notified. A value
less than 0 implies the divider should be reset to a value that
attempts to honor the preferred size of the left/top component.
After notifying the listeners, the last divider location is updated,
via

setLastDividerLocation

.

**Parameters:**
- location

- an int specifying a UI-specific value (typically a
pixel count)

---

#### public int getDividerLocation()

Returns the last value passed to

setDividerLocation

.
The value returned from this method may differ from the actual
divider location (if

setDividerLocation

was passed a
value bigger than the current size).

**Returns:**
- an integer specifying the location of the divider

---

#### @BeanProperty
(
bound
=false,

description
="The minimum location of the divider from the L&F.")
public int getMinimumDividerLocation()

Returns the minimum location of the divider from the look and feel
implementation.

**Returns:**
- an integer specifying a UI-specific value for the minimum
location (typically a pixel count); or -1 if the UI is

null

---

#### @BeanProperty
(
bound
=false)
public int getMaximumDividerLocation()

Returns the maximum location of the divider from the look and feel
implementation.

**Returns:**
- an integer specifying a UI-specific value for the maximum
location (typically a pixel count); or -1 if the UI is

null

---

#### public void remove​(
Component
component)

Removes the child component,

component

from the
pane. Resets the

leftComponent

or

rightComponent

instance variable, as necessary.

**Overrides:**
- remove

in class

Container

**Parameters:**
- component

- the

Component

to remove

**See Also:**
- Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.remove(int)

---

#### public void remove​(int index)

Removes the

Component

at the specified index.
Updates the

leftComponent

and

rightComponent

instance variables as necessary, and then messages super.

**Overrides:**
- remove

in class

Container

**Parameters:**
- index

- an integer specifying the component to remove, where
1 specifies the left/top component and 2 specifies the
bottom/right component

**See Also:**
- Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

---

#### public void removeAll()

Removes all the child components from the split pane. Resets the

leftComonent

and

rightComponent

instance variables.

**Overrides:**
- removeAll

in class

Container

**See Also:**
- Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

---

#### @BeanProperty
(
hidden
=true)
public boolean isValidateRoot()

Returns true, so that calls to

revalidate

on any descendant of this

JSplitPane

will cause a request to be queued that
will validate the

JSplitPane

and all its descendants.

**Overrides:**
- isValidateRoot

in class

JComponent

**Returns:**
- true

**See Also:**
- JComponent.revalidate()

,

Container.isValidateRoot()

---

#### protected void addImpl​(
Component
comp,

Object
constraints,
int index)

Adds the specified component to this split pane.
If

constraints

identifies the left/top or
right/bottom child component, and a component with that identifier
was previously added, it will be removed and then

comp

will be added in its place. If

constraints

is not
one of the known identifiers the layout manager may throw an

IllegalArgumentException

.

The possible constraints objects (Strings) are:

- JSplitPane.TOP

JSplitPane.LEFT

JSplitPane.BOTTOM

JSplitPane.RIGHT

If the

constraints

object is

null

,
the component is added in the
first available position (left/top if open, else right/bottom).

**Overrides:**
- addImpl

in class

Container

**Parameters:**
- comp

- the component to add
- constraints

- an

Object

specifying the
layout constraints
(position) for this component
- index

- an integer specifying the index in the container's
list.

**Throws:**
- IllegalArgumentException

- if the

constraints

object does not match an existing component

**See Also:**
- Container.addImpl(Component, Object, int)

---

#### protected void paintChildren​(
Graphics
g)

Subclassed to message the UI with

finishedPaintingChildren

after super has been messaged, as well as painting the border.

**Overrides:**
- paintChildren

in class

JComponent

**Parameters:**
- g

- the

Graphics

context within which to paint

**See Also:**
- JComponent.paint(java.awt.Graphics)

,

Container.paint(java.awt.Graphics)

---

#### protected
String
paramString()

Returns a string representation of this

JSplitPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JComponent

**Returns:**
- a string representation of this

JSplitPane

.

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this SplitPane.")
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JSplitPane.
For split panes, the AccessibleContext takes the form of an
AccessibleJSplitPane.
A new AccessibleJSplitPane instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJSplitPane that serves as the
AccessibleContext of this JSplitPane

---

### Additional Sections

#### Class JSplitPane

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JSplitPane

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JSplitPane

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JSplitPane

javax.swing.JComponent

- javax.swing.JSplitPane

javax.swing.JSplitPane

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
@JavaBean
(
defaultProperty
="UI")
public class
JSplitPane

extends
JComponent

implements
Accessible
```

JSplitPane

is used to divide two (and only two)

Component

s. The two

Component

s
are graphically divided based on the look and feel
implementation, and the two

Component

s can then be
interactively resized by the user.
Information on using

JSplitPane

is in

How to Use Split Panes

in

The Java Tutorial

.

The two

Component

s in a split pane can be aligned
left to right using

JSplitPane.HORIZONTAL_SPLIT

, or top to bottom using

JSplitPane.VERTICAL_SPLIT

.
The preferred way to change the size of the

Component

s
is to invoke

setDividerLocation

where

location

is either
the new x or y position, depending on the orientation of the

JSplitPane

.

To resize the

Component

s to their preferred sizes invoke

resetToPreferredSizes

.

When the user is resizing the

Component

s the minimum
size of the

Components

is used to determine the
maximum/minimum position the

Component

s
can be set to. If the minimum size of the two
components is greater than the size of the split pane the divider
will not allow you to resize it. To alter the minimum size of a

JComponent

, see

JComponent.setMinimumSize(java.awt.Dimension)

.

When the user resizes the split pane the new space is distributed between
the two components based on the

resizeWeight

property.
A value of 0,
the default, indicates the right/bottom component gets all the space,
where as a value of 1 indicates the left/top component gets all the space.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**Since:** 1.2
**See Also:** setDividerLocation(double)

,

resetToPreferredSizes()

,

Serialized Form

@JavaBean

(

defaultProperty

="UI")
public class

JSplitPane

extends

JComponent

implements

Accessible

JSplitPane

is used to divide two (and only two)

Component

s. The two

Component

s
are graphically divided based on the look and feel
implementation, and the two

Component

s can then be
interactively resized by the user.
Information on using

JSplitPane

is in

How to Use Split Panes

in

The Java Tutorial

.

The two

Component

s in a split pane can be aligned
left to right using

JSplitPane.HORIZONTAL_SPLIT

, or top to bottom using

JSplitPane.VERTICAL_SPLIT

.
The preferred way to change the size of the

Component

s
is to invoke

setDividerLocation

where

location

is either
the new x or y position, depending on the orientation of the

JSplitPane

.

To resize the

Component

s to their preferred sizes invoke

resetToPreferredSizes

.

When the user is resizing the

Component

s the minimum
size of the

Components

is used to determine the
maximum/minimum position the

Component

s
can be set to. If the minimum size of the two
components is greater than the size of the split pane the divider
will not allow you to resize it. To alter the minimum size of a

JComponent

, see

JComponent.setMinimumSize(java.awt.Dimension)

.

When the user resizes the split pane the new space is distributed between
the two components based on the

resizeWeight

property.
A value of 0,
the default, indicates the right/bottom component gets all the space,
where as a value of 1 indicates the left/top component gets all the space.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

The two

Component

s in a split pane can be aligned
left to right using

JSplitPane.HORIZONTAL_SPLIT

, or top to bottom using

JSplitPane.VERTICAL_SPLIT

.
The preferred way to change the size of the

Component

s
is to invoke

setDividerLocation

where

location

is either
the new x or y position, depending on the orientation of the

JSplitPane

.

To resize the

Component

s to their preferred sizes invoke

resetToPreferredSizes

.

When the user is resizing the

Component

s the minimum
size of the

Components

is used to determine the
maximum/minimum position the

Component

s
can be set to. If the minimum size of the two
components is greater than the size of the split pane the divider
will not allow you to resize it. To alter the minimum size of a

JComponent

, see

JComponent.setMinimumSize(java.awt.Dimension)

.

When the user resizes the split pane the new space is distributed between
the two components based on the

resizeWeight

property.
A value of 0,
the default, indicates the right/bottom component gets all the space,
where as a value of 1 indicates the left/top component gets all the space.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

To resize the

Component

s to their preferred sizes invoke

resetToPreferredSizes

.

When the user is resizing the

Component

s the minimum
size of the

Components

is used to determine the
maximum/minimum position the

Component

s
can be set to. If the minimum size of the two
components is greater than the size of the split pane the divider
will not allow you to resize it. To alter the minimum size of a

JComponent

, see

JComponent.setMinimumSize(java.awt.Dimension)

.

When the user resizes the split pane the new space is distributed between
the two components based on the

resizeWeight

property.
A value of 0,
the default, indicates the right/bottom component gets all the space,
where as a value of 1 indicates the left/top component gets all the space.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

When the user is resizing the

Component

s the minimum
size of the

Components

is used to determine the
maximum/minimum position the

Component

s
can be set to. If the minimum size of the two
components is greater than the size of the split pane the divider
will not allow you to resize it. To alter the minimum size of a

JComponent

, see

JComponent.setMinimumSize(java.awt.Dimension)

.

When the user resizes the split pane the new space is distributed between
the two components based on the

resizeWeight

property.
A value of 0,
the default, indicates the right/bottom component gets all the space,
where as a value of 1 indicates the left/top component gets all the space.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

When the user resizes the split pane the new space is distributed between
the two components based on the

resizeWeight

property.
A value of 0,
the default, indicates the right/bottom component gets all the space,
where as a value of 1 indicates the left/top component gets all the space.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

protected class

JSplitPane.AccessibleJSplitPane

This class implements accessibility support for the

JSplitPane

class.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

BOTTOM

Used to add a

Component

below the other

Component

.

static

String

CONTINUOUS_LAYOUT_PROPERTY

Bound property name for continuousLayout.

protected boolean

continuousLayout

Whether or not the views are continuously redisplayed while
resizing.

static

String

DIVIDER

Used to add a

Component

that will represent the divider.

static

String

DIVIDER_LOCATION_PROPERTY

Bound property for the dividerLocation.

static

String

DIVIDER_SIZE_PROPERTY

Bound property name for border.

protected int

dividerSize

Size of the divider.

static int

HORIZONTAL_SPLIT

Horizontal split indicates the

Component

s are
split along the x axis.

static

String

LAST_DIVIDER_LOCATION_PROPERTY

Bound property for lastLocation.

protected int

lastDividerLocation

Previous location of the split pane.

static

String

LEFT

Used to add a

Component

to the left of the other

Component

.

protected

Component

leftComponent

The left or top component.

static

String

ONE_TOUCH_EXPANDABLE_PROPERTY

Bound property for oneTouchExpandable.

protected boolean

oneTouchExpandable

Is a little widget provided to quickly expand/collapse the
split pane?

protected int

orientation

How the views are split.

static

String

ORIENTATION_PROPERTY

Bound property name for orientation (horizontal or vertical).

static

String

RESIZE_WEIGHT_PROPERTY

Bound property for weight.

static

String

RIGHT

Used to add a

Component

to the right of the other

Component

.

protected

Component

rightComponent

The right or bottom component.

static

String

TOP

Used to add a

Component

above the other

Component

.

static int

VERTICAL_SPLIT

Vertical split indicates the

Component

s are
split along the y axis.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JSplitPane

()

Creates a new

JSplitPane

configured to arrange the child
components side-by-side horizontally, using two buttons for the components.

JSplitPane

​(int newOrientation)

Creates a new

JSplitPane

configured with the
specified orientation.

JSplitPane

​(int newOrientation,
boolean newContinuousLayout)

Creates a new

JSplitPane

with the specified
orientation and redrawing style.

JSplitPane

​(int newOrientation,
boolean newContinuousLayout,

Component

newLeftComponent,

Component

newRightComponent)

Creates a new

JSplitPane

with the specified
orientation and
redrawing style, and with the specified components.

JSplitPane

​(int newOrientation,

Component

newLeftComponent,

Component

newRightComponent)

Creates a new

JSplitPane

with the specified
orientation and the specified components.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this split pane.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JSplitPane.

Component

getBottomComponent

()

Returns the component below, or to the right of the divider.

int

getDividerLocation

()

Returns the last value passed to

setDividerLocation

.

int

getDividerSize

()

Returns the size of the divider.

int

getLastDividerLocation

()

Returns the last location the divider was at.

Component

getLeftComponent

()

Returns the component to the left (or above) the divider.

int

getMaximumDividerLocation

()

Returns the maximum location of the divider from the look and feel
implementation.

int

getMinimumDividerLocation

()

Returns the minimum location of the divider from the look and feel
implementation.

int

getOrientation

()

Returns the orientation.

double

getResizeWeight

()

Returns the number that determines how extra space is distributed.

Component

getRightComponent

()

Returns the component to the right (or below) the divider.

Component

getTopComponent

()

Returns the component above, or to the left of the divider.

SplitPaneUI

getUI

()

Returns the

SplitPaneUI

that is providing the
current look and feel.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

boolean

isContinuousLayout

()

Gets the

continuousLayout

property.

boolean

isOneTouchExpandable

()

Gets the

oneTouchExpandable

property.

boolean

isValidateRoot

()

Returns true, so that calls to

revalidate

on any descendant of this

JSplitPane

will cause a request to be queued that
will validate the

JSplitPane

and all its descendants.

protected void

paintChildren

​(

Graphics

g)

Subclassed to message the UI with

finishedPaintingChildren

after super has been messaged, as well as painting the border.

protected

String

paramString

()

Returns a string representation of this

JSplitPane

.

void

remove

​(int index)

Removes the

Component

at the specified index.

void

remove

​(

Component

component)

Removes the child component,

component

from the
pane.

void

removeAll

()

Removes all the child components from the split pane.

void

resetToPreferredSizes

()

Lays out the

JSplitPane

layout based on the preferred size
of the children components.

void

setBottomComponent

​(

Component

comp)

Sets the component below, or to the right of the divider.

void

setContinuousLayout

​(boolean newContinuousLayout)

Sets the value of the

continuousLayout

property,
which must be

true

for the child components
to be continuously
redisplayed and laid out during user intervention.

void

setDividerLocation

​(double proportionalLocation)

Sets the divider location as a percentage of the

JSplitPane

's size.

void

setDividerLocation

​(int location)

Sets the location of the divider.

void

setDividerSize

​(int newSize)

Sets the size of the divider.

void

setLastDividerLocation

​(int newLastLocation)

Sets the last location the divider was at to

newLastLocation

.

void

setLeftComponent

​(

Component

comp)

Sets the component to the left (or above) the divider.

void

setOneTouchExpandable

​(boolean newValue)

Sets the value of the

oneTouchExpandable

property,
which must be

true

for the

JSplitPane

to provide a UI widget
on the divider to quickly expand/collapse the divider.

void

setOrientation

​(int orientation)

Sets the orientation, or how the splitter is divided.

void

setResizeWeight

​(double value)

Specifies how to distribute extra space when the size of the split pane
changes.

void

setRightComponent

​(

Component

comp)

Sets the component to the right (or below) the divider.

void

setTopComponent

​(

Component

comp)

Sets the component above, or to the left of the divider.

void

setUI

​(

SplitPaneUI

ui)

Sets the L&F object that renders this component.

void

updateUI

()

Notification from the

UIManager

that the L&F has changed.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

paint

,

paintBorder

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JSplitPane.AccessibleJSplitPane

This class implements accessibility support for the

JSplitPane

class.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

This class implements accessibility support for the

JSplitPane

class.

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

Fields

Modifier and Type

Field

Description

static

String

BOTTOM

Used to add a

Component

below the other

Component

.

static

String

CONTINUOUS_LAYOUT_PROPERTY

Bound property name for continuousLayout.

protected boolean

continuousLayout

Whether or not the views are continuously redisplayed while
resizing.

static

String

DIVIDER

Used to add a

Component

that will represent the divider.

static

String

DIVIDER_LOCATION_PROPERTY

Bound property for the dividerLocation.

static

String

DIVIDER_SIZE_PROPERTY

Bound property name for border.

protected int

dividerSize

Size of the divider.

static int

HORIZONTAL_SPLIT

Horizontal split indicates the

Component

s are
split along the x axis.

static

String

LAST_DIVIDER_LOCATION_PROPERTY

Bound property for lastLocation.

protected int

lastDividerLocation

Previous location of the split pane.

static

String

LEFT

Used to add a

Component

to the left of the other

Component

.

protected

Component

leftComponent

The left or top component.

static

String

ONE_TOUCH_EXPANDABLE_PROPERTY

Bound property for oneTouchExpandable.

protected boolean

oneTouchExpandable

Is a little widget provided to quickly expand/collapse the
split pane?

protected int

orientation

How the views are split.

static

String

ORIENTATION_PROPERTY

Bound property name for orientation (horizontal or vertical).

static

String

RESIZE_WEIGHT_PROPERTY

Bound property for weight.

static

String

RIGHT

Used to add a

Component

to the right of the other

Component

.

protected

Component

rightComponent

The right or bottom component.

static

String

TOP

Used to add a

Component

above the other

Component

.

static int

VERTICAL_SPLIT

Vertical split indicates the

Component

s are
split along the y axis.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Field Summary

Used to add a

Component

below the other

Component

.

Bound property name for continuousLayout.

Whether or not the views are continuously redisplayed while
resizing.

Used to add a

Component

that will represent the divider.

Bound property for the dividerLocation.

Bound property name for border.

Size of the divider.

Horizontal split indicates the

Component

s are
split along the x axis.

Bound property for lastLocation.

Previous location of the split pane.

Used to add a

Component

to the left of the other

Component

.

The left or top component.

Bound property for oneTouchExpandable.

Is a little widget provided to quickly expand/collapse the
split pane?

How the views are split.

Bound property name for orientation (horizontal or vertical).

Bound property for weight.

Used to add a

Component

to the right of the other

Component

.

The right or bottom component.

Used to add a

Component

above the other

Component

.

Vertical split indicates the

Component

s are
split along the y axis.

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Constructor Summary

Constructors

Constructor

Description

JSplitPane

()

Creates a new

JSplitPane

configured to arrange the child
components side-by-side horizontally, using two buttons for the components.

JSplitPane

​(int newOrientation)

Creates a new

JSplitPane

configured with the
specified orientation.

JSplitPane

​(int newOrientation,
boolean newContinuousLayout)

Creates a new

JSplitPane

with the specified
orientation and redrawing style.

JSplitPane

​(int newOrientation,
boolean newContinuousLayout,

Component

newLeftComponent,

Component

newRightComponent)

Creates a new

JSplitPane

with the specified
orientation and
redrawing style, and with the specified components.

JSplitPane

​(int newOrientation,

Component

newLeftComponent,

Component

newRightComponent)

Creates a new

JSplitPane

with the specified
orientation and the specified components.

---

#### Constructor Summary

Creates a new

JSplitPane

configured to arrange the child
components side-by-side horizontally, using two buttons for the components.

Creates a new

JSplitPane

configured with the
specified orientation.

Creates a new

JSplitPane

with the specified
orientation and redrawing style.

Creates a new

JSplitPane

with the specified
orientation and
redrawing style, and with the specified components.

Creates a new

JSplitPane

with the specified
orientation and the specified components.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this split pane.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JSplitPane.

Component

getBottomComponent

()

Returns the component below, or to the right of the divider.

int

getDividerLocation

()

Returns the last value passed to

setDividerLocation

.

int

getDividerSize

()

Returns the size of the divider.

int

getLastDividerLocation

()

Returns the last location the divider was at.

Component

getLeftComponent

()

Returns the component to the left (or above) the divider.

int

getMaximumDividerLocation

()

Returns the maximum location of the divider from the look and feel
implementation.

int

getMinimumDividerLocation

()

Returns the minimum location of the divider from the look and feel
implementation.

int

getOrientation

()

Returns the orientation.

double

getResizeWeight

()

Returns the number that determines how extra space is distributed.

Component

getRightComponent

()

Returns the component to the right (or below) the divider.

Component

getTopComponent

()

Returns the component above, or to the left of the divider.

SplitPaneUI

getUI

()

Returns the

SplitPaneUI

that is providing the
current look and feel.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

boolean

isContinuousLayout

()

Gets the

continuousLayout

property.

boolean

isOneTouchExpandable

()

Gets the

oneTouchExpandable

property.

boolean

isValidateRoot

()

Returns true, so that calls to

revalidate

on any descendant of this

JSplitPane

will cause a request to be queued that
will validate the

JSplitPane

and all its descendants.

protected void

paintChildren

​(

Graphics

g)

Subclassed to message the UI with

finishedPaintingChildren

after super has been messaged, as well as painting the border.

protected

String

paramString

()

Returns a string representation of this

JSplitPane

.

void

remove

​(int index)

Removes the

Component

at the specified index.

void

remove

​(

Component

component)

Removes the child component,

component

from the
pane.

void

removeAll

()

Removes all the child components from the split pane.

void

resetToPreferredSizes

()

Lays out the

JSplitPane

layout based on the preferred size
of the children components.

void

setBottomComponent

​(

Component

comp)

Sets the component below, or to the right of the divider.

void

setContinuousLayout

​(boolean newContinuousLayout)

Sets the value of the

continuousLayout

property,
which must be

true

for the child components
to be continuously
redisplayed and laid out during user intervention.

void

setDividerLocation

​(double proportionalLocation)

Sets the divider location as a percentage of the

JSplitPane

's size.

void

setDividerLocation

​(int location)

Sets the location of the divider.

void

setDividerSize

​(int newSize)

Sets the size of the divider.

void

setLastDividerLocation

​(int newLastLocation)

Sets the last location the divider was at to

newLastLocation

.

void

setLeftComponent

​(

Component

comp)

Sets the component to the left (or above) the divider.

void

setOneTouchExpandable

​(boolean newValue)

Sets the value of the

oneTouchExpandable

property,
which must be

true

for the

JSplitPane

to provide a UI widget
on the divider to quickly expand/collapse the divider.

void

setOrientation

​(int orientation)

Sets the orientation, or how the splitter is divided.

void

setResizeWeight

​(double value)

Specifies how to distribute extra space when the size of the split pane
changes.

void

setRightComponent

​(

Component

comp)

Sets the component to the right (or below) the divider.

void

setTopComponent

​(

Component

comp)

Sets the component above, or to the left of the divider.

void

setUI

​(

SplitPaneUI

ui)

Sets the L&F object that renders this component.

void

updateUI

()

Notification from the

UIManager

that the L&F has changed.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

paint

,

paintBorder

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

Adds the specified component to this split pane.

Gets the AccessibleContext associated with this JSplitPane.

Returns the component below, or to the right of the divider.

Returns the last value passed to

setDividerLocation

.

Returns the size of the divider.

Returns the last location the divider was at.

Returns the component to the left (or above) the divider.

Returns the maximum location of the divider from the look and feel
implementation.

Returns the minimum location of the divider from the look and feel
implementation.

Returns the orientation.

Returns the number that determines how extra space is distributed.

Returns the component to the right (or below) the divider.

Returns the component above, or to the left of the divider.

Returns the

SplitPaneUI

that is providing the
current look and feel.

Returns the name of the L&F class that renders this component.

Gets the

continuousLayout

property.

Gets the

oneTouchExpandable

property.

Returns true, so that calls to

revalidate

on any descendant of this

JSplitPane

will cause a request to be queued that
will validate the

JSplitPane

and all its descendants.

Subclassed to message the UI with

finishedPaintingChildren

after super has been messaged, as well as painting the border.

Returns a string representation of this

JSplitPane

.

Removes the

Component

at the specified index.

Removes the child component,

component

from the
pane.

Removes all the child components from the split pane.

Lays out the

JSplitPane

layout based on the preferred size
of the children components.

Sets the component below, or to the right of the divider.

Sets the value of the

continuousLayout

property,
which must be

true

for the child components
to be continuously
redisplayed and laid out during user intervention.

Sets the divider location as a percentage of the

JSplitPane

's size.

Sets the location of the divider.

Sets the size of the divider.

Sets the last location the divider was at to

newLastLocation

.

Sets the component to the left (or above) the divider.

Sets the value of the

oneTouchExpandable

property,
which must be

true

for the

JSplitPane

to provide a UI widget
on the divider to quickly expand/collapse the divider.

Sets the orientation, or how the splitter is divided.

Specifies how to distribute extra space when the size of the split pane
changes.

Sets the component to the right (or below) the divider.

Sets the component above, or to the left of the divider.

Sets the L&F object that renders this component.

Notification from the

UIManager

that the L&F has changed.

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

paint

,

paintBorder

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

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

- VERTICAL_SPLIT

```java
public static final int VERTICAL_SPLIT
```

Vertical split indicates the

Component

s are
split along the y axis. For example the two

Component

s will be split one on top of the other.

**See Also:** Constant Field Values

- HORIZONTAL_SPLIT

```java
public static final int HORIZONTAL_SPLIT
```

Horizontal split indicates the

Component

s are
split along the x axis. For example the two

Component

s will be split one to the left of the
other.

**See Also:** Constant Field Values

- LEFT

```java
public static final
String
LEFT
```

Used to add a

Component

to the left of the other

Component

.

**See Also:** Constant Field Values

- RIGHT

```java
public static final
String
RIGHT
```

Used to add a

Component

to the right of the other

Component

.

**See Also:** Constant Field Values

- TOP

```java
public static final
String
TOP
```

Used to add a

Component

above the other

Component

.

**See Also:** Constant Field Values

- BOTTOM

```java
public static final
String
BOTTOM
```

Used to add a

Component

below the other

Component

.

**See Also:** Constant Field Values

- DIVIDER

```java
public static final
String
DIVIDER
```

Used to add a

Component

that will represent the divider.

**See Also:** Constant Field Values

- ORIENTATION_PROPERTY

```java
public static final
String
ORIENTATION_PROPERTY
```

Bound property name for orientation (horizontal or vertical).

**See Also:** Constant Field Values

- CONTINUOUS_LAYOUT_PROPERTY

```java
public static final
String
CONTINUOUS_LAYOUT_PROPERTY
```

Bound property name for continuousLayout.

**See Also:** Constant Field Values

- DIVIDER_SIZE_PROPERTY

```java
public static final
String
DIVIDER_SIZE_PROPERTY
```

Bound property name for border.

**See Also:** Constant Field Values

- ONE_TOUCH_EXPANDABLE_PROPERTY

```java
public static final
String
ONE_TOUCH_EXPANDABLE_PROPERTY
```

Bound property for oneTouchExpandable.

**See Also:** Constant Field Values

- LAST_DIVIDER_LOCATION_PROPERTY

```java
public static final
String
LAST_DIVIDER_LOCATION_PROPERTY
```

Bound property for lastLocation.

**See Also:** Constant Field Values

- DIVIDER_LOCATION_PROPERTY

```java
public static final
String
DIVIDER_LOCATION_PROPERTY
```

Bound property for the dividerLocation.

**Since:** 1.3
**See Also:** Constant Field Values

- RESIZE_WEIGHT_PROPERTY

```java
public static final
String
RESIZE_WEIGHT_PROPERTY
```

Bound property for weight.

**Since:** 1.3
**See Also:** Constant Field Values

- orientation

```java
protected int orientation
```

How the views are split.

- continuousLayout

```java
protected boolean continuousLayout
```

Whether or not the views are continuously redisplayed while
resizing.

- leftComponent

```java
protected
Component
leftComponent
```

The left or top component.

- rightComponent

```java
protected
Component
rightComponent
```

The right or bottom component.

- dividerSize

```java
protected int dividerSize
```

Size of the divider.

- oneTouchExpandable

```java
protected boolean oneTouchExpandable
```

Is a little widget provided to quickly expand/collapse the
split pane?

- lastDividerLocation

```java
protected int lastDividerLocation
```

Previous location of the split pane.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JSplitPane

```java
public JSplitPane()
```

Creates a new

JSplitPane

configured to arrange the child
components side-by-side horizontally, using two buttons for the components.

- JSplitPane

```java
@ConstructorProperties
("orientation")
public JSplitPane​(int newOrientation)
```

Creates a new

JSplitPane

configured with the
specified orientation.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Throws:** IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT.

- JSplitPane

```java
public JSplitPane​(int newOrientation,
boolean newContinuousLayout)
```

Creates a new

JSplitPane

with the specified
orientation and redrawing style.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Parameters:** newContinuousLayout

- a boolean, true for the components to
redraw continuously as the divider changes position, false
to wait until the divider position stops changing to redraw
**Throws:** IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT

- JSplitPane

```java
public JSplitPane​(int newOrientation,

Component
newLeftComponent,

Component
newRightComponent)
```

Creates a new

JSplitPane

with the specified
orientation and the specified components.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Parameters:** newLeftComponent

- the

Component

that will
appear on the left
of a horizontally-split pane, or at the top of a
vertically-split pane
**Parameters:** newRightComponent

- the

Component

that will
appear on the right
of a horizontally-split pane, or at the bottom of a
vertically-split pane
**Throws:** IllegalArgumentException

- if

orientation

is not one of: HORIZONTAL_SPLIT or VERTICAL_SPLIT

- JSplitPane

```java
public JSplitPane​(int newOrientation,
boolean newContinuousLayout,

Component
newLeftComponent,

Component
newRightComponent)
```

Creates a new

JSplitPane

with the specified
orientation and
redrawing style, and with the specified components.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Parameters:** newContinuousLayout

- a boolean, true for the components to
redraw continuously as the divider changes position, false
to wait until the divider position stops changing to redraw
**Parameters:** newLeftComponent

- the

Component

that will
appear on the left
of a horizontally-split pane, or at the top of a
vertically-split pane
**Parameters:** newRightComponent

- the

Component

that will
appear on the right
of a horizontally-split pane, or at the bottom of a
vertically-split pane
**Throws:** IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT

============ METHOD DETAIL ==========

- Method Detail

- setUI

```java
public void setUI​(
SplitPaneUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

SplitPaneUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- getUI

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The L&F object that renders this component.")
public
SplitPaneUI
getUI()
```

Returns the

SplitPaneUI

that is providing the
current look and feel.

**Overrides:** getUI

in class

JComponent
**Returns:** the

SplitPaneUI

object that renders this component

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="A string that specifies the name of the L&F class.")
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "SplitPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setDividerSize

```java
@BeanProperty
(
description
="The size of the divider.")
public void setDividerSize​(int newSize)
```

Sets the size of the divider.

**Parameters:** newSize

- an integer giving the size of the divider in pixels

- getDividerSize

```java
public int getDividerSize()
```

Returns the size of the divider.

**Returns:** an integer giving the size of the divider in pixels

- setLeftComponent

```java
public void setLeftComponent​(
Component
comp)
```

Sets the component to the left (or above) the divider.

**Parameters:** comp

- the

Component

to display in that position

- getLeftComponent

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The component to the left (or above) the divider.")
public
Component
getLeftComponent()
```

Returns the component to the left (or above) the divider.

**Returns:** the

Component

displayed in that position

- setTopComponent

```java
@BeanProperty
(
bound
=false,

description
="The component above, or to the left of the divider.")
public void setTopComponent​(
Component
comp)
```

Sets the component above, or to the left of the divider.

**Parameters:** comp

- the

Component

to display in that position

- getTopComponent

```java
public
Component
getTopComponent()
```

Returns the component above, or to the left of the divider.

**Returns:** the

Component

displayed in that position

- setRightComponent

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The component to the right (or below) the divider.")
public void setRightComponent​(
Component
comp)
```

Sets the component to the right (or below) the divider.

**Parameters:** comp

- the

Component

to display in that position

- getRightComponent

```java
public
Component
getRightComponent()
```

Returns the component to the right (or below) the divider.

**Returns:** the

Component

displayed in that position

- setBottomComponent

```java
@BeanProperty
(
bound
=false,

description
="The component below, or to the right of the divider.")
public void setBottomComponent​(
Component
comp)
```

Sets the component below, or to the right of the divider.

**Parameters:** comp

- the

Component

to display in that position

- getBottomComponent

```java
public
Component
getBottomComponent()
```

Returns the component below, or to the right of the divider.

**Returns:** the

Component

displayed in that position

- setOneTouchExpandable

```java
@BeanProperty
(
description
="UI widget on the divider to quickly expand/collapse the divider.")
public void setOneTouchExpandable​(boolean newValue)
```

Sets the value of the

oneTouchExpandable

property,
which must be

true

for the

JSplitPane

to provide a UI widget
on the divider to quickly expand/collapse the divider.
The default value of this property is

false

.
Some look and feels might not support one-touch expanding;
they will ignore this property.

**Parameters:** newValue

-

true

to specify that the split pane should provide a
collapse/expand widget
**See Also:** isOneTouchExpandable()

- isOneTouchExpandable

```java
public boolean isOneTouchExpandable()
```

Gets the

oneTouchExpandable

property.

**Returns:** the value of the

oneTouchExpandable

property
**See Also:** setOneTouchExpandable(boolean)

- setLastDividerLocation

```java
@BeanProperty
(
description
="The last location the divider was at.")
public void setLastDividerLocation​(int newLastLocation)
```

Sets the last location the divider was at to

newLastLocation

.

**Parameters:** newLastLocation

- an integer specifying the last divider location
in pixels, from the left (or upper) edge of the pane to the
left (or upper) edge of the divider

- getLastDividerLocation

```java
public int getLastDividerLocation()
```

Returns the last location the divider was at.

**Returns:** an integer specifying the last divider location as a count
of pixels from the left (or upper) edge of the pane to the
left (or upper) edge of the divider

- setOrientation

```java
@BeanProperty
(
enumerationValues
={"JSplitPane.HORIZONTAL_SPLIT","JSplitPane.VERTICAL_SPLIT"},

description
="The orientation, or how the splitter is divided.")
public void setOrientation​(int orientation)
```

Sets the orientation, or how the splitter is divided. The options
are:

- JSplitPane.VERTICAL_SPLIT (above/below orientation of components)

JSplitPane.HORIZONTAL_SPLIT (left/right orientation of components)

**Parameters:** orientation

- an integer specifying the orientation
**Throws:** IllegalArgumentException

- if orientation is not one of:
HORIZONTAL_SPLIT or VERTICAL_SPLIT.

- getOrientation

```java
public int getOrientation()
```

Returns the orientation.

**Returns:** an integer giving the orientation
**See Also:** setOrientation(int)

- setContinuousLayout

```java
@BeanProperty
(
description
="Whether the child components are continuously redisplayed and laid out during user intervention.")
public void setContinuousLayout​(boolean newContinuousLayout)
```

Sets the value of the

continuousLayout

property,
which must be

true

for the child components
to be continuously
redisplayed and laid out during user intervention.
The default value of this property is look and feel dependent.
Some look and feels might not support continuous layout;
they will ignore this property.

**Parameters:** newContinuousLayout

-

true

if the components
should continuously be redrawn as the divider changes position
**See Also:** isContinuousLayout()

- isContinuousLayout

```java
public boolean isContinuousLayout()
```

Gets the

continuousLayout

property.

**Returns:** the value of the

continuousLayout

property
**See Also:** setContinuousLayout(boolean)

- setResizeWeight

```java
@BeanProperty
(
description
="Specifies how to distribute extra space when the split pane resizes.")
public void setResizeWeight​(double value)
```

Specifies how to distribute extra space when the size of the split pane
changes. A value of 0, the default,
indicates the right/bottom component gets all the extra space (the
left/top component acts fixed), where as a value of 1 specifies the
left/top component gets all the extra space (the right/bottom component
acts fixed). Specifically, the left/top component gets (weight * diff)
extra space and the right/bottom component gets (1 - weight) * diff
extra space.

**Parameters:** value

- as described above
**Throws:** IllegalArgumentException

- if

value

is < 0 or > 1
**Since:** 1.3

- getResizeWeight

```java
public double getResizeWeight()
```

Returns the number that determines how extra space is distributed.

**Returns:** how extra space is to be distributed on a resize of the
split pane
**Since:** 1.3

- resetToPreferredSizes

```java
public void resetToPreferredSizes()
```

Lays out the

JSplitPane

layout based on the preferred size
of the children components. This will likely result in changing
the divider location.

- setDividerLocation

```java
@BeanProperty
(
description
="The location of the divider.")
public void setDividerLocation​(double proportionalLocation)
```

Sets the divider location as a percentage of the

JSplitPane

's size.

This method is implemented in terms of

setDividerLocation(int)

.
This method immediately changes the size of the split pane based on
its current size. If the split pane is not correctly realized and on
screen, this method will have no effect (new divider location will
become (current size * proportionalLocation) which is 0).

**Parameters:** proportionalLocation

- a double-precision floating point value
that specifies a percentage, from zero (top/left) to 1.0
(bottom/right)
**Throws:** IllegalArgumentException

- if the specified location is < 0
or > 1.0

- setDividerLocation

```java
@BeanProperty
(
description
="The location of the divider.")
public void setDividerLocation​(int location)
```

Sets the location of the divider. This is passed off to the
look and feel implementation, and then listeners are notified. A value
less than 0 implies the divider should be reset to a value that
attempts to honor the preferred size of the left/top component.
After notifying the listeners, the last divider location is updated,
via

setLastDividerLocation

.

**Parameters:** location

- an int specifying a UI-specific value (typically a
pixel count)

- getDividerLocation

```java
public int getDividerLocation()
```

Returns the last value passed to

setDividerLocation

.
The value returned from this method may differ from the actual
divider location (if

setDividerLocation

was passed a
value bigger than the current size).

**Returns:** an integer specifying the location of the divider

- getMinimumDividerLocation

```java
@BeanProperty
(
bound
=false,

description
="The minimum location of the divider from the L&F.")
public int getMinimumDividerLocation()
```

Returns the minimum location of the divider from the look and feel
implementation.

**Returns:** an integer specifying a UI-specific value for the minimum
location (typically a pixel count); or -1 if the UI is

null

- getMaximumDividerLocation

```java
@BeanProperty
(
bound
=false)
public int getMaximumDividerLocation()
```

Returns the maximum location of the divider from the look and feel
implementation.

**Returns:** an integer specifying a UI-specific value for the maximum
location (typically a pixel count); or -1 if the UI is

null

- remove

```java
public void remove​(
Component
component)
```

Removes the child component,

component

from the
pane. Resets the

leftComponent

or

rightComponent

instance variable, as necessary.

**Overrides:** remove

in class

Container
**Parameters:** component

- the

Component

to remove
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.remove(int)

- remove

```java
public void remove​(int index)
```

Removes the

Component

at the specified index.
Updates the

leftComponent

and

rightComponent

instance variables as necessary, and then messages super.

**Overrides:** remove

in class

Container
**Parameters:** index

- an integer specifying the component to remove, where
1 specifies the left/top component and 2 specifies the
bottom/right component
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

- removeAll

```java
public void removeAll()
```

Removes all the child components from the split pane. Resets the

leftComonent

and

rightComponent

instance variables.

**Overrides:** removeAll

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

- isValidateRoot

```java
@BeanProperty
(
hidden
=true)
public boolean isValidateRoot()
```

Returns true, so that calls to

revalidate

on any descendant of this

JSplitPane

will cause a request to be queued that
will validate the

JSplitPane

and all its descendants.

**Overrides:** isValidateRoot

in class

JComponent
**Returns:** true
**See Also:** JComponent.revalidate()

,

Container.isValidateRoot()

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this split pane.
If

constraints

identifies the left/top or
right/bottom child component, and a component with that identifier
was previously added, it will be removed and then

comp

will be added in its place. If

constraints

is not
one of the known identifiers the layout manager may throw an

IllegalArgumentException

.

The possible constraints objects (Strings) are:

- JSplitPane.TOP

JSplitPane.LEFT

JSplitPane.BOTTOM

JSplitPane.RIGHT

If the

constraints

object is

null

,
the component is added in the
first available position (left/top if open, else right/bottom).

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to add
**Parameters:** constraints

- an

Object

specifying the
layout constraints
(position) for this component
**Parameters:** index

- an integer specifying the index in the container's
list.
**Throws:** IllegalArgumentException

- if the

constraints

object does not match an existing component
**See Also:** Container.addImpl(Component, Object, int)

- paintChildren

```java
protected void paintChildren​(
Graphics
g)
```

Subclassed to message the UI with

finishedPaintingChildren

after super has been messaged, as well as painting the border.

**Overrides:** paintChildren

in class

JComponent
**Parameters:** g

- the

Graphics

context within which to paint
**See Also:** JComponent.paint(java.awt.Graphics)

,

Container.paint(java.awt.Graphics)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JSplitPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JSplitPane

.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this SplitPane.")
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JSplitPane.
For split panes, the AccessibleContext takes the form of an
AccessibleJSplitPane.
A new AccessibleJSplitPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJSplitPane that serves as the
AccessibleContext of this JSplitPane

Field Detail

- VERTICAL_SPLIT

```java
public static final int VERTICAL_SPLIT
```

Vertical split indicates the

Component

s are
split along the y axis. For example the two

Component

s will be split one on top of the other.

**See Also:** Constant Field Values

- HORIZONTAL_SPLIT

```java
public static final int HORIZONTAL_SPLIT
```

Horizontal split indicates the

Component

s are
split along the x axis. For example the two

Component

s will be split one to the left of the
other.

**See Also:** Constant Field Values

- LEFT

```java
public static final
String
LEFT
```

Used to add a

Component

to the left of the other

Component

.

**See Also:** Constant Field Values

- RIGHT

```java
public static final
String
RIGHT
```

Used to add a

Component

to the right of the other

Component

.

**See Also:** Constant Field Values

- TOP

```java
public static final
String
TOP
```

Used to add a

Component

above the other

Component

.

**See Also:** Constant Field Values

- BOTTOM

```java
public static final
String
BOTTOM
```

Used to add a

Component

below the other

Component

.

**See Also:** Constant Field Values

- DIVIDER

```java
public static final
String
DIVIDER
```

Used to add a

Component

that will represent the divider.

**See Also:** Constant Field Values

- ORIENTATION_PROPERTY

```java
public static final
String
ORIENTATION_PROPERTY
```

Bound property name for orientation (horizontal or vertical).

**See Also:** Constant Field Values

- CONTINUOUS_LAYOUT_PROPERTY

```java
public static final
String
CONTINUOUS_LAYOUT_PROPERTY
```

Bound property name for continuousLayout.

**See Also:** Constant Field Values

- DIVIDER_SIZE_PROPERTY

```java
public static final
String
DIVIDER_SIZE_PROPERTY
```

Bound property name for border.

**See Also:** Constant Field Values

- ONE_TOUCH_EXPANDABLE_PROPERTY

```java
public static final
String
ONE_TOUCH_EXPANDABLE_PROPERTY
```

Bound property for oneTouchExpandable.

**See Also:** Constant Field Values

- LAST_DIVIDER_LOCATION_PROPERTY

```java
public static final
String
LAST_DIVIDER_LOCATION_PROPERTY
```

Bound property for lastLocation.

**See Also:** Constant Field Values

- DIVIDER_LOCATION_PROPERTY

```java
public static final
String
DIVIDER_LOCATION_PROPERTY
```

Bound property for the dividerLocation.

**Since:** 1.3
**See Also:** Constant Field Values

- RESIZE_WEIGHT_PROPERTY

```java
public static final
String
RESIZE_WEIGHT_PROPERTY
```

Bound property for weight.

**Since:** 1.3
**See Also:** Constant Field Values

- orientation

```java
protected int orientation
```

How the views are split.

- continuousLayout

```java
protected boolean continuousLayout
```

Whether or not the views are continuously redisplayed while
resizing.

- leftComponent

```java
protected
Component
leftComponent
```

The left or top component.

- rightComponent

```java
protected
Component
rightComponent
```

The right or bottom component.

- dividerSize

```java
protected int dividerSize
```

Size of the divider.

- oneTouchExpandable

```java
protected boolean oneTouchExpandable
```

Is a little widget provided to quickly expand/collapse the
split pane?

- lastDividerLocation

```java
protected int lastDividerLocation
```

Previous location of the split pane.

---

#### Field Detail

VERTICAL_SPLIT

```java
public static final int VERTICAL_SPLIT
```

Vertical split indicates the

Component

s are
split along the y axis. For example the two

Component

s will be split one on top of the other.

**See Also:** Constant Field Values

---

#### VERTICAL_SPLIT

public static final int VERTICAL_SPLIT

Vertical split indicates the

Component

s are
split along the y axis. For example the two

Component

s will be split one on top of the other.

HORIZONTAL_SPLIT

```java
public static final int HORIZONTAL_SPLIT
```

Horizontal split indicates the

Component

s are
split along the x axis. For example the two

Component

s will be split one to the left of the
other.

**See Also:** Constant Field Values

---

#### HORIZONTAL_SPLIT

public static final int HORIZONTAL_SPLIT

Horizontal split indicates the

Component

s are
split along the x axis. For example the two

Component

s will be split one to the left of the
other.

LEFT

```java
public static final
String
LEFT
```

Used to add a

Component

to the left of the other

Component

.

**See Also:** Constant Field Values

---

#### LEFT

public static final

String

LEFT

Used to add a

Component

to the left of the other

Component

.

RIGHT

```java
public static final
String
RIGHT
```

Used to add a

Component

to the right of the other

Component

.

**See Also:** Constant Field Values

---

#### RIGHT

public static final

String

RIGHT

Used to add a

Component

to the right of the other

Component

.

TOP

```java
public static final
String
TOP
```

Used to add a

Component

above the other

Component

.

**See Also:** Constant Field Values

---

#### TOP

public static final

String

TOP

Used to add a

Component

above the other

Component

.

BOTTOM

```java
public static final
String
BOTTOM
```

Used to add a

Component

below the other

Component

.

**See Also:** Constant Field Values

---

#### BOTTOM

public static final

String

BOTTOM

Used to add a

Component

below the other

Component

.

DIVIDER

```java
public static final
String
DIVIDER
```

Used to add a

Component

that will represent the divider.

**See Also:** Constant Field Values

---

#### DIVIDER

public static final

String

DIVIDER

Used to add a

Component

that will represent the divider.

ORIENTATION_PROPERTY

```java
public static final
String
ORIENTATION_PROPERTY
```

Bound property name for orientation (horizontal or vertical).

**See Also:** Constant Field Values

---

#### ORIENTATION_PROPERTY

public static final

String

ORIENTATION_PROPERTY

Bound property name for orientation (horizontal or vertical).

CONTINUOUS_LAYOUT_PROPERTY

```java
public static final
String
CONTINUOUS_LAYOUT_PROPERTY
```

Bound property name for continuousLayout.

**See Also:** Constant Field Values

---

#### CONTINUOUS_LAYOUT_PROPERTY

public static final

String

CONTINUOUS_LAYOUT_PROPERTY

Bound property name for continuousLayout.

DIVIDER_SIZE_PROPERTY

```java
public static final
String
DIVIDER_SIZE_PROPERTY
```

Bound property name for border.

**See Also:** Constant Field Values

---

#### DIVIDER_SIZE_PROPERTY

public static final

String

DIVIDER_SIZE_PROPERTY

Bound property name for border.

ONE_TOUCH_EXPANDABLE_PROPERTY

```java
public static final
String
ONE_TOUCH_EXPANDABLE_PROPERTY
```

Bound property for oneTouchExpandable.

**See Also:** Constant Field Values

---

#### ONE_TOUCH_EXPANDABLE_PROPERTY

public static final

String

ONE_TOUCH_EXPANDABLE_PROPERTY

Bound property for oneTouchExpandable.

LAST_DIVIDER_LOCATION_PROPERTY

```java
public static final
String
LAST_DIVIDER_LOCATION_PROPERTY
```

Bound property for lastLocation.

**See Also:** Constant Field Values

---

#### LAST_DIVIDER_LOCATION_PROPERTY

public static final

String

LAST_DIVIDER_LOCATION_PROPERTY

Bound property for lastLocation.

DIVIDER_LOCATION_PROPERTY

```java
public static final
String
DIVIDER_LOCATION_PROPERTY
```

Bound property for the dividerLocation.

**Since:** 1.3
**See Also:** Constant Field Values

---

#### DIVIDER_LOCATION_PROPERTY

public static final

String

DIVIDER_LOCATION_PROPERTY

Bound property for the dividerLocation.

RESIZE_WEIGHT_PROPERTY

```java
public static final
String
RESIZE_WEIGHT_PROPERTY
```

Bound property for weight.

**Since:** 1.3
**See Also:** Constant Field Values

---

#### RESIZE_WEIGHT_PROPERTY

public static final

String

RESIZE_WEIGHT_PROPERTY

Bound property for weight.

orientation

```java
protected int orientation
```

How the views are split.

---

#### orientation

protected int orientation

How the views are split.

continuousLayout

```java
protected boolean continuousLayout
```

Whether or not the views are continuously redisplayed while
resizing.

---

#### continuousLayout

protected boolean continuousLayout

Whether or not the views are continuously redisplayed while
resizing.

leftComponent

```java
protected
Component
leftComponent
```

The left or top component.

---

#### leftComponent

protected

Component

leftComponent

The left or top component.

rightComponent

```java
protected
Component
rightComponent
```

The right or bottom component.

---

#### rightComponent

protected

Component

rightComponent

The right or bottom component.

dividerSize

```java
protected int dividerSize
```

Size of the divider.

---

#### dividerSize

protected int dividerSize

Size of the divider.

oneTouchExpandable

```java
protected boolean oneTouchExpandable
```

Is a little widget provided to quickly expand/collapse the
split pane?

---

#### oneTouchExpandable

protected boolean oneTouchExpandable

Is a little widget provided to quickly expand/collapse the
split pane?

lastDividerLocation

```java
protected int lastDividerLocation
```

Previous location of the split pane.

---

#### lastDividerLocation

protected int lastDividerLocation

Previous location of the split pane.

Constructor Detail

- JSplitPane

```java
public JSplitPane()
```

Creates a new

JSplitPane

configured to arrange the child
components side-by-side horizontally, using two buttons for the components.

- JSplitPane

```java
@ConstructorProperties
("orientation")
public JSplitPane​(int newOrientation)
```

Creates a new

JSplitPane

configured with the
specified orientation.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Throws:** IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT.

- JSplitPane

```java
public JSplitPane​(int newOrientation,
boolean newContinuousLayout)
```

Creates a new

JSplitPane

with the specified
orientation and redrawing style.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Parameters:** newContinuousLayout

- a boolean, true for the components to
redraw continuously as the divider changes position, false
to wait until the divider position stops changing to redraw
**Throws:** IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT

- JSplitPane

```java
public JSplitPane​(int newOrientation,

Component
newLeftComponent,

Component
newRightComponent)
```

Creates a new

JSplitPane

with the specified
orientation and the specified components.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Parameters:** newLeftComponent

- the

Component

that will
appear on the left
of a horizontally-split pane, or at the top of a
vertically-split pane
**Parameters:** newRightComponent

- the

Component

that will
appear on the right
of a horizontally-split pane, or at the bottom of a
vertically-split pane
**Throws:** IllegalArgumentException

- if

orientation

is not one of: HORIZONTAL_SPLIT or VERTICAL_SPLIT

- JSplitPane

```java
public JSplitPane​(int newOrientation,
boolean newContinuousLayout,

Component
newLeftComponent,

Component
newRightComponent)
```

Creates a new

JSplitPane

with the specified
orientation and
redrawing style, and with the specified components.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Parameters:** newContinuousLayout

- a boolean, true for the components to
redraw continuously as the divider changes position, false
to wait until the divider position stops changing to redraw
**Parameters:** newLeftComponent

- the

Component

that will
appear on the left
of a horizontally-split pane, or at the top of a
vertically-split pane
**Parameters:** newRightComponent

- the

Component

that will
appear on the right
of a horizontally-split pane, or at the bottom of a
vertically-split pane
**Throws:** IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT

---

#### Constructor Detail

JSplitPane

```java
public JSplitPane()
```

Creates a new

JSplitPane

configured to arrange the child
components side-by-side horizontally, using two buttons for the components.

---

#### JSplitPane

public JSplitPane()

Creates a new

JSplitPane

configured to arrange the child
components side-by-side horizontally, using two buttons for the components.

JSplitPane

```java
@ConstructorProperties
("orientation")
public JSplitPane​(int newOrientation)
```

Creates a new

JSplitPane

configured with the
specified orientation.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Throws:** IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT.

---

#### JSplitPane

@ConstructorProperties

("orientation")
public JSplitPane​(int newOrientation)

Creates a new

JSplitPane

configured with the
specified orientation.

JSplitPane

```java
public JSplitPane​(int newOrientation,
boolean newContinuousLayout)
```

Creates a new

JSplitPane

with the specified
orientation and redrawing style.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Parameters:** newContinuousLayout

- a boolean, true for the components to
redraw continuously as the divider changes position, false
to wait until the divider position stops changing to redraw
**Throws:** IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT

---

#### JSplitPane

public JSplitPane​(int newOrientation,
boolean newContinuousLayout)

Creates a new

JSplitPane

with the specified
orientation and redrawing style.

JSplitPane

```java
public JSplitPane​(int newOrientation,

Component
newLeftComponent,

Component
newRightComponent)
```

Creates a new

JSplitPane

with the specified
orientation and the specified components.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Parameters:** newLeftComponent

- the

Component

that will
appear on the left
of a horizontally-split pane, or at the top of a
vertically-split pane
**Parameters:** newRightComponent

- the

Component

that will
appear on the right
of a horizontally-split pane, or at the bottom of a
vertically-split pane
**Throws:** IllegalArgumentException

- if

orientation

is not one of: HORIZONTAL_SPLIT or VERTICAL_SPLIT

---

#### JSplitPane

public JSplitPane​(int newOrientation,

Component

newLeftComponent,

Component

newRightComponent)

Creates a new

JSplitPane

with the specified
orientation and the specified components.

JSplitPane

```java
public JSplitPane​(int newOrientation,
boolean newContinuousLayout,

Component
newLeftComponent,

Component
newRightComponent)
```

Creates a new

JSplitPane

with the specified
orientation and
redrawing style, and with the specified components.

**Parameters:** newOrientation

-

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Parameters:** newContinuousLayout

- a boolean, true for the components to
redraw continuously as the divider changes position, false
to wait until the divider position stops changing to redraw
**Parameters:** newLeftComponent

- the

Component

that will
appear on the left
of a horizontally-split pane, or at the top of a
vertically-split pane
**Parameters:** newRightComponent

- the

Component

that will
appear on the right
of a horizontally-split pane, or at the bottom of a
vertically-split pane
**Throws:** IllegalArgumentException

- if

orientation

is not one of HORIZONTAL_SPLIT or VERTICAL_SPLIT

---

#### JSplitPane

public JSplitPane​(int newOrientation,
boolean newContinuousLayout,

Component

newLeftComponent,

Component

newRightComponent)

Creates a new

JSplitPane

with the specified
orientation and
redrawing style, and with the specified components.

Method Detail

- setUI

```java
public void setUI​(
SplitPaneUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

SplitPaneUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- getUI

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The L&F object that renders this component.")
public
SplitPaneUI
getUI()
```

Returns the

SplitPaneUI

that is providing the
current look and feel.

**Overrides:** getUI

in class

JComponent
**Returns:** the

SplitPaneUI

object that renders this component

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="A string that specifies the name of the L&F class.")
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "SplitPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setDividerSize

```java
@BeanProperty
(
description
="The size of the divider.")
public void setDividerSize​(int newSize)
```

Sets the size of the divider.

**Parameters:** newSize

- an integer giving the size of the divider in pixels

- getDividerSize

```java
public int getDividerSize()
```

Returns the size of the divider.

**Returns:** an integer giving the size of the divider in pixels

- setLeftComponent

```java
public void setLeftComponent​(
Component
comp)
```

Sets the component to the left (or above) the divider.

**Parameters:** comp

- the

Component

to display in that position

- getLeftComponent

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The component to the left (or above) the divider.")
public
Component
getLeftComponent()
```

Returns the component to the left (or above) the divider.

**Returns:** the

Component

displayed in that position

- setTopComponent

```java
@BeanProperty
(
bound
=false,

description
="The component above, or to the left of the divider.")
public void setTopComponent​(
Component
comp)
```

Sets the component above, or to the left of the divider.

**Parameters:** comp

- the

Component

to display in that position

- getTopComponent

```java
public
Component
getTopComponent()
```

Returns the component above, or to the left of the divider.

**Returns:** the

Component

displayed in that position

- setRightComponent

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The component to the right (or below) the divider.")
public void setRightComponent​(
Component
comp)
```

Sets the component to the right (or below) the divider.

**Parameters:** comp

- the

Component

to display in that position

- getRightComponent

```java
public
Component
getRightComponent()
```

Returns the component to the right (or below) the divider.

**Returns:** the

Component

displayed in that position

- setBottomComponent

```java
@BeanProperty
(
bound
=false,

description
="The component below, or to the right of the divider.")
public void setBottomComponent​(
Component
comp)
```

Sets the component below, or to the right of the divider.

**Parameters:** comp

- the

Component

to display in that position

- getBottomComponent

```java
public
Component
getBottomComponent()
```

Returns the component below, or to the right of the divider.

**Returns:** the

Component

displayed in that position

- setOneTouchExpandable

```java
@BeanProperty
(
description
="UI widget on the divider to quickly expand/collapse the divider.")
public void setOneTouchExpandable​(boolean newValue)
```

Sets the value of the

oneTouchExpandable

property,
which must be

true

for the

JSplitPane

to provide a UI widget
on the divider to quickly expand/collapse the divider.
The default value of this property is

false

.
Some look and feels might not support one-touch expanding;
they will ignore this property.

**Parameters:** newValue

-

true

to specify that the split pane should provide a
collapse/expand widget
**See Also:** isOneTouchExpandable()

- isOneTouchExpandable

```java
public boolean isOneTouchExpandable()
```

Gets the

oneTouchExpandable

property.

**Returns:** the value of the

oneTouchExpandable

property
**See Also:** setOneTouchExpandable(boolean)

- setLastDividerLocation

```java
@BeanProperty
(
description
="The last location the divider was at.")
public void setLastDividerLocation​(int newLastLocation)
```

Sets the last location the divider was at to

newLastLocation

.

**Parameters:** newLastLocation

- an integer specifying the last divider location
in pixels, from the left (or upper) edge of the pane to the
left (or upper) edge of the divider

- getLastDividerLocation

```java
public int getLastDividerLocation()
```

Returns the last location the divider was at.

**Returns:** an integer specifying the last divider location as a count
of pixels from the left (or upper) edge of the pane to the
left (or upper) edge of the divider

- setOrientation

```java
@BeanProperty
(
enumerationValues
={"JSplitPane.HORIZONTAL_SPLIT","JSplitPane.VERTICAL_SPLIT"},

description
="The orientation, or how the splitter is divided.")
public void setOrientation​(int orientation)
```

Sets the orientation, or how the splitter is divided. The options
are:

- JSplitPane.VERTICAL_SPLIT (above/below orientation of components)

JSplitPane.HORIZONTAL_SPLIT (left/right orientation of components)

**Parameters:** orientation

- an integer specifying the orientation
**Throws:** IllegalArgumentException

- if orientation is not one of:
HORIZONTAL_SPLIT or VERTICAL_SPLIT.

- getOrientation

```java
public int getOrientation()
```

Returns the orientation.

**Returns:** an integer giving the orientation
**See Also:** setOrientation(int)

- setContinuousLayout

```java
@BeanProperty
(
description
="Whether the child components are continuously redisplayed and laid out during user intervention.")
public void setContinuousLayout​(boolean newContinuousLayout)
```

Sets the value of the

continuousLayout

property,
which must be

true

for the child components
to be continuously
redisplayed and laid out during user intervention.
The default value of this property is look and feel dependent.
Some look and feels might not support continuous layout;
they will ignore this property.

**Parameters:** newContinuousLayout

-

true

if the components
should continuously be redrawn as the divider changes position
**See Also:** isContinuousLayout()

- isContinuousLayout

```java
public boolean isContinuousLayout()
```

Gets the

continuousLayout

property.

**Returns:** the value of the

continuousLayout

property
**See Also:** setContinuousLayout(boolean)

- setResizeWeight

```java
@BeanProperty
(
description
="Specifies how to distribute extra space when the split pane resizes.")
public void setResizeWeight​(double value)
```

Specifies how to distribute extra space when the size of the split pane
changes. A value of 0, the default,
indicates the right/bottom component gets all the extra space (the
left/top component acts fixed), where as a value of 1 specifies the
left/top component gets all the extra space (the right/bottom component
acts fixed). Specifically, the left/top component gets (weight * diff)
extra space and the right/bottom component gets (1 - weight) * diff
extra space.

**Parameters:** value

- as described above
**Throws:** IllegalArgumentException

- if

value

is < 0 or > 1
**Since:** 1.3

- getResizeWeight

```java
public double getResizeWeight()
```

Returns the number that determines how extra space is distributed.

**Returns:** how extra space is to be distributed on a resize of the
split pane
**Since:** 1.3

- resetToPreferredSizes

```java
public void resetToPreferredSizes()
```

Lays out the

JSplitPane

layout based on the preferred size
of the children components. This will likely result in changing
the divider location.

- setDividerLocation

```java
@BeanProperty
(
description
="The location of the divider.")
public void setDividerLocation​(double proportionalLocation)
```

Sets the divider location as a percentage of the

JSplitPane

's size.

This method is implemented in terms of

setDividerLocation(int)

.
This method immediately changes the size of the split pane based on
its current size. If the split pane is not correctly realized and on
screen, this method will have no effect (new divider location will
become (current size * proportionalLocation) which is 0).

**Parameters:** proportionalLocation

- a double-precision floating point value
that specifies a percentage, from zero (top/left) to 1.0
(bottom/right)
**Throws:** IllegalArgumentException

- if the specified location is < 0
or > 1.0

- setDividerLocation

```java
@BeanProperty
(
description
="The location of the divider.")
public void setDividerLocation​(int location)
```

Sets the location of the divider. This is passed off to the
look and feel implementation, and then listeners are notified. A value
less than 0 implies the divider should be reset to a value that
attempts to honor the preferred size of the left/top component.
After notifying the listeners, the last divider location is updated,
via

setLastDividerLocation

.

**Parameters:** location

- an int specifying a UI-specific value (typically a
pixel count)

- getDividerLocation

```java
public int getDividerLocation()
```

Returns the last value passed to

setDividerLocation

.
The value returned from this method may differ from the actual
divider location (if

setDividerLocation

was passed a
value bigger than the current size).

**Returns:** an integer specifying the location of the divider

- getMinimumDividerLocation

```java
@BeanProperty
(
bound
=false,

description
="The minimum location of the divider from the L&F.")
public int getMinimumDividerLocation()
```

Returns the minimum location of the divider from the look and feel
implementation.

**Returns:** an integer specifying a UI-specific value for the minimum
location (typically a pixel count); or -1 if the UI is

null

- getMaximumDividerLocation

```java
@BeanProperty
(
bound
=false)
public int getMaximumDividerLocation()
```

Returns the maximum location of the divider from the look and feel
implementation.

**Returns:** an integer specifying a UI-specific value for the maximum
location (typically a pixel count); or -1 if the UI is

null

- remove

```java
public void remove​(
Component
component)
```

Removes the child component,

component

from the
pane. Resets the

leftComponent

or

rightComponent

instance variable, as necessary.

**Overrides:** remove

in class

Container
**Parameters:** component

- the

Component

to remove
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.remove(int)

- remove

```java
public void remove​(int index)
```

Removes the

Component

at the specified index.
Updates the

leftComponent

and

rightComponent

instance variables as necessary, and then messages super.

**Overrides:** remove

in class

Container
**Parameters:** index

- an integer specifying the component to remove, where
1 specifies the left/top component and 2 specifies the
bottom/right component
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

- removeAll

```java
public void removeAll()
```

Removes all the child components from the split pane. Resets the

leftComonent

and

rightComponent

instance variables.

**Overrides:** removeAll

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

- isValidateRoot

```java
@BeanProperty
(
hidden
=true)
public boolean isValidateRoot()
```

Returns true, so that calls to

revalidate

on any descendant of this

JSplitPane

will cause a request to be queued that
will validate the

JSplitPane

and all its descendants.

**Overrides:** isValidateRoot

in class

JComponent
**Returns:** true
**See Also:** JComponent.revalidate()

,

Container.isValidateRoot()

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this split pane.
If

constraints

identifies the left/top or
right/bottom child component, and a component with that identifier
was previously added, it will be removed and then

comp

will be added in its place. If

constraints

is not
one of the known identifiers the layout manager may throw an

IllegalArgumentException

.

The possible constraints objects (Strings) are:

- JSplitPane.TOP

JSplitPane.LEFT

JSplitPane.BOTTOM

JSplitPane.RIGHT

If the

constraints

object is

null

,
the component is added in the
first available position (left/top if open, else right/bottom).

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to add
**Parameters:** constraints

- an

Object

specifying the
layout constraints
(position) for this component
**Parameters:** index

- an integer specifying the index in the container's
list.
**Throws:** IllegalArgumentException

- if the

constraints

object does not match an existing component
**See Also:** Container.addImpl(Component, Object, int)

- paintChildren

```java
protected void paintChildren​(
Graphics
g)
```

Subclassed to message the UI with

finishedPaintingChildren

after super has been messaged, as well as painting the border.

**Overrides:** paintChildren

in class

JComponent
**Parameters:** g

- the

Graphics

context within which to paint
**See Also:** JComponent.paint(java.awt.Graphics)

,

Container.paint(java.awt.Graphics)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JSplitPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JSplitPane

.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this SplitPane.")
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JSplitPane.
For split panes, the AccessibleContext takes the form of an
AccessibleJSplitPane.
A new AccessibleJSplitPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJSplitPane that serves as the
AccessibleContext of this JSplitPane

---

#### Method Detail

setUI

```java
public void setUI​(
SplitPaneUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

SplitPaneUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

---

#### setUI

public void setUI​(

SplitPaneUI

ui)

Sets the L&F object that renders this component.

getUI

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The L&F object that renders this component.")
public
SplitPaneUI
getUI()
```

Returns the

SplitPaneUI

that is providing the
current look and feel.

**Overrides:** getUI

in class

JComponent
**Returns:** the

SplitPaneUI

object that renders this component

---

#### getUI

@BeanProperty

(

bound

=false,

expert

=true,

description

="The L&F object that renders this component.")
public

SplitPaneUI

getUI()

Returns the

SplitPaneUI

that is providing the
current look and feel.

updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

getUIClassID

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="A string that specifies the name of the L&F class.")
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "SplitPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false,

expert

=true,

description

="A string that specifies the name of the L&F class.")
public

String

getUIClassID()

Returns the name of the L&F class that renders this component.

setDividerSize

```java
@BeanProperty
(
description
="The size of the divider.")
public void setDividerSize​(int newSize)
```

Sets the size of the divider.

**Parameters:** newSize

- an integer giving the size of the divider in pixels

---

#### setDividerSize

@BeanProperty

(

description

="The size of the divider.")
public void setDividerSize​(int newSize)

Sets the size of the divider.

getDividerSize

```java
public int getDividerSize()
```

Returns the size of the divider.

**Returns:** an integer giving the size of the divider in pixels

---

#### getDividerSize

public int getDividerSize()

Returns the size of the divider.

setLeftComponent

```java
public void setLeftComponent​(
Component
comp)
```

Sets the component to the left (or above) the divider.

**Parameters:** comp

- the

Component

to display in that position

---

#### setLeftComponent

public void setLeftComponent​(

Component

comp)

Sets the component to the left (or above) the divider.

getLeftComponent

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The component to the left (or above) the divider.")
public
Component
getLeftComponent()
```

Returns the component to the left (or above) the divider.

**Returns:** the

Component

displayed in that position

---

#### getLeftComponent

@BeanProperty

(

bound

=false,

preferred

=true,

description

="The component to the left (or above) the divider.")
public

Component

getLeftComponent()

Returns the component to the left (or above) the divider.

setTopComponent

```java
@BeanProperty
(
bound
=false,

description
="The component above, or to the left of the divider.")
public void setTopComponent​(
Component
comp)
```

Sets the component above, or to the left of the divider.

**Parameters:** comp

- the

Component

to display in that position

---

#### setTopComponent

@BeanProperty

(

bound

=false,

description

="The component above, or to the left of the divider.")
public void setTopComponent​(

Component

comp)

Sets the component above, or to the left of the divider.

getTopComponent

```java
public
Component
getTopComponent()
```

Returns the component above, or to the left of the divider.

**Returns:** the

Component

displayed in that position

---

#### getTopComponent

public

Component

getTopComponent()

Returns the component above, or to the left of the divider.

setRightComponent

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The component to the right (or below) the divider.")
public void setRightComponent​(
Component
comp)
```

Sets the component to the right (or below) the divider.

**Parameters:** comp

- the

Component

to display in that position

---

#### setRightComponent

@BeanProperty

(

bound

=false,

preferred

=true,

description

="The component to the right (or below) the divider.")
public void setRightComponent​(

Component

comp)

Sets the component to the right (or below) the divider.

getRightComponent

```java
public
Component
getRightComponent()
```

Returns the component to the right (or below) the divider.

**Returns:** the

Component

displayed in that position

---

#### getRightComponent

public

Component

getRightComponent()

Returns the component to the right (or below) the divider.

setBottomComponent

```java
@BeanProperty
(
bound
=false,

description
="The component below, or to the right of the divider.")
public void setBottomComponent​(
Component
comp)
```

Sets the component below, or to the right of the divider.

**Parameters:** comp

- the

Component

to display in that position

---

#### setBottomComponent

@BeanProperty

(

bound

=false,

description

="The component below, or to the right of the divider.")
public void setBottomComponent​(

Component

comp)

Sets the component below, or to the right of the divider.

getBottomComponent

```java
public
Component
getBottomComponent()
```

Returns the component below, or to the right of the divider.

**Returns:** the

Component

displayed in that position

---

#### getBottomComponent

public

Component

getBottomComponent()

Returns the component below, or to the right of the divider.

setOneTouchExpandable

```java
@BeanProperty
(
description
="UI widget on the divider to quickly expand/collapse the divider.")
public void setOneTouchExpandable​(boolean newValue)
```

Sets the value of the

oneTouchExpandable

property,
which must be

true

for the

JSplitPane

to provide a UI widget
on the divider to quickly expand/collapse the divider.
The default value of this property is

false

.
Some look and feels might not support one-touch expanding;
they will ignore this property.

**Parameters:** newValue

-

true

to specify that the split pane should provide a
collapse/expand widget
**See Also:** isOneTouchExpandable()

---

#### setOneTouchExpandable

@BeanProperty

(

description

="UI widget on the divider to quickly expand/collapse the divider.")
public void setOneTouchExpandable​(boolean newValue)

Sets the value of the

oneTouchExpandable

property,
which must be

true

for the

JSplitPane

to provide a UI widget
on the divider to quickly expand/collapse the divider.
The default value of this property is

false

.
Some look and feels might not support one-touch expanding;
they will ignore this property.

isOneTouchExpandable

```java
public boolean isOneTouchExpandable()
```

Gets the

oneTouchExpandable

property.

**Returns:** the value of the

oneTouchExpandable

property
**See Also:** setOneTouchExpandable(boolean)

---

#### isOneTouchExpandable

public boolean isOneTouchExpandable()

Gets the

oneTouchExpandable

property.

setLastDividerLocation

```java
@BeanProperty
(
description
="The last location the divider was at.")
public void setLastDividerLocation​(int newLastLocation)
```

Sets the last location the divider was at to

newLastLocation

.

**Parameters:** newLastLocation

- an integer specifying the last divider location
in pixels, from the left (or upper) edge of the pane to the
left (or upper) edge of the divider

---

#### setLastDividerLocation

@BeanProperty

(

description

="The last location the divider was at.")
public void setLastDividerLocation​(int newLastLocation)

Sets the last location the divider was at to

newLastLocation

.

getLastDividerLocation

```java
public int getLastDividerLocation()
```

Returns the last location the divider was at.

**Returns:** an integer specifying the last divider location as a count
of pixels from the left (or upper) edge of the pane to the
left (or upper) edge of the divider

---

#### getLastDividerLocation

public int getLastDividerLocation()

Returns the last location the divider was at.

setOrientation

```java
@BeanProperty
(
enumerationValues
={"JSplitPane.HORIZONTAL_SPLIT","JSplitPane.VERTICAL_SPLIT"},

description
="The orientation, or how the splitter is divided.")
public void setOrientation​(int orientation)
```

Sets the orientation, or how the splitter is divided. The options
are:

- JSplitPane.VERTICAL_SPLIT (above/below orientation of components)

JSplitPane.HORIZONTAL_SPLIT (left/right orientation of components)

**Parameters:** orientation

- an integer specifying the orientation
**Throws:** IllegalArgumentException

- if orientation is not one of:
HORIZONTAL_SPLIT or VERTICAL_SPLIT.

---

#### setOrientation

@BeanProperty

(

enumerationValues

={"JSplitPane.HORIZONTAL_SPLIT","JSplitPane.VERTICAL_SPLIT"},

description

="The orientation, or how the splitter is divided.")
public void setOrientation​(int orientation)

Sets the orientation, or how the splitter is divided. The options
are:

- JSplitPane.VERTICAL_SPLIT (above/below orientation of components)

JSplitPane.HORIZONTAL_SPLIT (left/right orientation of components)

JSplitPane.VERTICAL_SPLIT (above/below orientation of components)

JSplitPane.HORIZONTAL_SPLIT (left/right orientation of components)

getOrientation

```java
public int getOrientation()
```

Returns the orientation.

**Returns:** an integer giving the orientation
**See Also:** setOrientation(int)

---

#### getOrientation

public int getOrientation()

Returns the orientation.

setContinuousLayout

```java
@BeanProperty
(
description
="Whether the child components are continuously redisplayed and laid out during user intervention.")
public void setContinuousLayout​(boolean newContinuousLayout)
```

Sets the value of the

continuousLayout

property,
which must be

true

for the child components
to be continuously
redisplayed and laid out during user intervention.
The default value of this property is look and feel dependent.
Some look and feels might not support continuous layout;
they will ignore this property.

**Parameters:** newContinuousLayout

-

true

if the components
should continuously be redrawn as the divider changes position
**See Also:** isContinuousLayout()

---

#### setContinuousLayout

@BeanProperty

(

description

="Whether the child components are continuously redisplayed and laid out during user intervention.")
public void setContinuousLayout​(boolean newContinuousLayout)

Sets the value of the

continuousLayout

property,
which must be

true

for the child components
to be continuously
redisplayed and laid out during user intervention.
The default value of this property is look and feel dependent.
Some look and feels might not support continuous layout;
they will ignore this property.

isContinuousLayout

```java
public boolean isContinuousLayout()
```

Gets the

continuousLayout

property.

**Returns:** the value of the

continuousLayout

property
**See Also:** setContinuousLayout(boolean)

---

#### isContinuousLayout

public boolean isContinuousLayout()

Gets the

continuousLayout

property.

setResizeWeight

```java
@BeanProperty
(
description
="Specifies how to distribute extra space when the split pane resizes.")
public void setResizeWeight​(double value)
```

Specifies how to distribute extra space when the size of the split pane
changes. A value of 0, the default,
indicates the right/bottom component gets all the extra space (the
left/top component acts fixed), where as a value of 1 specifies the
left/top component gets all the extra space (the right/bottom component
acts fixed). Specifically, the left/top component gets (weight * diff)
extra space and the right/bottom component gets (1 - weight) * diff
extra space.

**Parameters:** value

- as described above
**Throws:** IllegalArgumentException

- if

value

is < 0 or > 1
**Since:** 1.3

---

#### setResizeWeight

@BeanProperty

(

description

="Specifies how to distribute extra space when the split pane resizes.")
public void setResizeWeight​(double value)

Specifies how to distribute extra space when the size of the split pane
changes. A value of 0, the default,
indicates the right/bottom component gets all the extra space (the
left/top component acts fixed), where as a value of 1 specifies the
left/top component gets all the extra space (the right/bottom component
acts fixed). Specifically, the left/top component gets (weight * diff)
extra space and the right/bottom component gets (1 - weight) * diff
extra space.

getResizeWeight

```java
public double getResizeWeight()
```

Returns the number that determines how extra space is distributed.

**Returns:** how extra space is to be distributed on a resize of the
split pane
**Since:** 1.3

---

#### getResizeWeight

public double getResizeWeight()

Returns the number that determines how extra space is distributed.

resetToPreferredSizes

```java
public void resetToPreferredSizes()
```

Lays out the

JSplitPane

layout based on the preferred size
of the children components. This will likely result in changing
the divider location.

---

#### resetToPreferredSizes

public void resetToPreferredSizes()

Lays out the

JSplitPane

layout based on the preferred size
of the children components. This will likely result in changing
the divider location.

setDividerLocation

```java
@BeanProperty
(
description
="The location of the divider.")
public void setDividerLocation​(double proportionalLocation)
```

Sets the divider location as a percentage of the

JSplitPane

's size.

This method is implemented in terms of

setDividerLocation(int)

.
This method immediately changes the size of the split pane based on
its current size. If the split pane is not correctly realized and on
screen, this method will have no effect (new divider location will
become (current size * proportionalLocation) which is 0).

**Parameters:** proportionalLocation

- a double-precision floating point value
that specifies a percentage, from zero (top/left) to 1.0
(bottom/right)
**Throws:** IllegalArgumentException

- if the specified location is < 0
or > 1.0

---

#### setDividerLocation

@BeanProperty

(

description

="The location of the divider.")
public void setDividerLocation​(double proportionalLocation)

Sets the divider location as a percentage of the

JSplitPane

's size.

This method is implemented in terms of

setDividerLocation(int)

.
This method immediately changes the size of the split pane based on
its current size. If the split pane is not correctly realized and on
screen, this method will have no effect (new divider location will
become (current size * proportionalLocation) which is 0).

This method is implemented in terms of

setDividerLocation(int)

.
This method immediately changes the size of the split pane based on
its current size. If the split pane is not correctly realized and on
screen, this method will have no effect (new divider location will
become (current size * proportionalLocation) which is 0).

setDividerLocation

```java
@BeanProperty
(
description
="The location of the divider.")
public void setDividerLocation​(int location)
```

Sets the location of the divider. This is passed off to the
look and feel implementation, and then listeners are notified. A value
less than 0 implies the divider should be reset to a value that
attempts to honor the preferred size of the left/top component.
After notifying the listeners, the last divider location is updated,
via

setLastDividerLocation

.

**Parameters:** location

- an int specifying a UI-specific value (typically a
pixel count)

---

#### setDividerLocation

@BeanProperty

(

description

="The location of the divider.")
public void setDividerLocation​(int location)

Sets the location of the divider. This is passed off to the
look and feel implementation, and then listeners are notified. A value
less than 0 implies the divider should be reset to a value that
attempts to honor the preferred size of the left/top component.
After notifying the listeners, the last divider location is updated,
via

setLastDividerLocation

.

getDividerLocation

```java
public int getDividerLocation()
```

Returns the last value passed to

setDividerLocation

.
The value returned from this method may differ from the actual
divider location (if

setDividerLocation

was passed a
value bigger than the current size).

**Returns:** an integer specifying the location of the divider

---

#### getDividerLocation

public int getDividerLocation()

Returns the last value passed to

setDividerLocation

.
The value returned from this method may differ from the actual
divider location (if

setDividerLocation

was passed a
value bigger than the current size).

getMinimumDividerLocation

```java
@BeanProperty
(
bound
=false,

description
="The minimum location of the divider from the L&F.")
public int getMinimumDividerLocation()
```

Returns the minimum location of the divider from the look and feel
implementation.

**Returns:** an integer specifying a UI-specific value for the minimum
location (typically a pixel count); or -1 if the UI is

null

---

#### getMinimumDividerLocation

@BeanProperty

(

bound

=false,

description

="The minimum location of the divider from the L&F.")
public int getMinimumDividerLocation()

Returns the minimum location of the divider from the look and feel
implementation.

getMaximumDividerLocation

```java
@BeanProperty
(
bound
=false)
public int getMaximumDividerLocation()
```

Returns the maximum location of the divider from the look and feel
implementation.

**Returns:** an integer specifying a UI-specific value for the maximum
location (typically a pixel count); or -1 if the UI is

null

---

#### getMaximumDividerLocation

@BeanProperty

(

bound

=false)
public int getMaximumDividerLocation()

Returns the maximum location of the divider from the look and feel
implementation.

remove

```java
public void remove​(
Component
component)
```

Removes the child component,

component

from the
pane. Resets the

leftComponent

or

rightComponent

instance variable, as necessary.

**Overrides:** remove

in class

Container
**Parameters:** component

- the

Component

to remove
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.remove(int)

---

#### remove

public void remove​(

Component

component)

Removes the child component,

component

from the
pane. Resets the

leftComponent

or

rightComponent

instance variable, as necessary.

remove

```java
public void remove​(int index)
```

Removes the

Component

at the specified index.
Updates the

leftComponent

and

rightComponent

instance variables as necessary, and then messages super.

**Overrides:** remove

in class

Container
**Parameters:** index

- an integer specifying the component to remove, where
1 specifies the left/top component and 2 specifies the
bottom/right component
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.validate()

,

Container.getComponentCount()

---

#### remove

public void remove​(int index)

Removes the

Component

at the specified index.
Updates the

leftComponent

and

rightComponent

instance variables as necessary, and then messages super.

removeAll

```java
public void removeAll()
```

Removes all the child components from the split pane. Resets the

leftComonent

and

rightComponent

instance variables.

**Overrides:** removeAll

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

---

#### removeAll

public void removeAll()

Removes all the child components from the split pane. Resets the

leftComonent

and

rightComponent

instance variables.

isValidateRoot

```java
@BeanProperty
(
hidden
=true)
public boolean isValidateRoot()
```

Returns true, so that calls to

revalidate

on any descendant of this

JSplitPane

will cause a request to be queued that
will validate the

JSplitPane

and all its descendants.

**Overrides:** isValidateRoot

in class

JComponent
**Returns:** true
**See Also:** JComponent.revalidate()

,

Container.isValidateRoot()

---

#### isValidateRoot

@BeanProperty

(

hidden

=true)
public boolean isValidateRoot()

Returns true, so that calls to

revalidate

on any descendant of this

JSplitPane

will cause a request to be queued that
will validate the

JSplitPane

and all its descendants.

addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this split pane.
If

constraints

identifies the left/top or
right/bottom child component, and a component with that identifier
was previously added, it will be removed and then

comp

will be added in its place. If

constraints

is not
one of the known identifiers the layout manager may throw an

IllegalArgumentException

.

The possible constraints objects (Strings) are:

- JSplitPane.TOP

JSplitPane.LEFT

JSplitPane.BOTTOM

JSplitPane.RIGHT

If the

constraints

object is

null

,
the component is added in the
first available position (left/top if open, else right/bottom).

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to add
**Parameters:** constraints

- an

Object

specifying the
layout constraints
(position) for this component
**Parameters:** index

- an integer specifying the index in the container's
list.
**Throws:** IllegalArgumentException

- if the

constraints

object does not match an existing component
**See Also:** Container.addImpl(Component, Object, int)

---

#### addImpl

protected void addImpl​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this split pane.
If

constraints

identifies the left/top or
right/bottom child component, and a component with that identifier
was previously added, it will be removed and then

comp

will be added in its place. If

constraints

is not
one of the known identifiers the layout manager may throw an

IllegalArgumentException

.

The possible constraints objects (Strings) are:

- JSplitPane.TOP

JSplitPane.LEFT

JSplitPane.BOTTOM

JSplitPane.RIGHT

If the

constraints

object is

null

,
the component is added in the
first available position (left/top if open, else right/bottom).

The possible constraints objects (Strings) are:

- JSplitPane.TOP

JSplitPane.LEFT

JSplitPane.BOTTOM

JSplitPane.RIGHT

If the

constraints

object is

null

,
the component is added in the
first available position (left/top if open, else right/bottom).

JSplitPane.TOP

JSplitPane.LEFT

JSplitPane.BOTTOM

JSplitPane.RIGHT

paintChildren

```java
protected void paintChildren​(
Graphics
g)
```

Subclassed to message the UI with

finishedPaintingChildren

after super has been messaged, as well as painting the border.

**Overrides:** paintChildren

in class

JComponent
**Parameters:** g

- the

Graphics

context within which to paint
**See Also:** JComponent.paint(java.awt.Graphics)

,

Container.paint(java.awt.Graphics)

---

#### paintChildren

protected void paintChildren​(

Graphics

g)

Subclassed to message the UI with

finishedPaintingChildren

after super has been messaged, as well as painting the border.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JSplitPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JSplitPane

.

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JSplitPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this SplitPane.")
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JSplitPane.
For split panes, the AccessibleContext takes the form of an
AccessibleJSplitPane.
A new AccessibleJSplitPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJSplitPane that serves as the
AccessibleContext of this JSplitPane

---

#### getAccessibleContext

@BeanProperty

(

bound

=false,

expert

=true,

description

="The AccessibleContext associated with this SplitPane.")
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JSplitPane.
For split panes, the AccessibleContext takes the form of an
AccessibleJSplitPane.
A new AccessibleJSplitPane instance is created if necessary.

---

