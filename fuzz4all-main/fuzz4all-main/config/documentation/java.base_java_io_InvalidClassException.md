# Class InvalidClassException

**Source:** `java.base\java\io\InvalidClassException.html`

### Class Description

```java
public class
InvalidClassException

extends
ObjectStreamException
```

Thrown when the Serialization runtime detects one of the following
problems with a Class.

- The serial version of the class does not match that of the class
descriptor read from the stream

The class contains unknown datatypes

The class does not have an accessible no-arg constructor

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public
String
classname

Name of the invalid class.

---

### Constructor Details

#### public InvalidClassException​(
String
reason)

Report an InvalidClassException for the reason specified.

**Parameters:**
- reason

- String describing the reason for the exception.

---

#### public InvalidClassException​(
String
cname,

String
reason)

Constructs an InvalidClassException object.

**Parameters:**
- cname

- a String naming the invalid class.
- reason

- a String describing the reason for the exception.

---

### Method Details

#### public
String
getMessage()

Produce the message and include the classname, if present.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- the detail message string of this

Throwable

instance
(which may be

null

).

---

### Additional Sections

#### Class InvalidClassException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.io.ObjectStreamException
- - java.io.InvalidClassException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.io.ObjectStreamException
- - java.io.InvalidClassException

java.lang.Exception

- java.io.IOException
- - java.io.ObjectStreamException
- - java.io.InvalidClassException

java.io.IOException

- java.io.ObjectStreamException
- - java.io.InvalidClassException

java.io.ObjectStreamException

- java.io.InvalidClassException

java.io.InvalidClassException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidClassException

extends
ObjectStreamException
```

Thrown when the Serialization runtime detects one of the following
problems with a Class.

- The serial version of the class does not match that of the class
descriptor read from the stream

The class contains unknown datatypes

The class does not have an accessible no-arg constructor

**Since:** 1.1
**See Also:** Serialized Form

public class

InvalidClassException

extends

ObjectStreamException

Thrown when the Serialization runtime detects one of the following
problems with a Class.

- The serial version of the class does not match that of the class
descriptor read from the stream

The class contains unknown datatypes

The class does not have an accessible no-arg constructor

The serial version of the class does not match that of the class
descriptor read from the stream

The class contains unknown datatypes

The class does not have an accessible no-arg constructor

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

String

classname

Name of the invalid class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InvalidClassException

​(

String

reason)

Report an InvalidClassException for the reason specified.

InvalidClassException

​(

String

cname,

String

reason)

Constructs an InvalidClassException object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMessage

()

Produce the message and include the classname, if present.

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

Field Summary

Fields

Modifier and Type

Field

Description

String

classname

Name of the invalid class.

---

#### Field Summary

Name of the invalid class.

Constructor Summary

Constructors

Constructor

Description

InvalidClassException

​(

String

reason)

Report an InvalidClassException for the reason specified.

InvalidClassException

​(

String

cname,

String

reason)

Constructs an InvalidClassException object.

---

#### Constructor Summary

Report an InvalidClassException for the reason specified.

Constructs an InvalidClassException object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMessage

()

Produce the message and include the classname, if present.

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

Produce the message and include the classname, if present.

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

============ FIELD DETAIL ===========

- Field Detail

- classname

```java
public
String
classname
```

Name of the invalid class.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InvalidClassException

```java
public InvalidClassException​(
String
reason)
```

Report an InvalidClassException for the reason specified.

**Parameters:** reason

- String describing the reason for the exception.

- InvalidClassException

```java
public InvalidClassException​(
String
cname,

String
reason)
```

Constructs an InvalidClassException object.

**Parameters:** cname

- a String naming the invalid class.
**Parameters:** reason

- a String describing the reason for the exception.

============ METHOD DETAIL ==========

- Method Detail

- getMessage

```java
public
String
getMessage()
```

Produce the message and include the classname, if present.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

Throwable

instance
(which may be

null

).

Field Detail

- classname

```java
public
String
classname
```

Name of the invalid class.

---

#### Field Detail

classname

```java
public
String
classname
```

Name of the invalid class.

---

#### classname

public

String

classname

Name of the invalid class.

Constructor Detail

- InvalidClassException

```java
public InvalidClassException​(
String
reason)
```

Report an InvalidClassException for the reason specified.

**Parameters:** reason

- String describing the reason for the exception.

- InvalidClassException

```java
public InvalidClassException​(
String
cname,

String
reason)
```

Constructs an InvalidClassException object.

**Parameters:** cname

- a String naming the invalid class.
**Parameters:** reason

- a String describing the reason for the exception.

---

#### Constructor Detail

InvalidClassException

```java
public InvalidClassException​(
String
reason)
```

Report an InvalidClassException for the reason specified.

**Parameters:** reason

- String describing the reason for the exception.

---

#### InvalidClassException

public InvalidClassException​(

String

reason)

Report an InvalidClassException for the reason specified.

InvalidClassException

```java
public InvalidClassException​(
String
cname,

String
reason)
```

Constructs an InvalidClassException object.

**Parameters:** cname

- a String naming the invalid class.
**Parameters:** reason

- a String describing the reason for the exception.

---

#### InvalidClassException

public InvalidClassException​(

String

cname,

String

reason)

Constructs an InvalidClassException object.

Method Detail

- getMessage

```java
public
String
getMessage()
```

Produce the message and include the classname, if present.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

Throwable

instance
(which may be

null

).

---

#### Method Detail

getMessage

```java
public
String
getMessage()
```

Produce the message and include the classname, if present.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

Throwable

instance
(which may be

null

).

---

#### getMessage

public

String

getMessage()

Produce the message and include the classname, if present.

---

