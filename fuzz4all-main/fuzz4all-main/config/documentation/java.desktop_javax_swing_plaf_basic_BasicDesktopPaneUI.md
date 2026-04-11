# Class BasicDesktopPaneUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicDesktopPaneUI.html`

### Class Description

```java
public class
BasicDesktopPaneUI

extends
DesktopPaneUI
```

Basic L&F for a desktop.

**Direct Known Subclasses:** SynthDesktopPaneUI

---

### Field Details

#### protected
JDesktopPane
desktop

The instance of

JDesktopPane

.

---

#### protected
DesktopManager
desktopManager

The instance of

DesktopManager

.

---

#### @Deprecated

protected
KeyStroke
minimizeKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
maximizeKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
closeKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
navigateKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
navigateKey2

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

### Constructor Details

#### public BasicDesktopPaneUI()

Constructs a new instance of

BasicDesktopPaneUI

.

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs a new instance of

BasicDesktopPaneUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

BasicDesktopPaneUI

---

#### protected void installDefaults()

Installs default properties.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected void installListeners()

Installs the

PropertyChangeListener

returned from

createPropertyChangeListener

on the

JDesktopPane

.

**See Also:**
- createPropertyChangeListener()

**Since:**
- 1.5

---

#### protected void uninstallListeners()

Uninstalls the

PropertyChangeListener

returned from

createPropertyChangeListener

from the

JDesktopPane

.

**See Also:**
- createPropertyChangeListener()

**Since:**
- 1.5

---

#### protected void installDesktopManager()

Installs desktop manager.

---

#### protected void uninstallDesktopManager()

Uninstalls desktop manager.

---

#### protected void installKeyboardActions()

Installs keyboard actions.

---

#### protected void registerKeyboardActions()

Registers keyboard actions.

---

#### protected void unregisterKeyboardActions()

Unregisters keyboard actions.

---

#### protected void uninstallKeyboardActions()

Unregisters keyboard actions.

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Returns the

PropertyChangeListener

to install on
the

JDesktopPane

.

**Returns:**
- The PropertyChangeListener that will be added to track
changes in the desktop pane.

**Since:**
- 1.5

---

### Additional Sections

#### Class BasicDesktopPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.DesktopPaneUI
- - javax.swing.plaf.basic.BasicDesktopPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.DesktopPaneUI
- - javax.swing.plaf.basic.BasicDesktopPaneUI

javax.swing.plaf.DesktopPaneUI

- javax.swing.plaf.basic.BasicDesktopPaneUI

javax.swing.plaf.basic.BasicDesktopPaneUI

**Direct Known Subclasses:** SynthDesktopPaneUI

```java
public class
BasicDesktopPaneUI

extends
DesktopPaneUI
```

Basic L&F for a desktop.

public class

BasicDesktopPaneUI

extends

DesktopPaneUI

Basic L&F for a desktop.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BasicDesktopPaneUI.CloseAction

Handles closing an internal frame.

protected class

BasicDesktopPaneUI.MaximizeAction

Handles maximizing an internal frame.

protected class

BasicDesktopPaneUI.MinimizeAction

Handles minimizing an internal frame.

protected class

BasicDesktopPaneUI.NavigateAction

Handles navigating to the next internal frame.

protected class

BasicDesktopPaneUI.OpenAction

Handles restoring a minimized or maximized internal frame.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

KeyStroke

closeKey

Deprecated.

As of 1.3.

protected

JDesktopPane

desktop

The instance of

JDesktopPane

.

protected

DesktopManager

desktopManager

The instance of

DesktopManager

.

protected

KeyStroke

maximizeKey

Deprecated.

As of 1.3.

protected

KeyStroke

minimizeKey

Deprecated.

As of 1.3.

protected

KeyStroke

navigateKey

Deprecated.

As of 1.3.

protected

KeyStroke

navigateKey2

Deprecated.

As of 1.3.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicDesktopPaneUI

()

Constructs a new instance of

BasicDesktopPaneUI

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

PropertyChangeListener

createPropertyChangeListener

()

Returns the

PropertyChangeListener

to install on
the

JDesktopPane

.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

BasicDesktopPaneUI

.

protected void

installDefaults

()

Installs default properties.

protected void

installDesktopManager

()

Installs desktop manager.

protected void

installKeyboardActions

()

Installs keyboard actions.

protected void

installListeners

()

Installs the

PropertyChangeListener

returned from

createPropertyChangeListener

on the

JDesktopPane

.

protected void

registerKeyboardActions

()

Registers keyboard actions.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallDesktopManager

()

Uninstalls desktop manager.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Uninstalls the

PropertyChangeListener

returned from

createPropertyChangeListener

from the

JDesktopPane

.

protected void

unregisterKeyboardActions

()

Unregisters keyboard actions.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BasicDesktopPaneUI.CloseAction

Handles closing an internal frame.

protected class

BasicDesktopPaneUI.MaximizeAction

Handles maximizing an internal frame.

protected class

BasicDesktopPaneUI.MinimizeAction

Handles minimizing an internal frame.

protected class

