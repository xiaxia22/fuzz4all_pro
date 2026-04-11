# Class KeySelectorException

**Source:** `java.xml.crypto\javax\xml\crypto\KeySelectorException.html`

### Class Description

```java
public class
KeySelectorException

extends
Exception
```

Indicates an exceptional condition thrown by a

KeySelector

.

A

KeySelectorException

can contain a cause: another
throwable that caused this

KeySelectorException

to get thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeySelectorException()

Constructs a new

KeySelectorException

with

null

as its detail message.

---

#### public KeySelectorException​(
String
message)

Constructs a new

KeySelectorException

with the specified
detail message.

**Parameters:**
- message

- the detail message

---

#### public KeySelectorException​(
String
message,

Throwable
cause)

Constructs a new

KeySelectorException

with the
specified detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

**Parameters:**
- message

- the detail message
- cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### public KeySelectorException​(
Throwable
cause)

Constructs a new

KeySelectorException

with the specified
cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

**Parameters:**
- cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

### Method Details

#### public
Throwable
getCause()

Returns the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

KeySelectorException

to get thrown.)

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown.

---

#### public void printStackTrace()

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the standard error stream.

**Overrides:**
- printStackTrace

in class

Throwable

---

#### public void printStackTrace​(
PrintStream
s)

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print stream.

**Overrides:**
- printStackTrace

in class

Throwable

**Parameters:**
- s

-

PrintStream

to use for output

---

#### public void printStackTrace​(
PrintWriter
s)

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print writer.

**Overrides:**
- printStackTrace

in class

Throwable

**Parameters:**
- s

-

PrintWriter

to use for output

---

### Additional Sections

#### Class KeySelectorException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.xml.crypto.KeySelectorException

java.lang.Throwable

- java.lang.Exception
- - javax.xml.crypto.KeySelectorException

java.lang.Exception

- javax.xml.crypto.KeySelectorException

javax.xml.crypto.KeySelectorException

**All Implemented Interfaces:** Serializable

```java
public class
KeySelectorException

extends
Exception
```

Indicates an exceptional condition thrown by a

KeySelector

.

A

KeySelectorException

can contain a cause: another
throwable that caused this

KeySelectorException

to get thrown.

**Since:** 1.6
**See Also:** Serialized Form

public class

KeySelectorException

extends

Exception

Indicates an exceptional condition thrown by a

KeySelector

.

A

KeySelectorException

can contain a cause: another
throwable that caused this

KeySelectorException

to get thrown.

A

KeySelectorException

can contain a cause: another
throwable that caused this

KeySelectorException

to get thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeySelectorException

()

Constructs a new

KeySelectorException

with

null

as its detail message.

KeySelectorException

​(

String

message)

Constructs a new

KeySelectorException

with the specified
detail message.

KeySelectorException

​(

String

message,

Throwable

cause)

Constructs a new

KeySelectorException

with the
specified detail message and cause.

KeySelectorException

​(

Throwable

cause)

Constructs a new

KeySelectorException

with the specified
cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Throwable

getCause

()

Returns the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown.

void

printStackTrace

()

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the standard error stream.

void

printStackTrace

​(

PrintStream

s)

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print stream.

void

printStackTrace

​(

PrintWriter

s)

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print writer.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

KeySelectorException

()

Constructs a new

KeySelectorException

with

null

as its detail message.

KeySelectorException

​(

String

message)

Constructs a new

KeySelectorException

with the specified
detail message.

KeySelectorException

​(

String

message,

Throwable

cause)

Constructs a new

KeySelectorException

with the
specified detail message and cause.

KeySelectorException

​(

Throwable

cause)

Constructs a new

KeySelectorException

with the specified
cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a new

KeySelectorException

with

null

as its detail message.

Constructs a new

KeySelectorException

with the specified
detail message.

Constructs a new

KeySelectorException

with the
specified detail message and cause.

Constructs a new

KeySelectorException

with the specified
cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Throwable

getCause

()

Returns the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown.

void

printStackTrace

()

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the standard error stream.

void

printStackTrace

​(

PrintStream

s)

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print stream.

