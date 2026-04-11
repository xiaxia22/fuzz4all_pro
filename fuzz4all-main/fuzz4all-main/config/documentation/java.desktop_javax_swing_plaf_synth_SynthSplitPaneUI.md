# Class SynthSplitPaneUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthSplitPaneUI.html`

### Class Description

```java
public class
SynthSplitPaneUI

extends
BasicSplitPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JSplitPane

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

#### public SynthSplitPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Creates a new SynthSplitPaneUI instance

**Parameters:**
- x

- component to create UI object for

**Returns:**
- the UI object

---

#### protected void installDefaults()

Installs the UI defaults.

**Overrides:**
- installDefaults

in class

BasicSplitPaneUI

---

#### protected void installListeners()

Installs the event listeners for the UI.

**Overrides:**
- installListeners

in class

BasicSplitPaneUI

---

#### protected void uninstallDefaults()

Uninstalls the UI defaults.

**Overrides:**
- uninstallDefaults

in class

BasicSplitPaneUI

---

#### protected void uninstallListeners()

Uninstalls the event listeners from the UI.

**Overrides:**
- uninstallListeners

in class

BasicSplitPaneUI

---

#### public
BasicSplitPaneDivider
createDefaultDivider()

Creates the default divider.

**Overrides:**
- createDefaultDivider

in class

BasicSplitPaneUI

**Returns:**
- the default divider

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

#### Class SynthSplitPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SplitPaneUI
- - javax.swing.plaf.basic.BasicSplitPaneUI
- - javax.swing.plaf.synth.SynthSplitPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SplitPaneUI
- - javax.swing.plaf.basic.BasicSplitPaneUI
- - javax.swing.plaf.synth.SynthSplitPaneUI

javax.swing.plaf.SplitPaneUI

- javax.swing.plaf.basic.BasicSplitPaneUI
- - javax.swing.plaf.synth.SynthSplitPaneUI

javax.swing.plaf.basic.BasicSplitPaneUI

- javax.swing.plaf.synth.SynthSplitPaneUI

javax.swing.plaf.synth.SynthSplitPaneUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthSplitPaneUI

extends
BasicSplitPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JSplitPane

.

**Since:** 1.7

public class

SynthSplitPaneUI

extends

BasicSplitPaneUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JSplitPane

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicSplitPaneUI

BasicSplitPaneUI.BasicHorizontalLayoutManager

,

BasicSplitPaneUI.BasicVerticalLayoutManager

,

BasicSplitPaneUI.FocusHandler

,

BasicSplitPaneUI.KeyboardDownRightHandler

,

BasicSplitPaneUI.KeyboardEndHandler

,

BasicSplitPaneUI.KeyboardHomeHandler

,

BasicSplitPaneUI.KeyboardResizeToggleHandler

,

BasicSplitPaneUI.KeyboardUpLeftHandler

,

BasicSplitPaneUI.PropertyHandler

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicSplitPaneUI

beginDragDividerLocation

,

divider

,

dividerResizeToggleKey

,

dividerSize

,

downKey

,

draggingHW

,

endKey

,

focusListener

,

homeKey

,

KEYBOARD_DIVIDER_MOVE_OFFSET

,

keyboardDownRightListener

,

keyboardEndListener

,

keyboardHomeListener

,

keyboardResizeToggleListener

,

keyboardUpLeftListener

,

layoutManager

,

leftKey

,

NON_CONTINUOUS_DIVIDER

,

nonContinuousLayoutDivider

,

propertyChangeListener

,

rightKey

,

splitPane

,

upKey

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

SynthSplitPaneUI

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

BasicSplitPaneDivider

createDefaultDivider

()

Creates the default divider.

static

ComponentUI

createUI

​(

JComponent

x)

Creates a new SynthSplitPaneUI instance

protected void

installDefaults

()

Installs the UI defaults.

protected void

installListeners

()

Installs the event listeners for the UI.

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

protected void

uninstallDefaults

()

Uninstalls the UI defaults.

protected void

uninstallListeners

()

Uninstalls the event listeners from the UI.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicSplitPaneUI

createDefaultNonContinuousLayoutDivider

,

createFocusListener

,

createKeyboardDownRightListener

,

createKeyboardEndListener

,

createKeyboardHomeListener

,

createKeyboardResizeToggleListener

,

createKeyboardUpLeftListener

,

createPropertyChangeListener

,

dragDividerTo

,

finishDraggingTo

,

finishedPaintingChildren

,

getDivider

,

getDividerBorderSize

,

getDividerLocation

,

getInsets

,

getLastDragLocation

,

getMaximumDividerLocation

,

getMaximumSize

,

getMinimumDividerLocation

,

getMinimumSize

,

getNonContinuousLayoutDivider

,

getOrientation

,

getPreferredSize

,

getSplitPane

,

installKeyboardActions

,

installUI

,

isContinuousLayout

,

resetLayoutManager

,

resetToPreferredSizes

,

setContinuousLayout

,

setDividerLocation

,

setLastDragLocation

,

setNonContinuousLayoutDivider

,

setNonContinuousLayoutDivider

,

setOrientation

,

startDragging

,

uninstallKeyboardActions

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

BasicSplitPaneUI

BasicSplitPaneUI.BasicHorizontalLayoutManager

,

BasicSplitPaneUI.BasicVerticalLayoutManager

,

BasicSplitPaneUI.FocusHandler

,

BasicSplitPaneUI.KeyboardDownRightHandler

,

BasicSplitPaneUI.KeyboardEndHandler

,

BasicSplitPaneUI.KeyboardHomeHandler

,

BasicSplitPaneUI.KeyboardResizeToggleHandler

,

BasicSplitPaneUI.KeyboardUpLeftHandler

,

BasicSplitPaneUI.PropertyHandler

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicSplitPaneUI

BasicSplitPaneUI.BasicHorizontalLayoutManager

,

BasicSplitPaneUI.BasicVerticalLayoutManager

,

BasicSplitPaneUI.FocusHandler

,

BasicSplitPaneUI.KeyboardDownRightHandler

,

BasicSplitPaneUI.KeyboardEndHandler

,

BasicSplitPaneUI.KeyboardHomeHandler

,

BasicSplitPaneUI.KeyboardResizeToggleHandler

,

BasicSplitPaneUI.KeyboardUpLeftHandler

,

BasicSplitPaneUI.PropertyHandler

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicSplitPaneUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicSplitPaneUI

beginDragDividerLocation

,

divider

,

dividerResizeToggleKey

,

dividerSize

,

downKey

,

draggingHW

,

endKey

,

focusListener

,

homeKey

,

KEYBOARD_DIVIDER_MOVE_OFFSET

,

keyboardDownRightListener

,

keyboardEndListener

,

keyboardHomeListener

,

keyboardResizeToggleListener

,

keyboardUpLeftListener

,

layoutManager

,

leftKey

,

NON_CONTINUOUS_DIVIDER

,

nonContinuousLayoutDivider

,

propertyChangeListener

,

rightKey

,

splitPane

,

upKey

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

BasicSplitPaneUI

beginDragDividerLocation

,

divider

,

dividerResizeToggleKey

,

dividerSize

,

downKey

,

draggingHW

,

endKey

,

focusListener

,

homeKey

,

KEYBOARD_DIVIDER_MOVE_OFFSET

,

keyboardDownRightListener

,

keyboardEndListener

,

keyboardHomeListener

,

keyboardResizeToggleListener

,

keyboardUpLeftListener

,

layoutManager

,

leftKey

,

NON_CONTINUOUS_DIVIDER

,

nonContinuousLayoutDivider

,

propertyChangeListener

,

rightKey

,

splitPane

,

upKey

---

#### Fields declared in class javax.swing.plaf.basic. BasicSplitPaneUI

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

SynthSplitPaneUI

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

BasicSplitPaneDivider

createDefaultDivider

()

Creates the default divider.

static

ComponentUI

createUI

​(

JComponent

x)

Creates a new SynthSplitPaneUI instance

protected void

installDefaults

()

Installs the UI defaults.

protected void

installListeners

()

Installs the event listeners for the UI.

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

protected void

uninstallDefaults

()

Uninstalls the UI defaults.

protected void

uninstallListeners

()

Uninstalls the event listeners from the UI.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicSplitPaneUI

createDefaultNonContinuousLayoutDivider

,

createFocusListener

,

createKeyboardDownRightListener

,

createKeyboardEndListener

,

createKeyboardHomeListener

,

createKeyboardResizeToggleListener

,

createKeyboardUpLeftListener

,

createPropertyChangeListener

,

dragDividerTo

,

finishDraggingTo

,

finishedPaintingChildren

,

getDivider

,

getDividerBorderSize

,

getDividerLocation

,

getInsets

,

getLastDragLocation

,

getMaximumDividerLocation

,

getMaximumSize

,

getMinimumDividerLocation

,

getMinimumSize

,

getNonContinuousLayoutDivider

,

getOrientation

,

getPreferredSize

,

getSplitPane

,

installKeyboardActions

,

installUI

,

isContinuousLayout

,

resetLayoutManager

,

resetToPreferredSizes

,

setContinuousLayout

,

setDividerLocation

,

setLastDragLocation

,

setNonContinuousLayoutDivider

,

setNonContinuousLayoutDivider

,

setOrientation

,

startDragging

,

uninstallKeyboardActions

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

Creates the default divider.

Creates a new SynthSplitPaneUI instance

Installs the UI defaults.

Installs the event listeners for the UI.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Uninstalls the UI defaults.

Uninstalls the event listeners from the UI.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicSplitPaneUI

createDefaultNonContinuousLayoutDivider

,

createFocusListener

,

createKeyboardDownRightListener

,

createKeyboardEndListener

,

createKeyboardHomeListener

,

createKeyboardResizeToggleListener

,

createKeyboardUpLeftListener

,

createPropertyChangeListener

,

dragDividerTo

,

finishDraggingTo

,

finishedPaintingChildren

,

getDivider

,

getDividerBorderSize

,

getDividerLocation

,

getInsets

,

getLastDragLocation

,

getMaximumDividerLocation

,

getMaximumSize

,

getMinimumDividerLocation

,

getMinimumSize

,

getNonContinuousLayoutDivider

,

getOrientation

,

getPreferredSize

,

getSplitPane

,

installKeyboardActions

,

installUI

,

isContinuousLayout

,

resetLayoutManager

,

resetToPreferredSizes

,

setContinuousLayout

,

setDividerLocation

,

setLastDragLocation

,

setNonContinuousLayoutDivider

,

setNonContinuousLayoutDivider

,

setOrientation

,

startDragging

,

uninstallKeyboardActions

,

uninstallUI

---

#### Methods declared in class javax.swing.plaf.basic. BasicSplitPaneUI

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

- SynthSplitPaneUI

```java
public SynthSplitPaneUI()
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

