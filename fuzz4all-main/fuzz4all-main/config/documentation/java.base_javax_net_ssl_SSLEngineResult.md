# Class SSLEngineResult

**Source:** `java.base\javax\net\ssl\SSLEngineResult.html`

### Class Description

```java
public class
SSLEngineResult

extends
Object
```

An encapsulation of the result state produced by

SSLEngine

I/O calls.

A

SSLEngine

provides a means for establishing
secure communication sessions between two peers.

SSLEngine

operations typically consume bytes from an input buffer and produce
bytes in an output buffer. This class provides operational result
values describing the state of the

SSLEngine

, including
indications of what operations are needed to finish an
ongoing handshake. Lastly, it reports the number of bytes consumed
and produced as a result of this operation.

**Since:** 1.5
**See Also:** SSLEngine

,

SSLEngine.wrap(ByteBuffer, ByteBuffer)

,

SSLEngine.unwrap(ByteBuffer, ByteBuffer)

---

### Field Details

*No entries found.*

### Constructor Details

#### public SSLEngineResult​(
SSLEngineResult.Status
status,

SSLEngineResult.HandshakeStatus
handshakeStatus,
int bytesConsumed,
int bytesProduced)

Initializes a new instance of this class.

**Parameters:**
- status

- the return value of the operation.
- handshakeStatus

- the current handshaking status.
- bytesConsumed

- the number of bytes consumed from the source ByteBuffer
- bytesProduced

- the number of bytes placed into the destination ByteBuffer

**Throws:**
- IllegalArgumentException

- if the

status

or

handshakeStatus

arguments are null, or if

bytesConsumed

or

bytesProduced

is negative.

---

#### public SSLEngineResult​(
SSLEngineResult.Status
status,

SSLEngineResult.HandshakeStatus
handshakeStatus,
int bytesConsumed,
int bytesProduced,
long sequenceNumber)

Initializes a new instance of this class.

**Parameters:**
- status

- the return value of the operation.
- handshakeStatus

- the current handshaking status.
- bytesConsumed

- the number of bytes consumed from the source ByteBuffer
- bytesProduced

- the number of bytes placed into the destination ByteBuffer
- sequenceNumber

- the sequence number (unsigned long) of the produced or
consumed SSL/TLS/DTLS record, or

-1L

if no record
produced or consumed

**Throws:**
- IllegalArgumentException

- if the

status

or

handshakeStatus

arguments are null, or if

bytesConsumed

or

bytesProduced

is negative

**Since:**
- 9

---

### Method Details

#### public final
SSLEngineResult.Status
getStatus()

Gets the return value of this

SSLEngine

operation.

**Returns:**
- the return value

---

#### public final
SSLEngineResult.HandshakeStatus
getHandshakeStatus()

Gets the handshake status of this

SSLEngine

operation.

**Returns:**
- the handshake status

---

#### public final int bytesConsumed()

Returns the number of bytes consumed from the input buffer.

**Returns:**
- the number of bytes consumed.

---

#### public final int bytesProduced()

Returns the number of bytes written to the output buffer.

**Returns:**
- the number of bytes produced

---

#### public final long sequenceNumber()

Returns the sequence number of the produced or consumed SSL/TLS/DTLS
record (optional operation).

**Returns:**
- the sequence number of the produced or consumed SSL/TLS/DTLS
record; or

-1L

if no record is produced or consumed,
or this operation is not supported by the underlying provider

**See Also:**
- Long.compareUnsigned(long, long)

**Since:**
- 9

**API Note:**
- Note that sequence number is an unsigned long and cannot
exceed

-1L

. It is desired to use the unsigned
long comparing mode for comparison of unsigned long values
(see also

Long.compareUnsigned()

).

For DTLS protocols, the first 16 bits of the sequence
number is a counter value (epoch) that is incremented on
every cipher state change. The remaining 48 bits on the
right side of the sequence number represents the sequence
of the record, which is maintained separately for each epoch.

**Implementation Note:**
- It is recommended that providers should never allow the
sequence number incremented to

-1L

. If the sequence
number is close to wrapping, renegotiate should be requested,
otherwise the connection should be closed immediately.
This should be carried on automatically by the underlying
implementation.

