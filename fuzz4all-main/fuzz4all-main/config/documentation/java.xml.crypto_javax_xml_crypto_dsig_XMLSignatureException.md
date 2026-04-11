# Class XMLSignatureException

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\XMLSignatureException.html`

### Class Description

```java
public class
XMLSignatureException

extends
Exception
```

Indicates an exceptional condition that occurred during the XML
signature generation or validation process.

An

XMLSignatureException

can contain a cause: another
throwable that caused this

XMLSignatureException

to get thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public XMLSignatureException()

Constructs a new

XMLSignatureException

with

null

as its detail message.

---

#### public XMLSignatureException​(
String
message)

Constructs a new

XMLSignatureException

with the specified
detail message.

**Parameters:**
- message

- the detail message

---

#### public XMLSignatureException​(
String
message,

Throwable
cause)

Constructs a new

XMLSignatureException

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

#### public XMLSignatureException​(
Throwable
cause)

Constructs a new

XMLSignatureException

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

XMLSignatureException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

XMLSignatureException

to get thrown.)

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause of this

XMLSignatureException

or

null

if the cause is nonexistent or unknown.

---

#### public void printStackTrace()

Prints this

XMLSignatureException

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

XMLSignatureException

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

XMLSignatureException

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

#### Class XMLSignatureException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.xml.crypto.dsig.XMLSignatureException

java.lang.Throwable

- java.lang.Exception
- - javax.xml.crypto.dsig.XMLSignatureException

java.lang.Exception

- javax.xml.crypto.dsig.XMLSignatureException

javax.xml.crypto.dsig.XMLSignatureException

**All Implemented Interfaces:** Serializable

```java
public class
XMLSignatureException

