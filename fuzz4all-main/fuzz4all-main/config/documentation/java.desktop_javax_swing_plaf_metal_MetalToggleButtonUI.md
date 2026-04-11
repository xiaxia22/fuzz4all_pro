# Class MetalToggleButtonUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalToggleButtonUI.html`

### Class Description

```java
public class
MetalToggleButtonUI

extends
BasicToggleButtonUI
```

MetalToggleButton implementation

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

#### protected
Color
focusColor

The color of a focused toggle button.

---

#### protected
Color
selectColor

The color of a selected button.

---

#### protected
Color
disabledTextColor

The color of a disabled text.

---

### Constructor Details

#### public MetalToggleButtonUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
b)

Constructs the

MetalToogleButtonUI

.

**Parameters:**
- b

- a component

**Returns:**
- the

MetalToogleButtonUI

.

---

#### protected
Color
getSelectColor()

Returns the color of a selected button.

**Returns:**
- the color of a selected button

---

#### protected
Color
getDisabledTextColor()

Returns the color of a disabled text.

**Returns:**
- the color of a disabled text

---

#### protected
Color
getFocusColor()

Returns the color of a focused toggle button.

**Returns:**
- the color of a focused toggle button

---

#### public void update​(
Graphics
g,

JComponent
c)

If necessary paints the background of the component, then invokes

paint

.

**Overrides:**
- update

in class

ComponentUI

**Parameters:**
- g

- Graphics to paint to
- c

- JComponent painting on

**Throws:**
- NullPointerException

- if

g

or

c

is
null

**See Also:**
- ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

,

ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

**Since:**
- 1.5

---

#### protected void paintIcon​(
Graphics
g,

AbstractButton
b,

Rectangle
iconRect)

Paints the appropriate icon of the button

b

in the
space

iconRect

.

**Overrides:**
- paintIcon

in class

BasicToggleButtonUI

**Parameters:**
- g

- Graphics to paint to
- b

- Button to render for
- iconRect

- space to render in

**Throws:**
- NullPointerException

- if any of the arguments are null.

**Since:**
- 1.5

---

### Additional Sections

#### Class MetalToggleButtonUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.basic.BasicToggleButtonUI
- - javax.swing.plaf.metal.MetalToggleButtonUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.basic.BasicToggleButtonUI
- - javax.swing.plaf.metal.MetalToggleButtonUI

javax.swing.plaf.ButtonUI

- javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.basic.BasicToggleButtonUI
- - javax.swing.plaf.metal.MetalToggleButtonUI

javax.swing.plaf.basic.BasicButtonUI

- javax.swing.plaf.basic.BasicToggleButtonUI
- - javax.swing.plaf.metal.MetalToggleButtonUI

javax.swing.plaf.basic.BasicToggleButtonUI

- javax.swing.plaf.metal.MetalToggleButtonUI

javax.swing.plaf.metal.MetalToggleButtonUI

```java
public class
MetalToggleButtonUI

extends
BasicToggleButtonUI
```

MetalToggleButton implementation

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

MetalToggleButtonUI

extends

BasicToggleButtonUI

MetalToggleButton implementation

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

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Color

disabledTextColor

The color of a disabled text.

protected

Color

focusColor

The color of a focused toggle button.

protected

Color

selectColor

The color of a selected button.

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

MetalToggleButtonUI

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

Constructs the

MetalToogleButtonUI

.

protected

Color

getDisabledTextColor

()

Returns the color of a disabled text.

protected

Color

getFocusColor

()

Returns the color of a focused toggle button.

protected

Color

getSelectColor

()

Returns the color of a selected button.

protected void

paintIcon

​(

Graphics

g,

AbstractButton

b,

Rectangle

iconRect)

Paints the appropriate icon of the button

b

in the
space

iconRect

.

void

update

​(

Graphics

g,

JComponent

c)

If necessary paints the background of the component, then invokes

paint

.

- Methods declared in class javax.swing.plaf.basic.

BasicToggleButtonUI

getTextShiftOffset

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

Fields

Modifier and Type

Field

Description

protected

Color

disabledTextColor

The color of a disabled text.

protected

Color

focusColor

The color of a focused toggle button.

protected

Color

selectColor

The color of a selected button.

- Fields declared in class javax.swing.plaf.basic.

BasicButtonUI

defaultTextIconGap

,

defaultTextShiftOffset

---

#### Field Summary

The color of a disabled text.

The color of a focused toggle button.

The color of a selected button.

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

MetalToggleButtonUI

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

Constructs the

MetalToogleButtonUI

.

protected

Color

getDisabledTextColor

()

Returns the color of a disabled text.

protected

Color

getFocusColor

()

Returns the color of a focused toggle button.

protected

Color

getSelectColor

()

Returns the color of a selected button.

protected void

paintIcon

​(

Graphics

g,

AbstractButton

b,

Rectangle

iconRect)

Paints the appropriate icon of the button

b

in the
space

iconRect

.

void

update

​(

Graphics

g,

JComponent

c)

If necessary paints the background of the component, then invokes

paint

.

- Methods declared in class javax.swing.plaf.basic.

BasicToggleButtonUI

getTextShiftOffset

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

Constructs the

MetalToogleButtonUI

.

Returns the color of a disabled text.

Returns the color of a focused toggle button.

Returns the color of a selected button.

Paints the appropriate icon of the button

b

in the
space

iconRect

.

If necessary paints the background of the component, then invokes

paint

.

Methods declared in class javax.swing.plaf.basic.

BasicToggleButtonUI

getTextShiftOffset

---

#### Methods declared in class javax.swing.plaf.basic. BasicToggleButtonUI

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

