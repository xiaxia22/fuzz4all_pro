# Class UncheckedIOException

**Source:** `java.base\java\io\UncheckedIOException.html`

### Class Description

```java
public class
UncheckedIOException

extends
RuntimeException
```

Wraps an

IOException

with an unchecked exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UncheckedIOException​(
String
message,

IOException
cause)

Constructs an instance of this class.

**Parameters:**
- message

- the detail message, can be null
- cause

- the

IOException

**Throws:**
- NullPointerException

- if the cause is

null

---

#### public UncheckedIOException​(
IOException
cause)

Constructs an instance of this class.

**Parameters:**
- cause

- the

IOException

**Throws:**
- NullPointerException

- if the cause is

null

---

### Method Details

#### public
IOException
getCause()

Returns the cause of this exception.

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the

IOException

which is the cause of this exception.

---

### Additional Sections

#### Class UncheckedIOException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.io.UncheckedIOException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.io.UncheckedIOException

java.lang.Exception

- java.lang.RuntimeException
- - java.io.UncheckedIOException

java.lang.RuntimeException

- java.io.UncheckedIOException

java.io.UncheckedIOException

**All Implemented Interfaces:** Serializable

```java
public class
UncheckedIOException

extends
RuntimeException
```

Wraps an

IOException

with an unchecked exception.

**Since:** 1.8
**See Also:** Serialized Form

public class

UncheckedIOException

extends

RuntimeException

Wraps an

IOException

with an unchecked exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UncheckedIOException

​(

IOException

cause)

Constructs an instance of this class.

UncheckedIOException

​(

String

message,

IOException

cause)

Constructs an instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

IOException

getCause

()

Returns the cause of this exception.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

UncheckedIOException

​(

IOException

cause)

Constructs an instance of this class.

UncheckedIOException

​(

String

message,

IOException

cause)

Constructs an instance of this class.

---

#### Constructor Summary

Constructs an instance of this class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

IOException

getCause

()

Returns the cause of this exception.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

Returns the cause of this exception.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

- UncheckedIOException

```java
public UncheckedIOException​(
String
message,

IOException
cause)
```

Constructs an instance of this class.

**Parameters:** message

- the detail message, can be null
**Parameters:** cause

- the

IOException
**Throws:** NullPointerException

- if the cause is

null

- UncheckedIOException

```java
public UncheckedIOException​(
IOException
cause)
```

Constructs an instance of this class.

**Parameters:** cause

- the

IOException
**Throws:** NullPointerException

- if the cause is

null

============ METHOD DETAIL ==========

- Method Detail

- getCause

```java
public
IOException
getCause()
```

Returns the cause of this exception.

**Overrides:** getCause

in class

Throwable
**Returns:** the

IOException

which is the cause of this exception.

Constructor Detail

- UncheckedIOException

```java
public UncheckedIOException​(
String
message,

IOException
cause)
```

Constructs an instance of this class.

**Parameters:** message

- the detail message, can be null
**Parameters:** cause

- the

IOException
**Throws:** NullPointerException

- if the cause is

null

- UncheckedIOException

```java
public UncheckedIOException​(
IOException
cause)
```

Constructs an instance of this class.

**Parameters:** cause

- the

IOException
**Throws:** NullPointerException

- if the cause is

null

---

#### Constructor Detail

UncheckedIOException

```java
public UncheckedIOException​(
String
message,

IOException
cause)
```

Constructs an instance of this class.

**Parameters:** message

- the detail message, can be null
**Parameters:** cause

- the

IOException
**Throws:** NullPointerException

- if the cause is

null

---

#### UncheckedIOException

public UncheckedIOException​(

String

message,

IOException

cause)

Constructs an instance of this class.

UncheckedIOException

```java
public UncheckedIOException​(
IOException
cause)
```

Constructs an instance of this class.

**Parameters:** cause

- the

IOException
**Throws:** NullPointerException

- if the cause is

null

---

#### UncheckedIOException

public UncheckedIOException​(

IOException

cause)

Constructs an instance of this class.

Method Detail

- getCause

```java
public
IOException
getCause()
```

Returns the cause of this exception.

**Overrides:** getCause

in class

Throwable
**Returns:** the

IOException

which is the cause of this exception.

---

#### Method Detail

getCause

```java
public
IOException
getCause()
```

Returns the cause of this exception.

**Overrides:** getCause

in class

Throwable
**Returns:** the

IOException

which is the cause of this exception.

---

#### getCause

public

IOException

getCause()

Returns the cause of this exception.

---

