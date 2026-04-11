# Class DirectoryIteratorException

**Source:** `java.base\java\nio\file\DirectoryIteratorException.html`

### Class Description

```java
public final class
DirectoryIteratorException

extends
ConcurrentModificationException
```

Runtime exception thrown if an I/O error is encountered when iterating over
the entries in a directory. The I/O error is retrieved as an

IOException

using the

getCause()

method.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DirectoryIteratorException​(
IOException
cause)

Constructs an instance of this class.

**Parameters:**
- cause

- the

IOException

that caused the directory iteration
to fail

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
- the cause

---

### Additional Sections

#### Class DirectoryIteratorException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.util.ConcurrentModificationException
- - java.nio.file.DirectoryIteratorException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.util.ConcurrentModificationException
- - java.nio.file.DirectoryIteratorException

java.lang.Exception

- java.lang.RuntimeException
- - java.util.ConcurrentModificationException
- - java.nio.file.DirectoryIteratorException

java.lang.RuntimeException

- java.util.ConcurrentModificationException
- - java.nio.file.DirectoryIteratorException

java.util.ConcurrentModificationException

- java.nio.file.DirectoryIteratorException

java.nio.file.DirectoryIteratorException

**All Implemented Interfaces:** Serializable

```java
public final class
DirectoryIteratorException

extends
ConcurrentModificationException
```

Runtime exception thrown if an I/O error is encountered when iterating over
the entries in a directory. The I/O error is retrieved as an

IOException

using the

getCause()

method.

**Since:** 1.7
**See Also:** DirectoryStream

,

Serialized Form

public final class

DirectoryIteratorException

extends

ConcurrentModificationException

Runtime exception thrown if an I/O error is encountered when iterating over
the entries in a directory. The I/O error is retrieved as an

IOException

using the

getCause()

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DirectoryIteratorException

​(

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

DirectoryIteratorException

​(

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

- DirectoryIteratorException

```java
public DirectoryIteratorException​(
IOException
cause)
```

Constructs an instance of this class.

**Parameters:** cause

- the

IOException

that caused the directory iteration
to fail
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
**Returns:** the cause

Constructor Detail

- DirectoryIteratorException

```java
public DirectoryIteratorException​(
IOException
cause)
```

Constructs an instance of this class.

**Parameters:** cause

- the

IOException

that caused the directory iteration
to fail
**Throws:** NullPointerException

- if the cause is

null

---

#### Constructor Detail

DirectoryIteratorException

```java
public DirectoryIteratorException​(
IOException
cause)
```

Constructs an instance of this class.

**Parameters:** cause

- the

IOException

that caused the directory iteration
to fail
**Throws:** NullPointerException

- if the cause is

null

---

#### DirectoryIteratorException

public DirectoryIteratorException​(

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
**Returns:** the cause

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
**Returns:** the cause

---

#### getCause

public

IOException

getCause()

Returns the cause of this exception.

---

