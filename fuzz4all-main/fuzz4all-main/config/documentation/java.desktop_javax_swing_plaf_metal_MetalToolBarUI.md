# Class MetalToolBarUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalToolBarUI.html`

### Class Description

```java
public class
MetalToolBarUI

extends
BasicToolBarUI
```

A Metal Look and Feel implementation of ToolBarUI. This implementation
is a "combined" view/controller.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

#### protected
ContainerListener
contListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:**
- createContainerListener()

---

#### protected
PropertyChangeListener
rolloverListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:**
- createRolloverListener()

---

### Constructor Details

#### public MetalToolBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs an instance of

MetalToolBarUI

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

MetalToolBarUI

---

#### protected
ContainerListener
createContainerListener()

Creates a container listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

**Returns:**
- an instance of a

ContainerListener

or null

---

#### protected
PropertyChangeListener
createRolloverListener()

Creates a property change listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

**Returns:**
- an instance of a

PropertyChangeListener

or null

---

#### protected void setDragOffset​(
Point
p)

Sets the offset of the mouse cursor inside the DragWindow.

**Parameters:**
- p

- the offset

---

#### public void update​(
Graphics
g,

JComponent
c)

If necessary paints the background of the component, then invokes

paint

.

**Overrides:**
- update

in class

ComponentUI

**Parameters:**
- g

- Graphics to paint to
- c

- JComponent painting on

**Throws:**
- NullPointerException

- if

g

or

c

is
null

**See Also:**
- ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

,

ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

**Since:**
- 1.5

---

### Additional Sections

#### Class MetalToolBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ToolBarUI
- - javax.swing.plaf.basic.BasicToolBarUI
- - javax.swing.plaf.metal.MetalToolBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ToolBarUI
- - javax.swing.plaf.basic.BasicToolBarUI
- - javax.swing.plaf.metal.MetalToolBarUI

javax.swing.plaf.ToolBarUI

- javax.swing.plaf.basic.BasicToolBarUI
- - javax.swing.plaf.metal.MetalToolBarUI

javax.swing.plaf.basic.BasicToolBarUI

- javax.swing.plaf.metal.MetalToolBarUI

javax.swing.plaf.metal.MetalToolBarUI

**All Implemented Interfaces:** SwingConstants

```java
public class
MetalToolBarUI

extends
BasicToolBarUI
```

A Metal Look and Feel implementation of ToolBarUI. This implementation
is a "combined" view/controller.

public class

MetalToolBarUI

extends

BasicToolBarUI

A Metal Look and Feel implementation of ToolBarUI. This implementation
is a "combined" view/controller.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

MetalToolBarUI.MetalContainerListener

No longer used.

protected class

MetalToolBarUI.MetalDockingListener

DockingListener

for

MetalToolBarUI

.

protected class

MetalToolBarUI.MetalRolloverListener

No longer used.

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicToolBarUI

BasicToolBarUI.DockingListener

,

BasicToolBarUI.DragWindow

,

BasicToolBarUI.FrameListener

,

BasicToolBarUI.PropertyListener

,

BasicToolBarUI.ToolBarContListener

,

BasicToolBarUI.ToolBarFocusListener

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ContainerListener

contListener

This protected field is implementation specific.

protected

PropertyChangeListener

rolloverListener

This protected field is implementation specific.

- Fields declared in class javax.swing.plaf.basic.

BasicToolBarUI

constraintBeforeFloating

,

dockingBorderColor

,

dockingColor

,

dockingListener

,

downKey

,

dragWindow

,

floatingBorderColor

,

floatingColor

,

focusedCompIndex

,

leftKey

,

propertyListener

,

rightKey

,

toolBar

,

toolBarContListener

,

toolBarFocusListener

,

upKey

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

MetalToolBarUI

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

protected

ContainerListener

createContainerListener

()

Creates a container listener that will be added to the JToolBar.

protected

PropertyChangeListener

createRolloverListener

()

Creates a property change listener that will be added to the JToolBar.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs an instance of

MetalToolBarUI

.

protected void

setDragOffset

​(

Point

p)

Sets the offset of the mouse cursor inside the DragWindow.

void

update

​(

Graphics

g,

JComponent

c)

If necessary paints the background of the component, then invokes

paint

.

- Methods declared in class javax.swing.plaf.basic.

BasicToolBarUI

canDock

,

createDockingListener

,

createDragWindow

,

createFloatingFrame

,

createFloatingWindow

,

createFrameListener

,

createNonRolloverBorder

,

createPropertyListener

,

createRolloverBorder

,

createToolBarContListener

,

createToolBarFocusListener

,

dragTo

,

floatAt

,

getDockingColor

,

getFloatingColor

,

