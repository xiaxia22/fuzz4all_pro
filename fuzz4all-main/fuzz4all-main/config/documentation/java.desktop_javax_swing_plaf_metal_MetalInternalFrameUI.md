# Class MetalInternalFrameUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalInternalFrameUI.html`

### Class Description

```java
public class
MetalInternalFrameUI

extends
BasicInternalFrameUI
```

Metal implementation of JInternalFrame.

---

### Field Details

#### protected static
String
IS_PALETTE

The property

JInternalFrame.isPalette

.

---

### Constructor Details

#### public MetalInternalFrameUI​(
JInternalFrame
b)

Constructs a new

MetalInternalFrameUI

instance.

**Parameters:**
- b

- an internal frame

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs a new

MetalInternalFrameUI

instance.

**Parameters:**
- c

- a component

**Returns:**
- a new

MetalInternalFrameUI

instance

---

#### public void setPalette​(boolean isPalette)

If

isPalette

is

true

, sets palette border and title

**Parameters:**
- isPalette

- if

true

, sets palette border and title

---

#### protected
MouseInputAdapter
createBorderListener​(
JInternalFrame
w)

Returns the

MouseInputAdapter

that will be installed
on the TitlePane.

**Overrides:**
- createBorderListener

in class

BasicInternalFrameUI

**Parameters:**
- w

- the

JInternalFrame

**Returns:**
- the

MouseInputAdapter

that will be installed
on the TitlePane.

**Since:**
- 1.6

---

### Additional Sections

#### Class MetalInternalFrameUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.InternalFrameUI
- - javax.swing.plaf.basic.BasicInternalFrameUI
- - javax.swing.plaf.metal.MetalInternalFrameUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.InternalFrameUI
- - javax.swing.plaf.basic.BasicInternalFrameUI
- - javax.swing.plaf.metal.MetalInternalFrameUI

javax.swing.plaf.InternalFrameUI

- javax.swing.plaf.basic.BasicInternalFrameUI
- - javax.swing.plaf.metal.MetalInternalFrameUI

javax.swing.plaf.basic.BasicInternalFrameUI

- javax.swing.plaf.metal.MetalInternalFrameUI

javax.swing.plaf.metal.MetalInternalFrameUI

```java
public class
MetalInternalFrameUI

extends
BasicInternalFrameUI
```

Metal implementation of JInternalFrame.

public class

MetalInternalFrameUI

extends

BasicInternalFrameUI

Metal implementation of JInternalFrame.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

BasicInternalFrameUI.BasicInternalFrameListener

,

BasicInternalFrameUI.BorderListener

,

BasicInternalFrameUI.ComponentHandler

,

BasicInternalFrameUI.GlassPaneDispatcher

,

BasicInternalFrameUI.InternalFrameLayout

,

BasicInternalFrameUI.InternalFramePropertyChangeListener

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static

String

IS_PALETTE

The property

JInternalFrame.isPalette

.

- Fields declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

borderListener

,

componentListener

,

eastPane

,

frame

,

glassPaneDispatcher

,

internalFrameLayout

,

northPane

,

openMenuKey

,

propertyChangeListener

,

southPane

,

titlePane

,

westPane

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalInternalFrameUI

​(

JInternalFrame

b)

Constructs a new

MetalInternalFrameUI

instance.

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

MouseInputAdapter

createBorderListener

​(

JInternalFrame

w)

Returns the

MouseInputAdapter

that will be installed
on the TitlePane.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new

MetalInternalFrameUI

instance.

void

setPalette

​(boolean isPalette)

If

isPalette

is

true

, sets palette border and title

- Methods declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

activateFrame

,

closeFrame

,

createComponentListener

,

createDesktopManager

,

createEastPane

,

createGlassPaneDispatcher

,

createInternalFrameListener

,

createLayoutManager

,

createNorthPane

,

createPropertyChangeListener

,

createSouthPane

,

createWestPane

,

deactivateFrame

,

deiconifyFrame

,

deinstallMouseHandlers

,

getDesktopManager

,

getEastPane

,

getMaximumSize

,

getMinimumSize

,

getNorthPane

,

getPreferredSize

,

getSouthPane

,

getWestPane

,

iconifyFrame

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installMouseHandlers

,

installUI

,

isKeyBindingActive

,

isKeyBindingRegistered

,

maximizeFrame

,

minimizeFrame

,

