# Class SynthRadioButtonUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthRadioButtonUI.html`

### Class Description

```java
public class
SynthRadioButtonUI

extends
SynthToggleButtonUI
```

Provides the Synth L&F UI delegate for

JRadioButton

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

#### public SynthRadioButtonUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
b)

Creates a new UI object for the given component.

**Parameters:**
- b

- component to create UI object for

**Returns:**
- the UI object

---

#### protected
Icon
getSizingIcon​(
AbstractButton
b)

Returns the Icon used in calculating the
preferred/minimum/maximum size.

**Overrides:**
- getSizingIcon

in class

SynthButtonUI

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

#### Class SynthRadioButtonUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.synth.SynthButtonUI
- - javax.swing.plaf.synth.SynthToggleButtonUI
- - javax.swing.plaf.synth.SynthRadioButtonUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.synth.SynthButtonUI
- - javax.swing.plaf.synth.SynthToggleButtonUI
- - javax.swing.plaf.synth.SynthRadioButtonUI

javax.swing.plaf.ButtonUI

- javax.swing.plaf.basic.BasicButtonUI
- - javax.swing.plaf.synth.SynthButtonUI
- - javax.swing.plaf.synth.SynthToggleButtonUI
- - javax.swing.plaf.synth.SynthRadioButtonUI

javax.swing.plaf.basic.BasicButtonUI

- javax.swing.plaf.synth.SynthButtonUI
- - javax.swing.plaf.synth.SynthToggleButtonUI
- - javax.swing.plaf.synth.SynthRadioButtonUI

javax.swing.plaf.synth.SynthButtonUI

- javax.swing.plaf.synth.SynthToggleButtonUI
- - javax.swing.plaf.synth.SynthRadioButtonUI

javax.swing.plaf.synth.SynthToggleButtonUI

- javax.swing.plaf.synth.SynthRadioButtonUI

javax.swing.plaf.synth.SynthRadioButtonUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

**Direct Known Subclasses:** SynthCheckBoxUI

```java
public class
SynthRadioButtonUI

extends
SynthToggleButtonUI
```

Provides the Synth L&F UI delegate for

JRadioButton

.

**Since:** 1.7

public class

SynthRadioButtonUI

extends

SynthToggleButtonUI

Provides the Synth L&F UI delegate for

JRadioButton

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

SynthRadioButtonUI

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

Creates a new UI object for the given component.

protected

Icon

getSizingIcon

​(

AbstractButton

b)

Returns the Icon used in calculating the
preferred/minimum/maximum size.

- Methods declared in class javax.swing.plaf.synth.

SynthButtonUI

getDefaultIcon

,

getIcon

,

paint

,

paint

,

update

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

SynthRadioButtonUI

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

Creates a new UI object for the given component.

protected

Icon

getSizingIcon

​(

AbstractButton

b)

Returns the Icon used in calculating the
preferred/minimum/maximum size.

- Methods declared in class javax.swing.plaf.synth.

SynthButtonUI

getDefaultIcon

,

getIcon

,

paint

,

paint

,

update

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

Returns the Icon used in calculating the
preferred/minimum/maximum size.

Methods declared in class javax.swing.plaf.synth.

SynthButtonUI

getDefaultIcon

,

getIcon

,

paint

,

paint

,

update

---

#### Methods declared in class javax.swing.plaf.synth. SynthButtonUI

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

- SynthRadioButtonUI

```java
public SynthRadioButtonUI()
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

Creates a new UI object for the given component.

**Parameters:** b

- component to create UI object for
**Returns:** the UI object

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

**Overrides:** getSizingIcon

in class

SynthButtonUI
**Parameters:** b

- specifies the

AbstractButton

used when calculating the preferred/minimum/maximum
size.
**Returns:** the Icon used in calculating the
preferred/minimum/maximum size.

Constructor Detail

- SynthRadioButtonUI

```java
public SynthRadioButtonUI()
```

---

#### Constructor Detail

SynthRadioButtonUI

```java
public SynthRadioButtonUI()
```

---

#### SynthRadioButtonUI

public SynthRadioButtonUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Creates a new UI object for the given component.

**Parameters:** b

- component to create UI object for
**Returns:** the UI object

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

**Overrides:** getSizingIcon

in class

SynthButtonUI
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
b)
```

Creates a new UI object for the given component.

**Parameters:** b

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

b)

Creates a new UI object for the given component.

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

**Overrides:** getSizingIcon

in class

SynthButtonUI
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

