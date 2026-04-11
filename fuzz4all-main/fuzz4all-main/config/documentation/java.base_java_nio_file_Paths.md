# Class Paths

**Source:** `java.base\java\nio\file\Paths.html`

### Class Description

```java
public final class
Paths

extends
Object
```

This class consists exclusively of static methods that return a

Path

by converting a path string or

URI

.

**API Note:** It is recommended to obtain a

Path

via the

Path.of

methods
instead of via the

get

methods defined in this class as this class
may be deprecated in a future release.
**Since:** 1.7
**See Also:** Path

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Path
get​(
String
first,

String
... more)

Converts a path string, or a sequence of strings that when joined form
a path string, to a

Path

.

**Parameters:**
- first

- the path string or initial part of the path string
- more

- additional strings to be joined to form the path string

**Returns:**
- the resulting

Path

**Throws:**
- InvalidPathException

- if the path string cannot be converted to a

Path

**See Also:**
- FileSystem.getPath(java.lang.String, java.lang.String...)

,

Path.of(String,String...)

**Implementation Requirements:**
- This method simply invokes

Path.of(String, String...)

with the given parameters.

---

#### public static
Path
get​(
URI
uri)

Converts the given URI to a

Path

object.

**Parameters:**
- uri

- the URI to convert

**Returns:**
- the resulting

Path

**Throws:**
- IllegalArgumentException

- if preconditions on the

uri

parameter do not hold. The
format of the URI is provider specific.
- FileSystemNotFoundException

- The file system, identified by the URI, does not exist and
cannot be created automatically, or the provider identified by
the URI's scheme component is not installed
- SecurityException

- if a security manager is installed and it denies an unspecified
permission to access the file system

**See Also:**
- Path.of(URI)

**Implementation Requirements:**
- This method simply invokes

* Path.of(URI)

with the given parameter.

---

### Additional Sections

#### Class Paths

java.lang.Object

- java.nio.file.Paths

java.nio.file.Paths

```java
public final class
Paths

extends
Object
```

This class consists exclusively of static methods that return a

Path

by converting a path string or

URI

.

**API Note:** It is recommended to obtain a

Path

via the

Path.of

methods
instead of via the

get

methods defined in this class as this class
may be deprecated in a future release.
**Since:** 1.7
**See Also:** Path

public final class

Paths

extends

Object

This class consists exclusively of static methods that return a

Path

by converting a path string or

URI

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Path

get

​(

String

first,

String

... more)

Converts a path string, or a sequence of strings that when joined form
a path string, to a

Path

.

static

Path

get

​(

URI

uri)

Converts the given URI to a

Path

object.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Path

get

​(

String

first,

String

... more)

Converts a path string, or a sequence of strings that when joined form
a path string, to a

Path

.

static

Path

get

​(

URI

uri)

Converts the given URI to a

Path

object.

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

Converts a path string, or a sequence of strings that when joined form
a path string, to a

Path

.

Converts the given URI to a

Path

object.

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

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public static
Path
get​(
String
first,

String
... more)
```

Converts a path string, or a sequence of strings that when joined form
a path string, to a

Path

.

**Implementation Requirements:** This method simply invokes

Path.of(String, String...)

with the given parameters.
**Parameters:** first

- the path string or initial part of the path string
**Parameters:** more

- additional strings to be joined to form the path string
**Returns:** the resulting

Path
**Throws:** InvalidPathException

- if the path string cannot be converted to a

Path
**See Also:** FileSystem.getPath(java.lang.String, java.lang.String...)

,

Path.of(String,String...)

- get

```java
public static
Path
get​(
URI
uri)
```

Converts the given URI to a

Path

object.

**Implementation Requirements:** This method simply invokes

* Path.of(URI)

with the given parameter.
**Parameters:** uri

- the URI to convert
**Returns:** the resulting

Path
**Throws:** IllegalArgumentException

- if preconditions on the

uri

parameter do not hold. The
format of the URI is provider specific.
**Throws:** FileSystemNotFoundException

- The file system, identified by the URI, does not exist and
cannot be created automatically, or the provider identified by
the URI's scheme component is not installed
**Throws:** SecurityException

- if a security manager is installed and it denies an unspecified
permission to access the file system
**See Also:** Path.of(URI)

Method Detail

- get

```java
public static
Path
get​(
String
first,

String
... more)
```

Converts a path string, or a sequence of strings that when joined form
a path string, to a

Path

.

**Implementation Requirements:** This method simply invokes

Path.of(String, String...)

with the given parameters.
**Parameters:** first

- the path string or initial part of the path string
**Parameters:** more

- additional strings to be joined to form the path string
**Returns:** the resulting

Path
**Throws:** InvalidPathException

- if the path string cannot be converted to a

Path
**See Also:** FileSystem.getPath(java.lang.String, java.lang.String...)

,

Path.of(String,String...)

- get

```java
public static
Path
get​(
URI
uri)
```

Converts the given URI to a

Path

object.

**Implementation Requirements:** This method simply invokes

* Path.of(URI)

with the given parameter.
**Parameters:** uri

- the URI to convert
**Returns:** the resulting

Path
**Throws:** IllegalArgumentException

- if preconditions on the

uri

parameter do not hold. The
format of the URI is provider specific.
**Throws:** FileSystemNotFoundException

- The file system, identified by the URI, does not exist and
cannot be created automatically, or the provider identified by
the URI's scheme component is not installed
**Throws:** SecurityException

- if a security manager is installed and it denies an unspecified
permission to access the file system
**See Also:** Path.of(URI)

---

#### Method Detail

get

```java
public static
Path
get​(
String
first,

String
... more)
```

Converts a path string, or a sequence of strings that when joined form
a path string, to a

Path

.

**Implementation Requirements:** This method simply invokes

Path.of(String, String...)

with the given parameters.
**Parameters:** first

- the path string or initial part of the path string
**Parameters:** more

- additional strings to be joined to form the path string
**Returns:** the resulting

Path
**Throws:** InvalidPathException

- if the path string cannot be converted to a

Path
**See Also:** FileSystem.getPath(java.lang.String, java.lang.String...)

,

Path.of(String,String...)

---

#### get

public static

Path

get​(

String

first,

String

... more)

Converts a path string, or a sequence of strings that when joined form
a path string, to a

Path

.

get

```java
public static
Path
get​(
URI
uri)
```

Converts the given URI to a

Path

object.

**Implementation Requirements:** This method simply invokes

* Path.of(URI)

with the given parameter.
**Parameters:** uri

- the URI to convert
**Returns:** the resulting

Path
**Throws:** IllegalArgumentException

- if preconditions on the

uri

parameter do not hold. The
format of the URI is provider specific.
**Throws:** FileSystemNotFoundException

- The file system, identified by the URI, does not exist and
cannot be created automatically, or the provider identified by
the URI's scheme component is not installed
**Throws:** SecurityException

- if a security manager is installed and it denies an unspecified
permission to access the file system
**See Also:** Path.of(URI)

---

#### get

public static

Path

get​(

URI

uri)

Converts the given URI to a

Path

object.

---

