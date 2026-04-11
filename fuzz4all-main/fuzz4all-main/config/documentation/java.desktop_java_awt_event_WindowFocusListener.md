# Interface WindowFocusListener

**Source:** `java.desktop\java\awt\event\WindowFocusListener.html`

### Class Description

```java
public interface
WindowFocusListener

extends
EventListener
```

The listener interface for receiving

WindowEvents

, including

WINDOW_GAINED_FOCUS

and

WINDOW_LOST_FOCUS

events.
The class that is interested in processing a

WindowEvent

either implements this interface (and
all the methods it contains) or extends the abstract

WindowAdapter

class (overriding only the methods of interest).
The listener object created from that class is then registered with a

Window

using the

Window

's

addWindowFocusListener

method.
When the

Window

's
status changes by virtue of it being opened, closed, activated, deactivated,
iconified, or deiconified, or by focus being transferred into or out of the

Window

, the relevant method in the listener object is invoked,
and the

WindowEvent

is passed to it.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void windowGainedFocus​(
WindowEvent
e)

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

**Parameters:**
- e

- the event to be processed

---

#### void windowLostFocus​(
WindowEvent
e)

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface WindowFocusListener

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
WindowFocusListener

extends
EventListener
```

The listener interface for receiving

WindowEvents

, including

WINDOW_GAINED_FOCUS

and

WINDOW_LOST_FOCUS

events.
The class that is interested in processing a

WindowEvent

either implements this interface (and
all the methods it contains) or extends the abstract

WindowAdapter

class (overriding only the methods of interest).
The listener object created from that class is then registered with a

Window

using the

Window

's

addWindowFocusListener

method.
When the

Window

's
status changes by virtue of it being opened, closed, activated, deactivated,
iconified, or deiconified, or by focus being transferred into or out of the

Window

, the relevant method in the listener object is invoked,
and the

WindowEvent

is passed to it.

**Since:** 1.4
**See Also:** WindowAdapter

,

WindowEvent

,

Tutorial: Writing a Window Listener

public interface

WindowFocusListener

extends

EventListener

The listener interface for receiving

WindowEvents

, including

WINDOW_GAINED_FOCUS

and

WINDOW_LOST_FOCUS

events.
The class that is interested in processing a

WindowEvent

either implements this interface (and
all the methods it contains) or extends the abstract

WindowAdapter

class (overriding only the methods of interest).
The listener object created from that class is then registered with a

Window

using the

Window

's

addWindowFocusListener

method.
When the

Window

's
status changes by virtue of it being opened, closed, activated, deactivated,
iconified, or deiconified, or by focus being transferred into or out of the

Window

, the relevant method in the listener object is invoked,
and the

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

windowGainedFocus

​(

WindowEvent

e)

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

void

windowLostFocus

​(

WindowEvent

e)

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

windowGainedFocus

​(

WindowEvent

e)

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

void

windowLostFocus

​(

WindowEvent

e)

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

---

#### Method Summary

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

============ METHOD DETAIL ==========

- Method Detail

- windowGainedFocus

```java
void windowGainedFocus​(
WindowEvent
e)
```

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

**Parameters:** e

- the event to be processed

- windowLostFocus

```java
void windowLostFocus​(
WindowEvent
e)
```

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

**Parameters:** e

- the event to be processed

Method Detail

- windowGainedFocus

```java
void windowGainedFocus​(
WindowEvent
e)
```

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

**Parameters:** e

- the event to be processed

- windowLostFocus

```java
void windowLostFocus​(
WindowEvent
e)
```

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

**Parameters:** e

- the event to be processed

---

#### Method Detail

windowGainedFocus

```java
void windowGainedFocus​(
WindowEvent
e)
```

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

**Parameters:** e

- the event to be processed

---

#### windowGainedFocus

void windowGainedFocus​(

WindowEvent

e)

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

windowLostFocus

```java
void windowLostFocus​(
WindowEvent
e)
```

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

**Parameters:** e

- the event to be processed

---

#### windowLostFocus

void windowLostFocus​(

WindowEvent

e)

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

---

