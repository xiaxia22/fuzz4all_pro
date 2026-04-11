# Class ScrollPaneLayout

**Source:** `java.desktop\javax\swing\ScrollPaneLayout.html`

### Class Description

```java
public class
ScrollPaneLayout

extends
Object

implements
LayoutManager
,
ScrollPaneConstants
,
Serializable
```

The layout manager used by

JScrollPane

.

JScrollPaneLayout

is
responsible for nine components: a viewport, two scrollbars,
a row header, a column header, and four "corner" components.

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

Serializable

,

ScrollPaneConstants

---

### Field Details

#### protected
JViewport
viewport

The scrollpane's viewport child.
Default is an empty

JViewport

.

**See Also:**
- JScrollPane.setViewport(javax.swing.JViewport)

---

#### protected
JScrollBar
vsb

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

**See Also:**
- JScrollPane.setVerticalScrollBar(javax.swing.JScrollBar)

---

#### protected
JScrollBar
hsb

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

**See Also:**
- JScrollPane.setHorizontalScrollBar(javax.swing.JScrollBar)

---

#### protected
JViewport
rowHead

The row header child. Default is

null

.

**See Also:**
- JScrollPane.setRowHeader(javax.swing.JViewport)

---

#### protected
JViewport
colHead

The column header child. Default is

null

.

**See Also:**
- JScrollPane.setColumnHeader(javax.swing.JViewport)

---

#### protected
Component
lowerLeft

The component to display in the lower left corner.
Default is

null

.

**See Also:**
- JScrollPane.setCorner(java.lang.String, java.awt.Component)

---

#### protected
Component
lowerRight

The component to display in the lower right corner.
Default is

null

.

**See Also:**
- JScrollPane.setCorner(java.lang.String, java.awt.Component)

---

#### protected
Component
upperLeft

The component to display in the upper left corner.
Default is

null

.

**See Also:**
- JScrollPane.setCorner(java.lang.String, java.awt.Component)

---

#### protected
Component
upperRight

The component to display in the upper right corner.
Default is

null

.

**See Also:**
- JScrollPane.setCorner(java.lang.String, java.awt.Component)

---

#### protected int vsbPolicy

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

**See Also:**
- JScrollPane.setVerticalScrollBarPolicy(int)

---

#### protected int hsbPolicy

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

**See Also:**
- JScrollPane.setHorizontalScrollBarPolicy(int)

---

### Constructor Details

#### public ScrollPaneLayout()

*No description found.*

---

### Method Details

#### public void syncWithScrollPane​(
JScrollPane
sp)

This method is invoked after the ScrollPaneLayout is set as the
LayoutManager of a

JScrollPane

.
It initializes all of the internal fields that
are ordinarily set by

addLayoutComponent

. For example:

```java
ScrollPaneLayout mySPLayout = new ScrollPanelLayout() {
public void layoutContainer(Container p) {
super.layoutContainer(p);
// do some extra work here ...
}
};
scrollpane.setLayout(mySPLayout):
```

**Parameters:**
- sp

- an instance of the

JScrollPane

---

#### protected
Component
addSingletonComponent​(
Component
oldC,

Component
newC)

Removes an existing component. When a new component, such as
the left corner, or vertical scrollbar, is added, the old one,
if it exists, must be removed.

This method returns

newC

. If

oldC

is
not equal to

newC

and is non-

null

,
it will be removed from its parent.

**Parameters:**
- oldC

- the

Component

to replace
- newC

- the

Component

to add

**Returns:**
- the

newC

---

#### public void addLayoutComponent​(
String
s,

Component
c)

Adds the specified component to the layout. The layout is
identified using one of:

- ScrollPaneConstants.VIEWPORT

ScrollPaneConstants.VERTICAL_SCROLLBAR

ScrollPaneConstants.HORIZONTAL_SCROLLBAR

ScrollPaneConstants.ROW_HEADER

ScrollPaneConstants.COLUMN_HEADER

ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

**Specified by:**
- addLayoutComponent

in interface

LayoutManager

**Parameters:**
- s

- the component identifier
- c

- the component to be added

**Throws:**
- IllegalArgumentException

- if

s

is an invalid key

---

#### public void removeLayoutComponent​(
Component
c)

Removes the specified component from the layout.

**Specified by:**
- removeLayoutComponent

in interface

LayoutManager

**Parameters:**
- c

- the component to remove

---

#### public int getVerticalScrollBarPolicy()

Returns the vertical scrollbar-display policy.

**Returns:**
- an integer giving the display policy

**See Also:**
- setVerticalScrollBarPolicy(int)

---

#### public void setVerticalScrollBarPolicy​(int x)

Sets the vertical scrollbar-display policy. The options
are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

**Parameters:**
- x

- an integer giving the display policy

**Throws:**
- IllegalArgumentException

- if

x

is an invalid
vertical scroll bar policy, as listed above

---

#### public int getHorizontalScrollBarPolicy()

Returns the horizontal scrollbar-display policy.

**Returns:**
- an integer giving the display policy

**See Also:**
- setHorizontalScrollBarPolicy(int)

---

#### public void setHorizontalScrollBarPolicy​(int x)

Sets the horizontal scrollbar-display policy.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

**Parameters:**
- x

- an int giving the display policy

**Throws:**
- IllegalArgumentException

- if

x

is not a valid
horizontal scrollbar policy, as listed above

---

#### public
JViewport
getViewport()

Returns the

JViewport

object that displays the
scrollable contents.

**Returns:**
- the

JViewport

object that displays the scrollable contents

**See Also:**
- JScrollPane.getViewport()

---

#### public
JScrollBar
getHorizontalScrollBar()

Returns the

JScrollBar

object that handles horizontal scrolling.

**Returns:**
- the

JScrollBar

object that handles horizontal scrolling

**See Also:**
- JScrollPane.getHorizontalScrollBar()

---

#### public
JScrollBar
getVerticalScrollBar()

Returns the

JScrollBar

object that handles vertical scrolling.

**Returns:**
- the

JScrollBar

object that handles vertical scrolling

**See Also:**
- JScrollPane.getVerticalScrollBar()

---

#### public
JViewport
getRowHeader()

Returns the

JViewport

object that is the row header.

**Returns:**
- the

JViewport

