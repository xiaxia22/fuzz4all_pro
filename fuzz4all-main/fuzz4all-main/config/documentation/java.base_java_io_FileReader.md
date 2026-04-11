# Class FileReader

**Source:** `java.base\java\io\FileReader.html`

### Class Description

```java
public class
FileReader

extends
InputStreamReader
```

Reads text from character files using a default buffer size. Decoding from bytes
to characters uses either a specified

charset

or the platform's

default charset

.

The

FileReader

is meant for reading streams of characters. For reading
streams of raw bytes, consider using a

FileInputStream

.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileReader​(
String
fileName)
throws
FileNotFoundException

Creates a new

FileReader

, given the name of the file to read,
using the platform's

default charset

.

**Parameters:**
- fileName

- the name of the file to read

**Throws:**
- FileNotFoundException

- if the named file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

---

#### public FileReader​(
File
file)
throws
FileNotFoundException

Creates a new

FileReader

, given the

File

to read,
using the platform's

default charset

.

**Parameters:**
- file

- the

File

to read

**Throws:**
- FileNotFoundException

- if the file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

---

#### public FileReader​(
FileDescriptor
fd)

Creates a new

FileReader

, given the

FileDescriptor

to read,
using the platform's

default charset

.

**Parameters:**
- fd

- the

FileDescriptor

to read

---

#### public FileReader​(
String
fileName,

Charset
charset)
throws
IOException

Creates a new

FileReader

, given the name of the file to read
and the

charset

.

**Parameters:**
- fileName

- the name of the file to read
- charset

- the

charset

**Throws:**
- IOException

- if the named file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

**Since:**
- 11

---

#### public FileReader​(
File
file,

Charset
charset)
throws
IOException

Creates a new

FileReader

, given the

File

to read and
the

charset

.

**Parameters:**
- file

- the

File

to read
- charset

- the

charset

**Throws:**
- IOException

- if the file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

**Since:**
- 11

---

### Method Details

*No entries found.*

### Additional Sections

#### Class FileReader

java.lang.Object

- java.io.Reader
- - java.io.InputStreamReader
- - java.io.FileReader

java.io.Reader

- java.io.InputStreamReader
- - java.io.FileReader

java.io.InputStreamReader

- java.io.FileReader

java.io.FileReader

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

```java
public class
FileReader

extends
InputStreamReader
```

Reads text from character files using a default buffer size. Decoding from bytes
to characters uses either a specified

charset

or the platform's

default charset

.

The

FileReader

is meant for reading streams of characters. For reading
streams of raw bytes, consider using a

FileInputStream

.

**Since:** 1.1
**See Also:** InputStreamReader

,

FileInputStream

public class

FileReader

extends

InputStreamReader

Reads text from character files using a default buffer size. Decoding from bytes
to characters uses either a specified

charset

or the platform's

default charset

.

The

FileReader

is meant for reading streams of characters. For reading
streams of raw bytes, consider using a

FileInputStream

.

The

FileReader

is meant for reading streams of characters. For reading
streams of raw bytes, consider using a

FileInputStream

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

Reader

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileReader

​(

File

file)

Creates a new

FileReader

, given the

File

to read,
using the platform's

default charset

.

FileReader

​(

FileDescriptor

fd)

Creates a new

FileReader

, given the

FileDescriptor

to read,
using the platform's

default charset

.

FileReader

​(

File

file,

Charset

charset)

Creates a new

FileReader

, given the

File

to read and
the

charset

.

FileReader

​(

String

fileName)

Creates a new

FileReader

, given the name of the file to read,
using the platform's

default charset

.

FileReader

​(

String

fileName,

Charset

charset)

Creates a new

FileReader

, given the name of the file to read
and the

charset

.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.io.

InputStreamReader

getEncoding

,

read

,

read

,

ready

- Methods declared in class java.io.

Reader

close

,

mark

,

markSupported

,

nullReader

,

read

,

read

,

reset

,

skip

,

transferTo

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

toString

,

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.io.

Reader

lock

---

#### Field Summary

Fields declared in class java.io.

Reader

lock

---

#### Fields declared in class java.io. Reader

Constructor Summary

Constructors

Constructor

Description

FileReader

​(

File

file)

Creates a new

FileReader

, given the

File

to read,
using the platform's

default charset

.

FileReader

​(

FileDescriptor

fd)

Creates a new

FileReader

, given the

FileDescriptor

to read,
using the platform's

default charset

.

FileReader

​(

File

file,

Charset

charset)

Creates a new

FileReader

, given the

File

to read and
the

charset

.

FileReader

​(

String

fileName)

Creates a new

FileReader

, given the name of the file to read,
using the platform's

default charset

.

FileReader

​(

String

fileName,

Charset

charset)

Creates a new

FileReader

, given the name of the file to read
and the

charset

.

---

#### Constructor Summary

Creates a new

FileReader

, given the

File

to read,
using the platform's

default charset

.

Creates a new

FileReader

, given the

FileDescriptor

to read,
using the platform's

default charset

.

Creates a new

FileReader

, given the

File

to read and
the

charset

.

Creates a new

FileReader

, given the name of the file to read,
using the platform's

default charset

.

Creates a new

FileReader

, given the name of the file to read
and the

charset

.

Method Summary

- Methods declared in class java.io.

InputStreamReader

getEncoding

,

read

,

read

,

ready

