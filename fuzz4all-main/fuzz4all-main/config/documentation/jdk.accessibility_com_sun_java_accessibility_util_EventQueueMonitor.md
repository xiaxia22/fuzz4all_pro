# Class EventQueueMonitor

**Source:** `jdk.accessibility\com\sun\java\accessibility\util\EventQueueMonitor.html`

### Class Description

```java
public class
EventQueueMonitor

extends
Object

implements
AWTEventListener
```

The

EventQueueMonitor

class provides key core functionality for Assistive
Technologies (and other system-level technologies that need some of the same
things that Assistive Technology needs).

**All Implemented Interfaces:** AWTEventListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public EventQueueMonitor()

Create a new

EventQueueMonitor

instance. Normally, this will
be called only by the AWT Toolkit during initialization time.
Assistive technologies should not create instances of
EventQueueMonitor by themselves. Instead, they should either
refer to it directly via the static methods in this class, e.g.,

getCurrentMousePosition()

or obtain the instance by asking the
Toolkit, e.g.,

Toolkit.getSystemEventQueue()

.

---

### Method Details

#### public static void maybeInitialize()

Tell the

EventQueueMonitor

to start listening for events.

---

#### public void eventDispatched​(
AWTEvent
theEvent)

Handle events as a result of registering a listener
on the

EventQueue

in

maybeInitialize()

.

**Specified by:**
- eventDispatched

in interface

AWTEventListener

**Parameters:**
- theEvent

- the event to be processed

---

#### public static
Accessible
getAccessibleAt​(
Point
p)

Obtain the

Accessible

object at the given point on the Screen.
The return value may be null if an

Accessible

object cannot be
found at the particular point.

**Parameters:**
- p

- the point to be accessed

**Returns:**
- the

Accessible

at the specified point

---

#### public static boolean isGUIInitialized()

Says whether the GUI subsystem has been initialized or not.
If this returns true, the assistive technology can freely
create GUI component instances. If the return value is false,
the assistive technology should register a

GUIInitializedListener

and wait to create GUI component instances until the listener is
called.

**Returns:**
- true if the GUI subsystem has been initialized

**See Also:**
- addGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

---

#### public static void addGUIInitializedListener​(
GUIInitializedListener
l)

Adds the specified listener to be notified when the GUI subsystem
is initialized. Assistive technologies should get the results of

isGUIInitialized()

before calling this method.

**Parameters:**
- l

- the listener to add

**See Also:**
- isGUIInitialized()

,

removeTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

---

#### public static void removeGUIInitializedListener​(
GUIInitializedListener
l)

Removes the specified listener to be notified when the GUI subsystem
is initialized.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

---

#### public static void addTopLevelWindowListener​(
TopLevelWindowListener
l)

Adds the specified listener to be notified when a top level window
is created or destroyed.

**Parameters:**
- l

- the listener to add

**See Also:**
- removeTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

---

#### public static void removeTopLevelWindowListener​(
TopLevelWindowListener
l)

Removes the specified listener to be notified when a top level window
is created or destroyed.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

---

#### public static
Point
getCurrentMousePosition()

Return the last recorded position of the mouse in screen coordinates.

**Returns:**
- the last recorded position of the mouse in screen coordinates

---

#### public static
Window
[] getTopLevelWindows()

Return the list of top level Windows in use in the Java Virtual Machine.

**Returns:**
- an array of top level

Window

s in use in the Java Virtual Machine

---

#### public static
Window
getTopLevelWindowWithFocus()

Return the top level

Window

that currently has keyboard focus.

**Returns:**
- the top level

Window

that currently has keyboard focus

---

### Additional Sections

#### Class EventQueueMonitor

java.lang.Object

- com.sun.java.accessibility.util.EventQueueMonitor

com.sun.java.accessibility.util.EventQueueMonitor

**All Implemented Interfaces:** AWTEventListener

,

EventListener

```java
public class
EventQueueMonitor

extends
Object

implements
AWTEventListener
```

The

EventQueueMonitor

class provides key core functionality for Assistive
Technologies (and other system-level technologies that need some of the same
things that Assistive Technology needs).

**See Also:** AWTEventMonitor

,

SwingEventMonitor

public class

