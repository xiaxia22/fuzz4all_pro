# Class MouseDragGestureRecognizer

**Source:** `java.desktop\java\awt\dnd\MouseDragGestureRecognizer.html`

### Class Description

```java
public abstract class
MouseDragGestureRecognizer

extends
DragGestureRecognizer

implements
MouseListener
,
MouseMotionListener
```

This abstract subclass of

DragGestureRecognizer

defines a

DragGestureRecognizer

for mouse-based gestures.

Each platform implements its own concrete subclass of this class,
available via the Toolkit.createDragGestureRecognizer() method,
to encapsulate
the recognition of the platform dependent mouse gesture(s) that initiate
a Drag and Drop operation.

Mouse drag gesture recognizers should honor the
drag gesture motion threshold, available through

DragSource.getDragThreshold()

.
A drag gesture should be recognized only when the distance
in either the horizontal or vertical direction between
the location of the latest mouse dragged event and the
location of the corresponding mouse button pressed event
is greater than the drag gesture motion threshold.

Drag gesture recognizers created with

DragSource.createDefaultDragGestureRecognizer(java.awt.Component, int, java.awt.dnd.DragGestureListener)

follow this convention.

**All Implemented Interfaces:** MouseListener

,

MouseMotionListener

,

Serializable

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c,
int act,

DragGestureListener
dgl)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, the

Component

to observe, the action(s)
permitted for this drag operation, and
the

DragGestureListener

to
notify when a drag gesture is detected.

**Parameters:**
- ds

- The DragSource for the Component c
- c

- The Component to observe
- act

- The actions permitted for this Drag
- dgl

- The DragGestureListener to notify when a gesture is detected

---

#### protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c,
int act)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for
the

Component

c,
the

Component

to observe, and the action(s)
permitted for this drag operation.

**Parameters:**
- ds

- The DragSource for the Component c
- c

- The Component to observe
- act

- The actions permitted for this drag

---

#### protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, and the

Component

to observe.

**Parameters:**
- ds

- The DragSource for the Component c
- c

- The Component to observe

---

#### protected MouseDragGestureRecognizer​(
DragSource
ds)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

.

**Parameters:**
- ds

- The DragSource for the Component

---

### Method Details

#### protected void registerListeners()

register this DragGestureRecognizer's Listeners with the Component

**Specified by:**
- registerListeners

in class

DragGestureRecognizer

---

#### protected void unregisterListeners()

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

**Specified by:**
- unregisterListeners

in class

DragGestureRecognizer

---

#### public void mouseClicked​(
MouseEvent
e)

Invoked when the mouse has been clicked on a component.

**Specified by:**
- mouseClicked

in interface

MouseListener

**Parameters:**
- e

- the

MouseEvent

---

#### public void mousePressed​(
MouseEvent
e)

Invoked when a mouse button has been
pressed on a

Component

.

**Specified by:**
- mousePressed

in interface

MouseListener

**Parameters:**
- e

- the

MouseEvent

---

#### public void mouseReleased​(
MouseEvent
e)

Invoked when a mouse button has been released on a component.

**Specified by:**
- mouseReleased

in interface

MouseListener

**Parameters:**
- e

- the

MouseEvent

---

#### public void mouseEntered​(
MouseEvent
e)

Invoked when the mouse enters a component.

**Specified by:**
- mouseEntered

in interface

MouseListener

**Parameters:**
- e

- the

MouseEvent

---

#### public void mouseExited​(
MouseEvent
e)

Invoked when the mouse exits a component.

**Specified by:**
- mouseExited

in interface

MouseListener

**Parameters:**
- e

- the

MouseEvent

---

#### public void mouseDragged​(
MouseEvent
e)

Invoked when a mouse button is pressed on a component.

**Specified by:**
- mouseDragged

in interface

MouseMotionListener

**Parameters:**
- e

- the

MouseEvent

---

#### public void mouseMoved​(
MouseEvent
e)

Invoked when the mouse button has been moved on a component
(with no buttons no down).

**Specified by:**
- mouseMoved

in interface

MouseMotionListener

**Parameters:**
- e

- the

MouseEvent

