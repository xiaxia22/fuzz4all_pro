# Class SNIServerName

**Source:** `java.base\javax\net\ssl\SNIServerName.html`

### Class Description

```java
public abstract class
SNIServerName

extends
Object
```

Instances of this class represent a server name in a Server Name
Indication (SNI) extension.

The SNI extension is a feature that extends the SSL/TLS/DTLS protocols to
indicate what server name the client is attempting to connect to during
handshaking. See section 3, "Server Name Indication", of

TLS Extensions (RFC 6066)

.

SNIServerName

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

**Direct Known Subclasses:** SNIHostName

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SNIServerName​(int type,
byte[] encoded)

Creates an

SNIServerName

using the specified name type and
encoded value.

Note that the

encoded

byte array is cloned to protect against
subsequent modification.

**Parameters:**
- type

- the type of the server name
- encoded

- the encoded value of the server name

**Throws:**
- IllegalArgumentException

- if

type

is not in the range
of 0 to 255, inclusive.
- NullPointerException

- if

encoded

is null

---

### Method Details

#### public final int getType()

Returns the name type of this server name.

**Returns:**
- the name type of this server name

---

#### public final byte[] getEncoded()

Returns a copy of the encoded server name value of this server name.

**Returns:**
- a copy of the encoded server name value of this server name

---

#### public boolean equals​(
Object
other)

Indicates whether some other object is "equal to" this server name.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the reference object with which to compare.

**Returns:**
- true if, and only if,

other

is of the same class
of this object, and has the same name type and
encoded value as this server name.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this server name.

The hash code value is generated using the name type and encoded
value of this server name.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this server name.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this server name, including the server
name type and the encoded server name value in this

SNIServerName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=<name type>, value=<name value>"
```

In this class, the format of "<name type>" is
"[LITERAL] (INTEGER)", where the optional "LITERAL" is the literal
name, and INTEGER is the integer value of the name type. The format
of "<name value>" is "XX:...:XX", where "XX" is the
hexadecimal digit representation of a byte value. For example, a
returned value of an pseudo server name may look like:

```java
"type=(31), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

or

```java
"type=host_name (0), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change, and subclasses may override the method with
their own formats.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this server name

---

### Additional Sections

#### Class SNIServerName

java.lang.Object

- javax.net.ssl.SNIServerName

javax.net.ssl.SNIServerName

**Direct Known Subclasses:** SNIHostName

```java
public abstract class
SNIServerName

extends
Object
```

Instances of this class represent a server name in a Server Name
Indication (SNI) extension.

The SNI extension is a feature that extends the SSL/TLS/DTLS protocols to
indicate what server name the client is attempting to connect to during
handshaking. See section 3, "Server Name Indication", of

TLS Extensions (RFC 6066)

.

SNIServerName

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

**Since:** 1.8
**See Also:** SSLParameters.getServerNames()

,

SSLParameters.setServerNames(List)

public abstract class

SNIServerName

extends

Object

Instances of this class represent a server name in a Server Name
Indication (SNI) extension.

The SNI extension is a feature that extends the SSL/TLS/DTLS protocols to
indicate what server name the client is attempting to connect to during
handshaking. See section 3, "Server Name Indication", of

TLS Extensions (RFC 6066)

.

SNIServerName

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

The SNI extension is a feature that extends the SSL/TLS/DTLS protocols to
indicate what server name the client is attempting to connect to during
handshaking. See section 3, "Server Name Indication", of

TLS Extensions (RFC 6066)

.

SNIServerName

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

SNIServerName

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SNIServerName

​(int type,
byte[] encoded)

Creates an

SNIServerName

using the specified name type and
encoded value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Indicates whether some other object is "equal to" this server name.

byte[]

getEncoded

()

Returns a copy of the encoded server name value of this server name.

int

getType

()

Returns the name type of this server name.

int

hashCode

()

Returns a hash code value for this server name.

String

toString

()

Returns a string representation of this server name, including the server
name type and the encoded server name value in this

SNIServerName

object.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SNIServerName

​(int type,
byte[] encoded)

Creates an

SNIServerName

using the specified name type and
encoded value.

---

#### Constructor Summary

Creates an

SNIServerName

using the specified name type and
encoded value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Indicates whether some other object is "equal to" this server name.

byte[]

getEncoded

()

Returns a copy of the encoded server name value of this server name.

int

getType

()

Returns the name type of this server name.

int

hashCode

()

Returns a hash code value for this server name.

String

toString

()

Returns a string representation of this server name, including the server
name type and the encoded server name value in this

SNIServerName

object.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Indicates whether some other object is "equal to" this server name.

Returns a copy of the encoded server name value of this server name.

Returns the name type of this server name.

Returns a hash code value for this server name.

Returns a string representation of this server name, including the server
name type and the encoded server name value in this

SNIServerName

object.

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SNIServerName

```java
protected SNIServerName​(int type,
byte[] encoded)
```

Creates an

SNIServerName

using the specified name type and
encoded value.

Note that the

encoded

byte array is cloned to protect against
subsequent modification.

**Parameters:** type

- the type of the server name
**Parameters:** encoded

- the encoded value of the server name
**Throws:** IllegalArgumentException

- if

type

is not in the range
of 0 to 255, inclusive.
**Throws:** NullPointerException

- if

encoded

is null

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public final int getType()
```

