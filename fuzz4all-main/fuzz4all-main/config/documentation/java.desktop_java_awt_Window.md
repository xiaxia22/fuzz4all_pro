# Class Window

**Source:** `java.desktop\java\awt\Window.html`

### Class Description

```java
public class
Window

extends
Container

implements
Accessible
```

A

Window

object is a top-level window with no borders and no
menubar.
The default layout for a window is

BorderLayout

.

A window must have either a frame, dialog, or another window defined as its
owner when it's constructed.

In a multi-screen environment, you can create a

Window

on a different screen device by constructing the

Window

with

Window(Window, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual device coordinate system.
The origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location of
the primary screen in the virtual device, negative coordinates are
possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Window

returns
virtual device coordinates. Call the

getBounds

method
of a

GraphicsConfiguration

to find its origin in the virtual
coordinate system.

The following code sets the location of a

Window

at (10, 10) relative to the origin of the physical screen
of the corresponding

GraphicsConfiguration

. If the
bounds of the

GraphicsConfiguration

is not taken
into account, the

Window

location would be set
at (10, 10) relative to the virtual-coordinate system and would appear
on the primary physical screen, which might be different from the
physical screen of the specified

GraphicsConfiguration

.

```java
Window w = new Window(Window owner, GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
w.setLocation(10 + bounds.x, 10 + bounds.y);
```

Note: the location and size of top-level windows (including

Window

s,

Frame

s, and

Dialog

s)
are under the control of the desktop's window management system.
Calls to

setLocation

,

setSize

, and

setBounds

are requests (not directives) which are
forwarded to the window management system. Every effort will be
made to honor such requests. However, in some cases the window
management system may ignore such requests, or modify the requested
geometry in order to place and size the

Window

in a way
that more closely matches the desktop settings.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

*No entries found.*

### Constructor Details

#### public Window​(
Frame
owner)

Constructs a new, initially invisible window with the specified

Frame

as its owner. The window will not be focusable
unless its owner is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a warning
banner is created.

**Parameters:**
- owner

- the

Frame

to act as owner or

null

if this window has no owner

**Throws:**
- IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

isShowing()

---

#### public Window​(
Window
owner)

Constructs a new, initially invisible window with the specified

Window

as its owner. This window will not be focusable
unless its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a
warning banner is created.

**Parameters:**
- owner

- the

Window

to act as owner or

null

if this window has no owner

**Throws:**
- IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

isShowing()

**Since:**
- 1.2

---

#### public Window​(
Window
owner,

GraphicsConfiguration
gc)

Constructs a new, initially invisible window with the specified owner

Window

and a

GraphicsConfiguration

of a screen device. The Window will not be focusable unless
its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

. If that
check fails with a

SecurityException

then a warning banner
is created.

**Parameters:**
- owner

- the window to act as owner or

null

if this window has no owner
- gc

- the

GraphicsConfiguration

of the target
screen device; if

gc

is

null

,
the system default

GraphicsConfiguration

is assumed

**Throws:**
- IllegalArgumentException

- if

gc

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

GraphicsConfiguration.getBounds()

,

isShowing()

**Since:**
- 1.3

---

### Method Details

#### public
List
<
Image
> getIconImages()

Returns the sequence of images to be displayed as the icon for this window.

This method returns a copy of the internally stored list, so all operations
on the returned object will not affect the window's behavior.

**Returns:**
- the copy of icon images' list for this window, or
empty list if this window doesn't have icon images.

**See Also:**
- setIconImages(java.util.List<? extends java.awt.Image>)

,

setIconImage(Image)

**Since:**
- 1.6

---

#### public void setIconImages​(
List
<? extends
Image
> icons)

Sets the sequence of images to be displayed as the icon
for this window. Subsequent calls to

getIconImages

will
always return a copy of the

icons

list.

Depending on the platform capabilities one or several images
of different dimensions will be used as the window's icon.

The

icons

list can contain

MultiResolutionImage

images also.
Suitable image depending on screen resolution is extracted from
base

MultiResolutionImage

image and added to the icons list
while base resolution image is removed from list.
The

icons

list is scanned for the images of most
appropriate dimensions from the beginning. If the list contains
several images of the same size, the first will be used.

Ownerless windows with no icon specified use platform-default icon.
The icon of an owned window may be inherited from the owner
unless explicitly overridden.
Setting the icon to

null

or empty list restores
the default behavior.

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

**Parameters:**
- icons

- the list of icon images to be displayed.

**See Also:**
- getIconImages()

,

setIconImage(Image)

**Since:**
- 1.6

---

#### public void setIconImage​(
Image
image)

Sets the image to be displayed as the icon for this window.

This method can be used instead of

setIconImages()

to specify a single image as a window's icon.

The following statement:

```java
setIconImage(image);
```

is equivalent to:

```java
ArrayList<Image> imageList = new ArrayList<Image>();
imageList.add(image);
setIconImages(imageList);
```

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

**Parameters:**
- image

- the icon image to be displayed.

**See Also:**
- setIconImages(java.util.List<? extends java.awt.Image>)

,

getIconImages()

**Since:**
- 1.6

---

#### public void addNotify()

Makes this Window displayable by creating the connection to its
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:**
- addNotify

in class

Container

**See Also:**
- Component.isDisplayable()

,

Container.removeNotify()

**Since:**
- 1.0

---

#### public void pack()

Causes this Window to be sized to fit the preferred size
and layouts of its subcomponents. The resulting width and
height of the window are automatically enlarged if either
of dimensions is less than the minimum size as specified
by the previous call to the

setMinimumSize

method.

If the window and/or its owner are not displayable yet,
both of them are made displayable before calculating
the preferred size. The Window is validated after its
size is being calculated.

**See Also:**
- Component.isDisplayable()

,

setMinimumSize(java.awt.Dimension)

---

#### public void setMinimumSize​(
Dimension
minimumSize)

Sets the minimum size of this window to a constant
value. Subsequent calls to

getMinimumSize

will always return this value. If current window's
size is less than

minimumSize

the size of the
window is automatically enlarged to honor the minimum size.

If the

setSize

or

setBounds

methods
are called afterwards with a width or height less than
that was specified by the

setMinimumSize

method
the window is automatically enlarged to meet
the

minimumSize

value. The

minimumSize

value also affects the behaviour of the

pack

method.

The default behavior is restored by setting the minimum size
parameter to the

null

value.

Resizing operation may be restricted if the user tries
to resize window below the

minimumSize

value.
This behaviour is platform-dependent.

**Overrides:**
- setMinimumSize

in class

Component

**Parameters:**
- minimumSize

- the new minimum size of this window

**See Also:**
- Component.setMinimumSize(java.awt.Dimension)

,

Container.getMinimumSize()

,

Component.isMinimumSizeSet()

,

setSize(Dimension)

,

pack()

**Since:**
- 1.6

---

#### public void setSize​(
Dimension
d)

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

d.width

and

d.height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:**
- setSize

in class

Component

**Parameters:**
- d

- the dimension specifying the new size
of this component

**See Also:**
- Component.getSize()

,

setBounds(int, int, int, int)

,

setMinimumSize(java.awt.Dimension)

**Since:**
- 1.6

---

#### public void setSize​(int width,
int height)

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

and

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:**
- setSize

in class

Component

**Parameters:**
- width

- the new width of this component in pixels
- height

- the new height of this component in pixels

**See Also:**
- Component.getSize()

,

setBounds(int, int, int, int)

,

setMinimumSize(java.awt.Dimension)

**Since:**
- 1.6

---

#### public void setLocation​(int x,
int y)

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:**
- setLocation

in class

Component

**Parameters:**
- x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
- y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space

**See Also:**
- Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

---

#### public void setLocation​(
Point
p)

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:**
- setLocation

in class

Component

**Parameters:**
- p

- the point defining the top-left corner
of the new location, given in the coordinate space of this
component's parent

**See Also:**
- Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

---

#### @Deprecated

public void reshape​(int x,
int y,
int width,
int height)

Description copied from class:

Component

**Overrides:**
- reshape

in class

Component

**Parameters:**
- x

- the

x

coordinate of the upper left corner of the rectangle
- y

- the

y

coordinate of the upper left corner of the rectangle
- width

- the width of the rectangle
- height

- the height of the rectangle

---

#### public void setVisible​(boolean b)

Shows or hides this

Window

depending on the value of parameter

b

.

If the method shows the window then the window is also made
focused under the following conditions:

- The

Window

meets the requirements outlined in the

isFocusableWindow()

method.

The

Window

's

autoRequestFocus

property is of the

true

value.

Native windowing system allows the

Window

to get focused.

There is an exception for the second condition (the value of the

autoRequestFocus

property). The property is not taken into account if the
window is a modal dialog, which blocks the currently focused window.

Developers must never assume that the window is the focused or active window
until it receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED event.

**Overrides:**
- setVisible

in class

Component

**Parameters:**
- b

- if

true

, makes the

Window

visible,
otherwise hides the

Window

.
If the

Window

and/or its owner
are not yet displayable, both are made displayable. The

Window

will be validated prior to being made visible.
If the

Window

is already visible, this will bring the

Window

to the front.

If

false

, hides this

Window

, its subcomponents, and all
of its owned children.
The

Window

and its subcomponents can be made visible again
with a call to

#setVisible(true)

.

**See Also:**
- Component.isDisplayable()

,

Component.setVisible(boolean)

,

toFront()

,

dispose()

,

setAutoRequestFocus(boolean)

,

isFocusableWindow()

---

#### @Deprecated

public void show()

Makes the Window visible. If the Window and/or its owner
are not yet displayable, both are made displayable. The
Window will be validated prior to being made visible.
If the Window is already visible, this will bring the Window
to the front.

**Overrides:**
- show

in class

Component

**See Also:**
- Component.isDisplayable()

,

toFront()

---

#### @Deprecated

public void hide()

Hide this Window, its subcomponents, and all of its owned children.
The Window and its subcomponents can be made visible again
with a call to

show

.

**Overrides:**
- hide

in class

Component

**See Also:**
- show()

,

dispose()

---

#### public void dispose()

Releases all of the native screen resources used by this

Window

, its subcomponents, and all of its owned
children. That is, the resources for these

Component

s
will be destroyed, any memory they consume will be returned to the
OS, and they will be marked as undisplayable.

The

Window

and its subcomponents can be made displayable
again by rebuilding the native resources with a subsequent call to

pack

or

show

. The states of the recreated

Window

and its subcomponents will be identical to the
states of these objects at the point where the

Window

was disposed (not accounting for additional modifications between
those actions).

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**See Also:**
- Component.isDisplayable()

,

pack()

,

show()

---

#### public void toFront()

If this Window is visible, brings this Window to the front and may make
it the focused Window.

Places this Window at the top of the stacking order and shows it in
front of any other Windows in this VM. No action will take place if this
Window is not visible. Some platforms do not allow Windows which own
other Windows to appear on top of those owned Windows. Some platforms
may not permit this VM to place its Windows above windows of native
applications, or Windows of other VMs. This permission may depend on
whether a Window in this VM is already focused. Every attempt will be
made to move this Window as high as possible in the stacking order;
however, developers should not assume that this method will move this
Window above all other windows in every situation.

Developers must never assume that this Window is the focused or active
Window until this Window receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED
event. On platforms where the top-most window is the focused window, this
method will

probably

focus this Window (if it is not already focused)
under the following conditions:

- The window meets the requirements outlined in the

isFocusableWindow()

method.

The window's property

autoRequestFocus

is of the

true

value.

Native windowing system allows the window to get focused.

On platforms where the stacking order does not typically affect the focused
window, this method will

probably

leave the focused and active
Windows unchanged.

If this method causes this Window to be focused, and this Window is a
Frame or a Dialog, it will also become activated. If this Window is
focused, but it is not a Frame or a Dialog, then the first Frame or
Dialog that is an owner of this Window will be activated.

If this window is blocked by modal dialog, then the blocking dialog
is brought to the front and remains above the blocked window.

**See Also:**
- toBack()

,

setAutoRequestFocus(boolean)

,

isFocusableWindow()

---

#### public void toBack()

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

**See Also:**
- toFront()

---

#### public
Toolkit
getToolkit()

Returns the toolkit of this frame.

**Overrides:**
- getToolkit

in class

Component

**Returns:**
- the toolkit of this window.

**See Also:**
- Toolkit

,

Toolkit.getDefaultToolkit()

,

Component.getToolkit()

---

#### public final
String
getWarningString()

Gets the warning string that is displayed with this window.
If this window is insecure, the warning string is displayed
somewhere in the visible area of the window. A window is
insecure if there is a security manager and the security
manager denies

AWTPermission("showWindowWithoutWarningBanner")

.

If the window is secure, then

getWarningString

returns

null

. If the window is insecure, this
method checks for the system property

awt.appletWarning

and returns the string value of that property.

**Returns:**
- the warning string for this window.

---

#### public
Locale
getLocale()

Gets the

Locale

object that is associated
with this window, if the locale has been set.
If no locale has been set, then the default locale
is returned.

**Overrides:**
- getLocale

in class

Component

**Returns:**
- the locale that is set for this window.

**See Also:**
- Locale

**Since:**
- 1.1

---

#### public
InputContext
getInputContext()

Gets the input context for this window. A window always has an input context,
which is shared by subcomponents unless they create and set their own.

**Overrides:**
- getInputContext

in class

Component

**Returns:**
- the input context used by this component;

null

if no context can be determined

**See Also:**
- Component.getInputContext()

**Since:**
- 1.2

---

#### public void setCursor​(
Cursor
cursor)

Set the cursor image to a specified cursor.

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

class. If this parameter is null
then the cursor for this window will be set to the type
Cursor.DEFAULT_CURSOR.

**See Also:**
- Component.getCursor()

,

Cursor

**Since:**
- 1.1

---

#### public
Window
getOwner()

Returns the owner of this window.

**Returns:**
- the owner of this window

**Since:**
- 1.2

---

#### public
Window
[] getOwnedWindows()

Return an array containing all the windows this
window currently owns.

**Returns:**
- the array of all the owned windows

**Since:**
- 1.2

---

#### public static
Window
[] getWindows()

Returns an array of all

Window

s, both owned and ownerless,
created by this application.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

**Returns:**
- the array of all the

Window

s created by the application

**See Also:**
- Frame.getFrames()

,

getOwnerlessWindows()

**Since:**
- 1.6

---

#### public static
Window
[] getOwnerlessWindows()

Returns an array of all

Window

s created by this application
that have no owner. They include

Frame

s and ownerless

Dialog

s and

Window

s.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

**Returns:**
- the array of all the ownerless

Window

s
created by this application

**See Also:**
- Frame.getFrames()

,

getWindows()

**Since:**
- 1.6

---

#### public void setModalExclusionType​(
Dialog.ModalExclusionType
exclusionType)

Specifies the modal exclusion type for this window. If a window is modal
excluded, it is not blocked by some modal dialogs. See

Dialog.ModalExclusionType

for
possible modal exclusion types.

If the given type is not supported,

NO_EXCLUDE

is used.

Note: changing the modal exclusion type for a visible window may have no
effect until it is hidden and then shown again.

**Parameters:**
- exclusionType

- the modal exclusion type for this window; a

null

value is equivalent to

NO_EXCLUDE

**Throws:**
- SecurityException

- if the calling thread does not have permission
to set the modal exclusion property to the window with the given

exclusionType

**See Also:**
- Dialog.ModalExclusionType

,

getModalExclusionType()

,

Toolkit.isModalExclusionTypeSupported(java.awt.Dialog.ModalExclusionType)

**Since:**
- 1.6

---

#### public
Dialog.ModalExclusionType
getModalExclusionType()

Returns the modal exclusion type of this window.

**Returns:**
- the modal exclusion type of this window

**See Also:**
- Dialog.ModalExclusionType

,

setModalExclusionType(java.awt.Dialog.ModalExclusionType)

**Since:**
- 1.6

---

#### public void addWindowListener​(
WindowListener
l)

Adds the specified window listener to receive window events from
this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the window listener

**See Also:**
- removeWindowListener(java.awt.event.WindowListener)

,

getWindowListeners()

---

#### public void addWindowStateListener​(
WindowStateListener
l)

Adds the specified window state listener to receive window
events from this window. If

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the window state listener

**See Also:**
- removeWindowStateListener(java.awt.event.WindowStateListener)

,

getWindowStateListeners()

**Since:**
- 1.4

---

#### public void addWindowFocusListener​(
WindowFocusListener
l)

Adds the specified window focus listener to receive window events
from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the window focus listener

**See Also:**
- removeWindowFocusListener(java.awt.event.WindowFocusListener)

,

getWindowFocusListeners()

**Since:**
- 1.4

---

#### public void removeWindowListener​(
WindowListener
l)

Removes the specified window listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the window listener

**See Also:**
- addWindowListener(java.awt.event.WindowListener)

,

getWindowListeners()

---

#### public void removeWindowStateListener​(
WindowStateListener
l)

Removes the specified window state listener so that it no
longer receives window events from this window. If

l

is

null

, no exception is thrown and
no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the window state listener

**See Also:**
- addWindowStateListener(java.awt.event.WindowStateListener)

,

getWindowStateListeners()

**Since:**
- 1.4

---

#### public void removeWindowFocusListener​(
WindowFocusListener
l)

Removes the specified window focus listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the window focus listener

**See Also:**
- addWindowFocusListener(java.awt.event.WindowFocusListener)

,

getWindowFocusListeners()

**Since:**
- 1.4

---

#### public
WindowListener
[] getWindowListeners()

Returns an array of all the window listeners
registered on this window.

**Returns:**
- all of this window's

WindowListener

s
or an empty array if no window
listeners are currently registered

**See Also:**
- addWindowListener(java.awt.event.WindowListener)

,

removeWindowListener(java.awt.event.WindowListener)

**Since:**
- 1.4

---

#### public
WindowFocusListener
[] getWindowFocusListeners()

Returns an array of all the window focus listeners
registered on this window.

**Returns:**
- all of this window's

WindowFocusListener

s
or an empty array if no window focus
listeners are currently registered

**See Also:**
- addWindowFocusListener(java.awt.event.WindowFocusListener)

,

removeWindowFocusListener(java.awt.event.WindowFocusListener)

**Since:**
- 1.4

---

#### public
WindowStateListener
[] getWindowStateListeners()

Returns an array of all the window state listeners
registered on this window.

**Returns:**
- all of this window's

WindowStateListener

s
or an empty array if no window state
listeners are currently registered

**See Also:**
- addWindowStateListener(java.awt.event.WindowStateListener)

,

removeWindowStateListener(java.awt.event.WindowStateListener)

**Since:**
- 1.4

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Window

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Window w

for its window listeners with the following code:

```java
WindowListener[] wls = (WindowListener[])(w.getListeners(WindowListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:**
- getListeners

in class

Container

**Parameters:**
- listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this window,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
- NullPointerException

- if

listenerType

is

null

**See Also:**
- getWindowListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of the listeners

---

#### protected void processEvent​(
AWTEvent
e)

Processes events on this window. If the event is an

WindowEvent

, it invokes the

processWindowEvent

method, else it invokes its
superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:**
- processEvent

in class

Container

**Parameters:**
- e

- the event

**See Also:**
- Component.processComponentEvent(java.awt.event.ComponentEvent)

,

Component.processFocusEvent(java.awt.event.FocusEvent)

,

Component.processKeyEvent(java.awt.event.KeyEvent)

,

Component.processMouseEvent(java.awt.event.MouseEvent)

,

Component.processMouseMotionEvent(java.awt.event.MouseEvent)

,

Component.processInputMethodEvent(java.awt.event.InputMethodEvent)

,

Component.processHierarchyEvent(java.awt.event.HierarchyEvent)

,

Component.processMouseWheelEvent(java.awt.event.MouseWheelEvent)

---

#### protected void processWindowEvent​(
WindowEvent
e)

Processes window events occurring on this window by
dispatching them to any registered WindowListener objects.
NOTE: This method will not be called unless window events
are enabled for this component; this happens when one of the
following occurs:

- A WindowListener object is registered via

addWindowListener

Window events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the window event

**See Also:**
- Component.enableEvents(long)

---

#### protected void processWindowFocusEvent​(
WindowEvent
e)

Processes window focus event occurring on this window by
dispatching them to any registered WindowFocusListener objects.
NOTE: this method will not be called unless window focus events
are enabled for this window. This happens when one of the
following occurs:

- a WindowFocusListener is registered via

addWindowFocusListener

Window focus events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the window focus event

**See Also:**
- Component.enableEvents(long)

**Since:**
- 1.4

---

#### protected void processWindowStateEvent​(
WindowEvent
e)

Processes window state event occurring on this window by
dispatching them to any registered

WindowStateListener

objects.
NOTE: this method will not be called unless window state events
are enabled for this window. This happens when one of the
following occurs:

- a

WindowStateListener

is registered via

addWindowStateListener

window state events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the window state event

**See Also:**
- Component.enableEvents(long)

**Since:**
- 1.4

---

#### public final void setAlwaysOnTop​(boolean alwaysOnTop)
throws
SecurityException

Sets whether this window should always be above other windows. If
there are multiple always-on-top windows, their relative order is
unspecified and platform dependent.

If some other window is already always-on-top then the
relative order between these windows is unspecified (depends on
platform). No window can be brought to be over the always-on-top
window except maybe another always-on-top window.

All windows owned by an always-on-top window inherit this state and
automatically become always-on-top. If a window ceases to be
always-on-top, the windows that it owns will no longer be
always-on-top. When an always-on-top window is sent

toBack

, its always-on-top state is set to

false

.

When this method is called on a window with a value of

true

, and the window is visible and the platform
supports always-on-top for this window, the window is immediately
brought forward, "sticking" it in the top-most position. If the
window isn`t currently visible, this method sets the always-on-top
state to

true

but does not bring the window forward.
When the window is later shown, it will be always-on-top.

When this method is called on a window with a value of

false

the always-on-top state is set to normal. It may also
cause an unspecified, platform-dependent change in the z-order of
top-level windows, but other always-on-top windows will remain in
top-most position. Calling this method with a value of

false

on a window that has a normal state has no effect.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

**Parameters:**
- alwaysOnTop

- true if the window should always be above other
windows

**Throws:**
- SecurityException

- if the calling thread does not have
permission to set the value of always-on-top property

**See Also:**
- isAlwaysOnTop()

,

toFront()

,

toBack()

,

AWTPermission

,

isAlwaysOnTopSupported()

,

getToolkit()

,

Toolkit.isAlwaysOnTopSupported()

**Since:**
- 1.5

---

#### public boolean isAlwaysOnTopSupported()

Returns whether the always-on-top mode is supported for this
window. Some platforms may not support always-on-top windows, some
may support only some kinds of top-level windows; for example,
a platform may not support always-on-top modal dialogs.

**Returns:**
- true

, if the always-on-top mode is supported for
this window and this window's toolkit supports always-on-top windows,

false

otherwise

**See Also:**
- setAlwaysOnTop(boolean)

,

getToolkit()

,

Toolkit.isAlwaysOnTopSupported()

**Since:**
- 1.6

---

#### public final boolean isAlwaysOnTop()

Returns whether this window is an always-on-top window.

**Returns:**
- true

, if the window is in always-on-top state,

false

otherwise

**See Also:**
- setAlwaysOnTop(boolean)

**Since:**
- 1.5

---

#### public
Component
getFocusOwner()

Returns the child Component of this Window that has focus if this Window
is focused; returns null otherwise.

**Returns:**
- the child Component with focus, or null if this Window is not
focused

**See Also:**
- getMostRecentFocusOwner()

,

isFocused()

---

#### public
Component
getMostRecentFocusOwner()

Returns the child Component of this Window that will receive the focus
when this Window is focused. If this Window is currently focused, this
method returns the same Component as

getFocusOwner()

. If
this Window is not focused, then the child Component that most recently
requested focus will be returned. If no child Component has ever
requested focus, and this is a focusable Window, then this Window's
initial focusable Component is returned. If no child Component has ever
requested focus, and this is a non-focusable Window, null is returned.

**Returns:**
- the child Component that will receive focus when this Window is
focused

**See Also:**
- getFocusOwner()

,

isFocused()

,

isFocusableWindow()

**Since:**
- 1.4

---

#### public boolean isActive()

Returns whether this Window is active. Only a Frame or a Dialog may be
active. The native windowing system may denote the active Window or its
children with special decorations, such as a highlighted title bar. The
active Window is always either the focused Window, or the first Frame or
Dialog that is an owner of the focused Window.

**Returns:**
- whether this is the active Window.

**See Also:**
- isFocused()

**Since:**
- 1.4

---

#### public boolean isFocused()

Returns whether this Window is focused. If there exists a focus owner,
the focused Window is the Window that is, or contains, that focus owner.
If there is no focus owner, then no Window is focused.

If the focused Window is a Frame or a Dialog it is also the active
Window. Otherwise, the active Window is the first Frame or Dialog that
is an owner of the focused Window.

**Returns:**
- whether this is the focused Window.

**See Also:**
- isActive()

**Since:**
- 1.4

---

#### public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)

Gets a focus traversal key for this Window. (See

setFocusTraversalKeys

for a full description of each key.)

If the traversal key has not been explicitly set for this Window,
then this Window's parent's traversal key is returned. If the
traversal key has not been explicitly set for any of this Window's
ancestors, then the current KeyboardFocusManager's default traversal key
is returned.

**Overrides:**
- getFocusTraversalKeys

in class

Container

**Parameters:**
- id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

**Returns:**
- the AWTKeyStroke for the specified key

**Throws:**
- IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

**See Also:**
- Container.setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

**Since:**
- 1.4

---

#### public final void setFocusCycleRoot​(boolean focusCycleRoot)

Does nothing because Windows must always be roots of a focus traversal
cycle. The passed-in value is ignored.

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

because all Windows must be roots of a
focus traversal cycle.

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

#### public final
Container
getFocusCycleRootAncestor()

Always returns

null

because Windows have no ancestors; they
represent the top of the Component hierarchy.

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

#### public final boolean isFocusableWindow()

Returns whether this Window can become the focused Window, that is,
whether this Window or any of its subcomponents can become the focus
owner. For a Frame or Dialog to be focusable, its focusable Window state
must be set to

true

. For a Window which is not a Frame or
Dialog to be focusable, its focusable Window state must be set to

true

, its nearest owning Frame or Dialog must be
showing on the screen, and it must contain at least one Component in
its focus traversal cycle. If any of these conditions is not met, then
neither this Window nor any of its subcomponents can become the focus
owner.

**Returns:**
- true

if this Window can be the focused Window;

false

otherwise

**See Also:**
- getFocusableWindowState()

,

setFocusableWindowState(boolean)

,

isShowing()

,

Component.isFocusable()

**Since:**
- 1.4

---

#### public boolean getFocusableWindowState()

Returns whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this method returns

false

, then

isFocusableWindow

will return

false

as well.
If this method returns

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

By default, all Windows have a focusable Window state of

true

.

**Returns:**
- whether this Window can be the focused Window

**See Also:**
- isFocusableWindow()

,

setFocusableWindowState(boolean)

,

isShowing()

,

Component.setFocusable(boolean)

**Since:**
- 1.4

---

#### public void setFocusableWindowState​(boolean focusableWindowState)

Sets whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this Window's focusable Window state is set to

false

, then

isFocusableWindow

will return

false

. If this
Window's focusable Window state is set to

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

Setting a Window's focusability state to

false

is the
standard mechanism for an application to identify to the AWT a Window
which will be used as a floating palette or toolbar, and thus should be
a non-focusable Window.

Setting the focusability state on a visible

Window

can have a delayed effect on some platforms — the actual
change may happen only when the

Window

becomes
hidden and then visible again. To ensure consistent behavior
across platforms, set the

Window

's focusable state
when the

Window

is invisible and then show it.

**Parameters:**
- focusableWindowState

- whether this Window can be the focused
Window

**See Also:**
- isFocusableWindow()

,

getFocusableWindowState()

,

isShowing()

,

Component.setFocusable(boolean)

**Since:**
- 1.4

---

#### public void setAutoRequestFocus​(boolean autoRequestFocus)

Sets whether this window should receive focus on
subsequently being shown (with a call to

setVisible(true)

),
or being moved to the front (with a call to

toFront()

).

Note that

setVisible(true)

may be called indirectly
(e.g. when showing an owner of the window makes the window to be shown).

toFront()

may also be called indirectly (e.g. when

setVisible(true)

is called on already visible window).
In all such cases this property takes effect as well.

The value of the property is not inherited by owned windows.

**Parameters:**
- autoRequestFocus

- whether this window should be focused on
subsequently being shown or being moved to the front

**See Also:**
- isAutoRequestFocus()

,

isFocusableWindow()

,

setVisible(boolean)

,

toFront()

**Since:**
- 1.7

---

#### public boolean isAutoRequestFocus()

Returns whether this window should receive focus on subsequently being shown
(with a call to

setVisible(true)

), or being moved to the front
(with a call to

toFront()

).

By default, the window has

autoRequestFocus

value of

true

.

**Returns:**
- autoRequestFocus

value

**See Also:**
- setAutoRequestFocus(boolean)

**Since:**
- 1.7

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:**
- addPropertyChangeListener

in class

Container

**Parameters:**
- listener

- the PropertyChangeListener to be added

**See Also:**
- Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

,

addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

---

#### public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:**
- addPropertyChangeListener

in class

Container

**Parameters:**
- propertyName

- one of the property names listed above
- listener

- the PropertyChangeListener to be added

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public boolean isValidateRoot()

Indicates if this container is a validate root.

Window

objects are the validate roots, and, therefore, they
override this method to return

true

.

**Overrides:**
- isValidateRoot

in class

Container

**Returns:**
- true

**See Also:**
- Container.isValidateRoot()

**Since:**
- 1.7

---

#### @Deprecated

public boolean postEvent​(
Event
e)

Description copied from interface:

MenuContainer

**Specified by:**
- postEvent

in interface

MenuContainer

**Overrides:**
- postEvent

in class

Component

**Parameters:**
- e

- the event to dispatch

**Returns:**
- the results of posting the event

---

#### public boolean isShowing()

Checks if this Window is showing on screen.

**Overrides:**
- isShowing

in class

Component

**Returns:**
- true

if the component is showing,

false

otherwise

**See Also:**
- Component.setVisible(boolean)

---

#### @Deprecated

public void applyResourceBundle​(
ResourceBundle
rb)

**Parameters:**
- rb

- the resource bundle

---

#### @Deprecated

public void applyResourceBundle​(
String
rbName)

**Parameters:**
- rbName

- the resource name

---

#### public void setType​(
Window.Type
type)

Sets the type of the window.

This method can only be called while the window is not displayable.

**Parameters:**
- type

- the window type

**Throws:**
- IllegalComponentStateException

- if the window
is displayable.
- IllegalArgumentException

- if the type is

null

**See Also:**
- Component.isDisplayable()

,

getType()

**Since:**
- 1.7

---

#### public
Window.Type
getType()

Returns the type of the window.

**Returns:**
- the type of the window

**See Also:**
- setType(java.awt.Window.Type)

**Since:**
- 1.7

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this Window.
For windows, the AccessibleContext takes the form of an
AccessibleAWTWindow.
A new AccessibleAWTWindow instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleAWTWindow that serves as the
AccessibleContext of this Window

