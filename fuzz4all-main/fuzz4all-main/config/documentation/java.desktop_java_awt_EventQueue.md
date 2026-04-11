# Class EventQueue

**Source:** `java.desktop\java\awt\EventQueue.html`

### Class Description

```java
public class
EventQueue

extends
Object
```

EventQueue

is a platform-independent class
that queues events, both from the underlying peer classes
and from trusted application classes.

It encapsulates asynchronous event dispatch machinery which
extracts events from the queue and dispatches them by calling

dispatchEvent(AWTEvent)

method
on this

EventQueue

with the event to be dispatched
as an argument. The particular behavior of this machinery is
implementation-dependent. The only requirements are that events
which were actually enqueued to this queue (note that events
being posted to the

EventQueue

can be coalesced)
are dispatched:

Some browsers partition applets in different code bases into
separate contexts, and establish walls between these contexts.
In such a scenario, there will be one

EventQueue

per context. Other browsers place all applets into the same
context, implying that there will be only a single, global

EventQueue

for all applets. This behavior is
implementation-dependent. Consult your browser's documentation
for more information.

For information on the threading issues of the event dispatch
machinery, see

AWT Threading Issues

.

---

### Field Details

*No entries found.*

### Constructor Details

#### public EventQueue()

Initializes a new instance of

EventQueue

.

---

### Method Details

#### public void postEvent​(
AWTEvent
theEvent)

Posts a 1.1-style event to the

EventQueue

.
If there is an existing event on the queue with the same ID
and event source, the source

Component

's

coalesceEvents

method will be called.

**Parameters:**
- theEvent

- an instance of

java.awt.AWTEvent

,
or a subclass of it

**Throws:**
- NullPointerException

- if

theEvent

is

null

---

#### public
AWTEvent
getNextEvent()
throws
InterruptedException

Removes an event from the

EventQueue

and
returns it. This method will block until an event has
been posted by another thread.

**Returns:**
- the next

AWTEvent

**Throws:**
- InterruptedException

- if any thread has interrupted this thread

---

#### public
AWTEvent
peekEvent()

Returns the first event on the

EventQueue

without removing it.

**Returns:**
- the first event

---

#### public
AWTEvent
peekEvent​(int id)

Returns the first event with the specified id, if any.

**Parameters:**
- id

- the id of the type of event desired

**Returns:**
- the first event of the specified id or

null

if there is no such event

---

#### protected void dispatchEvent​(
AWTEvent
event)

Dispatches an event. The manner in which the event is
dispatched depends upon the type of the event and the
type of the event's source object:

Event types, source types, and dispatch methods

Event Type

Source Type

Dispatched To

ActiveEvent

Any

event.dispatch()

Other

Component

source.dispatchEvent(AWTEvent)

Other

MenuComponent

source.dispatchEvent(AWTEvent)

Other

Other

No action (ignored)

**Parameters:**
- event

- an instance of

java.awt.AWTEvent

,
or a subclass of it

**Throws:**
- NullPointerException

- if

event

is

null

**Since:**
- 1.2

---

#### public static long getMostRecentEventTime()

Returns the timestamp of the most recent event that had a timestamp, and
that was dispatched from the

EventQueue

associated with the
calling thread. If an event with a timestamp is currently being
dispatched, its timestamp will be returned. If no events have yet
been dispatched, the EventQueue's initialization time will be
returned instead.In the current version of
the JDK, only

InputEvent

s,

ActionEvent

s, and

InvocationEvent

s have
timestamps; however, future versions of the JDK may add timestamps to
additional event types. Note that this method should only be invoked
from an application's

event dispatching thread

.
If this method is
invoked from another thread, the current system time (as reported by

System.currentTimeMillis()

) will be returned instead.

**Returns:**
- the timestamp of the last

InputEvent

,

ActionEvent

, or

InvocationEvent

to be
dispatched, or

System.currentTimeMillis()

if this
method is invoked on a thread other than an event dispatching
thread

**See Also:**
- InputEvent.getWhen()

,

ActionEvent.getWhen()

,

InvocationEvent.getWhen()

,

isDispatchThread()

**Since:**
- 1.4

---

#### public static
AWTEvent
getCurrentEvent()

Returns the event currently being dispatched by the

EventQueue

associated with the calling thread. This is
useful if a method needs access to the event, but was not designed to
receive a reference to it as an argument. Note that this method should
only be invoked from an application's event dispatching thread. If this
method is invoked from another thread, null will be returned.

**Returns:**
- the event currently being dispatched, or null if this method is
invoked on a thread other than an event dispatching thread

**Since:**
- 1.4

---

#### public void push​(
EventQueue
newEventQueue)

Replaces the existing

EventQueue

