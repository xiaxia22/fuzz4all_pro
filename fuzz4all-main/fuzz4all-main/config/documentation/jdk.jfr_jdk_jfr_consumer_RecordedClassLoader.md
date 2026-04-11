# Class RecordedClassLoader

**Source:** `jdk.jfr\jdk\jfr\consumer\RecordedClassLoader.html`

### Class Description

```java
public final class
RecordedClassLoader

extends
RecordedObject
```

A recorded Java class loader.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
RecordedClass
getType()

Returns the class of the class loader.

If the bootstrap class loader is represented as

null

in the Java
Virtual Machine (JVM), then

null

is also the return value of this
method.

**Returns:**
- class of the class loader, can be

null

---

#### public
String
getName()

Returns the name of the class loader (for example, "boot", "platform", and
"app").

**Returns:**
- the class loader name, can be

null

---

#### public long getId()

Returns a unique ID for the class loader.

The ID might not be the same between Java Virtual Machine (JVM) instances.

**Returns:**
- a unique ID

---

### Additional Sections

#### Class RecordedClassLoader

java.lang.Object

- jdk.jfr.consumer.RecordedObject
- - jdk.jfr.consumer.RecordedClassLoader

jdk.jfr.consumer.RecordedObject

- jdk.jfr.consumer.RecordedClassLoader

jdk.jfr.consumer.RecordedClassLoader

```java
public final class
RecordedClassLoader

extends
RecordedObject
```

A recorded Java class loader.

**Since:** 9

public final class

RecordedClassLoader

extends

RecordedObject

A recorded Java class loader.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getId

()

Returns a unique ID for the class loader.

String

getName

()

Returns the name of the class loader (for example, "boot", "platform", and
"app").

RecordedClass

getType

()

Returns the class of the class loader.

- Methods declared in class jdk.jfr.consumer.

RecordedObject

getBoolean

,

getByte

,

getChar

,

getClass

,

getDouble

,

getDuration

,

getFields

,

getFloat

,

getInstant

,

getInt

,

getLong

,

getShort

,

getString

,

getThread

,

getValue

,

hasField

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getId

()

Returns a unique ID for the class loader.

String

getName

()

Returns the name of the class loader (for example, "boot", "platform", and
"app").

RecordedClass

getType

()

Returns the class of the class loader.

- Methods declared in class jdk.jfr.consumer.

RecordedObject

getBoolean

,

getByte

,

getChar

,

getClass

,

getDouble

,

getDuration

,

getFields

,

getFloat

,

getInstant

,

getInt

,

getLong

,

getShort

,

getString

,

getThread

,

getValue

,

hasField

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

Returns a unique ID for the class loader.

Returns the name of the class loader (for example, "boot", "platform", and
"app").

Returns the class of the class loader.

Methods declared in class jdk.jfr.consumer.

RecordedObject

getBoolean

,

getByte

,

getChar

,

getClass

,

getDouble

,

getDuration

,

getFields

,

getFloat

,

getInstant

,

getInt

,

getLong

,

getShort

,

getString

,

getThread

,

getValue

,

hasField

,

toString

---

#### Methods declared in class jdk.jfr.consumer. RecordedObject

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

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public
RecordedClass
getType()
```

Returns the class of the class loader.

If the bootstrap class loader is represented as

null

in the Java
Virtual Machine (JVM), then

null

is also the return value of this
method.

**Returns:** class of the class loader, can be

null

- getName

```java
public
String
getName()
```

Returns the name of the class loader (for example, "boot", "platform", and
"app").

**Returns:** the class loader name, can be

null

- getId

```java
public long getId()
```

Returns a unique ID for the class loader.

The ID might not be the same between Java Virtual Machine (JVM) instances.

**Returns:** a unique ID

Method Detail

- getType

```java
public
RecordedClass
getType()
```

Returns the class of the class loader.

If the bootstrap class loader is represented as

null

in the Java
Virtual Machine (JVM), then

null

is also the return value of this
method.

**Returns:** class of the class loader, can be

null

- getName

```java
public
String
getName()
```

Returns the name of the class loader (for example, "boot", "platform", and
"app").

**Returns:** the class loader name, can be

null

- getId

```java
public long getId()
```

Returns a unique ID for the class loader.

The ID might not be the same between Java Virtual Machine (JVM) instances.

**Returns:** a unique ID

---

#### Method Detail

getType

```java
public
RecordedClass
getType()
```

Returns the class of the class loader.

If the bootstrap class loader is represented as

null

in the Java
Virtual Machine (JVM), then

null

is also the return value of this
method.

**Returns:** class of the class loader, can be

null

---

#### getType

public

RecordedClass

getType()

Returns the class of the class loader.

If the bootstrap class loader is represented as

null

in the Java
Virtual Machine (JVM), then

null

is also the return value of this
method.

If the bootstrap class loader is represented as

null

in the Java
Virtual Machine (JVM), then

null

is also the return value of this
method.

getName

```java
public
String
getName()
```

Returns the name of the class loader (for example, "boot", "platform", and
"app").

**Returns:** the class loader name, can be

null

---

#### getName

public

String

getName()

Returns the name of the class loader (for example, "boot", "platform", and
"app").

getId

```java
public long getId()
```

Returns a unique ID for the class loader.

The ID might not be the same between Java Virtual Machine (JVM) instances.

**Returns:** a unique ID

---

#### getId

public long getId()

Returns a unique ID for the class loader.

The ID might not be the same between Java Virtual Machine (JVM) instances.

The ID might not be the same between Java Virtual Machine (JVM) instances.

---

