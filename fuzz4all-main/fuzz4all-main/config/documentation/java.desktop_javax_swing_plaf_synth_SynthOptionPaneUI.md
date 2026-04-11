# Class SynthOptionPaneUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthOptionPaneUI.html`

### Class Description

```java
public class
SynthOptionPaneUI

extends
BasicOptionPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JOptionPane

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

#### public SynthOptionPaneUI()

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

#### protected
Container
createMessageArea()

Called from

BasicOptionPaneUI.installComponents()

to create a

Container

containing the body of the message. The icon is the created by calling

BasicOptionPaneUI.addIcon(java.awt.Container)

.

**Overrides:**
- createMessageArea

in class

BasicOptionPaneUI

**Returns:**
- a instance of

Container

---

### Additional Sections

#### Class SynthOptionPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.OptionPaneUI
- - javax.swing.plaf.basic.BasicOptionPaneUI
- - javax.swing.plaf.synth.SynthOptionPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.OptionPaneUI
- - javax.swing.plaf.basic.BasicOptionPaneUI
- - javax.swing.plaf.synth.SynthOptionPaneUI

javax.swing.plaf.OptionPaneUI

- javax.swing.plaf.basic.BasicOptionPaneUI
- - javax.swing.plaf.synth.SynthOptionPaneUI

javax.swing.plaf.basic.BasicOptionPaneUI

- javax.swing.plaf.synth.SynthOptionPaneUI

javax.swing.plaf.synth.SynthOptionPaneUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthOptionPaneUI

extends
BasicOptionPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JOptionPane

.

**Since:** 1.7

public class

SynthOptionPaneUI

extends

BasicOptionPaneUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JOptionPane

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicOptionPaneUI

BasicOptionPaneUI.ButtonActionListener

,

BasicOptionPaneUI.ButtonAreaLayout

,

BasicOptionPaneUI.PropertyChangeHandler

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicOptionPaneUI

hasCustomComponents

,

initialFocusComponent

,

inputComponent

,

MinimumHeight

,

minimumSize

,

MinimumWidth

,

optionPane

,

propertyChangeListener

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

SynthOptionPaneUI

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

Container

createMessageArea

()

Called from

BasicOptionPaneUI.installComponents()

to create a

Container

containing the body of the message.

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

BasicOptionPaneUI

addButtonComponents

,

addIcon

,

addMessageComponents

,

burstStringInto

,

containsCustomComponents

,

createButtonActionListener

,

createButtonArea

,

createLayoutManager

,

createPropertyChangeListener

,

createSeparator

,

getButtons

,

getIcon

,

getIconForType

,

getInitialValueIndex

,

getMaxCharactersPerLineCount

,

getMessage

,

getMinimumOptionPaneSize

,

getPreferredSize

,

getSizeButtonsToSameWidth

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

resetInputValue

,

selectInitialValue

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

,

getMaximumSize

,

getMinimumSize

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

BasicOptionPaneUI

BasicOptionPaneUI.ButtonActionListener

,

BasicOptionPaneUI.ButtonAreaLayout

,

BasicOptionPaneUI.PropertyChangeHandler

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicOptionPaneUI

BasicOptionPaneUI.ButtonActionListener

,

BasicOptionPaneUI.ButtonAreaLayout

,

BasicOptionPaneUI.PropertyChangeHandler

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicOptionPaneUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicOptionPaneUI

hasCustomComponents

,

initialFocusComponent

,

inputComponent

,

MinimumHeight

,

minimumSize

,

MinimumWidth

,

optionPane

,

propertyChangeListener

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

BasicOptionPaneUI

hasCustomComponents

,

initialFocusComponent

,

inputComponent

,

MinimumHeight

,

minimumSize

,

MinimumWidth

,

optionPane

,

propertyChangeListener

---

#### Fields declared in class javax.swing.plaf.basic. BasicOptionPaneUI

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

SynthOptionPaneUI

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

Container

createMessageArea

()

Called from

BasicOptionPaneUI.installComponents()

to create a

Container

containing the body of the message.

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

BasicOptionPaneUI

addButtonComponents

,

addIcon

,

addMessageComponents

,

burstStringInto

,

containsCustomComponents

,

createButtonActionListener

,

createButtonArea

,

createLayoutManager

,

createPropertyChangeListener

,

createSeparator

,

getButtons

,

getIcon

,

getIconForType

,

getInitialValueIndex

,

getMaxCharactersPerLineCount

,

getMessage

,

getMinimumOptionPaneSize

,

getPreferredSize

,

getSizeButtonsToSameWidth

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

resetInputValue

,

selectInitialValue

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

,

getMaximumSize

,

getMinimumSize

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

Called from

BasicOptionPaneUI.installComponents()

to create a

Container

containing the body of the message.

Creates a new UI object for the given component.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicOptionPaneUI

addButtonComponents

,

addIcon

,

addMessageComponents

,

burstStringInto

,

containsCustomComponents

,

createButtonActionListener

,

createButtonArea

,

createLayoutManager

,

createPropertyChangeListener

,

createSeparator

,

getButtons

,

getIcon

,

getIconForType

,

getInitialValueIndex

,

getMaxCharactersPerLineCount

,

getMessage

,

getMinimumOptionPaneSize

,

getPreferredSize

,

getSizeButtonsToSameWidth

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

resetInputValue

,

selectInitialValue

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

#### Methods declared in class javax.swing.plaf.basic. BasicOptionPaneUI

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

- SynthOptionPaneUI

```java
public SynthOptionPaneUI()
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

Paints the specified component. This implementation does nothing.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- createMessageArea

```java
protected
Container
createMessageArea()
```

Called from

BasicOptionPaneUI.installComponents()

to create a

Container

containing the body of the message. The icon is the created by calling

BasicOptionPaneUI.addIcon(java.awt.Container)

.

**Overrides:** createMessageArea

in class

BasicOptionPaneUI
**Returns:** a instance of

Container

Constructor Detail

- SynthOptionPaneUI

```java
public SynthOptionPaneUI()
```

---

#### Constructor Detail

SynthOptionPaneUI

```java
public SynthOptionPaneUI()
```

---

#### SynthOptionPaneUI

public SynthOptionPaneUI()

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

Paints the specified component. This implementation does nothing.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- createMessageArea

```java
protected
Container
createMessageArea()
```

Called from

BasicOptionPaneUI.installComponents()

to create a

Container

containing the body of the message. The icon is the created by calling

BasicOptionPaneUI.addIcon(java.awt.Container)

.

**Overrides:** createMessageArea

in class

BasicOptionPaneUI
**Returns:** a instance of

Container

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

createMessageArea

```java
protected
Container
createMessageArea()
```

Called from

BasicOptionPaneUI.installComponents()

to create a

Container

containing the body of the message. The icon is the created by calling

BasicOptionPaneUI.addIcon(java.awt.Container)

.

**Overrides:** createMessageArea

in class

BasicOptionPaneUI
**Returns:** a instance of

Container

---

#### createMessageArea

protected

Container

createMessageArea()

Called from

BasicOptionPaneUI.installComponents()

to create a

Container

containing the body of the message. The icon is the created by calling

BasicOptionPaneUI.addIcon(java.awt.Container)

.

---

