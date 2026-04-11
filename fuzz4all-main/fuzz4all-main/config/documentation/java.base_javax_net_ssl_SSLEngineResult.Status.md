# Enum SSLEngineResult.Status

**Source:** `java.base\javax\net\ssl\SSLEngineResult.Status.html`

### Class Description

```java
public static enum
SSLEngineResult.Status

extends
Enum
<
SSLEngineResult.Status
>
```

An

SSLEngineResult

enum describing the overall result
of the

SSLEngine

operation.

The

Status

value does not reflect the
state of a

SSLEngine

handshake currently
in progress. The

SSLEngineResult's HandshakeStatus

should be consulted for that information.

**All Implemented Interfaces:** Serializable

,

Comparable

<

SSLEngineResult.Status

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
SSLEngineResult.Status
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.Status c : SSLEngineResult.Status.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
SSLEngineResult.Status
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum SSLEngineResult.Status

java.lang.Object

- java.lang.Enum

<

SSLEngineResult.Status

>
- - javax.net.ssl.SSLEngineResult.Status

java.lang.Enum

<

SSLEngineResult.Status

>

- javax.net.ssl.SSLEngineResult.Status

javax.net.ssl.SSLEngineResult.Status

**All Implemented Interfaces:** Serializable

,

Comparable

<

SSLEngineResult.Status

>

**Enclosing class:** SSLEngineResult

```java
public static enum
SSLEngineResult.Status

extends
Enum
<
SSLEngineResult.Status
>
```

An

SSLEngineResult

enum describing the overall result
of the

SSLEngine

operation.

The

Status

value does not reflect the
state of a

SSLEngine

handshake currently
in progress. The

SSLEngineResult's HandshakeStatus

should be consulted for that information.

**Since:** 1.5

public static enum

SSLEngineResult.Status

extends

Enum

<

SSLEngineResult.Status

>

An

SSLEngineResult

enum describing the overall result
of the

SSLEngine

operation.

The

Status

value does not reflect the
state of a

SSLEngine

handshake currently
in progress. The

SSLEngineResult's HandshakeStatus

should be consulted for that information.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

BUFFER_OVERFLOW

The

SSLEngine

was not able to process the
operation because there are not enough bytes available in the
destination buffer to hold the result.

BUFFER_UNDERFLOW

The

SSLEngine

was not able to unwrap the
incoming data because there were not enough source bytes
available to make a complete packet.

CLOSED

The operation just closed this side of the

SSLEngine

, or the operation
could not be completed because it was already closed.

OK

The

SSLEngine

completed the operation, and
is available to process similar calls.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SSLEngineResult.Status

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SSLEngineResult.Status

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

BUFFER_OVERFLOW

The

SSLEngine

was not able to process the
operation because there are not enough bytes available in the
destination buffer to hold the result.

BUFFER_UNDERFLOW

The

SSLEngine

was not able to unwrap the
incoming data because there were not enough source bytes
available to make a complete packet.

CLOSED

The operation just closed this side of the

SSLEngine

, or the operation
could not be completed because it was already closed.

OK

The

SSLEngine

completed the operation, and
is available to process similar calls.

---

#### Enum Constant Summary

The

SSLEngine

was not able to process the
operation because there are not enough bytes available in the
destination buffer to hold the result.

The

SSLEngine

was not able to unwrap the
incoming data because there were not enough source bytes
available to make a complete packet.

The operation just closed this side of the

SSLEngine

, or the operation
could not be completed because it was already closed.

The

SSLEngine

completed the operation, and
is available to process similar calls.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SSLEngineResult.Status

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SSLEngineResult.Status

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- BUFFER_UNDERFLOW

```java
public static final
SSLEngineResult.Status
BUFFER_UNDERFLOW
```

The

SSLEngine

was not able to unwrap the
incoming data because there were not enough source bytes
available to make a complete packet.

Repeat the call once more bytes are available.

- BUFFER_OVERFLOW

```java
public static final
SSLEngineResult.Status
BUFFER_OVERFLOW
```

The

SSLEngine

