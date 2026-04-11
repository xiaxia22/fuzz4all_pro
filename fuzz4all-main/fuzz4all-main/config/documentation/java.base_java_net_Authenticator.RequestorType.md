# Enum Authenticator.RequestorType

**Source:** `java.base\java\net\Authenticator.RequestorType.html`

### Class Description

```java
public static enum
Authenticator.RequestorType

extends
Enum
<
Authenticator.RequestorType
>
```

The type of the entity requesting authentication.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Authenticator.RequestorType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Authenticator.RequestorType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Authenticator.RequestorType c : Authenticator.RequestorType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Authenticator.RequestorType
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

#### Enum Authenticator.RequestorType

java.lang.Object

- java.lang.Enum

<

Authenticator.RequestorType

>
- - java.net.Authenticator.RequestorType

java.lang.Enum

<

Authenticator.RequestorType

>

- java.net.Authenticator.RequestorType

java.net.Authenticator.RequestorType

**All Implemented Interfaces:** Serializable

,

Comparable

<

Authenticator.RequestorType

>

**Enclosing class:** Authenticator

```java
public static enum
Authenticator.RequestorType

extends
Enum
<
Authenticator.RequestorType
>
```

The type of the entity requesting authentication.

**Since:** 1.5

public static enum

Authenticator.RequestorType

extends

Enum

<

Authenticator.RequestorType

>

The type of the entity requesting authentication.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

PROXY

Entity requesting authentication is a HTTP proxy server.

SERVER

Entity requesting authentication is a HTTP origin server.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Authenticator.RequestorType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Authenticator.RequestorType

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

PROXY

Entity requesting authentication is a HTTP proxy server.

SERVER

Entity requesting authentication is a HTTP origin server.

---

#### Enum Constant Summary

Entity requesting authentication is a HTTP proxy server.

Entity requesting authentication is a HTTP origin server.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Authenticator.RequestorType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Authenticator.RequestorType

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

- PROXY

```java
public static final
Authenticator.RequestorType
PROXY
```

Entity requesting authentication is a HTTP proxy server.

- SERVER

```java
public static final
Authenticator.RequestorType
SERVER
```

Entity requesting authentication is a HTTP origin server.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Authenticator.RequestorType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Authenticator.RequestorType c : Authenticator.RequestorType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Authenticator.RequestorType
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

- PROXY

```java
public static final
Authenticator.RequestorType
PROXY
```

Entity requesting authentication is a HTTP proxy server.

- SERVER

```java
public static final
Authenticator.RequestorType
SERVER
```

Entity requesting authentication is a HTTP origin server.

---

#### Enum Constant Detail

PROXY

```java
public static final
Authenticator.RequestorType
PROXY
```

Entity requesting authentication is a HTTP proxy server.

---

#### PROXY

public static final

Authenticator.RequestorType

PROXY

Entity requesting authentication is a HTTP proxy server.

SERVER

```java
public static final
Authenticator.RequestorType
SERVER
```

Entity requesting authentication is a HTTP origin server.

---

#### SERVER

public static final

Authenticator.RequestorType

SERVER

Entity requesting authentication is a HTTP origin server.

Method Detail

- values

```java
public static
Authenticator.RequestorType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Authenticator.RequestorType c : Authenticator.RequestorType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Authenticator.RequestorType
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
Authenticator.RequestorType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Authenticator.RequestorType c : Authenticator.RequestorType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Authenticator.RequestorType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Authenticator.RequestorType c : Authenticator.RequestorType.values())
System.out.println(c);
```

for (Authenticator.RequestorType c : Authenticator.RequestorType.values())
System.out.println(c);

valueOf

```java
public static
Authenticator.RequestorType
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

Authenticator.RequestorType

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

