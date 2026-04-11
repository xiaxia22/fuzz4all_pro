# Class InternalFrameAdapter

**Source:** `java.desktop\javax\swing\event\InternalFrameAdapter.html`

### Class Description

```java
public abstract class
InternalFrameAdapter

extends
Object

implements
InternalFrameListener
```

An abstract adapter class for receiving internal frame events.
The methods in this class are empty. This class exists as
convenience for creating listener objects, and is functionally
equivalent to the WindowAdapter class in the AWT.

See

How to Write an Internal Frame Listener

in

The Java Tutorial

**All Implemented Interfaces:** EventListener

,

InternalFrameListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public InternalFrameAdapter()

*No description found.*

---

### Method Details

#### public void internalFrameOpened​(
InternalFrameEvent
e)

Invoked when an internal frame has been opened.

**Specified by:**
- internalFrameOpened

in interface

InternalFrameListener

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

#### public void internalFrameClosing​(
InternalFrameEvent
e)

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

**Specified by:**
- internalFrameClosing

in interface

InternalFrameListener

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

#### public void internalFrameClosed​(
InternalFrameEvent
e)

Invoked when an internal frame has been closed.

**Specified by:**
- internalFrameClosed

in interface

InternalFrameListener

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

#### public void internalFrameIconified​(
InternalFrameEvent
e)

Invoked when an internal frame is iconified.

**Specified by:**
- internalFrameIconified

in interface

InternalFrameListener

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

#### public void internalFrameDeiconified​(
InternalFrameEvent
e)

Invoked when an internal frame is de-iconified.

**Specified by:**
- internalFrameDeiconified

in interface

InternalFrameListener

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

#### public void internalFrameActivated​(
InternalFrameEvent
e)

Invoked when an internal frame is activated.

**Specified by:**
- internalFrameActivated

in interface

InternalFrameListener

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

#### public void internalFrameDeactivated​(
InternalFrameEvent
e)

Invoked when an internal frame is de-activated.

**Specified by:**
- internalFrameDeactivated

in interface

InternalFrameListener

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

#### Class InternalFrameAdapter

java.lang.Object

- javax.swing.event.InternalFrameAdapter

javax.swing.event.InternalFrameAdapter

**All Implemented Interfaces:** EventListener

,

InternalFrameListener

```java
public abstract class
InternalFrameAdapter

extends
Object

implements
InternalFrameListener
```

An abstract adapter class for receiving internal frame events.
The methods in this class are empty. This class exists as
convenience for creating listener objects, and is functionally
equivalent to the WindowAdapter class in the AWT.

See

How to Write an Internal Frame Listener

in

The Java Tutorial

**See Also:** InternalFrameEvent

,

InternalFrameListener

,

WindowListener

public abstract class

InternalFrameAdapter

extends

Object

implements

InternalFrameListener

An abstract adapter class for receiving internal frame events.
The methods in this class are empty. This class exists as
convenience for creating listener objects, and is functionally
equivalent to the WindowAdapter class in the AWT.

See

How to Write an Internal Frame Listener

in

The Java Tutorial

See

How to Write an Internal Frame Listener

in

The Java Tutorial

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InternalFrameAdapter

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

Invoked when an internal frame has been opened.

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

InternalFrameAdapter

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

Invoked when an internal frame has been opened.

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

Invoked when an internal frame is activated.

Invoked when an internal frame has been closed.

Invoked when an internal frame is in the process of being closed.

Invoked when an internal frame is de-activated.

Invoked when an internal frame is de-iconified.

Invoked when an internal frame is iconified.

Invoked when an internal frame has been opened.

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

- InternalFrameAdapter

```java
public InternalFrameAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- internalFrameOpened

```java
public void internalFrameOpened​(
InternalFrameEvent
e)
```

Invoked when an internal frame has been opened.

**Specified by:** internalFrameOpened

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.show()

- internalFrameClosing

```java
public void internalFrameClosing​(
InternalFrameEvent
e)
```

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

**Specified by:** internalFrameClosing

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setDefaultCloseOperation(int)

- internalFrameClosed

```java
public void internalFrameClosed​(
InternalFrameEvent
e)
```

Invoked when an internal frame has been closed.

**Specified by:** internalFrameClosed

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setClosed(boolean)

- internalFrameIconified

```java
public void internalFrameIconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is iconified.