---

### Additional Sections

#### Class MouseDragGestureRecognizer

java.lang.Object

- java.awt.dnd.DragGestureRecognizer
- - java.awt.dnd.MouseDragGestureRecognizer

java.awt.dnd.DragGestureRecognizer

- java.awt.dnd.MouseDragGestureRecognizer

java.awt.dnd.MouseDragGestureRecognizer

**All Implemented Interfaces:** MouseListener

,

MouseMotionListener

,

Serializable

,

EventListener

```java
public abstract class
MouseDragGestureRecognizer

extends
DragGestureRecognizer

implements
MouseListener
,
MouseMotionListener
```

This abstract subclass of

DragGestureRecognizer

defines a

DragGestureRecognizer

for mouse-based gestures.

Each platform implements its own concrete subclass of this class,
available via the Toolkit.createDragGestureRecognizer() method,
to encapsulate
the recognition of the platform dependent mouse gesture(s) that initiate
a Drag and Drop operation.

Mouse drag gesture recognizers should honor the
drag gesture motion threshold, available through

DragSource.getDragThreshold()

.
A drag gesture should be recognized only when the distance
in either the horizontal or vertical direction between
the location of the latest mouse dragged event and the
location of the corresponding mouse button pressed event
is greater than the drag gesture motion threshold.

Drag gesture recognizers created with

DragSource.createDefaultDragGestureRecognizer(java.awt.Component, int, java.awt.dnd.DragGestureListener)

follow this convention.

**See Also:** DragGestureListener

,

DragGestureEvent

,

DragSource

,

Serialized Form

public abstract class

MouseDragGestureRecognizer

extends

DragGestureRecognizer

implements

MouseListener

,

MouseMotionListener

This abstract subclass of

DragGestureRecognizer

defines a

DragGestureRecognizer

for mouse-based gestures.

Each platform implements its own concrete subclass of this class,
available via the Toolkit.createDragGestureRecognizer() method,
to encapsulate
the recognition of the platform dependent mouse gesture(s) that initiate
a Drag and Drop operation.

Mouse drag gesture recognizers should honor the
drag gesture motion threshold, available through

DragSource.getDragThreshold()

.
A drag gesture should be recognized only when the distance
in either the horizontal or vertical direction between
the location of the latest mouse dragged event and the
location of the corresponding mouse button pressed event
is greater than the drag gesture motion threshold.

Drag gesture recognizers created with

DragSource.createDefaultDragGestureRecognizer(java.awt.Component, int, java.awt.dnd.DragGestureListener)

follow this convention.

Mouse drag gesture recognizers should honor the
drag gesture motion threshold, available through

DragSource.getDragThreshold()

.
A drag gesture should be recognized only when the distance
in either the horizontal or vertical direction between
the location of the latest mouse dragged event and the
location of the corresponding mouse button pressed event
is greater than the drag gesture motion threshold.

Drag gesture recognizers created with

DragSource.createDefaultDragGestureRecognizer(java.awt.Component, int, java.awt.dnd.DragGestureListener)

follow this convention.

Drag gesture recognizers created with

DragSource.createDefaultDragGestureRecognizer(java.awt.Component, int, java.awt.dnd.DragGestureListener)

follow this convention.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.dnd.

DragGestureRecognizer

component

,

dragGestureListener

,

dragSource

,

events

,

sourceActions

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MouseDragGestureRecognizer

​(

DragSource

ds)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

.

protected

MouseDragGestureRecognizer

​(

DragSource

ds,

Component

c)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, and the

Component

to observe.

protected

MouseDragGestureRecognizer

​(

DragSource

ds,

Component

c,
int act)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for
the

Component

c,
the

Component

to observe, and the action(s)
permitted for this drag operation.

protected

MouseDragGestureRecognizer

​(

DragSource

ds,

Component

c,
int act,

DragGestureListener

dgl)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, the

Component

to observe, the action(s)
permitted for this drag operation, and
the

DragGestureListener

to
notify when a drag gesture is detected.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

mouseClicked

​(

MouseEvent

e)

Invoked when the mouse has been clicked on a component.

void

mouseDragged

