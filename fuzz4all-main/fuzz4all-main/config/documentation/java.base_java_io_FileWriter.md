# Class FileWriter

**Source:** `java.base\java\io\FileWriter.html`

### Class Description

```java
public class
FileWriter

extends
OutputStreamWriter
```

Writes text to character files using a default buffer size. Encoding from characters
to bytes uses either a specified

charset

or the platform's

default charset

.

Whether or not a file is available or may be created depends upon the
underlying platform. Some platforms, in particular, allow a file to be
opened for writing by only one

FileWriter

(or other file-writing
object) at a time. In such situations the constructors in this class
will fail if the file involved is already open.

The

FileWriter

is meant for writing streams of characters. For writing
streams of raw bytes, consider using a

FileOutputStream

.

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileWriter​(
String
fileName)
throws
IOException

Constructs a

FileWriter

given a file name, using the platform's

default charset

**Parameters:**
- fileName

- String The system-dependent filename.

**Throws:**
- IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

---

#### public FileWriter​(
String
fileName,
boolean append)
throws
IOException

Constructs a

FileWriter

given a file name and a boolean indicating
whether to append the data written, using the platform's

default charset

.

**Parameters:**
- fileName

- String The system-dependent filename.
- append

- boolean if

true

, then data will be written
to the end of the file rather than the beginning.

**Throws:**
- IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

---

#### public FileWriter​(
File
file)
throws
IOException

Constructs a

FileWriter

given the

File

to write,
using the platform's

default charset

**Parameters:**
- file

- the

File

to write.

**Throws:**
- IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason

---

#### public FileWriter​(
File
file,
boolean append)
throws
IOException

Constructs a

FileWriter

given the

File

to write and
a boolean indicating whether to append the data written, using the platform's

default charset

.

**Parameters:**
- file

- the

File

to write
- append

- if

true

, then bytes will be written
to the end of the file rather than the beginning

**Throws:**
- IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason

**Since:**
- 1.4

---

#### public FileWriter​(
FileDescriptor
fd)

Constructs a

FileWriter

given a file descriptor,
using the platform's

default charset

.

**Parameters:**
- fd

- the

FileDescriptor

to write.

---

#### public FileWriter​(
String
fileName,

Charset
charset)
throws
IOException

Constructs a

FileWriter

given a file name and

charset

.

**Parameters:**
- fileName

- the name of the file to write
- charset

- the

charset

**Throws:**
- IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

**Since:**
- 11

---

#### public FileWriter​(
String
fileName,

Charset
charset,
boolean append)
throws
IOException

Constructs a

FileWriter

given a file name,

charset

and a boolean indicating
whether to append the data written.

**Parameters:**
- fileName

- the name of the file to write
- charset

- the

charset
- append

- a boolean. If

true

, the writer will write the data
to the end of the file rather than the beginning.

**Throws:**
- IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

**Since:**
- 11

---

#### public FileWriter​(
File
file,

Charset
charset)
throws
IOException

Constructs a

FileWriter

given the

File

to write and

charset

.

**Parameters:**
- file

- the

File

to write
- charset

- the

charset

**Throws:**
- IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason

**Since:**
- 11

---

#### public FileWriter​(
File
file,

Charset
charset,
boolean append)
throws
IOException

Constructs a

FileWriter

given the

File

to write,

charset

and a boolean indicating
whether to append the data written.

**Parameters:**
- file

- the

File

to write
- charset

- the

charset
- append

- a boolean. If

true

, the writer will write the data
to the end of the file rather than the beginning.

**Throws:**
- IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason

**Since:**
- 11

---

### Method Details

*No entries found.*

### Additional Sections

#### Class FileWriter

java.lang.Object

- java.io.Writer
- - java.io.OutputStreamWriter
- - java.io.FileWriter

java.io.Writer

- java.io.OutputStreamWriter
- - java.io.FileWriter

java.io.OutputStreamWriter

- java.io.FileWriter

java.io.FileWriter

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

```java
public class
FileWriter

extends
OutputStreamWriter
```

Writes text to character files using a default buffer size. Encoding from characters
to bytes uses either a specified

charset

or the platform's

default charset

.

Whether or not a file is available or may be created depends upon the
underlying platform. Some platforms, in particular, allow a file to be
opened for writing by only one

FileWriter

(or other file-writing
object) at a time. In such situations the constructors in this class
will fail if the file involved is already open.

The

FileWriter

is meant for writing streams of characters. For writing
streams of raw bytes, consider using a

FileOutputStream

.

**Since:** 1.1
**See Also:** OutputStreamWriter

,

FileOutputStream

public class

FileWriter

extends

OutputStreamWriter

Writes text to character files using a default buffer size. Encoding from characters
to bytes uses either a specified

charset

or the platform's

default charset

.

