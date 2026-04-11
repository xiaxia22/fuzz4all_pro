# Class BasicToggleButtonUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicToggleButtonUI.html`

### Class Description

```java
public class
BasicToggleButtonUI

extends
BasicButtonUI
```

BasicToggleButton implementation

**Direct Known Subclasses:** BasicRadioButtonUI

,

MetalToggleButtonUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicToggleButtonUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
b)

Returns an instance of

BasicToggleButtonUI

.

**Parameters:**
- b

- a component

**Returns:**
- an instance of

BasicToggleButtonUI

---

#### protected void paintIcon​(
Graphics
g,

AbstractButton
b,

Rectangle
iconRect)

Paints an icon in the specified location.

**Parameters:**
- g

- an instance of

Graphics
- b

- an instance of

Button
- iconRect

- bounds of an icon

---

#### protected int getTextShiftOffset()

Overriden so that the text will not be rendered as shifted for
Toggle buttons and subclasses.

**Overrides:**
- getTextShiftOffset

in class

BasicButtonUI

**Returns:**
- the offset of the text

---

### Additional Sections

#### Class BasicToggleButtonUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.basic.BasicToggleButtonUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.basic.BasicToggleButtonUI

javax.swing.plaf.ButtonUI

- javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.basic.BasicToggleButtonUI

javax.swing.plaf.basic.BasicButtonUI

- javax.swing.plaf.basic.BasicToggleButtonUI

javax.swing.plaf.basic.BasicToggleButtonUI

**Direct Known Subclasses:** BasicRadioButtonUI

,

MetalToggleButtonUI

```java
public class
BasicToggleButtonUI

extends
BasicButtonUI
```

BasicToggleButton implementation

public class

BasicToggleButtonUI

extends

BasicButtonUI

BasicToggleButton implementation

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicButtonUI

defaultTextIconGap

,

defaultTextShiftOffset

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicToggleButtonUI

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

b)

Returns an instance of

BasicToggleButtonUI

.

protected int

getTextShiftOffset

()

Overriden so that the text will not be rendered as shifted for
Toggle buttons and subclasses.

protected void

paintIcon

​(

Graphics

g,

AbstractButton

b,

Rectangle

iconRect)

Paints an icon in the specified location.

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

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicButtonUI

defaultTextIconGap

,

defaultTextShiftOffset

---

#### Field Summary

Fields declared in class javax.swing.plaf.basic.

BasicButtonUI

defaultTextIconGap

,

defaultTextShiftOffset

---

#### Fields declared in class javax.swing.plaf.basic. BasicButtonUI

Constructor Summary

Constructors

Constructor

Description

BasicToggleButtonUI

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

b)

Returns an instance of

BasicToggleButtonUI

.

protected int

getTextShiftOffset

()

Overriden so that the text will not be rendered as shifted for
Toggle buttons and subclasses.

protected void

paintIcon

​(

Graphics

g,

AbstractButton

b,

Rectangle

iconRect)

Paints an icon in the specified location.

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

Returns an instance of

BasicToggleButtonUI

.

Overriden so that the text will not be rendered as shifted for
Toggle buttons and subclasses.

Paints an icon in the specified location.

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

- BasicToggleButtonUI

```java
public BasicToggleButtonUI()
```

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

Returns an instance of

BasicToggleButtonUI

.

**Parameters:** b

- a component
**Returns:** an instance of

BasicToggleButtonUI

- paintIcon

```java
protected void paintIcon​(
Graphics
g,

AbstractButton
b,

Rectangle
iconRect)
```

Paints an icon in the specified location.

**Parameters:** g

- an instance of

Graphics
**Parameters:** b

- an instance of

Button
**Parameters:** iconRect

- bounds of an icon

- getTextShiftOffset

```java
protected int getTextShiftOffset()
```

Overriden so that the text will not be rendered as shifted for
Toggle buttons and subclasses.

**Overrides:** getTextShiftOffset

in class

BasicButtonUI
**Returns:** the offset of the text

Constructor Detail

- BasicToggleButtonUI

```java
public BasicToggleButtonUI()
```

---

#### Constructor Detail

BasicToggleButtonUI

```java
public BasicToggleButtonUI()
```

---

#### BasicToggleButtonUI

public BasicToggleButtonUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Returns an instance of

BasicToggleButtonUI

.

**Parameters:** b

- a component
**Returns:** an instance of

BasicToggleButtonUI

- paintIcon

```java
protected void paintIcon​(
Graphics
g,

AbstractButton
b,

Rectangle
iconRect)
```

Paints an icon in the specified location.

**Parameters:** g

- an instance of

Graphics
**Parameters:** b

- an instance of

Button
**Parameters:** iconRect

- bounds of an icon

- getTextShiftOffset

```java
protected int getTextShiftOffset()
```

Overriden so that the text will not be rendered as shifted for
Toggle buttons and subclasses.

**Overrides:** getTextShiftOffset

in class

BasicButtonUI
**Returns:** the offset of the text

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

Returns an instance of

BasicToggleButtonUI

.

**Parameters:** b

- a component
**Returns:** an instance of

BasicToggleButtonUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

b)

Returns an instance of

BasicToggleButtonUI

.

paintIcon

```java
protected void paintIcon​(
Graphics
g,

AbstractButton
b,

Rectangle
iconRect)
```

Paints an icon in the specified location.

**Parameters:** g

- an instance of

Graphics
**Parameters:** b

- an instance of

Button
**Parameters:** iconRect

- bounds of an icon

---

#### paintIcon

protected void paintIcon​(

Graphics

g,

AbstractButton

b,

Rectangle

iconRect)

Paints an icon in the specified location.

getTextShiftOffset

```java
protected int getTextShiftOffset()
```

Overriden so that the text will not be rendered as shifted for
Toggle buttons and subclasses.

**Overrides:** getTextShiftOffset

in class

BasicButtonUI
**Returns:** the offset of the text

---

#### getTextShiftOffset

protected int getTextShiftOffset()

Overriden so that the text will not be rendered as shifted for
Toggle buttons and subclasses.

---

