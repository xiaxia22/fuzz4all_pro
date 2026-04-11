# Class IIOInvalidTreeException

**Source:** `java.desktop\javax\imageio\metadata\IIOInvalidTreeException.html`

### Class Description

```java
public class
IIOInvalidTreeException

extends
IIOException
```

An

IIOInvalidTreeException

is thrown when an attempt
by an

IIOMetadata

object to parse a tree of

IIOMetadataNode

s fails. The node that led to the
parsing error may be stored. As with any parsing error, the actual
error may occur at a different point that that where it is
detected. The node returned by

getOffendingNode

should merely be considered as a clue to the actual nature of the
problem.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Node
offendingNode

The

Node

that led to the parsing error, or

null

.

---

### Constructor Details

#### public IIOInvalidTreeException​(
String
message,

Node
offendingNode)

Constructs an

IIOInvalidTreeException

with a
message string and a reference to the

Node

that
caused the parsing error.

**Parameters:**
- message

- a

String

containing the reason for
the parsing failure.
- offendingNode

- the DOM

Node

that caused the
exception, or

null

.

---

#### public IIOInvalidTreeException​(
String
message,

Throwable
cause,

Node
offendingNode)

Constructs an

IIOInvalidTreeException

with a
message string, a reference to an exception that caused this
exception, and a reference to the

Node

that caused
the parsing error.

**Parameters:**
- message

- a

String

containing the reason for
the parsing failure.
- cause

- the

Throwable

(

Error

or

Exception

) that caused this exception to occur,
or

null

.
- offendingNode

- the DOM

Node

that caused the
exception, or

null

.

---

### Method Details

#### public
Node
getOffendingNode()

Returns the

Node

that caused the error in parsing.

**Returns:**
- the offending

Node

.

---

### Additional Sections

#### Class IIOInvalidTreeException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - javax.imageio.IIOException
- - javax.imageio.metadata.IIOInvalidTreeException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - javax.imageio.IIOException
- - javax.imageio.metadata.IIOInvalidTreeException

java.lang.Exception

- java.io.IOException
- - javax.imageio.IIOException
- - javax.imageio.metadata.IIOInvalidTreeException

java.io.IOException

- javax.imageio.IIOException
- - javax.imageio.metadata.IIOInvalidTreeException

javax.imageio.IIOException

- javax.imageio.metadata.IIOInvalidTreeException

javax.imageio.metadata.IIOInvalidTreeException

**All Implemented Interfaces:** Serializable

```java
public class
IIOInvalidTreeException

extends
IIOException
```

An

IIOInvalidTreeException

is thrown when an attempt
by an

IIOMetadata

object to parse a tree of

IIOMetadataNode

s fails. The node that led to the
parsing error may be stored. As with any parsing error, the actual
error may occur at a different point that that where it is
detected. The node returned by

getOffendingNode

should merely be considered as a clue to the actual nature of the
problem.

**See Also:** IIOMetadata.setFromTree(java.lang.String, org.w3c.dom.Node)

,

IIOMetadata.mergeTree(java.lang.String, org.w3c.dom.Node)

,

IIOMetadataNode

,

Serialized Form

public class

IIOInvalidTreeException

extends

IIOException

An

IIOInvalidTreeException

is thrown when an attempt
by an

IIOMetadata

object to parse a tree of

IIOMetadataNode

s fails. The node that led to the
parsing error may be stored. As with any parsing error, the actual
error may occur at a different point that that where it is
detected. The node returned by

getOffendingNode

should merely be considered as a clue to the actual nature of the
problem.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Node

offendingNode

The

Node

that led to the parsing error, or

null

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IIOInvalidTreeException

​(

String

message,

Throwable

cause,

Node

offendingNode)

Constructs an

IIOInvalidTreeException

with a
message string, a reference to an exception that caused this
exception, and a reference to the

Node

that caused
the parsing error.

IIOInvalidTreeException

​(

String

message,

Node

offendingNode)

Constructs an

IIOInvalidTreeException

with a
message string and a reference to the

Node

that
caused the parsing error.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Node

getOffendingNode

()

Returns the

Node

that caused the error in parsing.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

Node

offendingNode

The

Node

that led to the parsing error, or

null

.

---

#### Field Summary

The

Node

that led to the parsing error, or

null

.

Constructor Summary

Constructors

Constructor

Description

IIOInvalidTreeException

​(

String

message,

Throwable

cause,

Node

offendingNode)

Constructs an

IIOInvalidTreeException

with a
message string, a reference to an exception that caused this
exception, and a reference to the

Node

that caused
the parsing error.

IIOInvalidTreeException

​(

String

message,

Node

offendingNode)

Constructs an

IIOInvalidTreeException

with a
message string and a reference to the

Node

that
caused the parsing error.

---

#### Constructor Summary

Constructs an

IIOInvalidTreeException

with a
message string, a reference to an exception that caused this
exception, and a reference to the

Node

that caused
the parsing error.

