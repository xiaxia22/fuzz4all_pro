# Class JFrame

**Source:** `java.desktop\javax\swing\JFrame.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="JMenuBar",

description
="A toplevel window which can be minimized to an icon.")
public class
JFrame

extends
Frame

implements
WindowConstants
,
Accessible
,
RootPaneContainer
```

An extended version of

java.awt.Frame

that adds support for
the JFC/Swing component architecture.
You can find task-oriented documentation about using

JFrame

in

The Java Tutorial

, in the section

How to Make Frames

.

The

JFrame

class is slightly incompatible with

Frame

.
Like all other JFC/Swing top-level containers,
a

JFrame

contains a

JRootPane

as its only child.
The

content pane

provided by the root pane should,
as a rule, contain
all the non-menu components displayed by the

JFrame

.
This is different from the AWT

Frame

case.
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
For example, you can add a child component to a frame as follows:

```java
frame.add(child);
```

And the child will be added to the contentPane.
The content pane will
always be non-null. Attempting to set it to null will cause the JFrame
to throw an exception. The default content pane will have a BorderLayout
manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JFrame

.

Unlike a

Frame

, a

JFrame

has some notion of how to
respond when the user attempts to close the window. The default behavior
is to simply hide the JFrame when the user closes the window. To change the
default behavior, you invoke the method

setDefaultCloseOperation(int)

.
To make the

JFrame

behave the same as a

Frame

instance, use

setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE)

.

For more information on content panes
and other features that root panes provide,
see

Using Top-Level Containers

in

The Java Tutorial

.

In a multi-screen environment, you can create a

JFrame

on a different screen device. See

Frame

for more
information.

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

contentPane

and optional

menuBar

for this frame, as well as the

glassPane

.

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

JFrame

is constructed.

**See Also:**
- isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### protected
AccessibleContext
accessibleContext

The accessible context property.

---

### Constructor Details

#### public JFrame()
throws
HeadlessException

Constructs a new frame that is initially invisible.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

JComponent.getDefaultLocale()

---

#### public JFrame​(
GraphicsConfiguration
gc)

Creates a

Frame

in the specified

GraphicsConfiguration

of
a screen device and a blank title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- gc

- the

GraphicsConfiguration

that is used
to construct the new

Frame

;
if

gc

is

null

, the system
default

GraphicsConfiguration

is assumed

**Throws:**
- IllegalArgumentException

- if

gc

is not from
a screen device. This exception is always thrown when
GraphicsEnvironment.isHeadless() returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

**Since:**
- 1.3

---

#### public JFrame​(
String
title)
throws
HeadlessException

Creates a new, initially invisible

Frame

with the
specified title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- title

- the title for the frame

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

JComponent.getDefaultLocale()

---

#### public JFrame​(
String
title,

GraphicsConfiguration
gc)

Creates a

JFrame

with the specified title and the
specified

GraphicsConfiguration

of a screen device.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- title

- the title to be displayed in the
frame's border. A

null

value is treated as
an empty string, "".
- gc

- the

GraphicsConfiguration

that is used
to construct the new

JFrame

with;
if

gc

is

null

, the system
default

GraphicsConfiguration

is assumed

**Throws:**
- IllegalArgumentException

- if

gc

is not from
a screen device. This exception is always thrown when
GraphicsEnvironment.isHeadless() returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

**Since:**
- 1.3

---

### Method Details

#### protected void frameInit()

Called by the constructors to init the

JFrame

properly.

---

#### protected
JRootPane
createRootPane()

Called by the constructor methods to create the default

rootPane

.

**Returns:**
- a new

JRootPane

---

#### protected void processWindowEvent​(
WindowEvent
e)

Processes window events occurring on this component.
Hides the window or disposes of it, as specified by the setting
of the

defaultCloseOperation

property.

**Overrides:**
- processWindowEvent

in class

Window

**Parameters:**
- e

- the window event

**See Also:**
- setDefaultCloseOperation(int)

,

Window.processWindowEvent(java.awt.event.WindowEvent)

---

#### @BeanProperty
(
preferred
=true,

enumerationValues
={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE","WindowConstants.EXIT_ON_CLOSE"},

description
="The frame\'s default close operation.")
public void setDefaultCloseOperation​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this frame.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the frame after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
frame after invoking any registered

WindowListener

objects.

EXIT_ON_CLOSE

(defined in

WindowConstants

):
Exit the application using the

System

exit

method. Use this only in applications.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**Parameters:**
- operation

- the operation which should be performed when the
user closes the frame

**Throws:**
- IllegalArgumentException

- if defaultCloseOperation value
isn't one of the above valid values
- SecurityException

- if

EXIT_ON_CLOSE

has been specified and the

SecurityManager

will
not allow the caller to invoke

System.exit

**See Also:**
- Window.addWindowListener(java.awt.event.WindowListener)

,

getDefaultCloseOperation()

,

WindowConstants

,

Runtime.exit(int)

---

#### public int getDefaultCloseOperation()

Returns the operation that occurs when the user
initiates a "close" on this frame.

**Returns:**
- an integer indicating the window-close operation

**See Also:**
- setDefaultCloseOperation(int)

---

#### @BeanProperty
(
hidden
=true,

description
="Mechanism for transfer of data into the component")
public void setTransferHandler​(
TransferHandler
newHandler)

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JFrame

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**Parameters:**
- newHandler

- the new

TransferHandler

**See Also:**
- TransferHandler

,

getTransferHandler()

,

Component.setDropTarget(java.awt.dnd.DropTarget)

**Since:**
- 1.6

---

#### public
TransferHandler
getTransferHandler()

Gets the

transferHandler

property.

**Returns:**
- the value of the

transferHandler

property

**See Also:**
- TransferHandler

,

setTransferHandler(javax.swing.TransferHandler)

**Since:**
- 1.6

---

#### public void update​(
Graphics
g)

Just calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:**
- update

in class

Container

**Parameters:**
- g

- the Graphics context in which to paint

**See Also:**
- Component.update(Graphics)

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="The menubar for accessing pulldown menus from this frame.")
public void setJMenuBar​(
JMenuBar
menubar)

Sets the menubar for this frame.

**Parameters:**
- menubar

- the menubar being placed in the frame

**See Also:**
- getJMenuBar()

---

#### public
JMenuBar
getJMenuBar()

Returns the menubar set on this frame.

**Returns:**
- the menubar for this frame

**See Also:**
- setJMenuBar(javax.swing.JMenuBar)

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

JFrame

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

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JFrame

or

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

Sets the

LayoutManager

.
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

,

RootPaneContainer

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="the RootPane object for this frame.")
public
JRootPane
getRootPane()

Returns the

rootPane

object for this frame.

**Specified by:**
- getRootPane

in interface

RootPaneContainer

**Returns:**
- the

rootPane

property

**See Also:**
- setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

---

#### protected void setRootPane​(
JRootPane
root)

Sets the

rootPane

property.
This method is called by the constructor.

**Parameters:**
- root

- the

rootPane

object for this frame

**See Also:**
- getRootPane()

---

#### public
Container
getContentPane()

Returns the

contentPane

object for this frame.

**Specified by:**
- getContentPane

in interface

