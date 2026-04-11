# Class TrayIcon

**Source:** `java.desktop\java\awt\TrayIcon.html`

### Class Description

```java
public class
TrayIcon

extends
Object
```

A

TrayIcon

object represents a tray icon that can be
added to the

system tray

. A

TrayIcon

can have a tooltip (text), an image, a popup
menu, and a set of listeners associated with it.

A

TrayIcon

can generate various

MouseEvents

and supports adding corresponding listeners to receive
notification of these events.

TrayIcon

processes some
of the events by itself. For example, by default, when the
right-mouse click is performed on the

TrayIcon

it
displays the specified popup menu. When the mouse hovers
over the

TrayIcon

the tooltip is displayed (this behaviour is
platform dependent).

Note:

When the

MouseEvent

is
dispatched to its registered listeners its

component

property will be set to

null

. (See

ComponentEvent.getComponent()

) The

source

property will be set to this

TrayIcon

. (See

EventObject.getSource()

)

Note:

A well-behaved

TrayIcon

implementation
will assign different gestures to showing a popup menu and
selecting a tray icon.

A

TrayIcon

can generate an

ActionEvent

. On some platforms, this occurs when the user selects
the tray icon using either the mouse or keyboard.

If a SecurityManager is installed, the AWTPermission

accessSystemTray

must be granted in order to create
a

TrayIcon

. Otherwise the constructor will throw a
SecurityException.

See the

SystemTray

class overview for an example on how
to use the

TrayIcon

API.

**Since:** 1.6
**See Also:** SystemTray.add(java.awt.TrayIcon)

,

ComponentEvent.getComponent()

,

EventObject.getSource()

---

### Field Details

*No entries found.*

### Constructor Details

#### public TrayIcon​(
Image
image)

Creates a

TrayIcon

with the specified image.

**Parameters:**
- image

- the

Image

to be used

**Throws:**
- IllegalArgumentException

- if

image

is

null
- UnsupportedOperationException

- if the system tray isn't
supported by the current platform
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
- SecurityException

- if

accessSystemTray

permission
is not granted

**See Also:**
- SystemTray.add(TrayIcon)

,

TrayIcon(Image, String, PopupMenu)

,

TrayIcon(Image, String)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

---

#### public TrayIcon​(
Image
image,

String
tooltip)

Creates a

TrayIcon

with the specified image and
tooltip text. Tooltip may be not visible on some platforms.

**Parameters:**
- image

- the

Image

to be used
- tooltip

- the string to be used as tooltip text; if the
value is

null

no tooltip is shown

**Throws:**
- IllegalArgumentException

- if

image

is

null
- UnsupportedOperationException

- if the system tray isn't
supported by the current platform
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
- SecurityException

- if

accessSystemTray

permission
is not granted

**See Also:**
- SystemTray.add(TrayIcon)

,

TrayIcon(Image)

,

TrayIcon(Image, String, PopupMenu)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

---

#### public TrayIcon​(
Image
image,

String
tooltip,

PopupMenu
popup)

Creates a

TrayIcon

with the specified image,
tooltip and popup menu. Tooltip may be not visible on some platforms.

**Parameters:**
- image

- the

Image

to be used
- tooltip

- the string to be used as tooltip text; if the
value is

null

no tooltip is shown
- popup

- the menu to be used for the tray icon's popup
menu; if the value is

null

no popup menu is shown

**Throws:**
- IllegalArgumentException

- if

image

is

null
- UnsupportedOperationException

- if the system tray isn't
supported by the current platform
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
- SecurityException

- if

accessSystemTray

permission
is not granted

**See Also:**
- SystemTray.add(TrayIcon)

,

TrayIcon(Image, String)

,

TrayIcon(Image)

,

PopupMenu

,

MouseListener

,

addMouseListener(MouseListener)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

---

### Method Details

#### public void setImage​(
Image
image)

Sets the image for this

TrayIcon

. The previous
tray icon image is discarded without calling the

Image.flush()

method — you will need to call it
manually.

If the image represents an animated image, it will be
animated automatically.

See the

setImageAutoSize(boolean)

property for
details on the size of the displayed image.

Calling this method with the same image that is currently
being used has no effect.

**Parameters:**
- image

- the non-null

Image

to be used

**Throws:**
- NullPointerException

- if

image

is

null

**See Also:**
- getImage()

,

Image

,

SystemTray.add(TrayIcon)

,

TrayIcon(Image, String)

---

#### public
Image
getImage()

Returns the current image used for this

TrayIcon

.

**Returns:**
- the image

**See Also:**
- setImage(Image)

,

Image

---

#### public void setPopupMenu​(
PopupMenu
popup)

Sets the popup menu for this

TrayIcon

. If

popup

is

null

, no popup menu will be
associated with this

TrayIcon

.

Note that this

popup

must not be added to any
parent before or after it is set on the tray icon. If you add
it to some parent, the

popup

may be removed from
that parent.

The

popup

can be set on one

TrayIcon

only.
Setting the same popup on multiple

TrayIcon

s will cause
an

IllegalArgumentException

.

Note:

Some platforms may not support
showing the user-specified popup menu component when the user
right-clicks the tray icon. In this situation, either no menu
will be displayed or, on some systems, a native version of the
menu may be displayed.

**Parameters:**
- popup

- a

PopupMenu

or

null

to
remove any popup menu

**Throws:**
- IllegalArgumentException

- if the

popup

is already
set for another

TrayIcon

**See Also:**
- getPopupMenu()

---

#### public
PopupMenu
getPopupMenu()

Returns the popup menu associated with this

TrayIcon

.

**Returns:**
- the popup menu or

null

if none exists

**See Also:**
- setPopupMenu(PopupMenu)

---

#### public void setToolTip​(
String
tooltip)

Sets the tooltip string for this

TrayIcon

. The
tooltip is displayed automatically when the mouse hovers over
the icon. Tooltip may be not visible on some platforms.
Setting the tooltip to

null

removes any tooltip text.

When displayed, the tooltip string may be truncated on some platforms;
the number of characters that may be displayed is platform-dependent.

**Parameters:**
- tooltip

- the string for the tooltip; if the value is

null

no tooltip is shown

**See Also:**
- getToolTip()

---

#### public
String
getToolTip()

Returns the tooltip string associated with this

TrayIcon

.

**Returns:**
- the tooltip string or

null

if none exists

**See Also:**
- setToolTip(String)

---

#### public void setImageAutoSize​(boolean autosize)

Sets the auto-size property. Auto-size determines whether the
tray image is automatically sized to fit the space allocated
for the image on the tray. By default, the auto-size property
is set to

false

.

If auto-size is

false

, and the image size
doesn't match the tray icon space, the image is painted as-is
inside that space — if larger than the allocated space, it will
be cropped.

If auto-size is

true

, the image is stretched or shrunk to
fit the tray icon space.

**Parameters:**
- autosize

-

true

to auto-size the image,

false

otherwise

**See Also:**
- isImageAutoSize()

---

#### public boolean isImageAutoSize()

Returns the value of the auto-size property.

**Returns:**
- true

if the image will be auto-sized,

false

otherwise

**See Also:**
- setImageAutoSize(boolean)

---

#### public void addMouseListener​(
MouseListener
listener)

Adds the specified mouse listener to receive mouse events from
this

TrayIcon

. Calling this method with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_ENTERED

and

MOUSE_EXITED

mouse events are not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- listener

- the mouse listener

**See Also:**
- MouseEvent

,

MouseListener

,

removeMouseListener(MouseListener)

,

getMouseListeners()

---

#### public void removeMouseListener​(
MouseListener
listener)

Removes the specified mouse listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- listener

- the mouse listener

**See Also:**
- MouseEvent

,

MouseListener

,

addMouseListener(MouseListener)

,

getMouseListeners()

---

#### public
MouseListener
[] getMouseListeners()

Returns an array of all the mouse listeners
registered on this

TrayIcon

.

**Returns:**
- all of the

MouseListeners

registered on
this

TrayIcon