extends
Exception
```

Indicates an exceptional condition that occurred during the XML
signature generation or validation process.

An

XMLSignatureException

can contain a cause: another
throwable that caused this

XMLSignatureException

to get thrown.

**Since:** 1.6
**See Also:** Serialized Form

public class

XMLSignatureException

extends

Exception

Indicates an exceptional condition that occurred during the XML
signature generation or validation process.

An

XMLSignatureException

can contain a cause: another
throwable that caused this

XMLSignatureException

to get thrown.

An

XMLSignatureException

can contain a cause: another
throwable that caused this

XMLSignatureException

to get thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XMLSignatureException

()

Constructs a new

XMLSignatureException

with

null

as its detail message.

XMLSignatureException

​(

String

message)

Constructs a new

XMLSignatureException

with the specified
detail message.

XMLSignatureException

​(

String

message,

Throwable

cause)

Constructs a new

XMLSignatureException

with the
specified detail message and cause.

XMLSignatureException

​(

Throwable

cause)

Constructs a new

XMLSignatureException

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

XMLSignatureException

or

null

if the cause is nonexistent or unknown.

void

printStackTrace

()

Prints this

XMLSignatureException

, its backtrace and
the cause's backtrace to the standard error stream.

void

printStackTrace

​(

PrintStream

s)

Prints this

XMLSignatureException

, its backtrace and
the cause's backtrace to the specified print stream.

void

printStackTrace

​(

PrintWriter

s)

Prints this

XMLSignatureException

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

XMLSignatureException

()

Constructs a new

XMLSignatureException

with

null

as its detail message.

XMLSignatureException

​(

String

message)

Constructs a new

XMLSignatureException

with the specified
detail message.

XMLSignatureException

​(

String

message,

Throwable

cause)

Constructs a new

XMLSignatureException

with the
specified detail message and cause.

XMLSignatureException

​(

Throwable

cause)

Constructs a new

XMLSignatureException

with the specified
cause and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a new

XMLSignatureException

with

null

as its detail message.

Constructs a new

XMLSignatureException

with the specified
detail message.

Constructs a new

XMLSignatureException

with the
specified detail message and cause.

Constructs a new

XMLSignatureException

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

XMLSignatureException

or

null

if the cause is nonexistent or unknown.

void

printStackTrace

()

Prints this

XMLSignatureException

, its backtrace and
the cause's backtrace to the standard error stream.

void

printStackTrace

​(

PrintStream

s)

Prints this

XMLSignatureException

, its backtrace and
the cause's backtrace to the specified print stream.

void

printStackTrace

​(

PrintWriter

s)

Prints this

XMLSignatureException

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

XMLSignatureException

or

null

if the cause is nonexistent or unknown.

Prints this

XMLSignatureException

, its backtrace and
the cause's backtrace to the standard error stream.

Prints this

XMLSignatureException

, its backtrace and
the cause's backtrace to the specified print stream.

Prints this

XMLSignatureException

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

- XMLSignatureException

```java
public XMLSignatureException()
```

Constructs a new

XMLSignatureException

with

null

as its detail message.

- XMLSignatureException

```java
public XMLSignatureException​(
String
message)
```

Constructs a new

XMLSignatureException

with the specified
detail message.

**Parameters:** message

- the detail message

- XMLSignatureException

```java
public XMLSignatureException​(
String
message,

Throwable
cause)
```

Constructs a new

XMLSignatureException

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

- XMLSignatureException

```java
public XMLSignatureException​(
Throwable
cause)
```

Constructs a new

XMLSignatureException

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

XMLSignatureException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

XMLSignatureException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

XMLSignatureException

or

null

if the cause is nonexistent or unknown.

- printStackTrace

```java
public void printStackTrace()
```

Prints this

XMLSignatureException

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

XMLSignatureException

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

XMLSignatureException

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

- XMLSignatureException

```java
public XMLSignatureException()
```

Constructs a new

XMLSignatureException

with

null

as its detail message.

- XMLSignatureException

```java
public XMLSignatureException​(
String
message)
```

Constructs a new

XMLSignatureException

with the specified
detail message.

**Parameters:** message

- the detail message

- XMLSignatureException

```java
public XMLSignatureException​(
String
message,

Throwable
cause)
```

Constructs a new

XMLSignatureException

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

- XMLSignatureException

```java
public XMLSignatureException​(
Throwable
cause)
```

Constructs a new

XMLSignatureException

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

XMLSignatureException

```java
public XMLSignatureException()
```

Constructs a new

XMLSignatureException

with

null

as its detail message.

---

#### XMLSignatureException

public XMLSignatureException()

Constructs a new

XMLSignatureException

with

null

as its detail message.

XMLSignatureException

```java
public XMLSignatureException​(
String
message)
```

Constructs a new

XMLSignatureException

with the specified
detail message.

**Parameters:** message

- the detail message

---

#### XMLSignatureException

public XMLSignatureException​(

String

message)

Constructs a new

XMLSignatureException

with the specified
detail message.

XMLSignatureException

```java
public XMLSignatureException​(
String
message,

Throwable
cause)
```

Constructs a new

XMLSignatureException

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

#### XMLSignatureException

public XMLSignatureException​(

String

message,

Throwable

cause)

Constructs a new

XMLSignatureException

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

XMLSignatureException

```java
public XMLSignatureException​(
Throwable
cause)
```

Constructs a new

XMLSignatureException

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

#### XMLSignatureException

public XMLSignatureException​(

Throwable

cause)

Constructs a new

XMLSignatureException

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

XMLSignatureException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

XMLSignatureException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

XMLSignatureException

or

null

if the cause is nonexistent or unknown.

- printStackTrace

```java
public void printStackTrace()
```

Prints this

XMLSignatureException

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

XMLSignatureException

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

XMLSignatureException

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

XMLSignatureException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

XMLSignatureException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

XMLSignatureException

or

null

if the cause is nonexistent or unknown.

---

#### getCause

public

Throwable

getCause()

Returns the cause of this

XMLSignatureException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

XMLSignatureException

to get thrown.)

printStackTrace

```java
public void printStackTrace()
```

Prints this

XMLSignatureException

, its backtrace and
the cause's backtrace to the standard error stream.

**Overrides:** printStackTrace

in class

Throwable

---

#### printStackTrace

public void printStackTrace()

Prints this

XMLSignatureException

, its backtrace and
the cause's backtrace to the standard error stream.

printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Prints this

XMLSignatureException

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

XMLSignatureException

, its backtrace and
the cause's backtrace to the specified print stream.

printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Prints this

XMLSignatureException

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

XMLSignatureException

, its backtrace and
the cause's backtrace to the specified print writer.

---

