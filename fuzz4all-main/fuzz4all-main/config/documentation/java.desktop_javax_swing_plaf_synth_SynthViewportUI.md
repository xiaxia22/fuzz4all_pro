# Class SynthViewportUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthViewportUI.html`

### Class Description

```java
public class
SynthViewportUI

extends
ViewportUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JViewport

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

#### public SynthViewportUI()

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

#### protected void installDefaults​(
JComponent
c)

Installs defaults for a viewport.

**Parameters:**
- c

- a

JViewport

object

---

#### protected void installListeners​(
JComponent
c)

Installs listeners into the viewport.

**Parameters:**
- c

- a

JViewport

object

---

#### protected void uninstallListeners​(
JComponent
c)

Uninstalls listeners from the viewport.

**Parameters:**
- c

- a

JViewport

object

---

#### protected void uninstallDefaults​(
JComponent
c)

Uninstalls defaults from a viewport.

**Parameters:**
- c

- a

JViewport

object

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

#### public void paintBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border. The method is never called,
because the

JViewport

class does not support a border.
This implementation does nothing.

**Specified by:**
- paintBorder

in interface

SynthUI

**Parameters:**
- context

- a component context
- g

- the

Graphics

to paint on
- x

- the X coordinate
- y

- the Y coordinate
- w

- width of the border
- h

- height of the border

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

#### Class SynthViewportUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ViewportUI
- - javax.swing.plaf.synth.SynthViewportUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ViewportUI
- - javax.swing.plaf.synth.SynthViewportUI

javax.swing.plaf.ViewportUI

- javax.swing.plaf.synth.SynthViewportUI

javax.swing.plaf.synth.SynthViewportUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthViewportUI

extends
ViewportUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JViewport

.

**Since:** 1.7

public class

SynthViewportUI

extends

ViewportUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JViewport

.

=========== FIELD SUMMARY ===========

- Field Summary

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

SynthViewportUI

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

protected void

installDefaults

​(

JComponent

c)

Installs defaults for a viewport.

protected void

installListeners

​(

JComponent

c)

Installs listeners into the viewport.

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

paintBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border.

protected void

uninstallDefaults

​(

JComponent

c)

Uninstalls defaults from a viewport.

protected void

uninstallListeners

​(

JComponent

c)

Uninstalls listeners from the viewport.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

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

Field Summary

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

SynthViewportUI

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

protected void

installDefaults

​(

JComponent

c)

Installs defaults for a viewport.

protected void

installListeners

​(

JComponent

c)

Installs listeners into the viewport.

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

paintBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border.

protected void

uninstallDefaults

​(

JComponent

c)

Uninstalls defaults from a viewport.

protected void

uninstallListeners

​(

JComponent

c)

Uninstalls listeners from the viewport.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

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

---

#### Method Summary

Creates a new UI object for the given component.

Installs defaults for a viewport.

Installs listeners into the viewport.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Paints the border.

Uninstalls defaults from a viewport.

Uninstalls listeners from the viewport.

Notifies this UI delegate to repaint the specified component.

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

---

#### Methods declared in interface javax.swing.plaf.synth. SynthUI

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthViewportUI

```java
public SynthViewportUI()
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

- installDefaults

```java
protected void installDefaults​(
JComponent
c)
```

Installs defaults for a viewport.

**Parameters:** c

- a

JViewport

object

- installListeners

```java
protected void installListeners​(
JComponent
c)
```

Installs listeners into the viewport.

**Parameters:** c

- a

JViewport

object

- uninstallListeners

```java
protected void uninstallListeners​(
JComponent
c)
```

Uninstalls listeners from the viewport.

**Parameters:** c

- a

JViewport

object

- uninstallDefaults

```java
protected void uninstallDefaults​(
JComponent
c)
```

Uninstalls defaults from a viewport.

**Parameters:** c

- a

JViewport

object

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

- paintBorder

```java
public void paintBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border. The method is never called,
because the

JViewport

class does not support a border.
This implementation does nothing.

**Specified by:** paintBorder

in interface

SynthUI
**Parameters:** context

- a component context
**Parameters:** g

- the

Graphics

to paint on
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** w

- width of the border
**Parameters:** h

- height of the border

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

- SynthViewportUI

```java
public SynthViewportUI()
```

---

#### Constructor Detail

SynthViewportUI

```java
public SynthViewportUI()
```

---

#### SynthViewportUI

public SynthViewportUI()

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

- installDefaults

```java
protected void installDefaults​(
JComponent
c)
```

Installs defaults for a viewport.

**Parameters:** c

- a

JViewport

object

- installListeners

```java
protected void installListeners​(
JComponent
c)
```

Installs listeners into the viewport.

**Parameters:** c

- a

JViewport

object

- uninstallListeners

```java
protected void uninstallListeners​(
JComponent
c)
```

Uninstalls listeners from the viewport.

**Parameters:** c

- a

JViewport

object

- uninstallDefaults

```java
protected void uninstallDefaults​(
JComponent
c)
```

Uninstalls defaults from a viewport.

**Parameters:** c

- a

JViewport

object

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

- paintBorder

```java
public void paintBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border. The method is never called,
because the

JViewport

class does not support a border.
This implementation does nothing.

**Specified by:** paintBorder

in interface

SynthUI
**Parameters:** context

- a component context
**Parameters:** g

- the

Graphics

to paint on
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** w

- width of the border
**Parameters:** h

- height of the border

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

installDefaults

```java
protected void installDefaults​(
JComponent
c)
```

Installs defaults for a viewport.

**Parameters:** c

- a

JViewport

object

---

#### installDefaults

protected void installDefaults​(

JComponent

c)

Installs defaults for a viewport.

installListeners

```java
protected void installListeners​(
JComponent
c)
```

Installs listeners into the viewport.

**Parameters:** c

- a

JViewport

object

---

#### installListeners

protected void installListeners​(

JComponent

c)

Installs listeners into the viewport.

uninstallListeners

```java
protected void uninstallListeners​(
JComponent
c)
```

Uninstalls listeners from the viewport.

**Parameters:** c

- a

JViewport

object

---

#### uninstallListeners

protected void uninstallListeners​(

JComponent

c)

Uninstalls listeners from the viewport.

uninstallDefaults

```java
protected void uninstallDefaults​(
JComponent
c)
```

Uninstalls defaults from a viewport.

**Parameters:** c

- a

JViewport

object

---

#### uninstallDefaults

protected void uninstallDefaults​(

JComponent

c)

Uninstalls defaults from a viewport.

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

paintBorder

```java
public void paintBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border. The method is never called,
because the

JViewport

class does not support a border.
This implementation does nothing.

**Specified by:** paintBorder

in interface

SynthUI
**Parameters:** context

- a component context
**Parameters:** g

- the

Graphics

to paint on
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** w

- width of the border
**Parameters:** h

- height of the border

---

#### paintBorder

public void paintBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border. The method is never called,
because the

JViewport

class does not support a border.
This implementation does nothing.

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