replacePane

,

setEastPane

,

setKeyBindingActive

,

setKeyBindingRegistered

,

setNorthPane

,

setSouthPane

,

setupMenuCloseKey

,

setupMenuOpenKey

,

setWestPane

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

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

paint

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

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

BasicInternalFrameUI.BasicInternalFrameListener

,

BasicInternalFrameUI.BorderListener

,

BasicInternalFrameUI.ComponentHandler

,

BasicInternalFrameUI.GlassPaneDispatcher

,

BasicInternalFrameUI.InternalFrameLayout

,

BasicInternalFrameUI.InternalFramePropertyChangeListener

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

BasicInternalFrameUI.BasicInternalFrameListener

,

BasicInternalFrameUI.BorderListener

,

BasicInternalFrameUI.ComponentHandler

,

BasicInternalFrameUI.GlassPaneDispatcher

,

BasicInternalFrameUI.InternalFrameLayout

,

BasicInternalFrameUI.InternalFramePropertyChangeListener

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicInternalFrameUI

Field Summary

Fields

Modifier and Type

Field

Description

protected static

String

IS_PALETTE

The property

JInternalFrame.isPalette

.

- Fields declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

borderListener

,

componentListener

,

eastPane

,

frame

,

glassPaneDispatcher

,

internalFrameLayout

,

northPane

,

openMenuKey

,

propertyChangeListener

,

southPane

,

titlePane

,

westPane

---

#### Field Summary

The property

JInternalFrame.isPalette

.

Fields declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

borderListener

,

componentListener

,

eastPane

,

frame

,

glassPaneDispatcher

,

internalFrameLayout

,

northPane

,

openMenuKey

,

propertyChangeListener

,

southPane

,

titlePane

,

westPane

---

#### Fields declared in class javax.swing.plaf.basic. BasicInternalFrameUI

Constructor Summary

Constructors

Constructor

Description

MetalInternalFrameUI

​(

JInternalFrame

b)

Constructs a new

MetalInternalFrameUI

instance.

---

#### Constructor Summary

Constructs a new

MetalInternalFrameUI

instance.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

MouseInputAdapter

createBorderListener

​(

JInternalFrame

w)

Returns the

MouseInputAdapter

that will be installed
on the TitlePane.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new

MetalInternalFrameUI

instance.

void

setPalette

​(boolean isPalette)

If

isPalette

is

true

, sets palette border and title

- Methods declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

activateFrame

,

closeFrame

,

createComponentListener

,

createDesktopManager

,

createEastPane

,

createGlassPaneDispatcher

,

createInternalFrameListener

,

createLayoutManager

,

createNorthPane

,

createPropertyChangeListener

,

createSouthPane

,

createWestPane

,

deactivateFrame

,

deiconifyFrame

,

deinstallMouseHandlers

,

getDesktopManager

,

getEastPane

,

getMaximumSize

,

getMinimumSize

,

getNorthPane

,

getPreferredSize

,

getSouthPane

,

getWestPane

,

iconifyFrame

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installMouseHandlers

,

installUI

,

isKeyBindingActive

,

isKeyBindingRegistered

,

maximizeFrame

,

minimizeFrame

,

replacePane

,

setEastPane

,

setKeyBindingActive

,

setKeyBindingRegistered

,

setNorthPane

,

setSouthPane

,

setupMenuCloseKey

,

setupMenuOpenKey

,

setWestPane

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

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

paint

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

MouseInputAdapter

that will be installed
on the TitlePane.

Constructs a new

MetalInternalFrameUI

instance.

If

isPalette

is

true

, sets palette border and title

Methods declared in class javax.swing.plaf.basic.

BasicInternalFrameUI

activateFrame

,

closeFrame

,

createComponentListener

,

createDesktopManager

,

createEastPane

,

createGlassPaneDispatcher

,

createInternalFrameListener

,

createLayoutManager

,

createNorthPane

,

createPropertyChangeListener

,

createSouthPane

,

createWestPane

,

deactivateFrame

,

deiconifyFrame

,

deinstallMouseHandlers

,

getDesktopManager

,

getEastPane

,

getMaximumSize

,

getMinimumSize

,

getNorthPane

,

getPreferredSize

,

getSouthPane

,

getWestPane

,

iconifyFrame

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installMouseHandlers

,

installUI

,

isKeyBindingActive

,

isKeyBindingRegistered

,

