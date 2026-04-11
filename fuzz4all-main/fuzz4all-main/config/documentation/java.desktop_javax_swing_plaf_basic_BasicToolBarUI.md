# Class BasicToolBarUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicToolBarUI.html`

### Class Description

```java
public class
BasicToolBarUI

extends
ToolBarUI

implements
SwingConstants
```

A Basic L&F implementation of ToolBarUI. This implementation
is a "combined" view/controller.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

#### protected
JToolBar
toolBar

The instance of

JToolBar

.

---

#### protected
BasicToolBarUI.DragWindow
dragWindow

The instance of

DragWindow

.

---

#### protected int focusedCompIndex

The index of the focused component.

---

#### protected
Color
dockingColor

The background color of the docking border.

---

#### protected
Color
floatingColor

The background color of the not docking border.

---

#### protected
Color
dockingBorderColor

The color of the docking border.

---

#### protected
Color
floatingBorderColor

The color of the not docking border.

---

#### protected
MouseInputListener
dockingListener

The instance of a

MouseInputListener

.

---

#### protected
PropertyChangeListener
propertyListener

The instance of a

PropertyChangeListener

.

---

#### protected
ContainerListener
toolBarContListener

The instance of a

ContainerListener

.

---

#### protected
FocusListener
toolBarFocusListener

The instance of a

FocusListener

.

---

#### protected
String
constraintBeforeFloating

The layout before floating.

---

#### @Deprecated

protected
KeyStroke
upKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
downKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
leftKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
rightKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

### Constructor Details

#### public BasicToolBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs a new instance of

BasicToolBarUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

BasicToolBarUI

---

#### protected void installDefaults()

Installs default properties.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected void installComponents()

Registers components.

---

#### protected void uninstallComponents()

Unregisters components.

---

#### protected void installListeners()

Registers listeners.

---

#### protected void uninstallListeners()

Unregisters listeners.

---

#### protected void installKeyboardActions()

Registers keyboard actions.

---

#### protected void uninstallKeyboardActions()

Unregisters keyboard actions.

---

#### protected void navigateFocusedComp​(int direction)

Navigates the focused component.

**Parameters:**
- direction

- a direction

---

#### protected
Border
createRolloverBorder()

Creates a rollover border for toolbar components. The
rollover border will be installed if rollover borders are
enabled.

Override this method to provide an alternate rollover border.

**Returns:**
- a rollover border for toolbar components

**Since:**
- 1.4

---

#### protected
Border
createNonRolloverBorder()

Creates the non rollover border for toolbar components. This
border will be installed as the border for components added
to the toolbar if rollover borders are not enabled.

Override this method to provide an alternate rollover border.

**Returns:**
- the non rollover border for toolbar components

**Since:**
- 1.4

---

#### protected
JFrame
createFloatingFrame​(
JToolBar
toolbar)

No longer used, use BasicToolBarUI.createFloatingWindow(JToolBar)

**Parameters:**
- toolbar

- an instance of

JToolBar

**Returns:**
- an instance of

JFrame

**See Also:**
- createFloatingWindow(javax.swing.JToolBar)

---

#### protected
RootPaneContainer
createFloatingWindow​(
JToolBar
toolbar)

Creates a window which contains the toolbar after it has been
dragged out from its container

**Parameters:**
- toolbar

- an instance of

JToolBar

**Returns:**
- a

RootPaneContainer

object, containing the toolbar

**Since:**
- 1.4

---

#### protected
BasicToolBarUI.DragWindow
createDragWindow​(
JToolBar
toolbar)

Returns an instance of

DragWindow

.

**Parameters:**
- toolbar

- an instance of

JToolBar

**Returns:**
- an instance of

DragWindow

---

#### public boolean isRolloverBorders()

Returns a flag to determine whether rollover button borders
are enabled.

**Returns:**
- true if rollover borders are enabled; false otherwise

**See Also:**
- setRolloverBorders(boolean)

**Since:**
- 1.4

---

#### public void setRolloverBorders​(boolean rollover)

Sets the flag for enabling rollover borders on the toolbar and it will
also install the appropriate border depending on the state of the flag.

**Parameters:**
- rollover

- if true, rollover borders are installed.
Otherwise non-rollover borders are installed

**See Also:**
- isRolloverBorders()

**Since:**
- 1.4

---

#### protected void installRolloverBorders​(
JComponent
c)

Installs rollover borders on all the child components of the JComponent.

This is a convenience method to call

setBorderToRollover

for each child component.

**Parameters:**
- c

- container which holds the child components (usually a JToolBar)

**See Also:**
- setBorderToRollover(java.awt.Component)

**Since:**
- 1.4

---

#### protected void installNonRolloverBorders​(
JComponent
c)

Installs non-rollover borders on all the child components of the JComponent.
A non-rollover border is the border that is installed on the child component
while it is in the toolbar.

This is a convenience method to call

setBorderToNonRollover

for each child component.

**Parameters:**
- c

- container which holds the child components (usually a JToolBar)

**See Also:**
- setBorderToNonRollover(java.awt.Component)

**Since:**
- 1.4

---

#### protected void installNormalBorders​(
JComponent
c)

Installs normal borders on all the child components of the JComponent.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

This is a convenience method to call

setBorderNormal

for each child component.

**Parameters:**
- c

- container which holds the child components (usually a JToolBar)

**See Also:**
- setBorderToNonRollover(java.awt.Component)

**Since:**
- 1.4

---

#### protected void setBorderToRollover​(
Component
c)

Sets the border of the component to have a rollover border which
was created by the

createRolloverBorder()

method.

**Parameters:**
- c

- component which will have a rollover border installed

**See Also:**
- createRolloverBorder()

**Since:**
- 1.4

---

#### protected
Border
getRolloverBorder​(
AbstractButton
b)

Returns a rollover border for the button.

**Parameters:**
- b

- the button to calculate the rollover border for

**Returns:**
- the rollover border

**See Also:**
- setBorderToRollover(java.awt.Component)

**Since:**
- 1.6

---

#### protected void setBorderToNonRollover​(
Component
c)

Sets the border of the component to have a non-rollover border which
was created by the

createNonRolloverBorder()

method.

**Parameters:**
- c

- component which will have a non-rollover border installed

**See Also:**
- createNonRolloverBorder()

**Since:**
- 1.4

---

#### protected
Border
getNonRolloverBorder​(
AbstractButton
b)

Returns a non-rollover border for the button.

**Parameters:**
- b

- the button to calculate the non-rollover border for

**Returns:**
- the non-rollover border

**See Also:**
- setBorderToNonRollover(java.awt.Component)

**Since:**
- 1.6

---

#### protected void setBorderToNormal​(
Component
c)

Sets the border of the component to have a normal border.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

**Parameters:**
- c

- component which will have a normal border re-installed

**See Also:**
- createNonRolloverBorder()

**Since:**
- 1.4

---

#### public void setFloatingLocation​(int x,
int y)

Sets the floating location.

**Parameters:**
- x

- an X coordinate
- y

- an Y coordinate

---

#### public boolean isFloating()

Returns

true

if the

JToolBar

is floating

**Returns:**
- true

if the

JToolBar

is floating

---

#### public void setFloating​(boolean b,

Point
p)

Sets the floating property.

**Parameters:**
- b

-

true

if the

JToolBar

is floating
- p

- the position

---

#### public void setOrientation​(int orientation)

Sets the tool bar's orientation.

**Parameters:**
- orientation

- the new orientation

---

#### public
Color
getDockingColor()

Gets the color displayed when over a docking area

**Returns:**
- the color displayed when over a docking area

---

#### public void setDockingColor​(
Color
c)