or an empty array if no mouse
listeners are currently registered

**See Also:**
- addMouseListener(MouseListener)

,

removeMouseListener(MouseListener)

,

MouseListener

---

#### public void addMouseMotionListener​(
MouseMotionListener
listener)

Adds the specified mouse listener to receive mouse-motion
events from this

TrayIcon

. Calling this method
with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_DRAGGED

mouse event is not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- listener

- the mouse listener

**See Also:**
- MouseEvent

,

MouseMotionListener

,

removeMouseMotionListener(MouseMotionListener)

,

getMouseMotionListeners()

---

#### public void removeMouseMotionListener​(
MouseMotionListener
listener)

Removes the specified mouse-motion listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- listener

- the mouse listener

**See Also:**
- MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(MouseMotionListener)

,

getMouseMotionListeners()

---

#### public
MouseMotionListener
[] getMouseMotionListeners()

Returns an array of all the mouse-motion listeners
registered on this

TrayIcon

.

**Returns:**
- all of the

MouseInputListeners

registered on
this

TrayIcon

or an empty array if no mouse
listeners are currently registered

**See Also:**
- addMouseMotionListener(MouseMotionListener)

,

removeMouseMotionListener(MouseMotionListener)

,

MouseMotionListener

---

#### public
String
getActionCommand()

Returns the command name of the action event fired by this tray icon.

**Returns:**
- the action command name, or

null

if none exists

**See Also:**
- addActionListener(ActionListener)

,

setActionCommand(String)

---

#### public void setActionCommand​(
String
command)

Sets the command name for the action event fired by this tray
icon. By default, this action command is set to

null

.

**Parameters:**
- command

- a string used to set the tray icon's
action command.

**See Also:**
- ActionEvent

,

addActionListener(ActionListener)

,

getActionCommand()

---

#### public void addActionListener​(
ActionListener
listener)

Adds the specified action listener to receive

ActionEvent

s from this

TrayIcon

.
Action events usually occur when a user selects the tray icon,
using either the mouse or keyboard. The conditions in which
action events are generated are platform-dependent.

Calling this method with a

null

value has no
effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- listener

- the action listener

**See Also:**
- removeActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionListener

,

setActionCommand(String)

---

#### public void removeActionListener​(
ActionListener
listener)

Removes the specified action listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- listener

- the action listener

**See Also:**
- ActionEvent

,

ActionListener

,

addActionListener(ActionListener)

,

getActionListeners()

,

setActionCommand(String)

---

#### public
ActionListener
[] getActionListeners()

Returns an array of all the action listeners
registered on this

TrayIcon

.

**Returns:**
- all of the

ActionListeners

registered on
this

TrayIcon

or an empty array if no action
listeners are currently registered

**See Also:**
- addActionListener(ActionListener)

,

removeActionListener(ActionListener)

,

ActionListener

---

#### public void displayMessage​(
String
caption,

String
text,

TrayIcon.MessageType
messageType)

Displays a popup message near the tray icon. The message will
disappear after a time or if the user clicks on it. Clicking
on the message may trigger an

ActionEvent

.

Either the caption or the text may be

null

, but an

NullPointerException

is thrown if both are

null

.

When displayed, the caption or text strings may be truncated on
some platforms; the number of characters that may be displayed is
platform-dependent.

Note:

Some platforms may not support
showing a message.

**Parameters:**
- caption

- the caption displayed above the text, usually in
bold; may be

null
- text

- the text displayed for the particular message; may be

null
- messageType

- an enum indicating the message type

**Throws:**
- NullPointerException

- if both

caption

and

text

are

null

---

#### public
Dimension
getSize()

Returns the size, in pixels, of the space that the tray icon
occupies in the system tray. For the tray icon that is not yet
added to the system tray, the returned size is equal to the
result of the

SystemTray.getTrayIconSize()

.

**Returns:**
- the size of the tray icon, in pixels

**See Also:**
- setImageAutoSize(boolean)

,

Image

,

getSize()

---

### Additional Sections

#### Class TrayIcon

java.lang.Object

- java.awt.TrayIcon

java.awt.TrayIcon

```java
public class
TrayIcon

extends
Object
```

A

TrayIcon

object represents a tray icon that can be
added to the

system tray

. A

TrayIcon

can have a tooltip (text), an image, a popup
menu, and a set of listeners associated with it.

A

TrayIcon

can generate various

MouseEvents

and supports adding corresponding listeners to receive
notification of these events.

TrayIcon

processes some
of the events by itself. For example, by default, when the
right-mouse click is performed on the

TrayIcon

it
displays the specified popup menu. When the mouse hovers
over the

TrayIcon

the tooltip is displayed (this behaviour is
platform dependent).

Note:

When the

MouseEvent

is
dispatched to its registered listeners its

component

property will be set to

null

. (See

ComponentEvent.getComponent()

) The

source

property will be set to this

TrayIcon

. (See

EventObject.getSource()

)

Note:

A well-behaved

TrayIcon

implementation
will assign different gestures to showing a popup menu and
selecting a tray icon.

A

TrayIcon

can generate an

ActionEvent

. On some platforms, this occurs when the user selects
the tray icon using either the mouse or keyboard.

If a SecurityManager is installed, the AWTPermission

accessSystemTray

must be granted in order to create
a

TrayIcon

. Otherwise the constructor will throw a
SecurityException.

See the

SystemTray

class overview for an example on how
to use the

TrayIcon

API.

**Since:** 1.6
**See Also:** SystemTray.add(java.awt.TrayIcon)

,

ComponentEvent.getComponent()

,

EventObject.getSource()

public class

TrayIcon

extends

Object

A

TrayIcon

object represents a tray icon that can be
added to the

system tray

. A

TrayIcon

can have a tooltip (text), an image, a popup
menu, and a set of listeners associated with it.

A

TrayIcon

can generate various

MouseEvents

and supports adding corresponding listeners to receive
notification of these events.

TrayIcon

processes some
of the events by itself. For example, by default, when the
right-mouse click is performed on the

TrayIcon

it
displays the specified popup menu. When the mouse hovers
over the

TrayIcon

the tooltip is displayed (this behaviour is
platform dependent).

Note:

When the

MouseEvent

is
dispatched to its registered listeners its

component

property will be set to

null

. (See

ComponentEvent.getComponent()

) The

source

property will be set to this

TrayIcon

. (See

EventObject.getSource()

)

Note:

A well-behaved

TrayIcon

implementation
will assign different gestures to showing a popup menu and
selecting a tray icon.

A

TrayIcon

can generate an

ActionEvent

. On some platforms, this occurs when the user selects
the tray icon using either the mouse or keyboard.

If a SecurityManager is installed, the AWTPermission

accessSystemTray

must be granted in order to create
a

TrayIcon

. Otherwise the constructor will throw a
SecurityException.

See the

SystemTray

class overview for an example on how
to use the

TrayIcon

API.

A

TrayIcon

can generate various

MouseEvents

and supports adding corresponding listeners to receive
notification of these events.

TrayIcon

processes some
of the events by itself. For example, by default, when the
right-mouse click is performed on the

TrayIcon

it
displays the specified popup menu. When the mouse hovers
over the

TrayIcon

the tooltip is displayed (this behaviour is
platform dependent).

Note:

When the

MouseEvent

is
dispatched to its registered listeners its

component

property will be set to

null

. (See

ComponentEvent.getComponent()

) The

source

property will be set to this

TrayIcon

. (See

EventObject.getSource()

)

Note:

A well-behaved

TrayIcon

implementation
will assign different gestures to showing a popup menu and
selecting a tray icon.

A

TrayIcon

can generate an

ActionEvent

. On some platforms, this occurs when the user selects
the tray icon using either the mouse or keyboard.

If a SecurityManager is installed, the AWTPermission

accessSystemTray

must be granted in order to create
a

TrayIcon

. Otherwise the constructor will throw a
SecurityException.

See the

SystemTray

class overview for an example on how
to use the

TrayIcon

API.

Note:

When the

