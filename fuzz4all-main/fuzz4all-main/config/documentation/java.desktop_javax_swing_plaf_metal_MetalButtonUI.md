# Class MetalButtonUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalButtonUI.html`

### Class Description

```java
public class
MetalButtonUI

extends
BasicButtonUI
```

MetalButtonUI implementation

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

The color of the focused button.

---

#### protected
Color
selectColor

The color of the selected button.

---

#### protected
Color
disabledTextColor

The color of the disabled color.

---

### Constructor Details

#### public MetalButtonUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns an instance of

MetalButtonUI

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

MetalButtonUI

---

#### protected
Color
getSelectColor()

Returns the color of the selected button.

**Returns:**
- the color of the selected button

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

Returns the color of the focused button.

**Returns:**
- the color of the focused button

---

#### public void update​(
Graphics
g,

JComponent
c)

If necessary paints the background of the component, then
invokes

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

### Additional Sections

#### Class MetalButtonUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.metal.MetalButtonUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.metal.MetalButtonUI

javax.swing.plaf.ButtonUI

- javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.metal.MetalButtonUI

javax.swing.plaf.basic.BasicButtonUI

- javax.swing.plaf.metal.MetalButtonUI

javax.swing.plaf.metal.MetalButtonUI

```java
public class
MetalButtonUI

extends
BasicButtonUI
```

MetalButtonUI implementation

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

MetalButtonUI

extends

BasicButtonUI

MetalButtonUI implementation

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

The color of the disabled color.

protected

Color

focusColor

The color of the focused button.

protected

Color

selectColor

The color of the selected button.

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

MetalButtonUI

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

Returns an instance of

MetalButtonUI

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

Returns the color of the focused button.

protected

Color

getSelectColor

()

Returns the color of the selected button.

void

update

​(

Graphics

g,

JComponent

c)

If necessary paints the background of the component, then
invokes

paint

.

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

The color of the disabled color.

protected

Color

focusColor

The color of the focused button.

protected

Color

selectColor

The color of the selected button.

- Fields declared in class javax.swing.plaf.basic.

BasicButtonUI

defaultTextIconGap

,

defaultTextShiftOffset

---

#### Field Summary

The color of the disabled color.

The color of the focused button.

The color of the selected button.

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

MetalButtonUI

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

Returns an instance of

MetalButtonUI

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

Returns the color of the focused button.

protected

Color

getSelectColor

()

Returns the color of the selected button.

void

update

​(

Graphics

g,

JComponent

c)

If necessary paints the background of the component, then
invokes

paint

.

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

Returns an instance of

MetalButtonUI

.

Returns the color of a disabled text.

Returns the color of the focused button.

Returns the color of the selected button.

If necessary paints the background of the component, then
invokes

paint

.

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

The color of the focused button.

- selectColor

```java
protected
Color
selectColor
```

The color of the selected button.

- disabledTextColor

```java
protected
Color
disabledTextColor
```

The color of the disabled color.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalButtonUI

```java
public MetalButtonUI()
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

Returns an instance of

MetalButtonUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalButtonUI

- getSelectColor

```java
protected
Color
getSelectColor()
```

Returns the color of the selected button.

**Returns:** the color of the selected button

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

Returns the color of the focused button.

**Returns:** the color of the focused button

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

If necessary paints the background of the component, then
invokes

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

Field Detail

- focusColor

```java
protected
Color
focusColor
```

The color of the focused button.

- selectColor

```java
protected
Color
selectColor
```

The color of the selected button.

- disabledTextColor

```java
protected
Color
disabledTextColor
```

The color of the disabled color.

---

#### Field Detail

focusColor

```java
protected
Color
focusColor
```

The color of the focused button.

---

#### focusColor

protected

Color

focusColor

The color of the focused button.

selectColor

```java
protected
Color
selectColor
```

The color of the selected button.

---

#### selectColor

protected

Color

selectColor

The color of the selected button.

disabledTextColor

```java
protected
Color
disabledTextColor
```

The color of the disabled color.

---

#### disabledTextColor

protected

Color

disabledTextColor

The color of the disabled color.

Constructor Detail

- MetalButtonUI

```java
public MetalButtonUI()
```

---

#### Constructor Detail

MetalButtonUI

```java
public MetalButtonUI()
```

---

#### MetalButtonUI

public MetalButtonUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of

MetalButtonUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalButtonUI

- getSelectColor

```java
protected
Color
getSelectColor()
```

Returns the color of the selected button.

**Returns:** the color of the selected button

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

Returns the color of the focused button.

**Returns:** the color of the focused button

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

If necessary paints the background of the component, then
invokes

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

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of

MetalButtonUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalButtonUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns an instance of

MetalButtonUI

.

getSelectColor

```java
protected
Color
getSelectColor()
```

Returns the color of the selected button.

**Returns:** the color of the selected button

---

#### getSelectColor

protected

Color

getSelectColor()

Returns the color of the selected button.

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

Returns the color of the focused button.

**Returns:** the color of the focused button

---

#### getFocusColor

protected

Color

getFocusColor()

Returns the color of the focused button.

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

If necessary paints the background of the component, then
invokes

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

If necessary paints the background of the component, then
invokes

paint

.

---