EventQueueMonitor

extends

Object

implements

AWTEventListener

The

EventQueueMonitor

class provides key core functionality for Assistive
Technologies (and other system-level technologies that need some of the same
things that Assistive Technology needs).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EventQueueMonitor

()

Create a new

EventQueueMonitor

instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static void

addGUIInitializedListener

​(

GUIInitializedListener

l)

Adds the specified listener to be notified when the GUI subsystem
is initialized.

static void

addTopLevelWindowListener

​(

TopLevelWindowListener

l)

Adds the specified listener to be notified when a top level window
is created or destroyed.

void

eventDispatched

​(

AWTEvent

theEvent)

Handle events as a result of registering a listener
on the

EventQueue

in

maybeInitialize()

.

static

Accessible

getAccessibleAt

​(

Point

p)

Obtain the

Accessible

object at the given point on the Screen.

static

Point

getCurrentMousePosition

()

Return the last recorded position of the mouse in screen coordinates.

static

Window

[]

getTopLevelWindows

()

Return the list of top level Windows in use in the Java Virtual Machine.

static

Window

getTopLevelWindowWithFocus

()

Return the top level

Window

that currently has keyboard focus.

static boolean

isGUIInitialized

()

Says whether the GUI subsystem has been initialized or not.

static void

maybeInitialize

()

Tell the

EventQueueMonitor

to start listening for events.

static void

removeGUIInitializedListener

​(

GUIInitializedListener

l)

Removes the specified listener to be notified when the GUI subsystem
is initialized.

static void

removeTopLevelWindowListener

​(

TopLevelWindowListener

l)

Removes the specified listener to be notified when a top level window
is created or destroyed.

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

EventQueueMonitor

()

Create a new

EventQueueMonitor

instance.

---

#### Constructor Summary

Create a new

EventQueueMonitor

instance.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static void

addGUIInitializedListener

​(

GUIInitializedListener

l)

Adds the specified listener to be notified when the GUI subsystem
is initialized.

static void

addTopLevelWindowListener

​(

TopLevelWindowListener

l)

Adds the specified listener to be notified when a top level window
is created or destroyed.

void

eventDispatched

​(

AWTEvent

theEvent)

Handle events as a result of registering a listener
on the

EventQueue

in

maybeInitialize()

.

static

Accessible

getAccessibleAt

​(

Point

p)

Obtain the

Accessible

object at the given point on the Screen.

static

Point

getCurrentMousePosition

()

Return the last recorded position of the mouse in screen coordinates.

static

Window

[]

getTopLevelWindows

()

Return the list of top level Windows in use in the Java Virtual Machine.

static

Window

getTopLevelWindowWithFocus

()

Return the top level

Window

that currently has keyboard focus.

static boolean

isGUIInitialized

()

Says whether the GUI subsystem has been initialized or not.

static void

maybeInitialize

()

Tell the

EventQueueMonitor

to start listening for events.

static void

removeGUIInitializedListener

​(

GUIInitializedListener

l)

Removes the specified listener to be notified when the GUI subsystem
is initialized.

static void

removeTopLevelWindowListener

​(

TopLevelWindowListener

l)

Removes the specified listener to be notified when a top level window
is created or destroyed.

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

Adds the specified listener to be notified when the GUI subsystem
is initialized.

Adds the specified listener to be notified when a top level window
is created or destroyed.

Handle events as a result of registering a listener
on the

EventQueue

in

maybeInitialize()

.

Obtain the

Accessible

object at the given point on the Screen.

Return the last recorded position of the mouse in screen coordinates.

Return the list of top level Windows in use in the Java Virtual Machine.

Return the top level

Window

that currently has keyboard focus.

Says whether the GUI subsystem has been initialized or not.

Tell the

EventQueueMonitor

to start listening for events.

Removes the specified listener to be notified when the GUI subsystem
is initialized.

Removes the specified listener to be notified when a top level window
is created or destroyed.

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

- EventQueueMonitor

```java
public EventQueueMonitor()
```

Create a new

EventQueueMonitor

instance. Normally, this will
be called only by the AWT Toolkit during initialization time.
Assistive technologies should not create instances of
EventQueueMonitor by themselves. Instead, they should either
refer to it directly via the static methods in this class, e.g.,

