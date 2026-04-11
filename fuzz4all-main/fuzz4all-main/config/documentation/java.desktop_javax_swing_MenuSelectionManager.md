# Class MenuSelectionManager

**Source:** `java.desktop\javax\swing\MenuSelectionManager.html`

### Class Description

```java
public class
MenuSelectionManager

extends
Object
```

A MenuSelectionManager owns the selection in menu hierarchy.

**Since:** 1.2

---

### Field Details

#### protected transient
ChangeEvent
changeEvent

Only one ChangeEvent is needed per button model instance since the
event's only state is the source property. The source of events
generated is always "this".

---

#### protected
EventListenerList
listenerList

The collection of registered listeners

---

### Constructor Details

#### public MenuSelectionManager()

*No description found.*

---

### Method Details

#### public static
MenuSelectionManager
defaultManager()

Returns the default menu selection manager.

**Returns:**
- a MenuSelectionManager object

---

#### public void setSelectedPath​(
MenuElement
[] path)

Changes the selection in the menu hierarchy. The elements
in the array are sorted in order from the root menu
element to the currently selected menu element.

Note that this method is public but is used by the look and
feel engine and should not be called by client applications.

**Parameters:**
- path

- an array of

MenuElement

objects specifying
the selected path

---

#### public
MenuElement
[] getSelectedPath()

Returns the path to the currently selected menu item

**Returns:**
- an array of MenuElement objects representing the selected path

---

#### public void clearSelectedPath()

Tell the menu selection to close and unselect all the menu components. Call this method
when a choice has been made

---

#### public void addChangeListener​(
ChangeListener
l)

Adds a ChangeListener to the button.

**Parameters:**
- l

- the listener to add

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a ChangeListener from the button.

**Parameters:**
- l

- the listener to remove

---

#### public
ChangeListener
[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this MenuSelectionManager with addChangeListener().

**Returns:**
- all of the

ChangeListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:**
- EventListenerList

---

#### public void processMouseEvent​(
MouseEvent
event)

When a MenuElement receives an event from a MouseListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

**Parameters:**
- event

- a MouseEvent object

---

#### public
Component
componentForPoint​(
Component
source,

Point
sourcePoint)

Returns the component in the currently selected path
which contains sourcePoint.

**Parameters:**
- source

- The component in whose coordinate space sourcePoint
is given
- sourcePoint

- The point which is being tested

**Returns:**
- The component in the currently selected path which
contains sourcePoint (relative to the source component's
coordinate space. If sourcePoint is not inside a component
on the currently selected path, null is returned.

---

#### public void processKeyEvent​(
KeyEvent
e)

When a MenuElement receives an event from a KeyListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

**Parameters:**
- e

- a KeyEvent object

---

#### public boolean isComponentPartOfCurrentMenu​(
Component
c)

Return true if

c

is part of the currently used menu

**Parameters:**
- c

- a

Component

**Returns:**
- true if

c

is part of the currently used menu,
false otherwise

---

### Additional Sections

#### Class MenuSelectionManager

java.lang.Object

- javax.swing.MenuSelectionManager

javax.swing.MenuSelectionManager

```java
public class
MenuSelectionManager

extends
Object
```

A MenuSelectionManager owns the selection in menu hierarchy.

**Since:** 1.2

public class

MenuSelectionManager

extends

Object

A MenuSelectionManager owns the selection in menu hierarchy.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeEvent

changeEvent

Only one ChangeEvent is needed per button model instance since the
event's only state is the source property.

protected

EventListenerList

listenerList

The collection of registered listeners

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MenuSelectionManager

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

void

addChangeListener

​(

ChangeListener

l)

Adds a ChangeListener to the button.

void

clearSelectedPath

()

Tell the menu selection to close and unselect all the menu components.

Component

componentForPoint

​(

Component

source,

Point

sourcePoint)

Returns the component in the currently selected path
which contains sourcePoint.

static

MenuSelectionManager

defaultManager

()

Returns the default menu selection manager.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this MenuSelectionManager with addChangeListener().

