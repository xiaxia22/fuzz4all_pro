# Class JInternalFrame

**Source:** `java.desktop\javax\swing\JInternalFrame.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="JMenuBar",

description
="A frame container which is contained within another window.")
public class
JInternalFrame

extends
JComponent

implements
Accessible
,
WindowConstants
,
RootPaneContainer
```

A lightweight object that provides many of the features of
a native frame, including dragging, closing, becoming an icon,
resizing, title display, and support for a menu bar.
For task-oriented documentation and examples of using internal frames,
see

How to Use Internal Frames

,
a section in

The Java Tutorial

.

Generally,
you add

JInternalFrame

s to a

JDesktopPane

. The UI
delegates the look-and-feel-specific actions to the

DesktopManager

object maintained by the

JDesktopPane

.

The

JInternalFrame

content pane
is where you add child components.
As a convenience, the

add

,

remove

, and

setLayout

methods of this class are overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to an internal frame as follows:

```java
internalFrame.add(child);
```

And the child will be added to the contentPane.
The content pane is actually managed by an instance of

JRootPane

,
which also manages a layout pane, glass pane, and
optional menu bar for the internal frame. Please see the

JRootPane

documentation for a complete description of these components.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JInternalFrame

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

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

RootPaneContainer

,

WindowConstants

---

### Field Details

#### protected
JRootPane
rootPane

The

JRootPane

instance that manages the
content pane
and optional menu bar for this internal frame, as well as the
glass pane.

**See Also:**
- JRootPane

,

RootPaneContainer

---

#### protected boolean rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JInternalFrame

is
constructed.

**See Also:**
- isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### protected boolean closable

The frame can be closed.

---

#### protected boolean isClosed

The frame has been closed.

---

#### protected boolean maximizable

The frame can be expanded to the size of the desktop pane.

---

#### protected boolean isMaximum

The frame has been expanded to its maximum size.

**See Also:**
- maximizable

---

#### protected boolean iconable

The frame can "iconified" (shrunk down and displayed as
an icon-image).

**See Also:**
- JInternalFrame.JDesktopIcon

,

setIconifiable(boolean)

---

#### protected boolean isIcon

The frame has been iconified.

**See Also:**
- isIcon()

---

#### protected boolean resizable

The frame's size can be changed.

---

#### protected boolean isSelected

The frame is currently selected.

---

#### protected
Icon
frameIcon

The icon shown in the top-left corner of this internal frame.

---

#### protected
String
title

The title displayed in this internal frame's title bar.

---

#### protected
JInternalFrame.JDesktopIcon
desktopIcon

The icon that is displayed when this internal frame is iconified.

**See Also:**
- iconable

---

#### public static final
String
CONTENT_PANE_PROPERTY

Bound property name.

**See Also:**
- Constant Field Values

---

#### public static final
String
MENU_BAR_PROPERTY

Bound property name.

**See Also:**
- Constant Field Values

---

#### public static final
String
TITLE_PROPERTY

Bound property name.

**See Also:**
- Constant Field Values

---

#### public static final
String
LAYERED_PANE_PROPERTY

Bound property name.

**See Also:**
- Constant Field Values

---

#### public static final
String
ROOT_PANE_PROPERTY

Bound property name.

**See Also:**
- Constant Field Values

---

#### public static final
String
GLASS_PANE_PROPERTY

Bound property name.

**See Also:**
- Constant Field Values

---

#### public static final
String
FRAME_ICON_PROPERTY

Bound property name.

**See Also:**
- Constant Field Values

---

#### public static final
String
IS_SELECTED_PROPERTY

Constrained property name indicated that this frame has
selected status.

**See Also:**
- Constant Field Values

---

#### public static final
String
IS_CLOSED_PROPERTY

Constrained property name indicating that the internal frame is closed.

**See Also:**
- Constant Field Values

---

#### public static final
String
IS_MAXIMUM_PROPERTY

Constrained property name indicating that the internal frame is maximized.

**See Also:**
- Constant Field Values

---

#### public static final
String
IS_ICON_PROPERTY

Constrained property name indicating that the internal frame is iconified.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public JInternalFrame()

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with no title.

---

#### public JInternalFrame​(
String
title)

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with the specified title.
Note that passing in a

null

title

results in
unspecified behavior and possibly an exception.

**Parameters:**
- title

- the non-

null

String

to display in the title bar

---

#### public JInternalFrame​(
String
title,
boolean resizable)

Creates a non-closable, non-maximizable, non-iconifiable

JInternalFrame

with the specified title
and resizability.

**Parameters:**
- title

- the

String

to display in the title bar
- resizable

- if

true

, the internal frame can be resized

---

#### public JInternalFrame​(
String
title,
boolean resizable,
boolean closable)

Creates a non-maximizable, non-iconifiable

JInternalFrame

with the specified title, resizability, and
closability.

**Parameters:**
- title

- the

String

to display in the title bar
- resizable

- if

true

, the internal frame can be resized
- closable

- if

true

, the internal frame can be closed

---

#### public JInternalFrame​(
String
title,
boolean resizable,
boolean closable,
boolean maximizable)

Creates a non-iconifiable

JInternalFrame

with the specified title,
resizability, closability, and maximizability.

**Parameters:**
- title

- the

String

to display in the title bar
- resizable

- if

true

, the internal frame can be resized
- closable

- if

true

, the internal frame can be closed
- maximizable

- if

true

, the internal frame can be maximized

---

#### public JInternalFrame​(
String
title,
boolean resizable,
boolean closable,
boolean maximizable,
boolean iconifiable)

Creates a

JInternalFrame

with the specified title,
resizability, closability, maximizability, and iconifiability.
All

JInternalFrame

constructors use this one.

**Parameters:**
- title

- the

String

to display in the title bar
- resizable

- if

true

, the internal frame can be resized
- closable

- if

true

, the internal frame can be closed
- maximizable

- if

true

, the internal frame can be maximized
- iconifiable

- if

true

, the internal frame can be iconified

---

### Method Details

#### protected
JRootPane
createRootPane()

Called by the constructor to set up the

JRootPane

.

**Returns:**
- a new

JRootPane

**See Also:**
- JRootPane

---

#### public
InternalFrameUI
getUI()

Returns the look-and-feel object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

InternalFrameUI

object that renders
this component

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
InternalFrameUI
ui)

Sets the UI delegate for this

JInternalFrame

.

**Parameters:**
- ui

- the UI delegate

---

#### public void updateUI()

Notification from the

UIManager

that the look and feel
has changed.
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

description
="UIClassID")
public
String
getUIClassID()

Returns the name of the look-and-feel
class that renders this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "InternalFrameUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### protected boolean isRootPaneCheckingEnabled()

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Returns:**
- true if

add

and

setLayout

are forwarded; false otherwise

**See Also:**
- addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### @BeanProperty
(
hidden
=true,

description
="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Parameters:**
- enabled

- true if

add

and

setLayout

are forwarded, false if they should operate directly on the

JInternalFrame

.

**See Also:**
- addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

isRootPaneCheckingEnabled()

,

RootPaneContainer

---

#### protected void addImpl​(
Component
comp,

Object
constraints,
int index)

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

**Overrides:**
- addImpl

in class

Container

**Parameters:**
- comp

- the component to be enhanced
- constraints

- the constraints to be respected
- index

- the index

**Throws:**
- IllegalArgumentException

- if

index

is invalid
- IllegalArgumentException

- if adding the container's parent
to itself
- IllegalArgumentException

- if adding a window to a container

**See Also:**
- setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### public void remove​(
Component
comp)

Removes the specified component from the container. If

comp

is not a child of the

JInternalFrame

this will forward the call to the

contentPane

.

**Overrides:**
- remove

in class

Container

**Parameters:**
- comp

- the component to be removed

**Throws:**
- NullPointerException

- if

comp

is null

**See Also:**
- Container.add(java.awt.Component)

,

RootPaneContainer

---

#### public void setLayout​(
LayoutManager
manager)

Ensures that, by default, the layout of this component cannot be set.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

**Overrides:**
- setLayout

in class

Container

**Parameters:**
- manager

- the

LayoutManager

**See Also:**
- setRootPaneCheckingEnabled(boolean)

---

#### @Deprecated

public
JMenuBar
getMenuBar()

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

**Returns:**
- the current menu bar, or

null

if none has been set

---

#### public
JMenuBar
getJMenuBar()

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

**Returns:**
- the

JMenuBar

used by this internal frame

**See Also:**
- setJMenuBar(javax.swing.JMenuBar)

---

#### @Deprecated

public void setMenuBar​(
JMenuBar
m)

Sets the

menuBar

property for this

JInternalFrame

.

**Parameters:**
- m

- the

JMenuBar

to use in this internal frame

**See Also:**
- getJMenuBar()

---

#### @BeanProperty
(
preferred
=true,

description
="The menu bar for accessing pulldown menus from this internal frame.")
public void setJMenuBar​(
JMenuBar
m)

Sets the

menuBar

property for this

JInternalFrame

.

**Parameters:**
- m

- the

JMenuBar

to use in this internal frame

**See Also:**
- getJMenuBar()

---

#### public
Container
getContentPane()

Returns the content pane for this internal frame.

**Specified by:**
- getContentPane

in interface

RootPaneContainer

**Returns:**
- the content pane

**See Also:**
- RootPaneContainer.setContentPane(java.awt.Container)

---

#### @BeanProperty
(
hidden
=true,

description
="The client area of the internal frame where child components are normally inserted.")
public void setContentPane​(
Container
c)

Sets this

JInternalFrame

's

contentPane

property.

**Specified by:**
- setContentPane

in interface

RootPaneContainer

**Parameters:**
- c

- the content pane for this internal frame

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null

**See Also:**
- RootPaneContainer.getContentPane()

---

#### public
JLayeredPane
getLayeredPane()

Returns the layered pane for this internal frame.

**Specified by:**
- getLayeredPane

in interface

RootPaneContainer

**Returns:**
- a

JLayeredPane

object

**See Also:**
- RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

---

#### @BeanProperty
(
hidden
=true,

description
="The pane which holds the various desktop layers.")
public void setLayeredPane​(
JLayeredPane
layered)

Sets this

JInternalFrame

's

layeredPane

property.

**Specified by:**
- setLayeredPane

in interface

RootPaneContainer

**Parameters:**
- layered

- the

JLayeredPane

for this internal frame

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is

null

**See Also:**
- RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

---

#### public
Component
getGlassPane()

Returns the glass pane for this internal frame.

**Specified by:**
- getGlassPane

in interface

RootPaneContainer

**Returns:**
- the glass pane

**See Also:**
- RootPaneContainer.setGlassPane(java.awt.Component)

---

#### @BeanProperty
(
hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glass)

Sets this

JInternalFrame

's

glassPane

property.

**Specified by:**
- setGlassPane

in interface

RootPaneContainer

**Parameters:**
- glass

- the glass pane for this internal frame

**See Also:**
- RootPaneContainer.getGlassPane()

---

#### @BeanProperty
(
hidden
=true,

description
="The root pane used by this internal frame.")
public
JRootPane
getRootPane()

Returns the

rootPane

object for this internal frame.

**Specified by:**
- getRootPane

in interface

RootPaneContainer

**Overrides:**
- getRootPane

in class

JComponent

**Returns:**
- the

rootPane

property

**See Also:**
- RootPaneContainer.getRootPane()

---

#### protected void setRootPane​(
JRootPane
root)

Sets the

rootPane

property
for this

JInternalFrame

.
This method is called by the constructor.

**Parameters:**
- root

- the new

JRootPane

object

---

#### @BeanProperty
(
preferred
=true,

description
="Indicates whether this internal frame can be closed.")
public void setClosable​(boolean b)

Sets whether this

JInternalFrame

can be closed by
some user action.

**Parameters:**
- b

- a boolean value, where

true

means this internal frame can be closed

---

#### public boolean isClosable()

Returns whether this

JInternalFrame

can be closed by
some user action.

**Returns:**
- true

if this internal frame can be closed

---

#### public boolean isClosed()

Returns whether this

JInternalFrame

is currently closed.

**Returns:**
- true

if this internal frame is closed,

false

otherwise

---

#### @BeanProperty
(
description
="Indicates whether this internal frame has been closed.")
public void setClosed​(boolean b)
throws
PropertyVetoException

Closes this internal frame if the argument is

true

.
Do not invoke this method with a

false

argument;
the result of invoking

setClosed(false)

is unspecified.

If the internal frame is already closed,
this method does nothing and returns immediately.
Otherwise,
this method begins by firing
an

INTERNAL_FRAME_CLOSING

event.
Then this method sets the

closed

property to

true

unless a listener vetoes the property change.
This method finishes by making the internal frame
invisible and unselected,
and then firing an

INTERNAL_FRAME_CLOSED

event.

Note:

To reuse an internal frame that has been closed,
you must add it to a container
(even if you never removed it from its previous container).
Typically, this container will be the

JDesktopPane

that previously contained the internal frame.

**Parameters:**
- b

- must be

true

**Throws:**
- PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame

**See Also:**
- isClosed()

,

setDefaultCloseOperation(int)

,

dispose()

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

---

#### @BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be resized by the user.")
public void setResizable​(boolean b)

Sets whether the

JInternalFrame

can be resized by some
user action.

**Parameters:**
- b

- a boolean, where

true

means this internal frame can be resized

---

#### public boolean isResizable()

Returns whether the

JInternalFrame

can be resized
by some user action.

**Returns:**
- true

if this internal frame can be resized,

false

otherwise

---

#### @BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be iconified.")
public void setIconifiable​(boolean b)

Sets the

iconable

property,
which must be

true

for the user to be able to
make the

JInternalFrame

an icon.
Some look and feels might not implement iconification;
they will ignore this property.

**Parameters:**
- b

- a boolean, where

true

means this internal frame can be iconified

---

#### public boolean isIconifiable()

Gets the

iconable

property,
which by default is

false

.

**Returns:**
- the value of the

iconable

property.

**See Also:**
- setIconifiable(boolean)

---

#### public boolean isIcon()

Returns whether the

JInternalFrame

is currently iconified.

**Returns:**
- true

if this internal frame is iconified

---

#### @BeanProperty
(
description
="The image displayed when this internal frame is minimized.")
public void setIcon​(boolean b)
throws
PropertyVetoException

Iconifies or de-iconifies this internal frame,
if the look and feel supports iconification.
If the internal frame's state changes to iconified,
this method fires an

INTERNAL_FRAME_ICONIFIED

event.
If the state changes to de-iconified,
an

INTERNAL_FRAME_DEICONIFIED

event is fired.

**Parameters:**
- b

- a boolean, where

true

means to iconify this internal frame and

false

means to de-iconify it

**Throws:**
- PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame

**See Also:**
- InternalFrameEvent.INTERNAL_FRAME_ICONIFIED

,

InternalFrameEvent.INTERNAL_FRAME_DEICONIFIED

---

#### @BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be maximized.")
public void setMaximizable​(boolean b)

Sets the

maximizable

property,
which determines whether the

JInternalFrame

can be maximized by
some user action.
Some look and feels might not support maximizing internal frames;
they will ignore this property.

**Parameters:**
- b

-

true

to specify that this internal frame should be maximizable;

false

to specify that it should not be

---

#### public boolean isMaximizable()

Gets the value of the

maximizable

property.

**Returns:**
- the value of the

maximizable

property

**See Also:**
- setMaximizable(boolean)

---

#### public boolean isMaximum()

Returns whether the

JInternalFrame

is currently maximized.

**Returns:**
- true

if this internal frame is maximized,

false

otherwise

---

#### @BeanProperty
(
description
="Indicates whether this internal frame is maximized.")
public void setMaximum​(boolean b)
throws
PropertyVetoException

Maximizes and restores this internal frame. A maximized frame is resized to
fully fit the

JDesktopPane

area associated with the

JInternalFrame

.
A restored frame's size is set to the

JInternalFrame

's
actual size.

**Parameters:**
- b

- a boolean, where

true

maximizes this internal frame and

false

restores it

**Throws:**
- PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame

---

#### public
String
getTitle()

Returns the title of the

JInternalFrame

.

**Returns:**
- a

String

containing this internal frame's title

**See Also:**
- setTitle(java.lang.String)

---

#### @BeanProperty
(
preferred
=true,

description
="The text displayed in the title bar.")
public void setTitle​(
String
title)

Sets the

JInternalFrame

title.

title

may have a

null

value.

**Parameters:**
- title

- the

String

to display in the title bar

**See Also:**
- getTitle()

---

#### @BeanProperty
(
description
="Indicates whether this internal frame is currently the active frame.")
public void setSelected​(boolean selected)
throws
PropertyVetoException

Selects or deselects the internal frame
if it's showing.
A

JInternalFrame

normally draws its title bar
differently if it is
the selected frame, which indicates to the user that this
internal frame has the focus.
When this method changes the state of the internal frame
from deselected to selected, it fires an

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

event.
If the change is from selected to deselected,
an

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

event
is fired.

**Parameters:**
- selected

- a boolean, where

true

means this internal frame
should become selected (currently active)
and

false

means it should become deselected

**Throws:**
- PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame

**See Also:**
- Component.isShowing()

,

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

,

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

---

#### public boolean isSelected()

Returns whether the

JInternalFrame

is the
currently "selected" or active frame.

**Returns:**
- true

if this internal frame is currently selected (active)

**See Also:**
- setSelected(boolean)

---

#### @BeanProperty
(
description
="The icon shown in the top-left corner of this internal frame.")
public void setFrameIcon​(
Icon
icon)

Sets an image to be displayed in the titlebar of this internal frame (usually
in the top-left corner).
Some look and feels might not support displaying an icon in the titlebar.

This image is not the

desktopIcon

object, which
is the image displayed in the

JDesktop

when
this internal frame is iconified.

Passing

null

to this function is valid,
but the look and feel can choose the appropriate behavior
for that situation, such as displaying no icon
or a default icon for the look and feel.

**Parameters:**
- icon

- the

Icon

to display in the title bar

**See Also:**
- getFrameIcon()

---

#### public
Icon
getFrameIcon()

Returns the image displayed in the title bar of this internal frame (usually
in the top-left corner).

**Returns:**
- the

Icon

displayed in the title bar

**See Also:**
- setFrameIcon(javax.swing.Icon)

---

#### public void moveToFront()

Convenience method that moves this component to position 0 if its
parent is a

JLayeredPane

.

---

#### public void moveToBack()

Convenience method that moves this component to position -1 if its
parent is a

JLayeredPane

.

---

#### @BeanProperty
(
bound
=false)
public
Cursor
getLastCursor()

Returns the last

Cursor

that was set by the

setCursor

method that is not a resizable

Cursor

.

**Returns:**
- the last non-resizable

Cursor

**Since:**
- 1.6

---

#### public void setCursor​(
Cursor
cursor)

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

**Overrides:**
- setCursor

in class

Component

**Parameters:**
- cursor

- One of the constants defined
by the

Cursor

class;
if this parameter is

null

then this component will inherit
the cursor of its parent

**See Also:**
- Component.isEnabled()

,

Component.isShowing()

,

Component.getCursor()

,

Component.contains(int, int)

,

Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

,

Cursor

**Since:**
- 1.6

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="Specifies what desktop layer is used.")
public void setLayer​(
Integer
layer)

Convenience method for setting the layer attribute of this component.

**Parameters:**
- layer

- an

Integer

object specifying this
frame's desktop layer

**Throws:**
- NullPointerException

- if

layer

is

null

**See Also:**
- JLayeredPane

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="Specifies what desktop layer is used.")
public void setLayer​(int layer)

Convenience method for setting the layer attribute of this component.
The method

setLayer(Integer)

should be used for
layer values predefined in

JLayeredPane

.
When using

setLayer(int)

, care must be taken not to
accidentally clash with those values.

**Parameters:**
- layer

- an integer specifying this internal frame's desktop layer

**See Also:**
- setLayer(Integer)

,

JLayeredPane

**Since:**
- 1.3

---

#### public int getLayer()

Convenience method for getting the layer attribute of this component.

**Returns:**
- an

Integer

object specifying this
frame's desktop layer

**See Also:**
- JLayeredPane

---

#### @BeanProperty
(
bound
=false)
public
JDesktopPane
getDesktopPane()

Convenience method that searches the ancestor hierarchy for a

JDesktop

instance. If

JInternalFrame

finds none, the

desktopIcon

tree is searched.

**Returns:**
- the

JDesktopPane

this internal frame belongs to,
or

null

if none is found

---

#### @BeanProperty
(
description
="The icon shown when this internal frame is minimized.")
public void setDesktopIcon​(
JInternalFrame.JDesktopIcon
d)

Sets the

JDesktopIcon

associated with this

JInternalFrame

.

**Parameters:**
- d

- the

JDesktopIcon

to display on the desktop

**See Also:**
- getDesktopIcon()

---

#### public
JInternalFrame.JDesktopIcon
getDesktopIcon()

Returns the

JDesktopIcon

used when this

JInternalFrame

is iconified.

**Returns:**
- the

JDesktopIcon

displayed on the desktop

**See Also:**
- setDesktopIcon(javax.swing.JInternalFrame.JDesktopIcon)