getCurrentMousePosition()

or obtain the instance by asking the
Toolkit, e.g.,

Toolkit.getSystemEventQueue()

.

============ METHOD DETAIL ==========

- Method Detail

- maybeInitialize

```java
public static void maybeInitialize()
```

Tell the

EventQueueMonitor

to start listening for events.

- eventDispatched

```java
public void eventDispatched​(
AWTEvent
theEvent)
```

Handle events as a result of registering a listener
on the

EventQueue

in

maybeInitialize()

.

**Specified by:** eventDispatched

in interface

AWTEventListener
**Parameters:** theEvent

- the event to be processed

- getAccessibleAt

```java
public static
Accessible
getAccessibleAt​(
Point
p)
```

Obtain the

Accessible

object at the given point on the Screen.
The return value may be null if an

Accessible

object cannot be
found at the particular point.

**Parameters:** p

- the point to be accessed
**Returns:** the

Accessible

at the specified point

- isGUIInitialized

```java
public static boolean isGUIInitialized()
```

Says whether the GUI subsystem has been initialized or not.
If this returns true, the assistive technology can freely
create GUI component instances. If the return value is false,
the assistive technology should register a

GUIInitializedListener

and wait to create GUI component instances until the listener is
called.

**Returns:** true if the GUI subsystem has been initialized
**See Also:** addGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

- addGUIInitializedListener

```java
public static void addGUIInitializedListener​(
GUIInitializedListener
l)
```

Adds the specified listener to be notified when the GUI subsystem
is initialized. Assistive technologies should get the results of

isGUIInitialized()

before calling this method.

**Parameters:** l

- the listener to add
**See Also:** isGUIInitialized()

,

removeTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

- removeGUIInitializedListener

```java
public static void removeGUIInitializedListener​(
GUIInitializedListener
l)
```

Removes the specified listener to be notified when the GUI subsystem
is initialized.

**Parameters:** l

- the listener to remove
**See Also:** addGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

- addTopLevelWindowListener

```java
public static void addTopLevelWindowListener​(
TopLevelWindowListener
l)
```

Adds the specified listener to be notified when a top level window
is created or destroyed.

**Parameters:** l

- the listener to add
**See Also:** removeTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

- removeTopLevelWindowListener

```java
public static void removeTopLevelWindowListener​(
TopLevelWindowListener
l)
```

Removes the specified listener to be notified when a top level window
is created or destroyed.

**Parameters:** l

- the listener to remove
**See Also:** addTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

- getCurrentMousePosition

```java
public static
Point
getCurrentMousePosition()
```

Return the last recorded position of the mouse in screen coordinates.

**Returns:** the last recorded position of the mouse in screen coordinates

- getTopLevelWindows

```java
public static
Window
[] getTopLevelWindows()
```

Return the list of top level Windows in use in the Java Virtual Machine.

**Returns:** an array of top level

Window

s in use in the Java Virtual Machine

- getTopLevelWindowWithFocus

```java
public static
Window
getTopLevelWindowWithFocus()
```

Return the top level

Window

that currently has keyboard focus.

**Returns:** the top level

Window

that currently has keyboard focus

Constructor Detail

- EventQueueMonitor

```java
public EventQueueMonitor()
```

Create a new

EventQueueMonitor

instance. Normally, this will
be called only by the AWT Toolkit during initialization time.
Assistive technologies should not create instances of
EventQueueMonitor by themselves. Instead, they should either
refer to it directly via the static methods in this class, e.g.,

getCurrentMousePosition()

or obtain the instance by asking the
Toolkit, e.g.,

Toolkit.getSystemEventQueue()

.

---

#### Constructor Detail

EventQueueMonitor

```java
public EventQueueMonitor()
```

Create a new

EventQueueMonitor

instance. Normally, this will
be called only by the AWT Toolkit during initialization time.
Assistive technologies should not create instances of
EventQueueMonitor by themselves. Instead, they should either
refer to it directly via the static methods in this class, e.g.,

getCurrentMousePosition()

or obtain the instance by asking the
Toolkit, e.g.,

Toolkit.getSystemEventQueue()

.

---

#### EventQueueMonitor

