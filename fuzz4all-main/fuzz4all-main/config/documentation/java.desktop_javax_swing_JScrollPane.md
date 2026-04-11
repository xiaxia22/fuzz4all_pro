# Class JScrollPane

**Source:** `java.desktop\javax\swing\JScrollPane.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A specialized container that manages a viewport, optional scrollbars and headers")
public class
JScrollPane

extends
JComponent

implements
ScrollPaneConstants
,
Accessible
```

Provides a scrollable view of a lightweight component.
A

JScrollPane

manages a viewport, optional
vertical and horizontal scroll bars, and optional row and
column heading viewports.
You can find task-oriented documentation of

JScrollPane

in

How to Use Scroll Panes

,
a section in

The Java Tutorial

. Note that

JScrollPane

does not support heavyweight components.

Example

The

JViewport

provides a window,
or "viewport" onto a data
source -- for example, a text file. That data source is the
"scrollable client" (aka data model) displayed by the

JViewport

view.
A

JScrollPane

basically consists of

JScrollBar

s,
a

JViewport

, and the wiring between them,
as shown in the diagram at right.

In addition to the scroll bars and viewport,
a

JScrollPane

can have a
column header and a row header. Each of these is a

JViewport

object that
you specify with

setRowHeaderView

,
and

setColumnHeaderView

.
The column header viewport automatically scrolls left and right, tracking
the left-right scrolling of the main viewport.
(It never scrolls vertically, however.)
The row header acts in a similar fashion.

Where two scroll bars meet, the row header meets the column header,
or a scroll bar meets one of the headers, both components stop short
of the corner, leaving a rectangular space which is, by default, empty.
These spaces can potentially exist in any number of the four corners.
In the previous diagram, the top right space is present and identified
by the label "corner component".

Any number of these empty spaces can be replaced by using the

setCorner

method to add a component to a particular corner.
(Note: The same component cannot be added to multiple corners.)
This is useful if there's
some extra decoration or function you'd like to add to the scroll pane.
The size of each corner component is entirely determined by the size of the
headers and/or scroll bars that surround it.

A corner component will only be visible if there is an empty space in that
corner for it to exist in. For example, consider a component set into the
top right corner of a scroll pane with a column header. If the scroll pane's
vertical scrollbar is not present, perhaps because the view component hasn't
grown large enough to require it, then the corner component will not be
shown (since there is no empty space in that corner created by the meeting
of the header and vertical scroll bar). Forcing the scroll bar to always be
shown, using

setVerticalScrollBarPolicy(VERTICAL_SCROLLBAR_ALWAYS)

,
will ensure that the space for the corner component always exists.

To add a border around the main viewport,
you can use

setViewportBorder

.
(Of course, you can also add a border around the whole scroll pane using

setBorder

.)

A common operation to want to do is to set the background color that will
be used if the main viewport view is smaller than the viewport, or is
not opaque. This can be accomplished by setting the background color
of the viewport, via

scrollPane.getViewport().setBackground()

.
The reason for setting the color of the viewport and not the scrollpane
is that by default

JViewport

is opaque
which, among other things, means it will completely fill
in its background using its background color. Therefore when

JScrollPane

draws its background the viewport will
usually draw over it.

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

,

ScrollPaneConstants

---

### Field Details

#### protected int verticalScrollBarPolicy

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

**See Also:**
- setVerticalScrollBarPolicy(int)

---

#### protected int horizontalScrollBarPolicy

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

**See Also:**
- setHorizontalScrollBarPolicy(int)

---

#### protected
JViewport
viewport

The scrollpane's viewport child. Default is an empty

JViewport

.

**See Also:**
- setViewport(javax.swing.JViewport)

---

#### protected
JScrollBar
verticalScrollBar

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

**See Also:**
- setVerticalScrollBar(javax.swing.JScrollBar)

---

#### protected
JScrollBar
horizontalScrollBar

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

**See Also:**
- setHorizontalScrollBar(javax.swing.JScrollBar)

---

#### protected
JViewport
rowHeader

The row header child. Default is

null

.

**See Also:**
- setRowHeader(javax.swing.JViewport)

---

#### protected
JViewport
columnHeader

The column header child. Default is

null

.

**See Also:**
- setColumnHeader(javax.swing.JViewport)

---

#### protected
Component
lowerLeft

The component to display in the lower left corner.
Default is

null

.

**See Also:**
- setCorner(java.lang.String, java.awt.Component)

---

#### protected
Component
lowerRight

The component to display in the lower right corner.
Default is

null

.

**See Also:**
- setCorner(java.lang.String, java.awt.Component)

---

#### protected
Component
upperLeft

The component to display in the upper left corner.
Default is

null

.

**See Also:**
- setCorner(java.lang.String, java.awt.Component)

---

#### protected
Component
upperRight

The component to display in the upper right corner.
Default is

null

.

**See Also:**
- setCorner(java.lang.String, java.awt.Component)

---

### Constructor Details

#### public JScrollPane​(
Component
view,
int vsbPolicy,
int hsbPolicy)

Creates a

JScrollPane

that displays the view
component in a viewport
whose view position can be controlled with a pair of scrollbars.
The scrollbar policies specify when the scrollbars are displayed,
For example, if

vsbPolicy

is

VERTICAL_SCROLLBAR_AS_NEEDED

then the vertical scrollbar only appears if the view doesn't fit
vertically. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

**Parameters:**
- view

- the component to display in the scrollpanes viewport
- vsbPolicy

- an integer that specifies the vertical
scrollbar policy
- hsbPolicy

- an integer that specifies the horizontal
scrollbar policy

**See Also:**
- setViewportView(java.awt.Component)

---

#### public JScrollPane​(
Component
view)

Creates a

JScrollPane

that displays the
contents of the specified
component, where both horizontal and vertical scrollbars appear
whenever the component's contents are larger than the view.

**Parameters:**
- view

- the component to display in the scrollpane's viewport

**See Also:**
- setViewportView(java.awt.Component)

---

#### public JScrollPane​(int vsbPolicy,
int hsbPolicy)

Creates an empty (no viewport view)

JScrollPane

with specified
scrollbar policies. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

**Parameters:**
- vsbPolicy

- an integer that specifies the vertical
scrollbar policy
- hsbPolicy

- an integer that specifies the horizontal
scrollbar policy

**See Also:**
- setViewportView(java.awt.Component)

---

#### public JScrollPane()

Creates an empty (no viewport view)

JScrollPane

where both horizontal and vertical scrollbars appear when needed.

---

### Method Details

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public
ScrollPaneUI
getUI()

Returns the look and feel (L&F) object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

ScrollPaneUI

object that renders this
component

**See Also:**
- setUI(javax.swing.plaf.ScrollPaneUI)

---

#### public void setUI​(
ScrollPaneUI
ui)

Sets the

ScrollPaneUI

object that provides the
look and feel (L&F) for this component.

**Parameters:**
- ui

- the

ScrollPaneUI

L&F object

**See Also:**
- getUI()

---

#### public void updateUI()

Replaces the current

ScrollPaneUI

object with a version
from the current default look and feel.
To be called when the default look and feel changes.

**Overrides:**
- updateUI

in class

JComponent

**See Also:**
- JComponent.updateUI()

,

UIManager.getUI(javax.swing.JComponent)

---

#### @BeanProperty
(
bound
=false,

hidden
=true)
public
String
getUIClassID()

Returns the suffix used to construct the name of the L&F class used to
render this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "ScrollPaneUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### public void setLayout​(
LayoutManager
layout)

Sets the layout manager for this

JScrollPane

.
This method overrides

setLayout

in

java.awt.Container

to ensure that only

LayoutManager

s which
are subclasses of

ScrollPaneLayout

can be used in a

JScrollPane

. If

layout

is non-null, this
will invoke

syncWithScrollPane

on it.

**Overrides:**
- setLayout

in class

Container

**Parameters:**
- layout

- the specified layout manager

**Throws:**
- ClassCastException

- if layout is not a

ScrollPaneLayout

**See Also:**
- Container.getLayout()

,

Container.setLayout(java.awt.LayoutManager)

---

#### @BeanProperty
(
hidden
=true)
public boolean isValidateRoot()

Overridden to return true so that any calls to

revalidate

on any descendants of this

JScrollPane

will cause the
entire tree beginning with this

JScrollPane

to be
validated.

**Overrides:**
- isValidateRoot

in class

JComponent

**Returns:**
- true

**See Also:**
- Container.validate()

,

JComponent.revalidate()

,

JComponent.isValidateRoot()

,

Container.isValidateRoot()

---

#### public int getVerticalScrollBarPolicy()

Returns the vertical scroll bar policy value.

**Returns:**
- the

verticalScrollBarPolicy

property

**See Also:**
- setVerticalScrollBarPolicy(int)

---

#### @BeanProperty
(
preferred
=true,

enumerationValues
={"ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER","ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS"},

description
="The scrollpane vertical scrollbar policy")
public void setVerticalScrollBarPolicy​(int policy)

Determines when the vertical scrollbar appears in the scrollpane.
Legal values are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

**Parameters:**
- policy

- one of the three values listed above

**Throws:**
- IllegalArgumentException

- if

policy

is not one of the legal values shown above

**See Also:**
- getVerticalScrollBarPolicy()

---

#### public int getHorizontalScrollBarPolicy()

Returns the horizontal scroll bar policy value.

**Returns:**
- the

horizontalScrollBarPolicy

property

**See Also:**
- setHorizontalScrollBarPolicy(int)

---

#### @BeanProperty
(
preferred
=true,

enumerationValues
={"ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS"},

description
="The scrollpane scrollbar policy")
public void setHorizontalScrollBarPolicy​(int policy)

Determines when the horizontal scrollbar appears in the scrollpane.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

**Parameters:**
- policy

- one of the three values listed above

**Throws:**
- IllegalArgumentException

- if

policy

is not one of the legal values shown above

**See Also:**
- getHorizontalScrollBarPolicy()

---

#### public
Border
getViewportBorder()

Returns the

Border

object that surrounds the viewport.

**Returns:**
- the

viewportBorder

property

**See Also:**
- setViewportBorder(javax.swing.border.Border)

---

#### @BeanProperty
(
preferred
=true,

description
="The border around the viewport.")
public void setViewportBorder​(
Border
viewportBorder)

Adds a border around the viewport. Note that the border isn't
set on the viewport directly,

JViewport

doesn't support
the

JComponent

border property.
Similarly setting the

JScrollPane

s
viewport doesn't affect the

viewportBorder

property.

The default value of this property is computed by the look
and feel implementation.

**Parameters:**
- viewportBorder

- the border to be added

**See Also:**
- getViewportBorder()

,

setViewport(javax.swing.JViewport)

---

#### @BeanProperty
(
bound
=false)
public
Rectangle
getViewportBorderBounds()

Returns the bounds of the viewport's border.

**Returns:**
- a

Rectangle

object specifying the viewport border

---

#### public
JScrollBar
createHorizontalScrollBar()

Returns a

JScrollPane.ScrollBar

by default.
Subclasses may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to
create the horizontal scrollbar.

**Returns:**
- a

JScrollBar

with a horizontal orientation

**See Also:**
- JScrollBar

---

#### public
JScrollBar
getHorizontalScrollBar()

Returns the horizontal scroll bar that controls the viewport's
horizontal view position.

**Returns:**
- the

horizontalScrollBar

property

**See Also:**
- setHorizontalScrollBar(javax.swing.JScrollBar)

---

#### @BeanProperty
(
expert
=true,

description
="The horizontal scrollbar.")
public void setHorizontalScrollBar​(
JScrollBar
horizontalScrollBar)

Adds the scrollbar that controls the viewport's horizontal view
position to the scrollpane.
This is usually unnecessary, as

JScrollPane

creates
horizontal and vertical scrollbars by default.

**Parameters:**
- horizontalScrollBar

- the horizontal scrollbar to be added

**See Also:**
- createHorizontalScrollBar()

,

getHorizontalScrollBar()

---

#### public
JScrollBar
createVerticalScrollBar()

Returns a

JScrollPane.ScrollBar

by default. Subclasses
may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to create the
vertical scrollbar.

**Returns:**
- a

JScrollBar

with a vertical orientation

**See Also:**
- JScrollBar

---

#### public
JScrollBar
getVerticalScrollBar()

Returns the vertical scroll bar that controls the viewports
vertical view position.

**Returns:**
- the

verticalScrollBar

property

**See Also:**
- setVerticalScrollBar(javax.swing.JScrollBar)

---

#### @BeanProperty
(
expert
=true,

description
="The vertical scrollbar.")
public void setVerticalScrollBar​(
JScrollBar
verticalScrollBar)

Adds the scrollbar that controls the viewports vertical view position
to the scrollpane. This is usually unnecessary,
as

JScrollPane

creates vertical and
horizontal scrollbars by default.

**Parameters:**
- verticalScrollBar

- the new vertical scrollbar to be added

**See Also:**
- createVerticalScrollBar()

,

getVerticalScrollBar()

---

#### protected
JViewport
createViewport()

Returns a new

JViewport

by default.
Used to create the
viewport (as needed) in

setViewportView

,

setRowHeaderView

, and

setColumnHeaderView

.
Subclasses may override this method to return a subclass of

JViewport

.

**Returns:**
- a new

JViewport

---

#### public
JViewport
getViewport()

Returns the current

JViewport

.

**Returns:**
- the

viewport

property

**See Also:**
- setViewport(javax.swing.JViewport)

---

#### @BeanProperty
(
expert
=true,

visualUpdate
=true,

description
="The viewport child for this scrollpane")
public void setViewport​(
JViewport
viewport)

Removes the old viewport (if there is one); forces the
viewPosition of the new viewport to be in the +x,+y quadrant;
syncs up the row and column headers (if there are any) with the
new viewport; and finally syncs the scrollbars and
headers with the new viewport.

Most applications will find it more convenient to use

setViewportView

to add a viewport and a view to the scrollpane.

**Parameters:**
- viewport

- the new viewport to be used; if viewport is

null

, the old viewport is still removed
and the new viewport is set to

null

**See Also:**
- createViewport()

,

