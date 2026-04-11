# Class URIReferenceException

**Source:** `java.xml.crypto\javax\xml\crypto\URIReferenceException.html`

### Class Description

```java
public class
URIReferenceException

extends
Exception
```

Indicates an exceptional condition thrown while dereferencing a

URIReference

.

A

URIReferenceException

can contain a cause: another
throwable that caused this

URIReferenceException

to get thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public URIReferenceException()

Constructs a new

URIReferenceException

with

null

as its detail message.

---

#### public URIReferenceException​(
String
message)

Constructs a new

URIReferenceException

with the specified
detail message.

**Parameters:**
- message

- the detail message

---

#### public URIReferenceException​(
String
message,

Throwable
cause)

Constructs a new

URIReferenceException

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

#### public URIReferenceException​(
String
message,

Throwable
cause,

URIReference
uriReference)

Constructs a new

URIReferenceException

with the
specified detail message, cause and

URIReference

.

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
- uriReference

- the

URIReference

that was being
dereferenced when the error was encountered

**Throws:**
- NullPointerException

- if

uriReference

is

null

---

#### public URIReferenceException​(
Throwable
cause)

Constructs a new

URIReferenceException

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and detail
message of

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
URIReference
getURIReference()

Returns the

URIReference

that was being dereferenced
when the exception was thrown.

**Returns:**
- the

URIReference

that was being dereferenced
when the exception was thrown, or

null

if not specified

---

#### public
Throwable
getCause()

Returns the cause of this

URIReferenceException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

URIReferenceException

to get thrown.)

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause of this

URIReferenceException

or

null

if the cause is nonexistent or unknown.

---

#### public void printStackTrace()

Prints this

URIReferenceException

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

URIReferenceException

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

URIReferenceException

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

#### Class URIReferenceException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.xml.crypto.URIReferenceException

java.lang.Throwable

- java.lang.Exception
- - javax.xml.crypto.URIReferenceException

java.lang.Exception

- javax.xml.crypto.URIReferenceException

javax.xml.crypto.URIReferenceException

**All Implemented Interfaces:** Serializable

```java
public class
URIReferenceException

extends
Exception
```

Indicates an exceptional condition thrown while dereferencing a

URIReference

.

A

URIReferenceException

can contain a cause: another
throwable that caused this

URIReferenceException

to get thrown.

**Since:** 1.6
**See Also:** URIDereferencer.dereference(URIReference, XMLCryptoContext)

,

RetrievalMethod.dereference(XMLCryptoContext)

,

Serialized Form

public class

URIReferenceException

extends

Exception

Indicates an exceptional condition thrown while dereferencing a

URIReference

.

A

URIReferenceException

can contain a cause: another
throwable that caused this

URIReferenceException

to get thrown.

A

URIReferenceException

can contain a cause: another
throwable that caused this

URIReferenceException

to get thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

URIReferenceException

()

Constructs a new

URIReferenceException

with

null

as its detail message.

URIReferenceException

​(

String

message)

Constructs a new

URIReferenceException

with the specified
detail message.

URIReferenceException

​(

String

message,

Throwable

cause)

Constructs a new

URIReferenceException

with the
specified detail message and cause.

URIReferenceException

​(

String

message,

Throwable

cause,

URIReference

uriReference)

Constructs a new

URIReferenceException

with the
specified detail message, cause and

URIReference

.

URIReferenceException

​(

Throwable

cause)

Constructs a new

URIReferenceException

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and detail
message of

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

URIReferenceException

or

null

if the cause is nonexistent or unknown.

URIReference

getURIReference

()

Returns the

URIReference

that was being dereferenced
when the exception was thrown.

void

printStackTrace

()

Prints this

URIReferenceException

, its backtrace and
the cause's backtrace to the standard error stream.

void

printStackTrace

​(

PrintStream

s)

Prints this

URIReferenceException

, its backtrace and
the cause's backtrace to the specified print stream.

void

printStackTrace

​(

PrintWriter

s)

Prints this

URIReferenceException

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

URIReferenceException

()

Constructs a new

URIReferenceException

with

null

as its detail message.

URIReferenceException

