# Class Frame

**Source:** `java.desktop\java\awt\Frame.html`

### Class Description

```java
public class
Frame

extends
Window

implements
MenuContainer
```

A

Frame

is a top-level window with a title and a border.

The size of the frame includes any area designated for the
border. The dimensions of the border area may be obtained
using the

getInsets

method, however, since
these dimensions are platform-dependent, a valid insets
value cannot be obtained until the frame is made displayable
by either calling

pack

or

show

.
Since the border area is included in the overall size of the
frame, the border effectively obscures a portion of the frame,
constraining the area available for rendering and/or displaying
subcomponents to the rectangle which has an upper-left corner
location of

(insets.left, insets.top)

, and has a size of

width - (insets.left + insets.right)

by

height - (insets.top + insets.bottom)

.

The default layout for a frame is

BorderLayout

.

A frame may have its native decorations (i.e.

Frame

and

Titlebar

) turned off
with

setUndecorated

. This can only be done while the frame
is not

displayable

.

In a multi-screen environment, you can create a

Frame

on a different screen device by constructing the

Frame

with

Frame(GraphicsConfiguration)

or

Frame(String title, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen
device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual-coordinate system. The
origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location
of the primary screen in the virtual device, negative coordinates
are possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Frame

returns virtual device coordinates. Call the

getBounds

method of a

GraphicsConfiguration

to find its origin in
the virtual coordinate system.

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

#### @Deprecated

public static final int DEFAULT_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int CROSSHAIR_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int TEXT_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int WAIT_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int SW_RESIZE_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int SE_RESIZE_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int NW_RESIZE_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int NE_RESIZE_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int N_RESIZE_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int S_RESIZE_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int W_RESIZE_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int E_RESIZE_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int HAND_CURSOR

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int MOVE_CURSOR

**See Also:**
- Constant Field Values

---

#### public static final int NORMAL

Frame is in the "normal" state. This symbolic constant names a
frame state with all state bits cleared.

**See Also:**
- setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

---

#### public static final int ICONIFIED

This state bit indicates that frame is iconified.

**See Also:**
- setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

---

#### public static final int MAXIMIZED_HORIZ

This state bit indicates that frame is maximized in the
horizontal direction.

**See Also:**
- setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

**Since:**
- 1.4

---

#### public static final int MAXIMIZED_VERT

This state bit indicates that frame is maximized in the
vertical direction.

**See Also:**
- setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

**Since:**
- 1.4

---

#### public static final int MAXIMIZED_BOTH

This state bit mask indicates that frame is fully maximized
(that is both horizontally and vertically). It is just a
convenience alias for

MAXIMIZED_VERT | MAXIMIZED_HORIZ

.

Note that the correct test for frame being fully maximized is

```java
(state & Frame.MAXIMIZED_BOTH) == Frame.MAXIMIZED_BOTH
```

To test is frame is maximized in

some

direction use

```java
(state & Frame.MAXIMIZED_BOTH) != 0
```

**See Also:**
- setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

**Since:**
- 1.4

---

### Constructor Details

#### public Frame()
throws
HeadlessException

Constructs a new instance of

Frame

that is
initially invisible. The title of the

Frame

is empty.

**Throws:**
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### public Frame​(
GraphicsConfiguration
gc)

Constructs a new, initially invisible

Frame

with the
specified

GraphicsConfiguration

.

**Parameters:**
- gc

- the

GraphicsConfiguration

of the target screen device. If

gc

is

null

, the system default

GraphicsConfiguration

is assumed.

**Throws:**
- IllegalArgumentException

- if

gc

is not from a screen device.
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.3

---

#### public Frame​(
String
title)
throws
HeadlessException

Constructs a new, initially invisible

Frame

object
with the specified title.

**Parameters:**
- title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".

**Throws:**
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

GraphicsConfiguration.getBounds()

---

#### public Frame​(
String
title,

GraphicsConfiguration
gc)

Constructs a new, initially invisible

Frame

object
with the specified title and a

GraphicsConfiguration

.

**Parameters:**
- title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
- gc

- the

GraphicsConfiguration

of the target screen device. If

gc

is

null

, the system default

GraphicsConfiguration

is assumed.

**Throws:**
- IllegalArgumentException

- if

gc

is not from a screen device.
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

GraphicsConfiguration.getBounds()

**Since:**
- 1.3

---

### Method Details

#### public void addNotify()

Makes this Frame displayable by connecting it to
a native screen resource. Making a frame displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:**
- addNotify

in class

Window

**See Also:**
- Component.isDisplayable()

,

removeNotify()

---

#### public
String
getTitle()

Gets the title of the frame. The title is displayed in the
frame's border.

**Returns:**
- the title of this frame, or an empty string ("")
if this frame doesn't have a title.

**See Also:**
- setTitle(String)

---

#### public void setTitle​(
String
title)

Sets the title for this frame to the specified string.

**Parameters:**
- title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".

**See Also:**
- getTitle()

---

#### public
Image
getIconImage()

Returns the image to be displayed as the icon for this frame.

This method is obsolete and kept for backward compatibility
only. Use

Window.getIconImages()

instead.

If a list of several images was specified as a Window's icon,
this method will return the first item of the list.

**Returns:**
- the icon image for this frame, or

null

if this frame doesn't have an icon image.

**See Also:**
- Window.setIconImage(Image)

,

Window.getIconImages()

,

Window.setIconImages(java.util.List<? extends java.awt.Image>)

---

#### public
MenuBar
getMenuBar()

Gets the menu bar for this frame.

**Returns:**
- the menu bar for this frame, or

null

if this frame doesn't have a menu bar.

**See Also:**
- setMenuBar(MenuBar)

---

#### public void setMenuBar​(
MenuBar
mb)

Sets the menu bar for this frame to the specified menu bar.

**Parameters:**
- mb

- the menu bar being set.
If this parameter is

null

then any
existing menu bar on this frame is removed.

**See Also:**
- getMenuBar()

---

#### public boolean isResizable()

Indicates whether this frame is resizable by the user.
By default, all frames are initially resizable.

**Returns:**
- true

if the user can resize this frame;

false

otherwise.

**See Also:**
- setResizable(boolean)

---

#### public void setResizable​(boolean resizable)

Sets whether this frame is resizable by the user.

**Parameters:**
- resizable

-

true

if this frame is resizable;

false

otherwise.

**See Also:**
- isResizable()

---

#### public void setState​(int state)

Sets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with applications developed
earlier this method still accepts

Frame.NORMAL

and

Frame.ICONIFIED

only. The iconic
state of the frame is only changed, other aspects
of frame state are not affected by this method. If
the state passed to this method is neither

Frame.NORMAL

nor

Frame.ICONIFIED

the
method performs no actions at all.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getState()

method will be
changed. The application may determine whether a
specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

**Parameters:**
- state

- either

Frame.NORMAL

or

Frame.ICONIFIED

.

**See Also:**
- setExtendedState(int)

,

Window.addWindowStateListener(java.awt.event.WindowStateListener)

---

#### public void setExtendedState​(int state)

Sets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getExtendedState()

method will
be changed. The application may determine whether
a specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

**Parameters:**
- state

- a bitwise mask of frame state constants

**See Also:**
- Window.addWindowStateListener(java.awt.event.WindowStateListener)

**Since:**
- 1.4

---

#### public int getState()

Gets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with old programs this method still returns

Frame.NORMAL

and

Frame.ICONIFIED

but
it only reports the iconic state of the frame, other aspects of
frame state are not reported by this method.

**Returns:**
- Frame.NORMAL

or

Frame.ICONIFIED

.

**See Also:**
- setState(int)

,

getExtendedState()

---

#### public int getExtendedState()

Gets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

**Returns:**
- a bitwise mask of frame state constants

**See Also:**
- setExtendedState(int)

**Since:**
- 1.4

---

#### public void setMaximizedBounds​(
Rectangle
bounds)

Sets the maximized bounds for this frame.

When a frame is in maximized state the system supplies some
defaults bounds. This method allows some or all of those
system supplied values to be overridden.

If

bounds

is

null

, accept bounds
supplied by the system. If non-

null

you can
override some of the system supplied values while accepting
others by setting those fields you want to accept from system
to

Integer.MAX_VALUE

.

Note, the given maximized bounds are used as a hint for the native
system, because the underlying platform may not support setting the
location and/or size of the maximized windows. If that is the case, the
provided values do not affect the appearance of the frame in the
maximized state.

**Parameters:**
- bounds

- bounds for the maximized state

**See Also:**
- getMaximizedBounds()

**Since:**
- 1.4

---

#### public
Rectangle
getMaximizedBounds()

Gets maximized bounds for this frame.
Some fields may contain

Integer.MAX_VALUE

to indicate
that system supplied values for this field must be used.

**Returns:**
- maximized bounds for this frame; may be

null

**See Also:**
- setMaximizedBounds(Rectangle)

**Since:**
- 1.4

---

#### public void setUndecorated​(boolean undecorated)

Disables or enables decorations for this frame.

This method can only be called while the frame is not displayable. To
make this frame decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

**Parameters:**
- undecorated

-

true

if no frame decorations are to be
enabled;

false

if frame decorations are to be enabled

**Throws:**
- IllegalComponentStateException

- if the frame is displayable
- IllegalComponentStateException

- if

undecorated

is

false

, and this frame does not have the default shape
- IllegalComponentStateException

- if

undecorated

is

false

, and this frame opacity is less than

1.0f
- IllegalComponentStateException

- if

undecorated

is

false

, and the alpha value of this frame background
color is less than

1.0f

**See Also:**
- isUndecorated()

,

Component.isDisplayable()

,

Window.getShape()

,

Window.getOpacity()

,

Window.getBackground()

,

JFrame.setDefaultLookAndFeelDecorated(boolean)

**Since:**
- 1.4

---

#### public boolean isUndecorated()

Indicates whether this frame is undecorated.
By default, all frames are initially decorated.

**Returns:**
- true

if frame is undecorated;

false

otherwise.

**See Also:**
- setUndecorated(boolean)

**Since:**
- 1.4

---

#### public void remove​(
MenuComponent
m)

Removes the specified menu bar from this frame.

**Specified by:**
- remove

in interface

MenuContainer

**Overrides:**
- remove

in class

Component

**Parameters:**
- m

- the menu component to remove.
If

m

is

null

, then
no action is taken

**See Also:**
- Component.add(PopupMenu)

---

#### public void removeNotify()

Makes this Frame undisplayable by removing its connection
to its native screen resource. Making a Frame undisplayable
will cause any of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:**
- removeNotify

in class

Container

**See Also:**
- Component.isDisplayable()

,

addNotify()

---

#### protected
String
paramString()

Returns a string representing the state of this

Frame

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- paramString

in class

Container

**Returns:**
- the parameter string of this frame

---

#### @Deprecated

public void setCursor​(int cursorType)

Sets the cursor for this frame to the specified type.

**Parameters:**
- cursorType

- the cursor type

---

#### @Deprecated

