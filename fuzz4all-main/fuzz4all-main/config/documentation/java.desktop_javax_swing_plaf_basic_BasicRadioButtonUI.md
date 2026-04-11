# Class BasicRadioButtonUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicRadioButtonUI.html`

### Class Description

```java
public class
BasicRadioButtonUI

extends
BasicToggleButtonUI
```

RadioButtonUI implementation for BasicRadioButtonUI

**Direct Known Subclasses:** BasicCheckBoxUI

,

MetalRadioButtonUI

---

### Field Details

#### protected
Icon
icon

The icon.

---

### Constructor Details

#### public BasicRadioButtonUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
b)

Returns an instance of

BasicRadioButtonUI

.

**Parameters:**
- b

- a component

**Returns:**
- an instance of

BasicRadioButtonUI

---

#### public
Icon
getDefaultIcon()

Returns the default icon.

**Returns:**
- the default icon

---

#### public void paint​(
Graphics
g,

JComponent
c)

paint the radio button

**Overrides:**
- paint

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

context in which to paint
- c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

---

#### protected void paintFocus​(
Graphics
g,

Rectangle
textRect,

Dimension
size)

Paints focused radio button.

**Parameters:**
- g

- an instance of

Graphics
- textRect

- bounds
- size

- the size of radio button

---

#### public
Dimension
getPreferredSize​(
JComponent
c)

The preferred size of the radio button

**Overrides:**
- getPreferredSize

in class

ComponentUI

**Parameters:**
- c

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object containing given component's preferred
size appropriate for the look and feel

**See Also:**
- JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

### Additional Sections

#### Class BasicRadioButtonUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.basic.BasicToggleButtonUI
- - javax.swing.plaf.basic.BasicRadioButtonUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.basic.BasicToggleButtonUI
- - javax.swing.plaf.basic.BasicRadioButtonUI

javax.swing.plaf.ButtonUI

- javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.basic.BasicToggleButtonUI
- - javax.swing.plaf.basic.BasicRadioButtonUI

javax.swing.plaf.basic.BasicButtonUI

- javax.swing.plaf.basic.BasicToggleButtonUI
- - javax.swing.plaf.basic.BasicRadioButtonUI

javax.swing.plaf.basic.BasicToggleButtonUI

- javax.swing.plaf.basic.BasicRadioButtonUI

javax.swing.plaf.basic.BasicRadioButtonUI

**Direct Known Subclasses:** BasicCheckBoxUI

,

MetalRadioButtonUI

```java
public class
BasicRadioButtonUI

extends
BasicToggleButtonUI
```

RadioButtonUI implementation for BasicRadioButtonUI

public class

BasicRadioButtonUI

extends

BasicToggleButtonUI

RadioButtonUI implementation for BasicRadioButtonUI

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Icon

icon

The icon.

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

BasicRadioButtonUI

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

BasicRadioButtonUI

.

Icon

getDefaultIcon

()

Returns the default icon.

Dimension

getPreferredSize

​(

JComponent

c)

The preferred size of the radio button

void

paint

​(

Graphics

g,

JComponent

c)

paint the radio button

protected void

paintFocus

​(

Graphics

g,

Rectangle

textRect,

Dimension

size)

Paints focused radio button.

- Methods declared in class javax.swing.plaf.basic.

BasicToggleButtonUI

getTextShiftOffset

,

paintIcon

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

installUI

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

Fields

Modifier and Type

Field

Description

protected

Icon

icon

The icon.

- Fields declared in class javax.swing.plaf.basic.

BasicButtonUI

defaultTextIconGap

,

defaultTextShiftOffset

---

#### Field Summary

The icon.

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

BasicRadioButtonUI

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

BasicRadioButtonUI

.

Icon

getDefaultIcon

()

Returns the default icon.

Dimension

getPreferredSize

​(

JComponent

c)

The preferred size of the radio button

void

paint

​(

Graphics

g,

JComponent

c)

paint the radio button

protected void

paintFocus

​(

Graphics

g,

Rectangle

textRect,

Dimension

size)

Paints focused radio button.

- Methods declared in class javax.swing.plaf.basic.

BasicToggleButtonUI

getTextShiftOffset

,

paintIcon

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

installUI

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

BasicRadioButtonUI

.

Returns the default icon.

The preferred size of the radio button

paint the radio button

Paints focused radio button.

Methods declared in class javax.swing.plaf.basic.

BasicToggleButtonUI

getTextShiftOffset

,

paintIcon

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

installUI

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

============ FIELD DETAIL ===========

- Field Detail

- icon

```java
protected
Icon
icon
```

The icon.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicRadioButtonUI

```java
public BasicRadioButtonUI()
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

BasicRadioButtonUI

.

**Parameters:** b

- a component
**Returns:** an instance of

BasicRadioButtonUI

- getDefaultIcon

```java
public
Icon
getDefaultIcon()
```

Returns the default icon.

**Returns:** the default icon

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

paint the radio button

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

- paintFocus

```java
protected void paintFocus​(
Graphics
g,

Rectangle
textRect,

Dimension
size)
```

Paints focused radio button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** textRect

- bounds
**Parameters:** size

- the size of radio button

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

The preferred size of the radio button

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object containing given component's preferred
size appropriate for the look and feel
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

Field Detail

- icon

```java
protected
Icon
icon
```

The icon.

---

#### Field Detail

icon

```java
protected
Icon
icon
```

The icon.

---

#### icon

protected

Icon

icon

The icon.

Constructor Detail

- BasicRadioButtonUI

```java
public BasicRadioButtonUI()
```

---

#### Constructor Detail

BasicRadioButtonUI

```java
public BasicRadioButtonUI()
```

---

#### BasicRadioButtonUI

public BasicRadioButtonUI()

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

BasicRadioButtonUI

.

**Parameters:** b

- a component
**Returns:** an instance of

BasicRadioButtonUI

- getDefaultIcon

```java
public
Icon
getDefaultIcon()
```

Returns the default icon.

**Returns:** the default icon

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

paint the radio button

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

- paintFocus

```java
protected void paintFocus​(
Graphics
g,

Rectangle
textRect,

Dimension
size)
```

Paints focused radio button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** textRect

- bounds
**Parameters:** size

- the size of radio button

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

The preferred size of the radio button

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object containing given component's preferred
size appropriate for the look and feel
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

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

BasicRadioButtonUI

.

**Parameters:** b

- a component
**Returns:** an instance of

BasicRadioButtonUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

b)

Returns an instance of

BasicRadioButtonUI

.

getDefaultIcon

```java
public
Icon
getDefaultIcon()
```

Returns the default icon.

**Returns:** the default icon

---

#### getDefaultIcon

public

Icon

getDefaultIcon()

Returns the default icon.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

paint the radio button

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

paint the radio button

paintFocus

```java
protected void paintFocus​(
Graphics
g,

Rectangle
textRect,

Dimension
size)
```

Paints focused radio button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** textRect

- bounds
**Parameters:** size

- the size of radio button

---

#### paintFocus

protected void paintFocus​(

Graphics

g,

Rectangle

textRect,

Dimension

size)

Paints focused radio button.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

The preferred size of the radio button

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object containing given component's preferred
size appropriate for the look and feel
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### getPreferredSize

public

Dimension

getPreferredSize​(

JComponent

c)

The preferred size of the radio button

---