getNonRolloverBorder

,

getRolloverBorder

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installNonRolloverBorders

,

installNormalBorders

,

installRolloverBorders

,

isFloating

,

isRolloverBorders

,

navigateFocusedComp

,

paintDragWindow

,

setBorderToNonRollover

,

setBorderToNormal

,

setBorderToRollover

,

setDockingColor

,

setFloating

,

setFloatingColor

,

setFloatingLocation

,

setOrientation

,

setRolloverBorders

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

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

protected class

MetalToolBarUI.MetalContainerListener

No longer used.

protected class

MetalToolBarUI.MetalDockingListener

DockingListener

for

MetalToolBarUI

.

protected class

MetalToolBarUI.MetalRolloverListener

No longer used.

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicToolBarUI

BasicToolBarUI.DockingListener

,

BasicToolBarUI.DragWindow

,

BasicToolBarUI.FrameListener

,

BasicToolBarUI.PropertyListener

,

BasicToolBarUI.ToolBarContListener

,

BasicToolBarUI.ToolBarFocusListener

---

#### Nested Class Summary

No longer used.

DockingListener

for

MetalToolBarUI

.

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicToolBarUI

BasicToolBarUI.DockingListener

,

BasicToolBarUI.DragWindow

,

BasicToolBarUI.FrameListener

,

BasicToolBarUI.PropertyListener

,

BasicToolBarUI.ToolBarContListener

,

BasicToolBarUI.ToolBarFocusListener

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicToolBarUI

Field Summary

Fields

Modifier and Type

Field

Description

protected

ContainerListener

contListener

This protected field is implementation specific.

protected

PropertyChangeListener

rolloverListener

This protected field is implementation specific.

- Fields declared in class javax.swing.plaf.basic.

BasicToolBarUI

constraintBeforeFloating

,

dockingBorderColor

,

dockingColor

,

dockingListener

,

downKey

,

dragWindow

,

floatingBorderColor

,

floatingColor

,

focusedCompIndex

,

leftKey

,

propertyListener

,

rightKey

,

toolBar

,

toolBarContListener

,

toolBarFocusListener

,

upKey

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

This protected field is implementation specific.

Fields declared in class javax.swing.plaf.basic.

BasicToolBarUI

constraintBeforeFloating

,

dockingBorderColor

,

dockingColor

,

dockingListener

,

downKey

,

dragWindow

,

floatingBorderColor

,

floatingColor

,

focusedCompIndex

,

leftKey

,

propertyListener

,

rightKey

,

toolBar

,

toolBarContListener

,

toolBarFocusListener

,

upKey

---

#### Fields declared in class javax.swing.plaf.basic. BasicToolBarUI

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

MetalToolBarUI

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

protected

ContainerListener

createContainerListener

()

Creates a container listener that will be added to the JToolBar.

protected

PropertyChangeListener

createRolloverListener

()

Creates a property change listener that will be added to the JToolBar.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs an instance of

MetalToolBarUI

.

protected void

setDragOffset

​(

Point

p)

Sets the offset of the mouse cursor inside the DragWindow.

void

update

​(

Graphics

g,

JComponent

c)

If necessary paints the background of the component, then invokes

paint

.

- Methods declared in class javax.swing.plaf.basic.

BasicToolBarUI

canDock

,

createDockingListener

,

createDragWindow

,

createFloatingFrame

,

createFloatingWindow

,

createFrameListener

,

createNonRolloverBorder

,

createPropertyListener

,

createRolloverBorder

,

createToolBarContListener

,

createToolBarFocusListener

,

dragTo

,

floatAt

,

getDockingColor

,

getFloatingColor

,

getNonRolloverBorder

,

getRolloverBorder

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installNonRolloverBorders

,

installNormalBorders

,

installRolloverBorders

,

isFloating

,

isRolloverBorders

,

navigateFocusedComp

,

paintDragWindow

,

setBorderToNonRollover

,

setBorderToNormal

,

setBorderToRollover

,

setDockingColor

,

setFloating

,

setFloatingColor

,

setFloatingLocation

,

setOrientation

,

setRolloverBorders

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

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

Creates a container listener that will be added to the JToolBar.

Creates a property change listener that will be added to the JToolBar.

Constructs an instance of

MetalToolBarUI

.

Sets the offset of the mouse cursor inside the DragWindow.

If necessary paints the background of the component, then invokes

paint

.

Methods declared in class javax.swing.plaf.basic.

BasicToolBarUI

canDock

,

createDockingListener

,

createDragWindow

,

createFloatingFrame

,

createFloatingWindow

,

createFrameListener

,

createNonRolloverBorder

,

createPropertyListener

,

createRolloverBorder

,