object that is the row header

**See Also:**
- JScrollPane.getRowHeader()

---

#### public
JViewport
getColumnHeader()

Returns the

JViewport

object that is the column header.

**Returns:**
- the

JViewport

object that is the column header

**See Also:**
- JScrollPane.getColumnHeader()

---

#### public
Component
getCorner​(
String
key)

Returns the

Component

at the specified corner.

**Parameters:**
- key

- the

String

specifying the corner

**Returns:**
- the

Component

at the specified corner, as defined in

ScrollPaneConstants

; if

key

is not one of the
four corners,

null

is returned

**See Also:**
- JScrollPane.getCorner(java.lang.String)

---

#### public
Dimension
preferredLayoutSize​(
Container
parent)

The preferred size of a

ScrollPane

is the size of the insets,
plus the preferred size of the viewport, plus the preferred size of
the visible headers, plus the preferred size of the scrollbars
that will appear given the current view and the current
scrollbar displayPolicies.

Note that the rowHeader is calculated as part of the preferred width
and the colHeader is calculated as part of the preferred size.

**Specified by:**
- preferredLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the

Container

that will be laid out

**Returns:**
- a

Dimension

object specifying the preferred size of the
viewport and any scrollbars

**See Also:**
- ViewportLayout

,

LayoutManager

---

#### public
Dimension
minimumLayoutSize​(
Container
parent)

The minimum size of a

ScrollPane

is the size of the insets
plus minimum size of the viewport, plus the scrollpane's
viewportBorder insets, plus the minimum size
of the visible headers, plus the minimum size of the
scrollbars whose displayPolicy isn't NEVER.

**Specified by:**
- minimumLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the

Container

that will be laid out

**Returns:**
- a

Dimension

object specifying the minimum size

**See Also:**
- LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### public void layoutContainer​(
Container
parent)

Lays out the scrollpane. The positioning of components depends on
the following constraints:

- The row header, if present and visible, gets its preferred
width and the viewport's height.

The column header, if present and visible, gets its preferred
height and the viewport's width.

If a vertical scrollbar is needed, i.e. if the viewport's extent
height is smaller than its view height or if the

displayPolicy

is ALWAYS, it's treated like the row header with respect to its
dimensions and is made visible.

If a horizontal scrollbar is needed, it is treated like the
column header (see the paragraph above regarding the vertical scrollbar).

If the scrollpane has a non-

null

viewportBorder

, then space is allocated for that.

The viewport gets the space available after accounting for
the previous constraints.

The corner components, if provided, are aligned with the
ends of the scrollbars and headers. If there is a vertical
scrollbar, the right corners appear; if there is a horizontal
scrollbar, the lower corners appear; a row header gets left
corners, and a column header gets upper corners.

**Specified by:**
- layoutContainer

in interface

LayoutManager

**Parameters:**
- parent

- the

Container

to lay out

---

#### @Deprecated

public
Rectangle
getViewportBorderBounds​(
JScrollPane
scrollpane)

Returns the bounds of the border around the specified scroll pane's
viewport.

**Parameters:**
- scrollpane

- an instance of the

JScrollPane

**Returns:**
- the size and position of the viewport border

---

### Additional Sections

#### Class ScrollPaneLayout

java.lang.Object

- javax.swing.ScrollPaneLayout

javax.swing.ScrollPaneLayout

**All Implemented Interfaces:** LayoutManager

,

Serializable

,

ScrollPaneConstants

**Direct Known Subclasses:** ScrollPaneLayout.UIResource

```java
public class
ScrollPaneLayout

extends
Object

implements
LayoutManager
,
ScrollPaneConstants
,
Serializable
```

The layout manager used by

JScrollPane

.

JScrollPaneLayout

is
responsible for nine components: a viewport, two scrollbars,
a row header, a column header, and four "corner" components.

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
**See Also:** JScrollPane

,

JViewport

,

Serialized Form

public class

ScrollPaneLayout

extends

Object

implements

LayoutManager

,

ScrollPaneConstants

,

Serializable

The layout manager used by

JScrollPane

.

JScrollPaneLayout

is
responsible for nine components: a viewport, two scrollbars,
a row header, a column header, and four "corner" components.

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

ScrollPaneLayout.UIResource

The UI resource version of

ScrollPaneLayout

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JViewport

colHead

The column header child.

protected

JScrollBar

hsb

The scrollpane's horizontal scrollbar child.

protected int

hsbPolicy

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

rowHead

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

JViewport

viewport

The scrollpane's viewport child.

protected

JScrollBar

vsb

The scrollpane's vertical scrollbar child.

protected int

vsbPolicy

The display policy for the vertical scrollbar.

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

ScrollPaneLayout

()

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

String

s,

Component

c)

Adds the specified component to the layout.

protected

Component

addSingletonComponent

​(

Component

oldC,

Component

newC)

Removes an existing component.

JViewport

getColumnHeader

()

Returns the

JViewport

object that is the column header.

Component

getCorner

​(

String

key)

Returns the

Component

at the specified corner.

JScrollBar

getHorizontalScrollBar

()

Returns the

JScrollBar

object that handles horizontal scrolling.

int

getHorizontalScrollBarPolicy

()

Returns the horizontal scrollbar-display policy.

JViewport

getRowHeader

()

Returns the

JViewport

object that is the row header.

JScrollBar

getVerticalScrollBar

()

Returns the

JScrollBar

object that handles vertical scrolling.

int

getVerticalScrollBarPolicy

()

Returns the vertical scrollbar-display policy.

JViewport

getViewport

()

Returns the

JViewport

object that displays the
scrollable contents.

Rectangle

getViewportBorderBounds

​(

JScrollPane

scrollpane)

Deprecated.

As of JDK version Swing1.1
replaced by

JScrollPane.getViewportBorderBounds()

.

void

layoutContainer

​(

Container

parent)

Lays out the scrollpane.

Dimension

minimumLayoutSize

​(

Container

parent)

The minimum size of a

ScrollPane

is the size of the insets
plus minimum size of the viewport, plus the scrollpane's
viewportBorder insets, plus the minimum size
of the visible headers, plus the minimum size of the
scrollbars whose displayPolicy isn't NEVER.

Dimension

preferredLayoutSize

​(

Container

parent)

