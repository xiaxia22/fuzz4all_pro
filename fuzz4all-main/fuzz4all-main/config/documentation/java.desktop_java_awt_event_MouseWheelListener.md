# Interface MouseWheelListener

**Source:** `java.desktop\java\awt\event\MouseWheelListener.html`

### Class Description

```java
public interface
MouseWheelListener

extends
EventListener
```

The listener interface for receiving mouse wheel events on a component.
(For clicks and other mouse events, use the

MouseListener

.
For mouse movement and drags, use the

MouseMotionListener

.)

The class that is interested in processing a mouse wheel event
implements this interface (and all the methods it contains).

The listener object created from that class is then registered with a
component using the component's

addMouseWheelListener

method. A mouse wheel event is generated when the mouse wheel is rotated.
When a mouse wheel event occurs, that object's

mouseWheelMoved

method is invoked.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void mouseWheelMoved​(
MouseWheelEvent
e)

Invoked when the mouse wheel is rotated.

**Parameters:**
- e

- the event to be processed

**See Also:**
- MouseWheelEvent

---

### Additional Sections

#### Interface MouseWheelListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

,

BasicComboPopup.InvocationMouseHandler

,

BasicComboPopup.ListMouseHandler

,

BasicDesktopIconUI.MouseInputHandler

,

BasicFileChooserUI.DoubleClickListener

,

BasicInternalFrameUI.BorderListener

,

BasicScrollBarUI.ArrowButtonListener

,

BasicScrollBarUI.TrackListener

,

BasicScrollPaneUI.MouseWheelHandler

,

BasicSliderUI.TrackListener

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

MouseAdapter

,

MouseInputAdapter

,

ToolTipManager

```java
public interface
MouseWheelListener

extends
EventListener
```

The listener interface for receiving mouse wheel events on a component.
(For clicks and other mouse events, use the

MouseListener

.
For mouse movement and drags, use the

MouseMotionListener

.)

The class that is interested in processing a mouse wheel event
implements this interface (and all the methods it contains).

The listener object created from that class is then registered with a
component using the component's

addMouseWheelListener

method. A mouse wheel event is generated when the mouse wheel is rotated.
When a mouse wheel event occurs, that object's

mouseWheelMoved

method is invoked.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

**Since:** 1.4
**See Also:** MouseWheelEvent

public interface

MouseWheelListener

extends

EventListener

The listener interface for receiving mouse wheel events on a component.
(For clicks and other mouse events, use the

MouseListener

.
For mouse movement and drags, use the

MouseMotionListener

.)

The class that is interested in processing a mouse wheel event
implements this interface (and all the methods it contains).

The listener object created from that class is then registered with a
component using the component's

addMouseWheelListener

method. A mouse wheel event is generated when the mouse wheel is rotated.
When a mouse wheel event occurs, that object's

mouseWheelMoved

method is invoked.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

The class that is interested in processing a mouse wheel event
implements this interface (and all the methods it contains).

The listener object created from that class is then registered with a
component using the component's

addMouseWheelListener

method. A mouse wheel event is generated when the mouse wheel is rotated.
When a mouse wheel event occurs, that object's

mouseWheelMoved

method is invoked.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

The listener object created from that class is then registered with a
component using the component's

addMouseWheelListener

method. A mouse wheel event is generated when the mouse wheel is rotated.
When a mouse wheel event occurs, that object's

mouseWheelMoved

method is invoked.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

mouseWheelMoved

​(

MouseWheelEvent

e)

Invoked when the mouse wheel is rotated.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

mouseWheelMoved

​(

MouseWheelEvent

e)

Invoked when the mouse wheel is rotated.

---

#### Method Summary

Invoked when the mouse wheel is rotated.

============ METHOD DETAIL ==========

- Method Detail

- mouseWheelMoved

```java
void mouseWheelMoved​(
MouseWheelEvent
e)
```

Invoked when the mouse wheel is rotated.

**Parameters:** e

- the event to be processed
**See Also:** MouseWheelEvent

Method Detail

- mouseWheelMoved

```java
void mouseWheelMoved​(
MouseWheelEvent
e)
```

Invoked when the mouse wheel is rotated.

**Parameters:** e

- the event to be processed
**See Also:** MouseWheelEvent

---

#### Method Detail

mouseWheelMoved

```java
void mouseWheelMoved​(
MouseWheelEvent
e)
```

Invoked when the mouse wheel is rotated.

**Parameters:** e

- the event to be processed
**See Also:** MouseWheelEvent

---

#### mouseWheelMoved

void mouseWheelMoved​(

MouseWheelEvent

e)

Invoked when the mouse wheel is rotated.

---