---

#### public
String
toString()

Returns a String representation of this object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class SSLEngineResult

java.lang.Object

- javax.net.ssl.SSLEngineResult

javax.net.ssl.SSLEngineResult

```java
public class
SSLEngineResult

extends
Object
```

An encapsulation of the result state produced by

SSLEngine

I/O calls.

A

SSLEngine

provides a means for establishing
secure communication sessions between two peers.

SSLEngine

operations typically consume bytes from an input buffer and produce
bytes in an output buffer. This class provides operational result
values describing the state of the

SSLEngine

, including
indications of what operations are needed to finish an
ongoing handshake. Lastly, it reports the number of bytes consumed
and produced as a result of this operation.

**Since:** 1.5
**See Also:** SSLEngine

,

SSLEngine.wrap(ByteBuffer, ByteBuffer)

,

SSLEngine.unwrap(ByteBuffer, ByteBuffer)

public class

SSLEngineResult

extends

Object

An encapsulation of the result state produced by

SSLEngine

I/O calls.

A

SSLEngine

provides a means for establishing
secure communication sessions between two peers.

SSLEngine

operations typically consume bytes from an input buffer and produce
bytes in an output buffer. This class provides operational result
values describing the state of the

SSLEngine

, including
indications of what operations are needed to finish an
ongoing handshake. Lastly, it reports the number of bytes consumed
and produced as a result of this operation.

A

SSLEngine

provides a means for establishing
secure communication sessions between two peers.

SSLEngine

operations typically consume bytes from an input buffer and produce
bytes in an output buffer. This class provides operational result
values describing the state of the

SSLEngine

, including
indications of what operations are needed to finish an
ongoing handshake. Lastly, it reports the number of bytes consumed
and produced as a result of this operation.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SSLEngineResult.HandshakeStatus

An

SSLEngineResult

enum describing the current
handshaking state of this

SSLEngine

.

static class

SSLEngineResult.Status

An

SSLEngineResult

enum describing the overall result
of the

SSLEngine

operation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SSLEngineResult

​(

SSLEngineResult.Status

status,

SSLEngineResult.HandshakeStatus

handshakeStatus,
int bytesConsumed,
int bytesProduced)

Initializes a new instance of this class.

SSLEngineResult

​(

SSLEngineResult.Status

status,

SSLEngineResult.HandshakeStatus

handshakeStatus,
int bytesConsumed,
int bytesProduced,
long sequenceNumber)

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

bytesConsumed

()

Returns the number of bytes consumed from the input buffer.

int

bytesProduced

()

Returns the number of bytes written to the output buffer.

SSLEngineResult.HandshakeStatus

getHandshakeStatus

()

Gets the handshake status of this

SSLEngine

operation.

SSLEngineResult.Status

getStatus

()

Gets the return value of this

SSLEngine

operation.

long

sequenceNumber

()

Returns the sequence number of the produced or consumed SSL/TLS/DTLS
record (optional operation).

String

toString

()

Returns a String representation of this object.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SSLEngineResult.HandshakeStatus

An

SSLEngineResult

enum describing the current
handshaking state of this

SSLEngine

.

static class

SSLEngineResult.Status

An

SSLEngineResult

enum describing the overall result
of the

SSLEngine

operation.

---

#### Nested Class Summary

An

SSLEngineResult

enum describing the current
handshaking state of this

SSLEngine

.

An

SSLEngineResult

enum describing the overall result
of the

SSLEngine

operation.

Constructor Summary

Constructors

Constructor

Description

SSLEngineResult

​(

SSLEngineResult.Status

status,

SSLEngineResult.HandshakeStatus

handshakeStatus,
int bytesConsumed,
int bytesProduced)

Initializes a new instance of this class.

SSLEngineResult

​(

SSLEngineResult.Status

status,

SSLEngineResult.HandshakeStatus

handshakeStatus,
int bytesConsumed,
int bytesProduced,
long sequenceNumber)

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

bytesConsumed

()

Returns the number of bytes consumed from the input buffer.

int

bytesProduced

()

Returns the number of bytes written to the output buffer.

SSLEngineResult.HandshakeStatus