The preferred size of a

ScrollPane

is the size of the insets,
plus the preferred size of the viewport, plus the preferred size of
the visible headers, plus the preferred size of the scrollbars
that will appear given the current view and the current
scrollbar displayPolicies.

void

removeLayoutComponent

​(

Component

c)

Removes the specified component from the layout.

void

setHorizontalScrollBarPolicy

​(int x)

Sets the horizontal scrollbar-display policy.

void

setVerticalScrollBarPolicy

​(int x)

Sets the vertical scrollbar-display policy.

void

syncWithScrollPane

​(

JScrollPane

sp)

This method is invoked after the ScrollPaneLayout is set as the
LayoutManager of a

JScrollPane

.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ScrollPaneLayout.UIResource

The UI resource version of

ScrollPaneLayout

.

---

#### Nested Class Summary

The UI resource version of

ScrollPaneLayout

.

Field Summary

Fields

Modifier and Type

Field

Description

protected

JViewport

colHead

The column header child.

protected

JScrollBar

hsb

The scrollpane's horizontal scrollbar child.

protected int

hsbPolicy

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

rowHead

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

JViewport

viewport

The scrollpane's viewport child.

protected

JScrollBar

vsb

The scrollpane's vertical scrollbar child.

protected int

vsbPolicy

The display policy for the vertical scrollbar.

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

The scrollpane's viewport child.

The scrollpane's vertical scrollbar child.

The display policy for the vertical scrollbar.

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

ScrollPaneLayout

()

---

#### Constructor Summary

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

String

s,

Component

c)

Adds the specified component to the layout.

protected

Component

addSingletonComponent

​(

Component

oldC,

Component

newC)

Removes an existing component.

JViewport

getColumnHeader

()

Returns the

JViewport

object that is the column header.

Component

getCorner

​(

String

key)

Returns the

Component

at the specified corner.

JScrollBar

getHorizontalScrollBar

()

Returns the

JScrollBar

object that handles horizontal scrolling.

int

getHorizontalScrollBarPolicy

()

Returns the horizontal scrollbar-display policy.

JViewport

getRowHeader

()

Returns the

JViewport

object that is the row header.

JScrollBar

getVerticalScrollBar

()

Returns the

JScrollBar

object that handles vertical scrolling.

int

getVerticalScrollBarPolicy

()

Returns the vertical scrollbar-display policy.

JViewport

getViewport

()

Returns the

JViewport

object that displays the
scrollable contents.

Rectangle

getViewportBorderBounds

​(

JScrollPane

scrollpane)

Deprecated.

As of JDK version Swing1.1
replaced by

JScrollPane.getViewportBorderBounds()

.

void

layoutContainer

​(

Container

parent)

Lays out the scrollpane.

Dimension

minimumLayoutSize

​(

Container

parent)

The minimum size of a

ScrollPane

is the size of the insets
plus minimum size of the viewport, plus the scrollpane's
viewportBorder insets, plus the minimum size
of the visible headers, plus the minimum size of the
scrollbars whose displayPolicy isn't NEVER.

Dimension

preferredLayoutSize

​(

Container

parent)

The preferred size of a

ScrollPane

is the size of the insets,
plus the preferred size of the viewport, plus the preferred size of
the visible headers, plus the preferred size of the scrollbars
that will appear given the current view and the current
scrollbar displayPolicies.

void

removeLayoutComponent

​(

Component

c)

Removes the specified component from the layout.

void

setHorizontalScrollBarPolicy

​(int x)

Sets the horizontal scrollbar-display policy.

void

setVerticalScrollBarPolicy

​(int x)

Sets the vertical scrollbar-display policy.

void

syncWithScrollPane

​(

JScrollPane

sp)

This method is invoked after the ScrollPaneLayout is set as the
LayoutManager of a

JScrollPane

.

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

Adds the specified component to the layout.

Removes an existing component.

Returns the

JViewport

object that is the column header.

Returns the

Component

at the specified corner.

Returns the

JScrollBar

object that handles horizontal scrolling.

Returns the horizontal scrollbar-display policy.

Returns the

JViewport

object that is the row header.

Returns the

JScrollBar

object that handles vertical scrolling.

Returns the vertical scrollbar-display policy.

Returns the

JViewport

object that displays the
scrollable contents.

Deprecated.

As of JDK version Swing1.1
replaced by

JScrollPane.getViewportBorderBounds()

.

Lays out the scrollpane.

The minimum size of a

ScrollPane

is the size of the insets
plus minimum size of the viewport, plus the scrollpane's
viewportBorder insets, plus the minimum size
of the visible headers, plus the minimum size of the
scrollbars whose displayPolicy isn't NEVER.

The preferred size of a

ScrollPane

is the size of the insets,
plus the preferred size of the viewport, plus the preferred size of
the visible headers, plus the preferred size of the scrollbars
that will appear given the current view and the current
scrollbar displayPolicies.

Removes the specified component from the layout.

Sets the horizontal scrollbar-display policy.

Sets the vertical scrollbar-display policy.

This method is invoked after the ScrollPaneLayout is set as the
LayoutManager of a

JScrollPane

.

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

============ FIELD DETAIL ===========

- Field Detail

- viewport

```java
protected
JViewport
viewport
```

The scrollpane's viewport child.
Default is an empty

JViewport

.

**See Also:** JScrollPane.setViewport(javax.swing.JViewport)

- vsb

```java
protected
JScrollBar
vsb
```

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

**See Also:** JScrollPane.setVerticalScrollBar(javax.swing.JScrollBar)

- hsb

```java
protected
JScrollBar
hsb
```

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

**See Also:** JScrollPane.setHorizontalScrollBar(javax.swing.JScrollBar)

- rowHead

```java
protected
JViewport
rowHead
```

The row header child. Default is

null

.

**See Also:** JScrollPane.setRowHeader(javax.swing.JViewport)

- colHead

```java
protected
JViewport
colHead
```

The column header child. Default is

null

.

**See Also:** JScrollPane.setColumnHeader(javax.swing.JViewport)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

- vsbPolicy

```java
protected int vsbPolicy
```

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

**See Also:** JScrollPane.setVerticalScrollBarPolicy(int)

- hsbPolicy

```java
protected int hsbPolicy
```

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