public int getCursorType()

**Returns:**
- the cursor type for this frame

---

#### public static
Frame
[] getFrames()

Returns an array of all

Frame

s created by this application.
If called from an applet, the array includes only the

Frame

s
accessible by that applet.

Warning:

this method may return system created frames, such
as a shared, hidden frame which is used by Swing. Applications
should not assume the existence of these frames, nor should an
application assume anything about these frames such as component
positions,

LayoutManager

s or serialization.

Note

: To obtain a list of all ownerless windows, including
ownerless

Dialog

s (introduced in release 1.6), use

Window.getOwnerlessWindows

.

**Returns:**
- the array of all

Frame

s created by this application

**See Also:**
- Window.getWindows()

,

Window.getOwnerlessWindows()

**Since:**
- 1.2

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this Frame.
For frames, the AccessibleContext takes the form of an
AccessibleAWTFrame.
A new AccessibleAWTFrame instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Window

**Returns:**
- an AccessibleAWTFrame that serves as the
AccessibleContext of this Frame

**Since:**
- 1.3

---

### Additional Sections

#### Class Frame

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - java.awt.Window
- - java.awt.Frame

java.awt.Component

- java.awt.Container
- - java.awt.Window
- - java.awt.Frame

java.awt.Container

- java.awt.Window
- - java.awt.Frame

java.awt.Window

- java.awt.Frame

java.awt.Frame

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

**Direct Known Subclasses:** JFrame

```java
public class
Frame

extends
Window

implements
MenuContainer
```

A

Frame

is a top-level window with a title and a border.

The size of the frame includes any area designated for the
border. The dimensions of the border area may be obtained
using the

getInsets

method, however, since
these dimensions are platform-dependent, a valid insets
value cannot be obtained until the frame is made displayable
by either calling

pack

or

show

.
Since the border area is included in the overall size of the
frame, the border effectively obscures a portion of the frame,
constraining the area available for rendering and/or displaying
subcomponents to the rectangle which has an upper-left corner
location of

(insets.left, insets.top)

, and has a size of

width - (insets.left + insets.right)

by

height - (insets.top + insets.bottom)

.

The default layout for a frame is

BorderLayout

.

A frame may have its native decorations (i.e.

Frame

and

Titlebar

) turned off
with

setUndecorated

. This can only be done while the frame
is not

displayable

.

In a multi-screen environment, you can create a

Frame

on a different screen device by constructing the

Frame

with

Frame(GraphicsConfiguration)

or