getHandshakeStatus

()

Gets the handshake status of this

SSLEngine

operation.

SSLEngineResult.Status

getStatus

()

Gets the return value of this

SSLEngine

operation.

long

sequenceNumber

()

Returns the sequence number of the produced or consumed SSL/TLS/DTLS
record (optional operation).

String

toString

()

Returns a String representation of this object.

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

Returns the number of bytes consumed from the input buffer.

Returns the number of bytes written to the output buffer.

Gets the handshake status of this

SSLEngine

operation.

Gets the return value of this

SSLEngine

operation.

Returns the sequence number of the produced or consumed SSL/TLS/DTLS
record (optional operation).

Returns a String representation of this object.

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

- SSLEngineResult

```java
public SSLEngineResult​(
SSLEngineResult.Status
status,

SSLEngineResult.HandshakeStatus
handshakeStatus,
int bytesConsumed,
int bytesProduced)
```

Initializes a new instance of this class.

**Parameters:** status

- the return value of the operation.
**Parameters:** handshakeStatus

- the current handshaking status.
**Parameters:** bytesConsumed

- the number of bytes consumed from the source ByteBuffer
**Parameters:** bytesProduced

- the number of bytes placed into the destination ByteBuffer
**Throws:** IllegalArgumentException

- if the

status

or

handshakeStatus

arguments are null, or if

bytesConsumed

or

bytesProduced

is negative.

- SSLEngineResult

```java
public SSLEngineResult​(
SSLEngineResult.Status
status,

SSLEngineResult.HandshakeStatus
handshakeStatus,
int bytesConsumed,
int bytesProduced,
long sequenceNumber)
```

Initializes a new instance of this class.

**Parameters:** status

- the return value of the operation.
**Parameters:** handshakeStatus

- the current handshaking status.
**Parameters:** bytesConsumed

- the number of bytes consumed from the source ByteBuffer
**Parameters:** bytesProduced

- the number of bytes placed into the destination ByteBuffer
**Parameters:** sequenceNumber

- the sequence number (unsigned long) of the produced or
consumed SSL/TLS/DTLS record, or

-1L

if no record
produced or consumed
**Throws:** IllegalArgumentException

- if the

status

or

handshakeStatus

arguments are null, or if

bytesConsumed

or

bytesProduced

is negative
**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- getStatus

```java
public final
SSLEngineResult.Status
getStatus()
```

Gets the return value of this

SSLEngine

operation.

**Returns:** the return value

- getHandshakeStatus

```java
public final
SSLEngineResult.HandshakeStatus
getHandshakeStatus()
```

Gets the handshake status of this

SSLEngine

operation.

**Returns:** the handshake status

- bytesConsumed

```java
public final int bytesConsumed()
```

Returns the number of bytes consumed from the input buffer.

**Returns:** the number of bytes consumed.

- bytesProduced

```java
public final int bytesProduced()
```

Returns the number of bytes written to the output buffer.

**Returns:** the number of bytes produced

- sequenceNumber

```java
public final long sequenceNumber()
```

Returns the sequence number of the produced or consumed SSL/TLS/DTLS
record (optional operation).

**API Note:** Note that sequence number is an unsigned long and cannot
exceed

-1L

. It is desired to use the unsigned
long comparing mode for comparison of unsigned long values
(see also

Long.compareUnsigned()

).

For DTLS protocols, the first 16 bits of the sequence
number is a counter value (epoch) that is incremented on
every cipher state change. The remaining 48 bits on the
right side of the sequence number represents the sequence
of the record, which is maintained separately for each epoch.
**Implementation Note:** It is recommended that providers should never allow the
sequence number incremented to

-1L

. If the sequence
number is close to wrapping, renegotiate should be requested,
otherwise the connection should be closed immediately.
This should be carried on automatically by the underlying
implementation.
**Returns:** the sequence number of the produced or consumed SSL/TLS/DTLS
record; or

-1L

if no record is produced or consumed,
or this operation is not supported by the underlying provider
**Since:** 9
**See Also:** Long.compareUnsigned(long, long)

- toString

```java
public
String
toString()
```

Returns a String representation of this object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- SSLEngineResult