void

printStackTrace

​(

PrintWriter

s)

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print writer.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

Returns the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown.

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the standard error stream.

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print stream.

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print writer.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

- KeySelectorException

```java
public KeySelectorException()
```

Constructs a new

KeySelectorException

with

null

as its detail message.

- KeySelectorException

```java
public KeySelectorException​(
String
message)
```

Constructs a new

KeySelectorException

with the specified
detail message.

**Parameters:** message

- the detail message

- KeySelectorException

```java
public KeySelectorException​(
String
message,

Throwable
cause)
```

Constructs a new

KeySelectorException

with the
specified detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

- KeySelectorException

```java
public KeySelectorException​(
Throwable
cause)
```

Constructs a new

KeySelectorException

with the specified
cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

============ METHOD DETAIL ==========

- Method Detail

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

KeySelectorException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown.

- printStackTrace

```java
public void printStackTrace()
```

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the standard error stream.

**Overrides:** printStackTrace

in class

Throwable

- printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print stream.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

-

PrintStream

to use for output

- printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print writer.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

-

PrintWriter

to use for output

Constructor Detail

- KeySelectorException

```java
public KeySelectorException()
```

Constructs a new

KeySelectorException

with

null

as its detail message.

- KeySelectorException

```java
public KeySelectorException​(
String
message)
```

Constructs a new

KeySelectorException

with the specified
detail message.

**Parameters:** message

- the detail message

- KeySelectorException

```java
public KeySelectorException​(
String
message,

Throwable
cause)
```

Constructs a new

KeySelectorException

with the
specified detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

- KeySelectorException

```java
public KeySelectorException​(
Throwable
cause)
```

Constructs a new

KeySelectorException

with the specified
cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### Constructor Detail

KeySelectorException

```java
public KeySelectorException()
```

Constructs a new

KeySelectorException

with

null

as its detail message.

---

#### KeySelectorException

public KeySelectorException()

Constructs a new

KeySelectorException

with

null

as its detail message.

KeySelectorException

```java
public KeySelectorException​(
String
message)
```

Constructs a new

KeySelectorException

with the specified
detail message.

**Parameters:** message

- the detail message

---

#### KeySelectorException

public KeySelectorException​(

String

message)

Constructs a new

KeySelectorException

with the specified
detail message.

KeySelectorException

```java
public KeySelectorException​(
String
message,

Throwable
cause)
```

Constructs a new

KeySelectorException

with the
specified detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

**Parameters:** message

- the detail message
**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### KeySelectorException

public KeySelectorException​(

String

message,

Throwable

cause)

Constructs a new

KeySelectorException

with the
specified detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this exception's detail message.

KeySelectorException

```java
public KeySelectorException​(
Throwable
cause)
```

Constructs a new

KeySelectorException

with the specified
cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### KeySelectorException

public KeySelectorException​(

Throwable

cause)

Constructs a new

KeySelectorException

with the specified
cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

Method Detail

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

KeySelectorException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown.

- printStackTrace

```java
public void printStackTrace()
```

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the standard error stream.

**Overrides:** printStackTrace

in class

Throwable

- printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print stream.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

-

PrintStream

to use for output

- printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print writer.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

-

PrintWriter

to use for output

---

#### Method Detail

getCause

```java
public
Throwable
getCause()
```

Returns the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

KeySelectorException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown.

---

#### getCause

public

Throwable

getCause()

Returns the cause of this

KeySelectorException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

KeySelectorException

to get thrown.)

printStackTrace

```java
public void printStackTrace()
```

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the standard error stream.

**Overrides:** printStackTrace

in class

Throwable

---

#### printStackTrace

public void printStackTrace()

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the standard error stream.

printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print stream.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

-

PrintStream

to use for output

---

#### printStackTrace

public void printStackTrace​(

PrintStream

s)

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print stream.

printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print writer.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

-

PrintWriter

to use for output

---

#### printStackTrace

public void printStackTrace​(

PrintWriter

s)

Prints this

KeySelectorException

, its backtrace and
the cause's backtrace to the specified print writer.

---