RootPaneContainer

**Returns:**
- the

contentPane

property

**See Also:**
- setContentPane(java.awt.Container)

,

RootPaneContainer.getContentPane()

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="The client area of the frame where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

**Specified by:**
- setContentPane

in interface

RootPaneContainer

**Parameters:**
- contentPane

- the

contentPane

object for this frame

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null

**See Also:**
- getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

,

JRootPane

---

#### public
JLayeredPane
getLayeredPane()

Returns the

layeredPane

object for this frame.

**Specified by:**
- getLayeredPane

in interface

RootPaneContainer

**Returns:**
- the

layeredPane

property

**See Also:**
- setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="The pane that holds the various frame layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)

Sets the

layeredPane

property.
This method is called by the constructor.

**Specified by:**
- setLayeredPane

in interface

RootPaneContainer

**Parameters:**
- layeredPane

- the

layeredPane

object for this frame

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is

null

**See Also:**
- getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

---

#### public
Component
getGlassPane()

Returns the

glassPane

object for this frame.

**Specified by:**
- getGlassPane

in interface

RootPaneContainer

**Returns:**
- the

glassPane

property

**See Also:**
- setGlassPane(java.awt.Component)

,

RootPaneContainer.getGlassPane()

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glassPane)

Sets the

glassPane

property.
This method is called by the constructor.

**Specified by:**
- setGlassPane

in interface

RootPaneContainer

**Parameters:**
- glassPane

- the

glassPane

object for this frame

**See Also:**
- getGlassPane()

,

RootPaneContainer.setGlassPane(java.awt.Component)

---

#### @BeanProperty
(
bound
=false)
public
Graphics
getGraphics()

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Overrides:**
- getGraphics

in class

Component

**Returns:**
- a graphics context for this component, or

null

if it has none

**See Also:**
- Component.paint(java.awt.Graphics)

**Since:**
- 1.6

---

#### public void repaint​(long time,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

**Overrides:**
- repaint

in class

Component

**Parameters:**
- time

- maximum time in milliseconds before update
- x

- the

x

coordinate
- y

- the

y

coordinate
- width

- the width
- height

- the height

**See Also:**
- RepaintManager

**Since:**
- 1.6

---

#### public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)

Provides a hint as to whether or not newly created

JFrame

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JFrame

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JFrame

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JFrame by doing the following:

```java
JFrame frame = new JFrame();
frame.setUndecorated(true);
frame.getRootPane().setWindowDecorationStyle(JRootPane.FRAME);
```

**Parameters:**
- defaultLookAndFeelDecorated

- A hint as to whether or not current
look and feel should provide window decorations

**See Also:**
- LookAndFeel.getSupportsWindowDecorations()

**Since:**
- 1.4

---

#### public static boolean isDefaultLookAndFeelDecorated()

Returns true if newly created

JFrame

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

**Returns:**
- true if look and feel should provide Window decorations.

**Since:**
- 1.4

---

#### protected
String
paramString()

Returns a string representation of this

JFrame

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

Frame

**Returns:**
- a string representation of this

JFrame

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JFrame.
For JFrames, the AccessibleContext takes the form of an
AccessibleJFrame.
A new AccessibleJFrame instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Frame

**Returns:**
- an AccessibleJFrame that serves as the
AccessibleContext of this JFrame

---

### Additional Sections

#### Class JFrame

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - java.awt.Window
- - java.awt.Frame
- - javax.swing.JFrame

java.awt.Component

- java.awt.Container
- - java.awt.Window
- - java.awt.Frame
- - javax.swing.JFrame

java.awt.Container

- java.awt.Window
- - java.awt.Frame
- - javax.swing.JFrame

java.awt.Window

- java.awt.Frame
- - javax.swing.JFrame

java.awt.Frame

- javax.swing.JFrame

javax.swing.JFrame

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
="A toplevel window which can be minimized to an icon.")
public class
JFrame

extends
Frame