---

#### public
Rectangle
getNormalBounds()

If the

JInternalFrame

is not in maximized state, returns

getBounds()

; otherwise, returns the bounds that the

JInternalFrame

would be restored to.

**Returns:**
- a

Rectangle

containing the bounds of this
frame when in the normal state

**Since:**
- 1.3

---

#### public void setNormalBounds​(
Rectangle
r)

Sets the normal bounds for this internal frame, the bounds that
this internal frame would be restored to from its maximized state.
This method is intended for use only by desktop managers.

**Parameters:**
- r

- the bounds that this internal frame should be restored to

**Since:**
- 1.3

---

#### public
Component
getFocusOwner()

If this

JInternalFrame

is active,
returns the child that has focus.
Otherwise, returns

null

.

**Returns:**
- the component with focus, or

null

if no children have focus

**Since:**
- 1.3

---

#### @BeanProperty
(
bound
=false)
public
Component
getMostRecentFocusOwner()

Returns the child component of this

JInternalFrame

that will receive the
focus when this

JInternalFrame

is selected.
If this

JInternalFrame

is
currently selected, this method returns the same component as
the

getFocusOwner

method.
If this

JInternalFrame

is not selected,
then the child component that most recently requested focus will be
returned. If no child component has ever requested focus, then this

JInternalFrame

's initial focusable component is returned.
If no such
child exists, then this

JInternalFrame

's default component
to focus is returned.

**Returns:**
- the child component that will receive focus when this

JInternalFrame

is selected

**See Also:**
- getFocusOwner()

,

isSelected

**Since:**
- 1.4

---

#### public void restoreSubcomponentFocus()

Requests the internal frame to restore focus to the
last subcomponent that had focus. This is used by the UI when
the user selected this internal frame --
for example, by clicking on the title bar.

**Since:**
- 1.3

---

#### public void reshape​(int x,
int y,
int width,
int height)

Moves and resizes this component. Unlike other components,
this implementation also forces re-layout, so that frame
decorations such as the title bar are always redisplayed.

**Overrides:**
- reshape

in class

JComponent

**Parameters:**
- x

- an integer giving the component's new horizontal position
measured in pixels from the left of its container
- y

- an integer giving the component's new vertical position,
measured in pixels from the bottom of its container
- width

- an integer giving the component's new width in pixels
- height

- an integer giving the component's new height in pixels

**See Also:**
- Component.setBounds(int, int, int, int)

---

#### public void addInternalFrameListener​(
InternalFrameListener
l)

Adds the specified listener to receive internal
frame events from this internal frame.

**Parameters:**
- l

- the internal frame listener

---

#### public void removeInternalFrameListener​(
InternalFrameListener
l)

Removes the specified internal frame listener so that it no longer
receives internal frame events from this internal frame.

**Parameters:**
- l

- the internal frame listener

---

#### @BeanProperty
(
bound
=false)
public
InternalFrameListener
[] getInternalFrameListeners()

Returns an array of all the

InternalFrameListener

s added
to this

JInternalFrame

with

addInternalFrameListener

.

**Returns:**
- all of the

InternalFrameListener

s added or an empty
array if no listeners have been added

**See Also:**
- addInternalFrameListener(javax.swing.event.InternalFrameListener)

**Since:**
- 1.4

---

#### protected void fireInternalFrameEvent​(int id)

Fires an internal frame event.

**Parameters:**
- id

- the type of the event being fired; one of the following:

- InternalFrameEvent.INTERNAL_FRAME_OPENED

InternalFrameEvent.INTERNAL_FRAME_CLOSING

InternalFrameEvent.INTERNAL_FRAME_CLOSED

InternalFrameEvent.INTERNAL_FRAME_ICONIFIED

InternalFrameEvent.INTERNAL_FRAME_DEICONIFIED

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

If the event type is not one of the above, nothing happens.

---

#### public void doDefaultCloseAction()

Fires an

INTERNAL_FRAME_CLOSING

event
and then performs the action specified by
the internal frame's default close operation.
This method is typically invoked by the
look-and-feel-implemented action handler
for the internal frame's close button.

**See Also:**
- setDefaultCloseOperation(int)

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

**Since:**
- 1.3

---

#### public void setDefaultCloseOperation​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this internal frame.
The possible choices are:

The default value is

DISPOSE_ON_CLOSE

.
Before performing the specified close operation,
the internal frame fires
an

INTERNAL_FRAME_CLOSING

event.

---

#### public int getDefaultCloseOperation()

Returns the default operation that occurs when the user
initiates a "close" on this internal frame.

**Returns:**
- the operation that will occur when the user closes the internal
frame

**See Also:**
- setDefaultCloseOperation(int)

---

#### public void pack()

Causes subcomponents of this

JInternalFrame

to be laid out at their preferred size. Internal frames that are
iconized or maximized are first restored and then packed. If the
internal frame is unable to be restored its state is not changed
and will not be packed.

**See Also:**
- Window.pack()

---

#### public void show()

If the internal frame is not visible,
brings the internal frame to the front,
makes it visible,
and attempts to select it.
The first time the internal frame is made visible,
this method also fires an

INTERNAL_FRAME_OPENED

event.
This method does nothing if the internal frame is already visible.
Invoking this method
has the same result as invoking

setVisible(true)

.

**Overrides:**
- show

in class

Component

**See Also:**
- moveToFront()

,

setSelected(boolean)

,

InternalFrameEvent.INTERNAL_FRAME_OPENED

,

JComponent.setVisible(boolean)

---

#### public void dispose()

Makes this internal frame
invisible, unselected, and closed.
If the frame is not already closed,
this method fires an

INTERNAL_FRAME_CLOSED

event.
The results of invoking this method are similar to

setClosed(true)

,
but

dispose

always succeeds in closing
the internal frame and does not fire
an

INTERNAL_FRAME_CLOSING

event.

**See Also:**
- InternalFrameEvent.INTERNAL_FRAME_CLOSED

,

JComponent.setVisible(boolean)

,

setSelected(boolean)

,

setClosed(boolean)

---

#### public void toFront()

Brings this internal frame to the front.
Places this internal frame at the top of the stacking order
and makes the corresponding adjustment to other visible internal
frames.

**See Also:**
- Window.toFront()

,

moveToFront()

---

#### public void toBack()

Sends this internal frame to the back.
Places this internal frame at the bottom of the stacking order
and makes the corresponding adjustment to other visible
internal frames.

**See Also:**
- Window.toBack()

,

moveToBack()

---

#### public final void setFocusCycleRoot​(boolean focusCycleRoot)

Does nothing because

JInternalFrame

s must always be roots of a focus
traversal cycle.

**Overrides:**
- setFocusCycleRoot

in class

Container

**Parameters:**
- focusCycleRoot

- this value is ignored

**See Also:**
- isFocusCycleRoot()

,

Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

Container.getFocusTraversalPolicy()

**Since:**
- 1.4

---

#### public final boolean isFocusCycleRoot()

Always returns

true

because all

JInternalFrame

s must be
roots of a focus traversal cycle.

**Overrides:**
- isFocusCycleRoot

in class

Container

**Returns:**
- true

**See Also:**
- setFocusCycleRoot(boolean)

,

Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

Container.getFocusTraversalPolicy()

**Since:**
- 1.4

---

#### @BeanProperty
(
bound
=false)
public final
Container
getFocusCycleRootAncestor()

Always returns

null

because

JInternalFrame

s
must always be roots of a focus
traversal cycle.

**Overrides:**
- getFocusCycleRootAncestor

in class

Component

**Returns:**
- null

**See Also:**
- Container.isFocusCycleRoot()

**Since:**
- 1.4

---

#### @BeanProperty
(
bound
=false)
public final
String
getWarningString()

Gets the warning string that is displayed with this internal frame.
Since an internal frame is always secure (since it's fully
contained within a window that might need a warning string)
this method always returns

null

.

**Returns:**
- null

**See Also:**
- Window.getWarningString()

---

#### protected
String
paramString()

Returns a string representation of this

JInternalFrame

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

JInternalFrame

---

#### protected void paintComponent​(
Graphics
g)

Overridden to allow optimized painting when the
internal frame is being dragged.

**Overrides:**
- paintComponent

in class

JComponent

**Parameters:**
- g

- the

Graphics

object to protect

**See Also:**
- JComponent.paint(java.awt.Graphics)

,

ComponentUI

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

associated with this

JInternalFrame

.
For internal frames, the

AccessibleContext

takes the form of an

AccessibleJInternalFrame

object.
A new

AccessibleJInternalFrame

instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an

AccessibleJInternalFrame

that serves as the

AccessibleContext

of this

JInternalFrame

**See Also:**
- JInternalFrame.AccessibleJInternalFrame

---

### Additional Sections

#### Class JInternalFrame

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JInternalFrame

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JInternalFrame

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JInternalFrame

javax.swing.JComponent

- javax.swing.JInternalFrame

javax.swing.JInternalFrame

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

RootPaneContainer

,

WindowConstants

```java
@JavaBean
(
defaultProperty
="JMenuBar",

description
="A frame container which is contained within another window.")
public class
JInternalFrame

extends
JComponent

implements
Accessible
,
WindowConstants
,
RootPaneContainer
```

A lightweight object that provides many of the features of
a native frame, including dragging, closing, becoming an icon,
resizing, title display, and support for a menu bar.
For task-oriented documentation and examples of using internal frames,
see

How to Use Internal Frames

,
a section in

The Java Tutorial

.

Generally,
you add

JInternalFrame

s to a

JDesktopPane

. The UI
delegates the look-and-feel-specific actions to the

DesktopManager

object maintained by the

JDesktopPane

.

The

JInternalFrame

content pane
is where you add child components.
As a convenience, the

add

,

remove

, and

setLayout

methods of this class are overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to an internal frame as follows:

```java
internalFrame.add(child);
```

And the child will be added to the contentPane.
The content pane is actually managed by an instance of

JRootPane

,
which also manages a layout pane, glass pane, and
optional menu bar for the internal frame. Please see the

JRootPane

documentation for a complete description of these components.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JInternalFrame

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

**Since:** 1.2
**See Also:** InternalFrameEvent

,

JDesktopPane

,

DesktopManager

,

JInternalFrame.JDesktopIcon

,

JRootPane

,

RootPaneContainer

,

Serialized Form

@JavaBean

(

defaultProperty

="JMenuBar",

description

="A frame container which is contained within another window.")
public class

JInternalFrame

extends

JComponent

implements

Accessible

,

WindowConstants

,

RootPaneContainer

A lightweight object that provides many of the features of
a native frame, including dragging, closing, becoming an icon,
resizing, title display, and support for a menu bar.
For task-oriented documentation and examples of using internal frames,
see

How to Use Internal Frames

,
a section in

The Java Tutorial

.

Generally,
you add

JInternalFrame

s to a

JDesktopPane

. The UI
delegates the look-and-feel-specific actions to the

DesktopManager

object maintained by the

JDesktopPane

.

The

JInternalFrame

content pane
is where you add child components.
As a convenience, the

add

,

remove

, and

setLayout

methods of this class are overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to an internal frame as follows:

```java
internalFrame.add(child);
```

And the child will be added to the contentPane.
The content pane is actually managed by an instance of

JRootPane

,
which also manages a layout pane, glass pane, and
optional menu bar for the internal frame. Please see the

JRootPane

documentation for a complete description of these components.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JInternalFrame

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

Generally,
you add

JInternalFrame

s to a

JDesktopPane

. The UI
delegates the look-and-feel-specific actions to the

DesktopManager

object maintained by the

JDesktopPane

.

The

JInternalFrame

content pane
is where you add child components.
As a convenience, the

add

,

remove

, and

setLayout

methods of this class are overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to an internal frame as follows:

```java
internalFrame.add(child);
```

And the child will be added to the contentPane.
The content pane is actually managed by an instance of

JRootPane

,
which also manages a layout pane, glass pane, and
optional menu bar for the internal frame. Please see the

JRootPane

documentation for a complete description of these components.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JInternalFrame

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

The

JInternalFrame

content pane
is where you add child components.
As a convenience, the

add

,

remove

, and

setLayout

methods of this class are overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to an internal frame as follows:

```java
internalFrame.add(child);
```

And the child will be added to the contentPane.
The content pane is actually managed by an instance of

JRootPane

,
which also manages a layout pane, glass pane, and
optional menu bar for the internal frame. Please see the

JRootPane

documentation for a complete description of these components.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JInternalFrame

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

internalFrame.add(child);

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

JInternalFrame.AccessibleJInternalFrame

This class implements accessibility support for the

JInternalFrame

class.

static class

JInternalFrame.JDesktopIcon

This component represents an iconified version of a

JInternalFrame

.

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

protected boolean

closable

The frame can be closed.

static

String

CONTENT_PANE_PROPERTY

Bound property name.

protected

JInternalFrame.JDesktopIcon

desktopIcon

The icon that is displayed when this internal frame is iconified.

static

String

FRAME_ICON_PROPERTY

Bound property name.

protected

Icon

frameIcon

The icon shown in the top-left corner of this internal frame.

static

String

GLASS_PANE_PROPERTY

Bound property name.

protected boolean

iconable

The frame can "iconified" (shrunk down and displayed as
an icon-image).

static

String

IS_CLOSED_PROPERTY

Constrained property name indicating that the internal frame is closed.

static

String

IS_ICON_PROPERTY

Constrained property name indicating that the internal frame is iconified.

static

String

IS_MAXIMUM_PROPERTY

Constrained property name indicating that the internal frame is maximized.

static

String

IS_SELECTED_PROPERTY

Constrained property name indicated that this frame has
selected status.

protected boolean

isClosed

The frame has been closed.

protected boolean

isIcon

The frame has been iconified.

protected boolean

isMaximum

The frame has been expanded to its maximum size.

protected boolean

isSelected

The frame is currently selected.

static

String

LAYERED_PANE_PROPERTY

Bound property name.

protected boolean

maximizable

The frame can be expanded to the size of the desktop pane.

static

String

MENU_BAR_PROPERTY

Bound property name.

protected boolean

resizable

The frame's size can be changed.

static

String

ROOT_PANE_PROPERTY

Bound property name.

protected

JRootPane

rootPane

The

JRootPane

instance that manages the
content pane
and optional menu bar for this internal frame, as well as the
glass pane.

protected boolean

rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

protected

String

title

The title displayed in this internal frame's title bar.

static

String

TITLE_PROPERTY

Bound property name.

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

WindowConstants

DISPOSE_ON_CLOSE

,

DO_NOTHING_ON_CLOSE

,

EXIT_ON_CLOSE

,

HIDE_ON_CLOSE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JInternalFrame

()

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with no title.

JInternalFrame

​(

String

title)

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with the specified title.

JInternalFrame

​(

String

title,
boolean resizable)

Creates a non-closable, non-maximizable, non-iconifiable

JInternalFrame

with the specified title
and resizability.

JInternalFrame

​(

String

title,
boolean resizable,
boolean closable)

Creates a non-maximizable, non-iconifiable

JInternalFrame

with the specified title, resizability, and
closability.

JInternalFrame

​(

String

title,
boolean resizable,
boolean closable,
boolean maximizable)

Creates a non-iconifiable

JInternalFrame

with the specified title,
resizability, closability, and maximizability.

JInternalFrame

​(

String

title,
boolean resizable,
boolean closable,
boolean maximizable,
boolean iconifiable)

Creates a

JInternalFrame

with the specified title,
resizability, closability, maximizability, and iconifiability.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

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

Adds the specified child

Component

.

void

addInternalFrameListener

​(

InternalFrameListener

l)

Adds the specified listener to receive internal
frame events from this internal frame.

protected

JRootPane

createRootPane

()

Called by the constructor to set up the

JRootPane

.

void

dispose

()

Makes this internal frame
invisible, unselected, and closed.

void

doDefaultCloseAction

()

Fires an

INTERNAL_FRAME_CLOSING

event
and then performs the action specified by
the internal frame's default close operation.

protected void

fireInternalFrameEvent

​(int id)

Fires an internal frame event.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

JInternalFrame

.

Container

getContentPane

()

Returns the content pane for this internal frame.

int

getDefaultCloseOperation

()

Returns the default operation that occurs when the user
initiates a "close" on this internal frame.

JInternalFrame.JDesktopIcon

getDesktopIcon

()

Returns the

JDesktopIcon

used when this

JInternalFrame

is iconified.

JDesktopPane

getDesktopPane

()

Convenience method that searches the ancestor hierarchy for a

JDesktop

instance.

Container

getFocusCycleRootAncestor

()

Always returns

null

because

JInternalFrame

s
must always be roots of a focus
traversal cycle.

Component

getFocusOwner

()

If this

JInternalFrame

is active,
returns the child that has focus.

Icon

getFrameIcon

()

Returns the image displayed in the title bar of this internal frame (usually
in the top-left corner).

Component

getGlassPane

()

Returns the glass pane for this internal frame.

InternalFrameListener

[]

getInternalFrameListeners

()

Returns an array of all the

InternalFrameListener

s added
to this

JInternalFrame

with

addInternalFrameListener

.

JMenuBar

getJMenuBar

()

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

Cursor

getLastCursor

()

Returns the last

Cursor

that was set by the

setCursor

method that is not a resizable

Cursor

.

int

getLayer

()

Convenience method for getting the layer attribute of this component.

JLayeredPane

getLayeredPane

()

Returns the layered pane for this internal frame.

JMenuBar

getMenuBar

()

Deprecated.

As of Swing version 1.0.3,
replaced by

getJMenuBar()

.

Component

getMostRecentFocusOwner

()

Returns the child component of this

JInternalFrame

that will receive the
focus when this

JInternalFrame

is selected.

Rectangle

getNormalBounds

()

If the

JInternalFrame

is not in maximized state, returns

getBounds()

; otherwise, returns the bounds that the

JInternalFrame

would be restored to.

JRootPane

getRootPane

()

Returns the

rootPane

object for this internal frame.

String

getTitle

()

Returns the title of the

JInternalFrame

.

InternalFrameUI

getUI

()

Returns the look-and-feel object that renders this component.

String

getUIClassID

()

Returns the name of the look-and-feel
class that renders this component.

String

getWarningString

()

Gets the warning string that is displayed with this internal frame.

boolean

isClosable

()

Returns whether this

JInternalFrame

can be closed by
some user action.

boolean

isClosed

()

Returns whether this

JInternalFrame

is currently closed.

boolean

isFocusCycleRoot

()

Always returns

true

because all

JInternalFrame

s must be
roots of a focus traversal cycle.

boolean

isIcon

()

Returns whether the

JInternalFrame

is currently iconified.

boolean

isIconifiable

()

Gets the

iconable

property,
which by default is

false

.

boolean

isMaximizable

()

Gets the value of the

maximizable

property.

boolean

isMaximum

()

Returns whether the

JInternalFrame

is currently maximized.

boolean

isResizable

()

Returns whether the

JInternalFrame

can be resized
by some user action.

protected boolean

isRootPaneCheckingEnabled

()

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

boolean

isSelected

()

Returns whether the

JInternalFrame

is the
currently "selected" or active frame.

void

moveToBack

()

Convenience method that moves this component to position -1 if its
parent is a

JLayeredPane

.

void

moveToFront

()

Convenience method that moves this component to position 0 if its
parent is a

JLayeredPane

.

void

pack

()

Causes subcomponents of this

JInternalFrame

to be laid out at their preferred size.

protected void

paintComponent

​(

Graphics

g)

Overridden to allow optimized painting when the
internal frame is being dragged.

protected

String

paramString

()

Returns a string representation of this

JInternalFrame

.

void

remove

​(

Component

comp)

Removes the specified component from the container.

void

removeInternalFrameListener

​(

InternalFrameListener

l)

Removes the specified internal frame listener so that it no longer
receives internal frame events from this internal frame.

void

reshape

​(int x,
int y,
int width,
int height)

Moves and resizes this component.

void

restoreSubcomponentFocus

()

Requests the internal frame to restore focus to the
last subcomponent that had focus.

void

setClosable

​(boolean b)

Sets whether this

JInternalFrame

can be closed by
some user action.

void

setClosed

​(boolean b)

Closes this internal frame if the argument is

true

.

void

setContentPane

​(

Container

c)

Sets this

JInternalFrame

's

contentPane

property.

void

setCursor

​(

Cursor

cursor)

Sets the cursor image to the specified cursor.

void

setDefaultCloseOperation

​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this internal frame.

void

setDesktopIcon

​(

JInternalFrame.JDesktopIcon

d)

Sets the

JDesktopIcon

associated with this

JInternalFrame

.

void

setFocusCycleRoot

​(boolean focusCycleRoot)

Does nothing because

JInternalFrame

s must always be roots of a focus
traversal cycle.

void

setFrameIcon

​(

Icon

icon)

Sets an image to be displayed in the titlebar of this internal frame (usually
in the top-left corner).

void

setGlassPane

​(

Component

glass)

Sets this

JInternalFrame

's

glassPane

property.

void

setIcon

​(boolean b)

Iconifies or de-iconifies this internal frame,
if the look and feel supports iconification.

void

setIconifiable