Sets the color displayed when over a docking area

**Parameters:**
- c

- the new color

---

#### public
Color
getFloatingColor()

Gets the color displayed when over a floating area

**Returns:**
- the color displayed when over a floating area

---

#### public void setFloatingColor​(
Color
c)

Sets the color displayed when over a floating area

**Parameters:**
- c

- the new color

---

#### public boolean canDock​(
Component
c,

Point
p)

Returns

true

if the

JToolBar

can dock at the given position.

**Parameters:**
- c

- a component
- p

- a position

**Returns:**
- true

if the

JToolBar

can dock at the given position

---

#### protected void dragTo​(
Point
position,

Point
origin)

The method is used to drag

DragWindow

during the

JToolBar

is being dragged.

**Parameters:**
- position

- the relative to the

JTollBar

position
- origin

- the screen position of

JToolBar

before dragging

---

#### protected void floatAt​(
Point
position,

Point
origin)

The method is called at end of dragging to place the frame in either
its original place or in its floating frame.

**Parameters:**
- position

- the relative to the

JTollBar

position
- origin

- the screen position of

JToolBar

before dragging

---

#### protected
ContainerListener
createToolBarContListener()

Returns an instance of

ContainerListener

.

**Returns:**
- an instance of

ContainerListener

---

#### protected
FocusListener
createToolBarFocusListener()

Returns an instance of

FocusListener

.

**Returns:**
- an instance of

FocusListener

---

#### protected
PropertyChangeListener
createPropertyListener()

Returns an instance of

PropertyChangeListener

.

**Returns:**
- an instance of

PropertyChangeListener

---

#### protected
MouseInputListener
createDockingListener()

Returns an instance of

MouseInputListener

.

**Returns:**
- an instance of

MouseInputListener

---

#### protected
WindowListener
createFrameListener()

Constructs a new instance of

WindowListener

.

**Returns:**
- a new instance of

WindowListener

---

#### protected void paintDragWindow​(
Graphics
g)

Paints the contents of the window used for dragging.

**Parameters:**
- g

- Graphics to paint to.

**Throws:**
- NullPointerException

- is

g

is null

**Since:**
- 1.5

---

### Additional Sections

#### Class BasicToolBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ToolBarUI
- - javax.swing.plaf.basic.BasicToolBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ToolBarUI
- - javax.swing.plaf.basic.BasicToolBarUI

javax.swing.plaf.ToolBarUI

- javax.swing.plaf.basic.BasicToolBarUI

javax.swing.plaf.basic.BasicToolBarUI

**All Implemented Interfaces:** SwingConstants

**Direct Known Subclasses:** MetalToolBarUI

,

SynthToolBarUI

```java
public class
BasicToolBarUI

extends
ToolBarUI

implements
SwingConstants
```

A Basic L&F implementation of ToolBarUI. This implementation
is a "combined" view/controller.

public class

BasicToolBarUI

extends

ToolBarUI

implements

SwingConstants

A Basic L&F implementation of ToolBarUI. This implementation
is a "combined" view/controller.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicToolBarUI.DockingListener

This class should be treated as a "protected" inner class.

protected class

BasicToolBarUI.DragWindow

The window which appears during dragging the

JToolBar

.

protected class

BasicToolBarUI.FrameListener

The class listens for window events.

protected class

BasicToolBarUI.PropertyListener

The class listens for property changed events.

protected class

BasicToolBarUI.ToolBarContListener

The class listens for component events.

protected class

BasicToolBarUI.ToolBarFocusListener

The class listens for focus events.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

constraintBeforeFloating

The layout before floating.

protected

Color

dockingBorderColor

The color of the docking border.

protected

Color

dockingColor

The background color of the docking border.

protected

MouseInputListener

dockingListener

The instance of a

MouseInputListener

.

protected

KeyStroke

downKey

Deprecated.

As of Java 2 platform v1.3.

protected

BasicToolBarUI.DragWindow

dragWindow

The instance of

DragWindow

.

protected

Color

floatingBorderColor

The color of the not docking border.

protected

Color

floatingColor

The background color of the not docking border.

protected int

focusedCompIndex

The index of the focused component.

protected

KeyStroke

leftKey

Deprecated.

As of Java 2 platform v1.3.

protected

PropertyChangeListener

propertyListener

The instance of a

PropertyChangeListener

.

protected

KeyStroke

rightKey

Deprecated.

As of Java 2 platform v1.3.

protected

JToolBar

toolBar

The instance of

JToolBar

.

protected

ContainerListener

toolBarContListener

The instance of a

ContainerListener

.

protected

FocusListener

toolBarFocusListener

The instance of a

FocusListener

.

protected

KeyStroke

upKey

Deprecated.

As of Java 2 platform v1.3.

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

BasicToolBarUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canDock

​(

Component

c,

Point

p)

Returns

true

if the

JToolBar

can dock at the given position.

protected

MouseInputListener

createDockingListener

()

Returns an instance of

MouseInputListener

.

protected

BasicToolBarUI.DragWindow

createDragWindow

​(

JToolBar

toolbar)

Returns an instance of

DragWindow

.

protected

JFrame

createFloatingFrame

​(

JToolBar

toolbar)

No longer used, use BasicToolBarUI.createFloatingWindow(JToolBar)

protected

RootPaneContainer

createFloatingWindow

​(

JToolBar

toolbar)

Creates a window which contains the toolbar after it has been
dragged out from its container

protected

WindowListener

createFrameListener

()

Constructs a new instance of

WindowListener

.

protected

Border

createNonRolloverBorder

()

Creates the non rollover border for toolbar components.

protected

PropertyChangeListener

createPropertyListener

()

Returns an instance of

PropertyChangeListener

.

protected

Border

createRolloverBorder

()

Creates a rollover border for toolbar components.

protected

ContainerListener

createToolBarContListener

()

Returns an instance of

ContainerListener

.

protected

FocusListener

createToolBarFocusListener

()

Returns an instance of

FocusListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

BasicToolBarUI

.

protected void

dragTo

​(

Point

position,

Point

origin)

The method is used to drag

DragWindow

during the

JToolBar

is being dragged.

protected void

floatAt

​(

Point

position,

Point

origin)

The method is called at end of dragging to place the frame in either
its original place or in its floating frame.

Color

getDockingColor

()

Gets the color displayed when over a docking area

Color

getFloatingColor

()

Gets the color displayed when over a floating area

protected

Border

getNonRolloverBorder

​(

AbstractButton

b)

Returns a non-rollover border for the button.

protected

Border

getRolloverBorder

​(

AbstractButton

b)

Returns a rollover border for the button.

protected void

installComponents

()

Registers components.

protected void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListeners

()

Registers listeners.

protected void

installNonRolloverBorders

​(

JComponent

c)

Installs non-rollover borders on all the child components of the JComponent.

protected void

installNormalBorders

​(

JComponent

c)

Installs normal borders on all the child components of the JComponent.

protected void

installRolloverBorders

​(

JComponent

c)

Installs rollover borders on all the child components of the JComponent.

boolean

isFloating

()

Returns

true

if the

JToolBar

is floating

boolean

isRolloverBorders

()

Returns a flag to determine whether rollover button borders
are enabled.

protected void

navigateFocusedComp

​(int direction)

Navigates the focused component.

protected void

paintDragWindow

​(

Graphics

g)

Paints the contents of the window used for dragging.

protected void

setBorderToNonRollover

​(

Component

c)

Sets the border of the component to have a non-rollover border which
was created by the

createNonRolloverBorder()

method.

protected void

setBorderToNormal

​(

Component

c)

Sets the border of the component to have a normal border.

protected void

setBorderToRollover

