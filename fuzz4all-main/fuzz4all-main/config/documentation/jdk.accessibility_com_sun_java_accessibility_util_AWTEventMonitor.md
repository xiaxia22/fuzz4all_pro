# Class AWTEventMonitor

**Source:** `jdk.accessibility\com\sun\java\accessibility\util\AWTEventMonitor.html`

### Class Description

```java
public class
AWTEventMonitor

extends
Object
```

The

AWTEventMonitor

implements a suite of listeners that are
conditionally installed on every AWT component instance in the Java
Virtual Machine. The events captured by these listeners are made
available through a unified set of listeners supported by

AWTEventMonitor

.
With this, all the individual events on each of the AWT component
instances are funneled into one set of listeners broken down by category
(see

EventID

for the categories).

This class depends upon

EventQueueMonitor

, which provides the base
level support for capturing the top-level containers as they are created.

**Direct Known Subclasses:** SwingEventMonitor

---

### Field Details

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
Component
componentWithFocus

The current component with keyboard focus.

**See Also:**
- getComponentWithFocus()

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
ComponentListener
componentListener

The current list of registered ComponentListener classes.

**See Also:**
- addComponentListener(java.awt.event.ComponentListener)

,

removeComponentListener(java.awt.event.ComponentListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
ContainerListener
containerListener

The current list of registered ContainerListener classes.

**See Also:**
- addContainerListener(java.awt.event.ContainerListener)

,

removeContainerListener(java.awt.event.ContainerListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
FocusListener
focusListener

The current list of registered FocusListener classes.

**See Also:**
- addFocusListener(java.awt.event.FocusListener)

,

removeFocusListener(java.awt.event.FocusListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
KeyListener
keyListener

The current list of registered KeyListener classes.

**See Also:**
- addKeyListener(java.awt.event.KeyListener)

,

removeKeyListener(java.awt.event.KeyListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
MouseListener
mouseListener

The current list of registered MouseListener classes.

**See Also:**
- addMouseListener(java.awt.event.MouseListener)

,

removeMouseListener(java.awt.event.MouseListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
MouseMotionListener
mouseMotionListener

The current list of registered MouseMotionListener classes.

**See Also:**
- addMouseMotionListener(java.awt.event.MouseMotionListener)

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
WindowListener
windowListener

The current list of registered WindowListener classes.

**See Also:**
- addWindowListener(java.awt.event.WindowListener)

,

removeWindowListener(java.awt.event.WindowListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
ActionListener
actionListener

The current list of registered ActionListener classes.

**See Also:**
- addActionListener(java.awt.event.ActionListener)

,

removeActionListener(java.awt.event.ActionListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
AdjustmentListener
adjustmentListener

The current list of registered AdjustmentListener classes.

**See Also:**
- addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
ItemListener
itemListener

The current list of registered ItemListener classes.

**See Also:**
- addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

---

#### @Deprecated
(
since
="8",

forRemoval
=true)
protected static
TextListener
textListener

The current list of registered TextListener classes.

**See Also:**
- addTextListener(java.awt.event.TextListener)

,

removeTextListener(java.awt.event.TextListener)

---

### Constructor Details

#### public AWTEventMonitor()

*No description found.*

---

### Method Details

#### public static
Component
getComponentWithFocus()

Returns the component that currently has keyboard focus. The return
value can be null.

**Returns:**
- the component that has keyboard focus

---

#### public static void addComponentListener​(
ComponentListener
l)

Adds the specified listener to receive all

COMPONENT

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeComponentListener(java.awt.event.ComponentListener)

---

#### public static void removeComponentListener​(
ComponentListener
l)

Removes the specified listener so it no longer receives

COMPONENT

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addComponentListener(java.awt.event.ComponentListener)

---

#### public static void addContainerListener​(
ContainerListener
l)

Adds the specified listener to receive all

CONTAINER

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeContainerListener(java.awt.event.ContainerListener)

---

#### public static void removeContainerListener​(
ContainerListener
l)

Removes the specified listener so it no longer receives

CONTAINER

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addContainerListener(java.awt.event.ContainerListener)

---

#### public static void addFocusListener​(
FocusListener
l)

Adds the specified listener to receive all

FOCUS

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeFocusListener(java.awt.event.FocusListener)

---

#### public static void removeFocusListener​(
FocusListener
l)

Removes the specified listener so it no longer receives

FOCUS

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addFocusListener(java.awt.event.FocusListener)

---

#### public static void addKeyListener​(
KeyListener
l)

Adds the specified listener to receive all

KEY

events on each
component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeKeyListener(java.awt.event.KeyListener)

---

#### public static void removeKeyListener​(
KeyListener
l)

Removes the specified listener so it no longer receives

KEY

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addKeyListener(java.awt.event.KeyListener)

---

#### public static void addMouseListener​(
MouseListener
l)

Adds the specified listener to receive all

MOUSE

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeMouseListener(java.awt.event.MouseListener)

---

#### public static void removeMouseListener​(
MouseListener
l)

Removes the specified listener so it no longer receives

MOUSE

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addMouseListener(java.awt.event.MouseListener)

---

#### public static void addMouseMotionListener​(
MouseMotionListener
l)

Adds the specified listener to receive all mouse

MOTION

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeMouseMotionListener(java.awt.event.MouseMotionListener)

---

#### public static void removeMouseMotionListener​(
MouseMotionListener
l)

Removes the specified listener so it no longer receives

