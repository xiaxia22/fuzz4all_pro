# Class JApplet

**Source:** `java.desktop\javax\swing\JApplet.html`

### Class Description

```java
@Deprecated
(
since
="9")

@JavaBean
(
defaultProperty
="JMenuBar",

description
="Swing\'s Applet subclass.")
public class
JApplet

extends
Applet

implements
Accessible
,
RootPaneContainer
```

An extended version of

java.applet.Applet

that adds support for
the JFC/Swing component architecture.
You can find task-oriented documentation about using

JApplet

in

The Java Tutorial

,
in the section

How to Make Applets

.

The

JApplet

class is slightly incompatible with

java.applet.Applet

.

JApplet

contains a

JRootPane

as its only child. The

contentPane

should be the parent of any children of the

JApplet

.
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
For example, you can add a child component to an applet as follows:

```java
applet.add(child);
```

And the child will be added to the

contentPane

.
The

contentPane

will always be non-

null

.
Attempting to set it to

null

will cause the

JApplet

to throw an exception. The default

contentPane

will have a

BorderLayout

manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JApplet

.

Please see the

JRootPane

documentation for a
complete description of the

contentPane

,

glassPane

,
and

layeredPane

properties.

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

---

### Field Details

#### protected
JRootPane
rootPane

**See Also:**
- getRootPane()

,

setRootPane(javax.swing.JRootPane)

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

JApplet

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

AccessibleContext

associated with this

JApplet

---

### Constructor Details

#### public JApplet()
throws
HeadlessException

Creates a swing applet instance.

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

JComponent.getDefaultLocale()

---

### Method Details

#### protected
JRootPane
createRootPane()

Called by the constructor methods to create the default rootPane.

**Returns:**
- a new

JRootPane

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

JApplet

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

- the specified Graphics window

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
="The menubar for accessing pulldown menus from this applet.")
public void setJMenuBar​(
JMenuBar
menuBar)

Sets the menubar for this applet.

**Parameters:**
- menuBar

- the menubar being placed in the applet

**See Also:**
- getJMenuBar()

---

#### public
JMenuBar
getJMenuBar()

Returns the menubar set on this applet.

**Returns:**
- the menubar set on this applet

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

JApplet

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
="the RootPane object for this applet.")
public
JRootPane
getRootPane()

Returns the rootPane object for this applet.

**Specified by:**
- getRootPane

in interface

RootPaneContainer

**Returns:**
- this components single JRootPane child.

**See Also:**
- setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

---

#### protected void setRootPane​(
JRootPane
root)

Sets the rootPane property. This method is called by the constructor.

**Parameters:**
- root

- the rootPane object for this applet

**See Also:**
- getRootPane()

---

#### public
Container
getContentPane()

Returns the contentPane object for this applet.

**Specified by:**
- getContentPane

in interface

RootPaneContainer

**Returns:**
- the value of the contentPane property.

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
="The client area of the applet where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)

Sets the contentPane property. This method is called by the constructor.

**Specified by:**
- setContentPane

in interface

RootPaneContainer

**Parameters:**
- contentPane

- the contentPane object for this applet

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is null

**See Also:**
- getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

---

#### public
JLayeredPane
getLayeredPane()

Returns the layeredPane object for this applet.

**Specified by:**
- getLayeredPane

in interface

RootPaneContainer

**Returns:**
- the value of the layeredPane property.

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null

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
="The pane which holds the various applet layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)

Sets the layeredPane property. This method is called by the constructor.

**Specified by:**
- setLayeredPane

in interface

RootPaneContainer

**Parameters:**
- layeredPane

- the layeredPane object for this applet

**See Also:**
- getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

---

#### public
Component
getGlassPane()

Returns the glassPane object for this applet.

**Specified by:**
- getGlassPane

in interface

RootPaneContainer

**Returns:**
- the value of the glassPane property.

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

Sets the glassPane property.
This method is called by the constructor.

**Specified by:**
- setGlassPane

in interface

RootPaneContainer

**Parameters:**
- glassPane

- the glassPane object for this applet

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

#### protected
String
paramString()

Returns a string representation of this JApplet. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

Container

