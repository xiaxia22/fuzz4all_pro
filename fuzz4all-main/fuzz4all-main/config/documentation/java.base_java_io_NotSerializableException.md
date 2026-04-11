# Class NotSerializableException

**Source:** `java.base\java\io\NotSerializableException.html`

### Class Description

```java
public class
NotSerializableException

extends
ObjectStreamException
```

Thrown when an instance is required to have a Serializable interface.
The serialization runtime or the class of the instance can throw
this exception. The argument should be the name of the class.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NotSerializableException​(
String
classname)

Constructs a NotSerializableException object with message string.

**Parameters:**
- classname

- Class of the instance being serialized/deserialized.

---

#### public NotSerializableException()

Constructs a NotSerializableException object.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NotSerializableException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.io.ObjectStreamException
- - java.io.NotSerializableException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.io.ObjectStreamException
- - java.io.NotSerializableException

java.lang.Exception

- java.io.IOException
- - java.io.ObjectStreamException
- - java.io.NotSerializableException

java.io.IOException

- java.io.ObjectStreamException
- - java.io.NotSerializableException

java.io.ObjectStreamException

- java.io.NotSerializableException

java.io.NotSerializableException

**All Implemented Interfaces:** Serializable

```java
public class
NotSerializableException

extends
ObjectStreamException
```

Thrown when an instance is required to have a Serializable interface.
The serialization runtime or the class of the instance can throw
this exception. The argument should be the name of the class.

**Since:** 1.1
**See Also:** Serialized Form

public class

NotSerializableException

extends

ObjectStreamException

Thrown when an instance is required to have a Serializable interface.
The serialization runtime or the class of the instance can throw
this exception. The argument should be the name of the class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NotSerializableException

()

Constructs a NotSerializableException object.

NotSerializableException

​(

String

classname)

Constructs a NotSerializableException object with message string.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Constructor Summary

Constructors

Constructor

Description

NotSerializableException

()

Constructs a NotSerializableException object.

NotSerializableException

​(

String

classname)

Constructs a NotSerializableException object with message string.

---

#### Constructor Summary

Constructs a NotSerializableException object.

Constructs a NotSerializableException object with message string.

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

- NotSerializableException

```java
public NotSerializableException​(
String
classname)
```

Constructs a NotSerializableException object with message string.

**Parameters:** classname

- Class of the instance being serialized/deserialized.

- NotSerializableException

```java
public NotSerializableException()
```

Constructs a NotSerializableException object.

Constructor Detail

- NotSerializableException

```java
public NotSerializableException​(
String
classname)
```

Constructs a NotSerializableException object with message string.

**Parameters:** classname

- Class of the instance being serialized/deserialized.

- NotSerializableException

```java
public NotSerializableException()
```

Constructs a NotSerializableException object.

---

#### Constructor Detail

NotSerializableException

```java
public NotSerializableException​(
String
classname)
```

Constructs a NotSerializableException object with message string.

**Parameters:** classname

- Class of the instance being serialized/deserialized.

---

#### NotSerializableException

public NotSerializableException​(

String

classname)

Constructs a NotSerializableException object with message string.

NotSerializableException

```java
public NotSerializableException()
```

Constructs a NotSerializableException object.

---

#### NotSerializableException

public NotSerializableException()

Constructs a NotSerializableException object.

---

