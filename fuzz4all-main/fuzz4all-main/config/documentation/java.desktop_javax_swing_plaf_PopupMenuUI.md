# Class PopupMenuUI

**Source:** `java.desktop\javax\swing\plaf\PopupMenuUI.html`

### Class Description

```java
public abstract class
PopupMenuUI

extends
ComponentUI
```

Pluggable look and feel interface for JPopupMenu.

**Direct Known Subclasses:** BasicPopupMenuUI

,

MultiPopupMenuUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public PopupMenuUI()

*No description found.*

---

### Method Details

#### public boolean isPopupTrigger​(
MouseEvent
e)

Returns whether or not the given

MouseEvent

is the popup menu
trigger event for the platform

**Parameters:**
- e

- a

MouseEvent

**Returns:**
- true if the

MouseEvent e

is the popup menu trigger

**Since:**
- 1.3

---

#### public
Popup
getPopup​(
JPopupMenu
popup,
int x,
int y)

Returns the

Popup

that will be responsible for
displaying the

JPopupMenu

.

**Parameters:**
- popup

- JPopupMenu requesting Popup
- x

- Screen x location Popup is to be shown at
- y

- Screen y location Popup is to be shown at.

**Returns:**
- Popup that will show the JPopupMenu

**Since:**
- 1.4

---

### Additional Sections

#### Class PopupMenuUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.PopupMenuUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.PopupMenuUI

javax.swing.plaf.PopupMenuUI

**Direct Known Subclasses:** BasicPopupMenuUI

,

MultiPopupMenuUI

```java
public abstract class
PopupMenuUI

extends
ComponentUI
```

Pluggable look and feel interface for JPopupMenu.

public abstract class

PopupMenuUI

extends

ComponentUI

Pluggable look and feel interface for JPopupMenu.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PopupMenuUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Popup

getPopup

​(

JPopupMenu

popup,
int x,
int y)

Returns the

Popup

that will be responsible for
displaying the

JPopupMenu

.

boolean

isPopupTrigger

​(

MouseEvent

e)

Returns whether or not the given

MouseEvent

is the popup menu
trigger event for the platform

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

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

PopupMenuUI

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Popup

getPopup

​(

JPopupMenu

popup,
int x,
int y)

Returns the

Popup

that will be responsible for
displaying the

JPopupMenu

.

boolean

isPopupTrigger

​(

MouseEvent

e)

Returns whether or not the given

MouseEvent

is the popup menu
trigger event for the platform

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

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

Popup

that will be responsible for
displaying the

JPopupMenu

.

Returns whether or not the given

MouseEvent

is the popup menu
trigger event for the platform

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

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

- PopupMenuUI

```java
public PopupMenuUI()
```

============ METHOD DETAIL ==========

- Method Detail

- isPopupTrigger

```java
public boolean isPopupTrigger​(
MouseEvent
e)
```

Returns whether or not the given

MouseEvent

is the popup menu
trigger event for the platform

**Parameters:** e

- a

MouseEvent
**Returns:** true if the

MouseEvent e

is the popup menu trigger
**Since:** 1.3

- getPopup

```java
public
Popup
getPopup​(
JPopupMenu
popup,
int x,
int y)
```

Returns the

Popup

that will be responsible for
displaying the

JPopupMenu

.

**Parameters:** popup

- JPopupMenu requesting Popup
**Parameters:** x

- Screen x location Popup is to be shown at
**Parameters:** y

- Screen y location Popup is to be shown at.
**Returns:** Popup that will show the JPopupMenu
**Since:** 1.4

Constructor Detail

- PopupMenuUI

```java
public PopupMenuUI()
```

---

#### Constructor Detail

PopupMenuUI

```java
public PopupMenuUI()
```

---

#### PopupMenuUI

public PopupMenuUI()

Method Detail

- isPopupTrigger

```java
public boolean isPopupTrigger​(
MouseEvent
e)
```

Returns whether or not the given

MouseEvent

is the popup menu
trigger event for the platform

**Parameters:** e

- a

MouseEvent
**Returns:** true if the

MouseEvent e

is the popup menu trigger
**Since:** 1.3

- getPopup

```java
public
Popup
getPopup​(
JPopupMenu
popup,
int x,
int y)
```

Returns the

Popup

that will be responsible for
displaying the

JPopupMenu

.

**Parameters:** popup

- JPopupMenu requesting Popup
**Parameters:** x

- Screen x location Popup is to be shown at
**Parameters:** y

- Screen y location Popup is to be shown at.
**Returns:** Popup that will show the JPopupMenu
**Since:** 1.4

---

#### Method Detail

isPopupTrigger

```java
public boolean isPopupTrigger​(
MouseEvent
e)
```

Returns whether or not the given

MouseEvent

is the popup menu
trigger event for the platform

**Parameters:** e

- a

MouseEvent
**Returns:** true if the

MouseEvent e

is the popup menu trigger
**Since:** 1.3

---

#### isPopupTrigger

public boolean isPopupTrigger​(

MouseEvent

e)

Returns whether or not the given

MouseEvent

is the popup menu
trigger event for the platform

getPopup

```java
public
Popup
getPopup​(
JPopupMenu
popup,
int x,
int y)
```

Returns the

Popup

that will be responsible for
displaying the

JPopupMenu

.

**Parameters:** popup

- JPopupMenu requesting Popup
**Parameters:** x

- Screen x location Popup is to be shown at
**Parameters:** y

- Screen y location Popup is to be shown at.
**Returns:** Popup that will show the JPopupMenu
**Since:** 1.4

---

#### getPopup

public

Popup

getPopup​(

JPopupMenu

popup,
int x,
int y)

Returns the

Popup

that will be responsible for
displaying the

JPopupMenu

.

---

