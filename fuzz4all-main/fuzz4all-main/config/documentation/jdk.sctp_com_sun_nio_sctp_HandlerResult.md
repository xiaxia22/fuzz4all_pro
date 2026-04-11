# Enum HandlerResult

**Source:** `jdk.sctp\com\sun\nio\sctp\HandlerResult.html`

### Class Description

```java
public enum
HandlerResult

extends
Enum
<
HandlerResult
>
```

Defines notification handler results.

The

HandlerResult

is used to determine the behavior of the
channel after it handles a notification from the SCTP stack. Essentially its
value determines if the channel should try to receive another notificaiton or
a message before returning.

**All Implemented Interfaces:** Serializable

,

Comparable

<

HandlerResult

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
HandlerResult
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HandlerResult c : HandlerResult.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
HandlerResult
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

#### Enum HandlerResult

java.lang.Object

- java.lang.Enum

<

HandlerResult

>
- - com.sun.nio.sctp.HandlerResult

java.lang.Enum

<

HandlerResult

>

- com.sun.nio.sctp.HandlerResult

com.sun.nio.sctp.HandlerResult

**All Implemented Interfaces:** Serializable

,

Comparable

<

HandlerResult

>

```java
public enum
HandlerResult

extends
Enum
<
HandlerResult
>
```

Defines notification handler results.

The

HandlerResult

is used to determine the behavior of the
channel after it handles a notification from the SCTP stack. Essentially its
value determines if the channel should try to receive another notificaiton or
a message before returning.

**Since:** 1.7

public enum

HandlerResult

extends

Enum

<

HandlerResult

>

Defines notification handler results.

The

HandlerResult

is used to determine the behavior of the
channel after it handles a notification from the SCTP stack. Essentially its
value determines if the channel should try to receive another notificaiton or
a message before returning.

The

HandlerResult

is used to determine the behavior of the
channel after it handles a notification from the SCTP stack. Essentially its
value determines if the channel should try to receive another notificaiton or
a message before returning.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CONTINUE

Try to receieve another message or notification.

RETURN

Return without trying to receive any more data.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

HandlerResult

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

HandlerResult

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

CONTINUE

Try to receieve another message or notification.

RETURN

Return without trying to receive any more data.

---

#### Enum Constant Summary

Try to receieve another message or notification.

Return without trying to receive any more data.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

HandlerResult

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

HandlerResult

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

- CONTINUE

```java
public static final
HandlerResult
CONTINUE
```

Try to receieve another message or notification.

- RETURN

```java
public static final
HandlerResult
RETURN
```

Return without trying to receive any more data.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
HandlerResult
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HandlerResult c : HandlerResult.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
HandlerResult
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

- CONTINUE

```java
public static final
HandlerResult
CONTINUE
```

Try to receieve another message or notification.

- RETURN

```java
public static final
HandlerResult
RETURN
```

Return without trying to receive any more data.

---

#### Enum Constant Detail

CONTINUE

```java
public static final
HandlerResult
CONTINUE
```

Try to receieve another message or notification.

---

#### CONTINUE

public static final

HandlerResult

CONTINUE

Try to receieve another message or notification.

RETURN

```java
public static final
HandlerResult
RETURN
```

Return without trying to receive any more data.

---

#### RETURN

public static final

HandlerResult

RETURN

Return without trying to receive any more data.

Method Detail

- values

```java
public static
HandlerResult
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HandlerResult c : HandlerResult.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
HandlerResult
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
HandlerResult
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HandlerResult c : HandlerResult.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

HandlerResult

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HandlerResult c : HandlerResult.values())
System.out.println(c);
```

for (HandlerResult c : HandlerResult.values())
System.out.println(c);

valueOf

```java
public static
HandlerResult
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

HandlerResult

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