​(boolean b)

Sets the

iconable

property,
which must be

true

for the user to be able to
make the

JInternalFrame

an icon.

void

setJMenuBar

​(

JMenuBar

m)

Sets the

menuBar

property for this

JInternalFrame

.

void

setLayer

​(int layer)

Convenience method for setting the layer attribute of this component.

void

setLayer

​(

Integer

layer)

Convenience method for setting the layer attribute of this component.

void

setLayeredPane

​(

JLayeredPane

layered)

Sets this

JInternalFrame

's

layeredPane

property.

void

setLayout

​(

LayoutManager

manager)

Ensures that, by default, the layout of this component cannot be set.

void

setMaximizable

​(boolean b)

Sets the

maximizable

property,
which determines whether the

JInternalFrame

can be maximized by
some user action.

void

setMaximum

​(boolean b)

Maximizes and restores this internal frame.

void

setMenuBar

​(

JMenuBar

m)

Deprecated.

As of Swing version 1.0.3
replaced by

setJMenuBar(JMenuBar m)

.

void

setNormalBounds

​(

Rectangle

r)

Sets the normal bounds for this internal frame, the bounds that
this internal frame would be restored to from its maximized state.

void

setResizable

​(boolean b)

Sets whether the

JInternalFrame

can be resized by some
user action.

protected void

setRootPane

​(

JRootPane

root)

Sets the

rootPane

property
for this

JInternalFrame

.

protected void

setRootPaneCheckingEnabled

​(boolean enabled)

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

void

setSelected

​(boolean selected)

Selects or deselects the internal frame
if it's showing.

void

setTitle

​(

String

title)

Sets the

JInternalFrame

title.

void

setUI

​(

InternalFrameUI

ui)

Sets the UI delegate for this

JInternalFrame

.

void

show

()

If the internal frame is not visible,
brings the internal frame to the front,
makes it visible,
and attempts to select it.

void

toBack

()

Sends this internal frame to the back.

void

toFront

()

Brings this internal frame to the front.

void

updateUI

()

Notification from the

UIManager

that the look and feel
has changed.

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

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

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

removeAll

,

removeContainerListener

,

setComponentZOrder

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

JInternalFrame.AccessibleJInternalFrame

This class implements accessibility support for the

JInternalFrame

class.

static class

JInternalFrame.JDesktopIcon

This component represents an iconified version of a

JInternalFrame

.

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

JInternalFrame

class.

This component represents an iconified version of a

JInternalFrame

.

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

protected boolean

closable

The frame can be closed.

static

String

CONTENT_PANE_PROPERTY

Bound property name.

protected

JInternalFrame.JDesktopIcon

desktopIcon

The icon that is displayed when this internal frame is iconified.

static

String

FRAME_ICON_PROPERTY

Bound property name.

protected

Icon

frameIcon

The icon shown in the top-left corner of this internal frame.

static

String

GLASS_PANE_PROPERTY

Bound property name.

protected boolean

iconable

The frame can "iconified" (shrunk down and displayed as
an icon-image).

static

String

IS_CLOSED_PROPERTY

Constrained property name indicating that the internal frame is closed.

static

String

IS_ICON_PROPERTY

Constrained property name indicating that the internal frame is iconified.

static

String

IS_MAXIMUM_PROPERTY

Constrained property name indicating that the internal frame is maximized.

static

String

IS_SELECTED_PROPERTY

Constrained property name indicated that this frame has
selected status.

protected boolean

isClosed

The frame has been closed.

protected boolean

isIcon

The frame has been iconified.

protected boolean

isMaximum

The frame has been expanded to its maximum size.

protected boolean

isSelected

The frame is currently selected.

static

String

LAYERED_PANE_PROPERTY

Bound property name.

protected boolean

maximizable

The frame can be expanded to the size of the desktop pane.

static

String

MENU_BAR_PROPERTY

Bound property name.

protected boolean

resizable

The frame's size can be changed.

static

String

ROOT_PANE_PROPERTY

Bound property name.

protected

JRootPane

rootPane

The

JRootPane

instance that manages the
content pane
and optional menu bar for this internal frame, as well as the
glass pane.

protected boolean

rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

protected

String

title

The title displayed in this internal frame's title bar.

static

String

TITLE_PROPERTY

Bound property name.

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

WindowConstants

DISPOSE_ON_CLOSE

,

DO_NOTHING_ON_CLOSE

,

EXIT_ON_CLOSE

,

HIDE_ON_CLOSE

---

#### Field Summary

The frame can be closed.

Bound property name.

The icon that is displayed when this internal frame is iconified.

The icon shown in the top-left corner of this internal frame.

The frame can "iconified" (shrunk down and displayed as
an icon-image).

Constrained property name indicating that the internal frame is closed.

Constrained property name indicating that the internal frame is iconified.

Constrained property name indicating that the internal frame is maximized.

Constrained property name indicated that this frame has
selected status.

The frame has been closed.

The frame has been iconified.

The frame has been expanded to its maximum size.

The frame is currently selected.

The frame can be expanded to the size of the desktop pane.

The frame's size can be changed.

The

JRootPane

instance that manages the
content pane
and optional menu bar for this internal frame, as well as the
glass pane.

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

The title displayed in this internal frame's title bar.

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

WindowConstants

DISPOSE_ON_CLOSE

,

DO_NOTHING_ON_CLOSE

,

EXIT_ON_CLOSE

,

HIDE_ON_CLOSE

---

#### Fields declared in interface javax.swing. WindowConstants

Constructor Summary

Constructors

Constructor

Description

JInternalFrame

()

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with no title.

JInternalFrame

​(

String

title)

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with the specified title.

JInternalFrame

​(

String

title,
boolean resizable)

Creates a non-closable, non-maximizable, non-iconifiable

JInternalFrame

with the specified title
and resizability.

JInternalFrame

​(

String

title,
boolean resizable,
boolean closable)

Creates a non-maximizable, non-iconifiable

JInternalFrame

with the specified title, resizability, and
closability.

JInternalFrame

​(

String

title,
boolean resizable,
boolean closable,
boolean maximizable)

Creates a non-iconifiable

JInternalFrame

with the specified title,
resizability, closability, and maximizability.

JInternalFrame

​(

String

title,
boolean resizable,
boolean closable,
boolean maximizable,
boolean iconifiable)

Creates a

JInternalFrame

with the specified title,
resizability, closability, maximizability, and iconifiability.

---

#### Constructor Summary

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with no title.

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with the specified title.

Creates a non-closable, non-maximizable, non-iconifiable

JInternalFrame

with the specified title
and resizability.

Creates a non-maximizable, non-iconifiable

JInternalFrame

with the specified title, resizability, and
closability.

Creates a non-iconifiable

JInternalFrame

with the specified title,
resizability, closability, and maximizability.

Creates a

JInternalFrame

with the specified title,
resizability, closability, maximizability, and iconifiability.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

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

Adds the specified child

Component

.

void

addInternalFrameListener

​(

InternalFrameListener

l)

Adds the specified listener to receive internal
frame events from this internal frame.

protected

JRootPane

createRootPane

()

Called by the constructor to set up the

JRootPane

.

void

dispose

()

Makes this internal frame
invisible, unselected, and closed.

void

doDefaultCloseAction

()

Fires an

INTERNAL_FRAME_CLOSING

event
and then performs the action specified by
the internal frame's default close operation.

protected void

fireInternalFrameEvent

​(int id)

Fires an internal frame event.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

JInternalFrame

.

Container

getContentPane

()

Returns the content pane for this internal frame.

int

getDefaultCloseOperation

()

Returns the default operation that occurs when the user
initiates a "close" on this internal frame.

JInternalFrame.JDesktopIcon

getDesktopIcon

()

Returns the

JDesktopIcon

used when this

JInternalFrame

is iconified.

JDesktopPane

getDesktopPane

()

Convenience method that searches the ancestor hierarchy for a

JDesktop

instance.

Container

getFocusCycleRootAncestor

()

Always returns

null

because

JInternalFrame

s
must always be roots of a focus
traversal cycle.

Component

getFocusOwner

()

If this

JInternalFrame

is active,
returns the child that has focus.

Icon

getFrameIcon

()

Returns the image displayed in the title bar of this internal frame (usually
in the top-left corner).

Component

getGlassPane

()

Returns the glass pane for this internal frame.

InternalFrameListener

[]

getInternalFrameListeners

()

Returns an array of all the

InternalFrameListener

s added
to this

JInternalFrame

with

addInternalFrameListener

.

JMenuBar

getJMenuBar

()

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

Cursor

getLastCursor

()

Returns the last

Cursor

that was set by the

setCursor

method that is not a resizable

Cursor

.

int

getLayer

()

Convenience method for getting the layer attribute of this component.

JLayeredPane

getLayeredPane

()

Returns the layered pane for this internal frame.

JMenuBar

getMenuBar

()

Deprecated.

As of Swing version 1.0.3,
replaced by

getJMenuBar()

.

Component

getMostRecentFocusOwner

()

Returns the child component of this

JInternalFrame

that will receive the
focus when this

JInternalFrame

is selected.

Rectangle

getNormalBounds

()

If the

JInternalFrame

is not in maximized state, returns

getBounds()

; otherwise, returns the bounds that the

JInternalFrame

would be restored to.

JRootPane

getRootPane

()

Returns the

rootPane

object for this internal frame.

String

getTitle

()

Returns the title of the

JInternalFrame

.

InternalFrameUI

getUI

()

Returns the look-and-feel object that renders this component.

String

getUIClassID

()

Returns the name of the look-and-feel
class that renders this component.

String

getWarningString

()

Gets the warning string that is displayed with this internal frame.

boolean

isClosable

()

Returns whether this

JInternalFrame

can be closed by
some user action.

boolean

isClosed

()

Returns whether this

JInternalFrame

is currently closed.

boolean

isFocusCycleRoot

()

Always returns

true

because all

JInternalFrame

s must be
roots of a focus traversal cycle.

boolean

isIcon

()

Returns whether the

JInternalFrame

is currently iconified.

boolean

isIconifiable

()

Gets the

iconable

property,
which by default is

false

.

boolean

isMaximizable

()

Gets the value of the

maximizable

property.

boolean

isMaximum

()

Returns whether the

JInternalFrame

is currently maximized.

boolean

isResizable

()

Returns whether the

JInternalFrame

can be resized
by some user action.

protected boolean

isRootPaneCheckingEnabled

()

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

boolean

isSelected

()

Returns whether the

JInternalFrame

is the
currently "selected" or active frame.

void

moveToBack

()

Convenience method that moves this component to position -1 if its
parent is a

JLayeredPane

.

void

moveToFront

()

Convenience method that moves this component to position 0 if its
parent is a

JLayeredPane

.

void

pack

()

Causes subcomponents of this

JInternalFrame

to be laid out at their preferred size.

protected void

paintComponent

​(

Graphics

g)

Overridden to allow optimized painting when the
internal frame is being dragged.

protected

String

paramString

()

Returns a string representation of this

JInternalFrame

.

void

remove

​(

Component

comp)

Removes the specified component from the container.

void

removeInternalFrameListener

​(

InternalFrameListener

l)

Removes the specified internal frame listener so that it no longer
receives internal frame events from this internal frame.

void

reshape

​(int x,
int y,
int width,
int height)

Moves and resizes this component.

void

restoreSubcomponentFocus

()

Requests the internal frame to restore focus to the
last subcomponent that had focus.

void

setClosable

​(boolean b)

Sets whether this

JInternalFrame

can be closed by
some user action.

void

setClosed

​(boolean b)

Closes this internal frame if the argument is

true

.

void

setContentPane

​(

Container

c)

Sets this

JInternalFrame

's

contentPane

property.

void

setCursor

​(

Cursor

cursor)

Sets the cursor image to the specified cursor.

void

setDefaultCloseOperation

​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this internal frame.

void

setDesktopIcon

​(

JInternalFrame.JDesktopIcon

d)

Sets the

JDesktopIcon

associated with this

JInternalFrame

.

void

setFocusCycleRoot

​(boolean focusCycleRoot)

Does nothing because

JInternalFrame

s must always be roots of a focus
traversal cycle.

void

setFrameIcon

​(

Icon

icon)

Sets an image to be displayed in the titlebar of this internal frame (usually
in the top-left corner).

void

setGlassPane

​(

Component

glass)

Sets this

JInternalFrame

's

glassPane

property.

void

setIcon

​(boolean b)

Iconifies or de-iconifies this internal frame,
if the look and feel supports iconification.

void

setIconifiable

​(boolean b)

Sets the

iconable

property,
which must be

true

for the user to be able to
make the

JInternalFrame

an icon.

void

setJMenuBar

​(

JMenuBar

m)

Sets the

menuBar

property for this

JInternalFrame

.

void

setLayer

​(int layer)

Convenience method for setting the layer attribute of this component.

void

setLayer

​(

Integer

layer)

Convenience method for setting the layer attribute of this component.

void

setLayeredPane

​(

JLayeredPane

layered)

Sets this

JInternalFrame

's

layeredPane

property.

void

setLayout

​(

LayoutManager

manager)

Ensures that, by default, the layout of this component cannot be set.

void

setMaximizable

​(boolean b)

Sets the

maximizable

property,
which determines whether the

JInternalFrame

can be maximized by
some user action.

void

setMaximum

​(boolean b)

Maximizes and restores this internal frame.

void

setMenuBar

​(

JMenuBar

m)

Deprecated.

As of Swing version 1.0.3
replaced by

setJMenuBar(JMenuBar m)

.

void

setNormalBounds

​(

Rectangle

r)

Sets the normal bounds for this internal frame, the bounds that
this internal frame would be restored to from its maximized state.

void

setResizable

​(boolean b)

Sets whether the

JInternalFrame

can be resized by some
user action.

protected void

setRootPane

​(

JRootPane

root)

Sets the

rootPane

property
for this

JInternalFrame

.

protected void

setRootPaneCheckingEnabled

​(boolean enabled)

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

void

setSelected

​(boolean selected)

Selects or deselects the internal frame
if it's showing.

void

setTitle

​(

String

title)

Sets the

JInternalFrame

title.

void

setUI

​(

InternalFrameUI

ui)

Sets the UI delegate for this

JInternalFrame

.

void

show

()

If the internal frame is not visible,
brings the internal frame to the front,
makes it visible,
and attempts to select it.

void

toBack

()

Sends this internal frame to the back.

void

toFront

()

Brings this internal frame to the front.

void

updateUI

()

Notification from the

UIManager

that the look and feel
has changed.

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

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

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

removeAll

,

removeContainerListener

,

setComponentZOrder

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

Adds the specified child

Component

.

Adds the specified listener to receive internal
frame events from this internal frame.

Called by the constructor to set up the

JRootPane

.

Makes this internal frame
invisible, unselected, and closed.

Fires an

INTERNAL_FRAME_CLOSING

event
and then performs the action specified by
the internal frame's default close operation.

Fires an internal frame event.

Gets the

AccessibleContext

associated with this

JInternalFrame

.

Returns the content pane for this internal frame.

Returns the default operation that occurs when the user
initiates a "close" on this internal frame.

Returns the

JDesktopIcon

used when this

JInternalFrame

is iconified.

Convenience method that searches the ancestor hierarchy for a

JDesktop

instance.

Always returns

null

because

JInternalFrame

s
must always be roots of a focus
traversal cycle.

If this

JInternalFrame

is active,
returns the child that has focus.

Returns the image displayed in the title bar of this internal frame (usually
in the top-left corner).

Returns the glass pane for this internal frame.

Returns an array of all the

InternalFrameListener

s added
to this

JInternalFrame

with

addInternalFrameListener

.

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

Returns the last

Cursor

that was set by the

setCursor

method that is not a resizable

Cursor

.

Convenience method for getting the layer attribute of this component.

Returns the layered pane for this internal frame.

Deprecated.

As of Swing version 1.0.3,
replaced by

getJMenuBar()

.

Returns the child component of this

JInternalFrame

that will receive the
focus when this

JInternalFrame

is selected.

If the

JInternalFrame

is not in maximized state, returns

getBounds()

; otherwise, returns the bounds that the

JInternalFrame

would be restored to.

Returns the

rootPane

object for this internal frame.

Returns the title of the

JInternalFrame

.

Returns the look-and-feel object that renders this component.

Returns the name of the look-and-feel
class that renders this component.

Gets the warning string that is displayed with this internal frame.

Returns whether this

JInternalFrame

can be closed by
some user action.

Returns whether this

JInternalFrame

is currently closed.

Always returns

true

because all

JInternalFrame

s must be
roots of a focus traversal cycle.

Returns whether the

JInternalFrame

is currently iconified.

Gets the

iconable

property,
which by default is

false

.

Gets the value of the

maximizable

property.

Returns whether the

JInternalFrame

is currently maximized.

Returns whether the

JInternalFrame

can be resized
by some user action.

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

Returns whether the

JInternalFrame

is the
currently "selected" or active frame.

Convenience method that moves this component to position -1 if its
parent is a

JLayeredPane

.

Convenience method that moves this component to position 0 if its
parent is a

JLayeredPane

.

Causes subcomponents of this

JInternalFrame

to be laid out at their preferred size.

Overridden to allow optimized painting when the
internal frame is being dragged.

Returns a string representation of this

JInternalFrame

.

Removes the specified component from the container.

Removes the specified internal frame listener so that it no longer
receives internal frame events from this internal frame.

Moves and resizes this component.

Requests the internal frame to restore focus to the
last subcomponent that had focus.

Sets whether this

JInternalFrame

can be closed by
some user action.

Closes this internal frame if the argument is

true

.

Sets this

JInternalFrame

's

contentPane

property.

Sets the cursor image to the specified cursor.

Sets the operation that will happen by default when
the user initiates a "close" on this internal frame.

Sets the

JDesktopIcon

associated with this

JInternalFrame

.

Does nothing because

JInternalFrame

s must always be roots of a focus
traversal cycle.

Sets an image to be displayed in the titlebar of this internal frame (usually
in the top-left corner).

Sets this

JInternalFrame

's

glassPane

property.

Iconifies or de-iconifies this internal frame,
if the look and feel supports iconification.

Sets the

iconable

property,
which must be

true

for the user to be able to
make the

JInternalFrame

an icon.

Sets the

menuBar

property for this

JInternalFrame

.

Convenience method for setting the layer attribute of this component.

Sets this

JInternalFrame

's

layeredPane

property.

Ensures that, by default, the layout of this component cannot be set.

Sets the

maximizable

property,
which determines whether the

JInternalFrame

can be maximized by
some user action.

Maximizes and restores this internal frame.

Deprecated.

As of Swing version 1.0.3
replaced by

setJMenuBar(JMenuBar m)

.

Sets the normal bounds for this internal frame, the bounds that
this internal frame would be restored to from its maximized state.

Sets whether the

JInternalFrame

can be resized by some
user action.

Sets the

rootPane

property
for this

JInternalFrame

.

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

Selects or deselects the internal frame
if it's showing.

Sets the

JInternalFrame

title.

Sets the UI delegate for this

JInternalFrame

.

If the internal frame is not visible,
brings the internal frame to the front,
makes it visible,
and attempts to select it.

Sends this internal frame to the back.

Brings this internal frame to the front.

Notification from the

UIManager

that the look and feel
has changed.

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

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

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

removeAll

,

removeContainerListener

,

setComponentZOrder

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

- rootPane

```java
protected
JRootPane
rootPane
```

The

JRootPane

instance that manages the
content pane
and optional menu bar for this internal frame, as well as the
glass pane.

**See Also:** JRootPane

,

RootPaneContainer

- rootPaneCheckingEnabled

```java
protected boolean rootPaneCheckingEnabled
```

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JInternalFrame

is
constructed.

**See Also:** isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- closable

```java
protected boolean closable
```

The frame can be closed.

- isClosed

```java
protected boolean isClosed
```

The frame has been closed.

- maximizable

```java
protected boolean maximizable
```

The frame can be expanded to the size of the desktop pane.

- isMaximum

```java
protected boolean isMaximum
```

The frame has been expanded to its maximum size.

**See Also:** maximizable

- iconable

```java
protected boolean iconable
```

The frame can "iconified" (shrunk down and displayed as
an icon-image).

**See Also:** JInternalFrame.JDesktopIcon

,

setIconifiable(boolean)

- isIcon

```java
protected boolean isIcon
```

The frame has been iconified.

**See Also:** isIcon()

- resizable

```java
protected boolean resizable
```

The frame's size can be changed.

- isSelected

```java
protected boolean isSelected
```

The frame is currently selected.

- frameIcon

```java
protected
Icon
frameIcon
```

The icon shown in the top-left corner of this internal frame.

- title

```java
protected
String
title
```

The title displayed in this internal frame's title bar.

- desktopIcon

```java
protected
JInternalFrame.JDesktopIcon
desktopIcon
```

The icon that is displayed when this internal frame is iconified.

**See Also:** iconable

- CONTENT_PANE_PROPERTY

```java
public static final
String
CONTENT_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- MENU_BAR_PROPERTY

```java
public static final
String
MENU_BAR_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- TITLE_PROPERTY