BasicDesktopPaneUI.NavigateAction

Handles navigating to the next internal frame.

protected class

BasicDesktopPaneUI.OpenAction

Handles restoring a minimized or maximized internal frame.

---

#### Nested Class Summary

Handles closing an internal frame.

Handles maximizing an internal frame.

Handles minimizing an internal frame.

Handles navigating to the next internal frame.

Handles restoring a minimized or maximized internal frame.

Field Summary

Fields

Modifier and Type

Field

Description

protected

KeyStroke

closeKey

Deprecated.

As of 1.3.

protected

JDesktopPane

desktop

The instance of

JDesktopPane

.

protected

DesktopManager

desktopManager

The instance of

DesktopManager

.

protected

KeyStroke

maximizeKey

Deprecated.

As of 1.3.

protected

KeyStroke

minimizeKey

Deprecated.

As of 1.3.

protected

KeyStroke

navigateKey

Deprecated.

As of 1.3.

protected

KeyStroke

navigateKey2

Deprecated.

As of 1.3.

---

#### Field Summary

Deprecated.

As of 1.3.

The instance of

JDesktopPane

.

The instance of

DesktopManager

.

Constructor Summary

Constructors

Constructor

Description

BasicDesktopPaneUI

()

Constructs a new instance of

BasicDesktopPaneUI

.

---

#### Constructor Summary

Constructs a new instance of

BasicDesktopPaneUI

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

PropertyChangeListener

createPropertyChangeListener

()

Returns the

PropertyChangeListener

to install on
the

JDesktopPane

.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

BasicDesktopPaneUI

.

protected void

installDefaults

()

Installs default properties.

protected void

installDesktopManager

()

Installs desktop manager.

protected void

installKeyboardActions

()

Installs keyboard actions.

protected void

installListeners

()

Installs the

PropertyChangeListener

returned from

createPropertyChangeListener

on the

JDesktopPane

.

protected void

registerKeyboardActions

()

Registers keyboard actions.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallDesktopManager

()

Uninstalls desktop manager.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Uninstalls the

PropertyChangeListener

returned from

createPropertyChangeListener

from the

JDesktopPane

.

protected void

unregisterKeyboardActions

()

Unregisters keyboard actions.

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

Returns the

PropertyChangeListener

to install on
the

JDesktopPane

.

Constructs a new instance of

BasicDesktopPaneUI

.

Installs default properties.

Installs desktop manager.

Installs keyboard actions.

Installs the

PropertyChangeListener

returned from

createPropertyChangeListener

on the

JDesktopPane

.

Registers keyboard actions.

Uninstalls default properties.

Uninstalls desktop manager.

Unregisters keyboard actions.

Uninstalls the

PropertyChangeListener

returned from

createPropertyChangeListener

from the

JDesktopPane

.

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

- desktop

```java
protected
JDesktopPane
desktop
```

The instance of

JDesktopPane

.

- desktopManager

```java
protected
DesktopManager
desktopManager
```

The instance of

DesktopManager

.

- minimizeKey

```java
@Deprecated

protected
KeyStroke
minimizeKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- maximizeKey

```java
@Deprecated

protected
KeyStroke
maximizeKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- closeKey

```java
@Deprecated

protected
KeyStroke
closeKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- navigateKey

```java
@Deprecated

protected
KeyStroke
navigateKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- navigateKey2

```java
@Deprecated

protected
KeyStroke
navigateKey2
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicDesktopPaneUI

```java
public BasicDesktopPaneUI()
```

Constructs a new instance of

BasicDesktopPaneUI

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

BasicDesktopPaneUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicDesktopPaneUI

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

- installListeners

```java
protected void installListeners()
```

Installs the

PropertyChangeListener

returned from

createPropertyChangeListener

on the

JDesktopPane

.

**Since:** 1.5
**See Also:** createPropertyChangeListener()

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the

PropertyChangeListener

returned from

createPropertyChangeListener

from the

JDesktopPane

.

**Since:** 1.5
**See Also:** createPropertyChangeListener()

- installDesktopManager

```java
protected void installDesktopManager()
```

Installs desktop manager.

- uninstallDesktopManager

```java
protected void uninstallDesktopManager()
```

Uninstalls desktop manager.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs keyboard actions.

- registerKeyboardActions

```java
protected void registerKeyboardActions()
```

Registers keyboard actions.

- unregisterKeyboardActions

```java
protected void unregisterKeyboardActions()
```

Unregisters keyboard actions.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns the

PropertyChangeListener

to install on
the

JDesktopPane

.

**Returns:** The PropertyChangeListener that will be added to track
changes in the desktop pane.
**Since:** 1.5

Field Detail

- desktop

```java
protected
JDesktopPane
desktop
```

The instance of

JDesktopPane

.

- desktopManager

```java
protected
DesktopManager
desktopManager
```

The instance of

DesktopManager

.

- minimizeKey

```java
@Deprecated

protected
KeyStroke
minimizeKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- maximizeKey

```java
@Deprecated

protected
KeyStroke
maximizeKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- closeKey

```java
@Deprecated

protected
KeyStroke
closeKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- navigateKey