​(

MouseEvent

e)

Invoked when a mouse button is pressed on a component.

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

mouseMoved

​(

MouseEvent

e)

Invoked when the mouse button has been moved on a component
(with no buttons no down).

void

mousePressed

​(

MouseEvent

e)

Invoked when a mouse button has been
pressed on a

Component

.

void

mouseReleased

​(

MouseEvent

e)

Invoked when a mouse button has been released on a component.

protected void

registerListeners

()

register this DragGestureRecognizer's Listeners with the Component

protected void

unregisterListeners

()

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

- Methods declared in class java.awt.dnd.

DragGestureRecognizer

addDragGestureListener

,

appendEvent

,

fireDragGestureRecognized

,

getComponent

,

getDragSource

,

getSourceActions

,

getTriggerEvent

,

removeDragGestureListener

,

resetRecognizer

,

setComponent

,

setSourceActions

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

- Fields declared in class java.awt.dnd.

DragGestureRecognizer

component

,

dragGestureListener

,

dragSource

,

events

,

sourceActions

---

#### Field Summary

Fields declared in class java.awt.dnd.

DragGestureRecognizer

component

,

dragGestureListener

,

dragSource

,

events

,

sourceActions

---

#### Fields declared in class java.awt.dnd. DragGestureRecognizer

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MouseDragGestureRecognizer

​(

DragSource

ds)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

.

protected

MouseDragGestureRecognizer

​(

DragSource

ds,

Component

c)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, and the

Component

to observe.

protected

MouseDragGestureRecognizer

​(

DragSource

ds,

Component

c,
int act)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for
the

Component

c,
the

Component

to observe, and the action(s)
permitted for this drag operation.

protected

MouseDragGestureRecognizer

​(

DragSource

ds,

Component

c,
int act,

DragGestureListener

dgl)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, the

Component

to observe, the action(s)
permitted for this drag operation, and
the

DragGestureListener

to
notify when a drag gesture is detected.

---

#### Constructor Summary

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

.

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, and the

Component

to observe.

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for
the

Component

c,
the

Component

to observe, and the action(s)
permitted for this drag operation.

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, the

Component

to observe, the action(s)
permitted for this drag operation, and
the

DragGestureListener

to
notify when a drag gesture is detected.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

mouseClicked

​(

MouseEvent

e)

Invoked when the mouse has been clicked on a component.

void

mouseDragged

​(

MouseEvent

e)

Invoked when a mouse button is pressed on a component.

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

mouseMoved

​(

MouseEvent

e)

Invoked when the mouse button has been moved on a component
(with no buttons no down).

void

mousePressed

​(

MouseEvent

e)

Invoked when a mouse button has been
pressed on a

Component

.

void

mouseReleased

​(

MouseEvent

e)

Invoked when a mouse button has been released on a component.

protected void

registerListeners

()

register this DragGestureRecognizer's Listeners with the Component

protected void

unregisterListeners

()

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

- Methods declared in class java.awt.dnd.

DragGestureRecognizer

addDragGestureListener

,

appendEvent

,

fireDragGestureRecognized

,

getComponent

,

getDragSource

,

getSourceActions

,

getTriggerEvent

,

removeDragGestureListener

,

resetRecognizer

,

setComponent

,

setSourceActions

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

Invoked when the mouse has been clicked on a component.

Invoked when a mouse button is pressed on a component.

Invoked when the mouse enters a component.

Invoked when the mouse exits a component.

Invoked when the mouse button has been moved on a component
(with no buttons no down).

Invoked when a mouse button has been
pressed on a

Component

.

Invoked when a mouse button has been released on a component.

register this DragGestureRecognizer's Listeners with the Component

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

Methods declared in class java.awt.dnd.

DragGestureRecognizer

addDragGestureListener

,

appendEvent

,

fireDragGestureRecognized

,

getComponent

,

getDragSource

,

getSourceActions

,

getTriggerEvent

,

removeDragGestureListener

,

resetRecognizer

,

setComponent

,

setSourceActions

---

#### Methods declared in class java.awt.dnd. DragGestureRecognizer

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

- MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c,
int act,

