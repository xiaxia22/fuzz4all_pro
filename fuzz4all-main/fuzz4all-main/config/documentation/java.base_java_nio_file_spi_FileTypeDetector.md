# Class FileTypeDetector

**Source:** `java.base\java\nio\file\spi\FileTypeDetector.html`

### Class Description

```java
public abstract class
FileTypeDetector

extends
Object
```

A file type detector for probing a file to guess its file type.

A file type detector is a concrete implementation of this class, has a
zero-argument constructor, and implements the abstract methods specified
below.

The means by which a file type detector determines the file type is
highly implementation specific. A simple implementation might examine the

file extension

(a convention used in some platforms) and map it to
a file type. In other cases, the file type may be stored as a file

attribute

or the bytes in a
file may be examined to guess its file type.

**Since:** 1.7
**See Also:** Files.probeContentType(Path)

---

### Field Details

*No entries found.*

### Constructor Details

#### protected FileTypeDetector()

Initializes a new instance of this class.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("fileTypeDetector")

---

### Method Details

#### public abstract
String
probeContentType​(
Path
path)
throws
IOException

Probes the given file to guess its content type.

The means by which this method determines the file type is highly
implementation specific. It may simply examine the file name, it may use
a file

attribute

,
or it may examines bytes in the file.

The probe result is the string form of the value of a
Multipurpose Internet Mail Extension (MIME) content type as
defined by

RFC 2045:
Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet
Message Bodies

. The string must be parsable according to the
grammar in the RFC 2045.

**Parameters:**
- path

- the path to the file to probe

**Returns:**
- The content type or

null

if the file type is not
recognized

**Throws:**
- IOException

- An I/O error occurs
- SecurityException

- If the implementation requires to access the file, and a
security manager is installed, and it denies an unspecified
permission required by a file system provider implementation.
If the file reference is associated with the default file system
provider then the

SecurityManager.checkRead(String)

method
is invoked to check read access to the file.

**See Also:**
- Files.probeContentType(java.nio.file.Path)

---

### Additional Sections

#### Class FileTypeDetector

java.lang.Object

- java.nio.file.spi.FileTypeDetector

java.nio.file.spi.FileTypeDetector

```java
public abstract class
FileTypeDetector

extends
Object
```

A file type detector for probing a file to guess its file type.

A file type detector is a concrete implementation of this class, has a
zero-argument constructor, and implements the abstract methods specified
below.

The means by which a file type detector determines the file type is
highly implementation specific. A simple implementation might examine the

file extension

(a convention used in some platforms) and map it to
a file type. In other cases, the file type may be stored as a file

attribute

or the bytes in a
file may be examined to guess its file type.

**Since:** 1.7
**See Also:** Files.probeContentType(Path)

public abstract class

FileTypeDetector

extends

Object

A file type detector for probing a file to guess its file type.

A file type detector is a concrete implementation of this class, has a
zero-argument constructor, and implements the abstract methods specified
below.

The means by which a file type detector determines the file type is
highly implementation specific. A simple implementation might examine the

file extension

(a convention used in some platforms) and map it to
a file type. In other cases, the file type may be stored as a file

attribute

or the bytes in a
file may be examined to guess its file type.

A file type detector is a concrete implementation of this class, has a
zero-argument constructor, and implements the abstract methods specified
below.

The means by which a file type detector determines the file type is
highly implementation specific. A simple implementation might examine the

file extension

(a convention used in some platforms) and map it to
a file type. In other cases, the file type may be stored as a file

attribute

or the bytes in a
file may be examined to guess its file type.

The means by which a file type detector determines the file type is
highly implementation specific. A simple implementation might examine the

file extension

(a convention used in some platforms) and map it to
a file type. In other cases, the file type may be stored as a file

attribute

or the bytes in a
file may be examined to guess its file type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

FileTypeDetector

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

probeContentType

​(

Path

path)

Probes the given file to guess its content type.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

FileTypeDetector

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

probeContentType

​(

Path

path)

Probes the given file to guess its content type.

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

Probes the given file to guess its content type.

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

- FileTypeDetector