**See Also:** JScrollPane.setHorizontalScrollBarPolicy(int)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ScrollPaneLayout

```java
public ScrollPaneLayout()
```

============ METHOD DETAIL ==========

- Method Detail

- syncWithScrollPane

```java
public void syncWithScrollPane​(
JScrollPane
sp)
```

This method is invoked after the ScrollPaneLayout is set as the
LayoutManager of a

JScrollPane

.
It initializes all of the internal fields that
are ordinarily set by

addLayoutComponent

. For example:

```java
ScrollPaneLayout mySPLayout = new ScrollPanelLayout() {
public void layoutContainer(Container p) {
super.layoutContainer(p);
// do some extra work here ...
}
};
scrollpane.setLayout(mySPLayout):
```

**Parameters:** sp

- an instance of the

JScrollPane

- addSingletonComponent

```java
protected
Component
addSingletonComponent​(
Component
oldC,

Component
newC)
```

Removes an existing component. When a new component, such as
the left corner, or vertical scrollbar, is added, the old one,
if it exists, must be removed.

This method returns

newC

. If

oldC

is
not equal to

newC

and is non-

null

,
it will be removed from its parent.

**Parameters:** oldC

- the

Component

to replace
**Parameters:** newC

- the

Component

to add
**Returns:** the

newC

- addLayoutComponent

```java
public void addLayoutComponent​(
String
s,

Component
c)
```

Adds the specified component to the layout. The layout is
identified using one of:

- ScrollPaneConstants.VIEWPORT

ScrollPaneConstants.VERTICAL_SCROLLBAR

ScrollPaneConstants.HORIZONTAL_SCROLLBAR

ScrollPaneConstants.ROW_HEADER

ScrollPaneConstants.COLUMN_HEADER

ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** s

- the component identifier
**Parameters:** c

- the component to be added
**Throws:** IllegalArgumentException

- if

s

is an invalid key

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
c)
```

Removes the specified component from the layout.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** c

- the component to remove

- getVerticalScrollBarPolicy

```java
public int getVerticalScrollBarPolicy()
```

Returns the vertical scrollbar-display policy.

**Returns:** an integer giving the display policy
**See Also:** setVerticalScrollBarPolicy(int)

- setVerticalScrollBarPolicy

```java
public void setVerticalScrollBarPolicy​(int x)
```

Sets the vertical scrollbar-display policy. The options
are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

**Parameters:** x

- an integer giving the display policy
**Throws:** IllegalArgumentException

- if

x

is an invalid
vertical scroll bar policy, as listed above

- getHorizontalScrollBarPolicy

```java
public int getHorizontalScrollBarPolicy()
```

Returns the horizontal scrollbar-display policy.

**Returns:** an integer giving the display policy
**See Also:** setHorizontalScrollBarPolicy(int)

- setHorizontalScrollBarPolicy

```java
public void setHorizontalScrollBarPolicy​(int x)
```

Sets the horizontal scrollbar-display policy.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

**Parameters:** x

- an int giving the display policy
**Throws:** IllegalArgumentException

- if

x

is not a valid
horizontal scrollbar policy, as listed above

- getViewport

```java
public
JViewport
getViewport()
```

Returns the

JViewport

object that displays the
scrollable contents.

**Returns:** the

JViewport

object that displays the scrollable contents
**See Also:** JScrollPane.getViewport()

- getHorizontalScrollBar

```java
public
JScrollBar
getHorizontalScrollBar()
```

Returns the

JScrollBar

object that handles horizontal scrolling.

**Returns:** the

JScrollBar

object that handles horizontal scrolling
**See Also:** JScrollPane.getHorizontalScrollBar()

- getVerticalScrollBar

```java
public
JScrollBar
getVerticalScrollBar()
```

Returns the

JScrollBar

object that handles vertical scrolling.

**Returns:** the

JScrollBar

object that handles vertical scrolling
**See Also:** JScrollPane.getVerticalScrollBar()

- getRowHeader

```java
public
JViewport
getRowHeader()
```

Returns the

JViewport

object that is the row header.

**Returns:** the

JViewport

object that is the row header
**See Also:** JScrollPane.getRowHeader()

- getColumnHeader

```java
public
JViewport
getColumnHeader()
```

Returns the

JViewport

object that is the column header.

**Returns:** the

JViewport

object that is the column header
**See Also:** JScrollPane.getColumnHeader()

- getCorner

```java
public
Component
getCorner​(
String
key)
```

Returns the

Component

at the specified corner.

**Parameters:** key

- the

String

specifying the corner
**Returns:** the

Component

at the specified corner, as defined in

ScrollPaneConstants

; if

key

is not one of the
four corners,

null

is returned
**See Also:** JScrollPane.getCorner(java.lang.String)

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

The preferred size of a

ScrollPane

is the size of the insets,
plus the preferred size of the viewport, plus the preferred size of
the visible headers, plus the preferred size of the scrollbars
that will appear given the current view and the current
scrollbar displayPolicies.

Note that the rowHeader is calculated as part of the preferred width
and the colHeader is calculated as part of the preferred size.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the

Container

that will be laid out
**Returns:** a

Dimension

object specifying the preferred size of the
viewport and any scrollbars
**See Also:** ViewportLayout

,

LayoutManager

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

The minimum size of a

ScrollPane

is the size of the insets
plus minimum size of the viewport, plus the scrollpane's
viewportBorder insets, plus the minimum size
of the visible headers, plus the minimum size of the
scrollbars whose displayPolicy isn't NEVER.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the

Container

that will be laid out
**Returns:** a

Dimension

object specifying the minimum size
**See Also:** LayoutManager.preferredLayoutSize(java.awt.Container)

- layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Lays out the scrollpane. The positioning of components depends on
the following constraints:

- The row header, if present and visible, gets its preferred
width and the viewport's height.

The column header, if present and visible, gets its preferred
height and the viewport's width.

If a vertical scrollbar is needed, i.e. if the viewport's extent
height is smaller than its view height or if the

displayPolicy

is ALWAYS, it's treated like the row header with respect to its
dimensions and is made visible.

If a horizontal scrollbar is needed, it is treated like the
column header (see the paragraph above regarding the vertical scrollbar).

If the scrollpane has a non-

null

viewportBorder

, then space is allocated for that.

The viewport gets the space available after accounting for
the previous constraints.

The corner components, if provided, are aligned with the
ends of the scrollbars and headers. If there is a vertical
scrollbar, the right corners appear; if there is a horizontal
scrollbar, the lower corners appear; a row header gets left
corners, and a column header gets upper corners.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the

Container

to lay out

- getViewportBorderBounds

```java
@Deprecated

