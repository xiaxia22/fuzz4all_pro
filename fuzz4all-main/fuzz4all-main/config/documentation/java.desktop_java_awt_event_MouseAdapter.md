# Class MouseAdapter

**Source:** `java.desktop\java\awt\event\MouseAdapter.html`

### Class Description

```java
public abstract class
MouseAdapter

extends
Object

implements
MouseListener
,
MouseWheelListener
,
MouseMotionListener
```

An abstract adapter class for receiving mouse events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Mouse events let you track when a mouse is pressed, released, clicked,
moved, dragged, when it enters a component, when it exits and
when a mouse wheel is moved.

Extend this class to create a

MouseEvent

(including drag and motion events) or/and

MouseWheelEvent

listener and override the methods for the events of interest. (If you implement the

MouseListener

,

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseListener

addMouseMotionListener

,

addMouseWheelListener

methods.
The relevant method in the listener object is invoked and the

MouseEvent

or

MouseWheelEvent

is passed to it in following cases:

- when a mouse button is pressed, released, or clicked (pressed and released)

when the mouse cursor enters or exits the component

when the mouse wheel rotated, or mouse moved or dragged

**All Implemented Interfaces:** MouseListener

,

MouseMotionListener

,

MouseWheelListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public MouseAdapter()

*No description found.*

---

### Method Details

#### public void mouseWheelMoved​(
MouseWheelEvent
e)

Invoked when the mouse wheel is rotated.

**Specified by:**
- mouseWheelMoved

in interface

MouseWheelListener

**Parameters:**
- e

- the event to be processed

**See Also:**
- MouseWheelEvent

**Since:**
- 1.6

---

#### public void mouseDragged​(
MouseEvent
e)

Invoked when a mouse button is pressed on a component and then
dragged.

MOUSE_DRAGGED

events will continue to be
delivered to the component where the drag originated until the
mouse button is released (regardless of whether the mouse position
is within the bounds of the component).

Due to platform-dependent Drag&Drop implementations,

MOUSE_DRAGGED

events may not be delivered during a native
Drag&Drop operation.

**Specified by:**
- mouseDragged

in interface

MouseMotionListener

**Parameters:**
- e

- the event to be processed

**Since:**
- 1.6

---

#### public void mouseMoved​(
MouseEvent
e)

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

**Specified by:**
- mouseMoved

in interface

MouseMotionListener

**Parameters:**
- e

- the event to be processed

**Since:**
- 1.6

---

### Additional Sections

#### Class MouseAdapter

java.lang.Object

- java.awt.event.MouseAdapter

java.awt.event.MouseAdapter

**All Implemented Interfaces:** MouseListener

,

MouseMotionListener

,

MouseWheelListener

,

EventListener

**Direct Known Subclasses:** BasicComboPopup.InvocationMouseHandler

,

BasicComboPopup.ListMouseHandler

,

BasicFileChooserUI.DoubleClickListener

,

BasicScrollBarUI.ArrowButtonListener

,

BasicScrollBarUI.TrackListener

,

BasicSplitPaneDivider.MouseHandler

,

BasicTabbedPaneUI.MouseHandler

,

BasicTreeUI.MouseHandler

,

FormView.MouseEventListener

,

HTMLEditorKit.LinkController

,

MetalFileChooserUI.SingleClickListener

,

MouseInputAdapter

,

ToolTipManager

```java
public abstract class
MouseAdapter

extends
Object

implements
MouseListener
,
MouseWheelListener
,
MouseMotionListener
```

An abstract adapter class for receiving mouse events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Mouse events let you track when a mouse is pressed, released, clicked,
moved, dragged, when it enters a component, when it exits and
when a mouse wheel is moved.

Extend this class to create a

MouseEvent

(including drag and motion events) or/and

MouseWheelEvent

