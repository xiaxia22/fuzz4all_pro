# Class MetalScrollPaneUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalScrollPaneUI.html`

### Class Description

```java
public class
MetalScrollPaneUI

extends
BasicScrollPaneUI
```

A Metal L&F implementation of ScrollPaneUI.

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

**All Implemented Interfaces:** ScrollPaneConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public MetalScrollPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Constructs a new

MetalScrollPaneUI

.

**Parameters:**
- x

- a component

**Returns:**
- a new

MetalScrollPaneUI

---

#### @Deprecated

public void uninstallListeners​(
JScrollPane
scrollPane)

**Parameters:**
- scrollPane

- an instance of the

JScrollPane

---

#### protected
PropertyChangeListener
createScrollBarSwapListener()

Returns a new

PropertyChangeListener

for scroll bar swap events.

**Returns:**
- a new

PropertyChangeListener

for scroll bar swap events.

---

### Additional Sections

#### Class MetalScrollPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ScrollPaneUI
- - javax.swing.plaf.basic.BasicScrollPaneUI
- - javax.swing.plaf.metal.MetalScrollPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ScrollPaneUI
- - javax.swing.plaf.basic.BasicScrollPaneUI
- - javax.swing.plaf.metal.MetalScrollPaneUI

javax.swing.plaf.ScrollPaneUI

- javax.swing.plaf.basic.BasicScrollPaneUI
- - javax.swing.plaf.metal.MetalScrollPaneUI

javax.swing.plaf.basic.BasicScrollPaneUI

- javax.swing.plaf.metal.MetalScrollPaneUI

javax.swing.plaf.metal.MetalScrollPaneUI

**All Implemented Interfaces:** ScrollPaneConstants

```java
public class
MetalScrollPaneUI

extends
BasicScrollPaneUI
```

A Metal L&F implementation of ScrollPaneUI.

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

MetalScrollPaneUI

extends

BasicScrollPaneUI

A Metal L&F implementation of ScrollPaneUI.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalScrollPaneUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected

PropertyChangeListener

createScrollBarSwapListener

()

Returns a new

PropertyChangeListener

for scroll bar swap events.

static

ComponentUI

createUI

​(

JComponent

x)

Constructs a new

MetalScrollPaneUI

.

void

uninstallListeners

​(

JScrollPane

scrollPane)

Deprecated.

- Replaced by

BasicScrollPaneUI.uninstallListeners(JComponent)

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

paint

,

uninstallUI

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

Constructor Summary

Constructors

Constructor

Description

MetalScrollPaneUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected

PropertyChangeListener

createScrollBarSwapListener

()

Returns a new

PropertyChangeListener

for scroll bar swap events.

static

ComponentUI

createUI

​(

JComponent

x)

Constructs a new

MetalScrollPaneUI

.

void

uninstallListeners

​(

JScrollPane

scrollPane)

Deprecated.

- Replaced by

BasicScrollPaneUI.uninstallListeners(JComponent)

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

paint

,

uninstallUI

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

Returns a new

PropertyChangeListener

for scroll bar swap events.

Constructs a new

MetalScrollPaneUI

.

Deprecated.

- Replaced by

BasicScrollPaneUI.uninstallListeners(JComponent)

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

paint

,

uninstallUI

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

- MetalScrollPaneUI

```java
public MetalScrollPaneUI()
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

Constructs a new

MetalScrollPaneUI

.

**Parameters:** x

- a component
**Returns:** a new

MetalScrollPaneUI

- uninstallListeners

```java
@Deprecated

public void uninstallListeners​(
JScrollPane
scrollPane)
```

Deprecated.

- Replaced by

BasicScrollPaneUI.uninstallListeners(JComponent)

**Parameters:** scrollPane

- an instance of the

JScrollPane

- createScrollBarSwapListener

```java
protected
PropertyChangeListener
createScrollBarSwapListener()
```

Returns a new

PropertyChangeListener

for scroll bar swap events.

**Returns:** a new

PropertyChangeListener

for scroll bar swap events.

Constructor Detail

- MetalScrollPaneUI

```java
public MetalScrollPaneUI()
```

---

#### Constructor Detail

MetalScrollPaneUI

```java
public MetalScrollPaneUI()
```

---

#### MetalScrollPaneUI

public MetalScrollPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Constructs a new

MetalScrollPaneUI

.

**Parameters:** x

- a component
**Returns:** a new

MetalScrollPaneUI

- uninstallListeners

```java
@Deprecated

public void uninstallListeners​(
JScrollPane
scrollPane)
```

Deprecated.

- Replaced by

BasicScrollPaneUI.uninstallListeners(JComponent)

**Parameters:** scrollPane

- an instance of the

JScrollPane

- createScrollBarSwapListener

```java
protected
PropertyChangeListener
createScrollBarSwapListener()
```

Returns a new

PropertyChangeListener

for scroll bar swap events.

**Returns:** a new

PropertyChangeListener

for scroll bar swap events.

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

Constructs a new

MetalScrollPaneUI

.

**Parameters:** x

- a component
**Returns:** a new

MetalScrollPaneUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Constructs a new

MetalScrollPaneUI

.

uninstallListeners

```java
@Deprecated

public void uninstallListeners​(
JScrollPane
scrollPane)
```

Deprecated.

- Replaced by

BasicScrollPaneUI.uninstallListeners(JComponent)

**Parameters:** scrollPane

- an instance of the

JScrollPane

---

#### uninstallListeners

@Deprecated

public void uninstallListeners​(

JScrollPane

scrollPane)

createScrollBarSwapListener

```java
protected
PropertyChangeListener
createScrollBarSwapListener()
```

Returns a new

PropertyChangeListener

for scroll bar swap events.

**Returns:** a new

PropertyChangeListener

for scroll bar swap events.

---

#### createScrollBarSwapListener

protected

PropertyChangeListener

createScrollBarSwapListener()

Returns a new

PropertyChangeListener

for scroll bar swap events.

---