```java
@Deprecated

protected
KeyStroke
navigateKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- navigateKey2

```java
@Deprecated

protected
KeyStroke
navigateKey2
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### Field Detail

desktop

```java
protected
JDesktopPane
desktop
```

The instance of

JDesktopPane

.

---

#### desktop

protected

JDesktopPane

desktop

The instance of

JDesktopPane

.

desktopManager

```java
protected
DesktopManager
desktopManager
```

The instance of

DesktopManager

.

---

#### desktopManager

protected

DesktopManager

desktopManager

The instance of

DesktopManager

.

minimizeKey

```java
@Deprecated

protected
KeyStroke
minimizeKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### minimizeKey

@Deprecated

protected

KeyStroke

minimizeKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

maximizeKey

```java
@Deprecated

protected
KeyStroke
maximizeKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### maximizeKey

@Deprecated

protected

KeyStroke

maximizeKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

closeKey

```java
@Deprecated

protected
KeyStroke
closeKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### closeKey

@Deprecated

protected

KeyStroke

closeKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

navigateKey

```java
@Deprecated

protected
KeyStroke
navigateKey
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### navigateKey

@Deprecated

protected

KeyStroke

navigateKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

navigateKey2

```java
@Deprecated

protected
KeyStroke
navigateKey2
```

Deprecated.

As of 1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### navigateKey2

@Deprecated

protected

KeyStroke

navigateKey2

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

Constructor Detail

- BasicDesktopPaneUI

```java
public BasicDesktopPaneUI()
```

Constructs a new instance of

BasicDesktopPaneUI

.

---

#### Constructor Detail

BasicDesktopPaneUI

```java
public BasicDesktopPaneUI()
```

Constructs a new instance of

BasicDesktopPaneUI

.

---

#### BasicDesktopPaneUI

public BasicDesktopPaneUI()

Constructs a new instance of

BasicDesktopPaneUI

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

BasicDesktopPaneUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicDesktopPaneUI

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

- installListeners

```java
protected void installListeners()
```

Installs the

PropertyChangeListener

returned from

createPropertyChangeListener

on the

JDesktopPane

.

**Since:** 1.5
**See Also:** createPropertyChangeListener()

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the

PropertyChangeListener

returned from

createPropertyChangeListener

from the

JDesktopPane

.

**Since:** 1.5
**See Also:** createPropertyChangeListener()

- installDesktopManager

```java
protected void installDesktopManager()
```

Installs desktop manager.

- uninstallDesktopManager

```java
protected void uninstallDesktopManager()
```

Uninstalls desktop manager.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs keyboard actions.

- registerKeyboardActions

```java
protected void registerKeyboardActions()
```

Registers keyboard actions.

- unregisterKeyboardActions

```java
protected void unregisterKeyboardActions()
```

Unregisters keyboard actions.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns the

PropertyChangeListener

to install on
the

JDesktopPane

.

**Returns:** The PropertyChangeListener that will be added to track
changes in the desktop pane.
**Since:** 1.5

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

BasicDesktopPaneUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicDesktopPaneUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs a new instance of

BasicDesktopPaneUI

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

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

installListeners

```java
protected void installListeners()
```

Installs the

PropertyChangeListener

returned from

createPropertyChangeListener

on the

JDesktopPane

.

**Since:** 1.5
**See Also:** createPropertyChangeListener()

---

#### installListeners

protected void installListeners()

Installs the

PropertyChangeListener

returned from

createPropertyChangeListener

on the

JDesktopPane

.

uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the

PropertyChangeListener

returned from

createPropertyChangeListener

from the

JDesktopPane

.

**Since:** 1.5
**See Also:** createPropertyChangeListener()

---

#### uninstallListeners

protected void uninstallListeners()

Uninstalls the

PropertyChangeListener

returned from

createPropertyChangeListener

from the

JDesktopPane

.

installDesktopManager

```java
protected void installDesktopManager()
```

Installs desktop manager.

---

#### installDesktopManager

protected void installDesktopManager()

Installs desktop manager.

uninstallDesktopManager

```java
protected void uninstallDesktopManager()
```

Uninstalls desktop manager.

---

#### uninstallDesktopManager

protected void uninstallDesktopManager()

Uninstalls desktop manager.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs keyboard actions.

---

#### installKeyboardActions

protected void installKeyboardActions()

Installs keyboard actions.

registerKeyboardActions

```java
protected void registerKeyboardActions()
```

Registers keyboard actions.

---

#### registerKeyboardActions

protected void registerKeyboardActions()

Registers keyboard actions.

unregisterKeyboardActions

```java
protected void unregisterKeyboardActions()
```

Unregisters keyboard actions.

---

#### unregisterKeyboardActions

protected void unregisterKeyboardActions()

Unregisters keyboard actions.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters keyboard actions.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns the

PropertyChangeListener

to install on
the

JDesktopPane

.

**Returns:** The PropertyChangeListener that will be added to track
changes in the desktop pane.
**Since:** 1.5

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Returns the

PropertyChangeListener

to install on
the

JDesktopPane

.

---