MouseEvent

is
dispatched to its registered listeners its

component

property will be set to

null

. (See

ComponentEvent.getComponent()

) The

source

property will be set to this

TrayIcon

. (See

EventObject.getSource()

)

Note:

A well-behaved

TrayIcon

implementation
will assign different gestures to showing a popup menu and
selecting a tray icon.

A

TrayIcon

can generate an

ActionEvent

. On some platforms, this occurs when the user selects
the tray icon using either the mouse or keyboard.

If a SecurityManager is installed, the AWTPermission

accessSystemTray

must be granted in order to create
a

TrayIcon

. Otherwise the constructor will throw a
SecurityException.

See the

SystemTray

class overview for an example on how
to use the

TrayIcon

API.

Note:

A well-behaved

TrayIcon

implementation
will assign different gestures to showing a popup menu and
selecting a tray icon.

A

TrayIcon

can generate an

ActionEvent

. On some platforms, this occurs when the user selects
the tray icon using either the mouse or keyboard.

If a SecurityManager is installed, the AWTPermission

accessSystemTray

must be granted in order to create
a

TrayIcon

. Otherwise the constructor will throw a
SecurityException.

See the

SystemTray

class overview for an example on how
to use the

TrayIcon

API.

A

TrayIcon

can generate an

ActionEvent

. On some platforms, this occurs when the user selects
the tray icon using either the mouse or keyboard.

If a SecurityManager is installed, the AWTPermission

accessSystemTray

must be granted in order to create
a

TrayIcon

. Otherwise the constructor will throw a
SecurityException.

See the

SystemTray

class overview for an example on how
to use the

TrayIcon

API.

If a SecurityManager is installed, the AWTPermission

accessSystemTray

must be granted in order to create
a

TrayIcon

. Otherwise the constructor will throw a
SecurityException.

See the

SystemTray

class overview for an example on how
to use the

TrayIcon

API.

See the

SystemTray

class overview for an example on how
to use the

TrayIcon

API.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

TrayIcon.MessageType

The message type determines which icon will be displayed in the
caption of the message, and a possible system sound a message
may generate upon showing.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TrayIcon

​(

Image

image)

Creates a

TrayIcon

with the specified image.

TrayIcon

​(

Image

image,

String

tooltip)

Creates a

TrayIcon

with the specified image and
tooltip text.

TrayIcon

​(

Image

image,

String

tooltip,

PopupMenu

popup)

Creates a

TrayIcon

with the specified image,
tooltip and popup menu.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addActionListener

​(

ActionListener

listener)

Adds the specified action listener to receive

ActionEvent

s from this

TrayIcon

.

void

addMouseListener

​(

MouseListener

listener)

Adds the specified mouse listener to receive mouse events from
this

TrayIcon

.

void

addMouseMotionListener

​(

MouseMotionListener

listener)

Adds the specified mouse listener to receive mouse-motion
events from this

TrayIcon

.

void

displayMessage

​(

String

caption,

String

text,

TrayIcon.MessageType

messageType)

Displays a popup message near the tray icon.

String

getActionCommand

()

Returns the command name of the action event fired by this tray icon.

ActionListener

[]

getActionListeners

()

Returns an array of all the action listeners
registered on this

TrayIcon

.

Image

getImage

()

Returns the current image used for this

TrayIcon

.

MouseListener

[]

getMouseListeners

()

Returns an array of all the mouse listeners
registered on this

TrayIcon

.

MouseMotionListener

[]

getMouseMotionListeners

()

Returns an array of all the mouse-motion listeners
registered on this

TrayIcon

.

PopupMenu

getPopupMenu

()

Returns the popup menu associated with this

TrayIcon

.

Dimension

getSize

()

Returns the size, in pixels, of the space that the tray icon
occupies in the system tray.

String

getToolTip

()

Returns the tooltip string associated with this

TrayIcon

.

boolean

isImageAutoSize

()

Returns the value of the auto-size property.

void

removeActionListener

​(

ActionListener

listener)

Removes the specified action listener.

void

removeMouseListener

​(

MouseListener

listener)

Removes the specified mouse listener.

void

removeMouseMotionListener

​(

MouseMotionListener

listener)

Removes the specified mouse-motion listener.

void

setActionCommand

​(

String

command)

Sets the command name for the action event fired by this tray
icon.

void

setImage

​(

Image

image)

Sets the image for this

TrayIcon

.

void

setImageAutoSize

​(boolean autosize)

Sets the auto-size property.

void

setPopupMenu

​(

PopupMenu

popup)

Sets the popup menu for this

TrayIcon

.

void

setToolTip

​(

String

tooltip)

Sets the tooltip string for this

TrayIcon

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

TrayIcon.MessageType

The message type determines which icon will be displayed in the
caption of the message, and a possible system sound a message
may generate upon showing.

---

#### Nested Class Summary

The message type determines which icon will be displayed in the
caption of the message, and a possible system sound a message
may generate upon showing.

Constructor Summary

Constructors

Constructor

Description

TrayIcon

​(

Image

image)

Creates a

TrayIcon

with the specified image.

TrayIcon

​(

Image

image,

String

tooltip)

Creates a

TrayIcon

with the specified image and
tooltip text.

TrayIcon

​(

Image

image,

String

tooltip,

PopupMenu

popup)

Creates a

TrayIcon

with the specified image,
tooltip and popup menu.

---

#### Constructor Summary

Creates a

TrayIcon

with the specified image.

Creates a

TrayIcon

with the specified image and
tooltip text.

Creates a

TrayIcon

with the specified image,
tooltip and popup menu.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addActionListener

​(

ActionListener

listener)

Adds the specified action listener to receive

ActionEvent

s from this

TrayIcon

.

void

addMouseListener

​(

MouseListener

listener)

Adds the specified mouse listener to receive mouse events from
this

TrayIcon

.

void

addMouseMotionListener

​(

MouseMotionListener

listener)

Adds the specified mouse listener to receive mouse-motion
events from this

TrayIcon

.

void

displayMessage

​(

String

caption,

String

text,

TrayIcon.MessageType

messageType)

Displays a popup message near the tray icon.

String

getActionCommand

()

Returns the command name of the action event fired by this tray icon.

ActionListener

[]

getActionListeners

()

Returns an array of all the action listeners
registered on this

TrayIcon

.

Image

getImage

()

Returns the current image used for this

TrayIcon

.

MouseListener

[]

getMouseListeners

()

Returns an array of all the mouse listeners
registered on this

TrayIcon

.

MouseMotionListener

[]

getMouseMotionListeners

()

Returns an array of all the mouse-motion listeners
registered on this

TrayIcon

.

PopupMenu

getPopupMenu

()

Returns the popup menu associated with this

TrayIcon

.

Dimension

getSize

()

Returns the size, in pixels, of the space that the tray icon
occupies in the system tray.

String

getToolTip

()

Returns the tooltip string associated with this

TrayIcon

.

boolean

isImageAutoSize

()

Returns the value of the auto-size property.

void

removeActionListener

​(

ActionListener

listener)

Removes the specified action listener.

void

removeMouseListener

​(

MouseListener

listener)

Removes the specified mouse listener.

void

removeMouseMotionListener

​(

MouseMotionListener

listener)

Removes the specified mouse-motion listener.

void

setActionCommand

​(

String

command)

Sets the command name for the action event fired by this tray
icon.

void

setImage

​(

Image

image)

Sets the image for this

TrayIcon

.

void

setImageAutoSize

​(boolean autosize)

Sets the auto-size property.

void

setPopupMenu

​(

PopupMenu

popup)

Sets the popup menu for this

TrayIcon

.

void

setToolTip

​(

String

tooltip)

Sets the tooltip string for this

TrayIcon

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

Adds the specified action listener to receive

ActionEvent

s from this

TrayIcon

.

Adds the specified mouse listener to receive mouse events from
this

TrayIcon

.

Adds the specified mouse listener to receive mouse-motion
events from this

TrayIcon

.

Displays a popup message near the tray icon.

