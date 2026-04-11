# Class BasicMenuUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicMenuUI.html`

### Class Description

```java
public class
BasicMenuUI

extends
BasicMenuItemUI
```

A default L&F implementation of MenuUI. This implementation
is a "combined" view/controller.

**Direct Known Subclasses:** SynthMenuUI

---

### Field Details

#### protected
ChangeListener
changeListener

The instance of

ChangeListener

.

---

#### protected
MenuListener
menuListener

The instance of

MenuListener

.

---

### Constructor Details

#### public BasicMenuUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Constructs a new instance of

BasicMenuUI

.

**Parameters:**
- x

- a component

**Returns:**
- a new instance of

BasicMenuUI

---

#### protected
MenuListener
createMenuListener​(
JComponent
c)

Returns an instance of

MenuListener

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

MenuListener

---

#### protected
ChangeListener
createChangeListener​(
JComponent
c)

Returns an instance of

ChangeListener

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

ChangeListener

---

#### protected void setupPostTimer​(
JMenu
menu)

Sets timer to the

menu

.

**Parameters:**
- menu

- an instance of

JMenu

.

---

### Additional Sections

#### Class BasicMenuUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ButtonUI
- - javax.swing.plaf.MenuItemUI
- - javax.swing.plaf.basic.BasicMenuItemUI
- - javax.swing.plaf.basic.BasicMenuUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ButtonUI
- - javax.swing.plaf.MenuItemUI
- - javax.swing.plaf.basic.BasicMenuItemUI
- - javax.swing.plaf.basic.BasicMenuUI

javax.swing.plaf.ButtonUI

- javax.swing.plaf.MenuItemUI
- - javax.swing.plaf.basic.BasicMenuItemUI
- - javax.swing.plaf.basic.BasicMenuUI

javax.swing.plaf.MenuItemUI

- javax.swing.plaf.basic.BasicMenuItemUI
- - javax.swing.plaf.basic.BasicMenuUI

javax.swing.plaf.basic.BasicMenuItemUI

- javax.swing.plaf.basic.BasicMenuUI

javax.swing.plaf.basic.BasicMenuUI

**Direct Known Subclasses:** SynthMenuUI

```java
public class
BasicMenuUI

extends
BasicMenuItemUI
```

A default L&F implementation of MenuUI. This implementation
is a "combined" view/controller.

public class

BasicMenuUI

extends

BasicMenuItemUI

A default L&F implementation of MenuUI. This implementation
is a "combined" view/controller.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicMenuUI.ChangeHandler

As of Java 2 platform 1.4, this previously undocumented class
is now obsolete.

protected class

BasicMenuUI.MouseInputHandler

Instantiated and used by a menu item to handle the current menu selection
from mouse events.

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

MenuListener

menuListener

The instance of

MenuListener

.

- Fields declared in class javax.swing.plaf.basic.

BasicMenuItemUI

acceleratorDelimiter

,

acceleratorFont

,

acceleratorForeground

,

acceleratorSelectionForeground

,

arrowIcon

,

checkIcon

,

defaultTextIconGap

,

disabledForeground

,

menuDragMouseListener

,

menuItem

,

menuKeyListener

,

mouseInputListener

,

oldBorderPainted

,

propertyChangeListener

,

selectionBackground

,

selectionForeground

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicMenuUI

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

​(

JComponent

c)

Returns an instance of

ChangeListener

.

protected

MenuListener

createMenuListener

​(

JComponent

c)

Returns an instance of

MenuListener

.

static

ComponentUI

createUI

​(

JComponent

x)

Constructs a new instance of

BasicMenuUI

.

protected void

setupPostTimer

​(

JMenu

menu)

Sets timer to the

menu

.

- Methods declared in class javax.swing.plaf.basic.

BasicMenuItemUI

createMenuDragMouseListener

,

createMenuKeyListener

,

createMouseInputListener

,

createPropertyChangeListener

,

doClick

,

getPath

,

getPreferredMenuItemSize

,

getPropertyPrefix

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

paintBackground

,

paintMenuItem

,

paintText

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

update

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

BasicMenuUI.ChangeHandler

As of Java 2 platform 1.4, this previously undocumented class
is now obsolete.

protected class

BasicMenuUI.MouseInputHandler

Instantiated and used by a menu item to handle the current menu selection
from mouse events.

---

#### Nested Class Summary

As of Java 2 platform 1.4, this previously undocumented class
is now obsolete.

Instantiated and used by a menu item to handle the current menu selection
from mouse events.

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

MenuListener

menuListener

The instance of

MenuListener

.

- Fields declared in class javax.swing.plaf.basic.

BasicMenuItemUI

acceleratorDelimiter

,

acceleratorFont

,

acceleratorForeground

,

acceleratorSelectionForeground

,

arrowIcon

,

checkIcon

,

defaultTextIconGap

,

disabledForeground

,

menuDragMouseListener

,

menuItem

,

menuKeyListener

,

mouseInputListener

,

oldBorderPainted

,

propertyChangeListener

,

selectionBackground

,

selectionForeground

---

#### Field Summary

The instance of

ChangeListener

.

The instance of

MenuListener