```java
public SSLEngineResult​(
SSLEngineResult.Status
status,

SSLEngineResult.HandshakeStatus
handshakeStatus,
int bytesConsumed,
int bytesProduced)
```

Initializes a new instance of this class.

**Parameters:** status

- the return value of the operation.
**Parameters:** handshakeStatus

- the current handshaking status.
**Parameters:** bytesConsumed

- the number of bytes consumed from the source ByteBuffer
**Parameters:** bytesProduced

- the number of bytes placed into the destination ByteBuffer
**Throws:** IllegalArgumentException

- if the

status

or

handshakeStatus

arguments are null, or if

bytesConsumed

or

bytesProduced

is negative.

- SSLEngineResult

```java
public SSLEngineResult​(
SSLEngineResult.Status
status,

SSLEngineResult.HandshakeStatus
handshakeStatus,
int bytesConsumed,
int bytesProduced,
long sequenceNumber)
```

Initializes a new instance of this class.

**Parameters:** status

- the return value of the operation.
**Parameters:** handshakeStatus

- the current handshaking status.
**Parameters:** bytesConsumed

- the number of bytes consumed from the source ByteBuffer
**Parameters:** bytesProduced

- the number of bytes placed into the destination ByteBuffer
**Parameters:** sequenceNumber

- the sequence number (unsigned long) of the produced or
consumed SSL/TLS/DTLS record, or

-1L

if no record
produced or consumed
**Throws:** IllegalArgumentException

- if the

status

or

handshakeStatus

arguments are null, or if

bytesConsumed

or

bytesProduced

is negative
**Since:** 9

---

#### Constructor Detail

SSLEngineResult

```java
public SSLEngineResult​(
SSLEngineResult.Status
status,

SSLEngineResult.HandshakeStatus
handshakeStatus,
int bytesConsumed,
int bytesProduced)
```

Initializes a new instance of this class.

**Parameters:** status

- the return value of the operation.
**Parameters:** handshakeStatus

- the current handshaking status.
**Parameters:** bytesConsumed

- the number of bytes consumed from the source ByteBuffer
**Parameters:** bytesProduced

- the number of bytes placed into the destination ByteBuffer
**Throws:** IllegalArgumentException

- if the

status

or

handshakeStatus

arguments are null, or if

bytesConsumed

or

bytesProduced

is negative.

---

#### SSLEngineResult

public SSLEngineResult​(

SSLEngineResult.Status

status,

SSLEngineResult.HandshakeStatus

handshakeStatus,
int bytesConsumed,
int bytesProduced)

Initializes a new instance of this class.

SSLEngineResult

```java
public SSLEngineResult​(
SSLEngineResult.Status
status,

SSLEngineResult.HandshakeStatus
handshakeStatus,
int bytesConsumed,
int bytesProduced,
long sequenceNumber)
```

Initializes a new instance of this class.

**Parameters:** status

- the return value of the operation.
**Parameters:** handshakeStatus

- the current handshaking status.
**Parameters:** bytesConsumed

- the number of bytes consumed from the source ByteBuffer
**Parameters:** bytesProduced

- the number of bytes placed into the destination ByteBuffer
**Parameters:** sequenceNumber

- the sequence number (unsigned long) of the produced or
consumed SSL/TLS/DTLS record, or

-1L

if no record
produced or consumed
**Throws:** IllegalArgumentException

- if the

status

or

handshakeStatus

arguments are null, or if

bytesConsumed

or

bytesProduced

is negative
**Since:** 9

---

#### SSLEngineResult

public SSLEngineResult​(

SSLEngineResult.Status

status,

SSLEngineResult.HandshakeStatus

handshakeStatus,
int bytesConsumed,
int bytesProduced,
long sequenceNumber)

Initializes a new instance of this class.

Method Detail

- getStatus

```java
public final
SSLEngineResult.Status
getStatus()
```

Gets the return value of this

SSLEngine

operation.

**Returns:** the return value

- getHandshakeStatus

```java
public final
SSLEngineResult.HandshakeStatus
getHandshakeStatus()
```

Gets the handshake status of this

SSLEngine

operation.

**Returns:** the handshake status

- bytesConsumed

