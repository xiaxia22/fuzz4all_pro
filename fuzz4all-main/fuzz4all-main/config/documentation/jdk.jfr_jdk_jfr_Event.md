# Class Event

**Source:** `jdk.jfr\jdk\jfr\Event.html`

### Class Description

```java
public abstract class
Event

extends jdk.internal.event.Event
```

Base class for events, to be subclassed in order to define events and their
fields.

The following example shows how to implement an

Event

class.

```java
import jdk.jfr.Event;
import jdk.jfr.Description;
import jdk.jfr.Label;

public class Example {

@Label("Hello World")
@Description("Helps programmer getting started")
static class HelloWorld extends Event {
@Label("Message")
String message;
}

public static void main(String... args) {
HelloWorld event = new HelloWorld();
event.message = "hello, world!";
event.commit();
}
}
```

After an event is allocated and its field members are populated, it can be
written to the Flight Recorder system by using the

#commit()

method.

By default, an event is enabled. To disable an event annotate the

Event

class with

@Enabled(false)

.

Supported field types are the Java primitives:

boolean

,

char

,

byte

,

short

,

int

,

long

,

float

, and

double

. Supported reference types are:

String

,

Thread

and

Class

. Arrays, enums, and other reference types are silently
ignored and not included. Fields that are of the supported types can be
excluded by using the transient modifier. Static fields, even of the
supported types, are not included.

Tools can visualize data in a meaningful way when annotations are used (for
example,

Label

,

Description

, and

Timespan

).
Annotations applied to an

Event

class or its fields are included if
they are present (indirectly, directly, or associated), have the

MetadataDefinition

annotation, and they do not contain enums, arrays,
or classes.

Gathering data to store in an event can be expensive. The

shouldCommit()

method can be used to verify whether an event
instance would actually be written to the system when the

Event#commit()commit

method is invoked. If

shouldCommit()

returns false, then those operations can be
avoided.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Event()

Sole constructor, for invocation by subclass constructors, typically
implicit.

---

### Method Details

#### public final void begin()

Starts the timing of this event.

**Overrides:**
- begin

in class

jdk.internal.event.Event

---

#### public final void end()

Ends the timing of this event.

The

end

method must be invoked after the

begin

method.

**Overrides:**
- end

in class

jdk.internal.event.Event

---

#### public final void commit()

Writes the field values, time stamp, and event duration to the Flight
Recorder system.

If the event starts with an invocation of the

begin

method, but does
not end with an explicit invocation of the

end

method, then the event
ends when the

commit

method is invoked.

**Overrides:**
- commit

in class

jdk.internal.event.Event

---

#### public final boolean isEnabled()

Returns

true

if at least one recording is running, and the
enabled setting for this event is set to

true

, otherwise

false

is returned.

**Overrides:**
- isEnabled

in class

jdk.internal.event.Event

**Returns:**
- true

if event is enabled,

false

otherwise

---

#### public final boolean shouldCommit()

Returns

true

if the enabled setting for this event is set to

true

and if the duration is within the threshold for the event,

false

otherwise. The threshold is the minimum threshold for all
running recordings.

**Overrides:**
- shouldCommit

in class

jdk.internal.event.Event

**Returns:**
- true

if the event can be written to the Flight Recorder
system,

false

otherwise

---

#### public final void set​(int index,

Object
value)

Sets a field value.

Applicable only if the event is dynamically defined using the

EventFactory

class.

The supplied

index

corresponds to the index of the

ValueDescriptor

object passed to the factory method of the

EventFactory

class.

**Overrides:**
- set

in class

jdk.internal.event.Event

**Parameters:**
- index

- the index of the field that is passed to

EventFactory#create(String, java.util.List, java.util.List)
- value

- value to set, can be

null

**Throws:**
- UnsupportedOperationException

- if it's not a dynamically generated
event
- IndexOutOfBoundsException

- if

index

is less than

0

or
greater than or equal to the number of fields specified for the event

**See Also:**
- EventType.getFields()

,

EventFactory

---

### Additional Sections

#### Class Event

java.lang.Object

- jdk.internal.event.Event
- - jdk.jfr.Event

jdk.internal.event.Event

- jdk.jfr.Event

jdk.jfr.Event

```java
public abstract class
Event

extends jdk.internal.event.Event
```

Base class for events, to be subclassed in order to define events and their
fields.

The following example shows how to implement an

Event

class.

```java
import jdk.jfr.Event;
import jdk.jfr.Description;
import jdk.jfr.Label;

public class Example {

@Label("Hello World")
@Description("Helps programmer getting started")
static class HelloWorld extends Event {
@Label("Message")
String message;
}

public static void main(String... args) {
HelloWorld event = new HelloWorld();
event.message = "hello, world!";
event.commit();
}
}
```