```java
public static final
String
TITLE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- LAYERED_PANE_PROPERTY

```java
public static final
String
LAYERED_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- ROOT_PANE_PROPERTY

```java
public static final
String
ROOT_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- GLASS_PANE_PROPERTY

```java
public static final
String
GLASS_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- FRAME_ICON_PROPERTY

```java
public static final
String
FRAME_ICON_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- IS_SELECTED_PROPERTY

```java
public static final
String
IS_SELECTED_PROPERTY
```

Constrained property name indicated that this frame has
selected status.

**See Also:** Constant Field Values

- IS_CLOSED_PROPERTY

```java
public static final
String
IS_CLOSED_PROPERTY
```

Constrained property name indicating that the internal frame is closed.

**See Also:** Constant Field Values

- IS_MAXIMUM_PROPERTY

```java
public static final
String
IS_MAXIMUM_PROPERTY
```

Constrained property name indicating that the internal frame is maximized.

**See Also:** Constant Field Values

- IS_ICON_PROPERTY

```java
public static final
String
IS_ICON_PROPERTY
```

Constrained property name indicating that the internal frame is iconified.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JInternalFrame

```java
public JInternalFrame()
```

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with no title.

- JInternalFrame

```java
public JInternalFrame​(
String
title)
```

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with the specified title.
Note that passing in a

null

title

results in
unspecified behavior and possibly an exception.

**Parameters:** title

- the non-

null

String

to display in the title bar

- JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable)
```

Creates a non-closable, non-maximizable, non-iconifiable

JInternalFrame

with the specified title
and resizability.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized

- JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable,
boolean closable)
```

Creates a non-maximizable, non-iconifiable

JInternalFrame

with the specified title, resizability, and
closability.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized
**Parameters:** closable

- if

true

, the internal frame can be closed

- JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable,
boolean closable,
boolean maximizable)
```

Creates a non-iconifiable

JInternalFrame

with the specified title,
resizability, closability, and maximizability.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized
**Parameters:** closable

- if

true

, the internal frame can be closed
**Parameters:** maximizable

- if

true

, the internal frame can be maximized

- JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable,
boolean closable,
boolean maximizable,
boolean iconifiable)
```

Creates a

JInternalFrame

with the specified title,
resizability, closability, maximizability, and iconifiability.
All

JInternalFrame

constructors use this one.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized
**Parameters:** closable

- if

true

, the internal frame can be closed
**Parameters:** maximizable

- if

true

, the internal frame can be maximized
**Parameters:** iconifiable

- if

true

, the internal frame can be iconified

============ METHOD DETAIL ==========

- Method Detail

- createRootPane

```java
protected
JRootPane
createRootPane()
```

Called by the constructor to set up the

JRootPane

.

**Returns:** a new

JRootPane
**See Also:** JRootPane

- getUI

```java
public
InternalFrameUI
getUI()
```

Returns the look-and-feel object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

InternalFrameUI

object that renders
this component

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
InternalFrameUI
ui)
```

Sets the UI delegate for this

JInternalFrame

.

**Parameters:** ui

- the UI delegate

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the look and feel
has changed.
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

description
="UIClassID")
public
String
getUIClassID()
```

Returns the name of the look-and-feel
class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "InternalFrameUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- isRootPaneCheckingEnabled

```java
protected boolean isRootPaneCheckingEnabled()
```

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Returns:** true if

add

and

setLayout

are forwarded; false otherwise
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- setRootPaneCheckingEnabled

```java
@BeanProperty
(
hidden
=true,

description
="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)
```

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Parameters:** enabled

- true if

add

and

setLayout

are forwarded, false if they should operate directly on the

JInternalFrame

.
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

isRootPaneCheckingEnabled()

,

RootPaneContainer

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be enhanced
**Parameters:** constraints

- the constraints to be respected
**Parameters:** index

- the index
**Throws:** IllegalArgumentException

- if

index

is invalid
**Throws:** IllegalArgumentException

- if adding the container's parent
to itself
**Throws:** IllegalArgumentException

- if adding a window to a container
**See Also:** setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- remove

```java
public void remove​(
Component
comp)
```

Removes the specified component from the container. If

comp

is not a child of the

JInternalFrame

this will forward the call to the

contentPane

.

**Overrides:** remove

in class

Container
**Parameters:** comp

- the component to be removed
**Throws:** NullPointerException

- if

comp

is null
**See Also:** Container.add(java.awt.Component)

,

RootPaneContainer

- setLayout

```java
public void setLayout​(
LayoutManager
manager)
```

Ensures that, by default, the layout of this component cannot be set.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

**Overrides:** setLayout

in class

Container
**Parameters:** manager

- the

LayoutManager
**See Also:** setRootPaneCheckingEnabled(boolean)

- getMenuBar

```java
@Deprecated

public
JMenuBar
getMenuBar()
```

Deprecated.

As of Swing version 1.0.3,
replaced by

getJMenuBar()

.

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

**Returns:** the current menu bar, or

null

if none has been set

- getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

**Returns:** the

JMenuBar

used by this internal frame
**See Also:** setJMenuBar(javax.swing.JMenuBar)

- setMenuBar

```java
@Deprecated

public void setMenuBar​(
JMenuBar
m)
```

Deprecated.

As of Swing version 1.0.3
replaced by

setJMenuBar(JMenuBar m)

.

Sets the

menuBar

property for this

JInternalFrame

.

**Parameters:** m

- the

JMenuBar

to use in this internal frame
**See Also:** getJMenuBar()

- setJMenuBar

```java
@BeanProperty
(
preferred
=true,

description
="The menu bar for accessing pulldown menus from this internal frame.")
public void setJMenuBar​(
JMenuBar
m)
```

Sets the

menuBar

property for this

JInternalFrame

.

**Parameters:** m

- the

JMenuBar

to use in this internal frame
**See Also:** getJMenuBar()

- getContentPane

```java
public
Container
getContentPane()
```

Returns the content pane for this internal frame.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the content pane
**See Also:** RootPaneContainer.setContentPane(java.awt.Container)

- setContentPane

```java
@BeanProperty
(
hidden
=true,

description
="The client area of the internal frame where child components are normally inserted.")
public void setContentPane​(
Container
c)
```

Sets this

JInternalFrame

's

contentPane

property.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** c

- the content pane for this internal frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null
**See Also:** RootPaneContainer.getContentPane()

- getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Returns the layered pane for this internal frame.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** a

JLayeredPane

object
**See Also:** RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

- setLayeredPane

```java
@BeanProperty
(
hidden
=true,

description
="The pane which holds the various desktop layers.")
public void setLayeredPane​(
JLayeredPane
layered)
```

Sets this

JInternalFrame

's

layeredPane

property.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layered

- the

JLayeredPane

for this internal frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is

null
**See Also:** RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

- getGlassPane

```java
public
Component
getGlassPane()
```

Returns the glass pane for this internal frame.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the glass pane
**See Also:** RootPaneContainer.setGlassPane(java.awt.Component)

- setGlassPane

```java
@BeanProperty
(
hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glass)
```

Sets this

JInternalFrame

's

glassPane

property.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glass

- the glass pane for this internal frame
**See Also:** RootPaneContainer.getGlassPane()

- getRootPane

```java
@BeanProperty
(
hidden
=true,

description
="The root pane used by this internal frame.")
public
JRootPane
getRootPane()
```

Returns the

rootPane

object for this internal frame.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Overrides:** getRootPane

in class

JComponent
**Returns:** the

rootPane

property
**See Also:** RootPaneContainer.getRootPane()

- setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Sets the

rootPane

property
for this

JInternalFrame

.
This method is called by the constructor.

**Parameters:** root

- the new

JRootPane

object

- setClosable

```java
@BeanProperty
(
preferred
=true,

description
="Indicates whether this internal frame can be closed.")
public void setClosable​(boolean b)
```

Sets whether this

JInternalFrame

can be closed by
some user action.

**Parameters:** b

- a boolean value, where

true

means this internal frame can be closed

- isClosable

```java
public boolean isClosable()
```

Returns whether this

JInternalFrame

can be closed by
some user action.

**Returns:** true

if this internal frame can be closed

- isClosed

```java
public boolean isClosed()
```

Returns whether this

JInternalFrame

is currently closed.

**Returns:** true

if this internal frame is closed,

false

otherwise

- setClosed

```java
@BeanProperty
(
description
="Indicates whether this internal frame has been closed.")
public void setClosed​(boolean b)
throws
PropertyVetoException
```

Closes this internal frame if the argument is

true

.
Do not invoke this method with a

false

argument;
the result of invoking

setClosed(false)

is unspecified.

If the internal frame is already closed,
this method does nothing and returns immediately.
Otherwise,
this method begins by firing
an

INTERNAL_FRAME_CLOSING

event.
Then this method sets the

closed

property to

true

unless a listener vetoes the property change.
This method finishes by making the internal frame
invisible and unselected,
and then firing an

INTERNAL_FRAME_CLOSED

event.

Note:

To reuse an internal frame that has been closed,
you must add it to a container
(even if you never removed it from its previous container).
Typically, this container will be the

JDesktopPane

that previously contained the internal frame.

**Parameters:** b

- must be

true
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame
**See Also:** isClosed()

,

setDefaultCloseOperation(int)

,

dispose()

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

- setResizable

```java
@BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be resized by the user.")
public void setResizable​(boolean b)
```

Sets whether the

JInternalFrame

can be resized by some
user action.

**Parameters:** b

- a boolean, where

true

means this internal frame can be resized

- isResizable

```java
public boolean isResizable()
```

Returns whether the

JInternalFrame

can be resized
by some user action.

**Returns:** true

if this internal frame can be resized,

false

otherwise

- setIconifiable

```java
@BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be iconified.")
public void setIconifiable​(boolean b)
```

Sets the

iconable

property,
which must be

true

for the user to be able to
make the

JInternalFrame

an icon.
Some look and feels might not implement iconification;
they will ignore this property.

**Parameters:** b

- a boolean, where

true

means this internal frame can be iconified

- isIconifiable

```java
public boolean isIconifiable()
```

Gets the

iconable

property,
which by default is

false

.

**Returns:** the value of the

iconable

property.
**See Also:** setIconifiable(boolean)

- isIcon

```java
public boolean isIcon()
```

Returns whether the

JInternalFrame

is currently iconified.

**Returns:** true

if this internal frame is iconified

- setIcon

```java
@BeanProperty
(
description
="The image displayed when this internal frame is minimized.")
public void setIcon​(boolean b)
throws
PropertyVetoException
```

Iconifies or de-iconifies this internal frame,
if the look and feel supports iconification.
If the internal frame's state changes to iconified,
this method fires an

INTERNAL_FRAME_ICONIFIED

event.
If the state changes to de-iconified,
an

INTERNAL_FRAME_DEICONIFIED

event is fired.

**Parameters:** b

- a boolean, where

true

means to iconify this internal frame and

false

means to de-iconify it
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame
**See Also:** InternalFrameEvent.INTERNAL_FRAME_ICONIFIED

,

InternalFrameEvent.INTERNAL_FRAME_DEICONIFIED

- setMaximizable

```java
@BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be maximized.")
public void setMaximizable​(boolean b)
```

Sets the

maximizable

property,
which determines whether the

JInternalFrame

can be maximized by
some user action.
Some look and feels might not support maximizing internal frames;
they will ignore this property.

**Parameters:** b

-

true

to specify that this internal frame should be maximizable;

false

to specify that it should not be

- isMaximizable

```java
public boolean isMaximizable()
```

Gets the value of the

maximizable

property.

**Returns:** the value of the

maximizable

property
**See Also:** setMaximizable(boolean)

- isMaximum

```java
public boolean isMaximum()
```

Returns whether the

JInternalFrame

is currently maximized.

**Returns:** true

if this internal frame is maximized,

false

otherwise

- setMaximum

```java
@BeanProperty
(
description
="Indicates whether this internal frame is maximized.")
public void setMaximum​(boolean b)
throws
PropertyVetoException
```

Maximizes and restores this internal frame. A maximized frame is resized to
fully fit the

JDesktopPane

area associated with the

JInternalFrame

.
A restored frame's size is set to the

JInternalFrame

's
actual size.

**Parameters:** b

- a boolean, where

true

maximizes this internal frame and

false

restores it
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame

- getTitle

```java
public
String
getTitle()
```

Returns the title of the

JInternalFrame

.

**Returns:** a

String

containing this internal frame's title
**See Also:** setTitle(java.lang.String)

- setTitle

```java
@BeanProperty
(
preferred
=true,

description
="The text displayed in the title bar.")
public void setTitle​(
String
title)
```

Sets the

JInternalFrame

title.

title

may have a

null

value.

**Parameters:** title

- the

String

to display in the title bar
**See Also:** getTitle()

- setSelected

```java
@BeanProperty
(
description
="Indicates whether this internal frame is currently the active frame.")
public void setSelected​(boolean selected)
throws
PropertyVetoException
```

Selects or deselects the internal frame
if it's showing.
A

JInternalFrame

normally draws its title bar
differently if it is
the selected frame, which indicates to the user that this
internal frame has the focus.
When this method changes the state of the internal frame
from deselected to selected, it fires an

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

event.
If the change is from selected to deselected,
an

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

event
is fired.

**Parameters:** selected

- a boolean, where

true

means this internal frame
should become selected (currently active)
and

false

means it should become deselected
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame
**See Also:** Component.isShowing()

,

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

,

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

- isSelected

```java
public boolean isSelected()
```

Returns whether the

JInternalFrame

is the
currently "selected" or active frame.

**Returns:** true

if this internal frame is currently selected (active)
**See Also:** setSelected(boolean)

- setFrameIcon

```java
@BeanProperty
(
description
="The icon shown in the top-left corner of this internal frame.")
public void setFrameIcon​(
Icon
icon)
```

Sets an image to be displayed in the titlebar of this internal frame (usually
in the top-left corner).
Some look and feels might not support displaying an icon in the titlebar.

This image is not the

desktopIcon

object, which
is the image displayed in the

JDesktop

when
this internal frame is iconified.

Passing

null

to this function is valid,
but the look and feel can choose the appropriate behavior
for that situation, such as displaying no icon
or a default icon for the look and feel.

**Parameters:** icon

- the

Icon

to display in the title bar
**See Also:** getFrameIcon()

- getFrameIcon

```java
public
Icon
getFrameIcon()
```

Returns the image displayed in the title bar of this internal frame (usually
in the top-left corner).

**Returns:** the

Icon

displayed in the title bar
**See Also:** setFrameIcon(javax.swing.Icon)

- moveToFront

```java
public void moveToFront()
```

Convenience method that moves this component to position 0 if its
parent is a

JLayeredPane

.

- moveToBack

```java
public void moveToBack()
```

Convenience method that moves this component to position -1 if its
parent is a

JLayeredPane

.

- getLastCursor

```java
@BeanProperty
(
bound
=false)
public
Cursor
getLastCursor()
```

Returns the last

Cursor

that was set by the

setCursor

method that is not a resizable

Cursor

.

**Returns:** the last non-resizable

Cursor
**Since:** 1.6

- setCursor

```java
public void setCursor​(
Cursor
cursor)
```

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

**Overrides:** setCursor

in class

Component
**Parameters:** cursor

- One of the constants defined
by the

Cursor

class;
if this parameter is

null

then this component will inherit
the cursor of its parent
**Since:** 1.6
**See Also:** Component.isEnabled()

,

Component.isShowing()

,

Component.getCursor()

,

Component.contains(int, int)

,

Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

,

Cursor

- setLayer

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Specifies what desktop layer is used.")
public void setLayer​(
Integer
layer)
```

Convenience method for setting the layer attribute of this component.

**Parameters:** layer

- an

Integer

object specifying this
frame's desktop layer
**Throws:** NullPointerException

- if

layer

is

null
**See Also:** JLayeredPane

- setLayer

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Specifies what desktop layer is used.")
public void setLayer​(int layer)
```

Convenience method for setting the layer attribute of this component.
The method

setLayer(Integer)

should be used for
layer values predefined in

JLayeredPane

.
When using

setLayer(int)

, care must be taken not to
accidentally clash with those values.

**Parameters:** layer

- an integer specifying this internal frame's desktop layer
**Since:** 1.3
**See Also:** setLayer(Integer)

,

JLayeredPane

- getLayer

```java
public int getLayer()
```

Convenience method for getting the layer attribute of this component.

**Returns:** an

Integer

object specifying this
frame's desktop layer
**See Also:** JLayeredPane

- getDesktopPane

```java
@BeanProperty
(
bound
=false)
public
JDesktopPane
getDesktopPane()
```

Convenience method that searches the ancestor hierarchy for a

JDesktop

instance. If

JInternalFrame

finds none, the

desktopIcon

tree is searched.

**Returns:** the

JDesktopPane

this internal frame belongs to,
or

null

if none is found

- setDesktopIcon

```java
@BeanProperty
(
description
="The icon shown when this internal frame is minimized.")
public void setDesktopIcon​(
JInternalFrame.JDesktopIcon
d)
```

Sets the

JDesktopIcon

associated with this

JInternalFrame

.

**Parameters:** d

- the

JDesktopIcon

to display on the desktop
**See Also:** getDesktopIcon()

- getDesktopIcon

```java
public
JInternalFrame.JDesktopIcon
getDesktopIcon()
```

Returns the

JDesktopIcon

used when this

JInternalFrame

is iconified.

**Returns:** the

JDesktopIcon

displayed on the desktop
**See Also:** setDesktopIcon(javax.swing.JInternalFrame.JDesktopIcon)

- getNormalBounds

```java
public
Rectangle
getNormalBounds()
```

If the

JInternalFrame

is not in maximized state, returns

getBounds()

; otherwise, returns the bounds that the

JInternalFrame

would be restored to.

**Returns:** a

Rectangle

containing the bounds of this
frame when in the normal state
**Since:** 1.3

- setNormalBounds

```java
public void setNormalBounds​(
Rectangle
r)
```

Sets the normal bounds for this internal frame, the bounds that
this internal frame would be restored to from its maximized state.
This method is intended for use only by desktop managers.

**Parameters:** r

- the bounds that this internal frame should be restored to
**Since:** 1.3

- getFocusOwner

```java
public
Component
getFocusOwner()
```

If this

JInternalFrame

is active,
returns the child that has focus.
Otherwise, returns

null

.

**Returns:** the component with focus, or

null

if no children have focus
**Since:** 1.3

- getMostRecentFocusOwner

```java
@BeanProperty
(
bound
=false)
public
Component
getMostRecentFocusOwner()
```

Returns the child component of this

JInternalFrame

that will receive the
focus when this

JInternalFrame

is selected.
If this

JInternalFrame

is
currently selected, this method returns the same component as
the

getFocusOwner

method.
If this

JInternalFrame

is not selected,
then the child component that most recently requested focus will be
returned. If no child component has ever requested focus, then this

JInternalFrame

's initial focusable component is returned.
If no such
child exists, then this

JInternalFrame

's default component
to focus is returned.

**Returns:** the child component that will receive focus when this

JInternalFrame

is selected
**Since:** 1.4
**See Also:** getFocusOwner()

,

isSelected

- restoreSubcomponentFocus

```java
public void restoreSubcomponentFocus()
```

Requests the internal frame to restore focus to the
last subcomponent that had focus. This is used by the UI when
the user selected this internal frame --
for example, by clicking on the title bar.

**Since:** 1.3

- reshape

```java
public void reshape​(int x,
int y,
int width,
int height)
```

Moves and resizes this component. Unlike other components,
this implementation also forces re-layout, so that frame
decorations such as the title bar are always redisplayed.

**Overrides:** reshape

in class

JComponent
**Parameters:** x

- an integer giving the component's new horizontal position
measured in pixels from the left of its container
**Parameters:** y

- an integer giving the component's new vertical position,
measured in pixels from the bottom of its container
**Parameters:** width

- an integer giving the component's new width in pixels
**Parameters:** height

- an integer giving the component's new height in pixels
**See Also:** Component.setBounds(int, int, int, int)

- addInternalFrameListener

```java
public void addInternalFrameListener​(
InternalFrameListener
l)
```

Adds the specified listener to receive internal
frame events from this internal frame.

**Parameters:** l

- the internal frame listener

- removeInternalFrameListener

```java
public void removeInternalFrameListener​(
InternalFrameListener
l)
```

Removes the specified internal frame listener so that it no longer
receives internal frame events from this internal frame.

**Parameters:** l

- the internal frame listener

- getInternalFrameListeners

```java
@BeanProperty
(
bound
=false)
public
InternalFrameListener
[] getInternalFrameListeners()
```

Returns an array of all the

InternalFrameListener

s added
to this

JInternalFrame

with

addInternalFrameListener

.

**Returns:** all of the

InternalFrameListener

s added or an empty
array if no listeners have been added
**Since:** 1.4
**See Also:** addInternalFrameListener(javax.swing.event.InternalFrameListener)

- fireInternalFrameEvent

```java
protected void fireInternalFrameEvent​(int id)
```

Fires an internal frame event.

**Parameters:** id

- the type of the event being fired; one of the following:

- InternalFrameEvent.INTERNAL_FRAME_OPENED

InternalFrameEvent.INTERNAL_FRAME_CLOSING

InternalFrameEvent.INTERNAL_FRAME_CLOSED

InternalFrameEvent.INTERNAL_FRAME_ICONIFIED

InternalFrameEvent.INTERNAL_FRAME_DEICONIFIED

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

If the event type is not one of the above, nothing happens.

- doDefaultCloseAction

```java
public void doDefaultCloseAction()
```

Fires an

INTERNAL_FRAME_CLOSING

event
and then performs the action specified by
the internal frame's default close operation.
This method is typically invoked by the
look-and-feel-implemented action handler
for the internal frame's close button.

**Since:** 1.3
**See Also:** setDefaultCloseOperation(int)

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

- setDefaultCloseOperation

```java
public void setDefaultCloseOperation​(int operation)
```

Sets the operation that will happen by default when
the user initiates a "close" on this internal frame.
The possible choices are:

The default value is

DISPOSE_ON_CLOSE

.
Before performing the specified close operation,
the internal frame fires
an

INTERNAL_FRAME_CLOSING

event.

**Parameters:** operation

- one of the following constants defined in

javax.swing.WindowConstants

(an interface implemented by

JInternalFrame

):

DO_NOTHING_ON_CLOSE

,

HIDE_ON_CLOSE

, or

DISPOSE_ON_CLOSE
**See Also:** addInternalFrameListener(javax.swing.event.InternalFrameListener)

,

getDefaultCloseOperation()

,

JComponent.setVisible(boolean)

,

dispose()

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

- getDefaultCloseOperation

```java
public int getDefaultCloseOperation()
```

Returns the default operation that occurs when the user
initiates a "close" on this internal frame.

**Returns:** the operation that will occur when the user closes the internal
frame
**See Also:** setDefaultCloseOperation(int)

- pack

```java
public void pack()
```

Causes subcomponents of this

JInternalFrame

to be laid out at their preferred size. Internal frames that are
iconized or maximized are first restored and then packed. If the
internal frame is unable to be restored its state is not changed
and will not be packed.

**See Also:** Window.pack()

- show

```java
public void show()
```

If the internal frame is not visible,
brings the internal frame to the front,
makes it visible,
and attempts to select it.
The first time the internal frame is made visible,
this method also fires an

INTERNAL_FRAME_OPENED

event.
This method does nothing if the internal frame is already visible.
Invoking this method
has the same result as invoking

setVisible(true)

.

**Overrides:** show

in class

Component
**See Also:** moveToFront()

,

setSelected(boolean)

,

InternalFrameEvent.INTERNAL_FRAME_OPENED

,

JComponent.setVisible(boolean)

- dispose

```java
public void dispose()
```

Makes this internal frame
invisible, unselected, and closed.
If the frame is not already closed,
this method fires an

INTERNAL_FRAME_CLOSED

event.
The results of invoking this method are similar to

setClosed(true)

,
but

dispose

always succeeds in closing
the internal frame and does not fire
an

INTERNAL_FRAME_CLOSING

event.

**See Also:** InternalFrameEvent.INTERNAL_FRAME_CLOSED

,

JComponent.setVisible(boolean)

,

setSelected(boolean)

,

setClosed(boolean)

- toFront

```java
public void toFront()
```

Brings this internal frame to the front.
Places this internal frame at the top of the stacking order
and makes the corresponding adjustment to other visible internal
frames.

**See Also:** Window.toFront()

,

moveToFront()

- toBack

```java
public void toBack()
```

Sends this internal frame to the back.
Places this internal frame at the bottom of the stacking order
and makes the corresponding adjustment to other visible
internal frames.

**See Also:** Window.toBack()

,

moveToBack()

- setFocusCycleRoot

```java
public final void setFocusCycleRoot​(boolean focusCycleRoot)
```

Does nothing because

JInternalFrame

s must always be roots of a focus
traversal cycle.

**Overrides:** setFocusCycleRoot

in class

Container
**Parameters:** focusCycleRoot

- this value is ignored
**Since:** 1.4
**See Also:** isFocusCycleRoot()

,

Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

Container.getFocusTraversalPolicy()

- isFocusCycleRoot

```java
public final boolean isFocusCycleRoot()
```

Always returns

true

because all

JInternalFrame

s must be
roots of a focus traversal cycle.

**Overrides:** isFocusCycleRoot

in class

Container
**Returns:** true
**Since:** 1.4
**See Also:** setFocusCycleRoot(boolean)

,

Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

Container.getFocusTraversalPolicy()

- getFocusCycleRootAncestor

```java
@BeanProperty
(
bound
=false)
public final
Container
getFocusCycleRootAncestor()
```

Always returns

null

because

JInternalFrame

s
must always be roots of a focus
traversal cycle.

**Overrides:** getFocusCycleRootAncestor

in class

Component
**Returns:** null
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

- getWarningString

```java
@BeanProperty
(
bound
=false)
public final
String
getWarningString()
```

Gets the warning string that is displayed with this internal frame.
Since an internal frame is always secure (since it's fully
contained within a window that might need a warning string)
this method always returns

null

.

**Returns:** null
**See Also:** Window.getWarningString()

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JInternalFrame

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

JInternalFrame

- paintComponent

```java
protected void paintComponent​(
Graphics
g)
```

Overridden to allow optimized painting when the
internal frame is being dragged.

**Overrides:** paintComponent

in class

JComponent
**Parameters:** g

- the

Graphics

object to protect
**See Also:** JComponent.paint(java.awt.Graphics)

,

ComponentUI

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

Gets the

AccessibleContext

associated with this

JInternalFrame

.
For internal frames, the

AccessibleContext

takes the form of an

AccessibleJInternalFrame

object.
A new

AccessibleJInternalFrame

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleJInternalFrame

that serves as the

AccessibleContext

of this

JInternalFrame
**See Also:** JInternalFrame.AccessibleJInternalFrame

Field Detail

- rootPane

```java
protected
JRootPane
rootPane
```

The

JRootPane

instance that manages the
content pane
and optional menu bar for this internal frame, as well as the
glass pane.

**See Also:** JRootPane

,

RootPaneContainer

- rootPaneCheckingEnabled

```java
protected boolean rootPaneCheckingEnabled
```

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JInternalFrame

is
constructed.

**See Also:** isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- closable

```java
protected boolean closable
```

The frame can be closed.

- isClosed

```java
protected boolean isClosed
```

The frame has been closed.

- maximizable

```java
protected boolean maximizable
```

The frame can be expanded to the size of the desktop pane.

- isMaximum

```java
protected boolean isMaximum
```

The frame has been expanded to its maximum size.

**See Also:** maximizable

- iconable

```java
protected boolean iconable
```

The frame can "iconified" (shrunk down and displayed as
an icon-image).

**See Also:** JInternalFrame.JDesktopIcon

,

setIconifiable(boolean)

- isIcon

```java
protected boolean isIcon
```

The frame has been iconified.

**See Also:** isIcon()

- resizable

```java
protected boolean resizable
```

The frame's size can be changed.

- isSelected

```java
protected boolean isSelected
```

The frame is currently selected.

- frameIcon

```java
protected
Icon
frameIcon
```

The icon shown in the top-left corner of this internal frame.

- title

```java
protected
String
title
```

The title displayed in this internal frame's title bar.

- desktopIcon

```java
protected
JInternalFrame.JDesktopIcon
desktopIcon
```

The icon that is displayed when this internal frame is iconified.

**See Also:** iconable

- CONTENT_PANE_PROPERTY

```java
public static final
String
CONTENT_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- MENU_BAR_PROPERTY

```java
public static final
String
MENU_BAR_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- TITLE_PROPERTY

```java
public static final
String
TITLE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- LAYERED_PANE_PROPERTY

```java
public static final
String
LAYERED_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- ROOT_PANE_PROPERTY

```java
public static final
String
ROOT_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- GLASS_PANE_PROPERTY

```java
public static final
String
GLASS_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- FRAME_ICON_PROPERTY

```java
public static final
String
FRAME_ICON_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

- IS_SELECTED_PROPERTY

```java
public static final
String
IS_SELECTED_PROPERTY
```

Constrained property name indicated that this frame has
selected status.

**See Also:** Constant Field Values

- IS_CLOSED_PROPERTY

```java
public static final
String
IS_CLOSED_PROPERTY
```

Constrained property name indicating that the internal frame is closed.

**See Also:** Constant Field Values

- IS_MAXIMUM_PROPERTY

```java
public static final
String
IS_MAXIMUM_PROPERTY
```

Constrained property name indicating that the internal frame is maximized.

**See Also:** Constant Field Values

- IS_ICON_PROPERTY

```java
public static final
String
IS_ICON_PROPERTY
```

Constrained property name indicating that the internal frame is iconified.

**See Also:** Constant Field Values

---

#### Field Detail

rootPane

```java
protected
JRootPane
rootPane
```

The

JRootPane

instance that manages the
content pane
and optional menu bar for this internal frame, as well as the
glass pane.

**See Also:** JRootPane

,

RootPaneContainer

---

#### rootPane

protected

JRootPane

rootPane

The

JRootPane

instance that manages the
content pane
and optional menu bar for this internal frame, as well as the
glass pane.

rootPaneCheckingEnabled

```java
protected boolean rootPaneCheckingEnabled
```

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JInternalFrame

is
constructed.

**See Also:** isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### rootPaneCheckingEnabled

protected boolean rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JInternalFrame

is
constructed.

closable

```java
protected boolean closable
```

The frame can be closed.

---

#### closable

protected boolean closable

The frame can be closed.

isClosed

```java
protected boolean isClosed
```

The frame has been closed.

---

#### isClosed

protected boolean isClosed

The frame has been closed.

maximizable

```java
protected boolean maximizable
```

The frame can be expanded to the size of the desktop pane.

---

#### maximizable

protected boolean maximizable

The frame can be expanded to the size of the desktop pane.

isMaximum

```java
protected boolean isMaximum
```

The frame has been expanded to its maximum size.

**See Also:** maximizable

---

#### isMaximum

protected boolean isMaximum

The frame has been expanded to its maximum size.

iconable

```java
protected boolean iconable
```

The frame can "iconified" (shrunk down and displayed as
an icon-image).

**See Also:** JInternalFrame.JDesktopIcon

,

setIconifiable(boolean)

---

#### iconable

protected boolean iconable

The frame can "iconified" (shrunk down and displayed as
an icon-image).

isIcon

```java
protected boolean isIcon
```

The frame has been iconified.

**See Also:** isIcon()

---

#### isIcon

protected boolean isIcon

The frame has been iconified.

resizable

```java
protected boolean resizable
```

The frame's size can be changed.

---

#### resizable

protected boolean resizable

The frame's size can be changed.

isSelected

```java
protected boolean isSelected
```

The frame is currently selected.

---

#### isSelected

protected boolean isSelected

The frame is currently selected.

frameIcon

```java
protected
Icon
frameIcon
```

The icon shown in the top-left corner of this internal frame.

---

#### frameIcon

protected

Icon

frameIcon

The icon shown in the top-left corner of this internal frame.

title

```java
protected
String
title
```

The title displayed in this internal frame's title bar.

---

#### title

protected

String

title

The title displayed in this internal frame's title bar.

desktopIcon

```java
protected
JInternalFrame.JDesktopIcon
desktopIcon
```

The icon that is displayed when this internal frame is iconified.

**See Also:** iconable

---

#### desktopIcon

protected

JInternalFrame.JDesktopIcon

desktopIcon

The icon that is displayed when this internal frame is iconified.

CONTENT_PANE_PROPERTY

```java
public static final
String
CONTENT_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

---

#### CONTENT_PANE_PROPERTY

public static final

String

CONTENT_PANE_PROPERTY

Bound property name.

MENU_BAR_PROPERTY

```java
public static final
String
MENU_BAR_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

---

#### MENU_BAR_PROPERTY

public static final

String

MENU_BAR_PROPERTY

Bound property name.

TITLE_PROPERTY

```java
public static final
String
TITLE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

---

#### TITLE_PROPERTY

public static final

String

TITLE_PROPERTY

Bound property name.

LAYERED_PANE_PROPERTY

```java
public static final
String
LAYERED_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

---

#### LAYERED_PANE_PROPERTY

public static final

String

LAYERED_PANE_PROPERTY

Bound property name.

ROOT_PANE_PROPERTY

```java
public static final
String
ROOT_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

---

#### ROOT_PANE_PROPERTY

public static final

String

ROOT_PANE_PROPERTY

Bound property name.

GLASS_PANE_PROPERTY

```java
public static final
String
GLASS_PANE_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

---

#### GLASS_PANE_PROPERTY

public static final

String

GLASS_PANE_PROPERTY

Bound property name.

FRAME_ICON_PROPERTY

```java
public static final
String
FRAME_ICON_PROPERTY
```

Bound property name.

**See Also:** Constant Field Values

---

#### FRAME_ICON_PROPERTY

public static final

String

FRAME_ICON_PROPERTY

Bound property name.

IS_SELECTED_PROPERTY

```java
public static final
String
IS_SELECTED_PROPERTY
```

Constrained property name indicated that this frame has
selected status.

**See Also:** Constant Field Values

---

#### IS_SELECTED_PROPERTY

public static final

String

IS_SELECTED_PROPERTY

Constrained property name indicated that this frame has
selected status.

IS_CLOSED_PROPERTY

```java
public static final
String
IS_CLOSED_PROPERTY
```

Constrained property name indicating that the internal frame is closed.

**See Also:** Constant Field Values

---

#### IS_CLOSED_PROPERTY

public static final

String

IS_CLOSED_PROPERTY

Constrained property name indicating that the internal frame is closed.

IS_MAXIMUM_PROPERTY

```java
public static final
String
IS_MAXIMUM_PROPERTY
```

Constrained property name indicating that the internal frame is maximized.

**See Also:** Constant Field Values

---

#### IS_MAXIMUM_PROPERTY

public static final

String

IS_MAXIMUM_PROPERTY

Constrained property name indicating that the internal frame is maximized.

IS_ICON_PROPERTY

```java
public static final
String
IS_ICON_PROPERTY
```

Constrained property name indicating that the internal frame is iconified.

**See Also:** Constant Field Values

---

#### IS_ICON_PROPERTY

public static final

String

IS_ICON_PROPERTY

Constrained property name indicating that the internal frame is iconified.

Constructor Detail

- JInternalFrame

```java
public JInternalFrame()
```

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with no title.

- JInternalFrame

```java
public JInternalFrame​(
String
title)
```

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with the specified title.
Note that passing in a

null

title

results in
unspecified behavior and possibly an exception.

**Parameters:** title

- the non-

null

String

to display in the title bar

- JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable)
```

Creates a non-closable, non-maximizable, non-iconifiable

JInternalFrame

with the specified title
and resizability.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized

- JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable,
boolean closable)
```