Returns the command name of the action event fired by this tray icon.

Returns an array of all the action listeners
registered on this

TrayIcon

.

Returns the current image used for this

TrayIcon

.

Returns an array of all the mouse listeners
registered on this

TrayIcon

.

Returns an array of all the mouse-motion listeners
registered on this

TrayIcon

.

Returns the popup menu associated with this

TrayIcon

.

Returns the size, in pixels, of the space that the tray icon
occupies in the system tray.

Returns the tooltip string associated with this

TrayIcon

.

Returns the value of the auto-size property.

Removes the specified action listener.

Removes the specified mouse listener.

Removes the specified mouse-motion listener.

Sets the command name for the action event fired by this tray
icon.

Sets the image for this

TrayIcon

.

Sets the auto-size property.

Sets the popup menu for this

TrayIcon

.

Sets the tooltip string for this

TrayIcon

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TrayIcon

```java
public TrayIcon​(
Image
image)
```

Creates a

TrayIcon

with the specified image.

**Parameters:** image

- the

Image

to be used
**Throws:** IllegalArgumentException

- if

image

is

null
**Throws:** UnsupportedOperationException

- if the system tray isn't
supported by the current platform
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if

accessSystemTray

permission
is not granted
**See Also:** SystemTray.add(TrayIcon)

,

TrayIcon(Image, String, PopupMenu)

,

TrayIcon(Image, String)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

- TrayIcon

```java
public TrayIcon​(
Image
image,

String
tooltip)
```

Creates a

TrayIcon

with the specified image and
tooltip text. Tooltip may be not visible on some platforms.

**Parameters:** image

- the

Image

to be used
**Parameters:** tooltip

- the string to be used as tooltip text; if the
value is

null

no tooltip is shown
**Throws:** IllegalArgumentException

- if

image

is

null
**Throws:** UnsupportedOperationException

- if the system tray isn't
supported by the current platform
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if

accessSystemTray

permission
is not granted
**See Also:** SystemTray.add(TrayIcon)

,

TrayIcon(Image)

,

TrayIcon(Image, String, PopupMenu)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

- TrayIcon

```java
public TrayIcon​(
Image
image,

String
tooltip,

PopupMenu
popup)
```

Creates a

TrayIcon

with the specified image,
tooltip and popup menu. Tooltip may be not visible on some platforms.

**Parameters:** image

- the

Image

to be used
**Parameters:** tooltip

- the string to be used as tooltip text; if the
value is

null

no tooltip is shown
**Parameters:** popup

- the menu to be used for the tray icon's popup
menu; if the value is

null

no popup menu is shown
**Throws:** IllegalArgumentException

- if

image

is

null
**Throws:** UnsupportedOperationException

- if the system tray isn't
supported by the current platform
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if

accessSystemTray

permission
is not granted
**See Also:** SystemTray.add(TrayIcon)

,

TrayIcon(Image, String)

,

TrayIcon(Image)

,

PopupMenu

,

MouseListener

,

addMouseListener(MouseListener)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

============ METHOD DETAIL ==========

- Method Detail

- setImage

```java
public void setImage​(
Image
image)
```

Sets the image for this

TrayIcon

. The previous
tray icon image is discarded without calling the

Image.flush()

method — you will need to call it
manually.

If the image represents an animated image, it will be
animated automatically.

See the

setImageAutoSize(boolean)

property for
details on the size of the displayed image.

Calling this method with the same image that is currently
being used has no effect.

**Parameters:** image

- the non-null

Image

to be used
**Throws:** NullPointerException

- if

image

is

null
**See Also:** getImage()

,

Image

,

SystemTray.add(TrayIcon)

,

TrayIcon(Image, String)

- getImage

```java
public
Image
getImage()
```

Returns the current image used for this

TrayIcon

.

**Returns:** the image
**See Also:** setImage(Image)

,

Image

- setPopupMenu

```java
public void setPopupMenu​(
PopupMenu
popup)
```

Sets the popup menu for this

TrayIcon

. If

popup

is

null

, no popup menu will be
associated with this

TrayIcon

.

Note that this

popup

must not be added to any
parent before or after it is set on the tray icon. If you add
it to some parent, the

popup

may be removed from
that parent.

The

popup

can be set on one

TrayIcon

only.
Setting the same popup on multiple

TrayIcon

s will cause
an

IllegalArgumentException

.

Note:

Some platforms may not support
showing the user-specified popup menu component when the user
right-clicks the tray icon. In this situation, either no menu
will be displayed or, on some systems, a native version of the
menu may be displayed.

**Parameters:** popup

- a

PopupMenu

or

null

to
remove any popup menu
**Throws:** IllegalArgumentException

- if the

popup

is already
set for another

TrayIcon
**See Also:** getPopupMenu()

- getPopupMenu

```java
public
PopupMenu
getPopupMenu()
```

Returns the popup menu associated with this

TrayIcon

.

**Returns:** the popup menu or

null

if none exists
**See Also:** setPopupMenu(PopupMenu)

- setToolTip

```java
public void setToolTip​(
String
tooltip)
```

Sets the tooltip string for this

TrayIcon

. The
tooltip is displayed automatically when the mouse hovers over
the icon. Tooltip may be not visible on some platforms.
Setting the tooltip to

null

removes any tooltip text.

When displayed, the tooltip string may be truncated on some platforms;
the number of characters that may be displayed is platform-dependent.

**Parameters:** tooltip

- the string for the tooltip; if the value is

null

no tooltip is shown
**See Also:** getToolTip()

- getToolTip

```java
public
String
getToolTip()
```

Returns the tooltip string associated with this

TrayIcon

.

**Returns:** the tooltip string or

null

if none exists
**See Also:** setToolTip(String)

- setImageAutoSize

```java
public void setImageAutoSize​(boolean autosize)
```

Sets the auto-size property. Auto-size determines whether the
tray image is automatically sized to fit the space allocated
for the image on the tray. By default, the auto-size property
is set to

false

.

If auto-size is

false

, and the image size
doesn't match the tray icon space, the image is painted as-is
inside that space — if larger than the allocated space, it will
be cropped.

If auto-size is

true

, the image is stretched or shrunk to
fit the tray icon space.

**Parameters:** autosize

-

true

to auto-size the image,

false

otherwise
**See Also:** isImageAutoSize()

- isImageAutoSize

```java
public boolean isImageAutoSize()
```

Returns the value of the auto-size property.

**Returns:** true

if the image will be auto-sized,

false

otherwise
**See Also:** setImageAutoSize(boolean)

- addMouseListener

```java
public void addMouseListener​(
MouseListener
listener)
```

Adds the specified mouse listener to receive mouse events from
this

TrayIcon

. Calling this method with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_ENTERED

and

MOUSE_EXITED

mouse events are not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseListener

,

removeMouseListener(MouseListener)

,

getMouseListeners()

- removeMouseListener

```java
public void removeMouseListener​(
MouseListener
listener)
```

Removes the specified mouse listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseListener

,

addMouseListener(MouseListener)

,

getMouseListeners()

- getMouseListeners

```java
public
MouseListener
[] getMouseListeners()
```

Returns an array of all the mouse listeners
registered on this

TrayIcon

.

**Returns:** all of the

MouseListeners

registered on
this

TrayIcon

or an empty array if no mouse
listeners are currently registered
**See Also:** addMouseListener(MouseListener)

,

removeMouseListener(MouseListener)

,

MouseListener

- addMouseMotionListener

```java
public void addMouseMotionListener​(
MouseMotionListener
listener)
```

Adds the specified mouse listener to receive mouse-motion
events from this

TrayIcon

. Calling this method
with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_DRAGGED

mouse event is not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseMotionListener

,

removeMouseMotionListener(MouseMotionListener)

,

getMouseMotionListeners()

- removeMouseMotionListener

```java
public void removeMouseMotionListener​(
MouseMotionListener
listener)
```

Removes the specified mouse-motion listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(MouseMotionListener)

,

getMouseMotionListeners()

- getMouseMotionListeners

