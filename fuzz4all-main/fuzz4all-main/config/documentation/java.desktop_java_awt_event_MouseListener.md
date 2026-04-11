# Interface MouseListener

**Source:** `java.desktop\java\awt\event\MouseListener.html`

### Class Description

```java
public interface
MouseListener

extends
EventListener
```

The listener interface for receiving "interesting" mouse events
(press, release, click, enter, and exit) on a component.
(To track mouse moves and mouse drags, use the

MouseMotionListener

.)

The class that is interested in processing a mouse event
either implements this interface (and all the methods it
contains) or extends the abstract

MouseAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addMouseListener

method. A mouse event is generated when the mouse is pressed, released
clicked (pressed and released). A mouse event is also generated when
the mouse cursor enters or leaves a component. When a mouse event
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

#### void mouseClicked​(
MouseEvent
e)

Invoked when the mouse button has been clicked (pressed
and released) on a component.

**Parameters:**
- e

- the event to be processed

---

#### void mousePressed​(
MouseEvent
e)

Invoked when a mouse button has been pressed on a component.

**Parameters:**
- e

- the event to be processed

---

#### void mouseReleased​(
MouseEvent
e)

Invoked when a mouse button has been released on a component.

**Parameters:**
- e

- the event to be processed

---

#### void mouseEntered​(
MouseEvent
e)

Invoked when the mouse enters a component.

**Parameters:**
- e

- the event to be processed

---

#### void mouseExited​(
MouseEvent
e)

Invoked when the mouse exits a component.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface MouseListener

**All Superinterfaces:** EventListener

**All Known Subinterfaces:** MouseInputListener

**All Known Implementing Classes:** AWTEventMulticaster

,

BasicButtonListener

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

ToolTipManager

```java
public interface
MouseListener

extends
EventListener
```

The listener interface for receiving "interesting" mouse events
(press, release, click, enter, and exit) on a component.
(To track mouse moves and mouse drags, use the

MouseMotionListener

.)

The class that is interested in processing a mouse event
either implements this interface (and all the methods it
contains) or extends the abstract

MouseAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addMouseListener

method. A mouse event is generated when the mouse is pressed, released
clicked (pressed and released). A mouse event is also generated when
the mouse cursor enters or leaves a component. When a mouse event
occurs, the relevant method in the listener object is invoked, and
the

MouseEvent

is passed to it.

**Since:** 1.1
**See Also:** MouseAdapter

,

MouseEvent

,

Tutorial: Writing a Mouse Listener

public interface

MouseListener

extends

EventListener

The listener interface for receiving "interesting" mouse events
(press, release, click, enter, and exit) on a component.
(To track mouse moves and mouse drags, use the

MouseMotionListener

.)

The class that is interested in processing a mouse event
either implements this interface (and all the methods it
contains) or extends the abstract

MouseAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addMouseListener

method. A mouse event is generated when the mouse is pressed, released
clicked (pressed and released). A mouse event is also generated when
the mouse cursor enters or leaves a component. When a mouse event
occurs, the relevant method in the listener object is invoked, and
the

MouseEvent

is passed to it.

The class that is interested in processing a mouse event
either implements this interface (and all the methods it
contains) or extends the abstract

MouseAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addMouseListener

method. A mouse event is generated when the mouse is pressed, released
clicked (pressed and released). A mouse event is also generated when
the mouse cursor enters or leaves a component. When a mouse event
occurs, the relevant method in the listener object is invoked, and
the

MouseEvent

is passed to it.

The listener object created from that class is then registered with a
component using the component's

addMouseListener

method. A mouse event is generated when the mouse is pressed, released
clicked (pressed and released). A mouse event is also generated when
the mouse cursor enters or leaves a component. When a mouse event
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

mouseClicked

​(

MouseEvent

e)

Invoked when the mouse button has been clicked (pressed
and released) on a component.

void

mouseEntered

​(

MouseEvent

e)

Invoked when the mouse enters a component.

void

mouseExited

​(

MouseEvent

e)

Invoked when the mouse exits a component.

void

mousePressed

​(

MouseEvent

e)

Invoked when a mouse button has been pressed on a component.

void

mouseReleased

