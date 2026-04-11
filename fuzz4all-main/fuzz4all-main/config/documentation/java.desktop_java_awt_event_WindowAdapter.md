# Class WindowAdapter

**Source:** `java.desktop\java\awt\event\WindowAdapter.html`

### Class Description

```java
public abstract class
WindowAdapter

extends
Object

implements
WindowListener
,
WindowStateListener
,
WindowFocusListener
```

An abstract adapter class for receiving window events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

WindowEvent

listener
and override the methods for the events of interest. (If you implement the

WindowListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a Window using the window's

addWindowListener

method. When the window's status changes by virtue of being opened,
closed, activated or deactivated, iconified or deiconified,
the relevant method in the listener
object is invoked, and the

WindowEvent

is passed to it.

**All Implemented Interfaces:** WindowFocusListener

,

WindowListener

,

WindowStateListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public WindowAdapter()

*No description found.*

---

### Method Details

#### public void windowOpened​(
WindowEvent
e)

Invoked when a window has been opened.

**Specified by:**
- windowOpened

in interface

WindowListener

**Parameters:**
- e

- the event to be processed

---

#### public void windowClosing​(
WindowEvent
e)

Invoked when a window is in the process of being closed.
The close operation can be overridden at this point.

**Specified by:**
- windowClosing

in interface

WindowListener

**Parameters:**
- e

- the event to be processed

---

#### public void windowClosed​(
WindowEvent
e)

Invoked when a window has been closed.

**Specified by:**
- windowClosed

in interface

WindowListener

**Parameters:**
- e

- the event to be processed

---

#### public void windowIconified​(
WindowEvent
e)

Invoked when a window is iconified.

**Specified by:**
- windowIconified

in interface

WindowListener

**Parameters:**
- e

- the event to be processed

**See Also:**
- Window.setIconImage(java.awt.Image)

---

#### public void windowDeiconified​(
WindowEvent
e)

Invoked when a window is de-iconified.

**Specified by:**
- windowDeiconified

in interface

WindowListener

**Parameters:**
- e

- the event to be processed

---

#### public void windowActivated​(
WindowEvent
e)

Invoked when a window is activated.

**Specified by:**
- windowActivated

in interface

WindowListener

**Parameters:**
- e

- the event to be processed

---

#### public void windowDeactivated​(
WindowEvent
e)

Invoked when a window is de-activated.

**Specified by:**
- windowDeactivated

in interface

WindowListener

**Parameters:**
- e

- the event to be processed

---

#### public void windowStateChanged​(
WindowEvent
e)

Invoked when a window state is changed.

**Specified by:**
- windowStateChanged

in interface

WindowStateListener

**Parameters:**
- e

- the event to be processed

**Since:**
- 1.4

---

#### public void windowGainedFocus​(
WindowEvent
e)

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

**Specified by:**
- windowGainedFocus

in interface

WindowFocusListener

**Parameters:**
- e

- the event to be processed

**Since:**
- 1.4

---

#### public void windowLostFocus​(
WindowEvent
e)

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

**Specified by:**
- windowLostFocus

in interface

WindowFocusListener

**Parameters:**
- e

- the event to be processed

**Since:**
- 1.4

---

### Additional Sections

#### Class WindowAdapter

java.lang.Object

- java.awt.event.WindowAdapter

java.awt.event.WindowAdapter

**All Implemented Interfaces:** WindowFocusListener

,

WindowListener

,

WindowStateListener

,

EventListener

**Direct Known Subclasses:** BasicToolBarUI.FrameListener

,

JMenu.WinListener

```java
public abstract class
WindowAdapter

extends
Object

implements
WindowListener
,
WindowStateListener
,
WindowFocusListener
```

An abstract adapter class for receiving window events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

WindowEvent