getViewport()

,

setViewportView(java.awt.Component)

---

#### public void setViewportView​(
Component
view)

Creates a viewport if necessary and then sets its view. Applications
that don't provide the view directly to the

JScrollPane

constructor
should use this method to specify the scrollable child that's going
to be displayed in the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
```

Applications should not add children directly to the scrollpane.

**Parameters:**
- view

- the component to add to the viewport

**See Also:**
- setViewport(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

---

#### public
JViewport
getRowHeader()

Returns the row header.

**Returns:**
- the

rowHeader

property

**See Also:**
- setRowHeader(javax.swing.JViewport)

---

#### @BeanProperty
(
expert
=true,

description
="The row header child for this scrollpane")
public void setRowHeader​(
JViewport
rowHeader)

Removes the old rowHeader, if it exists; if the new rowHeader
isn't

null

, syncs the y coordinate of its
viewPosition with
the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setRowHeaderView

to add a row header component and its viewport to the scroll pane.

**Parameters:**
- rowHeader

- the new row header to be used; if

null

the old row header is still removed and the new rowHeader
is set to

null

**See Also:**
- getRowHeader()

,

setRowHeaderView(java.awt.Component)

---

#### public void setRowHeaderView​(
Component
view)

Creates a row-header viewport if necessary, sets
its view and then adds the row-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setRowHeaderView(myBigComponentsRowHeader);
```

**Parameters:**
- view

- the component to display as the row header

**See Also:**
- setRowHeader(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

---

#### public
JViewport
getColumnHeader()

Returns the column header.

**Returns:**
- the

columnHeader

property

**See Also:**
- setColumnHeader(javax.swing.JViewport)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The column header child for this scrollpane")
public void setColumnHeader​(
JViewport
columnHeader)

Removes the old columnHeader, if it exists; if the new columnHeader
isn't

null

, syncs the x coordinate of its viewPosition
with the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setColumnHeaderView

to add a column header component and its viewport to the scroll pane.

**Parameters:**
- columnHeader

- a

JViewport

which is the new column header

**See Also:**
- getColumnHeader()

,

setColumnHeaderView(java.awt.Component)

---

#### public void setColumnHeaderView​(
Component
view)

Creates a column-header viewport if necessary, sets
its view, and then adds the column-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setColumnHeaderView(myBigComponentsColumnHeader);
```

**Parameters:**
- view

- the component to display as the column header

**See Also:**
- setColumnHeader(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

---

#### public
Component
getCorner​(
String
key)

Returns the component at the specified corner. The

key

value specifying the corner is one of:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

**Parameters:**
- key

- one of the values as shown above

**Returns:**
- the corner component (which may be

null

)
identified by the given key, or

null

if the key is invalid

**See Also:**
- setCorner(java.lang.String, java.awt.Component)

---

#### public void setCorner​(
String
key,

Component
corner)

Adds a child that will appear in one of the scroll panes
corners, if there's room. For example with both scrollbars
showing (on the right and bottom edges of the scrollpane)
the lower left corner component will be shown in the space
between ends of the two scrollbars. Legal values for
the

key

are:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

Although "corner" doesn't match any beans property
signature,

PropertyChange

events are generated with the
property name set to the corner key.

**Parameters:**
- key

- identifies which corner the component will appear in
- corner

- one of the following components:

- lowerLeft

lowerRight

upperLeft

upperRight

**Throws:**
- IllegalArgumentException

- if corner key is invalid

---

#### public void setComponentOrientation​(
ComponentOrientation
co)

Sets the orientation for the vertical and horizontal
scrollbars as determined by the

ComponentOrientation

argument.

**Overrides:**
- setComponentOrientation

in class

Component

**Parameters:**
- co

- one of the following values:

- java.awt.ComponentOrientation.LEFT_TO_RIGHT

java.awt.ComponentOrientation.RIGHT_TO_LEFT

java.awt.ComponentOrientation.UNKNOWN

**See Also:**
- ComponentOrientation

---

#### @BeanProperty
(
description
="Flag for enabling/disabling mouse wheel scrolling")
public boolean isWheelScrollingEnabled()

Indicates whether or not scrolling will take place in response to the
mouse wheel. Wheel scrolling is enabled by default.

**Returns:**
- true if mouse wheel scrolling is enabled, false otherwise

**See Also:**
- setWheelScrollingEnabled(boolean)

**Since:**
- 1.4

---

#### @BeanProperty
(
description
="Flag for enabling/disabling mouse wheel scrolling")
public void setWheelScrollingEnabled​(boolean handleWheel)

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

**Parameters:**
- handleWheel

-

true

if scrolling should be done
automatically for a MouseWheelEvent,

false

otherwise.

**See Also:**
- isWheelScrollingEnabled()

,

MouseWheelEvent

,

MouseWheelListener

**Since:**
- 1.4

---

#### protected
String
paramString()

Returns a string representation of this

JScrollPane

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

JScrollPane

.

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleJScrollPane.
A new AccessibleJScrollPane instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJScrollPane that serves as the
AccessibleContext of this JScrollPane

---

### Additional Sections

#### Class JScrollPane

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JScrollPane

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JScrollPane

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JScrollPane

javax.swing.JComponent

- javax.swing.JScrollPane

javax.swing.JScrollPane

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

ScrollPaneConstants

```java
@JavaBean
(
defaultProperty
="UI",

description
="A specialized container that manages a viewport, optional scrollbars and headers")
public class
JScrollPane

extends
JComponent