​(

String

message)

Constructs a new

URIReferenceException

with the specified
detail message.

URIReferenceException

​(

String

message,

Throwable

cause)

Constructs a new

URIReferenceException

with the
specified detail message and cause.

URIReferenceException

​(

String

message,

Throwable

cause,

URIReference

uriReference)

Constructs a new

URIReferenceException

with the
specified detail message, cause and

URIReference

.

URIReferenceException

​(

Throwable

cause)

Constructs a new

URIReferenceException

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and detail
message of

cause

).

---

#### Constructor Summary

Constructs a new

URIReferenceException

with

null

as its detail message.

Constructs a new

URIReferenceException

with the specified
detail message.

Constructs a new

URIReferenceException

with the
specified detail message and cause.

Constructs a new

URIReferenceException

with the
specified detail message, cause and

URIReference

.

Constructs a new

URIReferenceException

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and detail
message of

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

URIReferenceException

or

null

if the cause is nonexistent or unknown.

URIReference

getURIReference

()

Returns the

URIReference

that was being dereferenced
when the exception was thrown.

void

printStackTrace

()

Prints this

URIReferenceException

, its backtrace and
the cause's backtrace to the standard error stream.

void

printStackTrace

​(

PrintStream

s)

Prints this

URIReferenceException

, its backtrace and
the cause's backtrace to the specified print stream.

void

printStackTrace

​(

PrintWriter

s)

Prints this

URIReferenceException

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

URIReferenceException

or

null

if the cause is nonexistent or unknown.

Returns the

URIReference

that was being dereferenced
when the exception was thrown.

Prints this

URIReferenceException

, its backtrace and
the cause's backtrace to the standard error stream.

Prints this

URIReferenceException

, its backtrace and
the cause's backtrace to the specified print stream.

Prints this

URIReferenceException

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

- URIReferenceException

```java
public URIReferenceException()
```

Constructs a new

URIReferenceException

with

null

as its detail message.

- URIReferenceException

```java
public URIReferenceException​(
String
message)
```

Constructs a new

URIReferenceException

with the specified
detail message.

**Parameters:** message

- the detail message

- URIReferenceException

```java
public URIReferenceException​(
String
message,

Throwable
cause)
```

Constructs a new

URIReferenceException

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

- URIReferenceException

```java
public URIReferenceException​(
String
message,

Throwable
cause,

URIReference
uriReference)
```

Constructs a new

URIReferenceException

with the
specified detail message, cause and

URIReference

.

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
**Parameters:** uriReference

- the

URIReference

that was being
dereferenced when the error was encountered
**Throws:** NullPointerException

- if

uriReference

is

null

- URIReferenceException

```java
public URIReferenceException​(
Throwable
cause)
```

Constructs a new

URIReferenceException

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and detail
message of

cause

).

**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

============ METHOD DETAIL ==========

- Method Detail

- getURIReference

```java
public
URIReference
getURIReference()
```

Returns the

URIReference

that was being dereferenced
when the exception was thrown.

**Returns:** the

URIReference

that was being dereferenced
when the exception was thrown, or

null

if not specified

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this

URIReferenceException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

URIReferenceException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

URIReferenceException

or

null

if the cause is nonexistent or unknown.

- printStackTrace

```java
public void printStackTrace()
```

Prints this

URIReferenceException

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

URIReferenceException

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

URIReferenceException

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

- URIReferenceException

```java
public URIReferenceException()
```

Constructs a new

URIReferenceException

with

null

as its detail message.

- URIReferenceException

```java
public URIReferenceException​(
String
message)
```

Constructs a new

URIReferenceException

with the specified
detail message.

**Parameters:** message

- the detail message

- URIReferenceException

```java
public URIReferenceException​(
String
message,

Throwable
cause)
```

Constructs a new

URIReferenceException

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

- URIReferenceException

```java
public URIReferenceException​(
String
message,

Throwable
cause,

URIReference
uriReference)
```

Constructs a new

URIReferenceException

with the
specified detail message, cause and

URIReference

.

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
**Parameters:** uriReference

- the

URIReference