Creates a non-maximizable, non-iconifiable

JInternalFrame

with the specified title, resizability, and
closability.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized
**Parameters:** closable

- if

true

, the internal frame can be closed

- JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable,
boolean closable,
boolean maximizable)
```

Creates a non-iconifiable

JInternalFrame

with the specified title,
resizability, closability, and maximizability.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized
**Parameters:** closable

- if

true

, the internal frame can be closed
**Parameters:** maximizable

- if

true

, the internal frame can be maximized

- JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable,
boolean closable,
boolean maximizable,
boolean iconifiable)
```

Creates a

JInternalFrame

with the specified title,
resizability, closability, maximizability, and iconifiability.
All

JInternalFrame

constructors use this one.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized
**Parameters:** closable

- if

true

, the internal frame can be closed
**Parameters:** maximizable

- if

true

, the internal frame can be maximized
**Parameters:** iconifiable

- if

true

, the internal frame can be iconified

---

#### Constructor Detail

JInternalFrame

```java
public JInternalFrame()
```

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with no title.

---

#### JInternalFrame

public JInternalFrame()

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with no title.

JInternalFrame

```java
public JInternalFrame​(
String
title)
```

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with the specified title.
Note that passing in a

null

title

results in
unspecified behavior and possibly an exception.

**Parameters:** title

- the non-

null

String

to display in the title bar

---

#### JInternalFrame

public JInternalFrame​(

String

title)

Creates a non-resizable, non-closable, non-maximizable,
non-iconifiable

JInternalFrame

with the specified title.
Note that passing in a

null

title

results in
unspecified behavior and possibly an exception.

JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable)
```

Creates a non-closable, non-maximizable, non-iconifiable

JInternalFrame

with the specified title
and resizability.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized

---

#### JInternalFrame

public JInternalFrame​(

String

title,
boolean resizable)

Creates a non-closable, non-maximizable, non-iconifiable

JInternalFrame

with the specified title
and resizability.

JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable,
boolean closable)
```

Creates a non-maximizable, non-iconifiable

JInternalFrame

with the specified title, resizability, and
closability.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized
**Parameters:** closable

- if

true

, the internal frame can be closed

---

#### JInternalFrame

public JInternalFrame​(

String

title,
boolean resizable,
boolean closable)

Creates a non-maximizable, non-iconifiable

JInternalFrame

with the specified title, resizability, and
closability.

JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable,
boolean closable,
boolean maximizable)
```

Creates a non-iconifiable

JInternalFrame

with the specified title,
resizability, closability, and maximizability.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized
**Parameters:** closable

- if

true

, the internal frame can be closed
**Parameters:** maximizable

- if

true

, the internal frame can be maximized

---

#### JInternalFrame

public JInternalFrame​(

String

title,
boolean resizable,
boolean closable,
boolean maximizable)

Creates a non-iconifiable

JInternalFrame

with the specified title,
resizability, closability, and maximizability.

JInternalFrame

```java
public JInternalFrame​(
String
title,
boolean resizable,
boolean closable,
boolean maximizable,
boolean iconifiable)
```

Creates a

JInternalFrame

with the specified title,
resizability, closability, maximizability, and iconifiability.
All

JInternalFrame

constructors use this one.

**Parameters:** title

- the

String

to display in the title bar
**Parameters:** resizable

- if

true

, the internal frame can be resized
**Parameters:** closable

- if

true

, the internal frame can be closed
**Parameters:** maximizable

- if

true

, the internal frame can be maximized
**Parameters:** iconifiable

- if

true

, the internal frame can be iconified

---

#### JInternalFrame

public JInternalFrame​(

String

title,
boolean resizable,
boolean closable,
boolean maximizable,
boolean iconifiable)

Creates a

JInternalFrame

with the specified title,
resizability, closability, maximizability, and iconifiability.
All

JInternalFrame

constructors use this one.

Method Detail

- createRootPane

```java
protected
JRootPane
createRootPane()
```

Called by the constructor to set up the

JRootPane

.

**Returns:** a new

JRootPane
**See Also:** JRootPane

- getUI

```java
public
InternalFrameUI
getUI()
```

Returns the look-and-feel object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

InternalFrameUI

object that renders
this component

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
InternalFrameUI
ui)
```

Sets the UI delegate for this

JInternalFrame

.

**Parameters:** ui

- the UI delegate

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the look and feel
has changed.
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

