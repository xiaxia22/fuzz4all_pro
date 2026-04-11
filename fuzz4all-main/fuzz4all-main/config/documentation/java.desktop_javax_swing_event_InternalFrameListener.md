# Interface InternalFrameListener

**Source:** `java.desktop\javax\swing\event\InternalFrameListener.html`

### Class Description

```java
public interface
InternalFrameListener

extends
EventListener
```

The listener interface for receiving internal frame events.
This class is functionally equivalent to the WindowListener class
in the AWT.

See

How to Write an Internal Frame Listener

in

The Java Tutorial

for further documentation.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void internalFrameOpened​(
InternalFrameEvent
e)

Invoked when a internal frame has been opened.

**Parameters:**
- e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event

**See Also:**
- JInternalFrame.show()

---

#### void internalFrameClosing​(
InternalFrameEvent
e)

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

**Parameters:**
- e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event

**See Also:**
- JInternalFrame.setDefaultCloseOperation(int)

---

#### void internalFrameClosed​(
InternalFrameEvent
e)

Invoked when an internal frame has been closed.

**Parameters:**
- e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event

**See Also:**
- JInternalFrame.setClosed(boolean)

---

#### void internalFrameIconified​(
InternalFrameEvent
e)

Invoked when an internal frame is iconified.

**Parameters:**
- e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event

**See Also:**
- JInternalFrame.setIcon(boolean)

---

#### void internalFrameDeiconified​(
InternalFrameEvent
e)

Invoked when an internal frame is de-iconified.

**Parameters:**
- e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event

**See Also:**
- JInternalFrame.setIcon(boolean)

---

#### void internalFrameActivated​(
InternalFrameEvent
e)

Invoked when an internal frame is activated.

**Parameters:**
- e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event

**See Also:**
- JInternalFrame.setSelected(boolean)

---

#### void internalFrameDeactivated​(
InternalFrameEvent
e)

Invoked when an internal frame is de-activated.

**Parameters:**
- e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event

**See Also:**
- JInternalFrame.setSelected(boolean)

---

### Additional Sections

#### Interface InternalFrameListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** BasicInternalFrameUI.BasicInternalFrameListener

,

InternalFrameAdapter

```java
public interface
InternalFrameListener

extends
EventListener
```

The listener interface for receiving internal frame events.
This class is functionally equivalent to the WindowListener class
in the AWT.

See

How to Write an Internal Frame Listener

in

The Java Tutorial

for further documentation.

**See Also:** WindowListener

public interface

InternalFrameListener

extends

EventListener

The listener interface for receiving internal frame events.
This class is functionally equivalent to the WindowListener class
in the AWT.

See

How to Write an Internal Frame Listener

in

The Java Tutorial

for further documentation.

See

How to Write an Internal Frame Listener

in

The Java Tutorial

for further documentation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

internalFrameActivated

​(

InternalFrameEvent

e)

Invoked when an internal frame is activated.

void

internalFrameClosed

​(

InternalFrameEvent

e)

Invoked when an internal frame has been closed.

void

internalFrameClosing

​(

InternalFrameEvent

e)

Invoked when an internal frame is in the process of being closed.

void

internalFrameDeactivated

​(

InternalFrameEvent

e)

Invoked when an internal frame is de-activated.

void

internalFrameDeiconified

​(

InternalFrameEvent

e)

Invoked when an internal frame is de-iconified.

void

internalFrameIconified

​(

InternalFrameEvent

e)

Invoked when an internal frame is iconified.

void

internalFrameOpened

​(

InternalFrameEvent

e)

Invoked when a internal frame has been opened.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

internalFrameActivated

​(

InternalFrameEvent

e)

Invoked when an internal frame is activated.

void

internalFrameClosed

​(

InternalFrameEvent

e)

Invoked when an internal frame has been closed.

void

internalFrameClosing

​(

InternalFrameEvent

e)

Invoked when an internal frame is in the process of being closed.

void

internalFrameDeactivated

​(

InternalFrameEvent

e)

Invoked when an internal frame is de-activated.