​(

MouseEvent

e)

Invoked when a mouse button has been released on a component.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

mouseClicked

​(

MouseEvent

e)

Invoked when the mouse button has been clicked (pressed
and released) on a component.

void

mouseEntered

​(

MouseEvent

e)

Invoked when the mouse enters a component.

void

mouseExited

​(

MouseEvent

e)

Invoked when the mouse exits a component.

void

mousePressed

​(

MouseEvent

e)

Invoked when a mouse button has been pressed on a component.

void

mouseReleased

​(

MouseEvent

e)

Invoked when a mouse button has been released on a component.

---

#### Method Summary

Invoked when the mouse button has been clicked (pressed
and released) on a component.

Invoked when the mouse enters a component.

Invoked when the mouse exits a component.

Invoked when a mouse button has been pressed on a component.

Invoked when a mouse button has been released on a component.

============ METHOD DETAIL ==========

- Method Detail

- mouseClicked

```java
void mouseClicked​(
MouseEvent
e)
```

Invoked when the mouse button has been clicked (pressed
and released) on a component.

**Parameters:** e

- the event to be processed

- mousePressed

```java
void mousePressed​(
MouseEvent
e)
```

Invoked when a mouse button has been pressed on a component.

**Parameters:** e

- the event to be processed

- mouseReleased

```java
void mouseReleased​(
MouseEvent
e)
```

Invoked when a mouse button has been released on a component.

**Parameters:** e

- the event to be processed

- mouseEntered

```java
void mouseEntered​(
MouseEvent
e)
```

Invoked when the mouse enters a component.

**Parameters:** e

- the event to be processed

- mouseExited

```java
void mouseExited​(
MouseEvent
e)
```

Invoked when the mouse exits a component.

**Parameters:** e

- the event to be processed

Method Detail

- mouseClicked

```java
void mouseClicked​(
MouseEvent
e)
```

Invoked when the mouse button has been clicked (pressed
and released) on a component.

**Parameters:** e

- the event to be processed

- mousePressed

```java
void mousePressed​(
MouseEvent
e)
```

Invoked when a mouse button has been pressed on a component.

**Parameters:** e

- the event to be processed

- mouseReleased

```java
void mouseReleased​(
MouseEvent
e)
```

Invoked when a mouse button has been released on a component.

**Parameters:** e

- the event to be processed

- mouseEntered

```java
void mouseEntered​(
MouseEvent
e)
```

Invoked when the mouse enters a component.

**Parameters:** e

- the event to be processed

- mouseExited

```java
void mouseExited​(
MouseEvent
e)
```

Invoked when the mouse exits a component.

**Parameters:** e

- the event to be processed

---

#### Method Detail

mouseClicked

```java
void mouseClicked​(
MouseEvent
e)
```

Invoked when the mouse button has been clicked (pressed
and released) on a component.

**Parameters:** e

- the event to be processed

---

#### mouseClicked

void mouseClicked​(

MouseEvent

e)

Invoked when the mouse button has been clicked (pressed
and released) on a component.

mousePressed

```java
void mousePressed​(
MouseEvent
e)
```

Invoked when a mouse button has been pressed on a component.

**Parameters:** e

- the event to be processed

---

#### mousePressed

void mousePressed​(

MouseEvent

e)

Invoked when a mouse button has been pressed on a component.

mouseReleased

```java
void mouseReleased​(
MouseEvent
e)
```

Invoked when a mouse button has been released on a component.

**Parameters:** e

- the event to be processed

---

#### mouseReleased

void mouseReleased​(

MouseEvent

e)

Invoked when a mouse button has been released on a component.

mouseEntered

```java
void mouseEntered​(
MouseEvent
e)
```

Invoked when the mouse enters a component.

**Parameters:** e

- the event to be processed

---

#### mouseEntered

void mouseEntered​(

MouseEvent

e)

Invoked when the mouse enters a component.

mouseExited

```java
void mouseExited​(
MouseEvent
e)
```

Invoked when the mouse exits a component.

**Parameters:** e

- the event to be processed

---

#### mouseExited

void mouseExited​(

MouseEvent

e)

Invoked when the mouse exits a component.

---