DragGestureListener
dgl)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, the

Component

to observe, the action(s)
permitted for this drag operation, and
the

DragGestureListener

to
notify when a drag gesture is detected.

**Parameters:** ds

- The DragSource for the Component c
**Parameters:** c

- The Component to observe
**Parameters:** act

- The actions permitted for this Drag
**Parameters:** dgl

- The DragGestureListener to notify when a gesture is detected

- MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c,
int act)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for
the

Component

c,
the

Component

to observe, and the action(s)
permitted for this drag operation.

**Parameters:** ds

- The DragSource for the Component c
**Parameters:** c

- The Component to observe
**Parameters:** act

- The actions permitted for this drag

- MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, and the

Component

to observe.

**Parameters:** ds

- The DragSource for the Component c
**Parameters:** c

- The Component to observe

- MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

.

**Parameters:** ds

- The DragSource for the Component

============ METHOD DETAIL ==========

- Method Detail

- registerListeners

```java
protected void registerListeners()
```

register this DragGestureRecognizer's Listeners with the Component

**Specified by:** registerListeners

in class

DragGestureRecognizer

- unregisterListeners

```java
protected void unregisterListeners()
```

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

**Specified by:** unregisterListeners

in class

DragGestureRecognizer

- mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Invoked when the mouse has been clicked on a component.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mousePressed

```java
public void mousePressed​(
MouseEvent
e)
```

Invoked when a mouse button has been
pressed on a

Component

.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mouseReleased

```java
public void mouseReleased​(
MouseEvent
e)
```

Invoked when a mouse button has been released on a component.

**Specified by:** mouseReleased

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mouseEntered

```java
public void mouseEntered​(
MouseEvent
e)
```

Invoked when the mouse enters a component.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mouseExited

```java
public void mouseExited​(
MouseEvent
e)
```

Invoked when the mouse exits a component.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Invoked when a mouse button is pressed on a component.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the

MouseEvent

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Invoked when the mouse button has been moved on a component
(with no buttons no down).

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the

MouseEvent

Constructor Detail

- MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c,
int act,

DragGestureListener
dgl)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, the

Component

to observe, the action(s)
permitted for this drag operation, and
the

DragGestureListener

to
notify when a drag gesture is detected.

**Parameters:** ds

- The DragSource for the Component c
**Parameters:** c

- The Component to observe
**Parameters:** act

- The actions permitted for this Drag
**Parameters:** dgl

- The DragGestureListener to notify when a gesture is detected

- MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c,
int act)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for
the

Component

c,
the

Component

to observe, and the action(s)
permitted for this drag operation.

**Parameters:** ds

- The DragSource for the Component c
**Parameters:** c

- The Component to observe
**Parameters:** act

- The actions permitted for this drag

- MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, and the

Component

to observe.

**Parameters:** ds

- The DragSource for the Component c
**Parameters:** c

- The Component to observe

- MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

.

**Parameters:** ds

- The DragSource for the Component

---

#### Constructor Detail

MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c,
int act,

DragGestureListener
dgl)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, the

Component

to observe, the action(s)
permitted for this drag operation, and
the

DragGestureListener

to
notify when a drag gesture is detected.

**Parameters:** ds

- The DragSource for the Component c
**Parameters:** c

- The Component to observe
**Parameters:** act

- The actions permitted for this Drag
**Parameters:** dgl

- The DragGestureListener to notify when a gesture is detected

---

#### MouseDragGestureRecognizer

protected MouseDragGestureRecognizer​(

DragSource

ds,

Component

c,
int act,

DragGestureListener

dgl)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, the

Component

to observe, the action(s)
permitted for this drag operation, and
the

DragGestureListener

to
notify when a drag gesture is detected.

MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c,
int act)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for
the

Component

c,
the

Component

to observe, and the action(s)
permitted for this drag operation.

**Parameters:** ds

- The DragSource for the Component c
**Parameters:** c

- The Component to observe
**Parameters:** act

- The actions permitted for this drag

---

#### MouseDragGestureRecognizer

protected MouseDragGestureRecognizer​(

DragSource

ds,

Component

c,
int act)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for
the