void

internalFrameDeiconified

​(

InternalFrameEvent

e)

Invoked when an internal frame is de-iconified.

void

internalFrameIconified

​(

InternalFrameEvent

e)

Invoked when an internal frame is iconified.

void

internalFrameOpened

​(

InternalFrameEvent

e)

Invoked when a internal frame has been opened.

---

#### Method Summary

Invoked when an internal frame is activated.

Invoked when an internal frame has been closed.

Invoked when an internal frame is in the process of being closed.

Invoked when an internal frame is de-activated.

Invoked when an internal frame is de-iconified.

Invoked when an internal frame is iconified.

Invoked when a internal frame has been opened.

============ METHOD DETAIL ==========

- Method Detail

- internalFrameOpened

```java
void internalFrameOpened​(
InternalFrameEvent
e)
```

Invoked when a internal frame has been opened.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.show()

- internalFrameClosing

```java
void internalFrameClosing​(
InternalFrameEvent
e)
```

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setDefaultCloseOperation(int)

- internalFrameClosed

```java
void internalFrameClosed​(
InternalFrameEvent
e)
```

Invoked when an internal frame has been closed.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setClosed(boolean)

- internalFrameIconified

```java
void internalFrameIconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is iconified.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

- internalFrameDeiconified

```java
void internalFrameDeiconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-iconified.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

- internalFrameActivated

```java
void internalFrameActivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is activated.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

- internalFrameDeactivated

```java
void internalFrameDeactivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-activated.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

Method Detail

- internalFrameOpened

```java
void internalFrameOpened​(
InternalFrameEvent
e)
```

Invoked when a internal frame has been opened.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.show()

- internalFrameClosing

```java
void internalFrameClosing​(
InternalFrameEvent
e)
```

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setDefaultCloseOperation(int)

- internalFrameClosed

```java
void internalFrameClosed​(
InternalFrameEvent
e)
```

Invoked when an internal frame has been closed.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setClosed(boolean)

- internalFrameIconified

```java
void internalFrameIconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is iconified.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

- internalFrameDeiconified

```java
void internalFrameDeiconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-iconified.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

- internalFrameActivated

```java
void internalFrameActivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is activated.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

- internalFrameDeactivated

```java
void internalFrameDeactivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-activated.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

---

#### Method Detail

internalFrameOpened

```java
void internalFrameOpened​(
InternalFrameEvent
e)
```

Invoked when a internal frame has been opened.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.show()

---

#### internalFrameOpened

void internalFrameOpened​(

InternalFrameEvent

e)

Invoked when a internal frame has been opened.

internalFrameClosing

```java
void internalFrameClosing​(
InternalFrameEvent
e)
```

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setDefaultCloseOperation(int)

---

#### internalFrameClosing

void internalFrameClosing​(

InternalFrameEvent

e)

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

internalFrameClosed

```java
void internalFrameClosed​(
InternalFrameEvent
e)
```

Invoked when an internal frame has been closed.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setClosed(boolean)

---

#### internalFrameClosed

void internalFrameClosed​(

InternalFrameEvent

e)

Invoked when an internal frame has been closed.

internalFrameIconified

```java
void internalFrameIconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is iconified.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

---

#### internalFrameIconified

void internalFrameIconified​(

InternalFrameEvent

e)

Invoked when an internal frame is iconified.

internalFrameDeiconified

```java
void internalFrameDeiconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-iconified.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

---

#### internalFrameDeiconified

void internalFrameDeiconified​(

InternalFrameEvent

e)

Invoked when an internal frame is de-iconified.

internalFrameActivated

```java
void internalFrameActivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is activated.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

---

#### internalFrameActivated

void internalFrameActivated​(

InternalFrameEvent

e)

Invoked when an internal frame is activated.

internalFrameDeactivated

```java
void internalFrameDeactivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-activated.

**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

---

#### internalFrameDeactivated

void internalFrameDeactivated​(

InternalFrameEvent

e)

Invoked when an internal frame is de-activated.

---