**Since:**
- 1.3

---

#### public void setLocationRelativeTo​(
Component
c)

Sets the location of the window relative to the specified
component according to the following scenarios.

The target screen mentioned below is a screen to which
the window should be placed after the setLocationRelativeTo
method is called.

- If the component is

null

, or the

GraphicsConfiguration

associated with this component is

null

, the window is placed in the center of the
screen. The center point can be obtained with the

GraphicsEnvironment.getCenterPoint

method.

If the component is not

null

, but it is not
currently showing, the window is placed in the center of
the target screen defined by the

GraphicsConfiguration

associated with this component.

If the component is not

null

and is shown on
the screen, then the window is located in such a way that
the center of the window coincides with the center of the
component.

If the screens configuration does not allow the window to
be moved from one screen to another, then the window is
only placed at the location determined according to the
above conditions and its

GraphicsConfiguration

is
not changed.

Note

: If the lower edge of the window is out of the screen,
then the window is placed to the side of the

Component

that is closest to the center of the screen. So if the
component is on the right part of the screen, the window
is placed to its left, and vice versa.

If after the window location has been calculated, the upper,
left, or right edge of the window is out of the screen,
then the window is located in such a way that the upper,
left, or right edge of the window coincides with the
corresponding edge of the screen. If both left and right
edges of the window are out of the screen, the window is
placed at the left side of the screen. The similar placement
will occur if both top and bottom edges are out of the screen.
In that case, the window is placed at the top side of the screen.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Parameters:**
- c

- the component in relation to which the window's location
is determined

**See Also:**
- GraphicsEnvironment.getCenterPoint()

**Since:**
- 1.4

---

#### public void createBufferStrategy​(int numBuffers)

Creates a new strategy for multi-buffering on this component.
Multi-buffering is useful for rendering performance. This method
attempts to create the best strategy available with the number of
buffers supplied. It will always create a

BufferStrategy

with that number of buffers.
A page-flipping strategy is attempted first, then a blitting strategy
using accelerated buffers. Finally, an unaccelerated blitting
strategy is used.

Each time this method is called,
the existing buffer strategy for this component is discarded.

**Parameters:**
- numBuffers

- number of buffers to create

**Throws:**
- IllegalArgumentException

- if numBuffers is less than 1.
- IllegalStateException

- if the component is not displayable

**See Also:**
- Component.isDisplayable()

,

getBufferStrategy()

**Since:**
- 1.4

---

#### public void createBufferStrategy​(int numBuffers,

BufferCapabilities
caps)
throws
AWTException

Creates a new strategy for multi-buffering on this component with the
required buffer capabilities. This is useful, for example, if only
accelerated memory or page flipping is desired (as specified by the
buffer capabilities).

Each time this method
is called, the existing buffer strategy for this component is discarded.

**Parameters:**
- numBuffers

- number of buffers to create, including the front buffer
- caps

- the required capabilities for creating the buffer strategy;
cannot be

null

**Throws:**
- AWTException

- if the capabilities supplied could not be
supported or met; this may happen, for example, if there is not enough
accelerated memory currently available, or if page flipping is specified
but not possible.
- IllegalArgumentException

- if numBuffers is less than 1, or if
caps is

null

**See Also:**
- getBufferStrategy()

**Since:**
- 1.4

---

#### public
BufferStrategy
getBufferStrategy()

Returns the

BufferStrategy

used by this component. This
method will return null if a

BufferStrategy

has not yet
been created or has been disposed.

**Returns:**
- the buffer strategy used by this component

**See Also:**
- createBufferStrategy(int)

**Since:**
- 1.4

---

#### public void setLocationByPlatform​(boolean locationByPlatform)

Sets whether this Window should appear at the default location for the
native windowing system or at the current location (returned by

getLocation

) the next time the Window is made visible.
This behavior resembles a native window shown without programmatically
setting its location. Most windowing systems cascade windows if their
locations are not explicitly set. The actual location is determined once the
window is shown on the screen.

This behavior can also be enabled by setting the System Property
"java.awt.Window.locationByPlatform" to "true", though calls to this method
take precedence.

Calls to

setVisible

,

setLocation

and

setBounds

after calling

setLocationByPlatform

clear
this property of the Window.

For example, after the following code is executed:

```java
setLocationByPlatform(true);
setVisible(true);
boolean flag = isLocationByPlatform();
```

The window will be shown at platform's default location and

flag

will be

false

.

In the following sample:

```java
setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);
```

The window will be shown at (10, 10) and

flag

will be

false

.

**Parameters:**
- locationByPlatform

-

true

if this Window should appear
at the default location,

false

if at the current location

**Throws:**
- IllegalComponentStateException

- if the window
is showing on screen and locationByPlatform is

true

.

**See Also:**
- setLocation(int, int)

,

isShowing()

,

setVisible(boolean)

,

isLocationByPlatform()

,

System.getProperty(String)

**Since:**
- 1.5

---

#### public boolean isLocationByPlatform()

Returns

true

if this Window will appear at the default location
for the native windowing system the next time this Window is made visible.
This method always returns

false

if the Window is showing on the
screen.

**Returns:**
- whether this Window will appear at the default location

**See Also:**
- setLocationByPlatform(boolean)

,

isShowing()

**Since:**
- 1.5

---

#### public void setBounds​(int x,
int y,
int width,
int height)

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

or

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:**
- setBounds

in class

Component

**Parameters:**
- x

- the new

x

-coordinate of this component
- y

- the new

y

-coordinate of this component
- width

- the new

width

of this component
- height

- the new

height

of this
component

**See Also:**
- Component.getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

setMinimumSize(java.awt.Dimension)

,

setLocationByPlatform(boolean)

,

isLocationByPlatform()

**Since:**
- 1.6

---

#### public void setBounds​(
Rectangle
r)

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

r.width

or

r.height

values
will be automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:**
- setBounds

in class

Component

**Parameters:**
- r

- the new bounding rectangle for this component

**See Also:**
- Component.getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

setMinimumSize(java.awt.Dimension)

,

setLocationByPlatform(boolean)

,

isLocationByPlatform()

**Since:**
- 1.6

---

#### public float getOpacity()

Returns the opacity of the window.

**Returns:**
- the opacity of the window

**See Also:**
- setOpacity(float)

,

GraphicsDevice.WindowTranslucency

**Since:**
- 1.7

---

#### public void setOpacity​(float opacity)

Sets the opacity of the window.

The opacity value is in the range [0..1]. Note that setting the opacity
level of 0 may or may not disable the mouse event handling on this
window. This is a platform-dependent behavior.

The following conditions must be met in order to set the opacity value
less than

1.0f

:

- The

TRANSLUCENT

translucency must be supported by the underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested opacity value is less than

1.0f

, and any of the
above conditions are not met, the window opacity will not change,
and the

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
current shape of this window (see

setShape(Shape)

).

**Parameters:**
- opacity

- the opacity level to set to the window

**Throws:**
- IllegalArgumentException

- if the opacity is out of the range
[0..1]
- IllegalComponentStateException

- if the window is decorated and
the opacity is less than

1.0f
- IllegalComponentStateException

- if the window is in full screen
mode, and the opacity is less than

1.0f
- UnsupportedOperationException

- if the

GraphicsDevice.WindowTranslucency#TRANSLUCENT TRANSLUCENT

translucency is not supported and the opacity is less than

1.0f

**See Also:**
- getOpacity()

,

setBackground(Color)

,

setShape(Shape)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

**Since:**
- 1.7

---

#### public
Shape
getShape()

Returns the shape of the window.

The value returned by this method may not be the same as
previously set with

setShape(shape)

, but it is guaranteed
to represent the same shape.

**Returns:**
- the shape of the window or

null

if no
shape is specified for the window

**See Also:**
- setShape(Shape)

,

GraphicsDevice.WindowTranslucency

**Since:**
- 1.7

---

#### public void setShape​(
Shape
shape)

Sets the shape of the window.

Setting a shape cuts off some parts of the window. Only the parts that
belong to the given

Shape

remain visible and clickable. If
the shape argument is

null

, this method restores the default
shape, making the window rectangular on most platforms.

The following conditions must be met to set a non-null shape:

- The

PERPIXEL_TRANSPARENT

translucency must be supported by the
underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested shape is not

null

, and any of the above
conditions are not met, the shape of this window will not change,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
opacity value (see

setOpacity(float)

). See

GraphicsDevice.WindowTranslucency

for more details.

**Parameters:**
- shape

- the shape to set to the window

**Throws:**
- IllegalComponentStateException

- if the shape is not

null

and the window is decorated
- IllegalComponentStateException

- if the shape is not

null

and the window is in full-screen mode
- UnsupportedOperationException

- if the shape is not

null

and

PERPIXEL_TRANSPARENT

translucency is not supported

**See Also:**
- getShape()

,

setBackground(Color)

,

setOpacity(float)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

**Since:**
- 1.7

---

#### public
Color
getBackground()

Gets the background color of this window.

Note that the alpha component of the returned color indicates whether
the window is in the non-opaque (per-pixel translucent) mode.

**Overrides:**
- getBackground

in class

Component

**Returns:**
- this component's background color

**See Also:**
- setBackground(Color)

,

isOpaque()

,

GraphicsDevice.WindowTranslucency

---

#### public void setBackground​(
Color
bgColor)

Sets the background color of this window.

If the windowing system supports the

PERPIXEL_TRANSLUCENT

translucency, the alpha component of the given background color
may effect the mode of operation for this window: it indicates whether
this window must be opaque (alpha equals

1.0f

) or per-pixel translucent
(alpha is less than

1.0f

). If the given background color is

null

, the window is considered completely opaque.

All the following conditions must be met to enable the per-pixel
transparency mode for this window:

- The

PERPIXEL_TRANSLUCENT

translucency must be supported by the graphics
device where this window is located

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the alpha component of the requested background color is less than

1.0f

, and any of the above conditions are not met, the background
color of this window will not change, the alpha component of the given
background color will not affect the mode of operation for this window,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

When the window is per-pixel translucent, the drawing sub-system
respects the alpha value of each individual pixel. If a pixel gets
painted with the alpha color component equal to zero, it becomes
visually transparent. If the alpha of the pixel is equal to 1.0f, the
pixel is fully opaque. Interim values of the alpha color component make
the pixel semi-transparent. In this mode, the background of the window
gets painted with the alpha value of the given background color. If the
alpha value of the argument of this method is equal to

0

, the
background is not painted at all.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

**Overrides:**
- setBackground

in class

Component

**Parameters:**
- bgColor

- the color to become this window's background color.

**Throws:**
- IllegalComponentStateException

- if the alpha value of the given
background color is less than

1.0f

and the window is decorated
- IllegalComponentStateException

- if the alpha value of the given
background color is less than

1.0f

and the window is in
full-screen mode
- UnsupportedOperationException

- if the alpha value of the given
background color is less than

1.0f

and

PERPIXEL_TRANSLUCENT

translucency is not supported

**See Also:**
- getBackground()

,

isOpaque()

,

setOpacity(float)

,

setShape(Shape)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

,

GraphicsConfiguration.isTranslucencyCapable()

---

#### public boolean isOpaque()

Indicates if the window is currently opaque.

The method returns

false

if the background color of the window
is not

null

and the alpha component of the color is less than

1.0f

. The method returns

true

otherwise.

**Overrides:**
- isOpaque

in class

Component

**Returns:**
- true

if the window is opaque,

false

otherwise

**See Also:**
- getBackground()

,

setBackground(Color)

**Since:**
- 1.7

---

#### public void paint​(
Graphics
g)

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

**Overrides:**
- paint

in class

Container

**Parameters:**
- g

- the specified Graphics window

**See Also:**
- Component.update(Graphics)

**Since:**
- 1.7

---

### Additional Sections

#### Class Window

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - java.awt.Window

java.awt.Component

- java.awt.Container
- - java.awt.Window

java.awt.Container

- java.awt.Window

java.awt.Window

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

**Direct Known Subclasses:** BasicToolBarUI.DragWindow

,

Dialog

,

Frame

,

JWindow

```java
public class
Window

extends
Container

implements
Accessible
```

A

Window

object is a top-level window with no borders and no
menubar.
The default layout for a window is

BorderLayout

.

A window must have either a frame, dialog, or another window defined as its
owner when it's constructed.

In a multi-screen environment, you can create a

Window

on a different screen device by constructing the

Window

with

