# Enum Proxy.Type

**Source:** `java.base\java\net\Proxy.Type.html`

### Class Description

```java
public static enum
Proxy.Type

extends
Enum
<
Proxy.Type
>
```

Represents the proxy type.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Proxy.Type

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Proxy.Type
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Proxy.Type c : Proxy.Type.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Proxy.Type
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

#### Enum Proxy.Type

java.lang.Object

- java.lang.Enum

<

Proxy.Type

>
- - java.net.Proxy.Type

java.lang.Enum

<

Proxy.Type

>

- java.net.Proxy.Type

java.net.Proxy.Type

**All Implemented Interfaces:** Serializable

,

Comparable

<

Proxy.Type

>

**Enclosing class:** Proxy

```java
public static enum
Proxy.Type

extends
Enum
<
Proxy.Type
>
```

Represents the proxy type.

**Since:** 1.5

public static enum

Proxy.Type

extends

Enum

<

Proxy.Type

>

Represents the proxy type.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

DIRECT

Represents a direct connection, or the absence of a proxy.

HTTP

Represents proxy for high level protocols such as HTTP or FTP.

SOCKS

Represents a SOCKS (V4 or V5) proxy.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Proxy.Type

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Proxy.Type

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

DIRECT

Represents a direct connection, or the absence of a proxy.

HTTP

Represents proxy for high level protocols such as HTTP or FTP.

SOCKS

Represents a SOCKS (V4 or V5) proxy.

---

#### Enum Constant Summary

Represents a direct connection, or the absence of a proxy.

Represents proxy for high level protocols such as HTTP or FTP.

Represents a SOCKS (V4 or V5) proxy.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Proxy.Type

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Proxy.Type

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

- DIRECT

```java
public static final
Proxy.Type
DIRECT
```

Represents a direct connection, or the absence of a proxy.

- HTTP

```java
public static final
Proxy.Type
HTTP
```

Represents proxy for high level protocols such as HTTP or FTP.

- SOCKS

```java
public static final
Proxy.Type
SOCKS
```

Represents a SOCKS (V4 or V5) proxy.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Proxy.Type
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Proxy.Type c : Proxy.Type.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Proxy.Type
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

- DIRECT

```java
public static final
Proxy.Type
DIRECT
```

Represents a direct connection, or the absence of a proxy.

- HTTP

```java
public static final
Proxy.Type
HTTP
```

Represents proxy for high level protocols such as HTTP or FTP.

- SOCKS

```java
public static final
Proxy.Type
SOCKS
```

Represents a SOCKS (V4 or V5) proxy.

---

#### Enum Constant Detail

DIRECT

```java
public static final
Proxy.Type
DIRECT
```

Represents a direct connection, or the absence of a proxy.

---

#### DIRECT

public static final

Proxy.Type

DIRECT

Represents a direct connection, or the absence of a proxy.

HTTP

```java
public static final
Proxy.Type
HTTP
```

Represents proxy for high level protocols such as HTTP or FTP.

---

#### HTTP

public static final

Proxy.Type

HTTP

Represents proxy for high level protocols such as HTTP or FTP.

SOCKS

```java
public static final
Proxy.Type
SOCKS
```

Represents a SOCKS (V4 or V5) proxy.

---

#### SOCKS

public static final

Proxy.Type

SOCKS

Represents a SOCKS (V4 or V5) proxy.

Method Detail

- values

```java
public static
Proxy.Type
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Proxy.Type c : Proxy.Type.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Proxy.Type
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
Proxy.Type
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Proxy.Type c : Proxy.Type.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Proxy.Type

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Proxy.Type c : Proxy.Type.values())
System.out.println(c);
```

for (Proxy.Type c : Proxy.Type.values())
System.out.println(c);

valueOf

```java
public static
Proxy.Type
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

Proxy.Type

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

