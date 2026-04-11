# Class InvocationEvent

**Source:** `java.desktop\java\awt\event\InvocationEvent.html`

### Class Description

```java
public class
InvocationEvent

extends
AWTEvent

implements
ActiveEvent
```

An event which executes the

run()

method on a

Runnable

when dispatched by the AWT event dispatcher thread. This class can
be used as a reference implementation of

ActiveEvent

rather
than declaring a new class and defining

dispatch()

.

Instances of this class are placed on the

EventQueue

by calls
to

invokeLater

and

invokeAndWait

. Client code
can use this fact to write replacement functions for

invokeLater

and

invokeAndWait

without writing special-case code
in any

AWTEventListener

objects.

An unspecified behavior will be caused if the

id

parameter
of any particular

InvocationEvent

instance is not
in the range from

INVOCATION_FIRST

to

INVOCATION_LAST

.

**All Implemented Interfaces:** ActiveEvent

,

Serializable

---

### Field Details

#### public static final int INVOCATION_FIRST

Marks the first integer id for the range of invocation event ids.

**See Also:**
- Constant Field Values

---

#### public static final int INVOCATION_DEFAULT

The default id for all InvocationEvents.

**See Also:**
- Constant Field Values

---

#### public static final int INVOCATION_LAST

Marks the last integer id for the range of invocation event ids.

**See Also:**
- Constant Field Values

---

#### protected
Runnable
runnable

The Runnable whose run() method will be called.

---

#### protected volatile
Object
notifier

The (potentially null) Object whose notifyAll() method will be called
immediately after the Runnable.run() method has returned or thrown an exception
or after the event was disposed.

**See Also:**
- isDispatched()

---

#### protected boolean catchExceptions

Set to true if dispatch() catches Throwable and stores it in the
exception instance variable. If false, Throwables are propagated up
to the EventDispatchThread's dispatch loop.

---

### Constructor Details

#### public InvocationEvent​(
Object
source,

Runnable
runnable)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

This is a convenience constructor. An invocation of the form

InvocationEvent(source, runnable)

behaves in exactly the same way as the invocation of

InvocationEvent(source, runnable, null, false)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:**
- source

- The

Object

that originated the event
- runnable

- The

Runnable

whose

run

method will be executed

**Throws:**
- IllegalArgumentException

- if

source

is null

**See Also:**
- EventObject.getSource()

,

InvocationEvent(Object, Runnable, Object, boolean)

---

#### public InvocationEvent​(
Object
source,

Runnable
runnable,

Object
notifier,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll()

will be called on it
immediately after

run

has returned or thrown an exception.

An invocation of the form

InvocationEvent(source, runnable, notifier, catchThrowables)

behaves in exactly the same way as the invocation of

InvocationEvent(source, InvocationEvent.INVOCATION_DEFAULT, runnable, notifier, catchThrowables)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:**
- source

- The

Object

that originated
the event
- runnable

- The

Runnable

whose

run

method will be
executed
- notifier

- The

Object

whose

notifyAll

method will be called after

Runnable.run

has returned or
thrown an exception or after the event was
disposed
- catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing
the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop

**Throws:**
- IllegalArgumentException

- if

source

is null

**See Also:**
- EventObject.getSource()

,

InvocationEvent(Object, int, Runnable, Object, boolean)

---

#### public InvocationEvent​(
Object
source,

Runnable
runnable,

Runnable
listener,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If listener is non-

null

,

listener.run()

will be called immediately after

run

has returned, thrown an exception or the event
was disposed.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:**
- source

- The

Object

that originated
the event
- runnable

- The

Runnable

whose

run

method will be
executed
- listener

- The

Runnable

Runnable whose

run()

method will be called
after the

InvocationEvent

was dispatched or disposed
- catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing
the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop

**Throws:**
- IllegalArgumentException

- if

source

is null

---

#### protected InvocationEvent​(
Object
source,
int id,

Runnable
runnable,

Object
notifier,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source and ID which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll

will be called on it immediately after

run

has returned or thrown an exception.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:**
- source

- The

Object

that originated
the event
- id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

InvocationEvent
- runnable

- The

Runnable

whose

run

method will be executed
- notifier

- The

Object

whose

notifyAll

method will be called after

Runnable.run

has returned or
thrown an exception or after the event was
disposed
- catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop

**Throws:**
- IllegalArgumentException

- if

source

is null

**See Also:**
- EventObject.getSource()

,

AWTEvent.getID()

---

### Method Details

#### public void dispatch()

Executes the Runnable's

run()

method and notifies the
notifier (if any) when

run()

has returned or thrown an exception.

**Specified by:**
- dispatch

in interface

ActiveEvent

**See Also:**
- isDispatched()

---

#### public
Exception
getException()

Returns any Exception caught while executing
the Runnable's

run()

method.

**Returns:**
- A reference to the Exception if one was thrown; null if no
Exception was thrown or if this InvocationEvent does not
catch exceptions