MOTION

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addMouseMotionListener(java.awt.event.MouseMotionListener)

---

#### public static void addWindowListener​(
WindowListener
l)

Adds the specified listener to receive all

WINDOW

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeWindowListener(java.awt.event.WindowListener)

---

#### public static void removeWindowListener​(
WindowListener
l)

Removes the specified listener so it no longer receives

WINDOW

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addWindowListener(java.awt.event.WindowListener)

---

#### public static void addActionListener​(
ActionListener
l)

Adds the specified listener to receive all

ACTION

events on each component instance in the Java Virtual Machine when they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeActionListener(java.awt.event.ActionListener)

---

#### public static void removeActionListener​(
ActionListener
l)

Removes the specified listener so it no longer receives

ACTION

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addActionListener(java.awt.event.ActionListener)

---

#### public static void addAdjustmentListener​(
AdjustmentListener
l)

Adds the specified listener to receive all

ADJUSTMENT

events on each component instance
in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeAdjustmentListener(java.awt.event.AdjustmentListener)

---

#### public static void removeAdjustmentListener​(
AdjustmentListener
l)

Removes the specified listener so it no longer receives

ADJUSTMENT

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addAdjustmentListener(java.awt.event.AdjustmentListener)

---

#### public static void addItemListener​(
ItemListener
l)

Adds the specified listener to receive all

ITEM

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeItemListener(java.awt.event.ItemListener)

---

#### public static void removeItemListener​(
ItemListener
l)

Removes the specified listener so it no longer receives

ITEM

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addItemListener(java.awt.event.ItemListener)

---

#### public static void addTextListener​(
TextListener
l)

Adds the specified listener to receive all

TEXT

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeTextListener(java.awt.event.TextListener)

---

#### public static void removeTextListener​(
TextListener
l)

Removes the specified listener so it no longer receives

TEXT

events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addTextListener(java.awt.event.TextListener)

---

### Additional Sections

#### Class AWTEventMonitor

java.lang.Object

- com.sun.java.accessibility.util.AWTEventMonitor

com.sun.java.accessibility.util.AWTEventMonitor

**Direct Known Subclasses:** SwingEventMonitor

```java
public class
AWTEventMonitor

extends
Object
```

The

AWTEventMonitor

implements a suite of listeners that are
conditionally installed on every AWT component instance in the Java
Virtual Machine. The events captured by these listeners are made
available through a unified set of listeners supported by

AWTEventMonitor

.
With this, all the individual events on each of the AWT component
instances are funneled into one set of listeners broken down by category
(see

EventID

for the categories).

This class depends upon

EventQueueMonitor

, which provides the base
level support for capturing the top-level containers as they are created.

public class

AWTEventMonitor

extends

Object

The

AWTEventMonitor

implements a suite of listeners that are
conditionally installed on every AWT component instance in the Java
Virtual Machine. The events captured by these listeners are made
available through a unified set of listeners supported by

AWTEventMonitor

.
With this, all the individual events on each of the AWT component
instances are funneled into one set of listeners broken down by category
(see

EventID

for the categories).

This class depends upon

EventQueueMonitor

, which provides the base
level support for capturing the top-level containers as they are created.

This class depends upon

EventQueueMonitor

, which provides the base
level support for capturing the top-level containers as they are created.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static

ActionListener

actionListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

AdjustmentListener

adjustmentListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

ComponentListener

componentListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

Component

componentWithFocus

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused; to get the component with focus use the
getComponentWithFocus method.

protected static

ContainerListener

containerListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

FocusListener

focusListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

ItemListener

itemListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

KeyListener

keyListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

MouseListener

mouseListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

MouseMotionListener

mouseMotionListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

TextListener

textListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

WindowListener

windowListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AWTEventMonitor

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static void

addActionListener

​(

ActionListener

l)

Adds the specified listener to receive all

ACTION

events on each component instance in the Java Virtual Machine when they occur.

static void

addAdjustmentListener

​(

AdjustmentListener

l)

Adds the specified listener to receive all

ADJUSTMENT

events on each component instance
in the Java Virtual Machine when they occur.

static void

addComponentListener

​(

ComponentListener

l)

Adds the specified listener to receive all

COMPONENT

events on each component instance in the Java Virtual Machine as they occur.

static void

addContainerListener

​(

ContainerListener

l)

Adds the specified listener to receive all

CONTAINER

events on each component instance in the Java Virtual Machine as they occur.

static void

addFocusListener

​(

FocusListener

l)

Adds the specified listener to receive all

FOCUS

events
on each component instance in the Java Virtual Machine when they occur.

static void

addItemListener

​(

ItemListener

l)

Adds the specified listener to receive all

ITEM

events
on each component instance in the Java Virtual Machine when they occur.

static void

addKeyListener

​(

KeyListener

l)

Adds the specified listener to receive all

KEY

events on each
component instance in the Java Virtual Machine when they occur.

static void

addMouseListener

​(

MouseListener

l)

Adds the specified listener to receive all

MOUSE

events
on each component instance in the Java Virtual Machine when they occur.

static void

addMouseMotionListener

​(

MouseMotionListener

l)

Adds the specified listener to receive all mouse

MOTION

events on each component instance in the Java Virtual Machine when they occur.

static void

addTextListener

​(

TextListener

l)

Adds the specified listener to receive all

TEXT

events
on each component instance in the Java Virtual Machine when they occur.

static void

addWindowListener

​(

WindowListener

l)

Adds the specified listener to receive all

WINDOW

