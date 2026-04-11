# Class IllformedLocaleException

**Source:** `java.base\java\util\IllformedLocaleException.html`

### Class Description

```java
public class
IllformedLocaleException

extends
RuntimeException
```

Thrown by methods in

Locale

and

Locale.Builder

to
indicate that an argument is not a well-formed BCP 47 tag.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IllformedLocaleException()

Constructs a new

IllformedLocaleException

with no
detail message and -1 as the error index.

---

#### public IllformedLocaleException​(
String
message)

Constructs a new

IllformedLocaleException

with the
given message and -1 as the error index.

**Parameters:**
- message

- the message

---

#### public IllformedLocaleException​(
String
message,
int errorIndex)

Constructs a new

IllformedLocaleException

with the
given message and the error index. The error index is the approximate
offset from the start of the ill-formed value to the point where the
parse first detected an error. A negative error index value indicates
either the error index is not applicable or unknown.

**Parameters:**
- message

- the message
- errorIndex

- the index

---

### Method Details

#### public int getErrorIndex()

Returns the index where the error was found. A negative value indicates
either the error index is not applicable or unknown.

**Returns:**
- the error index

---

### Additional Sections

#### Class IllformedLocaleException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.util.IllformedLocaleException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.util.IllformedLocaleException

java.lang.Exception

- java.lang.RuntimeException
- - java.util.IllformedLocaleException

java.lang.RuntimeException

- java.util.IllformedLocaleException

java.util.IllformedLocaleException

**All Implemented Interfaces:** Serializable

```java
public class
IllformedLocaleException

extends
RuntimeException
```

Thrown by methods in

Locale

and

Locale.Builder

to
indicate that an argument is not a well-formed BCP 47 tag.

**Since:** 1.7
**See Also:** Locale

,

Serialized Form

public class

IllformedLocaleException

extends

RuntimeException

Thrown by methods in

Locale

and

Locale.Builder

to
indicate that an argument is not a well-formed BCP 47 tag.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IllformedLocaleException

()

Constructs a new

IllformedLocaleException

with no
detail message and -1 as the error index.

IllformedLocaleException

​(

String

message)

Constructs a new

IllformedLocaleException

with the
given message and -1 as the error index.

IllformedLocaleException

​(

String

message,
int errorIndex)

Constructs a new

IllformedLocaleException

with the
given message and the error index.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getErrorIndex

()

Returns the index where the error was found.

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

getMessage

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

IllformedLocaleException

()

Constructs a new

IllformedLocaleException

with no
detail message and -1 as the error index.

IllformedLocaleException

​(

String

message)

Constructs a new

IllformedLocaleException

with the
given message and -1 as the error index.

IllformedLocaleException

​(

String

message,
int errorIndex)

Constructs a new

IllformedLocaleException

with the
given message and the error index.

---

#### Constructor Summary

Constructs a new

IllformedLocaleException

with no
detail message and -1 as the error index.

Constructs a new

IllformedLocaleException

with the
given message and -1 as the error index.

Constructs a new

IllformedLocaleException

with the
given message and the error index.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getErrorIndex

()

Returns the index where the error was found.

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

getMessage

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

Returns the index where the error was found.

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

getMessage

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

- IllformedLocaleException

```java
public IllformedLocaleException()
```

Constructs a new

IllformedLocaleException

with no
detail message and -1 as the error index.

- IllformedLocaleException

```java
public IllformedLocaleException​(
String
message)
```

Constructs a new

IllformedLocaleException

with the
given message and -1 as the error index.

**Parameters:** message

- the message

- IllformedLocaleException

```java
public IllformedLocaleException​(
String
message,
int errorIndex)
```

Constructs a new

IllformedLocaleException

with the
given message and the error index. The error index is the approximate
offset from the start of the ill-formed value to the point where the
parse first detected an error. A negative error index value indicates
either the error index is not applicable or unknown.

**Parameters:** message

- the message
**Parameters:** errorIndex

- the index

============ METHOD DETAIL ==========

- Method Detail

- getErrorIndex

```java
public int getErrorIndex()
```

Returns the index where the error was found. A negative value indicates
either the error index is not applicable or unknown.

**Returns:** the error index

Constructor Detail

- IllformedLocaleException

```java
public IllformedLocaleException()
```

Constructs a new

IllformedLocaleException

with no
detail message and -1 as the error index.

- IllformedLocaleException

```java
public IllformedLocaleException​(
String
message)
```

Constructs a new

IllformedLocaleException

with the
given message and -1 as the error index.

**Parameters:** message

- the message

- IllformedLocaleException

```java
public IllformedLocaleException​(
String
message,
int errorIndex)
```

Constructs a new

IllformedLocaleException

with the
given message and the error index. The error index is the approximate
offset from the start of the ill-formed value to the point where the
parse first detected an error. A negative error index value indicates
either the error index is not applicable or unknown.

**Parameters:** message

- the message
**Parameters:** errorIndex

- the index

---

#### Constructor Detail

IllformedLocaleException

```java
public IllformedLocaleException()
```

Constructs a new

IllformedLocaleException

with no
detail message and -1 as the error index.

---

#### IllformedLocaleException

public IllformedLocaleException()

Constructs a new

IllformedLocaleException

with no
detail message and -1 as the error index.

IllformedLocaleException

```java
public IllformedLocaleException​(
String
message)
```

Constructs a new

IllformedLocaleException

with the
given message and -1 as the error index.

**Parameters:** message

- the message

---

#### IllformedLocaleException

public IllformedLocaleException​(

String

message)

Constructs a new

IllformedLocaleException

with the
given message and -1 as the error index.

IllformedLocaleException

```java
public IllformedLocaleException​(
String
message,
int errorIndex)
```

Constructs a new

IllformedLocaleException

with the
given message and the error index. The error index is the approximate
offset from the start of the ill-formed value to the point where the
parse first detected an error. A negative error index value indicates
either the error index is not applicable or unknown.

**Parameters:** message

- the message
**Parameters:** errorIndex

- the index

---

#### IllformedLocaleException

public IllformedLocaleException​(

String

message,
int errorIndex)

Constructs a new

IllformedLocaleException

with the
given message and the error index. The error index is the approximate
offset from the start of the ill-formed value to the point where the
parse first detected an error. A negative error index value indicates
either the error index is not applicable or unknown.

Method Detail

- getErrorIndex

```java
public int getErrorIndex()
```

Returns the index where the error was found. A negative value indicates
either the error index is not applicable or unknown.

**Returns:** the error index

---

#### Method Detail

getErrorIndex

```java
public int getErrorIndex()
```

Returns the index where the error was found. A negative value indicates
either the error index is not applicable or unknown.

**Returns:** the error index

---

#### getErrorIndex

public int getErrorIndex()

Returns the index where the error was found. A negative value indicates
either the error index is not applicable or unknown.

---