Creates a new SynthSplitPaneUI instance

**Parameters:** x

- component to create UI object for
**Returns:** the UI object

- installDefaults

```java
protected void installDefaults()
```

Installs the UI defaults.

**Overrides:** installDefaults

in class

BasicSplitPaneUI

- installListeners

```java
protected void installListeners()
```

Installs the event listeners for the UI.

**Overrides:** installListeners

in class

BasicSplitPaneUI

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the UI defaults.

**Overrides:** uninstallDefaults

in class

BasicSplitPaneUI

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the event listeners from the UI.

**Overrides:** uninstallListeners

in class

BasicSplitPaneUI

- createDefaultDivider

```java
public
BasicSplitPaneDivider
createDefaultDivider()
```

Creates the default divider.

**Overrides:** createDefaultDivider

in class

BasicSplitPaneUI
**Returns:** the default divider

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

- SynthSplitPaneUI

```java
public SynthSplitPaneUI()
```

---

#### Constructor Detail

SynthSplitPaneUI

```java
public SynthSplitPaneUI()
```

---

#### SynthSplitPaneUI

public SynthSplitPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new SynthSplitPaneUI instance

**Parameters:** x

- component to create UI object for
**Returns:** the UI object

- installDefaults

```java
protected void installDefaults()
```

Installs the UI defaults.

