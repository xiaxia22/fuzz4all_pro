# Class URISyntaxException

**Source:** `java.base\java\net\URISyntaxException.html`

### Class Description

```java
public class
URISyntaxException

extends
Exception
```

Checked exception thrown to indicate that a string could not be parsed as a
URI reference.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public URISyntaxException​(
String
input,

String
reason,
int index)

Constructs an instance from the given input string, reason, and error
index.

**Parameters:**
- input

- The input string
- reason

- A string explaining why the input could not be parsed
- index

- The index at which the parse error occurred,
or

-1

if the index is not known

**Throws:**
- NullPointerException

- If either the input or reason strings are

null
- IllegalArgumentException

- If the error index is less than

-1

---

#### public URISyntaxException​(
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

- The input string
- reason

- A string explaining why the input could not be parsed

**Throws:**
- NullPointerException

- If either the input or reason strings are

null

---

### Method Details

#### public
String
getInput()

Returns the input string.

**Returns:**
- The input string

---

#### public
String
getReason()

Returns a string explaining why the input string could not be parsed.

**Returns:**
- The reason string

---

#### public int getIndex()

Returns an index into the input string of the position at which the
parse error occurred, or

-1

if this position is not known.

**Returns:**
- The error index

---

#### public
String
getMessage()

Returns a string describing the parse error. The resulting string
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
- A string describing the parse error

---

### Additional Sections

#### Class URISyntaxException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.net.URISyntaxException

java.lang.Throwable

- java.lang.Exception
- - java.net.URISyntaxException

java.lang.Exception

- java.net.URISyntaxException

java.net.URISyntaxException

**All Implemented Interfaces:** Serializable

```java
public class
URISyntaxException

extends
Exception
```

Checked exception thrown to indicate that a string could not be parsed as a
URI reference.

**Since:** 1.4
**See Also:** URI

,

Serialized Form

public class

URISyntaxException

extends

Exception

Checked exception thrown to indicate that a string could not be parsed as a
URI reference.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

URISyntaxException

​(

String

input,

String

reason)

Constructs an instance from the given input string and reason.

URISyntaxException

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
parse error occurred, or

-1

if this position is not known.

String

getInput

()

Returns the input string.

String

getMessage

()

Returns a string describing the parse error.

String

getReason

()

Returns a string explaining why the input string could not be parsed.

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

URISyntaxException

​(

String

input,

String

reason)

Constructs an instance from the given input string and reason.

URISyntaxException

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
parse error occurred, or

-1

if this position is not known.

String

getInput

()

Returns the input string.

String

getMessage

()

Returns a string describing the parse error.

String

getReason

()

Returns a string explaining why the input string could not be parsed.

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
parse error occurred, or

-1

if this position is not known.

Returns the input string.

Returns a string describing the parse error.

Returns a string explaining why the input string could not be parsed.

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

- URISyntaxException

```java
public URISyntaxException​(
String
input,

String
reason,
int index)
```

Constructs an instance from the given input string, reason, and error
index.

**Parameters:** input

- The input string
**Parameters:** reason

- A string explaining why the input could not be parsed
**Parameters:** index

- The index at which the parse error occurred,
or

-1

if the index is not known
**Throws:** NullPointerException

- If either the input or reason strings are

null
**Throws:** IllegalArgumentException

- If the error index is less than

-1

- URISyntaxException

```java
public URISyntaxException​(
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

- The input string
**Parameters:** reason

- A string explaining why the input could not be parsed
**Throws:** NullPointerException

- If either the input or reason strings are

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

**Returns:** The input string

- getReason

```java
public
String
getReason()
```

Returns a string explaining why the input string could not be parsed.

**Returns:** The reason string

- getIndex

```java
public int getIndex()
```

Returns an index into the input string of the position at which the
parse error occurred, or

-1

if this position is not known.

**Returns:** The error index

- getMessage

```java
public
String
getMessage()
```

Returns a string describing the parse error. The resulting string
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
**Returns:** A string describing the parse error

Constructor Detail

- URISyntaxException

```java
public URISyntaxException​(
String
input,

String
reason,
int index)
```

Constructs an instance from the given input string, reason, and error
index.

**Parameters:** input

- The input string
**Parameters:** reason

- A string explaining why the input could not be parsed
**Parameters:** index

- The index at which the parse error occurred,
or

-1

if the index is not known
**Throws:** NullPointerException

- If either the input or reason strings are

null
**Throws:** IllegalArgumentException

- If the error index is less than

-1

- URISyntaxException

```java
public URISyntaxException​(
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

- The input string
**Parameters:** reason

- A string explaining why the input could not be parsed
**Throws:** NullPointerException

- If either the input or reason strings are

null

---

#### Constructor Detail

URISyntaxException

```java
public URISyntaxException​(
String
input,

String
reason,
int index)
```

Constructs an instance from the given input string, reason, and error
index.

**Parameters:** input

- The input string
**Parameters:** reason

- A string explaining why the input could not be parsed
**Parameters:** index

- The index at which the parse error occurred,
or

-1

if the index is not known
**Throws:** NullPointerException

- If either the input or reason strings are

null
**Throws:** IllegalArgumentException

- If the error index is less than

-1

---

#### URISyntaxException

public URISyntaxException​(

String

input,

String

reason,
int index)

Constructs an instance from the given input string, reason, and error
index.

URISyntaxException

```java
public URISyntaxException​(
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

- The input string
**Parameters:** reason

- A string explaining why the input could not be parsed
**Throws:** NullPointerException

- If either the input or reason strings are

null

---

#### URISyntaxException

public URISyntaxException​(

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

**Returns:** The input string

- getReason

```java
public
String
getReason()
```

Returns a string explaining why the input string could not be parsed.

**Returns:** The reason string

- getIndex

```java
public int getIndex()
```

Returns an index into the input string of the position at which the
parse error occurred, or

-1

if this position is not known.

**Returns:** The error index

- getMessage

```java
public
String
getMessage()
```

Returns a string describing the parse error. The resulting string
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
**Returns:** A string describing the parse error

---

#### Method Detail

getInput

```java
public
String
getInput()
```

Returns the input string.

**Returns:** The input string

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

Returns a string explaining why the input string could not be parsed.

**Returns:** The reason string

---

#### getReason

public

String

getReason()

Returns a string explaining why the input string could not be parsed.

getIndex

```java
public int getIndex()
```

Returns an index into the input string of the position at which the
parse error occurred, or

-1

if this position is not known.

**Returns:** The error index

---

#### getIndex

public int getIndex()

Returns an index into the input string of the position at which the
parse error occurred, or

-1

if this position is not known.

getMessage

```java
public
String
getMessage()
```

Returns a string describing the parse error. The resulting string
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
**Returns:** A string describing the parse error

---

#### getMessage

public

String

getMessage()

Returns a string describing the parse error. The resulting string
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

