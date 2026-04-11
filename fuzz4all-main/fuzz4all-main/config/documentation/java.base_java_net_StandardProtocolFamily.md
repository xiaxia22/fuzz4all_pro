# Enum StandardProtocolFamily

**Source:** `java.base\java\net\StandardProtocolFamily.html`

### Class Description

```java
public enum
StandardProtocolFamily

extends
Enum
<
StandardProtocolFamily
>
implements
ProtocolFamily
```

Defines the standard families of communication protocols.

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardProtocolFamily

>

,

ProtocolFamily

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
StandardProtocolFamily
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardProtocolFamily c : StandardProtocolFamily.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
StandardProtocolFamily
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

#### Enum StandardProtocolFamily

java.lang.Object

- java.lang.Enum

<

StandardProtocolFamily

>
- - java.net.StandardProtocolFamily

java.lang.Enum

<

StandardProtocolFamily

>

- java.net.StandardProtocolFamily

java.net.StandardProtocolFamily

**All Implemented Interfaces:** Serializable

,

Comparable

<

StandardProtocolFamily

>

,

ProtocolFamily

```java
public enum
StandardProtocolFamily

extends
Enum
<
StandardProtocolFamily
>
implements
ProtocolFamily
```

Defines the standard families of communication protocols.

**Since:** 1.7

public enum

StandardProtocolFamily

extends

Enum

<

StandardProtocolFamily

>
implements

ProtocolFamily

Defines the standard families of communication protocols.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

INET

Internet Protocol Version 4 (IPv4)

INET6

Internet Protocol Version 6 (IPv6)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardProtocolFamily

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardProtocolFamily

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

- Methods declared in interface java.net.

ProtocolFamily

name

Enum Constant Summary

Enum Constants

Enum Constant

Description

INET

Internet Protocol Version 4 (IPv4)

INET6

Internet Protocol Version 6 (IPv6)

---

#### Enum Constant Summary

Internet Protocol Version 4 (IPv4)

Internet Protocol Version 6 (IPv6)

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StandardProtocolFamily

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StandardProtocolFamily

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

- Methods declared in interface java.net.

ProtocolFamily

name

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

Methods declared in interface java.net.

ProtocolFamily

name

---

#### Methods declared in interface java.net. ProtocolFamily

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- INET

```java
public static final
StandardProtocolFamily
INET
```

Internet Protocol Version 4 (IPv4)

- INET6

```java
public static final
StandardProtocolFamily
INET6
```

Internet Protocol Version 6 (IPv6)

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
StandardProtocolFamily
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardProtocolFamily c : StandardProtocolFamily.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardProtocolFamily
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

- INET

```java
public static final
StandardProtocolFamily
INET
```

Internet Protocol Version 4 (IPv4)

- INET6

```java
public static final
StandardProtocolFamily
INET6
```

Internet Protocol Version 6 (IPv6)

---

#### Enum Constant Detail

INET

```java
public static final
StandardProtocolFamily
INET
```

Internet Protocol Version 4 (IPv4)

---

#### INET

public static final

StandardProtocolFamily

INET

Internet Protocol Version 4 (IPv4)

INET6

```java
public static final
StandardProtocolFamily
INET6
```

Internet Protocol Version 6 (IPv6)

---

#### INET6

public static final

StandardProtocolFamily

INET6

Internet Protocol Version 6 (IPv6)

Method Detail

- values

```java
public static
StandardProtocolFamily
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardProtocolFamily c : StandardProtocolFamily.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StandardProtocolFamily
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
StandardProtocolFamily
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardProtocolFamily c : StandardProtocolFamily.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

StandardProtocolFamily

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StandardProtocolFamily c : StandardProtocolFamily.values())
System.out.println(c);
```

for (StandardProtocolFamily c : StandardProtocolFamily.values())
System.out.println(c);

valueOf

```java
public static
StandardProtocolFamily
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

StandardProtocolFamily

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