After an event is allocated and its field members are populated, it can be
written to the Flight Recorder system by using the

#commit()

method.

By default, an event is enabled. To disable an event annotate the

Event

class with

@Enabled(false)

.

Supported field types are the Java primitives:

boolean

,

char

,

byte

,

short

,

int

,

long

,

float

, and

double

. Supported reference types are:

String

,

Thread

and

Class

. Arrays, enums, and other reference types are silently
ignored and not included. Fields that are of the supported types can be
excluded by using the transient modifier. Static fields, even of the
supported types, are not included.

Tools can visualize data in a meaningful way when annotations are used (for
example,

Label

,

Description

, and

Timespan

).
Annotations applied to an

Event

class or its fields are included if
they are present (indirectly, directly, or associated), have the

MetadataDefinition

annotation, and they do not contain enums, arrays,
or classes.

Gathering data to store in an event can be expensive. The

shouldCommit()

method can be used to verify whether an event
instance would actually be written to the system when the

Event#commit()commit

method is invoked. If

shouldCommit()

returns false, then those operations can be
avoided.

**Since:** 9

public abstract class

Event

extends jdk.internal.event.Event

Base class for events, to be subclassed in order to define events and their
fields.

The following example shows how to implement an

Event

class.

```java
import jdk.jfr.Event;
import jdk.jfr.Description;
import jdk.jfr.Label;

public class Example {

@Label("Hello World")
@Description("Helps programmer getting started")
static class HelloWorld extends Event {
@Label("Message")
String message;
}

public static void main(String... args) {
HelloWorld event = new HelloWorld();
event.message = "hello, world!";
event.commit();
}
}
```

After an event is allocated and its field members are populated, it can be
written to the Flight Recorder system by using the

#commit()

method.

By default, an event is enabled. To disable an event annotate the

Event

class with

@Enabled(false)

.

Supported field types are the Java primitives:

boolean

,

char

,

byte

,

short

,

int

,

long

,

float

, and

double

. Supported reference types are:

String

,

Thread

and

Class

. Arrays, enums, and other reference types are silently
ignored and not included. Fields that are of the supported types can be
excluded by using the transient modifier. Static fields, even of the
supported types, are not included.

Tools can visualize data in a meaningful way when annotations are used (for
example,

Label

,

Description

, and

Timespan

).
Annotations applied to an

Event

class or its fields are included if
they are present (indirectly, directly, or associated), have the

MetadataDefinition

annotation, and they do not contain enums, arrays,
or classes.

Gathering data to store in an event can be expensive. The

shouldCommit()

method can be used to verify whether an event
instance would actually be written to the system when the

Event#commit()commit

method is invoked. If

shouldCommit()

returns false, then those operations can be
avoided.

The following example shows how to implement an

Event

class.

```java
import jdk.jfr.Event;
import jdk.jfr.Description;
import jdk.jfr.Label;

public class Example {

@Label("Hello World")
@Description("Helps programmer getting started")
static class HelloWorld extends Event {
@Label("Message")
String message;
}

public static void main(String... args) {
HelloWorld event = new HelloWorld();
event.message = "hello, world!";
event.commit();
}
}
```

After an event is allocated and its field members are populated, it can be
written to the Flight Recorder system by using the

#commit()

method.

By default, an event is enabled. To disable an event annotate the

Event

class with

@Enabled(false)

.

Supported field types are the Java primitives:

boolean

,

char

,

byte

,

short

,

int

,

long

,

float

, and

double

. Supported reference types are:

String

,

Thread

and

Class

. Arrays, enums, and other reference types are silently
ignored and not included. Fields that are of the supported types can be
excluded by using the transient modifier. Static fields, even of the
supported types, are not included.

Tools can visualize data in a meaningful way when annotations are used (for
example,

Label

,

Description

, and

Timespan

).
Annotations applied to an

Event

class or its fields are included if
they are present (indirectly, directly, or associated), have the

MetadataDefinition

annotation, and they do not contain enums, arrays,
or classes.

Gathering data to store in an event can be expensive. The

shouldCommit()

method can be used to verify whether an event
instance would actually be written to the system when the

Event#commit()commit

method is invoked. If

shouldCommit()

returns false, then those operations can be
avoided.

import jdk.jfr.Event;
import jdk.jfr.Description;
import jdk.jfr.Label;

