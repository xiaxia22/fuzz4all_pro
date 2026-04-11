# Enum SSLEngineResult.HandshakeStatus

**Source:** `java.base\javax\net\ssl\SSLEngineResult.HandshakeStatus.html`

### Class Description

```java
public static enum
SSLEngineResult.HandshakeStatus

extends
Enum
<
SSLEngineResult.HandshakeStatus
>
```

An

SSLEngineResult

enum describing the current
handshaking state of this

SSLEngine

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

SSLEngineResult.HandshakeStatus

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
SSLEngineResult.HandshakeStatus
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.HandshakeStatus c : SSLEngineResult.HandshakeStatus.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
SSLEngineResult.HandshakeStatus
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

#### Enum SSLEngineResult.HandshakeStatus

java.lang.Object

- java.lang.Enum

<

SSLEngineResult.HandshakeStatus

>
- - javax.net.ssl.SSLEngineResult.HandshakeStatus

java.lang.Enum

<

SSLEngineResult.HandshakeStatus

>

- javax.net.ssl.SSLEngineResult.HandshakeStatus

javax.net.ssl.SSLEngineResult.HandshakeStatus

**All Implemented Interfaces:** Serializable

,

Comparable

<

SSLEngineResult.HandshakeStatus

>

**Enclosing class:** SSLEngineResult

```java
public static enum
SSLEngineResult.HandshakeStatus

extends
Enum
<
SSLEngineResult.HandshakeStatus
>
```

An

SSLEngineResult

enum describing the current
handshaking state of this

SSLEngine

.

**Since:** 1.5

public static enum

SSLEngineResult.HandshakeStatus

extends

Enum

<

SSLEngineResult.HandshakeStatus

>

An

SSLEngineResult

enum describing the current
handshaking state of this

SSLEngine

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

FINISHED

The

SSLEngine

has just finished handshaking.

NEED_TASK

The

SSLEngine

needs the results of one (or more)
delegated tasks before handshaking can continue.

NEED_UNWRAP

The

SSLEngine

needs to receive data from the
remote side before handshaking can continue.

NEED_UNWRAP_AGAIN

The

SSLEngine

needs to unwrap before handshaking can
continue.

NEED_WRAP

The

SSLEngine

must send data to the remote side
before handshaking can continue, so

SSLEngine.wrap()

should be called.

NOT_HANDSHAKING

The

SSLEngine

is not currently handshaking.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SSLEngineResult.HandshakeStatus

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SSLEngineResult.HandshakeStatus

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

FINISHED

The

SSLEngine

has just finished handshaking.

NEED_TASK

The

SSLEngine

needs the results of one (or more)
delegated tasks before handshaking can continue.

NEED_UNWRAP

The

SSLEngine

needs to receive data from the
remote side before handshaking can continue.

NEED_UNWRAP_AGAIN

The

SSLEngine

needs to unwrap before handshaking can
continue.

NEED_WRAP

The

SSLEngine

must send data to the remote side
before handshaking can continue, so

SSLEngine.wrap()

should be called.

NOT_HANDSHAKING

The

SSLEngine

is not currently handshaking.

---

#### Enum Constant Summary

The

SSLEngine

has just finished handshaking.

The

SSLEngine

needs the results of one (or more)
delegated tasks before handshaking can continue.

The

SSLEngine

needs to receive data from the
remote side before handshaking can continue.

The

SSLEngine

needs to unwrap before handshaking can
continue.

The

SSLEngine

must send data to the remote side
before handshaking can continue, so

SSLEngine.wrap()

should be called.

The

SSLEngine

is not currently handshaking.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SSLEngineResult.HandshakeStatus

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SSLEngineResult.HandshakeStatus

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

- NOT_HANDSHAKING

```java
public static final
SSLEngineResult.HandshakeStatus
NOT_HANDSHAKING
```

The

SSLEngine

is not currently handshaking.

- FINISHED

```java
public static final
SSLEngineResult.HandshakeStatus
FINISHED
```

The

SSLEngine

has just finished handshaking.

This value is only generated by a call to

SSLEngine.wrap()/unwrap()

when that call
finishes a handshake. It is never generated by

SSLEngine.getHandshakeStatus()

.

**See Also:** SSLEngine.wrap(ByteBuffer, ByteBuffer)

,

SSLEngine.unwrap(ByteBuffer, ByteBuffer)

,

SSLEngine.getHandshakeStatus()

- NEED_TASK

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_TASK
```

The

SSLEngine

needs the results of one (or more)
delegated tasks before handshaking can continue.

**See Also:** SSLEngine.getDelegatedTask()

- NEED_WRAP

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_WRAP
```

The

SSLEngine

must send data to the remote side
before handshaking can continue, so

SSLEngine.wrap()

should be called.

**See Also:** SSLEngine.wrap(ByteBuffer, ByteBuffer)

- NEED_UNWRAP

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_UNWRAP
```

The

SSLEngine

needs to receive data from the
remote side before handshaking can continue.

- NEED_UNWRAP_AGAIN

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_UNWRAP_AGAIN
```

The

SSLEngine

needs to unwrap before handshaking can
continue.

This value is used to indicate that not-yet-interpreted data
has been previously received from the remote side, and does
not need to be received again.

This handshake status only applies to DTLS.

**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
SSLEngineResult.HandshakeStatus
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.HandshakeStatus c : SSLEngineResult.HandshakeStatus.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SSLEngineResult.HandshakeStatus
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

- NOT_HANDSHAKING

```java
public static final
SSLEngineResult.HandshakeStatus
NOT_HANDSHAKING
```

The

SSLEngine

is not currently handshaking.

- FINISHED