**Returns:**
- a string representation of this JApplet.

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JApplet.
For JApplets, the AccessibleContext takes the form of an
AccessibleJApplet.
A new AccessibleJApplet instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Applet

**Returns:**
- an AccessibleJApplet that serves as the
AccessibleContext of this JApplet

---

### Additional Sections

#### Class JApplet

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - java.awt.Panel
- - java.applet.Applet
- - javax.swing.JApplet

java.awt.Component

- java.awt.Container
- - java.awt.Panel
- - java.applet.Applet
- - javax.swing.JApplet

java.awt.Container

- java.awt.Panel
- - java.applet.Applet
- - javax.swing.JApplet

java.awt.Panel

- java.applet.Applet
- - javax.swing.JApplet

java.applet.Applet

- javax.swing.JApplet

javax.swing.JApplet

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

RootPaneContainer

```java
@Deprecated
(
since
="9")

@JavaBean
(
defaultProperty
="JMenuBar",

description
="Swing\'s Applet subclass.")
public class
JApplet

extends
Applet

implements
Accessible
,
RootPaneContainer
```

Deprecated.

The Applet API is deprecated, no replacement.

An extended version of

java.applet.Applet

that adds support for
the JFC/Swing component architecture.
You can find task-oriented documentation about using

JApplet

in

The Java Tutorial

,
in the section

How to Make Applets

.

The

JApplet

class is slightly incompatible with

java.applet.Applet

.

JApplet

contains a

JRootPane

as its only child. The

contentPane

should be the parent of any children of the

JApplet

.
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
For example, you can add a child component to an applet as follows:

```java
applet.add(child);
```

And the child will be added to the

contentPane

.
The

contentPane

will always be non-

null

.
Attempting to set it to

null

will cause the

JApplet

to throw an exception. The default

contentPane

will have a

BorderLayout

manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JApplet

.

Please see the

JRootPane

documentation for a
complete description of the

contentPane

,

glassPane

,
and

layeredPane

properties.

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
**See Also:** RootPaneContainer

,

Serialized Form

@Deprecated

(

since

="9")

@JavaBean

(

defaultProperty

="JMenuBar",

description

="Swing\'s Applet subclass.")
public class

JApplet

extends

Applet

implements

Accessible

,

RootPaneContainer

An extended version of

java.applet.Applet

that adds support for
the JFC/Swing component architecture.
You can find task-oriented documentation about using

JApplet

in

The Java Tutorial

,
in the section

How to Make Applets

.

The

JApplet

class is slightly incompatible with

java.applet.Applet

.

JApplet

contains a

JRootPane

as its only child. The

contentPane

should be the parent of any children of the

JApplet

.
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
For example, you can add a child component to an applet as follows:

```java
applet.add(child);
```

And the child will be added to the

contentPane

.
The

contentPane

will always be non-

null

.
Attempting to set it to

null

will cause the

JApplet

to throw an exception. The default

contentPane

will have a

BorderLayout

manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JApplet

.

Please see the

JRootPane

documentation for a
complete description of the

contentPane

,

glassPane

,
and

layeredPane

properties.

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

JApplet

class is slightly incompatible with

java.applet.Applet

.

JApplet

contains a

JRootPane

as its only child. The

contentPane

should be the parent of any children of the

JApplet

.
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
For example, you can add a child component to an applet as follows:

```java
applet.add(child);
```

And the child will be added to the

contentPane

.
The

contentPane

will always be non-

null

.
Attempting to set it to

null

will cause the

JApplet

to throw an exception. The default

contentPane

will have a

BorderLayout

manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JApplet

.

Please see the

JRootPane

documentation for a
complete description of the

contentPane

,

glassPane

,
and

layeredPane

properties.

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

applet.add(child);

Please see the

JRootPane

documentation for a
complete description of the

contentPane

,

glassPane

,
and

layeredPane

properties.

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

JApplet.AccessibleJApplet

Deprecated.

This class implements accessibility support for the

JApplet

class.

- Nested classes/interfaces declared in class java.applet.

Applet

Applet.AccessibleApplet

- Nested classes/interfaces declared in class java.awt.

Panel

Panel.AccessibleAWTPanel

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

Deprecated.

AccessibleContext

associated with this

JApplet

protected

