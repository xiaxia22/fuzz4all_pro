# Class FileSystemLoopException

**Source:** `java.base\java\nio\file\FileSystemLoopException.html`

### Class Description

```java
public class
FileSystemLoopException

extends
FileSystemException
```

Checked exception thrown when a file system loop, or cycle, is encountered.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileSystemLoopException​(
String
file)

Constructs an instance of this class.

**Parameters:**
- file

- a string identifying the file causing the cycle or

null

if
not known

---

### Method Details

*No entries found.*

### Additional Sections

#### Class FileSystemLoopException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.FileSystemLoopException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.FileSystemLoopException

java.lang.Exception

- java.io.IOException
- - java.nio.file.FileSystemException
- - java.nio.file.FileSystemLoopException

java.io.IOException

- java.nio.file.FileSystemException
- - java.nio.file.FileSystemLoopException

java.nio.file.FileSystemException

- java.nio.file.FileSystemLoopException

java.nio.file.FileSystemLoopException

**All Implemented Interfaces:** Serializable

```java
public class
FileSystemLoopException

extends
FileSystemException
```

Checked exception thrown when a file system loop, or cycle, is encountered.

**Since:** 1.7
**See Also:** Files.walkFileTree(java.nio.file.Path, java.util.Set<java.nio.file.FileVisitOption>, int, java.nio.file.FileVisitor<? super java.nio.file.Path>)

,

Serialized Form

public class

FileSystemLoopException

extends

FileSystemException

Checked exception thrown when a file system loop, or cycle, is encountered.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileSystemLoopException

​(

String

file)

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

FileSystemLoopException

​(

String

file)

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

- FileSystemLoopException

```java
public FileSystemLoopException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file causing the cycle or

null

if
not known

Constructor Detail

- FileSystemLoopException

```java
public FileSystemLoopException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file causing the cycle or

null

if
not known

---

#### Constructor Detail

FileSystemLoopException

```java
public FileSystemLoopException​(
String
file)
```

Constructs an instance of this class.

**Parameters:** file

- a string identifying the file causing the cycle or

null

if
not known

---

#### FileSystemLoopException

public FileSystemLoopException​(

String

file)

Constructs an instance of this class.

---

