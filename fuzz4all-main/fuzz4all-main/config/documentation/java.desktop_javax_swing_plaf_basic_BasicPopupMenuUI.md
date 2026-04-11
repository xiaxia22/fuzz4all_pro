# Class BasicPopupMenuUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicPopupMenuUI.html`

### Class Description

```java
public class
BasicPopupMenuUI

extends
PopupMenuUI
```

A Windows L&F implementation of PopupMenuUI. This implementation
is a "combined" view/controller.

**Direct Known Subclasses:** SynthPopupMenuUI

---

### Field Details

#### protected
JPopupMenu
popupMenu

The instance of

JPopupMenu

.

---

### Constructor Details

#### public BasicPopupMenuUI()

Constructs a new instance of

BasicPopupMenuUI

.

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Constructs a new instance of

BasicPopupMenuUI

.

**Parameters:**
- x

- a component

**Returns:**
- a new instance of

BasicPopupMenuUI

---

#### public void installDefaults()

Installs default properties.

---

#### protected void installListeners()

Registers listeners.

---

#### protected void installKeyboardActions()

Registers keyboard actions.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected void uninstallListeners()

Unregisters listeners.

---

#### protected void uninstallKeyboardActions()

Unregisters keyboard actions.

---

### Additional Sections

#### Class BasicPopupMenuUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.PopupMenuUI
- - javax.swing.plaf.basic.BasicPopupMenuUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.PopupMenuUI
- - javax.swing.plaf.basic.BasicPopupMenuUI

javax.swing.plaf.PopupMenuUI

- javax.swing.plaf.basic.BasicPopupMenuUI

javax.swing.plaf.basic.BasicPopupMenuUI

**Direct Known Subclasses:** SynthPopupMenuUI

```java
public class
BasicPopupMenuUI

extends
PopupMenuUI
```

A Windows L&F implementation of PopupMenuUI. This implementation
is a "combined" view/controller.

public class

BasicPopupMenuUI

extends

PopupMenuUI

A Windows L&F implementation of PopupMenuUI. This implementation
is a "combined" view/controller.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JPopupMenu

popupMenu

The instance of

JPopupMenu

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicPopupMenuUI

()

Constructs a new instance of

BasicPopupMenuUI

.

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

x)

Constructs a new instance of

BasicPopupMenuUI

.

void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListeners

()

Registers listeners.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

PopupMenuUI

getPopup

,

isPopupTrigger

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

Fields

Modifier and Type

Field

Description

protected

JPopupMenu

popupMenu

The instance of

JPopupMenu

.

---

#### Field Summary

The instance of

JPopupMenu

.

Constructor Summary

Constructors

Constructor

Description

BasicPopupMenuUI

()

Constructs a new instance of

BasicPopupMenuUI

.

---

#### Constructor Summary

Constructs a new instance of

BasicPopupMenuUI

.

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

x)

Constructs a new instance of

BasicPopupMenuUI

.

void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListeners

()

Registers listeners.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

PopupMenuUI

getPopup

,

isPopupTrigger

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

Constructs a new instance of

BasicPopupMenuUI

.

Installs default properties.

Registers keyboard actions.

Registers listeners.

Uninstalls default properties.

Unregisters keyboard actions.

Unregisters listeners.

Methods declared in class javax.swing.plaf.

PopupMenuUI

getPopup

,

isPopupTrigger

---

#### Methods declared in class javax.swing.plaf. PopupMenuUI

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

============ FIELD DETAIL ===========

- Field Detail

- popupMenu

```java
protected
JPopupMenu
popupMenu
```

The instance of

JPopupMenu

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicPopupMenuUI

```java
public BasicPopupMenuUI()
```

Constructs a new instance of

BasicPopupMenuUI

.

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

Constructs a new instance of

BasicPopupMenuUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicPopupMenuUI

- installDefaults

```java
public void installDefaults()
```

Installs default properties.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

Field Detail

- popupMenu

```java
protected
JPopupMenu
popupMenu
```

The instance of

JPopupMenu

.

---

#### Field Detail

popupMenu

```java
protected
JPopupMenu
popupMenu
```

The instance of

JPopupMenu

.

---

#### popupMenu

protected

JPopupMenu

popupMenu

The instance of

JPopupMenu

.

Constructor Detail

- BasicPopupMenuUI

```java
public BasicPopupMenuUI()
```

Constructs a new instance of

BasicPopupMenuUI

.

---

#### Constructor Detail

BasicPopupMenuUI

```java
public BasicPopupMenuUI()
```

Constructs a new instance of

BasicPopupMenuUI

.

---

#### BasicPopupMenuUI

public BasicPopupMenuUI()

Constructs a new instance of

BasicPopupMenuUI

.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Constructs a new instance of

BasicPopupMenuUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicPopupMenuUI

- installDefaults

```java
public void installDefaults()
```

Installs default properties.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

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

Constructs a new instance of

BasicPopupMenuUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicPopupMenuUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Constructs a new instance of

BasicPopupMenuUI

.

installDefaults

```java
public void installDefaults()
```

Installs default properties.

---

#### installDefaults

public void installDefaults()

Installs default properties.

installListeners

```java
protected void installListeners()
```

Registers listeners.

---

#### installListeners

protected void installListeners()

Registers listeners.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

---

#### installKeyboardActions

protected void installKeyboardActions()

Registers keyboard actions.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Unregisters listeners.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters keyboard actions.

---

