# Class IllegalArgumentException

**Source:** `java.base\java\lang\IllegalArgumentException.html`

### Class Description

```java
public class
IllegalArgumentException

extends
RuntimeException
```

Thrown to indicate that a method has been passed an illegal or
inappropriate argument.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IllegalArgumentException()

Constructs an

IllegalArgumentException

with no
detail message.

---

#### public IllegalArgumentException​(
String
s)

Constructs an

IllegalArgumentException

with the
specified detail message.

**Parameters:**
- s

- the detail message.

---

#### public IllegalArgumentException​(
String
message,

Throwable
cause)

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

**Parameters:**
- message

- the detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method).
- cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value
is permitted, and indicates that the cause is nonexistent or
unknown.)

**Since:**
- 1.5

---

#### public IllegalArgumentException​(
Throwable
cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

).

**Parameters:**
- cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

**Since:**
- 1.5

---

### Method Details

*No entries found.*

### Additional Sections

#### Class IllegalArgumentException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalArgumentException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalArgumentException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.IllegalArgumentException

java.lang.RuntimeException

- java.lang.IllegalArgumentException

java.lang.IllegalArgumentException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** IllegalChannelGroupException

,

IllegalCharsetNameException

,

IllegalFormatException

,

IllegalSelectorException

,

IllegalThreadStateException

,

InvalidKeyException

,

InvalidOpenTypeException

,

InvalidParameterException

,

InvalidPathException

,

InvalidStreamException

,

KeyAlreadyExistsException

,

NumberFormatException

,

PatternSyntaxException

,

ProviderMismatchException

,

UnresolvedAddressException

,

UnsupportedAddressTypeException

,

UnsupportedCharsetException

```java
public class
IllegalArgumentException

extends
RuntimeException
```

Thrown to indicate that a method has been passed an illegal or
inappropriate argument.

**Since:** 1.0
**See Also:** Serialized Form

public class

IllegalArgumentException

extends

RuntimeException

Thrown to indicate that a method has been passed an illegal or
inappropriate argument.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IllegalArgumentException

()

Constructs an

IllegalArgumentException

with no
detail message.

IllegalArgumentException

​(

String

s)

Constructs an

IllegalArgumentException

with the
specified detail message.

IllegalArgumentException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

IllegalArgumentException

​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

========== METHOD SUMMARY ===========

- Method Summary

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

IllegalArgumentException

()

Constructs an

IllegalArgumentException

with no
detail message.

IllegalArgumentException

​(

String

s)

Constructs an

IllegalArgumentException

with the
specified detail message.

IllegalArgumentException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

IllegalArgumentException

​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs an

IllegalArgumentException

with no
detail message.

Constructs an

IllegalArgumentException

with the
specified detail message.

Constructs a new exception with the specified detail message and
cause.

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

Method Summary

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

- IllegalArgumentException

```java
public IllegalArgumentException()
```

Constructs an

IllegalArgumentException

with no
detail message.

- IllegalArgumentException

```java
public IllegalArgumentException​(
String
s)
```

Constructs an

IllegalArgumentException

with the
specified detail message.

**Parameters:** s

- the detail message.

- IllegalArgumentException

```java
public IllegalArgumentException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

**Parameters:** message

- the detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method).
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value
is permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

- IllegalArgumentException

```java
public IllegalArgumentException​(
Throwable
cause)
```

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

Constructor Detail

- IllegalArgumentException

```java
public IllegalArgumentException()
```

Constructs an

IllegalArgumentException

with no
detail message.

- IllegalArgumentException

```java
public IllegalArgumentException​(
String
s)
```

Constructs an

IllegalArgumentException

with the
specified detail message.

**Parameters:** s

- the detail message.

- IllegalArgumentException

```java
public IllegalArgumentException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

**Parameters:** message

- the detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method).
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value
is permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

- IllegalArgumentException

```java
public IllegalArgumentException​(
Throwable
cause)
```

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

---

#### Constructor Detail

IllegalArgumentException

```java
public IllegalArgumentException()
```

Constructs an

IllegalArgumentException

with no
detail message.

---

#### IllegalArgumentException

public IllegalArgumentException()

Constructs an

IllegalArgumentException

with no
detail message.

IllegalArgumentException

```java
public IllegalArgumentException​(
String
s)
```

Constructs an

IllegalArgumentException

with the
specified detail message.

**Parameters:** s

- the detail message.

---

#### IllegalArgumentException

public IllegalArgumentException​(

String

s)

Constructs an

IllegalArgumentException

with the
specified detail message.

IllegalArgumentException

```java
public IllegalArgumentException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

**Parameters:** message

- the detail message (which is saved for later retrieval
by the

Throwable.getMessage()

method).
**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value
is permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

---

#### IllegalArgumentException

public IllegalArgumentException​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

Note that the detail message associated with

cause

is

not

automatically incorporated in this exception's detail
message.

IllegalArgumentException

```java
public IllegalArgumentException​(
Throwable
cause)
```

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

).

**Parameters:** cause

- the cause (which is saved for later retrieval by the

Throwable.getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Since:** 1.5

---

#### IllegalArgumentException

public IllegalArgumentException​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).
This constructor is useful for exceptions that are little more than
wrappers for other throwables (for example,

PrivilegedActionException

).

---

