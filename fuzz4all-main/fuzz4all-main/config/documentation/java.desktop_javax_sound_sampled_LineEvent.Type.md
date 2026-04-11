# Class LineEvent.Type

**Source:** `java.desktop\javax\sound\sampled\LineEvent.Type.html`

### Class Description

```java
public static class
LineEvent.Type

extends
Object
```

The LineEvent.Type inner class identifies what kind of event occurred on
a line. Static instances are provided for the common types (OPEN, CLOSE,
START, and STOP).

**Enclosing class:** LineEvent

---

### Field Details

#### public static final
LineEvent.Type
OPEN

A type of event that is sent when a line opens, reserving system
resources for itself.

**See Also:**
- CLOSE

,

Line.open()

---

#### public static final
LineEvent.Type
CLOSE

A type of event that is sent when a line closes, freeing the system
resources it had obtained when it was opened.

**See Also:**
- OPEN

,

Line.close()

---

#### public static final
LineEvent.Type
START

A type of event that is sent when a line begins to engage in active
input or output of audio data in response to a

start

request.

**See Also:**
- STOP

,

DataLine.start()

---

#### public static final
LineEvent.Type
STOP

A type of event that is sent when a line ceases active input or
output of audio data in response to a

stop

request, or because the end of media has been reached.

**See Also:**
- START

,

DataLine.stop()

---

### Constructor Details

#### protected Type​(
String
name)

Constructs a new event type.

**Parameters:**
- name

- name of the type

---

### Method Details

#### public final boolean equals​(
Object
obj)

Indicates whether the specified object is equal to this event type,
returning

true

if the objects are the same.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare

**Returns:**
- true

if the specified object is equal to this event
type;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns a hash code value for this event type.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this event type

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns the type name as the string representation.

**Overrides:**
- toString

in class

Object

**Returns:**
- the type name as the string representation

---

### Additional Sections

#### Class LineEvent.Type

java.lang.Object

- javax.sound.sampled.LineEvent.Type

javax.sound.sampled.LineEvent.Type

**Enclosing class:** LineEvent

```java
public static class
LineEvent.Type

extends
Object
```

The LineEvent.Type inner class identifies what kind of event occurred on
a line. Static instances are provided for the common types (OPEN, CLOSE,
START, and STOP).

**See Also:** LineEvent.getType()

public static class

LineEvent.Type

extends

Object

The LineEvent.Type inner class identifies what kind of event occurred on
a line. Static instances are provided for the common types (OPEN, CLOSE,
START, and STOP).

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

LineEvent.Type

CLOSE

A type of event that is sent when a line closes, freeing the system
resources it had obtained when it was opened.

static

LineEvent.Type

OPEN

A type of event that is sent when a line opens, reserving system
resources for itself.

static

LineEvent.Type

START

A type of event that is sent when a line begins to engage in active
input or output of audio data in response to a

start

request.

static

LineEvent.Type

STOP

A type of event that is sent when a line ceases active input or
output of audio data in response to a

stop

request, or because the end of media has been reached.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Type

​(

String

name)

Constructs a new event type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this event type,
returning

true

if the objects are the same.

int

hashCode

()

Returns a hash code value for this event type.

String

toString

()

Returns the type name as the string representation.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

static

LineEvent.Type

CLOSE

A type of event that is sent when a line closes, freeing the system
resources it had obtained when it was opened.

static

LineEvent.Type

OPEN

A type of event that is sent when a line opens, reserving system
resources for itself.

static

LineEvent.Type

START

A type of event that is sent when a line begins to engage in active
input or output of audio data in response to a

start

request.

static

LineEvent.Type

STOP

A type of event that is sent when a line ceases active input or
output of audio data in response to a

stop

request, or because the end of media has been reached.

---

#### Field Summary

A type of event that is sent when a line closes, freeing the system
resources it had obtained when it was opened.

A type of event that is sent when a line opens, reserving system
resources for itself.

A type of event that is sent when a line begins to engage in active
input or output of audio data in response to a

start

request.

A type of event that is sent when a line ceases active input or
output of audio data in response to a

stop

request, or because the end of media has been reached.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Type

​(

String

name)

Constructs a new event type.

---

#### Constructor Summary

Constructs a new event type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this event type,
returning

true

if the objects are the same.

int

hashCode

()

Returns a hash code value for this event type.

String

toString

()

Returns the type name as the string representation.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Indicates whether the specified object is equal to this event type,
returning

true