that was being
dereferenced when the error was encountered
**Throws:** NullPointerException

- if

uriReference

is

null

- URIReferenceException

```java
public URIReferenceException​(
Throwable
cause)
```

Constructs a new

URIReferenceException

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and detail
message of

cause

).

**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### Constructor Detail

URIReferenceException

```java
public URIReferenceException()
```

Constructs a new

URIReferenceException

with

null

as its detail message.

---

#### URIReferenceException

public URIReferenceException()

Constructs a new

URIReferenceException

with

null

as its detail message.

URIReferenceException

```java
public URIReferenceException​(
String
message)
```

Constructs a new

URIReferenceException

with the specified
detail message.

**Parameters:** message

- the detail message

---

#### URIReferenceException

public URIReferenceException​(

String

message)

Constructs a new

URIReferenceException

with the specified
detail message.

URIReferenceException

```java
public URIReferenceException​(
String
message,

Throwable
cause)
```

Constructs a new

URIReferenceException

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

#### URIReferenceException

public URIReferenceException​(

String

message,

Throwable

cause)

Constructs a new

URIReferenceException

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

URIReferenceException

```java
public URIReferenceException​(
String
message,

Throwable
cause,

URIReference
uriReference)
```

Constructs a new

URIReferenceException

with the
specified detail message, cause and

URIReference

.

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
**Parameters:** uriReference

- the

URIReference

that was being
dereferenced when the error was encountered
**Throws:** NullPointerException

- if

uriReference

is

null

---

#### URIReferenceException

public URIReferenceException​(

String

message,

Throwable

cause,

URIReference

uriReference)

Constructs a new

URIReferenceException

with the
specified detail message, cause and

URIReference

.

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

URIReferenceException

```java
public URIReferenceException​(
Throwable
cause)
```

Constructs a new

URIReferenceException

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and detail
message of

cause

).

**Parameters:** cause

- the cause (A

null

value is permitted, and
indicates that the cause is nonexistent or unknown.)

---

#### URIReferenceException

public URIReferenceException​(

Throwable

cause)

Constructs a new

URIReferenceException

with the specified
cause and a detail message of

(cause==null ? null :
cause.toString())

(which typically contains the class and detail
message of

cause

).

Method Detail

- getURIReference

```java
public
URIReference
getURIReference()
```

Returns the

URIReference

that was being dereferenced
when the exception was thrown.

**Returns:** the

URIReference

that was being dereferenced
when the exception was thrown, or

null

if not specified

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this

URIReferenceException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

URIReferenceException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

URIReferenceException

or

null

if the cause is nonexistent or unknown.

- printStackTrace

```java
public void printStackTrace()
```

Prints this

URIReferenceException

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

URIReferenceException

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

URIReferenceException

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

getURIReference

```java
public
URIReference
getURIReference()
```

Returns the

URIReference

that was being dereferenced
when the exception was thrown.

**Returns:** the

URIReference

that was being dereferenced
when the exception was thrown, or

null

if not specified

---

#### getURIReference

public

URIReference

getURIReference()

Returns the

URIReference

that was being dereferenced
when the exception was thrown.

getCause

```java
public
Throwable
getCause()
```

Returns the cause of this

URIReferenceException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

URIReferenceException

to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this

URIReferenceException

or

null

if the cause is nonexistent or unknown.

---

#### getCause

public

Throwable

getCause()

Returns the cause of this

URIReferenceException

or

null

if the cause is nonexistent or unknown. (The
cause is the throwable that caused this

URIReferenceException

to get thrown.)

printStackTrace

```java
public void printStackTrace()
```

Prints this

URIReferenceException

, its backtrace and
the cause's backtrace to the standard error stream.

**Overrides:** printStackTrace

in class

Throwable

---

#### printStackTrace

public void printStackTrace()

Prints this

URIReferenceException

, its backtrace and
the cause's backtrace to the standard error stream.

printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Prints this

URIReferenceException

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

URIReferenceException

, its backtrace and
the cause's backtrace to the specified print stream.

printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Prints this

URIReferenceException

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

URIReferenceException

, its backtrace and
the cause's backtrace to the specified print writer.

---