events on each component instance in the Java Virtual Machine when they occur.

static

Component

getComponentWithFocus

()

Returns the component that currently has keyboard focus.

static void

removeActionListener

​(

ActionListener

l)

Removes the specified listener so it no longer receives

ACTION

events when they occur.

static void

removeAdjustmentListener

​(

AdjustmentListener

l)

Removes the specified listener so it no longer receives

ADJUSTMENT

events when they occur.

static void

removeComponentListener

​(

ComponentListener

l)

Removes the specified listener so it no longer receives

COMPONENT

events when they occur.

static void

removeContainerListener

​(

ContainerListener

l)

Removes the specified listener so it no longer receives

CONTAINER

events when they occur.

static void

removeFocusListener

​(

FocusListener

l)

Removes the specified listener so it no longer receives

FOCUS

events when they occur.

static void

removeItemListener

​(

ItemListener

l)

Removes the specified listener so it no longer receives

ITEM

events when they occur.

static void

removeKeyListener

​(

KeyListener

l)

Removes the specified listener so it no longer receives

KEY

events when they occur.

static void

removeMouseListener

​(

MouseListener

l)

Removes the specified listener so it no longer receives

MOUSE

events when they occur.

static void

removeMouseMotionListener

​(

MouseMotionListener

l)

Removes the specified listener so it no longer receives

MOTION

events when they occur.

static void

removeTextListener

​(

TextListener

l)

Removes the specified listener so it no longer receives

TEXT

events when they occur.

static void

removeWindowListener

​(

WindowListener

l)

Removes the specified listener so it no longer receives

WINDOW

events when they occur.

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

protected static

ActionListener

actionListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

AdjustmentListener

adjustmentListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

ComponentListener

componentListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

Component

componentWithFocus

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused; to get the component with focus use the
getComponentWithFocus method.

protected static

ContainerListener

containerListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

FocusListener

focusListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

ItemListener

itemListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

KeyListener

keyListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

MouseListener

mouseListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

MouseMotionListener

mouseMotionListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

TextListener

textListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

protected static

WindowListener

windowListener

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

---

#### Field Summary

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused; to get the component with focus use the
getComponentWithFocus method.

Constructor Summary

Constructors

Constructor

Description

AWTEventMonitor

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static void

addActionListener

​(

ActionListener

l)

Adds the specified listener to receive all

ACTION

events on each component instance in the Java Virtual Machine when they occur.

static void

addAdjustmentListener

​(

AdjustmentListener

l)

Adds the specified listener to receive all

ADJUSTMENT

events on each component instance
in the Java Virtual Machine when they occur.

static void

addComponentListener

​(

ComponentListener

l)

Adds the specified listener to receive all

COMPONENT

events on each component instance in the Java Virtual Machine as they occur.

static void

addContainerListener

​(

ContainerListener

l)

Adds the specified listener to receive all

CONTAINER

events on each component instance in the Java Virtual Machine as they occur.

static void

addFocusListener

​(

FocusListener

l)

Adds the specified listener to receive all

FOCUS

events
on each component instance in the Java Virtual Machine when they occur.

static void

addItemListener

​(

ItemListener

l)

Adds the specified listener to receive all

ITEM

events
on each component instance in the Java Virtual Machine when they occur.

static void

addKeyListener

​(

KeyListener

l)

Adds the specified listener to receive all

KEY

events on each
component instance in the Java Virtual Machine when they occur.

static void

addMouseListener

​(

MouseListener

l)

Adds the specified listener to receive all

MOUSE

events
on each component instance in the Java Virtual Machine when they occur.

static void

addMouseMotionListener

​(

MouseMotionListener

l)

Adds the specified listener to receive all mouse

MOTION

events on each component instance in the Java Virtual Machine when they occur.

static void

addTextListener

​(

TextListener

l)

Adds the specified listener to receive all

TEXT

events
on each component instance in the Java Virtual Machine when they occur.

static void

addWindowListener

​(

WindowListener

l)

Adds the specified listener to receive all

WINDOW

events on each component instance in the Java Virtual Machine when they occur.

static

Component

getComponentWithFocus

()

Returns the component that currently has keyboard focus.

static void

removeActionListener

​(

ActionListener

l)

Removes the specified listener so it no longer receives

ACTION

events when they occur.

static void

removeAdjustmentListener

​(

AdjustmentListener

l)

Removes the specified listener so it no longer receives

ADJUSTMENT

events when they occur.

static void

removeComponentListener

​(

ComponentListener

l)

Removes the specified listener so it no longer receives

COMPONENT

events when they occur.

static void

removeContainerListener

​(

ContainerListener

l)

Removes the specified listener so it no longer receives

CONTAINER

events when they occur.

static void

removeFocusListener

​(

FocusListener

l)

Removes the specified listener so it no longer receives

FOCUS

events when they occur.

static void

removeItemListener

​(

ItemListener

l)

Removes the specified listener so it no longer receives

ITEM

events when they occur.

static void

removeKeyListener

​(

KeyListener

l)

Removes the specified listener so it no longer receives

KEY

events when they occur.

static void

removeMouseListener

​(

MouseListener

l)

Removes the specified listener so it no longer receives

MOUSE

events when they occur.

static void

removeMouseMotionListener

​(

MouseMotionListener

l)

Removes the specified listener so it no longer receives

MOTION

events when they occur.

static void

removeTextListener

​(

TextListener

l)

Removes the specified listener so it no longer receives

TEXT

events when they occur.