.

Fields declared in class javax.swing.plaf.basic.

BasicMenuItemUI

acceleratorDelimiter

,

acceleratorFont

,

acceleratorForeground

,

acceleratorSelectionForeground

,

arrowIcon

,

checkIcon

,

defaultTextIconGap

,

disabledForeground

,

menuDragMouseListener

,

menuItem

,

menuKeyListener

,

mouseInputListener

,

oldBorderPainted

,

propertyChangeListener

,

selectionBackground

,

selectionForeground

---

#### Fields declared in class javax.swing.plaf.basic. BasicMenuItemUI

Constructor Summary

Constructors

Constructor

Description

BasicMenuUI

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

​(

JComponent

c)

Returns an instance of

ChangeListener

.

protected

MenuListener

createMenuListener

​(

JComponent

c)

Returns an instance of

MenuListener

.

static

ComponentUI

createUI

​(

JComponent

x)

Constructs a new instance of

BasicMenuUI

.

protected void

setupPostTimer

​(

JMenu

menu)

Sets timer to the

menu

.

- Methods declared in class javax.swing.plaf.basic.

BasicMenuItemUI

createMenuDragMouseListener

,

createMenuKeyListener

,

createMouseInputListener

,

createPropertyChangeListener

,

doClick

,

getPath

,

getPreferredMenuItemSize

,

getPropertyPrefix

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

paintBackground

,

paintMenuItem

,

paintText

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

update

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

MenuListener

.

Constructs a new instance of

BasicMenuUI

.

Sets timer to the

menu

.

Methods declared in class javax.swing.plaf.basic.

BasicMenuItemUI

createMenuDragMouseListener

,

createMenuKeyListener

,

createMouseInputListener

,

createPropertyChangeListener

,

doClick

,

getPath

,

getPreferredMenuItemSize

,

getPropertyPrefix

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

paintBackground

,

paintMenuItem

,

paintText

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

update

---

#### Methods declared in class javax.swing.plaf.basic. BasicMenuItemUI

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

- changeListener

```java
protected
ChangeListener
changeListener
```

The instance of

ChangeListener

.

- menuListener

```java
protected
MenuListener
menuListener
```

The instance of

MenuListener

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicMenuUI

```java
public BasicMenuUI()
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

Constructs a new instance of

BasicMenuUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicMenuUI

- createMenuListener

```java
protected
MenuListener
createMenuListener​(
JComponent
c)
```

Returns an instance of

MenuListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MenuListener

- createChangeListener

```java
protected
ChangeListener
createChangeListener​(
JComponent
c)
```

Returns an instance of

ChangeListener

.

**Parameters:** c

- a component
**Returns:** an instance of

ChangeListener

- setupPostTimer

```java
protected void setupPostTimer​(
JMenu
menu)
```

Sets timer to the

menu

.

**Parameters:** menu

- an instance of

JMenu

.

Field Detail

- changeListener

```java
protected
ChangeListener
changeListener
```

The instance of

ChangeListener

.

- menuListener

```java
protected
MenuListener
menuListener
```

The instance of

MenuListener

.

---

#### Field Detail

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

menuListener

```java
protected
MenuListener
menuListener
```

The instance of

MenuListener

.

---

#### menuListener

protected

MenuListener

menuListener

The instance of

MenuListener

.

Constructor Detail

- BasicMenuUI

```java
public BasicMenuUI()
```

---

#### Constructor Detail

BasicMenuUI

```java
public BasicMenuUI()
```

---

#### BasicMenuUI

public BasicMenuUI()

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

BasicMenuUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicMenuUI

- createMenuListener

```java
protected
MenuListener
createMenuListener​(
JComponent
c)
```

Returns an instance of

MenuListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MenuListener

- createChangeListener

```java
protected
ChangeListener
createChangeListener​(
JComponent
c)
```

Returns an instance of

ChangeListener

.

**Parameters:** c

- a component
**Returns:** an instance of

ChangeListener

- setupPostTimer

```java
protected void setupPostTimer​(
JMenu
menu)
```

Sets timer to the

menu

.

**Parameters:** menu

- an instance of

JMenu

.

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

BasicMenuUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicMenuUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Constructs a new instance of

BasicMenuUI

.

createMenuListener

```java
protected
MenuListener
createMenuListener​(
JComponent
c)
```

Returns an instance of

MenuListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MenuListener

---

#### createMenuListener

protected

MenuListener

createMenuListener​(

JComponent

c)

Returns an instance of

MenuListener

.

createChangeListener

```java
protected
ChangeListener
createChangeListener​(
JComponent
c)
```

Returns an instance of

ChangeListener

.

**Parameters:** c

- a component
**Returns:** an instance of

ChangeListener

---

#### createChangeListener

protected

ChangeListener

createChangeListener​(

JComponent

c)

Returns an instance of

ChangeListener

.

setupPostTimer

```java
protected void setupPostTimer​(
JMenu
menu)
```

Sets timer to the

menu

.

**Parameters:** menu

- an instance of

JMenu

.

---

#### setupPostTimer

protected void setupPostTimer​(

JMenu

menu)

Sets timer to the

menu

.

---

