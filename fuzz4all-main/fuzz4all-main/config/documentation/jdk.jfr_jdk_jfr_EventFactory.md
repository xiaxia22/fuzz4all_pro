# Class EventFactory

**Source:** `jdk.jfr\jdk\jfr\EventFactory.html`

### Class Description

```java
public final class
EventFactory

extends
Object
```

Class for defining an event at runtime.

It's highly recommended that the event is defined at compile time, if the
field layout is known, so the Java Virtual Machine (JVM) can optimize the
code, possibly remove all instrumentation if Flight Recorder is inactive or
if the enabled setting for this event is set to

false

.

To define an event at compile time, see

Event

.

The following example shows how to implement a dynamic

Event

class.

```java
List<ValueDescriptor> fields = new ArrayList<>();
List<AnnotationElement> messageAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Message"));
fields.add(new ValueDescriptor(String.class, "message", messageAnnotations));
List<AnnotationElement> numberAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Number"));
fields.add(new ValueDescriptor(int.class, "number", numberAnnotations));

String[] category = { "Example", "Getting Started" };
List<AnnotationElement> eventAnnotations = new ArrayList<>();
eventAnnotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld"));
eventAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
eventAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));
eventAnnotations.add(new AnnotationElement(Category.class, category));

EventFactory f = EventFactory.create(eventAnnotations, fields);

Event event = f.newEvent();
event.set(0, "hello, world!");
event.set(1, 4711);
event.commit();
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
EventFactory
create​(
List
<
AnnotationElement
> annotationElements,

List
<
ValueDescriptor
> fields)

Creates an

EventFactory

object.

The order of the value descriptors specifies the index to use when setting
event values.

**Parameters:**
- annotationElements

- list of annotation elements that describes the
annotations on the event, not

null
- fields

- list of descriptors that describes the fields of the event, not

null

**Returns:**
- event factory, not

null

**Throws:**
- IllegalArgumentException

- if the input is not valid. For example,
input might not be valid if the field type or name is not valid in
the Java language or an annotation element references a type that
can't be found.
- SecurityException

- if a security manager exists and the caller does
not have

FlightRecorderPermission("registerEvent")

**See Also:**
- Event.set(int, Object)

---

#### public
Event
newEvent()

Instantiates an event, so it can be populated with data and written to the
Flight Recorder system.

Use the

Event.set(int, Object)

method to set a value.

**Returns:**
- an event instance, not

null

---

#### public
EventType
getEventType()

Returns the event type that is associated with this event factory.

**Returns:**
- event type that is associated with this event factory, not

null

**Throws:**
- IllegalStateException

- if the event factory is created with
the

Registered(false)

annotation and the event class is not
manually registered before the invocation of this method

---

#### public void register()

Registers an unregistered event.

By default, the event class associated with this event factory is registered
when the event factory is created, unless the event has the

Registered

annotation.

A registered event class can write data to Flight Recorder and event metadata
can be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is already registered,
the call to this method is ignored.

**Throws:**
- SecurityException

- if a security manager exists and the caller
does not have

FlightRecorderPermission("registerEvent")

**See Also:**
- Registered

,

FlightRecorder.register(Class)

---

#### public void unregister()

Unregisters the event that is associated with this event factory.

A unregistered event class can't write data to Flight Recorder and event
metadata can't be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is not already
registered, the call to this method is ignored.

**Throws:**
- SecurityException

- if a security manager exists and the caller does
not have

FlightRecorderPermission("registerEvent")

**See Also:**
- Registered

,

FlightRecorder.unregister(Class)

---

### Additional Sections

#### Class EventFactory

java.lang.Object

- jdk.jfr.EventFactory

jdk.jfr.EventFactory

```java
public final class
EventFactory

extends
Object
```

Class for defining an event at runtime.

It's highly recommended that the event is defined at compile time, if the
field layout is known, so the Java Virtual Machine (JVM) can optimize the
code, possibly remove all instrumentation if Flight Recorder is inactive or
if the enabled setting for this event is set to

false

.

To define an event at compile time, see

Event

.

The following example shows how to implement a dynamic

Event

class.

```java
List<ValueDescriptor> fields = new ArrayList<>();
List<AnnotationElement> messageAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Message"));
fields.add(new ValueDescriptor(String.class, "message", messageAnnotations));
List<AnnotationElement> numberAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Number"));
fields.add(new ValueDescriptor(int.class, "number", numberAnnotations));

String[] category = { "Example", "Getting Started" };
List<AnnotationElement> eventAnnotations = new ArrayList<>();
eventAnnotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld"));
eventAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
eventAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));
eventAnnotations.add(new AnnotationElement(Category.class, category));

EventFactory f = EventFactory.create(eventAnnotations, fields);

