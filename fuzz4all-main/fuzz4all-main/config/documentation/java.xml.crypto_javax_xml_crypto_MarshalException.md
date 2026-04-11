# Class MarshalException

**Source:** `java.xml.crypto\javax\xml\crypto\MarshalException.html`

### Class Description

```java
public class
MarshalException

extends
Exception
```

Indicates an exceptional condition that occurred during the XML
marshalling or unmarshalling process.

A

MarshalException

can contain a cause: another
throwable that caused this

MarshalException

to get thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MarshalException()

Constructs a new

MarshalException

with

null

as its detail message.

---

#### public MarshalException​(
String
message)

Constructs a new

MarshalException

with the specified
detail message.

**Parameters:**
- message

- the detail message

---

#### public MarshalException​(
String
message,

Throwable
cause)

Constructs a new

MarshalException

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

#### public MarshalException​(
Throwable
cause)

Constructs a new

MarshalException

with the specified cause
and a detail message of

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

MarshalException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

MarshalException

to get thrown.)

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause of this

MarshalException

or

null

if the cause is nonexistent or unknown.

---

#### public void printStackTrace()

Prints this

MarshalException

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

MarshalException

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

MarshalException

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

#### Class MarshalException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.xml.crypto.MarshalException

java.lang.Throwable

- java.lang.Exception
- - javax.xml.crypto.MarshalException

java.lang.Exception

- javax.xml.crypto.MarshalException

javax.xml.crypto.MarshalException

**All Implemented Interfaces:** Serializable

```java
public class
MarshalException

extends
Exception
```

Indicates an exceptional condition that occurred during the XML
marshalling or unmarshalling process.

A

MarshalException

can contain a cause: another
throwable that caused this

MarshalException

to get thrown.

**Since:** 1.6
**See Also:** XMLSignature.sign(XMLSignContext)

,

XMLSignatureFactory.unmarshalXMLSignature(XMLValidateContext)

,

Serialized Form

public class

MarshalException

extends

Exception

Indicates an exceptional condition that occurred during the XML
marshalling or unmarshalling process.

A

MarshalException

can contain a cause: another
throwable that caused this

MarshalException

to get thrown.

A

MarshalException

can contain a cause: another
throwable that caused this

MarshalException

to get thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MarshalException

()

Constructs a new

MarshalException

with

null

as its detail message.

MarshalException

​(

String

message)

Constructs a new

MarshalException

with the specified
detail message.

MarshalException

​(

String

message,

Throwable

cause)

Constructs a new

MarshalException

with the
specified detail message and cause.

MarshalException

​(

Throwable

cause)

Constructs a new

MarshalException

with the specified cause
and a detail message of

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

MarshalException

or

null

if the cause is nonexistent or unknown.

void

printStackTrace

()

Prints this

MarshalException

, its backtrace and
the cause's backtrace to the standard error stream.

void

printStackTrace

​(

PrintStream

s)

Prints this

MarshalException

, its backtrace and
the cause's backtrace to the specified print stream.

void

printStackTrace

​(

PrintWriter

s)

Prints this

MarshalException

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

MarshalException

()

Constructs a new

MarshalException

with

null

as its detail message.

MarshalException

​(

String

message)

Constructs a new

MarshalException

with the specified
detail message.

MarshalException

​(

String

message,

Throwable

cause)

Constructs a new

MarshalException

with the
specified detail message and cause.

MarshalException

​(

Throwable

cause)

Constructs a new

MarshalException

with the specified cause
and a detail message of

(cause==null ? null : cause.toString())