​(

Component

c)

Sets the border of the component to have a rollover border which
was created by the

createRolloverBorder()

method.

void

setDockingColor

​(

Color

c)

Sets the color displayed when over a docking area

void

setFloating

​(boolean b,

Point

p)

Sets the floating property.

void

setFloatingColor

​(

Color

c)

Sets the color displayed when over a floating area

void

setFloatingLocation

​(int x,
int y)

Sets the floating location.

void

setOrientation

​(int orientation)

Sets the tool bar's orientation.

void

setRolloverBorders

​(boolean rollover)

Sets the flag for enabling rollover borders on the toolbar and it will
also install the appropriate border depending on the state of the flag.

protected void

uninstallComponents

()

Unregisters components.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

class

BasicToolBarUI.DockingListener

This class should be treated as a "protected" inner class.

protected class

BasicToolBarUI.DragWindow

The window which appears during dragging the

JToolBar

.

protected class

BasicToolBarUI.FrameListener

The class listens for window events.

protected class

BasicToolBarUI.PropertyListener

The class listens for property changed events.

protected class

BasicToolBarUI.ToolBarContListener

The class listens for component events.

protected class

BasicToolBarUI.ToolBarFocusListener

The class listens for focus events.

---

#### Nested Class Summary

This class should be treated as a "protected" inner class.

The window which appears during dragging the

JToolBar

.

The class listens for window events.

The class listens for property changed events.

The class listens for component events.

The class listens for focus events.

Field Summary

Fields

Modifier and Type

Field

Description

protected

String

constraintBeforeFloating

The layout before floating.

protected

Color

dockingBorderColor

The color of the docking border.

protected

Color

dockingColor

The background color of the docking border.

protected

MouseInputListener

dockingListener

The instance of a

MouseInputListener

.

protected

KeyStroke

downKey

Deprecated.

As of Java 2 platform v1.3.

protected

BasicToolBarUI.DragWindow

dragWindow

The instance of

DragWindow

.

protected

Color

floatingBorderColor

The color of the not docking border.

protected

Color

floatingColor

The background color of the not docking border.

protected int

focusedCompIndex

The index of the focused component.

protected

KeyStroke

leftKey

Deprecated.

As of Java 2 platform v1.3.

protected

PropertyChangeListener

propertyListener

The instance of a

PropertyChangeListener

.

protected

KeyStroke

rightKey

Deprecated.

As of Java 2 platform v1.3.

protected

JToolBar

toolBar

The instance of

JToolBar

.

protected

ContainerListener

toolBarContListener

The instance of a

ContainerListener

.

protected

FocusListener

toolBarFocusListener

The instance of a

FocusListener

.

protected

KeyStroke

upKey

Deprecated.

As of Java 2 platform v1.3.

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

The layout before floating.

The color of the docking border.

The background color of the docking border.

The instance of a

MouseInputListener

.

Deprecated.

As of Java 2 platform v1.3.

The instance of

DragWindow

.

The color of the not docking border.

The background color of the not docking border.

The index of the focused component.

The instance of a

PropertyChangeListener

.

The instance of

JToolBar

.

The instance of a

ContainerListener

.

The instance of a

FocusListener

.

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

BasicToolBarUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canDock

​(

Component

c,

Point

p)

Returns

true

if the

JToolBar

can dock at the given position.

protected

MouseInputListener

createDockingListener

()

Returns an instance of

MouseInputListener

.

protected

BasicToolBarUI.DragWindow

createDragWindow

​(

JToolBar

toolbar)

Returns an instance of

DragWindow

.

protected

JFrame

createFloatingFrame

​(

JToolBar

toolbar)

No longer used, use BasicToolBarUI.createFloatingWindow(JToolBar)

protected

RootPaneContainer

createFloatingWindow

​(

JToolBar

toolbar)

Creates a window which contains the toolbar after it has been
dragged out from its container

protected

WindowListener

createFrameListener

()

Constructs a new instance of

WindowListener

.

protected

Border

createNonRolloverBorder

()

Creates the non rollover border for toolbar components.

protected

PropertyChangeListener

createPropertyListener

()

Returns an instance of

PropertyChangeListener

.

protected

Border

createRolloverBorder

()

Creates a rollover border for toolbar components.

protected

ContainerListener

createToolBarContListener

()

Returns an instance of

ContainerListener

.

protected

FocusListener

createToolBarFocusListener

()

Returns an instance of

FocusListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

BasicToolBarUI

.

protected void

dragTo

​(

Point

position,

Point

origin)

The method is used to drag

DragWindow

during the

JToolBar

is being dragged.

protected void

floatAt

​(

Point

position,

Point

origin)

The method is called at end of dragging to place the frame in either
its original place or in its floating frame.

Color

getDockingColor

()

Gets the color displayed when over a docking area

Color

getFloatingColor

()

Gets the color displayed when over a floating area

protected

Border

getNonRolloverBorder

​(

AbstractButton

b)

Returns a non-rollover border for the button.

protected

Border

getRolloverBorder

​(

AbstractButton

b)

Returns a rollover border for the button.

protected void

installComponents

()

Registers components.

protected void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListeners

()

Registers listeners.

protected void

installNonRolloverBorders

​(

JComponent

c)

Installs non-rollover borders on all the child components of the JComponent.

protected void

installNormalBorders

​(

JComponent

c)

Installs normal borders on all the child components of the JComponent.

protected void

installRolloverBorders

​(

JComponent

c)

Installs rollover borders on all the child components of the JComponent.

boolean

isFloating

()

Returns

true

if the

JToolBar

is floating

boolean

isRolloverBorders

()

Returns a flag to determine whether rollover button borders
are enabled.

protected void

navigateFocusedComp

​(int direction)

Navigates the focused component.

protected void

paintDragWindow

​(

Graphics

g)

Paints the contents of the window used for dragging.

protected void

setBorderToNonRollover

​(

Component

c)

Sets the border of the component to have a non-rollover border which
was created by the

createNonRolloverBorder()

method.

protected void

setBorderToNormal

​(

Component

c)

Sets the border of the component to have a normal border.

protected void

setBorderToRollover

​(

Component

c)

Sets the border of the component to have a rollover border which
was created by the

createRolloverBorder()

method.

void

setDockingColor

​(

Color

c)

Sets the color displayed when over a docking area

void

setFloating

​(boolean b,

Point

p)

Sets the floating property.

void

setFloatingColor

​(

Color

c)

Sets the color displayed when over a floating area

void

setFloatingLocation

​(int x,
int y)

Sets the floating location.

void

setOrientation

​(int orientation)

Sets the tool bar's orientation.

void

setRolloverBorders

​(boolean rollover)

Sets the flag for enabling rollover borders on the toolbar and it will
also install the appropriate border depending on the state of the flag.

protected void

uninstallComponents

()

Unregisters components.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

Returns

true

if the

JToolBar

can dock at the given position.

Returns an instance of

MouseInputListener

.

Returns an instance of

DragWindow

.

No longer used, use BasicToolBarUI.createFloatingWindow(JToolBar)

Creates a window which contains the toolbar after it has been
dragged out from its container

Constructs a new instance of

WindowListener

.

Creates the non rollover border for toolbar components.

Returns an instance of

PropertyChangeListener

.

Creates a rollover border for toolbar components.

Returns an instance of

ContainerListener

.

Returns an instance of

FocusListener

.

Constructs a new instance of

BasicToolBarUI

.

The method is used to drag

DragWindow

during the

JToolBar

is being dragged.

The method is called at end of dragging to place the frame in either
its original place or in its floating frame.

Gets the color displayed when over a docking area

Gets the color displayed when over a floating area

Returns a non-rollover border for the button.