Returns the name type of this server name.

**Returns:** the name type of this server name

- getEncoded

```java
public final byte[] getEncoded()
```

Returns a copy of the encoded server name value of this server name.

**Returns:** a copy of the encoded server name value of this server name

- equals

```java
public boolean equals​(
Object
other)
```

Indicates whether some other object is "equal to" this server name.

**Overrides:** equals

in class

Object
**Parameters:** other

- the reference object with which to compare.
**Returns:** true if, and only if,

other

is of the same class
of this object, and has the same name type and
encoded value as this server name.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this server name.

The hash code value is generated using the name type and encoded
value of this server name.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this server name.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this server name, including the server
name type and the encoded server name value in this

SNIServerName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=<name type>, value=<name value>"
```

In this class, the format of "<name type>" is
"[LITERAL] (INTEGER)", where the optional "LITERAL" is the literal
name, and INTEGER is the integer value of the name type. The format
of "<name value>" is "XX:...:XX", where "XX" is the
hexadecimal digit representation of a byte value. For example, a
returned value of an pseudo server name may look like:

```java
"type=(31), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

or

```java
"type=host_name (0), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change, and subclasses may override the method with
their own formats.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this server name

Constructor Detail

- SNIServerName

```java
protected SNIServerName​(int type,
byte[] encoded)
```

Creates an

SNIServerName

using the specified name type and
encoded value.

Note that the

encoded

byte array is cloned to protect against
subsequent modification.

**Parameters:** type

- the type of the server name
**Parameters:** encoded

- the encoded value of the server name
**Throws:** IllegalArgumentException

- if

type

is not in the range
of 0 to 255, inclusive.
**Throws:** NullPointerException

- if

encoded

is null

---

#### Constructor Detail

SNIServerName

```java
protected SNIServerName​(int type,
byte[] encoded)
```

Creates an

SNIServerName

using the specified name type and
encoded value.

Note that the

encoded

byte array is cloned to protect against
subsequent modification.

**Parameters:** type

- the type of the server name
**Parameters:** encoded

- the encoded value of the server name
**Throws:** IllegalArgumentException

- if

type

is not in the range
of 0 to 255, inclusive.
**Throws:** NullPointerException

- if

encoded

is null

---

#### SNIServerName

protected SNIServerName​(int type,
byte[] encoded)

Creates an

SNIServerName

using the specified name type and
encoded value.

Note that the

encoded

byte array is cloned to protect against
subsequent modification.

Note that the

encoded

byte array is cloned to protect against
subsequent modification.

Method Detail

- getType

```java
public final int getType()
```

Returns the name type of this server name.

**Returns:** the name type of this server name

- getEncoded

```java
public final byte[] getEncoded()
```

Returns a copy of the encoded server name value of this server name.

**Returns:** a copy of the encoded server name value of this server name

- equals

```java
public boolean equals​(
Object
other)
```

Indicates whether some other object is "equal to" this server name.

**Overrides:** equals

in class

Object
**Parameters:** other

- the reference object with which to compare.
**Returns:** true if, and only if,

other

is of the same class
of this object, and has the same name type and
encoded value as this server name.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this server name.

The hash code value is generated using the name type and encoded
value of this server name.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this server name.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this server name, including the server
name type and the encoded server name value in this

SNIServerName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=<name type>, value=<name value>"
```