if the objects are the same.

Returns a hash code value for this event type.

Returns the type name as the string representation.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- OPEN

```java
public static final
LineEvent.Type
OPEN
```

A type of event that is sent when a line opens, reserving system
resources for itself.

**See Also:** CLOSE

,

Line.open()

- CLOSE

```java
public static final
LineEvent.Type
CLOSE
```

A type of event that is sent when a line closes, freeing the system
resources it had obtained when it was opened.

**See Also:** OPEN

,

Line.close()

- START

```java
public static final
LineEvent.Type
START
```

A type of event that is sent when a line begins to engage in active
input or output of audio data in response to a

start

request.

**See Also:** STOP

,

DataLine.start()

- STOP

```java
public static final
LineEvent.Type
STOP
```

A type of event that is sent when a line ceases active input or
output of audio data in response to a

stop

request, or because the end of media has been reached.

**See Also:** START

,

DataLine.stop()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Type

```java
protected Type​(
String
name)
```

Constructs a new event type.

**Parameters:** name

- name of the type

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this event type,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this event
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this event type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this event type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the type name as the string representation.

**Overrides:** toString

in class

Object
**Returns:** the type name as the string representation

Field Detail

- OPEN

```java
public static final
LineEvent.Type
OPEN
```

A type of event that is sent when a line opens, reserving system
resources for itself.

**See Also:** CLOSE

,

Line.open()

- CLOSE

```java
public static final
LineEvent.Type
CLOSE
```

A type of event that is sent when a line closes, freeing the system
resources it had obtained when it was opened.

**See Also:** OPEN

,

Line.close()

- START

```java
public static final
LineEvent.Type
START
```

A type of event that is sent when a line begins to engage in active
input or output of audio data in response to a

start

request.

**See Also:** STOP

,

DataLine.start()

- STOP

```java
public static final
LineEvent.Type
STOP
```

A type of event that is sent when a line ceases active input or
output of audio data in response to a

stop

request, or because the end of media has been reached.

**See Also:** START

,

DataLine.stop()

---

#### Field Detail

OPEN

```java
public static final
LineEvent.Type
OPEN
```

A type of event that is sent when a line opens, reserving system
resources for itself.

**See Also:** CLOSE

,

Line.open()

---

#### OPEN

public static final

LineEvent.Type

OPEN

A type of event that is sent when a line opens, reserving system
resources for itself.

CLOSE

```java
public static final
LineEvent.Type
CLOSE
```

A type of event that is sent when a line closes, freeing the system
resources it had obtained when it was opened.

**See Also:** OPEN

,

Line.close()

---

#### CLOSE

public static final

LineEvent.Type

CLOSE

A type of event that is sent when a line closes, freeing the system
resources it had obtained when it was opened.

START

```java
public static final
LineEvent.Type
START
```

A type of event that is sent when a line begins to engage in active
input or output of audio data in response to a

start

request.

**See Also:** STOP

,

DataLine.start()

---

#### START

public static final

LineEvent.Type

START

A type of event that is sent when a line begins to engage in active
input or output of audio data in response to a

start

request.

STOP

```java
public static final
LineEvent.Type
STOP
```

A type of event that is sent when a line ceases active input or
output of audio data in response to a

stop

request, or because the end of media has been reached.

**See Also:** START

,

DataLine.stop()

---

#### STOP

public static final

LineEvent.Type

STOP

A type of event that is sent when a line ceases active input or
output of audio data in response to a

stop

request, or because the end of media has been reached.

Constructor Detail

- Type

```java
protected Type​(
String
name)
```

Constructs a new event type.

**Parameters:** name

- name of the type

---

#### Constructor Detail

Type

```java
protected Type​(
String
name)
```

Constructs a new event type.

**Parameters:** name

- name of the type

---

#### Type

protected Type​(

String

name)

Constructs a new event type.

Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this event type,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this event
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this event type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this event type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the type name as the string representation.

**Overrides:** toString

in class

Object
**Returns:** the type name as the string representation

---

#### Method Detail

equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this event type,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this event
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Indicates whether the specified object is equal to this event type,
returning

true

if the objects are the same.

hashCode

```java
public final int hashCode()
```

Returns a hash code value for this event type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this event type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hash code value for this event type.

toString

```java
public
String
toString()
```

Returns the type name as the string representation.

**Overrides:** toString

in class

Object
**Returns:** the type name as the string representation

---

#### toString

public

String

toString()

Returns the type name as the string representation.

---