static void

removeWindowListener

​(

WindowListener

l)

Removes the specified listener so it no longer receives

WINDOW

events when they occur.

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

Adds the specified listener to receive all

ACTION

events on each component instance in the Java Virtual Machine when they occur.

Adds the specified listener to receive all

ADJUSTMENT

events on each component instance
in the Java Virtual Machine when they occur.

Adds the specified listener to receive all

COMPONENT

events on each component instance in the Java Virtual Machine as they occur.

Adds the specified listener to receive all

CONTAINER

events on each component instance in the Java Virtual Machine as they occur.

Adds the specified listener to receive all

FOCUS

events
on each component instance in the Java Virtual Machine when they occur.

Adds the specified listener to receive all

ITEM

events
on each component instance in the Java Virtual Machine when they occur.

Adds the specified listener to receive all

KEY

events on each
component instance in the Java Virtual Machine when they occur.

Adds the specified listener to receive all

MOUSE

events
on each component instance in the Java Virtual Machine when they occur.

Adds the specified listener to receive all mouse

MOTION

events on each component instance in the Java Virtual Machine when they occur.

Adds the specified listener to receive all

TEXT

events
on each component instance in the Java Virtual Machine when they occur.

Adds the specified listener to receive all

WINDOW

events on each component instance in the Java Virtual Machine when they occur.

Returns the component that currently has keyboard focus.

Removes the specified listener so it no longer receives

ACTION

events when they occur.

Removes the specified listener so it no longer receives

ADJUSTMENT

events when they occur.

Removes the specified listener so it no longer receives

COMPONENT

events when they occur.

Removes the specified listener so it no longer receives

CONTAINER

events when they occur.

Removes the specified listener so it no longer receives

FOCUS

events when they occur.

Removes the specified listener so it no longer receives

ITEM

events when they occur.

Removes the specified listener so it no longer receives

KEY

events when they occur.

Removes the specified listener so it no longer receives

MOUSE

events when they occur.

Removes the specified listener so it no longer receives

MOTION

events when they occur.

Removes the specified listener so it no longer receives

TEXT

events when they occur.

Removes the specified listener so it no longer receives

WINDOW

events when they occur.

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

- componentWithFocus

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
Component
componentWithFocus
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused; to get the component with focus use the
getComponentWithFocus method.

The current component with keyboard focus.

**See Also:** getComponentWithFocus()

- componentListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ComponentListener
componentListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ComponentListener classes.

**See Also:** addComponentListener(java.awt.event.ComponentListener)

,

removeComponentListener(java.awt.event.ComponentListener)

- containerListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ContainerListener
containerListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ContainerListener classes.

**See Also:** addContainerListener(java.awt.event.ContainerListener)

,

removeContainerListener(java.awt.event.ContainerListener)

- focusListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
FocusListener
focusListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered FocusListener classes.

**See Also:** addFocusListener(java.awt.event.FocusListener)

,

removeFocusListener(java.awt.event.FocusListener)

- keyListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
KeyListener
keyListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered KeyListener classes.

**See Also:** addKeyListener(java.awt.event.KeyListener)

,

removeKeyListener(java.awt.event.KeyListener)

- mouseListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
MouseListener
mouseListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered MouseListener classes.

**See Also:** addMouseListener(java.awt.event.MouseListener)

,

removeMouseListener(java.awt.event.MouseListener)

- mouseMotionListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
MouseMotionListener
mouseMotionListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered MouseMotionListener classes.

**See Also:** addMouseMotionListener(java.awt.event.MouseMotionListener)

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

- windowListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
WindowListener
windowListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered WindowListener classes.

**See Also:** addWindowListener(java.awt.event.WindowListener)

,

removeWindowListener(java.awt.event.WindowListener)

- actionListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ActionListener
actionListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ActionListener classes.

**See Also:** addActionListener(java.awt.event.ActionListener)

,

removeActionListener(java.awt.event.ActionListener)

- adjustmentListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
AdjustmentListener
adjustmentListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered AdjustmentListener classes.

**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

- itemListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ItemListener
itemListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ItemListener classes.

**See Also:** addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

- textListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
TextListener
textListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered TextListener classes.

**See Also:** addTextListener(java.awt.event.TextListener)

,

removeTextListener(java.awt.event.TextListener)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AWTEventMonitor

```java
public AWTEventMonitor()
```

============ METHOD DETAIL ==========

- Method Detail

- getComponentWithFocus

```java
public static
Component
getComponentWithFocus()
```

Returns the component that currently has keyboard focus. The return
value can be null.

**Returns:** the component that has keyboard focus

- addComponentListener

```java
public static void addComponentListener​(
ComponentListener
l)
```

Adds the specified listener to receive all

COMPONENT

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeComponentListener(java.awt.event.ComponentListener)

- removeComponentListener

```java
public static void removeComponentListener​(
ComponentListener
l)
```

Removes the specified listener so it no longer receives

COMPONENT

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addComponentListener(java.awt.event.ComponentListener)

- addContainerListener

```java
public static void addContainerListener​(
ContainerListener
l)
```

Adds the specified listener to receive all

CONTAINER

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeContainerListener(java.awt.event.ContainerListener)

- removeContainerListener

```java
public static void removeContainerListener​(
ContainerListener
l)
```

Removes the specified listener so it no longer receives

CONTAINER

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addContainerListener(java.awt.event.ContainerListener)

- addFocusListener

