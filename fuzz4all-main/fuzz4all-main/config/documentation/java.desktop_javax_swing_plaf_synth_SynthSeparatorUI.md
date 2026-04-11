# Class SynthSeparatorUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthSeparatorUI.html`

### Class Description

```java
public class
SynthSeparatorUI

extends
SeparatorUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JSeparator

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

#### public SynthSeparatorUI()

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

#### public void installDefaults​(
JSeparator
c)

Installs default setting. This method is called when a

LookAndFeel

is installed.

**Parameters:**
- c

- specifies the

JSeparator

for the installed

LookAndFeel

.

---

#### public void uninstallDefaults​(
JSeparator
c)

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

**Parameters:**
- c

- specifies the

JSeparator

for the (un)installed

LookAndFeel

.

---

#### public void installListeners​(
JSeparator
c)

Installs listeners. This method is called when a

LookAndFeel

is installed.

**Parameters:**
- c

- specifies the

JSeparator

for the installed

LookAndFeel

.

---

#### public void uninstallListeners​(
JSeparator
c)

Uninstalls listeners. This method is called when a

LookAndFeel

is uninstalled.

**Parameters:**
- c

- specifies the

JSeparator

for the (un)installed

LookAndFeel

.

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

#### Class SynthSeparatorUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SeparatorUI
- - javax.swing.plaf.synth.SynthSeparatorUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SeparatorUI
- - javax.swing.plaf.synth.SynthSeparatorUI

javax.swing.plaf.SeparatorUI

- javax.swing.plaf.synth.SynthSeparatorUI

javax.swing.plaf.synth.SynthSeparatorUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthSeparatorUI

extends
SeparatorUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JSeparator

.

**Since:** 1.7

public class

SynthSeparatorUI

extends

SeparatorUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JSeparator

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

SynthSeparatorUI

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

installDefaults

​(

JSeparator

c)

Installs default setting.

void

installListeners

​(

JSeparator

c)

Installs listeners.

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

uninstallDefaults

​(

JSeparator

c)

Uninstalls default setting.

void

uninstallListeners

​(

JSeparator

c)

Uninstalls listeners.

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

,

paintBorder

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

SynthSeparatorUI

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

installDefaults

​(

JSeparator

c)

Installs default setting.

void

installListeners

​(

JSeparator

c)

Installs listeners.

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

uninstallDefaults

​(

JSeparator

c)

Uninstalls default setting.

void

uninstallListeners

​(

JSeparator

c)

Uninstalls listeners.

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

,

paintBorder

---

#### Method Summary

Creates a new UI object for the given component.

Installs default setting.

Installs listeners.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Uninstalls default setting.

Uninstalls listeners.

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

,

paintBorder

---

#### Methods declared in interface javax.swing.plaf.synth. SynthUI

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthSeparatorUI

```java
public SynthSeparatorUI()
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
public void installDefaults​(
JSeparator
c)
```

Installs default setting. This method is called when a

LookAndFeel

is installed.

**Parameters:** c

- specifies the

JSeparator

for the installed

LookAndFeel

.

- uninstallDefaults

```java
public void uninstallDefaults​(
JSeparator
c)
```

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

**Parameters:** c

- specifies the

JSeparator

for the (un)installed

LookAndFeel

.

- installListeners

```java
public void installListeners​(
JSeparator
c)
```

Installs listeners. This method is called when a

LookAndFeel

is installed.

**Parameters:** c

- specifies the

JSeparator

for the installed

LookAndFeel

.

- uninstallListeners

```java
public void uninstallListeners​(
JSeparator
c)
```

Uninstalls listeners. This method is called when a

LookAndFeel

is uninstalled.

**Parameters:** c

- specifies the

JSeparator

for the (un)installed

LookAndFeel

.

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

- SynthSeparatorUI

```java
public SynthSeparatorUI()
```

---

#### Constructor Detail

SynthSeparatorUI

```java
public SynthSeparatorUI()
```

---

#### SynthSeparatorUI

public SynthSeparatorUI()

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
public void installDefaults​(
JSeparator
c)
```

Installs default setting. This method is called when a

LookAndFeel

is installed.

**Parameters:** c

- specifies the

JSeparator

for the installed

LookAndFeel

.

- uninstallDefaults

```java
public void uninstallDefaults​(
JSeparator
c)
```

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

**Parameters:** c

- specifies the

JSeparator

for the (un)installed

LookAndFeel

.

- installListeners

```java
public void installListeners​(
JSeparator
c)
```

Installs listeners. This method is called when a

LookAndFeel

is installed.

**Parameters:** c

- specifies the

JSeparator

for the installed

LookAndFeel

.

- uninstallListeners

```java
public void uninstallListeners​(
JSeparator
c)
```

Uninstalls listeners. This method is called when a

LookAndFeel

is uninstalled.

**Parameters:** c

- specifies the

JSeparator

for the (un)installed

LookAndFeel

.

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
public void installDefaults​(
JSeparator
c)
```

Installs default setting. This method is called when a

LookAndFeel

is installed.

**Parameters:** c

- specifies the

JSeparator

for the installed

LookAndFeel

.

---

#### installDefaults

public void installDefaults​(

JSeparator

c)

Installs default setting. This method is called when a

LookAndFeel

is installed.

uninstallDefaults

```java
public void uninstallDefaults​(
JSeparator
c)
```

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

**Parameters:** c

- specifies the

JSeparator

for the (un)installed

LookAndFeel

.

---

#### uninstallDefaults

public void uninstallDefaults​(

JSeparator

c)

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

installListeners

```java
public void installListeners​(
JSeparator
c)
```

Installs listeners. This method is called when a

LookAndFeel

is installed.

**Parameters:** c

- specifies the

JSeparator

for the installed

LookAndFeel

.

---

#### installListeners

public void installListeners​(

JSeparator

c)

Installs listeners. This method is called when a

LookAndFeel

is installed.

uninstallListeners

```java
public void uninstallListeners​(
JSeparator
c)
```

Uninstalls listeners. This method is called when a

LookAndFeel

is uninstalled.

**Parameters:** c

- specifies the

JSeparator

for the (un)installed

LookAndFeel

.

---

#### uninstallListeners

public void uninstallListeners​(

JSeparator

c)

Uninstalls listeners. This method is called when a

LookAndFeel

is uninstalled.

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