- Methods declared in class java.io.

Reader

close

,

mark

,

markSupported

,

nullReader

,

read

,

read

,

reset

,

skip

,

transferTo

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class java.io.

InputStreamReader

getEncoding

,

read

,

read

,

ready

---

#### Methods declared in class java.io. InputStreamReader

Methods declared in class java.io.

Reader

close

,

mark

,

markSupported

,

nullReader

,

read

,

read

,

reset

,

skip

,

transferTo

---

#### Methods declared in class java.io. Reader

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

toString

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

- FileReader

```java
public FileReader​(
String
fileName)
throws
FileNotFoundException
```

Creates a new

FileReader

, given the name of the file to read,
using the platform's

default charset

.

**Parameters:** fileName

- the name of the file to read
**Throws:** FileNotFoundException

- if the named file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

- FileReader

```java
public FileReader​(
File
file)
throws
FileNotFoundException
```

Creates a new

FileReader

, given the

File

to read,
using the platform's

default charset

.

**Parameters:** file

- the

File

to read
**Throws:** FileNotFoundException

- if the file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

- FileReader

```java
public FileReader​(
FileDescriptor
fd)
```

Creates a new

FileReader

, given the

FileDescriptor

to read,
using the platform's

default charset

.

**Parameters:** fd

- the

FileDescriptor

to read

- FileReader

```java
public FileReader​(
String
fileName,

Charset
charset)
throws
IOException
```

Creates a new

FileReader

, given the name of the file to read
and the

charset

.

**Parameters:** fileName

- the name of the file to read
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the named file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.
**Since:** 11

- FileReader

```java
public FileReader​(
File
file,

Charset
charset)
throws
IOException
```

Creates a new

FileReader

, given the

File

to read and
the

charset

.

**Parameters:** file

- the

File

to read
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.
**Since:** 11

Constructor Detail

- FileReader

```java
public FileReader​(
String
fileName)
throws
FileNotFoundException
```

Creates a new

FileReader

, given the name of the file to read,
using the platform's

default charset

.

**Parameters:** fileName

- the name of the file to read
**Throws:** FileNotFoundException

- if the named file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

- FileReader

```java
public FileReader​(
File
file)
throws
FileNotFoundException
```

Creates a new

FileReader

, given the

File

to read,
using the platform's

default charset

.

**Parameters:** file

- the

File

to read
**Throws:** FileNotFoundException

- if the file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

- FileReader

```java
public FileReader​(
FileDescriptor
fd)
```

Creates a new

FileReader

, given the

FileDescriptor

to read,
using the platform's

default charset

.

**Parameters:** fd

- the

FileDescriptor

to read

- FileReader

```java
public FileReader​(
String
fileName,

Charset
charset)
throws
IOException
```

Creates a new

FileReader

, given the name of the file to read
and the

charset

.

**Parameters:** fileName

- the name of the file to read
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the named file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.
**Since:** 11

- FileReader

```java
public FileReader​(
File
file,

Charset
charset)
throws
IOException
```

Creates a new

FileReader

, given the

File

to read and
the

charset

.

**Parameters:** file

- the

File

to read
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.
**Since:** 11

---

#### Constructor Detail

FileReader

```java
public FileReader​(
String
fileName)
throws
FileNotFoundException
```

Creates a new

FileReader

, given the name of the file to read,
using the platform's

default charset

.

**Parameters:** fileName

- the name of the file to read
**Throws:** FileNotFoundException

- if the named file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

---

#### FileReader

public FileReader​(

String

fileName)
throws

FileNotFoundException

Creates a new

FileReader

, given the name of the file to read,
using the platform's

default charset

.

FileReader

```java
public FileReader​(
File
file)
throws
FileNotFoundException
```

Creates a new

FileReader

, given the

File

to read,
using the platform's

default charset

.

**Parameters:** file

- the

File

to read
**Throws:** FileNotFoundException

- if the file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.

---

#### FileReader

public FileReader​(

File

file)
throws

FileNotFoundException

Creates a new

FileReader

, given the

File

to read,
using the platform's

default charset

.

FileReader

```java
public FileReader​(
FileDescriptor
fd)
```

Creates a new

FileReader

, given the

FileDescriptor

to read,
using the platform's

default charset

.

**Parameters:** fd

- the

FileDescriptor

to read

---

#### FileReader

public FileReader​(

FileDescriptor

fd)

Creates a new

FileReader

, given the

FileDescriptor

to read,
using the platform's

default charset

.

FileReader

```java
public FileReader​(
String
fileName,

Charset
charset)
throws
IOException
```

Creates a new

FileReader

, given the name of the file to read
and the

charset

.

**Parameters:** fileName

- the name of the file to read
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the named file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.
**Since:** 11

---

#### FileReader

public FileReader​(

String

fileName,

Charset

charset)
throws

IOException

Creates a new

FileReader

, given the name of the file to read
and the

charset

.

FileReader

```java
public FileReader​(
File
file,

Charset
charset)
throws
IOException
```

Creates a new

FileReader

, given the

File

to read and
the

charset

.

**Parameters:** file

- the

File

to read
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the file does not exist,
is a directory rather than a regular file,
or for some other reason cannot be opened for
reading.
**Since:** 11

---

#### FileReader

public FileReader​(

File

file,

Charset

charset)
throws

IOException

Creates a new

FileReader

, given the

File

to read and
the

charset

.

---