public
Rectangle
getViewportBorderBounds​(
JScrollPane
scrollpane)
```

Deprecated.

As of JDK version Swing1.1
replaced by

JScrollPane.getViewportBorderBounds()

.

Returns the bounds of the border around the specified scroll pane's
viewport.

**Parameters:** scrollpane

- an instance of the

JScrollPane
**Returns:** the size and position of the viewport border

Field Detail

- viewport

```java
protected
JViewport
viewport
```

The scrollpane's viewport child.
Default is an empty

JViewport

.

**See Also:** JScrollPane.setViewport(javax.swing.JViewport)

- vsb

```java
protected
JScrollBar
vsb
```

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

**See Also:** JScrollPane.setVerticalScrollBar(javax.swing.JScrollBar)

- hsb

```java
protected
JScrollBar
hsb
```

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

**See Also:** JScrollPane.setHorizontalScrollBar(javax.swing.JScrollBar)

- rowHead

```java
protected
JViewport
rowHead
```

The row header child. Default is

null

.

**See Also:** JScrollPane.setRowHeader(javax.swing.JViewport)

- colHead

```java
protected
JViewport
colHead
```

The column header child. Default is

null

.

**See Also:** JScrollPane.setColumnHeader(javax.swing.JViewport)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

- vsbPolicy

```java
protected int vsbPolicy
```

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

**See Also:** JScrollPane.setVerticalScrollBarPolicy(int)

- hsbPolicy

```java
protected int hsbPolicy
```

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

**See Also:** JScrollPane.setHorizontalScrollBarPolicy(int)

---

#### Field Detail

viewport

```java
protected
JViewport
viewport
```

The scrollpane's viewport child.
Default is an empty

JViewport

.

**See Also:** JScrollPane.setViewport(javax.swing.JViewport)

---

#### viewport

protected

JViewport

viewport

The scrollpane's viewport child.
Default is an empty

JViewport

.

vsb

```java
protected
JScrollBar
vsb
```

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

**See Also:** JScrollPane.setVerticalScrollBar(javax.swing.JScrollBar)

---

#### vsb

protected

JScrollBar

vsb

The scrollpane's vertical scrollbar child.
Default is a

JScrollBar

.

hsb

```java
protected
JScrollBar
hsb
```

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

**See Also:** JScrollPane.setHorizontalScrollBar(javax.swing.JScrollBar)

---

#### hsb

protected

JScrollBar

hsb

The scrollpane's horizontal scrollbar child.
Default is a

JScrollBar

.

rowHead

```java
protected
JViewport
rowHead
```

The row header child. Default is

null

.

**See Also:** JScrollPane.setRowHeader(javax.swing.JViewport)

---

#### rowHead

protected

JViewport

rowHead

The row header child. Default is

null

.

colHead

```java
protected
JViewport
colHead
```

The column header child. Default is

null

.

**See Also:** JScrollPane.setColumnHeader(javax.swing.JViewport)

---

#### colHead

protected

JViewport

colHead

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

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

**See Also:** JScrollPane.setCorner(java.lang.String, java.awt.Component)

---

#### upperRight

protected

Component

upperRight

The component to display in the upper right corner.
Default is

null

.

vsbPolicy

```java
protected int vsbPolicy
```

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

**See Also:** JScrollPane.setVerticalScrollBarPolicy(int)

---

#### vsbPolicy

protected int vsbPolicy

The display policy for the vertical scrollbar.
The default is

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

This field is obsolete, please use the

JScrollPane

field instead.

hsbPolicy

```java
protected int hsbPolicy
```

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

**See Also:** JScrollPane.setHorizontalScrollBarPolicy(int)

---

#### hsbPolicy

protected int hsbPolicy

The display policy for the horizontal scrollbar.
The default is

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

.

This field is obsolete, please use the

JScrollPane

field instead.

This field is obsolete, please use the

JScrollPane

field instead.

Constructor Detail

- ScrollPaneLayout

```java
public ScrollPaneLayout()
```

---

#### Constructor Detail

ScrollPaneLayout

```java
public ScrollPaneLayout()
```

---

#### ScrollPaneLayout

public ScrollPaneLayout()

Method Detail

- syncWithScrollPane

```java
public void syncWithScrollPane​(
JScrollPane
sp)
```

This method is invoked after the ScrollPaneLayout is set as the
LayoutManager of a

JScrollPane

.
It initializes all of the internal fields that
are ordinarily set by

addLayoutComponent

. For example:

```java
ScrollPaneLayout mySPLayout = new ScrollPanelLayout() {
public void layoutContainer(Container p) {
super.layoutContainer(p);
// do some extra work here ...
}
};
scrollpane.setLayout(mySPLayout):
```

**Parameters:** sp

- an instance of the

JScrollPane

- addSingletonComponent

```java
protected
Component
addSingletonComponent​(
Component
oldC,

Component
newC)
```

Removes an existing component. When a new component, such as
the left corner, or vertical scrollbar, is added, the old one,
if it exists, must be removed.

This method returns

newC

. If

oldC

is
not equal to

newC

and is non-

null

,
it will be removed from its parent.

**Parameters:** oldC

- the

Component

to replace
**Parameters:** newC

- the

Component

to add
**Returns:** the

newC

- addLayoutComponent

```java
public void addLayoutComponent​(
String
s,

Component
c)
```

Adds the specified component to the layout. The layout is
identified using one of:

- ScrollPaneConstants.VIEWPORT

ScrollPaneConstants.VERTICAL_SCROLLBAR

ScrollPaneConstants.HORIZONTAL_SCROLLBAR

ScrollPaneConstants.ROW_HEADER

ScrollPaneConstants.COLUMN_HEADER

ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** s

- the component identifier
**Parameters:** c

- the component to be added
**Throws:** IllegalArgumentException

- if

s

is an invalid key

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
c)
```