public EventQueueMonitor()

Create a new

EventQueueMonitor

instance. Normally, this will
be called only by the AWT Toolkit during initialization time.
Assistive technologies should not create instances of
EventQueueMonitor by themselves. Instead, they should either
refer to it directly via the static methods in this class, e.g.,

getCurrentMousePosition()

or obtain the instance by asking the
Toolkit, e.g.,

Toolkit.getSystemEventQueue()

.

Method Detail

- maybeInitialize

```java
public static void maybeInitialize()
```

Tell the

EventQueueMonitor

to start listening for events.

- eventDispatched

```java
public void eventDispatched​(
AWTEvent
theEvent)
```

Handle events as a result of registering a listener
on the

EventQueue

in

maybeInitialize()

.

**Specified by:** eventDispatched

in interface

AWTEventListener
**Parameters:** theEvent

- the event to be processed

- getAccessibleAt

```java
public static
Accessible
getAccessibleAt​(
Point
p)
```

Obtain the

Accessible

object at the given point on the Screen.
The return value may be null if an

Accessible

object cannot be
found at the particular point.

**Parameters:** p

- the point to be accessed
**Returns:** the

Accessible

at the specified point

- isGUIInitialized

```java
public static boolean isGUIInitialized()
```

Says whether the GUI subsystem has been initialized or not.
If this returns true, the assistive technology can freely
create GUI component instances. If the return value is false,
the assistive technology should register a

GUIInitializedListener

and wait to create GUI component instances until the listener is
called.

**Returns:** true if the GUI subsystem has been initialized
**See Also:** addGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

- addGUIInitializedListener

```java
public static void addGUIInitializedListener​(
GUIInitializedListener
l)
```

Adds the specified listener to be notified when the GUI subsystem
is initialized. Assistive technologies should get the results of

isGUIInitialized()

before calling this method.

**Parameters:** l

- the listener to add
**See Also:** isGUIInitialized()

,

removeTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

- removeGUIInitializedListener

```java
public static void removeGUIInitializedListener​(
GUIInitializedListener
l)
```

Removes the specified listener to be notified when the GUI subsystem
is initialized.

**Parameters:** l

- the listener to remove
**See Also:** addGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

- addTopLevelWindowListener

```java
public static void addTopLevelWindowListener​(
TopLevelWindowListener
l)
```

Adds the specified listener to be notified when a top level window
is created or destroyed.

**Parameters:** l

- the listener to add
**See Also:** removeTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

- removeTopLevelWindowListener

```java
public static void removeTopLevelWindowListener​(
TopLevelWindowListener
l)
```

Removes the specified listener to be notified when a top level window
is created or destroyed.

**Parameters:** l

- the listener to remove
**See Also:** addTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

- getCurrentMousePosition

```java
public static
Point
getCurrentMousePosition()
```

Return the last recorded position of the mouse in screen coordinates.

**Returns:** the last recorded position of the mouse in screen coordinates

- getTopLevelWindows

```java
public static
Window
[] getTopLevelWindows()
```

Return the list of top level Windows in use in the Java Virtual Machine.

**Returns:** an array of top level

Window

s in use in the Java Virtual Machine

- getTopLevelWindowWithFocus

```java
public static
Window
getTopLevelWindowWithFocus()
```

Return the top level

Window

that currently has keyboard focus.

**Returns:** the top level

Window

that currently has keyboard focus

---

#### Method Detail

maybeInitialize

```java
public static void maybeInitialize()
```

Tell the

EventQueueMonitor

to start listening for events.

---

#### maybeInitialize

public static void maybeInitialize()

Tell the

EventQueueMonitor

to start listening for events.

eventDispatched

```java
public void eventDispatched​(
AWTEvent
theEvent)
```

Handle events as a result of registering a listener
on the

EventQueue

in

maybeInitialize()

.

**Specified by:** eventDispatched

in interface

AWTEventListener
**Parameters:** theEvent

- the event to be processed

---

#### eventDispatched

public void eventDispatched​(

AWTEvent

theEvent)

Handle events as a result of registering a listener
on the

EventQueue

in

maybeInitialize()

.

getAccessibleAt

```java
public static
Accessible
getAccessibleAt​(
Point
p)
```

