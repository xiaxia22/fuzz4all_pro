# Class FileAlreadyExistsException

**Source:** `java.base\java\nio\file\FileAlreadyExistsException.html`

### Class Description

```java
public class
FileAlreadyExistsException

extends
FileSystemException
```

Checked exception thrown when an attempt is made to create a file or
directory and a file of that name already exists.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileAlreadyExistsException​(
String
file)

Constructs an instance of this class.

**Parameters:**
- file

- a string identifying the file or

null

if not known

---

#### public FileAlreadyExistsException​(
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

#### Class FileAlreadyExistsException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.FileAlreadyExistsException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.FileAlreadyExistsException

java.lang.Exception

- java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.FileAlreadyExistsException

java.io.IOException

- java.nio.file.FileSystemException
- - java.nio.file.FileAlreadyExistsException

java.nio.file.FileSystemException

- java.nio.file.FileAlreadyExistsException

java.nio.file.FileAlreadyExistsException

**All Implemented Interfaces:** Serializable

```java
public class
FileAlreadyExistsException

extends
FileSystemException
```

Checked exception thrown when an attempt is made to create a file or
directory and a file of that name already exists.

**Since:** 1.7
**See Also:** Serialized Form

public class

FileAlreadyExistsException

extends

FileSystemException

Checked exception thrown when an attempt is made to create a file or
directory and a file of that name already exists.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileAlreadyExistsException

​(

String

file)

Constructs an instance of this class.

FileAlreadyExistsException

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

FileAlreadyExistsException

​(

String

file)

Constructs an instance of this class.

FileAlreadyExistsException

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

- FileAlreadyExistsException

```java
public FileAlreadyExistsException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known

- FileAlreadyExistsException

```java
public FileAlreadyExistsException​(
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

- FileAlreadyExistsException

```java
public FileAlreadyExistsException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known

- FileAlreadyExistsException

```java
public FileAlreadyExistsException​(
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

FileAlreadyExistsException

```java
public FileAlreadyExistsException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file or

null

if not known

---

#### FileAlreadyExistsException

public FileAlreadyExistsException​(

String

file)

Constructs an instance of this class.

FileAlreadyExistsException

```java
public FileAlreadyExistsException​(
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

#### FileAlreadyExistsException

public FileAlreadyExistsException​(

String

file,

String

other,

String

reason)

Constructs an instance of this class.

---