implements
WindowConstants
,
Accessible
,
RootPaneContainer
```

An extended version of

java.awt.Frame

that adds support for
the JFC/Swing component architecture.
You can find task-oriented documentation about using

JFrame

in

The Java Tutorial

, in the section

How to Make Frames

.

The

JFrame

class is slightly incompatible with

Frame

.
Like all other JFC/Swing top-level containers,
a

JFrame

contains a

JRootPane

as its only child.
The

content pane

provided by the root pane should,
as a rule, contain
all the non-menu components displayed by the

JFrame

.
This is different from the AWT

Frame

case.
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
For example, you can add a child component to a frame as follows:

```java
frame.add(child);
```

And the child will be added to the contentPane.
The content pane will
always be non-null. Attempting to set it to null will cause the JFrame
to throw an exception. The default content pane will have a BorderLayout
manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JFrame

.

Unlike a

Frame

, a

JFrame

has some notion of how to
respond when the user attempts to close the window. The default behavior
is to simply hide the JFrame when the user closes the window. To change the
default behavior, you invoke the method

setDefaultCloseOperation(int)

.
To make the

JFrame

behave the same as a

Frame

instance, use

setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE)

.

For more information on content panes
and other features that root panes provide,
see

Using Top-Level Containers

in

The Java Tutorial

.

In a multi-screen environment, you can create a

JFrame

on a different screen device. See

Frame

for more
information.

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
**See Also:** JRootPane

,

setDefaultCloseOperation(int)

,

WindowListener.windowClosing(java.awt.event.WindowEvent)

,

RootPaneContainer

,

Serialized Form

@JavaBean

(

defaultProperty

="JMenuBar",

description

="A toplevel window which can be minimized to an icon.")
public class

JFrame

extends

Frame

implements

WindowConstants

,

Accessible

,

RootPaneContainer

An extended version of

java.awt.Frame

that adds support for
the JFC/Swing component architecture.
You can find task-oriented documentation about using

JFrame

in

The Java Tutorial

, in the section

How to Make Frames

.

The

JFrame

class is slightly incompatible with

Frame

.
Like all other JFC/Swing top-level containers,
a

JFrame

contains a

JRootPane

as its only child.
The

content pane

provided by the root pane should,
as a rule, contain
all the non-menu components displayed by the

JFrame

.
This is different from the AWT

Frame

case.
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
For example, you can add a child component to a frame as follows:

```java
frame.add(child);
```

And the child will be added to the contentPane.
The content pane will
always be non-null. Attempting to set it to null will cause the JFrame
to throw an exception. The default content pane will have a BorderLayout
manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JFrame

.

Unlike a

Frame

, a

JFrame

has some notion of how to
respond when the user attempts to close the window. The default behavior
is to simply hide the JFrame when the user closes the window. To change the
default behavior, you invoke the method

setDefaultCloseOperation(int)

.
To make the

JFrame

behave the same as a

Frame

instance, use

setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE)

.

For more information on content panes
and other features that root panes provide,
see

Using Top-Level Containers

in

The Java Tutorial

.

In a multi-screen environment, you can create a

JFrame

on a different screen device. See

Frame

for more
information.

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

JFrame

class is slightly incompatible with

Frame

.
Like all other JFC/Swing top-level containers,
a

JFrame

contains a

JRootPane

as its only child.
The

content pane

provided by the root pane should,
as a rule, contain
all the non-menu components displayed by the

JFrame

.
This is different from the AWT

Frame

case.
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
For example, you can add a child component to a frame as follows:

```java
frame.add(child);
```

And the child will be added to the contentPane.
The content pane will
always be non-null. Attempting to set it to null will cause the JFrame
to throw an exception. The default content pane will have a BorderLayout
manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JFrame

.

Unlike a

Frame

, a

JFrame

has some notion of how to
respond when the user attempts to close the window. The default behavior
is to simply hide the JFrame when the user closes the window. To change the
default behavior, you invoke the method

setDefaultCloseOperation(int)

.
To make the

JFrame

behave the same as a

Frame

instance, use

setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE)

.

For more information on content panes
and other features that root panes provide,
see

Using Top-Level Containers

in

The Java Tutorial

.

In a multi-screen environment, you can create a

JFrame

on a different screen device. See

Frame

for more
information.

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

frame.add(child);

Unlike a

Frame

, a

JFrame

has some notion of how to
respond when the user attempts to close the window. The default behavior
is to simply hide the JFrame when the user closes the window. To change the
default behavior, you invoke the method

setDefaultCloseOperation(int)

.
To make the

JFrame

behave the same as a

Frame

instance, use

setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE)

.

For more information on content panes
and other features that root panes provide,
see

Using Top-Level Containers

in

The Java Tutorial

.

In a multi-screen environment, you can create a

JFrame

on a different screen device. See

Frame

for more
information.

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

For more information on content panes
and other features that root panes provide,
see

Using Top-Level Containers

in

The Java Tutorial

.

In a multi-screen environment, you can create a

JFrame

on a different screen device. See

Frame

for more
information.

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

In a multi-screen environment, you can create a

JFrame

on a different screen device. See

Frame

for more
information.

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

JFrame.AccessibleJFrame

This class implements accessibility support for the

JFrame

class.

- Nested classes/interfaces declared in class java.awt.

Frame

Frame.AccessibleAWTFrame

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

protected

AccessibleContext

accessibleContext

The accessible context property.

protected

JRootPane

rootPane

The

JRootPane

instance that manages the

contentPane

and optional

menuBar

for this frame, as well as the

glassPane

.

protected boolean

rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

- Fields declared in class java.awt.

Frame

CROSSHAIR_CURSOR

,

DEFAULT_CURSOR

,

E_RESIZE_CURSOR

,

HAND_CURSOR

,

ICONIFIED

,

MAXIMIZED_BOTH

,

MAXIMIZED_HORIZ

,

MAXIMIZED_VERT

,

MOVE_CURSOR

,

N_RESIZE_CURSOR

,

NE_RESIZE_CURSOR

,

NORMAL

,

NW_RESIZE_CURSOR

,

S_RESIZE_CURSOR

,

SE_RESIZE_CURSOR

,

SW_RESIZE_CURSOR

,

TEXT_CURSOR

,

W_RESIZE_CURSOR

,

WAIT_CURSOR

- Fields declared in class java.awt.

Component

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

JFrame

()

Constructs a new frame that is initially invisible.

JFrame

​(

GraphicsConfiguration

gc)

Creates a

Frame

in the specified

GraphicsConfiguration

of
a screen device and a blank title.

JFrame

​(

String

title)

Creates a new, initially invisible

Frame

with the
specified title.

JFrame

​(

String

title,

GraphicsConfiguration

gc)

Creates a

JFrame

with the specified title and the
specified

GraphicsConfiguration

of a screen device.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

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

Adds the specified child

Component

.

protected

JRootPane

createRootPane

()

Called by the constructor methods to create the default

rootPane

.

protected void

frameInit

()

Called by the constructors to init the

JFrame

properly.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JFrame.

Container

getContentPane

()

Returns the

contentPane

object for this frame.

int

getDefaultCloseOperation

()

Returns the operation that occurs when the user
initiates a "close" on this frame.

Component

getGlassPane

()

Returns the

glassPane

object for this frame.

Graphics

getGraphics

()

Creates a graphics context for this component.

JMenuBar

getJMenuBar

()

Returns the menubar set on this frame.

JLayeredPane

getLayeredPane

()

Returns the

layeredPane

object for this frame.

JRootPane

getRootPane

()

Returns the

rootPane

object for this frame.

TransferHandler

getTransferHandler

()

Gets the

transferHandler

property.

static boolean

isDefaultLookAndFeelDecorated

()

Returns true if newly created

JFrame

s should have their
Window decorations provided by the current look and feel.

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

protected

String

paramString

()

Returns a string representation of this

JFrame

.

protected void

processWindowEvent

​(

WindowEvent

e)

Processes window events occurring on this component.

void

remove

​(

Component

comp)

Removes the specified component from the container.

void

repaint

​(long time,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

time

milliseconds.

void

setContentPane

​(

Container

contentPane)

Sets the

contentPane

property.

void

setDefaultCloseOperation

​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this frame.

static void

setDefaultLookAndFeelDecorated

​(boolean defaultLookAndFeelDecorated)

Provides a hint as to whether or not newly created

JFrame

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel.

void

setGlassPane

​(

Component

glassPane)

Sets the

glassPane

property.

void

setJMenuBar

​(

JMenuBar

menubar)

Sets the menubar for this frame.

void

setLayeredPane

​(

JLayeredPane

layeredPane)

Sets the

layeredPane

property.

void

setLayout

​(

LayoutManager

manager)

Sets the

LayoutManager

.

protected void

setRootPane

​(

JRootPane

root)

Sets the

rootPane

property.

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

setTransferHandler

​(

TransferHandler

newHandler)

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component.

void

update

​(

Graphics

g)

Just calls

paint(g)

.

- Methods declared in class java.awt.

Frame

addNotify

,

getCursorType

,

getExtendedState

,

getFrames

,

getIconImage

,

getMaximizedBounds

,

getMenuBar

,

getState

,

getTitle

,

isResizable

,

isUndecorated

,

remove

,

removeNotify

,

setCursor

,

setExtendedState

,

setMaximizedBounds

,

setMenuBar

,

setResizable

,

setState

,

setTitle

,

setUndecorated

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

JFrame.AccessibleJFrame

This class implements accessibility support for the

JFrame

class.

- Nested classes/interfaces declared in class java.awt.

Frame

Frame.AccessibleAWTFrame

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

JFrame

class.

Nested classes/interfaces declared in class java.awt.

Frame

Frame.AccessibleAWTFrame

---

#### Nested classes/interfaces declared in class java.awt. Frame

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

protected

AccessibleContext

accessibleContext

The accessible context property.

protected

JRootPane

rootPane

The

JRootPane

instance that manages the

contentPane

and optional

menuBar

for this frame, as well as the

glassPane

.

protected boolean

rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

- Fields declared in class java.awt.

Frame

CROSSHAIR_CURSOR

,

DEFAULT_CURSOR

,

E_RESIZE_CURSOR

,

HAND_CURSOR

,

ICONIFIED

,

MAXIMIZED_BOTH

,

MAXIMIZED_HORIZ

,

MAXIMIZED_VERT

,

MOVE_CURSOR

,

N_RESIZE_CURSOR

,

NE_RESIZE_CURSOR

,

NORMAL

,

NW_RESIZE_CURSOR

,

S_RESIZE_CURSOR

,

SE_RESIZE_CURSOR

,

SW_RESIZE_CURSOR

,

TEXT_CURSOR

,

W_RESIZE_CURSOR

,

WAIT_CURSOR

- Fields declared in class java.awt.

Component

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

The accessible context property.

The

JRootPane

instance that manages the

contentPane

and optional

menuBar

for this frame, as well as the

glassPane

.

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

Fields declared in class java.awt.

Frame

CROSSHAIR_CURSOR

,

DEFAULT_CURSOR

,

E_RESIZE_CURSOR

,

HAND_CURSOR

,

ICONIFIED

,

MAXIMIZED_BOTH

,

MAXIMIZED_HORIZ

,

MAXIMIZED_VERT

,

MOVE_CURSOR

,

N_RESIZE_CURSOR

,

NE_RESIZE_CURSOR

,

NORMAL

,

NW_RESIZE_CURSOR

,

S_RESIZE_CURSOR

,

SE_RESIZE_CURSOR

,

SW_RESIZE_CURSOR

,

TEXT_CURSOR

,

W_RESIZE_CURSOR

,

WAIT_CURSOR

---

#### Fields declared in class java.awt. Frame

Fields declared in class java.awt.

Component

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

JFrame

()

Constructs a new frame that is initially invisible.

JFrame

​(

GraphicsConfiguration

gc)

Creates a

Frame

in the specified

GraphicsConfiguration

of
a screen device and a blank title.

JFrame

​(

String

title)

Creates a new, initially invisible

Frame

with the
specified title.

JFrame

​(

String

title,

GraphicsConfiguration

gc)

Creates a

JFrame

with the specified title and the
specified

GraphicsConfiguration

of a screen device.

---

#### Constructor Summary

Constructs a new frame that is initially invisible.

Creates a

Frame

in the specified

GraphicsConfiguration

of
a screen device and a blank title.

Creates a new, initially invisible

Frame

with the
specified title.

Creates a

JFrame

with the specified title and the
specified

GraphicsConfiguration

of a screen device.

Method Summary

All Methods

Static Methods

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

Adds the specified child

Component

.

protected

JRootPane

createRootPane

()

Called by the constructor methods to create the default

rootPane

.

protected void

frameInit

()

Called by the constructors to init the

JFrame

properly.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JFrame.

Container

getContentPane

()

Returns the

contentPane

object for this frame.

int

getDefaultCloseOperation

()

Returns the operation that occurs when the user
initiates a "close" on this frame.

Component

getGlassPane

()

Returns the

glassPane

object for this frame.

Graphics

getGraphics

()

Creates a graphics context for this component.

JMenuBar

getJMenuBar

()

Returns the menubar set on this frame.

JLayeredPane

getLayeredPane

()

Returns the

layeredPane

object for this frame.

JRootPane

getRootPane

()

Returns the

rootPane

object for this frame.

TransferHandler

getTransferHandler

()

Gets the

transferHandler

property.

static boolean

isDefaultLookAndFeelDecorated

()

Returns true if newly created

JFrame

s should have their
Window decorations provided by the current look and feel.

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

protected

String

paramString

()

Returns a string representation of this

JFrame

.

protected void

processWindowEvent

​(

WindowEvent

e)

Processes window events occurring on this component.

void

remove

​(

Component

comp)

Removes the specified component from the container.

void

repaint

​(long time,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

time

milliseconds.

void

setContentPane

​(

Container

contentPane)

Sets the

contentPane

property.

void

setDefaultCloseOperation

​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this frame.

static void

setDefaultLookAndFeelDecorated

​(boolean defaultLookAndFeelDecorated)

Provides a hint as to whether or not newly created

JFrame

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel.

void

setGlassPane

​(

Component

glassPane)

Sets the

glassPane

property.

void

setJMenuBar

​(

JMenuBar

menubar)

Sets the menubar for this frame.

void

setLayeredPane

​(

JLayeredPane

layeredPane)

Sets the

layeredPane

property.

void

setLayout

​(

LayoutManager

manager)

Sets the

LayoutManager

.

protected void

setRootPane

​(

JRootPane

root)

Sets the

rootPane

property.

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

setTransferHandler

​(

TransferHandler

newHandler)

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component.

void

update

​(

Graphics

g)

Just calls

paint(g)

.

- Methods declared in class java.awt.

Frame

addNotify

,

getCursorType

,

getExtendedState

,

getFrames

,

getIconImage

,

getMaximizedBounds

,

getMenuBar

,

getState

,

getTitle

,

isResizable

,

isUndecorated

,

remove

,

removeNotify

,

setCursor

,

setExtendedState

,

setMaximizedBounds

,

setMenuBar

,

setResizable

,

setState

,

setTitle

,

setUndecorated

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

Adds the specified child

Component

.

Called by the constructor methods to create the default

rootPane

.

Called by the constructors to init the

JFrame

properly.

Gets the AccessibleContext associated with this JFrame.

Returns the

contentPane

object for this frame.

Returns the operation that occurs when the user
initiates a "close" on this frame.

Returns the

glassPane

object for this frame.

Creates a graphics context for this component.

Returns the menubar set on this frame.

Returns the

layeredPane

object for this frame.

Returns the

rootPane

object for this frame.

Gets the

transferHandler

property.

Returns true if newly created

JFrame

s should have their
Window decorations provided by the current look and feel.

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

Returns a string representation of this

JFrame

.

Processes window events occurring on this component.

Removes the specified component from the container.

Repaints the specified rectangle of this component within

time

milliseconds.

Sets the

contentPane

property.

Sets the operation that will happen by default when
the user initiates a "close" on this frame.

Provides a hint as to whether or not newly created

JFrame

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel.

Sets the

glassPane

property.

Sets the menubar for this frame.

Sets the

layeredPane

property.

Sets the

LayoutManager

.

Sets the

rootPane

property.

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component.

Just calls

paint(g)

.

Methods declared in class java.awt.

Frame

addNotify

,

getCursorType

,

getExtendedState

,

getFrames

,

getIconImage

,

getMaximizedBounds

,

getMenuBar

,

getState

,

getTitle

,

isResizable

,

isUndecorated

,

remove

,

removeNotify

,

setCursor

,

setExtendedState

,

setMaximizedBounds

,

setMenuBar

,

setResizable

,

setState

,

setTitle

,

setUndecorated

---

#### Methods declared in class java.awt. Frame

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

- rootPane

```java
protected
JRootPane
rootPane
```

The

JRootPane

instance that manages the

contentPane

and optional

menuBar

for this frame, as well as the

glassPane

.

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

JFrame

is constructed.

**See Also:** isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

The accessible context property.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JFrame

```java
public JFrame()
throws
HeadlessException
```

Constructs a new frame that is initially invisible.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

JComponent.getDefaultLocale()

- JFrame

```java
public JFrame​(
GraphicsConfiguration
gc)
```

Creates a

Frame

in the specified

GraphicsConfiguration

of
a screen device and a blank title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** gc

- the

GraphicsConfiguration

that is used
to construct the new

Frame

;
if

gc

is

null

, the system
default

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if

gc

is not from
a screen device. This exception is always thrown when
GraphicsEnvironment.isHeadless() returns true.
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JFrame

```java
public JFrame​(
String
title)
throws
HeadlessException
```

Creates a new, initially invisible

Frame

with the
specified title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** title

- the title for the frame
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

JComponent.getDefaultLocale()

- JFrame

```java
public JFrame​(
String
title,

GraphicsConfiguration
gc)
```

Creates a

JFrame

with the specified title and the
specified

GraphicsConfiguration

of a screen device.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** title

- the title to be displayed in the
frame's border. A

null

value is treated as
an empty string, "".
**Parameters:** gc

- the

GraphicsConfiguration

that is used
to construct the new

JFrame

with;
if

gc

is

null

, the system
default

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if

gc

is not from
a screen device. This exception is always thrown when
GraphicsEnvironment.isHeadless() returns true.
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

============ METHOD DETAIL ==========

- Method Detail

- frameInit

```java
protected void frameInit()
```

Called by the constructors to init the

JFrame

properly.

- createRootPane

```java
protected
JRootPane
createRootPane()
```

Called by the constructor methods to create the default

rootPane

.

**Returns:** a new

JRootPane

- processWindowEvent

```java
protected void processWindowEvent​(
WindowEvent
e)
```

Processes window events occurring on this component.
Hides the window or disposes of it, as specified by the setting
of the

defaultCloseOperation

property.

**Overrides:** processWindowEvent

in class

Window
**Parameters:** e

- the window event
**See Also:** setDefaultCloseOperation(int)

,

Window.processWindowEvent(java.awt.event.WindowEvent)

- setDefaultCloseOperation

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE","WindowConstants.EXIT_ON_CLOSE"},

description
="The frame\'s default close operation.")
public void setDefaultCloseOperation​(int operation)
```