```java
public static void addFocusListener​(
FocusListener
l)
```

Adds the specified listener to receive all

FOCUS

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeFocusListener(java.awt.event.FocusListener)

- removeFocusListener

```java
public static void removeFocusListener​(
FocusListener
l)
```

Removes the specified listener so it no longer receives

FOCUS

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addFocusListener(java.awt.event.FocusListener)

- addKeyListener

```java
public static void addKeyListener​(
KeyListener
l)
```

Adds the specified listener to receive all

KEY

events on each
component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeKeyListener(java.awt.event.KeyListener)

- removeKeyListener

```java
public static void removeKeyListener​(
KeyListener
l)
```

Removes the specified listener so it no longer receives

KEY

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addKeyListener(java.awt.event.KeyListener)

- addMouseListener

```java
public static void addMouseListener​(
MouseListener
l)
```

Adds the specified listener to receive all

MOUSE

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeMouseListener(java.awt.event.MouseListener)

- removeMouseListener

```java
public static void removeMouseListener​(
MouseListener
l)
```

Removes the specified listener so it no longer receives

MOUSE

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addMouseListener(java.awt.event.MouseListener)

- addMouseMotionListener

```java
public static void addMouseMotionListener​(
MouseMotionListener
l)
```

Adds the specified listener to receive all mouse

MOTION

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeMouseMotionListener(java.awt.event.MouseMotionListener)

- removeMouseMotionListener

```java
public static void removeMouseMotionListener​(
MouseMotionListener
l)
```

Removes the specified listener so it no longer receives

MOTION

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addMouseMotionListener(java.awt.event.MouseMotionListener)

- addWindowListener

```java
public static void addWindowListener​(
WindowListener
l)
```

Adds the specified listener to receive all

WINDOW

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeWindowListener(java.awt.event.WindowListener)

- removeWindowListener

```java
public static void removeWindowListener​(
WindowListener
l)
```

Removes the specified listener so it no longer receives

WINDOW

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addWindowListener(java.awt.event.WindowListener)

- addActionListener

```java
public static void addActionListener​(
ActionListener
l)
```

Adds the specified listener to receive all

ACTION

events on each component instance in the Java Virtual Machine when they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeActionListener(java.awt.event.ActionListener)

- removeActionListener

```java
public static void removeActionListener​(
ActionListener
l)
```

Removes the specified listener so it no longer receives

ACTION

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addActionListener(java.awt.event.ActionListener)

- addAdjustmentListener

```java
public static void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds the specified listener to receive all

ADJUSTMENT

events on each component instance
in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeAdjustmentListener(java.awt.event.AdjustmentListener)

- removeAdjustmentListener

```java
public static void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes the specified listener so it no longer receives

ADJUSTMENT

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

- addItemListener

```java
public static void addItemListener​(
ItemListener
l)
```

Adds the specified listener to receive all

ITEM

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeItemListener(java.awt.event.ItemListener)

- removeItemListener

```java
public static void removeItemListener​(
ItemListener
l)
```

Removes the specified listener so it no longer receives

ITEM

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addItemListener(java.awt.event.ItemListener)

- addTextListener

```java
public static void addTextListener​(
TextListener
l)
```

Adds the specified listener to receive all

TEXT

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeTextListener(java.awt.event.TextListener)

- removeTextListener

```java
public static void removeTextListener​(
TextListener
l)
```

Removes the specified listener so it no longer receives

TEXT

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addTextListener(java.awt.event.TextListener)

Field Detail

- componentWithFocus

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
Component
componentWithFocus
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused; to get the component with focus use the
getComponentWithFocus method.

The current component with keyboard focus.

**See Also:** getComponentWithFocus()

- componentListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ComponentListener
componentListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ComponentListener classes.

**See Also:** addComponentListener(java.awt.event.ComponentListener)

,

removeComponentListener(java.awt.event.ComponentListener)

- containerListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ContainerListener
containerListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ContainerListener classes.

**See Also:** addContainerListener(java.awt.event.ContainerListener)

,

removeContainerListener(java.awt.event.ContainerListener)

- focusListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
FocusListener
focusListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered FocusListener classes.

**See Also:** addFocusListener(java.awt.event.FocusListener)

,

removeFocusListener(java.awt.event.FocusListener)

- keyListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
KeyListener
keyListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered KeyListener classes.

**See Also:** addKeyListener(java.awt.event.KeyListener)

,

removeKeyListener(java.awt.event.KeyListener)

- mouseListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
MouseListener
mouseListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered MouseListener classes.

**See Also:** addMouseListener(java.awt.event.MouseListener)

,

removeMouseListener(java.awt.event.MouseListener)

- mouseMotionListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
MouseMotionListener
mouseMotionListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered MouseMotionListener classes.

**See Also:** addMouseMotionListener(java.awt.event.MouseMotionListener)

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

- windowListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
WindowListener
windowListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered WindowListener classes.

**See Also:** addWindowListener(java.awt.event.WindowListener)

,

removeWindowListener(java.awt.event.WindowListener)

- actionListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ActionListener
actionListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ActionListener classes.

**See Also:** addActionListener(java.awt.event.ActionListener)

,

removeActionListener(java.awt.event.ActionListener)

- adjustmentListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
AdjustmentListener
adjustmentListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered AdjustmentListener classes.

**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

- itemListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ItemListener
itemListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ItemListener classes.

**See Also:** addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

- textListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
TextListener
textListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered TextListener classes.

