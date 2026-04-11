# Class MetalSplitPaneUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalSplitPaneUI.html`

### Class Description

```java
public class
MetalSplitPaneUI

extends
BasicSplitPaneUI
```

Metal split pane.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

---

### Field Details

*No entries found.*

### Constructor Details

#### public MetalSplitPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Creates a new

MetalSplitPaneUI

instance

**Parameters:**
- x

- a component

**Returns:**
- a new

MetalSplitPaneUI

instance

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

### Additional Sections

#### Class MetalSplitPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SplitPaneUI
- - javax.swing.plaf.basic.BasicSplitPaneUI
- - javax.swing.plaf.metal.MetalSplitPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SplitPaneUI
- - javax.swing.plaf.basic.BasicSplitPaneUI
- - javax.swing.plaf.metal.MetalSplitPaneUI

javax.swing.plaf.SplitPaneUI

- javax.swing.plaf.basic.BasicSplitPaneUI
- - javax.swing.plaf.metal.MetalSplitPaneUI

javax.swing.plaf.basic.BasicSplitPaneUI

- javax.swing.plaf.metal.MetalSplitPaneUI

javax.swing.plaf.metal.MetalSplitPaneUI

```java
public class
MetalSplitPaneUI

extends
BasicSplitPaneUI
```

Metal split pane.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

public class

MetalSplitPaneUI

extends

BasicSplitPaneUI

Metal split pane.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalSplitPaneUI

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

Creates a new

MetalSplitPaneUI

instance

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

installDefaults

,

installKeyboardActions

,

installListeners

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

paint

,

update

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

Constructor Summary

Constructors

Constructor

Description

MetalSplitPaneUI

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

Creates a new

MetalSplitPaneUI

instance

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

installDefaults

,

installKeyboardActions

,

installListeners

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

paint

,

update

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

Creates the default divider.

Creates a new

MetalSplitPaneUI

instance

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

installDefaults

,

installKeyboardActions

,

installListeners

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

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

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

,

paint

,

update

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalSplitPaneUI

```java
public MetalSplitPaneUI()
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

Creates a new

MetalSplitPaneUI

instance

**Parameters:** x

- a component
**Returns:** a new

MetalSplitPaneUI

instance

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

Constructor Detail

- MetalSplitPaneUI

```java
public MetalSplitPaneUI()
```

---

#### Constructor Detail

MetalSplitPaneUI

```java
public MetalSplitPaneUI()
```

---

#### MetalSplitPaneUI

public MetalSplitPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new

MetalSplitPaneUI

instance

**Parameters:** x

- a component
**Returns:** a new

MetalSplitPaneUI

instance

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

Creates a new

MetalSplitPaneUI

instance

**Parameters:** x

- a component
**Returns:** a new

MetalSplitPaneUI

instance

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Creates a new

MetalSplitPaneUI

instance

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

---