listener
and override the methods for the events of interest. (If you implement the

WindowListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a Window using the window's

addWindowListener

method. When the window's status changes by virtue of being opened,
closed, activated or deactivated, iconified or deiconified,
the relevant method in the listener
object is invoked, and the

WindowEvent

is passed to it.

**Since:** 1.1
**See Also:** WindowEvent

,

WindowListener

,

Tutorial: Writing a Window Listener

public abstract class

WindowAdapter

extends

Object

implements

WindowListener

,

WindowStateListener

,

WindowFocusListener

An abstract adapter class for receiving window events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

WindowEvent

listener
and override the methods for the events of interest. (If you implement the

WindowListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a Window using the window's

addWindowListener

method. When the window's status changes by virtue of being opened,
closed, activated or deactivated, iconified or deiconified,
the relevant method in the listener
object is invoked, and the

WindowEvent

is passed to it.

Extend this class to create a

WindowEvent

listener
and override the methods for the events of interest. (If you implement the

WindowListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a Window using the window's

addWindowListener

method. When the window's status changes by virtue of being opened,
closed, activated or deactivated, iconified or deiconified,
the relevant method in the listener
object is invoked, and the

WindowEvent

is passed to it.

Create a listener object using the extended class and then register it with
a Window using the window's

addWindowListener

method. When the window's status changes by virtue of being opened,
closed, activated or deactivated, iconified or deiconified,
the relevant method in the listener
object is invoked, and the

WindowEvent

is passed to it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

WindowAdapter

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

windowActivated

​(

WindowEvent

e)

Invoked when a window is activated.

void

windowClosed

​(

WindowEvent

e)

Invoked when a window has been closed.

void

windowClosing

​(

WindowEvent

e)

Invoked when a window is in the process of being closed.

void

windowDeactivated

​(

WindowEvent

e)

Invoked when a window is de-activated.

void

windowDeiconified

​(

WindowEvent

e)

Invoked when a window is de-iconified.

void

windowGainedFocus

​(

WindowEvent

e)

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

void

windowIconified

​(

WindowEvent

e)

Invoked when a window is iconified.

void

windowLostFocus

​(

WindowEvent

e)

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

void

windowOpened

​(

WindowEvent

e)

Invoked when a window has been opened.

void

windowStateChanged

​(

WindowEvent

e)

Invoked when a window state is changed.

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

WindowAdapter

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

windowActivated

​(

WindowEvent

e)

Invoked when a window is activated.

void

windowClosed

​(

WindowEvent

e)

Invoked when a window has been closed.

void

windowClosing

​(

WindowEvent

e)

Invoked when a window is in the process of being closed.

void

windowDeactivated

​(

WindowEvent

e)

Invoked when a window is de-activated.

void

windowDeiconified

​(

WindowEvent

e)

Invoked when a window is de-iconified.

void

windowGainedFocus

​(

WindowEvent

e)

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

void

windowIconified

​(

WindowEvent

e)

Invoked when a window is iconified.

void

windowLostFocus

​(

WindowEvent

e)

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

void

windowOpened

​(

WindowEvent

e)

Invoked when a window has been opened.

void

windowStateChanged

​(

WindowEvent

e)

Invoked when a window state is changed.

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

Invoked when a window is activated.

Invoked when a window has been closed.

Invoked when a window is in the process of being closed.

Invoked when a window is de-activated.

Invoked when a window is de-iconified.

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

Invoked when a window is iconified.

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

Invoked when a window has been opened.

Invoked when a window state is changed.

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

- WindowAdapter

```java
public WindowAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- windowOpened

```java
public void windowOpened​(
WindowEvent
e)
```

Invoked when a window has been opened.

**Specified by:** windowOpened

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowClosing

```java
public void windowClosing​(
WindowEvent
e)
```

Invoked when a window is in the process of being closed.
The close operation can be overridden at this point.

**Specified by:** windowClosing

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowClosed

```java
public void windowClosed​(
WindowEvent
e)
```

Invoked when a window has been closed.

**Specified by:** windowClosed

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowIconified

```java
public void windowIconified​(
WindowEvent
e)
```

Invoked when a window is iconified.

**Specified by:** windowIconified

in interface

WindowListener
**Parameters:** e

- the event to be processed
**See Also:** Window.setIconImage(java.awt.Image)

- windowDeiconified

```java
public void windowDeiconified​(
WindowEvent
e)
```

Invoked when a window is de-iconified.

**Specified by:** windowDeiconified

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowActivated

```java
public void windowActivated​(
WindowEvent
e)
```

Invoked when a window is activated.

**Specified by:** windowActivated

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowDeactivated

```java
public void windowDeactivated​(
WindowEvent
e)
```

Invoked when a window is de-activated.

**Specified by:** windowDeactivated

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowStateChanged

```java
public void windowStateChanged​(
WindowEvent
e)
```

Invoked when a window state is changed.

**Specified by:** windowStateChanged

in interface

WindowStateListener
**Parameters:** e

- the event to be processed
**Since:** 1.4

- windowGainedFocus

```java
public void windowGainedFocus​(
WindowEvent
e)
```

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

**Specified by:** windowGainedFocus

in interface

WindowFocusListener
**Parameters:** e

- the event to be processed
**Since:** 1.4

- windowLostFocus

```java
public void windowLostFocus​(
WindowEvent
e)
```

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

**Specified by:** windowLostFocus

in interface

WindowFocusListener
**Parameters:** e

- the event to be processed
**Since:** 1.4

Constructor Detail

- WindowAdapter

```java
public WindowAdapter()
```

---

#### Constructor Detail

WindowAdapter

```java
public WindowAdapter()
```

---

#### WindowAdapter

public WindowAdapter()

Method Detail

- windowOpened

```java
public void windowOpened​(
WindowEvent
e)
```

Invoked when a window has been opened.

**Specified by:** windowOpened

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowClosing

```java
public void windowClosing​(
WindowEvent
e)
```

Invoked when a window is in the process of being closed.
The close operation can be overridden at this point.

**Specified by:** windowClosing

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowClosed

```java
public void windowClosed​(
WindowEvent
e)
```

Invoked when a window has been closed.

**Specified by:** windowClosed

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowIconified

```java
public void windowIconified​(
WindowEvent
e)
```

Invoked when a window is iconified.

**Specified by:** windowIconified

in interface

WindowListener
**Parameters:** e

- the event to be processed
**See Also:** Window.setIconImage(java.awt.Image)

- windowDeiconified

```java
public void windowDeiconified​(
WindowEvent
e)
```

Invoked when a window is de-iconified.

**Specified by:** windowDeiconified

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowActivated

```java
public void windowActivated​(
WindowEvent
e)
```

Invoked when a window is activated.

**Specified by:** windowActivated

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowDeactivated

```java
public void windowDeactivated​(
WindowEvent
e)
```

Invoked when a window is de-activated.

**Specified by:** windowDeactivated

in interface

WindowListener
**Parameters:** e

- the event to be processed

- windowStateChanged

```java
public void windowStateChanged​(
WindowEvent
e)
```

Invoked when a window state is changed.

**Specified by:** windowStateChanged

in interface

WindowStateListener
**Parameters:** e

- the event to be processed
**Since:** 1.4

- windowGainedFocus

```java
public void windowGainedFocus​(
WindowEvent
e)
```

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

**Specified by:** windowGainedFocus

in interface

WindowFocusListener
**Parameters:** e

- the event to be processed
**Since:** 1.4

- windowLostFocus

```java
public void windowLostFocus​(
WindowEvent
e)
```

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

**Specified by:** windowLostFocus

in interface

WindowFocusListener
**Parameters:** e

- the event to be processed
**Since:** 1.4

---

#### Method Detail

windowOpened

```java
public void windowOpened​(
WindowEvent
e)
```

Invoked when a window has been opened.

**Specified by:** windowOpened

in interface

WindowListener
**Parameters:** e

- the event to be processed

---

#### windowOpened

public void windowOpened​(

WindowEvent

e)

Invoked when a window has been opened.

windowClosing

```java
public void windowClosing​(
WindowEvent
e)
```

Invoked when a window is in the process of being closed.
The close operation can be overridden at this point.

**Specified by:** windowClosing

in interface

WindowListener
**Parameters:** e

- the event to be processed

---

#### windowClosing

public void windowClosing​(

WindowEvent

e)

Invoked when a window is in the process of being closed.
The close operation can be overridden at this point.

windowClosed

```java
public void windowClosed​(
WindowEvent
e)
```

Invoked when a window has been closed.

**Specified by:** windowClosed

in interface

WindowListener
**Parameters:** e

- the event to be processed

---

#### windowClosed

public void windowClosed​(

WindowEvent

e)

Invoked when a window has been closed.

windowIconified

```java
public void windowIconified​(
WindowEvent
e)
```

Invoked when a window is iconified.

**Specified by:** windowIconified

in interface

WindowListener
**Parameters:** e

- the event to be processed
**See Also:** Window.setIconImage(java.awt.Image)

---

#### windowIconified

public void windowIconified​(

WindowEvent

e)

Invoked when a window is iconified.

windowDeiconified

```java
public void windowDeiconified​(
WindowEvent
e)
```

Invoked when a window is de-iconified.

**Specified by:** windowDeiconified

in interface

WindowListener
**Parameters:** e

- the event to be processed

---

#### windowDeiconified

public void windowDeiconified​(

WindowEvent

e)

Invoked when a window is de-iconified.

windowActivated

```java
public void windowActivated​(
WindowEvent
e)
```

Invoked when a window is activated.

**Specified by:** windowActivated

in interface

WindowListener
**Parameters:** e

- the event to be processed

---

#### windowActivated

public void windowActivated​(

WindowEvent

e)

Invoked when a window is activated.

windowDeactivated

```java
public void windowDeactivated​(
WindowEvent
e)
```

Invoked when a window is de-activated.

**Specified by:** windowDeactivated

in interface

WindowListener
**Parameters:** e

- the event to be processed

---

#### windowDeactivated

public void windowDeactivated​(

WindowEvent

e)

Invoked when a window is de-activated.

windowStateChanged

```java
public void windowStateChanged​(
WindowEvent
e)
```

Invoked when a window state is changed.

**Specified by:** windowStateChanged

in interface

WindowStateListener
**Parameters:** e

- the event to be processed
**Since:** 1.4

---

#### windowStateChanged

public void windowStateChanged​(

WindowEvent

e)

Invoked when a window state is changed.

windowGainedFocus

```java
public void windowGainedFocus​(
WindowEvent
e)
```

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

**Specified by:** windowGainedFocus

in interface

WindowFocusListener
**Parameters:** e

- the event to be processed
**Since:** 1.4

---

#### windowGainedFocus

public void windowGainedFocus​(

WindowEvent

e)

Invoked when the Window is set to be the focused Window, which means
that the Window, or one of its subcomponents, will receive keyboard
events.

windowLostFocus

```java
public void windowLostFocus​(
WindowEvent
e)
```

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

**Specified by:** windowLostFocus

in interface

WindowFocusListener
**Parameters:** e

- the event to be processed
**Since:** 1.4

---

#### windowLostFocus

public void windowLostFocus​(

WindowEvent

e)

Invoked when the Window is no longer the focused Window, which means
that keyboard events will no longer be delivered to the Window or any of
its subcomponents.

---

