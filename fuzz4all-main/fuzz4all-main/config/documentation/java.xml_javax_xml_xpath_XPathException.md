# Class XPathException

**Source:** `java.xml\javax\xml\xpath\XPathException.html`

### Class Description

```java
public class
XPathException

extends
Exception
```

XPathException

represents a generic XPath exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public XPathException​(
String
message)

Constructs a new

XPathException

with the specified detail

message

.

The

cause

is not initialized.

If

message

is

null

,
then a

NullPointerException

is thrown.

**Parameters:**
- message

- The detail message.

**Throws:**
- NullPointerException

- When

message

is

null

.

---

#### public XPathException​(
Throwable
cause)

Constructs a new

XPathException

with the specified

cause

.

If

cause

is

null

,
then a

NullPointerException

is thrown.

**Parameters:**
- cause

- The cause.

**Throws:**
- NullPointerException

- if

cause

is

null

.

---

### Method Details

#### public
Throwable
getCause()

Get the cause of this XPathException.

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- Cause of this XPathException.

---

#### public void printStackTrace​(
PrintStream
s)

Print stack trace to specified

PrintStream

.

**Overrides:**
- printStackTrace

in class

Throwable

**Parameters:**
- s

- Print stack trace to this

PrintStream

.

---

#### public void printStackTrace()

Print stack trace to

System.err

.

**Overrides:**
- printStackTrace

in class

Throwable

---

#### public void printStackTrace​(
PrintWriter
s)

Print stack trace to specified

PrintWriter

.

**Overrides:**
- printStackTrace

in class

Throwable

**Parameters:**
- s

- Print stack trace to this

PrintWriter

.

---

### Additional Sections

#### Class XPathException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.xml.xpath.XPathException

java.lang.Throwable

- java.lang.Exception
- - javax.xml.xpath.XPathException

java.lang.Exception

- javax.xml.xpath.XPathException

javax.xml.xpath.XPathException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** XPathExpressionException

,

XPathFactoryConfigurationException

```java
public class
XPathException

extends
Exception
```

XPathException

represents a generic XPath exception.

**Since:** 1.5
**See Also:** Serialized Form

public class

XPathException

extends

Exception

XPathException

represents a generic XPath exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XPathException

​(

String

message)

Constructs a new

XPathException

with the specified detail

message

.

XPathException

​(

Throwable

cause)

Constructs a new

XPathException

with the specified

cause

.

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

Get the cause of this XPathException.

void

printStackTrace

()

Print stack trace to

System.err

.

void

printStackTrace

​(

PrintStream

s)

Print stack trace to specified

PrintStream

.

void

printStackTrace

​(

PrintWriter

s)

Print stack trace to specified

PrintWriter

.

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

XPathException

​(

String

message)

Constructs a new

XPathException

with the specified detail

message

.

XPathException

​(

Throwable

cause)

Constructs a new

XPathException

with the specified

cause

.

---

#### Constructor Summary

Constructs a new

XPathException

with the specified detail

message

.

Constructs a new

XPathException

with the specified

cause

.

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

Get the cause of this XPathException.

void

printStackTrace

()

Print stack trace to

System.err

.

void

printStackTrace

​(

PrintStream

s)

Print stack trace to specified

PrintStream

.

void

printStackTrace

​(

PrintWriter

s)

Print stack trace to specified

PrintWriter

.

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

Get the cause of this XPathException.

Print stack trace to

System.err

.

Print stack trace to specified

PrintStream

.

Print stack trace to specified

PrintWriter

.

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

- XPathException

```java
public XPathException​(
String
message)
```

Constructs a new

XPathException

with the specified detail

message

.

The

cause

is not initialized.

If

message

is

null

,
then a

NullPointerException

is thrown.

**Parameters:** message

- The detail message.
**Throws:** NullPointerException

- When

message

is

null

.

- XPathException

```java
public XPathException​(
Throwable
cause)
```

Constructs a new

XPathException

with the specified

cause

.

If

cause

is

null

,
then a

NullPointerException

is thrown.

