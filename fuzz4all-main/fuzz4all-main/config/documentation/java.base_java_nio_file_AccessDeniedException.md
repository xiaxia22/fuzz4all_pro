# Class AccessDeniedException

**Source:** `java.base\java\nio\file\AccessDeniedException.html`

### Class Description

```java
public class
AccessDeniedException

extends
FileSystemException
```

Checked exception thrown when a file system operation is denied, typically
due to a file permission or other access check.

This exception is not related to the

AccessControlException

or

SecurityException

thrown by access controllers or security managers when
access to a file is denied.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AccessDeniedException​(
String
file)

Constructs an instance of this class.

**Parameters:**
- file

- a string identifying the file or

null

if not known

---

#### public AccessDeniedException​(
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

#### Class AccessDeniedException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.AccessDeniedException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.AccessDeniedException

java.lang.Exception

- java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.AccessDeniedException

java.io.IOException

- java.nio.file.FileSystemException
- - java.nio.file.AccessDeniedException

java.nio.file.FileSystemException

- java.nio.file.AccessDeniedException

java.nio.file.AccessDeniedException

**All Implemented Interfaces:** Serializable

```java
public class
AccessDeniedException

extends
FileSystemException
```

Checked exception thrown when a file system operation is denied, typically
due to a file permission or other access check.

This exception is not related to the

AccessControlException

or

SecurityException

thrown by access controllers or security managers when
access to a file is denied.

**Since:** 1.7
**See Also:** Serialized Form

public class

AccessDeniedException

extends

FileSystemException

Checked exception thrown when a file system operation is denied, typically
due to a file permission or other access check.

This exception is not related to the

AccessControlException

or

SecurityException

thrown by access controllers or security managers when
access to a file is denied.

This exception is not related to the

AccessControlException

or

SecurityException

thrown by access controllers or security managers when
access to a file is denied.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessDeniedException

​(

String

file)

Constructs an instance of this class.

AccessDeniedException

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

AccessDeniedException

​(

String

file)

Constructs an instance of this class.

AccessDeniedException

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

- AccessDeniedException

```java
public AccessDeniedException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known

- AccessDeniedException

```java
public AccessDeniedException​(
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

- AccessDeniedException

```java
public AccessDeniedException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known

- AccessDeniedException

```java
public AccessDeniedException​(
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

AccessDeniedException

```java
public AccessDeniedException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known

---

#### AccessDeniedException

public AccessDeniedException​(

String

file)

Constructs an instance of this class.

AccessDeniedException

```java
public AccessDeniedException​(
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

#### AccessDeniedException

public AccessDeniedException​(

String

file,

String

other,

String

reason)

Constructs an instance of this class.

---

