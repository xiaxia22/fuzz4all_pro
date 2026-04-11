# Class BasicDesktopIconUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicDesktopIconUI.html`

### Class Description

```java
public class
BasicDesktopIconUI

extends
DesktopIconUI
```

Basic L&F for a minimized window on a desktop.

**Direct Known Subclasses:** MetalDesktopIconUI

,

SynthDesktopIconUI

---

### Field Details

#### protected
JInternalFrame.JDesktopIcon
desktopIcon

The instance of

JInternalFrame.JDesktopIcon

.

---

#### protected
JInternalFrame
frame

The instance of

JInternalFrame

.

---

#### protected
JComponent
iconPane

The title pane component used in the desktop icon.

**Since:**
- 1.5

---

### Constructor Details

#### public BasicDesktopIconUI()

Constructs a new instance of

BasicDesktopIconUI

.

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs a new instance of

BasicDesktopIconUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

BasicDesktopIconUI

---

#### protected void installComponents()

Registers components.

---

#### protected void uninstallComponents()

Unregisters components.

---

#### protected void installListeners()

Registers listeners.

---

#### protected void uninstallListeners()

Unregisters listeners.

---

#### protected void installDefaults()

Installs default properties.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected
MouseInputListener
createMouseInputListener()

Returns a new instance of

MouseInputListener

.

**Returns:**
- a new instance of

MouseInputListener

---

#### public
Dimension
getMaximumSize​(
JComponent
c)

Desktop icons can not be resized. Therefore, we should always
return the minimum size of the desktop icon.

**Overrides:**
- getMaximumSize

in class

ComponentUI

**Parameters:**
- c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object or

null

**See Also:**
- ComponentUI.getMinimumSize(javax.swing.JComponent)

---

#### public
Insets
getInsets​(
JComponent
c)

Returns the insets.

**Parameters:**
- c

- a component

**Returns:**
- the insets

---

#### public void deiconize()

De-iconifies the internal frame.

---

### Additional Sections

#### Class BasicDesktopIconUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.DesktopIconUI
- - javax.swing.plaf.basic.BasicDesktopIconUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.DesktopIconUI
- - javax.swing.plaf.basic.BasicDesktopIconUI

javax.swing.plaf.DesktopIconUI

- javax.swing.plaf.basic.BasicDesktopIconUI

javax.swing.plaf.basic.BasicDesktopIconUI

**Direct Known Subclasses:** MetalDesktopIconUI

,

SynthDesktopIconUI

```java
public class
BasicDesktopIconUI

extends
DesktopIconUI
```

Basic L&F for a minimized window on a desktop.

public class

BasicDesktopIconUI

extends

DesktopIconUI

Basic L&F for a minimized window on a desktop.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicDesktopIconUI.MouseInputHandler

Listens for mouse movements and acts on them.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JInternalFrame.JDesktopIcon

desktopIcon

The instance of

JInternalFrame.JDesktopIcon

.

protected

JInternalFrame

frame

The instance of

JInternalFrame

.

protected

JComponent

iconPane

The title pane component used in the desktop icon.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicDesktopIconUI

()

Constructs a new instance of

BasicDesktopIconUI

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

protected

MouseInputListener

createMouseInputListener

()

Returns a new instance of

MouseInputListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

BasicDesktopIconUI

.

void

deiconize

()

De-iconifies the internal frame.

Insets

getInsets

​(

JComponent

c)

Returns the insets.

Dimension

getMaximumSize

​(

JComponent

c)

Desktop icons can not be resized.

protected void

installComponents

()

Registers components.

protected void

installDefaults

()

Installs default properties.

protected void

installListeners

()

Registers listeners.

protected void

uninstallComponents

()

Unregisters components.

protected void

uninstallDefaults

()

Uninstalls default properties.

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

Nested Classes

Modifier and Type

Class

Description

class

BasicDesktopIconUI.MouseInputHandler

Listens for mouse movements and acts on them.

---

#### Nested Class Summary

Listens for mouse movements and acts on them.

Field Summary

Fields

Modifier and Type

Field

Description

protected

JInternalFrame.JDesktopIcon

desktopIcon

The instance of

JInternalFrame.JDesktopIcon

.

protected

JInternalFrame

frame

The instance of

JInternalFrame

.

protected

JComponent

iconPane

The title pane component used in the desktop icon.

---

#### Field Summary

The instance of

JInternalFrame.JDesktopIcon

.

The instance of

JInternalFrame

.

The title pane component used in the desktop icon.

Constructor Summary

Constructors

Constructor

Description

BasicDesktopIconUI

()

Constructs a new instance of

BasicDesktopIconUI

.

---

#### Constructor Summary

Constructs a new instance of

BasicDesktopIconUI

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

MouseInputListener

createMouseInputListener

()

Returns a new instance of

MouseInputListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

BasicDesktopIconUI

.

void

deiconize

()

De-iconifies the internal frame.

Insets

getInsets

​(

JComponent

c)

Returns the insets.

Dimension

getMaximumSize

​(

JComponent

c)

Desktop icons can not be resized.

protected void

installComponents

()

Registers components.

protected void

installDefaults

()

Installs default properties.

protected void

installListeners

()

Registers listeners.

protected void

uninstallComponents

()

Unregisters components.

protected void

uninstallDefaults

()

Uninstalls default properties.

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

MouseInputListener

.

Constructs a new instance of

BasicDesktopIconUI

.

De-iconifies the internal frame.