Frame(String title, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen
device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual-coordinate system. The
origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location
of the primary screen in the virtual device, negative coordinates
are possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Frame

returns virtual device coordinates. Call the

getBounds

method of a

GraphicsConfiguration

to find its origin in
the virtual coordinate system.

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

**Since:** 1.0
**See Also:** WindowEvent

,

Window.addWindowListener(java.awt.event.WindowListener)

,

Serialized Form

public class

Frame

extends

Window

implements

MenuContainer

A

Frame

is a top-level window with a title and a border.

The size of the frame includes any area designated for the
border. The dimensions of the border area may be obtained
using the

getInsets

method, however, since
these dimensions are platform-dependent, a valid insets
value cannot be obtained until the frame is made displayable
by either calling

pack

or

show

.
Since the border area is included in the overall size of the
frame, the border effectively obscures a portion of the frame,
constraining the area available for rendering and/or displaying
subcomponents to the rectangle which has an upper-left corner
location of

(insets.left, insets.top)

, and has a size of

width - (insets.left + insets.right)

by

height - (insets.top + insets.bottom)

.

The default layout for a frame is

BorderLayout

.

A frame may have its native decorations (i.e.

Frame

and

Titlebar

) turned off
with

setUndecorated

. This can only be done while the frame
is not

displayable

.

In a multi-screen environment, you can create a

Frame

on a different screen device by constructing the

Frame

with

Frame(GraphicsConfiguration)

or

Frame(String title, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen
device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual-coordinate system. The
origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location
of the primary screen in the virtual device, negative coordinates
are possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Frame

returns virtual device coordinates. Call the

getBounds

method of a

GraphicsConfiguration

to find its origin in
the virtual coordinate system.

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

The size of the frame includes any area designated for the
border. The dimensions of the border area may be obtained
using the

getInsets

method, however, since
these dimensions are platform-dependent, a valid insets
value cannot be obtained until the frame is made displayable
by either calling

pack

or

show

.
Since the border area is included in the overall size of the
frame, the border effectively obscures a portion of the frame,
constraining the area available for rendering and/or displaying
subcomponents to the rectangle which has an upper-left corner
location of

(insets.left, insets.top)

, and has a size of

width - (insets.left + insets.right)

by

height - (insets.top + insets.bottom)

.

The default layout for a frame is

BorderLayout

.

A frame may have its native decorations (i.e.

Frame

and

Titlebar

) turned off
with

setUndecorated

. This can only be done while the frame
is not

displayable

.

In a multi-screen environment, you can create a

Frame

on a different screen device by constructing the

Frame

with

Frame(GraphicsConfiguration)

or

Frame(String title, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen
device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual-coordinate system. The
origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location
of the primary screen in the virtual device, negative coordinates
are possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Frame

returns virtual device coordinates. Call the

getBounds

method of a

GraphicsConfiguration

to find its origin in
the virtual coordinate system.

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

The default layout for a frame is

BorderLayout

.

A frame may have its native decorations (i.e.

Frame

and

Titlebar

) turned off
with

setUndecorated

. This can only be done while the frame
is not

displayable

.

In a multi-screen environment, you can create a

Frame

on a different screen device by constructing the

Frame

with

Frame(GraphicsConfiguration)

or

Frame(String title, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen
device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual-coordinate system. The
origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location
of the primary screen in the virtual device, negative coordinates
are possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Frame

returns virtual device coordinates. Call the

getBounds

method of a

GraphicsConfiguration

to find its origin in
the virtual coordinate system.

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

A frame may have its native decorations (i.e.

Frame

and

Titlebar

) turned off
with

setUndecorated

. This can only be done while the frame
is not

displayable

.

In a multi-screen environment, you can create a

Frame

on a different screen device by constructing the

Frame

with

Frame(GraphicsConfiguration)

or

Frame(String title, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen
device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual-coordinate system. The
origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location
of the primary screen in the virtual device, negative coordinates
are possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Frame

returns virtual device coordinates. Call the

getBounds

method of a

GraphicsConfiguration

to find its origin in
the virtual coordinate system.

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

In a multi-screen environment, you can create a

Frame

on a different screen device by constructing the

Frame

with

Frame(GraphicsConfiguration)

or

Frame(String title, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen
device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual-coordinate system. The
origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location
of the primary screen in the virtual device, negative coordinates
are possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Frame

returns virtual device coordinates. Call the

getBounds

method of a

GraphicsConfiguration

to find its origin in
the virtual coordinate system.

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual-coordinate system. The
origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location
of the primary screen in the virtual device, negative coordinates
are possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Frame

returns virtual device coordinates. Call the

getBounds

method of a

GraphicsConfiguration

to find its origin in
the virtual coordinate system.

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Frame

returns virtual device coordinates. Call the

getBounds

method of a

GraphicsConfiguration

to find its origin in
the virtual coordinate system.

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

The following code sets the
location of the

Frame

at (10, 10) relative
to the origin of the physical screen of the corresponding

GraphicsConfiguration

. If the bounds of the

GraphicsConfiguration

is not taken into account, the

Frame

location would be set at (10, 10) relative to the
virtual-coordinate system and would appear on the primary physical
screen, which might be different from the physical screen of the
specified

GraphicsConfiguration

.

```java
Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);
```

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

Frame f = new Frame(GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
f.setLocation(10 + bounds.x, 10 + bounds.y);

Frames are capable of generating the following types of

WindowEvent

s:

- WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

WINDOW_OPENED

WINDOW_CLOSING

:

If the program doesn't
explicitly hide or dispose the window while processing
this event, the window close operation is canceled.

WINDOW_CLOSED

WINDOW_ICONIFIED

WINDOW_DEICONIFIED

WINDOW_ACTIVATED

WINDOW_DEACTIVATED

WINDOW_GAINED_FOCUS

WINDOW_LOST_FOCUS

WINDOW_STATE_CHANGED

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Frame.AccessibleAWTFrame

This class implements accessibility support for the

Frame

class.

- Nested classes/interfaces declared in class java.awt.

Window

Window.AccessibleAWTWindow

,

Window.Type

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

static int

CROSSHAIR_CURSOR

Deprecated.

replaced by

Cursor.CROSSHAIR_CURSOR

.

static int

DEFAULT_CURSOR

Deprecated.

replaced by

Cursor.DEFAULT_CURSOR

.

static int

E_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.E_RESIZE_CURSOR

.

static int

HAND_CURSOR

Deprecated.

replaced by

Cursor.HAND_CURSOR

.

static int

ICONIFIED

This state bit indicates that frame is iconified.

static int

MAXIMIZED_BOTH

This state bit mask indicates that frame is fully maximized
(that is both horizontally and vertically).

static int

MAXIMIZED_HORIZ

This state bit indicates that frame is maximized in the
horizontal direction.

static int

MAXIMIZED_VERT

This state bit indicates that frame is maximized in the
vertical direction.

static int

MOVE_CURSOR

Deprecated.

replaced by

Cursor.MOVE_CURSOR

.

static int

N_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.N_RESIZE_CURSOR

.

static int

NE_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.NE_RESIZE_CURSOR

.

static int

NORMAL

Frame is in the "normal" state.

static int

NW_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.NW_RESIZE_CURSOR

.

static int

S_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.S_RESIZE_CURSOR

.

static int

SE_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.SE_RESIZE_CURSOR

.

static int

SW_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.SW_RESIZE_CURSOR

.

static int

TEXT_CURSOR

Deprecated.

replaced by

Cursor.TEXT_CURSOR

.

static int

W_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.W_RESIZE_CURSOR

.

static int

WAIT_CURSOR

Deprecated.

replaced by

Cursor.WAIT_CURSOR

.

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

Frame

()

Constructs a new instance of

Frame

that is
initially invisible.

Frame

​(

GraphicsConfiguration

gc)

Constructs a new, initially invisible

Frame

with the
specified

GraphicsConfiguration

.

Frame

​(

String

title)

Constructs a new, initially invisible

Frame

object
with the specified title.

Frame

​(

String

title,

GraphicsConfiguration

gc)

Constructs a new, initially invisible

Frame

object
with the specified title and a

GraphicsConfiguration

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addNotify

()

Makes this Frame displayable by connecting it to
a native screen resource.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Frame.

int

getCursorType

()

Deprecated.

As of JDK version 1.1,
replaced by

Component.getCursor()

.

int

getExtendedState

()

Gets the state of this frame.

static

Frame

[]

getFrames

()

Returns an array of all

Frame

s created by this application.

Image

getIconImage

()

Returns the image to be displayed as the icon for this frame.

Rectangle

getMaximizedBounds

()

Gets maximized bounds for this frame.

MenuBar

getMenuBar

()

Gets the menu bar for this frame.

int

getState

()

Gets the state of this frame (obsolete).

String

getTitle

()

Gets the title of the frame.

boolean

isResizable

()

Indicates whether this frame is resizable by the user.

boolean

isUndecorated

()

Indicates whether this frame is undecorated.

protected

String

paramString

()

Returns a string representing the state of this

Frame

.

void

remove

​(

MenuComponent

m)

Removes the specified menu bar from this frame.

void

removeNotify

()

Makes this Frame undisplayable by removing its connection
to its native screen resource.

void

setCursor

​(int cursorType)

Deprecated.

As of JDK version 1.1,
replaced by

Component.setCursor(Cursor)

.

void

setExtendedState

​(int state)

Sets the state of this frame.

void

setMaximizedBounds

​(

Rectangle

bounds)

Sets the maximized bounds for this frame.

void

setMenuBar

​(

MenuBar

mb)

Sets the menu bar for this frame to the specified menu bar.

void

setResizable

​(boolean resizable)

Sets whether this frame is resizable by the user.

void

setState

​(int state)

Sets the state of this frame (obsolete).

void

setTitle

​(

String

title)

Sets the title for this frame to the specified string.

void

setUndecorated

​(boolean undecorated)

Disables or enables decorations for this frame.

- Methods declared in class java.awt.

Window

addPropertyChangeListener

,

addPropertyChangeListener

,

addWindowFocusListener

,

addWindowListener

,

addWindowStateListener

,

applyResourceBundle

,

applyResourceBundle

,

createBufferStrategy

,

createBufferStrategy

,

dispose

,

getBackground

,

getBufferStrategy

,

getFocusableWindowState

,

getFocusCycleRootAncestor

,

getFocusOwner

,

getFocusTraversalKeys

,

getIconImages

,

getInputContext

,

getListeners

,

getLocale

,

getModalExclusionType

,

getMostRecentFocusOwner

,

getOpacity

,

getOwnedWindows

,

getOwner

,

getOwnerlessWindows

,

getShape

,

getToolkit

,

getType

,

getWarningString

,

getWindowFocusListeners

,

getWindowListeners

,

getWindows

,

getWindowStateListeners

,

hide

,

isActive

,

isAlwaysOnTop

,

isAlwaysOnTopSupported

,

isAutoRequestFocus

,

isFocusableWindow

,

isFocusCycleRoot

,

isFocused

,

isLocationByPlatform

,

isOpaque

,

isShowing

,

isValidateRoot

,

pack

,

paint

,

postEvent

,

processEvent

,

processWindowEvent

,

processWindowFocusEvent

,

processWindowStateEvent

,

removeWindowFocusListener

,

removeWindowListener

,

removeWindowStateListener

,

reshape

,

setAlwaysOnTop

,

setAutoRequestFocus

,

setBackground

,

setBounds

,

setBounds

,

setCursor

,

setFocusableWindowState

,

setFocusCycleRoot

,

setIconImage

,

setIconImages

,

setLocation

,

setLocation

,

setLocationByPlatform

,

setLocationRelativeTo

,

setMinimumSize

,

setModalExclusionType

,

setOpacity

,

setShape

,

setSize

,

setSize

,

setType

,

setVisible

,

show

,

toBack

,

toFront

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

getAlignmentX

,

getAlignmentY

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

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

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

print

,

printComponents

,

processContainerEvent

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

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

setLayout

,

transferFocusDownCycle

,

update

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

disable

,

disableEvents

,

dispatchEvent

,

enable

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

firePropertyChange

,

firePropertyChange

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

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

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocation

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

getSize

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

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

isDoubleBuffered

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

prepareImage

,

prepareImage

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

resize

,

resize

,

revalidate

,

setComponentOrientation

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setMaximumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

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

- Methods declared in interface java.awt.

MenuContainer

getFont

,

postEvent

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Frame.AccessibleAWTFrame

This class implements accessibility support for the

Frame

class.

- Nested classes/interfaces declared in class java.awt.

Window

Window.AccessibleAWTWindow

,

Window.Type

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

Frame

class.

Nested classes/interfaces declared in class java.awt.

Window

Window.AccessibleAWTWindow

,

Window.Type

---

#### Nested classes/interfaces declared in class java.awt. Window

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

static int

CROSSHAIR_CURSOR

Deprecated.

replaced by

Cursor.CROSSHAIR_CURSOR

.

static int

DEFAULT_CURSOR

Deprecated.

replaced by

Cursor.DEFAULT_CURSOR

.

static int

E_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.E_RESIZE_CURSOR

.

static int

HAND_CURSOR

Deprecated.

replaced by

Cursor.HAND_CURSOR

.

static int

ICONIFIED

This state bit indicates that frame is iconified.

static int

MAXIMIZED_BOTH

This state bit mask indicates that frame is fully maximized
(that is both horizontally and vertically).

static int

MAXIMIZED_HORIZ

This state bit indicates that frame is maximized in the
horizontal direction.

static int

MAXIMIZED_VERT

This state bit indicates that frame is maximized in the
vertical direction.

static int

MOVE_CURSOR

Deprecated.

replaced by

Cursor.MOVE_CURSOR

.

static int

N_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.N_RESIZE_CURSOR

.

static int

NE_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.NE_RESIZE_CURSOR

.

static int

NORMAL

Frame is in the "normal" state.

static int

NW_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.NW_RESIZE_CURSOR

.

static int

S_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.S_RESIZE_CURSOR

.

static int

SE_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.SE_RESIZE_CURSOR

.

static int

SW_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.SW_RESIZE_CURSOR

.

static int

TEXT_CURSOR

Deprecated.

replaced by

Cursor.TEXT_CURSOR

.

static int

W_RESIZE_CURSOR

Deprecated.

replaced by

Cursor.W_RESIZE_CURSOR

.

static int

WAIT_CURSOR

Deprecated.

replaced by

Cursor.WAIT_CURSOR

.

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

Deprecated.

replaced by

Cursor.CROSSHAIR_CURSOR

.

Deprecated.

replaced by

Cursor.DEFAULT_CURSOR

.

Deprecated.

replaced by

Cursor.E_RESIZE_CURSOR

.

Deprecated.

replaced by

Cursor.HAND_CURSOR

.

This state bit indicates that frame is iconified.

This state bit mask indicates that frame is fully maximized
(that is both horizontally and vertically).

This state bit indicates that frame is maximized in the
horizontal direction.

This state bit indicates that frame is maximized in the
vertical direction.

Deprecated.

replaced by

Cursor.MOVE_CURSOR

.

Deprecated.

replaced by

Cursor.N_RESIZE_CURSOR

.

Deprecated.

replaced by

Cursor.NE_RESIZE_CURSOR

.

Frame is in the "normal" state.

Deprecated.

replaced by

Cursor.NW_RESIZE_CURSOR

.

Deprecated.

replaced by

Cursor.S_RESIZE_CURSOR

.

Deprecated.

replaced by

Cursor.SE_RESIZE_CURSOR

.

Deprecated.

replaced by

Cursor.SW_RESIZE_CURSOR

.

Deprecated.

replaced by

Cursor.TEXT_CURSOR

.

Deprecated.

replaced by

Cursor.W_RESIZE_CURSOR

.

Deprecated.

replaced by

Cursor.WAIT_CURSOR

.

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

Frame

()

Constructs a new instance of

Frame

that is
initially invisible.

Frame

​(

GraphicsConfiguration

gc)

Constructs a new, initially invisible

Frame

with the
specified

GraphicsConfiguration

.

Frame

​(

String

title)

Constructs a new, initially invisible

Frame

object
with the specified title.

Frame

​(

String

title,

GraphicsConfiguration

gc)

Constructs a new, initially invisible

Frame

object
with the specified title and a

GraphicsConfiguration

.

---

#### Constructor Summary

Constructs a new instance of

Frame

that is
initially invisible.

Constructs a new, initially invisible

Frame

with the
specified

GraphicsConfiguration

.

Constructs a new, initially invisible

Frame

object
with the specified title.

Constructs a new, initially invisible

Frame

object
with the specified title and a

GraphicsConfiguration

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addNotify

()

Makes this Frame displayable by connecting it to
a native screen resource.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Frame.

int

getCursorType

()

Deprecated.

As of JDK version 1.1,
replaced by

Component.getCursor()

.

int

getExtendedState

()

Gets the state of this frame.

static

Frame

[]

getFrames

()

Returns an array of all

Frame

s created by this application.

Image

getIconImage

()

Returns the image to be displayed as the icon for this frame.

Rectangle

getMaximizedBounds

()

Gets maximized bounds for this frame.

MenuBar

getMenuBar

()

Gets the menu bar for this frame.

int

getState

()

Gets the state of this frame (obsolete).

String

getTitle

()

Gets the title of the frame.

boolean

isResizable

()

Indicates whether this frame is resizable by the user.

boolean

isUndecorated

()

Indicates whether this frame is undecorated.

protected

String

paramString

()

Returns a string representing the state of this

Frame

.

void

remove

​(

MenuComponent

m)

Removes the specified menu bar from this frame.

void

removeNotify

()

Makes this Frame undisplayable by removing its connection
to its native screen resource.

void

setCursor

​(int cursorType)

Deprecated.

As of JDK version 1.1,
replaced by

Component.setCursor(Cursor)

.

void

setExtendedState

​(int state)

Sets the state of this frame.

void

setMaximizedBounds

​(

Rectangle

bounds)

Sets the maximized bounds for this frame.

void

setMenuBar

​(

MenuBar

mb)

Sets the menu bar for this frame to the specified menu bar.

void

setResizable

​(boolean resizable)

Sets whether this frame is resizable by the user.

void

setState

​(int state)

Sets the state of this frame (obsolete).

void

setTitle

​(

String

title)

Sets the title for this frame to the specified string.

void

setUndecorated

​(boolean undecorated)

Disables or enables decorations for this frame.

- Methods declared in class java.awt.

Window

addPropertyChangeListener

,

addPropertyChangeListener

,

addWindowFocusListener

,

addWindowListener

,

addWindowStateListener

,

applyResourceBundle

,

applyResourceBundle

,

createBufferStrategy

,

createBufferStrategy

,

dispose

,

getBackground

,

getBufferStrategy

,

getFocusableWindowState

,

getFocusCycleRootAncestor

,

getFocusOwner

,

getFocusTraversalKeys

,

getIconImages

,

getInputContext

,

getListeners

,

getLocale

,

getModalExclusionType

,

getMostRecentFocusOwner

,

getOpacity

,

getOwnedWindows

,

getOwner

,

getOwnerlessWindows

,

getShape

,

getToolkit

,

getType

,

getWarningString

,

getWindowFocusListeners

,

getWindowListeners

,

getWindows

,

getWindowStateListeners

,

hide

,

isActive

,

isAlwaysOnTop

,

isAlwaysOnTopSupported

,

isAutoRequestFocus

,

isFocusableWindow

,

isFocusCycleRoot

,

isFocused

,

isLocationByPlatform

,

isOpaque

,

isShowing

,

isValidateRoot

,

pack

,

paint

,

postEvent

,

processEvent

,

processWindowEvent

,

processWindowFocusEvent

,

processWindowStateEvent

,

removeWindowFocusListener

,

removeWindowListener

,

removeWindowStateListener

,

reshape

,

setAlwaysOnTop

,

setAutoRequestFocus

,

setBackground

,

setBounds

,

setBounds

,

setCursor

,

setFocusableWindowState

,

setFocusCycleRoot

,

setIconImage

,

setIconImages

,

setLocation

,

setLocation

,

setLocationByPlatform

,

setLocationRelativeTo

,

setMinimumSize

,

setModalExclusionType

,

setOpacity

,

setShape

,

setSize

,

setSize

,

setType

,

setVisible

,

show

,

toBack

,

toFront

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

getAlignmentX

,

getAlignmentY

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

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

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

print

,

printComponents

,

processContainerEvent

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

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

setLayout

,

transferFocusDownCycle

,

update

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

disable

,

disableEvents

,

dispatchEvent

,

enable

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

firePropertyChange

,

firePropertyChange

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

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

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocation

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

getSize

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

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

isDoubleBuffered

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

prepareImage

,

prepareImage

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

resize

,

resize

,

revalidate

,

setComponentOrientation

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setMaximumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

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

- Methods declared in interface java.awt.

MenuContainer

getFont

,

postEvent

---

#### Method Summary

Makes this Frame displayable by connecting it to
a native screen resource.

Gets the AccessibleContext associated with this Frame.

Deprecated.

As of JDK version 1.1,
replaced by

Component.getCursor()

.

Gets the state of this frame.

Returns an array of all

Frame

s created by this application.

Returns the image to be displayed as the icon for this frame.

Gets maximized bounds for this frame.

Gets the menu bar for this frame.

Gets the state of this frame (obsolete).

Gets the title of the frame.

Indicates whether this frame is resizable by the user.

Indicates whether this frame is undecorated.

Returns a string representing the state of this

Frame

.

Removes the specified menu bar from this frame.

Makes this Frame undisplayable by removing its connection
to its native screen resource.

Deprecated.

As of JDK version 1.1,
replaced by

Component.setCursor(Cursor)

.

Sets the state of this frame.

Sets the maximized bounds for this frame.

Sets the menu bar for this frame to the specified menu bar.

Sets whether this frame is resizable by the user.

Sets the state of this frame (obsolete).

Sets the title for this frame to the specified string.

Disables or enables decorations for this frame.

Methods declared in class java.awt.

Window

addPropertyChangeListener

,

addPropertyChangeListener

,

addWindowFocusListener

,

addWindowListener

,

addWindowStateListener

,

applyResourceBundle

,

applyResourceBundle

,

createBufferStrategy

,

createBufferStrategy

,

dispose

,

getBackground

,

getBufferStrategy

,

getFocusableWindowState

,

getFocusCycleRootAncestor

,

getFocusOwner

,

getFocusTraversalKeys

,

getIconImages

,

getInputContext

,

getListeners

,

getLocale

,

getModalExclusionType

,

getMostRecentFocusOwner

,

getOpacity

,

getOwnedWindows

,

getOwner

,

getOwnerlessWindows

,

getShape

,

getToolkit

,

getType

,

getWarningString

,

getWindowFocusListeners

,

getWindowListeners

,

getWindows

,

getWindowStateListeners

,

hide

,

isActive

,

isAlwaysOnTop

,

isAlwaysOnTopSupported

,

isAutoRequestFocus

,

isFocusableWindow

,

isFocusCycleRoot

,

isFocused

,

isLocationByPlatform

,

isOpaque

,

isShowing

,

isValidateRoot

,

pack

,

paint

,

postEvent

,

processEvent

,

processWindowEvent

,

processWindowFocusEvent

,

processWindowStateEvent

,

removeWindowFocusListener

,

removeWindowListener

,

removeWindowStateListener

,

reshape

,

setAlwaysOnTop

,

setAutoRequestFocus

,

setBackground

,

setBounds

,

setBounds

,

setCursor

,

setFocusableWindowState

,

setFocusCycleRoot

,

setIconImage

,

setIconImages

,

setLocation

,

setLocation

,

setLocationByPlatform

,

setLocationRelativeTo

,

setMinimumSize

,

setModalExclusionType

,

setOpacity

,

setShape

,

setSize

,

setSize

,

setType

,

setVisible

,

show

,

toBack

,

toFront

---

#### Methods declared in class java.awt. Window

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

getAlignmentX

,

getAlignmentY

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

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

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

print

,

printComponents

,

processContainerEvent

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

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

setLayout

,

transferFocusDownCycle

,

update

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

disable

,

disableEvents

,

dispatchEvent

,

enable

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

firePropertyChange

,

firePropertyChange

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

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

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocation

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

getSize

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

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

isDoubleBuffered

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

prepareImage

,

prepareImage

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

resize

,

resize

,

revalidate

,

setComponentOrientation

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setMaximumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

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

Methods declared in interface java.awt.

MenuContainer

getFont

,

postEvent

---

#### Methods declared in interface java.awt. MenuContainer

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT_CURSOR

```java
@Deprecated

public static final int DEFAULT_CURSOR
```

Deprecated.

replaced by

Cursor.DEFAULT_CURSOR

.

**See Also:** Constant Field Values

- CROSSHAIR_CURSOR

```java
@Deprecated

public static final int CROSSHAIR_CURSOR
```

Deprecated.

replaced by

Cursor.CROSSHAIR_CURSOR

.

**See Also:** Constant Field Values

- TEXT_CURSOR

```java
@Deprecated

public static final int TEXT_CURSOR
```

Deprecated.

replaced by

Cursor.TEXT_CURSOR

.

**See Also:** Constant Field Values

- WAIT_CURSOR

```java
@Deprecated

public static final int WAIT_CURSOR
```

Deprecated.

replaced by

Cursor.WAIT_CURSOR

.

**See Also:** Constant Field Values

- SW_RESIZE_CURSOR

```java
@Deprecated

public static final int SW_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.SW_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- SE_RESIZE_CURSOR

```java
@Deprecated

public static final int SE_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.SE_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- NW_RESIZE_CURSOR

```java
@Deprecated

public static final int NW_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.NW_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- NE_RESIZE_CURSOR

```java
@Deprecated

public static final int NE_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.NE_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- N_RESIZE_CURSOR

```java
@Deprecated

public static final int N_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.N_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- S_RESIZE_CURSOR

```java
@Deprecated

public static final int S_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.S_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- W_RESIZE_CURSOR

```java
@Deprecated

public static final int W_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.W_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- E_RESIZE_CURSOR

```java
@Deprecated

public static final int E_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.E_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- HAND_CURSOR

```java
@Deprecated

public static final int HAND_CURSOR
```

Deprecated.

replaced by

Cursor.HAND_CURSOR

.

**See Also:** Constant Field Values

- MOVE_CURSOR

```java
@Deprecated

public static final int MOVE_CURSOR
```

Deprecated.

replaced by

Cursor.MOVE_CURSOR

.

**See Also:** Constant Field Values

- NORMAL

```java
public static final int NORMAL
```

Frame is in the "normal" state. This symbolic constant names a
frame state with all state bits cleared.

**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

- ICONIFIED

```java
public static final int ICONIFIED
```

This state bit indicates that frame is iconified.

**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

- MAXIMIZED_HORIZ

```java
public static final int MAXIMIZED_HORIZ
```

This state bit indicates that frame is maximized in the
horizontal direction.

**Since:** 1.4
**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

- MAXIMIZED_VERT

```java
public static final int MAXIMIZED_VERT
```

This state bit indicates that frame is maximized in the
vertical direction.

**Since:** 1.4
**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

- MAXIMIZED_BOTH

```java
public static final int MAXIMIZED_BOTH
```

This state bit mask indicates that frame is fully maximized
(that is both horizontally and vertically). It is just a
convenience alias for

MAXIMIZED_VERT | MAXIMIZED_HORIZ

.

Note that the correct test for frame being fully maximized is

```java
(state & Frame.MAXIMIZED_BOTH) == Frame.MAXIMIZED_BOTH
```

To test is frame is maximized in

some

direction use

```java
(state & Frame.MAXIMIZED_BOTH) != 0
```

**Since:** 1.4
**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Frame

```java
public Frame()
throws
HeadlessException
```

Constructs a new instance of

Frame

that is
initially invisible. The title of the

Frame

is empty.

**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Frame

```java
public Frame​(
GraphicsConfiguration
gc)
```

Constructs a new, initially invisible

Frame

with the
specified

GraphicsConfiguration

.

**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device. If

gc

is

null

, the system default

GraphicsConfiguration

is assumed.
**Throws:** IllegalArgumentException

- if

gc

is not from a screen device.
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

- Frame

```java
public Frame​(
String
title)
throws
HeadlessException
```

Constructs a new, initially invisible

Frame

object
with the specified title.

**Parameters:** title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

GraphicsConfiguration.getBounds()

- Frame

```java
public Frame​(
String
title,

GraphicsConfiguration
gc)
```

Constructs a new, initially invisible

Frame

object
with the specified title and a

GraphicsConfiguration

.

**Parameters:** title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device. If

gc

is

null

, the system default

GraphicsConfiguration

is assumed.
**Throws:** IllegalArgumentException

- if

gc

is not from a screen device.
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

GraphicsConfiguration.getBounds()

============ METHOD DETAIL ==========

- Method Detail

- addNotify

```java
public void addNotify()
```

Makes this Frame displayable by connecting it to
a native screen resource. Making a frame displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Window
**See Also:** Component.isDisplayable()

,

removeNotify()

- getTitle

```java
public
String
getTitle()
```

Gets the title of the frame. The title is displayed in the
frame's border.

**Returns:** the title of this frame, or an empty string ("")
if this frame doesn't have a title.
**See Also:** setTitle(String)

- setTitle

```java
public void setTitle​(
String
title)
```

Sets the title for this frame to the specified string.

**Parameters:** title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
**See Also:** getTitle()

- getIconImage

```java
public
Image
getIconImage()
```

Returns the image to be displayed as the icon for this frame.

This method is obsolete and kept for backward compatibility
only. Use

Window.getIconImages()

instead.

If a list of several images was specified as a Window's icon,
this method will return the first item of the list.

**Returns:** the icon image for this frame, or

null

if this frame doesn't have an icon image.
**See Also:** Window.setIconImage(Image)

,

Window.getIconImages()

,

Window.setIconImages(java.util.List<? extends java.awt.Image>)

- getMenuBar

```java
public
MenuBar
getMenuBar()
```

Gets the menu bar for this frame.

**Returns:** the menu bar for this frame, or

null

if this frame doesn't have a menu bar.
**See Also:** setMenuBar(MenuBar)

- setMenuBar

```java
public void setMenuBar​(
MenuBar
mb)
```

Sets the menu bar for this frame to the specified menu bar.

**Parameters:** mb

- the menu bar being set.
If this parameter is

null

then any
existing menu bar on this frame is removed.
**See Also:** getMenuBar()

- isResizable

```java
public boolean isResizable()
```

Indicates whether this frame is resizable by the user.
By default, all frames are initially resizable.

**Returns:** true

if the user can resize this frame;

false

otherwise.
**See Also:** setResizable(boolean)

- setResizable

```java
public void setResizable​(boolean resizable)
```

Sets whether this frame is resizable by the user.

**Parameters:** resizable

-

true

if this frame is resizable;

false

otherwise.
**See Also:** isResizable()

- setState

```java
public void setState​(int state)
```

Sets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with applications developed
earlier this method still accepts

Frame.NORMAL

and

Frame.ICONIFIED

only. The iconic
state of the frame is only changed, other aspects
of frame state are not affected by this method. If
the state passed to this method is neither

Frame.NORMAL

nor

Frame.ICONIFIED

the
method performs no actions at all.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getState()

method will be
changed. The application may determine whether a
specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

**Parameters:** state

- either

Frame.NORMAL

or

Frame.ICONIFIED

.
**See Also:** setExtendedState(int)

,

Window.addWindowStateListener(java.awt.event.WindowStateListener)

- setExtendedState

```java
public void setExtendedState​(int state)
```

Sets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getExtendedState()

method will
be changed. The application may determine whether
a specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

**Parameters:** state

- a bitwise mask of frame state constants
**Since:** 1.4
**See Also:** Window.addWindowStateListener(java.awt.event.WindowStateListener)

- getState

```java
public int getState()
```

Gets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with old programs this method still returns

Frame.NORMAL

and

Frame.ICONIFIED

but
it only reports the iconic state of the frame, other aspects of
frame state are not reported by this method.

**Returns:** Frame.NORMAL

or

Frame.ICONIFIED

.
**See Also:** setState(int)

,

getExtendedState()

- getExtendedState

```java
public int getExtendedState()
```

Gets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

**Returns:** a bitwise mask of frame state constants
**Since:** 1.4
**See Also:** setExtendedState(int)

- setMaximizedBounds

```java
public void setMaximizedBounds​(
Rectangle
bounds)
```

Sets the maximized bounds for this frame.

When a frame is in maximized state the system supplies some
defaults bounds. This method allows some or all of those
system supplied values to be overridden.

If

bounds

is

null

, accept bounds
supplied by the system. If non-

null

you can
override some of the system supplied values while accepting
others by setting those fields you want to accept from system
to

Integer.MAX_VALUE

.

Note, the given maximized bounds are used as a hint for the native
system, because the underlying platform may not support setting the
location and/or size of the maximized windows. If that is the case, the
provided values do not affect the appearance of the frame in the
maximized state.

**Parameters:** bounds

- bounds for the maximized state
**Since:** 1.4
**See Also:** getMaximizedBounds()

- getMaximizedBounds

```java
public
Rectangle
getMaximizedBounds()
```

Gets maximized bounds for this frame.
Some fields may contain

Integer.MAX_VALUE

to indicate
that system supplied values for this field must be used.

**Returns:** maximized bounds for this frame; may be

null
**Since:** 1.4
**See Also:** setMaximizedBounds(Rectangle)

- setUndecorated

```java
public void setUndecorated​(boolean undecorated)
```

Disables or enables decorations for this frame.

This method can only be called while the frame is not displayable. To
make this frame decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

**Parameters:** undecorated

-

true

if no frame decorations are to be
enabled;

false

if frame decorations are to be enabled
**Throws:** IllegalComponentStateException

- if the frame is displayable
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this frame does not have the default shape
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this frame opacity is less than

1.0f
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and the alpha value of this frame background
color is less than

1.0f
**Since:** 1.4
**See Also:** isUndecorated()

,

Component.isDisplayable()

,

Window.getShape()

,

Window.getOpacity()

,

Window.getBackground()

,

JFrame.setDefaultLookAndFeelDecorated(boolean)

- isUndecorated

```java
public boolean isUndecorated()
```

Indicates whether this frame is undecorated.
By default, all frames are initially decorated.

**Returns:** true

if frame is undecorated;

false

otherwise.
**Since:** 1.4
**See Also:** setUndecorated(boolean)

- remove

```java
public void remove​(
MenuComponent
m)
```

Removes the specified menu bar from this frame.

**Specified by:** remove

in interface

MenuContainer
**Overrides:** remove

in class

Component
**Parameters:** m

- the menu component to remove.
If

m

is

null

, then
no action is taken
**See Also:** Component.add(PopupMenu)

- removeNotify

```java
public void removeNotify()
```

Makes this Frame undisplayable by removing its connection
to its native screen resource. Making a Frame undisplayable
will cause any of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:** removeNotify

in class

Container
**See Also:** Component.isDisplayable()

,

addNotify()

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Frame

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Container
**Returns:** the parameter string of this frame

- setCursor

```java
@Deprecated

public void setCursor​(int cursorType)
```

Deprecated.

As of JDK version 1.1,
replaced by

Component.setCursor(Cursor)

.

Sets the cursor for this frame to the specified type.

**Parameters:** cursorType

- the cursor type

- getCursorType

```java
@Deprecated

public int getCursorType()
```

Deprecated.

As of JDK version 1.1,
replaced by

Component.getCursor()

.

**Returns:** the cursor type for this frame

- getFrames

```java
public static
Frame
[] getFrames()
```

Returns an array of all

Frame

s created by this application.
If called from an applet, the array includes only the

Frame

s
accessible by that applet.

Warning:

this method may return system created frames, such
as a shared, hidden frame which is used by Swing. Applications
should not assume the existence of these frames, nor should an
application assume anything about these frames such as component
positions,

LayoutManager

s or serialization.

Note

: To obtain a list of all ownerless windows, including
ownerless

Dialog

s (introduced in release 1.6), use

Window.getOwnerlessWindows

.

**Returns:** the array of all

Frame

s created by this application
**Since:** 1.2
**See Also:** Window.getWindows()

,

Window.getOwnerlessWindows()

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Frame.
For frames, the AccessibleContext takes the form of an
AccessibleAWTFrame.
A new AccessibleAWTFrame instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Window
**Returns:** an AccessibleAWTFrame that serves as the
AccessibleContext of this Frame
**Since:** 1.3

Field Detail

- DEFAULT_CURSOR

```java
@Deprecated

public static final int DEFAULT_CURSOR
```

Deprecated.

replaced by

Cursor.DEFAULT_CURSOR

.

**See Also:** Constant Field Values

- CROSSHAIR_CURSOR

```java
@Deprecated

public static final int CROSSHAIR_CURSOR
```

Deprecated.

replaced by

Cursor.CROSSHAIR_CURSOR

.

**See Also:** Constant Field Values

- TEXT_CURSOR

```java
@Deprecated

public static final int TEXT_CURSOR
```

Deprecated.

replaced by

Cursor.TEXT_CURSOR

.

**See Also:** Constant Field Values

- WAIT_CURSOR

```java
@Deprecated

public static final int WAIT_CURSOR
```

Deprecated.

replaced by

Cursor.WAIT_CURSOR

.

**See Also:** Constant Field Values

- SW_RESIZE_CURSOR

```java
@Deprecated

public static final int SW_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.SW_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- SE_RESIZE_CURSOR

```java
@Deprecated

public static final int SE_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.SE_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- NW_RESIZE_CURSOR

```java
@Deprecated

public static final int NW_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.NW_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- NE_RESIZE_CURSOR

```java
@Deprecated

public static final int NE_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.NE_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- N_RESIZE_CURSOR

```java
@Deprecated

public static final int N_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.N_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- S_RESIZE_CURSOR

```java
@Deprecated

public static final int S_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.S_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- W_RESIZE_CURSOR

```java
@Deprecated

public static final int W_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.W_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- E_RESIZE_CURSOR

```java
@Deprecated

public static final int E_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.E_RESIZE_CURSOR

.

**See Also:** Constant Field Values

- HAND_CURSOR

```java
@Deprecated

public static final int HAND_CURSOR
```

Deprecated.

replaced by

Cursor.HAND_CURSOR

.

**See Also:** Constant Field Values

- MOVE_CURSOR

```java
@Deprecated

public static final int MOVE_CURSOR
```

Deprecated.

replaced by

Cursor.MOVE_CURSOR

.

**See Also:** Constant Field Values

- NORMAL

```java
public static final int NORMAL
```

Frame is in the "normal" state. This symbolic constant names a
frame state with all state bits cleared.

**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

- ICONIFIED

```java
public static final int ICONIFIED
```

This state bit indicates that frame is iconified.

**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

- MAXIMIZED_HORIZ

```java
public static final int MAXIMIZED_HORIZ
```

This state bit indicates that frame is maximized in the
horizontal direction.

**Since:** 1.4
**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

- MAXIMIZED_VERT

```java
public static final int MAXIMIZED_VERT
```

This state bit indicates that frame is maximized in the
vertical direction.

**Since:** 1.4
**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

- MAXIMIZED_BOTH

```java
public static final int MAXIMIZED_BOTH
```

This state bit mask indicates that frame is fully maximized
(that is both horizontally and vertically). It is just a
convenience alias for

MAXIMIZED_VERT | MAXIMIZED_HORIZ

.

Note that the correct test for frame being fully maximized is

```java
(state & Frame.MAXIMIZED_BOTH) == Frame.MAXIMIZED_BOTH
```

To test is frame is maximized in

some

direction use

```java
(state & Frame.MAXIMIZED_BOTH) != 0
```

**Since:** 1.4
**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

---

#### Field Detail

DEFAULT_CURSOR

```java
@Deprecated

public static final int DEFAULT_CURSOR
```

Deprecated.

replaced by

Cursor.DEFAULT_CURSOR

.

**See Also:** Constant Field Values

---

#### DEFAULT_CURSOR

@Deprecated

public static final int DEFAULT_CURSOR

CROSSHAIR_CURSOR

```java
@Deprecated

public static final int CROSSHAIR_CURSOR
```

Deprecated.

replaced by

Cursor.CROSSHAIR_CURSOR

.

**See Also:** Constant Field Values

---

#### CROSSHAIR_CURSOR

@Deprecated

public static final int CROSSHAIR_CURSOR

TEXT_CURSOR

```java
@Deprecated

public static final int TEXT_CURSOR
```

Deprecated.

replaced by

Cursor.TEXT_CURSOR

.

**See Also:** Constant Field Values

---

#### TEXT_CURSOR

@Deprecated

public static final int TEXT_CURSOR

WAIT_CURSOR

```java
@Deprecated

public static final int WAIT_CURSOR
```

Deprecated.

replaced by

Cursor.WAIT_CURSOR

.

**See Also:** Constant Field Values

---

#### WAIT_CURSOR

@Deprecated

public static final int WAIT_CURSOR

SW_RESIZE_CURSOR

```java
@Deprecated

public static final int SW_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.SW_RESIZE_CURSOR

.

**See Also:** Constant Field Values

---

#### SW_RESIZE_CURSOR

@Deprecated

public static final int SW_RESIZE_CURSOR

SE_RESIZE_CURSOR

```java
@Deprecated

public static final int SE_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.SE_RESIZE_CURSOR

.

**See Also:** Constant Field Values

---

#### SE_RESIZE_CURSOR

@Deprecated

public static final int SE_RESIZE_CURSOR

NW_RESIZE_CURSOR

```java
@Deprecated

public static final int NW_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.NW_RESIZE_CURSOR

.

**See Also:** Constant Field Values

---

#### NW_RESIZE_CURSOR

@Deprecated

public static final int NW_RESIZE_CURSOR

NE_RESIZE_CURSOR

```java
@Deprecated

public static final int NE_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.NE_RESIZE_CURSOR

.

**See Also:** Constant Field Values

---

#### NE_RESIZE_CURSOR

@Deprecated

public static final int NE_RESIZE_CURSOR

N_RESIZE_CURSOR

```java
@Deprecated

public static final int N_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.N_RESIZE_CURSOR

.

**See Also:** Constant Field Values

---

#### N_RESIZE_CURSOR

@Deprecated

public static final int N_RESIZE_CURSOR

S_RESIZE_CURSOR

```java
@Deprecated

public static final int S_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.S_RESIZE_CURSOR

.

**See Also:** Constant Field Values

---

#### S_RESIZE_CURSOR

@Deprecated

public static final int S_RESIZE_CURSOR

W_RESIZE_CURSOR

```java
@Deprecated

public static final int W_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.W_RESIZE_CURSOR

.

**See Also:** Constant Field Values

---

#### W_RESIZE_CURSOR

@Deprecated

public static final int W_RESIZE_CURSOR

E_RESIZE_CURSOR

```java
@Deprecated

public static final int E_RESIZE_CURSOR
```

Deprecated.

replaced by

Cursor.E_RESIZE_CURSOR

.

**See Also:** Constant Field Values

---

#### E_RESIZE_CURSOR

@Deprecated

public static final int E_RESIZE_CURSOR

HAND_CURSOR

```java
@Deprecated

public static final int HAND_CURSOR
```

Deprecated.

replaced by

Cursor.HAND_CURSOR

.

**See Also:** Constant Field Values

---

#### HAND_CURSOR

@Deprecated

public static final int HAND_CURSOR

MOVE_CURSOR

```java
@Deprecated

public static final int MOVE_CURSOR
```

Deprecated.

replaced by

Cursor.MOVE_CURSOR

.

**See Also:** Constant Field Values

---

#### MOVE_CURSOR

@Deprecated

public static final int MOVE_CURSOR

NORMAL

```java
public static final int NORMAL
```

Frame is in the "normal" state. This symbolic constant names a
frame state with all state bits cleared.

**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

---

#### NORMAL

public static final int NORMAL

Frame is in the "normal" state. This symbolic constant names a
frame state with all state bits cleared.

ICONIFIED

```java
public static final int ICONIFIED
```

This state bit indicates that frame is iconified.

**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

---

#### ICONIFIED

public static final int ICONIFIED

This state bit indicates that frame is iconified.

MAXIMIZED_HORIZ

```java
public static final int MAXIMIZED_HORIZ
```

This state bit indicates that frame is maximized in the
horizontal direction.

**Since:** 1.4
**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

---

#### MAXIMIZED_HORIZ

public static final int MAXIMIZED_HORIZ

This state bit indicates that frame is maximized in the
horizontal direction.

MAXIMIZED_VERT

```java
public static final int MAXIMIZED_VERT
```

This state bit indicates that frame is maximized in the
vertical direction.

**Since:** 1.4
**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

---

#### MAXIMIZED_VERT

public static final int MAXIMIZED_VERT

This state bit indicates that frame is maximized in the
vertical direction.

MAXIMIZED_BOTH

```java
public static final int MAXIMIZED_BOTH
```

This state bit mask indicates that frame is fully maximized
(that is both horizontally and vertically). It is just a
convenience alias for

MAXIMIZED_VERT | MAXIMIZED_HORIZ

.

Note that the correct test for frame being fully maximized is

```java
(state & Frame.MAXIMIZED_BOTH) == Frame.MAXIMIZED_BOTH
```

To test is frame is maximized in

some

direction use

```java
(state & Frame.MAXIMIZED_BOTH) != 0
```

**Since:** 1.4
**See Also:** setExtendedState(int)

,

getExtendedState()

,

Constant Field Values

---

#### MAXIMIZED_BOTH

public static final int MAXIMIZED_BOTH

This state bit mask indicates that frame is fully maximized
(that is both horizontally and vertically). It is just a
convenience alias for

MAXIMIZED_VERT | MAXIMIZED_HORIZ

.

Note that the correct test for frame being fully maximized is

```java
(state & Frame.MAXIMIZED_BOTH) == Frame.MAXIMIZED_BOTH
```

To test is frame is maximized in

some

direction use

```java
(state & Frame.MAXIMIZED_BOTH) != 0
```

Note that the correct test for frame being fully maximized is

```java
(state & Frame.MAXIMIZED_BOTH) == Frame.MAXIMIZED_BOTH
```

To test is frame is maximized in

some

direction use

```java
(state & Frame.MAXIMIZED_BOTH) != 0
```

(state & Frame.MAXIMIZED_BOTH) == Frame.MAXIMIZED_BOTH

To test is frame is maximized in

some

direction use

```java
(state & Frame.MAXIMIZED_BOTH) != 0
```

(state & Frame.MAXIMIZED_BOTH) != 0

Constructor Detail

- Frame

```java
public Frame()
throws
HeadlessException
```

Constructs a new instance of

Frame

that is
initially invisible. The title of the

Frame

is empty.

**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Frame

```java
public Frame​(
GraphicsConfiguration
gc)
```

Constructs a new, initially invisible

Frame

with the
specified

GraphicsConfiguration

.

**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device. If

gc

is

null

, the system default

GraphicsConfiguration

is assumed.
**Throws:** IllegalArgumentException

- if

gc

is not from a screen device.
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

- Frame

```java
public Frame​(
String
title)
throws
HeadlessException
```

Constructs a new, initially invisible

Frame

object
with the specified title.

**Parameters:** title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

GraphicsConfiguration.getBounds()

- Frame

```java
public Frame​(
String
title,

GraphicsConfiguration
gc)
```

Constructs a new, initially invisible

Frame

object
with the specified title and a

GraphicsConfiguration

.

**Parameters:** title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device. If

gc

is

null

, the system default

GraphicsConfiguration

is assumed.
**Throws:** IllegalArgumentException

- if

gc

is not from a screen device.
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

GraphicsConfiguration.getBounds()

---

#### Constructor Detail

Frame

```java
public Frame()
throws
HeadlessException
```

Constructs a new instance of

Frame

that is
initially invisible. The title of the

Frame

is empty.

**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### Frame

public Frame()
throws

HeadlessException

Constructs a new instance of

Frame

that is
initially invisible. The title of the

Frame

is empty.

Frame

```java
public Frame​(
GraphicsConfiguration
gc)
```

Constructs a new, initially invisible

Frame

with the
specified

GraphicsConfiguration

.

**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device. If

gc

is

null

, the system default

GraphicsConfiguration

is assumed.
**Throws:** IllegalArgumentException

- if

gc

is not from a screen device.
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Frame

public Frame​(

GraphicsConfiguration

gc)

Constructs a new, initially invisible

Frame

with the
specified

GraphicsConfiguration

.

Frame

```java
public Frame​(
String
title)
throws
HeadlessException
```

Constructs a new, initially invisible

Frame

object
with the specified title.

**Parameters:** title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

GraphicsConfiguration.getBounds()

---

#### Frame

public Frame​(

String

title)
throws

HeadlessException

Constructs a new, initially invisible

Frame

object
with the specified title.

Frame

```java
public Frame​(
String
title,

GraphicsConfiguration
gc)
```

Constructs a new, initially invisible

Frame

object
with the specified title and a

GraphicsConfiguration

.

**Parameters:** title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device. If

gc

is

null

, the system default

GraphicsConfiguration

is assumed.
**Throws:** IllegalArgumentException

- if

gc

is not from a screen device.
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

GraphicsConfiguration.getBounds()

---

#### Frame

public Frame​(

String

title,

GraphicsConfiguration

gc)

Constructs a new, initially invisible

Frame

object
with the specified title and a

GraphicsConfiguration

.

Method Detail

- addNotify

```java
public void addNotify()
```

Makes this Frame displayable by connecting it to
a native screen resource. Making a frame displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Window
**See Also:** Component.isDisplayable()

,

removeNotify()

- getTitle

```java
public
String
getTitle()
```

Gets the title of the frame. The title is displayed in the
frame's border.

**Returns:** the title of this frame, or an empty string ("")
if this frame doesn't have a title.
**See Also:** setTitle(String)

- setTitle

```java
public void setTitle​(
String
title)
```

Sets the title for this frame to the specified string.

**Parameters:** title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
**See Also:** getTitle()

- getIconImage

```java
public
Image
getIconImage()
```

Returns the image to be displayed as the icon for this frame.

This method is obsolete and kept for backward compatibility
only. Use

Window.getIconImages()

instead.

If a list of several images was specified as a Window's icon,
this method will return the first item of the list.

**Returns:** the icon image for this frame, or

null

if this frame doesn't have an icon image.
**See Also:** Window.setIconImage(Image)

,

Window.getIconImages()

,

Window.setIconImages(java.util.List<? extends java.awt.Image>)

- getMenuBar

```java
public
MenuBar
getMenuBar()
```

Gets the menu bar for this frame.

**Returns:** the menu bar for this frame, or

null

if this frame doesn't have a menu bar.
**See Also:** setMenuBar(MenuBar)

- setMenuBar

```java
public void setMenuBar​(
MenuBar
mb)
```

Sets the menu bar for this frame to the specified menu bar.

**Parameters:** mb

- the menu bar being set.
If this parameter is

null

then any
existing menu bar on this frame is removed.
**See Also:** getMenuBar()

- isResizable

```java
public boolean isResizable()
```

Indicates whether this frame is resizable by the user.
By default, all frames are initially resizable.

**Returns:** true

if the user can resize this frame;

false

otherwise.
**See Also:** setResizable(boolean)

- setResizable

```java
public void setResizable​(boolean resizable)
```

Sets whether this frame is resizable by the user.

**Parameters:** resizable

-

true

if this frame is resizable;

false

otherwise.
**See Also:** isResizable()

- setState

```java
public void setState​(int state)
```

Sets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with applications developed
earlier this method still accepts

Frame.NORMAL

and

Frame.ICONIFIED

only. The iconic
state of the frame is only changed, other aspects
of frame state are not affected by this method. If
the state passed to this method is neither

Frame.NORMAL

nor

Frame.ICONIFIED

the
method performs no actions at all.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getState()

method will be
changed. The application may determine whether a
specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

**Parameters:** state

- either

Frame.NORMAL

or

Frame.ICONIFIED

.
**See Also:** setExtendedState(int)

,

Window.addWindowStateListener(java.awt.event.WindowStateListener)

- setExtendedState

```java
public void setExtendedState​(int state)
```

Sets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getExtendedState()

method will
be changed. The application may determine whether
a specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

**Parameters:** state

- a bitwise mask of frame state constants
**Since:** 1.4
**See Also:** Window.addWindowStateListener(java.awt.event.WindowStateListener)

- getState

```java
public int getState()
```

Gets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with old programs this method still returns

Frame.NORMAL

and

Frame.ICONIFIED

but
it only reports the iconic state of the frame, other aspects of
frame state are not reported by this method.

**Returns:** Frame.NORMAL

or

Frame.ICONIFIED

.
**See Also:** setState(int)

,

getExtendedState()

- getExtendedState

```java
public int getExtendedState()
```

Gets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

**Returns:** a bitwise mask of frame state constants
**Since:** 1.4
**See Also:** setExtendedState(int)

- setMaximizedBounds

```java
public void setMaximizedBounds​(
Rectangle
bounds)
```

Sets the maximized bounds for this frame.

When a frame is in maximized state the system supplies some
defaults bounds. This method allows some or all of those
system supplied values to be overridden.

If

bounds

is

null

, accept bounds
supplied by the system. If non-

null

you can
override some of the system supplied values while accepting
others by setting those fields you want to accept from system
to

Integer.MAX_VALUE

.

Note, the given maximized bounds are used as a hint for the native
system, because the underlying platform may not support setting the
location and/or size of the maximized windows. If that is the case, the
provided values do not affect the appearance of the frame in the
maximized state.

**Parameters:** bounds

- bounds for the maximized state
**Since:** 1.4
**See Also:** getMaximizedBounds()

- getMaximizedBounds

```java
public
Rectangle
getMaximizedBounds()
```

Gets maximized bounds for this frame.
Some fields may contain

Integer.MAX_VALUE

to indicate
that system supplied values for this field must be used.

**Returns:** maximized bounds for this frame; may be

null
**Since:** 1.4
**See Also:** setMaximizedBounds(Rectangle)

- setUndecorated

```java
public void setUndecorated​(boolean undecorated)
```

Disables or enables decorations for this frame.

This method can only be called while the frame is not displayable. To
make this frame decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

**Parameters:** undecorated

-

true

if no frame decorations are to be
enabled;

false

if frame decorations are to be enabled
**Throws:** IllegalComponentStateException

- if the frame is displayable
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this frame does not have the default shape
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this frame opacity is less than

1.0f
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and the alpha value of this frame background
color is less than

1.0f
**Since:** 1.4
**See Also:** isUndecorated()

,

Component.isDisplayable()

,

Window.getShape()

,

Window.getOpacity()

,

Window.getBackground()

,

JFrame.setDefaultLookAndFeelDecorated(boolean)

- isUndecorated

```java
public boolean isUndecorated()
```

Indicates whether this frame is undecorated.
By default, all frames are initially decorated.

**Returns:** true

if frame is undecorated;

false

otherwise.
**Since:** 1.4
**See Also:** setUndecorated(boolean)

- remove

```java
public void remove​(
MenuComponent
m)
```

Removes the specified menu bar from this frame.

**Specified by:** remove

in interface

MenuContainer
**Overrides:** remove

in class

Component
**Parameters:** m

- the menu component to remove.
If

m

is

null

, then
no action is taken
**See Also:** Component.add(PopupMenu)

- removeNotify

```java
public void removeNotify()
```

Makes this Frame undisplayable by removing its connection
to its native screen resource. Making a Frame undisplayable
will cause any of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:** removeNotify

in class

Container
**See Also:** Component.isDisplayable()

,

addNotify()

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Frame

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Container
**Returns:** the parameter string of this frame

- setCursor

```java
@Deprecated

public void setCursor​(int cursorType)
```

Deprecated.

As of JDK version 1.1,
replaced by

Component.setCursor(Cursor)

.

Sets the cursor for this frame to the specified type.

**Parameters:** cursorType

- the cursor type

- getCursorType

```java
@Deprecated

public int getCursorType()
```

Deprecated.

As of JDK version 1.1,
replaced by

Component.getCursor()

.

**Returns:** the cursor type for this frame

- getFrames

```java
public static
Frame
[] getFrames()
```

Returns an array of all

Frame

s created by this application.
If called from an applet, the array includes only the

Frame

s
accessible by that applet.

Warning:

this method may return system created frames, such
as a shared, hidden frame which is used by Swing. Applications
should not assume the existence of these frames, nor should an
application assume anything about these frames such as component
positions,

LayoutManager

s or serialization.

Note

: To obtain a list of all ownerless windows, including
ownerless

Dialog

s (introduced in release 1.6), use

Window.getOwnerlessWindows

.

**Returns:** the array of all

Frame

s created by this application
**Since:** 1.2
**See Also:** Window.getWindows()

,

Window.getOwnerlessWindows()

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Frame.
For frames, the AccessibleContext takes the form of an
AccessibleAWTFrame.
A new AccessibleAWTFrame instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Window
**Returns:** an AccessibleAWTFrame that serves as the
AccessibleContext of this Frame
**Since:** 1.3

---

#### Method Detail

addNotify

```java
public void addNotify()
```

Makes this Frame displayable by connecting it to
a native screen resource. Making a frame displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Window
**See Also:** Component.isDisplayable()

,

removeNotify()

---

#### addNotify

public void addNotify()

Makes this Frame displayable by connecting it to
a native screen resource. Making a frame displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

getTitle

```java
public
String
getTitle()
```

Gets the title of the frame. The title is displayed in the
frame's border.

**Returns:** the title of this frame, or an empty string ("")
if this frame doesn't have a title.
**See Also:** setTitle(String)

---

#### getTitle

public

String

getTitle()

Gets the title of the frame. The title is displayed in the
frame's border.

setTitle

```java
public void setTitle​(
String
title)
```

Sets the title for this frame to the specified string.

**Parameters:** title

- the title to be displayed in the frame's border.
A

null

value
is treated as an empty string, "".
**See Also:** getTitle()

---

#### setTitle

public void setTitle​(

String

title)

Sets the title for this frame to the specified string.

getIconImage

```java
public
Image
getIconImage()
```

Returns the image to be displayed as the icon for this frame.

This method is obsolete and kept for backward compatibility
only. Use

Window.getIconImages()

instead.

If a list of several images was specified as a Window's icon,
this method will return the first item of the list.

**Returns:** the icon image for this frame, or

null

if this frame doesn't have an icon image.
**See Also:** Window.setIconImage(Image)

,

Window.getIconImages()

,

Window.setIconImages(java.util.List<? extends java.awt.Image>)

---

#### getIconImage

public

Image

getIconImage()

Returns the image to be displayed as the icon for this frame.

This method is obsolete and kept for backward compatibility
only. Use

Window.getIconImages()

instead.

If a list of several images was specified as a Window's icon,
this method will return the first item of the list.

This method is obsolete and kept for backward compatibility
only. Use

Window.getIconImages()

instead.

If a list of several images was specified as a Window's icon,
this method will return the first item of the list.

If a list of several images was specified as a Window's icon,
this method will return the first item of the list.

getMenuBar

```java
public
MenuBar
getMenuBar()
```

Gets the menu bar for this frame.

**Returns:** the menu bar for this frame, or

null

if this frame doesn't have a menu bar.
**See Also:** setMenuBar(MenuBar)

---

#### getMenuBar

public

MenuBar

getMenuBar()

Gets the menu bar for this frame.

setMenuBar

```java
public void setMenuBar​(
MenuBar
mb)
```

Sets the menu bar for this frame to the specified menu bar.

**Parameters:** mb

- the menu bar being set.
If this parameter is

null

then any
existing menu bar on this frame is removed.
**See Also:** getMenuBar()

---

#### setMenuBar

public void setMenuBar​(

MenuBar

mb)

Sets the menu bar for this frame to the specified menu bar.

isResizable

```java
public boolean isResizable()
```

Indicates whether this frame is resizable by the user.
By default, all frames are initially resizable.

**Returns:** true

if the user can resize this frame;

false

otherwise.
**See Also:** setResizable(boolean)

---

#### isResizable

public boolean isResizable()

Indicates whether this frame is resizable by the user.
By default, all frames are initially resizable.

setResizable

```java
public void setResizable​(boolean resizable)
```

Sets whether this frame is resizable by the user.

**Parameters:** resizable

-

true

if this frame is resizable;

false

otherwise.
**See Also:** isResizable()

---

#### setResizable

public void setResizable​(boolean resizable)

Sets whether this frame is resizable by the user.

setState

```java
public void setState​(int state)
```

Sets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with applications developed
earlier this method still accepts

Frame.NORMAL

and

Frame.ICONIFIED

only. The iconic
state of the frame is only changed, other aspects
of frame state are not affected by this method. If
the state passed to this method is neither

Frame.NORMAL

nor

Frame.ICONIFIED

the
method performs no actions at all.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getState()

method will be
changed. The application may determine whether a
specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

**Parameters:** state

- either

Frame.NORMAL

or

Frame.ICONIFIED

.
**See Also:** setExtendedState(int)

,

Window.addWindowStateListener(java.awt.event.WindowStateListener)

---

#### setState

public void setState​(int state)

Sets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with applications developed
earlier this method still accepts

Frame.NORMAL

and

Frame.ICONIFIED

only. The iconic
state of the frame is only changed, other aspects
of frame state are not affected by this method. If
the state passed to this method is neither

Frame.NORMAL

nor

Frame.ICONIFIED

the
method performs no actions at all.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getState()

method will be
changed. The application may determine whether a
specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with applications developed
earlier this method still accepts

Frame.NORMAL

and

Frame.ICONIFIED

only. The iconic
state of the frame is only changed, other aspects
of frame state are not affected by this method. If
the state passed to this method is neither

Frame.NORMAL

nor

Frame.ICONIFIED

the
method performs no actions at all.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getState()

method will be
changed. The application may determine whether a
specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

For compatibility with applications developed
earlier this method still accepts

Frame.NORMAL

and

Frame.ICONIFIED

only. The iconic
state of the frame is only changed, other aspects
of frame state are not affected by this method. If
the state passed to this method is neither

Frame.NORMAL

nor

Frame.ICONIFIED

the
method performs no actions at all.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getState()

method will be
changed. The application may determine whether a
specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getState()

method will be
changed. The application may determine whether a
specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

setExtendedState

```java
public void setExtendedState​(int state)
```

Sets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getExtendedState()

method will
be changed. The application may determine whether
a specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

**Parameters:** state

- a bitwise mask of frame state constants
**Since:** 1.4
**See Also:** Window.addWindowStateListener(java.awt.event.WindowStateListener)

---

#### setExtendedState

public void setExtendedState​(int state)

Sets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getExtendedState()

method will
be changed. The application may determine whether
a specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

Note that if the state is not supported on a
given platform, neither the state nor the return
value of the

getExtendedState()

method will
be changed. The application may determine whether
a specific state is supported via the

Toolkit.isFrameStateSupported(int)

method.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

If the frame is currently visible on the
screen

(the

Window.isShowing()

method returns

true

), the developer should examine the
return value of the

WindowEvent.getNewState()

method of
the

WindowEvent

received through the

WindowStateListener

to
determine that the state has actually been
changed.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

If the frame is not visible on the
screen

, the events may or may not be
generated. In this case the developer may assume
that the state changes immediately after this
method returns. Later, when the

setVisible(true)

method is invoked, the frame
will attempt to apply this state. Receiving any

WindowEvent.WINDOW_STATE_CHANGED

events is not guaranteed in this case also.

getState

```java
public int getState()
```

Gets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with old programs this method still returns

Frame.NORMAL

and

Frame.ICONIFIED

but
it only reports the iconic state of the frame, other aspects of
frame state are not reported by this method.

**Returns:** Frame.NORMAL

or

Frame.ICONIFIED

.
**See Also:** setState(int)

,

getExtendedState()

---

#### getState

public int getState()

Gets the state of this frame (obsolete).

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with old programs this method still returns

Frame.NORMAL

and

Frame.ICONIFIED

but
it only reports the iconic state of the frame, other aspects of
frame state are not reported by this method.

In older versions of JDK a frame state could only be NORMAL or
ICONIFIED. Since JDK 1.4 set of supported frame states is
expanded and frame state is represented as a bitwise mask.

For compatibility with old programs this method still returns

Frame.NORMAL

and

Frame.ICONIFIED

but
it only reports the iconic state of the frame, other aspects of
frame state are not reported by this method.

For compatibility with old programs this method still returns

Frame.NORMAL

and

Frame.ICONIFIED

but
it only reports the iconic state of the frame, other aspects of
frame state are not reported by this method.

getExtendedState

```java
public int getExtendedState()
```

Gets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

**Returns:** a bitwise mask of frame state constants
**Since:** 1.4
**See Also:** setExtendedState(int)

---

#### getExtendedState

public int getExtendedState()

Gets the state of this frame. The state is
represented as a bitwise mask.

- NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

NORMAL

Indicates that no state bits are set.

ICONIFIED

MAXIMIZED_HORIZ

MAXIMIZED_VERT

MAXIMIZED_BOTH

Concatenates

MAXIMIZED_HORIZ

and

MAXIMIZED_VERT

.

setMaximizedBounds

```java
public void setMaximizedBounds​(
Rectangle
bounds)
```

Sets the maximized bounds for this frame.

When a frame is in maximized state the system supplies some
defaults bounds. This method allows some or all of those
system supplied values to be overridden.

If

bounds

is

null

, accept bounds
supplied by the system. If non-

null

you can
override some of the system supplied values while accepting
others by setting those fields you want to accept from system
to

Integer.MAX_VALUE

.

Note, the given maximized bounds are used as a hint for the native
system, because the underlying platform may not support setting the
location and/or size of the maximized windows. If that is the case, the
provided values do not affect the appearance of the frame in the
maximized state.

**Parameters:** bounds

- bounds for the maximized state
**Since:** 1.4
**See Also:** getMaximizedBounds()

---

#### setMaximizedBounds

public void setMaximizedBounds​(

Rectangle

bounds)

Sets the maximized bounds for this frame.

When a frame is in maximized state the system supplies some
defaults bounds. This method allows some or all of those
system supplied values to be overridden.

If

bounds

is

null

, accept bounds
supplied by the system. If non-

null

you can
override some of the system supplied values while accepting
others by setting those fields you want to accept from system
to

Integer.MAX_VALUE

.

Note, the given maximized bounds are used as a hint for the native
system, because the underlying platform may not support setting the
location and/or size of the maximized windows. If that is the case, the
provided values do not affect the appearance of the frame in the
maximized state.

When a frame is in maximized state the system supplies some
defaults bounds. This method allows some or all of those
system supplied values to be overridden.

If

bounds

is

null

, accept bounds
supplied by the system. If non-

null

you can
override some of the system supplied values while accepting
others by setting those fields you want to accept from system
to

Integer.MAX_VALUE

.

Note, the given maximized bounds are used as a hint for the native
system, because the underlying platform may not support setting the
location and/or size of the maximized windows. If that is the case, the
provided values do not affect the appearance of the frame in the
maximized state.

If

bounds

is

null

, accept bounds
supplied by the system. If non-

null

you can
override some of the system supplied values while accepting
others by setting those fields you want to accept from system
to

Integer.MAX_VALUE

.

Note, the given maximized bounds are used as a hint for the native
system, because the underlying platform may not support setting the
location and/or size of the maximized windows. If that is the case, the
provided values do not affect the appearance of the frame in the
maximized state.

Note, the given maximized bounds are used as a hint for the native
system, because the underlying platform may not support setting the
location and/or size of the maximized windows. If that is the case, the
provided values do not affect the appearance of the frame in the
maximized state.

getMaximizedBounds

```java
public
Rectangle
getMaximizedBounds()
```

Gets maximized bounds for this frame.
Some fields may contain

Integer.MAX_VALUE

to indicate
that system supplied values for this field must be used.

**Returns:** maximized bounds for this frame; may be

null
**Since:** 1.4
**See Also:** setMaximizedBounds(Rectangle)

---

#### getMaximizedBounds

public

Rectangle

getMaximizedBounds()

Gets maximized bounds for this frame.
Some fields may contain

Integer.MAX_VALUE

to indicate
that system supplied values for this field must be used.

setUndecorated

```java
public void setUndecorated​(boolean undecorated)
```

Disables or enables decorations for this frame.

This method can only be called while the frame is not displayable. To
make this frame decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

**Parameters:** undecorated

-

true

if no frame decorations are to be
enabled;

false

if frame decorations are to be enabled
**Throws:** IllegalComponentStateException

- if the frame is displayable
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this frame does not have the default shape
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this frame opacity is less than

1.0f
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and the alpha value of this frame background
color is less than

1.0f
**Since:** 1.4
**See Also:** isUndecorated()

,

Component.isDisplayable()

,

Window.getShape()

,

Window.getOpacity()

,

Window.getBackground()

,

JFrame.setDefaultLookAndFeelDecorated(boolean)

---

#### setUndecorated

public void setUndecorated​(boolean undecorated)

Disables or enables decorations for this frame.

This method can only be called while the frame is not displayable. To
make this frame decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

This method can only be called while the frame is not displayable. To
make this frame decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

isUndecorated

```java
public boolean isUndecorated()
```

Indicates whether this frame is undecorated.
By default, all frames are initially decorated.

**Returns:** true

if frame is undecorated;

false

otherwise.
**Since:** 1.4
**See Also:** setUndecorated(boolean)

---

#### isUndecorated

public boolean isUndecorated()

Indicates whether this frame is undecorated.
By default, all frames are initially decorated.

remove

```java
public void remove​(
MenuComponent
m)
```

Removes the specified menu bar from this frame.

**Specified by:** remove

in interface

MenuContainer
**Overrides:** remove

in class

Component
**Parameters:** m

- the menu component to remove.
If

m

is

null

, then
no action is taken
**See Also:** Component.add(PopupMenu)

---

#### remove

public void remove​(

MenuComponent

m)

Removes the specified menu bar from this frame.

removeNotify

```java
public void removeNotify()
```

Makes this Frame undisplayable by removing its connection
to its native screen resource. Making a Frame undisplayable
will cause any of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:** removeNotify

in class

Container
**See Also:** Component.isDisplayable()

,

addNotify()

---

#### removeNotify

public void removeNotify()

Makes this Frame undisplayable by removing its connection
to its native screen resource. Making a Frame undisplayable
will cause any of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Frame

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Container
**Returns:** the parameter string of this frame

---

#### paramString

protected

String

paramString()

Returns a string representing the state of this

Frame

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

setCursor

```java
@Deprecated

public void setCursor​(int cursorType)
```

Deprecated.

As of JDK version 1.1,
replaced by

Component.setCursor(Cursor)

.

Sets the cursor for this frame to the specified type.

**Parameters:** cursorType

- the cursor type

---

#### setCursor

@Deprecated

public void setCursor​(int cursorType)

Sets the cursor for this frame to the specified type.

getCursorType

```java
@Deprecated

public int getCursorType()
```

Deprecated.

As of JDK version 1.1,
replaced by

Component.getCursor()

.

**Returns:** the cursor type for this frame

---

#### getCursorType

@Deprecated

public int getCursorType()

getFrames

```java
public static
Frame
[] getFrames()
```

Returns an array of all

Frame

s created by this application.
If called from an applet, the array includes only the

Frame

s
accessible by that applet.

Warning:

this method may return system created frames, such
as a shared, hidden frame which is used by Swing. Applications
should not assume the existence of these frames, nor should an
application assume anything about these frames such as component
positions,

LayoutManager

s or serialization.

Note

: To obtain a list of all ownerless windows, including
ownerless

Dialog

s (introduced in release 1.6), use

Window.getOwnerlessWindows

.

**Returns:** the array of all

Frame

s created by this application
**Since:** 1.2
**See Also:** Window.getWindows()

,

Window.getOwnerlessWindows()

---

#### getFrames

public static

Frame

[] getFrames()

Returns an array of all

Frame

s created by this application.
If called from an applet, the array includes only the

Frame

s
accessible by that applet.

Warning:

this method may return system created frames, such
as a shared, hidden frame which is used by Swing. Applications
should not assume the existence of these frames, nor should an
application assume anything about these frames such as component
positions,

LayoutManager

s or serialization.

Note

: To obtain a list of all ownerless windows, including
ownerless

Dialog

s (introduced in release 1.6), use

Window.getOwnerlessWindows

.

Warning:

this method may return system created frames, such
as a shared, hidden frame which is used by Swing. Applications
should not assume the existence of these frames, nor should an
application assume anything about these frames such as component
positions,

LayoutManager

s or serialization.

Note

: To obtain a list of all ownerless windows, including
ownerless

Dialog

s (introduced in release 1.6), use

Window.getOwnerlessWindows

.

Note

: To obtain a list of all ownerless windows, including
ownerless

Dialog

s (introduced in release 1.6), use

Window.getOwnerlessWindows

.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Frame.
For frames, the AccessibleContext takes the form of an
AccessibleAWTFrame.
A new AccessibleAWTFrame instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Window
**Returns:** an AccessibleAWTFrame that serves as the
AccessibleContext of this Frame
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this Frame.
For frames, the AccessibleContext takes the form of an
AccessibleAWTFrame.
A new AccessibleAWTFrame instance is created if necessary.

---