In this class, the format of "<name type>" is
"[LITERAL] (INTEGER)", where the optional "LITERAL" is the literal
name, and INTEGER is the integer value of the name type. The format
of "<name value>" is "XX:...:XX", where "XX" is the
hexadecimal digit representation of a byte value. For example, a
returned value of an pseudo server name may look like:

```java
"type=(31), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

or

```java
"type=host_name (0), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change, and subclasses may override the method with
their own formats.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this server name

---

#### Method Detail

getType

```java
public final int getType()
```

Returns the name type of this server name.

**Returns:** the name type of this server name

---

#### getType

public final int getType()

Returns the name type of this server name.

getEncoded

```java
public final byte[] getEncoded()
```

Returns a copy of the encoded server name value of this server name.

**Returns:** a copy of the encoded server name value of this server name

---

#### getEncoded

public final byte[] getEncoded()

Returns a copy of the encoded server name value of this server name.

equals

```java
public boolean equals​(
Object
other)
```

Indicates whether some other object is "equal to" this server name.

**Overrides:** equals

in class

Object
**Parameters:** other

- the reference object with which to compare.
**Returns:** true if, and only if,

other

is of the same class
of this object, and has the same name type and
encoded value as this server name.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Indicates whether some other object is "equal to" this server name.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this server name.

The hash code value is generated using the name type and encoded
value of this server name.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this server name.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this server name.

The hash code value is generated using the name type and encoded
value of this server name.

The hash code value is generated using the name type and encoded
value of this server name.

toString

```java
public
String
toString()
```

Returns a string representation of this server name, including the server
name type and the encoded server name value in this

SNIServerName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=<name type>, value=<name value>"
```

In this class, the format of "<name type>" is
"[LITERAL] (INTEGER)", where the optional "LITERAL" is the literal
name, and INTEGER is the integer value of the name type. The format
of "<name value>" is "XX:...:XX", where "XX" is the
hexadecimal digit representation of a byte value. For example, a
returned value of an pseudo server name may look like:

```java
"type=(31), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

or

```java
"type=host_name (0), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change, and subclasses may override the method with
their own formats.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this server name

---

#### toString

public

String

toString()

Returns a string representation of this server name, including the server
name type and the encoded server name value in this

SNIServerName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=<name type>, value=<name value>"
```

In this class, the format of "<name type>" is
"[LITERAL] (INTEGER)", where the optional "LITERAL" is the literal
name, and INTEGER is the integer value of the name type. The format
of "<name value>" is "XX:...:XX", where "XX" is the
hexadecimal digit representation of a byte value. For example, a
returned value of an pseudo server name may look like:

```java
"type=(31), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

or

```java
"type=host_name (0), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change, and subclasses may override the method with
their own formats.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=<name type>, value=<name value>"
```

In this class, the format of "<name type>" is
"[LITERAL] (INTEGER)", where the optional "LITERAL" is the literal
name, and INTEGER is the integer value of the name type. The format
of "<name value>" is "XX:...:XX", where "XX" is the
hexadecimal digit representation of a byte value. For example, a
returned value of an pseudo server name may look like:

```java
"type=(31), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

or

```java
"type=host_name (0), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change, and subclasses may override the method with
their own formats.

"type=<name type>, value=<name value>"

In this class, the format of "<name type>" is
"[LITERAL] (INTEGER)", where the optional "LITERAL" is the literal
name, and INTEGER is the integer value of the name type. The format
of "<name value>" is "XX:...:XX", where "XX" is the
hexadecimal digit representation of a byte value. For example, a
returned value of an pseudo server name may look like:

```java
"type=(31), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

or

```java
"type=host_name (0), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change, and subclasses may override the method with
their own formats.

"type=(31), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"

"type=host_name (0), value=77:77:77:2E:65:78:61:6D:70:6C:65:2E:63:6E"

Please NOTE that the exact details of the representation are unspecified
and subject to change, and subclasses may override the method with
their own formats.

---