**See Also:** addTextListener(java.awt.event.TextListener)

,

removeTextListener(java.awt.event.TextListener)

---

#### Field Detail

componentWithFocus

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
Component
componentWithFocus
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused; to get the component with focus use the
getComponentWithFocus method.

The current component with keyboard focus.

**See Also:** getComponentWithFocus()

---

#### componentWithFocus

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

Component

componentWithFocus

The current component with keyboard focus.

componentListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ComponentListener
componentListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ComponentListener classes.

**See Also:** addComponentListener(java.awt.event.ComponentListener)

,

removeComponentListener(java.awt.event.ComponentListener)

---

#### componentListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

ComponentListener

componentListener

The current list of registered ComponentListener classes.

containerListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ContainerListener
containerListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ContainerListener classes.

**See Also:** addContainerListener(java.awt.event.ContainerListener)

,

removeContainerListener(java.awt.event.ContainerListener)

---

#### containerListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

ContainerListener

containerListener

The current list of registered ContainerListener classes.

focusListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
FocusListener
focusListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered FocusListener classes.

**See Also:** addFocusListener(java.awt.event.FocusListener)

,

removeFocusListener(java.awt.event.FocusListener)

---

#### focusListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

FocusListener

focusListener

The current list of registered FocusListener classes.

keyListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
KeyListener
keyListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered KeyListener classes.

**See Also:** addKeyListener(java.awt.event.KeyListener)

,

removeKeyListener(java.awt.event.KeyListener)

---

#### keyListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

KeyListener

keyListener

The current list of registered KeyListener classes.

mouseListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
MouseListener
mouseListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered MouseListener classes.

**See Also:** addMouseListener(java.awt.event.MouseListener)

,

removeMouseListener(java.awt.event.MouseListener)

---

#### mouseListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

MouseListener

mouseListener

The current list of registered MouseListener classes.

mouseMotionListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
MouseMotionListener
mouseMotionListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered MouseMotionListener classes.

**See Also:** addMouseMotionListener(java.awt.event.MouseMotionListener)

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

---

#### mouseMotionListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

MouseMotionListener

mouseMotionListener

The current list of registered MouseMotionListener classes.

windowListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
WindowListener
windowListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered WindowListener classes.

**See Also:** addWindowListener(java.awt.event.WindowListener)

,

removeWindowListener(java.awt.event.WindowListener)

---

#### windowListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

WindowListener

windowListener

The current list of registered WindowListener classes.

actionListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ActionListener
actionListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ActionListener classes.

**See Also:** addActionListener(java.awt.event.ActionListener)

,

removeActionListener(java.awt.event.ActionListener)

---

#### actionListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

ActionListener

actionListener

The current list of registered ActionListener classes.

adjustmentListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
AdjustmentListener
adjustmentListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered AdjustmentListener classes.

**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

---

#### adjustmentListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

AdjustmentListener

adjustmentListener

The current list of registered AdjustmentListener classes.

itemListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
ItemListener
itemListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered ItemListener classes.

**See Also:** addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

---

#### itemListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

ItemListener

itemListener

The current list of registered ItemListener classes.

textListener

```java
@Deprecated
(
since
="8",

forRemoval
=true)
protected static
TextListener
textListener
```

Deprecated, for removal: This API element is subject to removal in a future version.

This field is unused.

The current list of registered TextListener classes.

**See Also:** addTextListener(java.awt.event.TextListener)

,

removeTextListener(java.awt.event.TextListener)

---

#### textListener

@Deprecated

(

since

="8",

forRemoval

=true)
protected static

TextListener

textListener

The current list of registered TextListener classes.

Constructor Detail

- AWTEventMonitor

```java
public AWTEventMonitor()
```

---

#### Constructor Detail

AWTEventMonitor

```java
public AWTEventMonitor()
```

---

#### AWTEventMonitor

public AWTEventMonitor()

Method Detail

- getComponentWithFocus

```java
public static
Component
getComponentWithFocus()
```

Returns the component that currently has keyboard focus. The return
value can be null.

**Returns:** the component that has keyboard focus

- addComponentListener

```java
public static void addComponentListener​(
ComponentListener
l)
```

Adds the specified listener to receive all

COMPONENT

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeComponentListener(java.awt.event.ComponentListener)

- removeComponentListener

```java
public static void removeComponentListener​(
ComponentListener
l)
```

Removes the specified listener so it no longer receives

COMPONENT

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addComponentListener(java.awt.event.ComponentListener)

- addContainerListener

```java
public static void addContainerListener​(
ContainerListener
l)
```

Adds the specified listener to receive all

CONTAINER

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeContainerListener(java.awt.event.ContainerListener)

- removeContainerListener

```java
public static void removeContainerListener​(
ContainerListener
l)
```

Removes the specified listener so it no longer receives

CONTAINER

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addContainerListener(java.awt.event.ContainerListener)

- addFocusListener

```java
public static void addFocusListener​(
FocusListener
l)
```

Adds the specified listener to receive all

FOCUS

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeFocusListener(java.awt.event.FocusListener)

- removeFocusListener

```java
public static void removeFocusListener​(
FocusListener
l)
```

Removes the specified listener so it no longer receives

FOCUS

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addFocusListener(java.awt.event.FocusListener)

- addKeyListener

```java
public static void addKeyListener​(
KeyListener
l)
```

Adds the specified listener to receive all

KEY

events on each
component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeKeyListener(java.awt.event.KeyListener)

- removeKeyListener

