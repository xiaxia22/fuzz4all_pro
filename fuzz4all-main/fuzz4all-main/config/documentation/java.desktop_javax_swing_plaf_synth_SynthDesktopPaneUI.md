# Class SynthDesktopPaneUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthDesktopPaneUI.html`

### Class Description

```java
public class
SynthDesktopPaneUI

extends
BasicDesktopPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JDesktopPane

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

#### public SynthDesktopPaneUI()

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

#### Class SynthDesktopPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.DesktopPaneUI
- - javax.swing.plaf.basic.BasicDesktopPaneUI
- - javax.swing.plaf.synth.SynthDesktopPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.DesktopPaneUI
- - javax.swing.plaf.basic.BasicDesktopPaneUI
- - javax.swing.plaf.synth.SynthDesktopPaneUI

javax.swing.plaf.DesktopPaneUI

- javax.swing.plaf.basic.BasicDesktopPaneUI
- - javax.swing.plaf.synth.SynthDesktopPaneUI

javax.swing.plaf.basic.BasicDesktopPaneUI

- javax.swing.plaf.synth.SynthDesktopPaneUI

javax.swing.plaf.synth.SynthDesktopPaneUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthDesktopPaneUI

extends
BasicDesktopPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JDesktopPane

.

**Since:** 1.7

public class

SynthDesktopPaneUI

extends

BasicDesktopPaneUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JDesktopPane

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicDesktopPaneUI

BasicDesktopPaneUI.CloseAction

,

BasicDesktopPaneUI.MaximizeAction

,

BasicDesktopPaneUI.MinimizeAction

,

BasicDesktopPaneUI.NavigateAction

,

BasicDesktopPaneUI.OpenAction

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicDesktopPaneUI

closeKey

,

desktop

,

desktopManager

,

maximizeKey

,

minimizeKey

,

navigateKey

,

navigateKey2

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

SynthDesktopPaneUI

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

BasicDesktopPaneUI

createPropertyChangeListener

,

installDefaults

,

installDesktopManager

,

installKeyboardActions

,

installListeners

,

registerKeyboardActions

,

uninstallDefaults

,

uninstallDesktopManager

,

uninstallKeyboardActions

,

uninstallListeners

,

unregisterKeyboardActions

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

BasicDesktopPaneUI

BasicDesktopPaneUI.CloseAction

,

BasicDesktopPaneUI.MaximizeAction

,

BasicDesktopPaneUI.MinimizeAction

,

BasicDesktopPaneUI.NavigateAction

,

BasicDesktopPaneUI.OpenAction

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicDesktopPaneUI

BasicDesktopPaneUI.CloseAction

,

BasicDesktopPaneUI.MaximizeAction

,

BasicDesktopPaneUI.MinimizeAction

,

BasicDesktopPaneUI.NavigateAction

,

BasicDesktopPaneUI.OpenAction

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicDesktopPaneUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicDesktopPaneUI

closeKey

,

desktop

,

desktopManager

,

maximizeKey

,

minimizeKey

,

navigateKey

,

navigateKey2

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

BasicDesktopPaneUI

closeKey

,

desktop

,

desktopManager

,

maximizeKey

,

minimizeKey

,

navigateKey

,

navigateKey2

---

#### Fields declared in class javax.swing.plaf.basic. BasicDesktopPaneUI

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

SynthDesktopPaneUI

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

BasicDesktopPaneUI

createPropertyChangeListener

,

installDefaults

,

installDesktopManager

,

installKeyboardActions

,

installListeners

,

registerKeyboardActions

,

uninstallDefaults

,

uninstallDesktopManager

,

uninstallKeyboardActions

,

uninstallListeners

,

unregisterKeyboardActions

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

Creates a new UI object for the given component.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicDesktopPaneUI

createPropertyChangeListener

,

installDefaults

,

installDesktopManager

,

installKeyboardActions

,

installListeners

,

registerKeyboardActions

,

uninstallDefaults

,

uninstallDesktopManager

,

uninstallKeyboardActions

,

uninstallListeners

,

unregisterKeyboardActions

---

#### Methods declared in class javax.swing.plaf.basic. BasicDesktopPaneUI

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

- SynthDesktopPaneUI

```java
public SynthDesktopPaneUI()
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

- SynthDesktopPaneUI

```java
public SynthDesktopPaneUI()
```

---

#### Constructor Detail

SynthDesktopPaneUI

```java
public SynthDesktopPaneUI()
```

---

#### SynthDesktopPaneUI

public SynthDesktopPaneUI()

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