MenuElement

[]

getSelectedPath

()

Returns the path to the currently selected menu item

boolean

isComponentPartOfCurrentMenu

​(

Component

c)

Return true if

c

is part of the currently used menu

void

processKeyEvent

​(

KeyEvent

e)

When a MenuElement receives an event from a KeyListener, it should never process the event
directly.

void

processMouseEvent

​(

MouseEvent

event)

When a MenuElement receives an event from a MouseListener, it should never process the event
directly.

void

removeChangeListener

​(

ChangeListener

l)

Removes a ChangeListener from the button.

void

setSelectedPath

​(

MenuElement

[] path)

Changes the selection in the menu hierarchy.

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

ChangeEvent

changeEvent

Only one ChangeEvent is needed per button model instance since the
event's only state is the source property.

protected

EventListenerList

listenerList

The collection of registered listeners

---

#### Field Summary

Only one ChangeEvent is needed per button model instance since the
event's only state is the source property.

The collection of registered listeners

Constructor Summary

Constructors

Constructor

Description

MenuSelectionManager

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

void

addChangeListener

​(

ChangeListener

l)

Adds a ChangeListener to the button.

void

clearSelectedPath

()

Tell the menu selection to close and unselect all the menu components.

Component

componentForPoint

​(

Component

source,

Point

sourcePoint)

Returns the component in the currently selected path
which contains sourcePoint.

static

MenuSelectionManager

defaultManager

()

Returns the default menu selection manager.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this MenuSelectionManager with addChangeListener().

MenuElement

[]

getSelectedPath

()

Returns the path to the currently selected menu item

boolean

isComponentPartOfCurrentMenu

​(

Component

c)

Return true if

c

is part of the currently used menu

void

processKeyEvent

​(

KeyEvent

e)

When a MenuElement receives an event from a KeyListener, it should never process the event
directly.

void

processMouseEvent

​(

MouseEvent

event)

When a MenuElement receives an event from a MouseListener, it should never process the event
directly.

void

removeChangeListener

​(

ChangeListener

l)

Removes a ChangeListener from the button.

void

setSelectedPath

​(

MenuElement

[] path)

Changes the selection in the menu hierarchy.

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

Adds a ChangeListener to the button.

Tell the menu selection to close and unselect all the menu components.

Returns the component in the currently selected path
which contains sourcePoint.

Returns the default menu selection manager.

Notifies all listeners that have registered interest for
notification on this event type.

Returns an array of all the

ChangeListener

s added
to this MenuSelectionManager with addChangeListener().

Returns the path to the currently selected menu item

Return true if

c

is part of the currently used menu

When a MenuElement receives an event from a KeyListener, it should never process the event
directly.

When a MenuElement receives an event from a MouseListener, it should never process the event
directly.

Removes a ChangeListener from the button.

Changes the selection in the menu hierarchy.

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

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one ChangeEvent is needed per button model instance since the
event's only state is the source property. The source of events
generated is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

The collection of registered listeners

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MenuSelectionManager

```java
public MenuSelectionManager()
```

============ METHOD DETAIL ==========

- Method Detail

- defaultManager

```java
public static
MenuSelectionManager
defaultManager()
```

Returns the default menu selection manager.

**Returns:** a MenuSelectionManager object

- setSelectedPath

```java
public void setSelectedPath​(
MenuElement
[] path)
```

Changes the selection in the menu hierarchy. The elements
in the array are sorted in order from the root menu
element to the currently selected menu element.

Note that this method is public but is used by the look and
feel engine and should not be called by client applications.

**Parameters:** path

- an array of

MenuElement

objects specifying
the selected path

- getSelectedPath

```java
public
MenuElement
[] getSelectedPath()
```

Returns the path to the currently selected menu item

**Returns:** an array of MenuElement objects representing the selected path

- clearSelectedPath

```java
public void clearSelectedPath()
```

Tell the menu selection to close and unselect all the menu components. Call this method
when a choice has been made

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a ChangeListener to the button.

