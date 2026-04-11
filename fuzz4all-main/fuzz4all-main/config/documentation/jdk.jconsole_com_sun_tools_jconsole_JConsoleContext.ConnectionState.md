# Enum JConsoleContext.ConnectionState

**Source:** `jdk.jconsole\com\sun\tools\jconsole\JConsoleContext.ConnectionState.html`

### Class Description

```java
public static enum
JConsoleContext.ConnectionState

extends
Enum
<
JConsoleContext.ConnectionState
>
```

Values for the

ConnectionState

bound property.

**All Implemented Interfaces:** Serializable

,

Comparable

<

JConsoleContext.ConnectionState

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
JConsoleContext.ConnectionState
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JConsoleContext.ConnectionState c : JConsoleContext.ConnectionState.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
JConsoleContext.ConnectionState
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

#### Enum JConsoleContext.ConnectionState

java.lang.Object

- java.lang.Enum

<

JConsoleContext.ConnectionState

>
- - com.sun.tools.jconsole.JConsoleContext.ConnectionState

java.lang.Enum

<

JConsoleContext.ConnectionState

>

- com.sun.tools.jconsole.JConsoleContext.ConnectionState

com.sun.tools.jconsole.JConsoleContext.ConnectionState

**All Implemented Interfaces:** Serializable

,

Comparable

<

JConsoleContext.ConnectionState

>

**Enclosing interface:** JConsoleContext

```java
public static enum
JConsoleContext.ConnectionState

extends
Enum
<
JConsoleContext.ConnectionState
>
```

Values for the

ConnectionState

bound property.

public static enum

JConsoleContext.ConnectionState

extends

Enum

<

JConsoleContext.ConnectionState

>

Values for the

ConnectionState

bound property.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CONNECTED

The connection has been successfully established.

CONNECTING

The connection is being attempted.

DISCONNECTED

No connection present.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

JConsoleContext.ConnectionState

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

JConsoleContext.ConnectionState

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

CONNECTED

The connection has been successfully established.

CONNECTING

The connection is being attempted.

DISCONNECTED

No connection present.

---

#### Enum Constant Summary

The connection has been successfully established.

The connection is being attempted.

No connection present.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

JConsoleContext.ConnectionState

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

JConsoleContext.ConnectionState

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

- CONNECTED

```java
public static final
JConsoleContext.ConnectionState
CONNECTED
```

The connection has been successfully established.

- DISCONNECTED

```java
public static final
JConsoleContext.ConnectionState
DISCONNECTED
```

No connection present.

- CONNECTING

```java
public static final
JConsoleContext.ConnectionState
CONNECTING
```

The connection is being attempted.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
JConsoleContext.ConnectionState
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JConsoleContext.ConnectionState c : JConsoleContext.ConnectionState.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
JConsoleContext.ConnectionState
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

- CONNECTED

```java
public static final
JConsoleContext.ConnectionState
CONNECTED
```

The connection has been successfully established.

- DISCONNECTED

```java
public static final
JConsoleContext.ConnectionState
DISCONNECTED
```

No connection present.

- CONNECTING

```java
public static final
JConsoleContext.ConnectionState
CONNECTING
```

The connection is being attempted.

---

#### Enum Constant Detail

CONNECTED

```java
public static final
JConsoleContext.ConnectionState
CONNECTED
```

The connection has been successfully established.

---

#### CONNECTED

public static final

JConsoleContext.ConnectionState

CONNECTED

The connection has been successfully established.

DISCONNECTED

```java
public static final
JConsoleContext.ConnectionState
DISCONNECTED
```

No connection present.

---

#### DISCONNECTED

public static final

JConsoleContext.ConnectionState

DISCONNECTED

No connection present.

CONNECTING

```java
public static final
JConsoleContext.ConnectionState
CONNECTING
```

The connection is being attempted.

---

#### CONNECTING

public static final

JConsoleContext.ConnectionState

CONNECTING

The connection is being attempted.

Method Detail

- values

```java
public static
JConsoleContext.ConnectionState
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JConsoleContext.ConnectionState c : JConsoleContext.ConnectionState.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
JConsoleContext.ConnectionState
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
JConsoleContext.ConnectionState
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JConsoleContext.ConnectionState c : JConsoleContext.ConnectionState.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

JConsoleContext.ConnectionState

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JConsoleContext.ConnectionState c : JConsoleContext.ConnectionState.values())
System.out.println(c);
```

for (JConsoleContext.ConnectionState c : JConsoleContext.ConnectionState.values())
System.out.println(c);

valueOf

```java
public static
JConsoleContext.ConnectionState
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

JConsoleContext.ConnectionState

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