JRootPane

rootPane

Deprecated.

protected boolean

rootPaneCheckingEnabled

Deprecated.

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JApplet

()

Deprecated.

Creates a swing applet instance.

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

Deprecated.

Adds the specified child

Component

.

protected

JRootPane

createRootPane

()

Deprecated.

Called by the constructor methods to create the default rootPane.

AccessibleContext

getAccessibleContext

()

Deprecated.

Gets the AccessibleContext associated with this JApplet.

Container

getContentPane

()

Deprecated.

Returns the contentPane object for this applet.

Component

getGlassPane

()

Deprecated.

Returns the glassPane object for this applet.

Graphics

getGraphics

()

Deprecated.

Creates a graphics context for this component.

JMenuBar

getJMenuBar

()

Deprecated.

Returns the menubar set on this applet.

JLayeredPane

getLayeredPane

()

Deprecated.

Returns the layeredPane object for this applet.

JRootPane

getRootPane

()

Deprecated.

Returns the rootPane object for this applet.

TransferHandler

getTransferHandler

()

Deprecated.

Gets the

transferHandler

property.

protected boolean

isRootPaneCheckingEnabled

()

Deprecated.

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

Deprecated.

Returns a string representation of this JApplet.

void

remove

​(

Component

comp)

Deprecated.

Removes the specified component from the container.

void

repaint

​(long time,
int x,
int y,
int width,
int height)

Deprecated.

Repaints the specified rectangle of this component within

time

milliseconds.

void

setContentPane

​(

Container

contentPane)

Deprecated.

Sets the contentPane property.

void

setGlassPane

​(

Component

glassPane)

Deprecated.

Sets the glassPane property.

void

setJMenuBar

​(

JMenuBar

menuBar)

Deprecated.

Sets the menubar for this applet.

void

setLayeredPane

​(

JLayeredPane

layeredPane)

Deprecated.

Sets the layeredPane property.

void

setLayout

​(

LayoutManager

manager)

Deprecated.

Sets the

LayoutManager

.

protected void

setRootPane

​(

JRootPane

root)

Deprecated.

Sets the rootPane property.

protected void

setRootPaneCheckingEnabled

​(boolean enabled)

Deprecated.

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

Deprecated.

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component.

void

update

​(

Graphics

g)

Deprecated.

Just calls

paint(g)

.

- Methods declared in class java.applet.

Applet

destroy

,

getAppletContext

,

getAppletInfo

,

getAudioClip

,

getAudioClip

,

getCodeBase

,

getDocumentBase

,

getImage

,

getImage

,

getLocale

,

getParameter

,

getParameterInfo

,

init

,

isActive

,

isValidateRoot

,

newAudioClip

,

play

,

play

,

resize

,

resize

,

setStub

,

showStatus

,

start

,

stop

- Methods declared in class java.awt.

Panel

addNotify

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

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getListeners

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

paint

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

processEvent

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

setFocusCycleRoot

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

getBackground

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

getFocusCycleRootAncestor

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

getInputContext

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

getToolkit

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

isOpaque

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

reshape

,

revalidate

,

setBackground

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

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

JApplet.AccessibleJApplet

Deprecated.

This class implements accessibility support for the

JApplet

class.

- Nested classes/interfaces declared in class java.applet.

Applet

Applet.AccessibleApplet

- Nested classes/interfaces declared in class java.awt.

Panel

Panel.AccessibleAWTPanel

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

Deprecated.

This class implements accessibility support for the

JApplet

class.

Nested classes/interfaces declared in class java.applet.

Applet

Applet.AccessibleApplet

---

#### Nested classes/interfaces declared in class java.applet. Applet

Nested classes/interfaces declared in class java.awt.

Panel

Panel.AccessibleAWTPanel

---

#### Nested classes/interfaces declared in class java.awt. Panel

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

Deprecated.

AccessibleContext

associated with this

JApplet

protected

JRootPane

rootPane

Deprecated.

protected boolean

rootPaneCheckingEnabled

Deprecated.

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

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

---

#### Field Summary

Deprecated.

AccessibleContext

associated with this

JApplet

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

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

Constructor Summary

Constructors

Constructor

Description

JApplet

()

