# Class SynthToolBarUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthToolBarUI.html`

### Class Description

```java
public class
SynthToolBarUI

extends
BasicToolBarUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JToolBar

.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

,

SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthToolBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates a new UI object for the given component.

**Parameters:**
- c

- component to create UI object for

**Returns:**
- the UI object

---

#### protected
LayoutManager
createLayout()

Creates a

LayoutManager

to use with the toolbar.

**Returns:**
- a

LayoutManager

instance

---

#### public void update​(
Graphics
g,

JComponent
c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:**
- update

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### public void paint​(
Graphics
g,

JComponent
c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:**
- paint

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### protected void setBorderToNonRollover​(
Component
c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:**
- setBorderToNonRollover

in class

BasicToolBarUI

**Parameters:**
- c

- component which will have a non-rollover border installed

**See Also:**
- BasicToolBarUI.createNonRolloverBorder()

---

#### protected void setBorderToRollover​(
Component
c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:**
- setBorderToRollover

in class

BasicToolBarUI

**Parameters:**
- c

- component which will have a rollover border installed

**See Also:**
- BasicToolBarUI.createRolloverBorder()

---

#### protected void setBorderToNormal​(
Component
c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:**
- setBorderToNormal

in class

BasicToolBarUI

**Parameters:**
- c

- component which will have a normal border re-installed

**See Also:**
- BasicToolBarUI.createNonRolloverBorder()

---

#### protected void paint​(
SynthContext
context,

Graphics
g)

Paints the toolbar.

**Parameters:**
- context

- context for the component being painted
- g

- the

Graphics

object used for painting

**See Also:**
- update(Graphics,JComponent)

---

#### protected void paintContent​(
SynthContext
context,

Graphics
g,

Rectangle
bounds)

Paints the toolbar content.

**Parameters:**
- context

- context for the component being painted
- g

-

Graphics

object used for painting
- bounds

- bounding box for the toolbar

---

### Additional Sections

#### Class SynthToolBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ToolBarUI
- - javax.swing.plaf.basic.BasicToolBarUI
- - javax.swing.plaf.synth.SynthToolBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ToolBarUI
- - javax.swing.plaf.basic.BasicToolBarUI
- - javax.swing.plaf.synth.SynthToolBarUI

javax.swing.plaf.ToolBarUI

- javax.swing.plaf.basic.BasicToolBarUI
- - javax.swing.plaf.synth.SynthToolBarUI

javax.swing.plaf.basic.BasicToolBarUI

- javax.swing.plaf.synth.SynthToolBarUI

javax.swing.plaf.synth.SynthToolBarUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

,

SwingConstants

```java
public class
SynthToolBarUI

extends
BasicToolBarUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JToolBar

.

**Since:** 1.7

public class

SynthToolBarUI

extends

BasicToolBarUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JToolBar

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

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

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynthToolBarUI

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

LayoutManager

createLayout

()

Creates a

LayoutManager

to use with the toolbar.

static

ComponentUI

createUI

​(

JComponent

c)

Creates a new UI object for the given component.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the toolbar.

protected void

paintContent

​(

SynthContext

context,

Graphics

g,

Rectangle

bounds)

Paints the toolbar content.

protected void

setBorderToNonRollover