implements
ScrollPaneConstants
,
Accessible
```

Provides a scrollable view of a lightweight component.
A

JScrollPane

manages a viewport, optional
vertical and horizontal scroll bars, and optional row and
column heading viewports.
You can find task-oriented documentation of

JScrollPane

in

How to Use Scroll Panes

,
a section in

The Java Tutorial

. Note that

JScrollPane

does not support heavyweight components.

Example

The

JViewport

provides a window,
or "viewport" onto a data
source -- for example, a text file. That data source is the
"scrollable client" (aka data model) displayed by the

JViewport

view.
A

JScrollPane

basically consists of

JScrollBar

s,
a

JViewport

, and the wiring between them,
as shown in the diagram at right.

In addition to the scroll bars and viewport,
a

JScrollPane

can have a
column header and a row header. Each of these is a

JViewport

object that
you specify with

setRowHeaderView

,
and

setColumnHeaderView

.
The column header viewport automatically scrolls left and right, tracking
the left-right scrolling of the main viewport.
(It never scrolls vertically, however.)
The row header acts in a similar fashion.

Where two scroll bars meet, the row header meets the column header,
or a scroll bar meets one of the headers, both components stop short
of the corner, leaving a rectangular space which is, by default, empty.
These spaces can potentially exist in any number of the four corners.
In the previous diagram, the top right space is present and identified
by the label "corner component".

Any number of these empty spaces can be replaced by using the

setCorner

method to add a component to a particular corner.
(Note: The same component cannot be added to multiple corners.)
This is useful if there's
some extra decoration or function you'd like to add to the scroll pane.
The size of each corner component is entirely determined by the size of the
headers and/or scroll bars that surround it.

A corner component will only be visible if there is an empty space in that
corner for it to exist in. For example, consider a component set into the
top right corner of a scroll pane with a column header. If the scroll pane's
vertical scrollbar is not present, perhaps because the view component hasn't
grown large enough to require it, then the corner component will not be
shown (since there is no empty space in that corner created by the meeting
of the header and vertical scroll bar). Forcing the scroll bar to always be
shown, using

setVerticalScrollBarPolicy(VERTICAL_SCROLLBAR_ALWAYS)

,
will ensure that the space for the corner component always exists.

To add a border around the main viewport,
you can use

setViewportBorder

.
(Of course, you can also add a border around the whole scroll pane using

setBorder

.)

A common operation to want to do is to set the background color that will
be used if the main viewport view is smaller than the viewport, or is
not opaque. This can be accomplished by setting the background color
of the viewport, via

scrollPane.getViewport().setBackground()

.
The reason for setting the color of the viewport and not the scrollpane
is that by default

JViewport

is opaque
which, among other things, means it will completely fill
in its background using its background color. Therefore when

JScrollPane

draws its background the viewport will
usually draw over it.

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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
**See Also:** JScrollBar

,

JViewport

,

ScrollPaneLayout

,

Scrollable

,

Component.getPreferredSize()

,

setViewportView(java.awt.Component)

,

setRowHeaderView(java.awt.Component)

,

setColumnHeaderView(java.awt.Component)

,

setCorner(java.lang.String, java.awt.Component)

,

setViewportBorder(javax.swing.border.Border)

,

Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A specialized container that manages a viewport, optional scrollbars and headers")
public class

JScrollPane

extends

JComponent

implements

ScrollPaneConstants

,

Accessible

Provides a scrollable view of a lightweight component.
A

JScrollPane

manages a viewport, optional
vertical and horizontal scroll bars, and optional row and
column heading viewports.
You can find task-oriented documentation of

JScrollPane

in

How to Use Scroll Panes

,
a section in

The Java Tutorial

. Note that

JScrollPane

does not support heavyweight components.

Example

The

JViewport

provides a window,
or "viewport" onto a data
source -- for example, a text file. That data source is the
"scrollable client" (aka data model) displayed by the

JViewport

view.
A

JScrollPane

basically consists of

JScrollBar

s,
a

JViewport

, and the wiring between them,
as shown in the diagram at right.

In addition to the scroll bars and viewport,
a

JScrollPane

can have a
column header and a row header. Each of these is a

JViewport

object that
you specify with

setRowHeaderView

,
and

setColumnHeaderView

.
The column header viewport automatically scrolls left and right, tracking
the left-right scrolling of the main viewport.
(It never scrolls vertically, however.)
The row header acts in a similar fashion.

Where two scroll bars meet, the row header meets the column header,
or a scroll bar meets one of the headers, both components stop short
of the corner, leaving a rectangular space which is, by default, empty.
These spaces can potentially exist in any number of the four corners.
In the previous diagram, the top right space is present and identified
by the label "corner component".

Any number of these empty spaces can be replaced by using the

setCorner

method to add a component to a particular corner.
(Note: The same component cannot be added to multiple corners.)
This is useful if there's
some extra decoration or function you'd like to add to the scroll pane.
The size of each corner component is entirely determined by the size of the
headers and/or scroll bars that surround it.

A corner component will only be visible if there is an empty space in that
corner for it to exist in. For example, consider a component set into the
top right corner of a scroll pane with a column header. If the scroll pane's
vertical scrollbar is not present, perhaps because the view component hasn't
grown large enough to require it, then the corner component will not be
shown (since there is no empty space in that corner created by the meeting
of the header and vertical scroll bar). Forcing the scroll bar to always be
shown, using

setVerticalScrollBarPolicy(VERTICAL_SCROLLBAR_ALWAYS)

,
will ensure that the space for the corner component always exists.

To add a border around the main viewport,
you can use

setViewportBorder

.
(Of course, you can also add a border around the whole scroll pane using

setBorder

.)

A common operation to want to do is to set the background color that will
be used if the main viewport view is smaller than the viewport, or is
not opaque. This can be accomplished by setting the background color
of the viewport, via

scrollPane.getViewport().setBackground()

.
The reason for setting the color of the viewport and not the scrollpane
is that by default

JViewport

is opaque
which, among other things, means it will completely fill
in its background using its background color. Therefore when

JScrollPane

draws its background the viewport will
usually draw over it.

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

In addition to the scroll bars and viewport,
a

JScrollPane

can have a
column header and a row header. Each of these is a

JViewport

object that
you specify with

setRowHeaderView

,
and

setColumnHeaderView

.
The column header viewport automatically scrolls left and right, tracking
the left-right scrolling of the main viewport.
(It never scrolls vertically, however.)
The row header acts in a similar fashion.

Where two scroll bars meet, the row header meets the column header,
or a scroll bar meets one of the headers, both components stop short
of the corner, leaving a rectangular space which is, by default, empty.
These spaces can potentially exist in any number of the four corners.
In the previous diagram, the top right space is present and identified
by the label "corner component".

Any number of these empty spaces can be replaced by using the

setCorner

method to add a component to a particular corner.
(Note: The same component cannot be added to multiple corners.)
This is useful if there's
some extra decoration or function you'd like to add to the scroll pane.
The size of each corner component is entirely determined by the size of the
headers and/or scroll bars that surround it.

A corner component will only be visible if there is an empty space in that
corner for it to exist in. For example, consider a component set into the
top right corner of a scroll pane with a column header. If the scroll pane's
vertical scrollbar is not present, perhaps because the view component hasn't
grown large enough to require it, then the corner component will not be
shown (since there is no empty space in that corner created by the meeting
of the header and vertical scroll bar). Forcing the scroll bar to always be
shown, using

setVerticalScrollBarPolicy(VERTICAL_SCROLLBAR_ALWAYS)

,
will ensure that the space for the corner component always exists.

To add a border around the main viewport,
you can use

setViewportBorder

.
(Of course, you can also add a border around the whole scroll pane using

setBorder

.)

A common operation to want to do is to set the background color that will
be used if the main viewport view is smaller than the viewport, or is
not opaque. This can be accomplished by setting the background color
of the viewport, via

scrollPane.getViewport().setBackground()

.
The reason for setting the color of the viewport and not the scrollpane
is that by default

JViewport

is opaque
which, among other things, means it will completely fill
in its background using its background color. Therefore when

JScrollPane

draws its background the viewport will
usually draw over it.

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

Where two scroll bars meet, the row header meets the column header,
or a scroll bar meets one of the headers, both components stop short
of the corner, leaving a rectangular space which is, by default, empty.
These spaces can potentially exist in any number of the four corners.
In the previous diagram, the top right space is present and identified
by the label "corner component".

Any number of these empty spaces can be replaced by using the

setCorner

method to add a component to a particular corner.
(Note: The same component cannot be added to multiple corners.)
This is useful if there's
some extra decoration or function you'd like to add to the scroll pane.
The size of each corner component is entirely determined by the size of the
headers and/or scroll bars that surround it.

A corner component will only be visible if there is an empty space in that
corner for it to exist in. For example, consider a component set into the
top right corner of a scroll pane with a column header. If the scroll pane's
vertical scrollbar is not present, perhaps because the view component hasn't
grown large enough to require it, then the corner component will not be
shown (since there is no empty space in that corner created by the meeting
of the header and vertical scroll bar). Forcing the scroll bar to always be
shown, using

setVerticalScrollBarPolicy(VERTICAL_SCROLLBAR_ALWAYS)

,
will ensure that the space for the corner component always exists.

To add a border around the main viewport,
you can use

setViewportBorder

.
(Of course, you can also add a border around the whole scroll pane using

setBorder

.)

A common operation to want to do is to set the background color that will
be used if the main viewport view is smaller than the viewport, or is
not opaque. This can be accomplished by setting the background color
of the viewport, via

scrollPane.getViewport().setBackground()

.
The reason for setting the color of the viewport and not the scrollpane
is that by default

JViewport

is opaque
which, among other things, means it will completely fill
in its background using its background color. Therefore when

JScrollPane

draws its background the viewport will
usually draw over it.

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

Any number of these empty spaces can be replaced by using the

setCorner

method to add a component to a particular corner.
(Note: The same component cannot be added to multiple corners.)
This is useful if there's
some extra decoration or function you'd like to add to the scroll pane.
The size of each corner component is entirely determined by the size of the
headers and/or scroll bars that surround it.

A corner component will only be visible if there is an empty space in that
corner for it to exist in. For example, consider a component set into the
top right corner of a scroll pane with a column header. If the scroll pane's
vertical scrollbar is not present, perhaps because the view component hasn't
grown large enough to require it, then the corner component will not be
shown (since there is no empty space in that corner created by the meeting
of the header and vertical scroll bar). Forcing the scroll bar to always be
shown, using

setVerticalScrollBarPolicy(VERTICAL_SCROLLBAR_ALWAYS)

,
will ensure that the space for the corner component always exists.

To add a border around the main viewport,
you can use

setViewportBorder

.
(Of course, you can also add a border around the whole scroll pane using

setBorder

.)

A common operation to want to do is to set the background color that will
be used if the main viewport view is smaller than the viewport, or is
not opaque. This can be accomplished by setting the background color
of the viewport, via

scrollPane.getViewport().setBackground()

.
The reason for setting the color of the viewport and not the scrollpane
is that by default

JViewport

is opaque
which, among other things, means it will completely fill
in its background using its background color. Therefore when

JScrollPane

draws its background the viewport will
usually draw over it.

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

A corner component will only be visible if there is an empty space in that
corner for it to exist in. For example, consider a component set into the
top right corner of a scroll pane with a column header. If the scroll pane's
vertical scrollbar is not present, perhaps because the view component hasn't
grown large enough to require it, then the corner component will not be
shown (since there is no empty space in that corner created by the meeting
of the header and vertical scroll bar). Forcing the scroll bar to always be
shown, using

setVerticalScrollBarPolicy(VERTICAL_SCROLLBAR_ALWAYS)

,
will ensure that the space for the corner component always exists.

To add a border around the main viewport,
you can use

setViewportBorder

.
(Of course, you can also add a border around the whole scroll pane using

setBorder

.)

A common operation to want to do is to set the background color that will
be used if the main viewport view is smaller than the viewport, or is
not opaque. This can be accomplished by setting the background color
of the viewport, via

scrollPane.getViewport().setBackground()

.
The reason for setting the color of the viewport and not the scrollpane
is that by default

JViewport

is opaque
which, among other things, means it will completely fill
in its background using its background color. Therefore when

JScrollPane

draws its background the viewport will
usually draw over it.

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

To add a border around the main viewport,
you can use

setViewportBorder

.
(Of course, you can also add a border around the whole scroll pane using

setBorder

.)

A common operation to want to do is to set the background color that will
be used if the main viewport view is smaller than the viewport, or is
not opaque. This can be accomplished by setting the background color
of the viewport, via

scrollPane.getViewport().setBackground()

.
The reason for setting the color of the viewport and not the scrollpane
is that by default

JViewport

is opaque
which, among other things, means it will completely fill
in its background using its background color. Therefore when

JScrollPane

draws its background the viewport will
usually draw over it.

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

A common operation to want to do is to set the background color that will
be used if the main viewport view is smaller than the viewport, or is
not opaque. This can be accomplished by setting the background color
of the viewport, via

scrollPane.getViewport().setBackground()

.
The reason for setting the color of the viewport and not the scrollpane
is that by default

JViewport

is opaque
which, among other things, means it will completely fill
in its background using its background color. Therefore when

JScrollPane

draws its background the viewport will
usually draw over it.

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

By default

JScrollPane

uses

ScrollPaneLayout

to handle the layout of its child Components.

ScrollPaneLayout

determines the size to make the viewport view in one of two ways:

- If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

If the view implements

Scrollable

a combination of

getPreferredScrollableViewportSize

,

getScrollableTracksViewportWidth

and

getScrollableTracksViewportHeight

is used, otherwise

getPreferredSize

is used.

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

JScrollPane.AccessibleJScrollPane

This class implements accessibility support for the

JScrollPane

class.

protected class

JScrollPane.ScrollBar

By default

JScrollPane

creates scrollbars
that are instances
of this class.

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

protected

JViewport

columnHeader

The column header child.

protected

JScrollBar

horizontalScrollBar

The scrollpane's horizontal scrollbar child.

protected int

horizontalScrollBarPolicy

The display policy for the horizontal scrollbar.

protected

Component

lowerLeft

The component to display in the lower left corner.

protected

Component

lowerRight

The component to display in the lower right corner.

protected

JViewport

rowHeader

The row header child.

protected

Component

upperLeft

The component to display in the upper left corner.

protected

Component

upperRight

The component to display in the upper right corner.

protected

JScrollBar

verticalScrollBar

The scrollpane's vertical scrollbar child.

protected int

verticalScrollBarPolicy

The display policy for the vertical scrollbar.

protected

JViewport

viewport

The scrollpane's viewport child.

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

- Fields declared in interface javax.swing.

ScrollPaneConstants

COLUMN_HEADER

,

HORIZONTAL_SCROLLBAR

,

HORIZONTAL_SCROLLBAR_ALWAYS

,

HORIZONTAL_SCROLLBAR_AS_NEEDED

,

HORIZONTAL_SCROLLBAR_NEVER

,

HORIZONTAL_SCROLLBAR_POLICY

,

LOWER_LEADING_CORNER

,

LOWER_LEFT_CORNER

,

LOWER_RIGHT_CORNER

,

LOWER_TRAILING_CORNER

,

ROW_HEADER

,

UPPER_LEADING_CORNER

,

UPPER_LEFT_CORNER

,

UPPER_RIGHT_CORNER

,

UPPER_TRAILING_CORNER

,

VERTICAL_SCROLLBAR

,

VERTICAL_SCROLLBAR_ALWAYS

,

VERTICAL_SCROLLBAR_AS_NEEDED

,

VERTICAL_SCROLLBAR_NEVER

,

VERTICAL_SCROLLBAR_POLICY

,

VIEWPORT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JScrollPane

()

Creates an empty (no viewport view)

JScrollPane

where both horizontal and vertical scrollbars appear when needed.

JScrollPane

​(int vsbPolicy,
int hsbPolicy)

Creates an empty (no viewport view)

JScrollPane

with specified
scrollbar policies.

JScrollPane

​(

Component

view)

Creates a

JScrollPane

that displays the
contents of the specified
component, where both horizontal and vertical scrollbars appear
whenever the component's contents are larger than the view.

JScrollPane

​(

Component

view,
int vsbPolicy,
int hsbPolicy)

Creates a

JScrollPane

that displays the view
component in a viewport
whose view position can be controlled with a pair of scrollbars.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JScrollBar

createHorizontalScrollBar

()

Returns a

JScrollPane.ScrollBar

by default.

JScrollBar

createVerticalScrollBar

()

Returns a

JScrollPane.ScrollBar

by default.

protected

JViewport

createViewport

()

Returns a new

JViewport

by default.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JScrollPane.

JViewport

getColumnHeader

()

Returns the column header.

Component

getCorner

​(

String

key)

Returns the component at the specified corner.

JScrollBar

getHorizontalScrollBar

()

Returns the horizontal scroll bar that controls the viewport's
horizontal view position.

int

getHorizontalScrollBarPolicy

()

Returns the horizontal scroll bar policy value.

JViewport

getRowHeader

()

Returns the row header.

ScrollPaneUI

getUI

()

Returns the look and feel (L&F) object that renders this component.

String

getUIClassID

()

Returns the suffix used to construct the name of the L&F class used to
render this component.

JScrollBar

getVerticalScrollBar

()

Returns the vertical scroll bar that controls the viewports
vertical view position.

int

getVerticalScrollBarPolicy

()

Returns the vertical scroll bar policy value.

JViewport

getViewport

()

Returns the current

JViewport

.

Border

getViewportBorder

()

Returns the

Border

object that surrounds the viewport.

Rectangle

getViewportBorderBounds

()

Returns the bounds of the viewport's border.

boolean

isValidateRoot

()

Overridden to return true so that any calls to

revalidate

on any descendants of this

JScrollPane

will cause the
entire tree beginning with this

JScrollPane

to be
validated.

boolean

isWheelScrollingEnabled

()

Indicates whether or not scrolling will take place in response to the
mouse wheel.

protected

String

paramString

()

Returns a string representation of this

JScrollPane

.

void

setColumnHeader

​(

JViewport

columnHeader)

Removes the old columnHeader, if it exists; if the new columnHeader
isn't

null

, syncs the x coordinate of its viewPosition
with the viewport (if there is one) and then adds it to the scroll pane.

void

setColumnHeaderView

​(

Component

view)

Creates a column-header viewport if necessary, sets
its view, and then adds the column-header viewport
to the scrollpane.

void

setComponentOrientation

​(

ComponentOrientation

co)

Sets the orientation for the vertical and horizontal
scrollbars as determined by the

ComponentOrientation

argument.

void

setCorner

​(

String

key,

Component

corner)

Adds a child that will appear in one of the scroll panes
corners, if there's room.

void

setHorizontalScrollBar

​(

JScrollBar

horizontalScrollBar)

Adds the scrollbar that controls the viewport's horizontal view
position to the scrollpane.

void

setHorizontalScrollBarPolicy

​(int policy)

Determines when the horizontal scrollbar appears in the scrollpane.

void

setLayout

​(

LayoutManager

layout)

Sets the layout manager for this

JScrollPane

.

void

setRowHeader

​(

JViewport

rowHeader)

Removes the old rowHeader, if it exists; if the new rowHeader
isn't

null

, syncs the y coordinate of its
viewPosition with
the viewport (if there is one) and then adds it to the scroll pane.

void

setRowHeaderView

​(

Component

view)

Creates a row-header viewport if necessary, sets
its view and then adds the row-header viewport
to the scrollpane.

void

setUI

​(

ScrollPaneUI

ui)

Sets the

ScrollPaneUI

object that provides the
look and feel (L&F) for this component.

void

setVerticalScrollBar

​(

JScrollBar

verticalScrollBar)

Adds the scrollbar that controls the viewports vertical view position
to the scrollpane.

void

setVerticalScrollBarPolicy

​(int policy)

Determines when the vertical scrollbar appears in the scrollpane.

void

setViewport

​(

JViewport

viewport)

Removes the old viewport (if there is one); forces the
viewPosition of the new viewport to be in the +x,+y quadrant;
syncs up the row and column headers (if there are any) with the
new viewport; and finally syncs the scrollbars and
headers with the new viewport.

void

setViewportBorder

​(

Border

viewportBorder)

Adds a border around the viewport.

void

setViewportView

​(

Component

view)

Creates a viewport if necessary and then sets its view.

void

setWheelScrollingEnabled

​(boolean handleWheel)

Enables/disables scrolling in response to movement of the mouse wheel.

void

updateUI

()

Replaces the current

ScrollPaneUI

object with a version
from the current default look and feel.

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

paintChildren

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

addImpl

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

remove

,

remove

,

removeAll

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

JScrollPane.AccessibleJScrollPane

This class implements accessibility support for the

JScrollPane

class.

protected class

JScrollPane.ScrollBar

By default

JScrollPane

creates scrollbars
that are instances
of this class.

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

JScrollPane

class.

By default

JScrollPane

creates scrollbars
that are instances
of this class.

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

protected

JViewport

columnHeader

The column header child.

protected

JScrollBar

horizontalScrollBar

The scrollpane's horizontal scrollbar child.

protected int

horizontalScrollBarPolicy

The display policy for the horizontal scrollbar.

protected

Component

lowerLeft

The component to display in the lower left corner.

protected

Component

lowerRight

The component to display in the lower right corner.

protected

JViewport

rowHeader

The row header child.

protected

Component

upperLeft

The component to display in the upper left corner.

protected

Component

upperRight

The component to display in the upper right corner.

protected

JScrollBar

verticalScrollBar

The scrollpane's vertical scrollbar child.

protected int

verticalScrollBarPolicy

The display policy for the vertical scrollbar.

protected

JViewport

viewport

The scrollpane's viewport child.

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

- Fields declared in interface javax.swing.

ScrollPaneConstants

COLUMN_HEADER

,

HORIZONTAL_SCROLLBAR

,

HORIZONTAL_SCROLLBAR_ALWAYS

,

HORIZONTAL_SCROLLBAR_AS_NEEDED

,

HORIZONTAL_SCROLLBAR_NEVER

,

HORIZONTAL_SCROLLBAR_POLICY

,

LOWER_LEADING_CORNER

,

LOWER_LEFT_CORNER

,

LOWER_RIGHT_CORNER

,

LOWER_TRAILING_CORNER

,

ROW_HEADER

,

UPPER_LEADING_CORNER

,

UPPER_LEFT_CORNER

,

UPPER_RIGHT_CORNER

,

UPPER_TRAILING_CORNER

,

VERTICAL_SCROLLBAR

,

VERTICAL_SCROLLBAR_ALWAYS

,

VERTICAL_SCROLLBAR_AS_NEEDED

,

VERTICAL_SCROLLBAR_NEVER

,

VERTICAL_SCROLLBAR_POLICY

,

VIEWPORT

---

#### Field Summary

The column header child.

The scrollpane's horizontal scrollbar child.

The display policy for the horizontal scrollbar.

The component to display in the lower left corner.

The component to display in the lower right corner.

The row header child.

The component to display in the upper left corner.

The component to display in the upper right corner.

The scrollpane's vertical scrollbar child.

The display policy for the vertical scrollbar.

The scrollpane's viewport child.

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

Fields declared in interface javax.swing.

ScrollPaneConstants

COLUMN_HEADER

,

HORIZONTAL_SCROLLBAR

,

HORIZONTAL_SCROLLBAR_ALWAYS

,

HORIZONTAL_SCROLLBAR_AS_NEEDED

,

HORIZONTAL_SCROLLBAR_NEVER

,

HORIZONTAL_SCROLLBAR_POLICY

,

LOWER_LEADING_CORNER

,

LOWER_LEFT_CORNER

,

LOWER_RIGHT_CORNER

,

LOWER_TRAILING_CORNER

,

ROW_HEADER

,

UPPER_LEADING_CORNER

,

UPPER_LEFT_CORNER

,

UPPER_RIGHT_CORNER

,

UPPER_TRAILING_CORNER

,

VERTICAL_SCROLLBAR

,

VERTICAL_SCROLLBAR_ALWAYS

,

VERTICAL_SCROLLBAR_AS_NEEDED

,

VERTICAL_SCROLLBAR_NEVER

,

VERTICAL_SCROLLBAR_POLICY

,

VIEWPORT

---

#### Fields declared in interface javax.swing. ScrollPaneConstants

Constructor Summary

Constructors

Constructor

Description

JScrollPane

()

Creates an empty (no viewport view)

JScrollPane

where both horizontal and vertical scrollbars appear when needed.

JScrollPane

​(int vsbPolicy,
int hsbPolicy)

Creates an empty (no viewport view)

JScrollPane

with specified
scrollbar policies.

JScrollPane

​(

Component

view)

Creates a

JScrollPane

that displays the
contents of the specified
component, where both horizontal and vertical scrollbars appear
whenever the component's contents are larger than the view.

JScrollPane

​(

Component

view,
int vsbPolicy,
int hsbPolicy)

Creates a

JScrollPane

that displays the view
component in a viewport
whose view position can be controlled with a pair of scrollbars.

---

#### Constructor Summary

Creates an empty (no viewport view)

JScrollPane

where both horizontal and vertical scrollbars appear when needed.

Creates an empty (no viewport view)

JScrollPane

with specified
scrollbar policies.

Creates a

JScrollPane

that displays the
contents of the specified
component, where both horizontal and vertical scrollbars appear
whenever the component's contents are larger than the view.

Creates a

JScrollPane

that displays the view
component in a viewport
whose view position can be controlled with a pair of scrollbars.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JScrollBar

createHorizontalScrollBar

()

Returns a

JScrollPane.ScrollBar

by default.

JScrollBar

createVerticalScrollBar

()

Returns a

JScrollPane.ScrollBar

by default.

protected

JViewport

createViewport

()

Returns a new

JViewport

by default.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JScrollPane.

JViewport

getColumnHeader

()

Returns the column header.

Component

getCorner

​(

String

key)

Returns the component at the specified corner.

JScrollBar

getHorizontalScrollBar

()

Returns the horizontal scroll bar that controls the viewport's
horizontal view position.

int

getHorizontalScrollBarPolicy

()

Returns the horizontal scroll bar policy value.

JViewport

getRowHeader

()

Returns the row header.

ScrollPaneUI

getUI

()

Returns the look and feel (L&F) object that renders this component.

String

getUIClassID

()

Returns the suffix used to construct the name of the L&F class used to
render this component.

JScrollBar

getVerticalScrollBar

()

Returns the vertical scroll bar that controls the viewports
vertical view position.

int

getVerticalScrollBarPolicy

()

Returns the vertical scroll bar policy value.

JViewport

getViewport

()

Returns the current

JViewport

.

Border

getViewportBorder

()

Returns the

Border

object that surrounds the viewport.

Rectangle

getViewportBorderBounds

()

Returns the bounds of the viewport's border.

boolean

isValidateRoot

()

Overridden to return true so that any calls to

revalidate

on any descendants of this

JScrollPane

will cause the
entire tree beginning with this

JScrollPane

to be
validated.

boolean

isWheelScrollingEnabled

()

Indicates whether or not scrolling will take place in response to the
mouse wheel.

protected

String

paramString

()

Returns a string representation of this

JScrollPane

.

void

setColumnHeader

​(

JViewport

columnHeader)

Removes the old columnHeader, if it exists; if the new columnHeader
isn't

null

, syncs the x coordinate of its viewPosition
with the viewport (if there is one) and then adds it to the scroll pane.

void

setColumnHeaderView

​(

Component

view)

Creates a column-header viewport if necessary, sets
its view, and then adds the column-header viewport
to the scrollpane.

void

setComponentOrientation

​(

ComponentOrientation

co)

Sets the orientation for the vertical and horizontal
scrollbars as determined by the

ComponentOrientation

argument.

void

setCorner

​(

String

key,

Component

corner)

Adds a child that will appear in one of the scroll panes
corners, if there's room.

void

setHorizontalScrollBar

​(

JScrollBar

horizontalScrollBar)

Adds the scrollbar that controls the viewport's horizontal view
position to the scrollpane.

void

setHorizontalScrollBarPolicy

​(int policy)

Determines when the horizontal scrollbar appears in the scrollpane.

void

setLayout

​(

LayoutManager

layout)

Sets the layout manager for this

JScrollPane

.

void

setRowHeader

​(

JViewport

rowHeader)

Removes the old rowHeader, if it exists; if the new rowHeader
isn't

null

, syncs the y coordinate of its
viewPosition with
the viewport (if there is one) and then adds it to the scroll pane.

void

setRowHeaderView

​(

Component

view)

Creates a row-header viewport if necessary, sets
its view and then adds the row-header viewport
to the scrollpane.

void

setUI

​(

ScrollPaneUI

ui)

Sets the

ScrollPaneUI

object that provides the
look and feel (L&F) for this component.

void

setVerticalScrollBar

​(

JScrollBar

verticalScrollBar)

Adds the scrollbar that controls the viewports vertical view position
to the scrollpane.

void

setVerticalScrollBarPolicy

​(int policy)

Determines when the vertical scrollbar appears in the scrollpane.

void

setViewport

​(

JViewport

viewport)

Removes the old viewport (if there is one); forces the
viewPosition of the new viewport to be in the +x,+y quadrant;
syncs up the row and column headers (if there are any) with the
new viewport; and finally syncs the scrollbars and
headers with the new viewport.

void

setViewportBorder

​(

Border

viewportBorder)

Adds a border around the viewport.

void

setViewportView

​(

Component

view)

Creates a viewport if necessary and then sets its view.

void

setWheelScrollingEnabled

​(boolean handleWheel)

Enables/disables scrolling in response to movement of the mouse wheel.

void

updateUI

()

Replaces the current

ScrollPaneUI

object with a version
from the current default look and feel.

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

paintChildren

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

addImpl

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

remove

,

remove

,

removeAll

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

Returns a

JScrollPane.ScrollBar

by default.

Returns a new

JViewport

by default.

Gets the AccessibleContext associated with this JScrollPane.

Returns the column header.

Returns the component at the specified corner.

Returns the horizontal scroll bar that controls the viewport's
horizontal view position.

Returns the horizontal scroll bar policy value.

Returns the row header.

Returns the look and feel (L&F) object that renders this component.

Returns the suffix used to construct the name of the L&F class used to
render this component.

Returns the vertical scroll bar that controls the viewports
vertical view position.

Returns the vertical scroll bar policy value.

Returns the current

JViewport

.

Returns the

Border

object that surrounds the viewport.

Returns the bounds of the viewport's border.

Overridden to return true so that any calls to

revalidate

on any descendants of this

JScrollPane

will cause the
entire tree beginning with this

JScrollPane

to be
validated.

Indicates whether or not scrolling will take place in response to the
mouse wheel.

Returns a string representation of this

JScrollPane

.

Removes the old columnHeader, if it exists; if the new columnHeader
isn't

null

, syncs the x coordinate of its viewPosition
with the viewport (if there is one) and then adds it to the scroll pane.

Creates a column-header viewport if necessary, sets
its view, and then adds the column-header viewport
to the scrollpane.

Sets the orientation for the vertical and horizontal
scrollbars as determined by the

ComponentOrientation

argument.

Adds a child that will appear in one of the scroll panes
corners, if there's room.

Adds the scrollbar that controls the viewport's horizontal view
position to the scrollpane.

Determines when the horizontal scrollbar appears in the scrollpane.

Sets the layout manager for this

JScrollPane

.

Removes the old rowHeader, if it exists; if the new rowHeader
isn't

null

, syncs the y coordinate of its
viewPosition with
the viewport (if there is one) and then adds it to the scroll pane.

Creates a row-header viewport if necessary, sets
its view and then adds the row-header viewport
to the scrollpane.

Sets the

ScrollPaneUI

object that provides the
look and feel (L&F) for this component.

Adds the scrollbar that controls the viewports vertical view position
to the scrollpane.

Determines when the vertical scrollbar appears in the scrollpane.

Removes the old viewport (if there is one); forces the
viewPosition of the new viewport to be in the +x,+y quadrant;
syncs up the row and column headers (if there are any) with the
new viewport; and finally syncs the scrollbars and
headers with the new viewport.

Adds a border around the viewport.

Creates a viewport if necessary and then sets its view.

Enables/disables scrolling in response to movement of the mouse wheel.

Replaces the current

ScrollPaneUI

object with a version
from the current default look and feel.

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

paintChildren

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

addImpl

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

remove

,

remove

,

removeAll

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

- verticalScrollBarPolicy

```java
protected int verticalScrollBarPolicy
```

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

**See Also:** setVerticalScrollBarPolicy(int)

- horizontalScrollBarPolicy

```java
protected int horizontalScrollBarPolicy
```

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

**See Also:** setHorizontalScrollBarPolicy(int)

- viewport

```java
protected
JViewport
viewport
```

The scrollpane's viewport child. Default is an empty

JViewport

.

**See Also:** setViewport(javax.swing.JViewport)

- verticalScrollBar

```java
protected
JScrollBar
verticalScrollBar
```

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

**See Also:** setVerticalScrollBar(javax.swing.JScrollBar)

- horizontalScrollBar

```java
protected
JScrollBar
horizontalScrollBar
```

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

**See Also:** setHorizontalScrollBar(javax.swing.JScrollBar)

- rowHeader

```java
protected
JViewport
rowHeader
```

The row header child. Default is

null

.

**See Also:** setRowHeader(javax.swing.JViewport)

- columnHeader

```java
protected
JViewport
columnHeader
```

The column header child. Default is

null

.

**See Also:** setColumnHeader(javax.swing.JViewport)

- lowerLeft

```java
protected
Component
lowerLeft
```

The component to display in the lower left corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

- lowerRight

```java
protected
Component
lowerRight
```

The component to display in the lower right corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

- upperLeft

```java
protected
Component
upperLeft
```

The component to display in the upper left corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

- upperRight

```java
protected
Component
upperRight
```

The component to display in the upper right corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JScrollPane

```java
public JScrollPane​(
Component
view,
int vsbPolicy,
int hsbPolicy)
```

Creates a

JScrollPane

that displays the view
component in a viewport
whose view position can be controlled with a pair of scrollbars.
The scrollbar policies specify when the scrollbars are displayed,
For example, if

vsbPolicy

is

VERTICAL_SCROLLBAR_AS_NEEDED

then the vertical scrollbar only appears if the view doesn't fit
vertically. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

**Parameters:** view

- the component to display in the scrollpanes viewport
**Parameters:** vsbPolicy

- an integer that specifies the vertical
scrollbar policy
**Parameters:** hsbPolicy

- an integer that specifies the horizontal
scrollbar policy
**See Also:** setViewportView(java.awt.Component)

- JScrollPane

```java
public JScrollPane​(
Component
view)
```

Creates a

JScrollPane

that displays the
contents of the specified
component, where both horizontal and vertical scrollbars appear
whenever the component's contents are larger than the view.

**Parameters:** view

- the component to display in the scrollpane's viewport
**See Also:** setViewportView(java.awt.Component)

- JScrollPane

```java
public JScrollPane​(int vsbPolicy,
int hsbPolicy)
```

Creates an empty (no viewport view)

JScrollPane

with specified
scrollbar policies. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

**Parameters:** vsbPolicy

- an integer that specifies the vertical
scrollbar policy
**Parameters:** hsbPolicy

- an integer that specifies the horizontal
scrollbar policy
**See Also:** setViewportView(java.awt.Component)

- JScrollPane

```java
public JScrollPane()
```

Creates an empty (no viewport view)

JScrollPane

where both horizontal and vertical scrollbars appear when needed.

============ METHOD DETAIL ==========

- Method Detail

- getUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public
ScrollPaneUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

ScrollPaneUI

object that renders this
component
**See Also:** setUI(javax.swing.plaf.ScrollPaneUI)

- setUI

```java
public void setUI​(
ScrollPaneUI
ui)
```

Sets the

ScrollPaneUI

object that provides the
look and feel (L&F) for this component.

**Parameters:** ui

- the

ScrollPaneUI

L&F object
**See Also:** getUI()

- updateUI

```java
public void updateUI()
```

Replaces the current

ScrollPaneUI

object with a version
from the current default look and feel.
To be called when the default look and feel changes.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

,

UIManager.getUI(javax.swing.JComponent)

- getUIClassID

```java
@BeanProperty
(
bound
=false,

hidden
=true)
public
String
getUIClassID()
```

Returns the suffix used to construct the name of the L&F class used to
render this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ScrollPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setLayout

```java
public void setLayout​(
LayoutManager
layout)
```

Sets the layout manager for this

JScrollPane

.
This method overrides

setLayout

in

java.awt.Container

to ensure that only

LayoutManager

s which
are subclasses of

ScrollPaneLayout

can be used in a

JScrollPane

. If

layout

is non-null, this
will invoke

syncWithScrollPane

on it.

**Overrides:** setLayout

in class

Container
**Parameters:** layout

- the specified layout manager
**Throws:** ClassCastException

- if layout is not a

ScrollPaneLayout
**See Also:** Container.getLayout()

,

Container.setLayout(java.awt.LayoutManager)

- isValidateRoot

```java
@BeanProperty
(
hidden
=true)
public boolean isValidateRoot()
```

Overridden to return true so that any calls to

revalidate

on any descendants of this

JScrollPane

will cause the
entire tree beginning with this

JScrollPane

to be
validated.

**Overrides:** isValidateRoot

in class

JComponent
**Returns:** true
**See Also:** Container.validate()

,

JComponent.revalidate()

,

JComponent.isValidateRoot()

,

Container.isValidateRoot()

- getVerticalScrollBarPolicy

```java
public int getVerticalScrollBarPolicy()
```

Returns the vertical scroll bar policy value.

**Returns:** the

verticalScrollBarPolicy

property
**See Also:** setVerticalScrollBarPolicy(int)

- setVerticalScrollBarPolicy

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER","ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS"},

description
="The scrollpane vertical scrollbar policy")
public void setVerticalScrollBarPolicy​(int policy)
```