Removes the specified component from the layout.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** c

- the component to remove

- getVerticalScrollBarPolicy

```java
public int getVerticalScrollBarPolicy()
```

Returns the vertical scrollbar-display policy.

**Returns:** an integer giving the display policy
**See Also:** setVerticalScrollBarPolicy(int)

- setVerticalScrollBarPolicy

```java
public void setVerticalScrollBarPolicy​(int x)
```

Sets the vertical scrollbar-display policy. The options
are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

**Parameters:** x

- an integer giving the display policy
**Throws:** IllegalArgumentException

- if

x

is an invalid
vertical scroll bar policy, as listed above

- getHorizontalScrollBarPolicy

```java
public int getHorizontalScrollBarPolicy()
```

Returns the horizontal scrollbar-display policy.

**Returns:** an integer giving the display policy
**See Also:** setHorizontalScrollBarPolicy(int)

- setHorizontalScrollBarPolicy

```java
public void setHorizontalScrollBarPolicy​(int x)
```

Sets the horizontal scrollbar-display policy.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

**Parameters:** x

- an int giving the display policy
**Throws:** IllegalArgumentException

- if

x

is not a valid
horizontal scrollbar policy, as listed above

- getViewport

```java
public
JViewport
getViewport()
```

Returns the

JViewport

object that displays the
scrollable contents.

**Returns:** the

JViewport

object that displays the scrollable contents
**See Also:** JScrollPane.getViewport()

- getHorizontalScrollBar

```java
public
JScrollBar
getHorizontalScrollBar()
```

Returns the

JScrollBar

object that handles horizontal scrolling.

**Returns:** the

JScrollBar

object that handles horizontal scrolling
**See Also:** JScrollPane.getHorizontalScrollBar()

- getVerticalScrollBar

```java
public
JScrollBar
getVerticalScrollBar()
```

Returns the

JScrollBar

object that handles vertical scrolling.

**Returns:** the

JScrollBar

object that handles vertical scrolling
**See Also:** JScrollPane.getVerticalScrollBar()

- getRowHeader

```java
public
JViewport
getRowHeader()
```

Returns the

JViewport

object that is the row header.

**Returns:** the

JViewport

object that is the row header
**See Also:** JScrollPane.getRowHeader()

- getColumnHeader

```java
public
JViewport
getColumnHeader()
```

Returns the

JViewport

object that is the column header.

**Returns:** the

JViewport

object that is the column header
**See Also:** JScrollPane.getColumnHeader()

- getCorner

```java
public
Component
getCorner​(
String
key)
```

Returns the

Component

at the specified corner.

**Parameters:** key

- the

String

specifying the corner
**Returns:** the

Component

at the specified corner, as defined in

ScrollPaneConstants

; if

key

is not one of the
four corners,

null

is returned
**See Also:** JScrollPane.getCorner(java.lang.String)

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

The preferred size of a

ScrollPane

is the size of the insets,
plus the preferred size of the viewport, plus the preferred size of
the visible headers, plus the preferred size of the scrollbars
that will appear given the current view and the current
scrollbar displayPolicies.

Note that the rowHeader is calculated as part of the preferred width
and the colHeader is calculated as part of the preferred size.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the

Container

that will be laid out
**Returns:** a

Dimension

object specifying the preferred size of the
viewport and any scrollbars
**See Also:** ViewportLayout

,

LayoutManager

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

The minimum size of a

ScrollPane

is the size of the insets
plus minimum size of the viewport, plus the scrollpane's
viewportBorder insets, plus the minimum size
of the visible headers, plus the minimum size of the
scrollbars whose displayPolicy isn't NEVER.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the

Container

that will be laid out
**Returns:** a

Dimension

object specifying the minimum size
**See Also:** LayoutManager.preferredLayoutSize(java.awt.Container)

- layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Lays out the scrollpane. The positioning of components depends on
the following constraints:

- The row header, if present and visible, gets its preferred
width and the viewport's height.

The column header, if present and visible, gets its preferred
height and the viewport's width.

If a vertical scrollbar is needed, i.e. if the viewport's extent
height is smaller than its view height or if the

displayPolicy

is ALWAYS, it's treated like the row header with respect to its
dimensions and is made visible.

If a horizontal scrollbar is needed, it is treated like the
column header (see the paragraph above regarding the vertical scrollbar).

If the scrollpane has a non-

null

viewportBorder

, then space is allocated for that.

The viewport gets the space available after accounting for
the previous constraints.

The corner components, if provided, are aligned with the
ends of the scrollbars and headers. If there is a vertical
scrollbar, the right corners appear; if there is a horizontal
scrollbar, the lower corners appear; a row header gets left
corners, and a column header gets upper corners.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the

Container

to lay out

- getViewportBorderBounds

```java
@Deprecated

public
Rectangle
getViewportBorderBounds​(
JScrollPane
scrollpane)
```

Deprecated.

As of JDK version Swing1.1
replaced by

JScrollPane.getViewportBorderBounds()

.

Returns the bounds of the border around the specified scroll pane's
viewport.

**Parameters:** scrollpane

- an instance of the

JScrollPane
**Returns:** the size and position of the viewport border

---

#### Method Detail

syncWithScrollPane

```java
public void syncWithScrollPane​(
JScrollPane
sp)
```

This method is invoked after the ScrollPaneLayout is set as the
LayoutManager of a

JScrollPane

.
It initializes all of the internal fields that
are ordinarily set by

addLayoutComponent

. For example:

```java
ScrollPaneLayout mySPLayout = new ScrollPanelLayout() {
public void layoutContainer(Container p) {
super.layoutContainer(p);
// do some extra work here ...
}
};
scrollpane.setLayout(mySPLayout):
```

**Parameters:** sp

- an instance of the

JScrollPane

---

#### syncWithScrollPane

public void syncWithScrollPane​(

JScrollPane

sp)

This method is invoked after the ScrollPaneLayout is set as the
LayoutManager of a

JScrollPane

.
It initializes all of the internal fields that
are ordinarily set by

addLayoutComponent

. For example:

```java
ScrollPaneLayout mySPLayout = new ScrollPanelLayout() {
public void layoutContainer(Container p) {
super.layoutContainer(p);
// do some extra work here ...
}
};
scrollpane.setLayout(mySPLayout):
```