with the specified one.
Any pending events are transferred to the new

EventQueue

for processing by it.

**Parameters:**
- newEventQueue

- an

EventQueue

(or subclass thereof) instance to be use

**Throws:**
- NullPointerException

- if

newEventQueue

is

null

**See Also:**
- pop()

**Since:**
- 1.2

---

#### protected void pop()
throws
EmptyStackException

Stops dispatching events using this

EventQueue

.
Any pending events are transferred to the previous

EventQueue

for processing.

Warning: To avoid deadlock, do not declare this method
synchronized in a subclass.

**Throws:**
- EmptyStackException

- if no previous push was made
on this

EventQueue

**See Also:**
- push(java.awt.EventQueue)

**Since:**
- 1.2

---

#### public
SecondaryLoop
createSecondaryLoop()

Creates a new

secondary loop

associated with this
event queue. Use the

SecondaryLoop.enter()

and

SecondaryLoop.exit()

methods to start and stop the
event loop and dispatch the events from this queue.

**Returns:**
- secondaryLoop A new secondary loop object, which can
be used to launch a new nested event
loop and dispatch events from this queue

**See Also:**
- SecondaryLoop.enter()

,

SecondaryLoop.exit()

**Since:**
- 1.7

---

#### public static boolean isDispatchThread()

Returns true if the calling thread is

the current AWT EventQueue

's
dispatch thread. Use this method to ensure that a particular
task is being executed (or not being) there.

Note: use the

invokeLater(java.lang.Runnable)

or

invokeAndWait(java.lang.Runnable)

methods to execute a task in

the current AWT EventQueue

's
dispatch thread.

**Returns:**
- true if running in

the current AWT EventQueue

's
dispatch thread

**See Also:**
- invokeLater(java.lang.Runnable)

,

invokeAndWait(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

**Since:**
- 1.2

---

#### public static void invokeLater​(
Runnable
runnable)

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.

**Parameters:**
- runnable

- the

Runnable

whose

run

method should be executed
asynchronously in the

event dispatch thread

of

the system EventQueue

**See Also:**
- invokeAndWait(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

,

isDispatchThread()

**Since:**
- 1.2

---

#### public static void invokeAndWait​(
Runnable
runnable)
throws
InterruptedException
,

InvocationTargetException

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.
The call blocks until this has happened. This method
will throw an Error if called from the

event dispatcher thread

.

**Parameters:**
- runnable

- the

Runnable

whose

run

method should be executed
synchronously in the

event dispatch thread

of

the system EventQueue

**Throws:**
- InterruptedException

- if any thread has
interrupted this thread
- InvocationTargetException

- if an throwable is thrown
when running

runnable