(which typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs a new

MarshalException

with

null

as its detail message.

Constructs a new

MarshalException

with the specified
detail message.

Constructs a new

MarshalException

with the
specified detail message and cause.

Constructs a new

MarshalException

with the specified cause
and a detail message of

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

MarshalException

or

null

if the cause is nonexistent or unknown.

void

printStackTrace

()

Prints this

MarshalException

, its backtrace and
the cause's backtrace to the standard error stream.

void

printStackTrace

​(

PrintStream

s)

Prints this

MarshalException

, its backtrace and
the cause's backtrace to the specified print stream.

void

printStackTrace

​(

PrintWriter

s)

Prints this

MarshalException

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

MarshalException

or

null

if the cause is nonexistent or unknown.

Prints this

MarshalException

, its backtrace and
the cause's backtrace to the standard error stream.

Prints this

MarshalException

, its backtrace and
the cause's backtrace to the specified print stream.

Prints this

MarshalException

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

- MarshalException

```java
public MarshalException()
```

Constructs a new

MarshalException

with

null

as its detail message.

- MarshalException

```java
public MarshalException​(
String
message)
```

Constructs a new

MarshalException

with the specified
detail message.

**Parameters:** message

- the detail message

- MarshalException

```java
public MarshalException​(
String
message,

Throwable
cause)
```

Constructs a new

MarshalException

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

- MarshalException

```java
public MarshalException​(
Throwable
cause)
```

Constructs a new

MarshalException

with the specified cause
and a detail message of

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

MarshalException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

MarshalException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

MarshalException

or

null

if the cause is nonexistent or unknown.

- printStackTrace

```java
public void printStackTrace()
```

Prints this

MarshalException

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

MarshalException

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

MarshalException

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

- MarshalException

```java
public MarshalException()
```

Constructs a new

MarshalException

with

null

as its detail message.

- MarshalException

```java
public MarshalException​(
String
message)
```

Constructs a new

MarshalException

with the specified
detail message.

**Parameters:** message

- the detail message

- MarshalException

```java
public MarshalException​(
String
message,

Throwable
cause)
```

Constructs a new

MarshalException

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

- MarshalException

```java
public MarshalException​(
Throwable
cause)
```

Constructs a new

MarshalException

with the specified cause
and a detail message of

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

MarshalException

```java
public MarshalException()
```

Constructs a new

MarshalException

with

null

as its detail message.

---

#### MarshalException

public MarshalException()

Constructs a new

MarshalException

with

null

as its detail message.

MarshalException

```java
public MarshalException​(
String
message)
```

Constructs a new

MarshalException

with the specified
detail message.

**Parameters:** message

- the detail message

---

#### MarshalException

public MarshalException​(

String

message)

Constructs a new

MarshalException

with the specified
detail message.

MarshalException

```java
public MarshalException​(
String
message,

Throwable
cause)
```

Constructs a new

MarshalException

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

#### MarshalException

public MarshalException​(

String

message,

Throwable

cause)

Constructs a new

MarshalException

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

MarshalException

```java
public MarshalException​(
Throwable
cause)
```

Constructs a new

MarshalException

with the specified cause
and a detail message of

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

#### MarshalException

public MarshalException​(

Throwable

cause)

Constructs a new

MarshalException

with the specified cause
and a detail message of

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

MarshalException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

MarshalException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

MarshalException

or

null

if the cause is nonexistent or unknown.

- printStackTrace

```java
public void printStackTrace()
```

Prints this

MarshalException

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

MarshalException

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

MarshalException

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

MarshalException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

MarshalException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

MarshalException

or

null

if the cause is nonexistent or unknown.

---

#### getCause

public

Throwable

getCause()

Returns the cause of this

MarshalException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

MarshalException

to get thrown.)

printStackTrace

```java
public void printStackTrace()
```

Prints this

MarshalException

, its backtrace and
the cause's backtrace to the standard error stream.

**Overrides:** printStackTrace

in class

Throwable

---

#### printStackTrace

public void printStackTrace()

Prints this

MarshalException

, its backtrace and
the cause's backtrace to the standard error stream.

printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Prints this

MarshalException

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

MarshalException

, its backtrace and
the cause's backtrace to the specified print stream.

printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Prints this

MarshalException

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

MarshalException

, its backtrace and
the cause's backtrace to the specified print writer.

---