ScrollPaneLayout mySPLayout = new ScrollPanelLayout() {
public void layoutContainer(Container p) {
super.layoutContainer(p);
// do some extra work here ...
}
};
scrollpane.setLayout(mySPLayout):

addSingletonComponent

```java
protected
Component
addSingletonComponent​(
Component
oldC,

Component
newC)
```

Removes an existing component. When a new component, such as
the left corner, or vertical scrollbar, is added, the old one,
if it exists, must be removed.

This method returns

newC

. If

oldC

is
not equal to

newC

and is non-

null

,
it will be removed from its parent.

**Parameters:** oldC

- the

Component

to replace
**Parameters:** newC

- the

Component

to add
**Returns:** the

newC

---

#### addSingletonComponent

protected

Component

addSingletonComponent​(

Component

oldC,

Component

newC)

Removes an existing component. When a new component, such as
the left corner, or vertical scrollbar, is added, the old one,
if it exists, must be removed.

This method returns

newC

. If

oldC

is
not equal to

newC

and is non-

null

,
it will be removed from its parent.

This method returns

newC

. If

oldC

is
not equal to

newC

and is non-

null

,
it will be removed from its parent.

addLayoutComponent

```java
public void addLayoutComponent​(
String
s,

Component
c)
```

Adds the specified component to the layout. The layout is
identified using one of:

- ScrollPaneConstants.VIEWPORT

ScrollPaneConstants.VERTICAL_SCROLLBAR

ScrollPaneConstants.HORIZONTAL_SCROLLBAR

ScrollPaneConstants.ROW_HEADER

ScrollPaneConstants.COLUMN_HEADER

ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** s

- the component identifier
**Parameters:** c

- the component to be added
**Throws:** IllegalArgumentException

- if

s

is an invalid key

---

#### addLayoutComponent

public void addLayoutComponent​(

String

s,

Component

c)

Adds the specified component to the layout. The layout is
identified using one of:

- ScrollPaneConstants.VIEWPORT

ScrollPaneConstants.VERTICAL_SCROLLBAR

ScrollPaneConstants.HORIZONTAL_SCROLLBAR

ScrollPaneConstants.ROW_HEADER

ScrollPaneConstants.COLUMN_HEADER

ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

ScrollPaneConstants.VIEWPORT

ScrollPaneConstants.VERTICAL_SCROLLBAR

ScrollPaneConstants.HORIZONTAL_SCROLLBAR

ScrollPaneConstants.ROW_HEADER

ScrollPaneConstants.COLUMN_HEADER

ScrollPaneConstants.LOWER_LEFT_CORNER

ScrollPaneConstants.LOWER_RIGHT_CORNER

ScrollPaneConstants.UPPER_LEFT_CORNER

ScrollPaneConstants.UPPER_RIGHT_CORNER

removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
c)
```

Removes the specified component from the layout.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** c

- the component to remove

---

#### removeLayoutComponent

public void removeLayoutComponent​(

Component

c)

Removes the specified component from the layout.

getVerticalScrollBarPolicy

```java
public int getVerticalScrollBarPolicy()
```

Returns the vertical scrollbar-display policy.

**Returns:** an integer giving the display policy
**See Also:** setVerticalScrollBarPolicy(int)

---

#### getVerticalScrollBarPolicy

public int getVerticalScrollBarPolicy()

Returns the vertical scrollbar-display policy.

setVerticalScrollBarPolicy

```java
public void setVerticalScrollBarPolicy​(int x)
```

Sets the vertical scrollbar-display policy. The options
are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

**Parameters:** x

- an integer giving the display policy
**Throws:** IllegalArgumentException

- if

x

is an invalid
vertical scroll bar policy, as listed above

---

#### setVerticalScrollBarPolicy

public void setVerticalScrollBarPolicy​(int x)

Sets the vertical scrollbar-display policy. The options
are:

- ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER

ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS

getHorizontalScrollBarPolicy

```java
public int getHorizontalScrollBarPolicy()
```

Returns the horizontal scrollbar-display policy.

**Returns:** an integer giving the display policy
**See Also:** setHorizontalScrollBarPolicy(int)

---

#### getHorizontalScrollBarPolicy

public int getHorizontalScrollBarPolicy()

Returns the horizontal scrollbar-display policy.

setHorizontalScrollBarPolicy

```java
public void setHorizontalScrollBarPolicy​(int x)
```

Sets the horizontal scrollbar-display policy.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

**Parameters:** x

- an int giving the display policy
**Throws:** IllegalArgumentException

- if

x

is not a valid
horizontal scrollbar policy, as listed above

---

#### setHorizontalScrollBarPolicy

public void setHorizontalScrollBarPolicy​(int x)

Sets the horizontal scrollbar-display policy.
The options are:

- ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

Note: Applications should use the

JScrollPane

version
of this method. It only exists for backwards compatibility
with the Swing 1.0.2 (and earlier) versions of this class.

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER

ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS

getViewport

```java
public
JViewport
getViewport()
```

Returns the

JViewport

object that displays the
scrollable contents.

**Returns:** the

JViewport

object that displays the scrollable contents
**See Also:** JScrollPane.getViewport()

---

#### getViewport

public

JViewport

getViewport()

Returns the

JViewport

object that displays the
scrollable contents.

getHorizontalScrollBar

```java
public
JScrollBar
getHorizontalScrollBar()
```

Returns the

JScrollBar

object that handles horizontal scrolling.

**Returns:** the

JScrollBar

object that handles horizontal scrolling
**See Also:** JScrollPane.getHorizontalScrollBar()

---

#### getHorizontalScrollBar

public

JScrollBar

getHorizontalScrollBar()

Returns the

JScrollBar

object that handles horizontal scrolling.

getVerticalScrollBar

```java
public
JScrollBar
getVerticalScrollBar()
```

Returns the

JScrollBar

object that handles vertical scrolling.

**Returns:** the

JScrollBar

object that handles vertical scrolling
**See Also:** JScrollPane.getVerticalScrollBar()

---

#### getVerticalScrollBar

public

JScrollBar

getVerticalScrollBar()

Returns the

JScrollBar

object that handles vertical scrolling.

getRowHeader

```java
public
JViewport
getRowHeader()
```

Returns the

JViewport

object that is the row header.

**Returns:** the

JViewport

object that is the row header
**See Also:** JScrollPane.getRowHeader()

---

#### getRowHeader

public

JViewport

getRowHeader()

Returns the

JViewport

object that is the row header.

getColumnHeader

```java
public
JViewport
getColumnHeader()
```

Returns the

JViewport

object that is the column header.

**Returns:** the

JViewport

object that is the column header
**See Also:** JScrollPane.getColumnHeader()

---

#### getColumnHeader

public

JViewport

getColumnHeader()

Returns the

JViewport

object that is the column header.

getCorner

```java
public
Component
getCorner​(
String
key)
```

Returns the

Component

at the specified corner.

**Parameters:** key

- the

String

specifying the corner
**Returns:** the

Component

at the specified corner, as defined in

ScrollPaneConstants

; if

key

is not one of the
four corners,

null

is returned
**See Also:** JScrollPane.getCorner(java.lang.String)

---

#### getCorner

public

Component

getCorner​(

String

key)

Returns the

Component

at the specified corner.

preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

The preferred size of a

ScrollPane

is the size of the insets,
plus the preferred size of the viewport, plus the preferred size of
the visible headers, plus the preferred size of the scrollbars
that will appear given the current view and the current
scrollbar displayPolicies.

Note that the rowHeader is calculated as part of the preferred width
and the colHeader is calculated as part of the preferred size.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the

Container

that will be laid out
**Returns:** a

Dimension

object specifying the preferred size of the
viewport and any scrollbars
**See Also:** ViewportLayout

,

LayoutManager

---

#### preferredLayoutSize

public

Dimension

preferredLayoutSize​(

Container

parent)

The preferred size of a

ScrollPane

is the size of the insets,
plus the preferred size of the viewport, plus the preferred size of
the visible headers, plus the preferred size of the scrollbars
that will appear given the current view and the current
scrollbar displayPolicies.

Note that the rowHeader is calculated as part of the preferred width
and the colHeader is calculated as part of the preferred size.

Note that the rowHeader is calculated as part of the preferred width
and the colHeader is calculated as part of the preferred size.

minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

The minimum size of a

ScrollPane

is the size of the insets
plus minimum size of the viewport, plus the scrollpane's
viewportBorder insets, plus the minimum size
of the visible headers, plus the minimum size of the
scrollbars whose displayPolicy isn't NEVER.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the

Container

that will be laid out
**Returns:** a

Dimension

object specifying the minimum size
**See Also:** LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### minimumLayoutSize

public

Dimension

minimumLayoutSize​(

Container

parent)

The minimum size of a

ScrollPane

is the size of the insets
plus minimum size of the viewport, plus the scrollpane's
viewportBorder insets, plus the minimum size
of the visible headers, plus the minimum size of the
scrollbars whose displayPolicy isn't NEVER.

layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Lays out the scrollpane. The positioning of components depends on
the following constraints:

- The row header, if present and visible, gets its preferred
width and the viewport's height.

The column header, if present and visible, gets its preferred
height and the viewport's width.

If a vertical scrollbar is needed, i.e. if the viewport's extent
height is smaller than its view height or if the

displayPolicy

is ALWAYS, it's treated like the row header with respect to its
dimensions and is made visible.

If a horizontal scrollbar is needed, it is treated like the
column header (see the paragraph above regarding the vertical scrollbar).

If the scrollpane has a non-

null

viewportBorder

, then space is allocated for that.

The viewport gets the space available after accounting for
the previous constraints.

The corner components, if provided, are aligned with the
ends of the scrollbars and headers. If there is a vertical
scrollbar, the right corners appear; if there is a horizontal
scrollbar, the lower corners appear; a row header gets left
corners, and a column header gets upper corners.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the

Container

to lay out

---

#### layoutContainer

public void layoutContainer​(

Container

parent)

Lays out the scrollpane. The positioning of components depends on
the following constraints:

- The row header, if present and visible, gets its preferred
width and the viewport's height.

The column header, if present and visible, gets its preferred
height and the viewport's width.

If a vertical scrollbar is needed, i.e. if the viewport's extent
height is smaller than its view height or if the

displayPolicy

is ALWAYS, it's treated like the row header with respect to its
dimensions and is made visible.

If a horizontal scrollbar is needed, it is treated like the
column header (see the paragraph above regarding the vertical scrollbar).

If the scrollpane has a non-

null

viewportBorder

, then space is allocated for that.

The viewport gets the space available after accounting for
the previous constraints.

The corner components, if provided, are aligned with the
ends of the scrollbars and headers. If there is a vertical
scrollbar, the right corners appear; if there is a horizontal
scrollbar, the lower corners appear; a row header gets left
corners, and a column header gets upper corners.

The row header, if present and visible, gets its preferred
width and the viewport's height.

The column header, if present and visible, gets its preferred
height and the viewport's width.

If a vertical scrollbar is needed, i.e. if the viewport's extent
height is smaller than its view height or if the

displayPolicy

is ALWAYS, it's treated like the row header with respect to its
dimensions and is made visible.

If a horizontal scrollbar is needed, it is treated like the
column header (see the paragraph above regarding the vertical scrollbar).

If the scrollpane has a non-

null

viewportBorder

, then space is allocated for that.

The viewport gets the space available after accounting for
the previous constraints.

The corner components, if provided, are aligned with the
ends of the scrollbars and headers. If there is a vertical
scrollbar, the right corners appear; if there is a horizontal
scrollbar, the lower corners appear; a row header gets left
corners, and a column header gets upper corners.

getViewportBorderBounds

```java
@Deprecated

public
Rectangle
getViewportBorderBounds​(
JScrollPane
scrollpane)
```

Deprecated.

As of JDK version Swing1.1
replaced by

JScrollPane.getViewportBorderBounds()

.

Returns the bounds of the border around the specified scroll pane's
viewport.

**Parameters:** scrollpane

- an instance of the

JScrollPane
**Returns:** the size and position of the viewport border

---

#### getViewportBorderBounds

@Deprecated

public

Rectangle

getViewportBorderBounds​(

JScrollPane

scrollpane)

Returns the bounds of the border around the specified scroll pane's
viewport.

---