Returns a rollover border for the button.

Registers components.

Installs default properties.

Registers keyboard actions.

Registers listeners.

Installs non-rollover borders on all the child components of the JComponent.

Installs normal borders on all the child components of the JComponent.

Installs rollover borders on all the child components of the JComponent.

Returns

true

if the

JToolBar

is floating

Returns a flag to determine whether rollover button borders
are enabled.

Navigates the focused component.

Paints the contents of the window used for dragging.

Sets the border of the component to have a non-rollover border which
was created by the

createNonRolloverBorder()

method.

Sets the border of the component to have a normal border.

Sets the border of the component to have a rollover border which
was created by the

createRolloverBorder()

method.

Sets the color displayed when over a docking area

Sets the floating property.

Sets the color displayed when over a floating area

Sets the floating location.

Sets the tool bar's orientation.

Sets the flag for enabling rollover borders on the toolbar and it will
also install the appropriate border depending on the state of the flag.

Unregisters components.

Uninstalls default properties.

Unregisters keyboard actions.

Unregisters listeners.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

- toolBar

```java
protected
JToolBar
toolBar
```

The instance of

JToolBar

.

- dragWindow

```java
protected
BasicToolBarUI.DragWindow
dragWindow
```

The instance of

DragWindow

.

- focusedCompIndex

```java
protected int focusedCompIndex
```

The index of the focused component.

- dockingColor

```java
protected
Color
dockingColor
```

The background color of the docking border.

- floatingColor

```java
protected
Color
floatingColor
```

The background color of the not docking border.

- dockingBorderColor

```java
protected
Color
dockingBorderColor
```

The color of the docking border.

- floatingBorderColor

```java
protected
Color
floatingBorderColor
```

The color of the not docking border.

- dockingListener

```java
protected
MouseInputListener
dockingListener
```

The instance of a

MouseInputListener

.

- propertyListener

```java
protected
PropertyChangeListener
propertyListener
```

The instance of a

PropertyChangeListener

.

- toolBarContListener

```java
protected
ContainerListener
toolBarContListener
```

The instance of a

ContainerListener

.

- toolBarFocusListener

```java
protected
FocusListener
toolBarFocusListener
```

The instance of a

FocusListener

.

- constraintBeforeFloating

```java
protected
String
constraintBeforeFloating
```

The layout before floating.

- upKey

```java
@Deprecated

protected
KeyStroke
upKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- downKey

```java
@Deprecated

protected
KeyStroke
downKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- leftKey

```java
@Deprecated

protected
KeyStroke
leftKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- rightKey

```java
@Deprecated

protected
KeyStroke
rightKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicToolBarUI

```java
public BasicToolBarUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new instance of

BasicToolBarUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicToolBarUI

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- installComponents

```java
protected void installComponents()
```

Registers components.

- uninstallComponents

```java
protected void uninstallComponents()
```

Unregisters components.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- navigateFocusedComp

```java
protected void navigateFocusedComp​(int direction)
```

Navigates the focused component.

**Parameters:** direction

- a direction

- createRolloverBorder

```java
protected
Border
createRolloverBorder()
```

Creates a rollover border for toolbar components. The
rollover border will be installed if rollover borders are
enabled.

Override this method to provide an alternate rollover border.

**Returns:** a rollover border for toolbar components
**Since:** 1.4

- createNonRolloverBorder

```java
protected
Border
createNonRolloverBorder()
```

Creates the non rollover border for toolbar components. This
border will be installed as the border for components added
to the toolbar if rollover borders are not enabled.

Override this method to provide an alternate rollover border.

**Returns:** the non rollover border for toolbar components
**Since:** 1.4

- createFloatingFrame

```java
protected
JFrame
createFloatingFrame​(
JToolBar
toolbar)
```

No longer used, use BasicToolBarUI.createFloatingWindow(JToolBar)

**Parameters:** toolbar

- an instance of

JToolBar
**Returns:** an instance of

JFrame
**See Also:** createFloatingWindow(javax.swing.JToolBar)

- createFloatingWindow

```java
protected
RootPaneContainer
createFloatingWindow​(
JToolBar
toolbar)
```

Creates a window which contains the toolbar after it has been
dragged out from its container

**Parameters:** toolbar

- an instance of

JToolBar
**Returns:** a

RootPaneContainer

object, containing the toolbar
**Since:** 1.4

- createDragWindow

```java
protected
BasicToolBarUI.DragWindow
createDragWindow​(
JToolBar
toolbar)
```

Returns an instance of

DragWindow

.

**Parameters:** toolbar

- an instance of

JToolBar
**Returns:** an instance of

DragWindow

- isRolloverBorders

```java
public boolean isRolloverBorders()
```

Returns a flag to determine whether rollover button borders
are enabled.

**Returns:** true if rollover borders are enabled; false otherwise
**Since:** 1.4
**See Also:** setRolloverBorders(boolean)

- setRolloverBorders

```java
public void setRolloverBorders​(boolean rollover)
```

Sets the flag for enabling rollover borders on the toolbar and it will
also install the appropriate border depending on the state of the flag.

**Parameters:** rollover

- if true, rollover borders are installed.
Otherwise non-rollover borders are installed
**Since:** 1.4
**See Also:** isRolloverBorders()

- installRolloverBorders

```java
protected void installRolloverBorders​(
JComponent
c)
```

Installs rollover borders on all the child components of the JComponent.

This is a convenience method to call

setBorderToRollover

for each child component.

**Parameters:** c

- container which holds the child components (usually a JToolBar)
**Since:** 1.4
**See Also:** setBorderToRollover(java.awt.Component)

- installNonRolloverBorders

```java
protected void installNonRolloverBorders​(
JComponent
c)
```

Installs non-rollover borders on all the child components of the JComponent.
A non-rollover border is the border that is installed on the child component
while it is in the toolbar.

This is a convenience method to call

setBorderToNonRollover

for each child component.

**Parameters:** c

- container which holds the child components (usually a JToolBar)
**Since:** 1.4
**See Also:** setBorderToNonRollover(java.awt.Component)

- installNormalBorders

```java
protected void installNormalBorders​(
JComponent
c)
```

Installs normal borders on all the child components of the JComponent.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

This is a convenience method to call

setBorderNormal

for each child component.

**Parameters:** c

- container which holds the child components (usually a JToolBar)
**Since:** 1.4
**See Also:** setBorderToNonRollover(java.awt.Component)

- setBorderToRollover

```java
protected void setBorderToRollover​(
Component
c)
```

Sets the border of the component to have a rollover border which
was created by the

createRolloverBorder()

method.

**Parameters:** c

- component which will have a rollover border installed
**Since:** 1.4
**See Also:** createRolloverBorder()

- getRolloverBorder

```java
protected
Border
getRolloverBorder​(
AbstractButton
b)
```

Returns a rollover border for the button.

**Parameters:** b

- the button to calculate the rollover border for
**Returns:** the rollover border
**Since:** 1.6
**See Also:** setBorderToRollover(java.awt.Component)

- setBorderToNonRollover

```java
protected void setBorderToNonRollover​(
Component
c)
```

Sets the border of the component to have a non-rollover border which
was created by the

createNonRolloverBorder()

method.

**Parameters:** c

- component which will have a non-rollover border installed
**Since:** 1.4
**See Also:** createNonRolloverBorder()

- getNonRolloverBorder

```java
protected
Border
getNonRolloverBorder​(
AbstractButton
b)
```

Returns a non-rollover border for the button.

**Parameters:** b

- the button to calculate the non-rollover border for
**Returns:** the non-rollover border
**Since:** 1.6
**See Also:** setBorderToNonRollover(java.awt.Component)

- setBorderToNormal

```java
protected void setBorderToNormal​(
Component
c)
```

Sets the border of the component to have a normal border.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

**Parameters:** c

- component which will have a normal border re-installed
**Since:** 1.4
**See Also:** createNonRolloverBorder()

- setFloatingLocation

```java
public void setFloatingLocation​(int x,
int y)
```

Sets the floating location.

**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate

- isFloating

```java
public boolean isFloating()
```

Returns

true

if the

JToolBar

is floating

**Returns:** true

if the

JToolBar

is floating

- setFloating

```java
public void setFloating​(boolean b,

Point
p)
```

Sets the floating property.

**Parameters:** b

-

true

if the

JToolBar

is floating
**Parameters:** p

- the position

- setOrientation

```java
public void setOrientation​(int orientation)
```

Sets the tool bar's orientation.

**Parameters:** orientation

- the new orientation

- getDockingColor

```java
public
Color
getDockingColor()
```

Gets the color displayed when over a docking area

**Returns:** the color displayed when over a docking area

- setDockingColor

```java
public void setDockingColor​(
Color
c)
```

Sets the color displayed when over a docking area

**Parameters:** c

- the new color

- getFloatingColor

```java
public
Color
getFloatingColor()
```

Gets the color displayed when over a floating area

**Returns:** the color displayed when over a floating area

- setFloatingColor

```java
public void setFloatingColor​(
Color
c)
```

Sets the color displayed when over a floating area

**Parameters:** c

- the new color

- canDock

```java
public boolean canDock​(
Component
c,

Point
p)
```

Returns

true

if the

JToolBar

can dock at the given position.

**Parameters:** c

- a component
**Parameters:** p

- a position
**Returns:** true

if the

JToolBar

can dock at the given position

- dragTo

```java
protected void dragTo​(
Point
position,

Point
origin)
```

The method is used to drag

DragWindow

during the

JToolBar

is being dragged.

**Parameters:** position

- the relative to the

JTollBar

position
**Parameters:** origin

- the screen position of

JToolBar

before dragging

- floatAt

```java
protected void floatAt​(
Point
position,

Point
origin)
```

The method is called at end of dragging to place the frame in either
its original place or in its floating frame.

**Parameters:** position

- the relative to the

JTollBar

position
**Parameters:** origin

- the screen position of

JToolBar

before dragging

- createToolBarContListener

```java
protected
ContainerListener
createToolBarContListener()
```

Returns an instance of

ContainerListener

.

**Returns:** an instance of

ContainerListener

- createToolBarFocusListener

```java
protected
FocusListener
createToolBarFocusListener()
```

Returns an instance of

FocusListener

.

**Returns:** an instance of

FocusListener

- createPropertyListener

```java
protected
PropertyChangeListener
createPropertyListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