```java
public
MouseMotionListener
[] getMouseMotionListeners()
```

Returns an array of all the mouse-motion listeners
registered on this

TrayIcon

.

**Returns:** all of the

MouseInputListeners

registered on
this

TrayIcon

or an empty array if no mouse
listeners are currently registered
**See Also:** addMouseMotionListener(MouseMotionListener)

,

removeMouseMotionListener(MouseMotionListener)

,

MouseMotionListener

- getActionCommand

```java
public
String
getActionCommand()
```

Returns the command name of the action event fired by this tray icon.

**Returns:** the action command name, or

null

if none exists
**See Also:** addActionListener(ActionListener)

,

setActionCommand(String)

- setActionCommand

```java
public void setActionCommand​(
String
command)
```

Sets the command name for the action event fired by this tray
icon. By default, this action command is set to

null

.

**Parameters:** command

- a string used to set the tray icon's
action command.
**See Also:** ActionEvent

,

addActionListener(ActionListener)

,

getActionCommand()

- addActionListener

```java
public void addActionListener​(
ActionListener
listener)
```

Adds the specified action listener to receive

ActionEvent

s from this

TrayIcon

.
Action events usually occur when a user selects the tray icon,
using either the mouse or keyboard. The conditions in which
action events are generated are platform-dependent.

Calling this method with a

null

value has no
effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the action listener
**See Also:** removeActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionListener

,

setActionCommand(String)

- removeActionListener

```java
public void removeActionListener​(
ActionListener
listener)
```

Removes the specified action listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the action listener
**See Also:** ActionEvent

,

ActionListener

,

addActionListener(ActionListener)

,

getActionListeners()

,

setActionCommand(String)

- getActionListeners

```java
public
ActionListener
[] getActionListeners()
```

Returns an array of all the action listeners
registered on this

TrayIcon

.

**Returns:** all of the

ActionListeners

registered on
this

TrayIcon

or an empty array if no action
listeners are currently registered
**See Also:** addActionListener(ActionListener)

,

removeActionListener(ActionListener)

,

ActionListener

- displayMessage

```java
public void displayMessage​(
String
caption,

String
text,

TrayIcon.MessageType
messageType)
```

Displays a popup message near the tray icon. The message will
disappear after a time or if the user clicks on it. Clicking
on the message may trigger an

ActionEvent

.

Either the caption or the text may be

null

, but an

NullPointerException

is thrown if both are

null

.

When displayed, the caption or text strings may be truncated on
some platforms; the number of characters that may be displayed is
platform-dependent.

Note:

Some platforms may not support
showing a message.

**Parameters:** caption

- the caption displayed above the text, usually in
bold; may be

null
**Parameters:** text

- the text displayed for the particular message; may be

null
**Parameters:** messageType

- an enum indicating the message type
**Throws:** NullPointerException

- if both

caption

and

text

are

null

- getSize

```java
public
Dimension
getSize()
```

Returns the size, in pixels, of the space that the tray icon
occupies in the system tray. For the tray icon that is not yet
added to the system tray, the returned size is equal to the
result of the

SystemTray.getTrayIconSize()

.

**Returns:** the size of the tray icon, in pixels
**See Also:** setImageAutoSize(boolean)

,

Image

,

getSize()

Constructor Detail

- TrayIcon

```java
public TrayIcon​(
Image
image)
```

Creates a

TrayIcon

with the specified image.

**Parameters:** image

- the

Image

to be used
**Throws:** IllegalArgumentException

- if

image

is

null
**Throws:** UnsupportedOperationException

- if the system tray isn't
supported by the current platform
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if

accessSystemTray

permission
is not granted
**See Also:** SystemTray.add(TrayIcon)

,

TrayIcon(Image, String, PopupMenu)

,

TrayIcon(Image, String)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

- TrayIcon

```java
public TrayIcon​(
Image
image,

String
tooltip)
```

Creates a

TrayIcon

with the specified image and
tooltip text. Tooltip may be not visible on some platforms.

**Parameters:** image

- the

Image

to be used
**Parameters:** tooltip

- the string to be used as tooltip text; if the
value is

null

no tooltip is shown
**Throws:** IllegalArgumentException

- if

image

is

null
**Throws:** UnsupportedOperationException

- if the system tray isn't
supported by the current platform
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if

accessSystemTray

permission
is not granted
**See Also:** SystemTray.add(TrayIcon)

,

TrayIcon(Image)

,

TrayIcon(Image, String, PopupMenu)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

- TrayIcon

```java
public TrayIcon​(
Image
image,

String
tooltip,

PopupMenu
popup)
```

Creates a

TrayIcon

with the specified image,
tooltip and popup menu. Tooltip may be not visible on some platforms.

**Parameters:** image

- the

Image

to be used
**Parameters:** tooltip

- the string to be used as tooltip text; if the
value is

null

no tooltip is shown
**Parameters:** popup

- the menu to be used for the tray icon's popup
menu; if the value is

null

no popup menu is shown
**Throws:** IllegalArgumentException

- if

image

is

null
**Throws:** UnsupportedOperationException

- if the system tray isn't
supported by the current platform
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if

accessSystemTray

permission
is not granted
**See Also:** SystemTray.add(TrayIcon)

,

TrayIcon(Image, String)

,

TrayIcon(Image)

,

PopupMenu

,

MouseListener

,

addMouseListener(MouseListener)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

---

#### Constructor Detail

TrayIcon

```java
public TrayIcon​(
Image
image)
```

Creates a

TrayIcon

with the specified image.

**Parameters:** image

- the

Image

to be used
**Throws:** IllegalArgumentException

- if

image

is

null
**Throws:** UnsupportedOperationException

- if the system tray isn't
supported by the current platform
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if

accessSystemTray

permission
is not granted
**See Also:** SystemTray.add(TrayIcon)

,

TrayIcon(Image, String, PopupMenu)

,

TrayIcon(Image, String)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

---

#### TrayIcon

public TrayIcon​(

Image

image)

Creates a

TrayIcon

with the specified image.

TrayIcon

```java
public TrayIcon​(
Image
image,

String
tooltip)
```

Creates a

TrayIcon

with the specified image and
tooltip text. Tooltip may be not visible on some platforms.

**Parameters:** image

- the

Image

to be used
**Parameters:** tooltip

- the string to be used as tooltip text; if the
value is

null

no tooltip is shown
**Throws:** IllegalArgumentException

- if

image

is

null
**Throws:** UnsupportedOperationException

- if the system tray isn't
supported by the current platform
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if

accessSystemTray

permission
is not granted
**See Also:** SystemTray.add(TrayIcon)

,

TrayIcon(Image)

,

TrayIcon(Image, String, PopupMenu)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

---

#### TrayIcon

public TrayIcon​(

Image

image,

String

tooltip)

Creates a

TrayIcon

with the specified image and
tooltip text. Tooltip may be not visible on some platforms.

TrayIcon

```java
public TrayIcon​(
Image
image,

String
tooltip,

PopupMenu
popup)
```

Creates a

TrayIcon

with the specified image,
tooltip and popup menu. Tooltip may be not visible on some platforms.

**Parameters:** image

- the

Image

to be used
**Parameters:** tooltip

- the string to be used as tooltip text; if the
value is

null

no tooltip is shown
**Parameters:** popup

- the menu to be used for the tray icon's popup
menu; if the value is

null

no popup menu is shown
**Throws:** IllegalArgumentException

- if

image

is

null
**Throws:** UnsupportedOperationException

- if the system tray isn't
supported by the current platform
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if

accessSystemTray

permission
is not granted
**See Also:** SystemTray.add(TrayIcon)

,

TrayIcon(Image, String)

,

TrayIcon(Image)

,

PopupMenu

,

MouseListener

,

addMouseListener(MouseListener)

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

---

#### TrayIcon

public TrayIcon​(

Image

image,

String

tooltip,

PopupMenu

popup)

Creates a

TrayIcon

with the specified image,
tooltip and popup menu. Tooltip may be not visible on some platforms.