createToolBarContListener

,

createToolBarFocusListener

,

dragTo

,

floatAt

,

getDockingColor

,

getFloatingColor

,

getNonRolloverBorder

,

getRolloverBorder

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installNonRolloverBorders

,

installNormalBorders

,

installRolloverBorders

,

isFloating

,

isRolloverBorders

,

navigateFocusedComp

,

paintDragWindow

,

setBorderToNonRollover

,

setBorderToNormal

,

setBorderToRollover

,

setDockingColor

,

setFloating

,

setFloatingColor

,

setFloatingLocation

,

setOrientation

,

setRolloverBorders

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

---

#### Methods declared in class javax.swing.plaf.basic. BasicToolBarUI

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

- contListener

```java
protected
ContainerListener
contListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createContainerListener()

- rolloverListener

```java
protected
PropertyChangeListener
rolloverListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createRolloverListener()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalToolBarUI

```java
public MetalToolBarUI()
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

Constructs an instance of

MetalToolBarUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalToolBarUI

- createContainerListener

```java
protected
ContainerListener
createContainerListener()
```

Creates a container listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

**Returns:** an instance of a

ContainerListener

or null

- createRolloverListener

```java
protected
PropertyChangeListener
createRolloverListener()
```

Creates a property change listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

**Returns:** an instance of a

PropertyChangeListener

or null

- setDragOffset

```java
protected void setDragOffset​(
Point
p)
```

Sets the offset of the mouse cursor inside the DragWindow.

**Parameters:** p

- the offset

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

If necessary paints the background of the component, then invokes

paint

.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- Graphics to paint to
**Parameters:** c

- JComponent painting on
**Throws:** NullPointerException

- if

g

or

c

is
null
**Since:** 1.5
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

,

ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

Field Detail

- contListener

```java
protected
ContainerListener
contListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createContainerListener()

- rolloverListener

```java
protected
PropertyChangeListener
rolloverListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createRolloverListener()

---

#### Field Detail

contListener

```java
protected
ContainerListener
contListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createContainerListener()

---

#### contListener

protected

ContainerListener

contListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

rolloverListener

```java
protected
PropertyChangeListener
rolloverListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createRolloverListener()

---

#### rolloverListener

protected

PropertyChangeListener

rolloverListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

Constructor Detail

- MetalToolBarUI

```java
public MetalToolBarUI()
```

---

#### Constructor Detail

MetalToolBarUI

```java
public MetalToolBarUI()
```

---

#### MetalToolBarUI

public MetalToolBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs an instance of

MetalToolBarUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalToolBarUI

- createContainerListener

```java
protected
ContainerListener
createContainerListener()
```

Creates a container listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

**Returns:** an instance of a

ContainerListener

or null

- createRolloverListener

```java
protected
PropertyChangeListener
createRolloverListener()
```

Creates a property change listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

**Returns:** an instance of a

PropertyChangeListener

or null

- setDragOffset

```java
protected void setDragOffset​(
Point
p)
```

Sets the offset of the mouse cursor inside the DragWindow.

**Parameters:** p

- the offset

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

If necessary paints the background of the component, then invokes

paint

.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- Graphics to paint to
**Parameters:** c

- JComponent painting on
**Throws:** NullPointerException

- if

g

or

c

is
null
**Since:** 1.5
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

,

ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

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

Constructs an instance of

MetalToolBarUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalToolBarUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs an instance of

MetalToolBarUI

.

createContainerListener

```java
protected
ContainerListener
createContainerListener()
```

Creates a container listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

**Returns:** an instance of a

ContainerListener

or null

---

#### createContainerListener

protected

ContainerListener

createContainerListener()

Creates a container listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

createRolloverListener

```java
protected
PropertyChangeListener
createRolloverListener()
```

Creates a property change listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

**Returns:** an instance of a

PropertyChangeListener

or null

---

#### createRolloverListener

protected

PropertyChangeListener

createRolloverListener()

Creates a property change listener that will be added to the JToolBar.
If this method returns null then it will not be added to the
toolbar.

setDragOffset

```java
protected void setDragOffset​(
Point
p)
```

Sets the offset of the mouse cursor inside the DragWindow.

**Parameters:** p

- the offset

---

#### setDragOffset

protected void setDragOffset​(

Point

p)

Sets the offset of the mouse cursor inside the DragWindow.

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

If necessary paints the background of the component, then invokes

paint

.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- Graphics to paint to
**Parameters:** c

- JComponent painting on
**Throws:** NullPointerException

- if

g

or

c

is
null
**Since:** 1.5
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

,

ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

---

#### update

public void update​(

Graphics

g,

JComponent

c)

If necessary paints the background of the component, then invokes

paint

.

---

