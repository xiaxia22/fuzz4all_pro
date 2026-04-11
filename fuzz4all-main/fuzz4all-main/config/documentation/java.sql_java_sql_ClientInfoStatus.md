# Enum ClientInfoStatus

**Source:** `java.sql\java\sql\ClientInfoStatus.html`

### Class Description

```java
public enum
ClientInfoStatus

extends
Enum
<
ClientInfoStatus
>
```

Enumeration for status of the reason that a property could not be set
via a call to

Connection.setClientInfo

**All Implemented Interfaces:** Serializable

,

Comparable

<

ClientInfoStatus

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ClientInfoStatus
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ClientInfoStatus c : ClientInfoStatus.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ClientInfoStatus
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

#### Enum ClientInfoStatus

java.lang.Object

- java.lang.Enum

<

ClientInfoStatus

>
- - java.sql.ClientInfoStatus

java.lang.Enum

<

ClientInfoStatus

>

- java.sql.ClientInfoStatus

java.sql.ClientInfoStatus

**All Implemented Interfaces:** Serializable

,

Comparable

<

ClientInfoStatus

>

```java
public enum
ClientInfoStatus

extends
Enum
<
ClientInfoStatus
>
```

Enumeration for status of the reason that a property could not be set
via a call to

Connection.setClientInfo

**Since:** 1.6

public enum

ClientInfoStatus

extends

Enum

<

ClientInfoStatus

>

Enumeration for status of the reason that a property could not be set
via a call to

Connection.setClientInfo

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

REASON_UNKNOWN

The client info property could not be set for some unknown reason

REASON_UNKNOWN_PROPERTY

The client info property name specified was not a recognized property
name.

REASON_VALUE_INVALID

The value specified for the client info property was not valid.

REASON_VALUE_TRUNCATED

The value specified for the client info property was too large.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ClientInfoStatus

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ClientInfoStatus

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

REASON_UNKNOWN

The client info property could not be set for some unknown reason

REASON_UNKNOWN_PROPERTY

The client info property name specified was not a recognized property
name.

REASON_VALUE_INVALID

The value specified for the client info property was not valid.

REASON_VALUE_TRUNCATED

The value specified for the client info property was too large.

---

#### Enum Constant Summary

The client info property could not be set for some unknown reason

The client info property name specified was not a recognized property
name.

The value specified for the client info property was not valid.

The value specified for the client info property was too large.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ClientInfoStatus

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ClientInfoStatus

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

- REASON_UNKNOWN

```java
public static final
ClientInfoStatus
REASON_UNKNOWN
```

The client info property could not be set for some unknown reason

**Since:** 1.6

- REASON_UNKNOWN_PROPERTY

```java
public static final
ClientInfoStatus
REASON_UNKNOWN_PROPERTY
```

The client info property name specified was not a recognized property
name.

**Since:** 1.6

- REASON_VALUE_INVALID

```java
public static final
ClientInfoStatus
REASON_VALUE_INVALID
```

The value specified for the client info property was not valid.

**Since:** 1.6

- REASON_VALUE_TRUNCATED

```java
public static final
ClientInfoStatus
REASON_VALUE_TRUNCATED
```

The value specified for the client info property was too large.

**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ClientInfoStatus
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ClientInfoStatus c : ClientInfoStatus.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ClientInfoStatus
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

- REASON_UNKNOWN

```java
public static final
ClientInfoStatus
REASON_UNKNOWN
```

The client info property could not be set for some unknown reason

**Since:** 1.6

- REASON_UNKNOWN_PROPERTY

```java
public static final
ClientInfoStatus
REASON_UNKNOWN_PROPERTY
```

The client info property name specified was not a recognized property
name.

**Since:** 1.6

- REASON_VALUE_INVALID

```java
public static final
ClientInfoStatus
REASON_VALUE_INVALID
```

The value specified for the client info property was not valid.

**Since:** 1.6

- REASON_VALUE_TRUNCATED

```java
public static final
ClientInfoStatus
REASON_VALUE_TRUNCATED
```

The value specified for the client info property was too large.

**Since:** 1.6

---

#### Enum Constant Detail

REASON_UNKNOWN

```java
public static final
ClientInfoStatus
REASON_UNKNOWN
```

The client info property could not be set for some unknown reason

**Since:** 1.6

---

#### REASON_UNKNOWN

public static final

ClientInfoStatus

REASON_UNKNOWN

The client info property could not be set for some unknown reason

REASON_UNKNOWN_PROPERTY

```java
public static final
ClientInfoStatus
REASON_UNKNOWN_PROPERTY
```

The client info property name specified was not a recognized property
name.

**Since:** 1.6

---

#### REASON_UNKNOWN_PROPERTY

public static final

ClientInfoStatus

REASON_UNKNOWN_PROPERTY

The client info property name specified was not a recognized property
name.

REASON_VALUE_INVALID

```java
public static final
ClientInfoStatus
REASON_VALUE_INVALID
```

The value specified for the client info property was not valid.

**Since:** 1.6

---

#### REASON_VALUE_INVALID

public static final

ClientInfoStatus

REASON_VALUE_INVALID

The value specified for the client info property was not valid.

REASON_VALUE_TRUNCATED

```java
public static final
ClientInfoStatus
REASON_VALUE_TRUNCATED
```

The value specified for the client info property was too large.

**Since:** 1.6

---

#### REASON_VALUE_TRUNCATED

public static final

ClientInfoStatus

REASON_VALUE_TRUNCATED

The value specified for the client info property was too large.

Method Detail

- values

```java
public static
ClientInfoStatus
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ClientInfoStatus c : ClientInfoStatus.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ClientInfoStatus
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
ClientInfoStatus
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ClientInfoStatus c : ClientInfoStatus.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ClientInfoStatus

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ClientInfoStatus c : ClientInfoStatus.values())
System.out.println(c);
```

for (ClientInfoStatus c : ClientInfoStatus.values())
System.out.println(c);

valueOf

```java
public static
ClientInfoStatus
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

ClientInfoStatus

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

