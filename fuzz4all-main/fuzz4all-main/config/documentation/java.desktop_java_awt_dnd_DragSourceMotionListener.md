# Interface DragSourceMotionListener

**Source:** `java.desktop\java\awt\dnd\DragSourceMotionListener.html`

### Class Description

```java
public interface
DragSourceMotionListener

extends
EventListener
```

A listener interface for receiving mouse motion events during a drag
operation.

The class that is interested in processing mouse motion events during
a drag operation either implements this interface or extends the abstract

DragSourceAdapter

class (overriding only the methods of
interest).

Create a listener object using that class and then register it with
a

DragSource

. Whenever the mouse moves during a drag
operation initiated with this

DragSource

, that object's

dragMouseMoved

method is invoked, and the

DragSourceDragEvent

is passed to it.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void dragMouseMoved​(
DragSourceDragEvent
dsde)

Called whenever the mouse is moved during a drag operation.

**Parameters:**
- dsde

- the

DragSourceDragEvent

---

### Additional Sections

#### Interface DragSourceMotionListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** DragSourceAdapter

,

DragSourceContext

```java
public interface
DragSourceMotionListener

extends
EventListener
```

A listener interface for receiving mouse motion events during a drag
operation.

The class that is interested in processing mouse motion events during
a drag operation either implements this interface or extends the abstract

DragSourceAdapter

class (overriding only the methods of
interest).

Create a listener object using that class and then register it with
a

DragSource

. Whenever the mouse moves during a drag
operation initiated with this

DragSource

, that object's

dragMouseMoved

method is invoked, and the

DragSourceDragEvent

is passed to it.

**Since:** 1.4
**See Also:** DragSourceDragEvent

,

DragSource

,

DragSourceListener

,

DragSourceAdapter

public interface

DragSourceMotionListener

extends

EventListener

A listener interface for receiving mouse motion events during a drag
operation.

The class that is interested in processing mouse motion events during
a drag operation either implements this interface or extends the abstract

DragSourceAdapter

class (overriding only the methods of
interest).

Create a listener object using that class and then register it with
a

DragSource

. Whenever the mouse moves during a drag
operation initiated with this

DragSource

, that object's

dragMouseMoved

method is invoked, and the

DragSourceDragEvent

is passed to it.

The class that is interested in processing mouse motion events during
a drag operation either implements this interface or extends the abstract

DragSourceAdapter

class (overriding only the methods of
interest).

Create a listener object using that class and then register it with
a

DragSource

. Whenever the mouse moves during a drag
operation initiated with this

DragSource

, that object's

dragMouseMoved

method is invoked, and the

DragSourceDragEvent

is passed to it.

Create a listener object using that class and then register it with
a

DragSource

. Whenever the mouse moves during a drag
operation initiated with this

DragSource

, that object's

dragMouseMoved

method is invoked, and the

DragSourceDragEvent

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

dragMouseMoved

​(

DragSourceDragEvent

dsde)

Called whenever the mouse is moved during a drag operation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dragMouseMoved

​(

DragSourceDragEvent

dsde)

Called whenever the mouse is moved during a drag operation.

---

#### Method Summary

Called whenever the mouse is moved during a drag operation.

============ METHOD DETAIL ==========

- Method Detail

- dragMouseMoved

```java
void dragMouseMoved​(
DragSourceDragEvent
dsde)
```

Called whenever the mouse is moved during a drag operation.

**Parameters:** dsde

- the

DragSourceDragEvent

Method Detail

- dragMouseMoved

```java
void dragMouseMoved​(
DragSourceDragEvent
dsde)
```

Called whenever the mouse is moved during a drag operation.

**Parameters:** dsde

- the

DragSourceDragEvent

---

#### Method Detail

dragMouseMoved

```java
void dragMouseMoved​(
DragSourceDragEvent
dsde)
```

Called whenever the mouse is moved during a drag operation.

**Parameters:** dsde

- the

DragSourceDragEvent

---

#### dragMouseMoved

void dragMouseMoved​(

DragSourceDragEvent

dsde)

Called whenever the mouse is moved during a drag operation.

---

