# Class BasicMenuBarUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicMenuBarUI.html`

### Class Description

```java
public class
BasicMenuBarUI

extends
MenuBarUI
```

A default L&F implementation of MenuBarUI. This implementation
is a "combined" view/controller.

**Direct Known Subclasses:** MetalMenuBarUI

,

SynthMenuBarUI

---

### Field Details

#### protected
JMenuBar
menuBar

The instance of

JMenuBar

.

---

#### protected
ContainerListener
containerListener

The instance of

ContainerListener

.

---

#### protected
ChangeListener
changeListener

The instance of

ChangeListener

.

---

### Constructor Details

#### public BasicMenuBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Returns a new instance of

BasicMenuBarUI

.

**Parameters:**
- x

- a component

**Returns:**
- a new instance of

BasicMenuBarUI

---

#### protected void installDefaults()

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

#### protected
ContainerListener
createContainerListener()

Returns an instance of

ContainerListener

.

**Returns:**
- an instance of

ContainerListener

---

#### protected
ChangeListener
createChangeListener()

Returns an instance of

ChangeListener

.

**Returns:**
- an instance of

ChangeListener

---

### Additional Sections

#### Class BasicMenuBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.MenuBarUI
- - javax.swing.plaf.basic.BasicMenuBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.MenuBarUI
- - javax.swing.plaf.basic.BasicMenuBarUI

javax.swing.plaf.MenuBarUI

- javax.swing.plaf.basic.BasicMenuBarUI

javax.swing.plaf.basic.BasicMenuBarUI

**Direct Known Subclasses:** MetalMenuBarUI

,

SynthMenuBarUI

```java
public class
BasicMenuBarUI

extends
MenuBarUI
```

A default L&F implementation of MenuBarUI. This implementation
is a "combined" view/controller.

public class

BasicMenuBarUI

extends

MenuBarUI

A default L&F implementation of MenuBarUI. This implementation
is a "combined" view/controller.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeListener

changeListener

The instance of

ChangeListener

.

protected

ContainerListener

containerListener

The instance of

ContainerListener

.

protected

JMenuBar

menuBar

The instance of

JMenuBar

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicMenuBarUI

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

ChangeListener

createChangeListener

()

Returns an instance of

ChangeListener

.

protected

ContainerListener

createContainerListener

()

Returns an instance of

ContainerListener

.

static

ComponentUI

createUI

​(

JComponent

x)

Returns a new instance of

BasicMenuBarUI

.

protected void

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

ChangeListener

changeListener

The instance of

ChangeListener

.

protected

ContainerListener

containerListener

The instance of

ContainerListener

.

protected

JMenuBar

menuBar

The instance of

JMenuBar

.

---

#### Field Summary

The instance of

ChangeListener

.

The instance of

ContainerListener

.

The instance of

JMenuBar

.

Constructor Summary

Constructors

Constructor

Description

BasicMenuBarUI

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

ChangeListener

createChangeListener

()

Returns an instance of

ChangeListener

.

protected

ContainerListener

createContainerListener

()

Returns an instance of

ContainerListener

.

static

ComponentUI

createUI

​(

JComponent

x)

Returns a new instance of

BasicMenuBarUI

.

protected void

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

Returns an instance of

ChangeListener

.

Returns an instance of

ContainerListener

.

Returns a new instance of

BasicMenuBarUI

.

Installs default properties.

Registers keyboard actions.

Registers listeners.

Uninstalls default properties.

Unregisters keyboard actions.

Unregisters listeners.

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

- menuBar

```java
protected
JMenuBar
menuBar
```

The instance of

JMenuBar

.

- containerListener

```java
protected
ContainerListener
containerListener
```

The instance of

ContainerListener

.

- changeListener

```java
protected
ChangeListener
changeListener
```

The instance of

ChangeListener

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicMenuBarUI

```java
public BasicMenuBarUI()
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

Returns a new instance of

BasicMenuBarUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicMenuBarUI

- installDefaults

```java
protected void installDefaults()
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

- createContainerListener

```java
protected
ContainerListener
createContainerListener()
```

Returns an instance of

ContainerListener

.

**Returns:** an instance of

ContainerListener

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Returns an instance of

ChangeListener

.

**Returns:** an instance of

ChangeListener

Field Detail

- menuBar

```java
protected
JMenuBar
menuBar
```

The instance of

JMenuBar

.

- containerListener

```java
protected
ContainerListener
containerListener
```

The instance of

ContainerListener

.

- changeListener

```java
protected
ChangeListener
changeListener
```

The instance of

ChangeListener

.

---

#### Field Detail

menuBar

```java
protected
JMenuBar
menuBar
```

The instance of

JMenuBar

.

---

#### menuBar

protected

JMenuBar

menuBar

The instance of

JMenuBar

.

containerListener

```java
protected
ContainerListener
containerListener
```

The instance of

ContainerListener

.

---

#### containerListener

protected

ContainerListener

containerListener

The instance of

ContainerListener

.

changeListener

```java
protected
ChangeListener
changeListener
```

The instance of

ChangeListener

.

---

#### changeListener

protected

ChangeListener

changeListener

The instance of

ChangeListener

.

Constructor Detail

- BasicMenuBarUI

```java
public BasicMenuBarUI()
```

---

#### Constructor Detail

BasicMenuBarUI

```java
public BasicMenuBarUI()
```

---

#### BasicMenuBarUI

public BasicMenuBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Returns a new instance of

BasicMenuBarUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicMenuBarUI

- installDefaults

```java
protected void installDefaults()
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

- createContainerListener

```java
protected
ContainerListener
createContainerListener()
```

Returns an instance of

ContainerListener

.

**Returns:** an instance of

ContainerListener

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Returns an instance of

ChangeListener

.

**Returns:** an instance of

ChangeListener

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

Returns a new instance of

BasicMenuBarUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicMenuBarUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Returns a new instance of

BasicMenuBarUI

.

installDefaults

```java
protected void installDefaults()
```

Installs default properties.

---

#### installDefaults

protected void installDefaults()

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

createContainerListener

```java
protected
ContainerListener
createContainerListener()
```

Returns an instance of

ContainerListener

.

**Returns:** an instance of

ContainerListener

---

#### createContainerListener

protected

ContainerListener

createContainerListener()

Returns an instance of

ContainerListener

.

createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Returns an instance of

ChangeListener

.

**Returns:** an instance of

ChangeListener

---

#### createChangeListener

protected

ChangeListener

createChangeListener()

Returns an instance of

ChangeListener

.

---