description
="UIClassID")
public
String
getUIClassID()
```

Returns the name of the look-and-feel
class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "InternalFrameUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- isRootPaneCheckingEnabled

```java
protected boolean isRootPaneCheckingEnabled()
```

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Returns:** true if

add

and

setLayout

are forwarded; false otherwise
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- setRootPaneCheckingEnabled

```java
@BeanProperty
(
hidden
=true,

description
="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)
```

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Parameters:** enabled

- true if

add

and

setLayout

are forwarded, false if they should operate directly on the

JInternalFrame

.
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

isRootPaneCheckingEnabled()

,

RootPaneContainer

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be enhanced
**Parameters:** constraints

- the constraints to be respected
**Parameters:** index

- the index
**Throws:** IllegalArgumentException

- if

index

is invalid
**Throws:** IllegalArgumentException

- if adding the container's parent
to itself
**Throws:** IllegalArgumentException

- if adding a window to a container
**See Also:** setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- remove

```java
public void remove​(
Component
comp)
```

Removes the specified component from the container. If

comp

is not a child of the

JInternalFrame

this will forward the call to the

contentPane

.

**Overrides:** remove

in class

Container
**Parameters:** comp

- the component to be removed
**Throws:** NullPointerException

- if

comp

is null
**See Also:** Container.add(java.awt.Component)

,

RootPaneContainer

- setLayout

```java
public void setLayout​(
LayoutManager
manager)
```

Ensures that, by default, the layout of this component cannot be set.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

**Overrides:** setLayout

in class

Container
**Parameters:** manager

- the

LayoutManager
**See Also:** setRootPaneCheckingEnabled(boolean)

- getMenuBar

```java
@Deprecated

public
JMenuBar
getMenuBar()
```

Deprecated.

As of Swing version 1.0.3,
replaced by

getJMenuBar()

.

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

**Returns:** the current menu bar, or

null

if none has been set

- getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

**Returns:** the

JMenuBar

used by this internal frame
**See Also:** setJMenuBar(javax.swing.JMenuBar)

- setMenuBar

```java
@Deprecated

public void setMenuBar​(
JMenuBar
m)
```

Deprecated.

As of Swing version 1.0.3
replaced by

setJMenuBar(JMenuBar m)

.

Sets the

menuBar

property for this

JInternalFrame

.

**Parameters:** m

- the

JMenuBar

to use in this internal frame
**See Also:** getJMenuBar()

- setJMenuBar

```java
@BeanProperty
(
preferred
=true,

description
="The menu bar for accessing pulldown menus from this internal frame.")
public void setJMenuBar​(
JMenuBar
m)
```

Sets the

menuBar

property for this

JInternalFrame

.

**Parameters:** m

- the

JMenuBar

to use in this internal frame
**See Also:** getJMenuBar()

- getContentPane

```java
public
Container
getContentPane()
```

Returns the content pane for this internal frame.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the content pane
**See Also:** RootPaneContainer.setContentPane(java.awt.Container)

- setContentPane

```java
@BeanProperty
(
hidden
=true,

description
="The client area of the internal frame where child components are normally inserted.")
public void setContentPane​(
Container
c)
```

Sets this

JInternalFrame

's

contentPane

property.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** c

- the content pane for this internal frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null
**See Also:** RootPaneContainer.getContentPane()

- getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Returns the layered pane for this internal frame.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** a

JLayeredPane

object
**See Also:** RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

- setLayeredPane

```java
@BeanProperty
(
hidden
=true,

description
="The pane which holds the various desktop layers.")
public void setLayeredPane​(
JLayeredPane
layered)
```

Sets this

JInternalFrame

's

layeredPane

property.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layered

- the

JLayeredPane

for this internal frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is

null
**See Also:** RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

- getGlassPane

```java
public
Component
getGlassPane()
```

Returns the glass pane for this internal frame.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the glass pane
**See Also:** RootPaneContainer.setGlassPane(java.awt.Component)

- setGlassPane

```java
@BeanProperty
(
hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glass)
```

Sets this

JInternalFrame

's

glassPane

property.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glass

- the glass pane for this internal frame
**See Also:** RootPaneContainer.getGlassPane()

- getRootPane

```java
@BeanProperty
(
hidden
=true,

description
="The root pane used by this internal frame.")
public
JRootPane
getRootPane()
```

Returns the

rootPane

object for this internal frame.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Overrides:** getRootPane

in class

JComponent
**Returns:** the

rootPane

property
**See Also:** RootPaneContainer.getRootPane()

- setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Sets the

rootPane

property
for this

JInternalFrame

.
This method is called by the constructor.

**Parameters:** root

- the new

JRootPane

object

- setClosable

```java
@BeanProperty
(
preferred
=true,

description
="Indicates whether this internal frame can be closed.")
public void setClosable​(boolean b)
```

Sets whether this

JInternalFrame

can be closed by
some user action.

**Parameters:** b

- a boolean value, where

true

means this internal frame can be closed

- isClosable

```java
public boolean isClosable()
```

Returns whether this

JInternalFrame

can be closed by
some user action.

**Returns:** true

if this internal frame can be closed

- isClosed

```java
public boolean isClosed()
```

Returns whether this

JInternalFrame

is currently closed.

**Returns:** true

if this internal frame is closed,

false

otherwise

- setClosed

```java
@BeanProperty
(
description
="Indicates whether this internal frame has been closed.")
public void setClosed​(boolean b)
throws
PropertyVetoException
```

Closes this internal frame if the argument is

true

.
Do not invoke this method with a

false

argument;
the result of invoking

setClosed(false)

is unspecified.

If the internal frame is already closed,
this method does nothing and returns immediately.
Otherwise,
this method begins by firing
an

INTERNAL_FRAME_CLOSING

event.
Then this method sets the

closed

property to

true

unless a listener vetoes the property change.
This method finishes by making the internal frame
invisible and unselected,
and then firing an

INTERNAL_FRAME_CLOSED

event.

Note:

To reuse an internal frame that has been closed,
you must add it to a container
(even if you never removed it from its previous container).
Typically, this container will be the

JDesktopPane

that previously contained the internal frame.

**Parameters:** b

- must be

true
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame
**See Also:** isClosed()

,

setDefaultCloseOperation(int)

,

dispose()

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

- setResizable

```java
@BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be resized by the user.")
public void setResizable​(boolean b)
```

Sets whether the

JInternalFrame

can be resized by some
user action.

**Parameters:** b

- a boolean, where

true

means this internal frame can be resized

- isResizable

```java
public boolean isResizable()
```

Returns whether the

JInternalFrame

can be resized
by some user action.

**Returns:** true

if this internal frame can be resized,

false

otherwise

- setIconifiable

```java
@BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be iconified.")
public void setIconifiable​(boolean b)
```

Sets the

iconable

property,
which must be

true

for the user to be able to
make the

JInternalFrame

an icon.
Some look and feels might not implement iconification;
they will ignore this property.

**Parameters:** b

- a boolean, where

true

means this internal frame can be iconified

- isIconifiable

```java
public boolean isIconifiable()
```

Gets the

iconable

property,
which by default is

false

.

**Returns:** the value of the

iconable

property.
**See Also:** setIconifiable(boolean)

- isIcon

```java
public boolean isIcon()
```

Returns whether the

JInternalFrame

is currently iconified.

**Returns:** true

if this internal frame is iconified

- setIcon

```java
@BeanProperty
(
description
="The image displayed when this internal frame is minimized.")
public void setIcon​(boolean b)
throws
PropertyVetoException
```

Iconifies or de-iconifies this internal frame,
if the look and feel supports iconification.
If the internal frame's state changes to iconified,
this method fires an

INTERNAL_FRAME_ICONIFIED

event.
If the state changes to de-iconified,
an

INTERNAL_FRAME_DEICONIFIED

event is fired.

**Parameters:** b

- a boolean, where

true

means to iconify this internal frame and

false

means to de-iconify it
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame
**See Also:** InternalFrameEvent.INTERNAL_FRAME_ICONIFIED

,

InternalFrameEvent.INTERNAL_FRAME_DEICONIFIED

- setMaximizable

```java
@BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be maximized.")
public void setMaximizable​(boolean b)
```

Sets the

maximizable

property,
which determines whether the

JInternalFrame

can be maximized by
some user action.
Some look and feels might not support maximizing internal frames;
they will ignore this property.

**Parameters:** b

-

true

to specify that this internal frame should be maximizable;

false

to specify that it should not be

- isMaximizable

```java
public boolean isMaximizable()
```

Gets the value of the

maximizable

property.

**Returns:** the value of the

maximizable

property
**See Also:** setMaximizable(boolean)

- isMaximum

```java
public boolean isMaximum()
```

Returns whether the

JInternalFrame

is currently maximized.

**Returns:** true

if this internal frame is maximized,

false

otherwise

- setMaximum

```java
@BeanProperty
(
description
="Indicates whether this internal frame is maximized.")
public void setMaximum​(boolean b)
throws
PropertyVetoException
```

Maximizes and restores this internal frame. A maximized frame is resized to
fully fit the

JDesktopPane

area associated with the

JInternalFrame

.
A restored frame's size is set to the

JInternalFrame

's
actual size.

**Parameters:** b

- a boolean, where

true

maximizes this internal frame and

false

restores it
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame

- getTitle

```java
public
String
getTitle()
```

Returns the title of the

JInternalFrame

.

**Returns:** a

String

containing this internal frame's title
**See Also:** setTitle(java.lang.String)

- setTitle

```java
@BeanProperty
(
preferred
=true,

description
="The text displayed in the title bar.")
public void setTitle​(
String
title)
```

Sets the

JInternalFrame

title.

title

may have a

null

value.

**Parameters:** title

- the

String

to display in the title bar
**See Also:** getTitle()

- setSelected

```java
@BeanProperty
(
description
="Indicates whether this internal frame is currently the active frame.")
public void setSelected​(boolean selected)
throws
PropertyVetoException
```

Selects or deselects the internal frame
if it's showing.
A

JInternalFrame

normally draws its title bar
differently if it is
the selected frame, which indicates to the user that this
internal frame has the focus.
When this method changes the state of the internal frame
from deselected to selected, it fires an

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

event.
If the change is from selected to deselected,
an

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

event
is fired.

**Parameters:** selected

- a boolean, where

true

means this internal frame
should become selected (currently active)
and

false

means it should become deselected
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame
**See Also:** Component.isShowing()

,

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

,

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

- isSelected

```java
public boolean isSelected()
```

Returns whether the

JInternalFrame

is the
currently "selected" or active frame.

**Returns:** true

if this internal frame is currently selected (active)
**See Also:** setSelected(boolean)

- setFrameIcon

```java
@BeanProperty
(
description
="The icon shown in the top-left corner of this internal frame.")
public void setFrameIcon​(
Icon
icon)
```

Sets an image to be displayed in the titlebar of this internal frame (usually
in the top-left corner).
Some look and feels might not support displaying an icon in the titlebar.

This image is not the

desktopIcon

object, which
is the image displayed in the

JDesktop

when
this internal frame is iconified.

Passing

null

to this function is valid,
but the look and feel can choose the appropriate behavior
for that situation, such as displaying no icon
or a default icon for the look and feel.

**Parameters:** icon

- the

Icon

to display in the title bar
**See Also:** getFrameIcon()

- getFrameIcon

```java
public
Icon
getFrameIcon()
```

Returns the image displayed in the title bar of this internal frame (usually
in the top-left corner).

**Returns:** the

Icon

displayed in the title bar
**See Also:** setFrameIcon(javax.swing.Icon)

- moveToFront

```java
public void moveToFront()
```

Convenience method that moves this component to position 0 if its
parent is a

JLayeredPane

.

- moveToBack

```java
public void moveToBack()
```

Convenience method that moves this component to position -1 if its
parent is a

JLayeredPane

.

- getLastCursor

```java
@BeanProperty
(
bound
=false)
public
Cursor
getLastCursor()
```

Returns the last

Cursor

that was set by the

setCursor

method that is not a resizable

Cursor

.

**Returns:** the last non-resizable

Cursor
**Since:** 1.6

- setCursor

```java
public void setCursor​(
Cursor
cursor)
```

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

**Overrides:** setCursor

in class

Component
**Parameters:** cursor

- One of the constants defined
by the

Cursor

class;
if this parameter is

null

then this component will inherit
the cursor of its parent
**Since:** 1.6
**See Also:** Component.isEnabled()

,

Component.isShowing()

,

Component.getCursor()

,

Component.contains(int, int)

,

Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

,

Cursor

- setLayer

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Specifies what desktop layer is used.")
public void setLayer​(
Integer
layer)
```

Convenience method for setting the layer attribute of this component.

**Parameters:** layer

- an

Integer

object specifying this
frame's desktop layer
**Throws:** NullPointerException

- if

layer

is

null
**See Also:** JLayeredPane

- setLayer

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Specifies what desktop layer is used.")
public void setLayer​(int layer)
```

Convenience method for setting the layer attribute of this component.
The method

setLayer(Integer)

should be used for
layer values predefined in

JLayeredPane

.
When using

setLayer(int)

, care must be taken not to
accidentally clash with those values.

**Parameters:** layer

- an integer specifying this internal frame's desktop layer
**Since:** 1.3
**See Also:** setLayer(Integer)

,

JLayeredPane

- getLayer

```java
public int getLayer()
```

Convenience method for getting the layer attribute of this component.

**Returns:** an

Integer

object specifying this
frame's desktop layer
**See Also:** JLayeredPane

- getDesktopPane

```java
@BeanProperty
(
bound
=false)
public
JDesktopPane
getDesktopPane()
```

Convenience method that searches the ancestor hierarchy for a

JDesktop

instance. If

JInternalFrame

finds none, the

desktopIcon

tree is searched.

**Returns:** the

JDesktopPane

this internal frame belongs to,
or

null

if none is found

- setDesktopIcon

```java
@BeanProperty
(
description
="The icon shown when this internal frame is minimized.")
public void setDesktopIcon​(
JInternalFrame.JDesktopIcon
d)
```

Sets the

JDesktopIcon

associated with this

JInternalFrame

.

**Parameters:** d

- the

JDesktopIcon

to display on the desktop
**See Also:** getDesktopIcon()

- getDesktopIcon

```java
public
JInternalFrame.JDesktopIcon
getDesktopIcon()
```

Returns the

JDesktopIcon

used when this

JInternalFrame

is iconified.

**Returns:** the

JDesktopIcon

displayed on the desktop
**See Also:** setDesktopIcon(javax.swing.JInternalFrame.JDesktopIcon)

- getNormalBounds

```java
public
Rectangle
getNormalBounds()
```

If the

JInternalFrame

is not in maximized state, returns

getBounds()

; otherwise, returns the bounds that the

JInternalFrame

would be restored to.

**Returns:** a

Rectangle

containing the bounds of this
frame when in the normal state
**Since:** 1.3

- setNormalBounds

```java
public void setNormalBounds​(
Rectangle
r)
```

Sets the normal bounds for this internal frame, the bounds that
this internal frame would be restored to from its maximized state.
This method is intended for use only by desktop managers.

**Parameters:** r

- the bounds that this internal frame should be restored to
**Since:** 1.3

- getFocusOwner

```java
public
Component
getFocusOwner()
```

If this

JInternalFrame

is active,
returns the child that has focus.
Otherwise, returns

null

.

**Returns:** the component with focus, or

null

if no children have focus
**Since:** 1.3

- getMostRecentFocusOwner

```java
@BeanProperty
(
bound
=false)
public
Component
getMostRecentFocusOwner()
```

Returns the child component of this

JInternalFrame

that will receive the
focus when this

JInternalFrame

is selected.
If this

JInternalFrame

is
currently selected, this method returns the same component as
the

getFocusOwner

method.
If this

JInternalFrame

is not selected,
then the child component that most recently requested focus will be
returned. If no child component has ever requested focus, then this

JInternalFrame

's initial focusable component is returned.
If no such
child exists, then this

JInternalFrame

's default component
to focus is returned.

**Returns:** the child component that will receive focus when this

JInternalFrame

is selected
**Since:** 1.4
**See Also:** getFocusOwner()

,

isSelected

- restoreSubcomponentFocus

```java
public void restoreSubcomponentFocus()
```

Requests the internal frame to restore focus to the
last subcomponent that had focus. This is used by the UI when
the user selected this internal frame --
for example, by clicking on the title bar.

**Since:** 1.3

- reshape

```java
public void reshape​(int x,
int y,
int width,
int height)
```

Moves and resizes this component. Unlike other components,
this implementation also forces re-layout, so that frame
decorations such as the title bar are always redisplayed.

**Overrides:** reshape

in class

JComponent
**Parameters:** x

- an integer giving the component's new horizontal position
measured in pixels from the left of its container
**Parameters:** y

- an integer giving the component's new vertical position,
measured in pixels from the bottom of its container
**Parameters:** width

- an integer giving the component's new width in pixels
**Parameters:** height

- an integer giving the component's new height in pixels
**See Also:** Component.setBounds(int, int, int, int)

- addInternalFrameListener

```java
public void addInternalFrameListener​(
InternalFrameListener
l)
```

Adds the specified listener to receive internal
frame events from this internal frame.

**Parameters:** l

- the internal frame listener

- removeInternalFrameListener

```java
public void removeInternalFrameListener​(
InternalFrameListener
l)
```

Removes the specified internal frame listener so that it no longer
receives internal frame events from this internal frame.

**Parameters:** l

- the internal frame listener

- getInternalFrameListeners

```java
@BeanProperty
(
bound
=false)
public
InternalFrameListener
[] getInternalFrameListeners()
```

Returns an array of all the

InternalFrameListener

s added
to this

JInternalFrame

with

addInternalFrameListener

.

**Returns:** all of the

InternalFrameListener

s added or an empty
array if no listeners have been added
**Since:** 1.4
**See Also:** addInternalFrameListener(javax.swing.event.InternalFrameListener)

- fireInternalFrameEvent

```java
protected void fireInternalFrameEvent​(int id)
```

Fires an internal frame event.

**Parameters:** id

- the type of the event being fired; one of the following:

- InternalFrameEvent.INTERNAL_FRAME_OPENED

InternalFrameEvent.INTERNAL_FRAME_CLOSING

InternalFrameEvent.INTERNAL_FRAME_CLOSED

InternalFrameEvent.INTERNAL_FRAME_ICONIFIED

InternalFrameEvent.INTERNAL_FRAME_DEICONIFIED

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

If the event type is not one of the above, nothing happens.

- doDefaultCloseAction

```java
public void doDefaultCloseAction()
```

Fires an

INTERNAL_FRAME_CLOSING

event
and then performs the action specified by
the internal frame's default close operation.
This method is typically invoked by the
look-and-feel-implemented action handler
for the internal frame's close button.

**Since:** 1.3
**See Also:** setDefaultCloseOperation(int)

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

- setDefaultCloseOperation

```java
public void setDefaultCloseOperation​(int operation)
```

Sets the operation that will happen by default when
the user initiates a "close" on this internal frame.
The possible choices are:

The default value is

DISPOSE_ON_CLOSE

.
Before performing the specified close operation,
the internal frame fires
an

INTERNAL_FRAME_CLOSING

event.

**Parameters:** operation

- one of the following constants defined in

javax.swing.WindowConstants

(an interface implemented by

JInternalFrame

):

DO_NOTHING_ON_CLOSE

,

HIDE_ON_CLOSE

, or

DISPOSE_ON_CLOSE
**See Also:** addInternalFrameListener(javax.swing.event.InternalFrameListener)

,

getDefaultCloseOperation()

,

JComponent.setVisible(boolean)

,

dispose()

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

- getDefaultCloseOperation

```java
public int getDefaultCloseOperation()
```

Returns the default operation that occurs when the user
initiates a "close" on this internal frame.

**Returns:** the operation that will occur when the user closes the internal
frame
**See Also:** setDefaultCloseOperation(int)

- pack

```java
public void pack()
```

Causes subcomponents of this

JInternalFrame

to be laid out at their preferred size. Internal frames that are
iconized or maximized are first restored and then packed. If the
internal frame is unable to be restored its state is not changed
and will not be packed.

**See Also:** Window.pack()

- show

```java
public void show()
```

If the internal frame is not visible,
brings the internal frame to the front,
makes it visible,
and attempts to select it.
The first time the internal frame is made visible,
this method also fires an

INTERNAL_FRAME_OPENED

event.
This method does nothing if the internal frame is already visible.
Invoking this method
has the same result as invoking

setVisible(true)

.

**Overrides:** show

in class

Component
**See Also:** moveToFront()

,

setSelected(boolean)

,

InternalFrameEvent.INTERNAL_FRAME_OPENED

,

JComponent.setVisible(boolean)

- dispose

```java
public void dispose()
```

Makes this internal frame
invisible, unselected, and closed.
If the frame is not already closed,
this method fires an

INTERNAL_FRAME_CLOSED

event.
The results of invoking this method are similar to

setClosed(true)

,
but

dispose

always succeeds in closing
the internal frame and does not fire
an

INTERNAL_FRAME_CLOSING

event.

**See Also:** InternalFrameEvent.INTERNAL_FRAME_CLOSED

,

JComponent.setVisible(boolean)

,

setSelected(boolean)

,

setClosed(boolean)

- toFront

```java
public void toFront()
```

Brings this internal frame to the front.
Places this internal frame at the top of the stacking order
and makes the corresponding adjustment to other visible internal
frames.

**See Also:** Window.toFront()

,

moveToFront()

- toBack

```java
public void toBack()
```

Sends this internal frame to the back.
Places this internal frame at the bottom of the stacking order
and makes the corresponding adjustment to other visible
internal frames.

**See Also:** Window.toBack()

,

moveToBack()

- setFocusCycleRoot

```java
public final void setFocusCycleRoot​(boolean focusCycleRoot)
```

Does nothing because

JInternalFrame

s must always be roots of a focus
traversal cycle.

**Overrides:** setFocusCycleRoot

in class

Container
**Parameters:** focusCycleRoot

- this value is ignored
**Since:** 1.4
**See Also:** isFocusCycleRoot()

,

Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

Container.getFocusTraversalPolicy()

- isFocusCycleRoot

```java
public final boolean isFocusCycleRoot()
```

Always returns

true

because all

JInternalFrame

s must be
roots of a focus traversal cycle.

**Overrides:** isFocusCycleRoot

in class

Container
**Returns:** true
**Since:** 1.4
**See Also:** setFocusCycleRoot(boolean)

,

Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

Container.getFocusTraversalPolicy()

- getFocusCycleRootAncestor

```java
@BeanProperty
(
bound
=false)
public final
Container
getFocusCycleRootAncestor()
```

Always returns

null

because

JInternalFrame

s
must always be roots of a focus
traversal cycle.

**Overrides:** getFocusCycleRootAncestor

in class

Component
**Returns:** null
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

- getWarningString

```java
@BeanProperty
(
bound
=false)
public final
String
getWarningString()
```

Gets the warning string that is displayed with this internal frame.
Since an internal frame is always secure (since it's fully
contained within a window that might need a warning string)
this method always returns

null

.

**Returns:** null
**See Also:** Window.getWarningString()

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JInternalFrame

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

JInternalFrame

- paintComponent

```java
protected void paintComponent​(
Graphics
g)
```

Overridden to allow optimized painting when the
internal frame is being dragged.

**Overrides:** paintComponent

in class

JComponent
**Parameters:** g

- the

Graphics

object to protect
**See Also:** JComponent.paint(java.awt.Graphics)

,

ComponentUI

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

Gets the

AccessibleContext

associated with this

JInternalFrame

.
For internal frames, the

AccessibleContext

takes the form of an

AccessibleJInternalFrame

object.
A new

AccessibleJInternalFrame

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleJInternalFrame

that serves as the

AccessibleContext

of this

JInternalFrame
**See Also:** JInternalFrame.AccessibleJInternalFrame

---

#### Method Detail

createRootPane

```java
protected
JRootPane
createRootPane()
```

Called by the constructor to set up the

JRootPane

.

**Returns:** a new

JRootPane
**See Also:** JRootPane

---

#### createRootPane

protected

JRootPane

createRootPane()

Called by the constructor to set up the

JRootPane

.

getUI

```java
public
InternalFrameUI
getUI()
```

Returns the look-and-feel object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

InternalFrameUI

object that renders
this component

---

#### getUI

public

InternalFrameUI

getUI()

Returns the look-and-feel object that renders this component.

setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
InternalFrameUI
ui)
```

Sets the UI delegate for this

JInternalFrame

.

**Parameters:** ui

- the UI delegate

---

#### setUI

@BeanProperty

(

hidden

=true,

visualUpdate

=true,

description

="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(

InternalFrameUI

ui)

Sets the UI delegate for this

JInternalFrame

.

updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the look and feel
has changed.
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

that the look and feel
has changed.
Replaces the current UI object with the latest version from the

UIManager

.

getUIClassID

```java
@BeanProperty
(
bound
=false,

description
="UIClassID")
public
String
getUIClassID()
```

Returns the name of the look-and-feel
class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "InternalFrameUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false,

description

="UIClassID")
public