Method Detail

- setImage

```java
public void setImage​(
Image
image)
```

Sets the image for this

TrayIcon

. The previous
tray icon image is discarded without calling the

Image.flush()

method — you will need to call it
manually.

If the image represents an animated image, it will be
animated automatically.

See the

setImageAutoSize(boolean)

property for
details on the size of the displayed image.

Calling this method with the same image that is currently
being used has no effect.

**Parameters:** image

- the non-null

Image

to be used
**Throws:** NullPointerException

- if

image

is

null
**See Also:** getImage()

,

Image

,

SystemTray.add(TrayIcon)

,

TrayIcon(Image, String)

- getImage

```java
public
Image
getImage()
```

Returns the current image used for this

TrayIcon

.

**Returns:** the image
**See Also:** setImage(Image)

,

Image

- setPopupMenu

```java
public void setPopupMenu​(
PopupMenu
popup)
```

Sets the popup menu for this

TrayIcon

. If

popup

is

null

, no popup menu will be
associated with this

TrayIcon

.

Note that this

popup

must not be added to any
parent before or after it is set on the tray icon. If you add
it to some parent, the

popup

may be removed from
that parent.

The

popup

can be set on one

TrayIcon

only.
Setting the same popup on multiple

TrayIcon

s will cause
an

IllegalArgumentException

.

Note:

Some platforms may not support
showing the user-specified popup menu component when the user
right-clicks the tray icon. In this situation, either no menu
will be displayed or, on some systems, a native version of the
menu may be displayed.

**Parameters:** popup

- a

PopupMenu

or

null

to
remove any popup menu
**Throws:** IllegalArgumentException

- if the

popup

is already
set for another

TrayIcon
**See Also:** getPopupMenu()

- getPopupMenu

```java
public
PopupMenu
getPopupMenu()
```

Returns the popup menu associated with this

TrayIcon

.

**Returns:** the popup menu or

null

if none exists
**See Also:** setPopupMenu(PopupMenu)

- setToolTip

```java
public void setToolTip​(
String
tooltip)
```

Sets the tooltip string for this

TrayIcon

. The
tooltip is displayed automatically when the mouse hovers over
the icon. Tooltip may be not visible on some platforms.
Setting the tooltip to

null

removes any tooltip text.

When displayed, the tooltip string may be truncated on some platforms;
the number of characters that may be displayed is platform-dependent.

**Parameters:** tooltip

- the string for the tooltip; if the value is

null

no tooltip is shown
**See Also:** getToolTip()

- getToolTip

```java
public
String
getToolTip()
```

Returns the tooltip string associated with this

TrayIcon

.

**Returns:** the tooltip string or

null

if none exists
**See Also:** setToolTip(String)

- setImageAutoSize

```java
public void setImageAutoSize​(boolean autosize)
```

Sets the auto-size property. Auto-size determines whether the
tray image is automatically sized to fit the space allocated
for the image on the tray. By default, the auto-size property
is set to

false

.

If auto-size is

false

, and the image size
doesn't match the tray icon space, the image is painted as-is
inside that space — if larger than the allocated space, it will
be cropped.

If auto-size is

true

, the image is stretched or shrunk to
fit the tray icon space.

**Parameters:** autosize

-

true

to auto-size the image,

false

otherwise
**See Also:** isImageAutoSize()

- isImageAutoSize

```java
public boolean isImageAutoSize()
```

Returns the value of the auto-size property.

**Returns:** true

if the image will be auto-sized,

false

otherwise
**See Also:** setImageAutoSize(boolean)

- addMouseListener

```java
public void addMouseListener​(
MouseListener
listener)
```

Adds the specified mouse listener to receive mouse events from
this

TrayIcon

. Calling this method with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_ENTERED

and

MOUSE_EXITED

mouse events are not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseListener

,

removeMouseListener(MouseListener)

,

getMouseListeners()

- removeMouseListener

```java
public void removeMouseListener​(
MouseListener
listener)
```

Removes the specified mouse listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseListener

,

addMouseListener(MouseListener)

,

getMouseListeners()

- getMouseListeners

```java
public
MouseListener
[] getMouseListeners()
```

Returns an array of all the mouse listeners
registered on this

TrayIcon

.

**Returns:** all of the

MouseListeners

registered on
this

TrayIcon

or an empty array if no mouse
listeners are currently registered
**See Also:** addMouseListener(MouseListener)

,

removeMouseListener(MouseListener)

,

MouseListener

- addMouseMotionListener

```java
public void addMouseMotionListener​(
MouseMotionListener
listener)
```

Adds the specified mouse listener to receive mouse-motion
events from this

TrayIcon

. Calling this method
with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_DRAGGED

mouse event is not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseMotionListener

,

removeMouseMotionListener(MouseMotionListener)

,

getMouseMotionListeners()

- removeMouseMotionListener

```java
public void removeMouseMotionListener​(
MouseMotionListener
listener)
```

Removes the specified mouse-motion listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(MouseMotionListener)

,

getMouseMotionListeners()

- getMouseMotionListeners

```java
public
MouseMotionListener
[] getMouseMotionListeners()
```

Returns an array of all the mouse-motion listeners
registered on this

TrayIcon

.

**Returns:** all of the

MouseInputListeners

registered on
this

TrayIcon

or an empty array if no mouse
listeners are currently registered
**See Also:** addMouseMotionListener(MouseMotionListener)

,

removeMouseMotionListener(MouseMotionListener)

,

MouseMotionListener

- getActionCommand

```java
public
String
getActionCommand()
```

Returns the command name of the action event fired by this tray icon.

**Returns:** the action command name, or

null

if none exists
**See Also:** addActionListener(ActionListener)

,

setActionCommand(String)

- setActionCommand

```java
public void setActionCommand​(
String
command)
```

Sets the command name for the action event fired by this tray
icon. By default, this action command is set to

null

.

**Parameters:** command

- a string used to set the tray icon's
action command.
**See Also:** ActionEvent

,

addActionListener(ActionListener)

,

getActionCommand()

- addActionListener

```java
public void addActionListener​(
ActionListener
listener)
```

Adds the specified action listener to receive

ActionEvent

s from this

TrayIcon

.
Action events usually occur when a user selects the tray icon,
using either the mouse or keyboard. The conditions in which
action events are generated are platform-dependent.

Calling this method with a

null

value has no
effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the action listener
**See Also:** removeActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionListener

,

setActionCommand(String)

- removeActionListener

```java
public void removeActionListener​(
ActionListener
listener)
```

Removes the specified action listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the action listener
**See Also:** ActionEvent

,

ActionListener

,

addActionListener(ActionListener)

,

getActionListeners()

,

setActionCommand(String)

- getActionListeners

```java
public
ActionListener
[] getActionListeners()
```

Returns an array of all the action listeners
registered on this

TrayIcon

.

**Returns:** all of the

ActionListeners

registered on
this

TrayIcon

or an empty array if no action
listeners are currently registered
**See Also:** addActionListener(ActionListener)

,

removeActionListener(ActionListener)

,

ActionListener

- displayMessage

```java
public void displayMessage​(
String
caption,

String
text,

TrayIcon.MessageType
messageType)
```

Displays a popup message near the tray icon. The message will
disappear after a time or if the user clicks on it. Clicking
on the message may trigger an

ActionEvent

.

Either the caption or the text may be

null

, but an

NullPointerException

is thrown if both are

null

.

When displayed, the caption or text strings may be truncated on
some platforms; the number of characters that may be displayed is
platform-dependent.

Note:

Some platforms may not support
showing a message.

**Parameters:** caption

- the caption displayed above the text, usually in
bold; may be

null
**Parameters:** text

- the text displayed for the particular message; may be

null
**Parameters:** messageType

- an enum indicating the message type
**Throws:** NullPointerException

- if both

caption

and

text

are

null

- getSize

```java
public
Dimension
getSize()
```

Returns the size, in pixels, of the space that the tray icon
occupies in the system tray. For the tray icon that is not yet
added to the system tray, the returned size is equal to the
result of the