Component

c,
the

Component

to observe, and the action(s)
permitted for this drag operation.

MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds,

Component
c)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, and the

Component

to observe.

**Parameters:** ds

- The DragSource for the Component c
**Parameters:** c

- The Component to observe

---

#### MouseDragGestureRecognizer

protected MouseDragGestureRecognizer​(

DragSource

ds,

Component

c)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

c, and the

Component

to observe.

MouseDragGestureRecognizer

```java
protected MouseDragGestureRecognizer​(
DragSource
ds)
```

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

.

**Parameters:** ds

- The DragSource for the Component

---

#### MouseDragGestureRecognizer

protected MouseDragGestureRecognizer​(

DragSource

ds)

Construct a new

MouseDragGestureRecognizer

given the

DragSource

for the

Component

.

Method Detail

- registerListeners

```java
protected void registerListeners()
```

register this DragGestureRecognizer's Listeners with the Component

**Specified by:** registerListeners

in class

DragGestureRecognizer

- unregisterListeners

```java
protected void unregisterListeners()
```

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

**Specified by:** unregisterListeners

in class

DragGestureRecognizer

- mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Invoked when the mouse has been clicked on a component.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mousePressed

```java
public void mousePressed​(
MouseEvent
e)
```

Invoked when a mouse button has been
pressed on a

Component

.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mouseReleased

```java
public void mouseReleased​(
MouseEvent
e)
```

Invoked when a mouse button has been released on a component.

**Specified by:** mouseReleased

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mouseEntered

```java
public void mouseEntered​(
MouseEvent
e)
```

Invoked when the mouse enters a component.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mouseExited

```java
public void mouseExited​(
MouseEvent
e)
```

Invoked when the mouse exits a component.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Invoked when a mouse button is pressed on a component.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the

MouseEvent

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Invoked when the mouse button has been moved on a component
(with no buttons no down).

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the

MouseEvent

---

#### Method Detail

registerListeners

```java
protected void registerListeners()
```

register this DragGestureRecognizer's Listeners with the Component

**Specified by:** registerListeners

in class

DragGestureRecognizer

---

#### registerListeners

protected void registerListeners()

register this DragGestureRecognizer's Listeners with the Component

unregisterListeners

```java
protected void unregisterListeners()
```

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

**Specified by:** unregisterListeners

in class

DragGestureRecognizer

---

#### unregisterListeners

protected void unregisterListeners()

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Invoked when the mouse has been clicked on a component.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

---

#### mouseClicked

public void mouseClicked​(

MouseEvent

e)

Invoked when the mouse has been clicked on a component.

mousePressed

```java
public void mousePressed​(
MouseEvent
e)
```

Invoked when a mouse button has been
pressed on a

Component

.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

---

#### mousePressed

public void mousePressed​(

MouseEvent

e)

Invoked when a mouse button has been
pressed on a

Component

.

mouseReleased

```java
public void mouseReleased​(
MouseEvent
e)
```

Invoked when a mouse button has been released on a component.

**Specified by:** mouseReleased

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

---

#### mouseReleased

public void mouseReleased​(

MouseEvent

e)

Invoked when a mouse button has been released on a component.

mouseEntered

```java
public void mouseEntered​(
MouseEvent
e)
```

Invoked when the mouse enters a component.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

---

#### mouseEntered

public void mouseEntered​(

MouseEvent

e)

Invoked when the mouse enters a component.

mouseExited

```java
public void mouseExited​(
MouseEvent
e)
```

Invoked when the mouse exits a component.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** e

- the

MouseEvent

---

#### mouseExited

public void mouseExited​(

MouseEvent

e)

Invoked when the mouse exits a component.

mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Invoked when a mouse button is pressed on a component.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the

MouseEvent

---

#### mouseDragged

public void mouseDragged​(

MouseEvent

e)

Invoked when a mouse button is pressed on a component.

mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Invoked when the mouse button has been moved on a component
(with no buttons no down).

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the

MouseEvent

---

#### mouseMoved

public void mouseMoved​(

MouseEvent

e)

Invoked when the mouse button has been moved on a component
(with no buttons no down).

---