Determines when the vertical scrollbar appears in the scrollpane.
Legal values are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

**Parameters:** policy

- one of the three values listed above
**Throws:** IllegalArgumentException

- if

policy

is not one of the legal values shown above
**See Also:** getVerticalScrollBarPolicy()

- getHorizontalScrollBarPolicy

```java
public int getHorizontalScrollBarPolicy()
```

Returns the horizontal scroll bar policy value.

**Returns:** the

horizontalScrollBarPolicy

property
**See Also:** setHorizontalScrollBarPolicy(int)

- setHorizontalScrollBarPolicy

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS"},

description
="The scrollpane scrollbar policy")
public void setHorizontalScrollBarPolicy​(int policy)
```

Determines when the horizontal scrollbar appears in the scrollpane.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

**Parameters:** policy

- one of the three values listed above
**Throws:** IllegalArgumentException

- if

policy

is not one of the legal values shown above
**See Also:** getHorizontalScrollBarPolicy()

- getViewportBorder

```java
public
Border
getViewportBorder()
```

Returns the

Border

object that surrounds the viewport.

**Returns:** the

viewportBorder

property
**See Also:** setViewportBorder(javax.swing.border.Border)

- setViewportBorder

```java
@BeanProperty
(
preferred
=true,

description
="The border around the viewport.")
public void setViewportBorder​(
Border
viewportBorder)
```

Adds a border around the viewport. Note that the border isn't
set on the viewport directly,

JViewport

doesn't support
the

JComponent

border property.
Similarly setting the

JScrollPane

s
viewport doesn't affect the

viewportBorder

property.

The default value of this property is computed by the look
and feel implementation.

**Parameters:** viewportBorder

- the border to be added
**See Also:** getViewportBorder()

,

setViewport(javax.swing.JViewport)

- getViewportBorderBounds

```java
@BeanProperty
(
bound
=false)
public
Rectangle
getViewportBorderBounds()
```

Returns the bounds of the viewport's border.

**Returns:** a

Rectangle

object specifying the viewport border

- createHorizontalScrollBar

```java
public
JScrollBar
createHorizontalScrollBar()
```

Returns a

JScrollPane.ScrollBar

by default.
Subclasses may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to
create the horizontal scrollbar.

**Returns:** a

JScrollBar

with a horizontal orientation
**See Also:** JScrollBar

- getHorizontalScrollBar

```java
public
JScrollBar
getHorizontalScrollBar()
```

Returns the horizontal scroll bar that controls the viewport's
horizontal view position.

**Returns:** the

horizontalScrollBar

property
**See Also:** setHorizontalScrollBar(javax.swing.JScrollBar)

- setHorizontalScrollBar

```java
@BeanProperty
(
expert
=true,

description
="The horizontal scrollbar.")
public void setHorizontalScrollBar​(
JScrollBar
horizontalScrollBar)
```

Adds the scrollbar that controls the viewport's horizontal view
position to the scrollpane.
This is usually unnecessary, as

JScrollPane

creates
horizontal and vertical scrollbars by default.

**Parameters:** horizontalScrollBar

- the horizontal scrollbar to be added
**See Also:** createHorizontalScrollBar()

,

getHorizontalScrollBar()

- createVerticalScrollBar

```java
public
JScrollBar
createVerticalScrollBar()
```

Returns a

JScrollPane.ScrollBar

by default. Subclasses
may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to create the
vertical scrollbar.

**Returns:** a

JScrollBar

with a vertical orientation
**See Also:** JScrollBar

- getVerticalScrollBar

```java
public
JScrollBar
getVerticalScrollBar()
```

Returns the vertical scroll bar that controls the viewports
vertical view position.

**Returns:** the

verticalScrollBar

property
**See Also:** setVerticalScrollBar(javax.swing.JScrollBar)

- setVerticalScrollBar

```java
@BeanProperty
(
expert
=true,

description
="The vertical scrollbar.")
public void setVerticalScrollBar​(
JScrollBar
verticalScrollBar)
```

Adds the scrollbar that controls the viewports vertical view position
to the scrollpane. This is usually unnecessary,
as

JScrollPane

creates vertical and
horizontal scrollbars by default.

**Parameters:** verticalScrollBar

- the new vertical scrollbar to be added
**See Also:** createVerticalScrollBar()

,

getVerticalScrollBar()

- createViewport

```java
protected
JViewport
createViewport()
```

Returns a new

JViewport

by default.
Used to create the
viewport (as needed) in

setViewportView

,

setRowHeaderView

, and

setColumnHeaderView

.
Subclasses may override this method to return a subclass of

JViewport

.

**Returns:** a new

JViewport

- getViewport

```java
public
JViewport
getViewport()
```

Returns the current

JViewport

.

**Returns:** the

viewport

property
**See Also:** setViewport(javax.swing.JViewport)

- setViewport

```java
@BeanProperty
(
expert
=true,

visualUpdate
=true,

description
="The viewport child for this scrollpane")
public void setViewport​(
JViewport
viewport)
```

Removes the old viewport (if there is one); forces the
viewPosition of the new viewport to be in the +x,+y quadrant;
syncs up the row and column headers (if there are any) with the
new viewport; and finally syncs the scrollbars and
headers with the new viewport.

Most applications will find it more convenient to use

setViewportView

to add a viewport and a view to the scrollpane.

**Parameters:** viewport

- the new viewport to be used; if viewport is

null

, the old viewport is still removed
and the new viewport is set to

null
**See Also:** createViewport()

,

getViewport()

,

setViewportView(java.awt.Component)

- setViewportView

```java
public void setViewportView​(
Component
view)
```

Creates a viewport if necessary and then sets its view. Applications
that don't provide the view directly to the

JScrollPane

constructor
should use this method to specify the scrollable child that's going
to be displayed in the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
```