SystemTray.getTrayIconSize()

.

**Returns:** the size of the tray icon, in pixels
**See Also:** setImageAutoSize(boolean)

,

Image

,

getSize()

---

#### Method Detail

setImage

```java
public void setImage​(
Image
image)
```

Sets the image for this

TrayIcon

. The previous
tray icon image is discarded without calling the

Image.flush()

method — you will need to call it
manually.

If the image represents an animated image, it will be
animated automatically.

See the

setImageAutoSize(boolean)

property for
details on the size of the displayed image.

Calling this method with the same image that is currently
being used has no effect.

**Parameters:** image

- the non-null

Image

to be used
**Throws:** NullPointerException

- if

image

is

null
**See Also:** getImage()

,

Image

,

SystemTray.add(TrayIcon)

,

TrayIcon(Image, String)

---

#### setImage

public void setImage​(

Image

image)

Sets the image for this

TrayIcon

. The previous
tray icon image is discarded without calling the

Image.flush()

method — you will need to call it
manually.

If the image represents an animated image, it will be
animated automatically.

See the

setImageAutoSize(boolean)

property for
details on the size of the displayed image.

Calling this method with the same image that is currently
being used has no effect.

If the image represents an animated image, it will be
animated automatically.

See the

setImageAutoSize(boolean)

property for
details on the size of the displayed image.

Calling this method with the same image that is currently
being used has no effect.

See the

setImageAutoSize(boolean)

property for
details on the size of the displayed image.

Calling this method with the same image that is currently
being used has no effect.

Calling this method with the same image that is currently
being used has no effect.

getImage

```java
public
Image
getImage()
```

Returns the current image used for this

TrayIcon

.

**Returns:** the image
**See Also:** setImage(Image)

,

Image

---

#### getImage

public

Image

getImage()

Returns the current image used for this

TrayIcon

.

setPopupMenu

```java
public void setPopupMenu​(
PopupMenu
popup)
```

Sets the popup menu for this

TrayIcon

. If

popup

is

null

, no popup menu will be
associated with this

TrayIcon

.

Note that this

popup

must not be added to any
parent before or after it is set on the tray icon. If you add
it to some parent, the

popup

may be removed from
that parent.

The

popup

can be set on one

TrayIcon

only.
Setting the same popup on multiple

TrayIcon

s will cause
an

IllegalArgumentException

.

Note:

Some platforms may not support
showing the user-specified popup menu component when the user
right-clicks the tray icon. In this situation, either no menu
will be displayed or, on some systems, a native version of the
menu may be displayed.

**Parameters:** popup

- a

PopupMenu

or

null

to
remove any popup menu
**Throws:** IllegalArgumentException

- if the

popup

is already
set for another

TrayIcon
**See Also:** getPopupMenu()

---

#### setPopupMenu

public void setPopupMenu​(

PopupMenu

popup)

Sets the popup menu for this

TrayIcon

. If

popup

is

null

, no popup menu will be
associated with this

TrayIcon

.

Note that this

popup

must not be added to any
parent before or after it is set on the tray icon. If you add
it to some parent, the

popup

may be removed from
that parent.

The

popup

can be set on one

TrayIcon

only.
Setting the same popup on multiple

TrayIcon

s will cause
an

IllegalArgumentException

.

Note:

Some platforms may not support
showing the user-specified popup menu component when the user
right-clicks the tray icon. In this situation, either no menu
will be displayed or, on some systems, a native version of the
menu may be displayed.

Note that this

popup

must not be added to any
parent before or after it is set on the tray icon. If you add
it to some parent, the

popup

may be removed from
that parent.

The

popup

can be set on one

TrayIcon

only.
Setting the same popup on multiple

TrayIcon

s will cause
an

IllegalArgumentException

.

Note:

Some platforms may not support
showing the user-specified popup menu component when the user
right-clicks the tray icon. In this situation, either no menu
will be displayed or, on some systems, a native version of the
menu may be displayed.

The

popup

can be set on one

TrayIcon

only.
Setting the same popup on multiple

TrayIcon

s will cause
an

IllegalArgumentException

.

Note:

Some platforms may not support
showing the user-specified popup menu component when the user
right-clicks the tray icon. In this situation, either no menu
will be displayed or, on some systems, a native version of the
menu may be displayed.

Note:

Some platforms may not support
showing the user-specified popup menu component when the user
right-clicks the tray icon. In this situation, either no menu
will be displayed or, on some systems, a native version of the
menu may be displayed.

getPopupMenu

```java
public
PopupMenu
getPopupMenu()
```

Returns the popup menu associated with this

TrayIcon

.

**Returns:** the popup menu or

null

if none exists
**See Also:** setPopupMenu(PopupMenu)

---

#### getPopupMenu

public

PopupMenu

getPopupMenu()

Returns the popup menu associated with this

TrayIcon

.

setToolTip

```java
public void setToolTip​(
String
tooltip)
```

Sets the tooltip string for this

TrayIcon

. The
tooltip is displayed automatically when the mouse hovers over
the icon. Tooltip may be not visible on some platforms.
Setting the tooltip to

null

removes any tooltip text.

When displayed, the tooltip string may be truncated on some platforms;
the number of characters that may be displayed is platform-dependent.

**Parameters:** tooltip

- the string for the tooltip; if the value is

null

no tooltip is shown
**See Also:** getToolTip()

---

#### setToolTip

public void setToolTip​(

String

tooltip)

Sets the tooltip string for this

TrayIcon

. The
tooltip is displayed automatically when the mouse hovers over
the icon. Tooltip may be not visible on some platforms.
Setting the tooltip to

null

removes any tooltip text.

When displayed, the tooltip string may be truncated on some platforms;
the number of characters that may be displayed is platform-dependent.

getToolTip

```java
public
String
getToolTip()
```

Returns the tooltip string associated with this

TrayIcon

.

**Returns:** the tooltip string or

null

if none exists
**See Also:** setToolTip(String)

---

#### getToolTip

public

String

getToolTip()

Returns the tooltip string associated with this

TrayIcon

.

setImageAutoSize

```java
public void setImageAutoSize​(boolean autosize)
```

Sets the auto-size property. Auto-size determines whether the
tray image is automatically sized to fit the space allocated
for the image on the tray. By default, the auto-size property
is set to

false

.

If auto-size is

false

, and the image size
doesn't match the tray icon space, the image is painted as-is
inside that space — if larger than the allocated space, it will
be cropped.

If auto-size is

true

, the image is stretched or shrunk to
fit the tray icon space.

**Parameters:** autosize

-

true

to auto-size the image,

false

otherwise
**See Also:** isImageAutoSize()

---

#### setImageAutoSize

public void setImageAutoSize​(boolean autosize)

Sets the auto-size property. Auto-size determines whether the
tray image is automatically sized to fit the space allocated
for the image on the tray. By default, the auto-size property
is set to

false

.

If auto-size is

false

, and the image size
doesn't match the tray icon space, the image is painted as-is
inside that space — if larger than the allocated space, it will
be cropped.

If auto-size is

true

, the image is stretched or shrunk to
fit the tray icon space.

If auto-size is

false

, and the image size
doesn't match the tray icon space, the image is painted as-is
inside that space — if larger than the allocated space, it will
be cropped.

If auto-size is

true

, the image is stretched or shrunk to
fit the tray icon space.

If auto-size is

true

, the image is stretched or shrunk to
fit the tray icon space.

isImageAutoSize

```java
public boolean isImageAutoSize()
```

Returns the value of the auto-size property.

**Returns:** true

if the image will be auto-sized,

false

otherwise
**See Also:** setImageAutoSize(boolean)

---

#### isImageAutoSize

public boolean isImageAutoSize()

Returns the value of the auto-size property.

addMouseListener

```java
public void addMouseListener​(
MouseListener
listener)
```

Adds the specified mouse listener to receive mouse events from
this

TrayIcon

. Calling this method with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_ENTERED

and

MOUSE_EXITED

