# Class SimpleFileVisitor<T>

**Source:** `java.base\java\nio\file\SimpleFileVisitor.html`

### Class Description

```java
public class
SimpleFileVisitor<T>

extends
Object

implements
FileVisitor
<T>
```

A simple visitor of files with default behavior to visit all files and to
re-throw I/O errors.

Methods in this class may be overridden subject to their general contract.

**Type Parameters:** T

- The type of reference to the files

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SimpleFileVisitor()

Initializes a new instance of this class.

---

### Method Details

#### public
FileVisitResult
preVisitDirectory​(
T
dir,

BasicFileAttributes
attrs)
throws
IOException

Invoked for a directory before entries in the directory are visited.

Unless overridden, this method returns

CONTINUE

.

**Specified by:**
- preVisitDirectory

in interface

FileVisitor

<

T

>

**Parameters:**
- dir

- a reference to the directory
- attrs

- the directory's basic attributes

**Returns:**
- the visit result

**Throws:**
- IOException

- if an I/O error occurs

---

#### public
FileVisitResult
visitFile​(
T
file,

BasicFileAttributes
attrs)
throws
IOException

Invoked for a file in a directory.

Unless overridden, this method returns

CONTINUE

.

**Specified by:**
- visitFile

in interface

FileVisitor

<

T

>

**Parameters:**
- file

- a reference to the file
- attrs

- the file's basic attributes

**Returns:**
- the visit result

**Throws:**
- IOException

- if an I/O error occurs

---

#### public
FileVisitResult
visitFileFailed​(
T
file,

IOException
exc)
throws
IOException

Invoked for a file that could not be visited.

Unless overridden, this method re-throws the I/O exception that prevented
the file from being visited.

**Specified by:**
- visitFileFailed

in interface

FileVisitor

<

T

>

**Parameters:**
- file

- a reference to the file
- exc

- the I/O exception that prevented the file from being visited

**Returns:**
- the visit result

**Throws:**
- IOException

- if an I/O error occurs

---

#### public
FileVisitResult
postVisitDirectory​(
T
dir,

IOException
exc)
throws
IOException

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

Unless overridden, this method returns

CONTINUE

if the directory iteration completes without an I/O exception;
otherwise this method re-throws the I/O exception that caused the iteration
of the directory to terminate prematurely.

**Specified by:**
- postVisitDirectory

in interface

FileVisitor

<

T

>

**Parameters:**
- dir

- a reference to the directory
- exc

-

null

if the iteration of the directory completes without
an error; otherwise the I/O exception that caused the iteration
of the directory to complete prematurely

**Returns:**
- the visit result

**Throws:**
- IOException

- if an I/O error occurs

---

### Additional Sections

#### Class SimpleFileVisitor<T>

java.lang.Object

- java.nio.file.SimpleFileVisitor<T>

java.nio.file.SimpleFileVisitor<T>

**Type Parameters:** T

- The type of reference to the files

**All Implemented Interfaces:** FileVisitor

<T>

```java
public class
SimpleFileVisitor<T>

extends
Object

implements
FileVisitor
<T>
```

A simple visitor of files with default behavior to visit all files and to
re-throw I/O errors.

Methods in this class may be overridden subject to their general contract.

**Since:** 1.7

public class

SimpleFileVisitor<T>

extends

Object

implements

FileVisitor

<T>

A simple visitor of files with default behavior to visit all files and to
re-throw I/O errors.

Methods in this class may be overridden subject to their general contract.

Methods in this class may be overridden subject to their general contract.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleFileVisitor

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

FileVisitResult

postVisitDirectory

​(

T

dir,

IOException

exc)

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

FileVisitResult

preVisitDirectory

​(

T

dir,

BasicFileAttributes

attrs)

Invoked for a directory before entries in the directory are visited.

FileVisitResult

visitFile

​(

T

file,

BasicFileAttributes

attrs)

Invoked for a file in a directory.

FileVisitResult