public class Example {

@Label("Hello World")
@Description("Helps programmer getting started")
static class HelloWorld extends Event {
@Label("Message")
String message;
}

public static void main(String... args) {
HelloWorld event = new HelloWorld();
event.message = "hello, world!";
event.commit();
}
}

After an event is allocated and its field members are populated, it can be
written to the Flight Recorder system by using the

#commit()

method.

By default, an event is enabled. To disable an event annotate the

Event

class with

@Enabled(false)

.

Supported field types are the Java primitives:

boolean

,

char

,

byte

,

short

,

int

,

long

,

float

, and

double

. Supported reference types are:

String

,

Thread

and

Class

. Arrays, enums, and other reference types are silently
ignored and not included. Fields that are of the supported types can be
excluded by using the transient modifier. Static fields, even of the
supported types, are not included.

Tools can visualize data in a meaningful way when annotations are used (for
example,

Label

,

Description

, and

Timespan

).
Annotations applied to an

Event

class or its fields are included if
they are present (indirectly, directly, or associated), have the

MetadataDefinition

annotation, and they do not contain enums, arrays,
or classes.

Gathering data to store in an event can be expensive. The

shouldCommit()

method can be used to verify whether an event
instance would actually be written to the system when the

Event#commit()commit

method is invoked. If

shouldCommit()

returns false, then those operations can be
avoided.

By default, an event is enabled. To disable an event annotate the

Event

class with

@Enabled(false)

.

Supported field types are the Java primitives:

boolean

,

char

,

byte

,

short

,

int

,

long

,

float

, and

double

. Supported reference types are:

String

,

Thread

and

Class

. Arrays, enums, and other reference types are silently
ignored and not included. Fields that are of the supported types can be
excluded by using the transient modifier. Static fields, even of the
supported types, are not included.

Tools can visualize data in a meaningful way when annotations are used (for
example,

Label

,

Description

, and

Timespan

).
Annotations applied to an

Event

class or its fields are included if
they are present (indirectly, directly, or associated), have the

MetadataDefinition

annotation, and they do not contain enums, arrays,
or classes.

Gathering data to store in an event can be expensive. The

shouldCommit()

method can be used to verify whether an event
instance would actually be written to the system when the

Event#commit()commit

method is invoked. If

shouldCommit()

returns false, then those operations can be
avoided.

Supported field types are the Java primitives:

boolean

,

char

,

byte

,

short

,

int

,

long

,

float

, and

double

. Supported reference types are:

String

,

Thread

and

Class

. Arrays, enums, and other reference types are silently
ignored and not included. Fields that are of the supported types can be
excluded by using the transient modifier. Static fields, even of the
supported types, are not included.

Tools can visualize data in a meaningful way when annotations are used (for
example,

Label

,

Description

, and

Timespan

).
Annotations applied to an

Event

class or its fields are included if
they are present (indirectly, directly, or associated), have the

MetadataDefinition

annotation, and they do not contain enums, arrays,
or classes.

Gathering data to store in an event can be expensive. The

shouldCommit()

method can be used to verify whether an event
instance would actually be written to the system when the

Event#commit()commit

method is invoked. If

shouldCommit()

returns false, then those operations can be
avoided.

Tools can visualize data in a meaningful way when annotations are used (for
example,

Label

,

Description

, and

Timespan

).
Annotations applied to an

Event

class or its fields are included if
they are present (indirectly, directly, or associated), have the

MetadataDefinition

annotation, and they do not contain enums, arrays,
or classes.

Gathering data to store in an event can be expensive. The

shouldCommit()

method can be used to verify whether an event
instance would actually be written to the system when the

Event#commit()commit

method is invoked. If

shouldCommit()

returns false, then those operations can be
avoided.

Gathering data to store in an event can be expensive. The

shouldCommit()

method can be used to verify whether an event
instance would actually be written to the system when the

Event#commit()commit

method is invoked. If

shouldCommit()

returns false, then those operations can be
avoided.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Event

()

Sole constructor, for invocation by subclass constructors, typically
implicit.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

begin

()

Starts the timing of this event.

void

commit

()

Writes the field values, time stamp, and event duration to the Flight
Recorder system.

void

end

()

Ends the timing of this event.

boolean

isEnabled

()

Returns

true

if at least one recording is running, and the
enabled setting for this event is set to

true

, otherwise

false

is returned.

void

set

​(int index,

Object

value)

Sets a field value.

boolean

shouldCommit

()

Returns

true

if the enabled setting for this event is set to

true

and if the duration is within the threshold for the event,

false

otherwise.

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

Modifier

Constructor

Description

protected

Event

()

Sole constructor, for invocation by subclass constructors, typically
implicit.

---

#### Constructor Summary

