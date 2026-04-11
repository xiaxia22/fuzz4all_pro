# Interface MouseMotionListener

**Source:** `java.desktop\java\awt\event\MouseMotionListener.html`

### Class Description

```java
public interface
MouseMotionListener

extends
EventListener
```

The listener interface for receiving mouse motion events on a component.
(For clicks and other mouse events, use the

MouseListener

.)

The class that is interested in processing a mouse motion event
either implements this interface (and all the methods it
contains) or extends the abstract

MouseMotionAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addMouseMotionListener

method. A mouse motion event is generated when the mouse is moved
or dragged. (Many such events will be generated). When a mouse motion event
occurs, the relevant method in the listener object is invoked, and
the

MouseEvent

is passed to it.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void mouseDragged​(
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

**Parameters:**
- e

- the event to be processed

---

#### void mouseMoved​(
MouseEvent
e)

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface MouseMotionListener

**All Superinterfaces:** EventListener

**All Known Subinterfaces:** MouseInputListener

**All Known Implementing Classes:** AWTEventMulticaster

,

BasicButtonListener

,

BasicComboPopup.InvocationMouseHandler

,

BasicComboPopup.InvocationMouseMotionHandler

,

BasicComboPopup.ListMouseHandler

,

BasicComboPopup.ListMouseMotionHandler

,

BasicDesktopIconUI.MouseInputHandler

,

BasicFileChooserUI.DoubleClickListener

,

BasicInternalFrameUI.BorderListener

,

BasicInternalFrameUI.GlassPaneDispatcher

,

BasicListUI.MouseInputHandler

,

BasicMenuItemUI.MouseInputHandler

,

BasicMenuUI.MouseInputHandler

,

BasicScrollBarUI.ArrowButtonListener

,

BasicScrollBarUI.TrackListener

,

BasicSliderUI.TrackListener

,

BasicSplitPaneDivider.MouseHandler

,

BasicTabbedPaneUI.MouseHandler

,

BasicTableHeaderUI.MouseInputHandler

,

BasicTableUI.MouseInputHandler

,

BasicTextUI.BasicCaret

,

BasicToolBarUI.DockingListener

,

BasicTreeUI.MouseHandler

,

BasicTreeUI.MouseInputHandler

,

DefaultCaret

,

FormView.MouseEventListener

,

HTMLEditorKit.LinkController

,

MetalFileChooserUI.SingleClickListener

,

MetalToolBarUI.MetalDockingListener

,

MouseAdapter

,

MouseDragGestureRecognizer

,

MouseInputAdapter

,

MouseMotionAdapter

,

ToolTipManager

```java
public interface
MouseMotionListener

extends
EventListener
```

The listener interface for receiving mouse motion events on a component.
(For clicks and other mouse events, use the

MouseListener

.)

The class that is interested in processing a mouse motion event
either implements this interface (and all the methods it
contains) or extends the abstract

MouseMotionAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addMouseMotionListener

method. A mouse motion event is generated when the mouse is moved
or dragged. (Many such events will be generated). When a mouse motion event
occurs, the relevant method in the listener object is invoked, and
the

MouseEvent

is passed to it.

**Since:** 1.1
**See Also:** MouseMotionAdapter

,

MouseEvent

,

Tutorial: Writing a Mouse Motion Listener

public interface

MouseMotionListener

extends

EventListener

The listener interface for receiving mouse motion events on a component.
(For clicks and other mouse events, use the

MouseListener

.)

The class that is interested in processing a mouse motion event
either implements this interface (and all the methods it
contains) or extends the abstract

MouseMotionAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addMouseMotionListener

method. A mouse motion event is generated when the mouse is moved
or dragged. (Many such events will be generated). When a mouse motion event
occurs, the relevant method in the listener object is invoked, and
the

MouseEvent

is passed to it.

The class that is interested in processing a mouse motion event
either implements this interface (and all the methods it
contains) or extends the abstract

MouseMotionAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addMouseMotionListener

method. A mouse motion event is generated when the mouse is moved
or dragged. (Many such events will be generated). When a mouse motion event
occurs, the relevant method in the listener object is invoked, and
the

MouseEvent

is passed to it.

The listener object created from that class is then registered with a
component using the component's

addMouseMotionListener

method. A mouse motion event is generated when the mouse is moved
or dragged. (Many such events will be generated). When a mouse motion event
occurs, the relevant method in the listener object is invoked, and
the

MouseEvent

is passed to it.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

Method Summary

All Methods

Instance Methods

Abstract Methods

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

---

#### Method Summary

Invoked when a mouse button is pressed on a component and then
dragged.

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

============ METHOD DETAIL ==========

- Method Detail

- mouseDragged

```java
void mouseDragged​(
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

**Parameters:** e

- the event to be processed

- mouseMoved

```java
void mouseMoved​(
MouseEvent
e)
```

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

**Parameters:** e

- the event to be processed

Method Detail

- mouseDragged

```java
void mouseDragged​(
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

**Parameters:** e

- the event to be processed

- mouseMoved

```java
void mouseMoved​(
MouseEvent
e)
```

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

**Parameters:** e

- the event to be processed

---

#### Method Detail

mouseDragged

```java
void mouseDragged​(
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

**Parameters:** e

- the event to be processed

---

#### mouseDragged

void mouseDragged​(

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
void mouseMoved​(
MouseEvent
e)
```

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

**Parameters:** e

- the event to be processed

---

#### mouseMoved

void mouseMoved​(

MouseEvent

e)

Invoked when the mouse cursor has been moved onto a component
but no buttons have been pushed.

---

