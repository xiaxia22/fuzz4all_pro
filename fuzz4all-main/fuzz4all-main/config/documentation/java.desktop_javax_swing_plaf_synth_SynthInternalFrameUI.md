# Class SynthInternalFrameUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthInternalFrameUI.html`

### Class Description

```java
public class
SynthInternalFrameUI

extends
BasicInternalFrameUI

implements
SynthUI
,
PropertyChangeListener
```

Provides the Synth L&F UI delegate for

JInternalFrame

.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SynthInternalFrameUI​(
JInternalFrame
b)

Constructs a

SynthInternalFrameUI

.

**Parameters:**
- b

- an internal frame

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
b)

Creates a new UI object for the given component.

**Parameters:**
- b

- component to create UI object for

**Returns:**
- the UI object

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

#### protected void paint​(
SynthContext
context,

Graphics
g)

Paints the specified component. This implementation does nothing.

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

### Additional Sections

#### Class SynthInternalFrameUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.InternalFrameUI
- - javax.swing.plaf.basic.BasicInternalFrameUI
- - javax.swing.plaf.synth.SynthInternalFrameUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.InternalFrameUI
- - javax.swing.plaf.basic.BasicInternalFrameUI
- - javax.swing.plaf.synth.SynthInternalFrameUI

javax.swing.plaf.InternalFrameUI

- javax.swing.plaf.basic.BasicInternalFrameUI
- - javax.swing.plaf.synth.SynthInternalFrameUI

javax.swing.plaf.basic.BasicInternalFrameUI

- javax.swing.plaf.synth.SynthInternalFrameUI

javax.swing.plaf.synth.SynthInternalFrameUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthInternalFrameUI

extends
BasicInternalFrameUI