was not able to process the
operation because there are not enough bytes available in the
destination buffer to hold the result.

Repeat the call once more bytes are available.

**See Also:** SSLSession.getPacketBufferSize()

,

SSLSession.getApplicationBufferSize()

- OK

```java
public static final
SSLEngineResult.Status
OK
```

The

SSLEngine

completed the operation, and
is available to process similar calls.

- CLOSED

```java
public static final
SSLEngineResult.Status
CLOSED
```

The operation just closed this side of the

SSLEngine

, or the operation
could not be completed because it was already closed.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
SSLEngineResult.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.Status c : SSLEngineResult.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SSLEngineResult.Status
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- BUFFER_UNDERFLOW

```java
public static final
SSLEngineResult.Status
BUFFER_UNDERFLOW
```

The

SSLEngine

was not able to unwrap the
incoming data because there were not enough source bytes
available to make a complete packet.

Repeat the call once more bytes are available.

- BUFFER_OVERFLOW

```java
public static final
SSLEngineResult.Status
BUFFER_OVERFLOW
```

The

SSLEngine

was not able to process the
operation because there are not enough bytes available in the
destination buffer to hold the result.

Repeat the call once more bytes are available.

**See Also:** SSLSession.getPacketBufferSize()

,

SSLSession.getApplicationBufferSize()

- OK

```java
public static final
SSLEngineResult.Status
OK
```

The

SSLEngine

completed the operation, and
is available to process similar calls.

- CLOSED

```java
public static final
SSLEngineResult.Status
CLOSED
```

The operation just closed this side of the

SSLEngine

, or the operation
could not be completed because it was already closed.

---

#### Enum Constant Detail

BUFFER_UNDERFLOW

```java
public static final
SSLEngineResult.Status
BUFFER_UNDERFLOW
```

The

SSLEngine

was not able to unwrap the
incoming data because there were not enough source bytes
available to make a complete packet.

Repeat the call once more bytes are available.

---

#### BUFFER_UNDERFLOW

public static final

SSLEngineResult.Status

BUFFER_UNDERFLOW

The

SSLEngine

was not able to unwrap the
incoming data because there were not enough source bytes
available to make a complete packet.

Repeat the call once more bytes are available.

Repeat the call once more bytes are available.

BUFFER_OVERFLOW

```java
public static final
SSLEngineResult.Status
BUFFER_OVERFLOW
```

The

SSLEngine

was not able to process the
operation because there are not enough bytes available in the
destination buffer to hold the result.

Repeat the call once more bytes are available.

**See Also:** SSLSession.getPacketBufferSize()

,

SSLSession.getApplicationBufferSize()

---

#### BUFFER_OVERFLOW

public static final

SSLEngineResult.Status

BUFFER_OVERFLOW

The

SSLEngine

was not able to process the
operation because there are not enough bytes available in the
destination buffer to hold the result.

Repeat the call once more bytes are available.

Repeat the call once more bytes are available.

OK

```java
public static final
SSLEngineResult.Status
OK
```

The

SSLEngine

completed the operation, and
is available to process similar calls.

---

#### OK

public static final

SSLEngineResult.Status

OK

The

SSLEngine

completed the operation, and
is available to process similar calls.

CLOSED

```java
public static final
SSLEngineResult.Status
CLOSED
```

The operation just closed this side of the

SSLEngine

, or the operation
could not be completed because it was already closed.

---

#### CLOSED

public static final

SSLEngineResult.Status

CLOSED

The operation just closed this side of the

SSLEngine

, or the operation
could not be completed because it was already closed.

Method Detail

- values

```java
public static
SSLEngineResult.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.Status c : SSLEngineResult.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SSLEngineResult.Status
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
SSLEngineResult.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.Status c : SSLEngineResult.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

SSLEngineResult.Status

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.Status c : SSLEngineResult.Status.values())
System.out.println(c);
```

for (SSLEngineResult.Status c : SSLEngineResult.Status.values())
System.out.println(c);

valueOf

```java
public static
SSLEngineResult.Status
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

SSLEngineResult.Status

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