**Parameters:** cause

- The cause.
**Throws:** NullPointerException

- if

cause

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- getCause

```java
public
Throwable
getCause()
```

Get the cause of this XPathException.

**Overrides:** getCause

in class

Throwable
**Returns:** Cause of this XPathException.

- printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Print stack trace to specified

PrintStream

.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- Print stack trace to this

PrintStream

.

- printStackTrace

```java
public void printStackTrace()
```

Print stack trace to

System.err

.

**Overrides:** printStackTrace

in class

Throwable

- printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Print stack trace to specified

PrintWriter

.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- Print stack trace to this

PrintWriter

.

Constructor Detail

- XPathException

```java
public XPathException​(
String
message)
```

Constructs a new

XPathException

with the specified detail

message

.

The

cause

is not initialized.

If

message

is

null

,
then a

NullPointerException

is thrown.

**Parameters:** message

- The detail message.
**Throws:** NullPointerException

- When

message

is

null

.

- XPathException

```java
public XPathException​(
Throwable
cause)
```

Constructs a new

XPathException

with the specified

cause

.

If

cause

is

null

,
then a

NullPointerException

is thrown.

**Parameters:** cause

- The cause.
**Throws:** NullPointerException

- if

cause

is

null

.

---

#### Constructor Detail

XPathException

```java
public XPathException​(
String
message)
```

Constructs a new

XPathException

with the specified detail

message

.

The

cause

is not initialized.

If

message

is

null

,
then a

NullPointerException

is thrown.

**Parameters:** message

- The detail message.
**Throws:** NullPointerException

- When

message

is

null

.

---

#### XPathException

public XPathException​(

String

message)

Constructs a new

XPathException

with the specified detail

message

.

The

cause

is not initialized.

If

message

is

null

,
then a

NullPointerException

is thrown.

The

cause

is not initialized.

If

message

is

null

,
then a

NullPointerException

is thrown.

If

message

is

null

,
then a

NullPointerException

is thrown.

XPathException

```java
public XPathException​(
Throwable
cause)
```

Constructs a new

XPathException

with the specified

cause

.

If

cause

is

null

,
then a

NullPointerException

is thrown.

**Parameters:** cause

- The cause.
**Throws:** NullPointerException

- if

cause

is

null

.

---

#### XPathException

public XPathException​(

Throwable

cause)

Constructs a new

XPathException

with the specified

cause

.

If

cause

is

null

,
then a

NullPointerException

is thrown.

If

cause

is

null

,
then a

NullPointerException

is thrown.

Method Detail

- getCause

```java
public
Throwable
getCause()
```

Get the cause of this XPathException.

**Overrides:** getCause

in class

Throwable
**Returns:** Cause of this XPathException.

- printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Print stack trace to specified

PrintStream

.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- Print stack trace to this

PrintStream

.

- printStackTrace

```java
public void printStackTrace()
```

Print stack trace to

System.err

.

**Overrides:** printStackTrace

in class

Throwable

- printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Print stack trace to specified

PrintWriter

.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- Print stack trace to this

PrintWriter

.

---

#### Method Detail

getCause

```java
public
Throwable
getCause()
```

Get the cause of this XPathException.

**Overrides:** getCause

in class

Throwable
**Returns:** Cause of this XPathException.

---

#### getCause

public

Throwable

getCause()

Get the cause of this XPathException.

printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Print stack trace to specified

PrintStream

.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- Print stack trace to this

PrintStream

.

---

#### printStackTrace

public void printStackTrace​(

PrintStream

s)

Print stack trace to specified

PrintStream

.

printStackTrace

```java
public void printStackTrace()
```

Print stack trace to

System.err

.

**Overrides:** printStackTrace

in class

Throwable

---

#### printStackTrace

public void printStackTrace()

Print stack trace to

System.err

.

printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Print stack trace to specified

PrintWriter

.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- Print stack trace to this

PrintWriter

.

---

#### printStackTrace

public void printStackTrace​(

PrintWriter

s)

Print stack trace to specified

PrintWriter

.

---