**See Also:**
- invokeLater(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

,

isDispatchThread()

**Since:**
- 1.2

---

### Additional Sections

#### Class EventQueue

java.lang.Object

- java.awt.EventQueue

java.awt.EventQueue

```java
public class
EventQueue

extends
Object
```

EventQueue

is a platform-independent class
that queues events, both from the underlying peer classes
and from trusted application classes.

It encapsulates asynchronous event dispatch machinery which
extracts events from the queue and dispatches them by calling

dispatchEvent(AWTEvent)

method
on this

EventQueue

with the event to be dispatched
as an argument. The particular behavior of this machinery is
implementation-dependent. The only requirements are that events
which were actually enqueued to this queue (note that events
being posted to the

EventQueue

can be coalesced)
are dispatched:

Some browsers partition applets in different code bases into
separate contexts, and establish walls between these contexts.
In such a scenario, there will be one

EventQueue

per context. Other browsers place all applets into the same
context, implying that there will be only a single, global

EventQueue

for all applets. This behavior is
implementation-dependent. Consult your browser's documentation
for more information.

For information on the threading issues of the event dispatch
machinery, see

AWT Threading Issues

.

**Since:** 1.1

public class

EventQueue

extends

Object

EventQueue

is a platform-independent class
that queues events, both from the underlying peer classes
and from trusted application classes.

It encapsulates asynchronous event dispatch machinery which
extracts events from the queue and dispatches them by calling

dispatchEvent(AWTEvent)

method
on this

EventQueue

with the event to be dispatched
as an argument. The particular behavior of this machinery is
implementation-dependent. The only requirements are that events
which were actually enqueued to this queue (note that events
being posted to the

EventQueue

can be coalesced)
are dispatched:

Some browsers partition applets in different code bases into
separate contexts, and establish walls between these contexts.
In such a scenario, there will be one

EventQueue

per context. Other browsers place all applets into the same
context, implying that there will be only a single, global

EventQueue

for all applets. This behavior is
implementation-dependent. Consult your browser's documentation
for more information.

For information on the threading issues of the event dispatch
machinery, see

AWT Threading Issues

.

It encapsulates asynchronous event dispatch machinery which
extracts events from the queue and dispatches them by calling

dispatchEvent(AWTEvent)

method
on this

EventQueue

with the event to be dispatched
as an argument. The particular behavior of this machinery is
implementation-dependent. The only requirements are that events
which were actually enqueued to this queue (note that events
being posted to the

EventQueue

can be coalesced)
are dispatched:

Some browsers partition applets in different code bases into
separate contexts, and establish walls between these contexts.
In such a scenario, there will be one

EventQueue

per context. Other browsers place all applets into the same
context, implying that there will be only a single, global

EventQueue

for all applets. This behavior is
implementation-dependent. Consult your browser's documentation
for more information.

For information on the threading issues of the event dispatch
machinery, see

AWT Threading Issues

.

Some browsers partition applets in different code bases into
separate contexts, and establish walls between these contexts.
In such a scenario, there will be one

EventQueue

per context. Other browsers place all applets into the same
context, implying that there will be only a single, global

EventQueue

for all applets. This behavior is
implementation-dependent. Consult your browser's documentation
for more information.

For information on the threading issues of the event dispatch
machinery, see

AWT Threading Issues

.

For information on the threading issues of the event dispatch
machinery, see

AWT Threading Issues

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EventQueue

()

Initializes a new instance of

EventQueue

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SecondaryLoop

createSecondaryLoop

()

Creates a new

secondary loop

associated with this
event queue.

protected void

dispatchEvent

​(

AWTEvent

event)

Dispatches an event.

static

AWTEvent

getCurrentEvent

()

Returns the event currently being dispatched by the

EventQueue

associated with the calling thread.

static long

getMostRecentEventTime

()

Returns the timestamp of the most recent event that had a timestamp, and
that was dispatched from the

EventQueue

associated with the
calling thread.

AWTEvent

getNextEvent

()

Removes an event from the

EventQueue

and
returns it.

static void

invokeAndWait

​(

Runnable

runnable)

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.

static void

invokeLater

​(

Runnable

runnable)

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.

static boolean

isDispatchThread

()

Returns true if the calling thread is

the current AWT EventQueue

's
dispatch thread.

AWTEvent

peekEvent

()

Returns the first event on the

EventQueue

without removing it.

AWTEvent

peekEvent

​(int id)

Returns the first event with the specified id, if any.

protected void

pop

()

Stops dispatching events using this

EventQueue

.

void

postEvent

​(

AWTEvent

theEvent)

Posts a 1.1-style event to the

EventQueue

.

void

push

​(

EventQueue

newEventQueue)

Replaces the existing

EventQueue

with the specified one.

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

EventQueue

()

Initializes a new instance of

EventQueue

.

---

#### Constructor Summary

Initializes a new instance of

EventQueue

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SecondaryLoop

createSecondaryLoop

()

Creates a new

secondary loop

associated with this
event queue.

protected void

dispatchEvent

​(

AWTEvent

event)

Dispatches an event.

static

AWTEvent

getCurrentEvent

()

Returns the event currently being dispatched by the

EventQueue

associated with the calling thread.

static long

getMostRecentEventTime

()

Returns the timestamp of the most recent event that had a timestamp, and
that was dispatched from the

EventQueue

associated with the
calling thread.

AWTEvent

getNextEvent

()

Removes an event from the

EventQueue

and
returns it.

static void

invokeAndWait

​(

Runnable

runnable)

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.

static void

invokeLater

​(

Runnable

runnable)

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.

static boolean

isDispatchThread

()

Returns true if the calling thread is

the current AWT EventQueue

's
dispatch thread.

AWTEvent

peekEvent

()

Returns the first event on the

EventQueue

without removing it.

AWTEvent

peekEvent

​(int id)

Returns the first event with the specified id, if any.

protected void

pop

()

Stops dispatching events using this

EventQueue

.

void

postEvent

​(

AWTEvent

theEvent)

Posts a 1.1-style event to the

EventQueue

.

void

push

​(

EventQueue

newEventQueue)

Replaces the existing

EventQueue

with the specified one.

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

Creates a new

secondary loop

associated with this
event queue.

Dispatches an event.

Returns the event currently being dispatched by the

EventQueue

associated with the calling thread.

Returns the timestamp of the most recent event that had a timestamp, and
that was dispatched from the

EventQueue

associated with the
calling thread.

Removes an event from the

EventQueue

and
returns it.

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.

Returns true if the calling thread is

the current AWT EventQueue

's
dispatch thread.

Returns the first event on the

EventQueue

without removing it.

Returns the first event with the specified id, if any.

Stops dispatching events using this

EventQueue

.

Posts a 1.1-style event to the

EventQueue

.

Replaces the existing

EventQueue

with the specified one.

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

- EventQueue

```java
public EventQueue()
```

Initializes a new instance of

EventQueue

.

============ METHOD DETAIL ==========

- Method Detail

- postEvent

```java
public void postEvent​(
AWTEvent
theEvent)
```

Posts a 1.1-style event to the

EventQueue

.
If there is an existing event on the queue with the same ID
and event source, the source

Component

's

coalesceEvents

method will be called.

**Parameters:** theEvent

- an instance of

java.awt.AWTEvent

,
or a subclass of it
**Throws:** NullPointerException

- if

theEvent

is

null

- getNextEvent

```java
public
AWTEvent
getNextEvent()
throws
InterruptedException
```

Removes an event from the

EventQueue

and
returns it. This method will block until an event has
been posted by another thread.

**Returns:** the next

AWTEvent
**Throws:** InterruptedException

- if any thread has interrupted this thread

- peekEvent

```java
public
AWTEvent
peekEvent()
```

Returns the first event on the

EventQueue

without removing it.

**Returns:** the first event

- peekEvent

```java
public
AWTEvent
peekEvent​(int id)
```

Returns the first event with the specified id, if any.

**Parameters:** id

- the id of the type of event desired
**Returns:** the first event of the specified id or

null

if there is no such event

- dispatchEvent

```java
protected void dispatchEvent​(
AWTEvent
event)
```

Dispatches an event. The manner in which the event is
dispatched depends upon the type of the event and the
type of the event's source object:

Event types, source types, and dispatch methods

Event Type

Source Type

Dispatched To

ActiveEvent

Any

event.dispatch()

Other

Component

source.dispatchEvent(AWTEvent)

Other

MenuComponent

source.dispatchEvent(AWTEvent)

Other

Other

No action (ignored)

**Parameters:** event

- an instance of

java.awt.AWTEvent

,
or a subclass of it
**Throws:** NullPointerException

- if

event

is

null
**Since:** 1.2

- getMostRecentEventTime

```java
public static long getMostRecentEventTime()
```

Returns the timestamp of the most recent event that had a timestamp, and
that was dispatched from the

EventQueue

associated with the
calling thread. If an event with a timestamp is currently being
dispatched, its timestamp will be returned. If no events have yet
been dispatched, the EventQueue's initialization time will be
returned instead.In the current version of
the JDK, only

InputEvent

s,

ActionEvent

s, and

InvocationEvent

s have
timestamps; however, future versions of the JDK may add timestamps to
additional event types. Note that this method should only be invoked
from an application's

event dispatching thread

.
If this method is
invoked from another thread, the current system time (as reported by

System.currentTimeMillis()

) will be returned instead.

**Returns:** the timestamp of the last

InputEvent

,

ActionEvent

, or

InvocationEvent

to be
dispatched, or

System.currentTimeMillis()

if this
method is invoked on a thread other than an event dispatching
thread
**Since:** 1.4
**See Also:** InputEvent.getWhen()

,

ActionEvent.getWhen()

,

InvocationEvent.getWhen()

,

isDispatchThread()

- getCurrentEvent

```java
public static
AWTEvent
getCurrentEvent()
```

Returns the event currently being dispatched by the

EventQueue

associated with the calling thread. This is
useful if a method needs access to the event, but was not designed to
receive a reference to it as an argument. Note that this method should
only be invoked from an application's event dispatching thread. If this
method is invoked from another thread, null will be returned.

**Returns:** the event currently being dispatched, or null if this method is
invoked on a thread other than an event dispatching thread
**Since:** 1.4

- push

```java
public void push​(
EventQueue
newEventQueue)
```

Replaces the existing

EventQueue

with the specified one.
Any pending events are transferred to the new

EventQueue

for processing by it.

**Parameters:** newEventQueue

- an

EventQueue

(or subclass thereof) instance to be use
**Throws:** NullPointerException

- if

newEventQueue

is

null
**Since:** 1.2
**See Also:** pop()

- pop

```java
protected void pop()
throws
EmptyStackException
```

Stops dispatching events using this

EventQueue

.
Any pending events are transferred to the previous

EventQueue

for processing.

Warning: To avoid deadlock, do not declare this method
synchronized in a subclass.

**Throws:** EmptyStackException

- if no previous push was made
on this

EventQueue
**Since:** 1.2
**See Also:** push(java.awt.EventQueue)

- createSecondaryLoop

```java
public
SecondaryLoop
createSecondaryLoop()
```

Creates a new

secondary loop

associated with this
event queue. Use the

SecondaryLoop.enter()

and

SecondaryLoop.exit()

methods to start and stop the
event loop and dispatch the events from this queue.

**Returns:** secondaryLoop A new secondary loop object, which can
be used to launch a new nested event
loop and dispatch events from this queue
**Since:** 1.7
**See Also:** SecondaryLoop.enter()

,

SecondaryLoop.exit()

- isDispatchThread

```java
public static boolean isDispatchThread()
```

Returns true if the calling thread is

the current AWT EventQueue

's
dispatch thread. Use this method to ensure that a particular
task is being executed (or not being) there.

Note: use the

invokeLater(java.lang.Runnable)

or

invokeAndWait(java.lang.Runnable)

methods to execute a task in

the current AWT EventQueue

's
dispatch thread.

**Returns:** true if running in

the current AWT EventQueue

's
dispatch thread
**Since:** 1.2
**See Also:** invokeLater(java.lang.Runnable)

,

invokeAndWait(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

- invokeLater

```java
public static void invokeLater​(
Runnable
runnable)
```

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.

**Parameters:** runnable

- the

Runnable

whose

run

method should be executed
asynchronously in the

event dispatch thread

of

the system EventQueue
**Since:** 1.2
**See Also:** invokeAndWait(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

,

isDispatchThread()

- invokeAndWait

```java
public static void invokeAndWait​(
Runnable
runnable)
throws
InterruptedException
,

InvocationTargetException
```

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.
The call blocks until this has happened. This method
will throw an Error if called from the

event dispatcher thread

.

**Parameters:** runnable

- the

Runnable

whose

run

method should be executed
synchronously in the

event dispatch thread

of

the system EventQueue
**Throws:** InterruptedException

- if any thread has
interrupted this thread
**Throws:** InvocationTargetException

- if an throwable is thrown
when running

runnable
**Since:** 1.2
**See Also:** invokeLater(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

,

isDispatchThread()

Constructor Detail

- EventQueue

```java
public EventQueue()
```

Initializes a new instance of

EventQueue

.

---

#### Constructor Detail

EventQueue

```java
public EventQueue()
```

Initializes a new instance of

EventQueue

.

---

#### EventQueue

public EventQueue()

Initializes a new instance of

EventQueue

.

Method Detail

- postEvent

```java
public void postEvent​(
AWTEvent
theEvent)
```

Posts a 1.1-style event to the

EventQueue

.
If there is an existing event on the queue with the same ID
and event source, the source

Component

's

coalesceEvents

method will be called.

**Parameters:** theEvent

- an instance of

java.awt.AWTEvent

,
or a subclass of it
**Throws:** NullPointerException

- if

theEvent

is

null

- getNextEvent

```java
public
AWTEvent
getNextEvent()
throws
InterruptedException
```

Removes an event from the

EventQueue

and
returns it. This method will block until an event has
been posted by another thread.

**Returns:** the next

AWTEvent
**Throws:** InterruptedException

- if any thread has interrupted this thread

- peekEvent

```java
public
AWTEvent
peekEvent()
```

Returns the first event on the

EventQueue

without removing it.

**Returns:** the first event

- peekEvent

```java
public
AWTEvent
peekEvent​(int id)
```

Returns the first event with the specified id, if any.

**Parameters:** id

- the id of the type of event desired
**Returns:** the first event of the specified id or

null

if there is no such event

- dispatchEvent

```java
protected void dispatchEvent​(
AWTEvent
event)
```

Dispatches an event. The manner in which the event is
dispatched depends upon the type of the event and the
type of the event's source object:

Event types, source types, and dispatch methods

Event Type

Source Type

Dispatched To

ActiveEvent

Any

event.dispatch()

Other

Component

source.dispatchEvent(AWTEvent)

Other

MenuComponent

source.dispatchEvent(AWTEvent)

Other

Other

No action (ignored)

**Parameters:** event

- an instance of

java.awt.AWTEvent

,
or a subclass of it
**Throws:** NullPointerException

- if

event

is

null
**Since:** 1.2

- getMostRecentEventTime

```java
public static long getMostRecentEventTime()
```

Returns the timestamp of the most recent event that had a timestamp, and
that was dispatched from the

EventQueue

associated with the
calling thread. If an event with a timestamp is currently being
dispatched, its timestamp will be returned. If no events have yet
been dispatched, the EventQueue's initialization time will be
returned instead.In the current version of
the JDK, only

InputEvent

s,

ActionEvent

s, and

InvocationEvent

s have
timestamps; however, future versions of the JDK may add timestamps to
additional event types. Note that this method should only be invoked
from an application's

event dispatching thread

.
If this method is
invoked from another thread, the current system time (as reported by

System.currentTimeMillis()

) will be returned instead.

**Returns:** the timestamp of the last

InputEvent

,

ActionEvent

, or

InvocationEvent

to be
dispatched, or

System.currentTimeMillis()

if this
method is invoked on a thread other than an event dispatching
thread
**Since:** 1.4
**See Also:** InputEvent.getWhen()

,

ActionEvent.getWhen()

,

InvocationEvent.getWhen()

,

isDispatchThread()

- getCurrentEvent

```java
public static
AWTEvent
getCurrentEvent()
```

Returns the event currently being dispatched by the

EventQueue

associated with the calling thread. This is
useful if a method needs access to the event, but was not designed to
receive a reference to it as an argument. Note that this method should
only be invoked from an application's event dispatching thread. If this
method is invoked from another thread, null will be returned.

**Returns:** the event currently being dispatched, or null if this method is
invoked on a thread other than an event dispatching thread
**Since:** 1.4

- push

```java
public void push​(
EventQueue
newEventQueue)
```

Replaces the existing

EventQueue

with the specified one.
Any pending events are transferred to the new

EventQueue

for processing by it.

**Parameters:** newEventQueue

- an

EventQueue

(or subclass thereof) instance to be use
**Throws:** NullPointerException

- if

newEventQueue

is

null
**Since:** 1.2
**See Also:** pop()

- pop

```java
protected void pop()
throws
EmptyStackException
```

Stops dispatching events using this

EventQueue

.
Any pending events are transferred to the previous

EventQueue

for processing.

Warning: To avoid deadlock, do not declare this method
synchronized in a subclass.

**Throws:** EmptyStackException

- if no previous push was made
on this

EventQueue
**Since:** 1.2
**See Also:** push(java.awt.EventQueue)

- createSecondaryLoop

```java
public
SecondaryLoop
createSecondaryLoop()
```

Creates a new

secondary loop

associated with this
event queue. Use the

SecondaryLoop.enter()

and

SecondaryLoop.exit()

methods to start and stop the
event loop and dispatch the events from this queue.

**Returns:** secondaryLoop A new secondary loop object, which can
be used to launch a new nested event
loop and dispatch events from this queue
**Since:** 1.7
**See Also:** SecondaryLoop.enter()

,

SecondaryLoop.exit()

- isDispatchThread

```java
public static boolean isDispatchThread()
```

Returns true if the calling thread is

the current AWT EventQueue

's
dispatch thread. Use this method to ensure that a particular
task is being executed (or not being) there.

Note: use the

invokeLater(java.lang.Runnable)

or

invokeAndWait(java.lang.Runnable)

methods to execute a task in

the current AWT EventQueue

's
dispatch thread.

**Returns:** true if running in

the current AWT EventQueue

's
dispatch thread
**Since:** 1.2
**See Also:** invokeLater(java.lang.Runnable)

,

invokeAndWait(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

- invokeLater

```java
public static void invokeLater​(
Runnable
runnable)
```

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.

**Parameters:** runnable

- the

Runnable

whose

run

method should be executed
asynchronously in the

event dispatch thread

of

the system EventQueue
**Since:** 1.2
**See Also:** invokeAndWait(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

,

isDispatchThread()

- invokeAndWait

```java
public static void invokeAndWait​(
Runnable
runnable)
throws
InterruptedException
,

InvocationTargetException
```

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.
The call blocks until this has happened. This method
will throw an Error if called from the

event dispatcher thread

.

**Parameters:** runnable

- the

Runnable

whose

run

method should be executed
synchronously in the

event dispatch thread

of

the system EventQueue
**Throws:** InterruptedException

- if any thread has
interrupted this thread
**Throws:** InvocationTargetException

- if an throwable is thrown
when running

runnable
**Since:** 1.2
**See Also:** invokeLater(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

,

isDispatchThread()

---

#### Method Detail

postEvent

```java
public void postEvent​(
AWTEvent
theEvent)
```

Posts a 1.1-style event to the

EventQueue

.
If there is an existing event on the queue with the same ID
and event source, the source

Component

's

coalesceEvents

method will be called.

**Parameters:** theEvent

- an instance of

java.awt.AWTEvent

,
or a subclass of it
**Throws:** NullPointerException

- if

theEvent

is

null

---

#### postEvent

public void postEvent​(

AWTEvent

theEvent)

Posts a 1.1-style event to the

EventQueue

.
If there is an existing event on the queue with the same ID
and event source, the source

Component

's

coalesceEvents

method will be called.

getNextEvent

```java
public
AWTEvent
getNextEvent()
throws
InterruptedException
```

Removes an event from the

EventQueue

and
returns it. This method will block until an event has
been posted by another thread.

**Returns:** the next

AWTEvent
**Throws:** InterruptedException

- if any thread has interrupted this thread

---

#### getNextEvent

public

AWTEvent

getNextEvent()
throws

InterruptedException

Removes an event from the

EventQueue

and
returns it. This method will block until an event has
been posted by another thread.

peekEvent

```java
public
AWTEvent
peekEvent()
```

Returns the first event on the

EventQueue

without removing it.

**Returns:** the first event

---

#### peekEvent

public

AWTEvent

peekEvent()

Returns the first event on the

EventQueue

without removing it.

peekEvent

```java
public
AWTEvent
peekEvent​(int id)
```

Returns the first event with the specified id, if any.

**Parameters:** id

- the id of the type of event desired
**Returns:** the first event of the specified id or

null

if there is no such event

---

#### peekEvent

public

AWTEvent

peekEvent​(int id)

Returns the first event with the specified id, if any.

dispatchEvent

```java
protected void dispatchEvent​(
AWTEvent
event)
```

Dispatches an event. The manner in which the event is
dispatched depends upon the type of the event and the
type of the event's source object:

Event types, source types, and dispatch methods

Event Type

Source Type

Dispatched To

ActiveEvent

Any

event.dispatch()

Other

Component

source.dispatchEvent(AWTEvent)

Other

MenuComponent

source.dispatchEvent(AWTEvent)

Other

Other

No action (ignored)

**Parameters:** event

- an instance of

java.awt.AWTEvent

,
or a subclass of it
**Throws:** NullPointerException

- if

event

is

null
**Since:** 1.2

---

#### dispatchEvent

protected void dispatchEvent​(

AWTEvent

event)

Dispatches an event. The manner in which the event is
dispatched depends upon the type of the event and the
type of the event's source object:

Event types, source types, and dispatch methods

Event Type

Source Type

Dispatched To

ActiveEvent

Any

event.dispatch()

Other

Component

source.dispatchEvent(AWTEvent)

Other

MenuComponent

source.dispatchEvent(AWTEvent)

Other

Other

No action (ignored)

getMostRecentEventTime

```java
public static long getMostRecentEventTime()
```

Returns the timestamp of the most recent event that had a timestamp, and
that was dispatched from the

EventQueue

associated with the
calling thread. If an event with a timestamp is currently being
dispatched, its timestamp will be returned. If no events have yet
been dispatched, the EventQueue's initialization time will be
returned instead.In the current version of
the JDK, only

InputEvent

s,

ActionEvent

s, and

InvocationEvent

s have
timestamps; however, future versions of the JDK may add timestamps to
additional event types. Note that this method should only be invoked
from an application's

event dispatching thread

.
If this method is
invoked from another thread, the current system time (as reported by

System.currentTimeMillis()

) will be returned instead.

**Returns:** the timestamp of the last

InputEvent

,

ActionEvent

, or

InvocationEvent

to be
dispatched, or

System.currentTimeMillis()

if this
method is invoked on a thread other than an event dispatching
thread
**Since:** 1.4
**See Also:** InputEvent.getWhen()

,

ActionEvent.getWhen()

,

InvocationEvent.getWhen()

,

isDispatchThread()

---

#### getMostRecentEventTime

public static long getMostRecentEventTime()

Returns the timestamp of the most recent event that had a timestamp, and
that was dispatched from the

EventQueue

associated with the
calling thread. If an event with a timestamp is currently being
dispatched, its timestamp will be returned. If no events have yet
been dispatched, the EventQueue's initialization time will be
returned instead.In the current version of
the JDK, only

InputEvent

s,

ActionEvent

s, and

InvocationEvent

s have
timestamps; however, future versions of the JDK may add timestamps to
additional event types. Note that this method should only be invoked
from an application's

event dispatching thread

.
If this method is
invoked from another thread, the current system time (as reported by

System.currentTimeMillis()

) will be returned instead.

getCurrentEvent

```java
public static
AWTEvent
getCurrentEvent()
```

Returns the event currently being dispatched by the

EventQueue

associated with the calling thread. This is
useful if a method needs access to the event, but was not designed to
receive a reference to it as an argument. Note that this method should
only be invoked from an application's event dispatching thread. If this
method is invoked from another thread, null will be returned.

**Returns:** the event currently being dispatched, or null if this method is
invoked on a thread other than an event dispatching thread
**Since:** 1.4

---

#### getCurrentEvent

public static

AWTEvent

getCurrentEvent()

Returns the event currently being dispatched by the

EventQueue

associated with the calling thread. This is
useful if a method needs access to the event, but was not designed to
receive a reference to it as an argument. Note that this method should
only be invoked from an application's event dispatching thread. If this
method is invoked from another thread, null will be returned.

push

```java
public void push​(
EventQueue
newEventQueue)
```

Replaces the existing

EventQueue

with the specified one.
Any pending events are transferred to the new

EventQueue

for processing by it.

**Parameters:** newEventQueue

- an

EventQueue

(or subclass thereof) instance to be use
**Throws:** NullPointerException

- if

newEventQueue

is

null
**Since:** 1.2
**See Also:** pop()

---

#### push

public void push​(

EventQueue

newEventQueue)

Replaces the existing

EventQueue

with the specified one.
Any pending events are transferred to the new

EventQueue

for processing by it.

pop

```java
protected void pop()
throws
EmptyStackException
```

Stops dispatching events using this

EventQueue

.
Any pending events are transferred to the previous

EventQueue

for processing.

Warning: To avoid deadlock, do not declare this method
synchronized in a subclass.

**Throws:** EmptyStackException

- if no previous push was made
on this

EventQueue
**Since:** 1.2
**See Also:** push(java.awt.EventQueue)

---

#### pop

protected void pop()
throws

EmptyStackException

Stops dispatching events using this

EventQueue

.
Any pending events are transferred to the previous

EventQueue

for processing.

Warning: To avoid deadlock, do not declare this method
synchronized in a subclass.

Warning: To avoid deadlock, do not declare this method
synchronized in a subclass.

createSecondaryLoop

```java
public
SecondaryLoop
createSecondaryLoop()
```

Creates a new

secondary loop

associated with this
event queue. Use the

SecondaryLoop.enter()

and

SecondaryLoop.exit()

methods to start and stop the
event loop and dispatch the events from this queue.

**Returns:** secondaryLoop A new secondary loop object, which can
be used to launch a new nested event
loop and dispatch events from this queue
**Since:** 1.7
**See Also:** SecondaryLoop.enter()

,

SecondaryLoop.exit()

---

#### createSecondaryLoop

public

SecondaryLoop

createSecondaryLoop()

Creates a new

secondary loop

associated with this
event queue. Use the

SecondaryLoop.enter()

and

SecondaryLoop.exit()

methods to start and stop the
event loop and dispatch the events from this queue.

isDispatchThread

```java
public static boolean isDispatchThread()
```

Returns true if the calling thread is

the current AWT EventQueue

's
dispatch thread. Use this method to ensure that a particular
task is being executed (or not being) there.

Note: use the

invokeLater(java.lang.Runnable)

or

invokeAndWait(java.lang.Runnable)

methods to execute a task in

the current AWT EventQueue

's
dispatch thread.

**Returns:** true if running in

the current AWT EventQueue

's
dispatch thread
**Since:** 1.2
**See Also:** invokeLater(java.lang.Runnable)

,

invokeAndWait(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

---

#### isDispatchThread

public static boolean isDispatchThread()

Returns true if the calling thread is

the current AWT EventQueue

's
dispatch thread. Use this method to ensure that a particular
task is being executed (or not being) there.

Note: use the

invokeLater(java.lang.Runnable)

or

invokeAndWait(java.lang.Runnable)

methods to execute a task in

the current AWT EventQueue

's
dispatch thread.

Note: use the

invokeLater(java.lang.Runnable)

or

invokeAndWait(java.lang.Runnable)

methods to execute a task in

the current AWT EventQueue

's
dispatch thread.

invokeLater

```java
public static void invokeLater​(
Runnable
runnable)
```

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.

**Parameters:** runnable

- the

Runnable

whose

run

method should be executed
asynchronously in the

event dispatch thread

of

the system EventQueue
**Since:** 1.2
**See Also:** invokeAndWait(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

,

isDispatchThread()

---

#### invokeLater

public static void invokeLater​(

Runnable

runnable)

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.

invokeAndWait

```java
public static void invokeAndWait​(
Runnable
runnable)
throws
InterruptedException
,

InvocationTargetException
```

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.
The call blocks until this has happened. This method
will throw an Error if called from the

event dispatcher thread

.

**Parameters:** runnable

- the

Runnable

whose

run

method should be executed
synchronously in the

event dispatch thread

of

the system EventQueue
**Throws:** InterruptedException

- if any thread has
interrupted this thread
**Throws:** InvocationTargetException

- if an throwable is thrown
when running

runnable
**Since:** 1.2
**See Also:** invokeLater(java.lang.Runnable)

,

Toolkit.getSystemEventQueue()

,

isDispatchThread()

---

#### invokeAndWait

public static void invokeAndWait​(

Runnable

runnable)
throws

InterruptedException

,

InvocationTargetException

Causes

runnable

to have its

run

method called in the

dispatch thread

of

the system EventQueue

.
This will happen after all pending events are processed.
The call blocks until this has happened. This method
will throw an Error if called from the

event dispatcher thread

.

---

