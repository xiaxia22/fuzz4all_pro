# Class FileNotFoundException

**Source:** `java.base\java\io\FileNotFoundException.html`

### Class Description

```java
public class
FileNotFoundException

extends
IOException
```

Signals that an attempt to open the file denoted by a specified pathname
has failed.

This exception will be thrown by the

FileInputStream

,

FileOutputStream

, and

RandomAccessFile

constructors when a file
with the specified pathname does not exist. It will also be thrown by these
constructors if the file does exist but for some reason is inaccessible, for
example when an attempt is made to open a read-only file for writing.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileNotFoundException()

Constructs a

FileNotFoundException

with

null

as its error detail message.

---

#### public FileNotFoundException​(
String
s)

Constructs a

FileNotFoundException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

**Parameters:**
- s

- the detail message.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class FileNotFoundException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.io.FileNotFoundException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.io.FileNotFoundException

java.lang.Exception

- java.io.IOException
- - java.io.FileNotFoundException

java.io.IOException

- java.io.FileNotFoundException

java.io.FileNotFoundException

**All Implemented Interfaces:** Serializable

```java
public class
FileNotFoundException

extends
IOException
```

Signals that an attempt to open the file denoted by a specified pathname
has failed.

This exception will be thrown by the

FileInputStream

,

FileOutputStream

, and

RandomAccessFile

constructors when a file
with the specified pathname does not exist. It will also be thrown by these
constructors if the file does exist but for some reason is inaccessible, for
example when an attempt is made to open a read-only file for writing.

**Since:** 1.0
**See Also:** Serialized Form

public class

FileNotFoundException

extends

IOException

Signals that an attempt to open the file denoted by a specified pathname
has failed.

This exception will be thrown by the

FileInputStream

,

FileOutputStream

, and

RandomAccessFile

constructors when a file
with the specified pathname does not exist. It will also be thrown by these
constructors if the file does exist but for some reason is inaccessible, for
example when an attempt is made to open a read-only file for writing.

This exception will be thrown by the

FileInputStream

,

FileOutputStream

, and

RandomAccessFile

constructors when a file
with the specified pathname does not exist. It will also be thrown by these
constructors if the file does exist but for some reason is inaccessible, for
example when an attempt is made to open a read-only file for writing.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileNotFoundException

()

Constructs a

FileNotFoundException

with

null

as its error detail message.

FileNotFoundException

​(

String

s)

Constructs a

FileNotFoundException

with the
specified detail message.

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

FileNotFoundException

()

Constructs a

FileNotFoundException

with

null

as its error detail message.

FileNotFoundException

​(

String

s)

Constructs a

FileNotFoundException

with the
specified detail message.

---

#### Constructor Summary

Constructs a

FileNotFoundException

with

null

as its error detail message.

Constructs a

FileNotFoundException

with the
specified detail message.

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

- FileNotFoundException

```java
public FileNotFoundException()
```

Constructs a

FileNotFoundException

with

null

as its error detail message.

- FileNotFoundException

```java
public FileNotFoundException​(
String
s)
```

Constructs a

FileNotFoundException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

**Parameters:** s

- the detail message.

Constructor Detail

- FileNotFoundException

```java
public FileNotFoundException()
```

Constructs a

FileNotFoundException

with

null

as its error detail message.

- FileNotFoundException

```java
public FileNotFoundException​(
String
s)
```

Constructs a

FileNotFoundException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

**Parameters:** s

- the detail message.

---

#### Constructor Detail

FileNotFoundException

```java
public FileNotFoundException()
```

Constructs a

FileNotFoundException

with

null

as its error detail message.

---

#### FileNotFoundException

public FileNotFoundException()

Constructs a

FileNotFoundException

with

null

as its error detail message.

FileNotFoundException

```java
public FileNotFoundException​(
String
s)
```

Constructs a

FileNotFoundException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

**Parameters:** s

- the detail message.

---

#### FileNotFoundException

public FileNotFoundException​(

String

s)

Constructs a

FileNotFoundException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

---