Whether or not a file is available or may be created depends upon the
underlying platform. Some platforms, in particular, allow a file to be
opened for writing by only one

FileWriter

(or other file-writing
object) at a time. In such situations the constructors in this class
will fail if the file involved is already open.

The

FileWriter

is meant for writing streams of characters. For writing
streams of raw bytes, consider using a

FileOutputStream

.

Whether or not a file is available or may be created depends upon the
underlying platform. Some platforms, in particular, allow a file to be
opened for writing by only one

FileWriter

(or other file-writing
object) at a time. In such situations the constructors in this class
will fail if the file involved is already open.

The

FileWriter

is meant for writing streams of characters. For writing
streams of raw bytes, consider using a

FileOutputStream

.

The

FileWriter

is meant for writing streams of characters. For writing
streams of raw bytes, consider using a

FileOutputStream

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

Writer

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileWriter

​(

File

file)

Constructs a

FileWriter

given the

File

to write,
using the platform's

default charset

FileWriter

​(

FileDescriptor

fd)

Constructs a

FileWriter

given a file descriptor,
using the platform's

default charset

.

FileWriter

​(

File

file,
boolean append)

Constructs a

FileWriter

given the

File

to write and
a boolean indicating whether to append the data written, using the platform's

default charset

.

FileWriter

​(

File

file,

Charset

charset)

Constructs a

FileWriter

given the

File

to write and

charset

.

FileWriter

​(

File

file,

Charset

charset,
boolean append)

Constructs a

FileWriter

given the

File

to write,

charset

and a boolean indicating
whether to append the data written.

FileWriter

​(

String

fileName)

Constructs a

FileWriter

given a file name, using the platform's

default charset

FileWriter

​(

String

fileName,
boolean append)

Constructs a

FileWriter

given a file name and a boolean indicating
whether to append the data written, using the platform's

default charset

.

FileWriter

​(

String

fileName,

Charset

charset)

Constructs a

FileWriter

given a file name and

charset

.

FileWriter

​(

String

fileName,

Charset

charset,
boolean append)

Constructs a

FileWriter

given a file name,

charset

and a boolean indicating
whether to append the data written.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.io.

OutputStreamWriter

flush

,

getEncoding

,

write

,

write

,

write

- Methods declared in class java.io.

Writer

append

,

append

,

append

,

close

,

nullWriter

,

write

,

write

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

Writer

lock

---

#### Field Summary

Fields declared in class java.io.

Writer

lock

---

#### Fields declared in class java.io. Writer

Constructor Summary

Constructors

Constructor

Description

FileWriter

​(

File

file)

Constructs a

FileWriter

given the

File

to write,
using the platform's

default charset

FileWriter

​(

FileDescriptor

fd)

Constructs a

FileWriter

given a file descriptor,
using the platform's

default charset

.

FileWriter

​(

File

file,
boolean append)

Constructs a

FileWriter

given the

File

to write and
a boolean indicating whether to append the data written, using the platform's

default charset

.

FileWriter

​(

File

file,

Charset

charset)

Constructs a

FileWriter

given the

File

to write and

charset

.

FileWriter

​(

File

file,

Charset

charset,
boolean append)

Constructs a

FileWriter

given the

File

to write,

charset

and a boolean indicating
whether to append the data written.

FileWriter

​(

String

fileName)

Constructs a

FileWriter

given a file name, using the platform's

default charset

FileWriter

​(

String

fileName,
boolean append)

Constructs a

FileWriter

given a file name and a boolean indicating
whether to append the data written, using the platform's

default charset

.

FileWriter

​(

String

fileName,

Charset

charset)

Constructs a

FileWriter

given a file name and

charset

.

FileWriter

​(

String

fileName,

Charset

charset,
boolean append)

Constructs a

FileWriter

given a file name,

charset

and a boolean indicating
whether to append the data written.

---

#### Constructor Summary

Constructs a

FileWriter

given the

File

to write,
using the platform's

default charset

Constructs a

FileWriter

given a file descriptor,
using the platform's

default charset

.

Constructs a

FileWriter

given the

File

to write and
a boolean indicating whether to append the data written, using the platform's

default charset

.

Constructs a

FileWriter

given the

File

to write and

charset

.

Constructs a

FileWriter

given the

File

to write,

charset

and a boolean indicating
whether to append the data written.

Constructs a

FileWriter

given a file name, using the platform's

default charset

Constructs a

FileWriter

given a file name and a boolean indicating
whether to append the data written, using the platform's

default charset

.

Constructs a

FileWriter

given a file name and

charset

.

Constructs a

FileWriter

given a file name,

charset

and a boolean indicating
whether to append the data written.

Method Summary

- Methods declared in class java.io.

OutputStreamWriter

flush

,

getEncoding

,

write

,

write

,

write

- Methods declared in class java.io.