============ FIELD DETAIL ===========

- Field Detail

- focusColor

```java
protected
Color
focusColor
```

The color of a focused toggle button.

- selectColor

```java
protected
Color
selectColor
```

The color of a selected button.

- disabledTextColor

```java
protected
Color
disabledTextColor
```

The color of a disabled text.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalToggleButtonUI

```java
public MetalToggleButtonUI()
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

Constructs the

MetalToogleButtonUI

.

**Parameters:** b

- a component
**Returns:** the

MetalToogleButtonUI

.

- getSelectColor

```java
protected
Color
getSelectColor()
```

Returns the color of a selected button.

**Returns:** the color of a selected button

- getDisabledTextColor

```java
protected
Color
getDisabledTextColor()
```

Returns the color of a disabled text.

**Returns:** the color of a disabled text

- getFocusColor

```java
protected
Color
getFocusColor()
```

Returns the color of a focused toggle button.

**Returns:** the color of a focused toggle button

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

If necessary paints the background of the component, then invokes

paint

.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- Graphics to paint to
**Parameters:** c

- JComponent painting on
**Throws:** NullPointerException

- if

g

or

c

is
null
**Since:** 1.5
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

,

ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

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

Paints the appropriate icon of the button

b

in the
space

iconRect

.

**Overrides:** paintIcon

in class

BasicToggleButtonUI
**Parameters:** g

- Graphics to paint to
**Parameters:** b

- Button to render for
**Parameters:** iconRect

- space to render in
**Throws:** NullPointerException

- if any of the arguments are null.
**Since:** 1.5

Field Detail

- focusColor

```java
protected
Color
focusColor
```

The color of a focused toggle button.

- selectColor

```java
protected
Color
selectColor
```

The color of a selected button.

- disabledTextColor

```java
protected
Color
disabledTextColor
```

The color of a disabled text.

---

#### Field Detail

focusColor

```java
protected
Color
focusColor
```

The color of a focused toggle button.

---

#### focusColor

protected

Color

focusColor

The color of a focused toggle button.

selectColor

```java
protected
Color
selectColor
```

The color of a selected button.

---

#### selectColor

protected

Color

selectColor

The color of a selected button.

disabledTextColor

```java
protected
Color
disabledTextColor
```

The color of a disabled text.

---

#### disabledTextColor

protected

Color

disabledTextColor

The color of a disabled text.

Constructor Detail

- MetalToggleButtonUI

```java
public MetalToggleButtonUI()
```

---

#### Constructor Detail

MetalToggleButtonUI

```java
public MetalToggleButtonUI()
```

---

#### MetalToggleButtonUI

public MetalToggleButtonUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Constructs the

MetalToogleButtonUI

.

**Parameters:** b

- a component
**Returns:** the

MetalToogleButtonUI

.

- getSelectColor

```java
protected
Color
getSelectColor()
```

Returns the color of a selected button.

**Returns:** the color of a selected button

- getDisabledTextColor

```java
protected
Color
getDisabledTextColor()
```

Returns the color of a disabled text.

**Returns:** the color of a disabled text

- getFocusColor

```java
protected
Color
getFocusColor()
```

Returns the color of a focused toggle button.

**Returns:** the color of a focused toggle button

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

If necessary paints the background of the component, then invokes

paint

.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- Graphics to paint to
**Parameters:** c

- JComponent painting on
**Throws:** NullPointerException

- if

g

or

c

is
null
**Since:** 1.5
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

,

ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

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

Paints the appropriate icon of the button

b

in the
space

iconRect

.

**Overrides:** paintIcon

in class

BasicToggleButtonUI
**Parameters:** g

- Graphics to paint to
**Parameters:** b

- Button to render for
**Parameters:** iconRect

- space to render in
**Throws:** NullPointerException

- if any of the arguments are null.
**Since:** 1.5

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

Constructs the

MetalToogleButtonUI

.

**Parameters:** b

- a component
**Returns:** the

MetalToogleButtonUI

.

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

b)

Constructs the

MetalToogleButtonUI

.

getSelectColor

```java
protected
Color
getSelectColor()
```

Returns the color of a selected button.

**Returns:** the color of a selected button

---

#### getSelectColor

protected

Color

getSelectColor()

Returns the color of a selected button.

getDisabledTextColor

```java
protected
Color
getDisabledTextColor()
```

Returns the color of a disabled text.

**Returns:** the color of a disabled text

---

#### getDisabledTextColor

protected

Color

getDisabledTextColor()

Returns the color of a disabled text.

getFocusColor

```java
protected
Color
getFocusColor()
```

Returns the color of a focused toggle button.

**Returns:** the color of a focused toggle button

---

#### getFocusColor

protected

Color

getFocusColor()

Returns the color of a focused toggle button.

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

If necessary paints the background of the component, then invokes

paint

.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- Graphics to paint to
**Parameters:** c

- JComponent painting on
**Throws:** NullPointerException

- if

g

or

c

is
null
**Since:** 1.5
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

,

ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

---

#### update

public void update​(

Graphics

g,

JComponent

c)

If necessary paints the background of the component, then invokes

paint

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

Paints the appropriate icon of the button

b

in the
space

iconRect

.

**Overrides:** paintIcon

in class

BasicToggleButtonUI
**Parameters:** g

- Graphics to paint to
**Parameters:** b

- Button to render for
**Parameters:** iconRect

- space to render in
**Throws:** NullPointerException

- if any of the arguments are null.
**Since:** 1.5

---

#### paintIcon

protected void paintIcon​(

Graphics

g,

AbstractButton

b,

Rectangle

iconRect)

Paints the appropriate icon of the button

b

in the
space

iconRect

.

---