**Overrides:** installDefaults

in class

BasicSplitPaneUI

- installListeners

```java
protected void installListeners()
```

Installs the event listeners for the UI.

**Overrides:** installListeners

in class

BasicSplitPaneUI

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the UI defaults.

**Overrides:** uninstallDefaults

in class

BasicSplitPaneUI

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the event listeners from the UI.

**Overrides:** uninstallListeners

in class

BasicSplitPaneUI

- createDefaultDivider

```java
public
BasicSplitPaneDivider
createDefaultDivider()
```

Creates the default divider.

**Overrides:** createDefaultDivider

in class

BasicSplitPaneUI
**Returns:** the default divider

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
x)
```

Creates a new SynthSplitPaneUI instance

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

Creates a new SynthSplitPaneUI instance

installDefaults

```java
protected void installDefaults()
```

Installs the UI defaults.

**Overrides:** installDefaults

in class

BasicSplitPaneUI

---

#### installDefaults

protected void installDefaults()

Installs the UI defaults.

installListeners

```java
protected void installListeners()
```

Installs the event listeners for the UI.

**Overrides:** installListeners

in class

BasicSplitPaneUI

---

#### installListeners

protected void installListeners()

Installs the event listeners for the UI.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the UI defaults.

**Overrides:** uninstallDefaults

in class

BasicSplitPaneUI

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls the UI defaults.

uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the event listeners from the UI.

**Overrides:** uninstallListeners

in class

BasicSplitPaneUI

---

#### uninstallListeners

protected void uninstallListeners()

Uninstalls the event listeners from the UI.

createDefaultDivider

```java
public
BasicSplitPaneDivider
createDefaultDivider()
```

Creates the default divider.

**Overrides:** createDefaultDivider

in class

BasicSplitPaneUI
**Returns:** the default divider

---

#### createDefaultDivider

public

BasicSplitPaneDivider

createDefaultDivider()

Creates the default divider.

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