Sole constructor, for invocation by subclass constructors, typically
implicit.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

begin

()

Starts the timing of this event.

void

commit

()

Writes the field values, time stamp, and event duration to the Flight
Recorder system.

void

end

()

Ends the timing of this event.

boolean

isEnabled

()

Returns

true

if at least one recording is running, and the
enabled setting for this event is set to

true

, otherwise

false

is returned.

void

set

​(int index,

Object

value)

Sets a field value.

boolean

shouldCommit

()

Returns

true

if the enabled setting for this event is set to

true

and if the duration is within the threshold for the event,

false

otherwise.

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

Starts the timing of this event.

Writes the field values, time stamp, and event duration to the Flight
Recorder system.

Ends the timing of this event.

Returns

true

if at least one recording is running, and the
enabled setting for this event is set to

true

, otherwise

false

is returned.

Sets a field value.

Returns

true

if the enabled setting for this event is set to

true

and if the duration is within the threshold for the event,

false

otherwise.

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

- Event

```java
protected Event()
```

Sole constructor, for invocation by subclass constructors, typically
implicit.

============ METHOD DETAIL ==========

- Method Detail

- begin

```java
public final void begin()
```

Starts the timing of this event.

**Overrides:** begin

in class

jdk.internal.event.Event

- end

```java
public final void end()
```

Ends the timing of this event.

The

end

method must be invoked after the

begin

method.

**Overrides:** end

in class

jdk.internal.event.Event

- commit

```java
public final void commit()
```

Writes the field values, time stamp, and event duration to the Flight
Recorder system.

If the event starts with an invocation of the

begin

method, but does
not end with an explicit invocation of the

end

method, then the event
ends when the

commit

method is invoked.

**Overrides:** commit

in class

jdk.internal.event.Event

- isEnabled

```java
public final boolean isEnabled()
```

Returns

true

if at least one recording is running, and the
enabled setting for this event is set to

true

, otherwise

false

is returned.

**Overrides:** isEnabled

in class

jdk.internal.event.Event
**Returns:** true

if event is enabled,

false

otherwise

- shouldCommit

```java
public final boolean shouldCommit()
```

Returns

true

if the enabled setting for this event is set to

true

and if the duration is within the threshold for the event,

false

otherwise. The threshold is the minimum threshold for all
running recordings.

**Overrides:** shouldCommit

in class

jdk.internal.event.Event
**Returns:** true

if the event can be written to the Flight Recorder
system,

false

otherwise

- set

```java
public final void set​(int index,

Object
value)
```

Sets a field value.

Applicable only if the event is dynamically defined using the

EventFactory

class.

The supplied

index

corresponds to the index of the

ValueDescriptor

object passed to the factory method of the

EventFactory

class.

**Overrides:** set

in class

jdk.internal.event.Event
**Parameters:** index

- the index of the field that is passed to

EventFactory#create(String, java.util.List, java.util.List)
**Parameters:** value

- value to set, can be

null
**Throws:** UnsupportedOperationException

- if it's not a dynamically generated
event
**Throws:** IndexOutOfBoundsException

- if

index

is less than

0

or
greater than or equal to the number of fields specified for the event
**See Also:** EventType.getFields()

,

EventFactory

Constructor Detail

- Event

```java
protected Event()
```

Sole constructor, for invocation by subclass constructors, typically
implicit.

---

#### Constructor Detail

Event

```java
protected Event()
```

Sole constructor, for invocation by subclass constructors, typically
implicit.

---

#### Event

protected Event()

Sole constructor, for invocation by subclass constructors, typically
implicit.

Method Detail

- begin

```java
public final void begin()
```

Starts the timing of this event.

**Overrides:** begin

in class

jdk.internal.event.Event

- end

```java
public final void end()
```

Ends the timing of this event.

The

end

method must be invoked after the

begin

method.

**Overrides:** end

in class

jdk.internal.event.Event

- commit

```java
public final void commit()
```

Writes the field values, time stamp, and event duration to the Flight
Recorder system.

If the event starts with an invocation of the

begin

method, but does
not end with an explicit invocation of the

end

method, then the event
ends when the

commit

method is invoked.

**Overrides:** commit

in class

jdk.internal.event.Event

- isEnabled

```java
public final boolean isEnabled()
```

Returns

true

if at least one recording is running, and the
enabled setting for this event is set to

true

, otherwise

false

is returned.

**Overrides:** isEnabled

in class

jdk.internal.event.Event
**Returns:** true

if event is enabled,

false

otherwise

- shouldCommit

```java
public final boolean shouldCommit()
```

Returns

true

if the enabled setting for this event is set to

true