Writer

append

,

append

,

append

,

close

,

nullWriter

,

write

,

write

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

OutputStreamWriter

flush

,

getEncoding

,

write

,

write

,

write

---

#### Methods declared in class java.io. OutputStreamWriter

Methods declared in class java.io.

Writer

append

,

append

,

append

,

close

,

nullWriter

,

write

,

write

---

#### Methods declared in class java.io. Writer

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

- FileWriter

```java
public FileWriter​(
String
fileName)
throws
IOException
```

Constructs a

FileWriter

given a file name, using the platform's

default charset

**Parameters:** fileName

- String The system-dependent filename.
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

- FileWriter

```java
public FileWriter​(
String
fileName,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given a file name and a boolean indicating
whether to append the data written, using the platform's

default charset

.

**Parameters:** fileName

- String The system-dependent filename.
**Parameters:** append

- boolean if

true

, then data will be written
to the end of the file rather than the beginning.
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

- FileWriter

```java
public FileWriter​(
File
file)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write,
using the platform's

default charset

**Parameters:** file

- the

File

to write.
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason

- FileWriter

```java
public FileWriter​(
File
file,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write and
a boolean indicating whether to append the data written, using the platform's

default charset

.

**Parameters:** file

- the

File

to write
**Parameters:** append

- if

true

, then bytes will be written
to the end of the file rather than the beginning
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason
**Since:** 1.4

- FileWriter

```java
public FileWriter​(
FileDescriptor
fd)
```

Constructs a

FileWriter

given a file descriptor,
using the platform's

default charset

.

**Parameters:** fd

- the

FileDescriptor

to write.

- FileWriter

```java
public FileWriter​(
String
fileName,

Charset
charset)
throws
IOException
```

Constructs a

FileWriter

given a file name and

charset

.

**Parameters:** fileName

- the name of the file to write
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason
**Since:** 11

- FileWriter

```java
public FileWriter​(
String
fileName,

Charset
charset,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given a file name,

charset

and a boolean indicating
whether to append the data written.

**Parameters:** fileName

- the name of the file to write
**Parameters:** charset

- the

charset
**Parameters:** append

- a boolean. If

true

, the writer will write the data
to the end of the file rather than the beginning.
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason
**Since:** 11

- FileWriter

```java
public FileWriter​(
File
file,

Charset
charset)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write and

charset

.

**Parameters:** file

- the

File

to write
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason
**Since:** 11

- FileWriter

```java
public FileWriter​(
File
file,

Charset
charset,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write,

charset

and a boolean indicating
whether to append the data written.

**Parameters:** file

- the

File

to write
**Parameters:** charset

- the

charset
**Parameters:** append

- a boolean. If

true

, the writer will write the data
to the end of the file rather than the beginning.
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason
**Since:** 11

Constructor Detail

- FileWriter

```java
public FileWriter​(
String
fileName)
throws
IOException
```

Constructs a

FileWriter

given a file name, using the platform's

default charset

**Parameters:** fileName

- String The system-dependent filename.
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

- FileWriter

```java
public FileWriter​(
String
fileName,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given a file name and a boolean indicating
whether to append the data written, using the platform's

default charset

.

**Parameters:** fileName

- String The system-dependent filename.
**Parameters:** append

- boolean if

true

, then data will be written
to the end of the file rather than the beginning.
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

- FileWriter

```java
public FileWriter​(
File
file)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write,
using the platform's

default charset

**Parameters:** file

- the

File

to write.
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason

- FileWriter

```java
public FileWriter​(
File
file,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write and
a boolean indicating whether to append the data written, using the platform's

default charset

.

**Parameters:** file

- the

File

to write
**Parameters:** append

- if

true

, then bytes will be written
to the end of the file rather than the beginning
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason
**Since:** 1.4

- FileWriter

```java
public FileWriter​(
FileDescriptor
fd)
```

Constructs a

FileWriter

given a file descriptor,
using the platform's

default charset

.

**Parameters:** fd

- the

FileDescriptor

to write.

- FileWriter

```java
public FileWriter​(
String
fileName,

Charset
charset)
throws
IOException
```

Constructs a

FileWriter

given a file name and

charset

.

**Parameters:** fileName

- the name of the file to write
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason
**Since:** 11

- FileWriter

```java
public FileWriter​(
String
fileName,

Charset
charset,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given a file name,

charset

and a boolean indicating
whether to append the data written.

**Parameters:** fileName

- the name of the file to write
**Parameters:** charset

- the

charset
**Parameters:** append

- a boolean. If

true

, the writer will write the data
to the end of the file rather than the beginning.
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason
**Since:** 11

- FileWriter

```java
public FileWriter​(
File
file,

Charset
charset)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write and

charset

.

**Parameters:** file

- the

File

to write
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason
**Since:** 11

- FileWriter

```java
public FileWriter​(
File
file,

Charset
charset,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write,

charset

and a boolean indicating
whether to append the data written.

**Parameters:** file

- the

File

to write
**Parameters:** charset

- the

charset
**Parameters:** append

- a boolean. If

true

, the writer will write the data
to the end of the file rather than the beginning.
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason
**Since:** 11

---

#### Constructor Detail

FileWriter

```java
public FileWriter​(
String
fileName)
throws
IOException
```

Constructs a

FileWriter

given a file name, using the platform's

default charset

**Parameters:** fileName

- String The system-dependent filename.
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

---

#### FileWriter

public FileWriter​(

String

fileName)
throws

IOException

Constructs a

FileWriter

given a file name, using the platform's

default charset

FileWriter

```java
public FileWriter​(
String
fileName,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given a file name and a boolean indicating
whether to append the data written, using the platform's

default charset

.

**Parameters:** fileName

- String The system-dependent filename.
**Parameters:** append

- boolean if

true

, then data will be written
to the end of the file rather than the beginning.
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason

---

#### FileWriter

public FileWriter​(

String

fileName,
boolean append)
throws

IOException

Constructs a

FileWriter

given a file name and a boolean indicating
whether to append the data written, using the platform's

default charset

.

FileWriter

```java
public FileWriter​(
File
file)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write,
using the platform's

default charset

**Parameters:** file

- the

File

to write.
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason

---

#### FileWriter

public FileWriter​(

File

file)
throws

IOException

Constructs a

FileWriter

given the

File

to write,
using the platform's

default charset

FileWriter

```java
public FileWriter​(
File
file,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write and
a boolean indicating whether to append the data written, using the platform's

default charset

.

**Parameters:** file

- the

File

to write
**Parameters:** append

- if

true

, then bytes will be written
to the end of the file rather than the beginning
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason
**Since:** 1.4

---

#### FileWriter

public FileWriter​(

File

file,
boolean append)
throws

IOException

Constructs a

FileWriter

given the

File

to write and
a boolean indicating whether to append the data written, using the platform's

default charset

.

FileWriter

```java
public FileWriter​(
FileDescriptor
fd)
```

Constructs a

FileWriter

given a file descriptor,
using the platform's

default charset

.

**Parameters:** fd

- the

FileDescriptor

to write.

---

#### FileWriter

public FileWriter​(

FileDescriptor

fd)

Constructs a

FileWriter

given a file descriptor,
using the platform's

default charset

.

FileWriter

```java
public FileWriter​(
String
fileName,

Charset
charset)
throws
IOException
```

Constructs a

FileWriter

given a file name and

charset

.

**Parameters:** fileName

- the name of the file to write
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason
**Since:** 11

---

#### FileWriter

public FileWriter​(

String

fileName,

Charset

charset)
throws

IOException

Constructs a

FileWriter

given a file name and

charset

.

FileWriter

```java
public FileWriter​(
String
fileName,

Charset
charset,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given a file name,

charset

and a boolean indicating
whether to append the data written.

**Parameters:** fileName

- the name of the file to write
**Parameters:** charset

- the

charset
**Parameters:** append

- a boolean. If

true

, the writer will write the data
to the end of the file rather than the beginning.
**Throws:** IOException

- if the named file exists but is a directory rather
than a regular file, does not exist but cannot be
created, or cannot be opened for any other reason
**Since:** 11

---

#### FileWriter

public FileWriter​(

String

fileName,

Charset

charset,
boolean append)
throws

IOException

Constructs a

FileWriter

given a file name,

charset

and a boolean indicating
whether to append the data written.

FileWriter

```java
public FileWriter​(
File
file,

Charset
charset)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write and

charset

.

**Parameters:** file

- the

File

to write
**Parameters:** charset

- the

charset
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason
**Since:** 11

---

#### FileWriter

public FileWriter​(

File

file,

Charset

charset)
throws

IOException

Constructs a

FileWriter

given the

File

to write and

charset

.

FileWriter

```java
public FileWriter​(
File
file,

Charset
charset,
boolean append)
throws
IOException
```

Constructs a

FileWriter

given the

File

to write,

charset

and a boolean indicating
whether to append the data written.

**Parameters:** file

- the

File

to write
**Parameters:** charset

- the

charset
**Parameters:** append

- a boolean. If

true

, the writer will write the data
to the end of the file rather than the beginning.
**Throws:** IOException

- if the file exists but is a directory rather than
a regular file, does not exist but cannot be created,
or cannot be opened for any other reason
**Since:** 11

---

#### FileWriter

public FileWriter​(

File

file,

Charset

charset,
boolean append)
throws

IOException

Constructs a

FileWriter

given the

File

to write,

charset

and a boolean indicating
whether to append the data written.

---

