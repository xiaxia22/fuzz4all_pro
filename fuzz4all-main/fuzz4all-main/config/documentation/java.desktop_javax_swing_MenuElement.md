# Interface MenuElement

**Source:** `java.desktop\javax\swing\MenuElement.html`

### Class Description

```java
public interface
MenuElement
```

Any component that can be placed into a menu should implement this interface.
This interface is used by

MenuSelectionManager

to handle selection and navigation in menu hierarchies.

**All Known Implementing Classes:** BasicComboPopup

,

BasicInternalFrameTitlePane.SystemMenuBar

,

JCheckBoxMenuItem

,

JMenu

,

JMenuBar

,

JMenuItem

,

JPopupMenu

,

JRadioButtonMenuItem

,

MetalComboBoxUI.MetalComboPopup

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void processMouseEvent​(
MouseEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)

Processes a mouse event.

event

is a

MouseEvent

with
source being the receiving element's component.

path

is the
path of the receiving element in the menu hierarchy including the
receiving element itself.

manager

is the

MenuSelectionManager

for the menu hierarchy. This method should
process the

MouseEvent

and change the menu selection if necessary
by using

MenuSelectionManager

's API Note: you do not have to
forward the event to sub-components. This is done automatically by the

MenuSelectionManager

.

**Parameters:**
- event

- a

MouseEvent

to be processed
- path

- the path of the receiving element in the menu hierarchy
- manager

- the

MenuSelectionManager

for the menu hierarchy

---

#### void processKeyEvent​(
KeyEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)

Process a key event.

**Parameters:**
- event

- a

KeyEvent

to be processed
- path

- the path of the receiving element in the menu hierarchy
- manager

- the

MenuSelectionManager

for the menu hierarchy

---

#### void menuSelectionChanged​(boolean isIncluded)

Call by the

MenuSelectionManager

when the

MenuElement

is
added or removed from the menu selection.

**Parameters:**
- isIncluded

- can be used to indicate if this

MenuElement

is
active (if it is a menu) or is on the part of the menu path that
changed (if it is a menu item).

---

#### MenuElement
[] getSubElements()

This method should return an array containing the sub-elements for the
receiving menu element.

**Returns:**
- an array of

MenuElement

s

---

#### Component
getComponent()

This method should return the

java.awt.Component

used to paint the
receiving element. The returned component will be used to convert events
and detect if an event is inside a

MenuElement

's component.

**Returns:**
- the

Component

value

---

### Additional Sections

#### Interface MenuElement

**All Known Implementing Classes:** BasicComboPopup

,

BasicInternalFrameTitlePane.SystemMenuBar

,

JCheckBoxMenuItem

,

JMenu

,

JMenuBar

,

JMenuItem

,

JPopupMenu

,

JRadioButtonMenuItem

,

MetalComboBoxUI.MetalComboPopup

```java
public interface
MenuElement
```

Any component that can be placed into a menu should implement this interface.
This interface is used by

MenuSelectionManager

to handle selection and navigation in menu hierarchies.

**Since:** 1.2

public interface

MenuElement

Any component that can be placed into a menu should implement this interface.
This interface is used by

MenuSelectionManager

to handle selection and navigation in menu hierarchies.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getComponent

()

This method should return the

java.awt.Component

used to paint the
receiving element.

MenuElement

[]

getSubElements

()

This method should return an array containing the sub-elements for the
receiving menu element.

void

menuSelectionChanged

​(boolean isIncluded)

Call by the

MenuSelectionManager

when the

MenuElement

is
added or removed from the menu selection.

void

processKeyEvent

​(

KeyEvent

event,

MenuElement

[] path,

MenuSelectionManager

manager)

Process a key event.

void

processMouseEvent

​(

MouseEvent

event,

MenuElement

[] path,

MenuSelectionManager

manager)

Processes a mouse event.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getComponent

()

This method should return the

java.awt.Component

used to paint the
receiving element.

MenuElement

[]

getSubElements

()

This method should return an array containing the sub-elements for the
receiving menu element.

void

menuSelectionChanged

​(boolean isIncluded)

Call by the

MenuSelectionManager

when the

MenuElement

is
added or removed from the menu selection.

void

processKeyEvent

​(

KeyEvent

event,

MenuElement

[] path,

MenuSelectionManager

manager)

Process a key event.

void

processMouseEvent

​(

MouseEvent

event,

MenuElement

[] path,

MenuSelectionManager

manager)

Processes a mouse event.

---

#### Method Summary

This method should return the

java.awt.Component

used to paint the
receiving element.

This method should return an array containing the sub-elements for the
receiving menu element.

Call by the

MenuSelectionManager

when the

MenuElement

is
added or removed from the menu selection.

Process a key event.

Processes a mouse event.

============ METHOD DETAIL ==========

- Method Detail

- processMouseEvent

```java
void processMouseEvent​(
MouseEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)
```

Processes a mouse event.

event

is a

MouseEvent

with
source being the receiving element's component.

path

is the
path of the receiving element in the menu hierarchy including the
receiving element itself.

manager

is the

MenuSelectionManager

for the menu hierarchy. This method should
process the

MouseEvent

and change the menu selection if necessary
by using

MenuSelectionManager

's API Note: you do not have to
forward the event to sub-components. This is done automatically by the

MenuSelectionManager

.

**Parameters:** event

- a

MouseEvent

to be processed
**Parameters:** path

- the path of the receiving element in the menu hierarchy
**Parameters:** manager

- the

MenuSelectionManager

for the menu hierarchy

- processKeyEvent

```java
void processKeyEvent​(
KeyEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)
```

Process a key event.

**Parameters:** event

- a

KeyEvent

to be processed
**Parameters:** path

- the path of the receiving element in the menu hierarchy
**Parameters:** manager