```java
protected FileTypeDetector()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("fileTypeDetector")

============ METHOD DETAIL ==========

- Method Detail

- probeContentType

```java
public abstract
String
probeContentType​(
Path
path)
throws
IOException
```

Probes the given file to guess its content type.

The means by which this method determines the file type is highly
implementation specific. It may simply examine the file name, it may use
a file

attribute

,
or it may examines bytes in the file.

The probe result is the string form of the value of a
Multipurpose Internet Mail Extension (MIME) content type as
defined by

RFC 2045:
Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet
Message Bodies

. The string must be parsable according to the
grammar in the RFC 2045.

**Parameters:** path

- the path to the file to probe
**Returns:** The content type or

null

if the file type is not
recognized
**Throws:** IOException

- An I/O error occurs
**Throws:** SecurityException

- If the implementation requires to access the file, and a
security manager is installed, and it denies an unspecified
permission required by a file system provider implementation.
If the file reference is associated with the default file system
provider then the

SecurityManager.checkRead(String)

method
is invoked to check read access to the file.
**See Also:** Files.probeContentType(java.nio.file.Path)

Constructor Detail

- FileTypeDetector

```java
protected FileTypeDetector()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("fileTypeDetector")

---

#### Constructor Detail

FileTypeDetector

```java
protected FileTypeDetector()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("fileTypeDetector")

---

#### FileTypeDetector

protected FileTypeDetector()

Initializes a new instance of this class.

Method Detail

- probeContentType

```java
public abstract
String
probeContentType​(
Path
path)
throws
IOException
```

Probes the given file to guess its content type.

The means by which this method determines the file type is highly
implementation specific. It may simply examine the file name, it may use
a file

attribute

,
or it may examines bytes in the file.

The probe result is the string form of the value of a
Multipurpose Internet Mail Extension (MIME) content type as
defined by

RFC 2045:
Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet
Message Bodies

. The string must be parsable according to the
grammar in the RFC 2045.

**Parameters:** path

- the path to the file to probe
**Returns:** The content type or

null

if the file type is not
recognized
**Throws:** IOException

- An I/O error occurs
**Throws:** SecurityException

- If the implementation requires to access the file, and a
security manager is installed, and it denies an unspecified
permission required by a file system provider implementation.
If the file reference is associated with the default file system
provider then the

SecurityManager.checkRead(String)

method
is invoked to check read access to the file.
**See Also:** Files.probeContentType(java.nio.file.Path)

---

#### Method Detail

probeContentType

```java
public abstract
String
probeContentType​(
Path
path)
throws
IOException
```

Probes the given file to guess its content type.

The means by which this method determines the file type is highly
implementation specific. It may simply examine the file name, it may use
a file

attribute

,
or it may examines bytes in the file.

The probe result is the string form of the value of a
Multipurpose Internet Mail Extension (MIME) content type as
defined by

RFC 2045:
Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet
Message Bodies

. The string must be parsable according to the
grammar in the RFC 2045.

**Parameters:** path

- the path to the file to probe
**Returns:** The content type or

null

if the file type is not
recognized
**Throws:** IOException

- An I/O error occurs
**Throws:** SecurityException

- If the implementation requires to access the file, and a
security manager is installed, and it denies an unspecified
permission required by a file system provider implementation.
If the file reference is associated with the default file system
provider then the

SecurityManager.checkRead(String)

method
is invoked to check read access to the file.
**See Also:** Files.probeContentType(java.nio.file.Path)

---

#### probeContentType

public abstract

String

probeContentType​(

Path

path)
throws

IOException

Probes the given file to guess its content type.

The means by which this method determines the file type is highly
implementation specific. It may simply examine the file name, it may use
a file

attribute

,
or it may examines bytes in the file.

The probe result is the string form of the value of a
Multipurpose Internet Mail Extension (MIME) content type as
defined by

RFC 2045:
Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet
Message Bodies

. The string must be parsable according to the
grammar in the RFC 2045.

The means by which this method determines the file type is highly
implementation specific. It may simply examine the file name, it may use
a file

attribute

,
or it may examines bytes in the file.

The probe result is the string form of the value of a
Multipurpose Internet Mail Extension (MIME) content type as
defined by

RFC 2045:
Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet
Message Bodies

. The string must be parsable according to the
grammar in the RFC 2045.

The probe result is the string form of the value of a
Multipurpose Internet Mail Extension (MIME) content type as
defined by

RFC 2045:
Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet
Message Bodies

. The string must be parsable according to the
grammar in the RFC 2045.

---