implements
SynthUI
,
PropertyChangeListener
```

Provides the Synth L&F UI delegate for

JInternalFrame

.

**Since:** 1.7

public class

SynthInternalFrameUI

extends

BasicInternalFrameUI

implements

SynthUI

,

PropertyChangeListener

Provides the Synth L&F UI delegate for

JInternalFrame

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

BasicInternalFrameUI.BasicInternalFrameListener

,

BasicInternalFrameUI.BorderListener

,

BasicInternalFrameUI.ComponentHandler

,

BasicInternalFrameUI.GlassPaneDispatcher

,

BasicInternalFrameUI.InternalFrameLayout

,

BasicInternalFrameUI.InternalFramePropertyChangeListener

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

borderListener

,

componentListener

,

eastPane

,

frame

,

glassPaneDispatcher

,

internalFrameLayout

,

northPane

,

openMenuKey

,

propertyChangeListener

,

southPane

,

titlePane

,

westPane

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

Modifier

Constructor

Description

protected

SynthInternalFrameUI

​(

JInternalFrame

b)

Constructs a

SynthInternalFrameUI

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

ComponentUI

createUI

​(

JComponent

b)

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

Paints the specified component.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

activateFrame

,

closeFrame

,

createBorderListener

,

createComponentListener

,

createDesktopManager

,

createEastPane

,

createGlassPaneDispatcher

,

createInternalFrameListener

,

createLayoutManager

,

createNorthPane

,

createPropertyChangeListener

,

createSouthPane

,

createWestPane

,

deactivateFrame

,

deiconifyFrame

,

deinstallMouseHandlers

,

getDesktopManager

,

getEastPane

,

getMaximumSize

,

getMinimumSize

,

getNorthPane

,

getPreferredSize

,

getSouthPane

,

getWestPane

,

iconifyFrame

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installMouseHandlers

,

installUI

,

isKeyBindingActive

,

isKeyBindingRegistered

,

maximizeFrame

,

minimizeFrame

,

replacePane

,

setEastPane

,

setKeyBindingActive

,

setKeyBindingRegistered

,

setNorthPane

,

setSouthPane

,

setupMenuCloseKey

,

setupMenuOpenKey

,

setWestPane

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

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

BasicInternalFrameUI

BasicInternalFrameUI.BasicInternalFrameListener

,

BasicInternalFrameUI.BorderListener

,

BasicInternalFrameUI.ComponentHandler

,

BasicInternalFrameUI.GlassPaneDispatcher

,

BasicInternalFrameUI.InternalFrameLayout

,

BasicInternalFrameUI.InternalFramePropertyChangeListener

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

BasicInternalFrameUI.BasicInternalFrameListener

,

BasicInternalFrameUI.BorderListener

,

BasicInternalFrameUI.ComponentHandler

,

BasicInternalFrameUI.GlassPaneDispatcher

,

BasicInternalFrameUI.InternalFrameLayout

,

BasicInternalFrameUI.InternalFramePropertyChangeListener

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicInternalFrameUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

borderListener

,

componentListener

,

eastPane

,

frame

,

glassPaneDispatcher

,

internalFrameLayout

,

northPane

,

openMenuKey

,

propertyChangeListener

,

southPane

,

titlePane

,

westPane

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

BasicInternalFrameUI

borderListener

,

componentListener

,

eastPane

,

frame

,

glassPaneDispatcher

,

internalFrameLayout

,

northPane

,

openMenuKey

,

propertyChangeListener

,

southPane

,

titlePane

,

westPane

---

#### Fields declared in class javax.swing.plaf.basic. BasicInternalFrameUI

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

Modifier

Constructor

Description

protected

SynthInternalFrameUI

​(

JInternalFrame

b)

Constructs a

SynthInternalFrameUI

.

---

#### Constructor Summary

Constructs a

SynthInternalFrameUI

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

ComponentUI

createUI

​(

JComponent

b)

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

Paints the specified component.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

activateFrame

,

closeFrame

,

createBorderListener

,

createComponentListener

,

createDesktopManager

,

createEastPane

,

createGlassPaneDispatcher

,

createInternalFrameListener

,

createLayoutManager

,

createNorthPane

,

createPropertyChangeListener

,

createSouthPane

,

createWestPane

,

deactivateFrame

,

deiconifyFrame

,

deinstallMouseHandlers

,

getDesktopManager

,

getEastPane

,

getMaximumSize

,

getMinimumSize

,

getNorthPane

,

getPreferredSize

,

getSouthPane

,

getWestPane

,

iconifyFrame

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installMouseHandlers

,

installUI

,

isKeyBindingActive

,

isKeyBindingRegistered

,

maximizeFrame

,

minimizeFrame

,

replacePane

,

setEastPane

,

setKeyBindingActive

,

setKeyBindingRegistered

,

setNorthPane

,

setSouthPane

,

setupMenuCloseKey

,

setupMenuOpenKey

,

setWestPane

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

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

Creates a new UI object for the given component.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

activateFrame

,

closeFrame

,

createBorderListener

,

createComponentListener

,

createDesktopManager

,

createEastPane

,

createGlassPaneDispatcher

,

createInternalFrameListener

,

createLayoutManager

,

createNorthPane

,

createPropertyChangeListener

,

createSouthPane

,

createWestPane

,

deactivateFrame

,

deiconifyFrame

,

deinstallMouseHandlers

,

getDesktopManager

,

getEastPane

,

getMaximumSize

,

getMinimumSize

,

getNorthPane

,

getPreferredSize

,

getSouthPane

,

getWestPane

,

iconifyFrame

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installMouseHandlers

,

installUI

,

isKeyBindingActive

,

isKeyBindingRegistered

,

maximizeFrame

,

minimizeFrame

,

replacePane

,

setEastPane

,

setKeyBindingActive

,

setKeyBindingRegistered

,

setNorthPane

,

setSouthPane

,

setupMenuCloseKey

,

setupMenuOpenKey

,

setWestPane

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

---

#### Methods declared in class javax.swing.plaf.basic. BasicInternalFrameUI

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

- SynthInternalFrameUI

```java
protected SynthInternalFrameUI​(
JInternalFrame
b)
```

Constructs a

SynthInternalFrameUI

.

**Parameters:** b

- an internal frame

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Creates a new UI object for the given component.

**Parameters:** b

- component to create UI object for
**Returns:** the UI object

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

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component. This implementation does nothing.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

Constructor Detail

- SynthInternalFrameUI

```java
protected SynthInternalFrameUI​(
JInternalFrame
b)
```

Constructs a

SynthInternalFrameUI

.

**Parameters:** b

- an internal frame

---

#### Constructor Detail

SynthInternalFrameUI

```java
protected SynthInternalFrameUI​(
JInternalFrame
b)
```

Constructs a

SynthInternalFrameUI

.

**Parameters:** b

- an internal frame

---

#### SynthInternalFrameUI

protected SynthInternalFrameUI​(

JInternalFrame

b)

Constructs a

SynthInternalFrameUI

.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Creates a new UI object for the given component.

**Parameters:** b

- component to create UI object for
**Returns:** the UI object

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

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component. This implementation does nothing.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Creates a new UI object for the given component.

**Parameters:** b

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

b)

Creates a new UI object for the given component.

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

paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component. This implementation does nothing.

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

Paints the specified component. This implementation does nothing.

---