Obtain the

Accessible

object at the given point on the Screen.
The return value may be null if an

Accessible

object cannot be
found at the particular point.

**Parameters:** p

- the point to be accessed
**Returns:** the

Accessible

at the specified point

---

#### getAccessibleAt

public static

Accessible

getAccessibleAt​(

Point

p)

Obtain the

Accessible

object at the given point on the Screen.
The return value may be null if an

Accessible

object cannot be
found at the particular point.

isGUIInitialized

```java
public static boolean isGUIInitialized()
```

Says whether the GUI subsystem has been initialized or not.
If this returns true, the assistive technology can freely
create GUI component instances. If the return value is false,
the assistive technology should register a

GUIInitializedListener

and wait to create GUI component instances until the listener is
called.

**Returns:** true if the GUI subsystem has been initialized
**See Also:** addGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

---

#### isGUIInitialized

public static boolean isGUIInitialized()

Says whether the GUI subsystem has been initialized or not.
If this returns true, the assistive technology can freely
create GUI component instances. If the return value is false,
the assistive technology should register a

GUIInitializedListener

and wait to create GUI component instances until the listener is
called.

addGUIInitializedListener

```java
public static void addGUIInitializedListener​(
GUIInitializedListener
l)
```

Adds the specified listener to be notified when the GUI subsystem
is initialized. Assistive technologies should get the results of

isGUIInitialized()

before calling this method.

**Parameters:** l

- the listener to add
**See Also:** isGUIInitialized()

,

removeTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

---

#### addGUIInitializedListener

public static void addGUIInitializedListener​(

GUIInitializedListener

l)

Adds the specified listener to be notified when the GUI subsystem
is initialized. Assistive technologies should get the results of

isGUIInitialized()

before calling this method.

removeGUIInitializedListener

```java
public static void removeGUIInitializedListener​(
GUIInitializedListener
l)
```

Removes the specified listener to be notified when the GUI subsystem
is initialized.

**Parameters:** l

- the listener to remove
**See Also:** addGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

---

#### removeGUIInitializedListener

public static void removeGUIInitializedListener​(

GUIInitializedListener

l)

Removes the specified listener to be notified when the GUI subsystem
is initialized.

addTopLevelWindowListener

```java
public static void addTopLevelWindowListener​(
TopLevelWindowListener
l)
```

Adds the specified listener to be notified when a top level window
is created or destroyed.

**Parameters:** l

- the listener to add
**See Also:** removeTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

---

#### addTopLevelWindowListener

public static void addTopLevelWindowListener​(

TopLevelWindowListener

l)

Adds the specified listener to be notified when a top level window
is created or destroyed.

removeTopLevelWindowListener

```java
public static void removeTopLevelWindowListener​(
TopLevelWindowListener
l)
```

Removes the specified listener to be notified when a top level window
is created or destroyed.

**Parameters:** l

- the listener to remove
**See Also:** addTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

---

#### removeTopLevelWindowListener

public static void removeTopLevelWindowListener​(

TopLevelWindowListener

l)

Removes the specified listener to be notified when a top level window
is created or destroyed.

getCurrentMousePosition

```java
public static
Point
getCurrentMousePosition()
```

Return the last recorded position of the mouse in screen coordinates.

**Returns:** the last recorded position of the mouse in screen coordinates

---

#### getCurrentMousePosition

public static

Point

getCurrentMousePosition()

Return the last recorded position of the mouse in screen coordinates.

getTopLevelWindows

```java
public static
Window
[] getTopLevelWindows()
```

Return the list of top level Windows in use in the Java Virtual Machine.

**Returns:** an array of top level

Window

s in use in the Java Virtual Machine

---

#### getTopLevelWindows

public static

Window

[] getTopLevelWindows()

Return the list of top level Windows in use in the Java Virtual Machine.

getTopLevelWindowWithFocus

```java
public static
Window
getTopLevelWindowWithFocus()
```

Return the top level

Window

that currently has keyboard focus.

**Returns:** the top level

Window

that currently has keyboard focus

---

#### getTopLevelWindowWithFocus

public static

Window

getTopLevelWindowWithFocus()

Return the top level

Window

that currently has keyboard focus.

---