visitFileFailed

​(

T

file,

IOException

exc)

Invoked for a file that could not be visited.

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

SimpleFileVisitor

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

FileVisitResult

postVisitDirectory

​(

T

dir,

IOException

exc)

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

FileVisitResult

preVisitDirectory

​(

T

dir,

BasicFileAttributes

attrs)

Invoked for a directory before entries in the directory are visited.

FileVisitResult

visitFile

​(

T

file,

BasicFileAttributes

attrs)

Invoked for a file in a directory.

FileVisitResult

visitFileFailed

​(

T

file,

IOException

exc)

Invoked for a file that could not be visited.

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

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

Invoked for a directory before entries in the directory are visited.

Invoked for a file in a directory.

Invoked for a file that could not be visited.

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

- SimpleFileVisitor

```java
protected SimpleFileVisitor()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- preVisitDirectory

```java
public
FileVisitResult
preVisitDirectory​(
T
dir,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a directory before entries in the directory are visited.

Unless overridden, this method returns

CONTINUE

.

**Specified by:** preVisitDirectory

in interface

FileVisitor

<

T

>
**Parameters:** dir

- a reference to the directory
**Parameters:** attrs

- the directory's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- visitFile

```java
public
FileVisitResult
visitFile​(
T
file,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a file in a directory.

Unless overridden, this method returns

CONTINUE

.

**Specified by:** visitFile

in interface

FileVisitor

<

T

>
**Parameters:** file

- a reference to the file
**Parameters:** attrs

- the file's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- visitFileFailed

```java
public
FileVisitResult
visitFileFailed​(
T
file,

IOException
exc)
throws
IOException
```

Invoked for a file that could not be visited.

Unless overridden, this method re-throws the I/O exception that prevented
the file from being visited.

**Specified by:** visitFileFailed

in interface

FileVisitor

<

T

>
**Parameters:** file

- a reference to the file
**Parameters:** exc

- the I/O exception that prevented the file from being visited
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- postVisitDirectory

```java
public
FileVisitResult
postVisitDirectory​(
T
dir,

IOException
exc)
throws
IOException
```

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

Unless overridden, this method returns

CONTINUE

if the directory iteration completes without an I/O exception;
otherwise this method re-throws the I/O exception that caused the iteration
of the directory to terminate prematurely.

**Specified by:** postVisitDirectory

in interface

FileVisitor

<

T

>
**Parameters:** dir

- a reference to the directory
**Parameters:** exc

-

null

if the iteration of the directory completes without
an error; otherwise the I/O exception that caused the iteration
of the directory to complete prematurely
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

Constructor Detail

- SimpleFileVisitor

```java
protected SimpleFileVisitor()
```

Initializes a new instance of this class.

---

#### Constructor Detail

SimpleFileVisitor

```java
protected SimpleFileVisitor()
```

Initializes a new instance of this class.

---

#### SimpleFileVisitor

protected SimpleFileVisitor()

Initializes a new instance of this class.

Method Detail

- preVisitDirectory

```java
public
FileVisitResult
preVisitDirectory​(
T
dir,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a directory before entries in the directory are visited.

Unless overridden, this method returns

CONTINUE

.

**Specified by:** preVisitDirectory

in interface

FileVisitor

<

T

>
**Parameters:** dir

- a reference to the directory
**Parameters:** attrs

- the directory's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- visitFile

```java
public
FileVisitResult
visitFile​(
T
file,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a file in a directory.

Unless overridden, this method returns

CONTINUE

.

**Specified by:** visitFile

in interface

FileVisitor

<

T

>
**Parameters:** file

- a reference to the file
**Parameters:** attrs

- the file's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- visitFileFailed

```java
public
FileVisitResult
visitFileFailed​(
T
file,

IOException
exc)
throws
IOException
```

Invoked for a file that could not be visited.

Unless overridden, this method re-throws the I/O exception that prevented
the file from being visited.

**Specified by:** visitFileFailed

in interface

FileVisitor

<

T

>
**Parameters:** file

- a reference to the file
**Parameters:** exc

- the I/O exception that prevented the file from being visited
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- postVisitDirectory

```java
public
FileVisitResult
postVisitDirectory​(
T
dir,

IOException
exc)
throws
IOException
```

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

Unless overridden, this method returns

CONTINUE

if the directory iteration completes without an I/O exception;
otherwise this method re-throws the I/O exception that caused the iteration
of the directory to terminate prematurely.

**Specified by:** postVisitDirectory

in interface

FileVisitor

<

T

>
**Parameters:** dir

- a reference to the directory
**Parameters:** exc

-

null

if the iteration of the directory completes without
an error; otherwise the I/O exception that caused the iteration
of the directory to complete prematurely
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### Method Detail

preVisitDirectory

```java
public
FileVisitResult
preVisitDirectory​(
T
dir,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a directory before entries in the directory are visited.

Unless overridden, this method returns

CONTINUE

.

**Specified by:** preVisitDirectory

in interface

FileVisitor

<

T

>
**Parameters:** dir

- a reference to the directory
**Parameters:** attrs

- the directory's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### preVisitDirectory

public

FileVisitResult

preVisitDirectory​(

T

dir,

BasicFileAttributes

attrs)
throws

IOException

Invoked for a directory before entries in the directory are visited.

Unless overridden, this method returns

CONTINUE

.

Unless overridden, this method returns

CONTINUE

.

visitFile

```java
public
FileVisitResult
visitFile​(
T
file,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a file in a directory.

Unless overridden, this method returns

CONTINUE

.

**Specified by:** visitFile

in interface

FileVisitor

<

T

>
**Parameters:** file

- a reference to the file
**Parameters:** attrs

- the file's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### visitFile

public

FileVisitResult

visitFile​(

T

file,

BasicFileAttributes

attrs)
throws

IOException

Invoked for a file in a directory.

Unless overridden, this method returns

CONTINUE

.

Unless overridden, this method returns

CONTINUE

.

visitFileFailed

```java
public
FileVisitResult
visitFileFailed​(
T
file,

IOException
exc)
throws
IOException
```

Invoked for a file that could not be visited.

Unless overridden, this method re-throws the I/O exception that prevented
the file from being visited.

**Specified by:** visitFileFailed

in interface

FileVisitor

<

T

>
**Parameters:** file

- a reference to the file
**Parameters:** exc

- the I/O exception that prevented the file from being visited
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### visitFileFailed

public

FileVisitResult

visitFileFailed​(

T

file,

IOException

exc)
throws

IOException

Invoked for a file that could not be visited.

Unless overridden, this method re-throws the I/O exception that prevented
the file from being visited.

Unless overridden, this method re-throws the I/O exception that prevented
the file from being visited.

postVisitDirectory

```java
public
FileVisitResult
postVisitDirectory​(
T
dir,

IOException
exc)
throws
IOException
```

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

Unless overridden, this method returns

CONTINUE

if the directory iteration completes without an I/O exception;
otherwise this method re-throws the I/O exception that caused the iteration
of the directory to terminate prematurely.

**Specified by:** postVisitDirectory

in interface

FileVisitor

<

T

>
**Parameters:** dir

- a reference to the directory
**Parameters:** exc

-

null

if the iteration of the directory completes without
an error; otherwise the I/O exception that caused the iteration
of the directory to complete prematurely
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### postVisitDirectory

public

FileVisitResult

postVisitDirectory​(

T

dir,

IOException

exc)
throws

IOException

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

Unless overridden, this method returns

CONTINUE

if the directory iteration completes without an I/O exception;
otherwise this method re-throws the I/O exception that caused the iteration
of the directory to terminate prematurely.

Unless overridden, this method returns

CONTINUE

if the directory iteration completes without an I/O exception;
otherwise this method re-throws the I/O exception that caused the iteration
of the directory to terminate prematurely.

---