Sets the operation that will happen by default when
the user initiates a "close" on this frame.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the frame after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
frame after invoking any registered

WindowListener

objects.

EXIT_ON_CLOSE

(defined in

WindowConstants

):
Exit the application using the

System

exit

method. Use this only in applications.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**Parameters:** operation

- the operation which should be performed when the
user closes the frame
**Throws:** IllegalArgumentException

- if defaultCloseOperation value
isn't one of the above valid values
**Throws:** SecurityException

- if

EXIT_ON_CLOSE

has been specified and the

SecurityManager

will
not allow the caller to invoke

System.exit
**See Also:** Window.addWindowListener(java.awt.event.WindowListener)

,

getDefaultCloseOperation()

,

WindowConstants

,

Runtime.exit(int)

- getDefaultCloseOperation

```java
public int getDefaultCloseOperation()
```

Returns the operation that occurs when the user
initiates a "close" on this frame.

**Returns:** an integer indicating the window-close operation
**See Also:** setDefaultCloseOperation(int)

- setTransferHandler

```java
@BeanProperty
(
hidden
=true,

description
="Mechanism for transfer of data into the component")
public void setTransferHandler​(
TransferHandler
newHandler)
```

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JFrame

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**Parameters:** newHandler

- the new

TransferHandler
**Since:** 1.6
**See Also:** TransferHandler