Constructs an

IIOInvalidTreeException

with a
message string and a reference to the

Node

that
caused the parsing error.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Node

getOffendingNode

()

Returns the

Node

that caused the error in parsing.

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

Returns the

Node

that caused the error in parsing.

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

============ FIELD DETAIL ===========

- Field Detail

- offendingNode

```java
protected
Node
offendingNode
```

The

Node

that led to the parsing error, or

null

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- IIOInvalidTreeException

```java
public IIOInvalidTreeException​(
String
message,

Node
offendingNode)
```

Constructs an

IIOInvalidTreeException

with a
message string and a reference to the

Node

that
caused the parsing error.

**Parameters:** message

- a

String

containing the reason for
the parsing failure.
**Parameters:** offendingNode

- the DOM

Node

that caused the
exception, or

null

.

- IIOInvalidTreeException

```java
public IIOInvalidTreeException​(
String
message,

Throwable
cause,

Node
offendingNode)
```

Constructs an

IIOInvalidTreeException

with a
message string, a reference to an exception that caused this
exception, and a reference to the

Node

that caused
the parsing error.

**Parameters:** message

- a

String

containing the reason for
the parsing failure.
**Parameters:** cause

- the

Throwable

(

Error

or

Exception

) that caused this exception to occur,
or

null

.
**Parameters:** offendingNode

- the DOM

Node

that caused the
exception, or

null

.

============ METHOD DETAIL ==========

- Method Detail

- getOffendingNode

```java
public
Node
getOffendingNode()
```

Returns the

Node

that caused the error in parsing.

**Returns:** the offending

Node

.

Field Detail

- offendingNode

```java
protected
Node
offendingNode
```

The

Node

that led to the parsing error, or

null

.

---

#### Field Detail

offendingNode

```java
protected
Node
offendingNode
```

The

Node

that led to the parsing error, or

null

.

---

#### offendingNode

protected

Node

offendingNode

The

Node

that led to the parsing error, or

null

.

Constructor Detail

- IIOInvalidTreeException

```java
public IIOInvalidTreeException​(
String
message,

Node
offendingNode)
```

Constructs an

IIOInvalidTreeException

with a
message string and a reference to the

Node

that
caused the parsing error.

**Parameters:** message

- a

String

containing the reason for
the parsing failure.
**Parameters:** offendingNode

- the DOM

Node

that caused the
exception, or

null

.

- IIOInvalidTreeException

```java
public IIOInvalidTreeException​(
String
message,

Throwable
cause,

Node
offendingNode)
```

Constructs an

IIOInvalidTreeException

with a
message string, a reference to an exception that caused this
exception, and a reference to the

Node

that caused
the parsing error.

**Parameters:** message

- a

String

containing the reason for
the parsing failure.
**Parameters:** cause

- the

Throwable

(

Error

or

Exception

) that caused this exception to occur,
or

null

.
**Parameters:** offendingNode

- the DOM

Node

that caused the
exception, or

null

.

---

#### Constructor Detail

IIOInvalidTreeException

```java
public IIOInvalidTreeException​(
String
message,

Node
offendingNode)
```

Constructs an

IIOInvalidTreeException

with a
message string and a reference to the

Node

that
caused the parsing error.

**Parameters:** message

- a

String

containing the reason for
the parsing failure.
**Parameters:** offendingNode

- the DOM

Node

that caused the
exception, or

null

.

---

#### IIOInvalidTreeException

public IIOInvalidTreeException​(

String

message,

Node

offendingNode)

Constructs an

IIOInvalidTreeException

with a
message string and a reference to the

Node

that
caused the parsing error.

IIOInvalidTreeException

```java
public IIOInvalidTreeException​(
String
message,

Throwable
cause,

Node
offendingNode)
```

Constructs an

IIOInvalidTreeException

with a
message string, a reference to an exception that caused this
exception, and a reference to the

Node

that caused
the parsing error.

**Parameters:** message

- a

String

containing the reason for
the parsing failure.
**Parameters:** cause

- the

Throwable

(

Error

or

Exception

) that caused this exception to occur,
or

null

.
**Parameters:** offendingNode

- the DOM

Node

that caused the
exception, or

null

.

---

#### IIOInvalidTreeException

public IIOInvalidTreeException​(

String

message,

Throwable

cause,

Node

offendingNode)

Constructs an

IIOInvalidTreeException

with a
message string, a reference to an exception that caused this
exception, and a reference to the

Node

that caused
the parsing error.

Method Detail

- getOffendingNode

```java
public
Node
getOffendingNode()
```

Returns the

Node

that caused the error in parsing.

**Returns:** the offending

Node

.

---

#### Method Detail

getOffendingNode

```java
public
Node
getOffendingNode()
```

Returns the

Node

that caused the error in parsing.

**Returns:** the offending

Node

.

---

#### getOffendingNode

public

Node

getOffendingNode()

Returns the

Node

that caused the error in parsing.

---