Applications should not add children directly to the scrollpane.

**Parameters:** view

- the component to add to the viewport
**See Also:** setViewport(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

- getRowHeader

```java
public
JViewport
getRowHeader()
```

Returns the row header.

**Returns:** the

rowHeader

property
**See Also:** setRowHeader(javax.swing.JViewport)

- setRowHeader

```java
@BeanProperty
(
expert
=true,

description
="The row header child for this scrollpane")
public void setRowHeader​(
JViewport
rowHeader)
```

Removes the old rowHeader, if it exists; if the new rowHeader
isn't

null

, syncs the y coordinate of its
viewPosition with
the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setRowHeaderView

to add a row header component and its viewport to the scroll pane.

**Parameters:** rowHeader

- the new row header to be used; if

null

the old row header is still removed and the new rowHeader
is set to

null
**See Also:** getRowHeader()

,

setRowHeaderView(java.awt.Component)

- setRowHeaderView

```java
public void setRowHeaderView​(
Component
view)
```

Creates a row-header viewport if necessary, sets
its view and then adds the row-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setRowHeaderView(myBigComponentsRowHeader);
```

**Parameters:** view

- the component to display as the row header
**See Also:** setRowHeader(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

- getColumnHeader

```java
public
JViewport
getColumnHeader()
```

Returns the column header.

**Returns:** the

columnHeader

property
**See Also:** setColumnHeader(javax.swing.JViewport)

- setColumnHeader

```java
@BeanProperty
(
visualUpdate
=true,

description
="The column header child for this scrollpane")
public void setColumnHeader​(
JViewport
columnHeader)
```

Removes the old columnHeader, if it exists; if the new columnHeader
isn't

null

, syncs the x coordinate of its viewPosition
with the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setColumnHeaderView

to add a column header component and its viewport to the scroll pane.

**Parameters:** columnHeader

- a

JViewport

which is the new column header
**See Also:** getColumnHeader()

,

setColumnHeaderView(java.awt.Component)

- setColumnHeaderView

```java
public void setColumnHeaderView​(
Component
view)
```

Creates a column-header viewport if necessary, sets
its view, and then adds the column-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setColumnHeaderView(myBigComponentsColumnHeader);
```

**Parameters:** view

- the component to display as the column header
**See Also:** setColumnHeader(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

- getCorner

```java
public
Component
getCorner​(
String
key)
```

Returns the component at the specified corner. The

key

value specifying the corner is one of:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

**Parameters:** key

- one of the values as shown above
**Returns:** the corner component (which may be

null

)
identified by the given key, or

null

if the key is invalid
**See Also:** setCorner(java.lang.String, java.awt.Component)

- setCorner

```java
public void setCorner​(
String
key,

Component
corner)
```

Adds a child that will appear in one of the scroll panes
corners, if there's room. For example with both scrollbars
showing (on the right and bottom edges of the scrollpane)
the lower left corner component will be shown in the space
between ends of the two scrollbars. Legal values for
the

key

are:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

Although "corner" doesn't match any beans property
signature,

PropertyChange

events are generated with the
property name set to the corner key.

**Parameters:** key

- identifies which corner the component will appear in
**Parameters:** corner

- one of the following components:

- lowerLeft

lowerRight

upperLeft

upperRight
**Throws:** IllegalArgumentException

- if corner key is invalid

- setComponentOrientation

```java
public void setComponentOrientation​(
ComponentOrientation
co)
```

Sets the orientation for the vertical and horizontal
scrollbars as determined by the

ComponentOrientation

argument.

**Overrides:** setComponentOrientation

in class

Component
**Parameters:** co

- one of the following values:

- java.awt.ComponentOrientation.LEFT_TO_RIGHT

java.awt.ComponentOrientation.RIGHT_TO_LEFT

java.awt.ComponentOrientation.UNKNOWN
**See Also:** ComponentOrientation

- isWheelScrollingEnabled

```java
@BeanProperty
(
description
="Flag for enabling/disabling mouse wheel scrolling")
public boolean isWheelScrollingEnabled()
```

Indicates whether or not scrolling will take place in response to the
mouse wheel. Wheel scrolling is enabled by default.

**Returns:** true if mouse wheel scrolling is enabled, false otherwise
**Since:** 1.4
**See Also:** setWheelScrollingEnabled(boolean)

- setWheelScrollingEnabled

```java
@BeanProperty
(
description
="Flag for enabling/disabling mouse wheel scrolling")
public void setWheelScrollingEnabled​(boolean handleWheel)
```

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

**Parameters:** handleWheel

-

true

if scrolling should be done
automatically for a MouseWheelEvent,

false

otherwise.
**Since:** 1.4
**See Also:** isWheelScrollingEnabled()

,

MouseWheelEvent

,

MouseWheelListener

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JScrollPane

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

JScrollPane

.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleJScrollPane.
A new AccessibleJScrollPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJScrollPane that serves as the
AccessibleContext of this JScrollPane

Field Detail

- verticalScrollBarPolicy

```java
protected int verticalScrollBarPolicy
```

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

**See Also:** setVerticalScrollBarPolicy(int)

- horizontalScrollBarPolicy

```java
protected int horizontalScrollBarPolicy
```

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

**See Also:** setHorizontalScrollBarPolicy(int)

- viewport

```java
protected
JViewport
viewport
```

The scrollpane's viewport child. Default is an empty

JViewport

.

**See Also:** setViewport(javax.swing.JViewport)

- verticalScrollBar

```java
protected
JScrollBar
verticalScrollBar
```

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

**See Also:** setVerticalScrollBar(javax.swing.JScrollBar)

- horizontalScrollBar

```java
protected
JScrollBar
horizontalScrollBar
```

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

**See Also:** setHorizontalScrollBar(javax.swing.JScrollBar)

- rowHeader

```java
protected
JViewport
rowHeader
```

The row header child. Default is

null

.

**See Also:** setRowHeader(javax.swing.JViewport)

- columnHeader

```java
protected
JViewport
columnHeader
```

The column header child. Default is

null

.

**See Also:** setColumnHeader(javax.swing.JViewport)

- lowerLeft

```java
protected
Component
lowerLeft
```

The component to display in the lower left corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

- lowerRight

```java
protected
Component
lowerRight
```

The component to display in the lower right corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

- upperLeft

```java
protected
Component
upperLeft
```

The component to display in the upper left corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

- upperRight

```java
protected
Component
upperRight
```

The component to display in the upper right corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

---

#### Field Detail

verticalScrollBarPolicy

```java
protected int verticalScrollBarPolicy
```

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

**See Also:** setVerticalScrollBarPolicy(int)

---

#### verticalScrollBarPolicy

protected int verticalScrollBarPolicy

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

horizontalScrollBarPolicy

```java
protected int horizontalScrollBarPolicy
```

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

**See Also:** setHorizontalScrollBarPolicy(int)

---

#### horizontalScrollBarPolicy

protected int horizontalScrollBarPolicy

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

viewport

```java
protected
JViewport
viewport
```

The scrollpane's viewport child. Default is an empty

JViewport

.

**See Also:** setViewport(javax.swing.JViewport)

---

#### viewport

protected

JViewport

viewport

The scrollpane's viewport child. Default is an empty

JViewport

.

verticalScrollBar

```java
protected
JScrollBar
verticalScrollBar
```

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

**See Also:** setVerticalScrollBar(javax.swing.JScrollBar)

---

#### verticalScrollBar

protected

JScrollBar

verticalScrollBar

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

horizontalScrollBar

```java
protected
JScrollBar
horizontalScrollBar
```

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

**See Also:** setHorizontalScrollBar(javax.swing.JScrollBar)

---

#### horizontalScrollBar

protected

JScrollBar

horizontalScrollBar

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

rowHeader

```java
protected
JViewport
rowHeader
```

The row header child. Default is

null

.

**See Also:** setRowHeader(javax.swing.JViewport)

---

#### rowHeader

protected

JViewport

rowHeader

The row header child. Default is

null

.

columnHeader

```java
protected
JViewport
columnHeader
```

The column header child. Default is

null

.

**See Also:** setColumnHeader(javax.swing.JViewport)

---

#### columnHeader

protected

JViewport

columnHeader

The column header child. Default is

null

.

lowerLeft

```java
protected
Component
lowerLeft
```

The component to display in the lower left corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

---

#### lowerLeft

protected

Component

lowerLeft

The component to display in the lower left corner.
Default is

null

.

lowerRight

```java
protected
Component
lowerRight
```

The component to display in the lower right corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

---

#### lowerRight

protected

Component

lowerRight

The component to display in the lower right corner.
Default is

null

.

upperLeft

```java
protected
Component
upperLeft
```

The component to display in the upper left corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

---

#### upperLeft

protected

Component

upperLeft

The component to display in the upper left corner.
Default is

null

.

upperRight

```java
protected
Component
upperRight
```

The component to display in the upper right corner.
Default is

null

.

**See Also:** setCorner(java.lang.String, java.awt.Component)

---

#### upperRight

protected

Component

upperRight

The component to display in the upper right corner.
Default is

null

.

Constructor Detail

- JScrollPane

```java
public JScrollPane​(
Component
view,
int vsbPolicy,
int hsbPolicy)
```

Creates a

JScrollPane

that displays the view
component in a viewport
whose view position can be controlled with a pair of scrollbars.
The scrollbar policies specify when the scrollbars are displayed,
For example, if

vsbPolicy

is

VERTICAL_SCROLLBAR_AS_NEEDED

then the vertical scrollbar only appears if the view doesn't fit
vertically. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

**Parameters:** view

- the component to display in the scrollpanes viewport
**Parameters:** vsbPolicy

- an integer that specifies the vertical
scrollbar policy
**Parameters:** hsbPolicy

- an integer that specifies the horizontal
scrollbar policy
**See Also:** setViewportView(java.awt.Component)

- JScrollPane

```java
public JScrollPane​(
Component
view)
```

Creates a

JScrollPane

that displays the
contents of the specified
component, where both horizontal and vertical scrollbars appear
whenever the component's contents are larger than the view.

**Parameters:** view

- the component to display in the scrollpane's viewport
**See Also:** setViewportView(java.awt.Component)

- JScrollPane

```java
public JScrollPane​(int vsbPolicy,
int hsbPolicy)
```

Creates an empty (no viewport view)

JScrollPane

with specified
scrollbar policies. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

**Parameters:** vsbPolicy

- an integer that specifies the vertical
scrollbar policy
**Parameters:** hsbPolicy

- an integer that specifies the horizontal
scrollbar policy
**See Also:** setViewportView(java.awt.Component)

- JScrollPane

```java
public JScrollPane()
```

Creates an empty (no viewport view)

JScrollPane

where both horizontal and vertical scrollbars appear when needed.

---

#### Constructor Detail

JScrollPane

```java
public JScrollPane​(
Component
view,
int vsbPolicy,
int hsbPolicy)
```

Creates a

JScrollPane

that displays the view
component in a viewport
whose view position can be controlled with a pair of scrollbars.
The scrollbar policies specify when the scrollbars are displayed,
For example, if

vsbPolicy

is

VERTICAL_SCROLLBAR_AS_NEEDED

then the vertical scrollbar only appears if the view doesn't fit
vertically. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

**Parameters:** view

- the component to display in the scrollpanes viewport
**Parameters:** vsbPolicy

- an integer that specifies the vertical
scrollbar policy
**Parameters:** hsbPolicy

- an integer that specifies the horizontal
scrollbar policy
**See Also:** setViewportView(java.awt.Component)

---

#### JScrollPane

public JScrollPane​(

Component

view,
int vsbPolicy,
int hsbPolicy)

Creates a

JScrollPane

that displays the view
component in a viewport
whose view position can be controlled with a pair of scrollbars.
The scrollbar policies specify when the scrollbars are displayed,
For example, if

vsbPolicy

is

VERTICAL_SCROLLBAR_AS_NEEDED

then the vertical scrollbar only appears if the view doesn't fit
vertically. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

JScrollPane

```java
public JScrollPane​(
Component
view)
```

Creates a

JScrollPane

that displays the
contents of the specified
component, where both horizontal and vertical scrollbars appear
whenever the component's contents are larger than the view.

**Parameters:** view

- the component to display in the scrollpane's viewport
**See Also:** setViewportView(java.awt.Component)

---

#### JScrollPane

public JScrollPane​(

Component

view)

Creates a

JScrollPane

that displays the
contents of the specified
component, where both horizontal and vertical scrollbars appear
whenever the component's contents are larger than the view.

JScrollPane

```java
public JScrollPane​(int vsbPolicy,
int hsbPolicy)
```

Creates an empty (no viewport view)

JScrollPane

with specified
scrollbar policies. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

**Parameters:** vsbPolicy

- an integer that specifies the vertical
scrollbar policy
**Parameters:** hsbPolicy

- an integer that specifies the horizontal
scrollbar policy
**See Also:** setViewportView(java.awt.Component)

---

#### JScrollPane

public JScrollPane​(int vsbPolicy,
int hsbPolicy)

Creates an empty (no viewport view)

JScrollPane

with specified
scrollbar policies. The available policy settings are listed at

setVerticalScrollBarPolicy(int)

and

setHorizontalScrollBarPolicy(int)

.

JScrollPane

```java
public JScrollPane()
```

Creates an empty (no viewport view)

JScrollPane

where both horizontal and vertical scrollbars appear when needed.

---

#### JScrollPane

public JScrollPane()

Creates an empty (no viewport view)

JScrollPane

where both horizontal and vertical scrollbars appear when needed.

Method Detail

- getUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public
ScrollPaneUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

ScrollPaneUI

object that renders this
component
**See Also:** setUI(javax.swing.plaf.ScrollPaneUI)

- setUI

```java
public void setUI​(
ScrollPaneUI
ui)
```

Sets the

ScrollPaneUI

object that provides the
look and feel (L&F) for this component.

**Parameters:** ui

- the

ScrollPaneUI

L&F object
**See Also:** getUI()

- updateUI

```java
public void updateUI()
```

Replaces the current

ScrollPaneUI

object with a version
from the current default look and feel.
To be called when the default look and feel changes.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

,

UIManager.getUI(javax.swing.JComponent)

- getUIClassID

```java
@BeanProperty
(
bound
=false,

hidden
=true)
public
String
getUIClassID()
```

Returns the suffix used to construct the name of the L&F class used to
render this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ScrollPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setLayout

```java
public void setLayout​(
LayoutManager
layout)
```

Sets the layout manager for this

JScrollPane

.
This method overrides

setLayout

in

java.awt.Container

to ensure that only

LayoutManager

s which
are subclasses of

ScrollPaneLayout

can be used in a

JScrollPane

. If

layout

is non-null, this
will invoke

syncWithScrollPane

on it.

**Overrides:** setLayout

in class

Container
**Parameters:** layout

- the specified layout manager
**Throws:** ClassCastException

- if layout is not a

ScrollPaneLayout
**See Also:** Container.getLayout()

,

Container.setLayout(java.awt.LayoutManager)

- isValidateRoot

```java
@BeanProperty
(
hidden
=true)
public boolean isValidateRoot()
```

Overridden to return true so that any calls to

revalidate

on any descendants of this

JScrollPane

will cause the
entire tree beginning with this

JScrollPane

to be
validated.

**Overrides:** isValidateRoot

in class

JComponent
**Returns:** true
**See Also:** Container.validate()

,

JComponent.revalidate()

,

JComponent.isValidateRoot()

,

Container.isValidateRoot()

- getVerticalScrollBarPolicy

```java
public int getVerticalScrollBarPolicy()
```

Returns the vertical scroll bar policy value.

**Returns:** the

verticalScrollBarPolicy

property
**See Also:** setVerticalScrollBarPolicy(int)

- setVerticalScrollBarPolicy

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER","ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS"},

description
="The scrollpane vertical scrollbar policy")
public void setVerticalScrollBarPolicy​(int policy)
```

Determines when the vertical scrollbar appears in the scrollpane.
Legal values are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

**Parameters:** policy

- one of the three values listed above
**Throws:** IllegalArgumentException

- if

policy

is not one of the legal values shown above
**See Also:** getVerticalScrollBarPolicy()

- getHorizontalScrollBarPolicy

```java
public int getHorizontalScrollBarPolicy()
```

Returns the horizontal scroll bar policy value.

**Returns:** the

horizontalScrollBarPolicy

property
**See Also:** setHorizontalScrollBarPolicy(int)

- setHorizontalScrollBarPolicy

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS"},

description
="The scrollpane scrollbar policy")
public void setHorizontalScrollBarPolicy​(int policy)
```

Determines when the horizontal scrollbar appears in the scrollpane.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

**Parameters:** policy

- one of the three values listed above
**Throws:** IllegalArgumentException

- if

policy

is not one of the legal values shown above
**See Also:** getHorizontalScrollBarPolicy()

- getViewportBorder

```java
public
Border
getViewportBorder()
```

Returns the

Border

object that surrounds the viewport.

**Returns:** the

viewportBorder

property
**See Also:** setViewportBorder(javax.swing.border.Border)

- setViewportBorder

```java
@BeanProperty
(
preferred
=true,

description
="The border around the viewport.")
public void setViewportBorder​(
Border
viewportBorder)
```

Adds a border around the viewport. Note that the border isn't
set on the viewport directly,

JViewport

doesn't support
the

JComponent

border property.
Similarly setting the

JScrollPane

s
viewport doesn't affect the

viewportBorder

property.

The default value of this property is computed by the look
and feel implementation.

**Parameters:** viewportBorder

- the border to be added
**See Also:** getViewportBorder()

,

setViewport(javax.swing.JViewport)

- getViewportBorderBounds

```java
@BeanProperty
(
bound
=false)
public
Rectangle
getViewportBorderBounds()
```

Returns the bounds of the viewport's border.

**Returns:** a

Rectangle

object specifying the viewport border

- createHorizontalScrollBar

```java
public
JScrollBar
createHorizontalScrollBar()
```

Returns a

JScrollPane.ScrollBar

by default.
Subclasses may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to
create the horizontal scrollbar.

**Returns:** a

JScrollBar

with a horizontal orientation
**See Also:** JScrollBar

- getHorizontalScrollBar

```java
public
JScrollBar
getHorizontalScrollBar()
```

Returns the horizontal scroll bar that controls the viewport's
horizontal view position.

**Returns:** the

horizontalScrollBar

property
**See Also:** setHorizontalScrollBar(javax.swing.JScrollBar)

- setHorizontalScrollBar

```java
@BeanProperty
(
expert
=true,

description
="The horizontal scrollbar.")
public void setHorizontalScrollBar​(
JScrollBar
horizontalScrollBar)
```

Adds the scrollbar that controls the viewport's horizontal view
position to the scrollpane.
This is usually unnecessary, as

JScrollPane

creates
horizontal and vertical scrollbars by default.

**Parameters:** horizontalScrollBar

- the horizontal scrollbar to be added
**See Also:** createHorizontalScrollBar()

,

getHorizontalScrollBar()

- createVerticalScrollBar

```java
public
JScrollBar
createVerticalScrollBar()
```

Returns a

JScrollPane.ScrollBar

by default. Subclasses
may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to create the
vertical scrollbar.

**Returns:** a

JScrollBar

with a vertical orientation
**See Also:** JScrollBar

- getVerticalScrollBar

```java
public
JScrollBar
getVerticalScrollBar()
```

Returns the vertical scroll bar that controls the viewports
vertical view position.

**Returns:** the

verticalScrollBar

property
**See Also:** setVerticalScrollBar(javax.swing.JScrollBar)

- setVerticalScrollBar

```java
@BeanProperty
(
expert
=true,

description
="The vertical scrollbar.")
public void setVerticalScrollBar​(
JScrollBar
verticalScrollBar)
```

Adds the scrollbar that controls the viewports vertical view position
to the scrollpane. This is usually unnecessary,
as

JScrollPane

creates vertical and
horizontal scrollbars by default.

**Parameters:** verticalScrollBar

- the new vertical scrollbar to be added
**See Also:** createVerticalScrollBar()

,

getVerticalScrollBar()

- createViewport

```java
protected
JViewport
createViewport()
```

Returns a new

JViewport

by default.
Used to create the
viewport (as needed) in

setViewportView

,

setRowHeaderView

, and

setColumnHeaderView

.
Subclasses may override this method to return a subclass of

JViewport

.

**Returns:** a new

JViewport

- getViewport

```java
public
JViewport
getViewport()
```

Returns the current

JViewport

.

**Returns:** the

viewport

property
**See Also:** setViewport(javax.swing.JViewport)

- setViewport

```java
@BeanProperty
(
expert
=true,

visualUpdate
=true,

description
="The viewport child for this scrollpane")
public void setViewport​(
JViewport
viewport)
```

Removes the old viewport (if there is one); forces the
viewPosition of the new viewport to be in the +x,+y quadrant;
syncs up the row and column headers (if there are any) with the
new viewport; and finally syncs the scrollbars and
headers with the new viewport.

Most applications will find it more convenient to use

setViewportView

to add a viewport and a view to the scrollpane.

**Parameters:** viewport

- the new viewport to be used; if viewport is

null

, the old viewport is still removed
and the new viewport is set to

null
**See Also:** createViewport()

,

getViewport()

,

setViewportView(java.awt.Component)

- setViewportView

```java
public void setViewportView​(
Component
view)
```

Creates a viewport if necessary and then sets its view. Applications
that don't provide the view directly to the

JScrollPane

constructor
should use this method to specify the scrollable child that's going
to be displayed in the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
```

Applications should not add children directly to the scrollpane.

**Parameters:** view

- the component to add to the viewport
**See Also:** setViewport(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

- getRowHeader

```java
public
JViewport
getRowHeader()
```

Returns the row header.

**Returns:** the

rowHeader

property
**See Also:** setRowHeader(javax.swing.JViewport)

- setRowHeader

```java
@BeanProperty
(
expert
=true,

description
="The row header child for this scrollpane")
public void setRowHeader​(
JViewport
rowHeader)
```

Removes the old rowHeader, if it exists; if the new rowHeader
isn't

null

, syncs the y coordinate of its
viewPosition with
the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setRowHeaderView

to add a row header component and its viewport to the scroll pane.

**Parameters:** rowHeader

- the new row header to be used; if

null

the old row header is still removed and the new rowHeader
is set to

null
**See Also:** getRowHeader()

,

setRowHeaderView(java.awt.Component)

- setRowHeaderView

```java
public void setRowHeaderView​(
Component
view)
```

Creates a row-header viewport if necessary, sets
its view and then adds the row-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setRowHeaderView(myBigComponentsRowHeader);
```

**Parameters:** view

- the component to display as the row header
**See Also:** setRowHeader(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

- getColumnHeader

```java
public
JViewport
getColumnHeader()
```

Returns the column header.

**Returns:** the

columnHeader

property
**See Also:** setColumnHeader(javax.swing.JViewport)

- setColumnHeader

```java
@BeanProperty
(
visualUpdate
=true,

description
="The column header child for this scrollpane")
public void setColumnHeader​(
JViewport
columnHeader)
```

Removes the old columnHeader, if it exists; if the new columnHeader
isn't

null

, syncs the x coordinate of its viewPosition
with the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setColumnHeaderView

to add a column header component and its viewport to the scroll pane.

**Parameters:** columnHeader

- a

JViewport

which is the new column header
**See Also:** getColumnHeader()

,

setColumnHeaderView(java.awt.Component)

- setColumnHeaderView

```java
public void setColumnHeaderView​(
Component
view)
```

Creates a column-header viewport if necessary, sets
its view, and then adds the column-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setColumnHeaderView(myBigComponentsColumnHeader);
```

**Parameters:** view

- the component to display as the column header
**See Also:** setColumnHeader(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

- getCorner

```java
public
Component
getCorner​(
String
key)
```

Returns the component at the specified corner. The

key

value specifying the corner is one of:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

**Parameters:** key

- one of the values as shown above
**Returns:** the corner component (which may be

null

)
identified by the given key, or

null

if the key is invalid
**See Also:** setCorner(java.lang.String, java.awt.Component)

- setCorner

```java
public void setCorner​(
String
key,

Component
corner)
```

Adds a child that will appear in one of the scroll panes
corners, if there's room. For example with both scrollbars
showing (on the right and bottom edges of the scrollpane)
the lower left corner component will be shown in the space
between ends of the two scrollbars. Legal values for
the

key

are:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

Although "corner" doesn't match any beans property
signature,

PropertyChange

events are generated with the
property name set to the corner key.

**Parameters:** key

- identifies which corner the component will appear in
**Parameters:** corner

- one of the following components:

- lowerLeft

lowerRight

upperLeft

upperRight
**Throws:** IllegalArgumentException

- if corner key is invalid

- setComponentOrientation

```java
public void setComponentOrientation​(
ComponentOrientation
co)
```

Sets the orientation for the vertical and horizontal
scrollbars as determined by the

ComponentOrientation

argument.

**Overrides:** setComponentOrientation

in class

Component
**Parameters:** co

- one of the following values:

- java.awt.ComponentOrientation.LEFT_TO_RIGHT

java.awt.ComponentOrientation.RIGHT_TO_LEFT

java.awt.ComponentOrientation.UNKNOWN
**See Also:** ComponentOrientation

- isWheelScrollingEnabled

```java
@BeanProperty
(
description
="Flag for enabling/disabling mouse wheel scrolling")
public boolean isWheelScrollingEnabled()
```

Indicates whether or not scrolling will take place in response to the
mouse wheel. Wheel scrolling is enabled by default.

**Returns:** true if mouse wheel scrolling is enabled, false otherwise
**Since:** 1.4
**See Also:** setWheelScrollingEnabled(boolean)

- setWheelScrollingEnabled

```java
@BeanProperty
(
description
="Flag for enabling/disabling mouse wheel scrolling")
public void setWheelScrollingEnabled​(boolean handleWheel)
```

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

**Parameters:** handleWheel

-

true

if scrolling should be done
automatically for a MouseWheelEvent,

false

otherwise.
**Since:** 1.4
**See Also:** isWheelScrollingEnabled()

,

MouseWheelEvent

,

MouseWheelListener

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JScrollPane

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

JScrollPane

.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleJScrollPane.
A new AccessibleJScrollPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJScrollPane that serves as the
AccessibleContext of this JScrollPane

---

#### Method Detail

getUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public
ScrollPaneUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

ScrollPaneUI

object that renders this
component
**See Also:** setUI(javax.swing.plaf.ScrollPaneUI)

---

#### getUI

@BeanProperty

(

hidden

=true,

visualUpdate

=true,

description

="The UI object that implements the Component\'s LookAndFeel.")
public

ScrollPaneUI

getUI()

Returns the look and feel (L&F) object that renders this component.

setUI

```java
public void setUI​(
ScrollPaneUI
ui)
```

Sets the

ScrollPaneUI

object that provides the
look and feel (L&F) for this component.

**Parameters:** ui

- the

ScrollPaneUI

L&F object
**See Also:** getUI()

---

#### setUI

public void setUI​(

ScrollPaneUI

ui)

Sets the

ScrollPaneUI

object that provides the
look and feel (L&F) for this component.

updateUI

```java
public void updateUI()
```

Replaces the current

ScrollPaneUI

object with a version
from the current default look and feel.
To be called when the default look and feel changes.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

,

UIManager.getUI(javax.swing.JComponent)

---

#### updateUI

public void updateUI()

Replaces the current

ScrollPaneUI

object with a version
from the current default look and feel.
To be called when the default look and feel changes.

getUIClassID

```java
@BeanProperty
(
bound
=false,

hidden
=true)
public
String
getUIClassID()
```

Returns the suffix used to construct the name of the L&F class used to
render this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ScrollPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false,

hidden

=true)
public

String

getUIClassID()

Returns the suffix used to construct the name of the L&F class used to
render this component.

setLayout

```java
public void setLayout​(
LayoutManager
layout)
```

Sets the layout manager for this

JScrollPane

.
This method overrides

setLayout

in

java.awt.Container

to ensure that only

LayoutManager

s which
are subclasses of

ScrollPaneLayout

can be used in a

JScrollPane

. If

layout

is non-null, this
will invoke

syncWithScrollPane

on it.

**Overrides:** setLayout

in class

Container
**Parameters:** layout

- the specified layout manager
**Throws:** ClassCastException

- if layout is not a

ScrollPaneLayout
**See Also:** Container.getLayout()

,

Container.setLayout(java.awt.LayoutManager)

---

#### setLayout

public void setLayout​(

LayoutManager

layout)

Sets the layout manager for this

JScrollPane

.
This method overrides

setLayout

in

java.awt.Container

to ensure that only

LayoutManager

s which
are subclasses of

ScrollPaneLayout

can be used in a

JScrollPane

. If

layout

is non-null, this
will invoke

syncWithScrollPane

on it.

isValidateRoot

```java
@BeanProperty
(
hidden
=true)
public boolean isValidateRoot()
```

Overridden to return true so that any calls to

revalidate

on any descendants of this

JScrollPane

will cause the
entire tree beginning with this

JScrollPane

to be
validated.

**Overrides:** isValidateRoot

in class

JComponent
**Returns:** true
**See Also:** Container.validate()

,

JComponent.revalidate()

,

JComponent.isValidateRoot()

,

Container.isValidateRoot()

---

#### isValidateRoot

@BeanProperty

(

hidden

=true)
public boolean isValidateRoot()

Overridden to return true so that any calls to

revalidate

on any descendants of this

JScrollPane

will cause the
entire tree beginning with this

JScrollPane

to be
validated.

getVerticalScrollBarPolicy

```java
public int getVerticalScrollBarPolicy()
```

Returns the vertical scroll bar policy value.

**Returns:** the

verticalScrollBarPolicy

property
**See Also:** setVerticalScrollBarPolicy(int)

---

#### getVerticalScrollBarPolicy

public int getVerticalScrollBarPolicy()

Returns the vertical scroll bar policy value.

setVerticalScrollBarPolicy

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER","ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS"},

description
="The scrollpane vertical scrollbar policy")
public void setVerticalScrollBarPolicy​(int policy)
```

Determines when the vertical scrollbar appears in the scrollpane.
Legal values are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

**Parameters:** policy

- one of the three values listed above
**Throws:** IllegalArgumentException

- if

policy

is not one of the legal values shown above
**See Also:** getVerticalScrollBarPolicy()

---

#### setVerticalScrollBarPolicy

@BeanProperty

(

preferred

=true,

enumerationValues

={"ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER","ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS"},

description

="The scrollpane vertical scrollbar policy")
public void setVerticalScrollBarPolicy​(int policy)

Determines when the vertical scrollbar appears in the scrollpane.
Legal values are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

getHorizontalScrollBarPolicy

```java
public int getHorizontalScrollBarPolicy()
```

Returns the horizontal scroll bar policy value.

**Returns:** the

horizontalScrollBarPolicy

property
**See Also:** setHorizontalScrollBarPolicy(int)

---

#### getHorizontalScrollBarPolicy

public int getHorizontalScrollBarPolicy()

Returns the horizontal scroll bar policy value.

setHorizontalScrollBarPolicy

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS"},

description
="The scrollpane scrollbar policy")
public void setHorizontalScrollBarPolicy​(int policy)
```

Determines when the horizontal scrollbar appears in the scrollpane.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

**Parameters:** policy

- one of the three values listed above
**Throws:** IllegalArgumentException

- if

policy

is not one of the legal values shown above
**See Also:** getHorizontalScrollBarPolicy()

---

#### setHorizontalScrollBarPolicy

@BeanProperty

(

preferred

=true,

enumerationValues

={"ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS"},

description

="The scrollpane scrollbar policy")
public void setHorizontalScrollBarPolicy​(int policy)

Determines when the horizontal scrollbar appears in the scrollpane.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

getViewportBorder

```java
public
Border
getViewportBorder()
```

Returns the

Border

object that surrounds the viewport.

**Returns:** the

viewportBorder

property
**See Also:** setViewportBorder(javax.swing.border.Border)

---

#### getViewportBorder

public

Border

getViewportBorder()

Returns the

Border

object that surrounds the viewport.

setViewportBorder

```java
@BeanProperty
(
preferred
=true,

description
="The border around the viewport.")
public void setViewportBorder​(
Border
viewportBorder)
```

Adds a border around the viewport. Note that the border isn't
set on the viewport directly,

JViewport

doesn't support
the

JComponent

border property.
Similarly setting the

JScrollPane

s
viewport doesn't affect the

viewportBorder

property.

The default value of this property is computed by the look
and feel implementation.

**Parameters:** viewportBorder

- the border to be added
**See Also:** getViewportBorder()

,

setViewport(javax.swing.JViewport)

---

#### setViewportBorder

@BeanProperty

(

preferred

=true,

description

="The border around the viewport.")
public void setViewportBorder​(

Border

viewportBorder)

Adds a border around the viewport. Note that the border isn't
set on the viewport directly,

JViewport

doesn't support
the

JComponent

border property.
Similarly setting the

JScrollPane

s
viewport doesn't affect the

viewportBorder

property.

The default value of this property is computed by the look
and feel implementation.

The default value of this property is computed by the look
and feel implementation.

getViewportBorderBounds

```java
@BeanProperty
(
bound
=false)
public
Rectangle
getViewportBorderBounds()
```

Returns the bounds of the viewport's border.

**Returns:** a

Rectangle

object specifying the viewport border

---

#### getViewportBorderBounds

@BeanProperty

(

bound

=false)
public

Rectangle

getViewportBorderBounds()

Returns the bounds of the viewport's border.

createHorizontalScrollBar

```java
public
JScrollBar
createHorizontalScrollBar()
```

Returns a

JScrollPane.ScrollBar

by default.
Subclasses may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to
create the horizontal scrollbar.

**Returns:** a

JScrollBar

with a horizontal orientation
**See Also:** JScrollBar

---

#### createHorizontalScrollBar

public

JScrollBar

createHorizontalScrollBar()

Returns a

JScrollPane.ScrollBar

by default.
Subclasses may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to
create the horizontal scrollbar.

getHorizontalScrollBar

```java
public
JScrollBar
getHorizontalScrollBar()
```

Returns the horizontal scroll bar that controls the viewport's
horizontal view position.

**Returns:** the

horizontalScrollBar

property
**See Also:** setHorizontalScrollBar(javax.swing.JScrollBar)

---

#### getHorizontalScrollBar

public

JScrollBar

getHorizontalScrollBar()

Returns the horizontal scroll bar that controls the viewport's
horizontal view position.

setHorizontalScrollBar

```java
@BeanProperty
(
expert
=true,

description
="The horizontal scrollbar.")
public void setHorizontalScrollBar​(
JScrollBar
horizontalScrollBar)
```

Adds the scrollbar that controls the viewport's horizontal view
position to the scrollpane.
This is usually unnecessary, as

JScrollPane

creates
horizontal and vertical scrollbars by default.

**Parameters:** horizontalScrollBar

- the horizontal scrollbar to be added
**See Also:** createHorizontalScrollBar()

,

getHorizontalScrollBar()

---

#### setHorizontalScrollBar

@BeanProperty

(

expert

=true,

description

="The horizontal scrollbar.")
public void setHorizontalScrollBar​(

JScrollBar

horizontalScrollBar)

Adds the scrollbar that controls the viewport's horizontal view
position to the scrollpane.
This is usually unnecessary, as

JScrollPane

creates
horizontal and vertical scrollbars by default.

createVerticalScrollBar

```java
public
JScrollBar
createVerticalScrollBar()
```

Returns a

JScrollPane.ScrollBar

by default. Subclasses
may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to create the
vertical scrollbar.

**Returns:** a

JScrollBar

with a vertical orientation
**See Also:** JScrollBar

---

#### createVerticalScrollBar

public

JScrollBar

createVerticalScrollBar()

Returns a

JScrollPane.ScrollBar

by default. Subclasses
may override this method to force

ScrollPaneUI

implementations to use a

JScrollBar

subclass.
Used by

ScrollPaneUI

implementations to create the
vertical scrollbar.

getVerticalScrollBar

```java
public
JScrollBar
getVerticalScrollBar()
```

Returns the vertical scroll bar that controls the viewports
vertical view position.

**Returns:** the

verticalScrollBar

property
**See Also:** setVerticalScrollBar(javax.swing.JScrollBar)

---

#### getVerticalScrollBar

public

JScrollBar

getVerticalScrollBar()

Returns the vertical scroll bar that controls the viewports
vertical view position.

setVerticalScrollBar

```java
@BeanProperty
(
expert
=true,

description
="The vertical scrollbar.")
public void setVerticalScrollBar​(
JScrollBar
verticalScrollBar)
```

Adds the scrollbar that controls the viewports vertical view position
to the scrollpane. This is usually unnecessary,
as

JScrollPane

creates vertical and
horizontal scrollbars by default.

**Parameters:** verticalScrollBar

- the new vertical scrollbar to be added
**See Also:** createVerticalScrollBar()

,

getVerticalScrollBar()

---

#### setVerticalScrollBar

@BeanProperty

(

expert

=true,

description

="The vertical scrollbar.")
public void setVerticalScrollBar​(

JScrollBar

verticalScrollBar)

Adds the scrollbar that controls the viewports vertical view position
to the scrollpane. This is usually unnecessary,
as

JScrollPane

creates vertical and
horizontal scrollbars by default.

createViewport

```java
protected
JViewport
createViewport()
```

Returns a new

JViewport

by default.
Used to create the
viewport (as needed) in

setViewportView

,

setRowHeaderView

, and

setColumnHeaderView

.
Subclasses may override this method to return a subclass of

JViewport

.

**Returns:** a new

JViewport

---

#### createViewport

protected

JViewport

createViewport()

Returns a new

JViewport

by default.
Used to create the
viewport (as needed) in

setViewportView

,

setRowHeaderView

, and

setColumnHeaderView

.
Subclasses may override this method to return a subclass of

JViewport

.

getViewport

```java
public
JViewport
getViewport()
```

Returns the current

JViewport

.

**Returns:** the

viewport

property
**See Also:** setViewport(javax.swing.JViewport)

---

#### getViewport

public

JViewport

getViewport()

Returns the current

JViewport

.

setViewport

```java
@BeanProperty
(
expert
=true,

visualUpdate
=true,

description
="The viewport child for this scrollpane")
public void setViewport​(
JViewport
viewport)
```

Removes the old viewport (if there is one); forces the
viewPosition of the new viewport to be in the +x,+y quadrant;
syncs up the row and column headers (if there are any) with the
new viewport; and finally syncs the scrollbars and
headers with the new viewport.

Most applications will find it more convenient to use

setViewportView

to add a viewport and a view to the scrollpane.

**Parameters:** viewport

- the new viewport to be used; if viewport is

null

, the old viewport is still removed
and the new viewport is set to

null
**See Also:** createViewport()

,

getViewport()

,

setViewportView(java.awt.Component)

---

#### setViewport

@BeanProperty

(

expert

=true,

visualUpdate

=true,

description

="The viewport child for this scrollpane")
public void setViewport​(

JViewport

viewport)

Removes the old viewport (if there is one); forces the
viewPosition of the new viewport to be in the +x,+y quadrant;
syncs up the row and column headers (if there are any) with the
new viewport; and finally syncs the scrollbars and
headers with the new viewport.

Most applications will find it more convenient to use

setViewportView

to add a viewport and a view to the scrollpane.

Most applications will find it more convenient to use

setViewportView

to add a viewport and a view to the scrollpane.

setViewportView

```java
public void setViewportView​(
Component
view)
```

Creates a viewport if necessary and then sets its view. Applications
that don't provide the view directly to the

JScrollPane

constructor
should use this method to specify the scrollable child that's going
to be displayed in the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
```

Applications should not add children directly to the scrollpane.

**Parameters:** view

- the component to add to the viewport
**See Also:** setViewport(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

---

#### setViewportView

public void setViewportView​(

Component

view)

Creates a viewport if necessary and then sets its view. Applications
that don't provide the view directly to the

JScrollPane

constructor
should use this method to specify the scrollable child that's going
to be displayed in the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
```

Applications should not add children directly to the scrollpane.

JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);

getRowHeader

```java
public
JViewport
getRowHeader()
```

Returns the row header.

**Returns:** the

rowHeader

property
**See Also:** setRowHeader(javax.swing.JViewport)

---

#### getRowHeader

public

JViewport

getRowHeader()

Returns the row header.

setRowHeader

```java
@BeanProperty
(
expert
=true,

description
="The row header child for this scrollpane")
public void setRowHeader​(
JViewport
rowHeader)
```

Removes the old rowHeader, if it exists; if the new rowHeader
isn't

null

, syncs the y coordinate of its
viewPosition with
the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setRowHeaderView

to add a row header component and its viewport to the scroll pane.

**Parameters:** rowHeader

- the new row header to be used; if

null

the old row header is still removed and the new rowHeader
is set to

null
**See Also:** getRowHeader()

,

setRowHeaderView(java.awt.Component)

---

#### setRowHeader

@BeanProperty

(

expert

=true,

description

="The row header child for this scrollpane")
public void setRowHeader​(

JViewport

rowHeader)

Removes the old rowHeader, if it exists; if the new rowHeader
isn't

null

, syncs the y coordinate of its
viewPosition with
the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setRowHeaderView

to add a row header component and its viewport to the scroll pane.

Most applications will find it more convenient to use

setRowHeaderView

to add a row header component and its viewport to the scroll pane.

setRowHeaderView

```java
public void setRowHeaderView​(
Component
view)
```

Creates a row-header viewport if necessary, sets
its view and then adds the row-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setRowHeaderView(myBigComponentsRowHeader);
```

**Parameters:** view

- the component to display as the row header
**See Also:** setRowHeader(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

---

#### setRowHeaderView

public void setRowHeaderView​(

Component

view)

Creates a row-header viewport if necessary, sets
its view and then adds the row-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setRowHeaderView(myBigComponentsRowHeader);
```

JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setRowHeaderView(myBigComponentsRowHeader);

getColumnHeader

```java
public
JViewport
getColumnHeader()
```

Returns the column header.

**Returns:** the

columnHeader

property
**See Also:** setColumnHeader(javax.swing.JViewport)

---

#### getColumnHeader

public

JViewport

getColumnHeader()

Returns the column header.

setColumnHeader

```java
@BeanProperty
(
visualUpdate
=true,

description
="The column header child for this scrollpane")
public void setColumnHeader​(
JViewport
columnHeader)
```

Removes the old columnHeader, if it exists; if the new columnHeader
isn't

null

, syncs the x coordinate of its viewPosition
with the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setColumnHeaderView

to add a column header component and its viewport to the scroll pane.

**Parameters:** columnHeader

- a

JViewport

which is the new column header
**See Also:** getColumnHeader()

,

setColumnHeaderView(java.awt.Component)

---

#### setColumnHeader

@BeanProperty

(

visualUpdate

=true,

description

="The column header child for this scrollpane")
public void setColumnHeader​(

JViewport

columnHeader)

Removes the old columnHeader, if it exists; if the new columnHeader
isn't

null

, syncs the x coordinate of its viewPosition
with the viewport (if there is one) and then adds it to the scroll pane.

Most applications will find it more convenient to use

setColumnHeaderView

to add a column header component and its viewport to the scroll pane.

Most applications will find it more convenient to use

setColumnHeaderView

to add a column header component and its viewport to the scroll pane.

setColumnHeaderView

```java
public void setColumnHeaderView​(
Component
view)
```

Creates a column-header viewport if necessary, sets
its view, and then adds the column-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setColumnHeaderView(myBigComponentsColumnHeader);
```

**Parameters:** view

- the component to display as the column header
**See Also:** setColumnHeader(javax.swing.JViewport)

,

JViewport.setView(java.awt.Component)

---

#### setColumnHeaderView

public void setColumnHeaderView​(

Component

view)

Creates a column-header viewport if necessary, sets
its view, and then adds the column-header viewport
to the scrollpane. For example:

```java
JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setColumnHeaderView(myBigComponentsColumnHeader);
```

JScrollPane scrollpane = new JScrollPane();
scrollpane.setViewportView(myBigComponentToScroll);
scrollpane.setColumnHeaderView(myBigComponentsColumnHeader);

getCorner

```java
public
Component
getCorner​(
String
key)
```

Returns the component at the specified corner. The

key

value specifying the corner is one of:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

**Parameters:** key

- one of the values as shown above
**Returns:** the corner component (which may be

null

)
identified by the given key, or

null

if the key is invalid
**See Also:** setCorner(java.lang.String, java.awt.Component)

---

#### getCorner

public

Component

getCorner​(

String

key)

Returns the component at the specified corner. The

key

value specifying the corner is one of:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

setCorner

```java
public void setCorner​(
String
key,

Component
corner)
```

Adds a child that will appear in one of the scroll panes
corners, if there's room. For example with both scrollbars
showing (on the right and bottom edges of the scrollpane)
the lower left corner component will be shown in the space
between ends of the two scrollbars. Legal values for
the

key

are:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

Although "corner" doesn't match any beans property
signature,

PropertyChange

events are generated with the
property name set to the corner key.

**Parameters:** key

- identifies which corner the component will appear in
**Parameters:** corner

- one of the following components:

- lowerLeft

lowerRight

upperLeft

upperRight
**Throws:** IllegalArgumentException

- if corner key is invalid

---

#### setCorner

public void setCorner​(

String

key,

Component

corner)

Adds a child that will appear in one of the scroll panes
corners, if there's room. For example with both scrollbars
showing (on the right and bottom edges of the scrollpane)
the lower left corner component will be shown in the space
between ends of the two scrollbars. Legal values for
the

key

are:

- ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

Although "corner" doesn't match any beans property
signature,

PropertyChange

events are generated with the
property name set to the corner key.

ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.LOWER_LEADING_CORNER

ScrollPaneConstants.LOWER_TRAILING_CORNER

ScrollPaneConstants.UPPER_LEADING_CORNER

ScrollPaneConstants.UPPER_TRAILING_CORNER

Although "corner" doesn't match any beans property
signature,

PropertyChange

events are generated with the
property name set to the corner key.

lowerLeft

lowerRight

upperLeft

upperRight

setComponentOrientation

```java
public void setComponentOrientation​(
ComponentOrientation
co)
```

Sets the orientation for the vertical and horizontal
scrollbars as determined by the

ComponentOrientation

argument.

**Overrides:** setComponentOrientation

in class

Component
**Parameters:** co

- one of the following values:

- java.awt.ComponentOrientation.LEFT_TO_RIGHT

java.awt.ComponentOrientation.RIGHT_TO_LEFT

java.awt.ComponentOrientation.UNKNOWN
**See Also:** ComponentOrientation

---

#### setComponentOrientation

public void setComponentOrientation​(

ComponentOrientation

co)

Sets the orientation for the vertical and horizontal
scrollbars as determined by the

ComponentOrientation

argument.

java.awt.ComponentOrientation.LEFT_TO_RIGHT

java.awt.ComponentOrientation.RIGHT_TO_LEFT

java.awt.ComponentOrientation.UNKNOWN

isWheelScrollingEnabled

```java
@BeanProperty
(
description
="Flag for enabling/disabling mouse wheel scrolling")
public boolean isWheelScrollingEnabled()
```

Indicates whether or not scrolling will take place in response to the
mouse wheel. Wheel scrolling is enabled by default.

**Returns:** true if mouse wheel scrolling is enabled, false otherwise
**Since:** 1.4
**See Also:** setWheelScrollingEnabled(boolean)

---

#### isWheelScrollingEnabled

@BeanProperty

(

description

="Flag for enabling/disabling mouse wheel scrolling")
public boolean isWheelScrollingEnabled()

Indicates whether or not scrolling will take place in response to the
mouse wheel. Wheel scrolling is enabled by default.

setWheelScrollingEnabled

```java
@BeanProperty
(
description
="Flag for enabling/disabling mouse wheel scrolling")
public void setWheelScrollingEnabled​(boolean handleWheel)
```

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

**Parameters:** handleWheel

-

true

if scrolling should be done
automatically for a MouseWheelEvent,

false

otherwise.
**Since:** 1.4
**See Also:** isWheelScrollingEnabled()

,

MouseWheelEvent

,

MouseWheelListener

---

#### setWheelScrollingEnabled

@BeanProperty

(

description

="Flag for enabling/disabling mouse wheel scrolling")
public void setWheelScrollingEnabled​(boolean handleWheel)

Enables/disables scrolling in response to movement of the mouse wheel.
Wheel scrolling is enabled by default.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JScrollPane

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

JScrollPane

.

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JScrollPane

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
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleJScrollPane.
A new AccessibleJScrollPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJScrollPane that serves as the
AccessibleContext of this JScrollPane

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JScrollPane.
For scroll panes, the AccessibleContext takes the form of an
AccessibleJScrollPane.
A new AccessibleJScrollPane instance is created if necessary.

---