,

getTransferHandler()

,

Component.setDropTarget(java.awt.dnd.DropTarget)

- getTransferHandler

```java
public
TransferHandler
getTransferHandler()
```

Gets the

transferHandler

property.

**Returns:** the value of the

transferHandler

property
**Since:** 1.6
**See Also:** TransferHandler

,

setTransferHandler(javax.swing.TransferHandler)

- update

```java
public void update​(
Graphics
g)
```

Just calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:** update

in class

Container
**Parameters:** g

- the Graphics context in which to paint
**See Also:** Component.update(Graphics)

- setJMenuBar

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The menubar for accessing pulldown menus from this frame.")
public void setJMenuBar​(
JMenuBar
menubar)
```

Sets the menubar for this frame.

**Parameters:** menubar

- the menubar being placed in the frame
**See Also:** getJMenuBar()

- getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Returns the menubar set on this frame.

**Returns:** the menubar for this frame
**See Also:** setJMenuBar(javax.swing.JMenuBar)

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

JFrame

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

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JFrame

or

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

Sets the

LayoutManager

.
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

,

RootPaneContainer

- getRootPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="the RootPane object for this frame.")
public
JRootPane
getRootPane()
```

Returns the

rootPane

object for this frame.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Returns:** the

rootPane

property
**See Also:** setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

- setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Sets the

rootPane

property.
This method is called by the constructor.

**Parameters:** root

- the

rootPane

object for this frame
**See Also:** getRootPane()

- getContentPane

```java
public
Container
getContentPane()
```

Returns the

contentPane

object for this frame.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the

contentPane

property
**See Also:** setContentPane(java.awt.Container)

,

RootPaneContainer.getContentPane()

- setContentPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The client area of the frame where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)
```

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** contentPane

- the

contentPane

object for this frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null
**See Also:** getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

,

JRootPane

- getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Returns the

layeredPane

object for this frame.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** the

layeredPane

property
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

- setLayeredPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The pane that holds the various frame layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)
```

Sets the

layeredPane

property.
This method is called by the constructor.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layeredPane

- the

layeredPane

object for this frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is

null
**See Also:** getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

- getGlassPane

```java
public
Component
getGlassPane()
```

Returns the

glassPane

object for this frame.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the

glassPane

property
**See Also:** setGlassPane(java.awt.Component)

,

RootPaneContainer.getGlassPane()

- setGlassPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glassPane)
```

Sets the

glassPane

property.
This method is called by the constructor.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glassPane

- the

glassPane

object for this frame
**See Also:** getGlassPane()

,

RootPaneContainer.setGlassPane(java.awt.Component)

- getGraphics

```java
@BeanProperty
(
bound
=false)
public
Graphics
getGraphics()
```

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Overrides:** getGraphics

in class

Component
**Returns:** a graphics context for this component, or

null

if it has none
**Since:** 1.6
**See Also:** Component.paint(java.awt.Graphics)

- repaint

```java
public void repaint​(long time,
int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

**Overrides:** repaint

in class

Component
**Parameters:** time

- maximum time in milliseconds before update
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.6
**See Also:** RepaintManager

- setDefaultLookAndFeelDecorated

```java
public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)
```

Provides a hint as to whether or not newly created

JFrame

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JFrame

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JFrame

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JFrame by doing the following:

```java
JFrame frame = new JFrame();
frame.setUndecorated(true);
frame.getRootPane().setWindowDecorationStyle(JRootPane.FRAME);
```

**Parameters:** defaultLookAndFeelDecorated

- A hint as to whether or not current
look and feel should provide window decorations
**Since:** 1.4
**See Also:** LookAndFeel.getSupportsWindowDecorations()

- isDefaultLookAndFeelDecorated

```java
public static boolean isDefaultLookAndFeelDecorated()
```

Returns true if newly created

JFrame

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

**Returns:** true if look and feel should provide Window decorations.
**Since:** 1.4

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JFrame

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

Frame
**Returns:** a string representation of this

JFrame

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JFrame.
For JFrames, the AccessibleContext takes the form of an
AccessibleJFrame.
A new AccessibleJFrame instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Frame
**Returns:** an AccessibleJFrame that serves as the
AccessibleContext of this JFrame

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

contentPane

and optional

menuBar

for this frame, as well as the

glassPane

.

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

JFrame

is constructed.

**See Also:** isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

The accessible context property.

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

contentPane

and optional

menuBar

for this frame, as well as the

glassPane

.

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

contentPane

and optional

menuBar

for this frame, as well as the

glassPane

.

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

JFrame

is constructed.

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

JFrame

is constructed.

accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

The accessible context property.

---

#### accessibleContext

protected

AccessibleContext

accessibleContext

The accessible context property.

Constructor Detail

- JFrame

```java
public JFrame()
throws
HeadlessException
```

Constructs a new frame that is initially invisible.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

JComponent.getDefaultLocale()

- JFrame

```java
public JFrame​(
GraphicsConfiguration
gc)
```

Creates a

Frame

in the specified

GraphicsConfiguration

of
a screen device and a blank title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** gc

- the

GraphicsConfiguration

that is used
to construct the new

Frame

;
if

gc

is

null

, the system
default

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if

gc

is not from
a screen device. This exception is always thrown when
GraphicsEnvironment.isHeadless() returns true.
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JFrame

```java
public JFrame​(
String
title)
throws
HeadlessException
```

Creates a new, initially invisible

Frame

with the
specified title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** title

- the title for the frame
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

JComponent.getDefaultLocale()

- JFrame

```java
public JFrame​(
String
title,

GraphicsConfiguration
gc)
```

Creates a

JFrame

with the specified title and the
specified

GraphicsConfiguration

of a screen device.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** title

- the title to be displayed in the
frame's border. A

null

value is treated as
an empty string, "".
**Parameters:** gc

- the

GraphicsConfiguration

that is used
to construct the new

JFrame

with;
if

gc

is

null

, the system
default

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if

gc

is not from
a screen device. This exception is always thrown when
GraphicsEnvironment.isHeadless() returns true.
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### Constructor Detail

JFrame

```java
public JFrame()
throws
HeadlessException
```

Constructs a new frame that is initially invisible.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

JComponent.getDefaultLocale()

---

#### JFrame

public JFrame()
throws

HeadlessException

Constructs a new frame that is initially invisible.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JFrame

```java
public JFrame​(
GraphicsConfiguration
gc)
```

Creates a

Frame

in the specified

GraphicsConfiguration

of
a screen device and a blank title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** gc

- the

GraphicsConfiguration

that is used
to construct the new

Frame

;
if

gc

is

null

, the system
default

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if

gc

is not from
a screen device. This exception is always thrown when
GraphicsEnvironment.isHeadless() returns true.
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JFrame

public JFrame​(

GraphicsConfiguration

gc)

Creates a

Frame

in the specified

GraphicsConfiguration

of
a screen device and a blank title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JFrame

```java
public JFrame​(
String
title)
throws
HeadlessException
```

Creates a new, initially invisible

Frame

with the
specified title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** title

- the title for the frame
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

,

JComponent.getDefaultLocale()

---

#### JFrame

public JFrame​(

String

title)
throws

HeadlessException

Creates a new, initially invisible

Frame

with the
specified title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JFrame

```java
public JFrame​(
String
title,

GraphicsConfiguration
gc)
```

Creates a

JFrame

with the specified title and the
specified

GraphicsConfiguration

of a screen device.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** title

- the title to be displayed in the
frame's border. A

null

value is treated as
an empty string, "".
**Parameters:** gc

- the

GraphicsConfiguration

that is used
to construct the new

JFrame

with;
if

gc

is

null

, the system
default

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if

gc

is not from
a screen device. This exception is always thrown when
GraphicsEnvironment.isHeadless() returns true.
**Since:** 1.3
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JFrame

public JFrame​(

String

title,

GraphicsConfiguration

gc)

Creates a

JFrame

with the specified title and the
specified

GraphicsConfiguration

of a screen device.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

Method Detail

- frameInit

```java
protected void frameInit()
```

Called by the constructors to init the

JFrame

properly.

- createRootPane

```java
protected
JRootPane
createRootPane()
```

Called by the constructor methods to create the default

rootPane

.

**Returns:** a new

JRootPane

- processWindowEvent

```java
protected void processWindowEvent​(
WindowEvent
e)
```

Processes window events occurring on this component.
Hides the window or disposes of it, as specified by the setting
of the

defaultCloseOperation

property.

**Overrides:** processWindowEvent

in class

Window
**Parameters:** e

- the window event
**See Also:** setDefaultCloseOperation(int)

,

Window.processWindowEvent(java.awt.event.WindowEvent)

- setDefaultCloseOperation

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE","WindowConstants.EXIT_ON_CLOSE"},

description
="The frame\'s default close operation.")
public void setDefaultCloseOperation​(int operation)
```

Sets the operation that will happen by default when
the user initiates a "close" on this frame.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the frame after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
frame after invoking any registered

WindowListener

objects.

EXIT_ON_CLOSE

(defined in

WindowConstants

):
Exit the application using the

System

exit

method. Use this only in applications.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**Parameters:** operation

- the operation which should be performed when the
user closes the frame
**Throws:** IllegalArgumentException

- if defaultCloseOperation value
isn't one of the above valid values
**Throws:** SecurityException

- if

EXIT_ON_CLOSE

has been specified and the

SecurityManager

will
not allow the caller to invoke

System.exit
**See Also:** Window.addWindowListener(java.awt.event.WindowListener)

,

getDefaultCloseOperation()

,

WindowConstants

,

Runtime.exit(int)

- getDefaultCloseOperation

```java
public int getDefaultCloseOperation()
```

Returns the operation that occurs when the user
initiates a "close" on this frame.

**Returns:** an integer indicating the window-close operation
**See Also:** setDefaultCloseOperation(int)

- setTransferHandler

```java
@BeanProperty
(
hidden
=true,

description
="Mechanism for transfer of data into the component")
public void setTransferHandler​(
TransferHandler
newHandler)
```

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JFrame

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**Parameters:** newHandler

- the new

TransferHandler
**Since:** 1.6
**See Also:** TransferHandler

,

getTransferHandler()

,

Component.setDropTarget(java.awt.dnd.DropTarget)

- getTransferHandler

```java
public
TransferHandler
getTransferHandler()
```

Gets the

transferHandler

property.

**Returns:** the value of the

transferHandler

property
**Since:** 1.6
**See Also:** TransferHandler

,

setTransferHandler(javax.swing.TransferHandler)

- update

```java
public void update​(
Graphics
g)
```

Just calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:** update

in class

Container
**Parameters:** g

- the Graphics context in which to paint
**See Also:** Component.update(Graphics)

- setJMenuBar

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The menubar for accessing pulldown menus from this frame.")
public void setJMenuBar​(
JMenuBar
menubar)
```

Sets the menubar for this frame.

**Parameters:** menubar

- the menubar being placed in the frame
**See Also:** getJMenuBar()

- getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Returns the menubar set on this frame.

**Returns:** the menubar for this frame
**See Also:** setJMenuBar(javax.swing.JMenuBar)

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