Event event = f.newEvent();
event.set(0, "hello, world!");
event.set(1, 4711);
event.commit();
```

**Since:** 9

public final class

EventFactory

extends

Object

Class for defining an event at runtime.

It's highly recommended that the event is defined at compile time, if the
field layout is known, so the Java Virtual Machine (JVM) can optimize the
code, possibly remove all instrumentation if Flight Recorder is inactive or
if the enabled setting for this event is set to

false

.

To define an event at compile time, see

Event

.

The following example shows how to implement a dynamic

Event

class.

```java
List<ValueDescriptor> fields = new ArrayList<>();
List<AnnotationElement> messageAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Message"));
fields.add(new ValueDescriptor(String.class, "message", messageAnnotations));
List<AnnotationElement> numberAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Number"));
fields.add(new ValueDescriptor(int.class, "number", numberAnnotations));

String[] category = { "Example", "Getting Started" };
List<AnnotationElement> eventAnnotations = new ArrayList<>();
eventAnnotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld"));
eventAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
eventAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));
eventAnnotations.add(new AnnotationElement(Category.class, category));

EventFactory f = EventFactory.create(eventAnnotations, fields);

Event event = f.newEvent();
event.set(0, "hello, world!");
event.set(1, 4711);
event.commit();
```

It's highly recommended that the event is defined at compile time, if the
field layout is known, so the Java Virtual Machine (JVM) can optimize the
code, possibly remove all instrumentation if Flight Recorder is inactive or
if the enabled setting for this event is set to

false

.

To define an event at compile time, see

Event

.

The following example shows how to implement a dynamic

Event

class.

```java
List<ValueDescriptor> fields = new ArrayList<>();
List<AnnotationElement> messageAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Message"));
fields.add(new ValueDescriptor(String.class, "message", messageAnnotations));
List<AnnotationElement> numberAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Number"));
fields.add(new ValueDescriptor(int.class, "number", numberAnnotations));

String[] category = { "Example", "Getting Started" };
List<AnnotationElement> eventAnnotations = new ArrayList<>();
eventAnnotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld"));
eventAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
eventAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));
eventAnnotations.add(new AnnotationElement(Category.class, category));

EventFactory f = EventFactory.create(eventAnnotations, fields);

Event event = f.newEvent();
event.set(0, "hello, world!");
event.set(1, 4711);
event.commit();
```

To define an event at compile time, see

Event

.

The following example shows how to implement a dynamic

Event

class.

```java
List<ValueDescriptor> fields = new ArrayList<>();
List<AnnotationElement> messageAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Message"));
fields.add(new ValueDescriptor(String.class, "message", messageAnnotations));
List<AnnotationElement> numberAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Number"));
fields.add(new ValueDescriptor(int.class, "number", numberAnnotations));

String[] category = { "Example", "Getting Started" };
List<AnnotationElement> eventAnnotations = new ArrayList<>();
eventAnnotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld"));
eventAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
eventAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));
eventAnnotations.add(new AnnotationElement(Category.class, category));

EventFactory f = EventFactory.create(eventAnnotations, fields);

Event event = f.newEvent();
event.set(0, "hello, world!");
event.set(1, 4711);
event.commit();
```

The following example shows how to implement a dynamic

Event

class.

```java
List<ValueDescriptor> fields = new ArrayList<>();
List<AnnotationElement> messageAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Message"));
fields.add(new ValueDescriptor(String.class, "message", messageAnnotations));
List<AnnotationElement> numberAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Number"));
fields.add(new ValueDescriptor(int.class, "number", numberAnnotations));

String[] category = { "Example", "Getting Started" };
List<AnnotationElement> eventAnnotations = new ArrayList<>();
eventAnnotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld"));
eventAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
eventAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));
eventAnnotations.add(new AnnotationElement(Category.class, category));

EventFactory f = EventFactory.create(eventAnnotations, fields);

