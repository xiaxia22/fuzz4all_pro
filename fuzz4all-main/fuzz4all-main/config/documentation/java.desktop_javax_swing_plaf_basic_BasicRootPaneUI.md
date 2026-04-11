# Class BasicRootPaneUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicRootPaneUI.html`

### Class Description

```java
public class
BasicRootPaneUI

extends
RootPaneUI

implements
PropertyChangeListener
```

Basic implementation of RootPaneUI, there is one shared between all
JRootPane instances.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicRootPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns a new instance of

BasicRootPaneUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

BasicRootPaneUI

---

#### protected void installDefaults​(
JRootPane
c)

Installs default properties.

**Parameters:**
- c

- an instance of

JRootPane

---

#### protected void installComponents​(
JRootPane
root)

Installs components.

**Parameters:**
- root

- an instance of

JRootPane

---

#### protected void installListeners​(
JRootPane
root)

Registers listeners.

**Parameters:**
- root

- an instance of

JRootPane

---

#### protected void installKeyboardActions​(
JRootPane
root)

Registers keyboard actions.

**Parameters:**
- root

- an instance of

JRootPane

---

#### protected void uninstallDefaults​(
JRootPane
root)

Uninstalls default properties.

**Parameters:**
- root

- an instance of

JRootPane

---

#### protected void uninstallComponents​(
JRootPane
root)

Unregisters components.

**Parameters:**
- root

- an instance of

JRootPane

---

#### protected void uninstallListeners​(
JRootPane
root)

Unregisters listeners.

**Parameters:**
- root

- an instance of

JRootPane

---

#### protected void uninstallKeyboardActions​(
JRootPane
root)

Unregisters keyboard actions.

**Parameters:**
- root

- an instance of

JRootPane

---

#### public void propertyChange​(
PropertyChangeEvent
e)

Invoked when a property changes on the root pane. If the event
indicates the

defaultButton

has changed, this will
reinstall the keyboard actions.

**Specified by:**
- propertyChange

in interface

PropertyChangeListener

**Parameters:**
- e

- A PropertyChangeEvent object describing the event source
and the property that has changed.

---

### Additional Sections

#### Class BasicRootPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.RootPaneUI
- - javax.swing.plaf.basic.BasicRootPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.RootPaneUI
- - javax.swing.plaf.basic.BasicRootPaneUI

javax.swing.plaf.RootPaneUI

- javax.swing.plaf.basic.BasicRootPaneUI

javax.swing.plaf.basic.BasicRootPaneUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

**Direct Known Subclasses:** MetalRootPaneUI

,

SynthRootPaneUI

```java
public class
BasicRootPaneUI

extends
RootPaneUI

implements
PropertyChangeListener
```

Basic implementation of RootPaneUI, there is one shared between all
JRootPane instances.

**Since:** 1.3

public class

BasicRootPaneUI

extends

RootPaneUI

implements

PropertyChangeListener

Basic implementation of RootPaneUI, there is one shared between all
JRootPane instances.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicRootPaneUI

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

Returns a new instance of

BasicRootPaneUI

.

protected void

installComponents

​(

JRootPane

root)

Installs components.

protected void

installDefaults

​(

JRootPane

c)

Installs default properties.

protected void

installKeyboardActions

​(

JRootPane

root)

Registers keyboard actions.

protected void

installListeners

​(

JRootPane

root)

Registers listeners.

void

propertyChange

​(

PropertyChangeEvent

e)

Invoked when a property changes on the root pane.

protected void

uninstallComponents

​(

JRootPane

root)

Unregisters components.

protected void

uninstallDefaults

​(

JRootPane

root)

Uninstalls default properties.

protected void

uninstallKeyboardActions

​(

JRootPane

root)

Unregisters keyboard actions.

protected void

uninstallListeners

​(

JRootPane

root)

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

Constructor Summary

Constructors

Constructor

Description

BasicRootPaneUI

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

Returns a new instance of

BasicRootPaneUI

.

protected void

installComponents

​(

JRootPane

root)

Installs components.

protected void

installDefaults

​(

JRootPane

c)

Installs default properties.

protected void

installKeyboardActions

​(

JRootPane

root)

Registers keyboard actions.

protected void

installListeners

​(

JRootPane

root)

Registers listeners.

void

propertyChange

​(

PropertyChangeEvent

e)

Invoked when a property changes on the root pane.

protected void

uninstallComponents

​(

JRootPane

root)

Unregisters components.

protected void

uninstallDefaults

​(

JRootPane

root)

Uninstalls default properties.

protected void

uninstallKeyboardActions

​(

JRootPane

root)

Unregisters keyboard actions.

protected void

uninstallListeners

​(

JRootPane

root)

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

Returns a new instance of

BasicRootPaneUI

.

Installs components.

Installs default properties.

Registers keyboard actions.

Registers listeners.

Invoked when a property changes on the root pane.

Unregisters components.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicRootPaneUI

```java
public BasicRootPaneUI()
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

Returns a new instance of

BasicRootPaneUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicRootPaneUI

- installDefaults

```java
protected void installDefaults​(
JRootPane
c)
```

Installs default properties.

**Parameters:** c

- an instance of

JRootPane

- installComponents

```java
protected void installComponents​(
JRootPane
root)
```

Installs components.

**Parameters:** root

- an instance of

JRootPane

- installListeners

```java
protected void installListeners​(
JRootPane
root)
```

Registers listeners.

**Parameters:** root

- an instance of

JRootPane

- installKeyboardActions

```java
protected void installKeyboardActions​(
JRootPane
root)
```

Registers keyboard actions.

**Parameters:** root

- an instance of

JRootPane

- uninstallDefaults

```java
protected void uninstallDefaults​(
JRootPane
root)
```

Uninstalls default properties.

**Parameters:** root

- an instance of

JRootPane

- uninstallComponents

```java
protected void uninstallComponents​(
JRootPane
root)
```

Unregisters components.

**Parameters:** root

- an instance of

JRootPane

- uninstallListeners

```java
protected void uninstallListeners​(
JRootPane
root)
```

Unregisters listeners.

**Parameters:** root

- an instance of

JRootPane

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JRootPane
root)
```

Unregisters keyboard actions.

**Parameters:** root

- an instance of

JRootPane

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
e)
```

Invoked when a property changes on the root pane. If the event
indicates the

defaultButton

has changed, this will
reinstall the keyboard actions.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** e

- A PropertyChangeEvent object describing the event source
and the property that has changed.

Constructor Detail

- BasicRootPaneUI

```java
public BasicRootPaneUI()
```

---

#### Constructor Detail

BasicRootPaneUI

```java
public BasicRootPaneUI()
```

---

#### BasicRootPaneUI

public BasicRootPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicRootPaneUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicRootPaneUI

- installDefaults

```java
protected void installDefaults​(
JRootPane
c)
```

Installs default properties.

**Parameters:** c

- an instance of

JRootPane

- installComponents

```java
protected void installComponents​(
JRootPane
root)
```

Installs components.

**Parameters:** root

- an instance of

JRootPane

- installListeners

```java
protected void installListeners​(
JRootPane
root)
```

Registers listeners.

**Parameters:** root

- an instance of

JRootPane

- installKeyboardActions

```java
protected void installKeyboardActions​(
JRootPane
root)
```

Registers keyboard actions.

**Parameters:** root

- an instance of

JRootPane

- uninstallDefaults

```java
protected void uninstallDefaults​(
JRootPane
root)
```

Uninstalls default properties.

**Parameters:** root

- an instance of

JRootPane

- uninstallComponents

```java
protected void uninstallComponents​(
JRootPane
root)
```

Unregisters components.

**Parameters:** root

- an instance of

JRootPane

- uninstallListeners

```java
protected void uninstallListeners​(
JRootPane
root)
```

Unregisters listeners.

**Parameters:** root

- an instance of

JRootPane

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JRootPane
root)
```

Unregisters keyboard actions.

**Parameters:** root

- an instance of

JRootPane

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
e)
```

Invoked when a property changes on the root pane. If the event
indicates the

defaultButton

has changed, this will
reinstall the keyboard actions.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** e

- A PropertyChangeEvent object describing the event source
and the property that has changed.

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

Returns a new instance of

BasicRootPaneUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicRootPaneUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns a new instance of

BasicRootPaneUI

.

installDefaults

```java
protected void installDefaults​(
JRootPane
c)
```

Installs default properties.

**Parameters:** c

- an instance of

JRootPane

---

#### installDefaults

protected void installDefaults​(

JRootPane

c)

Installs default properties.

installComponents

```java
protected void installComponents​(
JRootPane
root)
```

Installs components.

**Parameters:** root

- an instance of

JRootPane

---

#### installComponents

protected void installComponents​(

JRootPane

root)

Installs components.

installListeners

```java
protected void installListeners​(
JRootPane
root)
```

Registers listeners.

**Parameters:** root

- an instance of

JRootPane

---

#### installListeners

protected void installListeners​(

JRootPane

root)

Registers listeners.

installKeyboardActions

```java
protected void installKeyboardActions​(
JRootPane
root)
```

Registers keyboard actions.

**Parameters:** root

- an instance of

JRootPane

---

#### installKeyboardActions

protected void installKeyboardActions​(

JRootPane

root)

Registers keyboard actions.

uninstallDefaults

```java
protected void uninstallDefaults​(
JRootPane
root)
```

Uninstalls default properties.

**Parameters:** root

- an instance of

JRootPane

---

#### uninstallDefaults

protected void uninstallDefaults​(

JRootPane

root)

Uninstalls default properties.

uninstallComponents

```java
protected void uninstallComponents​(
JRootPane
root)
```

Unregisters components.

**Parameters:** root

- an instance of

JRootPane

---

#### uninstallComponents

protected void uninstallComponents​(

JRootPane

root)

Unregisters components.

uninstallListeners

```java
protected void uninstallListeners​(
JRootPane
root)
```

Unregisters listeners.

**Parameters:** root

- an instance of

JRootPane

---

#### uninstallListeners

protected void uninstallListeners​(

JRootPane

root)

Unregisters listeners.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JRootPane
root)
```

Unregisters keyboard actions.

**Parameters:** root

- an instance of

JRootPane

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions​(

JRootPane

root)

Unregisters keyboard actions.

propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
e)
```

Invoked when a property changes on the root pane. If the event
indicates the

defaultButton

has changed, this will
reinstall the keyboard actions.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** e

- A PropertyChangeEvent object describing the event source
and the property that has changed.

---

#### propertyChange

public void propertyChange​(

PropertyChangeEvent

e)

Invoked when a property changes on the root pane. If the event
indicates the

defaultButton

has changed, this will
reinstall the keyboard actions.

---