mouse events are not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseListener

,

removeMouseListener(MouseListener)

,

getMouseListeners()

---

#### addMouseListener

public void addMouseListener​(

MouseListener

listener)

Adds the specified mouse listener to receive mouse events from
this

TrayIcon

. Calling this method with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_ENTERED

and

MOUSE_EXITED

mouse events are not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_ENTERED

and

MOUSE_EXITED

mouse events are not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Note:

The

MOUSE_ENTERED

and

MOUSE_EXITED

mouse events are not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeMouseListener

```java
public void removeMouseListener​(
MouseListener
listener)
```

Removes the specified mouse listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseListener

,

addMouseListener(MouseListener)

,

getMouseListeners()

---

#### removeMouseListener

public void removeMouseListener​(

MouseListener

listener)

Removes the specified mouse listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getMouseListeners

```java
public
MouseListener
[] getMouseListeners()
```

Returns an array of all the mouse listeners
registered on this

TrayIcon

.

**Returns:** all of the

MouseListeners

registered on
this

TrayIcon

or an empty array if no mouse
listeners are currently registered
**See Also:** addMouseListener(MouseListener)

,

removeMouseListener(MouseListener)

,

MouseListener

---

#### getMouseListeners

public

MouseListener

[] getMouseListeners()

Returns an array of all the mouse listeners
registered on this

TrayIcon

.

addMouseMotionListener

```java
public void addMouseMotionListener​(
MouseMotionListener
listener)
```

Adds the specified mouse listener to receive mouse-motion
events from this

TrayIcon

. Calling this method
with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_DRAGGED

mouse event is not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseMotionListener

,

removeMouseMotionListener(MouseMotionListener)

,

getMouseMotionListeners()

---

#### addMouseMotionListener

public void addMouseMotionListener​(

MouseMotionListener

listener)

Adds the specified mouse listener to receive mouse-motion
events from this

TrayIcon

. Calling this method
with a

null

value has no effect.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_DRAGGED

mouse event is not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Note

: The

MouseEvent

's coordinates (received
from the

TrayIcon

) are relative to the screen, not the

TrayIcon

.

Note:

The

MOUSE_DRAGGED

mouse event is not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Note:

The

MOUSE_DRAGGED

mouse event is not supported.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeMouseMotionListener

```java
public void removeMouseMotionListener​(
MouseMotionListener
listener)
```

Removes the specified mouse-motion listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the mouse listener
**See Also:** MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(MouseMotionListener)

,

getMouseMotionListeners()

---

#### removeMouseMotionListener

public void removeMouseMotionListener​(

MouseMotionListener

listener)

Removes the specified mouse-motion listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getMouseMotionListeners

```java
public
MouseMotionListener
[] getMouseMotionListeners()
```

Returns an array of all the mouse-motion listeners
registered on this

TrayIcon

.

**Returns:** all of the

MouseInputListeners

registered on
this

TrayIcon

or an empty array if no mouse
listeners are currently registered
**See Also:** addMouseMotionListener(MouseMotionListener)

,

removeMouseMotionListener(MouseMotionListener)

,

MouseMotionListener

---

#### getMouseMotionListeners

public

MouseMotionListener

[] getMouseMotionListeners()

Returns an array of all the mouse-motion listeners
registered on this

TrayIcon

.

getActionCommand

```java
public
String
getActionCommand()
```

Returns the command name of the action event fired by this tray icon.

**Returns:** the action command name, or

null

if none exists
**See Also:** addActionListener(ActionListener)

,

setActionCommand(String)

---

#### getActionCommand

public

String

getActionCommand()

Returns the command name of the action event fired by this tray icon.

setActionCommand

```java
public void setActionCommand​(
String
command)
```

Sets the command name for the action event fired by this tray
icon. By default, this action command is set to

null

.

**Parameters:** command

- a string used to set the tray icon's
action command.
**See Also:** ActionEvent

,

addActionListener(ActionListener)

,

getActionCommand()

---

#### setActionCommand

public void setActionCommand​(

String

command)

Sets the command name for the action event fired by this tray
icon. By default, this action command is set to

null

.

addActionListener

```java
public void addActionListener​(
ActionListener
listener)
```

Adds the specified action listener to receive

ActionEvent

s from this

TrayIcon

.
Action events usually occur when a user selects the tray icon,
using either the mouse or keyboard. The conditions in which
action events are generated are platform-dependent.

Calling this method with a

null

value has no
effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the action listener
**See Also:** removeActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionListener

,

setActionCommand(String)

---

#### addActionListener

public void addActionListener​(

ActionListener

listener)

Adds the specified action listener to receive

ActionEvent

s from this

TrayIcon

.
Action events usually occur when a user selects the tray icon,
using either the mouse or keyboard. The conditions in which
action events are generated are platform-dependent.

Calling this method with a

null

value has no
effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Calling this method with a

null

value has no
effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeActionListener

```java
public void removeActionListener​(
ActionListener
listener)
```

Removes the specified action listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** listener

- the action listener
**See Also:** ActionEvent

,

ActionListener

,

addActionListener(ActionListener)

,

getActionListeners()

,

setActionCommand(String)

---

#### removeActionListener

public void removeActionListener​(

ActionListener

listener)

Removes the specified action listener. Calling this method with

null

or an invalid value has no effect.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getActionListeners

```java
public
ActionListener
[] getActionListeners()
```

Returns an array of all the action listeners
registered on this

TrayIcon

.

**Returns:** all of the

ActionListeners

registered on
this

TrayIcon

or an empty array if no action
listeners are currently registered
**See Also:** addActionListener(ActionListener)

,

removeActionListener(ActionListener)

,

ActionListener

---

#### getActionListeners

public

ActionListener

[] getActionListeners()

Returns an array of all the action listeners
registered on this

TrayIcon

.

displayMessage

```java
public void displayMessage​(
String
caption,

String
text,

TrayIcon.MessageType
messageType)
```

Displays a popup message near the tray icon. The message will
disappear after a time or if the user clicks on it. Clicking
on the message may trigger an

ActionEvent

.

Either the caption or the text may be

null

, but an

NullPointerException

is thrown if both are

null

.

When displayed, the caption or text strings may be truncated on
some platforms; the number of characters that may be displayed is
platform-dependent.

Note:

Some platforms may not support
showing a message.

**Parameters:** caption

- the caption displayed above the text, usually in
bold; may be

null
**Parameters:** text

- the text displayed for the particular message; may be

null
**Parameters:** messageType

- an enum indicating the message type
**Throws:** NullPointerException

- if both

caption

and

text

are

null

---

#### displayMessage

public void displayMessage​(

String

caption,

String

text,

TrayIcon.MessageType

messageType)

Displays a popup message near the tray icon. The message will
disappear after a time or if the user clicks on it. Clicking
on the message may trigger an

ActionEvent

.

Either the caption or the text may be

null

, but an

NullPointerException

is thrown if both are

null

.

When displayed, the caption or text strings may be truncated on
some platforms; the number of characters that may be displayed is
platform-dependent.

Note:

Some platforms may not support
showing a message.

Either the caption or the text may be

null

, but an

NullPointerException

is thrown if both are

null

.

When displayed, the caption or text strings may be truncated on
some platforms; the number of characters that may be displayed is
platform-dependent.

Note:

Some platforms may not support
showing a message.

Note:

Some platforms may not support
showing a message.

getSize

```java
public
Dimension
getSize()
```

Returns the size, in pixels, of the space that the tray icon
occupies in the system tray. For the tray icon that is not yet
added to the system tray, the returned size is equal to the
result of the

SystemTray.getTrayIconSize()

.

**Returns:** the size of the tray icon, in pixels
**See Also:** setImageAutoSize(boolean)

,

Image

,

getSize()

---

#### getSize

public

Dimension

getSize()

Returns the size, in pixels, of the space that the tray icon
occupies in the system tray. For the tray icon that is not yet
added to the system tray, the returned size is equal to the
result of the

SystemTray.getTrayIconSize()

.

---

