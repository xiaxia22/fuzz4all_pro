# Class InvalidPathException

**Source:** `java.base\java\nio\file\InvalidPathException.html`

### Class Description

```java
public class
InvalidPathException

extends
IllegalArgumentException
```

Unchecked exception thrown when path string cannot be converted into a

Path

because the path string contains invalid characters, or
the path string is invalid for other file system specific reasons.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InvalidPathException​(
String
input,

String
reason,
int index)

Constructs an instance from the given input string, reason, and error
index.

**Parameters:**
- input

- the input string
- reason

- a string explaining why the input was rejected
- index

- the index at which the error occurred,
or

-1

if the index is not known

**Throws:**
- NullPointerException

- if either the input or reason strings are

null
- IllegalArgumentException

- if the error index is less than

-1

---

#### public InvalidPathException​(
String
input,

String
reason)

Constructs an instance from the given input string and reason. The
resulting object will have an error index of

-1

.

**Parameters:**
- input

- the input string
- reason

- a string explaining why the input was rejected

**Throws:**
- NullPointerException

- if either the input or reason strings are

null

---

### Method Details

#### public
String
getInput()

Returns the input string.

**Returns:**
- the input string

---

#### public
String
getReason()

Returns a string explaining why the input string was rejected.

**Returns:**
- the reason string

---

#### public int getIndex()

Returns an index into the input string of the position at which the
error occurred, or

-1

if this position is not known.

**Returns:**
- the error index

---

#### public
String
getMessage()

Returns a string describing the error. The resulting string
consists of the reason string followed by a colon character
(

':'

), a space, and the input string. If the error index is
defined then the string

" at index "

followed by the index, in
decimal, is inserted after the reason string and before the colon
character.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- a string describing the error

---

### Additional Sections

#### Class InvalidPathException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalArgumentException
- - java.nio.file.InvalidPathException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalArgumentException
- - java.nio.file.InvalidPathException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.IllegalArgumentException
- - java.nio.file.InvalidPathException

java.lang.RuntimeException

- java.lang.IllegalArgumentException
- - java.nio.file.InvalidPathException

java.lang.IllegalArgumentException

- java.nio.file.InvalidPathException

java.nio.file.InvalidPathException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidPathException

extends
IllegalArgumentException
```

Unchecked exception thrown when path string cannot be converted into a

Path

because the path string contains invalid characters, or
the path string is invalid for other file system specific reasons.

**Since:** 1.7
**See Also:** Serialized Form

public class

InvalidPathException

extends

IllegalArgumentException

Unchecked exception thrown when path string cannot be converted into a

Path

because the path string contains invalid characters, or
the path string is invalid for other file system specific reasons.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InvalidPathException

​(

String

input,

String

reason)

Constructs an instance from the given input string and reason.

InvalidPathException

​(

String

input,

String

reason,
int index)

Constructs an instance from the given input string, reason, and error
index.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIndex

()

Returns an index into the input string of the position at which the
error occurred, or

-1

if this position is not known.

String

getInput

()

Returns the input string.

String

getMessage

()

Returns a string describing the error.

String

getReason

()

Returns a string explaining why the input string was rejected.

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

InvalidPathException

​(

String

input,

String

reason)

Constructs an instance from the given input string and reason.

InvalidPathException

​(

String

input,

String

reason,
int index)

Constructs an instance from the given input string, reason, and error
index.

---

#### Constructor Summary

Constructs an instance from the given input string and reason.

Constructs an instance from the given input string, reason, and error
index.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIndex

()

Returns an index into the input string of the position at which the
error occurred, or

-1

if this position is not known.

String

getInput

()

Returns the input string.

String

getMessage

()

Returns a string describing the error.

String

getReason

()

Returns a string explaining why the input string was rejected.

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

Returns an index into the input string of the position at which the
error occurred, or

-1

if this position is not known.

Returns the input string.

Returns a string describing the error.

Returns a string explaining why the input string was rejected.

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

- InvalidPathException

```java
public InvalidPathException​(
String
input,

String
reason,
int index)
```

Constructs an instance from the given input string, reason, and error
index.

**Parameters:** input

- the input string
**Parameters:** reason

- a string explaining why the input was rejected
**Parameters:** index

- the index at which the error occurred,
or

-1

if the index is not known
**Throws:** NullPointerException

- if either the input or reason strings are

null
**Throws:** IllegalArgumentException

- if the error index is less than

-1

- InvalidPathException

```java
public InvalidPathException​(
String
input,

String
reason)
```

Constructs an instance from the given input string and reason. The
resulting object will have an error index of

-1

.

**Parameters:** input

- the input string
**Parameters:** reason

- a string explaining why the input was rejected
**Throws:** NullPointerException

- if either the input or reason strings are

null

============ METHOD DETAIL ==========

- Method Detail

- getInput

```java
public
String
getInput()
```

Returns the input string.

**Returns:** the input string

- getReason

```java
public
String
getReason()
```

Returns a string explaining why the input string was rejected.

**Returns:** the reason string

- getIndex

```java
public int getIndex()
```

Returns an index into the input string of the position at which the
error occurred, or

-1

if this position is not known.

**Returns:** the error index

- getMessage

```java
public
String
getMessage()
```

Returns a string describing the error. The resulting string
consists of the reason string followed by a colon character
(

':'

), a space, and the input string. If the error index is
defined then the string

" at index "

followed by the index, in
decimal, is inserted after the reason string and before the colon
character.

**Overrides:** getMessage

in class

Throwable
**Returns:** a string describing the error

Constructor Detail

- InvalidPathException

```java
public InvalidPathException​(
String
input,

String
reason,
int index)
```

Constructs an instance from the given input string, reason, and error
index.

**Parameters:** input

- the input string
**Parameters:** reason

- a string explaining why the input was rejected
**Parameters:** index

- the index at which the error occurred,
or

-1

if the index is not known
**Throws:** NullPointerException

- if either the input or reason strings are

null
**Throws:** IllegalArgumentException

- if the error index is less than

-1

- InvalidPathException

```java
public InvalidPathException​(
String
input,

String
reason)
```

Constructs an instance from the given input string and reason. The
resulting object will have an error index of

-1

.

**Parameters:** input

- the input string
**Parameters:** reason

- a string explaining why the input was rejected
**Throws:** NullPointerException

- if either the input or reason strings are

null

---

#### Constructor Detail

InvalidPathException

```java
public InvalidPathException​(
String
input,

String
reason,
int index)
```

Constructs an instance from the given input string, reason, and error
index.

**Parameters:** input

- the input string
**Parameters:** reason

- a string explaining why the input was rejected
**Parameters:** index

- the index at which the error occurred,
or

-1

if the index is not known
**Throws:** NullPointerException

- if either the input or reason strings are

null
**Throws:** IllegalArgumentException

- if the error index is less than

-1

---

#### InvalidPathException

public InvalidPathException​(

String

input,

String

reason,
int index)

Constructs an instance from the given input string, reason, and error
index.

InvalidPathException

```java
public InvalidPathException​(
String
input,

String
reason)
```

Constructs an instance from the given input string and reason. The
resulting object will have an error index of

-1

.

**Parameters:** input

- the input string
**Parameters:** reason

- a string explaining why the input was rejected
**Throws:** NullPointerException

- if either the input or reason strings are

null

---

#### InvalidPathException

public InvalidPathException​(

String

input,

String

reason)

Constructs an instance from the given input string and reason. The
resulting object will have an error index of

-1

.

Method Detail

- getInput

```java
public
String
getInput()
```

Returns the input string.

**Returns:** the input string

- getReason

```java
public
String
getReason()
```

Returns a string explaining why the input string was rejected.

**Returns:** the reason string

- getIndex

```java
public int getIndex()
```

Returns an index into the input string of the position at which the
error occurred, or

-1

if this position is not known.

**Returns:** the error index

- getMessage

```java
public
String
getMessage()
```

Returns a string describing the error. The resulting string
consists of the reason string followed by a colon character
(

':'

), a space, and the input string. If the error index is
defined then the string

" at index "

followed by the index, in
decimal, is inserted after the reason string and before the colon
character.

**Overrides:** getMessage

in class

Throwable
**Returns:** a string describing the error

---

#### Method Detail

getInput

```java
public
String
getInput()
```

Returns the input string.

**Returns:** the input string

---

#### getInput

public

String

getInput()

Returns the input string.

getReason

```java
public
String
getReason()
```

Returns a string explaining why the input string was rejected.

**Returns:** the reason string

---

#### getReason

public

String

getReason()

Returns a string explaining why the input string was rejected.

getIndex

```java
public int getIndex()
```

Returns an index into the input string of the position at which the
error occurred, or

-1

if this position is not known.

**Returns:** the error index

---

#### getIndex

public int getIndex()

Returns an index into the input string of the position at which the
error occurred, or

-1

if this position is not known.

getMessage

```java
public
String
getMessage()
```

Returns a string describing the error. The resulting string
consists of the reason string followed by a colon character
(

':'

), a space, and the input string. If the error index is
defined then the string

" at index "

followed by the index, in
decimal, is inserted after the reason string and before the colon
character.

**Overrides:** getMessage

in class

Throwable
**Returns:** a string describing the error

---

#### getMessage

public

String

getMessage()

Returns a string describing the error. The resulting string
consists of the reason string followed by a colon character
(

':'

), a space, and the input string. If the error index is
defined then the string

" at index "

followed by the index, in
decimal, is inserted after the reason string and before the colon
character.

---