```java
public final int bytesConsumed()
```

Returns the number of bytes consumed from the input buffer.

**Returns:** the number of bytes consumed.

- bytesProduced

```java
public final int bytesProduced()
```

Returns the number of bytes written to the output buffer.

**Returns:** the number of bytes produced

- sequenceNumber

```java
public final long sequenceNumber()
```

Returns the sequence number of the produced or consumed SSL/TLS/DTLS
record (optional operation).

**API Note:** Note that sequence number is an unsigned long and cannot
exceed

-1L

. It is desired to use the unsigned
long comparing mode for comparison of unsigned long values
(see also

Long.compareUnsigned()

).

For DTLS protocols, the first 16 bits of the sequence
number is a counter value (epoch) that is incremented on
every cipher state change. The remaining 48 bits on the
right side of the sequence number represents the sequence
of the record, which is maintained separately for each epoch.
**Implementation Note:** It is recommended that providers should never allow the
sequence number incremented to

-1L

. If the sequence
number is close to wrapping, renegotiate should be requested,
otherwise the connection should be closed immediately.
This should be carried on automatically by the underlying
implementation.
**Returns:** the sequence number of the produced or consumed SSL/TLS/DTLS
record; or

-1L

if no record is produced or consumed,
or this operation is not supported by the underlying provider
**Since:** 9
**See Also:** Long.compareUnsigned(long, long)

- toString

```java
public
String
toString()
```

Returns a String representation of this object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getStatus

```java
public final
SSLEngineResult.Status
getStatus()
```

Gets the return value of this

SSLEngine

operation.

**Returns:** the return value

---

#### getStatus

public final

SSLEngineResult.Status

getStatus()

Gets the return value of this

SSLEngine

operation.

getHandshakeStatus

```java
public final
SSLEngineResult.HandshakeStatus
getHandshakeStatus()
```

Gets the handshake status of this

SSLEngine

operation.

**Returns:** the handshake status

---

#### getHandshakeStatus

public final

SSLEngineResult.HandshakeStatus

getHandshakeStatus()

Gets the handshake status of this

SSLEngine

operation.

bytesConsumed

```java
public final int bytesConsumed()
```

Returns the number of bytes consumed from the input buffer.

**Returns:** the number of bytes consumed.

---

#### bytesConsumed

public final int bytesConsumed()

Returns the number of bytes consumed from the input buffer.

bytesProduced

```java
public final int bytesProduced()
```

Returns the number of bytes written to the output buffer.

**Returns:** the number of bytes produced

---

#### bytesProduced

public final int bytesProduced()

Returns the number of bytes written to the output buffer.

sequenceNumber

```java
public final long sequenceNumber()
```

Returns the sequence number of the produced or consumed SSL/TLS/DTLS
record (optional operation).

**API Note:** Note that sequence number is an unsigned long and cannot
exceed

-1L

. It is desired to use the unsigned
long comparing mode for comparison of unsigned long values
(see also

Long.compareUnsigned()

).

For DTLS protocols, the first 16 bits of the sequence
number is a counter value (epoch) that is incremented on
every cipher state change. The remaining 48 bits on the
right side of the sequence number represents the sequence
of the record, which is maintained separately for each epoch.
**Implementation Note:** It is recommended that providers should never allow the
sequence number incremented to

-1L

. If the sequence
number is close to wrapping, renegotiate should be requested,
otherwise the connection should be closed immediately.
This should be carried on automatically by the underlying
implementation.
**Returns:** the sequence number of the produced or consumed SSL/TLS/DTLS
record; or

-1L

if no record is produced or consumed,
or this operation is not supported by the underlying provider
**Since:** 9
**See Also:** Long.compareUnsigned(long, long)

---

#### sequenceNumber

public final long sequenceNumber()

Returns the sequence number of the produced or consumed SSL/TLS/DTLS
record (optional operation).

For DTLS protocols, the first 16 bits of the sequence
number is a counter value (epoch) that is incremented on
every cipher state change. The remaining 48 bits on the
right side of the sequence number represents the sequence
of the record, which is maintained separately for each epoch.

toString

```java
public
String
toString()
```

Returns a String representation of this object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a String representation of this object.

---