Returns the insets.

Desktop icons can not be resized.

Registers components.

Installs default properties.

Registers listeners.

Unregisters components.

Uninstalls default properties.

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

- desktopIcon

```java
protected
JInternalFrame.JDesktopIcon
desktopIcon
```

The instance of

JInternalFrame.JDesktopIcon

.

- frame

```java
protected
JInternalFrame
frame
```

The instance of

JInternalFrame

.

- iconPane

```java
protected
JComponent
iconPane
```

The title pane component used in the desktop icon.

**Since:** 1.5

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicDesktopIconUI

```java
public BasicDesktopIconUI()
```

Constructs a new instance of

BasicDesktopIconUI

.

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

Constructs a new instance of

BasicDesktopIconUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicDesktopIconUI

- installComponents

```java
protected void installComponents()
```

Registers components.

- uninstallComponents

```java
protected void uninstallComponents()
```

Unregisters components.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Returns a new instance of

MouseInputListener

.

**Returns:** a new instance of

MouseInputListener

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Desktop icons can not be resized. Therefore, we should always
return the minimum size of the desktop icon.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** ComponentUI.getMinimumSize(javax.swing.JComponent)

- getInsets

```java
public
Insets
getInsets​(
JComponent
c)
```

Returns the insets.

**Parameters:** c

- a component
**Returns:** the insets

- deiconize

```java
public void deiconize()
```

De-iconifies the internal frame.

Field Detail

- desktopIcon

```java
protected
JInternalFrame.JDesktopIcon
desktopIcon
```

The instance of

JInternalFrame.JDesktopIcon

.

- frame

```java
protected
JInternalFrame
frame
```

The instance of

JInternalFrame

.

- iconPane

```java
protected
JComponent
iconPane
```

The title pane component used in the desktop icon.

**Since:** 1.5

---

#### Field Detail

desktopIcon

```java
protected
JInternalFrame.JDesktopIcon
desktopIcon
```

The instance of

JInternalFrame.JDesktopIcon

.

---

#### desktopIcon

protected

JInternalFrame.JDesktopIcon

desktopIcon

The instance of

JInternalFrame.JDesktopIcon

.

frame

```java
protected
JInternalFrame
frame
```

The instance of

JInternalFrame

.

---

#### frame

protected

JInternalFrame

frame

The instance of

JInternalFrame

.

iconPane

```java
protected
JComponent
iconPane
```

The title pane component used in the desktop icon.

**Since:** 1.5

---

#### iconPane

protected

JComponent

iconPane

The title pane component used in the desktop icon.

Constructor Detail

- BasicDesktopIconUI

```java
public BasicDesktopIconUI()
```

Constructs a new instance of

BasicDesktopIconUI

.

---

#### Constructor Detail

BasicDesktopIconUI

```java
public BasicDesktopIconUI()
```

Constructs a new instance of

BasicDesktopIconUI

.

---

#### BasicDesktopIconUI

public BasicDesktopIconUI()

Constructs a new instance of

BasicDesktopIconUI

.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new instance of

BasicDesktopIconUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicDesktopIconUI

- installComponents

```java
protected void installComponents()
```

Registers components.

- uninstallComponents

```java
protected void uninstallComponents()
```

Unregisters components.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Returns a new instance of

MouseInputListener

.

**Returns:** a new instance of

MouseInputListener

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Desktop icons can not be resized. Therefore, we should always
return the minimum size of the desktop icon.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** ComponentUI.getMinimumSize(javax.swing.JComponent)

- getInsets

```java
public
Insets
getInsets​(
JComponent
c)
```

Returns the insets.

**Parameters:** c

- a component
**Returns:** the insets

- deiconize

```java
public void deiconize()
```

De-iconifies the internal frame.

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

Constructs a new instance of

BasicDesktopIconUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicDesktopIconUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs a new instance of

BasicDesktopIconUI

.

installComponents

```java
protected void installComponents()
```

Registers components.

---

#### installComponents

protected void installComponents()

Registers components.

uninstallComponents

```java
protected void uninstallComponents()
```

Unregisters components.

---

#### uninstallComponents

protected void uninstallComponents()

Unregisters components.

installListeners

```java
protected void installListeners()
```

Registers listeners.

---

#### installListeners

protected void installListeners()

Registers listeners.

uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Unregisters listeners.

installDefaults

```java
protected void installDefaults()
```

Installs default properties.

---

#### installDefaults

protected void installDefaults()

Installs default properties.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Returns a new instance of

MouseInputListener

.

**Returns:** a new instance of

MouseInputListener

---

#### createMouseInputListener

protected

MouseInputListener

createMouseInputListener()

Returns a new instance of

MouseInputListener

.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Desktop icons can not be resized. Therefore, we should always
return the minimum size of the desktop icon.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** ComponentUI.getMinimumSize(javax.swing.JComponent)

---

#### getMaximumSize

public

Dimension

getMaximumSize​(

JComponent

c)

Desktop icons can not be resized. Therefore, we should always
return the minimum size of the desktop icon.

getInsets

```java
public
Insets
getInsets​(
JComponent
c)
```

Returns the insets.

**Parameters:** c

- a component
**Returns:** the insets

---

#### getInsets

public

Insets

getInsets​(

JComponent

c)

Returns the insets.

deiconize

```java
public void deiconize()
```

De-iconifies the internal frame.

---

#### deiconize

public void deiconize()

De-iconifies the internal frame.

---