---

#### public
Throwable
getThrowable()

Returns any Throwable caught while executing
the Runnable's

run()

method.

**Returns:**
- A reference to the Throwable if one was thrown; null if no
Throwable was thrown or if this InvocationEvent does not
catch Throwables

**Since:**
- 1.5

---

#### public long getWhen()

Returns the timestamp of when this event occurred.

**Returns:**
- this event's timestamp

**Since:**
- 1.4

---

#### public boolean isDispatched()

Returns

true

if the event is dispatched or any exception is
thrown while dispatching,

false

otherwise. The method should
be called by a waiting thread that calls the

notifier.wait()

method.
Since spurious wakeups are possible (as explained in

Object.wait()

),
this method should be used in a waiting loop to ensure that the event
got dispatched:

```java
while (!event.isDispatched()) {
notifier.wait();
}
```

If the waiting thread wakes up without dispatching the event,
the

isDispatched()

method returns

false

, and
the

while

loop executes once more, thus, causing
the awakened thread to revert to the waiting mode.

If the

notifier.notifyAll()

happens before the waiting thread
enters the

notifier.wait()

method, the

while

loop ensures
that the waiting thread will not enter the

notifier.wait()

method.
Otherwise, there is no guarantee that the waiting thread will ever be woken
from the wait.

**Returns:**
- true

if the event has been dispatched, or any exception
has been thrown while dispatching,

false

otherwise

**See Also:**
- dispatch()

,

notifier

,

catchExceptions

**Since:**
- 1.7

---

#### public
String
paramString()

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

**Overrides:**
- paramString

in class

AWTEvent

**Returns:**
- A string identifying the event and its attributes

---

### Additional Sections

#### Class InvocationEvent

java.lang.Object

- java.util.EventObject
- - java.awt.AWTEvent
- - java.awt.event.InvocationEvent

java.util.EventObject

- java.awt.AWTEvent
- - java.awt.event.InvocationEvent

java.awt.AWTEvent

- java.awt.event.InvocationEvent

java.awt.event.InvocationEvent

**All Implemented Interfaces:** ActiveEvent

,

Serializable

```java
public class
InvocationEvent

extends
AWTEvent

implements
ActiveEvent
```

An event which executes the

run()

method on a

Runnable

when dispatched by the AWT event dispatcher thread. This class can
be used as a reference implementation of

ActiveEvent

rather
than declaring a new class and defining

dispatch()

.

Instances of this class are placed on the

EventQueue

by calls
to

invokeLater

and

invokeAndWait

. Client code
can use this fact to write replacement functions for

invokeLater

and

invokeAndWait

without writing special-case code
in any

AWTEventListener

objects.

An unspecified behavior will be caused if the

id

parameter
of any particular

InvocationEvent

instance is not
in the range from

INVOCATION_FIRST

to

INVOCATION_LAST

.

**Since:** 1.2
**See Also:** ActiveEvent

,

EventQueue.invokeLater(java.lang.Runnable)

,

EventQueue.invokeAndWait(java.lang.Runnable)

,

AWTEventListener

,

Serialized Form

public class

InvocationEvent

extends

AWTEvent

implements

ActiveEvent

An event which executes the

run()

method on a

Runnable

when dispatched by the AWT event dispatcher thread. This class can
be used as a reference implementation of

ActiveEvent

rather
than declaring a new class and defining

dispatch()

.

Instances of this class are placed on the

EventQueue

by calls
to

invokeLater

and

invokeAndWait

. Client code
can use this fact to write replacement functions for

invokeLater

and

invokeAndWait

without writing special-case code
in any

AWTEventListener

objects.

An unspecified behavior will be caused if the

id

parameter
of any particular

InvocationEvent

instance is not
in the range from

INVOCATION_FIRST

to

INVOCATION_LAST

.

Instances of this class are placed on the

EventQueue

by calls
to

invokeLater

and

invokeAndWait

. Client code
can use this fact to write replacement functions for

invokeLater

and

invokeAndWait

without writing special-case code
in any

AWTEventListener

objects.

An unspecified behavior will be caused if the

id

parameter
of any particular

InvocationEvent

instance is not
in the range from

INVOCATION_FIRST

to

INVOCATION_LAST

.

An unspecified behavior will be caused if the

id

parameter
of any particular

InvocationEvent

instance is not
in the range from

INVOCATION_FIRST

to

INVOCATION_LAST

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

catchExceptions

Set to true if dispatch() catches Throwable and stores it in the
exception instance variable.

static int

INVOCATION_DEFAULT

The default id for all InvocationEvents.

static int

INVOCATION_FIRST

Marks the first integer id for the range of invocation event ids.

static int

INVOCATION_LAST

Marks the last integer id for the range of invocation event ids.

protected

Object

notifier

The (potentially null) Object whose notifyAll() method will be called
immediately after the Runnable.run() method has returned or thrown an exception
or after the event was disposed.

protected

Runnable

runnable