JFrame

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

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JFrame

or

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

Sets the

LayoutManager

.
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

,

RootPaneContainer

- getRootPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="the RootPane object for this frame.")
public
JRootPane
getRootPane()
```

Returns the

rootPane

object for this frame.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Returns:** the

rootPane

property
**See Also:** setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

- setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Sets the

rootPane

property.
This method is called by the constructor.

**Parameters:** root

- the

rootPane

object for this frame
**See Also:** getRootPane()

- getContentPane

```java
public
Container
getContentPane()
```

Returns the

contentPane

object for this frame.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the

contentPane

property
**See Also:** setContentPane(java.awt.Container)

,

RootPaneContainer.getContentPane()

- setContentPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The client area of the frame where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)
```

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** contentPane

- the

contentPane

object for this frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null
**See Also:** getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

,

JRootPane

- getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Returns the

layeredPane

object for this frame.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** the

layeredPane

property
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

- setLayeredPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The pane that holds the various frame layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)
```

Sets the

layeredPane

property.
This method is called by the constructor.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layeredPane

- the

layeredPane

object for this frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is

null
**See Also:** getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

- getGlassPane

```java
public
Component
getGlassPane()
```

Returns the

glassPane

object for this frame.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the

glassPane

property
**See Also:** setGlassPane(java.awt.Component)

,

RootPaneContainer.getGlassPane()

- setGlassPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glassPane)
```

Sets the

glassPane

property.
This method is called by the constructor.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glassPane

- the

glassPane

object for this frame
**See Also:** getGlassPane()

,

RootPaneContainer.setGlassPane(java.awt.Component)

- getGraphics

```java
@BeanProperty
(
bound
=false)
public
Graphics
getGraphics()
```

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Overrides:** getGraphics

in class

Component
**Returns:** a graphics context for this component, or

null

if it has none
**Since:** 1.6
**See Also:** Component.paint(java.awt.Graphics)

- repaint

```java
public void repaint​(long time,
int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

**Overrides:** repaint

in class

Component
**Parameters:** time

- maximum time in milliseconds before update
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.6
**See Also:** RepaintManager

- setDefaultLookAndFeelDecorated

```java
public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)
```

Provides a hint as to whether or not newly created

JFrame

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JFrame

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JFrame

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JFrame by doing the following:

```java
JFrame frame = new JFrame();
frame.setUndecorated(true);
frame.getRootPane().setWindowDecorationStyle(JRootPane.FRAME);
```

**Parameters:** defaultLookAndFeelDecorated

- A hint as to whether or not current
look and feel should provide window decorations
**Since:** 1.4
**See Also:** LookAndFeel.getSupportsWindowDecorations()

- isDefaultLookAndFeelDecorated

```java
public static boolean isDefaultLookAndFeelDecorated()
```

Returns true if newly created

JFrame

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

**Returns:** true if look and feel should provide Window decorations.
**Since:** 1.4

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JFrame

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

Frame
**Returns:** a string representation of this

JFrame

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JFrame.
For JFrames, the AccessibleContext takes the form of an
AccessibleJFrame.
A new AccessibleJFrame instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Frame
**Returns:** an AccessibleJFrame that serves as the
AccessibleContext of this JFrame

---

#### Method Detail

frameInit

```java
protected void frameInit()
```

Called by the constructors to init the

JFrame

properly.

---

#### frameInit

protected void frameInit()

Called by the constructors to init the

JFrame

properly.

createRootPane

```java
protected
JRootPane
createRootPane()
```

Called by the constructor methods to create the default

rootPane

.

**Returns:** a new

JRootPane

---

#### createRootPane

protected

JRootPane

createRootPane()

Called by the constructor methods to create the default

rootPane

.

processWindowEvent

```java
protected void processWindowEvent​(
WindowEvent
e)
```

Processes window events occurring on this component.
Hides the window or disposes of it, as specified by the setting
of the

defaultCloseOperation

property.

**Overrides:** processWindowEvent

in class

Window
**Parameters:** e

- the window event
**See Also:** setDefaultCloseOperation(int)

,

Window.processWindowEvent(java.awt.event.WindowEvent)

---

#### processWindowEvent

protected void processWindowEvent​(

WindowEvent

e)

Processes window events occurring on this component.
Hides the window or disposes of it, as specified by the setting
of the

defaultCloseOperation

property.

setDefaultCloseOperation

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE","WindowConstants.EXIT_ON_CLOSE"},

description
="The frame\'s default close operation.")
public void setDefaultCloseOperation​(int operation)
```

Sets the operation that will happen by default when
the user initiates a "close" on this frame.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the frame after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
frame after invoking any registered

WindowListener

objects.

EXIT_ON_CLOSE

(defined in

WindowConstants

):
Exit the application using the

System

exit

method. Use this only in applications.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**Parameters:** operation

- the operation which should be performed when the
user closes the frame
**Throws:** IllegalArgumentException

- if defaultCloseOperation value
isn't one of the above valid values
**Throws:** SecurityException

- if

EXIT_ON_CLOSE

has been specified and the

SecurityManager

will
not allow the caller to invoke

System.exit
**See Also:** Window.addWindowListener(java.awt.event.WindowListener)

,

getDefaultCloseOperation()

,

WindowConstants

,

Runtime.exit(int)

---

#### setDefaultCloseOperation

@BeanProperty