​(

Component

c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

protected void

setBorderToNormal

​(

Component

c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

protected void

setBorderToRollover

​(

Component

c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

Nested Class Summary

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

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

---

#### Field Summary

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

Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

---

#### Fields declared in interface javax.swing.plaf.synth. SynthConstants

Constructor Summary

Constructors

Constructor

Description

SynthToolBarUI

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

LayoutManager

createLayout

()

Creates a

LayoutManager

to use with the toolbar.

static

ComponentUI

createUI

​(

JComponent

c)

Creates a new UI object for the given component.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the toolbar.

protected void

paintContent

​(

SynthContext

context,

Graphics

g,

Rectangle

bounds)

Paints the toolbar content.

protected void

setBorderToNonRollover

​(

Component

c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

protected void

setBorderToNormal

​(

Component

c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

protected void

setBorderToRollover

​(

Component

c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Method Summary

Creates a

LayoutManager

to use with the toolbar.

Creates a new UI object for the given component.

Paints the specified component according to the Look and Feel.

Paints the toolbar.

Paints the toolbar content.

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

Notifies this UI delegate to repaint the specified component.

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

Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Methods declared in interface java.beans. PropertyChangeListener

Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Methods declared in interface javax.swing.plaf.synth. SynthUI

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthToolBarUI

```java
public SynthToolBarUI()
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

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

- createLayout

```java
protected
LayoutManager
createLayout()
```

Creates a

LayoutManager

to use with the toolbar.

**Returns:** a

LayoutManager

instance

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- setBorderToNonRollover

```java
protected void setBorderToNonRollover​(
Component
c)
```

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:** setBorderToNonRollover

in class

BasicToolBarUI
**Parameters:** c

- component which will have a non-rollover border installed
**See Also:** BasicToolBarUI.createNonRolloverBorder()

- setBorderToRollover

```java
protected void setBorderToRollover​(
Component
c)
```

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:** setBorderToRollover

in class

BasicToolBarUI
**Parameters:** c

- component which will have a rollover border installed
**See Also:** BasicToolBarUI.createRolloverBorder()

- setBorderToNormal

```java
protected void setBorderToNormal​(
Component
c)
```

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:** setBorderToNormal

in class

BasicToolBarUI
**Parameters:** c

- component which will have a normal border re-installed
**See Also:** BasicToolBarUI.createNonRolloverBorder()

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the toolbar.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- paintContent

```java
protected void paintContent​(
SynthContext
context,

Graphics
g,

Rectangle
bounds)
```

Paints the toolbar content.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** bounds

- bounding box for the toolbar

Constructor Detail

- SynthToolBarUI

```java
public SynthToolBarUI()
```

---

#### Constructor Detail

SynthToolBarUI

```java
public SynthToolBarUI()
```

---

#### SynthToolBarUI

public SynthToolBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

- createLayout

```java
protected
LayoutManager
createLayout()
```

Creates a

LayoutManager

to use with the toolbar.

**Returns:** a

LayoutManager

instance

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- setBorderToNonRollover

```java
protected void setBorderToNonRollover​(
Component
c)
```

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:** setBorderToNonRollover

in class

BasicToolBarUI
**Parameters:** c

- component which will have a non-rollover border installed
**See Also:** BasicToolBarUI.createNonRolloverBorder()

- setBorderToRollover

```java
protected void setBorderToRollover​(
Component
c)
```

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:** setBorderToRollover

in class

BasicToolBarUI
**Parameters:** c

- component which will have a rollover border installed
**See Also:** BasicToolBarUI.createRolloverBorder()

- setBorderToNormal

```java
protected void setBorderToNormal​(
Component
c)
```

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:** setBorderToNormal

in class

BasicToolBarUI
**Parameters:** c

- component which will have a normal border re-installed
**See Also:** BasicToolBarUI.createNonRolloverBorder()

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the toolbar.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- paintContent

```java
protected void paintContent​(
SynthContext
context,

Graphics
g,

Rectangle
bounds)
```

Paints the toolbar content.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** bounds

- bounding box for the toolbar

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

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates a new UI object for the given component.

createLayout

```java
protected
LayoutManager
createLayout()
```

Creates a

LayoutManager

to use with the toolbar.

**Returns:** a

LayoutManager

instance

---

#### createLayout

protected

LayoutManager

createLayout()

Creates a

LayoutManager

to use with the toolbar.

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### update

public void update​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

setBorderToNonRollover

```java
protected void setBorderToNonRollover​(
Component
c)
```

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:** setBorderToNonRollover

in class

BasicToolBarUI
**Parameters:** c

- component which will have a non-rollover border installed
**See Also:** BasicToolBarUI.createNonRolloverBorder()

---

#### setBorderToNonRollover

protected void setBorderToNonRollover​(

Component

c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

setBorderToRollover

```java
protected void setBorderToRollover​(
Component
c)
```

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:** setBorderToRollover

in class

BasicToolBarUI
**Parameters:** c

- component which will have a rollover border installed
**See Also:** BasicToolBarUI.createRolloverBorder()

---

#### setBorderToRollover

protected void setBorderToRollover​(

Component

c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

setBorderToNormal

```java
protected void setBorderToNormal​(
Component
c)
```

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

**Overrides:** setBorderToNormal

in class

BasicToolBarUI
**Parameters:** c

- component which will have a normal border re-installed
**See Also:** BasicToolBarUI.createNonRolloverBorder()

---

#### setBorderToNormal

protected void setBorderToNormal​(

Component

c)

This implementation does nothing, because the

rollover

property of the

JToolBar

class is not used
in the Synth Look and Feel.

paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the toolbar.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

---

#### paint

protected void paint​(

SynthContext

context,

Graphics

g)

Paints the toolbar.

paintContent

```java
protected void paintContent​(
SynthContext
context,

Graphics
g,

Rectangle
bounds)
```

Paints the toolbar content.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** bounds

- bounding box for the toolbar

---

#### paintContent

protected void paintContent​(

SynthContext

context,

Graphics

g,

Rectangle

bounds)

Paints the toolbar content.

---

