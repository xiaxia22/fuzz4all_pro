# Interface WindowStateListener

**Source:** `java.desktop\java\awt\event\WindowStateListener.html`

### Class Description

```java
public interface
WindowStateListener

extends
EventListener
```

The listener interface for receiving window state events.

The class that is interested in processing a window state event
either implements this interface (and all the methods it contains)
or extends the abstract

WindowAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with
a window using the

Window

's

addWindowStateListener

method. When the window's
state changes by virtue of being iconified, maximized etc., the

windowStateChanged

method in the listener object is
invoked, and the

WindowEvent

is passed to it.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void windowStateChanged​(
WindowEvent
e)

Invoked when window state is changed.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface WindowStateListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

,

BasicToolBarUI.FrameListener

,

JMenu.WinListener

,

WindowAdapter

```java
public interface
WindowStateListener

extends
EventListener
```

The listener interface for receiving window state events.

The class that is interested in processing a window state event
either implements this interface (and all the methods it contains)
or extends the abstract

WindowAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with
a window using the

Window

's

addWindowStateListener

method. When the window's
state changes by virtue of being iconified, maximized etc., the

windowStateChanged

method in the listener object is
invoked, and the

WindowEvent

is passed to it.

**Since:** 1.4
**See Also:** WindowAdapter

,

WindowEvent

public interface

WindowStateListener

extends

EventListener

The listener interface for receiving window state events.

The class that is interested in processing a window state event
either implements this interface (and all the methods it contains)
or extends the abstract

WindowAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with
a window using the

Window

's

addWindowStateListener

method. When the window's
state changes by virtue of being iconified, maximized etc., the

windowStateChanged

method in the listener object is
invoked, and the

WindowEvent

is passed to it.

The class that is interested in processing a window state event
either implements this interface (and all the methods it contains)
or extends the abstract

WindowAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with
a window using the

Window

's

addWindowStateListener

method. When the window's
state changes by virtue of being iconified, maximized etc., the

windowStateChanged

method in the listener object is
invoked, and the

WindowEvent

is passed to it.

The listener object created from that class is then registered with
a window using the

Window

's

addWindowStateListener

method. When the window's
state changes by virtue of being iconified, maximized etc., the

windowStateChanged

method in the listener object is
invoked, and the

WindowEvent

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

windowStateChanged

​(

WindowEvent

e)

Invoked when window state is changed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

windowStateChanged

​(

WindowEvent

e)

Invoked when window state is changed.

---

#### Method Summary

Invoked when window state is changed.

============ METHOD DETAIL ==========

- Method Detail

- windowStateChanged

```java
void windowStateChanged​(
WindowEvent
e)
```

Invoked when window state is changed.

**Parameters:** e

- the event to be processed

Method Detail

- windowStateChanged

```java
void windowStateChanged​(
WindowEvent
e)
```

Invoked when window state is changed.

**Parameters:** e

- the event to be processed

---

#### Method Detail

windowStateChanged

```java
void windowStateChanged​(
WindowEvent
e)
```

Invoked when window state is changed.

**Parameters:** e

- the event to be processed

---

#### windowStateChanged

void windowStateChanged​(

WindowEvent

e)

Invoked when window state is changed.

---