(

preferred

=true,

enumerationValues

={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE","WindowConstants.EXIT_ON_CLOSE"},

description

="The frame\'s default close operation.")
public void setDefaultCloseOperation​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this frame.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the frame after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
frame after invoking any registered

WindowListener

objects.

EXIT_ON_CLOSE

(defined in

WindowConstants

):
Exit the application using the

System

exit

method. Use this only in applications.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the frame after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
frame after invoking any registered

WindowListener

objects.

EXIT_ON_CLOSE

(defined in

WindowConstants

):
Exit the application using the

System

exit

method. Use this only in applications.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

getDefaultCloseOperation

```java
public int getDefaultCloseOperation()
```

Returns the operation that occurs when the user
initiates a "close" on this frame.

**Returns:** an integer indicating the window-close operation
**See Also:** setDefaultCloseOperation(int)

---

#### getDefaultCloseOperation

public int getDefaultCloseOperation()

Returns the operation that occurs when the user
initiates a "close" on this frame.

setTransferHandler

```java
@BeanProperty
(
hidden
=true,

description
="Mechanism for transfer of data into the component")
public void setTransferHandler​(
TransferHandler
newHandler)
```

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JFrame

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**Parameters:** newHandler

- the new

TransferHandler
**Since:** 1.6
**See Also:** TransferHandler

,

getTransferHandler()

,

Component.setDropTarget(java.awt.dnd.DropTarget)

---

#### setTransferHandler

@BeanProperty

(

hidden

=true,

description

="Mechanism for transfer of data into the component")
public void setTransferHandler​(

TransferHandler

newHandler)

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JFrame

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JFrame

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

Note: When used with

JFrame

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

getTransferHandler

```java
public
TransferHandler
getTransferHandler()
```

Gets the

transferHandler

property.

**Returns:** the value of the

transferHandler

property
**Since:** 1.6
**See Also:** TransferHandler

,

setTransferHandler(javax.swing.TransferHandler)

---

#### getTransferHandler

public

TransferHandler

getTransferHandler()

Gets the

transferHandler

property.

update

```java
public void update​(
Graphics
g)
```

Just calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:** update

in class

Container
**Parameters:** g

- the Graphics context in which to paint
**See Also:** Component.update(Graphics)

---

#### update

public void update​(

Graphics

g)

Just calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

setJMenuBar

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The menubar for accessing pulldown menus from this frame.")
public void setJMenuBar​(
JMenuBar
menubar)
```

Sets the menubar for this frame.

**Parameters:** menubar

- the menubar being placed in the frame
**See Also:** getJMenuBar()

---

#### setJMenuBar

@BeanProperty

(

bound

=false,

hidden

=true,

description

="The menubar for accessing pulldown menus from this frame.")
public void setJMenuBar​(

JMenuBar

menubar)

Sets the menubar for this frame.

getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Returns the menubar set on this frame.

**Returns:** the menubar for this frame
**See Also:** setJMenuBar(javax.swing.JMenuBar)

---

#### getJMenuBar

public

JMenuBar

getJMenuBar()

Returns the menubar set on this frame.

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

JFrame

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

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JFrame

or

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

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JFrame

or

contentPane

.

setLayout

```java
public void setLayout​(
LayoutManager
manager)
```

Sets the

LayoutManager

.
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

,

RootPaneContainer

---

#### setLayout

public void setLayout​(

LayoutManager

manager)

Sets the

LayoutManager

.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

getRootPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="the RootPane object for this frame.")
public
JRootPane
getRootPane()
```

Returns the

rootPane

object for this frame.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Returns:** the

rootPane

property
**See Also:** setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

---

#### getRootPane

@BeanProperty

(

bound

=false,

hidden

=true,

description

="the RootPane object for this frame.")
public

JRootPane

getRootPane()

Returns the

rootPane

object for this frame.

setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Sets the

rootPane

property.
This method is called by the constructor.

**Parameters:** root

- the

rootPane

object for this frame
**See Also:** getRootPane()

---

#### setRootPane

protected void setRootPane​(

JRootPane

root)

Sets the

rootPane

property.
This method is called by the constructor.

getContentPane

```java
public
Container
getContentPane()
```

Returns the

contentPane

object for this frame.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the

contentPane

property
**See Also:** setContentPane(java.awt.Container)

,

RootPaneContainer.getContentPane()

---

#### getContentPane

public

Container

getContentPane()

Returns the

contentPane

object for this frame.

setContentPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The client area of the frame where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)
```

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** contentPane

- the

contentPane

object for this frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null
**See Also:** getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

,

JRootPane

---

#### setContentPane

@BeanProperty

(

bound

=false,

hidden

=true,

description

="The client area of the frame where child components are normally inserted.")
public void setContentPane​(

Container

contentPane)

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Returns the

layeredPane

object for this frame.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** the

layeredPane

property
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

---

#### getLayeredPane

public

JLayeredPane

getLayeredPane()

Returns the

layeredPane

object for this frame.

setLayeredPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The pane that holds the various frame layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)
```

Sets the

layeredPane

property.
This method is called by the constructor.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layeredPane

- the

layeredPane

object for this frame
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is

null
**See Also:** getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

---

#### setLayeredPane

@BeanProperty

(

bound

=false,

hidden

=true,

description

="The pane that holds the various frame layers.")
public void setLayeredPane​(

JLayeredPane

layeredPane)

Sets the

layeredPane

property.
This method is called by the constructor.

getGlassPane

```java
public
Component
getGlassPane()
```

Returns the

glassPane

object for this frame.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the

glassPane

property
**See Also:** setGlassPane(java.awt.Component)

,

RootPaneContainer.getGlassPane()

---

#### getGlassPane

public

Component

getGlassPane()

Returns the

glassPane

object for this frame.

setGlassPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glassPane)
```

Sets the

glassPane

property.
This method is called by the constructor.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glassPane

- the

glassPane

object for this frame
**See Also:** getGlassPane()

,

RootPaneContainer.setGlassPane(java.awt.Component)

---

#### setGlassPane

@BeanProperty

(

bound

=false,

hidden

=true,

description

="A transparent pane used for menu rendering.")
public void setGlassPane​(

Component

glassPane)

Sets the

glassPane

property.
This method is called by the constructor.

getGraphics

```java
@BeanProperty
(
bound
=false)
public
Graphics
getGraphics()
```

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Overrides:** getGraphics

in class

Component
**Returns:** a graphics context for this component, or

null

if it has none
**Since:** 1.6
**See Also:** Component.paint(java.awt.Graphics)

---

#### getGraphics

@BeanProperty

(

bound

=false)
public

Graphics

getGraphics()

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

repaint

```java
public void repaint​(long time,
int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

**Overrides:** repaint

in class

Component
**Parameters:** time

- maximum time in milliseconds before update
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.6
**See Also:** RepaintManager

---

#### repaint

public void repaint​(long time,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

setDefaultLookAndFeelDecorated

```java
public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)
```

Provides a hint as to whether or not newly created

JFrame

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JFrame

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JFrame

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JFrame by doing the following:

```java
JFrame frame = new JFrame();
frame.setUndecorated(true);
frame.getRootPane().setWindowDecorationStyle(JRootPane.FRAME);
```

**Parameters:** defaultLookAndFeelDecorated

- A hint as to whether or not current
look and feel should provide window decorations
**Since:** 1.4
**See Also:** LookAndFeel.getSupportsWindowDecorations()

---

#### setDefaultLookAndFeelDecorated

public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)

Provides a hint as to whether or not newly created

JFrame

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JFrame

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JFrame

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JFrame by doing the following:

```java
JFrame frame = new JFrame();
frame.setUndecorated(true);
frame.getRootPane().setWindowDecorationStyle(JRootPane.FRAME);
```

You can get the same effect on a single JFrame by doing the following:

```java
JFrame frame = new JFrame();
frame.setUndecorated(true);
frame.getRootPane().setWindowDecorationStyle(JRootPane.FRAME);
```

JFrame frame = new JFrame();
frame.setUndecorated(true);
frame.getRootPane().setWindowDecorationStyle(JRootPane.FRAME);

isDefaultLookAndFeelDecorated

```java
public static boolean isDefaultLookAndFeelDecorated()
```

Returns true if newly created

JFrame

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

**Returns:** true if look and feel should provide Window decorations.
**Since:** 1.4

---

#### isDefaultLookAndFeelDecorated

public static boolean isDefaultLookAndFeelDecorated()

Returns true if newly created

JFrame

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JFrame

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

Frame
**Returns:** a string representation of this

JFrame

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JFrame

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
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JFrame.
For JFrames, the AccessibleContext takes the form of an
AccessibleJFrame.
A new AccessibleJFrame instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Frame
**Returns:** an AccessibleJFrame that serves as the
AccessibleContext of this JFrame

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JFrame.
For JFrames, the AccessibleContext takes the form of an
AccessibleJFrame.
A new AccessibleJFrame instance is created if necessary.

---