Deprecated.

Creates a swing applet instance.

---

#### Constructor Summary

Deprecated.

Creates a swing applet instance.

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

Deprecated.

Adds the specified child

Component

.

protected

JRootPane

createRootPane

()

Deprecated.

Called by the constructor methods to create the default rootPane.

AccessibleContext

getAccessibleContext

()

Deprecated.

Gets the AccessibleContext associated with this JApplet.

Container

getContentPane

()

Deprecated.

Returns the contentPane object for this applet.

Component

getGlassPane

()

Deprecated.

Returns the glassPane object for this applet.

Graphics

getGraphics

()

Deprecated.

Creates a graphics context for this component.

JMenuBar

getJMenuBar

()

Deprecated.

Returns the menubar set on this applet.

JLayeredPane

getLayeredPane

()

Deprecated.

Returns the layeredPane object for this applet.

JRootPane

getRootPane

()

Deprecated.

Returns the rootPane object for this applet.

TransferHandler

getTransferHandler

()

Deprecated.

Gets the

transferHandler

property.

protected boolean

isRootPaneCheckingEnabled

()

Deprecated.

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

Deprecated.

Returns a string representation of this JApplet.

void

remove

​(

Component

comp)

Deprecated.

Removes the specified component from the container.

void

repaint

​(long time,
int x,
int y,
int width,
int height)

Deprecated.

Repaints the specified rectangle of this component within

time

milliseconds.

void

setContentPane

​(

Container

contentPane)

Deprecated.

Sets the contentPane property.

void

setGlassPane

​(

Component

glassPane)

Deprecated.

Sets the glassPane property.

void

setJMenuBar

​(

JMenuBar

menuBar)

Deprecated.

Sets the menubar for this applet.

void

setLayeredPane

​(

JLayeredPane

layeredPane)

Deprecated.

Sets the layeredPane property.

void

setLayout

​(

LayoutManager

manager)

Deprecated.

Sets the

LayoutManager

.

protected void

setRootPane

​(

JRootPane

root)

Deprecated.

Sets the rootPane property.

protected void

setRootPaneCheckingEnabled

​(boolean enabled)

Deprecated.

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

Deprecated.

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component.

void

update

​(

Graphics

g)

Deprecated.

Just calls

paint(g)

.

- Methods declared in class java.applet.

Applet

destroy

,

getAppletContext

,

getAppletInfo

,

getAudioClip

,

getAudioClip

,

getCodeBase

,

getDocumentBase

,

getImage

,

getImage

,

getLocale

,

getParameter

,

getParameterInfo

,

init

,

isActive

,

isValidateRoot

,

newAudioClip

,

play

,

play

,

resize

,

resize

,

setStub

,

showStatus

,

start

,

stop

- Methods declared in class java.awt.

Panel

addNotify

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

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getListeners

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

paint

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

processEvent

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

setFocusCycleRoot

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

getBackground

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

getFocusCycleRootAncestor

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

getInputContext

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

getToolkit

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

isOpaque

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

reshape

,

revalidate

,

setBackground

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

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

Deprecated.

Adds the specified child

Component

.

Called by the constructor methods to create the default rootPane.

Gets the AccessibleContext associated with this JApplet.

Returns the contentPane object for this applet.

Returns the glassPane object for this applet.

Creates a graphics context for this component.

Returns the menubar set on this applet.

Returns the layeredPane object for this applet.

Returns the rootPane object for this applet.

Gets the

transferHandler

property.

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

Returns a string representation of this JApplet.

Removes the specified component from the container.

Repaints the specified rectangle of this component within

time

milliseconds.

Sets the contentPane property.

Sets the glassPane property.

Sets the menubar for this applet.

Sets the layeredPane property.

Sets the

LayoutManager

.

Sets the rootPane property.

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

Methods declared in class java.applet.

Applet

destroy

,

getAppletContext

,

getAppletInfo

,

getAudioClip

,

getAudioClip

,

getCodeBase

,

getDocumentBase

,

getImage

,

getImage

,

getLocale

,

getParameter

,

getParameterInfo

,

init

,

isActive

,

isValidateRoot

,

newAudioClip

,

play

,

play

,

resize

,

resize

,

setStub

