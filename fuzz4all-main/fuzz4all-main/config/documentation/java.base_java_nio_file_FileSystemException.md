# Class FileSystemException

**Source:** `java.base\java\nio\file\FileSystemException.html`

### Class Description

```java
public class
FileSystemException

extends
IOException
```

Thrown when a file system operation fails on one or two files. This class is
the general class for file system exceptions.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileSystemException​(
String
file)

Constructs an instance of this class. This constructor should be used
when an operation involving one file fails and there isn't any additional
information to explain the reason.

**Parameters:**
- file

- a string identifying the file or

null

if not known.

---

#### public FileSystemException​(
String
file,

String
other,

String
reason)

Constructs an instance of this class. This constructor should be used
when an operation involving two files fails, or there is additional
information to explain the reason.

**Parameters:**
- file

- a string identifying the file or

null

if not known.
- other

- a string identifying the other file or

null

if there
isn't another file or if not known
- reason

- a reason message with additional information or

null

---

### Method Details

#### public
String
getFile()

Returns the file used to create this exception.

**Returns:**
- the file (can be

null

)

---

#### public
String
getOtherFile()

Returns the other file used to create this exception.

**Returns:**
- the other file (can be

null

)

---

#### public
String
getReason()

Returns the string explaining why the file system operation failed.

**Returns:**
- the string explaining why the file system operation failed

---

#### public
String
getMessage()

Returns the detail message string.

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

#### Class FileSystemException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.nio.file.FileSystemException

java.lang.Exception

- java.io.IOException
- - java.nio.file.FileSystemException

java.io.IOException

- java.nio.file.FileSystemException

java.nio.file.FileSystemException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AccessDeniedException

,

AtomicMoveNotSupportedException

,

DirectoryNotEmptyException

,

FileAlreadyExistsException

,

FileSystemLoopException

,

NoSuchFileException

,

NotDirectoryException

,

NotLinkException

```java
public class
FileSystemException

extends
IOException
```

Thrown when a file system operation fails on one or two files. This class is
the general class for file system exceptions.

**Since:** 1.7
**See Also:** Serialized Form

public class

FileSystemException

extends

IOException

Thrown when a file system operation fails on one or two files. This class is
the general class for file system exceptions.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileSystemException

​(

String

file)

Constructs an instance of this class.

FileSystemException

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

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getFile

()

Returns the file used to create this exception.

String

getMessage

()

Returns the detail message string.

String

getOtherFile

()

Returns the other file used to create this exception.

String

getReason

()

Returns the string explaining why the file system operation failed.

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

FileSystemException

​(

String

file)

Constructs an instance of this class.

FileSystemException

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

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getFile

()

Returns the file used to create this exception.

String

getMessage

()

Returns the detail message string.

String

getOtherFile

()

Returns the other file used to create this exception.

String

getReason

()

Returns the string explaining why the file system operation failed.

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

Returns the file used to create this exception.

Returns the detail message string.

Returns the other file used to create this exception.

Returns the string explaining why the file system operation failed.

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

- FileSystemException

```java
public FileSystemException​(
String
file)
```

Constructs an instance of this class. This constructor should be used
when an operation involving one file fails and there isn't any additional
information to explain the reason.

**Parameters:** file

- a string identifying the file or

null

if not known.

- FileSystemException

```java
public FileSystemException​(
String
file,

String
other,

String
reason)
```

Constructs an instance of this class. This constructor should be used
when an operation involving two files fails, or there is additional
information to explain the reason.

**Parameters:** file

- a string identifying the file or

null

if not known.
**Parameters:** other

- a string identifying the other file or

null

if there
isn't another file or if not known
**Parameters:** reason

- a reason message with additional information or

null

============ METHOD DETAIL ==========

- Method Detail

- getFile

```java
public
String
getFile()
```

Returns the file used to create this exception.

**Returns:** the file (can be

null

)

- getOtherFile

```java
public
String
getOtherFile()
```

Returns the other file used to create this exception.

**Returns:** the other file (can be

null

)

- getReason

```java
public
String
getReason()
```

Returns the string explaining why the file system operation failed.

**Returns:** the string explaining why the file system operation failed

- getMessage

```java
public
String
getMessage()
```

Returns the detail message string.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

Throwable

instance
(which may be

null

).

Constructor Detail

- FileSystemException

```java
public FileSystemException​(
String
file)
```

Constructs an instance of this class. This constructor should be used
when an operation involving one file fails and there isn't any additional
information to explain the reason.

**Parameters:** file

- a string identifying the file or

null

if not known.

- FileSystemException

```java
public FileSystemException​(
String
file,

String
other,

String
reason)
```

Constructs an instance of this class. This constructor should be used
when an operation involving two files fails, or there is additional
information to explain the reason.

**Parameters:** file

- a string identifying the file or

null

if not known.
**Parameters:** other

- a string identifying the other file or

null

if there
isn't another file or if not known
**Parameters:** reason

- a reason message with additional information or

null

---

#### Constructor Detail

FileSystemException

```java
public FileSystemException​(
String
file)
```

Constructs an instance of this class. This constructor should be used
when an operation involving one file fails and there isn't any additional
information to explain the reason.

**Parameters:** file

- a string identifying the file or

null

if not known.

---

#### FileSystemException

public FileSystemException​(

String

file)

Constructs an instance of this class. This constructor should be used
when an operation involving one file fails and there isn't any additional
information to explain the reason.

FileSystemException

```java
public FileSystemException​(
String
file,

String
other,

String
reason)
```

Constructs an instance of this class. This constructor should be used
when an operation involving two files fails, or there is additional
information to explain the reason.

**Parameters:** file

- a string identifying the file or

null

if not known.
**Parameters:** other

- a string identifying the other file or

null

if there
isn't another file or if not known
**Parameters:** reason

- a reason message with additional information or

null

---

#### FileSystemException

public FileSystemException​(

String

file,

String

other,

String

reason)

Constructs an instance of this class. This constructor should be used
when an operation involving two files fails, or there is additional
information to explain the reason.

Method Detail

- getFile

```java
public
String
getFile()
```

Returns the file used to create this exception.

**Returns:** the file (can be

null

)

- getOtherFile

```java
public
String
getOtherFile()
```

Returns the other file used to create this exception.

**Returns:** the other file (can be

null

)

- getReason

```java
public
String
getReason()
```

Returns the string explaining why the file system operation failed.

**Returns:** the string explaining why the file system operation failed

- getMessage

```java
public
String
getMessage()
```

Returns the detail message string.

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

getFile

```java
public
String
getFile()
```

Returns the file used to create this exception.

**Returns:** the file (can be

null

)

---

#### getFile

public

String

getFile()

Returns the file used to create this exception.

getOtherFile

```java
public
String
getOtherFile()
```

Returns the other file used to create this exception.

**Returns:** the other file (can be

null

)

---

#### getOtherFile

public

String

getOtherFile()

Returns the other file used to create this exception.

getReason

```java
public
String
getReason()
```

Returns the string explaining why the file system operation failed.

**Returns:** the string explaining why the file system operation failed

---

#### getReason

public

String

getReason()

Returns the string explaining why the file system operation failed.

getMessage

```java
public
String
getMessage()
```

Returns the detail message string.

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

Returns the detail message string.

---

