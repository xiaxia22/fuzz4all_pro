# Class MalformedParametersException

**Source:** `java.base\java\lang\reflect\MalformedParametersException.html`

### Class Description

```java
public class
MalformedParametersException

extends
RuntimeException
```

Thrown when

the
java.lang.reflect package

attempts to read method parameters from
a class file and determines that one or more parameters are
malformed.

The following is a list of conditions under which this exception
can be thrown:

- The number of parameters (parameter_count) is wrong for the method

A constant pool index is out of bounds.

A constant pool index does not refer to a UTF-8 entry

A parameter's name is "", or contains an illegal character

The flags field contains an illegal flag (something other than
FINAL, SYNTHETIC, or MANDATED)

See

Executable.getParameters()

for more
information.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MalformedParametersException()

Create a

MalformedParametersException

with an empty
reason.

---

#### public MalformedParametersException​(
String
reason)

Create a

MalformedParametersException

.

**Parameters:**
- reason

- The reason for the exception.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class MalformedParametersException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.reflect.MalformedParametersException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.reflect.MalformedParametersException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.reflect.MalformedParametersException

java.lang.RuntimeException

- java.lang.reflect.MalformedParametersException

java.lang.reflect.MalformedParametersException

**All Implemented Interfaces:** Serializable

```java
public class
MalformedParametersException

extends
RuntimeException
```

Thrown when

the
java.lang.reflect package

attempts to read method parameters from
a class file and determines that one or more parameters are
malformed.

The following is a list of conditions under which this exception
can be thrown:

- The number of parameters (parameter_count) is wrong for the method

A constant pool index is out of bounds.

A constant pool index does not refer to a UTF-8 entry

A parameter's name is "", or contains an illegal character

The flags field contains an illegal flag (something other than
FINAL, SYNTHETIC, or MANDATED)

See

Executable.getParameters()

for more
information.

**Since:** 1.8
**See Also:** Executable.getParameters()

,

Serialized Form

public class

MalformedParametersException

extends

RuntimeException

Thrown when

the
java.lang.reflect package

attempts to read method parameters from
a class file and determines that one or more parameters are
malformed.

The following is a list of conditions under which this exception
can be thrown:

- The number of parameters (parameter_count) is wrong for the method

A constant pool index is out of bounds.

A constant pool index does not refer to a UTF-8 entry

A parameter's name is "", or contains an illegal character

The flags field contains an illegal flag (something other than
FINAL, SYNTHETIC, or MANDATED)

See

Executable.getParameters()

for more
information.

The following is a list of conditions under which this exception
can be thrown:

- The number of parameters (parameter_count) is wrong for the method

A constant pool index is out of bounds.

A constant pool index does not refer to a UTF-8 entry

A parameter's name is "", or contains an illegal character

The flags field contains an illegal flag (something other than
FINAL, SYNTHETIC, or MANDATED)

See

Executable.getParameters()

for more
information.

The number of parameters (parameter_count) is wrong for the method

A constant pool index is out of bounds.

A constant pool index does not refer to a UTF-8 entry

A parameter's name is "", or contains an illegal character

The flags field contains an illegal flag (something other than
FINAL, SYNTHETIC, or MANDATED)

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MalformedParametersException

()

Create a

MalformedParametersException

with an empty
reason.

MalformedParametersException

​(

String

reason)

Create a

MalformedParametersException

.

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

MalformedParametersException

()

Create a

MalformedParametersException

with an empty
reason.

MalformedParametersException

​(

String

reason)

Create a

MalformedParametersException

.

---

#### Constructor Summary

Create a

MalformedParametersException

with an empty
reason.

Create a

MalformedParametersException

.

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

- MalformedParametersException

```java
public MalformedParametersException()
```

Create a

MalformedParametersException

with an empty
reason.

- MalformedParametersException

```java
public MalformedParametersException​(
String
reason)
```

Create a

MalformedParametersException

.

**Parameters:** reason

- The reason for the exception.

Constructor Detail

- MalformedParametersException

```java
public MalformedParametersException()
```

Create a

MalformedParametersException

with an empty
reason.

- MalformedParametersException

```java
public MalformedParametersException​(
String
reason)
```

Create a

MalformedParametersException

.

**Parameters:** reason

- The reason for the exception.

---

#### Constructor Detail

MalformedParametersException

```java
public MalformedParametersException()
```

Create a

MalformedParametersException

with an empty
reason.

---

#### MalformedParametersException

public MalformedParametersException()

Create a

MalformedParametersException

with an empty
reason.

MalformedParametersException

```java
public MalformedParametersException​(
String
reason)
```

Create a

MalformedParametersException

.

**Parameters:** reason

- The reason for the exception.

---

#### MalformedParametersException

public MalformedParametersException​(

String

reason)

Create a

MalformedParametersException

.

---