,

showStatus

,

start

,

stop

---

#### Methods declared in class java.applet. Applet

Methods declared in class java.awt.

Panel

addNotify

---

#### Methods declared in class java.awt. Panel

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

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getListeners

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

paint

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

processEvent

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

setFocusCycleRoot

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

getBackground

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

getFocusCycleRootAncestor

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

getInputContext

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

getToolkit

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

isOpaque

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

reshape

,

revalidate

,

setBackground

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

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

- rootPane

```java
protected
JRootPane
rootPane
```

Deprecated.

**See Also:** getRootPane()

,

setRootPane(javax.swing.JRootPane)

- rootPaneCheckingEnabled

```java
protected boolean rootPaneCheckingEnabled
```

Deprecated.

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JApplet

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

Deprecated.

AccessibleContext

associated with this

JApplet

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JApplet

```java
public JApplet()
throws
HeadlessException
```

Deprecated.

Creates a swing applet instance.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

============ METHOD DETAIL ==========

- Method Detail

- createRootPane

```java
protected
JRootPane
createRootPane()
```

Deprecated.

Called by the constructor methods to create the default rootPane.

**Returns:** a new

JRootPane

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

Deprecated.

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

JApplet

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

Deprecated.

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

Deprecated.

Just calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:** update

in class

Container
**Parameters:** g

- the specified Graphics window
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
="The menubar for accessing pulldown menus from this applet.")
public void setJMenuBar​(
JMenuBar
menuBar)
```

Deprecated.

Sets the menubar for this applet.

**Parameters:** menuBar

- the menubar being placed in the applet
**See Also:** getJMenuBar()

- getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Deprecated.

Returns the menubar set on this applet.

**Returns:** the menubar set on this applet
**See Also:** setJMenuBar(javax.swing.JMenuBar)

- isRootPaneCheckingEnabled

```java
protected boolean isRootPaneCheckingEnabled()
```

Deprecated.

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

Deprecated.

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

JApplet

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

Deprecated.

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

Deprecated.

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

Deprecated.

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
="the RootPane object for this applet.")
public
JRootPane
getRootPane()
```

Deprecated.

Returns the rootPane object for this applet.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Returns:** this components single JRootPane child.
**See Also:** setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

- setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Deprecated.

Sets the rootPane property. This method is called by the constructor.

**Parameters:** root

- the rootPane object for this applet
**See Also:** getRootPane()

- getContentPane

```java
public
Container
getContentPane()
```

Deprecated.

Returns the contentPane object for this applet.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the value of the contentPane property.
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
="The client area of the applet where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)
```

Deprecated.

Sets the contentPane property. This method is called by the constructor.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** contentPane

- the contentPane object for this applet
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is null
**See Also:** getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

- getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Deprecated.

Returns the layeredPane object for this applet.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** the value of the layeredPane property.
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null
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
="The pane which holds the various applet layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)
```

Deprecated.

Sets the layeredPane property. This method is called by the constructor.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layeredPane

- the layeredPane object for this applet
**See Also:** getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

- getGlassPane

```java
public
Component
getGlassPane()
```

Deprecated.

Returns the glassPane object for this applet.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the value of the glassPane property.
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

Deprecated.

Sets the glassPane property.
This method is called by the constructor.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glassPane

- the glassPane object for this applet
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

Deprecated.

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

Deprecated.

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

- paramString

```java
protected
String
paramString()
```

Deprecated.

Returns a string representation of this JApplet. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

Container
**Returns:** a string representation of this JApplet.

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Deprecated.

Gets the AccessibleContext associated with this JApplet.
For JApplets, the AccessibleContext takes the form of an
AccessibleJApplet.
A new AccessibleJApplet instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Applet
**Returns:** an AccessibleJApplet that serves as the
AccessibleContext of this JApplet

Field Detail

- rootPane

```java
protected
JRootPane
rootPane
```

Deprecated.

**See Also:** getRootPane()

,

setRootPane(javax.swing.JRootPane)

- rootPaneCheckingEnabled

```java
protected boolean rootPaneCheckingEnabled
```

Deprecated.

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JApplet

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

Deprecated.

AccessibleContext

associated with this

JApplet

---