```java
public static final
SSLEngineResult.HandshakeStatus
FINISHED
```

The

SSLEngine

has just finished handshaking.

This value is only generated by a call to

SSLEngine.wrap()/unwrap()

when that call
finishes a handshake. It is never generated by

SSLEngine.getHandshakeStatus()

.

**See Also:** SSLEngine.wrap(ByteBuffer, ByteBuffer)

,

SSLEngine.unwrap(ByteBuffer, ByteBuffer)

,

SSLEngine.getHandshakeStatus()

- NEED_TASK

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_TASK
```

The

SSLEngine

needs the results of one (or more)
delegated tasks before handshaking can continue.

**See Also:** SSLEngine.getDelegatedTask()

- NEED_WRAP

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_WRAP
```

The

SSLEngine

must send data to the remote side
before handshaking can continue, so

SSLEngine.wrap()

should be called.

**See Also:** SSLEngine.wrap(ByteBuffer, ByteBuffer)

- NEED_UNWRAP

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_UNWRAP
```

The

SSLEngine

needs to receive data from the
remote side before handshaking can continue.

- NEED_UNWRAP_AGAIN

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_UNWRAP_AGAIN
```

The

SSLEngine

needs to unwrap before handshaking can
continue.

This value is used to indicate that not-yet-interpreted data
has been previously received from the remote side, and does
not need to be received again.

This handshake status only applies to DTLS.

**Since:** 9

---

#### Enum Constant Detail

NOT_HANDSHAKING

```java
public static final
SSLEngineResult.HandshakeStatus
NOT_HANDSHAKING
```

The

SSLEngine

is not currently handshaking.

---

#### NOT_HANDSHAKING

public static final

SSLEngineResult.HandshakeStatus

NOT_HANDSHAKING

The

SSLEngine

is not currently handshaking.

FINISHED

```java
public static final
SSLEngineResult.HandshakeStatus
FINISHED
```

The

SSLEngine

has just finished handshaking.

This value is only generated by a call to

SSLEngine.wrap()/unwrap()

when that call
finishes a handshake. It is never generated by

SSLEngine.getHandshakeStatus()

.

**See Also:** SSLEngine.wrap(ByteBuffer, ByteBuffer)

,

SSLEngine.unwrap(ByteBuffer, ByteBuffer)

,

SSLEngine.getHandshakeStatus()

---

#### FINISHED

public static final

SSLEngineResult.HandshakeStatus

FINISHED

The

SSLEngine

has just finished handshaking.

This value is only generated by a call to

SSLEngine.wrap()/unwrap()

when that call
finishes a handshake. It is never generated by

SSLEngine.getHandshakeStatus()

.

This value is only generated by a call to

SSLEngine.wrap()/unwrap()

when that call
finishes a handshake. It is never generated by

SSLEngine.getHandshakeStatus()

.

NEED_TASK

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_TASK
```

The

SSLEngine

needs the results of one (or more)
delegated tasks before handshaking can continue.

**See Also:** SSLEngine.getDelegatedTask()

---

#### NEED_TASK

public static final

SSLEngineResult.HandshakeStatus

NEED_TASK

The

SSLEngine

needs the results of one (or more)
delegated tasks before handshaking can continue.

NEED_WRAP

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_WRAP
```

The

SSLEngine

must send data to the remote side
before handshaking can continue, so

SSLEngine.wrap()

should be called.

**See Also:** SSLEngine.wrap(ByteBuffer, ByteBuffer)

---

#### NEED_WRAP

public static final

SSLEngineResult.HandshakeStatus

NEED_WRAP

The

SSLEngine

must send data to the remote side
before handshaking can continue, so

SSLEngine.wrap()

should be called.

NEED_UNWRAP

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_UNWRAP
```

The

SSLEngine

needs to receive data from the
remote side before handshaking can continue.

---

#### NEED_UNWRAP

public static final

SSLEngineResult.HandshakeStatus

NEED_UNWRAP

The

SSLEngine

needs to receive data from the
remote side before handshaking can continue.

NEED_UNWRAP_AGAIN

```java
public static final
SSLEngineResult.HandshakeStatus
NEED_UNWRAP_AGAIN
```

The

SSLEngine

needs to unwrap before handshaking can
continue.

This value is used to indicate that not-yet-interpreted data
has been previously received from the remote side, and does
not need to be received again.

This handshake status only applies to DTLS.

**Since:** 9

---

#### NEED_UNWRAP_AGAIN

public static final

SSLEngineResult.HandshakeStatus

NEED_UNWRAP_AGAIN

The

SSLEngine

needs to unwrap before handshaking can
continue.

This value is used to indicate that not-yet-interpreted data
has been previously received from the remote side, and does
not need to be received again.

This handshake status only applies to DTLS.

This value is used to indicate that not-yet-interpreted data
has been previously received from the remote side, and does
not need to be received again.

This handshake status only applies to DTLS.

This handshake status only applies to DTLS.

Method Detail

- values

```java
public static
SSLEngineResult.HandshakeStatus
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.HandshakeStatus c : SSLEngineResult.HandshakeStatus.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SSLEngineResult.HandshakeStatus
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
SSLEngineResult.HandshakeStatus
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.HandshakeStatus c : SSLEngineResult.HandshakeStatus.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

SSLEngineResult.HandshakeStatus

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SSLEngineResult.HandshakeStatus c : SSLEngineResult.HandshakeStatus.values())
System.out.println(c);
```

for (SSLEngineResult.HandshakeStatus c : SSLEngineResult.HandshakeStatus.values())
System.out.println(c);

valueOf

```java
public static
SSLEngineResult.HandshakeStatus
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

SSLEngineResult.HandshakeStatus

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

