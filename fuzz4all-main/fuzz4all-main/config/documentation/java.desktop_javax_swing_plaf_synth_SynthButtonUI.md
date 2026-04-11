# Class SynthButtonUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthButtonUI.html`

### Class Description

```java
public class
SynthButtonUI

extends
BasicButtonUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JButton

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

#### public SynthButtonUI()

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

#### protected
Icon
getDefaultIcon​(
AbstractButton
b)

Returns the default icon. This should not callback
to the JComponent.

**Parameters:**
- b

- button the icon is associated with

**Returns:**
- default icon

---

#### protected
Icon
getIcon​(
AbstractButton
b)

Returns the Icon to use for painting the button. The icon is chosen with
respect to the current state of the button.

**Parameters:**
- b

- button the icon is associated with

**Returns:**
- an icon

---

#### protected
Icon
getSizingIcon​(
AbstractButton
b)

Returns the Icon used in calculating the
preferred/minimum/maximum size.

**Parameters:**
- b

- specifies the

AbstractButton

used when calculating the preferred/minimum/maximum
size.

**Returns:**
- the Icon used in calculating the
preferred/minimum/maximum size.

---

### Additional Sections

#### Class SynthButtonUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.synth.SynthButtonUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.synth.SynthButtonUI

javax.swing.plaf.ButtonUI

- javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.synth.SynthButtonUI

javax.swing.plaf.basic.BasicButtonUI

- javax.swing.plaf.synth.SynthButtonUI

javax.swing.plaf.synth.SynthButtonUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

**Direct Known Subclasses:** SynthToggleButtonUI

```java
public class
SynthButtonUI

extends
BasicButtonUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JButton

.

**Since:** 1.7

public class

SynthButtonUI

extends

BasicButtonUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JButton

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicButtonUI

defaultTextIconGap

,

defaultTextShiftOffset

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

SynthButtonUI

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

protected

Icon

getDefaultIcon

​(

AbstractButton

b)

Returns the default icon.

protected

Icon

getIcon

​(

AbstractButton

b)

Returns the Icon to use for painting the button.

protected

Icon

getSizingIcon

​(

AbstractButton

b)

Returns the Icon used in calculating the
preferred/minimum/maximum size.

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

BasicButtonUI

clearTextShiftOffset

,

createButtonListener

,

getBaseline

,

getBaselineResizeBehavior

,

getDefaultTextIconGap

,

getPropertyPrefix

,

getTextShiftOffset

,

installDefaults

,

installKeyboardActions

,

installListeners

,

paintButtonPressed

,

paintFocus

,

paintIcon

,

paintText

,

paintText

,

setTextShiftOffset

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

- Fields declared in class javax.swing.plaf.basic.

BasicButtonUI

defaultTextIconGap

,

defaultTextShiftOffset

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

BasicButtonUI

defaultTextIconGap

,

defaultTextShiftOffset

---

#### Fields declared in class javax.swing.plaf.basic. BasicButtonUI

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

SynthButtonUI

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

protected

Icon

getDefaultIcon

​(

AbstractButton

b)

Returns the default icon.

protected

Icon

getIcon

​(

AbstractButton

b)

Returns the Icon to use for painting the button.

protected

Icon

getSizingIcon

​(

AbstractButton

b)

Returns the Icon used in calculating the
preferred/minimum/maximum size.

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

BasicButtonUI

clearTextShiftOffset

,

createButtonListener

,

getBaseline

,

getBaselineResizeBehavior

,

getDefaultTextIconGap

,

getPropertyPrefix

,

getTextShiftOffset

,

installDefaults

,

installKeyboardActions

,

installListeners

,

paintButtonPressed

,

paintFocus

,

paintIcon

,

paintText

,

paintText

,

setTextShiftOffset

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

Returns the default icon.

Returns the Icon to use for painting the button.

Returns the Icon used in calculating the
preferred/minimum/maximum size.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicButtonUI

