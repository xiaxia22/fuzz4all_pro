# Enum QuitStrategy

**Source:** `java.desktop\java\awt\desktop\QuitStrategy.html`

### Class Description

```java
public enum
QuitStrategy

extends
Enum
<
QuitStrategy
>
```

The strategy used to shut down the application, if Sudden Termination is not enabled.

**All Implemented Interfaces:** Serializable

,

Comparable

<

QuitStrategy

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
QuitStrategy
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (QuitStrategy c : QuitStrategy.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
QuitStrategy
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

#### Enum QuitStrategy

java.lang.Object

- java.lang.Enum

<

QuitStrategy

>
- - java.awt.desktop.QuitStrategy

java.lang.Enum

<

QuitStrategy

>

- java.awt.desktop.QuitStrategy

java.awt.desktop.QuitStrategy

**All Implemented Interfaces:** Serializable

,

Comparable

<

QuitStrategy

>

```java
public enum
QuitStrategy

extends
Enum
<
QuitStrategy
>
```

The strategy used to shut down the application, if Sudden Termination is not enabled.

**Since:** 9
**See Also:** Desktop.setQuitHandler(java.awt.desktop.QuitHandler)

,

Desktop.setQuitStrategy(java.awt.desktop.QuitStrategy)

,

Desktop.enableSuddenTermination()

,

Desktop.disableSuddenTermination()

public enum

QuitStrategy

extends

Enum

<

QuitStrategy

>

The strategy used to shut down the application, if Sudden Termination is not enabled.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CLOSE_ALL_WINDOWS

Shuts down the application by closing each window from back-to-front.

NORMAL_EXIT

Shuts down the application by calling

System.exit(0)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

QuitStrategy

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

QuitStrategy

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

CLOSE_ALL_WINDOWS

Shuts down the application by closing each window from back-to-front.

NORMAL_EXIT

Shuts down the application by calling

System.exit(0)

.

---

#### Enum Constant Summary

Shuts down the application by closing each window from back-to-front.

Shuts down the application by calling

System.exit(0)

.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

QuitStrategy

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

QuitStrategy

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

- NORMAL_EXIT

```java
public static final
QuitStrategy
NORMAL_EXIT
```

Shuts down the application by calling

System.exit(0)

. This is the default strategy.

- CLOSE_ALL_WINDOWS

```java
public static final
QuitStrategy
CLOSE_ALL_WINDOWS
```

Shuts down the application by closing each window from back-to-front.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
QuitStrategy
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (QuitStrategy c : QuitStrategy.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
QuitStrategy
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

- NORMAL_EXIT

```java
public static final
QuitStrategy
NORMAL_EXIT
```

Shuts down the application by calling

System.exit(0)

. This is the default strategy.

- CLOSE_ALL_WINDOWS

```java
public static final
QuitStrategy
CLOSE_ALL_WINDOWS
```

Shuts down the application by closing each window from back-to-front.

---

#### Enum Constant Detail

NORMAL_EXIT

```java
public static final
QuitStrategy
NORMAL_EXIT
```

Shuts down the application by calling

System.exit(0)

. This is the default strategy.

---

#### NORMAL_EXIT

public static final

QuitStrategy

NORMAL_EXIT

Shuts down the application by calling

System.exit(0)

. This is the default strategy.

CLOSE_ALL_WINDOWS

```java
public static final
QuitStrategy
CLOSE_ALL_WINDOWS
```

Shuts down the application by closing each window from back-to-front.

---

#### CLOSE_ALL_WINDOWS

public static final

QuitStrategy

CLOSE_ALL_WINDOWS

Shuts down the application by closing each window from back-to-front.

Method Detail

- values

```java
public static
QuitStrategy
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (QuitStrategy c : QuitStrategy.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
QuitStrategy
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
QuitStrategy
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (QuitStrategy c : QuitStrategy.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

QuitStrategy

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (QuitStrategy c : QuitStrategy.values())
System.out.println(c);
```

for (QuitStrategy c : QuitStrategy.values())
System.out.println(c);

valueOf

```java
public static
QuitStrategy
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

QuitStrategy

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