```java
public static void removeKeyListener​(
KeyListener
l)
```

Removes the specified listener so it no longer receives

KEY

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addKeyListener(java.awt.event.KeyListener)

- addMouseListener

```java
public static void addMouseListener​(
MouseListener
l)
```

Adds the specified listener to receive all

MOUSE

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeMouseListener(java.awt.event.MouseListener)

- removeMouseListener

```java
public static void removeMouseListener​(
MouseListener
l)
```

Removes the specified listener so it no longer receives

MOUSE

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addMouseListener(java.awt.event.MouseListener)

- addMouseMotionListener

```java
public static void addMouseMotionListener​(
MouseMotionListener
l)
```

Adds the specified listener to receive all mouse

MOTION

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeMouseMotionListener(java.awt.event.MouseMotionListener)

- removeMouseMotionListener

```java
public static void removeMouseMotionListener​(
MouseMotionListener
l)
```

Removes the specified listener so it no longer receives

MOTION

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addMouseMotionListener(java.awt.event.MouseMotionListener)

- addWindowListener

```java
public static void addWindowListener​(
WindowListener
l)
```

Adds the specified listener to receive all

WINDOW

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeWindowListener(java.awt.event.WindowListener)

- removeWindowListener

```java
public static void removeWindowListener​(
WindowListener
l)
```

Removes the specified listener so it no longer receives

WINDOW

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addWindowListener(java.awt.event.WindowListener)

- addActionListener

```java
public static void addActionListener​(
ActionListener
l)
```

Adds the specified listener to receive all

ACTION

events on each component instance in the Java Virtual Machine when they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeActionListener(java.awt.event.ActionListener)

- removeActionListener

```java
public static void removeActionListener​(
ActionListener
l)
```

Removes the specified listener so it no longer receives

ACTION

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addActionListener(java.awt.event.ActionListener)

- addAdjustmentListener

```java
public static void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds the specified listener to receive all

ADJUSTMENT

events on each component instance
in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeAdjustmentListener(java.awt.event.AdjustmentListener)

- removeAdjustmentListener

```java
public static void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes the specified listener so it no longer receives

ADJUSTMENT

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

- addItemListener

```java
public static void addItemListener​(
ItemListener
l)
```

Adds the specified listener to receive all

ITEM

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeItemListener(java.awt.event.ItemListener)

- removeItemListener

```java
public static void removeItemListener​(
ItemListener
l)
```

Removes the specified listener so it no longer receives

ITEM

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addItemListener(java.awt.event.ItemListener)

- addTextListener

```java
public static void addTextListener​(
TextListener
l)
```

Adds the specified listener to receive all

TEXT

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeTextListener(java.awt.event.TextListener)

- removeTextListener

```java
public static void removeTextListener​(
TextListener
l)
```

Removes the specified listener so it no longer receives

TEXT

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addTextListener(java.awt.event.TextListener)

---

#### Method Detail

getComponentWithFocus

```java
public static
Component
getComponentWithFocus()
```

Returns the component that currently has keyboard focus. The return
value can be null.

**Returns:** the component that has keyboard focus

---

#### getComponentWithFocus

public static

Component

getComponentWithFocus()

Returns the component that currently has keyboard focus. The return
value can be null.

addComponentListener

```java
public static void addComponentListener​(
ComponentListener
l)
```

Adds the specified listener to receive all

COMPONENT

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeComponentListener(java.awt.event.ComponentListener)

---

#### addComponentListener

public static void addComponentListener​(

ComponentListener

l)

Adds the specified listener to receive all

COMPONENT

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeComponentListener

```java
public static void removeComponentListener​(
ComponentListener
l)
```

Removes the specified listener so it no longer receives

COMPONENT

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addComponentListener(java.awt.event.ComponentListener)

---

#### removeComponentListener

public static void removeComponentListener​(

ComponentListener

l)

Removes the specified listener so it no longer receives

COMPONENT

events when they occur.

addContainerListener

```java
public static void addContainerListener​(
ContainerListener
l)
```

Adds the specified listener to receive all

CONTAINER

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeContainerListener(java.awt.event.ContainerListener)

---

#### addContainerListener

public static void addContainerListener​(

ContainerListener

l)

Adds the specified listener to receive all

CONTAINER

events on each component instance in the Java Virtual Machine as they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeContainerListener

```java
public static void removeContainerListener​(
ContainerListener
l)
```

Removes the specified listener so it no longer receives

CONTAINER

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addContainerListener(java.awt.event.ContainerListener)

---

#### removeContainerListener

public static void removeContainerListener​(

ContainerListener

l)

Removes the specified listener so it no longer receives

CONTAINER

events when they occur.

addFocusListener

```java
public static void addFocusListener​(
FocusListener
l)
```

Adds the specified listener to receive all

FOCUS

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeFocusListener(java.awt.event.FocusListener)

---

#### addFocusListener

public static void addFocusListener​(

FocusListener

l)

Adds the specified listener to receive all

FOCUS

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeFocusListener

```java
public static void removeFocusListener​(
FocusListener
l)
```

Removes the specified listener so it no longer receives

FOCUS

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addFocusListener(java.awt.event.FocusListener)

---

#### removeFocusListener

public static void removeFocusListener​(

FocusListener

l)

Removes the specified listener so it no longer receives

FOCUS

events when they occur.

addKeyListener

```java
public static void addKeyListener​(
KeyListener
l)
```

Adds the specified listener to receive all

KEY