Event event = f.newEvent();
event.set(0, "hello, world!");
event.set(1, 4711);
event.commit();
```

List<ValueDescriptor> fields = new ArrayList<>();
List<AnnotationElement> messageAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Message"));
fields.add(new ValueDescriptor(String.class, "message", messageAnnotations));
List<AnnotationElement> numberAnnotations = Collections.singletonList(new AnnotationElement(Label.class, "Number"));
fields.add(new ValueDescriptor(int.class, "number", numberAnnotations));

String[] category = { "Example", "Getting Started" };
List<AnnotationElement> eventAnnotations = new ArrayList<>();
eventAnnotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld"));
eventAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
eventAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));
eventAnnotations.add(new AnnotationElement(Category.class, category));

EventFactory f = EventFactory.create(eventAnnotations, fields);

Event event = f.newEvent();
event.set(0, "hello, world!");
event.set(1, 4711);
event.commit();

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

EventFactory

create

​(

List

<

AnnotationElement

> annotationElements,

List

<

ValueDescriptor

> fields)

Creates an

EventFactory

object.

EventType

getEventType

()

Returns the event type that is associated with this event factory.

Event

newEvent

()

Instantiates an event, so it can be populated with data and written to the
Flight Recorder system.

void

register

()

Registers an unregistered event.

void

unregister

()

Unregisters the event that is associated with this event factory.

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

EventFactory

create

​(

List

<

AnnotationElement

> annotationElements,

List

<

ValueDescriptor

> fields)

Creates an

EventFactory

object.

EventType

getEventType

()

Returns the event type that is associated with this event factory.

Event

newEvent

()

Instantiates an event, so it can be populated with data and written to the
Flight Recorder system.

void

register

()

Registers an unregistered event.

void

unregister

()

Unregisters the event that is associated with this event factory.

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

Creates an

EventFactory

object.

Returns the event type that is associated with this event factory.

Instantiates an event, so it can be populated with data and written to the
Flight Recorder system.

Registers an unregistered event.

Unregisters the event that is associated with this event factory.

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

============ METHOD DETAIL ==========

- Method Detail

- create

```java
public static
EventFactory
create​(
List
<
AnnotationElement
> annotationElements,

List
<
ValueDescriptor
> fields)
```

Creates an

EventFactory

object.

The order of the value descriptors specifies the index to use when setting
event values.

**Parameters:** annotationElements

- list of annotation elements that describes the
annotations on the event, not

null
**Parameters:** fields

- list of descriptors that describes the fields of the event, not

null
**Returns:** event factory, not

null
**Throws:** IllegalArgumentException

- if the input is not valid. For example,
input might not be valid if the field type or name is not valid in
the Java language or an annotation element references a type that
can't be found.
**Throws:** SecurityException

- if a security manager exists and the caller does
not have

FlightRecorderPermission("registerEvent")
**See Also:** Event.set(int, Object)

- newEvent

```java
public
Event
newEvent()
```

Instantiates an event, so it can be populated with data and written to the
Flight Recorder system.

Use the

Event.set(int, Object)

method to set a value.

**Returns:** an event instance, not

null

- getEventType

```java
public
EventType
getEventType()
```

Returns the event type that is associated with this event factory.

**Returns:** event type that is associated with this event factory, not

null
**Throws:** IllegalStateException

- if the event factory is created with
the

Registered(false)

annotation and the event class is not
manually registered before the invocation of this method

- register

```java
public void register()
```

Registers an unregistered event.

By default, the event class associated with this event factory is registered
when the event factory is created, unless the event has the

Registered

annotation.

A registered event class can write data to Flight Recorder and event metadata
can be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is already registered,
the call to this method is ignored.

**Throws:** SecurityException

- if a security manager exists and the caller
does not have

FlightRecorderPermission("registerEvent")
**See Also:** Registered

,

FlightRecorder.register(Class)

- unregister

```java
public void unregister()
```

Unregisters the event that is associated with this event factory.

A unregistered event class can't write data to Flight Recorder and event
metadata can't be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is not already
registered, the call to this method is ignored.

**Throws:** SecurityException

- if a security manager exists and the caller does
not have

FlightRecorderPermission("registerEvent")
**See Also:** Registered

,

FlightRecorder.unregister(Class)

Method Detail

- create

```java
public static
EventFactory
create​(
List
<
AnnotationElement
> annotationElements,

List
<
ValueDescriptor
> fields)
```

Creates an

EventFactory

object.

The order of the value descriptors specifies the index to use when setting
event values.

**Parameters:** annotationElements

- list of annotation elements that describes the
annotations on the event, not

null
**Parameters:** fields

- list of descriptors that describes the fields of the event, not

null
**Returns:** event factory, not

null
**Throws:** IllegalArgumentException

- if the input is not valid. For example,
input might not be valid if the field type or name is not valid in
the Java language or an annotation element references a type that
can't be found.
**Throws:** SecurityException

- if a security manager exists and the caller does
not have

FlightRecorderPermission("registerEvent")
**See Also:** Event.set(int, Object)

- newEvent

```java
public
Event
newEvent()
```

Instantiates an event, so it can be populated with data and written to the
Flight Recorder system.

Use the

Event.set(int, Object)

method to set a value.

**Returns:** an event instance, not

null

- getEventType

```java
public
EventType
getEventType()
```

Returns the event type that is associated with this event factory.

**Returns:** event type that is associated with this event factory, not

null
**Throws:** IllegalStateException

- if the event factory is created with
the

Registered(false)

annotation and the event class is not
manually registered before the invocation of this method

- register

```java
public void register()
```

Registers an unregistered event.

By default, the event class associated with this event factory is registered
when the event factory is created, unless the event has the

Registered

annotation.

A registered event class can write data to Flight Recorder and event metadata
can be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is already registered,
the call to this method is ignored.

**Throws:** SecurityException

- if a security manager exists and the caller
does not have

FlightRecorderPermission("registerEvent")
**See Also:** Registered

,

FlightRecorder.register(Class)

- unregister

```java
public void unregister()
```

Unregisters the event that is associated with this event factory.

A unregistered event class can't write data to Flight Recorder and event
metadata can't be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is not already
registered, the call to this method is ignored.

**Throws:** SecurityException

- if a security manager exists and the caller does
not have

FlightRecorderPermission("registerEvent")
**See Also:** Registered

,

FlightRecorder.unregister(Class)

---

#### Method Detail

create

```java
public static
EventFactory
create​(
List
<
AnnotationElement
> annotationElements,

List
<
ValueDescriptor
> fields)
```

Creates an

EventFactory

object.

The order of the value descriptors specifies the index to use when setting
event values.

**Parameters:** annotationElements

- list of annotation elements that describes the
annotations on the event, not

null
**Parameters:** fields

- list of descriptors that describes the fields of the event, not

null
**Returns:** event factory, not

null
**Throws:** IllegalArgumentException

- if the input is not valid. For example,
input might not be valid if the field type or name is not valid in
the Java language or an annotation element references a type that
can't be found.
**Throws:** SecurityException

- if a security manager exists and the caller does
not have

FlightRecorderPermission("registerEvent")
**See Also:** Event.set(int, Object)

---

#### create

public static

EventFactory

create​(

List

<

AnnotationElement

> annotationElements,

List

<

ValueDescriptor

> fields)

Creates an

EventFactory

object.

The order of the value descriptors specifies the index to use when setting
event values.

The order of the value descriptors specifies the index to use when setting
event values.

newEvent

```java
public
Event
newEvent()
```

Instantiates an event, so it can be populated with data and written to the
Flight Recorder system.

Use the

Event.set(int, Object)

method to set a value.

**Returns:** an event instance, not

null

---

#### newEvent

public

Event

newEvent()

Instantiates an event, so it can be populated with data and written to the
Flight Recorder system.

Use the

Event.set(int, Object)

method to set a value.

Use the

Event.set(int, Object)

method to set a value.

getEventType

```java
public
EventType
getEventType()
```

Returns the event type that is associated with this event factory.

**Returns:** event type that is associated with this event factory, not

null
**Throws:** IllegalStateException

- if the event factory is created with
the

Registered(false)

annotation and the event class is not
manually registered before the invocation of this method

---

#### getEventType

public

EventType

getEventType()

Returns the event type that is associated with this event factory.

register

```java
public void register()
```

Registers an unregistered event.

By default, the event class associated with this event factory is registered
when the event factory is created, unless the event has the

Registered

annotation.

A registered event class can write data to Flight Recorder and event metadata
can be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is already registered,
the call to this method is ignored.

**Throws:** SecurityException

- if a security manager exists and the caller
does not have

FlightRecorderPermission("registerEvent")
**See Also:** Registered

,

FlightRecorder.register(Class)

---

#### register

public void register()

Registers an unregistered event.

By default, the event class associated with this event factory is registered
when the event factory is created, unless the event has the

Registered

annotation.

A registered event class can write data to Flight Recorder and event metadata
can be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is already registered,
the call to this method is ignored.

By default, the event class associated with this event factory is registered
when the event factory is created, unless the event has the

Registered

annotation.

A registered event class can write data to Flight Recorder and event metadata
can be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is already registered,
the call to this method is ignored.

A registered event class can write data to Flight Recorder and event metadata
can be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is already registered,
the call to this method is ignored.

If the event class associated with this event factory is already registered,
the call to this method is ignored.

unregister

```java
public void unregister()
```

Unregisters the event that is associated with this event factory.

A unregistered event class can't write data to Flight Recorder and event
metadata can't be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is not already
registered, the call to this method is ignored.

**Throws:** SecurityException

- if a security manager exists and the caller does
not have

FlightRecorderPermission("registerEvent")
**See Also:** Registered

,

FlightRecorder.unregister(Class)

---

#### unregister

public void unregister()

Unregisters the event that is associated with this event factory.

A unregistered event class can't write data to Flight Recorder and event
metadata can't be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is not already
registered, the call to this method is ignored.

A unregistered event class can't write data to Flight Recorder and event
metadata can't be obtained by invoking

FlightRecorder.getEventTypes()

.

If the event class associated with this event factory is not already
registered, the call to this method is ignored.

If the event class associated with this event factory is not already
registered, the call to this method is ignored.

---