- the

MenuSelectionManager

for the menu hierarchy

- menuSelectionChanged

```java
void menuSelectionChanged​(boolean isIncluded)
```

Call by the

MenuSelectionManager

when the

MenuElement

is
added or removed from the menu selection.

**Parameters:** isIncluded

- can be used to indicate if this

MenuElement

is
active (if it is a menu) or is on the part of the menu path that
changed (if it is a menu item).

- getSubElements

```java
MenuElement
[] getSubElements()
```

This method should return an array containing the sub-elements for the
receiving menu element.

**Returns:** an array of

MenuElement

s

- getComponent

```java
Component
getComponent()
```

This method should return the

java.awt.Component

used to paint the
receiving element. The returned component will be used to convert events
and detect if an event is inside a

MenuElement

's component.

**Returns:** the

Component

value

Method Detail

- processMouseEvent

```java
void processMouseEvent​(
MouseEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)
```

Processes a mouse event.

event

is a

MouseEvent

with
source being the receiving element's component.

path

is the
path of the receiving element in the menu hierarchy including the
receiving element itself.

manager

is the

MenuSelectionManager

for the menu hierarchy. This method should
process the

MouseEvent

and change the menu selection if necessary
by using

MenuSelectionManager

's API Note: you do not have to
forward the event to sub-components. This is done automatically by the

MenuSelectionManager

.

**Parameters:** event

- a

MouseEvent

to be processed
**Parameters:** path

- the path of the receiving element in the menu hierarchy
**Parameters:** manager

- the

MenuSelectionManager

for the menu hierarchy

- processKeyEvent

```java
void processKeyEvent​(
KeyEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)
```

Process a key event.

**Parameters:** event

- a

KeyEvent

to be processed
**Parameters:** path

- the path of the receiving element in the menu hierarchy
**Parameters:** manager

- the

MenuSelectionManager

for the menu hierarchy

- menuSelectionChanged

```java
void menuSelectionChanged​(boolean isIncluded)
```

Call by the

MenuSelectionManager

when the

MenuElement

is
added or removed from the menu selection.

**Parameters:** isIncluded

- can be used to indicate if this

MenuElement

is
active (if it is a menu) or is on the part of the menu path that
changed (if it is a menu item).

- getSubElements

```java
MenuElement
[] getSubElements()
```

This method should return an array containing the sub-elements for the
receiving menu element.

**Returns:** an array of

MenuElement

s

- getComponent

```java
Component
getComponent()
```

This method should return the

java.awt.Component

used to paint the
receiving element. The returned component will be used to convert events
and detect if an event is inside a

MenuElement

's component.

**Returns:** the

Component

value

---

#### Method Detail

processMouseEvent

```java
void processMouseEvent​(
MouseEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)
```

Processes a mouse event.

event

is a

MouseEvent

with
source being the receiving element's component.

path

is the
path of the receiving element in the menu hierarchy including the
receiving element itself.

manager

is the

MenuSelectionManager

for the menu hierarchy. This method should
process the

MouseEvent

and change the menu selection if necessary
by using

MenuSelectionManager

's API Note: you do not have to
forward the event to sub-components. This is done automatically by the

MenuSelectionManager

.

**Parameters:** event

- a

MouseEvent

to be processed
**Parameters:** path

- the path of the receiving element in the menu hierarchy
**Parameters:** manager

- the

MenuSelectionManager

for the menu hierarchy

---

#### processMouseEvent

void processMouseEvent​(

MouseEvent

event,

MenuElement

[] path,

MenuSelectionManager

manager)

Processes a mouse event.

event

is a

MouseEvent

with
source being the receiving element's component.

path

is the
path of the receiving element in the menu hierarchy including the
receiving element itself.

manager

is the

MenuSelectionManager

for the menu hierarchy. This method should
process the

MouseEvent

and change the menu selection if necessary
by using

MenuSelectionManager

's API Note: you do not have to
forward the event to sub-components. This is done automatically by the

MenuSelectionManager

.

processKeyEvent

```java
void processKeyEvent​(
KeyEvent
event,

MenuElement
[] path,

MenuSelectionManager
manager)
```

Process a key event.

**Parameters:** event

- a

KeyEvent

to be processed
**Parameters:** path

- the path of the receiving element in the menu hierarchy
**Parameters:** manager

- the

MenuSelectionManager

for the menu hierarchy

---

#### processKeyEvent

void processKeyEvent​(

KeyEvent

event,

MenuElement

[] path,

MenuSelectionManager

manager)

Process a key event.

menuSelectionChanged

```java
void menuSelectionChanged​(boolean isIncluded)
```

Call by the

MenuSelectionManager

when the

MenuElement

is
added or removed from the menu selection.

**Parameters:** isIncluded

- can be used to indicate if this

MenuElement

is
active (if it is a menu) or is on the part of the menu path that
changed (if it is a menu item).

---

#### menuSelectionChanged

void menuSelectionChanged​(boolean isIncluded)

Call by the

MenuSelectionManager

when the

MenuElement

is
added or removed from the menu selection.

getSubElements

```java
MenuElement
[] getSubElements()
```

This method should return an array containing the sub-elements for the
receiving menu element.

**Returns:** an array of

MenuElement

s

---

#### getSubElements

MenuElement

[] getSubElements()

This method should return an array containing the sub-elements for the
receiving menu element.

getComponent

```java
Component
getComponent()
```

This method should return the

java.awt.Component

used to paint the
receiving element. The returned component will be used to convert events
and detect if an event is inside a

MenuElement

's component.

**Returns:** the

Component

value

---

#### getComponent

Component

getComponent()

This method should return the

java.awt.Component

used to paint the
receiving element. The returned component will be used to convert events
and detect if an event is inside a

MenuElement

's component.

---