listener and override the methods for the events of interest. (If you implement the

MouseListener

,

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseListener

addMouseMotionListener

,

addMouseWheelListener

methods.
The relevant method in the listener object is invoked and the

MouseEvent

or

MouseWheelEvent

is passed to it in following cases:

- when a mouse button is pressed, released, or clicked (pressed and released)

when the mouse cursor enters or exits the component

when the mouse wheel rotated, or mouse moved or dragged

**Since:** 1.1
**See Also:** MouseEvent

,

MouseWheelEvent

,

MouseListener

,

MouseMotionListener

,

MouseWheelListener

,

Tutorial: Writing a Mouse Listener

public abstract class

MouseAdapter

extends

Object

implements

MouseListener

,

MouseWheelListener

,

MouseMotionListener

An abstract adapter class for receiving mouse events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Mouse events let you track when a mouse is pressed, released, clicked,
moved, dragged, when it enters a component, when it exits and
when a mouse wheel is moved.

Extend this class to create a

MouseEvent

(including drag and motion events) or/and

MouseWheelEvent

listener and override the methods for the events of interest. (If you implement the

MouseListener

,

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseListener

addMouseMotionListener

,

addMouseWheelListener

methods.
The relevant method in the listener object is invoked and the

MouseEvent

or

MouseWheelEvent

is passed to it in following cases:

- when a mouse button is pressed, released, or clicked (pressed and released)

when the mouse cursor enters or exits the component

when the mouse wheel rotated, or mouse moved or dragged

Mouse events let you track when a mouse is pressed, released, clicked,
moved, dragged, when it enters a component, when it exits and
when a mouse wheel is moved.

Extend this class to create a

MouseEvent

(including drag and motion events) or/and

MouseWheelEvent

listener and override the methods for the events of interest. (If you implement the

MouseListener

,

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseListener

addMouseMotionListener

,

addMouseWheelListener

methods.
The relevant method in the listener object is invoked and the

MouseEvent

or

MouseWheelEvent

is passed to it in following cases:

- when a mouse button is pressed, released, or clicked (pressed and released)

when the mouse cursor enters or exits the component

when the mouse wheel rotated, or mouse moved or dragged

Extend this class to create a

MouseEvent

(including drag and motion events) or/and

MouseWheelEvent

listener and override the methods for the events of interest. (If you implement the

MouseListener

,

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseListener

addMouseMotionListener

,

addMouseWheelListener

methods.
The relevant method in the listener object is invoked and the

MouseEvent

or

MouseWheelEvent

is passed to it in following cases:

- when a mouse button is pressed, released, or clicked (pressed and released)

when the mouse cursor enters or exits the component

when the mouse wheel rotated, or mouse moved or dragged

Create a listener object using the extended class and then register it with
a component using the component's

addMouseListener

addMouseMotionListener

,

addMouseWheelListener

methods.
The relevant method in the listener object is invoked and the

MouseEvent

or

MouseWheelEvent

is passed to it in following cases:

- when a mouse button is pressed, released, or clicked (pressed and released)

when the mouse cursor enters or exits the component

when the mouse wheel rotated, or mouse moved or dragged

when a mouse button is pressed, released, or clicked (pressed and released)

when the mouse cursor enters or exits the component

when the mouse wheel rotated, or mouse moved or dragged

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MouseAdapter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

mouseDragged

​(

MouseEvent

e)

Invoked when a mouse button is pressed on a component and then
dragged.

void

mouseMoved

​(

MouseEvent

e)

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

void

mouseWheelMoved

​(

MouseWheelEvent

e)

Invoked when the mouse wheel is rotated.

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

- Methods declared in interface java.awt.event.

MouseListener

mouseClicked

,

mouseEntered

,

mouseExited

,

mousePressed

,

mouseReleased

Constructor Summary

Constructors

Constructor

Description

MouseAdapter

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

void

mouseDragged

​(

MouseEvent

e)

Invoked when a mouse button is pressed on a component and then
dragged.

void

mouseMoved

​(

MouseEvent

e)

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

void

mouseWheelMoved

​(

MouseWheelEvent

e)

Invoked when the mouse wheel is rotated.

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

- Methods declared in interface java.awt.event.

MouseListener

mouseClicked

,

mouseEntered

,

mouseExited

,

mousePressed

,

mouseReleased

---

#### Method Summary

Invoked when a mouse button is pressed on a component and then
dragged.

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

Invoked when the mouse wheel is rotated.

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

Methods declared in interface java.awt.event.

MouseListener

mouseClicked

,

mouseEntered

,

mouseExited

,

mousePressed

,

mouseReleased

---

#### Methods declared in interface java.awt.event. MouseListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MouseAdapter

```java
public MouseAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- mouseWheelMoved

```java
public void mouseWheelMoved​(
MouseWheelEvent
e)
```

Invoked when the mouse wheel is rotated.

**Specified by:** mouseWheelMoved

in interface

MouseWheelListener
**Parameters:** e

- the event to be processed
**Since:** 1.6
**See Also:** MouseWheelEvent

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Invoked when a mouse button is pressed on a component and then
dragged.

MOUSE_DRAGGED

events will continue to be
delivered to the component where the drag originated until the
mouse button is released (regardless of whether the mouse position
is within the bounds of the component).

Due to platform-dependent Drag&Drop implementations,

MOUSE_DRAGGED

events may not be delivered during a native
Drag&Drop operation.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the event to be processed
**Since:** 1.6

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the event to be processed
**Since:** 1.6

Constructor Detail

- MouseAdapter

```java
public MouseAdapter()
```

---

#### Constructor Detail

MouseAdapter

```java
public MouseAdapter()
```

---

#### MouseAdapter

public MouseAdapter()

Method Detail

- mouseWheelMoved

```java
public void mouseWheelMoved​(
MouseWheelEvent
e)
```

Invoked when the mouse wheel is rotated.

**Specified by:** mouseWheelMoved

in interface

MouseWheelListener
**Parameters:** e

- the event to be processed
**Since:** 1.6
**See Also:** MouseWheelEvent

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Invoked when a mouse button is pressed on a component and then
dragged.

MOUSE_DRAGGED

events will continue to be
delivered to the component where the drag originated until the
mouse button is released (regardless of whether the mouse position
is within the bounds of the component).

Due to platform-dependent Drag&Drop implementations,

MOUSE_DRAGGED

events may not be delivered during a native
Drag&Drop operation.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the event to be processed
**Since:** 1.6

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the event to be processed
**Since:** 1.6

---

#### Method Detail

mouseWheelMoved

```java
public void mouseWheelMoved​(
MouseWheelEvent
e)
```

Invoked when the mouse wheel is rotated.

**Specified by:** mouseWheelMoved

in interface

MouseWheelListener
**Parameters:** e

- the event to be processed
**Since:** 1.6
**See Also:** MouseWheelEvent

---

#### mouseWheelMoved

public void mouseWheelMoved​(

MouseWheelEvent

e)

Invoked when the mouse wheel is rotated.

mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Invoked when a mouse button is pressed on a component and then
dragged.

MOUSE_DRAGGED

events will continue to be
delivered to the component where the drag originated until the
mouse button is released (regardless of whether the mouse position
is within the bounds of the component).

Due to platform-dependent Drag&Drop implementations,

MOUSE_DRAGGED

events may not be delivered during a native
Drag&Drop operation.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the event to be processed
**Since:** 1.6

---

#### mouseDragged

public void mouseDragged​(

MouseEvent

e)

Invoked when a mouse button is pressed on a component and then
dragged.

MOUSE_DRAGGED

events will continue to be
delivered to the component where the drag originated until the
mouse button is released (regardless of whether the mouse position
is within the bounds of the component).

Due to platform-dependent Drag&Drop implementations,

MOUSE_DRAGGED

events may not be delivered during a native
Drag&Drop operation.

Due to platform-dependent Drag&Drop implementations,

MOUSE_DRAGGED

events may not be delivered during a native
Drag&Drop operation.

mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the event to be processed
**Since:** 1.6

---

#### mouseMoved

public void mouseMoved​(

MouseEvent

e)

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

---