**Parameters:** l

- the listener to add

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the button.

**Parameters:** l

- the listener to remove

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this MenuSelectionManager with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

- processMouseEvent

```java
public void processMouseEvent​(
MouseEvent
event)
```

When a MenuElement receives an event from a MouseListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

**Parameters:** event

- a MouseEvent object

- componentForPoint

```java
public
Component
componentForPoint​(
Component
source,

Point
sourcePoint)
```

Returns the component in the currently selected path
which contains sourcePoint.

**Parameters:** source

- The component in whose coordinate space sourcePoint
is given
**Parameters:** sourcePoint

- The point which is being tested
**Returns:** The component in the currently selected path which
contains sourcePoint (relative to the source component's
coordinate space. If sourcePoint is not inside a component
on the currently selected path, null is returned.

- processKeyEvent

```java
public void processKeyEvent​(
KeyEvent
e)
```

When a MenuElement receives an event from a KeyListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

**Parameters:** e

- a KeyEvent object

- isComponentPartOfCurrentMenu

```java
public boolean isComponentPartOfCurrentMenu​(
Component
c)
```

Return true if

c

is part of the currently used menu

**Parameters:** c

- a

Component
**Returns:** true if

c

is part of the currently used menu,
false otherwise

Field Detail

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one ChangeEvent is needed per button model instance since the
event's only state is the source property. The source of events
generated is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

The collection of registered listeners

---

#### Field Detail

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one ChangeEvent is needed per button model instance since the
event's only state is the source property. The source of events
generated is always "this".

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Only one ChangeEvent is needed per button model instance since the
event's only state is the source property. The source of events
generated is always "this".

listenerList

```java
protected
EventListenerList
listenerList
```

The collection of registered listeners

---

#### listenerList

protected

EventListenerList

listenerList

The collection of registered listeners

Constructor Detail

- MenuSelectionManager

```java
public MenuSelectionManager()
```

---

#### Constructor Detail

MenuSelectionManager

```java
public MenuSelectionManager()
```

---

#### MenuSelectionManager

public MenuSelectionManager()

Method Detail

- defaultManager

```java
public static
MenuSelectionManager
defaultManager()
```

Returns the default menu selection manager.

**Returns:** a MenuSelectionManager object

- setSelectedPath

```java
public void setSelectedPath​(
MenuElement
[] path)
```

Changes the selection in the menu hierarchy. The elements
in the array are sorted in order from the root menu
element to the currently selected menu element.

Note that this method is public but is used by the look and
feel engine and should not be called by client applications.

**Parameters:** path

- an array of

MenuElement

objects specifying
the selected path

- getSelectedPath

```java
public
MenuElement
[] getSelectedPath()
```

Returns the path to the currently selected menu item

**Returns:** an array of MenuElement objects representing the selected path

- clearSelectedPath

```java
public void clearSelectedPath()
```

Tell the menu selection to close and unselect all the menu components. Call this method
when a choice has been made

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a ChangeListener to the button.

**Parameters:** l

- the listener to add

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the button.

**Parameters:** l

- the listener to remove

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this MenuSelectionManager with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

- processMouseEvent

```java
public void processMouseEvent​(
MouseEvent
event)
```

When a MenuElement receives an event from a MouseListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

**Parameters:** event

- a MouseEvent object

- componentForPoint

```java
public
Component
componentForPoint​(
Component
source,

Point
sourcePoint)
```

Returns the component in the currently selected path
which contains sourcePoint.

**Parameters:** source

- The component in whose coordinate space sourcePoint
is given
**Parameters:** sourcePoint

- The point which is being tested
**Returns:** The component in the currently selected path which
contains sourcePoint (relative to the source component's
coordinate space. If sourcePoint is not inside a component
on the currently selected path, null is returned.

- processKeyEvent

```java
public void processKeyEvent​(
KeyEvent
e)
```

When a MenuElement receives an event from a KeyListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

**Parameters:** e

- a KeyEvent object

- isComponentPartOfCurrentMenu

```java
public boolean isComponentPartOfCurrentMenu​(
Component
c)
```

Return true if

c

is part of the currently used menu

**Parameters:** c

- a

Component
**Returns:** true if

c

is part of the currently used menu,
false otherwise

---

#### Method Detail

defaultManager

```java
public static
MenuSelectionManager
defaultManager()
```

Returns the default menu selection manager.

**Returns:** a MenuSelectionManager object

---

#### defaultManager

public static

MenuSelectionManager

defaultManager()

Returns the default menu selection manager.

setSelectedPath

```java
public void setSelectedPath​(
MenuElement
[] path)
```

Changes the selection in the menu hierarchy. The elements
in the array are sorted in order from the root menu
element to the currently selected menu element.

Note that this method is public but is used by the look and
feel engine and should not be called by client applications.

**Parameters:** path

- an array of

MenuElement

objects specifying
the selected path

---

#### setSelectedPath

public void setSelectedPath​(

MenuElement

[] path)

Changes the selection in the menu hierarchy. The elements
in the array are sorted in order from the root menu
element to the currently selected menu element.

Note that this method is public but is used by the look and
feel engine and should not be called by client applications.

Note that this method is public but is used by the look and
feel engine and should not be called by client applications.

getSelectedPath

```java
public
MenuElement
[] getSelectedPath()
```

Returns the path to the currently selected menu item

**Returns:** an array of MenuElement objects representing the selected path

---

#### getSelectedPath

public

MenuElement

[] getSelectedPath()

Returns the path to the currently selected menu item

clearSelectedPath

```java
public void clearSelectedPath()
```

Tell the menu selection to close and unselect all the menu components. Call this method
when a choice has been made

---

#### clearSelectedPath

public void clearSelectedPath()

Tell the menu selection to close and unselect all the menu components. Call this method
when a choice has been made

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a ChangeListener to the button.

**Parameters:** l

- the listener to add

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a ChangeListener to the button.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the button.

**Parameters:** l

- the listener to remove

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a ChangeListener from the button.

getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this MenuSelectionManager with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getChangeListeners

public

ChangeListener

[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this MenuSelectionManager with addChangeListener().

fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

processMouseEvent

```java
public void processMouseEvent​(
MouseEvent
event)
```

When a MenuElement receives an event from a MouseListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

**Parameters:** event

- a MouseEvent object

---

#### processMouseEvent

public void processMouseEvent​(

MouseEvent

event)

When a MenuElement receives an event from a MouseListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

componentForPoint

```java
public
Component
componentForPoint​(
Component
source,

Point
sourcePoint)
```

Returns the component in the currently selected path
which contains sourcePoint.

**Parameters:** source

- The component in whose coordinate space sourcePoint
is given
**Parameters:** sourcePoint

- The point which is being tested
**Returns:** The component in the currently selected path which
contains sourcePoint (relative to the source component's
coordinate space. If sourcePoint is not inside a component
on the currently selected path, null is returned.

---

#### componentForPoint

public

Component

componentForPoint​(

Component

source,

Point

sourcePoint)

Returns the component in the currently selected path
which contains sourcePoint.

processKeyEvent

```java
public void processKeyEvent​(
KeyEvent
e)
```

When a MenuElement receives an event from a KeyListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

**Parameters:** e

- a KeyEvent object

---

#### processKeyEvent

public void processKeyEvent​(

KeyEvent

e)

When a MenuElement receives an event from a KeyListener, it should never process the event
directly. Instead all MenuElements should call this method with the event.

isComponentPartOfCurrentMenu

```java
public boolean isComponentPartOfCurrentMenu​(
Component
c)
```

Return true if

c

is part of the currently used menu

**Parameters:** c

- a

Component
**Returns:** true if

c

is part of the currently used menu,
false otherwise

---

#### isComponentPartOfCurrentMenu

public boolean isComponentPartOfCurrentMenu​(

Component

c)

Return true if

c

is part of the currently used menu

---