clearTextShiftOffset

,

createButtonListener

,

getBaseline

,

getBaselineResizeBehavior

,

getDefaultTextIconGap

,

getPropertyPrefix

,

getTextShiftOffset

,

installDefaults

,

installKeyboardActions

,

installListeners

,

paintButtonPressed

,

paintFocus

,

paintIcon

,

paintText

,

paintText

,

setTextShiftOffset

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

---

#### Methods declared in class javax.swing.plaf.basic. BasicButtonUI

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

- SynthButtonUI

```java
public SynthButtonUI()
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

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- getDefaultIcon

```java
protected
Icon
getDefaultIcon​(
AbstractButton
b)
```

Returns the default icon. This should not callback
to the JComponent.

**Parameters:** b

- button the icon is associated with
**Returns:** default icon

- getIcon

```java
protected
Icon
getIcon​(
AbstractButton
b)
```

Returns the Icon to use for painting the button. The icon is chosen with
respect to the current state of the button.

**Parameters:** b

- button the icon is associated with
**Returns:** an icon

- getSizingIcon

```java
protected
Icon
getSizingIcon​(
AbstractButton
b)
```

Returns the Icon used in calculating the
preferred/minimum/maximum size.

**Parameters:** b

- specifies the

AbstractButton

used when calculating the preferred/minimum/maximum
size.
**Returns:** the Icon used in calculating the
preferred/minimum/maximum size.

Constructor Detail

- SynthButtonUI

```java
public SynthButtonUI()
```

---

#### Constructor Detail

SynthButtonUI

```java
public SynthButtonUI()
```

---

#### SynthButtonUI

public SynthButtonUI()

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

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- getDefaultIcon

```java
protected
Icon
getDefaultIcon​(
AbstractButton
b)
```

Returns the default icon. This should not callback
to the JComponent.

**Parameters:** b

- button the icon is associated with
**Returns:** default icon

- getIcon

```java
protected
Icon
getIcon​(
AbstractButton
b)
```

Returns the Icon to use for painting the button. The icon is chosen with
respect to the current state of the button.

**Parameters:** b

- button the icon is associated with
**Returns:** an icon

- getSizingIcon

```java
protected
Icon
getSizingIcon​(
AbstractButton
b)
```

Returns the Icon used in calculating the
preferred/minimum/maximum size.

**Parameters:** b

- specifies the

AbstractButton

used when calculating the preferred/minimum/maximum
size.
**Returns:** the Icon used in calculating the
preferred/minimum/maximum size.

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

getDefaultIcon

```java
protected
Icon
getDefaultIcon​(
AbstractButton
b)
```

Returns the default icon. This should not callback
to the JComponent.

**Parameters:** b

- button the icon is associated with
**Returns:** default icon

---

#### getDefaultIcon

protected

Icon

getDefaultIcon​(

AbstractButton

b)

Returns the default icon. This should not callback
to the JComponent.

getIcon

```java
protected
Icon
getIcon​(
AbstractButton
b)
```

Returns the Icon to use for painting the button. The icon is chosen with
respect to the current state of the button.

**Parameters:** b

- button the icon is associated with
**Returns:** an icon

---

#### getIcon

protected

Icon

getIcon​(

AbstractButton

b)

Returns the Icon to use for painting the button. The icon is chosen with
respect to the current state of the button.

getSizingIcon

```java
protected
Icon
getSizingIcon​(
AbstractButton
b)
```

Returns the Icon used in calculating the
preferred/minimum/maximum size.

**Parameters:** b

- specifies the

AbstractButton

used when calculating the preferred/minimum/maximum
size.
**Returns:** the Icon used in calculating the
preferred/minimum/maximum size.

---

#### getSizingIcon

protected

Icon

getSizingIcon​(

AbstractButton

b)

Returns the Icon used in calculating the
preferred/minimum/maximum size.

---