**Specified by:** internalFrameIconified

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

- internalFrameDeiconified

```java
public void internalFrameDeiconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-iconified.

**Specified by:** internalFrameDeiconified

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

- internalFrameActivated

```java
public void internalFrameActivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is activated.

**Specified by:** internalFrameActivated

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

- internalFrameDeactivated

```java
public void internalFrameDeactivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-activated.

**Specified by:** internalFrameDeactivated

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

Constructor Detail

- InternalFrameAdapter

```java
public InternalFrameAdapter()
```

---

#### Constructor Detail

InternalFrameAdapter

```java
public InternalFrameAdapter()
```

---

#### InternalFrameAdapter

public InternalFrameAdapter()

Method Detail

- internalFrameOpened

```java
public void internalFrameOpened​(
InternalFrameEvent
e)
```

Invoked when an internal frame has been opened.

**Specified by:** internalFrameOpened

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.show()

- internalFrameClosing

```java
public void internalFrameClosing​(
InternalFrameEvent
e)
```

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

**Specified by:** internalFrameClosing

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setDefaultCloseOperation(int)

- internalFrameClosed

```java
public void internalFrameClosed​(
InternalFrameEvent
e)
```

Invoked when an internal frame has been closed.

**Specified by:** internalFrameClosed

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setClosed(boolean)

- internalFrameIconified

```java
public void internalFrameIconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is iconified.

**Specified by:** internalFrameIconified

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

- internalFrameDeiconified

```java
public void internalFrameDeiconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-iconified.

**Specified by:** internalFrameDeiconified

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

- internalFrameActivated

```java
public void internalFrameActivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is activated.

**Specified by:** internalFrameActivated

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

- internalFrameDeactivated

```java
public void internalFrameDeactivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-activated.

**Specified by:** internalFrameDeactivated

in interface

InternalFrameListener
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
public void internalFrameOpened​(
InternalFrameEvent
e)
```

Invoked when an internal frame has been opened.

**Specified by:** internalFrameOpened

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.show()

---

#### internalFrameOpened

public void internalFrameOpened​(

InternalFrameEvent

e)

Invoked when an internal frame has been opened.

internalFrameClosing

```java
public void internalFrameClosing​(
InternalFrameEvent
e)
```

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

**Specified by:** internalFrameClosing

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setDefaultCloseOperation(int)

---

#### internalFrameClosing

public void internalFrameClosing​(

InternalFrameEvent

e)

Invoked when an internal frame is in the process of being closed.
The close operation can be overridden at this point.

internalFrameClosed

```java
public void internalFrameClosed​(
InternalFrameEvent
e)
```

Invoked when an internal frame has been closed.

**Specified by:** internalFrameClosed

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setClosed(boolean)

---

#### internalFrameClosed

public void internalFrameClosed​(

InternalFrameEvent

e)

Invoked when an internal frame has been closed.

internalFrameIconified

```java
public void internalFrameIconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is iconified.

**Specified by:** internalFrameIconified

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

---

#### internalFrameIconified

public void internalFrameIconified​(

InternalFrameEvent

e)

Invoked when an internal frame is iconified.

internalFrameDeiconified

```java
public void internalFrameDeiconified​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-iconified.

**Specified by:** internalFrameDeiconified

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setIcon(boolean)

---

#### internalFrameDeiconified

public void internalFrameDeiconified​(

InternalFrameEvent

e)

Invoked when an internal frame is de-iconified.

internalFrameActivated

```java
public void internalFrameActivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is activated.

**Specified by:** internalFrameActivated

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

---

#### internalFrameActivated

public void internalFrameActivated​(

InternalFrameEvent

e)

Invoked when an internal frame is activated.

internalFrameDeactivated

```java
public void internalFrameDeactivated​(
InternalFrameEvent
e)
```

Invoked when an internal frame is de-activated.

**Specified by:** internalFrameDeactivated

in interface

InternalFrameListener
**Parameters:** e

- an

InternalFrameEvent

with information about the

JInteralFrame

that originated the event
**See Also:** JInternalFrame.setSelected(boolean)

---

#### internalFrameDeactivated

public void internalFrameDeactivated​(

InternalFrameEvent

e)

Invoked when an internal frame is de-activated.

---