The Runnable whose run() method will be called.

- Fields declared in class java.awt.

AWTEvent

ACTION_EVENT_MASK

,

ADJUSTMENT_EVENT_MASK

,

COMPONENT_EVENT_MASK

,

consumed

,

CONTAINER_EVENT_MASK

,

FOCUS_EVENT_MASK

,

HIERARCHY_BOUNDS_EVENT_MASK

,

HIERARCHY_EVENT_MASK

,

id

,

INPUT_METHOD_EVENT_MASK

,

INVOCATION_EVENT_MASK

,

ITEM_EVENT_MASK

,

KEY_EVENT_MASK

,

MOUSE_EVENT_MASK

,

MOUSE_MOTION_EVENT_MASK

,

MOUSE_WHEEL_EVENT_MASK

,

PAINT_EVENT_MASK

,

RESERVED_ID_MAX

,

TEXT_EVENT_MASK

,

WINDOW_EVENT_MASK

,

WINDOW_FOCUS_EVENT_MASK

,

WINDOW_STATE_EVENT_MASK

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

InvocationEvent

​(

Object

source,
int id,

Runnable

runnable,

Object

notifier,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source and ID which will execute the runnable's

run

method when dispatched.

InvocationEvent

​(

Object

source,

Runnable

runnable)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

InvocationEvent

​(

Object

source,

Runnable

runnable,

Object

notifier,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

InvocationEvent

​(

Object

source,

Runnable

runnable,

Runnable

listener,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

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

()

Executes the Runnable's

run()

method and notifies the
notifier (if any) when

run()

has returned or thrown an exception.

Exception

getException

()

Returns any Exception caught while executing
the Runnable's

run()

method.

Throwable

getThrowable

()

Returns any Throwable caught while executing
the Runnable's

run()

method.

long

getWhen

()

Returns the timestamp of when this event occurred.

boolean

isDispatched

()

Returns

true

if the event is dispatched or any exception is
thrown while dispatching,

false

otherwise.

String

paramString

()

Returns a parameter string identifying this event.

- Methods declared in class java.awt.

AWTEvent

consume

,

getID

,

isConsumed

,

setSource

,

toString

- Methods declared in class java.util.

EventObject

getSource

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

Fields

Modifier and Type

Field

Description

protected boolean

catchExceptions

Set to true if dispatch() catches Throwable and stores it in the
exception instance variable.

static int

INVOCATION_DEFAULT

The default id for all InvocationEvents.

static int

INVOCATION_FIRST

Marks the first integer id for the range of invocation event ids.

static int

INVOCATION_LAST

Marks the last integer id for the range of invocation event ids.

protected

Object

notifier

The (potentially null) Object whose notifyAll() method will be called
immediately after the Runnable.run() method has returned or thrown an exception
or after the event was disposed.

protected

Runnable

runnable

The Runnable whose run() method will be called.

- Fields declared in class java.awt.

AWTEvent

ACTION_EVENT_MASK

,

ADJUSTMENT_EVENT_MASK

,

COMPONENT_EVENT_MASK

,

consumed

,

CONTAINER_EVENT_MASK

,

FOCUS_EVENT_MASK

,

HIERARCHY_BOUNDS_EVENT_MASK

,

HIERARCHY_EVENT_MASK

,

id

,

INPUT_METHOD_EVENT_MASK

,

INVOCATION_EVENT_MASK

,

ITEM_EVENT_MASK

,

KEY_EVENT_MASK

,

MOUSE_EVENT_MASK

,

MOUSE_MOTION_EVENT_MASK

,

MOUSE_WHEEL_EVENT_MASK

,

PAINT_EVENT_MASK

,

RESERVED_ID_MAX

,

TEXT_EVENT_MASK

,

WINDOW_EVENT_MASK

,

WINDOW_FOCUS_EVENT_MASK

,

WINDOW_STATE_EVENT_MASK

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Set to true if dispatch() catches Throwable and stores it in the
exception instance variable.

The default id for all InvocationEvents.

Marks the first integer id for the range of invocation event ids.

Marks the last integer id for the range of invocation event ids.

The (potentially null) Object whose notifyAll() method will be called
immediately after the Runnable.run() method has returned or thrown an exception
or after the event was disposed.

The Runnable whose run() method will be called.

Fields declared in class java.awt.

AWTEvent

ACTION_EVENT_MASK

,

ADJUSTMENT_EVENT_MASK

,

COMPONENT_EVENT_MASK

,

consumed

,

CONTAINER_EVENT_MASK

,

FOCUS_EVENT_MASK

,

HIERARCHY_BOUNDS_EVENT_MASK

,

HIERARCHY_EVENT_MASK

,

id

,

INPUT_METHOD_EVENT_MASK

,

INVOCATION_EVENT_MASK

,

ITEM_EVENT_MASK

,

KEY_EVENT_MASK

,

MOUSE_EVENT_MASK

,

MOUSE_MOTION_EVENT_MASK

,

MOUSE_WHEEL_EVENT_MASK

,

PAINT_EVENT_MASK

,

RESERVED_ID_MAX

,

TEXT_EVENT_MASK

,

WINDOW_EVENT_MASK

,

WINDOW_FOCUS_EVENT_MASK

,

WINDOW_STATE_EVENT_MASK

---

#### Fields declared in class java.awt. AWTEvent

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

InvocationEvent

​(

Object

source,
int id,

Runnable

runnable,

Object

notifier,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source and ID which will execute the runnable's

run

method when dispatched.

InvocationEvent

​(

Object

source,

Runnable

runnable)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

InvocationEvent

​(

Object

source,

Runnable

runnable,

Object

notifier,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

InvocationEvent

​(

Object

source,

Runnable

runnable,

Runnable

listener,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

---

#### Constructor Summary

Constructs an

InvocationEvent

with the specified
source and ID which will execute the runnable's

run

method when dispatched.

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

dispatch

()

Executes the Runnable's

run()

method and notifies the
notifier (if any) when

run()

has returned or thrown an exception.

Exception

getException

()

Returns any Exception caught while executing
the Runnable's

run()

method.

Throwable

getThrowable

()

Returns any Throwable caught while executing
the Runnable's

run()

method.

long

getWhen

()

Returns the timestamp of when this event occurred.

boolean

isDispatched

()

Returns

true

if the event is dispatched or any exception is
thrown while dispatching,

false

otherwise.

String

paramString

()

Returns a parameter string identifying this event.

- Methods declared in class java.awt.

AWTEvent

consume

,

getID

,

isConsumed

,

setSource

,

toString

- Methods declared in class java.util.

EventObject

getSource

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

Executes the Runnable's

run()

method and notifies the
notifier (if any) when

run()

has returned or thrown an exception.

Returns any Exception caught while executing
the Runnable's

run()

method.

Returns any Throwable caught while executing
the Runnable's

run()

method.

Returns the timestamp of when this event occurred.

Returns

true

if the event is dispatched or any exception is
thrown while dispatching,

false

otherwise.

Returns a parameter string identifying this event.

Methods declared in class java.awt.

AWTEvent

consume

,

getID

,

isConsumed

,

setSource

,

toString

---

#### Methods declared in class java.awt. AWTEvent

Methods declared in class java.util.

EventObject

getSource

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

============ FIELD DETAIL ===========

- Field Detail

- INVOCATION_FIRST

```java
public static final int INVOCATION_FIRST
```

Marks the first integer id for the range of invocation event ids.

**See Also:** Constant Field Values

- INVOCATION_DEFAULT

```java
public static final int INVOCATION_DEFAULT
```

The default id for all InvocationEvents.

**See Also:** Constant Field Values

- INVOCATION_LAST

```java
public static final int INVOCATION_LAST
```

Marks the last integer id for the range of invocation event ids.

**See Also:** Constant Field Values

- runnable

```java
protected
Runnable
runnable
```

The Runnable whose run() method will be called.

- notifier

```java
protected volatile
Object
notifier
```

The (potentially null) Object whose notifyAll() method will be called
immediately after the Runnable.run() method has returned or thrown an exception
or after the event was disposed.

**See Also:** isDispatched()

- catchExceptions

```java
protected boolean catchExceptions
```

Set to true if dispatch() catches Throwable and stores it in the
exception instance variable. If false, Throwables are propagated up
to the EventDispatchThread's dispatch loop.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InvocationEvent

```java
public InvocationEvent​(
Object
source,

Runnable
runnable)
```

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

This is a convenience constructor. An invocation of the form

InvocationEvent(source, runnable)

behaves in exactly the same way as the invocation of

InvocationEvent(source, runnable, null, false)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated the event
**Parameters:** runnable

- The

Runnable

whose

run

method will be executed
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

InvocationEvent(Object, Runnable, Object, boolean)

- InvocationEvent

```java
public InvocationEvent​(
Object
source,

Runnable
runnable,

Object
notifier,
boolean catchThrowables)
```

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll()

will be called on it
immediately after

run

has returned or thrown an exception.

An invocation of the form

InvocationEvent(source, runnable, notifier, catchThrowables)

behaves in exactly the same way as the invocation of

InvocationEvent(source, InvocationEvent.INVOCATION_DEFAULT, runnable, notifier, catchThrowables)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated
the event
**Parameters:** runnable

- The

Runnable

whose

run

method will be
executed
**Parameters:** notifier

- The

Object

whose

notifyAll

method will be called after

Runnable.run

has returned or
thrown an exception or after the event was
disposed
**Parameters:** catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing
the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

InvocationEvent(Object, int, Runnable, Object, boolean)

- InvocationEvent

```java
public InvocationEvent​(
Object
source,

Runnable
runnable,

Runnable
listener,
boolean catchThrowables)
```

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If listener is non-

null

,

listener.run()

will be called immediately after

run

has returned, thrown an exception or the event
was disposed.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated
the event
**Parameters:** runnable

- The

Runnable

whose

run

method will be
executed
**Parameters:** listener

- The

Runnable

Runnable whose

run()

method will be called
after the

InvocationEvent

was dispatched or disposed
**Parameters:** catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing
the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop
**Throws:** IllegalArgumentException

- if

source

is null

- InvocationEvent

```java
protected InvocationEvent​(
Object
source,
int id,

Runnable
runnable,

Object
notifier,
boolean catchThrowables)
```

Constructs an

InvocationEvent

with the specified
source and ID which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll

will be called on it immediately after

run

has returned or thrown an exception.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated
the event
**Parameters:** id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

InvocationEvent
**Parameters:** runnable

- The

Runnable

whose

run

method will be executed
**Parameters:** notifier

- The

Object

whose

notifyAll

method will be called after

Runnable.run

has returned or
thrown an exception or after the event was
disposed
**Parameters:** catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

============ METHOD DETAIL ==========

- Method Detail

- dispatch

```java
public void dispatch()
```

Executes the Runnable's

run()

method and notifies the
notifier (if any) when

run()

has returned or thrown an exception.

**Specified by:** dispatch

in interface

ActiveEvent
**See Also:** isDispatched()

- getException

```java
public
Exception
getException()
```

Returns any Exception caught while executing
the Runnable's

run()

method.

**Returns:** A reference to the Exception if one was thrown; null if no
Exception was thrown or if this InvocationEvent does not
catch exceptions

- getThrowable

```java
public
Throwable
getThrowable()
```

Returns any Throwable caught while executing
the Runnable's

run()

method.

**Returns:** A reference to the Throwable if one was thrown; null if no
Throwable was thrown or if this InvocationEvent does not
catch Throwables
**Since:** 1.5

- getWhen

```java
public long getWhen()
```

Returns the timestamp of when this event occurred.

**Returns:** this event's timestamp
**Since:** 1.4

- isDispatched

```java
public boolean isDispatched()
```

Returns

true

if the event is dispatched or any exception is
thrown while dispatching,

false

otherwise. The method should
be called by a waiting thread that calls the

notifier.wait()

method.
Since spurious wakeups are possible (as explained in

Object.wait()

),
this method should be used in a waiting loop to ensure that the event
got dispatched:

```java
while (!event.isDispatched()) {
notifier.wait();
}
```

If the waiting thread wakes up without dispatching the event,
the

isDispatched()

method returns

false

, and
the

while

loop executes once more, thus, causing
the awakened thread to revert to the waiting mode.

If the

notifier.notifyAll()

happens before the waiting thread
enters the

notifier.wait()

method, the

while

loop ensures
that the waiting thread will not enter the

notifier.wait()

method.
Otherwise, there is no guarantee that the waiting thread will ever be woken
from the wait.

**Returns:** true

if the event has been dispatched, or any exception
has been thrown while dispatching,

false

otherwise
**Since:** 1.7
**See Also:** dispatch()

,

notifier

,

catchExceptions

- paramString

```java
public
String
paramString()
```

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

**Overrides:** paramString

in class

AWTEvent
**Returns:** A string identifying the event and its attributes

Field Detail

- INVOCATION_FIRST

```java
public static final int INVOCATION_FIRST
```

Marks the first integer id for the range of invocation event ids.

**See Also:** Constant Field Values

- INVOCATION_DEFAULT

```java
public static final int INVOCATION_DEFAULT
```

The default id for all InvocationEvents.

**See Also:** Constant Field Values

- INVOCATION_LAST

```java
public static final int INVOCATION_LAST
```

Marks the last integer id for the range of invocation event ids.

**See Also:** Constant Field Values

- runnable

```java
protected
Runnable
runnable
```

The Runnable whose run() method will be called.

- notifier

```java
protected volatile
Object
notifier
```

The (potentially null) Object whose notifyAll() method will be called
immediately after the Runnable.run() method has returned or thrown an exception
or after the event was disposed.

**See Also:** isDispatched()

- catchExceptions

```java
protected boolean catchExceptions
```

Set to true if dispatch() catches Throwable and stores it in the
exception instance variable. If false, Throwables are propagated up
to the EventDispatchThread's dispatch loop.

---

#### Field Detail

INVOCATION_FIRST

```java
public static final int INVOCATION_FIRST
```

Marks the first integer id for the range of invocation event ids.

**See Also:** Constant Field Values

---

#### INVOCATION_FIRST

public static final int INVOCATION_FIRST

Marks the first integer id for the range of invocation event ids.

INVOCATION_DEFAULT

```java
public static final int INVOCATION_DEFAULT
```

The default id for all InvocationEvents.

**See Also:** Constant Field Values

---

#### INVOCATION_DEFAULT

public static final int INVOCATION_DEFAULT

The default id for all InvocationEvents.

INVOCATION_LAST

```java
public static final int INVOCATION_LAST
```

Marks the last integer id for the range of invocation event ids.

**See Also:** Constant Field Values

---

#### INVOCATION_LAST

public static final int INVOCATION_LAST

Marks the last integer id for the range of invocation event ids.

runnable

```java
protected
Runnable
runnable
```

The Runnable whose run() method will be called.

---

#### runnable

protected

Runnable

runnable

The Runnable whose run() method will be called.

notifier

```java
protected volatile
Object
notifier
```

The (potentially null) Object whose notifyAll() method will be called
immediately after the Runnable.run() method has returned or thrown an exception
or after the event was disposed.

**See Also:** isDispatched()

---

#### notifier

protected volatile

Object

notifier

The (potentially null) Object whose notifyAll() method will be called
immediately after the Runnable.run() method has returned or thrown an exception
or after the event was disposed.

catchExceptions

```java
protected boolean catchExceptions
```

Set to true if dispatch() catches Throwable and stores it in the
exception instance variable. If false, Throwables are propagated up
to the EventDispatchThread's dispatch loop.

---

#### catchExceptions

protected boolean catchExceptions

Set to true if dispatch() catches Throwable and stores it in the
exception instance variable. If false, Throwables are propagated up
to the EventDispatchThread's dispatch loop.

Constructor Detail

- InvocationEvent

```java
public InvocationEvent​(
Object
source,

Runnable
runnable)
```

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

This is a convenience constructor. An invocation of the form

InvocationEvent(source, runnable)

behaves in exactly the same way as the invocation of

InvocationEvent(source, runnable, null, false)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated the event
**Parameters:** runnable

- The

Runnable

whose

run

method will be executed
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

InvocationEvent(Object, Runnable, Object, boolean)

- InvocationEvent

```java
public InvocationEvent​(
Object
source,

Runnable
runnable,

Object
notifier,
boolean catchThrowables)
```

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll()

will be called on it
immediately after

run

has returned or thrown an exception.

An invocation of the form

InvocationEvent(source, runnable, notifier, catchThrowables)

behaves in exactly the same way as the invocation of

InvocationEvent(source, InvocationEvent.INVOCATION_DEFAULT, runnable, notifier, catchThrowables)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated
the event
**Parameters:** runnable

- The

Runnable

whose

run

method will be
executed
**Parameters:** notifier

- The

Object

whose

notifyAll

method will be called after

Runnable.run

has returned or
thrown an exception or after the event was
disposed
**Parameters:** catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing
the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

InvocationEvent(Object, int, Runnable, Object, boolean)

- InvocationEvent

```java
public InvocationEvent​(
Object
source,

Runnable
runnable,

Runnable
listener,
boolean catchThrowables)
```

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If listener is non-

null

,

listener.run()

will be called immediately after

run

has returned, thrown an exception or the event
was disposed.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated
the event
**Parameters:** runnable

- The

Runnable

whose

run

method will be
executed
**Parameters:** listener

- The

Runnable

Runnable whose

run()

method will be called
after the

InvocationEvent

was dispatched or disposed
**Parameters:** catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing
the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop
**Throws:** IllegalArgumentException

- if

source

is null

- InvocationEvent

```java
protected InvocationEvent​(
Object
source,
int id,

Runnable
runnable,

Object
notifier,
boolean catchThrowables)
```

Constructs an

InvocationEvent

with the specified
source and ID which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll

will be called on it immediately after

run

has returned or thrown an exception.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated
the event
**Parameters:** id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

InvocationEvent
**Parameters:** runnable

- The

Runnable

whose

run

method will be executed
**Parameters:** notifier

- The

Object

whose

notifyAll

method will be called after

Runnable.run

has returned or
thrown an exception or after the event was
disposed
**Parameters:** catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

---

#### Constructor Detail

InvocationEvent

```java
public InvocationEvent​(
Object
source,

Runnable
runnable)
```

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

This is a convenience constructor. An invocation of the form

InvocationEvent(source, runnable)

behaves in exactly the same way as the invocation of

InvocationEvent(source, runnable, null, false)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated the event
**Parameters:** runnable

- The

Runnable

whose

run

method will be executed
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

InvocationEvent(Object, Runnable, Object, boolean)

---

#### InvocationEvent

public InvocationEvent​(

Object

source,

Runnable

runnable)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched.

This is a convenience constructor. An invocation of the form

InvocationEvent(source, runnable)

behaves in exactly the same way as the invocation of

InvocationEvent(source, runnable, null, false)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

This is a convenience constructor. An invocation of the form

InvocationEvent(source, runnable)

behaves in exactly the same way as the invocation of

InvocationEvent(source, runnable, null, false)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

This method throws an

IllegalArgumentException

if

source

is

null

.

InvocationEvent

```java
public InvocationEvent​(
Object
source,

Runnable
runnable,

Object
notifier,
boolean catchThrowables)
```

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll()

will be called on it
immediately after

run

has returned or thrown an exception.

An invocation of the form

InvocationEvent(source, runnable, notifier, catchThrowables)

behaves in exactly the same way as the invocation of

InvocationEvent(source, InvocationEvent.INVOCATION_DEFAULT, runnable, notifier, catchThrowables)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated
the event
**Parameters:** runnable

- The

Runnable

whose

run

method will be
executed
**Parameters:** notifier

- The

Object

whose

notifyAll

method will be called after

Runnable.run

has returned or
thrown an exception or after the event was
disposed
**Parameters:** catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing
the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

InvocationEvent(Object, int, Runnable, Object, boolean)

---

#### InvocationEvent

public InvocationEvent​(

Object

source,

Runnable

runnable,

Object

notifier,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll()

will be called on it
immediately after

run

has returned or thrown an exception.

An invocation of the form

InvocationEvent(source, runnable, notifier, catchThrowables)

behaves in exactly the same way as the invocation of

InvocationEvent(source, InvocationEvent.INVOCATION_DEFAULT, runnable, notifier, catchThrowables)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

An invocation of the form

InvocationEvent(source, runnable, notifier, catchThrowables)

behaves in exactly the same way as the invocation of

InvocationEvent(source, InvocationEvent.INVOCATION_DEFAULT, runnable, notifier, catchThrowables)

.

This method throws an

IllegalArgumentException

if

source

is

null

.

This method throws an

IllegalArgumentException

if

source

is

null

.

InvocationEvent

```java
public InvocationEvent​(
Object
source,

Runnable
runnable,

Runnable
listener,
boolean catchThrowables)
```

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If listener is non-

null

,

listener.run()

will be called immediately after

run

has returned, thrown an exception or the event
was disposed.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated
the event
**Parameters:** runnable

- The

Runnable

whose

run

method will be
executed
**Parameters:** listener

- The

Runnable

Runnable whose

run()

method will be called
after the

InvocationEvent

was dispatched or disposed
**Parameters:** catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing
the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop
**Throws:** IllegalArgumentException

- if

source

is null

---

#### InvocationEvent

public InvocationEvent​(

Object

source,

Runnable

runnable,

Runnable

listener,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source which will execute the runnable's

run

method when dispatched. If listener is non-

null

,

listener.run()

will be called immediately after

run

has returned, thrown an exception or the event
was disposed.

This method throws an

IllegalArgumentException

if

source

is

null

.

This method throws an

IllegalArgumentException

if

source

is

null

.

InvocationEvent

```java
protected InvocationEvent​(
Object
source,
int id,

Runnable
runnable,

Object
notifier,
boolean catchThrowables)
```

Constructs an

InvocationEvent

with the specified
source and ID which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll

will be called on it immediately after

run

has returned or thrown an exception.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Object

that originated
the event
**Parameters:** id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

InvocationEvent
**Parameters:** runnable

- The

Runnable

whose

run

method will be executed
**Parameters:** notifier

- The

Object

whose

notifyAll

method will be called after

Runnable.run

has returned or
thrown an exception or after the event was
disposed
**Parameters:** catchThrowables

- Specifies whether

dispatch

should catch Throwable when executing the

Runnable

's

run

method, or should instead propagate those
Throwables to the EventDispatchThread's
dispatch loop
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

---

#### InvocationEvent

protected InvocationEvent​(

Object

source,
int id,

Runnable

runnable,

Object

notifier,
boolean catchThrowables)

Constructs an

InvocationEvent

with the specified
source and ID which will execute the runnable's

run

method when dispatched. If notifier is non-

null

,

notifyAll

will be called on it immediately after

run

has returned or thrown an exception.

This method throws an

IllegalArgumentException

if

source

is

null

.

This method throws an

IllegalArgumentException

if

source

is

null

.

Method Detail

- dispatch

```java
public void dispatch()
```

Executes the Runnable's

run()

method and notifies the
notifier (if any) when

run()

has returned or thrown an exception.

**Specified by:** dispatch

in interface

ActiveEvent
**See Also:** isDispatched()

- getException

```java
public
Exception
getException()
```

Returns any Exception caught while executing
the Runnable's

run()

method.

**Returns:** A reference to the Exception if one was thrown; null if no
Exception was thrown or if this InvocationEvent does not
catch exceptions

- getThrowable

```java
public
Throwable
getThrowable()
```

Returns any Throwable caught while executing
the Runnable's

run()

method.

**Returns:** A reference to the Throwable if one was thrown; null if no
Throwable was thrown or if this InvocationEvent does not
catch Throwables
**Since:** 1.5

- getWhen

```java
public long getWhen()
```

Returns the timestamp of when this event occurred.

**Returns:** this event's timestamp
**Since:** 1.4

- isDispatched

```java
public boolean isDispatched()
```

Returns

true

if the event is dispatched or any exception is
thrown while dispatching,

false

otherwise. The method should
be called by a waiting thread that calls the

notifier.wait()

method.
Since spurious wakeups are possible (as explained in

Object.wait()

),
this method should be used in a waiting loop to ensure that the event
got dispatched:

```java
while (!event.isDispatched()) {
notifier.wait();
}
```

If the waiting thread wakes up without dispatching the event,
the

isDispatched()

method returns

false

, and
the

while

loop executes once more, thus, causing
the awakened thread to revert to the waiting mode.

If the

notifier.notifyAll()

happens before the waiting thread
enters the

notifier.wait()

method, the

while

loop ensures
that the waiting thread will not enter the

notifier.wait()

method.
Otherwise, there is no guarantee that the waiting thread will ever be woken
from the wait.

**Returns:** true

if the event has been dispatched, or any exception
has been thrown while dispatching,

false

otherwise
**Since:** 1.7
**See Also:** dispatch()

,

notifier

,

catchExceptions

- paramString

```java
public
String
paramString()
```

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

**Overrides:** paramString

in class

AWTEvent
**Returns:** A string identifying the event and its attributes

---

#### Method Detail

dispatch

```java
public void dispatch()
```

Executes the Runnable's

run()

method and notifies the
notifier (if any) when

run()

has returned or thrown an exception.

**Specified by:** dispatch

in interface

ActiveEvent
**See Also:** isDispatched()

---

#### dispatch

public void dispatch()

Executes the Runnable's

run()

method and notifies the
notifier (if any) when

run()

has returned or thrown an exception.

getException

```java
public
Exception
getException()
```

Returns any Exception caught while executing
the Runnable's

run()

method.

**Returns:** A reference to the Exception if one was thrown; null if no
Exception was thrown or if this InvocationEvent does not
catch exceptions

---

#### getException

public

Exception

getException()

Returns any Exception caught while executing
the Runnable's

run()

method.

getThrowable

```java
public
Throwable
getThrowable()
```

Returns any Throwable caught while executing
the Runnable's

run()

method.

**Returns:** A reference to the Throwable if one was thrown; null if no
Throwable was thrown or if this InvocationEvent does not
catch Throwables
**Since:** 1.5

---

#### getThrowable

public

Throwable

getThrowable()

Returns any Throwable caught while executing
the Runnable's

run()

method.

getWhen

```java
public long getWhen()
```

Returns the timestamp of when this event occurred.

**Returns:** this event's timestamp
**Since:** 1.4

---

#### getWhen

public long getWhen()

Returns the timestamp of when this event occurred.

isDispatched

```java
public boolean isDispatched()
```

Returns

true

if the event is dispatched or any exception is
thrown while dispatching,

false

otherwise. The method should
be called by a waiting thread that calls the

notifier.wait()

method.
Since spurious wakeups are possible (as explained in

Object.wait()

),
this method should be used in a waiting loop to ensure that the event
got dispatched:

```java
while (!event.isDispatched()) {
notifier.wait();
}
```

If the waiting thread wakes up without dispatching the event,
the

isDispatched()

method returns

false

, and
the

while

loop executes once more, thus, causing
the awakened thread to revert to the waiting mode.

If the

notifier.notifyAll()

happens before the waiting thread
enters the

notifier.wait()

method, the

while

loop ensures
that the waiting thread will not enter the

notifier.wait()

method.
Otherwise, there is no guarantee that the waiting thread will ever be woken
from the wait.

**Returns:** true

if the event has been dispatched, or any exception
has been thrown while dispatching,

false

otherwise
**Since:** 1.7
**See Also:** dispatch()

,

notifier

,

catchExceptions

---

#### isDispatched

public boolean isDispatched()

Returns

true

if the event is dispatched or any exception is
thrown while dispatching,

false

otherwise. The method should
be called by a waiting thread that calls the

notifier.wait()

method.
Since spurious wakeups are possible (as explained in

Object.wait()

),
this method should be used in a waiting loop to ensure that the event
got dispatched:

```java
while (!event.isDispatched()) {
notifier.wait();
}
```

If the waiting thread wakes up without dispatching the event,
the

isDispatched()

method returns

false

, and
the

while

loop executes once more, thus, causing
the awakened thread to revert to the waiting mode.

If the

notifier.notifyAll()

happens before the waiting thread
enters the

notifier.wait()

method, the

while

loop ensures
that the waiting thread will not enter the

notifier.wait()

method.
Otherwise, there is no guarantee that the waiting thread will ever be woken
from the wait.

while (!event.isDispatched()) {
notifier.wait();
}

If the

notifier.notifyAll()

happens before the waiting thread
enters the

notifier.wait()

method, the

while

loop ensures
that the waiting thread will not enter the

notifier.wait()

method.
Otherwise, there is no guarantee that the waiting thread will ever be woken
from the wait.

paramString

```java
public
String
paramString()
```

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

**Overrides:** paramString

in class

AWTEvent
**Returns:** A string identifying the event and its attributes

---

#### paramString

public

String

paramString()

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

---

