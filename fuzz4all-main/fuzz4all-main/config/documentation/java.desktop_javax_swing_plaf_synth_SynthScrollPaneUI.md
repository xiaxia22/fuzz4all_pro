# Class SynthScrollPaneUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthScrollPaneUI.html`

### Class Description

```java
public class
SynthScrollPaneUI

extends
BasicScrollPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JScrollPane

.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

,

ScrollPaneConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthScrollPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Creates a new UI object for the given component.

**Parameters:**
- x

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

Paints the specified component.

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

#### Class SynthScrollPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ScrollPaneUI
- - javax.swing.plaf.basic.BasicScrollPaneUI
- - javax.swing.plaf.synth.SynthScrollPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ScrollPaneUI
- - javax.swing.plaf.basic.BasicScrollPaneUI
- - javax.swing.plaf.synth.SynthScrollPaneUI

javax.swing.plaf.ScrollPaneUI

- javax.swing.plaf.basic.BasicScrollPaneUI
- - javax.swing.plaf.synth.SynthScrollPaneUI

javax.swing.plaf.basic.BasicScrollPaneUI

- javax.swing.plaf.synth.SynthScrollPaneUI

javax.swing.plaf.synth.SynthScrollPaneUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

,

ScrollPaneConstants

```java
public class
SynthScrollPaneUI

extends
BasicScrollPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JScrollPane

.

**Since:** 1.7

public class

SynthScrollPaneUI

extends

BasicScrollPaneUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JScrollPane

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicScrollPaneUI

BasicScrollPaneUI.HSBChangeListener

,

BasicScrollPaneUI.MouseWheelHandler

,

BasicScrollPaneUI.PropertyChangeHandler

,

BasicScrollPaneUI.ViewportChangeHandler

,

BasicScrollPaneUI.VSBChangeListener

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicScrollPaneUI

hsbChangeListener

,

scrollpane

,

spPropertyChangeListener

,

viewportChangeListener

,

vsbChangeListener

- Fields declared in interface javax.swing.

ScrollPaneConstants

COLUMN_HEADER

,

HORIZONTAL_SCROLLBAR

,

HORIZONTAL_SCROLLBAR_ALWAYS

,

HORIZONTAL_SCROLLBAR_AS_NEEDED

,

HORIZONTAL_SCROLLBAR_NEVER

,

HORIZONTAL_SCROLLBAR_POLICY

,

LOWER_LEADING_CORNER

,

LOWER_LEFT_CORNER

,

LOWER_RIGHT_CORNER

,

LOWER_TRAILING_CORNER

,

ROW_HEADER

,

UPPER_LEADING_CORNER

,

UPPER_LEFT_CORNER

,

UPPER_RIGHT_CORNER

,

UPPER_TRAILING_CORNER

,

VERTICAL_SCROLLBAR

,

VERTICAL_SCROLLBAR_ALWAYS

,

VERTICAL_SCROLLBAR_AS_NEEDED

,

VERTICAL_SCROLLBAR_NEVER

,

VERTICAL_SCROLLBAR_POLICY

,

VIEWPORT

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

SynthScrollPaneUI

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

x)

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

BasicScrollPaneUI

createHSBChangeListener

,

createMouseWheelListener

,

createPropertyChangeListener

,

createViewportChangeListener

,

createVSBChangeListener

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

installDefaults

,

installKeyboardActions

,

installListeners

,

syncScrollPaneWithViewport

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

updateColumnHeader

,

updateRowHeader

,

updateScrollBarDisplayPolicy

,

updateViewport

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

BasicScrollPaneUI

BasicScrollPaneUI.HSBChangeListener

,

BasicScrollPaneUI.MouseWheelHandler

,

BasicScrollPaneUI.PropertyChangeHandler

,

BasicScrollPaneUI.ViewportChangeHandler

,

BasicScrollPaneUI.VSBChangeListener

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicScrollPaneUI

BasicScrollPaneUI.HSBChangeListener

,

BasicScrollPaneUI.MouseWheelHandler

,

BasicScrollPaneUI.PropertyChangeHandler

,

BasicScrollPaneUI.ViewportChangeHandler

,

BasicScrollPaneUI.VSBChangeListener

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicScrollPaneUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicScrollPaneUI

hsbChangeListener

,

scrollpane

,

spPropertyChangeListener

,

viewportChangeListener

,

vsbChangeListener

- Fields declared in interface javax.swing.

ScrollPaneConstants

COLUMN_HEADER

,

HORIZONTAL_SCROLLBAR

,

HORIZONTAL_SCROLLBAR_ALWAYS

,

HORIZONTAL_SCROLLBAR_AS_NEEDED

,

HORIZONTAL_SCROLLBAR_NEVER

,

HORIZONTAL_SCROLLBAR_POLICY

,

LOWER_LEADING_CORNER

,

LOWER_LEFT_CORNER

,

LOWER_RIGHT_CORNER

,

LOWER_TRAILING_CORNER

,

ROW_HEADER

,

UPPER_LEADING_CORNER

,

UPPER_LEFT_CORNER

,

UPPER_RIGHT_CORNER

,

UPPER_TRAILING_CORNER

,

VERTICAL_SCROLLBAR

,

VERTICAL_SCROLLBAR_ALWAYS

,

VERTICAL_SCROLLBAR_AS_NEEDED

,

VERTICAL_SCROLLBAR_NEVER

,

VERTICAL_SCROLLBAR_POLICY

,

VIEWPORT

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

BasicScrollPaneUI

hsbChangeListener

,

scrollpane

,

spPropertyChangeListener

,

viewportChangeListener

,

vsbChangeListener

---

#### Fields declared in class javax.swing.plaf.basic. BasicScrollPaneUI

Fields declared in interface javax.swing.

ScrollPaneConstants

COLUMN_HEADER

,

HORIZONTAL_SCROLLBAR

,

HORIZONTAL_SCROLLBAR_ALWAYS

,

HORIZONTAL_SCROLLBAR_AS_NEEDED

,

HORIZONTAL_SCROLLBAR_NEVER

,

HORIZONTAL_SCROLLBAR_POLICY

,

LOWER_LEADING_CORNER

,

LOWER_LEFT_CORNER

,

LOWER_RIGHT_CORNER

,

LOWER_TRAILING_CORNER

,

ROW_HEADER

,

UPPER_LEADING_CORNER

,

UPPER_LEFT_CORNER

,

UPPER_RIGHT_CORNER

,

UPPER_TRAILING_CORNER

,

VERTICAL_SCROLLBAR

,

VERTICAL_SCROLLBAR_ALWAYS

,

VERTICAL_SCROLLBAR_AS_NEEDED

,

VERTICAL_SCROLLBAR_NEVER

,

VERTICAL_SCROLLBAR_POLICY

,

VIEWPORT

---

#### Fields declared in interface javax.swing. ScrollPaneConstants

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

SynthScrollPaneUI

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

x)

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

BasicScrollPaneUI

createHSBChangeListener

,

createMouseWheelListener

,

createPropertyChangeListener

,

createViewportChangeListener

,

createVSBChangeListener

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

installDefaults

,

installKeyboardActions

,

installListeners

,

syncScrollPaneWithViewport

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

updateColumnHeader

,

updateRowHeader

,

updateScrollBarDisplayPolicy

,

updateViewport

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

BasicScrollPaneUI

createHSBChangeListener

,

createMouseWheelListener

,

createPropertyChangeListener

,

createViewportChangeListener

,

createVSBChangeListener

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

installDefaults

,

installKeyboardActions

,

installListeners

,

syncScrollPaneWithViewport

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

updateColumnHeader

,

updateRowHeader

,

updateScrollBarDisplayPolicy

,

updateViewport

---

#### Methods declared in class javax.swing.plaf.basic. BasicScrollPaneUI

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

- SynthScrollPaneUI

```java
public SynthScrollPaneUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new UI object for the given component.

**Parameters:** x

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

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

Constructor Detail

- SynthScrollPaneUI

```java
public SynthScrollPaneUI()
```

---

#### Constructor Detail

SynthScrollPaneUI

```java
public SynthScrollPaneUI()
```

---

#### SynthScrollPaneUI

public SynthScrollPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new UI object for the given component.

**Parameters:** x

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

Paints the specified component.

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
x)
```

Creates a new UI object for the given component.

**Parameters:** x

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

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

Paints the specified component.

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

Paints the specified component.

---

