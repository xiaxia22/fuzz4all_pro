# Enum TrayIcon.MessageType

**Source:** `java.desktop\java\awt\TrayIcon.MessageType.html`

### Class Description

```java
public static enum
TrayIcon.MessageType

extends
Enum
<
TrayIcon.MessageType
>
```

The message type determines which icon will be displayed in the
caption of the message, and a possible system sound a message
may generate upon showing.

**All Implemented Interfaces:** Serializable

,

Comparable

<

TrayIcon.MessageType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
TrayIcon.MessageType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TrayIcon.MessageType c : TrayIcon.MessageType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
TrayIcon.MessageType
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

#### Enum TrayIcon.MessageType

java.lang.Object

- java.lang.Enum

<

TrayIcon.MessageType

>
- - java.awt.TrayIcon.MessageType

java.lang.Enum

<

TrayIcon.MessageType

>

- java.awt.TrayIcon.MessageType

java.awt.TrayIcon.MessageType

**All Implemented Interfaces:** Serializable

,

Comparable

<

TrayIcon.MessageType

>

**Enclosing class:** TrayIcon

```java
public static enum
TrayIcon.MessageType

extends
Enum
<
TrayIcon.MessageType
>
```

The message type determines which icon will be displayed in the
caption of the message, and a possible system sound a message
may generate upon showing.

**Since:** 1.6
**See Also:** TrayIcon

,

TrayIcon.displayMessage(String, String, MessageType)

public static enum

TrayIcon.MessageType

extends

Enum

<

TrayIcon.MessageType

>

The message type determines which icon will be displayed in the
caption of the message, and a possible system sound a message
may generate upon showing.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ERROR

An error message

INFO

An information message

NONE

Simple message

WARNING

A warning message

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

TrayIcon.MessageType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

TrayIcon.MessageType

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

ERROR

An error message

INFO

An information message

NONE

Simple message

WARNING

A warning message

---

#### Enum Constant Summary

An error message

An information message

Simple message

A warning message

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

TrayIcon.MessageType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

TrayIcon.MessageType

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

- ERROR

```java
public static final
TrayIcon.MessageType
ERROR
```

An error message

- WARNING

```java
public static final
TrayIcon.MessageType
WARNING
```

A warning message

- INFO

```java
public static final
TrayIcon.MessageType
INFO
```

An information message

- NONE

```java
public static final
TrayIcon.MessageType
NONE
```

Simple message

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
TrayIcon.MessageType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TrayIcon.MessageType c : TrayIcon.MessageType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
TrayIcon.MessageType
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

- ERROR

```java
public static final
TrayIcon.MessageType
ERROR
```

An error message

- WARNING

```java
public static final
TrayIcon.MessageType
WARNING
```

A warning message

- INFO

```java
public static final
TrayIcon.MessageType
INFO
```

An information message

- NONE

```java
public static final
TrayIcon.MessageType
NONE
```

Simple message

---

#### Enum Constant Detail

ERROR

```java
public static final
TrayIcon.MessageType
ERROR
```

An error message

---

#### ERROR

public static final

TrayIcon.MessageType

ERROR

An error message

WARNING

```java
public static final
TrayIcon.MessageType
WARNING
```

A warning message

---

#### WARNING

public static final

TrayIcon.MessageType

WARNING

A warning message

INFO

```java
public static final
TrayIcon.MessageType
INFO
```

An information message

---

#### INFO

public static final

TrayIcon.MessageType

INFO

An information message

NONE

```java
public static final
TrayIcon.MessageType
NONE
```

Simple message

---

#### NONE

public static final

TrayIcon.MessageType

NONE

Simple message

Method Detail

- values

```java
public static
TrayIcon.MessageType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TrayIcon.MessageType c : TrayIcon.MessageType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
TrayIcon.MessageType
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
TrayIcon.MessageType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TrayIcon.MessageType c : TrayIcon.MessageType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

TrayIcon.MessageType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TrayIcon.MessageType c : TrayIcon.MessageType.values())
System.out.println(c);
```

for (TrayIcon.MessageType c : TrayIcon.MessageType.values())
System.out.println(c);

valueOf

```java
public static
TrayIcon.MessageType
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

TrayIcon.MessageType

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