and if the duration is within the threshold for the event,

false

otherwise. The threshold is the minimum threshold for all
running recordings.

**Overrides:** shouldCommit

in class

jdk.internal.event.Event
**Returns:** true

if the event can be written to the Flight Recorder
system,

false

otherwise

- set

```java
public final void set​(int index,

Object
value)
```

Sets a field value.

Applicable only if the event is dynamically defined using the

EventFactory

class.

The supplied

index

corresponds to the index of the

ValueDescriptor

object passed to the factory method of the

EventFactory

class.

**Overrides:** set

in class

jdk.internal.event.Event
**Parameters:** index

- the index of the field that is passed to

EventFactory#create(String, java.util.List, java.util.List)
**Parameters:** value

- value to set, can be

null
**Throws:** UnsupportedOperationException

- if it's not a dynamically generated
event
**Throws:** IndexOutOfBoundsException

- if

index

is less than

0

or
greater than or equal to the number of fields specified for the event
**See Also:** EventType.getFields()

,

EventFactory

---

#### Method Detail

begin

```java
public final void begin()
```

Starts the timing of this event.

**Overrides:** begin

in class

jdk.internal.event.Event

---

#### begin

public final void begin()

Starts the timing of this event.

end

```java
public final void end()
```

Ends the timing of this event.

The

end

method must be invoked after the

begin

method.

**Overrides:** end

in class

jdk.internal.event.Event

---

#### end

public final void end()

Ends the timing of this event.

The

end

method must be invoked after the

begin

method.

commit

```java
public final void commit()
```

Writes the field values, time stamp, and event duration to the Flight
Recorder system.

If the event starts with an invocation of the

begin

method, but does
not end with an explicit invocation of the

end

method, then the event
ends when the

commit

method is invoked.

**Overrides:** commit

in class

jdk.internal.event.Event

---

#### commit

public final void commit()

Writes the field values, time stamp, and event duration to the Flight
Recorder system.

If the event starts with an invocation of the

begin

method, but does
not end with an explicit invocation of the

end

method, then the event
ends when the

commit

method is invoked.

If the event starts with an invocation of the

begin

method, but does
not end with an explicit invocation of the

end

method, then the event
ends when the

commit

method is invoked.

isEnabled

```java
public final boolean isEnabled()
```

Returns

true

if at least one recording is running, and the
enabled setting for this event is set to

true

, otherwise

false

is returned.

**Overrides:** isEnabled

in class

jdk.internal.event.Event
**Returns:** true

if event is enabled,

false

otherwise

---

#### isEnabled

public final boolean isEnabled()

Returns

true

if at least one recording is running, and the
enabled setting for this event is set to

true

, otherwise

false

is returned.

shouldCommit

```java
public final boolean shouldCommit()
```

Returns

true

if the enabled setting for this event is set to

true

and if the duration is within the threshold for the event,

false

otherwise. The threshold is the minimum threshold for all
running recordings.

**Overrides:** shouldCommit

in class

jdk.internal.event.Event
**Returns:** true

if the event can be written to the Flight Recorder
system,

false

otherwise

---

#### shouldCommit

public final boolean shouldCommit()

Returns

true

if the enabled setting for this event is set to

true

and if the duration is within the threshold for the event,

false

otherwise. The threshold is the minimum threshold for all
running recordings.

set

```java
public final void set​(int index,

Object
value)
```

Sets a field value.

Applicable only if the event is dynamically defined using the

EventFactory

class.

The supplied

index

corresponds to the index of the

ValueDescriptor

object passed to the factory method of the

EventFactory

class.

**Overrides:** set

in class

jdk.internal.event.Event
**Parameters:** index

- the index of the field that is passed to

EventFactory#create(String, java.util.List, java.util.List)
**Parameters:** value

- value to set, can be

null
**Throws:** UnsupportedOperationException

- if it's not a dynamically generated
event
**Throws:** IndexOutOfBoundsException

- if

index

is less than

0

or
greater than or equal to the number of fields specified for the event
**See Also:** EventType.getFields()

,

EventFactory

---

#### set

public final void set​(int index,

Object

value)

Sets a field value.

Applicable only if the event is dynamically defined using the

EventFactory

class.

The supplied

index

corresponds to the index of the

ValueDescriptor

object passed to the factory method of the

EventFactory

class.

Applicable only if the event is dynamically defined using the

EventFactory

class.

The supplied

index

corresponds to the index of the

ValueDescriptor

object passed to the factory method of the

EventFactory

class.

The supplied

index

corresponds to the index of the

ValueDescriptor

object passed to the factory method of the

EventFactory

class.

---

