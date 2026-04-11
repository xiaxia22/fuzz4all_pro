# Class NotLinkException

**Source:** `java.base\java\nio\file\NotLinkException.html`

### Class Description

```java
public class
NotLinkException

extends
FileSystemException
```

Checked exception thrown when a file system operation fails because a file
is not a symbolic link.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NotLinkException​(
String
file)

Constructs an instance of this class.

**Parameters:**
- file

- a string identifying the file or

null

if not known

---

#### public NotLinkException​(
String
file,

String
other,

String
reason)

Constructs an instance of this class.

**Parameters:**
- file

- a string identifying the file or

null

if not known
- other

- a string identifying the other file or

null

if not known
- reason

- a reason message with additional information or

null

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NotLinkException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.NotLinkException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.NotLinkException

java.lang.Exception

- java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.NotLinkException

java.io.IOException

- java.nio.file.FileSystemException
- - java.nio.file.NotLinkException

java.nio.file.FileSystemException

- java.nio.file.NotLinkException

java.nio.file.NotLinkException

**All Implemented Interfaces:** Serializable

```java
public class
NotLinkException

extends
FileSystemException
```

Checked exception thrown when a file system operation fails because a file
is not a symbolic link.

**Since:** 1.7
**See Also:** Serialized Form

public class

NotLinkException

extends

FileSystemException

Checked exception thrown when a file system operation fails because a file
is not a symbolic link.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NotLinkException

​(

String

file)

Constructs an instance of this class.

NotLinkException

​(

String

file,

String

other,

String

reason)

Constructs an instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.nio.file.

FileSystemException

getFile

,

getMessage

,

getOtherFile

,

getReason

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

Constructor Summary

Constructors

Constructor

Description

NotLinkException

​(

String

file)

Constructs an instance of this class.

NotLinkException

​(

String

file,

String

other,

String

reason)

Constructs an instance of this class.

---

#### Constructor Summary

Constructs an instance of this class.

Method Summary

- Methods declared in class java.nio.file.

FileSystemException

getFile

,

getMessage

,

getOtherFile

,

getReason

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

Methods declared in class java.nio.file.

FileSystemException

getFile

,

getMessage

,

getOtherFile

,

getReason

---

#### Methods declared in class java.nio.file. FileSystemException

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NotLinkException

```java
public NotLinkException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known

- NotLinkException

```java
public NotLinkException​(
String
file,

String
other,

String
reason)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known
**Parameters:** other

- a string identifying the other file or

null

if not known
**Parameters:** reason

- a reason message with additional information or

null

Constructor Detail

- NotLinkException

```java
public NotLinkException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known

- NotLinkException

```java
public NotLinkException​(
String
file,

String
other,

String
reason)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known
**Parameters:** other

- a string identifying the other file or

null

if not known
**Parameters:** reason

- a reason message with additional information or

null

---

#### Constructor Detail

NotLinkException

```java
public NotLinkException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known

---

#### NotLinkException

public NotLinkException​(

String

file)

Constructs an instance of this class.

NotLinkException

```java
public NotLinkException​(
String
file,

String
other,

String
reason)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known
**Parameters:** other

- a string identifying the other file or

null

if not known
**Parameters:** reason

- a reason message with additional information or

null

---

#### NotLinkException

public NotLinkException​(

String

file,

String

other,

String

reason)

Constructs an instance of this class.

---