#### Field Detail

rootPane

```java
protected
JRootPane
rootPane
```

Deprecated.

**See Also:** getRootPane()

,

setRootPane(javax.swing.JRootPane)

---

#### rootPane

protected

JRootPane

rootPane

rootPaneCheckingEnabled

```java
protected boolean rootPaneCheckingEnabled
```

Deprecated.

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JApplet

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

JApplet

is constructed.

accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

Deprecated.

AccessibleContext

associated with this

JApplet

---

#### accessibleContext

protected

AccessibleContext

accessibleContext

AccessibleContext

associated with this

JApplet

Constructor Detail

- JApplet

```java
public JApplet()
throws
HeadlessException
```

Deprecated.

Creates a swing applet instance.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### Constructor Detail

JApplet

```java
public JApplet()
throws
HeadlessException
```

Deprecated.

Creates a swing applet instance.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JApplet

public JApplet()
throws

HeadlessException

Creates a swing applet instance.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

Method Detail

- createRootPane

```java
protected
JRootPane
createRootPane()
```

Deprecated.

Called by the constructor methods to create the default rootPane.

**Returns:** a new

JRootPane

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

Deprecated.

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

JApplet

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

Deprecated.

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

Deprecated.

Just calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:** update

in class

Container
**Parameters:** g

- the specified Graphics window
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
="The menubar for accessing pulldown menus from this applet.")
public void setJMenuBar​(
JMenuBar
menuBar)
```

Deprecated.

Sets the menubar for this applet.

**Parameters:** menuBar

- the menubar being placed in the applet
**See Also:** getJMenuBar()

- getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Deprecated.

Returns the menubar set on this applet.

**Returns:** the menubar set on this applet
**See Also:** setJMenuBar(javax.swing.JMenuBar)

- isRootPaneCheckingEnabled

```java
protected boolean isRootPaneCheckingEnabled()
```

Deprecated.

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

Deprecated.

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

JApplet

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

Deprecated.

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

Deprecated.

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

Deprecated.

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
="the RootPane object for this applet.")
public
JRootPane
getRootPane()
```

Deprecated.

Returns the rootPane object for this applet.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Returns:** this components single JRootPane child.
**See Also:** setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

- setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Deprecated.

Sets the rootPane property. This method is called by the constructor.

**Parameters:** root

- the rootPane object for this applet
**See Also:** getRootPane()

- getContentPane

```java
public
Container
getContentPane()
```

Deprecated.

Returns the contentPane object for this applet.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the value of the contentPane property.
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
="The client area of the applet where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)
```

Deprecated.

Sets the contentPane property. This method is called by the constructor.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** contentPane

- the contentPane object for this applet
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is null
**See Also:** getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

- getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Deprecated.

Returns the layeredPane object for this applet.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** the value of the layeredPane property.
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null
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
="The pane which holds the various applet layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)
```

Deprecated.

Sets the layeredPane property. This method is called by the constructor.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layeredPane

- the layeredPane object for this applet
**See Also:** getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

- getGlassPane

```java
public
Component
getGlassPane()
```

Deprecated.

Returns the glassPane object for this applet.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the value of the glassPane property.
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

Deprecated.

Sets the glassPane property.
This method is called by the constructor.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glassPane

- the glassPane object for this applet
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

Deprecated.

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

Deprecated.

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

- paramString

```java
protected
String
paramString()
```

Deprecated.

Returns a string representation of this JApplet. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

Container
**Returns:** a string representation of this JApplet.

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Deprecated.

Gets the AccessibleContext associated with this JApplet.
For JApplets, the AccessibleContext takes the form of an
AccessibleJApplet.
A new AccessibleJApplet instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Applet
**Returns:** an AccessibleJApplet that serves as the
AccessibleContext of this JApplet

---

#### Method Detail

createRootPane

```java
protected
JRootPane
createRootPane()
```

Deprecated.

Called by the constructor methods to create the default rootPane.

**Returns:** a new

JRootPane

---

#### createRootPane

protected

JRootPane

createRootPane()

Called by the constructor methods to create the default rootPane.

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

Deprecated.

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

JApplet

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

JApplet

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

JApplet

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

JApplet

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

Deprecated.

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