- createDockingListener

```java
protected
MouseInputListener
createDockingListener()
```

Returns an instance of

MouseInputListener

.

**Returns:** an instance of

MouseInputListener

- createFrameListener

```java
protected
WindowListener
createFrameListener()
```

Constructs a new instance of

WindowListener

.

**Returns:** a new instance of

WindowListener

- paintDragWindow

```java
protected void paintDragWindow​(
Graphics
g)
```

Paints the contents of the window used for dragging.

**Parameters:** g

- Graphics to paint to.
**Throws:** NullPointerException

- is

g

is null
**Since:** 1.5

Field Detail

- toolBar

```java
protected
JToolBar
toolBar
```

The instance of

JToolBar

.

- dragWindow

```java
protected
BasicToolBarUI.DragWindow
dragWindow
```

The instance of

DragWindow

.

- focusedCompIndex

```java
protected int focusedCompIndex
```

The index of the focused component.

- dockingColor

```java
protected
Color
dockingColor
```

The background color of the docking border.

- floatingColor

```java
protected
Color
floatingColor
```

The background color of the not docking border.

- dockingBorderColor

```java
protected
Color
dockingBorderColor
```

The color of the docking border.

- floatingBorderColor

```java
protected
Color
floatingBorderColor
```

The color of the not docking border.

- dockingListener

```java
protected
MouseInputListener
dockingListener
```

The instance of a

MouseInputListener

.

- propertyListener

```java
protected
PropertyChangeListener
propertyListener
```

The instance of a

PropertyChangeListener

.

- toolBarContListener

```java
protected
ContainerListener
toolBarContListener
```

The instance of a

ContainerListener

.

- toolBarFocusListener

```java
protected
FocusListener
toolBarFocusListener
```

The instance of a

FocusListener

.

- constraintBeforeFloating

```java
protected
String
constraintBeforeFloating
```

The layout before floating.

- upKey

```java
@Deprecated

protected
KeyStroke
upKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- downKey

```java
@Deprecated

protected
KeyStroke
downKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- leftKey

```java
@Deprecated

protected
KeyStroke
leftKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- rightKey

```java
@Deprecated

protected
KeyStroke
rightKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### Field Detail

toolBar

```java
protected
JToolBar
toolBar
```

The instance of

JToolBar

.

---

#### toolBar

protected

JToolBar

toolBar

The instance of

JToolBar

.

dragWindow

```java
protected
BasicToolBarUI.DragWindow
dragWindow
```

The instance of

DragWindow

.

---

#### dragWindow

protected

BasicToolBarUI.DragWindow

dragWindow

The instance of

DragWindow

.

focusedCompIndex

```java
protected int focusedCompIndex
```

The index of the focused component.

---

#### focusedCompIndex

protected int focusedCompIndex

The index of the focused component.

dockingColor

```java
protected
Color
dockingColor
```

The background color of the docking border.

---

#### dockingColor

protected

Color

dockingColor

The background color of the docking border.

floatingColor

```java
protected
Color
floatingColor
```

The background color of the not docking border.

---

#### floatingColor

protected

Color

floatingColor

The background color of the not docking border.

dockingBorderColor

```java
protected
Color
dockingBorderColor
```

The color of the docking border.

---

#### dockingBorderColor

protected

Color

dockingBorderColor

The color of the docking border.

floatingBorderColor

```java
protected
Color
floatingBorderColor
```

The color of the not docking border.

---

#### floatingBorderColor

protected

Color

floatingBorderColor

The color of the not docking border.

dockingListener

```java
protected
MouseInputListener
dockingListener
```

The instance of a

MouseInputListener

.

---

#### dockingListener

protected

MouseInputListener

dockingListener

The instance of a

MouseInputListener

.

propertyListener

```java
protected
PropertyChangeListener
propertyListener
```

The instance of a

PropertyChangeListener

.

---

#### propertyListener

protected

PropertyChangeListener

propertyListener

The instance of a

PropertyChangeListener

.

toolBarContListener

```java
protected
ContainerListener
toolBarContListener
```

The instance of a

ContainerListener

.

---

#### toolBarContListener

protected

ContainerListener

toolBarContListener

The instance of a

ContainerListener

.

toolBarFocusListener

```java
protected
FocusListener
toolBarFocusListener
```

The instance of a

FocusListener

.

---

#### toolBarFocusListener

protected

FocusListener

toolBarFocusListener

The instance of a

FocusListener

.

constraintBeforeFloating

```java
protected
String
constraintBeforeFloating
```

The layout before floating.

---

#### constraintBeforeFloating

protected

String

constraintBeforeFloating

The layout before floating.

upKey

```java
@Deprecated

protected
KeyStroke
upKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### upKey

@Deprecated

protected

KeyStroke

upKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

downKey

```java
@Deprecated

protected
KeyStroke
downKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### downKey

@Deprecated

protected

KeyStroke

downKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

leftKey

