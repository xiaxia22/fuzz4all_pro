# Class NamingExceptionEvent

**Source:** `java.naming\javax\naming\event\NamingExceptionEvent.html`

### Class Description

```java
public class
NamingExceptionEvent

extends
EventObject
```

This class represents an event fired when the procedures/processes
used to collect information for notifying listeners of

NamingEvent

s threw a

NamingException

.
This can happen, for example, if the server which the listener is using
aborts subsequent to the

addNamingListener()

call.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NamingExceptionEvent​(
EventContext
source,

NamingException
exc)

Constructs an instance of

NamingExceptionEvent

using
the context in which the

NamingException

was thrown and the exception
that was thrown.

**Parameters:**
- source

- The non-null context in which the exception was thrown.
- exc

- The non-null

NamingException

that was thrown.

---

### Method Details

#### public
NamingException
getException()

Retrieves the exception that was thrown.

**Returns:**
- The exception that was thrown.

---

#### public
EventContext
getEventContext()

Retrieves the

EventContext

that fired this event.
This returns the same object as

EventObject.getSource()

.

**Returns:**
- The non-null

EventContext

that fired this event.

---

#### public void dispatch​(
NamingListener
listener)

Invokes the

namingExceptionThrown()

method on
a listener using this event.

**Parameters:**
- listener

- The non-null naming listener on which to invoke
the method.

---

### Additional Sections

#### Class NamingExceptionEvent

java.lang.Object

- java.util.EventObject
- - javax.naming.event.NamingExceptionEvent

java.util.EventObject

- javax.naming.event.NamingExceptionEvent

javax.naming.event.NamingExceptionEvent

**All Implemented Interfaces:** Serializable

```java
public class
NamingExceptionEvent

extends
EventObject
```

This class represents an event fired when the procedures/processes
used to collect information for notifying listeners of

NamingEvent

s threw a

NamingException

.
This can happen, for example, if the server which the listener is using
aborts subsequent to the

addNamingListener()

call.

**Since:** 1.3
**See Also:** NamingListener.namingExceptionThrown(javax.naming.event.NamingExceptionEvent)

,

EventContext

,

Serialized Form

public class

NamingExceptionEvent

extends

EventObject

This class represents an event fired when the procedures/processes
used to collect information for notifying listeners of

NamingEvent

s threw a

NamingException

.
This can happen, for example, if the server which the listener is using
aborts subsequent to the

addNamingListener()

call.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NamingExceptionEvent

​(

EventContext

source,

NamingException

exc)

Constructs an instance of

NamingExceptionEvent

using
the context in which the

NamingException

was thrown and the exception
that was thrown.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

dispatch

​(

NamingListener

listener)

Invokes the

namingExceptionThrown()

method on
a listener using this event.

EventContext

getEventContext

()

Retrieves the

EventContext

that fired this event.

NamingException

getException

()

Retrieves the exception that was thrown.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

NamingExceptionEvent

​(

EventContext

source,

NamingException

exc)

Constructs an instance of

NamingExceptionEvent

using
the context in which the

NamingException

was thrown and the exception
that was thrown.

---

#### Constructor Summary

Constructs an instance of

NamingExceptionEvent

using
the context in which the

NamingException

was thrown and the exception
that was thrown.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

dispatch

​(

NamingListener

listener)

Invokes the

namingExceptionThrown()

method on
a listener using this event.

EventContext

getEventContext

()

Retrieves the

EventContext

that fired this event.

NamingException

getException

()

Retrieves the exception that was thrown.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Invokes the

namingExceptionThrown()

method on
a listener using this event.

Retrieves the

EventContext

that fired this event.

Retrieves the exception that was thrown.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NamingExceptionEvent

```java
public NamingExceptionEvent​(
EventContext
source,

NamingException
exc)
```

Constructs an instance of

NamingExceptionEvent

using
the context in which the

NamingException

was thrown and the exception
that was thrown.

**Parameters:** source

- The non-null context in which the exception was thrown.
**Parameters:** exc

- The non-null

NamingException

that was thrown.

============ METHOD DETAIL ==========

- Method Detail

- getException

```java
public
NamingException
getException()
```

Retrieves the exception that was thrown.

**Returns:** The exception that was thrown.

- getEventContext

```java
public
EventContext
getEventContext()
```

Retrieves the

EventContext

that fired this event.
This returns the same object as

EventObject.getSource()

.

**Returns:** The non-null

EventContext

that fired this event.

- dispatch

```java
public void dispatch​(
NamingListener
listener)
```

Invokes the

namingExceptionThrown()

method on
a listener using this event.

**Parameters:** listener

- The non-null naming listener on which to invoke
the method.

Constructor Detail

- NamingExceptionEvent

```java
public NamingExceptionEvent​(
EventContext
source,

NamingException
exc)
```

Constructs an instance of

NamingExceptionEvent

using
the context in which the

NamingException

was thrown and the exception
that was thrown.

**Parameters:** source

- The non-null context in which the exception was thrown.
**Parameters:** exc

- The non-null

NamingException

that was thrown.

---

#### Constructor Detail

NamingExceptionEvent

```java
public NamingExceptionEvent​(
EventContext
source,

NamingException
exc)
```

Constructs an instance of

NamingExceptionEvent

using
the context in which the

NamingException

was thrown and the exception
that was thrown.

**Parameters:** source

- The non-null context in which the exception was thrown.
**Parameters:** exc

- The non-null

NamingException

that was thrown.

---

#### NamingExceptionEvent

public NamingExceptionEvent​(

EventContext

source,

NamingException

exc)

Constructs an instance of

NamingExceptionEvent

using
the context in which the

NamingException

was thrown and the exception
that was thrown.

Method Detail

- getException

```java
public
NamingException
getException()
```

Retrieves the exception that was thrown.

**Returns:** The exception that was thrown.

- getEventContext

```java
public
EventContext
getEventContext()
```

Retrieves the

EventContext

that fired this event.
This returns the same object as

EventObject.getSource()

.

**Returns:** The non-null

EventContext

that fired this event.

- dispatch

```java
public void dispatch​(
NamingListener
listener)
```

Invokes the

namingExceptionThrown()

method on
a listener using this event.

**Parameters:** listener

- The non-null naming listener on which to invoke
the method.

---

#### Method Detail

getException

```java
public
NamingException
getException()
```

Retrieves the exception that was thrown.

**Returns:** The exception that was thrown.

---

#### getException

public

NamingException

getException()

Retrieves the exception that was thrown.

getEventContext

```java
public
EventContext
getEventContext()
```

Retrieves the

EventContext

that fired this event.
This returns the same object as

EventObject.getSource()

.

**Returns:** The non-null

EventContext

that fired this event.

---

#### getEventContext

public

EventContext

getEventContext()

Retrieves the

EventContext

that fired this event.
This returns the same object as

EventObject.getSource()

.

dispatch

```java
public void dispatch​(
NamingListener
listener)
```

Invokes the

namingExceptionThrown()

method on
a listener using this event.

**Parameters:** listener

- The non-null naming listener on which to invoke
the method.

---

#### dispatch

public void dispatch​(

NamingListener

listener)

Invokes the

namingExceptionThrown()

method on
a listener using this event.

---