Deprecated.

Just calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:** update

in class

Container
**Parameters:** g

- the specified Graphics window
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
="The menubar for accessing pulldown menus from this applet.")
public void setJMenuBar​(
JMenuBar
menuBar)
```

Deprecated.

Sets the menubar for this applet.

**Parameters:** menuBar

- the menubar being placed in the applet
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

="The menubar for accessing pulldown menus from this applet.")
public void setJMenuBar​(

JMenuBar

menuBar)

Sets the menubar for this applet.

getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Deprecated.

Returns the menubar set on this applet.

**Returns:** the menubar set on this applet
**See Also:** setJMenuBar(javax.swing.JMenuBar)

---

#### getJMenuBar

public

JMenuBar

getJMenuBar()

Returns the menubar set on this applet.

isRootPaneCheckingEnabled

```java
protected boolean isRootPaneCheckingEnabled()
```

Deprecated.

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

Deprecated.

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

JApplet

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

Deprecated.

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

Deprecated.

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

Deprecated.

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
="the RootPane object for this applet.")
public
JRootPane
getRootPane()
```

Deprecated.

Returns the rootPane object for this applet.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Returns:** this components single JRootPane child.
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

="the RootPane object for this applet.")
public

JRootPane

getRootPane()

Returns the rootPane object for this applet.

setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Deprecated.

Sets the rootPane property. This method is called by the constructor.

**Parameters:** root

- the rootPane object for this applet
**See Also:** getRootPane()

---

#### setRootPane

protected void setRootPane​(

JRootPane

root)

Sets the rootPane property. This method is called by the constructor.

getContentPane

```java
public
Container
getContentPane()
```

Deprecated.

Returns the contentPane object for this applet.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the value of the contentPane property.
**See Also:** setContentPane(java.awt.Container)

,

RootPaneContainer.getContentPane()

---

#### getContentPane

public

Container

getContentPane()

Returns the contentPane object for this applet.

setContentPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The client area of the applet where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)
```

Deprecated.

Sets the contentPane property. This method is called by the constructor.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** contentPane

- the contentPane object for this applet
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is null
**See Also:** getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

---

#### setContentPane

@BeanProperty

(

bound

=false,

hidden

=true,

description

="The client area of the applet where child components are normally inserted.")
public void setContentPane​(

Container

contentPane)

Sets the contentPane property. This method is called by the constructor.

getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Deprecated.

Returns the layeredPane object for this applet.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** the value of the layeredPane property.
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

---

#### getLayeredPane

public

JLayeredPane

getLayeredPane()

Returns the layeredPane object for this applet.

setLayeredPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The pane which holds the various applet layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)
```

Deprecated.

Sets the layeredPane property. This method is called by the constructor.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layeredPane

- the layeredPane object for this applet
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

="The pane which holds the various applet layers.")
public void setLayeredPane​(

JLayeredPane

layeredPane)

Sets the layeredPane property. This method is called by the constructor.

getGlassPane

```java
public
Component
getGlassPane()
```

Deprecated.

Returns the glassPane object for this applet.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the value of the glassPane property.
**See Also:** setGlassPane(java.awt.Component)

,

RootPaneContainer.getGlassPane()

---

#### getGlassPane

public

Component

getGlassPane()

Returns the glassPane object for this applet.

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

Deprecated.

Sets the glassPane property.
This method is called by the constructor.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glassPane

- the glassPane object for this applet
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

Sets the glassPane property.
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

Deprecated.

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

Deprecated.

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

paramString

```java
protected
String
paramString()
```

Deprecated.

Returns a string representation of this JApplet. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

Container
**Returns:** a string representation of this JApplet.

---

#### paramString

protected

String

paramString()

Returns a string representation of this JApplet. This method
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

Deprecated.

Gets the AccessibleContext associated with this JApplet.
For JApplets, the AccessibleContext takes the form of an
AccessibleJApplet.
A new AccessibleJApplet instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Applet
**Returns:** an AccessibleJApplet that serves as the
AccessibleContext of this JApplet

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JApplet.
For JApplets, the AccessibleContext takes the form of an
AccessibleJApplet.
A new AccessibleJApplet instance is created if necessary.

---