String

getUIClassID()

Returns the name of the look-and-feel
class that renders this component.

isRootPaneCheckingEnabled

```java
protected boolean isRootPaneCheckingEnabled()
```

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Returns:** true if

add

and

setLayout

are forwarded; false otherwise
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### isRootPaneCheckingEnabled

protected boolean isRootPaneCheckingEnabled()

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

setRootPaneCheckingEnabled

```java
@BeanProperty
(
hidden
=true,

description
="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)
```

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Parameters:** enabled

- true if

add

and

setLayout

are forwarded, false if they should operate directly on the

JInternalFrame

.
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

isRootPaneCheckingEnabled()

,

RootPaneContainer

---

#### setRootPaneCheckingEnabled

@BeanProperty

(

hidden

=true,

description

="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be enhanced
**Parameters:** constraints

- the constraints to be respected
**Parameters:** index

- the index
**Throws:** IllegalArgumentException

- if

index

is invalid
**Throws:** IllegalArgumentException

- if adding the container's parent
to itself
**Throws:** IllegalArgumentException

- if adding a window to a container
**See Also:** setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### addImpl

protected void addImpl​(

Component

comp,

Object

constraints,
int index)

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

remove

```java
public void remove​(
Component
comp)
```

Removes the specified component from the container. If

comp

is not a child of the

JInternalFrame

this will forward the call to the

contentPane

.

**Overrides:** remove

in class

Container
**Parameters:** comp

- the component to be removed
**Throws:** NullPointerException

- if

comp

is null
**See Also:** Container.add(java.awt.Component)

,

RootPaneContainer

---

#### remove

public void remove​(

Component

comp)

Removes the specified component from the container. If

comp

is not a child of the

JInternalFrame

this will forward the call to the

contentPane

.

setLayout

```java
public void setLayout​(
LayoutManager
manager)
```

Ensures that, by default, the layout of this component cannot be set.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

**Overrides:** setLayout

in class

Container
**Parameters:** manager

- the

LayoutManager
**See Also:** setRootPaneCheckingEnabled(boolean)

---

#### setLayout

public void setLayout​(

LayoutManager

manager)

Ensures that, by default, the layout of this component cannot be set.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

getMenuBar

```java
@Deprecated

public
JMenuBar
getMenuBar()
```

Deprecated.

As of Swing version 1.0.3,
replaced by

getJMenuBar()

.

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

**Returns:** the current menu bar, or

null

if none has been set

---

#### getMenuBar

@Deprecated

public

JMenuBar

getMenuBar()

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

**Returns:** the

JMenuBar

used by this internal frame
**See Also:** setJMenuBar(javax.swing.JMenuBar)

---

#### getJMenuBar

public

JMenuBar

getJMenuBar()

Returns the current

JMenuBar

for this

JInternalFrame

, or

null

if no menu bar has been set.

setMenuBar

```java
@Deprecated

public void setMenuBar​(
JMenuBar
m)
```

Deprecated.

As of Swing version 1.0.3
replaced by

setJMenuBar(JMenuBar m)

.

Sets the

menuBar

property for this

JInternalFrame

.

**Parameters:** m

- the

JMenuBar

to use in this internal frame
**See Also:** getJMenuBar()

---

#### setMenuBar

@Deprecated

public void setMenuBar​(

JMenuBar

m)

Sets the

menuBar

property for this

JInternalFrame

.

setJMenuBar

```java
@BeanProperty
(
preferred
=true,

description
="The menu bar for accessing pulldown menus from this internal frame.")
public void setJMenuBar​(
JMenuBar
m)
```

Sets the

menuBar

property for this

JInternalFrame

.

**Parameters:** m

- the

JMenuBar

to use in this internal frame
**See Also:** getJMenuBar()

---

#### setJMenuBar

@BeanProperty

(

preferred

=true,

description

="The menu bar for accessing pulldown menus from this internal frame.")
public void setJMenuBar​(

JMenuBar

m)

Sets the

menuBar

property for this

JInternalFrame

.

getContentPane

```java
public
Container
getContentPane()
```

Returns the content pane for this internal frame.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the content pane
**See Also:** RootPaneContainer.setContentPane(java.awt.Container)

---

#### getContentPane

public

Container

getContentPane()

Returns the content pane for this internal frame.

setContentPane

```java
@BeanProperty
(
hidden
=true,

description
="The client area of the internal frame where child components are normally inserted.")
public void setContentPane​(
Container
c)
```

Sets this

JInternalFrame

's

contentPane

property.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** c

- the content pane for this internal frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null
**See Also:** RootPaneContainer.getContentPane()

---

#### setContentPane

@BeanProperty

(

hidden

=true,

description

="The client area of the internal frame where child components are normally inserted.")
public void setContentPane​(

Container

c)

Sets this

JInternalFrame

's

contentPane

property.

getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Returns the layered pane for this internal frame.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** a

JLayeredPane

object
**See Also:** RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

---

#### getLayeredPane

public

JLayeredPane

getLayeredPane()

Returns the layered pane for this internal frame.

setLayeredPane

```java
@BeanProperty
(
hidden
=true,

description
="The pane which holds the various desktop layers.")
public void setLayeredPane​(
JLayeredPane
layered)
```

Sets this

JInternalFrame

's

layeredPane

property.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layered

- the

JLayeredPane

for this internal frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is

null
**See Also:** RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

---

#### setLayeredPane

@BeanProperty

(

hidden

=true,

description

="The pane which holds the various desktop layers.")
public void setLayeredPane​(

JLayeredPane

layered)

Sets this

JInternalFrame

's

layeredPane

property.

getGlassPane

```java
public
Component
getGlassPane()
```

Returns the glass pane for this internal frame.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the glass pane
**See Also:** RootPaneContainer.setGlassPane(java.awt.Component)

---

#### getGlassPane

public

Component

getGlassPane()

Returns the glass pane for this internal frame.

setGlassPane

```java
@BeanProperty
(
hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glass)
```

Sets this

JInternalFrame

's

glassPane

property.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glass

- the glass pane for this internal frame
**See Also:** RootPaneContainer.getGlassPane()

---

#### setGlassPane

@BeanProperty

(

hidden

=true,

description

="A transparent pane used for menu rendering.")
public void setGlassPane​(

Component

glass)

Sets this

JInternalFrame

's

glassPane

property.

getRootPane

```java
@BeanProperty
(
hidden
=true,

description
="The root pane used by this internal frame.")
public
JRootPane
getRootPane()
```

Returns the

rootPane

object for this internal frame.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Overrides:** getRootPane

in class

JComponent
**Returns:** the

rootPane

property
**See Also:** RootPaneContainer.getRootPane()

---

#### getRootPane

@BeanProperty

(

hidden

=true,

description

="The root pane used by this internal frame.")
public

JRootPane

getRootPane()

Returns the

rootPane

object for this internal frame.

setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Sets the

rootPane

property
for this

JInternalFrame

.
This method is called by the constructor.

**Parameters:** root

- the new

JRootPane

object

---

#### setRootPane

protected void setRootPane​(

JRootPane

root)

Sets the

rootPane

property
for this

JInternalFrame

.
This method is called by the constructor.

setClosable

```java
@BeanProperty
(
preferred
=true,

description
="Indicates whether this internal frame can be closed.")
public void setClosable​(boolean b)
```

Sets whether this

JInternalFrame

can be closed by
some user action.

**Parameters:** b

- a boolean value, where

true

means this internal frame can be closed

---

#### setClosable

@BeanProperty

(

preferred

=true,

description

="Indicates whether this internal frame can be closed.")
public void setClosable​(boolean b)

Sets whether this

JInternalFrame

can be closed by
some user action.

isClosable

```java
public boolean isClosable()
```

Returns whether this

JInternalFrame

can be closed by
some user action.

**Returns:** true

if this internal frame can be closed

---

#### isClosable

public boolean isClosable()

Returns whether this

JInternalFrame

can be closed by
some user action.

isClosed

```java
public boolean isClosed()
```

Returns whether this

JInternalFrame

is currently closed.

**Returns:** true

if this internal frame is closed,

false

otherwise

---

#### isClosed

public boolean isClosed()

Returns whether this

JInternalFrame

is currently closed.

setClosed

```java
@BeanProperty
(
description
="Indicates whether this internal frame has been closed.")
public void setClosed​(boolean b)
throws
PropertyVetoException
```

Closes this internal frame if the argument is

true

.
Do not invoke this method with a

false

argument;
the result of invoking

setClosed(false)

is unspecified.

If the internal frame is already closed,
this method does nothing and returns immediately.
Otherwise,
this method begins by firing
an

INTERNAL_FRAME_CLOSING

event.
Then this method sets the

closed

property to

true

unless a listener vetoes the property change.
This method finishes by making the internal frame
invisible and unselected,
and then firing an

INTERNAL_FRAME_CLOSED

event.

Note:

To reuse an internal frame that has been closed,
you must add it to a container
(even if you never removed it from its previous container).
Typically, this container will be the

JDesktopPane

that previously contained the internal frame.

**Parameters:** b

- must be

true
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame
**See Also:** isClosed()

,

setDefaultCloseOperation(int)

,

dispose()

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

---

#### setClosed

@BeanProperty

(

description

="Indicates whether this internal frame has been closed.")
public void setClosed​(boolean b)
throws

PropertyVetoException

Closes this internal frame if the argument is

true

.
Do not invoke this method with a

false

argument;
the result of invoking

setClosed(false)

is unspecified.

If the internal frame is already closed,
this method does nothing and returns immediately.
Otherwise,
this method begins by firing
an

INTERNAL_FRAME_CLOSING

event.
Then this method sets the

closed

property to

true

unless a listener vetoes the property change.
This method finishes by making the internal frame
invisible and unselected,
and then firing an

INTERNAL_FRAME_CLOSED

event.

Note:

To reuse an internal frame that has been closed,
you must add it to a container
(even if you never removed it from its previous container).
Typically, this container will be the

JDesktopPane

that previously contained the internal frame.

If the internal frame is already closed,
this method does nothing and returns immediately.
Otherwise,
this method begins by firing
an

INTERNAL_FRAME_CLOSING

event.
Then this method sets the

closed

property to

true

unless a listener vetoes the property change.
This method finishes by making the internal frame
invisible and unselected,
and then firing an

INTERNAL_FRAME_CLOSED

event.

Note:

To reuse an internal frame that has been closed,
you must add it to a container
(even if you never removed it from its previous container).
Typically, this container will be the

JDesktopPane

that previously contained the internal frame.

Note:

To reuse an internal frame that has been closed,
you must add it to a container
(even if you never removed it from its previous container).
Typically, this container will be the

JDesktopPane

that previously contained the internal frame.

setResizable

```java
@BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be resized by the user.")
public void setResizable​(boolean b)
```

Sets whether the

JInternalFrame

can be resized by some
user action.

**Parameters:** b

- a boolean, where

true

means this internal frame can be resized

---

#### setResizable

@BeanProperty

(

preferred

=true,

description

="Determines whether this internal frame can be resized by the user.")
public void setResizable​(boolean b)

Sets whether the

JInternalFrame

can be resized by some
user action.

isResizable

```java
public boolean isResizable()
```

Returns whether the

JInternalFrame

can be resized
by some user action.

**Returns:** true

if this internal frame can be resized,

false

otherwise

---

#### isResizable

public boolean isResizable()

Returns whether the

JInternalFrame

can be resized
by some user action.

setIconifiable

```java
@BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be iconified.")
public void setIconifiable​(boolean b)
```

Sets the

iconable

property,
which must be

true

for the user to be able to
make the

JInternalFrame

an icon.
Some look and feels might not implement iconification;
they will ignore this property.

**Parameters:** b

- a boolean, where

true

means this internal frame can be iconified

---

#### setIconifiable

@BeanProperty

(

preferred

=true,

description

="Determines whether this internal frame can be iconified.")
public void setIconifiable​(boolean b)

Sets the

iconable

property,
which must be

true

for the user to be able to
make the

JInternalFrame

an icon.
Some look and feels might not implement iconification;
they will ignore this property.

isIconifiable

```java
public boolean isIconifiable()
```

Gets the

iconable

property,
which by default is

false

.

**Returns:** the value of the

iconable

property.
**See Also:** setIconifiable(boolean)

---

#### isIconifiable

public boolean isIconifiable()

Gets the

iconable

property,
which by default is

false

.

isIcon

```java
public boolean isIcon()
```

Returns whether the

JInternalFrame

is currently iconified.

**Returns:** true

if this internal frame is iconified

---

#### isIcon

public boolean isIcon()

Returns whether the

JInternalFrame

is currently iconified.

setIcon

```java
@BeanProperty
(
description
="The image displayed when this internal frame is minimized.")
public void setIcon​(boolean b)
throws
PropertyVetoException
```

Iconifies or de-iconifies this internal frame,
if the look and feel supports iconification.
If the internal frame's state changes to iconified,
this method fires an

INTERNAL_FRAME_ICONIFIED

event.
If the state changes to de-iconified,
an

INTERNAL_FRAME_DEICONIFIED

event is fired.

**Parameters:** b

- a boolean, where

true

means to iconify this internal frame and

false

means to de-iconify it
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame
**See Also:** InternalFrameEvent.INTERNAL_FRAME_ICONIFIED

,

InternalFrameEvent.INTERNAL_FRAME_DEICONIFIED

---

#### setIcon

@BeanProperty

(

description

="The image displayed when this internal frame is minimized.")
public void setIcon​(boolean b)
throws

PropertyVetoException

Iconifies or de-iconifies this internal frame,
if the look and feel supports iconification.
If the internal frame's state changes to iconified,
this method fires an

INTERNAL_FRAME_ICONIFIED

event.
If the state changes to de-iconified,
an

INTERNAL_FRAME_DEICONIFIED

event is fired.

setMaximizable

```java
@BeanProperty
(
preferred
=true,

description
="Determines whether this internal frame can be maximized.")
public void setMaximizable​(boolean b)
```

Sets the

maximizable

property,
which determines whether the

JInternalFrame

can be maximized by
some user action.
Some look and feels might not support maximizing internal frames;
they will ignore this property.

**Parameters:** b

-

true

to specify that this internal frame should be maximizable;

false

to specify that it should not be

---

#### setMaximizable

@BeanProperty

(

preferred

=true,

description

="Determines whether this internal frame can be maximized.")
public void setMaximizable​(boolean b)

Sets the

maximizable

property,
which determines whether the

JInternalFrame

can be maximized by
some user action.
Some look and feels might not support maximizing internal frames;
they will ignore this property.

isMaximizable

```java
public boolean isMaximizable()
```

Gets the value of the

maximizable

property.

**Returns:** the value of the

maximizable

property
**See Also:** setMaximizable(boolean)

---

#### isMaximizable

public boolean isMaximizable()

Gets the value of the

maximizable

property.

isMaximum

```java
public boolean isMaximum()
```

Returns whether the

JInternalFrame

is currently maximized.

**Returns:** true

if this internal frame is maximized,

false

otherwise

---

#### isMaximum

public boolean isMaximum()

Returns whether the

JInternalFrame

is currently maximized.

setMaximum

```java
@BeanProperty
(
description
="Indicates whether this internal frame is maximized.")
public void setMaximum​(boolean b)
throws
PropertyVetoException
```

Maximizes and restores this internal frame. A maximized frame is resized to
fully fit the

JDesktopPane

area associated with the

JInternalFrame

.
A restored frame's size is set to the

JInternalFrame

's
actual size.

**Parameters:** b

- a boolean, where

true

maximizes this internal frame and

false

restores it
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame

---

#### setMaximum

@BeanProperty

(

description

="Indicates whether this internal frame is maximized.")
public void setMaximum​(boolean b)
throws

PropertyVetoException

Maximizes and restores this internal frame. A maximized frame is resized to
fully fit the

JDesktopPane

area associated with the

JInternalFrame

.
A restored frame's size is set to the

JInternalFrame

's
actual size.

getTitle

```java
public
String
getTitle()
```

Returns the title of the

JInternalFrame

.

**Returns:** a

String

containing this internal frame's title
**See Also:** setTitle(java.lang.String)

---

#### getTitle

public

String

getTitle()

Returns the title of the

JInternalFrame

.

setTitle

```java
@BeanProperty
(
preferred
=true,

description
="The text displayed in the title bar.")
public void setTitle​(
String
title)
```

Sets the

JInternalFrame

title.

title

may have a

null

value.

**Parameters:** title

- the

String

to display in the title bar
**See Also:** getTitle()

---

#### setTitle

@BeanProperty

(

preferred

=true,

description

="The text displayed in the title bar.")
public void setTitle​(

String

title)

Sets the

JInternalFrame

title.

title

may have a

null

value.

setSelected

```java
@BeanProperty
(
description
="Indicates whether this internal frame is currently the active frame.")
public void setSelected​(boolean selected)
throws
PropertyVetoException
```

Selects or deselects the internal frame
if it's showing.
A

JInternalFrame

normally draws its title bar
differently if it is
the selected frame, which indicates to the user that this
internal frame has the focus.
When this method changes the state of the internal frame
from deselected to selected, it fires an

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

event.
If the change is from selected to deselected,
an

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

event
is fired.

**Parameters:** selected

- a boolean, where

true

means this internal frame
should become selected (currently active)
and

false

means it should become deselected
**Throws:** PropertyVetoException

- when the attempt to set the
property is vetoed by the

JInternalFrame
**See Also:** Component.isShowing()

,

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

,

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

---

#### setSelected

@BeanProperty

(

description

="Indicates whether this internal frame is currently the active frame.")
public void setSelected​(boolean selected)
throws

PropertyVetoException

Selects or deselects the internal frame
if it's showing.
A

JInternalFrame

normally draws its title bar
differently if it is
the selected frame, which indicates to the user that this
internal frame has the focus.
When this method changes the state of the internal frame
from deselected to selected, it fires an

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

event.
If the change is from selected to deselected,
an

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

event
is fired.

isSelected

```java
public boolean isSelected()
```

Returns whether the

JInternalFrame

is the
currently "selected" or active frame.

**Returns:** true

if this internal frame is currently selected (active)
**See Also:** setSelected(boolean)

---

#### isSelected

public boolean isSelected()

Returns whether the

JInternalFrame

is the
currently "selected" or active frame.

setFrameIcon

```java
@BeanProperty
(
description
="The icon shown in the top-left corner of this internal frame.")
public void setFrameIcon​(
Icon
icon)
```

Sets an image to be displayed in the titlebar of this internal frame (usually
in the top-left corner).
Some look and feels might not support displaying an icon in the titlebar.

This image is not the

desktopIcon

object, which
is the image displayed in the

JDesktop

when
this internal frame is iconified.

Passing

null

to this function is valid,
but the look and feel can choose the appropriate behavior
for that situation, such as displaying no icon
or a default icon for the look and feel.

**Parameters:** icon

- the

Icon

to display in the title bar
**See Also:** getFrameIcon()

---

#### setFrameIcon

@BeanProperty

(

description

="The icon shown in the top-left corner of this internal frame.")
public void setFrameIcon​(

Icon

icon)

Sets an image to be displayed in the titlebar of this internal frame (usually
in the top-left corner).
Some look and feels might not support displaying an icon in the titlebar.

This image is not the

desktopIcon

object, which
is the image displayed in the

JDesktop

when
this internal frame is iconified.

Passing

null

to this function is valid,
but the look and feel can choose the appropriate behavior
for that situation, such as displaying no icon
or a default icon for the look and feel.

getFrameIcon

```java
public
Icon
getFrameIcon()
```

Returns the image displayed in the title bar of this internal frame (usually
in the top-left corner).

**Returns:** the

Icon

displayed in the title bar
**See Also:** setFrameIcon(javax.swing.Icon)

---

#### getFrameIcon

public

Icon

getFrameIcon()

Returns the image displayed in the title bar of this internal frame (usually
in the top-left corner).

moveToFront

```java
public void moveToFront()
```

Convenience method that moves this component to position 0 if its
parent is a

JLayeredPane

.

---

#### moveToFront

public void moveToFront()

Convenience method that moves this component to position 0 if its
parent is a

JLayeredPane

.

moveToBack

```java
public void moveToBack()
```

Convenience method that moves this component to position -1 if its
parent is a

JLayeredPane

.

---

#### moveToBack

public void moveToBack()

Convenience method that moves this component to position -1 if its
parent is a

JLayeredPane

.

getLastCursor

```java
@BeanProperty
(
bound
=false)
public
Cursor
getLastCursor()
```

Returns the last

Cursor

that was set by the

setCursor

method that is not a resizable

Cursor

.

**Returns:** the last non-resizable

Cursor
**Since:** 1.6

---

#### getLastCursor

@BeanProperty

(

bound

=false)
public

Cursor

getLastCursor()

Returns the last

Cursor

that was set by the

setCursor

method that is not a resizable

Cursor

.

setCursor

```java
public void setCursor​(
Cursor
cursor)
```

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

**Overrides:** setCursor

in class

Component
**Parameters:** cursor

- One of the constants defined
by the

Cursor

class;
if this parameter is

null

then this component will inherit
the cursor of its parent
**Since:** 1.6
**See Also:** Component.isEnabled()

,

Component.isShowing()

,

Component.getCursor()

,

Component.contains(int, int)

,

Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

,

Cursor

---

#### setCursor

public void setCursor​(

Cursor

cursor)

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

setLayer

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Specifies what desktop layer is used.")
public void setLayer​(
Integer
layer)
```

Convenience method for setting the layer attribute of this component.

**Parameters:** layer

- an

Integer

object specifying this
frame's desktop layer
**Throws:** NullPointerException

- if

layer

is

null
**See Also:** JLayeredPane

---

#### setLayer

@BeanProperty

(

bound

=false,

expert

=true,

description

="Specifies what desktop layer is used.")
public void setLayer​(

Integer

layer)

Convenience method for setting the layer attribute of this component.

setLayer

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Specifies what desktop layer is used.")
public void setLayer​(int layer)
```

Convenience method for setting the layer attribute of this component.
The method

setLayer(Integer)

should be used for
layer values predefined in

JLayeredPane

.
When using

setLayer(int)

, care must be taken not to
accidentally clash with those values.

**Parameters:** layer

- an integer specifying this internal frame's desktop layer
**Since:** 1.3
**See Also:** setLayer(Integer)

,

JLayeredPane

---

#### setLayer

@BeanProperty

(

bound

=false,

expert

=true,

description

="Specifies what desktop layer is used.")
public void setLayer​(int layer)

Convenience method for setting the layer attribute of this component.
The method

setLayer(Integer)

should be used for
layer values predefined in

JLayeredPane

.
When using

setLayer(int)

, care must be taken not to
accidentally clash with those values.

getLayer

```java
public int getLayer()
```

Convenience method for getting the layer attribute of this component.

**Returns:** an

Integer

object specifying this
frame's desktop layer
**See Also:** JLayeredPane

---

#### getLayer

public int getLayer()

Convenience method for getting the layer attribute of this component.

getDesktopPane

```java
@BeanProperty
(
bound
=false)
public
JDesktopPane
getDesktopPane()
```

Convenience method that searches the ancestor hierarchy for a

JDesktop

instance. If

JInternalFrame

finds none, the

desktopIcon

tree is searched.

**Returns:** the

JDesktopPane

this internal frame belongs to,
or

null

if none is found

---

#### getDesktopPane

@BeanProperty

(

bound

=false)
public

JDesktopPane

getDesktopPane()

Convenience method that searches the ancestor hierarchy for a

JDesktop

instance. If

JInternalFrame

finds none, the

desktopIcon

tree is searched.

setDesktopIcon

```java
@BeanProperty
(
description
="The icon shown when this internal frame is minimized.")
public void setDesktopIcon​(
JInternalFrame.JDesktopIcon
d)
```

Sets the

JDesktopIcon

associated with this

JInternalFrame

.

**Parameters:** d

- the

JDesktopIcon

to display on the desktop
**See Also:** getDesktopIcon()

---

#### setDesktopIcon

@BeanProperty

(

description

="The icon shown when this internal frame is minimized.")
public void setDesktopIcon​(

JInternalFrame.JDesktopIcon

d)

Sets the

JDesktopIcon

associated with this

JInternalFrame

.

getDesktopIcon

```java
public
JInternalFrame.JDesktopIcon
getDesktopIcon()
```

Returns the

JDesktopIcon

used when this

JInternalFrame

is iconified.

**Returns:** the

JDesktopIcon

displayed on the desktop
**See Also:** setDesktopIcon(javax.swing.JInternalFrame.JDesktopIcon)

---

#### getDesktopIcon

public

JInternalFrame.JDesktopIcon

getDesktopIcon()

Returns the

JDesktopIcon

used when this

JInternalFrame

is iconified.

getNormalBounds

```java
public
Rectangle
getNormalBounds()
```

If the

JInternalFrame

is not in maximized state, returns

getBounds()

; otherwise, returns the bounds that the

JInternalFrame

would be restored to.

**Returns:** a

Rectangle

containing the bounds of this
frame when in the normal state
**Since:** 1.3

---

#### getNormalBounds

public

Rectangle

getNormalBounds()

If the

JInternalFrame

is not in maximized state, returns

getBounds()

; otherwise, returns the bounds that the

JInternalFrame

would be restored to.

setNormalBounds

```java
public void setNormalBounds​(
Rectangle
r)
```

Sets the normal bounds for this internal frame, the bounds that
this internal frame would be restored to from its maximized state.
This method is intended for use only by desktop managers.

**Parameters:** r

- the bounds that this internal frame should be restored to
**Since:** 1.3

---

#### setNormalBounds

public void setNormalBounds​(

Rectangle

r)

Sets the normal bounds for this internal frame, the bounds that
this internal frame would be restored to from its maximized state.
This method is intended for use only by desktop managers.

getFocusOwner

```java
public
Component
getFocusOwner()
```

If this

JInternalFrame

is active,
returns the child that has focus.
Otherwise, returns

null

.

**Returns:** the component with focus, or

null

if no children have focus
**Since:** 1.3

---

#### getFocusOwner

public

Component

getFocusOwner()

If this

JInternalFrame

is active,
returns the child that has focus.
Otherwise, returns

null

.

getMostRecentFocusOwner

```java
@BeanProperty
(
bound
=false)
public
Component
getMostRecentFocusOwner()
```

Returns the child component of this

JInternalFrame

that will receive the
focus when this

JInternalFrame

is selected.
If this

JInternalFrame

is
currently selected, this method returns the same component as
the

getFocusOwner

method.
If this

JInternalFrame

is not selected,
then the child component that most recently requested focus will be
returned. If no child component has ever requested focus, then this

JInternalFrame

's initial focusable component is returned.
If no such
child exists, then this

JInternalFrame

's default component
to focus is returned.

**Returns:** the child component that will receive focus when this

JInternalFrame

is selected
**Since:** 1.4
**See Also:** getFocusOwner()

,

isSelected

---

#### getMostRecentFocusOwner

@BeanProperty

(

bound

=false)
public

Component

getMostRecentFocusOwner()

Returns the child component of this

JInternalFrame

that will receive the
focus when this

JInternalFrame

is selected.
If this

JInternalFrame

is
currently selected, this method returns the same component as
the

getFocusOwner

method.
If this

JInternalFrame

is not selected,
then the child component that most recently requested focus will be
returned. If no child component has ever requested focus, then this

JInternalFrame

's initial focusable component is returned.
If no such
child exists, then this

JInternalFrame

's default component
to focus is returned.

restoreSubcomponentFocus

```java
public void restoreSubcomponentFocus()
```

Requests the internal frame to restore focus to the
last subcomponent that had focus. This is used by the UI when
the user selected this internal frame --
for example, by clicking on the title bar.

**Since:** 1.3

---

#### restoreSubcomponentFocus

public void restoreSubcomponentFocus()

Requests the internal frame to restore focus to the
last subcomponent that had focus. This is used by the UI when
the user selected this internal frame --
for example, by clicking on the title bar.

reshape

```java
public void reshape​(int x,
int y,
int width,
int height)
```

Moves and resizes this component. Unlike other components,
this implementation also forces re-layout, so that frame
decorations such as the title bar are always redisplayed.

**Overrides:** reshape

in class

JComponent
**Parameters:** x

- an integer giving the component's new horizontal position
measured in pixels from the left of its container
**Parameters:** y

- an integer giving the component's new vertical position,
measured in pixels from the bottom of its container
**Parameters:** width

- an integer giving the component's new width in pixels
**Parameters:** height

- an integer giving the component's new height in pixels
**See Also:** Component.setBounds(int, int, int, int)

---

#### reshape

public void reshape​(int x,
int y,
int width,
int height)

Moves and resizes this component. Unlike other components,
this implementation also forces re-layout, so that frame
decorations such as the title bar are always redisplayed.

addInternalFrameListener

```java
public void addInternalFrameListener​(
InternalFrameListener
l)
```

Adds the specified listener to receive internal
frame events from this internal frame.

**Parameters:** l

- the internal frame listener

---

#### addInternalFrameListener

public void addInternalFrameListener​(

InternalFrameListener

l)

Adds the specified listener to receive internal
frame events from this internal frame.

removeInternalFrameListener

```java
public void removeInternalFrameListener​(
InternalFrameListener
l)
```

Removes the specified internal frame listener so that it no longer
receives internal frame events from this internal frame.

**Parameters:** l

- the internal frame listener

---

#### removeInternalFrameListener

public void removeInternalFrameListener​(

InternalFrameListener

l)

Removes the specified internal frame listener so that it no longer
receives internal frame events from this internal frame.

getInternalFrameListeners

```java
@BeanProperty
(
bound
=false)
public
InternalFrameListener
[] getInternalFrameListeners()
```

Returns an array of all the

InternalFrameListener

s added
to this

JInternalFrame

with

addInternalFrameListener

.

**Returns:** all of the

InternalFrameListener

s added or an empty
array if no listeners have been added
**Since:** 1.4
**See Also:** addInternalFrameListener(javax.swing.event.InternalFrameListener)

---

#### getInternalFrameListeners

@BeanProperty

(

bound

=false)
public

InternalFrameListener

[] getInternalFrameListeners()

Returns an array of all the

InternalFrameListener

s added
to this

JInternalFrame

with

addInternalFrameListener

.

fireInternalFrameEvent

```java
protected void fireInternalFrameEvent​(int id)
```

Fires an internal frame event.

**Parameters:** id

- the type of the event being fired; one of the following:

- InternalFrameEvent.INTERNAL_FRAME_OPENED

InternalFrameEvent.INTERNAL_FRAME_CLOSING

InternalFrameEvent.INTERNAL_FRAME_CLOSED

InternalFrameEvent.INTERNAL_FRAME_ICONIFIED

InternalFrameEvent.INTERNAL_FRAME_DEICONIFIED

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

If the event type is not one of the above, nothing happens.

---

#### fireInternalFrameEvent

protected void fireInternalFrameEvent​(int id)

Fires an internal frame event.

InternalFrameEvent.INTERNAL_FRAME_OPENED

InternalFrameEvent.INTERNAL_FRAME_CLOSING

InternalFrameEvent.INTERNAL_FRAME_CLOSED

InternalFrameEvent.INTERNAL_FRAME_ICONIFIED

InternalFrameEvent.INTERNAL_FRAME_DEICONIFIED

InternalFrameEvent.INTERNAL_FRAME_ACTIVATED

InternalFrameEvent.INTERNAL_FRAME_DEACTIVATED

doDefaultCloseAction

```java
public void doDefaultCloseAction()
```

Fires an

INTERNAL_FRAME_CLOSING

event
and then performs the action specified by
the internal frame's default close operation.
This method is typically invoked by the
look-and-feel-implemented action handler
for the internal frame's close button.

**Since:** 1.3
**See Also:** setDefaultCloseOperation(int)

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

---

#### doDefaultCloseAction

public void doDefaultCloseAction()

Fires an

INTERNAL_FRAME_CLOSING

event
and then performs the action specified by
the internal frame's default close operation.
This method is typically invoked by the
look-and-feel-implemented action handler
for the internal frame's close button.

setDefaultCloseOperation

```java
public void setDefaultCloseOperation​(int operation)
```

Sets the operation that will happen by default when
the user initiates a "close" on this internal frame.
The possible choices are:

The default value is

DISPOSE_ON_CLOSE

.
Before performing the specified close operation,
the internal frame fires
an

INTERNAL_FRAME_CLOSING

event.

**Parameters:** operation

- one of the following constants defined in

javax.swing.WindowConstants

(an interface implemented by

JInternalFrame

):

DO_NOTHING_ON_CLOSE

,

HIDE_ON_CLOSE

, or

DISPOSE_ON_CLOSE
**See Also:** addInternalFrameListener(javax.swing.event.InternalFrameListener)

,

getDefaultCloseOperation()

,

JComponent.setVisible(boolean)

,

dispose()

,

InternalFrameEvent.INTERNAL_FRAME_CLOSING

---

#### setDefaultCloseOperation

public void setDefaultCloseOperation​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this internal frame.
The possible choices are:

The default value is

DISPOSE_ON_CLOSE

.
Before performing the specified close operation,
the internal frame fires
an

INTERNAL_FRAME_CLOSING

event.

The default value is

DISPOSE_ON_CLOSE

.
Before performing the specified close operation,
the internal frame fires
an

INTERNAL_FRAME_CLOSING

event.

getDefaultCloseOperation

```java
public int getDefaultCloseOperation()
```

Returns the default operation that occurs when the user
initiates a "close" on this internal frame.

**Returns:** the operation that will occur when the user closes the internal
frame
**See Also:** setDefaultCloseOperation(int)

---

#### getDefaultCloseOperation

public int getDefaultCloseOperation()

Returns the default operation that occurs when the user
initiates a "close" on this internal frame.

pack

```java
public void pack()
```

Causes subcomponents of this

JInternalFrame

to be laid out at their preferred size. Internal frames that are
iconized or maximized are first restored and then packed. If the
internal frame is unable to be restored its state is not changed
and will not be packed.

**See Also:** Window.pack()

---

#### pack

public void pack()

Causes subcomponents of this

JInternalFrame

to be laid out at their preferred size. Internal frames that are
iconized or maximized are first restored and then packed. If the
internal frame is unable to be restored its state is not changed
and will not be packed.

show

```java
public void show()
```

If the internal frame is not visible,
brings the internal frame to the front,
makes it visible,
and attempts to select it.
The first time the internal frame is made visible,
this method also fires an

INTERNAL_FRAME_OPENED

event.
This method does nothing if the internal frame is already visible.
Invoking this method
has the same result as invoking

setVisible(true)

.

**Overrides:** show

in class

Component
**See Also:** moveToFront()

,

setSelected(boolean)

,

InternalFrameEvent.INTERNAL_FRAME_OPENED

,

JComponent.setVisible(boolean)

---

#### show

public void show()

If the internal frame is not visible,
brings the internal frame to the front,
makes it visible,
and attempts to select it.
The first time the internal frame is made visible,
this method also fires an

INTERNAL_FRAME_OPENED

event.
This method does nothing if the internal frame is already visible.
Invoking this method
has the same result as invoking

setVisible(true)

.

dispose

```java
public void dispose()
```

Makes this internal frame
invisible, unselected, and closed.
If the frame is not already closed,
this method fires an

INTERNAL_FRAME_CLOSED

event.
The results of invoking this method are similar to

setClosed(true)

,
but

dispose

always succeeds in closing
the internal frame and does not fire
an

INTERNAL_FRAME_CLOSING

event.

**See Also:** InternalFrameEvent.INTERNAL_FRAME_CLOSED

,

JComponent.setVisible(boolean)

,

setSelected(boolean)

,

setClosed(boolean)

---

#### dispose

public void dispose()

Makes this internal frame
invisible, unselected, and closed.
If the frame is not already closed,
this method fires an

INTERNAL_FRAME_CLOSED

event.
The results of invoking this method are similar to

setClosed(true)

,
but

dispose

always succeeds in closing
the internal frame and does not fire
an

INTERNAL_FRAME_CLOSING

event.

toFront

```java
public void toFront()
```

Brings this internal frame to the front.
Places this internal frame at the top of the stacking order
and makes the corresponding adjustment to other visible internal
frames.

**See Also:** Window.toFront()

,

moveToFront()

---

#### toFront

public void toFront()

Brings this internal frame to the front.
Places this internal frame at the top of the stacking order
and makes the corresponding adjustment to other visible internal
frames.

toBack

```java
public void toBack()
```

Sends this internal frame to the back.
Places this internal frame at the bottom of the stacking order
and makes the corresponding adjustment to other visible
internal frames.

**See Also:** Window.toBack()

,

moveToBack()

---

#### toBack

public void toBack()

Sends this internal frame to the back.
Places this internal frame at the bottom of the stacking order
and makes the corresponding adjustment to other visible
internal frames.

setFocusCycleRoot

```java
public final void setFocusCycleRoot​(boolean focusCycleRoot)
```

Does nothing because

JInternalFrame

s must always be roots of a focus
traversal cycle.

**Overrides:** setFocusCycleRoot

in class

Container
**Parameters:** focusCycleRoot

- this value is ignored
**Since:** 1.4
**See Also:** isFocusCycleRoot()

,

Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

Container.getFocusTraversalPolicy()

---

#### setFocusCycleRoot

public final void setFocusCycleRoot​(boolean focusCycleRoot)

Does nothing because

JInternalFrame

s must always be roots of a focus
traversal cycle.

isFocusCycleRoot

```java
public final boolean isFocusCycleRoot()
```

Always returns

true

because all

JInternalFrame

s must be
roots of a focus traversal cycle.

**Overrides:** isFocusCycleRoot

in class

Container
**Returns:** true
**Since:** 1.4
**See Also:** setFocusCycleRoot(boolean)

,

Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

Container.getFocusTraversalPolicy()

---

#### isFocusCycleRoot

public final boolean isFocusCycleRoot()

Always returns

true

because all

JInternalFrame

s must be
roots of a focus traversal cycle.

getFocusCycleRootAncestor

```java
@BeanProperty
(
bound
=false)
public final
Container
getFocusCycleRootAncestor()
```

Always returns

null

because

JInternalFrame

s
must always be roots of a focus
traversal cycle.

**Overrides:** getFocusCycleRootAncestor

in class

Component
**Returns:** null
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

---

#### getFocusCycleRootAncestor

@BeanProperty

(

bound

=false)
public final

Container

getFocusCycleRootAncestor()

Always returns

null

because

JInternalFrame

s
must always be roots of a focus
traversal cycle.

getWarningString

```java
@BeanProperty
(
bound
=false)
public final
String
getWarningString()
```

Gets the warning string that is displayed with this internal frame.
Since an internal frame is always secure (since it's fully
contained within a window that might need a warning string)
this method always returns

null

.

**Returns:** null
**See Also:** Window.getWarningString()

---

#### getWarningString

@BeanProperty

(

bound

=false)
public final

String

getWarningString()

Gets the warning string that is displayed with this internal frame.
Since an internal frame is always secure (since it's fully
contained within a window that might need a warning string)
this method always returns

null

.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JInternalFrame

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

JInternalFrame

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JInternalFrame

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

paintComponent

```java
protected void paintComponent​(
Graphics
g)
```

Overridden to allow optimized painting when the
internal frame is being dragged.

**Overrides:** paintComponent

in class

JComponent
**Parameters:** g

- the

Graphics

object to protect
**See Also:** JComponent.paint(java.awt.Graphics)

,

ComponentUI

---

#### paintComponent

protected void paintComponent​(

Graphics

g)

Overridden to allow optimized painting when the
internal frame is being dragged.

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

Gets the

AccessibleContext

associated with this

JInternalFrame

.
For internal frames, the

AccessibleContext

takes the form of an

AccessibleJInternalFrame

object.
A new

AccessibleJInternalFrame

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleJInternalFrame

that serves as the

AccessibleContext

of this

JInternalFrame
**See Also:** JInternalFrame.AccessibleJInternalFrame

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

associated with this

JInternalFrame

.
For internal frames, the

AccessibleContext

takes the form of an

AccessibleJInternalFrame

object.
A new

AccessibleJInternalFrame

instance is created if necessary.

---