```java
@Deprecated

protected
KeyStroke
leftKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### leftKey

@Deprecated

protected

KeyStroke

leftKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

rightKey

```java
@Deprecated

protected
KeyStroke
rightKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### rightKey

@Deprecated

protected

KeyStroke

rightKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

Constructor Detail

- BasicToolBarUI

```java
public BasicToolBarUI()
```

---

#### Constructor Detail

BasicToolBarUI

```java
public BasicToolBarUI()
```

---

#### BasicToolBarUI

public BasicToolBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new instance of

BasicToolBarUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicToolBarUI

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- installComponents

```java
protected void installComponents()
```

Registers components.

- uninstallComponents

```java
protected void uninstallComponents()
```

Unregisters components.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- navigateFocusedComp

```java
protected void navigateFocusedComp​(int direction)
```

Navigates the focused component.

**Parameters:** direction

- a direction

- createRolloverBorder

```java
protected
Border
createRolloverBorder()
```

Creates a rollover border for toolbar components. The
rollover border will be installed if rollover borders are
enabled.

Override this method to provide an alternate rollover border.

**Returns:** a rollover border for toolbar components
**Since:** 1.4

- createNonRolloverBorder

```java
protected
Border
createNonRolloverBorder()
```

Creates the non rollover border for toolbar components. This
border will be installed as the border for components added
to the toolbar if rollover borders are not enabled.

Override this method to provide an alternate rollover border.

**Returns:** the non rollover border for toolbar components
**Since:** 1.4

- createFloatingFrame

```java
protected
JFrame
createFloatingFrame​(
JToolBar
toolbar)
```

No longer used, use BasicToolBarUI.createFloatingWindow(JToolBar)

**Parameters:** toolbar

- an instance of

JToolBar
**Returns:** an instance of

JFrame
**See Also:** createFloatingWindow(javax.swing.JToolBar)

- createFloatingWindow

```java
protected
RootPaneContainer
createFloatingWindow​(
JToolBar
toolbar)
```

Creates a window which contains the toolbar after it has been
dragged out from its container

**Parameters:** toolbar

- an instance of

JToolBar
**Returns:** a

RootPaneContainer

object, containing the toolbar
**Since:** 1.4

- createDragWindow

```java
protected
BasicToolBarUI.DragWindow
createDragWindow​(
JToolBar
toolbar)
```

Returns an instance of

DragWindow

.

**Parameters:** toolbar

- an instance of

JToolBar
**Returns:** an instance of

DragWindow

- isRolloverBorders

```java
public boolean isRolloverBorders()
```

Returns a flag to determine whether rollover button borders
are enabled.

**Returns:** true if rollover borders are enabled; false otherwise
**Since:** 1.4
**See Also:** setRolloverBorders(boolean)

- setRolloverBorders

```java
public void setRolloverBorders​(boolean rollover)
```

Sets the flag for enabling rollover borders on the toolbar and it will
also install the appropriate border depending on the state of the flag.

**Parameters:** rollover

- if true, rollover borders are installed.
Otherwise non-rollover borders are installed
**Since:** 1.4
**See Also:** isRolloverBorders()

- installRolloverBorders

```java
protected void installRolloverBorders​(
JComponent
c)
```

Installs rollover borders on all the child components of the JComponent.

This is a convenience method to call

setBorderToRollover

for each child component.

**Parameters:** c

- container which holds the child components (usually a JToolBar)
**Since:** 1.4
**See Also:** setBorderToRollover(java.awt.Component)

- installNonRolloverBorders

```java
protected void installNonRolloverBorders​(
JComponent
c)
```

Installs non-rollover borders on all the child components of the JComponent.
A non-rollover border is the border that is installed on the child component
while it is in the toolbar.

This is a convenience method to call

setBorderToNonRollover

for each child component.

**Parameters:** c

- container which holds the child components (usually a JToolBar)
**Since:** 1.4
**See Also:** setBorderToNonRollover(java.awt.Component)

- installNormalBorders

```java
protected void installNormalBorders​(
JComponent
c)
```

Installs normal borders on all the child components of the JComponent.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

This is a convenience method to call

setBorderNormal

for each child component.

**Parameters:** c

- container which holds the child components (usually a JToolBar)
**Since:** 1.4
**See Also:** setBorderToNonRollover(java.awt.Component)

- setBorderToRollover

```java
protected void setBorderToRollover​(
Component
c)
```

Sets the border of the component to have a rollover border which
was created by the

createRolloverBorder()

method.

**Parameters:** c

- component which will have a rollover border installed
**Since:** 1.4
**See Also:** createRolloverBorder()

- getRolloverBorder

```java
protected
Border
getRolloverBorder​(
AbstractButton
b)
```

Returns a rollover border for the button.

**Parameters:** b

- the button to calculate the rollover border for
**Returns:** the rollover border
**Since:** 1.6
**See Also:** setBorderToRollover(java.awt.Component)

- setBorderToNonRollover

```java
protected void setBorderToNonRollover​(
Component
c)
```

Sets the border of the component to have a non-rollover border which
was created by the

createNonRolloverBorder()

method.

**Parameters:** c

- component which will have a non-rollover border installed
**Since:** 1.4
**See Also:** createNonRolloverBorder()

- getNonRolloverBorder

```java
protected
Border
getNonRolloverBorder​(
AbstractButton
b)
```

Returns a non-rollover border for the button.

**Parameters:** b

- the button to calculate the non-rollover border for
**Returns:** the non-rollover border
**Since:** 1.6
**See Also:** setBorderToNonRollover(java.awt.Component)

- setBorderToNormal

```java
protected void setBorderToNormal​(
Component
c)
```

Sets the border of the component to have a normal border.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

**Parameters:** c

- component which will have a normal border re-installed
**Since:** 1.4
**See Also:** createNonRolloverBorder()

- setFloatingLocation

```java
public void setFloatingLocation​(int x,
int y)
```

Sets the floating location.

**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate

- isFloating

```java
public boolean isFloating()
```

Returns

true

if the

JToolBar

is floating

**Returns:** true

if the

JToolBar

is floating

- setFloating

```java
public void setFloating​(boolean b,

Point
p)
```

Sets the floating property.

**Parameters:** b

-

true

if the

JToolBar

is floating
**Parameters:** p

- the position

- setOrientation

```java
public void setOrientation​(int orientation)
```

Sets the tool bar's orientation.

**Parameters:** orientation

- the new orientation

- getDockingColor

```java
public
Color
getDockingColor()
```

Gets the color displayed when over a docking area

**Returns:** the color displayed when over a docking area

- setDockingColor

```java
public void setDockingColor​(
Color
c)
```

Sets the color displayed when over a docking area

**Parameters:** c

- the new color

- getFloatingColor

```java
public
Color
getFloatingColor()
```

Gets the color displayed when over a floating area

**Returns:** the color displayed when over a floating area

- setFloatingColor

```java
public void setFloatingColor​(
Color
c)
```

Sets the color displayed when over a floating area

**Parameters:** c

- the new color

- canDock

```java
public boolean canDock​(
Component
c,

Point
p)
```

Returns

true

if the

JToolBar

can dock at the given position.

**Parameters:** c

- a component
**Parameters:** p

- a position
**Returns:** true

if the

JToolBar

can dock at the given position

- dragTo

```java
protected void dragTo​(
Point
position,

Point
origin)
```

The method is used to drag

DragWindow

during the

JToolBar

is being dragged.

**Parameters:** position

- the relative to the

JTollBar

position
**Parameters:** origin

- the screen position of

JToolBar

before dragging

- floatAt

```java
protected void floatAt​(
Point
position,

Point
origin)
```