events on each
component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeKeyListener(java.awt.event.KeyListener)

---

#### addKeyListener

public static void addKeyListener​(

KeyListener

l)

Adds the specified listener to receive all

KEY

events on each
component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeKeyListener

```java
public static void removeKeyListener​(
KeyListener
l)
```

Removes the specified listener so it no longer receives

KEY

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addKeyListener(java.awt.event.KeyListener)

---

#### removeKeyListener

public static void removeKeyListener​(

KeyListener

l)

Removes the specified listener so it no longer receives

KEY

events when they occur.

addMouseListener

```java
public static void addMouseListener​(
MouseListener
l)
```

Adds the specified listener to receive all

MOUSE

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeMouseListener(java.awt.event.MouseListener)

---

#### addMouseListener

public static void addMouseListener​(

MouseListener

l)

Adds the specified listener to receive all

MOUSE

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeMouseListener

```java
public static void removeMouseListener​(
MouseListener
l)
```

Removes the specified listener so it no longer receives

MOUSE

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addMouseListener(java.awt.event.MouseListener)

---

#### removeMouseListener

public static void removeMouseListener​(

MouseListener

l)

Removes the specified listener so it no longer receives

MOUSE

events when they occur.

addMouseMotionListener

```java
public static void addMouseMotionListener​(
MouseMotionListener
l)
```

Adds the specified listener to receive all mouse

MOTION

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeMouseMotionListener(java.awt.event.MouseMotionListener)

---

#### addMouseMotionListener

public static void addMouseMotionListener​(

MouseMotionListener

l)

Adds the specified listener to receive all mouse

MOTION

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeMouseMotionListener

```java
public static void removeMouseMotionListener​(
MouseMotionListener
l)
```

Removes the specified listener so it no longer receives

MOTION

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addMouseMotionListener(java.awt.event.MouseMotionListener)

---

#### removeMouseMotionListener

public static void removeMouseMotionListener​(

MouseMotionListener

l)

Removes the specified listener so it no longer receives

MOTION

events when they occur.

addWindowListener

```java
public static void addWindowListener​(
WindowListener
l)
```

Adds the specified listener to receive all

WINDOW

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeWindowListener(java.awt.event.WindowListener)

---

#### addWindowListener

public static void addWindowListener​(

WindowListener

l)

Adds the specified listener to receive all

WINDOW

events on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeWindowListener

```java
public static void removeWindowListener​(
WindowListener
l)
```

Removes the specified listener so it no longer receives

WINDOW

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addWindowListener(java.awt.event.WindowListener)

---

#### removeWindowListener

public static void removeWindowListener​(

WindowListener

l)

Removes the specified listener so it no longer receives

WINDOW

events when they occur.

addActionListener

```java
public static void addActionListener​(
ActionListener
l)
```

Adds the specified listener to receive all

ACTION

events on each component instance in the Java Virtual Machine when they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeActionListener(java.awt.event.ActionListener)

---

#### addActionListener

public static void addActionListener​(

ActionListener

l)

Adds the specified listener to receive all

ACTION

events on each component instance in the Java Virtual Machine when they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeActionListener

```java
public static void removeActionListener​(
ActionListener
l)
```

Removes the specified listener so it no longer receives

ACTION

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addActionListener(java.awt.event.ActionListener)

---

#### removeActionListener

public static void removeActionListener​(

ActionListener

l)

Removes the specified listener so it no longer receives

ACTION

events when they occur.

addAdjustmentListener

```java
public static void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds the specified listener to receive all

ADJUSTMENT

events on each component instance
in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeAdjustmentListener(java.awt.event.AdjustmentListener)

---

#### addAdjustmentListener

public static void addAdjustmentListener​(

AdjustmentListener

l)

Adds the specified listener to receive all

ADJUSTMENT

events on each component instance
in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeAdjustmentListener

```java
public static void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes the specified listener so it no longer receives

ADJUSTMENT

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

---

#### removeAdjustmentListener

public static void removeAdjustmentListener​(

AdjustmentListener

l)

Removes the specified listener so it no longer receives

ADJUSTMENT

events when they occur.

addItemListener

```java
public static void addItemListener​(
ItemListener
l)
```

Adds the specified listener to receive all

ITEM

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeItemListener(java.awt.event.ItemListener)

---

#### addItemListener

public static void addItemListener​(

ItemListener

l)

Adds the specified listener to receive all

ITEM

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeItemListener

```java
public static void removeItemListener​(
ItemListener
l)
```

Removes the specified listener so it no longer receives

ITEM

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addItemListener(java.awt.event.ItemListener)

---

#### removeItemListener

public static void removeItemListener​(

ItemListener

l)

Removes the specified listener so it no longer receives

ITEM

events when they occur.

addTextListener

```java
public static void addTextListener​(
TextListener
l)
```

Adds the specified listener to receive all

TEXT

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removeTextListener(java.awt.event.TextListener)

---

#### addTextListener

public static void addTextListener​(

TextListener

l)

Adds the specified listener to receive all

TEXT

events
on each component instance in the Java Virtual Machine when they occur.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

Note: this listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to component instances that support this listener type.

removeTextListener

```java
public static void removeTextListener​(
TextListener
l)
```

Removes the specified listener so it no longer receives

TEXT

events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addTextListener(java.awt.event.TextListener)

---

#### removeTextListener

public static void removeTextListener​(

TextListener

l)

Removes the specified listener so it no longer receives

TEXT

events when they occur.

---

