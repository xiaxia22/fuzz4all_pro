# Class MouseMotionAdapter

**Source:** `java.desktop\java\awt\event\MouseMotionAdapter.html`

### Class Description

```java
public abstract class
MouseMotionAdapter

extends
Object

implements
MouseMotionListener
```

An abstract adapter class for receiving mouse motion events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Mouse motion events occur when a mouse is moved or dragged.
(Many such events will be generated in a normal program.
To track clicks and other mouse events, use the MouseAdapter.)

Extend this class to create a

MouseEvent

listener
and override the methods for the events of interest. (If you implement the

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseMotionListener

method. When the mouse is moved or dragged, the relevant method in the
listener object is invoked and the

MouseEvent

is passed to it.

**All Implemented Interfaces:** MouseMotionListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public MouseMotionAdapter()

*No description found.*

---

### Method Details

#### public void mouseDragged​(
MouseEvent
e)

Invoked when a mouse button is pressed on a component and then
dragged. Mouse drag events will continue to be delivered to
the component where the first originated until the mouse button is
released (regardless of whether the mouse position is within the
bounds of the component).

**Specified by:**
- mouseDragged

in interface

MouseMotionListener

**Parameters:**
- e

- the event to be processed

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

- the event to be processed

---

### Additional Sections

#### Class MouseMotionAdapter

java.lang.Object

- java.awt.event.MouseMotionAdapter

java.awt.event.MouseMotionAdapter

**All Implemented Interfaces:** MouseMotionListener

,

EventListener

**Direct Known Subclasses:** BasicComboPopup.InvocationMouseMotionHandler

,

BasicComboPopup.ListMouseMotionHandler

```java
public abstract class
MouseMotionAdapter

extends
Object

implements
MouseMotionListener
```

An abstract adapter class for receiving mouse motion events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Mouse motion events occur when a mouse is moved or dragged.
(Many such events will be generated in a normal program.
To track clicks and other mouse events, use the MouseAdapter.)

Extend this class to create a

MouseEvent

listener
and override the methods for the events of interest. (If you implement the

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseMotionListener

method. When the mouse is moved or dragged, the relevant method in the
listener object is invoked and the

MouseEvent

is passed to it.

**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

Tutorial: Writing a Mouse Motion Listener

public abstract class

MouseMotionAdapter

extends

Object

implements

MouseMotionListener

An abstract adapter class for receiving mouse motion events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Mouse motion events occur when a mouse is moved or dragged.
(Many such events will be generated in a normal program.
To track clicks and other mouse events, use the MouseAdapter.)

Extend this class to create a

MouseEvent

listener
and override the methods for the events of interest. (If you implement the

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseMotionListener

method. When the mouse is moved or dragged, the relevant method in the
listener object is invoked and the

MouseEvent

is passed to it.

Mouse motion events occur when a mouse is moved or dragged.
(Many such events will be generated in a normal program.
To track clicks and other mouse events, use the MouseAdapter.)

Extend this class to create a

MouseEvent

listener
and override the methods for the events of interest. (If you implement the

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseMotionListener

method. When the mouse is moved or dragged, the relevant method in the
listener object is invoked and the

MouseEvent

is passed to it.

Extend this class to create a

MouseEvent

listener
and override the methods for the events of interest. (If you implement the

MouseMotionListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addMouseMotionListener

method. When the mouse is moved or dragged, the relevant method in the
listener object is invoked and the

MouseEvent

is passed to it.

Create a listener object using the extended class and then register it with
a component using the component's

addMouseMotionListener

method. When the mouse is moved or dragged, the relevant method in the
listener object is invoked and the

MouseEvent

is passed to it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MouseMotionAdapter

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

Invoked when the mouse button has been moved on a component
(with no buttons no down).

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

MouseMotionAdapter

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

Invoked when the mouse button has been moved on a component
(with no buttons no down).

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

Invoked when a mouse button is pressed on a component and then
dragged.

Invoked when the mouse button has been moved on a component
(with no buttons no down).

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

- MouseMotionAdapter

```java
public MouseMotionAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Invoked when a mouse button is pressed on a component and then
dragged. Mouse drag events will continue to be delivered to
the component where the first originated until the mouse button is
released (regardless of whether the mouse position is within the
bounds of the component).

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the event to be processed

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

- the event to be processed

Constructor Detail

- MouseMotionAdapter

```java
public MouseMotionAdapter()
```

---

#### Constructor Detail

MouseMotionAdapter

```java
public MouseMotionAdapter()
```

---

#### MouseMotionAdapter

public MouseMotionAdapter()

Method Detail

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Invoked when a mouse button is pressed on a component and then
dragged. Mouse drag events will continue to be delivered to
the component where the first originated until the mouse button is
released (regardless of whether the mouse position is within the
bounds of the component).

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the event to be processed

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

- the event to be processed

---

#### Method Detail

mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Invoked when a mouse button is pressed on a component and then
dragged. Mouse drag events will continue to be delivered to
the component where the first originated until the mouse button is
released (regardless of whether the mouse position is within the
bounds of the component).

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the event to be processed

---

#### mouseDragged

public void mouseDragged​(

MouseEvent

e)

Invoked when a mouse button is pressed on a component and then
dragged. Mouse drag events will continue to be delivered to
the component where the first originated until the mouse button is
released (regardless of whether the mouse position is within the
bounds of the component).

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

- the event to be processed

---

#### mouseMoved

public void mouseMoved​(

MouseEvent

e)

Invoked when the mouse button has been moved on a component
(with no buttons no down).

---

