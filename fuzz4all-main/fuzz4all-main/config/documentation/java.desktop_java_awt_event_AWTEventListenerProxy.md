# Class AWTEventListenerProxy

**Source:** `java.desktop\java\awt\event\AWTEventListenerProxy.html`

### Class Description

```java
public class
AWTEventListenerProxy

extends
EventListenerProxy
<
AWTEventListener
>
implements
AWTEventListener
```

A class which extends the

EventListenerProxy

specifically for adding an

AWTEventListener

for a specific event mask.
Instances of this class can be added as

AWTEventListener

s
to a

Toolkit

object.

The

getAWTEventListeners

method of

Toolkit

can return a mixture of

AWTEventListener

and

AWTEventListenerProxy

objects.

**All Implemented Interfaces:** AWTEventListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public AWTEventListenerProxy​(long eventMask,

AWTEventListener
listener)

Constructor which binds the

AWTEventListener

to a specific event mask.

**Parameters:**
- eventMask

- the bitmap of event types to receive
- listener

- the listener object

---

### Method Details

#### public void eventDispatched​(
AWTEvent
event)

Forwards the AWT event to the listener delegate.

**Specified by:**
- eventDispatched

in interface

AWTEventListener

**Parameters:**
- event

- the AWT event

---

#### public long getEventMask()

Returns the event mask associated with the listener.

**Returns:**
- the event mask associated with the listener

---

### Additional Sections

#### Class AWTEventListenerProxy

java.lang.Object

- java.util.EventListenerProxy

<

AWTEventListener

>
- - java.awt.event.AWTEventListenerProxy

java.util.EventListenerProxy

<

AWTEventListener

>

- java.awt.event.AWTEventListenerProxy

java.awt.event.AWTEventListenerProxy

**All Implemented Interfaces:** AWTEventListener

,

EventListener

```java
public class
AWTEventListenerProxy

extends
EventListenerProxy
<
AWTEventListener
>
implements
AWTEventListener
```

A class which extends the

EventListenerProxy

specifically for adding an

AWTEventListener

for a specific event mask.
Instances of this class can be added as

AWTEventListener

s
to a

Toolkit

object.

The

getAWTEventListeners

method of

Toolkit

can return a mixture of

AWTEventListener

and

AWTEventListenerProxy

objects.

**Since:** 1.4
**See Also:** Toolkit

,

EventListenerProxy

public class

AWTEventListenerProxy

extends

EventListenerProxy

<

AWTEventListener

>
implements

AWTEventListener

A class which extends the

EventListenerProxy

specifically for adding an

AWTEventListener

for a specific event mask.
Instances of this class can be added as

AWTEventListener

s
to a

Toolkit

object.

The

getAWTEventListeners

method of

Toolkit

can return a mixture of

AWTEventListener

and

AWTEventListenerProxy

objects.

The

getAWTEventListeners

method of

Toolkit

can return a mixture of

AWTEventListener

and

AWTEventListenerProxy

objects.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AWTEventListenerProxy

​(long eventMask,

AWTEventListener

listener)

Constructor which binds the

AWTEventListener

to a specific event mask.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

eventDispatched

​(

AWTEvent

event)

Forwards the AWT event to the listener delegate.

long

getEventMask

()

Returns the event mask associated with the listener.

- Methods declared in class java.util.

EventListenerProxy

getListener

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

AWTEventListenerProxy

​(long eventMask,

AWTEventListener

listener)

Constructor which binds the

AWTEventListener

to a specific event mask.

---

#### Constructor Summary

Constructor which binds the

AWTEventListener

to a specific event mask.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

eventDispatched

​(

AWTEvent

event)

Forwards the AWT event to the listener delegate.

long

getEventMask

()

Returns the event mask associated with the listener.

- Methods declared in class java.util.

EventListenerProxy

getListener

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

Forwards the AWT event to the listener delegate.

Returns the event mask associated with the listener.

Methods declared in class java.util.

EventListenerProxy

getListener

---

#### Methods declared in class java.util. EventListenerProxy

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

- AWTEventListenerProxy

```java
public AWTEventListenerProxy​(long eventMask,

AWTEventListener
listener)
```

Constructor which binds the

AWTEventListener

to a specific event mask.

**Parameters:** eventMask

- the bitmap of event types to receive
**Parameters:** listener

- the listener object

============ METHOD DETAIL ==========

- Method Detail

- eventDispatched

```java
public void eventDispatched​(
AWTEvent
event)
```

Forwards the AWT event to the listener delegate.

**Specified by:** eventDispatched

in interface

AWTEventListener
**Parameters:** event

- the AWT event

- getEventMask

```java
public long getEventMask()
```

Returns the event mask associated with the listener.

**Returns:** the event mask associated with the listener

Constructor Detail

- AWTEventListenerProxy

```java
public AWTEventListenerProxy​(long eventMask,

AWTEventListener
listener)
```

Constructor which binds the

AWTEventListener

to a specific event mask.

**Parameters:** eventMask

- the bitmap of event types to receive
**Parameters:** listener

- the listener object

---

#### Constructor Detail

AWTEventListenerProxy

```java
public AWTEventListenerProxy​(long eventMask,

AWTEventListener
listener)
```

Constructor which binds the

AWTEventListener

to a specific event mask.

**Parameters:** eventMask

- the bitmap of event types to receive
**Parameters:** listener

- the listener object

---

#### AWTEventListenerProxy

public AWTEventListenerProxy​(long eventMask,

AWTEventListener

listener)

Constructor which binds the

AWTEventListener

to a specific event mask.

Method Detail

- eventDispatched

```java
public void eventDispatched​(
AWTEvent
event)
```

Forwards the AWT event to the listener delegate.

**Specified by:** eventDispatched

in interface

AWTEventListener
**Parameters:** event

- the AWT event

- getEventMask

```java
public long getEventMask()
```

Returns the event mask associated with the listener.

**Returns:** the event mask associated with the listener

---

#### Method Detail

eventDispatched

```java
public void eventDispatched​(
AWTEvent
event)
```

Forwards the AWT event to the listener delegate.

**Specified by:** eventDispatched

in interface

AWTEventListener
**Parameters:** event

- the AWT event

---

#### eventDispatched

public void eventDispatched​(

AWTEvent

event)

Forwards the AWT event to the listener delegate.

getEventMask

```java
public long getEventMask()
```

Returns the event mask associated with the listener.

**Returns:** the event mask associated with the listener

---

#### getEventMask

public long getEventMask()

Returns the event mask associated with the listener.

---

