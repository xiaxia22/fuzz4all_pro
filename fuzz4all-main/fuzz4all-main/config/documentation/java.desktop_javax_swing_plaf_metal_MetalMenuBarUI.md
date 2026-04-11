# Class MetalMenuBarUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalMenuBarUI.html`

### Class Description

```java
public class
MetalMenuBarUI

extends
BasicMenuBarUI
```

Metal implementation of

MenuBarUI

. This class is responsible
for providing the metal look and feel for

JMenuBar

s.

**Since:** 1.5
**See Also:** MenuBarUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public MetalMenuBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Creates the

ComponentUI

implementation for the passed
in component.

**Parameters:**
- x

- JComponent to create the ComponentUI implementation for

**Returns:**
- ComponentUI implementation for

x

**Throws:**
- NullPointerException

- if

x

is null

---

#### public void installUI​(
JComponent
c)

Configures the specified component appropriate for the metal look and
feel.

**Overrides:**
- installUI

in class

ComponentUI

**Parameters:**
- c

- the component where this UI delegate is being installed

**Throws:**
- NullPointerException

- if

c

is null.

**See Also:**
- ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### public void uninstallUI​(
JComponent
c)

Reverses configuration which was done on the specified component during

installUI

.

**Overrides:**
- uninstallUI

in class

ComponentUI

**Parameters:**
- c

- the component where this UI delegate is being installed

**Throws:**
- NullPointerException

- if

c

is null.

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

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

#### Class MetalMenuBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.MenuBarUI
- - javax.swing.plaf.basic.BasicMenuBarUI
- - javax.swing.plaf.metal.MetalMenuBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.MenuBarUI
- - javax.swing.plaf.basic.BasicMenuBarUI
- - javax.swing.plaf.metal.MetalMenuBarUI

javax.swing.plaf.MenuBarUI

- javax.swing.plaf.basic.BasicMenuBarUI
- - javax.swing.plaf.metal.MetalMenuBarUI

javax.swing.plaf.basic.BasicMenuBarUI

- javax.swing.plaf.metal.MetalMenuBarUI

javax.swing.plaf.metal.MetalMenuBarUI

```java
public class
MetalMenuBarUI

extends
BasicMenuBarUI
```

Metal implementation of

MenuBarUI

. This class is responsible
for providing the metal look and feel for

JMenuBar

s.

**Since:** 1.5
**See Also:** MenuBarUI

public class

MetalMenuBarUI

extends

BasicMenuBarUI

Metal implementation of

MenuBarUI

. This class is responsible
for providing the metal look and feel for

JMenuBar

s.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicMenuBarUI

changeListener

,

containerListener

,

menuBar

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalMenuBarUI

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

x)

Creates the

ComponentUI

implementation for the passed
in component.

void

installUI

​(

JComponent

c)

Configures the specified component appropriate for the metal look and
feel.

void

uninstallUI

​(

JComponent

c)

Reverses configuration which was done on the specified component during

installUI

.

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

BasicMenuBarUI

createChangeListener

,

createContainerListener

,

installDefaults

,

installKeyboardActions

,

installListeners

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

paint

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

- Fields declared in class javax.swing.plaf.basic.

BasicMenuBarUI

changeListener

,

containerListener

,

menuBar

---

#### Field Summary

Fields declared in class javax.swing.plaf.basic.

BasicMenuBarUI

changeListener

,

containerListener

,

menuBar

---

#### Fields declared in class javax.swing.plaf.basic. BasicMenuBarUI

Constructor Summary

Constructors

Constructor

Description

MetalMenuBarUI

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

x)

Creates the

ComponentUI

implementation for the passed
in component.

void

installUI

​(

JComponent

c)

Configures the specified component appropriate for the metal look and
feel.

void

uninstallUI

​(

JComponent

c)

Reverses configuration which was done on the specified component during

installUI

.

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

BasicMenuBarUI

createChangeListener

,

createContainerListener

,

installDefaults

,

installKeyboardActions

,

installListeners

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

paint

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

Creates the

ComponentUI

implementation for the passed
in component.

Configures the specified component appropriate for the metal look and
feel.

Reverses configuration which was done on the specified component during

installUI

.

If necessary paints the background of the component, then
invokes

paint

.

Methods declared in class javax.swing.plaf.basic.

BasicMenuBarUI

createChangeListener

,

createContainerListener

,

installDefaults

,

installKeyboardActions

,

installListeners

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

---

#### Methods declared in class javax.swing.plaf.basic. BasicMenuBarUI

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

paint

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

- MetalMenuBarUI

```java
public MetalMenuBarUI()
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

Creates the

ComponentUI

implementation for the passed
in component.

**Parameters:** x

- JComponent to create the ComponentUI implementation for
**Returns:** ComponentUI implementation for

x
**Throws:** NullPointerException

- if

x

is null

- installUI

```java
public void installUI​(
JComponent
c)
```

Configures the specified component appropriate for the metal look and
feel.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**Throws:** NullPointerException

- if

c

is null.
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Reverses configuration which was done on the specified component during

installUI

.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**Throws:** NullPointerException

- if

c

is null.
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

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

Constructor Detail

- MetalMenuBarUI

```java
public MetalMenuBarUI()
```

---

#### Constructor Detail

MetalMenuBarUI

```java
public MetalMenuBarUI()
```

---

#### MetalMenuBarUI

public MetalMenuBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates the

ComponentUI

implementation for the passed
in component.

**Parameters:** x

- JComponent to create the ComponentUI implementation for
**Returns:** ComponentUI implementation for

x
**Throws:** NullPointerException

- if

x

is null

- installUI

```java
public void installUI​(
JComponent
c)
```

Configures the specified component appropriate for the metal look and
feel.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**Throws:** NullPointerException

- if

c

is null.
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Reverses configuration which was done on the specified component during

installUI

.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**Throws:** NullPointerException

- if

c

is null.
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

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
x)
```

Creates the

ComponentUI

implementation for the passed
in component.

**Parameters:** x

- JComponent to create the ComponentUI implementation for
**Returns:** ComponentUI implementation for

x
**Throws:** NullPointerException

- if

x

is null

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Creates the

ComponentUI

implementation for the passed
in component.

installUI

```java
public void installUI​(
JComponent
c)
```

Configures the specified component appropriate for the metal look and
feel.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**Throws:** NullPointerException

- if

c

is null.
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### installUI

public void installUI​(

JComponent

c)

Configures the specified component appropriate for the metal look and
feel.

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Reverses configuration which was done on the specified component during

installUI

.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**Throws:** NullPointerException

- if

c

is null.
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### uninstallUI

public void uninstallUI​(

JComponent

c)

Reverses configuration which was done on the specified component during

installUI

.

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