Window(Window, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual device coordinate system.
The origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location of
the primary screen in the virtual device, negative coordinates are
possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Window

returns
virtual device coordinates. Call the

getBounds

method
of a

GraphicsConfiguration

to find its origin in the virtual
coordinate system.

The following code sets the location of a

Window

at (10, 10) relative to the origin of the physical screen
of the corresponding

GraphicsConfiguration

. If the
bounds of the

GraphicsConfiguration

is not taken
into account, the

Window

location would be set
at (10, 10) relative to the virtual-coordinate system and would appear
on the primary physical screen, which might be different from the
physical screen of the specified

GraphicsConfiguration

.

```java
Window w = new Window(Window owner, GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
w.setLocation(10 + bounds.x, 10 + bounds.y);
```

Note: the location and size of top-level windows (including

Window

s,

Frame

s, and

Dialog

s)
are under the control of the desktop's window management system.
Calls to

setLocation

,

setSize

, and

setBounds

are requests (not directives) which are
forwarded to the window management system. Every effort will be
made to honor such requests. However, in some cases the window
management system may ignore such requests, or modify the requested
geometry in order to place and size the

Window

in a way
that more closely matches the desktop settings.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

**Since:** 1.0
**See Also:** WindowEvent

,

addWindowListener(java.awt.event.WindowListener)

,

BorderLayout

,

Serialized Form

public class

Window

extends

Container

implements

Accessible

A

Window

object is a top-level window with no borders and no
menubar.
The default layout for a window is

BorderLayout

.

A window must have either a frame, dialog, or another window defined as its
owner when it's constructed.

In a multi-screen environment, you can create a

Window

on a different screen device by constructing the

Window

with

Window(Window, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual device coordinate system.
The origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location of
the primary screen in the virtual device, negative coordinates are
possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Window

returns
virtual device coordinates. Call the

getBounds

method
of a

GraphicsConfiguration

to find its origin in the virtual
coordinate system.

The following code sets the location of a

Window

at (10, 10) relative to the origin of the physical screen
of the corresponding

GraphicsConfiguration

. If the
bounds of the

GraphicsConfiguration

is not taken
into account, the

Window

location would be set
at (10, 10) relative to the virtual-coordinate system and would appear
on the primary physical screen, which might be different from the
physical screen of the specified

GraphicsConfiguration

.

```java
Window w = new Window(Window owner, GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
w.setLocation(10 + bounds.x, 10 + bounds.y);
```

Note: the location and size of top-level windows (including

Window

s,

Frame

s, and

Dialog

s)
are under the control of the desktop's window management system.
Calls to

setLocation

,

setSize

, and

setBounds

are requests (not directives) which are
forwarded to the window management system. Every effort will be
made to honor such requests. However, in some cases the window
management system may ignore such requests, or modify the requested
geometry in order to place and size the

Window

in a way
that more closely matches the desktop settings.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

A window must have either a frame, dialog, or another window defined as its
owner when it's constructed.

In a multi-screen environment, you can create a

Window

on a different screen device by constructing the

Window

with

Window(Window, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual device coordinate system.
The origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location of
the primary screen in the virtual device, negative coordinates are
possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Window

returns
virtual device coordinates. Call the

getBounds

method
of a

GraphicsConfiguration

to find its origin in the virtual
coordinate system.

The following code sets the location of a

Window

at (10, 10) relative to the origin of the physical screen
of the corresponding

GraphicsConfiguration

. If the
bounds of the

GraphicsConfiguration

is not taken
into account, the

Window

location would be set
at (10, 10) relative to the virtual-coordinate system and would appear
on the primary physical screen, which might be different from the
physical screen of the specified

GraphicsConfiguration

.

```java
Window w = new Window(Window owner, GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
w.setLocation(10 + bounds.x, 10 + bounds.y);
```

Note: the location and size of top-level windows (including

Window

s,

Frame

s, and

Dialog

s)
are under the control of the desktop's window management system.
Calls to

setLocation

,

setSize

, and

setBounds

are requests (not directives) which are
forwarded to the window management system. Every effort will be
made to honor such requests. However, in some cases the window
management system may ignore such requests, or modify the requested
geometry in order to place and size the

Window

in a way
that more closely matches the desktop settings.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

In a multi-screen environment, you can create a

Window

on a different screen device by constructing the

Window

with

Window(Window, GraphicsConfiguration)

. The

GraphicsConfiguration

object is one of the

GraphicsConfiguration

objects of the target screen device.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual device coordinate system.
The origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location of
the primary screen in the virtual device, negative coordinates are
possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Window

returns
virtual device coordinates. Call the

getBounds

method
of a

GraphicsConfiguration

to find its origin in the virtual
coordinate system.

The following code sets the location of a

Window

at (10, 10) relative to the origin of the physical screen
of the corresponding

GraphicsConfiguration

. If the
bounds of the

GraphicsConfiguration

is not taken
into account, the

Window

location would be set
at (10, 10) relative to the virtual-coordinate system and would appear
on the primary physical screen, which might be different from the
physical screen of the specified

GraphicsConfiguration

.

```java
Window w = new Window(Window owner, GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
w.setLocation(10 + bounds.x, 10 + bounds.y);
```

Note: the location and size of top-level windows (including

Window

s,

Frame

s, and

Dialog

s)
are under the control of the desktop's window management system.
Calls to

setLocation

,

setSize

, and

setBounds

are requests (not directives) which are
forwarded to the window management system. Every effort will be
made to honor such requests. However, in some cases the window
management system may ignore such requests, or modify the requested
geometry in order to place and size the

Window

in a way
that more closely matches the desktop settings.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

In a virtual device multi-screen environment in which the desktop
area could span multiple physical screen devices, the bounds of all
configurations are relative to the virtual device coordinate system.
The origin of the virtual-coordinate system is at the upper left-hand
corner of the primary physical screen. Depending on the location of
the primary screen in the virtual device, negative coordinates are
possible, as shown in the following figure.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Window

returns
virtual device coordinates. Call the

getBounds

method
of a

GraphicsConfiguration

to find its origin in the virtual
coordinate system.

The following code sets the location of a

Window

at (10, 10) relative to the origin of the physical screen
of the corresponding

GraphicsConfiguration

. If the
bounds of the

GraphicsConfiguration

is not taken
into account, the

Window

location would be set
at (10, 10) relative to the virtual-coordinate system and would appear
on the primary physical screen, which might be different from the
physical screen of the specified

GraphicsConfiguration

.

```java
Window w = new Window(Window owner, GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
w.setLocation(10 + bounds.x, 10 + bounds.y);
```

Note: the location and size of top-level windows (including

Window

s,

Frame

s, and

Dialog

s)
are under the control of the desktop's window management system.
Calls to

setLocation

,

setSize

, and

setBounds

are requests (not directives) which are
forwarded to the window management system. Every effort will be
made to honor such requests. However, in some cases the window
management system may ignore such requests, or modify the requested
geometry in order to place and size the

Window

in a way
that more closely matches the desktop settings.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

In such an environment, when calling

setLocation

,
you must pass a virtual coordinate to this method. Similarly,
calling

getLocationOnScreen

on a

Window

returns
virtual device coordinates. Call the

getBounds

method
of a

GraphicsConfiguration

to find its origin in the virtual
coordinate system.

The following code sets the location of a

Window

at (10, 10) relative to the origin of the physical screen
of the corresponding

GraphicsConfiguration

. If the
bounds of the

GraphicsConfiguration

is not taken
into account, the

Window

location would be set
at (10, 10) relative to the virtual-coordinate system and would appear
on the primary physical screen, which might be different from the
physical screen of the specified

GraphicsConfiguration

.

```java
Window w = new Window(Window owner, GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
w.setLocation(10 + bounds.x, 10 + bounds.y);
```

Note: the location and size of top-level windows (including

Window

s,

Frame

s, and

Dialog

s)
are under the control of the desktop's window management system.
Calls to

setLocation

,

setSize

, and

setBounds

are requests (not directives) which are
forwarded to the window management system. Every effort will be
made to honor such requests. However, in some cases the window
management system may ignore such requests, or modify the requested
geometry in order to place and size the

Window

in a way
that more closely matches the desktop settings.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

The following code sets the location of a

Window

at (10, 10) relative to the origin of the physical screen
of the corresponding

GraphicsConfiguration

. If the
bounds of the

GraphicsConfiguration

is not taken
into account, the

Window

location would be set
at (10, 10) relative to the virtual-coordinate system and would appear
on the primary physical screen, which might be different from the
physical screen of the specified

GraphicsConfiguration

.

```java
Window w = new Window(Window owner, GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
w.setLocation(10 + bounds.x, 10 + bounds.y);
```

Note: the location and size of top-level windows (including

Window

s,

Frame

s, and

Dialog

s)
are under the control of the desktop's window management system.
Calls to

setLocation

,

setSize

, and

setBounds

are requests (not directives) which are
forwarded to the window management system. Every effort will be
made to honor such requests. However, in some cases the window
management system may ignore such requests, or modify the requested
geometry in order to place and size the

Window

in a way
that more closely matches the desktop settings.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

Window w = new Window(Window owner, GraphicsConfiguration gc);
Rectangle bounds = gc.getBounds();
w.setLocation(10 + bounds.x, 10 + bounds.y);

Note: the location and size of top-level windows (including

Window

s,

Frame

s, and

Dialog

s)
are under the control of the desktop's window management system.
Calls to

setLocation

,

setSize

, and

setBounds

are requests (not directives) which are
forwarded to the window management system. Every effort will be
made to honor such requests. However, in some cases the window
management system may ignore such requests, or modify the requested
geometry in order to place and size the

Window

in a way
that more closely matches the desktop settings.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

Due to the asynchronous nature of native event handling, the results
returned by

getBounds

,

getLocation

,

getLocationOnScreen

, and

getSize

might not
reflect the actual geometry of the Window on screen until the last
request has been processed. During the processing of subsequent
requests these values might change accordingly while the window
management system fulfills the requests.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

An application may set the size and location of an invisible

Window

arbitrarily, but the window management system may
subsequently change its size and/or location when the

Window

is made visible. One or more

ComponentEvent

s
will be generated to indicate the new geometry.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

Windows are capable of generating the following WindowEvents:
WindowOpened, WindowClosed, WindowGainedFocus, WindowLostFocus.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Window.AccessibleAWTWindow

This class implements accessibility support for the

Window

class.

static class

Window.Type

Enumeration of available

window types

.

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

Window

​(

Frame

owner)

Constructs a new, initially invisible window with the specified

Frame

as its owner.

Window

​(

Window

owner)

Constructs a new, initially invisible window with the specified

Window

as its owner.

Window

​(

Window

owner,

GraphicsConfiguration

gc)

Constructs a new, initially invisible window with the specified owner

Window

and a

GraphicsConfiguration

of a screen device.

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

Makes this Window displayable by creating the connection to its
native screen resource.

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list.

void

addPropertyChangeListener

​(

String

propertyName,

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list for a specific
property.

void

addWindowFocusListener

​(

WindowFocusListener

l)

Adds the specified window focus listener to receive window events
from this window.

void

addWindowListener

​(

WindowListener

l)

Adds the specified window listener to receive window events from
this window.

void

addWindowStateListener

​(

WindowStateListener

l)

Adds the specified window state listener to receive window
events from this window.

void

applyResourceBundle

​(

String

rbName)

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

void

applyResourceBundle

​(

ResourceBundle

rb)

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

void

createBufferStrategy

​(int numBuffers)

Creates a new strategy for multi-buffering on this component.

void

createBufferStrategy

​(int numBuffers,

BufferCapabilities

caps)

Creates a new strategy for multi-buffering on this component with the
required buffer capabilities.

void

dispose

()

Releases all of the native screen resources used by this

Window

, its subcomponents, and all of its owned
children.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Window.

Color

getBackground

()

Gets the background color of this window.

BufferStrategy

getBufferStrategy

()

Returns the

BufferStrategy

used by this component.

boolean

getFocusableWindowState

()

Returns whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

.

Container

getFocusCycleRootAncestor

()

Always returns

null

because Windows have no ancestors; they
represent the top of the Component hierarchy.

Component

getFocusOwner

()

Returns the child Component of this Window that has focus if this Window
is focused; returns null otherwise.

Set

<

AWTKeyStroke

>

getFocusTraversalKeys

​(int id)

Gets a focus traversal key for this Window.

List

<

Image

>

getIconImages

()

Returns the sequence of images to be displayed as the icon for this window.

InputContext

getInputContext

()

Gets the input context for this window.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Window

.

Locale

getLocale

()

Gets the

Locale

object that is associated
with this window, if the locale has been set.

Dialog.ModalExclusionType

getModalExclusionType

()

Returns the modal exclusion type of this window.

Component

getMostRecentFocusOwner

()

Returns the child Component of this Window that will receive the focus
when this Window is focused.

float

getOpacity

()

Returns the opacity of the window.

Window

[]

getOwnedWindows

()

Return an array containing all the windows this
window currently owns.

Window

getOwner

()

Returns the owner of this window.

static

Window

[]

getOwnerlessWindows

()

Returns an array of all

Window

s created by this application
that have no owner.

Shape

getShape

()

Returns the shape of the window.

Toolkit

getToolkit

()

Returns the toolkit of this frame.

Window.Type

getType

()

Returns the type of the window.

String

getWarningString

()

Gets the warning string that is displayed with this window.

WindowFocusListener

[]

getWindowFocusListeners

()

Returns an array of all the window focus listeners
registered on this window.

WindowListener

[]

getWindowListeners

()

Returns an array of all the window listeners
registered on this window.

static

Window

[]

getWindows

()

Returns an array of all

Window

s, both owned and ownerless,
created by this application.

WindowStateListener

[]

getWindowStateListeners

()

Returns an array of all the window state listeners
registered on this window.

void

hide

()

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

boolean

isActive

()

Returns whether this Window is active.

boolean

isAlwaysOnTop

()

Returns whether this window is an always-on-top window.

boolean

isAlwaysOnTopSupported

()

Returns whether the always-on-top mode is supported for this
window.

boolean

isAutoRequestFocus

()

Returns whether this window should receive focus on subsequently being shown
(with a call to

setVisible(true)

), or being moved to the front
(with a call to

toFront()

).

boolean

isFocusableWindow

()

Returns whether this Window can become the focused Window, that is,
whether this Window or any of its subcomponents can become the focus
owner.

boolean

isFocusCycleRoot

()

Always returns

true

because all Windows must be roots of a
focus traversal cycle.

boolean

isFocused

()

Returns whether this Window is focused.

boolean

isLocationByPlatform

()

Returns

true

if this Window will appear at the default location
for the native windowing system the next time this Window is made visible.

boolean

isOpaque

()

Indicates if the window is currently opaque.

boolean

isShowing

()

Checks if this Window is showing on screen.

boolean

isValidateRoot

()

Indicates if this container is a validate root.

void

pack

()

Causes this Window to be sized to fit the preferred size
and layouts of its subcomponents.

void

paint

​(

Graphics

g)

Paints the container.

boolean

postEvent

​(

Event

e)

Deprecated.

As of JDK version 1.1
replaced by

dispatchEvent(AWTEvent)

.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this window.

protected void

processWindowEvent

​(

WindowEvent

e)

Processes window events occurring on this window by
dispatching them to any registered WindowListener objects.

protected void

processWindowFocusEvent

​(

WindowEvent

e)

Processes window focus event occurring on this window by
dispatching them to any registered WindowFocusListener objects.

protected void

processWindowStateEvent

​(

WindowEvent

e)

Processes window state event occurring on this window by
dispatching them to any registered

WindowStateListener

objects.

void

removeWindowFocusListener

​(

WindowFocusListener

l)

Removes the specified window focus listener so that it no longer
receives window events from this window.

void

removeWindowListener

​(

WindowListener

l)

Removes the specified window listener so that it no longer
receives window events from this window.

void

removeWindowStateListener

​(

WindowStateListener

l)

Removes the specified window state listener so that it no
longer receives window events from this window.

void

reshape

​(int x,
int y,
int width,
int height)

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

void

setAlwaysOnTop

​(boolean alwaysOnTop)

Sets whether this window should always be above other windows.

void

setAutoRequestFocus

​(boolean autoRequestFocus)

Sets whether this window should receive focus on
subsequently being shown (with a call to

setVisible(true)

),
or being moved to the front (with a call to

toFront()

).

void

setBackground

​(

Color

bgColor)

Sets the background color of this window.

void

setBounds

​(int x,
int y,
int width,
int height)

Moves and resizes this component.

void

setBounds

​(

Rectangle

r)

Moves and resizes this component to conform to the new
bounding rectangle

r

.

void

setCursor

​(

Cursor

cursor)

Set the cursor image to a specified cursor.

void

setFocusableWindowState

​(boolean focusableWindowState)

Sets whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

.

void

setFocusCycleRoot

​(boolean focusCycleRoot)

Does nothing because Windows must always be roots of a focus traversal
cycle.

void

setIconImage

​(

Image

image)

Sets the image to be displayed as the icon for this window.

void

setIconImages

​(

List

<? extends

Image

> icons)

Sets the sequence of images to be displayed as the icon
for this window.

void

setLocation

​(int x,
int y)

Moves this component to a new location.

void

setLocation

​(

Point

p)

Moves this component to a new location.

void

setLocationByPlatform

​(boolean locationByPlatform)

Sets whether this Window should appear at the default location for the
native windowing system or at the current location (returned by

getLocation

) the next time the Window is made visible.

void

setLocationRelativeTo

​(

Component

c)

Sets the location of the window relative to the specified
component according to the following scenarios.

void

setMinimumSize

​(

Dimension

minimumSize)

Sets the minimum size of this window to a constant
value.

void

setModalExclusionType

​(

Dialog.ModalExclusionType

exclusionType)

Specifies the modal exclusion type for this window.

void

setOpacity

​(float opacity)

Sets the opacity of the window.

void

setShape

​(

Shape

shape)

Sets the shape of the window.

void

setSize

​(int width,
int height)

Resizes this component so that it has width

width

and height

height

.

void

setSize

​(

Dimension

d)

Resizes this component so that it has width

d.width

and height

d.height

.

void

setType

​(

Window.Type

type)

Sets the type of the window.

void

setVisible

​(boolean b)

Shows or hides this

Window

depending on the value of parameter

b

.

void

show

()

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

void

toBack

()

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

void

toFront

()

If this Window is visible, brings this Window to the front and may make
it the focused Window.

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

paramString

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

removeNotify

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Window.AccessibleAWTWindow

This class implements accessibility support for the

Window

class.

static class

Window.Type

Enumeration of available

window types

.

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

Window

class.

Enumeration of available

window types

.

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

Window

​(

Frame

owner)

Constructs a new, initially invisible window with the specified

Frame

as its owner.

Window

​(

Window

owner)

Constructs a new, initially invisible window with the specified

Window

as its owner.

Window

​(

Window

owner,

GraphicsConfiguration

gc)

Constructs a new, initially invisible window with the specified owner

Window

and a

GraphicsConfiguration

of a screen device.

---

#### Constructor Summary

Constructs a new, initially invisible window with the specified

Frame

as its owner.

Constructs a new, initially invisible window with the specified

Window

as its owner.

Constructs a new, initially invisible window with the specified owner

Window

and a

GraphicsConfiguration

of a screen device.

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

Makes this Window displayable by creating the connection to its
native screen resource.

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list.

void

addPropertyChangeListener

​(

String

propertyName,

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list for a specific
property.

void

addWindowFocusListener

​(

WindowFocusListener

l)

Adds the specified window focus listener to receive window events
from this window.

void

addWindowListener

​(

WindowListener

l)

Adds the specified window listener to receive window events from
this window.

void

addWindowStateListener

​(

WindowStateListener

l)

Adds the specified window state listener to receive window
events from this window.

void

applyResourceBundle

​(

String

rbName)

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

void

applyResourceBundle

​(

ResourceBundle

rb)

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

void

createBufferStrategy

​(int numBuffers)

Creates a new strategy for multi-buffering on this component.

void

createBufferStrategy

​(int numBuffers,

BufferCapabilities

caps)

Creates a new strategy for multi-buffering on this component with the
required buffer capabilities.

void

dispose

()

Releases all of the native screen resources used by this

Window

, its subcomponents, and all of its owned
children.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Window.

Color

getBackground

()

Gets the background color of this window.

BufferStrategy

getBufferStrategy

()

Returns the

BufferStrategy

used by this component.

boolean

getFocusableWindowState

()

Returns whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

.

Container

getFocusCycleRootAncestor

()

Always returns

null

because Windows have no ancestors; they
represent the top of the Component hierarchy.

Component

getFocusOwner

()

Returns the child Component of this Window that has focus if this Window
is focused; returns null otherwise.

Set

<

AWTKeyStroke

>

getFocusTraversalKeys

​(int id)

Gets a focus traversal key for this Window.

List

<

Image

>

getIconImages

()

Returns the sequence of images to be displayed as the icon for this window.

InputContext

getInputContext

()

Gets the input context for this window.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Window

.

Locale

getLocale

()

Gets the

Locale

object that is associated
with this window, if the locale has been set.

Dialog.ModalExclusionType

getModalExclusionType

()

Returns the modal exclusion type of this window.

Component

getMostRecentFocusOwner

()

Returns the child Component of this Window that will receive the focus
when this Window is focused.

float

getOpacity

()

Returns the opacity of the window.

Window

[]

getOwnedWindows

()

Return an array containing all the windows this
window currently owns.

Window

getOwner

()

Returns the owner of this window.

static

Window

[]

getOwnerlessWindows

()

Returns an array of all

Window

s created by this application
that have no owner.

Shape

getShape

()

Returns the shape of the window.

Toolkit

getToolkit

()

Returns the toolkit of this frame.

Window.Type

getType

()

Returns the type of the window.

String

getWarningString

()

Gets the warning string that is displayed with this window.

WindowFocusListener

[]

getWindowFocusListeners

()

Returns an array of all the window focus listeners
registered on this window.

WindowListener

[]

getWindowListeners

()

Returns an array of all the window listeners
registered on this window.

static

Window

[]

getWindows

()

Returns an array of all

Window

s, both owned and ownerless,
created by this application.

WindowStateListener

[]

getWindowStateListeners

()

Returns an array of all the window state listeners
registered on this window.

void

hide

()

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

boolean

isActive

()

Returns whether this Window is active.

boolean

isAlwaysOnTop

()

Returns whether this window is an always-on-top window.

boolean

isAlwaysOnTopSupported

()

Returns whether the always-on-top mode is supported for this
window.

boolean

isAutoRequestFocus

()

Returns whether this window should receive focus on subsequently being shown
(with a call to

setVisible(true)

), or being moved to the front
(with a call to

toFront()

).

boolean

isFocusableWindow

()

Returns whether this Window can become the focused Window, that is,
whether this Window or any of its subcomponents can become the focus
owner.

boolean

isFocusCycleRoot

()

Always returns

true

because all Windows must be roots of a
focus traversal cycle.

boolean

isFocused

()

Returns whether this Window is focused.

boolean

isLocationByPlatform

()

Returns

true

if this Window will appear at the default location
for the native windowing system the next time this Window is made visible.

boolean

isOpaque

()

Indicates if the window is currently opaque.

boolean

isShowing

()

Checks if this Window is showing on screen.

boolean

isValidateRoot

()

Indicates if this container is a validate root.

void

pack

()

Causes this Window to be sized to fit the preferred size
and layouts of its subcomponents.

void

paint

​(

Graphics

g)

Paints the container.

boolean

postEvent

​(

Event

e)

Deprecated.

As of JDK version 1.1
replaced by

dispatchEvent(AWTEvent)

.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this window.

protected void

processWindowEvent

​(

WindowEvent

e)

Processes window events occurring on this window by
dispatching them to any registered WindowListener objects.

protected void

processWindowFocusEvent

​(

WindowEvent

e)

Processes window focus event occurring on this window by
dispatching them to any registered WindowFocusListener objects.

protected void

processWindowStateEvent

​(

WindowEvent

e)

Processes window state event occurring on this window by
dispatching them to any registered

WindowStateListener

objects.

void

removeWindowFocusListener

​(

WindowFocusListener

l)

Removes the specified window focus listener so that it no longer
receives window events from this window.

void

removeWindowListener

​(

WindowListener

l)

Removes the specified window listener so that it no longer
receives window events from this window.

void

removeWindowStateListener

​(

WindowStateListener

l)

Removes the specified window state listener so that it no
longer receives window events from this window.

void

reshape

​(int x,
int y,
int width,
int height)

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

void

setAlwaysOnTop

​(boolean alwaysOnTop)

Sets whether this window should always be above other windows.

void

setAutoRequestFocus

​(boolean autoRequestFocus)

Sets whether this window should receive focus on
subsequently being shown (with a call to

setVisible(true)

),
or being moved to the front (with a call to

toFront()

).

void

setBackground

​(

Color

bgColor)

Sets the background color of this window.

void

setBounds

​(int x,
int y,
int width,
int height)

Moves and resizes this component.

void

setBounds

​(

Rectangle

r)

Moves and resizes this component to conform to the new
bounding rectangle

r

.

void

setCursor

​(

Cursor

cursor)

Set the cursor image to a specified cursor.

void

setFocusableWindowState

​(boolean focusableWindowState)

Sets whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

.

void

setFocusCycleRoot

​(boolean focusCycleRoot)

Does nothing because Windows must always be roots of a focus traversal
cycle.

void

setIconImage

​(

Image

image)

Sets the image to be displayed as the icon for this window.

void

setIconImages

​(

List

<? extends

Image

> icons)

Sets the sequence of images to be displayed as the icon
for this window.

void

setLocation

​(int x,
int y)

Moves this component to a new location.

void

setLocation

​(

Point

p)

Moves this component to a new location.

void

setLocationByPlatform

​(boolean locationByPlatform)

Sets whether this Window should appear at the default location for the
native windowing system or at the current location (returned by

getLocation

) the next time the Window is made visible.

void

setLocationRelativeTo

​(

Component

c)

Sets the location of the window relative to the specified
component according to the following scenarios.

void

setMinimumSize

​(

Dimension

minimumSize)

Sets the minimum size of this window to a constant
value.

void

setModalExclusionType

​(

Dialog.ModalExclusionType

exclusionType)

Specifies the modal exclusion type for this window.

void

setOpacity

​(float opacity)

Sets the opacity of the window.

void

setShape

​(

Shape

shape)

Sets the shape of the window.

void

setSize

​(int width,
int height)

Resizes this component so that it has width

width

and height

height

.

void

setSize

​(

Dimension

d)

Resizes this component so that it has width

d.width

and height

d.height

.

void

setType

​(

Window.Type

type)

Sets the type of the window.

void

setVisible

​(boolean b)

Shows or hides this

Window

depending on the value of parameter

b

.

void

show

()

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

void

toBack

()

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

void

toFront

()

If this Window is visible, brings this Window to the front and may make
it the focused Window.

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

paramString

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

removeNotify

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

---

#### Method Summary

Makes this Window displayable by creating the connection to its
native screen resource.

Adds a PropertyChangeListener to the listener list.

Adds a PropertyChangeListener to the listener list for a specific
property.

Adds the specified window focus listener to receive window events
from this window.

Adds the specified window listener to receive window events from
this window.

Adds the specified window state listener to receive window
events from this window.

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

Creates a new strategy for multi-buffering on this component.

Creates a new strategy for multi-buffering on this component with the
required buffer capabilities.

Releases all of the native screen resources used by this

Window

, its subcomponents, and all of its owned
children.

Gets the AccessibleContext associated with this Window.

Gets the background color of this window.

Returns the

BufferStrategy

used by this component.

Returns whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

.

Always returns

null

because Windows have no ancestors; they
represent the top of the Component hierarchy.

Returns the child Component of this Window that has focus if this Window
is focused; returns null otherwise.

Gets a focus traversal key for this Window.

Returns the sequence of images to be displayed as the icon for this window.

Gets the input context for this window.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Window

.

Gets the

Locale

object that is associated
with this window, if the locale has been set.

Returns the modal exclusion type of this window.

Returns the child Component of this Window that will receive the focus
when this Window is focused.

Returns the opacity of the window.

Return an array containing all the windows this
window currently owns.

Returns the owner of this window.

Returns an array of all

Window

s created by this application
that have no owner.

Returns the shape of the window.

Returns the toolkit of this frame.

Returns the type of the window.

Gets the warning string that is displayed with this window.

Returns an array of all the window focus listeners
registered on this window.

Returns an array of all the window listeners
registered on this window.

Returns an array of all

Window

s, both owned and ownerless,
created by this application.

Returns an array of all the window state listeners
registered on this window.

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Returns whether this Window is active.

Returns whether this window is an always-on-top window.

Returns whether the always-on-top mode is supported for this
window.

Returns whether this window should receive focus on subsequently being shown
(with a call to

setVisible(true)

), or being moved to the front
(with a call to

toFront()

).

Returns whether this Window can become the focused Window, that is,
whether this Window or any of its subcomponents can become the focus
owner.

Always returns

true

because all Windows must be roots of a
focus traversal cycle.

Returns whether this Window is focused.

Returns

true

if this Window will appear at the default location
for the native windowing system the next time this Window is made visible.

Indicates if the window is currently opaque.

Checks if this Window is showing on screen.

Indicates if this container is a validate root.

Causes this Window to be sized to fit the preferred size
and layouts of its subcomponents.

Paints the container.

Deprecated.

As of JDK version 1.1
replaced by

dispatchEvent(AWTEvent)

.

Processes events on this window.

Processes window events occurring on this window by
dispatching them to any registered WindowListener objects.

Processes window focus event occurring on this window by
dispatching them to any registered WindowFocusListener objects.

Processes window state event occurring on this window by
dispatching them to any registered

WindowStateListener

objects.

Removes the specified window focus listener so that it no longer
receives window events from this window.

Removes the specified window listener so that it no longer
receives window events from this window.

Removes the specified window state listener so that it no
longer receives window events from this window.

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

Sets whether this window should always be above other windows.

Sets whether this window should receive focus on
subsequently being shown (with a call to

setVisible(true)

),
or being moved to the front (with a call to

toFront()

).

Sets the background color of this window.

Moves and resizes this component.

Moves and resizes this component to conform to the new
bounding rectangle

r

.

Set the cursor image to a specified cursor.

Sets whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

.

Does nothing because Windows must always be roots of a focus traversal
cycle.

Sets the image to be displayed as the icon for this window.

Sets the sequence of images to be displayed as the icon
for this window.

Moves this component to a new location.

Sets whether this Window should appear at the default location for the
native windowing system or at the current location (returned by

getLocation

) the next time the Window is made visible.

Sets the location of the window relative to the specified
component according to the following scenarios.

Sets the minimum size of this window to a constant
value.

Specifies the modal exclusion type for this window.

Sets the opacity of the window.

Sets the shape of the window.

Resizes this component so that it has width

width

and height

height

.

Resizes this component so that it has width

d.width

and height

d.height

.

Sets the type of the window.

Shows or hides this

Window

depending on the value of parameter

b

.

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

If this Window is visible, brings this Window to the front and may make
it the focused Window.

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

paramString

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

removeNotify

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Window

```java
public Window​(
Frame
owner)
```

Constructs a new, initially invisible window with the specified

Frame

as its owner. The window will not be focusable
unless its owner is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a warning
banner is created.

**Parameters:** owner

- the

Frame

to act as owner or

null

if this window has no owner
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

,

isShowing()

- Window

```java
public Window​(
Window
owner)
```

Constructs a new, initially invisible window with the specified

Window

as its owner. This window will not be focusable
unless its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a
warning banner is created.

**Parameters:** owner

- the

Window

to act as owner or

null

if this window has no owner
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

,

isShowing()

- Window

```java
public Window​(
Window
owner,

GraphicsConfiguration
gc)
```

Constructs a new, initially invisible window with the specified owner

Window

and a

GraphicsConfiguration

of a screen device. The Window will not be focusable unless
its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

. If that
check fails with a

SecurityException

then a warning banner
is created.

**Parameters:** owner

- the window to act as owner or

null

if this window has no owner
**Parameters:** gc

- the

GraphicsConfiguration

of the target
screen device; if

gc

is

null

,
the system default

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

GraphicsConfiguration.getBounds()

,

isShowing()

============ METHOD DETAIL ==========

- Method Detail

- getIconImages

```java
public
List
<
Image
> getIconImages()
```

Returns the sequence of images to be displayed as the icon for this window.

This method returns a copy of the internally stored list, so all operations
on the returned object will not affect the window's behavior.

**Returns:** the copy of icon images' list for this window, or
empty list if this window doesn't have icon images.
**Since:** 1.6
**See Also:** setIconImages(java.util.List<? extends java.awt.Image>)

,

setIconImage(Image)

- setIconImages

```java
public void setIconImages​(
List
<? extends
Image
> icons)
```

Sets the sequence of images to be displayed as the icon
for this window. Subsequent calls to

getIconImages

will
always return a copy of the

icons

list.

Depending on the platform capabilities one or several images
of different dimensions will be used as the window's icon.

The

icons

list can contain

MultiResolutionImage

images also.
Suitable image depending on screen resolution is extracted from
base

MultiResolutionImage

image and added to the icons list
while base resolution image is removed from list.
The

icons

list is scanned for the images of most
appropriate dimensions from the beginning. If the list contains
several images of the same size, the first will be used.

Ownerless windows with no icon specified use platform-default icon.
The icon of an owned window may be inherited from the owner
unless explicitly overridden.
Setting the icon to

null

or empty list restores
the default behavior.

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

**Parameters:** icons

- the list of icon images to be displayed.
**Since:** 1.6
**See Also:** getIconImages()

,

setIconImage(Image)

- setIconImage

```java
public void setIconImage​(
Image
image)
```

Sets the image to be displayed as the icon for this window.

This method can be used instead of

setIconImages()

to specify a single image as a window's icon.

The following statement:

```java
setIconImage(image);
```

is equivalent to:

```java
ArrayList<Image> imageList = new ArrayList<Image>();
imageList.add(image);
setIconImages(imageList);
```

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

**Parameters:** image

- the icon image to be displayed.
**Since:** 1.6
**See Also:** setIconImages(java.util.List<? extends java.awt.Image>)

,

getIconImages()

- addNotify

```java
public void addNotify()
```

Makes this Window displayable by creating the connection to its
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Container
**Since:** 1.0
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

- pack

```java
public void pack()
```

Causes this Window to be sized to fit the preferred size
and layouts of its subcomponents. The resulting width and
height of the window are automatically enlarged if either
of dimensions is less than the minimum size as specified
by the previous call to the

setMinimumSize

method.

If the window and/or its owner are not displayable yet,
both of them are made displayable before calculating
the preferred size. The Window is validated after its
size is being calculated.

**See Also:** Component.isDisplayable()

,

setMinimumSize(java.awt.Dimension)

- setMinimumSize

```java
public void setMinimumSize​(
Dimension
minimumSize)
```

Sets the minimum size of this window to a constant
value. Subsequent calls to

getMinimumSize

will always return this value. If current window's
size is less than

minimumSize

the size of the
window is automatically enlarged to honor the minimum size.

If the

setSize

or

setBounds

methods
are called afterwards with a width or height less than
that was specified by the

setMinimumSize

method
the window is automatically enlarged to meet
the

minimumSize

value. The

minimumSize

value also affects the behaviour of the

pack

method.

The default behavior is restored by setting the minimum size
parameter to the

null

value.

Resizing operation may be restricted if the user tries
to resize window below the

minimumSize

value.
This behaviour is platform-dependent.

**Overrides:** setMinimumSize

in class

Component
**Parameters:** minimumSize

- the new minimum size of this window
**Since:** 1.6
**See Also:** Component.setMinimumSize(java.awt.Dimension)

,

Container.getMinimumSize()

,

Component.isMinimumSizeSet()

,

setSize(Dimension)

,

pack()

- setSize

```java
public void setSize​(
Dimension
d)
```

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

d.width

and

d.height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setSize

in class

Component
**Parameters:** d

- the dimension specifying the new size
of this component
**Since:** 1.6
**See Also:** Component.getSize()

,

setBounds(int, int, int, int)

,

setMinimumSize(java.awt.Dimension)

- setSize

```java
public void setSize​(int width,
int height)
```

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

and

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setSize

in class

Component
**Parameters:** width

- the new width of this component in pixels
**Parameters:** height

- the new height of this component in pixels
**Since:** 1.6
**See Also:** Component.getSize()

,

setBounds(int, int, int, int)

,

setMinimumSize(java.awt.Dimension)

- setLocation

```java
public void setLocation​(int x,
int y)
```

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setLocation

in class

Component
**Parameters:** x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Parameters:** y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space
**See Also:** Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

- setLocation

```java
public void setLocation​(
Point
p)
```

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setLocation

in class

Component
**Parameters:** p

- the point defining the top-left corner
of the new location, given in the coordinate space of this
component's parent
**See Also:** Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

- reshape

```java
@Deprecated

public void reshape​(int x,
int y,
int width,
int height)
```

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

Description copied from class:

Component

Reshapes the bounding rectangle for this component.

**Overrides:** reshape

in class

Component
**Parameters:** x

- the

x

coordinate of the upper left corner of the rectangle
**Parameters:** y

- the

y

coordinate of the upper left corner of the rectangle
**Parameters:** width

- the width of the rectangle
**Parameters:** height

- the height of the rectangle

- setVisible

```java
public void setVisible​(boolean b)
```

Shows or hides this

Window

depending on the value of parameter

b

.

If the method shows the window then the window is also made
focused under the following conditions:

- The

Window

meets the requirements outlined in the

isFocusableWindow()

method.

The

Window

's

autoRequestFocus

property is of the

true

value.

Native windowing system allows the

Window

to get focused.

There is an exception for the second condition (the value of the

autoRequestFocus

property). The property is not taken into account if the
window is a modal dialog, which blocks the currently focused window.

Developers must never assume that the window is the focused or active window
until it receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED event.

**Overrides:** setVisible

in class

Component
**Parameters:** b

- if

true

, makes the

Window

visible,
otherwise hides the

Window

.
If the

Window

and/or its owner
are not yet displayable, both are made displayable. The

Window

will be validated prior to being made visible.
If the

Window

is already visible, this will bring the

Window

to the front.

If

false

, hides this

Window

, its subcomponents, and all
of its owned children.
The

Window

and its subcomponents can be made visible again
with a call to

#setVisible(true)

.
**See Also:** Component.isDisplayable()

,

Component.setVisible(boolean)

,

toFront()

,

dispose()

,

setAutoRequestFocus(boolean)

,

isFocusableWindow()

- show

```java
@Deprecated

public void show()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Makes the Window visible. If the Window and/or its owner
are not yet displayable, both are made displayable. The
Window will be validated prior to being made visible.
If the Window is already visible, this will bring the Window
to the front.

**Overrides:** show

in class

Component
**See Also:** Component.isDisplayable()

,

toFront()

- hide

```java
@Deprecated

public void hide()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Hide this Window, its subcomponents, and all of its owned children.
The Window and its subcomponents can be made visible again
with a call to

show

.

**Overrides:** hide

in class

Component
**See Also:** show()

,

dispose()

- dispose

```java
public void dispose()
```

Releases all of the native screen resources used by this

Window

, its subcomponents, and all of its owned
children. That is, the resources for these

Component

s
will be destroyed, any memory they consume will be returned to the
OS, and they will be marked as undisplayable.

The

Window

and its subcomponents can be made displayable
again by rebuilding the native resources with a subsequent call to

pack

or

show

. The states of the recreated

Window

and its subcomponents will be identical to the
states of these objects at the point where the

Window

was disposed (not accounting for additional modifications between
those actions).

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**See Also:** Component.isDisplayable()

,

pack()

,

show()

- toFront

```java
public void toFront()
```

If this Window is visible, brings this Window to the front and may make
it the focused Window.

Places this Window at the top of the stacking order and shows it in
front of any other Windows in this VM. No action will take place if this
Window is not visible. Some platforms do not allow Windows which own
other Windows to appear on top of those owned Windows. Some platforms
may not permit this VM to place its Windows above windows of native
applications, or Windows of other VMs. This permission may depend on
whether a Window in this VM is already focused. Every attempt will be
made to move this Window as high as possible in the stacking order;
however, developers should not assume that this method will move this
Window above all other windows in every situation.

Developers must never assume that this Window is the focused or active
Window until this Window receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED
event. On platforms where the top-most window is the focused window, this
method will

probably

focus this Window (if it is not already focused)
under the following conditions:

- The window meets the requirements outlined in the

isFocusableWindow()

method.

The window's property

autoRequestFocus

is of the

true

value.

Native windowing system allows the window to get focused.

On platforms where the stacking order does not typically affect the focused
window, this method will

probably

leave the focused and active
Windows unchanged.

If this method causes this Window to be focused, and this Window is a
Frame or a Dialog, it will also become activated. If this Window is
focused, but it is not a Frame or a Dialog, then the first Frame or
Dialog that is an owner of this Window will be activated.

If this window is blocked by modal dialog, then the blocking dialog
is brought to the front and remains above the blocked window.

**See Also:** toBack()

,

setAutoRequestFocus(boolean)

,

isFocusableWindow()

- toBack

```java
public void toBack()
```

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

**See Also:** toFront()

- getToolkit

```java
public
Toolkit
getToolkit()
```

Returns the toolkit of this frame.

**Overrides:** getToolkit

in class

Component
**Returns:** the toolkit of this window.
**See Also:** Toolkit

,

Toolkit.getDefaultToolkit()

,

Component.getToolkit()

- getWarningString

```java
public final
String
getWarningString()
```

Gets the warning string that is displayed with this window.
If this window is insecure, the warning string is displayed
somewhere in the visible area of the window. A window is
insecure if there is a security manager and the security
manager denies

AWTPermission("showWindowWithoutWarningBanner")

.

If the window is secure, then

getWarningString

returns

null

. If the window is insecure, this
method checks for the system property

awt.appletWarning

and returns the string value of that property.

**Returns:** the warning string for this window.

- getLocale

```java
public
Locale
getLocale()
```

Gets the

Locale

object that is associated
with this window, if the locale has been set.
If no locale has been set, then the default locale
is returned.

**Overrides:** getLocale

in class

Component
**Returns:** the locale that is set for this window.
**Since:** 1.1
**See Also:** Locale

- getInputContext

```java
public
InputContext
getInputContext()
```

Gets the input context for this window. A window always has an input context,
which is shared by subcomponents unless they create and set their own.

**Overrides:** getInputContext

in class

Component
**Returns:** the input context used by this component;

null

if no context can be determined
**Since:** 1.2
**See Also:** Component.getInputContext()

- setCursor

```java
public void setCursor​(
Cursor
cursor)
```

Set the cursor image to a specified cursor.

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

class. If this parameter is null
then the cursor for this window will be set to the type
Cursor.DEFAULT_CURSOR.
**Since:** 1.1
**See Also:** Component.getCursor()

,

Cursor

- getOwner

```java
public
Window
getOwner()
```

Returns the owner of this window.

**Returns:** the owner of this window
**Since:** 1.2

- getOwnedWindows

```java
public
Window
[] getOwnedWindows()
```

Return an array containing all the windows this
window currently owns.

**Returns:** the array of all the owned windows
**Since:** 1.2

- getWindows

```java
public static
Window
[] getWindows()
```

Returns an array of all

Window

s, both owned and ownerless,
created by this application.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

**Returns:** the array of all the

Window

s created by the application
**Since:** 1.6
**See Also:** Frame.getFrames()

,

getOwnerlessWindows()

- getOwnerlessWindows

```java
public static
Window
[] getOwnerlessWindows()
```

Returns an array of all

Window

s created by this application
that have no owner. They include

Frame

s and ownerless

Dialog

s and

Window

s.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

**Returns:** the array of all the ownerless

Window

s
created by this application
**Since:** 1.6
**See Also:** Frame.getFrames()

,

getWindows()

- setModalExclusionType

```java
public void setModalExclusionType​(
Dialog.ModalExclusionType
exclusionType)
```

Specifies the modal exclusion type for this window. If a window is modal
excluded, it is not blocked by some modal dialogs. See

Dialog.ModalExclusionType

for
possible modal exclusion types.

If the given type is not supported,

NO_EXCLUDE

is used.

Note: changing the modal exclusion type for a visible window may have no
effect until it is hidden and then shown again.

**Parameters:** exclusionType

- the modal exclusion type for this window; a

null

value is equivalent to

NO_EXCLUDE
**Throws:** SecurityException

- if the calling thread does not have permission
to set the modal exclusion property to the window with the given

exclusionType
**Since:** 1.6
**See Also:** Dialog.ModalExclusionType

,

getModalExclusionType()

,

Toolkit.isModalExclusionTypeSupported(java.awt.Dialog.ModalExclusionType)

- getModalExclusionType

```java
public
Dialog.ModalExclusionType
getModalExclusionType()
```

Returns the modal exclusion type of this window.

**Returns:** the modal exclusion type of this window
**Since:** 1.6
**See Also:** Dialog.ModalExclusionType

,

setModalExclusionType(java.awt.Dialog.ModalExclusionType)

- addWindowListener

```java
public void addWindowListener​(
WindowListener
l)
```

Adds the specified window listener to receive window events from
this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window listener
**See Also:** removeWindowListener(java.awt.event.WindowListener)

,

getWindowListeners()

- addWindowStateListener

```java
public void addWindowStateListener​(
WindowStateListener
l)
```

Adds the specified window state listener to receive window
events from this window. If

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window state listener
**Since:** 1.4
**See Also:** removeWindowStateListener(java.awt.event.WindowStateListener)

,

getWindowStateListeners()

- addWindowFocusListener

```java
public void addWindowFocusListener​(
WindowFocusListener
l)
```

Adds the specified window focus listener to receive window events
from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window focus listener
**Since:** 1.4
**See Also:** removeWindowFocusListener(java.awt.event.WindowFocusListener)

,

getWindowFocusListeners()

- removeWindowListener

```java
public void removeWindowListener​(
WindowListener
l)
```

Removes the specified window listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window listener
**See Also:** addWindowListener(java.awt.event.WindowListener)

,

getWindowListeners()

- removeWindowStateListener

```java
public void removeWindowStateListener​(
WindowStateListener
l)
```

Removes the specified window state listener so that it no
longer receives window events from this window. If

l

is

null

, no exception is thrown and
no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window state listener
**Since:** 1.4
**See Also:** addWindowStateListener(java.awt.event.WindowStateListener)

,

getWindowStateListeners()

- removeWindowFocusListener

```java
public void removeWindowFocusListener​(
WindowFocusListener
l)
```

Removes the specified window focus listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window focus listener
**Since:** 1.4
**See Also:** addWindowFocusListener(java.awt.event.WindowFocusListener)

,

getWindowFocusListeners()

- getWindowListeners

```java
public
WindowListener
[] getWindowListeners()
```

Returns an array of all the window listeners
registered on this window.

**Returns:** all of this window's

WindowListener

s
or an empty array if no window
listeners are currently registered
**Since:** 1.4
**See Also:** addWindowListener(java.awt.event.WindowListener)

,

removeWindowListener(java.awt.event.WindowListener)

- getWindowFocusListeners

```java
public
WindowFocusListener
[] getWindowFocusListeners()
```

Returns an array of all the window focus listeners
registered on this window.

**Returns:** all of this window's

WindowFocusListener

s
or an empty array if no window focus
listeners are currently registered
**Since:** 1.4
**See Also:** addWindowFocusListener(java.awt.event.WindowFocusListener)

,

removeWindowFocusListener(java.awt.event.WindowFocusListener)

- getWindowStateListeners

```java
public
WindowStateListener
[] getWindowStateListeners()
```

Returns an array of all the window state listeners
registered on this window.

**Returns:** all of this window's

WindowStateListener

s
or an empty array if no window state
listeners are currently registered
**Since:** 1.4
**See Also:** addWindowStateListener(java.awt.event.WindowStateListener)

,

removeWindowStateListener(java.awt.event.WindowStateListener)

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Window

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Window w

for its window listeners with the following code:

```java
WindowListener[] wls = (WindowListener[])(w.getListeners(WindowListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Container
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this window,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Throws:** NullPointerException

- if

listenerType

is

null
**Since:** 1.3
**See Also:** getWindowListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this window. If the event is an

WindowEvent

, it invokes the

processWindowEvent

method, else it invokes its
superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Container
**Parameters:** e

- the event
**See Also:** Component.processComponentEvent(java.awt.event.ComponentEvent)

,

Component.processFocusEvent(java.awt.event.FocusEvent)

,

Component.processKeyEvent(java.awt.event.KeyEvent)

,

Component.processMouseEvent(java.awt.event.MouseEvent)

,

Component.processMouseMotionEvent(java.awt.event.MouseEvent)

,

Component.processInputMethodEvent(java.awt.event.InputMethodEvent)

,

Component.processHierarchyEvent(java.awt.event.HierarchyEvent)

,

Component.processMouseWheelEvent(java.awt.event.MouseWheelEvent)

- processWindowEvent

```java
protected void processWindowEvent​(
WindowEvent
e)
```

Processes window events occurring on this window by
dispatching them to any registered WindowListener objects.
NOTE: This method will not be called unless window events
are enabled for this component; this happens when one of the
following occurs:

- A WindowListener object is registered via

addWindowListener

Window events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the window event
**See Also:** Component.enableEvents(long)

- processWindowFocusEvent

```java
protected void processWindowFocusEvent​(
WindowEvent
e)
```

Processes window focus event occurring on this window by
dispatching them to any registered WindowFocusListener objects.
NOTE: this method will not be called unless window focus events
are enabled for this window. This happens when one of the
following occurs:

- a WindowFocusListener is registered via

addWindowFocusListener

Window focus events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the window focus event
**Since:** 1.4
**See Also:** Component.enableEvents(long)

- processWindowStateEvent

```java
protected void processWindowStateEvent​(
WindowEvent
e)
```

Processes window state event occurring on this window by
dispatching them to any registered

WindowStateListener

objects.
NOTE: this method will not be called unless window state events
are enabled for this window. This happens when one of the
following occurs:

- a

WindowStateListener

is registered via

addWindowStateListener

window state events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the window state event
**Since:** 1.4
**See Also:** Component.enableEvents(long)

- setAlwaysOnTop

```java
public final void setAlwaysOnTop​(boolean alwaysOnTop)
throws
SecurityException
```

Sets whether this window should always be above other windows. If
there are multiple always-on-top windows, their relative order is
unspecified and platform dependent.

If some other window is already always-on-top then the
relative order between these windows is unspecified (depends on
platform). No window can be brought to be over the always-on-top
window except maybe another always-on-top window.

All windows owned by an always-on-top window inherit this state and
automatically become always-on-top. If a window ceases to be
always-on-top, the windows that it owns will no longer be
always-on-top. When an always-on-top window is sent

toBack

, its always-on-top state is set to

false

.

When this method is called on a window with a value of

true

, and the window is visible and the platform
supports always-on-top for this window, the window is immediately
brought forward, "sticking" it in the top-most position. If the
window isn`t currently visible, this method sets the always-on-top
state to

true

but does not bring the window forward.
When the window is later shown, it will be always-on-top.

When this method is called on a window with a value of

false

the always-on-top state is set to normal. It may also
cause an unspecified, platform-dependent change in the z-order of
top-level windows, but other always-on-top windows will remain in
top-most position. Calling this method with a value of

false

on a window that has a normal state has no effect.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

**Parameters:** alwaysOnTop

- true if the window should always be above other
windows
**Throws:** SecurityException

- if the calling thread does not have
permission to set the value of always-on-top property
**Since:** 1.5
**See Also:** isAlwaysOnTop()

,

toFront()

,

toBack()

,

AWTPermission

,

isAlwaysOnTopSupported()

,

getToolkit()

,

Toolkit.isAlwaysOnTopSupported()

- isAlwaysOnTopSupported

```java
public boolean isAlwaysOnTopSupported()
```

Returns whether the always-on-top mode is supported for this
window. Some platforms may not support always-on-top windows, some
may support only some kinds of top-level windows; for example,
a platform may not support always-on-top modal dialogs.

**Returns:** true

, if the always-on-top mode is supported for
this window and this window's toolkit supports always-on-top windows,

false

otherwise
**Since:** 1.6
**See Also:** setAlwaysOnTop(boolean)

,

getToolkit()

,

Toolkit.isAlwaysOnTopSupported()

- isAlwaysOnTop

```java
public final boolean isAlwaysOnTop()
```

Returns whether this window is an always-on-top window.

**Returns:** true

, if the window is in always-on-top state,

false

otherwise
**Since:** 1.5
**See Also:** setAlwaysOnTop(boolean)

- getFocusOwner

```java
public
Component
getFocusOwner()
```

Returns the child Component of this Window that has focus if this Window
is focused; returns null otherwise.

**Returns:** the child Component with focus, or null if this Window is not
focused
**See Also:** getMostRecentFocusOwner()

,

isFocused()

- getMostRecentFocusOwner

```java
public
Component
getMostRecentFocusOwner()
```

Returns the child Component of this Window that will receive the focus
when this Window is focused. If this Window is currently focused, this
method returns the same Component as

getFocusOwner()

. If
this Window is not focused, then the child Component that most recently
requested focus will be returned. If no child Component has ever
requested focus, and this is a focusable Window, then this Window's
initial focusable Component is returned. If no child Component has ever
requested focus, and this is a non-focusable Window, null is returned.

**Returns:** the child Component that will receive focus when this Window is
focused
**Since:** 1.4
**See Also:** getFocusOwner()

,

isFocused()

,

isFocusableWindow()

- isActive

```java
public boolean isActive()
```

Returns whether this Window is active. Only a Frame or a Dialog may be
active. The native windowing system may denote the active Window or its
children with special decorations, such as a highlighted title bar. The
active Window is always either the focused Window, or the first Frame or
Dialog that is an owner of the focused Window.

**Returns:** whether this is the active Window.
**Since:** 1.4
**See Also:** isFocused()

- isFocused

```java
public boolean isFocused()
```

Returns whether this Window is focused. If there exists a focus owner,
the focused Window is the Window that is, or contains, that focus owner.
If there is no focus owner, then no Window is focused.

If the focused Window is a Frame or a Dialog it is also the active
Window. Otherwise, the active Window is the first Frame or Dialog that
is an owner of the focused Window.

**Returns:** whether this is the focused Window.
**Since:** 1.4
**See Also:** isActive()

- getFocusTraversalKeys

```java
public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)
```

Gets a focus traversal key for this Window. (See

setFocusTraversalKeys

for a full description of each key.)

If the traversal key has not been explicitly set for this Window,
then this Window's parent's traversal key is returned. If the
traversal key has not been explicitly set for any of this Window's
ancestors, then the current KeyboardFocusManager's default traversal key
is returned.

**Overrides:** getFocusTraversalKeys

in class

Container
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Returns:** the AWTKeyStroke for the specified key
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4
**See Also:** Container.setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

- setFocusCycleRoot

```java
public final void setFocusCycleRoot​(boolean focusCycleRoot)
```

Does nothing because Windows must always be roots of a focus traversal
cycle. The passed-in value is ignored.

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

because all Windows must be roots of a
focus traversal cycle.

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
public final
Container
getFocusCycleRootAncestor()
```

Always returns

null

because Windows have no ancestors; they
represent the top of the Component hierarchy.

**Overrides:** getFocusCycleRootAncestor

in class

Component
**Returns:** null
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

- isFocusableWindow

```java
public final boolean isFocusableWindow()
```

Returns whether this Window can become the focused Window, that is,
whether this Window or any of its subcomponents can become the focus
owner. For a Frame or Dialog to be focusable, its focusable Window state
must be set to

true

. For a Window which is not a Frame or
Dialog to be focusable, its focusable Window state must be set to

true

, its nearest owning Frame or Dialog must be
showing on the screen, and it must contain at least one Component in
its focus traversal cycle. If any of these conditions is not met, then
neither this Window nor any of its subcomponents can become the focus
owner.

**Returns:** true

if this Window can be the focused Window;

false

otherwise
**Since:** 1.4
**See Also:** getFocusableWindowState()

,

setFocusableWindowState(boolean)

,

isShowing()

,

Component.isFocusable()

- getFocusableWindowState

```java
public boolean getFocusableWindowState()
```

Returns whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this method returns

false

, then

isFocusableWindow

will return

false

as well.
If this method returns

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

By default, all Windows have a focusable Window state of

true

.

**Returns:** whether this Window can be the focused Window
**Since:** 1.4
**See Also:** isFocusableWindow()

,

setFocusableWindowState(boolean)

,

isShowing()

,

Component.setFocusable(boolean)

- setFocusableWindowState

```java
public void setFocusableWindowState​(boolean focusableWindowState)
```

Sets whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this Window's focusable Window state is set to

false

, then

isFocusableWindow

will return

false

. If this
Window's focusable Window state is set to

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

Setting a Window's focusability state to

false

is the
standard mechanism for an application to identify to the AWT a Window
which will be used as a floating palette or toolbar, and thus should be
a non-focusable Window.

Setting the focusability state on a visible

Window

can have a delayed effect on some platforms — the actual
change may happen only when the

Window

becomes
hidden and then visible again. To ensure consistent behavior
across platforms, set the

Window

's focusable state
when the

Window

is invisible and then show it.

**Parameters:** focusableWindowState

- whether this Window can be the focused
Window
**Since:** 1.4
**See Also:** isFocusableWindow()

,

getFocusableWindowState()

,

isShowing()

,

Component.setFocusable(boolean)

- setAutoRequestFocus

```java
public void setAutoRequestFocus​(boolean autoRequestFocus)
```

Sets whether this window should receive focus on
subsequently being shown (with a call to

setVisible(true)

),
or being moved to the front (with a call to

toFront()

).

Note that

setVisible(true)

may be called indirectly
(e.g. when showing an owner of the window makes the window to be shown).

toFront()

may also be called indirectly (e.g. when

setVisible(true)

is called on already visible window).
In all such cases this property takes effect as well.

The value of the property is not inherited by owned windows.

**Parameters:** autoRequestFocus

- whether this window should be focused on
subsequently being shown or being moved to the front
**Since:** 1.7
**See Also:** isAutoRequestFocus()

,

isFocusableWindow()

,

setVisible(boolean)

,

toFront()

- isAutoRequestFocus

```java
public boolean isAutoRequestFocus()
```

Returns whether this window should receive focus on subsequently being shown
(with a call to

setVisible(true)

), or being moved to the front
(with a call to

toFront()

).

By default, the window has

autoRequestFocus

value of

true

.

**Returns:** autoRequestFocus

value
**Since:** 1.7
**See Also:** setAutoRequestFocus(boolean)

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Container
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

,

addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Container
**Parameters:** propertyName

- one of the property names listed above
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

- isValidateRoot

```java
public boolean isValidateRoot()
```

Indicates if this container is a validate root.

Window

objects are the validate roots, and, therefore, they
override this method to return

true

.

**Overrides:** isValidateRoot

in class

Container
**Returns:** true
**Since:** 1.7
**See Also:** Container.isValidateRoot()

- postEvent

```java
@Deprecated

public boolean postEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1
replaced by

dispatchEvent(AWTEvent)

.

Description copied from interface:

MenuContainer

Posts an event to the listeners.

**Specified by:** postEvent

in interface

MenuContainer
**Overrides:** postEvent

in class

Component
**Parameters:** e

- the event to dispatch
**Returns:** the results of posting the event

- isShowing

```java
public boolean isShowing()
```

Checks if this Window is showing on screen.

**Overrides:** isShowing

in class

Component
**Returns:** true

if the component is showing,

false

otherwise
**See Also:** Component.setVisible(boolean)

- applyResourceBundle

```java
@Deprecated

public void applyResourceBundle​(
ResourceBundle
rb)
```

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

**Parameters:** rb

- the resource bundle

- applyResourceBundle

```java
@Deprecated

public void applyResourceBundle​(
String
rbName)
```

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

**Parameters:** rbName

- the resource name

- setType

```java
public void setType​(
Window.Type
type)
```

Sets the type of the window.

This method can only be called while the window is not displayable.

**Parameters:** type

- the window type
**Throws:** IllegalComponentStateException

- if the window
is displayable.
**Throws:** IllegalArgumentException

- if the type is

null
**Since:** 1.7
**See Also:** Component.isDisplayable()

,

getType()

- getType

```java
public
Window.Type
getType()
```

Returns the type of the window.

**Returns:** the type of the window
**Since:** 1.7
**See Also:** setType(java.awt.Window.Type)

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Window.
For windows, the AccessibleContext takes the form of an
AccessibleAWTWindow.
A new AccessibleAWTWindow instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleAWTWindow that serves as the
AccessibleContext of this Window
**Since:** 1.3

- setLocationRelativeTo

```java
public void setLocationRelativeTo​(
Component
c)
```

Sets the location of the window relative to the specified
component according to the following scenarios.

The target screen mentioned below is a screen to which
the window should be placed after the setLocationRelativeTo
method is called.

- If the component is

null

, or the

GraphicsConfiguration

associated with this component is

null

, the window is placed in the center of the
screen. The center point can be obtained with the

GraphicsEnvironment.getCenterPoint

method.

If the component is not

null

, but it is not
currently showing, the window is placed in the center of
the target screen defined by the

GraphicsConfiguration

associated with this component.

If the component is not

null

and is shown on
the screen, then the window is located in such a way that
the center of the window coincides with the center of the
component.

If the screens configuration does not allow the window to
be moved from one screen to another, then the window is
only placed at the location determined according to the
above conditions and its

GraphicsConfiguration

is
not changed.

Note

: If the lower edge of the window is out of the screen,
then the window is placed to the side of the

Component

that is closest to the center of the screen. So if the
component is on the right part of the screen, the window
is placed to its left, and vice versa.

If after the window location has been calculated, the upper,
left, or right edge of the window is out of the screen,
then the window is located in such a way that the upper,
left, or right edge of the window coincides with the
corresponding edge of the screen. If both left and right
edges of the window are out of the screen, the window is
placed at the left side of the screen. The similar placement
will occur if both top and bottom edges are out of the screen.
In that case, the window is placed at the top side of the screen.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Parameters:** c

- the component in relation to which the window's location
is determined
**Since:** 1.4
**See Also:** GraphicsEnvironment.getCenterPoint()

- createBufferStrategy

```java
public void createBufferStrategy​(int numBuffers)
```

Creates a new strategy for multi-buffering on this component.
Multi-buffering is useful for rendering performance. This method
attempts to create the best strategy available with the number of
buffers supplied. It will always create a

BufferStrategy

with that number of buffers.
A page-flipping strategy is attempted first, then a blitting strategy
using accelerated buffers. Finally, an unaccelerated blitting
strategy is used.

Each time this method is called,
the existing buffer strategy for this component is discarded.

**Parameters:** numBuffers

- number of buffers to create
**Throws:** IllegalArgumentException

- if numBuffers is less than 1.
**Throws:** IllegalStateException

- if the component is not displayable
**Since:** 1.4
**See Also:** Component.isDisplayable()

,

getBufferStrategy()

- createBufferStrategy

```java
public void createBufferStrategy​(int numBuffers,

BufferCapabilities
caps)
throws
AWTException
```

Creates a new strategy for multi-buffering on this component with the
required buffer capabilities. This is useful, for example, if only
accelerated memory or page flipping is desired (as specified by the
buffer capabilities).

Each time this method
is called, the existing buffer strategy for this component is discarded.

**Parameters:** numBuffers

- number of buffers to create, including the front buffer
**Parameters:** caps

- the required capabilities for creating the buffer strategy;
cannot be

null
**Throws:** AWTException

- if the capabilities supplied could not be
supported or met; this may happen, for example, if there is not enough
accelerated memory currently available, or if page flipping is specified
but not possible.
**Throws:** IllegalArgumentException

- if numBuffers is less than 1, or if
caps is

null
**Since:** 1.4
**See Also:** getBufferStrategy()

- getBufferStrategy

```java
public
BufferStrategy
getBufferStrategy()
```

Returns the

BufferStrategy

used by this component. This
method will return null if a

BufferStrategy

has not yet
been created or has been disposed.

**Returns:** the buffer strategy used by this component
**Since:** 1.4
**See Also:** createBufferStrategy(int)

- setLocationByPlatform

```java
public void setLocationByPlatform​(boolean locationByPlatform)
```

Sets whether this Window should appear at the default location for the
native windowing system or at the current location (returned by

getLocation

) the next time the Window is made visible.
This behavior resembles a native window shown without programmatically
setting its location. Most windowing systems cascade windows if their
locations are not explicitly set. The actual location is determined once the
window is shown on the screen.

This behavior can also be enabled by setting the System Property
"java.awt.Window.locationByPlatform" to "true", though calls to this method
take precedence.

Calls to

setVisible

,

setLocation

and

setBounds

after calling

setLocationByPlatform

clear
this property of the Window.

For example, after the following code is executed:

```java
setLocationByPlatform(true);
setVisible(true);
boolean flag = isLocationByPlatform();
```

The window will be shown at platform's default location and

flag

will be

false

.

In the following sample:

```java
setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);
```

The window will be shown at (10, 10) and

flag

will be

false

.

**Parameters:** locationByPlatform

-

true

if this Window should appear
at the default location,

false

if at the current location
**Throws:** IllegalComponentStateException

- if the window
is showing on screen and locationByPlatform is

true

.
**Since:** 1.5
**See Also:** setLocation(int, int)

,

isShowing()

,

setVisible(boolean)

,

isLocationByPlatform()

,

System.getProperty(String)

- isLocationByPlatform

```java
public boolean isLocationByPlatform()
```

Returns

true

if this Window will appear at the default location
for the native windowing system the next time this Window is made visible.
This method always returns

false

if the Window is showing on the
screen.

**Returns:** whether this Window will appear at the default location
**Since:** 1.5
**See Also:** setLocationByPlatform(boolean)

,

isShowing()

- setBounds

```java
public void setBounds​(int x,
int y,
int width,
int height)
```

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

or

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setBounds

in class

Component
**Parameters:** x

- the new

x

-coordinate of this component
**Parameters:** y

- the new

y

-coordinate of this component
**Parameters:** width

- the new

width

of this component
**Parameters:** height

- the new

height

of this
component
**Since:** 1.6
**See Also:** Component.getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

setMinimumSize(java.awt.Dimension)

,

setLocationByPlatform(boolean)

,

isLocationByPlatform()

- setBounds

```java
public void setBounds​(
Rectangle
r)
```

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

r.width

or

r.height

values
will be automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setBounds

in class

Component
**Parameters:** r

- the new bounding rectangle for this component
**Since:** 1.6
**See Also:** Component.getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

setMinimumSize(java.awt.Dimension)

,

setLocationByPlatform(boolean)

,

isLocationByPlatform()

- getOpacity

```java
public float getOpacity()
```

Returns the opacity of the window.

**Returns:** the opacity of the window
**Since:** 1.7
**See Also:** setOpacity(float)

,

GraphicsDevice.WindowTranslucency

- setOpacity

```java
public void setOpacity​(float opacity)
```

Sets the opacity of the window.

The opacity value is in the range [0..1]. Note that setting the opacity
level of 0 may or may not disable the mouse event handling on this
window. This is a platform-dependent behavior.

The following conditions must be met in order to set the opacity value
less than

1.0f

:

- The

TRANSLUCENT

translucency must be supported by the underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested opacity value is less than

1.0f

, and any of the
above conditions are not met, the window opacity will not change,
and the

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
current shape of this window (see

setShape(Shape)

).

**Parameters:** opacity

- the opacity level to set to the window
**Throws:** IllegalArgumentException

- if the opacity is out of the range
[0..1]
**Throws:** IllegalComponentStateException

- if the window is decorated and
the opacity is less than

1.0f
**Throws:** IllegalComponentStateException

- if the window is in full screen
mode, and the opacity is less than

1.0f
**Throws:** UnsupportedOperationException

- if the

GraphicsDevice.WindowTranslucency#TRANSLUCENT TRANSLUCENT

translucency is not supported and the opacity is less than

1.0f
**Since:** 1.7
**See Also:** getOpacity()

,

setBackground(Color)

,

setShape(Shape)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

- getShape

```java
public
Shape
getShape()
```

Returns the shape of the window.

The value returned by this method may not be the same as
previously set with

setShape(shape)

, but it is guaranteed
to represent the same shape.

**Returns:** the shape of the window or

null

if no
shape is specified for the window
**Since:** 1.7
**See Also:** setShape(Shape)

,

GraphicsDevice.WindowTranslucency

- setShape

```java
public void setShape​(
Shape
shape)
```

Sets the shape of the window.

Setting a shape cuts off some parts of the window. Only the parts that
belong to the given

Shape

remain visible and clickable. If
the shape argument is

null

, this method restores the default
shape, making the window rectangular on most platforms.

The following conditions must be met to set a non-null shape:

- The

PERPIXEL_TRANSPARENT

translucency must be supported by the
underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested shape is not

null

, and any of the above
conditions are not met, the shape of this window will not change,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
opacity value (see

setOpacity(float)

). See

GraphicsDevice.WindowTranslucency

for more details.

**Parameters:** shape

- the shape to set to the window
**Throws:** IllegalComponentStateException

- if the shape is not

null

and the window is decorated
**Throws:** IllegalComponentStateException

- if the shape is not

null

and the window is in full-screen mode
**Throws:** UnsupportedOperationException

- if the shape is not

null

and

PERPIXEL_TRANSPARENT

translucency is not supported
**Since:** 1.7
**See Also:** getShape()

,

setBackground(Color)

,

setOpacity(float)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

- getBackground

```java
public
Color
getBackground()
```

Gets the background color of this window.

Note that the alpha component of the returned color indicates whether
the window is in the non-opaque (per-pixel translucent) mode.

**Overrides:** getBackground

in class

Component
**Returns:** this component's background color
**See Also:** setBackground(Color)

,

isOpaque()

,

GraphicsDevice.WindowTranslucency

- setBackground

```java
public void setBackground​(
Color
bgColor)
```

Sets the background color of this window.

If the windowing system supports the

PERPIXEL_TRANSLUCENT

translucency, the alpha component of the given background color
may effect the mode of operation for this window: it indicates whether
this window must be opaque (alpha equals

1.0f

) or per-pixel translucent
(alpha is less than

1.0f

). If the given background color is

null

, the window is considered completely opaque.

All the following conditions must be met to enable the per-pixel
transparency mode for this window:

- The

PERPIXEL_TRANSLUCENT

translucency must be supported by the graphics
device where this window is located

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the alpha component of the requested background color is less than

1.0f

, and any of the above conditions are not met, the background
color of this window will not change, the alpha component of the given
background color will not affect the mode of operation for this window,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

When the window is per-pixel translucent, the drawing sub-system
respects the alpha value of each individual pixel. If a pixel gets
painted with the alpha color component equal to zero, it becomes
visually transparent. If the alpha of the pixel is equal to 1.0f, the
pixel is fully opaque. Interim values of the alpha color component make
the pixel semi-transparent. In this mode, the background of the window
gets painted with the alpha value of the given background color. If the
alpha value of the argument of this method is equal to

0

, the
background is not painted at all.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

**Overrides:** setBackground

in class

Component
**Parameters:** bgColor

- the color to become this window's background color.
**Throws:** IllegalComponentStateException

- if the alpha value of the given
background color is less than

1.0f

and the window is decorated
**Throws:** IllegalComponentStateException

- if the alpha value of the given
background color is less than

1.0f

and the window is in
full-screen mode
**Throws:** UnsupportedOperationException

- if the alpha value of the given
background color is less than

1.0f

and

PERPIXEL_TRANSLUCENT

translucency is not supported
**See Also:** getBackground()

,

isOpaque()

,

setOpacity(float)

,

setShape(Shape)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

,

GraphicsConfiguration.isTranslucencyCapable()

- isOpaque

```java
public boolean isOpaque()
```

Indicates if the window is currently opaque.

The method returns

false

if the background color of the window
is not

null

and the alpha component of the color is less than

1.0f

. The method returns

true

otherwise.

**Overrides:** isOpaque

in class

Component
**Returns:** true

if the window is opaque,

false

otherwise
**Since:** 1.7
**See Also:** getBackground()

,

setBackground(Color)

- paint

```java
public void paint​(
Graphics
g)
```

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

**Overrides:** paint

in class

Container
**Parameters:** g

- the specified Graphics window
**Since:** 1.7
**See Also:** Component.update(Graphics)

Constructor Detail

- Window

```java
public Window​(
Frame
owner)
```

Constructs a new, initially invisible window with the specified

Frame

as its owner. The window will not be focusable
unless its owner is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a warning
banner is created.

**Parameters:** owner

- the

Frame

to act as owner or

null

if this window has no owner
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

,

isShowing()

- Window

```java
public Window​(
Window
owner)
```

Constructs a new, initially invisible window with the specified

Window

as its owner. This window will not be focusable
unless its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a
warning banner is created.

**Parameters:** owner

- the

Window

to act as owner or

null

if this window has no owner
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

,

isShowing()

- Window

```java
public Window​(
Window
owner,

GraphicsConfiguration
gc)
```

Constructs a new, initially invisible window with the specified owner

Window

and a

GraphicsConfiguration

of a screen device. The Window will not be focusable unless
its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

. If that
check fails with a

SecurityException

then a warning banner
is created.

**Parameters:** owner

- the window to act as owner or

null

if this window has no owner
**Parameters:** gc

- the

GraphicsConfiguration

of the target
screen device; if

gc

is

null

,
the system default

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

GraphicsConfiguration.getBounds()

,

isShowing()

---

#### Constructor Detail

Window

```java
public Window​(
Frame
owner)
```

Constructs a new, initially invisible window with the specified

Frame

as its owner. The window will not be focusable
unless its owner is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a warning
banner is created.

**Parameters:** owner

- the

Frame

to act as owner or

null

if this window has no owner
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

,

isShowing()

---

#### Window

public Window​(

Frame

owner)

Constructs a new, initially invisible window with the specified

Frame

as its owner. The window will not be focusable
unless its owner is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a warning
banner is created.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a warning
banner is created.

Window

```java
public Window​(
Window
owner)
```

Constructs a new, initially invisible window with the specified

Window

as its owner. This window will not be focusable
unless its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a
warning banner is created.

**Parameters:** owner

- the

Window

to act as owner or

null

if this window has no owner
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

,

isShowing()

---

#### Window

public Window​(

Window

owner)

Constructs a new, initially invisible window with the specified

Window

as its owner. This window will not be focusable
unless its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a
warning banner is created.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

.
If that check fails with a

SecurityException

then a
warning banner is created.

Window

```java
public Window​(
Window
owner,

GraphicsConfiguration
gc)
```

Constructs a new, initially invisible window with the specified owner

Window

and a

GraphicsConfiguration

of a screen device. The Window will not be focusable unless
its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

. If that
check fails with a

SecurityException

then a warning banner
is created.

**Parameters:** owner

- the window to act as owner or

null

if this window has no owner
**Parameters:** gc

- the

GraphicsConfiguration

of the target
screen device; if

gc

is

null

,
the system default

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

GraphicsConfiguration.getBounds()

,

isShowing()

---

#### Window

public Window​(

Window

owner,

GraphicsConfiguration

gc)

Constructs a new, initially invisible window with the specified owner

Window

and a

GraphicsConfiguration

of a screen device. The Window will not be focusable unless
its nearest owning

Frame

or

Dialog

is showing on the screen.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

. If that
check fails with a

SecurityException

then a warning banner
is created.

If there is a security manager set, it is invoked to check

AWTPermission("showWindowWithoutWarningBanner")

. If that
check fails with a

SecurityException

then a warning banner
is created.

Method Detail

- getIconImages

```java
public
List
<
Image
> getIconImages()
```

Returns the sequence of images to be displayed as the icon for this window.

This method returns a copy of the internally stored list, so all operations
on the returned object will not affect the window's behavior.

**Returns:** the copy of icon images' list for this window, or
empty list if this window doesn't have icon images.
**Since:** 1.6
**See Also:** setIconImages(java.util.List<? extends java.awt.Image>)

,

setIconImage(Image)

- setIconImages

```java
public void setIconImages​(
List
<? extends
Image
> icons)
```

Sets the sequence of images to be displayed as the icon
for this window. Subsequent calls to

getIconImages

will
always return a copy of the

icons

list.

Depending on the platform capabilities one or several images
of different dimensions will be used as the window's icon.

The

icons

list can contain

MultiResolutionImage

images also.
Suitable image depending on screen resolution is extracted from
base

MultiResolutionImage

image and added to the icons list
while base resolution image is removed from list.
The

icons

list is scanned for the images of most
appropriate dimensions from the beginning. If the list contains
several images of the same size, the first will be used.

Ownerless windows with no icon specified use platform-default icon.
The icon of an owned window may be inherited from the owner
unless explicitly overridden.
Setting the icon to

null

or empty list restores
the default behavior.

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

**Parameters:** icons

- the list of icon images to be displayed.
**Since:** 1.6
**See Also:** getIconImages()

,

setIconImage(Image)

- setIconImage

```java
public void setIconImage​(
Image
image)
```

Sets the image to be displayed as the icon for this window.

This method can be used instead of

setIconImages()

to specify a single image as a window's icon.

The following statement:

```java
setIconImage(image);
```

is equivalent to:

```java
ArrayList<Image> imageList = new ArrayList<Image>();
imageList.add(image);
setIconImages(imageList);
```

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

**Parameters:** image

- the icon image to be displayed.
**Since:** 1.6
**See Also:** setIconImages(java.util.List<? extends java.awt.Image>)

,

getIconImages()

- addNotify

```java
public void addNotify()
```

Makes this Window displayable by creating the connection to its
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Container
**Since:** 1.0
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

- pack

```java
public void pack()
```

Causes this Window to be sized to fit the preferred size
and layouts of its subcomponents. The resulting width and
height of the window are automatically enlarged if either
of dimensions is less than the minimum size as specified
by the previous call to the

setMinimumSize

method.

If the window and/or its owner are not displayable yet,
both of them are made displayable before calculating
the preferred size. The Window is validated after its
size is being calculated.

**See Also:** Component.isDisplayable()

,

setMinimumSize(java.awt.Dimension)

- setMinimumSize

```java
public void setMinimumSize​(
Dimension
minimumSize)
```

Sets the minimum size of this window to a constant
value. Subsequent calls to

getMinimumSize

will always return this value. If current window's
size is less than

minimumSize

the size of the
window is automatically enlarged to honor the minimum size.

If the

setSize

or

setBounds

methods
are called afterwards with a width or height less than
that was specified by the

setMinimumSize

method
the window is automatically enlarged to meet
the

minimumSize

value. The

minimumSize

value also affects the behaviour of the

pack

method.

The default behavior is restored by setting the minimum size
parameter to the

null

value.

Resizing operation may be restricted if the user tries
to resize window below the

minimumSize

value.
This behaviour is platform-dependent.

**Overrides:** setMinimumSize

in class

Component
**Parameters:** minimumSize

- the new minimum size of this window
**Since:** 1.6
**See Also:** Component.setMinimumSize(java.awt.Dimension)

,

Container.getMinimumSize()

,

Component.isMinimumSizeSet()

,

setSize(Dimension)

,

pack()

- setSize

```java
public void setSize​(
Dimension
d)
```

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

d.width

and

d.height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setSize

in class

Component
**Parameters:** d

- the dimension specifying the new size
of this component
**Since:** 1.6
**See Also:** Component.getSize()

,

setBounds(int, int, int, int)

,

setMinimumSize(java.awt.Dimension)

- setSize

```java
public void setSize​(int width,
int height)
```

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

and

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setSize

in class

Component
**Parameters:** width

- the new width of this component in pixels
**Parameters:** height

- the new height of this component in pixels
**Since:** 1.6
**See Also:** Component.getSize()

,

setBounds(int, int, int, int)

,

setMinimumSize(java.awt.Dimension)

- setLocation

```java
public void setLocation​(int x,
int y)
```

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setLocation

in class

Component
**Parameters:** x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Parameters:** y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space
**See Also:** Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

- setLocation

```java
public void setLocation​(
Point
p)
```

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setLocation

in class

Component
**Parameters:** p

- the point defining the top-left corner
of the new location, given in the coordinate space of this
component's parent
**See Also:** Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

- reshape

```java
@Deprecated

public void reshape​(int x,
int y,
int width,
int height)
```

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

Description copied from class:

Component

Reshapes the bounding rectangle for this component.

**Overrides:** reshape

in class

Component
**Parameters:** x

- the

x

coordinate of the upper left corner of the rectangle
**Parameters:** y

- the

y

coordinate of the upper left corner of the rectangle
**Parameters:** width

- the width of the rectangle
**Parameters:** height

- the height of the rectangle

- setVisible

```java
public void setVisible​(boolean b)
```

Shows or hides this

Window

depending on the value of parameter

b

.

If the method shows the window then the window is also made
focused under the following conditions:

- The

Window

meets the requirements outlined in the

isFocusableWindow()

method.

The

Window

's

autoRequestFocus

property is of the

true

value.

Native windowing system allows the

Window

to get focused.

There is an exception for the second condition (the value of the

autoRequestFocus

property). The property is not taken into account if the
window is a modal dialog, which blocks the currently focused window.

Developers must never assume that the window is the focused or active window
until it receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED event.

**Overrides:** setVisible

in class

Component
**Parameters:** b

- if

true

, makes the

Window

visible,
otherwise hides the

Window

.
If the

Window

and/or its owner
are not yet displayable, both are made displayable. The

Window

will be validated prior to being made visible.
If the

Window

is already visible, this will bring the

Window

to the front.

If

false

, hides this

Window

, its subcomponents, and all
of its owned children.
The

Window

and its subcomponents can be made visible again
with a call to

#setVisible(true)

.
**See Also:** Component.isDisplayable()

,

Component.setVisible(boolean)

,

toFront()

,

dispose()

,

setAutoRequestFocus(boolean)

,

isFocusableWindow()

- show

```java
@Deprecated

public void show()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Makes the Window visible. If the Window and/or its owner
are not yet displayable, both are made displayable. The
Window will be validated prior to being made visible.
If the Window is already visible, this will bring the Window
to the front.

**Overrides:** show

in class

Component
**See Also:** Component.isDisplayable()

,

toFront()

- hide

```java
@Deprecated

public void hide()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Hide this Window, its subcomponents, and all of its owned children.
The Window and its subcomponents can be made visible again
with a call to

show

.

**Overrides:** hide

in class

Component
**See Also:** show()

,

dispose()

- dispose

```java
public void dispose()
```

Releases all of the native screen resources used by this

Window

, its subcomponents, and all of its owned
children. That is, the resources for these

Component

s
will be destroyed, any memory they consume will be returned to the
OS, and they will be marked as undisplayable.

The

Window

and its subcomponents can be made displayable
again by rebuilding the native resources with a subsequent call to

pack

or

show

. The states of the recreated

Window

and its subcomponents will be identical to the
states of these objects at the point where the

Window

was disposed (not accounting for additional modifications between
those actions).

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**See Also:** Component.isDisplayable()

,

pack()

,

show()

- toFront

```java
public void toFront()
```

If this Window is visible, brings this Window to the front and may make
it the focused Window.

Places this Window at the top of the stacking order and shows it in
front of any other Windows in this VM. No action will take place if this
Window is not visible. Some platforms do not allow Windows which own
other Windows to appear on top of those owned Windows. Some platforms
may not permit this VM to place its Windows above windows of native
applications, or Windows of other VMs. This permission may depend on
whether a Window in this VM is already focused. Every attempt will be
made to move this Window as high as possible in the stacking order;
however, developers should not assume that this method will move this
Window above all other windows in every situation.

Developers must never assume that this Window is the focused or active
Window until this Window receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED
event. On platforms where the top-most window is the focused window, this
method will

probably

focus this Window (if it is not already focused)
under the following conditions:

- The window meets the requirements outlined in the

isFocusableWindow()

method.

The window's property

autoRequestFocus

is of the

true

value.

Native windowing system allows the window to get focused.

On platforms where the stacking order does not typically affect the focused
window, this method will

probably

leave the focused and active
Windows unchanged.

If this method causes this Window to be focused, and this Window is a
Frame or a Dialog, it will also become activated. If this Window is
focused, but it is not a Frame or a Dialog, then the first Frame or
Dialog that is an owner of this Window will be activated.

If this window is blocked by modal dialog, then the blocking dialog
is brought to the front and remains above the blocked window.

**See Also:** toBack()

,

setAutoRequestFocus(boolean)

,

isFocusableWindow()

- toBack

```java
public void toBack()
```

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

**See Also:** toFront()

- getToolkit

```java
public
Toolkit
getToolkit()
```

Returns the toolkit of this frame.

**Overrides:** getToolkit

in class

Component
**Returns:** the toolkit of this window.
**See Also:** Toolkit

,

Toolkit.getDefaultToolkit()

,

Component.getToolkit()

- getWarningString

```java
public final
String
getWarningString()
```

Gets the warning string that is displayed with this window.
If this window is insecure, the warning string is displayed
somewhere in the visible area of the window. A window is
insecure if there is a security manager and the security
manager denies

AWTPermission("showWindowWithoutWarningBanner")

.

If the window is secure, then

getWarningString

returns

null

. If the window is insecure, this
method checks for the system property

awt.appletWarning

and returns the string value of that property.

**Returns:** the warning string for this window.

- getLocale

```java
public
Locale
getLocale()
```

Gets the

Locale

object that is associated
with this window, if the locale has been set.
If no locale has been set, then the default locale
is returned.

**Overrides:** getLocale

in class

Component
**Returns:** the locale that is set for this window.
**Since:** 1.1
**See Also:** Locale

- getInputContext

```java
public
InputContext
getInputContext()
```

Gets the input context for this window. A window always has an input context,
which is shared by subcomponents unless they create and set their own.

**Overrides:** getInputContext

in class

Component
**Returns:** the input context used by this component;

null

if no context can be determined
**Since:** 1.2
**See Also:** Component.getInputContext()

- setCursor

```java
public void setCursor​(
Cursor
cursor)
```

Set the cursor image to a specified cursor.

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

class. If this parameter is null
then the cursor for this window will be set to the type
Cursor.DEFAULT_CURSOR.
**Since:** 1.1
**See Also:** Component.getCursor()

,

Cursor

- getOwner

```java
public
Window
getOwner()
```

Returns the owner of this window.

**Returns:** the owner of this window
**Since:** 1.2

- getOwnedWindows

```java
public
Window
[] getOwnedWindows()
```

Return an array containing all the windows this
window currently owns.

**Returns:** the array of all the owned windows
**Since:** 1.2

- getWindows

```java
public static
Window
[] getWindows()
```

Returns an array of all

Window

s, both owned and ownerless,
created by this application.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

**Returns:** the array of all the

Window

s created by the application
**Since:** 1.6
**See Also:** Frame.getFrames()

,

getOwnerlessWindows()

- getOwnerlessWindows

```java
public static
Window
[] getOwnerlessWindows()
```

Returns an array of all

Window

s created by this application
that have no owner. They include

Frame

s and ownerless

Dialog

s and

Window

s.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

**Returns:** the array of all the ownerless

Window

s
created by this application
**Since:** 1.6
**See Also:** Frame.getFrames()

,

getWindows()

- setModalExclusionType

```java
public void setModalExclusionType​(
Dialog.ModalExclusionType
exclusionType)
```

Specifies the modal exclusion type for this window. If a window is modal
excluded, it is not blocked by some modal dialogs. See

Dialog.ModalExclusionType

for
possible modal exclusion types.

If the given type is not supported,

NO_EXCLUDE

is used.

Note: changing the modal exclusion type for a visible window may have no
effect until it is hidden and then shown again.

**Parameters:** exclusionType

- the modal exclusion type for this window; a

null

value is equivalent to

NO_EXCLUDE
**Throws:** SecurityException

- if the calling thread does not have permission
to set the modal exclusion property to the window with the given

exclusionType
**Since:** 1.6
**See Also:** Dialog.ModalExclusionType

,

getModalExclusionType()

,

Toolkit.isModalExclusionTypeSupported(java.awt.Dialog.ModalExclusionType)

- getModalExclusionType

```java
public
Dialog.ModalExclusionType
getModalExclusionType()
```

Returns the modal exclusion type of this window.

**Returns:** the modal exclusion type of this window
**Since:** 1.6
**See Also:** Dialog.ModalExclusionType

,

setModalExclusionType(java.awt.Dialog.ModalExclusionType)

- addWindowListener

```java
public void addWindowListener​(
WindowListener
l)
```

Adds the specified window listener to receive window events from
this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window listener
**See Also:** removeWindowListener(java.awt.event.WindowListener)

,

getWindowListeners()

- addWindowStateListener

```java
public void addWindowStateListener​(
WindowStateListener
l)
```

Adds the specified window state listener to receive window
events from this window. If

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window state listener
**Since:** 1.4
**See Also:** removeWindowStateListener(java.awt.event.WindowStateListener)

,

getWindowStateListeners()

- addWindowFocusListener

```java
public void addWindowFocusListener​(
WindowFocusListener
l)
```

Adds the specified window focus listener to receive window events
from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window focus listener
**Since:** 1.4
**See Also:** removeWindowFocusListener(java.awt.event.WindowFocusListener)

,

getWindowFocusListeners()

- removeWindowListener

```java
public void removeWindowListener​(
WindowListener
l)
```

Removes the specified window listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window listener
**See Also:** addWindowListener(java.awt.event.WindowListener)

,

getWindowListeners()

- removeWindowStateListener

```java
public void removeWindowStateListener​(
WindowStateListener
l)
```

Removes the specified window state listener so that it no
longer receives window events from this window. If

l

is

null

, no exception is thrown and
no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window state listener
**Since:** 1.4
**See Also:** addWindowStateListener(java.awt.event.WindowStateListener)

,

getWindowStateListeners()

- removeWindowFocusListener

```java
public void removeWindowFocusListener​(
WindowFocusListener
l)
```

Removes the specified window focus listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window focus listener
**Since:** 1.4
**See Also:** addWindowFocusListener(java.awt.event.WindowFocusListener)

,

getWindowFocusListeners()

- getWindowListeners

```java
public
WindowListener
[] getWindowListeners()
```

Returns an array of all the window listeners
registered on this window.

**Returns:** all of this window's

WindowListener

s
or an empty array if no window
listeners are currently registered
**Since:** 1.4
**See Also:** addWindowListener(java.awt.event.WindowListener)

,

removeWindowListener(java.awt.event.WindowListener)

- getWindowFocusListeners

```java
public
WindowFocusListener
[] getWindowFocusListeners()
```

Returns an array of all the window focus listeners
registered on this window.

**Returns:** all of this window's

WindowFocusListener

s
or an empty array if no window focus
listeners are currently registered
**Since:** 1.4
**See Also:** addWindowFocusListener(java.awt.event.WindowFocusListener)

,

removeWindowFocusListener(java.awt.event.WindowFocusListener)

- getWindowStateListeners

```java
public
WindowStateListener
[] getWindowStateListeners()
```

Returns an array of all the window state listeners
registered on this window.

**Returns:** all of this window's

WindowStateListener

s
or an empty array if no window state
listeners are currently registered
**Since:** 1.4
**See Also:** addWindowStateListener(java.awt.event.WindowStateListener)

,

removeWindowStateListener(java.awt.event.WindowStateListener)

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Window

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Window w

for its window listeners with the following code:

```java
WindowListener[] wls = (WindowListener[])(w.getListeners(WindowListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Container
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this window,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Throws:** NullPointerException

- if

listenerType

is

null
**Since:** 1.3
**See Also:** getWindowListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this window. If the event is an

WindowEvent

, it invokes the

processWindowEvent

method, else it invokes its
superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Container
**Parameters:** e

- the event
**See Also:** Component.processComponentEvent(java.awt.event.ComponentEvent)

,

Component.processFocusEvent(java.awt.event.FocusEvent)

,

Component.processKeyEvent(java.awt.event.KeyEvent)

,

Component.processMouseEvent(java.awt.event.MouseEvent)

,

Component.processMouseMotionEvent(java.awt.event.MouseEvent)

,

Component.processInputMethodEvent(java.awt.event.InputMethodEvent)

,

Component.processHierarchyEvent(java.awt.event.HierarchyEvent)

,

Component.processMouseWheelEvent(java.awt.event.MouseWheelEvent)

- processWindowEvent

```java
protected void processWindowEvent​(
WindowEvent
e)
```

Processes window events occurring on this window by
dispatching them to any registered WindowListener objects.
NOTE: This method will not be called unless window events
are enabled for this component; this happens when one of the
following occurs:

- A WindowListener object is registered via

addWindowListener

Window events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the window event
**See Also:** Component.enableEvents(long)

- processWindowFocusEvent

```java
protected void processWindowFocusEvent​(
WindowEvent
e)
```

Processes window focus event occurring on this window by
dispatching them to any registered WindowFocusListener objects.
NOTE: this method will not be called unless window focus events
are enabled for this window. This happens when one of the
following occurs:

- a WindowFocusListener is registered via

addWindowFocusListener

Window focus events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the window focus event
**Since:** 1.4
**See Also:** Component.enableEvents(long)

- processWindowStateEvent

```java
protected void processWindowStateEvent​(
WindowEvent
e)
```

Processes window state event occurring on this window by
dispatching them to any registered

WindowStateListener

objects.
NOTE: this method will not be called unless window state events
are enabled for this window. This happens when one of the
following occurs:

- a

WindowStateListener

is registered via

addWindowStateListener

window state events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the window state event
**Since:** 1.4
**See Also:** Component.enableEvents(long)

- setAlwaysOnTop

```java
public final void setAlwaysOnTop​(boolean alwaysOnTop)
throws
SecurityException
```

Sets whether this window should always be above other windows. If
there are multiple always-on-top windows, their relative order is
unspecified and platform dependent.

If some other window is already always-on-top then the
relative order between these windows is unspecified (depends on
platform). No window can be brought to be over the always-on-top
window except maybe another always-on-top window.

All windows owned by an always-on-top window inherit this state and
automatically become always-on-top. If a window ceases to be
always-on-top, the windows that it owns will no longer be
always-on-top. When an always-on-top window is sent

toBack

, its always-on-top state is set to

false

.

When this method is called on a window with a value of

true

, and the window is visible and the platform
supports always-on-top for this window, the window is immediately
brought forward, "sticking" it in the top-most position. If the
window isn`t currently visible, this method sets the always-on-top
state to

true

but does not bring the window forward.
When the window is later shown, it will be always-on-top.

When this method is called on a window with a value of

false

the always-on-top state is set to normal. It may also
cause an unspecified, platform-dependent change in the z-order of
top-level windows, but other always-on-top windows will remain in
top-most position. Calling this method with a value of

false

on a window that has a normal state has no effect.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

**Parameters:** alwaysOnTop

- true if the window should always be above other
windows
**Throws:** SecurityException

- if the calling thread does not have
permission to set the value of always-on-top property
**Since:** 1.5
**See Also:** isAlwaysOnTop()

,

toFront()

,

toBack()

,

AWTPermission

,

isAlwaysOnTopSupported()

,

getToolkit()

,

Toolkit.isAlwaysOnTopSupported()

- isAlwaysOnTopSupported

```java
public boolean isAlwaysOnTopSupported()
```

Returns whether the always-on-top mode is supported for this
window. Some platforms may not support always-on-top windows, some
may support only some kinds of top-level windows; for example,
a platform may not support always-on-top modal dialogs.

**Returns:** true

, if the always-on-top mode is supported for
this window and this window's toolkit supports always-on-top windows,

false

otherwise
**Since:** 1.6
**See Also:** setAlwaysOnTop(boolean)

,

getToolkit()

,

Toolkit.isAlwaysOnTopSupported()

- isAlwaysOnTop

```java
public final boolean isAlwaysOnTop()
```

Returns whether this window is an always-on-top window.

**Returns:** true

, if the window is in always-on-top state,

false

otherwise
**Since:** 1.5
**See Also:** setAlwaysOnTop(boolean)

- getFocusOwner

```java
public
Component
getFocusOwner()
```

Returns the child Component of this Window that has focus if this Window
is focused; returns null otherwise.

**Returns:** the child Component with focus, or null if this Window is not
focused
**See Also:** getMostRecentFocusOwner()

,

isFocused()

- getMostRecentFocusOwner

```java
public
Component
getMostRecentFocusOwner()
```

Returns the child Component of this Window that will receive the focus
when this Window is focused. If this Window is currently focused, this
method returns the same Component as

getFocusOwner()

. If
this Window is not focused, then the child Component that most recently
requested focus will be returned. If no child Component has ever
requested focus, and this is a focusable Window, then this Window's
initial focusable Component is returned. If no child Component has ever
requested focus, and this is a non-focusable Window, null is returned.

**Returns:** the child Component that will receive focus when this Window is
focused
**Since:** 1.4
**See Also:** getFocusOwner()

,

isFocused()

,

isFocusableWindow()

- isActive

```java
public boolean isActive()
```

Returns whether this Window is active. Only a Frame or a Dialog may be
active. The native windowing system may denote the active Window or its
children with special decorations, such as a highlighted title bar. The
active Window is always either the focused Window, or the first Frame or
Dialog that is an owner of the focused Window.

**Returns:** whether this is the active Window.
**Since:** 1.4
**See Also:** isFocused()

- isFocused

```java
public boolean isFocused()
```

Returns whether this Window is focused. If there exists a focus owner,
the focused Window is the Window that is, or contains, that focus owner.
If there is no focus owner, then no Window is focused.

If the focused Window is a Frame or a Dialog it is also the active
Window. Otherwise, the active Window is the first Frame or Dialog that
is an owner of the focused Window.

**Returns:** whether this is the focused Window.
**Since:** 1.4
**See Also:** isActive()

- getFocusTraversalKeys

```java
public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)
```

Gets a focus traversal key for this Window. (See

setFocusTraversalKeys

for a full description of each key.)

If the traversal key has not been explicitly set for this Window,
then this Window's parent's traversal key is returned. If the
traversal key has not been explicitly set for any of this Window's
ancestors, then the current KeyboardFocusManager's default traversal key
is returned.

**Overrides:** getFocusTraversalKeys

in class

Container
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Returns:** the AWTKeyStroke for the specified key
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4
**See Also:** Container.setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

- setFocusCycleRoot

```java
public final void setFocusCycleRoot​(boolean focusCycleRoot)
```

Does nothing because Windows must always be roots of a focus traversal
cycle. The passed-in value is ignored.

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

because all Windows must be roots of a
focus traversal cycle.

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
public final
Container
getFocusCycleRootAncestor()
```

Always returns

null

because Windows have no ancestors; they
represent the top of the Component hierarchy.

**Overrides:** getFocusCycleRootAncestor

in class

Component
**Returns:** null
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

- isFocusableWindow

```java
public final boolean isFocusableWindow()
```

Returns whether this Window can become the focused Window, that is,
whether this Window or any of its subcomponents can become the focus
owner. For a Frame or Dialog to be focusable, its focusable Window state
must be set to

true

. For a Window which is not a Frame or
Dialog to be focusable, its focusable Window state must be set to

true

, its nearest owning Frame or Dialog must be
showing on the screen, and it must contain at least one Component in
its focus traversal cycle. If any of these conditions is not met, then
neither this Window nor any of its subcomponents can become the focus
owner.

**Returns:** true

if this Window can be the focused Window;

false

otherwise
**Since:** 1.4
**See Also:** getFocusableWindowState()

,

setFocusableWindowState(boolean)

,

isShowing()

,

Component.isFocusable()

- getFocusableWindowState

```java
public boolean getFocusableWindowState()
```

Returns whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this method returns

false

, then

isFocusableWindow

will return

false

as well.
If this method returns

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

By default, all Windows have a focusable Window state of

true

.

**Returns:** whether this Window can be the focused Window
**Since:** 1.4
**See Also:** isFocusableWindow()

,

setFocusableWindowState(boolean)

,

isShowing()

,

Component.setFocusable(boolean)

- setFocusableWindowState

```java
public void setFocusableWindowState​(boolean focusableWindowState)
```

Sets whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this Window's focusable Window state is set to

false

, then

isFocusableWindow

will return

false

. If this
Window's focusable Window state is set to

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

Setting a Window's focusability state to

false

is the
standard mechanism for an application to identify to the AWT a Window
which will be used as a floating palette or toolbar, and thus should be
a non-focusable Window.

Setting the focusability state on a visible

Window

can have a delayed effect on some platforms — the actual
change may happen only when the

Window

becomes
hidden and then visible again. To ensure consistent behavior
across platforms, set the

Window

's focusable state
when the

Window

is invisible and then show it.

**Parameters:** focusableWindowState

- whether this Window can be the focused
Window
**Since:** 1.4
**See Also:** isFocusableWindow()

,

getFocusableWindowState()

,

isShowing()

,

Component.setFocusable(boolean)

- setAutoRequestFocus

```java
public void setAutoRequestFocus​(boolean autoRequestFocus)
```

Sets whether this window should receive focus on
subsequently being shown (with a call to

setVisible(true)

),
or being moved to the front (with a call to

toFront()

).

Note that

setVisible(true)

may be called indirectly
(e.g. when showing an owner of the window makes the window to be shown).

toFront()

may also be called indirectly (e.g. when

setVisible(true)

is called on already visible window).
In all such cases this property takes effect as well.

The value of the property is not inherited by owned windows.

**Parameters:** autoRequestFocus

- whether this window should be focused on
subsequently being shown or being moved to the front
**Since:** 1.7
**See Also:** isAutoRequestFocus()

,

isFocusableWindow()

,

setVisible(boolean)

,

toFront()

- isAutoRequestFocus

```java
public boolean isAutoRequestFocus()
```

Returns whether this window should receive focus on subsequently being shown
(with a call to

setVisible(true)

), or being moved to the front
(with a call to

toFront()

).

By default, the window has

autoRequestFocus

value of

true

.

**Returns:** autoRequestFocus

value
**Since:** 1.7
**See Also:** setAutoRequestFocus(boolean)

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Container
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

,

addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Container
**Parameters:** propertyName

- one of the property names listed above
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

- isValidateRoot

```java
public boolean isValidateRoot()
```

Indicates if this container is a validate root.

Window

objects are the validate roots, and, therefore, they
override this method to return

true

.

**Overrides:** isValidateRoot

in class

Container
**Returns:** true
**Since:** 1.7
**See Also:** Container.isValidateRoot()

- postEvent

```java
@Deprecated

public boolean postEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1
replaced by

dispatchEvent(AWTEvent)

.

Description copied from interface:

MenuContainer

Posts an event to the listeners.

**Specified by:** postEvent

in interface

MenuContainer
**Overrides:** postEvent

in class

Component
**Parameters:** e

- the event to dispatch
**Returns:** the results of posting the event

- isShowing

```java
public boolean isShowing()
```

Checks if this Window is showing on screen.

**Overrides:** isShowing

in class

Component
**Returns:** true

if the component is showing,

false

otherwise
**See Also:** Component.setVisible(boolean)

- applyResourceBundle

```java
@Deprecated

public void applyResourceBundle​(
ResourceBundle
rb)
```

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

**Parameters:** rb

- the resource bundle

- applyResourceBundle

```java
@Deprecated

public void applyResourceBundle​(
String
rbName)
```

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

**Parameters:** rbName

- the resource name

- setType

```java
public void setType​(
Window.Type
type)
```

Sets the type of the window.

This method can only be called while the window is not displayable.

**Parameters:** type

- the window type
**Throws:** IllegalComponentStateException

- if the window
is displayable.
**Throws:** IllegalArgumentException

- if the type is

null
**Since:** 1.7
**See Also:** Component.isDisplayable()

,

getType()

- getType

```java
public
Window.Type
getType()
```

Returns the type of the window.

**Returns:** the type of the window
**Since:** 1.7
**See Also:** setType(java.awt.Window.Type)

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Window.
For windows, the AccessibleContext takes the form of an
AccessibleAWTWindow.
A new AccessibleAWTWindow instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleAWTWindow that serves as the
AccessibleContext of this Window
**Since:** 1.3

- setLocationRelativeTo

```java
public void setLocationRelativeTo​(
Component
c)
```

Sets the location of the window relative to the specified
component according to the following scenarios.

The target screen mentioned below is a screen to which
the window should be placed after the setLocationRelativeTo
method is called.

- If the component is

null

, or the

GraphicsConfiguration

associated with this component is

null

, the window is placed in the center of the
screen. The center point can be obtained with the

GraphicsEnvironment.getCenterPoint

method.

If the component is not

null

, but it is not
currently showing, the window is placed in the center of
the target screen defined by the

GraphicsConfiguration

associated with this component.

If the component is not

null

and is shown on
the screen, then the window is located in such a way that
the center of the window coincides with the center of the
component.

If the screens configuration does not allow the window to
be moved from one screen to another, then the window is
only placed at the location determined according to the
above conditions and its

GraphicsConfiguration

is
not changed.

Note

: If the lower edge of the window is out of the screen,
then the window is placed to the side of the

Component

that is closest to the center of the screen. So if the
component is on the right part of the screen, the window
is placed to its left, and vice versa.

If after the window location has been calculated, the upper,
left, or right edge of the window is out of the screen,
then the window is located in such a way that the upper,
left, or right edge of the window coincides with the
corresponding edge of the screen. If both left and right
edges of the window are out of the screen, the window is
placed at the left side of the screen. The similar placement
will occur if both top and bottom edges are out of the screen.
In that case, the window is placed at the top side of the screen.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Parameters:** c

- the component in relation to which the window's location
is determined
**Since:** 1.4
**See Also:** GraphicsEnvironment.getCenterPoint()

- createBufferStrategy

```java
public void createBufferStrategy​(int numBuffers)
```

Creates a new strategy for multi-buffering on this component.
Multi-buffering is useful for rendering performance. This method
attempts to create the best strategy available with the number of
buffers supplied. It will always create a

BufferStrategy

with that number of buffers.
A page-flipping strategy is attempted first, then a blitting strategy
using accelerated buffers. Finally, an unaccelerated blitting
strategy is used.

Each time this method is called,
the existing buffer strategy for this component is discarded.

**Parameters:** numBuffers

- number of buffers to create
**Throws:** IllegalArgumentException

- if numBuffers is less than 1.
**Throws:** IllegalStateException

- if the component is not displayable
**Since:** 1.4
**See Also:** Component.isDisplayable()

,

getBufferStrategy()

- createBufferStrategy

```java
public void createBufferStrategy​(int numBuffers,

BufferCapabilities
caps)
throws
AWTException
```

Creates a new strategy for multi-buffering on this component with the
required buffer capabilities. This is useful, for example, if only
accelerated memory or page flipping is desired (as specified by the
buffer capabilities).

Each time this method
is called, the existing buffer strategy for this component is discarded.

**Parameters:** numBuffers

- number of buffers to create, including the front buffer
**Parameters:** caps

- the required capabilities for creating the buffer strategy;
cannot be

null
**Throws:** AWTException

- if the capabilities supplied could not be
supported or met; this may happen, for example, if there is not enough
accelerated memory currently available, or if page flipping is specified
but not possible.
**Throws:** IllegalArgumentException

- if numBuffers is less than 1, or if
caps is

null
**Since:** 1.4
**See Also:** getBufferStrategy()

- getBufferStrategy

```java
public
BufferStrategy
getBufferStrategy()
```

Returns the

BufferStrategy

used by this component. This
method will return null if a

BufferStrategy

has not yet
been created or has been disposed.

**Returns:** the buffer strategy used by this component
**Since:** 1.4
**See Also:** createBufferStrategy(int)

- setLocationByPlatform

```java
public void setLocationByPlatform​(boolean locationByPlatform)
```

Sets whether this Window should appear at the default location for the
native windowing system or at the current location (returned by

getLocation

) the next time the Window is made visible.
This behavior resembles a native window shown without programmatically
setting its location. Most windowing systems cascade windows if their
locations are not explicitly set. The actual location is determined once the
window is shown on the screen.

This behavior can also be enabled by setting the System Property
"java.awt.Window.locationByPlatform" to "true", though calls to this method
take precedence.

Calls to

setVisible

,

setLocation

and

setBounds

after calling

setLocationByPlatform

clear
this property of the Window.

For example, after the following code is executed:

```java
setLocationByPlatform(true);
setVisible(true);
boolean flag = isLocationByPlatform();
```

The window will be shown at platform's default location and

flag

will be

false

.

In the following sample:

```java
setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);
```

The window will be shown at (10, 10) and

flag

will be

false

.

**Parameters:** locationByPlatform

-

true

if this Window should appear
at the default location,

false

if at the current location
**Throws:** IllegalComponentStateException

- if the window
is showing on screen and locationByPlatform is

true

.
**Since:** 1.5
**See Also:** setLocation(int, int)

,

isShowing()

,

setVisible(boolean)

,

isLocationByPlatform()

,

System.getProperty(String)

- isLocationByPlatform

```java
public boolean isLocationByPlatform()
```

Returns

true

if this Window will appear at the default location
for the native windowing system the next time this Window is made visible.
This method always returns

false

if the Window is showing on the
screen.

**Returns:** whether this Window will appear at the default location
**Since:** 1.5
**See Also:** setLocationByPlatform(boolean)

,

isShowing()

- setBounds

```java
public void setBounds​(int x,
int y,
int width,
int height)
```

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

or

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setBounds

in class

Component
**Parameters:** x

- the new

x

-coordinate of this component
**Parameters:** y

- the new

y

-coordinate of this component
**Parameters:** width

- the new

width

of this component
**Parameters:** height

- the new

height

of this
component
**Since:** 1.6
**See Also:** Component.getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

setMinimumSize(java.awt.Dimension)

,

setLocationByPlatform(boolean)

,

isLocationByPlatform()

- setBounds

```java
public void setBounds​(
Rectangle
r)
```

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

r.width

or

r.height

values
will be automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setBounds

in class

Component
**Parameters:** r

- the new bounding rectangle for this component
**Since:** 1.6
**See Also:** Component.getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

setMinimumSize(java.awt.Dimension)

,

setLocationByPlatform(boolean)

,

isLocationByPlatform()

- getOpacity

```java
public float getOpacity()
```

Returns the opacity of the window.

**Returns:** the opacity of the window
**Since:** 1.7
**See Also:** setOpacity(float)

,

GraphicsDevice.WindowTranslucency

- setOpacity

```java
public void setOpacity​(float opacity)
```

Sets the opacity of the window.

The opacity value is in the range [0..1]. Note that setting the opacity
level of 0 may or may not disable the mouse event handling on this
window. This is a platform-dependent behavior.

The following conditions must be met in order to set the opacity value
less than

1.0f

:

- The

TRANSLUCENT

translucency must be supported by the underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested opacity value is less than

1.0f

, and any of the
above conditions are not met, the window opacity will not change,
and the

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
current shape of this window (see

setShape(Shape)

).

**Parameters:** opacity

- the opacity level to set to the window
**Throws:** IllegalArgumentException

- if the opacity is out of the range
[0..1]
**Throws:** IllegalComponentStateException

- if the window is decorated and
the opacity is less than

1.0f
**Throws:** IllegalComponentStateException

- if the window is in full screen
mode, and the opacity is less than

1.0f
**Throws:** UnsupportedOperationException

- if the

GraphicsDevice.WindowTranslucency#TRANSLUCENT TRANSLUCENT

translucency is not supported and the opacity is less than

1.0f
**Since:** 1.7
**See Also:** getOpacity()

,

setBackground(Color)

,

setShape(Shape)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

- getShape

```java
public
Shape
getShape()
```

Returns the shape of the window.

The value returned by this method may not be the same as
previously set with

setShape(shape)

, but it is guaranteed
to represent the same shape.

**Returns:** the shape of the window or

null

if no
shape is specified for the window
**Since:** 1.7
**See Also:** setShape(Shape)

,

GraphicsDevice.WindowTranslucency

- setShape

```java
public void setShape​(
Shape
shape)
```

Sets the shape of the window.

Setting a shape cuts off some parts of the window. Only the parts that
belong to the given

Shape

remain visible and clickable. If
the shape argument is

null

, this method restores the default
shape, making the window rectangular on most platforms.

The following conditions must be met to set a non-null shape:

- The

PERPIXEL_TRANSPARENT

translucency must be supported by the
underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested shape is not

null

, and any of the above
conditions are not met, the shape of this window will not change,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
opacity value (see

setOpacity(float)

). See

GraphicsDevice.WindowTranslucency

for more details.

**Parameters:** shape

- the shape to set to the window
**Throws:** IllegalComponentStateException

- if the shape is not

null

and the window is decorated
**Throws:** IllegalComponentStateException

- if the shape is not

null

and the window is in full-screen mode
**Throws:** UnsupportedOperationException

- if the shape is not

null

and

PERPIXEL_TRANSPARENT

translucency is not supported
**Since:** 1.7
**See Also:** getShape()

,

setBackground(Color)

,

setOpacity(float)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

- getBackground

```java
public
Color
getBackground()
```

Gets the background color of this window.

Note that the alpha component of the returned color indicates whether
the window is in the non-opaque (per-pixel translucent) mode.

**Overrides:** getBackground

in class

Component
**Returns:** this component's background color
**See Also:** setBackground(Color)

,

isOpaque()

,

GraphicsDevice.WindowTranslucency

- setBackground

```java
public void setBackground​(
Color
bgColor)
```

Sets the background color of this window.

If the windowing system supports the

PERPIXEL_TRANSLUCENT

translucency, the alpha component of the given background color
may effect the mode of operation for this window: it indicates whether
this window must be opaque (alpha equals

1.0f

) or per-pixel translucent
(alpha is less than

1.0f

). If the given background color is

null

, the window is considered completely opaque.

All the following conditions must be met to enable the per-pixel
transparency mode for this window:

- The

PERPIXEL_TRANSLUCENT

translucency must be supported by the graphics
device where this window is located

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the alpha component of the requested background color is less than

1.0f

, and any of the above conditions are not met, the background
color of this window will not change, the alpha component of the given
background color will not affect the mode of operation for this window,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

When the window is per-pixel translucent, the drawing sub-system
respects the alpha value of each individual pixel. If a pixel gets
painted with the alpha color component equal to zero, it becomes
visually transparent. If the alpha of the pixel is equal to 1.0f, the
pixel is fully opaque. Interim values of the alpha color component make
the pixel semi-transparent. In this mode, the background of the window
gets painted with the alpha value of the given background color. If the
alpha value of the argument of this method is equal to

0

, the
background is not painted at all.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

**Overrides:** setBackground

in class

Component
**Parameters:** bgColor

- the color to become this window's background color.
**Throws:** IllegalComponentStateException

- if the alpha value of the given
background color is less than

1.0f

and the window is decorated
**Throws:** IllegalComponentStateException

- if the alpha value of the given
background color is less than

1.0f

and the window is in
full-screen mode
**Throws:** UnsupportedOperationException

- if the alpha value of the given
background color is less than

1.0f

and

PERPIXEL_TRANSLUCENT

translucency is not supported
**See Also:** getBackground()

,

isOpaque()

,

setOpacity(float)

,

setShape(Shape)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

,

GraphicsConfiguration.isTranslucencyCapable()

- isOpaque

```java
public boolean isOpaque()
```

Indicates if the window is currently opaque.

The method returns

false

if the background color of the window
is not

null

and the alpha component of the color is less than

1.0f

. The method returns

true

otherwise.

**Overrides:** isOpaque

in class

Component
**Returns:** true

if the window is opaque,

false

otherwise
**Since:** 1.7
**See Also:** getBackground()

,

setBackground(Color)

- paint

```java
public void paint​(
Graphics
g)
```

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

**Overrides:** paint

in class

Container
**Parameters:** g

- the specified Graphics window
**Since:** 1.7
**See Also:** Component.update(Graphics)

---

#### Method Detail

getIconImages

```java
public
List
<
Image
> getIconImages()
```

Returns the sequence of images to be displayed as the icon for this window.

This method returns a copy of the internally stored list, so all operations
on the returned object will not affect the window's behavior.

**Returns:** the copy of icon images' list for this window, or
empty list if this window doesn't have icon images.
**Since:** 1.6
**See Also:** setIconImages(java.util.List<? extends java.awt.Image>)

,

setIconImage(Image)

---

#### getIconImages

public

List

<

Image

> getIconImages()

Returns the sequence of images to be displayed as the icon for this window.

This method returns a copy of the internally stored list, so all operations
on the returned object will not affect the window's behavior.

This method returns a copy of the internally stored list, so all operations
on the returned object will not affect the window's behavior.

setIconImages

```java
public void setIconImages​(
List
<? extends
Image
> icons)
```

Sets the sequence of images to be displayed as the icon
for this window. Subsequent calls to

getIconImages

will
always return a copy of the

icons

list.

Depending on the platform capabilities one or several images
of different dimensions will be used as the window's icon.

The

icons

list can contain

MultiResolutionImage

images also.
Suitable image depending on screen resolution is extracted from
base

MultiResolutionImage

image and added to the icons list
while base resolution image is removed from list.
The

icons

list is scanned for the images of most
appropriate dimensions from the beginning. If the list contains
several images of the same size, the first will be used.

Ownerless windows with no icon specified use platform-default icon.
The icon of an owned window may be inherited from the owner
unless explicitly overridden.
Setting the icon to

null

or empty list restores
the default behavior.

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

**Parameters:** icons

- the list of icon images to be displayed.
**Since:** 1.6
**See Also:** getIconImages()

,

setIconImage(Image)

---

#### setIconImages

public void setIconImages​(

List

<? extends

Image

> icons)

Sets the sequence of images to be displayed as the icon
for this window. Subsequent calls to

getIconImages

will
always return a copy of the

icons

list.

Depending on the platform capabilities one or several images
of different dimensions will be used as the window's icon.

The

icons

list can contain

MultiResolutionImage

images also.
Suitable image depending on screen resolution is extracted from
base

MultiResolutionImage

image and added to the icons list
while base resolution image is removed from list.
The

icons

list is scanned for the images of most
appropriate dimensions from the beginning. If the list contains
several images of the same size, the first will be used.

Ownerless windows with no icon specified use platform-default icon.
The icon of an owned window may be inherited from the owner
unless explicitly overridden.
Setting the icon to

null

or empty list restores
the default behavior.

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

Depending on the platform capabilities one or several images
of different dimensions will be used as the window's icon.

The

icons

list can contain

MultiResolutionImage

images also.
Suitable image depending on screen resolution is extracted from
base

MultiResolutionImage

image and added to the icons list
while base resolution image is removed from list.
The

icons

list is scanned for the images of most
appropriate dimensions from the beginning. If the list contains
several images of the same size, the first will be used.

Ownerless windows with no icon specified use platform-default icon.
The icon of an owned window may be inherited from the owner
unless explicitly overridden.
Setting the icon to

null

or empty list restores
the default behavior.

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

The

icons

list can contain

MultiResolutionImage

images also.
Suitable image depending on screen resolution is extracted from
base

MultiResolutionImage

image and added to the icons list
while base resolution image is removed from list.
The

icons

list is scanned for the images of most
appropriate dimensions from the beginning. If the list contains
several images of the same size, the first will be used.

Ownerless windows with no icon specified use platform-default icon.
The icon of an owned window may be inherited from the owner
unless explicitly overridden.
Setting the icon to

null

or empty list restores
the default behavior.

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

Ownerless windows with no icon specified use platform-default icon.
The icon of an owned window may be inherited from the owner
unless explicitly overridden.
Setting the icon to

null

or empty list restores
the default behavior.

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

setIconImage

```java
public void setIconImage​(
Image
image)
```

Sets the image to be displayed as the icon for this window.

This method can be used instead of

setIconImages()

to specify a single image as a window's icon.

The following statement:

```java
setIconImage(image);
```

is equivalent to:

```java
ArrayList<Image> imageList = new ArrayList<Image>();
imageList.add(image);
setIconImages(imageList);
```

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

**Parameters:** image

- the icon image to be displayed.
**Since:** 1.6
**See Also:** setIconImages(java.util.List<? extends java.awt.Image>)

,

getIconImages()

---

#### setIconImage

public void setIconImage​(

Image

image)

Sets the image to be displayed as the icon for this window.

This method can be used instead of

setIconImages()

to specify a single image as a window's icon.

The following statement:

```java
setIconImage(image);
```

is equivalent to:

```java
ArrayList<Image> imageList = new ArrayList<Image>();
imageList.add(image);
setIconImages(imageList);
```

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

This method can be used instead of

setIconImages()

to specify a single image as a window's icon.

The following statement:

```java
setIconImage(image);
```

is equivalent to:

```java
ArrayList<Image> imageList = new ArrayList<Image>();
imageList.add(image);
setIconImages(imageList);
```

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

The following statement:

```java
setIconImage(image);
```

is equivalent to:

```java
ArrayList<Image> imageList = new ArrayList<Image>();
imageList.add(image);
setIconImages(imageList);
```

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

setIconImage(image);

ArrayList<Image> imageList = new ArrayList<Image>();
imageList.add(image);
setIconImages(imageList);

Note : Native windowing systems may use different images of differing
dimensions to represent a window, depending on the context (e.g.
window decoration, window list, taskbar, etc.). They could also use
just a single image for all contexts or no image at all.

addNotify

```java
public void addNotify()
```

Makes this Window displayable by creating the connection to its
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Container
**Since:** 1.0
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

---

#### addNotify

public void addNotify()

Makes this Window displayable by creating the connection to its
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

pack

```java
public void pack()
```

Causes this Window to be sized to fit the preferred size
and layouts of its subcomponents. The resulting width and
height of the window are automatically enlarged if either
of dimensions is less than the minimum size as specified
by the previous call to the

setMinimumSize

method.

If the window and/or its owner are not displayable yet,
both of them are made displayable before calculating
the preferred size. The Window is validated after its
size is being calculated.

**See Also:** Component.isDisplayable()

,

setMinimumSize(java.awt.Dimension)

---

#### pack

public void pack()

Causes this Window to be sized to fit the preferred size
and layouts of its subcomponents. The resulting width and
height of the window are automatically enlarged if either
of dimensions is less than the minimum size as specified
by the previous call to the

setMinimumSize

method.

If the window and/or its owner are not displayable yet,
both of them are made displayable before calculating
the preferred size. The Window is validated after its
size is being calculated.

If the window and/or its owner are not displayable yet,
both of them are made displayable before calculating
the preferred size. The Window is validated after its
size is being calculated.

setMinimumSize

```java
public void setMinimumSize​(
Dimension
minimumSize)
```

Sets the minimum size of this window to a constant
value. Subsequent calls to

getMinimumSize

will always return this value. If current window's
size is less than

minimumSize

the size of the
window is automatically enlarged to honor the minimum size.

If the

setSize

or

setBounds

methods
are called afterwards with a width or height less than
that was specified by the

setMinimumSize

method
the window is automatically enlarged to meet
the

minimumSize

value. The

minimumSize

value also affects the behaviour of the

pack

method.

The default behavior is restored by setting the minimum size
parameter to the

null

value.

Resizing operation may be restricted if the user tries
to resize window below the

minimumSize

value.
This behaviour is platform-dependent.

**Overrides:** setMinimumSize

in class

Component
**Parameters:** minimumSize

- the new minimum size of this window
**Since:** 1.6
**See Also:** Component.setMinimumSize(java.awt.Dimension)

,

Container.getMinimumSize()

,

Component.isMinimumSizeSet()

,

setSize(Dimension)

,

pack()

---

#### setMinimumSize

public void setMinimumSize​(

Dimension

minimumSize)

Sets the minimum size of this window to a constant
value. Subsequent calls to

getMinimumSize

will always return this value. If current window's
size is less than

minimumSize

the size of the
window is automatically enlarged to honor the minimum size.

If the

setSize

or

setBounds

methods
are called afterwards with a width or height less than
that was specified by the

setMinimumSize

method
the window is automatically enlarged to meet
the

minimumSize

value. The

minimumSize

value also affects the behaviour of the

pack

method.

The default behavior is restored by setting the minimum size
parameter to the

null

value.

Resizing operation may be restricted if the user tries
to resize window below the

minimumSize

value.
This behaviour is platform-dependent.

If the

setSize

or

setBounds

methods
are called afterwards with a width or height less than
that was specified by the

setMinimumSize

method
the window is automatically enlarged to meet
the

minimumSize

value. The

minimumSize

value also affects the behaviour of the

pack

method.

The default behavior is restored by setting the minimum size
parameter to the

null

value.

Resizing operation may be restricted if the user tries
to resize window below the

minimumSize

value.
This behaviour is platform-dependent.

The default behavior is restored by setting the minimum size
parameter to the

null

value.

Resizing operation may be restricted if the user tries
to resize window below the

minimumSize

value.
This behaviour is platform-dependent.

Resizing operation may be restricted if the user tries
to resize window below the

minimumSize

value.
This behaviour is platform-dependent.

setSize

```java
public void setSize​(
Dimension
d)
```

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

d.width

and

d.height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setSize

in class

Component
**Parameters:** d

- the dimension specifying the new size
of this component
**Since:** 1.6
**See Also:** Component.getSize()

,

setBounds(int, int, int, int)

,

setMinimumSize(java.awt.Dimension)

---

#### setSize

public void setSize​(

Dimension

d)

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

d.width

and

d.height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

d.width

and

d.height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The

d.width

and

d.height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

setSize

```java
public void setSize​(int width,
int height)
```

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

and

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setSize

in class

Component
**Parameters:** width

- the new width of this component in pixels
**Parameters:** height

- the new height of this component in pixels
**Since:** 1.6
**See Also:** Component.getSize()

,

setBounds(int, int, int, int)

,

setMinimumSize(java.awt.Dimension)

---

#### setSize

public void setSize​(int width,
int height)

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

and

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

and

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The

width

and

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

setLocation

```java
public void setLocation​(int x,
int y)
```

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setLocation

in class

Component
**Parameters:** x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Parameters:** y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space
**See Also:** Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

---

#### setLocation

public void setLocation​(int x,
int y)

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

setLocation

```java
public void setLocation​(
Point
p)
```

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setLocation

in class

Component
**Parameters:** p

- the point defining the top-left corner
of the new location, given in the coordinate space of this
component's parent
**See Also:** Component.getLocation()

,

Component.setBounds(int, int, int, int)

,

Component.invalidate()

---

#### setLocation

public void setLocation​(

Point

p)

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

reshape

```java
@Deprecated

public void reshape​(int x,
int y,
int width,
int height)
```

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

Description copied from class:

Component

Reshapes the bounding rectangle for this component.

**Overrides:** reshape

in class

Component
**Parameters:** x

- the

x

coordinate of the upper left corner of the rectangle
**Parameters:** y

- the

y

coordinate of the upper left corner of the rectangle
**Parameters:** width

- the width of the rectangle
**Parameters:** height

- the height of the rectangle

---

#### reshape

@Deprecated

public void reshape​(int x,
int y,
int width,
int height)

Description copied from class:

Component

Reshapes the bounding rectangle for this component.

setVisible

```java
public void setVisible​(boolean b)
```

Shows or hides this

Window

depending on the value of parameter

b

.

If the method shows the window then the window is also made
focused under the following conditions:

- The

Window

meets the requirements outlined in the

isFocusableWindow()

method.

The

Window

's

autoRequestFocus

property is of the

true

value.

Native windowing system allows the

Window

to get focused.

There is an exception for the second condition (the value of the

autoRequestFocus

property). The property is not taken into account if the
window is a modal dialog, which blocks the currently focused window.

Developers must never assume that the window is the focused or active window
until it receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED event.

**Overrides:** setVisible

in class

Component
**Parameters:** b

- if

true

, makes the

Window

visible,
otherwise hides the

Window

.
If the

Window

and/or its owner
are not yet displayable, both are made displayable. The

Window

will be validated prior to being made visible.
If the

Window

is already visible, this will bring the

Window

to the front.

If

false

, hides this

Window

, its subcomponents, and all
of its owned children.
The

Window

and its subcomponents can be made visible again
with a call to

#setVisible(true)

.
**See Also:** Component.isDisplayable()

,

Component.setVisible(boolean)

,

toFront()

,

dispose()

,

setAutoRequestFocus(boolean)

,

isFocusableWindow()

---

#### setVisible

public void setVisible​(boolean b)

Shows or hides this

Window

depending on the value of parameter

b

.

If the method shows the window then the window is also made
focused under the following conditions:

- The

Window

meets the requirements outlined in the

isFocusableWindow()

method.

The

Window

's

autoRequestFocus

property is of the

true

value.

Native windowing system allows the

Window

to get focused.

There is an exception for the second condition (the value of the

autoRequestFocus

property). The property is not taken into account if the
window is a modal dialog, which blocks the currently focused window.

Developers must never assume that the window is the focused or active window
until it receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED event.

If the method shows the window then the window is also made
focused under the following conditions:

- The

Window

meets the requirements outlined in the

isFocusableWindow()

method.

The

Window

's

autoRequestFocus

property is of the

true

value.

Native windowing system allows the

Window

to get focused.

There is an exception for the second condition (the value of the

autoRequestFocus

property). The property is not taken into account if the
window is a modal dialog, which blocks the currently focused window.

Developers must never assume that the window is the focused or active window
until it receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED event.

The

Window

meets the requirements outlined in the

isFocusableWindow()

method.

The

Window

's

autoRequestFocus

property is of the

true

value.

Native windowing system allows the

Window

to get focused.

Developers must never assume that the window is the focused or active window
until it receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED event.

If

false

, hides this

Window

, its subcomponents, and all
of its owned children.
The

Window

and its subcomponents can be made visible again
with a call to

#setVisible(true)

.

show

```java
@Deprecated

public void show()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Makes the Window visible. If the Window and/or its owner
are not yet displayable, both are made displayable. The
Window will be validated prior to being made visible.
If the Window is already visible, this will bring the Window
to the front.

**Overrides:** show

in class

Component
**See Also:** Component.isDisplayable()

,

toFront()

---

#### show

@Deprecated

public void show()

Makes the Window visible. If the Window and/or its owner
are not yet displayable, both are made displayable. The
Window will be validated prior to being made visible.
If the Window is already visible, this will bring the Window
to the front.

hide

```java
@Deprecated

public void hide()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Hide this Window, its subcomponents, and all of its owned children.
The Window and its subcomponents can be made visible again
with a call to

show

.

**Overrides:** hide

in class

Component
**See Also:** show()

,

dispose()

---

#### hide

@Deprecated

public void hide()

Hide this Window, its subcomponents, and all of its owned children.
The Window and its subcomponents can be made visible again
with a call to

show

.

dispose

```java
public void dispose()
```

Releases all of the native screen resources used by this

Window

, its subcomponents, and all of its owned
children. That is, the resources for these

Component

s
will be destroyed, any memory they consume will be returned to the
OS, and they will be marked as undisplayable.

The

Window

and its subcomponents can be made displayable
again by rebuilding the native resources with a subsequent call to

pack

or

show

. The states of the recreated

Window

and its subcomponents will be identical to the
states of these objects at the point where the

Window

was disposed (not accounting for additional modifications between
those actions).

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**See Also:** Component.isDisplayable()

,

pack()

,

show()

---

#### dispose

public void dispose()

Releases all of the native screen resources used by this

Window

, its subcomponents, and all of its owned
children. That is, the resources for these

Component

s
will be destroyed, any memory they consume will be returned to the
OS, and they will be marked as undisplayable.

The

Window

and its subcomponents can be made displayable
again by rebuilding the native resources with a subsequent call to

pack

or

show

. The states of the recreated

Window

and its subcomponents will be identical to the
states of these objects at the point where the

Window

was disposed (not accounting for additional modifications between
those actions).

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

The

Window

and its subcomponents can be made displayable
again by rebuilding the native resources with a subsequent call to

pack

or

show

. The states of the recreated

Window

and its subcomponents will be identical to the
states of these objects at the point where the

Window

was disposed (not accounting for additional modifications between
those actions).

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

toFront

```java
public void toFront()
```

If this Window is visible, brings this Window to the front and may make
it the focused Window.

Places this Window at the top of the stacking order and shows it in
front of any other Windows in this VM. No action will take place if this
Window is not visible. Some platforms do not allow Windows which own
other Windows to appear on top of those owned Windows. Some platforms
may not permit this VM to place its Windows above windows of native
applications, or Windows of other VMs. This permission may depend on
whether a Window in this VM is already focused. Every attempt will be
made to move this Window as high as possible in the stacking order;
however, developers should not assume that this method will move this
Window above all other windows in every situation.

Developers must never assume that this Window is the focused or active
Window until this Window receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED
event. On platforms where the top-most window is the focused window, this
method will

probably

focus this Window (if it is not already focused)
under the following conditions:

- The window meets the requirements outlined in the

isFocusableWindow()

method.

The window's property

autoRequestFocus

is of the

true

value.

Native windowing system allows the window to get focused.

On platforms where the stacking order does not typically affect the focused
window, this method will

probably

leave the focused and active
Windows unchanged.

If this method causes this Window to be focused, and this Window is a
Frame or a Dialog, it will also become activated. If this Window is
focused, but it is not a Frame or a Dialog, then the first Frame or
Dialog that is an owner of this Window will be activated.

If this window is blocked by modal dialog, then the blocking dialog
is brought to the front and remains above the blocked window.

**See Also:** toBack()

,

setAutoRequestFocus(boolean)

,

isFocusableWindow()

---

#### toFront

public void toFront()

If this Window is visible, brings this Window to the front and may make
it the focused Window.

Places this Window at the top of the stacking order and shows it in
front of any other Windows in this VM. No action will take place if this
Window is not visible. Some platforms do not allow Windows which own
other Windows to appear on top of those owned Windows. Some platforms
may not permit this VM to place its Windows above windows of native
applications, or Windows of other VMs. This permission may depend on
whether a Window in this VM is already focused. Every attempt will be
made to move this Window as high as possible in the stacking order;
however, developers should not assume that this method will move this
Window above all other windows in every situation.

Developers must never assume that this Window is the focused or active
Window until this Window receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED
event. On platforms where the top-most window is the focused window, this
method will

probably

focus this Window (if it is not already focused)
under the following conditions:

- The window meets the requirements outlined in the

isFocusableWindow()

method.

The window's property

autoRequestFocus

is of the

true

value.

Native windowing system allows the window to get focused.

On platforms where the stacking order does not typically affect the focused
window, this method will

probably

leave the focused and active
Windows unchanged.

If this method causes this Window to be focused, and this Window is a
Frame or a Dialog, it will also become activated. If this Window is
focused, but it is not a Frame or a Dialog, then the first Frame or
Dialog that is an owner of this Window will be activated.

If this window is blocked by modal dialog, then the blocking dialog
is brought to the front and remains above the blocked window.

Places this Window at the top of the stacking order and shows it in
front of any other Windows in this VM. No action will take place if this
Window is not visible. Some platforms do not allow Windows which own
other Windows to appear on top of those owned Windows. Some platforms
may not permit this VM to place its Windows above windows of native
applications, or Windows of other VMs. This permission may depend on
whether a Window in this VM is already focused. Every attempt will be
made to move this Window as high as possible in the stacking order;
however, developers should not assume that this method will move this
Window above all other windows in every situation.

Developers must never assume that this Window is the focused or active
Window until this Window receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED
event. On platforms where the top-most window is the focused window, this
method will

probably

focus this Window (if it is not already focused)
under the following conditions:

- The window meets the requirements outlined in the

isFocusableWindow()

method.

The window's property

autoRequestFocus

is of the

true

value.

Native windowing system allows the window to get focused.

On platforms where the stacking order does not typically affect the focused
window, this method will

probably

leave the focused and active
Windows unchanged.

If this method causes this Window to be focused, and this Window is a
Frame or a Dialog, it will also become activated. If this Window is
focused, but it is not a Frame or a Dialog, then the first Frame or
Dialog that is an owner of this Window will be activated.

If this window is blocked by modal dialog, then the blocking dialog
is brought to the front and remains above the blocked window.

Developers must never assume that this Window is the focused or active
Window until this Window receives a WINDOW_GAINED_FOCUS or WINDOW_ACTIVATED
event. On platforms where the top-most window is the focused window, this
method will

probably

focus this Window (if it is not already focused)
under the following conditions:

- The window meets the requirements outlined in the

isFocusableWindow()

method.

The window's property

autoRequestFocus

is of the

true

value.

Native windowing system allows the window to get focused.

On platforms where the stacking order does not typically affect the focused
window, this method will

probably

leave the focused and active
Windows unchanged.

If this method causes this Window to be focused, and this Window is a
Frame or a Dialog, it will also become activated. If this Window is
focused, but it is not a Frame or a Dialog, then the first Frame or
Dialog that is an owner of this Window will be activated.

If this window is blocked by modal dialog, then the blocking dialog
is brought to the front and remains above the blocked window.

The window meets the requirements outlined in the

isFocusableWindow()

method.

The window's property

autoRequestFocus

is of the

true

value.

Native windowing system allows the window to get focused.

If this method causes this Window to be focused, and this Window is a
Frame or a Dialog, it will also become activated. If this Window is
focused, but it is not a Frame or a Dialog, then the first Frame or
Dialog that is an owner of this Window will be activated.

If this window is blocked by modal dialog, then the blocking dialog
is brought to the front and remains above the blocked window.

If this window is blocked by modal dialog, then the blocking dialog
is brought to the front and remains above the blocked window.

toBack

```java
public void toBack()
```

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

**See Also:** toFront()

---

#### toBack

public void toBack()

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

getToolkit

```java
public
Toolkit
getToolkit()
```

Returns the toolkit of this frame.

**Overrides:** getToolkit

in class

Component
**Returns:** the toolkit of this window.
**See Also:** Toolkit

,

Toolkit.getDefaultToolkit()

,

Component.getToolkit()

---

#### getToolkit

public

Toolkit

getToolkit()

Returns the toolkit of this frame.

getWarningString

```java
public final
String
getWarningString()
```

Gets the warning string that is displayed with this window.
If this window is insecure, the warning string is displayed
somewhere in the visible area of the window. A window is
insecure if there is a security manager and the security
manager denies

AWTPermission("showWindowWithoutWarningBanner")

.

If the window is secure, then

getWarningString

returns

null

. If the window is insecure, this
method checks for the system property

awt.appletWarning

and returns the string value of that property.

**Returns:** the warning string for this window.

---

#### getWarningString

public final

String

getWarningString()

Gets the warning string that is displayed with this window.
If this window is insecure, the warning string is displayed
somewhere in the visible area of the window. A window is
insecure if there is a security manager and the security
manager denies

AWTPermission("showWindowWithoutWarningBanner")

.

If the window is secure, then

getWarningString

returns

null

. If the window is insecure, this
method checks for the system property

awt.appletWarning

and returns the string value of that property.

If the window is secure, then

getWarningString

returns

null

. If the window is insecure, this
method checks for the system property

awt.appletWarning

and returns the string value of that property.

getLocale

```java
public
Locale
getLocale()
```

Gets the

Locale

object that is associated
with this window, if the locale has been set.
If no locale has been set, then the default locale
is returned.

**Overrides:** getLocale

in class

Component
**Returns:** the locale that is set for this window.
**Since:** 1.1
**See Also:** Locale

---

#### getLocale

public

Locale

getLocale()

Gets the

Locale

object that is associated
with this window, if the locale has been set.
If no locale has been set, then the default locale
is returned.

getInputContext

```java
public
InputContext
getInputContext()
```

Gets the input context for this window. A window always has an input context,
which is shared by subcomponents unless they create and set their own.

**Overrides:** getInputContext

in class

Component
**Returns:** the input context used by this component;

null

if no context can be determined
**Since:** 1.2
**See Also:** Component.getInputContext()

---

#### getInputContext

public

InputContext

getInputContext()

Gets the input context for this window. A window always has an input context,
which is shared by subcomponents unless they create and set their own.

setCursor

```java
public void setCursor​(
Cursor
cursor)
```

Set the cursor image to a specified cursor.

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

class. If this parameter is null
then the cursor for this window will be set to the type
Cursor.DEFAULT_CURSOR.
**Since:** 1.1
**See Also:** Component.getCursor()

,

Cursor

---

#### setCursor

public void setCursor​(

Cursor

cursor)

Set the cursor image to a specified cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

getOwner

```java
public
Window
getOwner()
```

Returns the owner of this window.

**Returns:** the owner of this window
**Since:** 1.2

---

#### getOwner

public

Window

getOwner()

Returns the owner of this window.

getOwnedWindows

```java
public
Window
[] getOwnedWindows()
```

Return an array containing all the windows this
window currently owns.

**Returns:** the array of all the owned windows
**Since:** 1.2

---

#### getOwnedWindows

public

Window

[] getOwnedWindows()

Return an array containing all the windows this
window currently owns.

getWindows

```java
public static
Window
[] getWindows()
```

Returns an array of all

Window

s, both owned and ownerless,
created by this application.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

**Returns:** the array of all the

Window

s created by the application
**Since:** 1.6
**See Also:** Frame.getFrames()

,

getOwnerlessWindows()

---

#### getWindows

public static

Window

[] getWindows()

Returns an array of all

Window

s, both owned and ownerless,
created by this application.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

getOwnerlessWindows

```java
public static
Window
[] getOwnerlessWindows()
```

Returns an array of all

Window

s created by this application
that have no owner. They include

Frame

s and ownerless

Dialog

s and

Window

s.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

**Returns:** the array of all the ownerless

Window

s
created by this application
**Since:** 1.6
**See Also:** Frame.getFrames()

,

getWindows()

---

#### getOwnerlessWindows

public static

Window

[] getOwnerlessWindows()

Returns an array of all

Window

s created by this application
that have no owner. They include

Frame

s and ownerless

Dialog

s and

Window

s.
If called from an applet, the array includes only the

Window

s
accessible by that applet.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

Warning:

this method may return system created windows, such
as a print dialog. Applications should not assume the existence of
these dialogs, nor should an application assume anything about these
dialogs such as component positions,

LayoutManager

s
or serialization.

setModalExclusionType

```java
public void setModalExclusionType​(
Dialog.ModalExclusionType
exclusionType)
```

Specifies the modal exclusion type for this window. If a window is modal
excluded, it is not blocked by some modal dialogs. See

Dialog.ModalExclusionType

for
possible modal exclusion types.

If the given type is not supported,

NO_EXCLUDE

is used.

Note: changing the modal exclusion type for a visible window may have no
effect until it is hidden and then shown again.

**Parameters:** exclusionType

- the modal exclusion type for this window; a

null

value is equivalent to

NO_EXCLUDE
**Throws:** SecurityException

- if the calling thread does not have permission
to set the modal exclusion property to the window with the given

exclusionType
**Since:** 1.6
**See Also:** Dialog.ModalExclusionType

,

getModalExclusionType()

,

Toolkit.isModalExclusionTypeSupported(java.awt.Dialog.ModalExclusionType)

---

#### setModalExclusionType

public void setModalExclusionType​(

Dialog.ModalExclusionType

exclusionType)

Specifies the modal exclusion type for this window. If a window is modal
excluded, it is not blocked by some modal dialogs. See

Dialog.ModalExclusionType

for
possible modal exclusion types.

If the given type is not supported,

NO_EXCLUDE

is used.

Note: changing the modal exclusion type for a visible window may have no
effect until it is hidden and then shown again.

If the given type is not supported,

NO_EXCLUDE

is used.

Note: changing the modal exclusion type for a visible window may have no
effect until it is hidden and then shown again.

Note: changing the modal exclusion type for a visible window may have no
effect until it is hidden and then shown again.

getModalExclusionType

```java
public
Dialog.ModalExclusionType
getModalExclusionType()
```

Returns the modal exclusion type of this window.

**Returns:** the modal exclusion type of this window
**Since:** 1.6
**See Also:** Dialog.ModalExclusionType

,

setModalExclusionType(java.awt.Dialog.ModalExclusionType)

---

#### getModalExclusionType

public

Dialog.ModalExclusionType

getModalExclusionType()

Returns the modal exclusion type of this window.

addWindowListener

```java
public void addWindowListener​(
WindowListener
l)
```

Adds the specified window listener to receive window events from
this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window listener
**See Also:** removeWindowListener(java.awt.event.WindowListener)

,

getWindowListeners()

---

#### addWindowListener

public void addWindowListener​(

WindowListener

l)

Adds the specified window listener to receive window events from
this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

addWindowStateListener

```java
public void addWindowStateListener​(
WindowStateListener
l)
```

Adds the specified window state listener to receive window
events from this window. If

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window state listener
**Since:** 1.4
**See Also:** removeWindowStateListener(java.awt.event.WindowStateListener)

,

getWindowStateListeners()

---

#### addWindowStateListener

public void addWindowStateListener​(

WindowStateListener

l)

Adds the specified window state listener to receive window
events from this window. If

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

addWindowFocusListener

```java
public void addWindowFocusListener​(
WindowFocusListener
l)
```

Adds the specified window focus listener to receive window events
from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window focus listener
**Since:** 1.4
**See Also:** removeWindowFocusListener(java.awt.event.WindowFocusListener)

,

getWindowFocusListeners()

---

#### addWindowFocusListener

public void addWindowFocusListener​(

WindowFocusListener

l)

Adds the specified window focus listener to receive window events
from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeWindowListener

```java
public void removeWindowListener​(
WindowListener
l)
```

Removes the specified window listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window listener
**See Also:** addWindowListener(java.awt.event.WindowListener)

,

getWindowListeners()

---

#### removeWindowListener

public void removeWindowListener​(

WindowListener

l)

Removes the specified window listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeWindowStateListener

```java
public void removeWindowStateListener​(
WindowStateListener
l)
```

Removes the specified window state listener so that it no
longer receives window events from this window. If

l

is

null

, no exception is thrown and
no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window state listener
**Since:** 1.4
**See Also:** addWindowStateListener(java.awt.event.WindowStateListener)

,

getWindowStateListeners()

---

#### removeWindowStateListener

public void removeWindowStateListener​(

WindowStateListener

l)

Removes the specified window state listener so that it no
longer receives window events from this window. If

l

is

null

, no exception is thrown and
no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeWindowFocusListener

```java
public void removeWindowFocusListener​(
WindowFocusListener
l)
```

Removes the specified window focus listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the window focus listener
**Since:** 1.4
**See Also:** addWindowFocusListener(java.awt.event.WindowFocusListener)

,

getWindowFocusListeners()

---

#### removeWindowFocusListener

public void removeWindowFocusListener​(

WindowFocusListener

l)

Removes the specified window focus listener so that it no longer
receives window events from this window.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getWindowListeners

```java
public
WindowListener
[] getWindowListeners()
```

Returns an array of all the window listeners
registered on this window.

**Returns:** all of this window's

WindowListener

s
or an empty array if no window
listeners are currently registered
**Since:** 1.4
**See Also:** addWindowListener(java.awt.event.WindowListener)

,

removeWindowListener(java.awt.event.WindowListener)

---

#### getWindowListeners

public

WindowListener

[] getWindowListeners()

Returns an array of all the window listeners
registered on this window.

getWindowFocusListeners

```java
public
WindowFocusListener
[] getWindowFocusListeners()
```

Returns an array of all the window focus listeners
registered on this window.

**Returns:** all of this window's

WindowFocusListener

s
or an empty array if no window focus
listeners are currently registered
**Since:** 1.4
**See Also:** addWindowFocusListener(java.awt.event.WindowFocusListener)

,

removeWindowFocusListener(java.awt.event.WindowFocusListener)

---

#### getWindowFocusListeners

public

WindowFocusListener

[] getWindowFocusListeners()

Returns an array of all the window focus listeners
registered on this window.

getWindowStateListeners

```java
public
WindowStateListener
[] getWindowStateListeners()
```

Returns an array of all the window state listeners
registered on this window.

**Returns:** all of this window's

WindowStateListener

s
or an empty array if no window state
listeners are currently registered
**Since:** 1.4
**See Also:** addWindowStateListener(java.awt.event.WindowStateListener)

,

removeWindowStateListener(java.awt.event.WindowStateListener)

---

#### getWindowStateListeners

public

WindowStateListener

[] getWindowStateListeners()

Returns an array of all the window state listeners
registered on this window.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Window

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Window w

for its window listeners with the following code:

```java
WindowListener[] wls = (WindowListener[])(w.getListeners(WindowListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Container
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this window,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Throws:** NullPointerException

- if

listenerType

is

null
**Since:** 1.3
**See Also:** getWindowListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Window

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Window w

for its window listeners with the following code:

```java
WindowListener[] wls = (WindowListener[])(w.getListeners(WindowListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Window w

for its window listeners with the following code:

```java
WindowListener[] wls = (WindowListener[])(w.getListeners(WindowListener.class));
```

If no such listeners exist, this method returns an empty array.

WindowListener[] wls = (WindowListener[])(w.getListeners(WindowListener.class));

processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this window. If the event is an

WindowEvent

, it invokes the

processWindowEvent

method, else it invokes its
superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Container
**Parameters:** e

- the event
**See Also:** Component.processComponentEvent(java.awt.event.ComponentEvent)

,

Component.processFocusEvent(java.awt.event.FocusEvent)

,

Component.processKeyEvent(java.awt.event.KeyEvent)

,

Component.processMouseEvent(java.awt.event.MouseEvent)

,

Component.processMouseMotionEvent(java.awt.event.MouseEvent)

,

Component.processInputMethodEvent(java.awt.event.InputMethodEvent)

,

Component.processHierarchyEvent(java.awt.event.HierarchyEvent)

,

Component.processMouseWheelEvent(java.awt.event.MouseWheelEvent)

---

#### processEvent

protected void processEvent​(

AWTEvent

e)

Processes events on this window. If the event is an

WindowEvent

, it invokes the

processWindowEvent

method, else it invokes its
superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processWindowEvent

```java
protected void processWindowEvent​(
WindowEvent
e)
```

Processes window events occurring on this window by
dispatching them to any registered WindowListener objects.
NOTE: This method will not be called unless window events
are enabled for this component; this happens when one of the
following occurs:

- A WindowListener object is registered via

addWindowListener

Window events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the window event
**See Also:** Component.enableEvents(long)

---

#### processWindowEvent

protected void processWindowEvent​(

WindowEvent

e)

Processes window events occurring on this window by
dispatching them to any registered WindowListener objects.
NOTE: This method will not be called unless window events
are enabled for this component; this happens when one of the
following occurs:

- A WindowListener object is registered via

addWindowListener

Window events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

A WindowListener object is registered via

addWindowListener

Window events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processWindowFocusEvent

```java
protected void processWindowFocusEvent​(
WindowEvent
e)
```

Processes window focus event occurring on this window by
dispatching them to any registered WindowFocusListener objects.
NOTE: this method will not be called unless window focus events
are enabled for this window. This happens when one of the
following occurs:

- a WindowFocusListener is registered via

addWindowFocusListener

Window focus events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the window focus event
**Since:** 1.4
**See Also:** Component.enableEvents(long)

---

#### processWindowFocusEvent

protected void processWindowFocusEvent​(

WindowEvent

e)

Processes window focus event occurring on this window by
dispatching them to any registered WindowFocusListener objects.
NOTE: this method will not be called unless window focus events
are enabled for this window. This happens when one of the
following occurs:

- a WindowFocusListener is registered via

addWindowFocusListener

Window focus events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

a WindowFocusListener is registered via

addWindowFocusListener

Window focus events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processWindowStateEvent

```java
protected void processWindowStateEvent​(
WindowEvent
e)
```

Processes window state event occurring on this window by
dispatching them to any registered

WindowStateListener

objects.
NOTE: this method will not be called unless window state events
are enabled for this window. This happens when one of the
following occurs:

- a

WindowStateListener

is registered via

addWindowStateListener

window state events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the window state event
**Since:** 1.4
**See Also:** Component.enableEvents(long)

---

#### processWindowStateEvent

protected void processWindowStateEvent​(

WindowEvent

e)

Processes window state event occurring on this window by
dispatching them to any registered

WindowStateListener

objects.
NOTE: this method will not be called unless window state events
are enabled for this window. This happens when one of the
following occurs:

- a

WindowStateListener

is registered via

addWindowStateListener

window state events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

a

WindowStateListener

is registered via

addWindowStateListener

window state events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

setAlwaysOnTop

```java
public final void setAlwaysOnTop​(boolean alwaysOnTop)
throws
SecurityException
```

Sets whether this window should always be above other windows. If
there are multiple always-on-top windows, their relative order is
unspecified and platform dependent.

If some other window is already always-on-top then the
relative order between these windows is unspecified (depends on
platform). No window can be brought to be over the always-on-top
window except maybe another always-on-top window.

All windows owned by an always-on-top window inherit this state and
automatically become always-on-top. If a window ceases to be
always-on-top, the windows that it owns will no longer be
always-on-top. When an always-on-top window is sent

toBack

, its always-on-top state is set to

false

.

When this method is called on a window with a value of

true

, and the window is visible and the platform
supports always-on-top for this window, the window is immediately
brought forward, "sticking" it in the top-most position. If the
window isn`t currently visible, this method sets the always-on-top
state to

true

but does not bring the window forward.
When the window is later shown, it will be always-on-top.

When this method is called on a window with a value of

false

the always-on-top state is set to normal. It may also
cause an unspecified, platform-dependent change in the z-order of
top-level windows, but other always-on-top windows will remain in
top-most position. Calling this method with a value of

false

on a window that has a normal state has no effect.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

**Parameters:** alwaysOnTop

- true if the window should always be above other
windows
**Throws:** SecurityException

- if the calling thread does not have
permission to set the value of always-on-top property
**Since:** 1.5
**See Also:** isAlwaysOnTop()

,

toFront()

,

toBack()

,

AWTPermission

,

isAlwaysOnTopSupported()

,

getToolkit()

,

Toolkit.isAlwaysOnTopSupported()

---

#### setAlwaysOnTop

public final void setAlwaysOnTop​(boolean alwaysOnTop)
throws

SecurityException

Sets whether this window should always be above other windows. If
there are multiple always-on-top windows, their relative order is
unspecified and platform dependent.

If some other window is already always-on-top then the
relative order between these windows is unspecified (depends on
platform). No window can be brought to be over the always-on-top
window except maybe another always-on-top window.

All windows owned by an always-on-top window inherit this state and
automatically become always-on-top. If a window ceases to be
always-on-top, the windows that it owns will no longer be
always-on-top. When an always-on-top window is sent

toBack

, its always-on-top state is set to

false

.

When this method is called on a window with a value of

true

, and the window is visible and the platform
supports always-on-top for this window, the window is immediately
brought forward, "sticking" it in the top-most position. If the
window isn`t currently visible, this method sets the always-on-top
state to

true

but does not bring the window forward.
When the window is later shown, it will be always-on-top.

When this method is called on a window with a value of

false

the always-on-top state is set to normal. It may also
cause an unspecified, platform-dependent change in the z-order of
top-level windows, but other always-on-top windows will remain in
top-most position. Calling this method with a value of

false

on a window that has a normal state has no effect.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

If some other window is already always-on-top then the
relative order between these windows is unspecified (depends on
platform). No window can be brought to be over the always-on-top
window except maybe another always-on-top window.

All windows owned by an always-on-top window inherit this state and
automatically become always-on-top. If a window ceases to be
always-on-top, the windows that it owns will no longer be
always-on-top. When an always-on-top window is sent

toBack

, its always-on-top state is set to

false

.

When this method is called on a window with a value of

true

, and the window is visible and the platform
supports always-on-top for this window, the window is immediately
brought forward, "sticking" it in the top-most position. If the
window isn`t currently visible, this method sets the always-on-top
state to

true

but does not bring the window forward.
When the window is later shown, it will be always-on-top.

When this method is called on a window with a value of

false

the always-on-top state is set to normal. It may also
cause an unspecified, platform-dependent change in the z-order of
top-level windows, but other always-on-top windows will remain in
top-most position. Calling this method with a value of

false

on a window that has a normal state has no effect.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

All windows owned by an always-on-top window inherit this state and
automatically become always-on-top. If a window ceases to be
always-on-top, the windows that it owns will no longer be
always-on-top. When an always-on-top window is sent

toBack

, its always-on-top state is set to

false

.

When this method is called on a window with a value of

true

, and the window is visible and the platform
supports always-on-top for this window, the window is immediately
brought forward, "sticking" it in the top-most position. If the
window isn`t currently visible, this method sets the always-on-top
state to

true

but does not bring the window forward.
When the window is later shown, it will be always-on-top.

When this method is called on a window with a value of

false

the always-on-top state is set to normal. It may also
cause an unspecified, platform-dependent change in the z-order of
top-level windows, but other always-on-top windows will remain in
top-most position. Calling this method with a value of

false

on a window that has a normal state has no effect.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

When this method is called on a window with a value of

true

, and the window is visible and the platform
supports always-on-top for this window, the window is immediately
brought forward, "sticking" it in the top-most position. If the
window isn`t currently visible, this method sets the always-on-top
state to

true

but does not bring the window forward.
When the window is later shown, it will be always-on-top.

When this method is called on a window with a value of

false

the always-on-top state is set to normal. It may also
cause an unspecified, platform-dependent change in the z-order of
top-level windows, but other always-on-top windows will remain in
top-most position. Calling this method with a value of

false

on a window that has a normal state has no effect.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

When this method is called on a window with a value of

false

the always-on-top state is set to normal. It may also
cause an unspecified, platform-dependent change in the z-order of
top-level windows, but other always-on-top windows will remain in
top-most position. Calling this method with a value of

false

on a window that has a normal state has no effect.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

Note

: some platforms might not support always-on-top
windows. To detect if always-on-top windows are supported by the
current platform, use

Toolkit.isAlwaysOnTopSupported()

and

isAlwaysOnTopSupported()

. If always-on-top mode
isn't supported for this window or this window's toolkit does not
support always-on-top windows, calling this method has no effect.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

If a SecurityManager is installed, the calling thread must be
granted the AWTPermission "setWindowAlwaysOnTop" in
order to set the value of this property. If this
permission is not granted, this method will throw a
SecurityException, and the current value of the property will
be left unchanged.

isAlwaysOnTopSupported

```java
public boolean isAlwaysOnTopSupported()
```

Returns whether the always-on-top mode is supported for this
window. Some platforms may not support always-on-top windows, some
may support only some kinds of top-level windows; for example,
a platform may not support always-on-top modal dialogs.

**Returns:** true

, if the always-on-top mode is supported for
this window and this window's toolkit supports always-on-top windows,

false

otherwise
**Since:** 1.6
**See Also:** setAlwaysOnTop(boolean)

,

getToolkit()

,

Toolkit.isAlwaysOnTopSupported()

---

#### isAlwaysOnTopSupported

public boolean isAlwaysOnTopSupported()

Returns whether the always-on-top mode is supported for this
window. Some platforms may not support always-on-top windows, some
may support only some kinds of top-level windows; for example,
a platform may not support always-on-top modal dialogs.

isAlwaysOnTop

```java
public final boolean isAlwaysOnTop()
```

Returns whether this window is an always-on-top window.

**Returns:** true

, if the window is in always-on-top state,

false

otherwise
**Since:** 1.5
**See Also:** setAlwaysOnTop(boolean)

---

#### isAlwaysOnTop

public final boolean isAlwaysOnTop()

Returns whether this window is an always-on-top window.

getFocusOwner

```java
public
Component
getFocusOwner()
```

Returns the child Component of this Window that has focus if this Window
is focused; returns null otherwise.

**Returns:** the child Component with focus, or null if this Window is not
focused
**See Also:** getMostRecentFocusOwner()

,

isFocused()

---

#### getFocusOwner

public

Component

getFocusOwner()

Returns the child Component of this Window that has focus if this Window
is focused; returns null otherwise.

getMostRecentFocusOwner

```java
public
Component
getMostRecentFocusOwner()
```

Returns the child Component of this Window that will receive the focus
when this Window is focused. If this Window is currently focused, this
method returns the same Component as

getFocusOwner()

. If
this Window is not focused, then the child Component that most recently
requested focus will be returned. If no child Component has ever
requested focus, and this is a focusable Window, then this Window's
initial focusable Component is returned. If no child Component has ever
requested focus, and this is a non-focusable Window, null is returned.

**Returns:** the child Component that will receive focus when this Window is
focused
**Since:** 1.4
**See Also:** getFocusOwner()

,

isFocused()

,

isFocusableWindow()

---

#### getMostRecentFocusOwner

public

Component

getMostRecentFocusOwner()

Returns the child Component of this Window that will receive the focus
when this Window is focused. If this Window is currently focused, this
method returns the same Component as

getFocusOwner()

. If
this Window is not focused, then the child Component that most recently
requested focus will be returned. If no child Component has ever
requested focus, and this is a focusable Window, then this Window's
initial focusable Component is returned. If no child Component has ever
requested focus, and this is a non-focusable Window, null is returned.

isActive

```java
public boolean isActive()
```

Returns whether this Window is active. Only a Frame or a Dialog may be
active. The native windowing system may denote the active Window or its
children with special decorations, such as a highlighted title bar. The
active Window is always either the focused Window, or the first Frame or
Dialog that is an owner of the focused Window.

**Returns:** whether this is the active Window.
**Since:** 1.4
**See Also:** isFocused()

---

#### isActive

public boolean isActive()

Returns whether this Window is active. Only a Frame or a Dialog may be
active. The native windowing system may denote the active Window or its
children with special decorations, such as a highlighted title bar. The
active Window is always either the focused Window, or the first Frame or
Dialog that is an owner of the focused Window.

isFocused

```java
public boolean isFocused()
```

Returns whether this Window is focused. If there exists a focus owner,
the focused Window is the Window that is, or contains, that focus owner.
If there is no focus owner, then no Window is focused.

If the focused Window is a Frame or a Dialog it is also the active
Window. Otherwise, the active Window is the first Frame or Dialog that
is an owner of the focused Window.

**Returns:** whether this is the focused Window.
**Since:** 1.4
**See Also:** isActive()

---

#### isFocused

public boolean isFocused()

Returns whether this Window is focused. If there exists a focus owner,
the focused Window is the Window that is, or contains, that focus owner.
If there is no focus owner, then no Window is focused.

If the focused Window is a Frame or a Dialog it is also the active
Window. Otherwise, the active Window is the first Frame or Dialog that
is an owner of the focused Window.

If the focused Window is a Frame or a Dialog it is also the active
Window. Otherwise, the active Window is the first Frame or Dialog that
is an owner of the focused Window.

getFocusTraversalKeys

```java
public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)
```

Gets a focus traversal key for this Window. (See

setFocusTraversalKeys

for a full description of each key.)

If the traversal key has not been explicitly set for this Window,
then this Window's parent's traversal key is returned. If the
traversal key has not been explicitly set for any of this Window's
ancestors, then the current KeyboardFocusManager's default traversal key
is returned.

**Overrides:** getFocusTraversalKeys

in class

Container
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Returns:** the AWTKeyStroke for the specified key
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4
**See Also:** Container.setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

---

#### getFocusTraversalKeys

public

Set

<

AWTKeyStroke

> getFocusTraversalKeys​(int id)

Gets a focus traversal key for this Window. (See

setFocusTraversalKeys

for a full description of each key.)

If the traversal key has not been explicitly set for this Window,
then this Window's parent's traversal key is returned. If the
traversal key has not been explicitly set for any of this Window's
ancestors, then the current KeyboardFocusManager's default traversal key
is returned.

If the traversal key has not been explicitly set for this Window,
then this Window's parent's traversal key is returned. If the
traversal key has not been explicitly set for any of this Window's
ancestors, then the current KeyboardFocusManager's default traversal key
is returned.

setFocusCycleRoot

```java
public final void setFocusCycleRoot​(boolean focusCycleRoot)
```

Does nothing because Windows must always be roots of a focus traversal
cycle. The passed-in value is ignored.

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

Does nothing because Windows must always be roots of a focus traversal
cycle. The passed-in value is ignored.

isFocusCycleRoot

```java
public final boolean isFocusCycleRoot()
```

Always returns

true

because all Windows must be roots of a
focus traversal cycle.

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

because all Windows must be roots of a
focus traversal cycle.

getFocusCycleRootAncestor

```java
public final
Container
getFocusCycleRootAncestor()
```

Always returns

null

because Windows have no ancestors; they
represent the top of the Component hierarchy.

**Overrides:** getFocusCycleRootAncestor

in class

Component
**Returns:** null
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

---

#### getFocusCycleRootAncestor

public final

Container

getFocusCycleRootAncestor()

Always returns

null

because Windows have no ancestors; they
represent the top of the Component hierarchy.

isFocusableWindow

```java
public final boolean isFocusableWindow()
```

Returns whether this Window can become the focused Window, that is,
whether this Window or any of its subcomponents can become the focus
owner. For a Frame or Dialog to be focusable, its focusable Window state
must be set to

true

. For a Window which is not a Frame or
Dialog to be focusable, its focusable Window state must be set to

true

, its nearest owning Frame or Dialog must be
showing on the screen, and it must contain at least one Component in
its focus traversal cycle. If any of these conditions is not met, then
neither this Window nor any of its subcomponents can become the focus
owner.

**Returns:** true

if this Window can be the focused Window;

false

otherwise
**Since:** 1.4
**See Also:** getFocusableWindowState()

,

setFocusableWindowState(boolean)

,

isShowing()

,

Component.isFocusable()

---

#### isFocusableWindow

public final boolean isFocusableWindow()

Returns whether this Window can become the focused Window, that is,
whether this Window or any of its subcomponents can become the focus
owner. For a Frame or Dialog to be focusable, its focusable Window state
must be set to

true

. For a Window which is not a Frame or
Dialog to be focusable, its focusable Window state must be set to

true

, its nearest owning Frame or Dialog must be
showing on the screen, and it must contain at least one Component in
its focus traversal cycle. If any of these conditions is not met, then
neither this Window nor any of its subcomponents can become the focus
owner.

getFocusableWindowState

```java
public boolean getFocusableWindowState()
```

Returns whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this method returns

false

, then

isFocusableWindow

will return

false

as well.
If this method returns

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

By default, all Windows have a focusable Window state of

true

.

**Returns:** whether this Window can be the focused Window
**Since:** 1.4
**See Also:** isFocusableWindow()

,

setFocusableWindowState(boolean)

,

isShowing()

,

Component.setFocusable(boolean)

---

#### getFocusableWindowState

public boolean getFocusableWindowState()

Returns whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this method returns

false

, then

isFocusableWindow

will return

false

as well.
If this method returns

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

By default, all Windows have a focusable Window state of

true

.

By default, all Windows have a focusable Window state of

true

.

setFocusableWindowState

```java
public void setFocusableWindowState​(boolean focusableWindowState)
```

Sets whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this Window's focusable Window state is set to

false

, then

isFocusableWindow

will return

false

. If this
Window's focusable Window state is set to

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

Setting a Window's focusability state to

false

is the
standard mechanism for an application to identify to the AWT a Window
which will be used as a floating palette or toolbar, and thus should be
a non-focusable Window.

Setting the focusability state on a visible

Window

can have a delayed effect on some platforms — the actual
change may happen only when the

Window

becomes
hidden and then visible again. To ensure consistent behavior
across platforms, set the

Window

's focusable state
when the

Window

is invisible and then show it.

**Parameters:** focusableWindowState

- whether this Window can be the focused
Window
**Since:** 1.4
**See Also:** isFocusableWindow()

,

getFocusableWindowState()

,

isShowing()

,

Component.setFocusable(boolean)

---

#### setFocusableWindowState

public void setFocusableWindowState​(boolean focusableWindowState)

Sets whether this Window can become the focused Window if it meets
the other requirements outlined in

isFocusableWindow

. If
this Window's focusable Window state is set to

false

, then

isFocusableWindow

will return

false

. If this
Window's focusable Window state is set to

true

, then

isFocusableWindow

may return

true

or

false

depending upon the other requirements which must be
met in order for a Window to be focusable.

Setting a Window's focusability state to

false

is the
standard mechanism for an application to identify to the AWT a Window
which will be used as a floating palette or toolbar, and thus should be
a non-focusable Window.

Setting the focusability state on a visible

Window

can have a delayed effect on some platforms — the actual
change may happen only when the

Window

becomes
hidden and then visible again. To ensure consistent behavior
across platforms, set the

Window

's focusable state
when the

Window

is invisible and then show it.

Setting a Window's focusability state to

false

is the
standard mechanism for an application to identify to the AWT a Window
which will be used as a floating palette or toolbar, and thus should be
a non-focusable Window.

Setting the focusability state on a visible

Window

can have a delayed effect on some platforms — the actual
change may happen only when the

Window

becomes
hidden and then visible again. To ensure consistent behavior
across platforms, set the

Window

's focusable state
when the

Window

is invisible and then show it.

setAutoRequestFocus

```java
public void setAutoRequestFocus​(boolean autoRequestFocus)
```

Sets whether this window should receive focus on
subsequently being shown (with a call to

setVisible(true)

),
or being moved to the front (with a call to

toFront()

).

Note that

setVisible(true)

may be called indirectly
(e.g. when showing an owner of the window makes the window to be shown).

toFront()

may also be called indirectly (e.g. when

setVisible(true)

is called on already visible window).
In all such cases this property takes effect as well.

The value of the property is not inherited by owned windows.

**Parameters:** autoRequestFocus

- whether this window should be focused on
subsequently being shown or being moved to the front
**Since:** 1.7
**See Also:** isAutoRequestFocus()

,

isFocusableWindow()

,

setVisible(boolean)

,

toFront()

---

#### setAutoRequestFocus

public void setAutoRequestFocus​(boolean autoRequestFocus)

Sets whether this window should receive focus on
subsequently being shown (with a call to

setVisible(true)

),
or being moved to the front (with a call to

toFront()

).

Note that

setVisible(true)

may be called indirectly
(e.g. when showing an owner of the window makes the window to be shown).

toFront()

may also be called indirectly (e.g. when

setVisible(true)

is called on already visible window).
In all such cases this property takes effect as well.

The value of the property is not inherited by owned windows.

Note that

setVisible(true)

may be called indirectly
(e.g. when showing an owner of the window makes the window to be shown).

toFront()

may also be called indirectly (e.g. when

setVisible(true)

is called on already visible window).
In all such cases this property takes effect as well.

The value of the property is not inherited by owned windows.

The value of the property is not inherited by owned windows.

isAutoRequestFocus

```java
public boolean isAutoRequestFocus()
```

Returns whether this window should receive focus on subsequently being shown
(with a call to

setVisible(true)

), or being moved to the front
(with a call to

toFront()

).

By default, the window has

autoRequestFocus

value of

true

.

**Returns:** autoRequestFocus

value
**Since:** 1.7
**See Also:** setAutoRequestFocus(boolean)

---

#### isAutoRequestFocus

public boolean isAutoRequestFocus()

Returns whether this window should receive focus on subsequently being shown
(with a call to

setVisible(true)

), or being moved to the front
(with a call to

toFront()

).

By default, the window has

autoRequestFocus

value of

true

.

By default, the window has

autoRequestFocus

value of

true

.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Container
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

,

addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

this Window's font ("font")

this Window's background color ("background")

this Window's foreground color ("foreground")

this Window's focusability ("focusable")

this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")

this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")

this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")

this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")

this Window's focus traversal policy ("focusTraversalPolicy")

this Window's focusable Window state ("focusableWindowState")

this Window's always-on-top state("alwaysOnTop")

If listener is null, no exception is thrown and no action is performed.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Container
**Parameters:** propertyName

- one of the property names listed above
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

String

propertyName,

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Window's font ("font")
- this Window's background color ("background")
- this Window's foreground color ("foreground")
- this Window's focusability ("focusable")
- this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Window's focus traversal policy ("focusTraversalPolicy")
- this Window's focusable Window state ("focusableWindowState")
- this Window's always-on-top state("alwaysOnTop")

Note that if this Window is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

this Window's font ("font")

this Window's background color ("background")

this Window's foreground color ("foreground")

this Window's focusability ("focusable")

this Window's focus traversal keys enabled state
("focusTraversalKeysEnabled")

this Window's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")

this Window's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")

this Window's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

this Window's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")

this Window's focus traversal policy ("focusTraversalPolicy")

this Window's focusable Window state ("focusableWindowState")

this Window's always-on-top state("alwaysOnTop")

If listener is null, no exception is thrown and no action is performed.

isValidateRoot

```java
public boolean isValidateRoot()
```

Indicates if this container is a validate root.

Window

objects are the validate roots, and, therefore, they
override this method to return

true

.

**Overrides:** isValidateRoot

in class

Container
**Returns:** true
**Since:** 1.7
**See Also:** Container.isValidateRoot()

---

#### isValidateRoot

public boolean isValidateRoot()

Indicates if this container is a validate root.

Window

objects are the validate roots, and, therefore, they
override this method to return

true

.

Window

objects are the validate roots, and, therefore, they
override this method to return

true

.

postEvent

```java
@Deprecated

public boolean postEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1
replaced by

dispatchEvent(AWTEvent)

.

Description copied from interface:

MenuContainer

Posts an event to the listeners.

**Specified by:** postEvent

in interface

MenuContainer
**Overrides:** postEvent

in class

Component
**Parameters:** e

- the event to dispatch
**Returns:** the results of posting the event

---

#### postEvent

@Deprecated

public boolean postEvent​(

Event

e)

Description copied from interface:

MenuContainer

Posts an event to the listeners.

isShowing

```java
public boolean isShowing()
```

Checks if this Window is showing on screen.

**Overrides:** isShowing

in class

Component
**Returns:** true

if the component is showing,

false

otherwise
**See Also:** Component.setVisible(boolean)

---

#### isShowing

public boolean isShowing()

Checks if this Window is showing on screen.

applyResourceBundle

```java
@Deprecated

public void applyResourceBundle​(
ResourceBundle
rb)
```

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

**Parameters:** rb

- the resource bundle

---

#### applyResourceBundle

@Deprecated

public void applyResourceBundle​(

ResourceBundle

rb)

applyResourceBundle

```java
@Deprecated

public void applyResourceBundle​(
String
rbName)
```

Deprecated.

As of J2SE 1.4, replaced by

Component.applyComponentOrientation

.

**Parameters:** rbName

- the resource name

---

#### applyResourceBundle

@Deprecated

public void applyResourceBundle​(

String

rbName)

setType

```java
public void setType​(
Window.Type
type)
```

Sets the type of the window.

This method can only be called while the window is not displayable.

**Parameters:** type

- the window type
**Throws:** IllegalComponentStateException

- if the window
is displayable.
**Throws:** IllegalArgumentException

- if the type is

null
**Since:** 1.7
**See Also:** Component.isDisplayable()

,

getType()

---

#### setType

public void setType​(

Window.Type

type)

Sets the type of the window.

This method can only be called while the window is not displayable.

getType

```java
public
Window.Type
getType()
```

Returns the type of the window.

**Returns:** the type of the window
**Since:** 1.7
**See Also:** setType(java.awt.Window.Type)

---

#### getType

public

Window.Type

getType()

Returns the type of the window.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Window.
For windows, the AccessibleContext takes the form of an
AccessibleAWTWindow.
A new AccessibleAWTWindow instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleAWTWindow that serves as the
AccessibleContext of this Window
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this Window.
For windows, the AccessibleContext takes the form of an
AccessibleAWTWindow.
A new AccessibleAWTWindow instance is created if necessary.

setLocationRelativeTo

```java
public void setLocationRelativeTo​(
Component
c)
```

Sets the location of the window relative to the specified
component according to the following scenarios.

The target screen mentioned below is a screen to which
the window should be placed after the setLocationRelativeTo
method is called.

- If the component is

null

, or the

GraphicsConfiguration

associated with this component is

null

, the window is placed in the center of the
screen. The center point can be obtained with the

GraphicsEnvironment.getCenterPoint

method.

If the component is not

null

, but it is not
currently showing, the window is placed in the center of
the target screen defined by the

GraphicsConfiguration

associated with this component.

If the component is not

null

and is shown on
the screen, then the window is located in such a way that
the center of the window coincides with the center of the
component.

If the screens configuration does not allow the window to
be moved from one screen to another, then the window is
only placed at the location determined according to the
above conditions and its

GraphicsConfiguration

is
not changed.

Note

: If the lower edge of the window is out of the screen,
then the window is placed to the side of the

Component

that is closest to the center of the screen. So if the
component is on the right part of the screen, the window
is placed to its left, and vice versa.

If after the window location has been calculated, the upper,
left, or right edge of the window is out of the screen,
then the window is located in such a way that the upper,
left, or right edge of the window coincides with the
corresponding edge of the screen. If both left and right
edges of the window are out of the screen, the window is
placed at the left side of the screen. The similar placement
will occur if both top and bottom edges are out of the screen.
In that case, the window is placed at the top side of the screen.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Parameters:** c

- the component in relation to which the window's location
is determined
**Since:** 1.4
**See Also:** GraphicsEnvironment.getCenterPoint()

---

#### setLocationRelativeTo

public void setLocationRelativeTo​(

Component

c)

Sets the location of the window relative to the specified
component according to the following scenarios.

The target screen mentioned below is a screen to which
the window should be placed after the setLocationRelativeTo
method is called.

- If the component is

null

, or the

GraphicsConfiguration

associated with this component is

null

, the window is placed in the center of the
screen. The center point can be obtained with the

GraphicsEnvironment.getCenterPoint

method.

If the component is not

null

, but it is not
currently showing, the window is placed in the center of
the target screen defined by the

GraphicsConfiguration

associated with this component.

If the component is not

null

and is shown on
the screen, then the window is located in such a way that
the center of the window coincides with the center of the
component.

If the screens configuration does not allow the window to
be moved from one screen to another, then the window is
only placed at the location determined according to the
above conditions and its

GraphicsConfiguration

is
not changed.

Note

: If the lower edge of the window is out of the screen,
then the window is placed to the side of the

Component

that is closest to the center of the screen. So if the
component is on the right part of the screen, the window
is placed to its left, and vice versa.

If after the window location has been calculated, the upper,
left, or right edge of the window is out of the screen,
then the window is located in such a way that the upper,
left, or right edge of the window coincides with the
corresponding edge of the screen. If both left and right
edges of the window are out of the screen, the window is
placed at the left side of the screen. The similar placement
will occur if both top and bottom edges are out of the screen.
In that case, the window is placed at the top side of the screen.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The target screen mentioned below is a screen to which
the window should be placed after the setLocationRelativeTo
method is called.

- If the component is

null

, or the

GraphicsConfiguration

associated with this component is

null

, the window is placed in the center of the
screen. The center point can be obtained with the

GraphicsEnvironment.getCenterPoint

method.

If the component is not

null

, but it is not
currently showing, the window is placed in the center of
the target screen defined by the

GraphicsConfiguration

associated with this component.

If the component is not

null

and is shown on
the screen, then the window is located in such a way that
the center of the window coincides with the center of the
component.

If the screens configuration does not allow the window to
be moved from one screen to another, then the window is
only placed at the location determined according to the
above conditions and its

GraphicsConfiguration

is
not changed.

Note

: If the lower edge of the window is out of the screen,
then the window is placed to the side of the

Component

that is closest to the center of the screen. So if the
component is on the right part of the screen, the window
is placed to its left, and vice versa.

If after the window location has been calculated, the upper,
left, or right edge of the window is out of the screen,
then the window is located in such a way that the upper,
left, or right edge of the window coincides with the
corresponding edge of the screen. If both left and right
edges of the window are out of the screen, the window is
placed at the left side of the screen. The similar placement
will occur if both top and bottom edges are out of the screen.
In that case, the window is placed at the top side of the screen.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

If the component is

null

, or the

GraphicsConfiguration

associated with this component is

null

, the window is placed in the center of the
screen. The center point can be obtained with the

GraphicsEnvironment.getCenterPoint

method.

If the component is not

null

, but it is not
currently showing, the window is placed in the center of
the target screen defined by the

GraphicsConfiguration

associated with this component.

If the component is not

null

and is shown on
the screen, then the window is located in such a way that
the center of the window coincides with the center of the
component.

If the screens configuration does not allow the window to
be moved from one screen to another, then the window is
only placed at the location determined according to the
above conditions and its

GraphicsConfiguration

is
not changed.

Note

: If the lower edge of the window is out of the screen,
then the window is placed to the side of the

Component

that is closest to the center of the screen. So if the
component is on the right part of the screen, the window
is placed to its left, and vice versa.

If after the window location has been calculated, the upper,
left, or right edge of the window is out of the screen,
then the window is located in such a way that the upper,
left, or right edge of the window coincides with the
corresponding edge of the screen. If both left and right
edges of the window are out of the screen, the window is
placed at the left side of the screen. The similar placement
will occur if both top and bottom edges are out of the screen.
In that case, the window is placed at the top side of the screen.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

Note

: If the lower edge of the window is out of the screen,
then the window is placed to the side of the

Component

that is closest to the center of the screen. So if the
component is on the right part of the screen, the window
is placed to its left, and vice versa.

If after the window location has been calculated, the upper,
left, or right edge of the window is out of the screen,
then the window is located in such a way that the upper,
left, or right edge of the window coincides with the
corresponding edge of the screen. If both left and right
edges of the window are out of the screen, the window is
placed at the left side of the screen. The similar placement
will occur if both top and bottom edges are out of the screen.
In that case, the window is placed at the top side of the screen.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

If after the window location has been calculated, the upper,
left, or right edge of the window is out of the screen,
then the window is located in such a way that the upper,
left, or right edge of the window coincides with the
corresponding edge of the screen. If both left and right
edges of the window are out of the screen, the window is
placed at the left side of the screen. The similar placement
will occur if both top and bottom edges are out of the screen.
In that case, the window is placed at the top side of the screen.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

createBufferStrategy

```java
public void createBufferStrategy​(int numBuffers)
```

Creates a new strategy for multi-buffering on this component.
Multi-buffering is useful for rendering performance. This method
attempts to create the best strategy available with the number of
buffers supplied. It will always create a

BufferStrategy

with that number of buffers.
A page-flipping strategy is attempted first, then a blitting strategy
using accelerated buffers. Finally, an unaccelerated blitting
strategy is used.

Each time this method is called,
the existing buffer strategy for this component is discarded.

**Parameters:** numBuffers

- number of buffers to create
**Throws:** IllegalArgumentException

- if numBuffers is less than 1.
**Throws:** IllegalStateException

- if the component is not displayable
**Since:** 1.4
**See Also:** Component.isDisplayable()

,

getBufferStrategy()

---

#### createBufferStrategy

public void createBufferStrategy​(int numBuffers)

Creates a new strategy for multi-buffering on this component.
Multi-buffering is useful for rendering performance. This method
attempts to create the best strategy available with the number of
buffers supplied. It will always create a

BufferStrategy

with that number of buffers.
A page-flipping strategy is attempted first, then a blitting strategy
using accelerated buffers. Finally, an unaccelerated blitting
strategy is used.

Each time this method is called,
the existing buffer strategy for this component is discarded.

Each time this method is called,
the existing buffer strategy for this component is discarded.

createBufferStrategy

```java
public void createBufferStrategy​(int numBuffers,

BufferCapabilities
caps)
throws
AWTException
```

Creates a new strategy for multi-buffering on this component with the
required buffer capabilities. This is useful, for example, if only
accelerated memory or page flipping is desired (as specified by the
buffer capabilities).

Each time this method
is called, the existing buffer strategy for this component is discarded.

**Parameters:** numBuffers

- number of buffers to create, including the front buffer
**Parameters:** caps

- the required capabilities for creating the buffer strategy;
cannot be

null
**Throws:** AWTException

- if the capabilities supplied could not be
supported or met; this may happen, for example, if there is not enough
accelerated memory currently available, or if page flipping is specified
but not possible.
**Throws:** IllegalArgumentException

- if numBuffers is less than 1, or if
caps is

null
**Since:** 1.4
**See Also:** getBufferStrategy()

---

#### createBufferStrategy

public void createBufferStrategy​(int numBuffers,

BufferCapabilities

caps)
throws

AWTException

Creates a new strategy for multi-buffering on this component with the
required buffer capabilities. This is useful, for example, if only
accelerated memory or page flipping is desired (as specified by the
buffer capabilities).

Each time this method
is called, the existing buffer strategy for this component is discarded.

Each time this method
is called, the existing buffer strategy for this component is discarded.

getBufferStrategy

```java
public
BufferStrategy
getBufferStrategy()
```

Returns the

BufferStrategy

used by this component. This
method will return null if a

BufferStrategy

has not yet
been created or has been disposed.

**Returns:** the buffer strategy used by this component
**Since:** 1.4
**See Also:** createBufferStrategy(int)

---

#### getBufferStrategy

public

BufferStrategy

getBufferStrategy()

Returns the

BufferStrategy

used by this component. This
method will return null if a

BufferStrategy

has not yet
been created or has been disposed.

setLocationByPlatform

```java
public void setLocationByPlatform​(boolean locationByPlatform)
```

Sets whether this Window should appear at the default location for the
native windowing system or at the current location (returned by

getLocation

) the next time the Window is made visible.
This behavior resembles a native window shown without programmatically
setting its location. Most windowing systems cascade windows if their
locations are not explicitly set. The actual location is determined once the
window is shown on the screen.

This behavior can also be enabled by setting the System Property
"java.awt.Window.locationByPlatform" to "true", though calls to this method
take precedence.

Calls to

setVisible

,

setLocation

and

setBounds

after calling

setLocationByPlatform

clear
this property of the Window.

For example, after the following code is executed:

```java
setLocationByPlatform(true);
setVisible(true);
boolean flag = isLocationByPlatform();
```

The window will be shown at platform's default location and

flag

will be

false

.

In the following sample:

```java
setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);
```

The window will be shown at (10, 10) and

flag

will be

false

.

**Parameters:** locationByPlatform

-

true

if this Window should appear
at the default location,

false

if at the current location
**Throws:** IllegalComponentStateException

- if the window
is showing on screen and locationByPlatform is

true

.
**Since:** 1.5
**See Also:** setLocation(int, int)

,

isShowing()

,

setVisible(boolean)

,

isLocationByPlatform()

,

System.getProperty(String)

---

#### setLocationByPlatform

public void setLocationByPlatform​(boolean locationByPlatform)

Sets whether this Window should appear at the default location for the
native windowing system or at the current location (returned by

getLocation

) the next time the Window is made visible.
This behavior resembles a native window shown without programmatically
setting its location. Most windowing systems cascade windows if their
locations are not explicitly set. The actual location is determined once the
window is shown on the screen.

This behavior can also be enabled by setting the System Property
"java.awt.Window.locationByPlatform" to "true", though calls to this method
take precedence.

Calls to

setVisible

,

setLocation

and

setBounds

after calling

setLocationByPlatform

clear
this property of the Window.

For example, after the following code is executed:

```java
setLocationByPlatform(true);
setVisible(true);
boolean flag = isLocationByPlatform();
```

The window will be shown at platform's default location and

flag

will be

false

.

In the following sample:

```java
setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);
```

The window will be shown at (10, 10) and

flag

will be

false

.

This behavior can also be enabled by setting the System Property
"java.awt.Window.locationByPlatform" to "true", though calls to this method
take precedence.

Calls to

setVisible

,

setLocation

and

setBounds

after calling

setLocationByPlatform

clear
this property of the Window.

For example, after the following code is executed:

```java
setLocationByPlatform(true);
setVisible(true);
boolean flag = isLocationByPlatform();
```

The window will be shown at platform's default location and

flag

will be

false

.

In the following sample:

```java
setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);
```

The window will be shown at (10, 10) and

flag

will be

false

.

Calls to

setVisible

,

setLocation

and

setBounds

after calling

setLocationByPlatform

clear
this property of the Window.

For example, after the following code is executed:

```java
setLocationByPlatform(true);
setVisible(true);
boolean flag = isLocationByPlatform();
```

The window will be shown at platform's default location and

flag

will be

false

.

In the following sample:

```java
setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);
```

The window will be shown at (10, 10) and

flag

will be

false

.

For example, after the following code is executed:

```java
setLocationByPlatform(true);
setVisible(true);
boolean flag = isLocationByPlatform();
```

The window will be shown at platform's default location and

flag

will be

false

.

In the following sample:

```java
setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);
```

The window will be shown at (10, 10) and

flag

will be

false

.

setLocationByPlatform(true);
setVisible(true);
boolean flag = isLocationByPlatform();

In the following sample:

```java
setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);
```

The window will be shown at (10, 10) and

flag

will be

false

.

setLocationByPlatform(true);
setLocation(10, 10);
boolean flag = isLocationByPlatform();
setVisible(true);

isLocationByPlatform

```java
public boolean isLocationByPlatform()
```

Returns

true

if this Window will appear at the default location
for the native windowing system the next time this Window is made visible.
This method always returns

false

if the Window is showing on the
screen.

**Returns:** whether this Window will appear at the default location
**Since:** 1.5
**See Also:** setLocationByPlatform(boolean)

,

isShowing()

---

#### isLocationByPlatform

public boolean isLocationByPlatform()

Returns

true

if this Window will appear at the default location
for the native windowing system the next time this Window is made visible.
This method always returns

false

if the Window is showing on the
screen.

setBounds

```java
public void setBounds​(int x,
int y,
int width,
int height)
```

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

or

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setBounds

in class

Component
**Parameters:** x

- the new

x

-coordinate of this component
**Parameters:** y

- the new

y

-coordinate of this component
**Parameters:** width

- the new

width

of this component
**Parameters:** height

- the new

height

of this
component
**Since:** 1.6
**See Also:** Component.getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

setMinimumSize(java.awt.Dimension)

,

setLocationByPlatform(boolean)

,

isLocationByPlatform()

---

#### setBounds

public void setBounds​(int x,
int y,
int width,
int height)

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

or

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

width

or

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The

width

or

height

values
are automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

setBounds

```java
public void setBounds​(
Rectangle
r)
```

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

r.width

or

r.height

values
will be automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

**Overrides:** setBounds

in class

Component
**Parameters:** r

- the new bounding rectangle for this component
**Since:** 1.6
**See Also:** Component.getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

setMinimumSize(java.awt.Dimension)

,

setLocationByPlatform(boolean)

,

isLocationByPlatform()

---

#### setBounds

public void setBounds​(

Rectangle

r)

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

r.width

or

r.height

values
will be automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

The

r.width

or

r.height

values
will be automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The

r.width

or

r.height

values
will be automatically enlarged if either is less than
the minimum size as specified by previous call to

setMinimumSize

.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

The method changes the geometry-related data. Therefore,
the native windowing system may ignore such requests, or it may modify
the requested data, so that the

Window

object is placed and sized
in a way that corresponds closely to the desktop settings.

getOpacity

```java
public float getOpacity()
```

Returns the opacity of the window.

**Returns:** the opacity of the window
**Since:** 1.7
**See Also:** setOpacity(float)

,

GraphicsDevice.WindowTranslucency

---

#### getOpacity

public float getOpacity()

Returns the opacity of the window.

setOpacity

```java
public void setOpacity​(float opacity)
```

Sets the opacity of the window.

The opacity value is in the range [0..1]. Note that setting the opacity
level of 0 may or may not disable the mouse event handling on this
window. This is a platform-dependent behavior.

The following conditions must be met in order to set the opacity value
less than

1.0f

:

- The

TRANSLUCENT

translucency must be supported by the underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested opacity value is less than

1.0f

, and any of the
above conditions are not met, the window opacity will not change,
and the

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
current shape of this window (see

setShape(Shape)

).

**Parameters:** opacity

- the opacity level to set to the window
**Throws:** IllegalArgumentException

- if the opacity is out of the range
[0..1]
**Throws:** IllegalComponentStateException

- if the window is decorated and
the opacity is less than

1.0f
**Throws:** IllegalComponentStateException

- if the window is in full screen
mode, and the opacity is less than

1.0f
**Throws:** UnsupportedOperationException

- if the

GraphicsDevice.WindowTranslucency#TRANSLUCENT TRANSLUCENT

translucency is not supported and the opacity is less than

1.0f
**Since:** 1.7
**See Also:** getOpacity()

,

setBackground(Color)

,

setShape(Shape)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

---

#### setOpacity

public void setOpacity​(float opacity)

Sets the opacity of the window.

The opacity value is in the range [0..1]. Note that setting the opacity
level of 0 may or may not disable the mouse event handling on this
window. This is a platform-dependent behavior.

The following conditions must be met in order to set the opacity value
less than

1.0f

:

- The

TRANSLUCENT

translucency must be supported by the underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested opacity value is less than

1.0f

, and any of the
above conditions are not met, the window opacity will not change,
and the

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
current shape of this window (see

setShape(Shape)

).

The opacity value is in the range [0..1]. Note that setting the opacity
level of 0 may or may not disable the mouse event handling on this
window. This is a platform-dependent behavior.

The following conditions must be met in order to set the opacity value
less than

1.0f

:

- The

TRANSLUCENT

translucency must be supported by the underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested opacity value is less than

1.0f

, and any of the
above conditions are not met, the window opacity will not change,
and the

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
current shape of this window (see

setShape(Shape)

).

The following conditions must be met in order to set the opacity value
less than

1.0f

:

- The

TRANSLUCENT

translucency must be supported by the underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested opacity value is less than

1.0f

, and any of the
above conditions are not met, the window opacity will not change,
and the

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
current shape of this window (see

setShape(Shape)

).

The

TRANSLUCENT

translucency must be supported by the underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested opacity value is less than

1.0f

, and any of the
above conditions are not met, the window opacity will not change,
and the

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
current shape of this window (see

setShape(Shape)

).

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
current shape of this window (see

setShape(Shape)

).

getShape

```java
public
Shape
getShape()
```

Returns the shape of the window.

The value returned by this method may not be the same as
previously set with

setShape(shape)

, but it is guaranteed
to represent the same shape.

**Returns:** the shape of the window or

null

if no
shape is specified for the window
**Since:** 1.7
**See Also:** setShape(Shape)

,

GraphicsDevice.WindowTranslucency

---

#### getShape

public

Shape

getShape()

Returns the shape of the window.

The value returned by this method may not be the same as
previously set with

setShape(shape)

, but it is guaranteed
to represent the same shape.

setShape

```java
public void setShape​(
Shape
shape)
```

Sets the shape of the window.

Setting a shape cuts off some parts of the window. Only the parts that
belong to the given

Shape

remain visible and clickable. If
the shape argument is

null

, this method restores the default
shape, making the window rectangular on most platforms.

The following conditions must be met to set a non-null shape:

- The

PERPIXEL_TRANSPARENT

translucency must be supported by the
underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested shape is not

null

, and any of the above
conditions are not met, the shape of this window will not change,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
opacity value (see

setOpacity(float)

). See

GraphicsDevice.WindowTranslucency

for more details.

**Parameters:** shape

- the shape to set to the window
**Throws:** IllegalComponentStateException

- if the shape is not

null

and the window is decorated
**Throws:** IllegalComponentStateException

- if the shape is not

null

and the window is in full-screen mode
**Throws:** UnsupportedOperationException

- if the shape is not

null

and

PERPIXEL_TRANSPARENT

translucency is not supported
**Since:** 1.7
**See Also:** getShape()

,

setBackground(Color)

,

setOpacity(float)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

---

#### setShape

public void setShape​(

Shape

shape)

Sets the shape of the window.

Setting a shape cuts off some parts of the window. Only the parts that
belong to the given

Shape

remain visible and clickable. If
the shape argument is

null

, this method restores the default
shape, making the window rectangular on most platforms.

The following conditions must be met to set a non-null shape:

- The

PERPIXEL_TRANSPARENT

translucency must be supported by the
underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested shape is not

null

, and any of the above
conditions are not met, the shape of this window will not change,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
opacity value (see

setOpacity(float)

). See

GraphicsDevice.WindowTranslucency

for more details.

Setting a shape cuts off some parts of the window. Only the parts that
belong to the given

Shape

remain visible and clickable. If
the shape argument is

null

, this method restores the default
shape, making the window rectangular on most platforms.

The following conditions must be met to set a non-null shape:

- The

PERPIXEL_TRANSPARENT

translucency must be supported by the
underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested shape is not

null

, and any of the above
conditions are not met, the shape of this window will not change,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
opacity value (see

setOpacity(float)

). See

GraphicsDevice.WindowTranslucency

for more details.

The following conditions must be met to set a non-null shape:

- The

PERPIXEL_TRANSPARENT

translucency must be supported by the
underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested shape is not

null

, and any of the above
conditions are not met, the shape of this window will not change,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
opacity value (see

setOpacity(float)

). See

GraphicsDevice.WindowTranslucency

for more details.

The

PERPIXEL_TRANSPARENT

translucency must be supported by the
underlying system

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the requested shape is not

null

, and any of the above
conditions are not met, the shape of this window will not change,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
opacity value (see

setOpacity(float)

). See

GraphicsDevice.WindowTranslucency

for more details.

The translucency levels of individual pixels may also be effected by the
alpha component of their color (see

setBackground(Color)

) and the
opacity value (see

setOpacity(float)

). See

GraphicsDevice.WindowTranslucency

for more details.

getBackground

```java
public
Color
getBackground()
```

Gets the background color of this window.

Note that the alpha component of the returned color indicates whether
the window is in the non-opaque (per-pixel translucent) mode.

**Overrides:** getBackground

in class

Component
**Returns:** this component's background color
**See Also:** setBackground(Color)

,

isOpaque()

,

GraphicsDevice.WindowTranslucency

---

#### getBackground

public

Color

getBackground()

Gets the background color of this window.

Note that the alpha component of the returned color indicates whether
the window is in the non-opaque (per-pixel translucent) mode.

Note that the alpha component of the returned color indicates whether
the window is in the non-opaque (per-pixel translucent) mode.

setBackground

```java
public void setBackground​(
Color
bgColor)
```

Sets the background color of this window.

If the windowing system supports the

PERPIXEL_TRANSLUCENT

translucency, the alpha component of the given background color
may effect the mode of operation for this window: it indicates whether
this window must be opaque (alpha equals

1.0f

) or per-pixel translucent
(alpha is less than

1.0f

). If the given background color is

null

, the window is considered completely opaque.

All the following conditions must be met to enable the per-pixel
transparency mode for this window:

- The

PERPIXEL_TRANSLUCENT

translucency must be supported by the graphics
device where this window is located

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the alpha component of the requested background color is less than

1.0f

, and any of the above conditions are not met, the background
color of this window will not change, the alpha component of the given
background color will not affect the mode of operation for this window,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

When the window is per-pixel translucent, the drawing sub-system
respects the alpha value of each individual pixel. If a pixel gets
painted with the alpha color component equal to zero, it becomes
visually transparent. If the alpha of the pixel is equal to 1.0f, the
pixel is fully opaque. Interim values of the alpha color component make
the pixel semi-transparent. In this mode, the background of the window
gets painted with the alpha value of the given background color. If the
alpha value of the argument of this method is equal to

0

, the
background is not painted at all.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

**Overrides:** setBackground

in class

Component
**Parameters:** bgColor

- the color to become this window's background color.
**Throws:** IllegalComponentStateException

- if the alpha value of the given
background color is less than

1.0f

and the window is decorated
**Throws:** IllegalComponentStateException

- if the alpha value of the given
background color is less than

1.0f

and the window is in
full-screen mode
**Throws:** UnsupportedOperationException

- if the alpha value of the given
background color is less than

1.0f

and

PERPIXEL_TRANSLUCENT

translucency is not supported
**See Also:** getBackground()

,

isOpaque()

,

setOpacity(float)

,

setShape(Shape)

,

Frame.isUndecorated()

,

Dialog.isUndecorated()

,

GraphicsDevice.WindowTranslucency

,

GraphicsDevice.isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency)

,

GraphicsConfiguration.isTranslucencyCapable()

---

#### setBackground

public void setBackground​(

Color

bgColor)

Sets the background color of this window.

If the windowing system supports the

PERPIXEL_TRANSLUCENT

translucency, the alpha component of the given background color
may effect the mode of operation for this window: it indicates whether
this window must be opaque (alpha equals

1.0f

) or per-pixel translucent
(alpha is less than

1.0f

). If the given background color is

null

, the window is considered completely opaque.

All the following conditions must be met to enable the per-pixel
transparency mode for this window:

- The

PERPIXEL_TRANSLUCENT

translucency must be supported by the graphics
device where this window is located

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the alpha component of the requested background color is less than

1.0f

, and any of the above conditions are not met, the background
color of this window will not change, the alpha component of the given
background color will not affect the mode of operation for this window,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

When the window is per-pixel translucent, the drawing sub-system
respects the alpha value of each individual pixel. If a pixel gets
painted with the alpha color component equal to zero, it becomes
visually transparent. If the alpha of the pixel is equal to 1.0f, the
pixel is fully opaque. Interim values of the alpha color component make
the pixel semi-transparent. In this mode, the background of the window
gets painted with the alpha value of the given background color. If the
alpha value of the argument of this method is equal to

0

, the
background is not painted at all.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

If the windowing system supports the

PERPIXEL_TRANSLUCENT

translucency, the alpha component of the given background color
may effect the mode of operation for this window: it indicates whether
this window must be opaque (alpha equals

1.0f

) or per-pixel translucent
(alpha is less than

1.0f

). If the given background color is

null

, the window is considered completely opaque.

All the following conditions must be met to enable the per-pixel
transparency mode for this window:

- The

PERPIXEL_TRANSLUCENT

translucency must be supported by the graphics
device where this window is located

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the alpha component of the requested background color is less than

1.0f

, and any of the above conditions are not met, the background
color of this window will not change, the alpha component of the given
background color will not affect the mode of operation for this window,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

When the window is per-pixel translucent, the drawing sub-system
respects the alpha value of each individual pixel. If a pixel gets
painted with the alpha color component equal to zero, it becomes
visually transparent. If the alpha of the pixel is equal to 1.0f, the
pixel is fully opaque. Interim values of the alpha color component make
the pixel semi-transparent. In this mode, the background of the window
gets painted with the alpha value of the given background color. If the
alpha value of the argument of this method is equal to

0

, the
background is not painted at all.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

All the following conditions must be met to enable the per-pixel
transparency mode for this window:

- The

PERPIXEL_TRANSLUCENT

translucency must be supported by the graphics
device where this window is located

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the alpha component of the requested background color is less than

1.0f

, and any of the above conditions are not met, the background
color of this window will not change, the alpha component of the given
background color will not affect the mode of operation for this window,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

When the window is per-pixel translucent, the drawing sub-system
respects the alpha value of each individual pixel. If a pixel gets
painted with the alpha color component equal to zero, it becomes
visually transparent. If the alpha of the pixel is equal to 1.0f, the
pixel is fully opaque. Interim values of the alpha color component make
the pixel semi-transparent. In this mode, the background of the window
gets painted with the alpha value of the given background color. If the
alpha value of the argument of this method is equal to

0

, the
background is not painted at all.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

The

PERPIXEL_TRANSLUCENT

translucency must be supported by the graphics
device where this window is located

The window must be undecorated (see

Frame.setUndecorated(boolean)

and

Dialog.setUndecorated(boolean)

)

The window must not be in full-screen mode (see

GraphicsDevice.setFullScreenWindow(Window)

)

If the alpha component of the requested background color is less than

1.0f

, and any of the above conditions are not met, the background
color of this window will not change, the alpha component of the given
background color will not affect the mode of operation for this window,
and either the

UnsupportedOperationException

or

IllegalComponentStateException

will be thrown.

When the window is per-pixel translucent, the drawing sub-system
respects the alpha value of each individual pixel. If a pixel gets
painted with the alpha color component equal to zero, it becomes
visually transparent. If the alpha of the pixel is equal to 1.0f, the
pixel is fully opaque. Interim values of the alpha color component make
the pixel semi-transparent. In this mode, the background of the window
gets painted with the alpha value of the given background color. If the
alpha value of the argument of this method is equal to

0

, the
background is not painted at all.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

When the window is per-pixel translucent, the drawing sub-system
respects the alpha value of each individual pixel. If a pixel gets
painted with the alpha color component equal to zero, it becomes
visually transparent. If the alpha of the pixel is equal to 1.0f, the
pixel is fully opaque. Interim values of the alpha color component make
the pixel semi-transparent. In this mode, the background of the window
gets painted with the alpha value of the given background color. If the
alpha value of the argument of this method is equal to

0

, the
background is not painted at all.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

The actual level of translucency of a given pixel also depends on window
opacity (see

setOpacity(float)

), as well as the current shape of
this window (see

setShape(Shape)

).

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

Note that painting a pixel with the alpha value of

0

may or may
not disable the mouse event handling on this pixel. This is a
platform-dependent behavior. To make sure the mouse events do not get
dispatched to a particular pixel, the pixel must be excluded from the
shape of the window.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

Enabling the per-pixel translucency mode may change the graphics
configuration of this window due to the native platform requirements.

isOpaque

```java
public boolean isOpaque()
```

Indicates if the window is currently opaque.

The method returns

false

if the background color of the window
is not

null

and the alpha component of the color is less than

1.0f

. The method returns

true

otherwise.

**Overrides:** isOpaque

in class

Component
**Returns:** true

if the window is opaque,

false

otherwise
**Since:** 1.7
**See Also:** getBackground()

,

setBackground(Color)

---

#### isOpaque

public boolean isOpaque()

Indicates if the window is currently opaque.

The method returns

false

if the background color of the window
is not

null

and the alpha component of the color is less than

1.0f

. The method returns

true

otherwise.

The method returns

false

if the background color of the window
is not

null

and the alpha component of the color is less than

1.0f

. The method returns

true

otherwise.

paint

```java
public void paint​(
Graphics
g)
```

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

**Overrides:** paint

in class

Container
**Parameters:** g

- the specified Graphics window
**Since:** 1.7
**See Also:** Component.update(Graphics)

---

#### paint

public void paint​(

Graphics

g)

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

---