The method is called at end of dragging to place the frame in either
its original place or in its floating frame.

**Parameters:** position

- the relative to the

JTollBar

position
**Parameters:** origin

- the screen position of

JToolBar

before dragging

- createToolBarContListener

```java
protected
ContainerListener
createToolBarContListener()
```

Returns an instance of

ContainerListener

.

**Returns:** an instance of

ContainerListener

- createToolBarFocusListener

```java
protected
FocusListener
createToolBarFocusListener()
```

Returns an instance of

FocusListener

.

**Returns:** an instance of

FocusListener

- createPropertyListener

```java
protected
PropertyChangeListener
createPropertyListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

- createDockingListener

```java
protected
MouseInputListener
createDockingListener()
```

Returns an instance of

MouseInputListener

.

**Returns:** an instance of

MouseInputListener

- createFrameListener

```java
protected
WindowListener
createFrameListener()
```

Constructs a new instance of

WindowListener

.

**Returns:** a new instance of

WindowListener

- paintDragWindow

```java
protected void paintDragWindow​(
Graphics
g)
```

Paints the contents of the window used for dragging.

**Parameters:** g

- Graphics to paint to.
**Throws:** NullPointerException

- is

g

is null
**Since:** 1.5

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new instance of

BasicToolBarUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicToolBarUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs a new instance of

BasicToolBarUI

.

installDefaults

```java
protected void installDefaults()
```

Installs default properties.

---

#### installDefaults

protected void installDefaults()

Installs default properties.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

installComponents

```java
protected void installComponents()
```

Registers components.

---

#### installComponents

protected void installComponents()

Registers components.

uninstallComponents

```java
protected void uninstallComponents()
```

Unregisters components.

---

#### uninstallComponents

protected void uninstallComponents()

Unregisters components.

installListeners

```java
protected void installListeners()
```

Registers listeners.

---

#### installListeners

protected void installListeners()

Registers listeners.

uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Unregisters listeners.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

---

#### installKeyboardActions

protected void installKeyboardActions()

Registers keyboard actions.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters keyboard actions.

navigateFocusedComp

```java
protected void navigateFocusedComp​(int direction)
```

Navigates the focused component.

**Parameters:** direction

- a direction

---

#### navigateFocusedComp

protected void navigateFocusedComp​(int direction)

Navigates the focused component.

createRolloverBorder

```java
protected
Border
createRolloverBorder()
```

Creates a rollover border for toolbar components. The
rollover border will be installed if rollover borders are
enabled.

Override this method to provide an alternate rollover border.

**Returns:** a rollover border for toolbar components
**Since:** 1.4

---

#### createRolloverBorder

protected

Border

createRolloverBorder()

Creates a rollover border for toolbar components. The
rollover border will be installed if rollover borders are
enabled.

Override this method to provide an alternate rollover border.

Override this method to provide an alternate rollover border.

createNonRolloverBorder

```java
protected
Border
createNonRolloverBorder()
```

Creates the non rollover border for toolbar components. This
border will be installed as the border for components added
to the toolbar if rollover borders are not enabled.

Override this method to provide an alternate rollover border.

**Returns:** the non rollover border for toolbar components
**Since:** 1.4

---

#### createNonRolloverBorder

protected

Border

createNonRolloverBorder()

Creates the non rollover border for toolbar components. This
border will be installed as the border for components added
to the toolbar if rollover borders are not enabled.

Override this method to provide an alternate rollover border.

Override this method to provide an alternate rollover border.

createFloatingFrame

```java
protected
JFrame
createFloatingFrame​(
JToolBar
toolbar)
```

No longer used, use BasicToolBarUI.createFloatingWindow(JToolBar)

**Parameters:** toolbar

- an instance of

JToolBar
**Returns:** an instance of

JFrame
**See Also:** createFloatingWindow(javax.swing.JToolBar)

---

#### createFloatingFrame

protected

JFrame

createFloatingFrame​(

JToolBar

toolbar)

No longer used, use BasicToolBarUI.createFloatingWindow(JToolBar)

createFloatingWindow

```java
protected
RootPaneContainer
createFloatingWindow​(
JToolBar
toolbar)
```

Creates a window which contains the toolbar after it has been
dragged out from its container

**Parameters:** toolbar

- an instance of

JToolBar
**Returns:** a

RootPaneContainer

object, containing the toolbar
**Since:** 1.4

---

#### createFloatingWindow

protected

RootPaneContainer

createFloatingWindow​(

JToolBar

toolbar)

Creates a window which contains the toolbar after it has been
dragged out from its container

createDragWindow

```java
protected
BasicToolBarUI.DragWindow
createDragWindow​(
JToolBar
toolbar)
```

Returns an instance of

DragWindow

.

**Parameters:** toolbar

- an instance of

JToolBar
**Returns:** an instance of

DragWindow

---

#### createDragWindow

protected

BasicToolBarUI.DragWindow

createDragWindow​(

JToolBar

toolbar)

Returns an instance of

DragWindow

.

isRolloverBorders

```java
public boolean isRolloverBorders()
```

Returns a flag to determine whether rollover button borders
are enabled.

**Returns:** true if rollover borders are enabled; false otherwise
**Since:** 1.4
**See Also:** setRolloverBorders(boolean)

---

#### isRolloverBorders

public boolean isRolloverBorders()

Returns a flag to determine whether rollover button borders
are enabled.

setRolloverBorders

```java
public void setRolloverBorders​(boolean rollover)
```

Sets the flag for enabling rollover borders on the toolbar and it will
also install the appropriate border depending on the state of the flag.

**Parameters:** rollover

- if true, rollover borders are installed.
Otherwise non-rollover borders are installed
**Since:** 1.4
**See Also:** isRolloverBorders()

---

#### setRolloverBorders

public void setRolloverBorders​(boolean rollover)

Sets the flag for enabling rollover borders on the toolbar and it will
also install the appropriate border depending on the state of the flag.

installRolloverBorders

```java
protected void installRolloverBorders​(
JComponent
c)
```

Installs rollover borders on all the child components of the JComponent.

This is a convenience method to call

setBorderToRollover

for each child component.

**Parameters:** c

- container which holds the child components (usually a JToolBar)
**Since:** 1.4
**See Also:** setBorderToRollover(java.awt.Component)

---

#### installRolloverBorders

protected void installRolloverBorders​(

JComponent

c)

Installs rollover borders on all the child components of the JComponent.

This is a convenience method to call

setBorderToRollover

for each child component.

This is a convenience method to call

setBorderToRollover

for each child component.

installNonRolloverBorders

```java
protected void installNonRolloverBorders​(
JComponent
c)
```

Installs non-rollover borders on all the child components of the JComponent.
A non-rollover border is the border that is installed on the child component
while it is in the toolbar.

This is a convenience method to call

setBorderToNonRollover

for each child component.

**Parameters:** c

- container which holds the child components (usually a JToolBar)
**Since:** 1.4
**See Also:** setBorderToNonRollover(java.awt.Component)

---

#### installNonRolloverBorders

protected void installNonRolloverBorders​(

JComponent

c)

Installs non-rollover borders on all the child components of the JComponent.
A non-rollover border is the border that is installed on the child component
while it is in the toolbar.

This is a convenience method to call

setBorderToNonRollover

for each child component.

This is a convenience method to call

setBorderToNonRollover

for each child component.

installNormalBorders

```java
protected void installNormalBorders​(
JComponent
c)
```

Installs normal borders on all the child components of the JComponent.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

This is a convenience method to call

setBorderNormal

for each child component.

**Parameters:** c

- container which holds the child components (usually a JToolBar)
**Since:** 1.4
**See Also:** setBorderToNonRollover(java.awt.Component)

---

#### installNormalBorders

protected void installNormalBorders​(

JComponent

c)

Installs normal borders on all the child components of the JComponent.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

This is a convenience method to call

setBorderNormal

for each child component.

This is a convenience method to call

setBorderNormal

for each child component.

setBorderToRollover

```java
protected void setBorderToRollover​(
Component
c)
```

Sets the border of the component to have a rollover border which
was created by the

createRolloverBorder()

method.

**Parameters:** c

- component which will have a rollover border installed
**Since:** 1.4
**See Also:** createRolloverBorder()

---

#### setBorderToRollover

protected void setBorderToRollover​(

Component

c)

Sets the border of the component to have a rollover border which
was created by the

createRolloverBorder()

method.

getRolloverBorder

```java
protected
Border
getRolloverBorder​(
AbstractButton
b)
```

Returns a rollover border for the button.

**Parameters:** b

- the button to calculate the rollover border for
**Returns:** the rollover border
**Since:** 1.6
**See Also:** setBorderToRollover(java.awt.Component)

---

#### getRolloverBorder

protected

Border

getRolloverBorder​(

AbstractButton

b)

Returns a rollover border for the button.

setBorderToNonRollover

```java
protected void setBorderToNonRollover​(
Component
c)
```

Sets the border of the component to have a non-rollover border which
was created by the

createNonRolloverBorder()

method.

**Parameters:** c

- component which will have a non-rollover border installed
**Since:** 1.4
**See Also:** createNonRolloverBorder()

---

#### setBorderToNonRollover

protected void setBorderToNonRollover​(

Component

c)

Sets the border of the component to have a non-rollover border which
was created by the

createNonRolloverBorder()

method.

getNonRolloverBorder

```java
protected
Border
getNonRolloverBorder​(
AbstractButton
b)
```

Returns a non-rollover border for the button.

**Parameters:** b

- the button to calculate the non-rollover border for
**Returns:** the non-rollover border
**Since:** 1.6
**See Also:** setBorderToNonRollover(java.awt.Component)

---

#### getNonRolloverBorder

protected

Border

getNonRolloverBorder​(

AbstractButton

b)

Returns a non-rollover border for the button.

setBorderToNormal

```java
protected void setBorderToNormal​(
Component
c)
```

Sets the border of the component to have a normal border.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

**Parameters:** c

- component which will have a normal border re-installed
**Since:** 1.4
**See Also:** createNonRolloverBorder()

---

#### setBorderToNormal

protected void setBorderToNormal​(

Component

c)

Sets the border of the component to have a normal border.
A normal border is the original border that was installed on the child
component before it was added to the toolbar.

setFloatingLocation

```java
public void setFloatingLocation​(int x,
int y)
```

Sets the floating location.

**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate

---

#### setFloatingLocation

public void setFloatingLocation​(int x,
int y)

Sets the floating location.

isFloating

```java
public boolean isFloating()
```

Returns

true

if the

JToolBar

is floating

**Returns:** true

if the

JToolBar

is floating

---

#### isFloating

public boolean isFloating()

Returns

true

if the

JToolBar

is floating

setFloating

```java
public void setFloating​(boolean b,

Point
p)
```

Sets the floating property.

**Parameters:** b

-

true

if the

JToolBar

is floating
**Parameters:** p

- the position

---

#### setFloating

public void setFloating​(boolean b,

Point

p)

Sets the floating property.

setOrientation

```java
public void setOrientation​(int orientation)
```

Sets the tool bar's orientation.

**Parameters:** orientation

- the new orientation

---

#### setOrientation

public void setOrientation​(int orientation)

Sets the tool bar's orientation.

getDockingColor

```java
public
Color
getDockingColor()
```

Gets the color displayed when over a docking area

**Returns:** the color displayed when over a docking area

---

#### getDockingColor

public

Color

getDockingColor()

Gets the color displayed when over a docking area

setDockingColor

```java
public void setDockingColor​(
Color
c)
```

Sets the color displayed when over a docking area

**Parameters:** c

- the new color

---

#### setDockingColor

public void setDockingColor​(

Color

c)

Sets the color displayed when over a docking area

getFloatingColor

```java
public
Color
getFloatingColor()
```

Gets the color displayed when over a floating area

**Returns:** the color displayed when over a floating area

---

#### getFloatingColor

public

Color

getFloatingColor()

Gets the color displayed when over a floating area

setFloatingColor

```java
public void setFloatingColor​(
Color
c)
```

Sets the color displayed when over a floating area

**Parameters:** c

- the new color

---

#### setFloatingColor

public void setFloatingColor​(

Color

c)

Sets the color displayed when over a floating area

canDock

```java
public boolean canDock​(
Component
c,

Point
p)
```

Returns

true

if the

JToolBar

can dock at the given position.

**Parameters:** c

- a component
**Parameters:** p

- a position
**Returns:** true

if the

JToolBar

can dock at the given position

---

#### canDock

public boolean canDock​(

Component

c,

Point

p)

Returns

true

if the

JToolBar

can dock at the given position.

dragTo

```java
protected void dragTo​(
Point
position,

Point
origin)
```

The method is used to drag

DragWindow

during the

JToolBar

is being dragged.

**Parameters:** position

- the relative to the

JTollBar

position
**Parameters:** origin

- the screen position of

JToolBar

before dragging

---

#### dragTo

protected void dragTo​(

Point

position,

Point

origin)

The method is used to drag

DragWindow

during the

JToolBar

is being dragged.

floatAt

```java
protected void floatAt​(
Point
position,

Point
origin)
```

The method is called at end of dragging to place the frame in either
its original place or in its floating frame.

**Parameters:** position

- the relative to the

JTollBar

position
**Parameters:** origin

- the screen position of

JToolBar

before dragging

---

#### floatAt

protected void floatAt​(

Point

position,

Point

origin)

The method is called at end of dragging to place the frame in either
its original place or in its floating frame.

createToolBarContListener

```java
protected
ContainerListener
createToolBarContListener()
```

Returns an instance of

ContainerListener

.

**Returns:** an instance of

ContainerListener

---

#### createToolBarContListener

protected

ContainerListener

createToolBarContListener()

Returns an instance of

ContainerListener

.

createToolBarFocusListener

```java
protected
FocusListener
createToolBarFocusListener()
```

Returns an instance of

FocusListener

.

**Returns:** an instance of

FocusListener

---

#### createToolBarFocusListener

protected

FocusListener

createToolBarFocusListener()

Returns an instance of

FocusListener

.

createPropertyListener

```java
protected
PropertyChangeListener
createPropertyListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

---

#### createPropertyListener

protected

PropertyChangeListener

createPropertyListener()

Returns an instance of

PropertyChangeListener

.

createDockingListener

```java
protected
MouseInputListener
createDockingListener()
```

Returns an instance of

MouseInputListener

.

**Returns:** an instance of

MouseInputListener

---

#### createDockingListener

protected

MouseInputListener

createDockingListener()

Returns an instance of

MouseInputListener

.

createFrameListener

```java
protected
WindowListener
createFrameListener()
```

Constructs a new instance of

WindowListener

.

**Returns:** a new instance of

WindowListener

---

#### createFrameListener

protected

WindowListener

createFrameListener()

Constructs a new instance of

WindowListener

.

paintDragWindow

```java
protected void paintDragWindow​(
Graphics
g)
```

Paints the contents of the window used for dragging.

**Parameters:** g

- Graphics to paint to.
**Throws:** NullPointerException

- is

g

is null
**Since:** 1.5

---

#### paintDragWindow

protected void paintDragWindow​(

Graphics

g)

Paints the contents of the window used for dragging.

---