maximizeFrame

,

minimizeFrame

,

replacePane

,

setEastPane

,

setKeyBindingActive

,

setKeyBindingRegistered

,

setNorthPane

,

setSouthPane

,

setupMenuCloseKey

,

setupMenuOpenKey

,

setWestPane

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

---

#### Methods declared in class javax.swing.plaf.basic. BasicInternalFrameUI

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

paint

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

- IS_PALETTE

```java
protected static
String
IS_PALETTE
```

The property

JInternalFrame.isPalette

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalInternalFrameUI

```java
public MetalInternalFrameUI​(
JInternalFrame
b)
```

Constructs a new

MetalInternalFrameUI

instance.

**Parameters:** b

- an internal frame

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

Constructs a new

MetalInternalFrameUI

instance.

**Parameters:** c

- a component
**Returns:** a new

MetalInternalFrameUI

instance

- setPalette

```java
public void setPalette​(boolean isPalette)
```

If

isPalette

is

true

, sets palette border and title

**Parameters:** isPalette

- if

true

, sets palette border and title

- createBorderListener

```java
protected
MouseInputAdapter
createBorderListener​(
JInternalFrame
w)
```

Returns the

MouseInputAdapter

that will be installed
on the TitlePane.

**Overrides:** createBorderListener

in class

BasicInternalFrameUI
**Parameters:** w

- the

JInternalFrame
**Returns:** the

MouseInputAdapter

that will be installed
on the TitlePane.
**Since:** 1.6

Field Detail

- IS_PALETTE

```java
protected static
String
IS_PALETTE
```

The property

JInternalFrame.isPalette

.

---

#### Field Detail

IS_PALETTE

```java
protected static
String
IS_PALETTE
```

The property

JInternalFrame.isPalette

.

---

#### IS_PALETTE

protected static

String

IS_PALETTE

The property

JInternalFrame.isPalette

.

Constructor Detail

- MetalInternalFrameUI

```java
public MetalInternalFrameUI​(
JInternalFrame
b)
```

Constructs a new

MetalInternalFrameUI

instance.

**Parameters:** b

- an internal frame

---

#### Constructor Detail

MetalInternalFrameUI

```java
public MetalInternalFrameUI​(
JInternalFrame
b)
```

Constructs a new

MetalInternalFrameUI

instance.

**Parameters:** b

- an internal frame

---

#### MetalInternalFrameUI

public MetalInternalFrameUI​(

JInternalFrame

b)

Constructs a new

MetalInternalFrameUI

instance.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new

MetalInternalFrameUI

instance.

**Parameters:** c

- a component
**Returns:** a new

MetalInternalFrameUI

instance

- setPalette

```java
public void setPalette​(boolean isPalette)
```

If

isPalette

is

true

, sets palette border and title

**Parameters:** isPalette

- if

true

, sets palette border and title

- createBorderListener

```java
protected
MouseInputAdapter
createBorderListener​(
JInternalFrame
w)
```

Returns the

MouseInputAdapter

that will be installed
on the TitlePane.

**Overrides:** createBorderListener

in class

BasicInternalFrameUI
**Parameters:** w

- the

JInternalFrame
**Returns:** the

MouseInputAdapter

that will be installed
on the TitlePane.
**Since:** 1.6

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

Constructs a new

MetalInternalFrameUI

instance.

**Parameters:** c

- a component
**Returns:** a new

MetalInternalFrameUI

instance

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs a new

MetalInternalFrameUI

instance.

setPalette

```java
public void setPalette​(boolean isPalette)
```

If

isPalette

is

true

, sets palette border and title

**Parameters:** isPalette

- if

true

, sets palette border and title

---

#### setPalette

public void setPalette​(boolean isPalette)

If

isPalette

is

true

, sets palette border and title

createBorderListener

```java
protected
MouseInputAdapter
createBorderListener​(
JInternalFrame
w)
```

Returns the

MouseInputAdapter

that will be installed
on the TitlePane.

**Overrides:** createBorderListener

in class

BasicInternalFrameUI
**Parameters:** w

- the

JInternalFrame
**Returns:** the

MouseInputAdapter

that will be installed
on the TitlePane.
**Since:** 1.6

---

#### createBorderListener

protected

MouseInputAdapter

createBorderListener​(

JInternalFrame

w)

Returns the

MouseInputAdapter

that will be installed
on the TitlePane.

---

