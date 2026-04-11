# Class HTMLEditorKit.LinkController

**Source:** `java.desktop\javax\swing\text\html\HTMLEditorKit.LinkController.html`

### Class Description

```java
public static class
HTMLEditorKit.LinkController

extends
MouseAdapter

implements
MouseMotionListener
,
Serializable
```

Class to watch the associated component and fire
hyperlink events on it when appropriate.

**All Implemented Interfaces:** MouseListener

,

MouseMotionListener

,

MouseWheelListener

,

Serializable

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public LinkController()

*No description found.*

---

### Method Details

#### public void mouseClicked​(
MouseEvent
e)

Called for a mouse click event.
If the component is read-only (ie a browser) then
the clicked event is used to drive an attempt to
follow the reference specified by a link.

**Specified by:**
- mouseClicked

in interface

MouseListener

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseListener.mouseClicked(java.awt.event.MouseEvent)

---

#### protected void activateLink​(int pos,

JEditorPane
editor)

Calls linkActivated on the associated JEditorPane
if the given position represents a link.

This is implemented
to forward to the method with the same name, but with the following
args both == -1.

**Parameters:**
- pos

- the position
- editor

- the editor pane

---

### Additional Sections

#### Class HTMLEditorKit.LinkController

java.lang.Object

- java.awt.event.MouseAdapter
- - javax.swing.text.html.HTMLEditorKit.LinkController

java.awt.event.MouseAdapter

- javax.swing.text.html.HTMLEditorKit.LinkController

javax.swing.text.html.HTMLEditorKit.LinkController

**All Implemented Interfaces:** MouseListener

,

MouseMotionListener

,

MouseWheelListener

,

Serializable

,

EventListener

**Enclosing class:** HTMLEditorKit

```java
public static class
HTMLEditorKit.LinkController

extends
MouseAdapter

implements
MouseMotionListener
,
Serializable
```

Class to watch the associated component and fire
hyperlink events on it when appropriate.

**See Also:** Serialized Form

public static class

HTMLEditorKit.LinkController

extends

MouseAdapter

implements

MouseMotionListener

,

Serializable

Class to watch the associated component and fire
hyperlink events on it when appropriate.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LinkController

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

activateLink

​(int pos,

JEditorPane

editor)

Calls linkActivated on the associated JEditorPane
if the given position represents a link.

void

mouseClicked

​(

MouseEvent

e)

Called for a mouse click event.

- Methods declared in class java.awt.event.

MouseAdapter

mouseDragged

,

mouseMoved

,

mouseWheelMoved

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

mouseEntered

,

mouseExited

,

mousePressed

,

mouseReleased

- Methods declared in interface java.awt.event.

MouseMotionListener

mouseDragged

,

mouseMoved

Constructor Summary

Constructors

Constructor

Description

LinkController

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

protected void

activateLink

​(int pos,

JEditorPane

editor)

Calls linkActivated on the associated JEditorPane
if the given position represents a link.

void

mouseClicked

​(

MouseEvent

e)

Called for a mouse click event.

- Methods declared in class java.awt.event.

MouseAdapter

mouseDragged

,

mouseMoved

,

mouseWheelMoved

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

mouseEntered

,

mouseExited

,

mousePressed

,

mouseReleased

- Methods declared in interface java.awt.event.

MouseMotionListener

mouseDragged

,

mouseMoved

---

#### Method Summary

Calls linkActivated on the associated JEditorPane
if the given position represents a link.

Called for a mouse click event.

Methods declared in class java.awt.event.

MouseAdapter

mouseDragged

,

mouseMoved

,

mouseWheelMoved

---

#### Methods declared in class java.awt.event. MouseAdapter

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

mouseEntered

,

mouseExited

,

mousePressed

,

mouseReleased

---

#### Methods declared in interface java.awt.event. MouseListener

Methods declared in interface java.awt.event.

MouseMotionListener

mouseDragged

,

mouseMoved

---

#### Methods declared in interface java.awt.event. MouseMotionListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LinkController

```java
public LinkController()
```

============ METHOD DETAIL ==========

- Method Detail

- mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Called for a mouse click event.
If the component is read-only (ie a browser) then
the clicked event is used to drive an attempt to
follow the reference specified by a link.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseClicked(java.awt.event.MouseEvent)

- activateLink

```java
protected void activateLink​(int pos,

JEditorPane
editor)
```

Calls linkActivated on the associated JEditorPane
if the given position represents a link.

This is implemented
to forward to the method with the same name, but with the following
args both == -1.

**Parameters:** pos

- the position
**Parameters:** editor

- the editor pane

Constructor Detail

- LinkController

```java
public LinkController()
```

---

#### Constructor Detail

LinkController

```java
public LinkController()
```

---

#### LinkController

public LinkController()

Method Detail

- mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Called for a mouse click event.
If the component is read-only (ie a browser) then
the clicked event is used to drive an attempt to
follow the reference specified by a link.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseClicked(java.awt.event.MouseEvent)

- activateLink

```java
protected void activateLink​(int pos,

JEditorPane
editor)
```

Calls linkActivated on the associated JEditorPane
if the given position represents a link.

This is implemented
to forward to the method with the same name, but with the following
args both == -1.

**Parameters:** pos

- the position
**Parameters:** editor

- the editor pane

---

#### Method Detail

mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Called for a mouse click event.
If the component is read-only (ie a browser) then
the clicked event is used to drive an attempt to
follow the reference specified by a link.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseClicked(java.awt.event.MouseEvent)

---

#### mouseClicked

public void mouseClicked​(

MouseEvent

e)

Called for a mouse click event.
If the component is read-only (ie a browser) then
the clicked event is used to drive an attempt to
follow the reference specified by a link.

activateLink

```java
protected void activateLink​(int pos,

JEditorPane
editor)
```

Calls linkActivated on the associated JEditorPane
if the given position represents a link.

This is implemented
to forward to the method with the same name, but with the following
args both == -1.

**Parameters:** pos

- the position
**Parameters:** editor

- the editor pane

---

#### activateLink

protected void activateLink​(int pos,

JEditorPane

editor)

Calls linkActivated on the associated JEditorPane
if the given position represents a link.

This is implemented
to forward to the method with the same name, but with the following
args both == -1.

This is implemented
to forward to the method with the same name, but with the following
args both == -1.

---

