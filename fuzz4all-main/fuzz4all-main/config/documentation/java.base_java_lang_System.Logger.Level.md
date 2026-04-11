# Enum System.Logger.Level

**Source:** `java.base\java\lang\System.Logger.Level.html`

### Class Description

```java
public static enum
System.Logger.Level

extends
Enum
<
System.Logger.Level
>
```

System

loggers

levels.

A level has a

name

and

severity

.
Level values are

ALL

,

TRACE

,

DEBUG

,

INFO

,

WARNING

,

ERROR

,

OFF

,
by order of increasing severity.

ALL

and

OFF

are simple markers with severities mapped respectively to

Integer.MIN_VALUE

and

Integer.MAX_VALUE

.

Severity values and Mapping to

java.util.logging.Level

.

System logger levels

are mapped to

java.util.logging levels

of corresponding severity.

The mapping is as follows:

System.Logger Severity Level Mapping

System.Logger Levels

java.util.logging Levels

ALL

ALL

TRACE

FINER

DEBUG

FINE

INFO

INFO

WARNING

WARNING

ERROR

SEVERE

OFF

OFF

**All Implemented Interfaces:** Serializable

,

Comparable

<

System.Logger.Level

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
System.Logger.Level
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (System.Logger.Level c : System.Logger.Level.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
System.Logger.Level
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

#### public final
String
getName()

Returns the name of this level.

**Returns:**
- this level

Enum.name()

.

---

#### public final int getSeverity()

Returns the severity of this level.
A higher severity means a more severe condition.

**Returns:**
- this level severity.

---

### Additional Sections

#### Enum System.Logger.Level

java.lang.Object

- java.lang.Enum

<

System.Logger.Level

>
- - java.lang.System.Logger.Level

java.lang.Enum

<

System.Logger.Level

>

- java.lang.System.Logger.Level

java.lang.System.Logger.Level

**All Implemented Interfaces:** Serializable

,

Comparable

<

System.Logger.Level

>

**Enclosing interface:** System.Logger

```java
public static enum
System.Logger.Level

extends
Enum
<
System.Logger.Level
>
```

System

loggers

levels.

A level has a

name

and

severity

.
Level values are

ALL

,

TRACE

,

DEBUG

,

INFO

,

WARNING

,

ERROR

,

OFF

,
by order of increasing severity.

ALL

and

OFF

are simple markers with severities mapped respectively to

Integer.MIN_VALUE

and

Integer.MAX_VALUE

.

Severity values and Mapping to

java.util.logging.Level

.

System logger levels

are mapped to

java.util.logging levels

of corresponding severity.

The mapping is as follows:

System.Logger Severity Level Mapping

System.Logger Levels

java.util.logging Levels

ALL

ALL

TRACE

FINER

DEBUG

FINE

INFO

INFO

WARNING

WARNING

ERROR

SEVERE

OFF

OFF

**Since:** 9
**See Also:** System.LoggerFinder

,

System.Logger

public static enum

System.Logger.Level

extends

Enum

<

System.Logger.Level

>

System

loggers

levels.

A level has a

name

and

severity

.
Level values are

ALL

,

TRACE

,

DEBUG

,

INFO

,

WARNING

,

ERROR

,

OFF

,
by order of increasing severity.

ALL

and

OFF

are simple markers with severities mapped respectively to

Integer.MIN_VALUE

and

Integer.MAX_VALUE

.

Severity values and Mapping to

java.util.logging.Level

.

System logger levels

are mapped to

java.util.logging levels

of corresponding severity.

The mapping is as follows:

System.Logger Severity Level Mapping

System.Logger Levels

java.util.logging Levels

ALL

ALL

TRACE

FINER

DEBUG

FINE

INFO

INFO

WARNING

WARNING

ERROR

SEVERE

OFF

OFF

Severity values and Mapping to

java.util.logging.Level

.

System logger levels

are mapped to

java.util.logging levels

of corresponding severity.

The mapping is as follows:

System.Logger Severity Level Mapping

System.Logger Levels

java.util.logging Levels

ALL

ALL

TRACE

FINER

DEBUG

FINE

INFO

INFO

WARNING

WARNING

ERROR

SEVERE

OFF

OFF

System logger levels

are mapped to

java.util.logging levels

of corresponding severity.

The mapping is as follows:

System.Logger Severity Level Mapping

System.Logger Levels

java.util.logging Levels

ALL

ALL

TRACE

FINER

DEBUG

FINE

INFO

INFO

WARNING

WARNING

ERROR

SEVERE

OFF

OFF

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ALL

A marker to indicate that all levels are enabled.

DEBUG

DEBUG

level: usually used to log debug information traces.

ERROR

ERROR

level: usually used to log error messages.

INFO

INFO

level: usually used to log information messages.

OFF

A marker to indicate that all levels are disabled.

TRACE

TRACE

level: usually used to log diagnostic information.

WARNING

WARNING

level: usually used to log warning messages.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of this level.

int

getSeverity

()

Returns the severity of this level.

static

System.Logger.Level

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

System.Logger.Level

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

ALL

A marker to indicate that all levels are enabled.

DEBUG

DEBUG

level: usually used to log debug information traces.

ERROR

ERROR

level: usually used to log error messages.

INFO

INFO

level: usually used to log information messages.

OFF

A marker to indicate that all levels are disabled.

TRACE

TRACE

level: usually used to log diagnostic information.

WARNING

WARNING

level: usually used to log warning messages.

---

#### Enum Constant Summary

A marker to indicate that all levels are enabled.

DEBUG

level: usually used to log debug information traces.

ERROR

level: usually used to log error messages.

INFO

level: usually used to log information messages.

A marker to indicate that all levels are disabled.

TRACE

level: usually used to log diagnostic information.

WARNING

level: usually used to log warning messages.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of this level.

int

getSeverity

()

Returns the severity of this level.

static

System.Logger.Level

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

System.Logger.Level

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

Returns the name of this level.

Returns the severity of this level.

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

- ALL

```java
public static final
System.Logger.Level
ALL
```

A marker to indicate that all levels are enabled.
This level

severity

is

Integer.MIN_VALUE

.

- TRACE

```java
public static final
System.Logger.Level
TRACE
```

TRACE

level: usually used to log diagnostic information.
This level

severity

is

400

.

- DEBUG

```java
public static final
System.Logger.Level
DEBUG
```

DEBUG

level: usually used to log debug information traces.
This level

severity

is

500

.

- INFO

```java
public static final
System.Logger.Level
INFO
```

INFO

level: usually used to log information messages.
This level

severity

is

800

.

- WARNING

```java
public static final
System.Logger.Level
WARNING
```

WARNING

level: usually used to log warning messages.
This level

severity

is

900

.

- ERROR

```java
public static final
System.Logger.Level
ERROR
```

ERROR

level: usually used to log error messages.
This level

severity

is

1000

.

- OFF

```java
public static final
System.Logger.Level
OFF
```

A marker to indicate that all levels are disabled.
This level

severity

is

Integer.MAX_VALUE

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
System.Logger.Level
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (System.Logger.Level c : System.Logger.Level.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
System.Logger.Level
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

- getName

```java
public final
String
getName()
```

Returns the name of this level.

**Returns:** this level

Enum.name()

.

- getSeverity

```java
public final int getSeverity()
```

Returns the severity of this level.
A higher severity means a more severe condition.

**Returns:** this level severity.

Enum Constant Detail

- ALL

```java
public static final
System.Logger.Level
ALL
```

A marker to indicate that all levels are enabled.
This level

severity

is

Integer.MIN_VALUE

.

- TRACE

```java
public static final
System.Logger.Level
TRACE
```

TRACE

level: usually used to log diagnostic information.
This level

severity

is

400

.

- DEBUG

```java
public static final
System.Logger.Level
DEBUG
```

DEBUG

level: usually used to log debug information traces.
This level

severity

is

500

.

- INFO

```java
public static final
System.Logger.Level
INFO
```

INFO

level: usually used to log information messages.
This level

severity

is

800

.

- WARNING

```java
public static final
System.Logger.Level
WARNING
```

WARNING

level: usually used to log warning messages.
This level

severity

is

900

.

- ERROR

```java
public static final
System.Logger.Level
ERROR
```

ERROR

level: usually used to log error messages.
This level

severity

is

1000

.

- OFF

```java
public static final
System.Logger.Level
OFF
```

A marker to indicate that all levels are disabled.
This level

severity

is

Integer.MAX_VALUE

.

---

#### Enum Constant Detail

ALL

```java
public static final
System.Logger.Level
ALL
```

A marker to indicate that all levels are enabled.
This level

severity

is

Integer.MIN_VALUE

.

---

#### ALL

public static final

System.Logger.Level

ALL

A marker to indicate that all levels are enabled.
This level

severity

is

Integer.MIN_VALUE

.

TRACE

```java
public static final
System.Logger.Level
TRACE
```

TRACE

level: usually used to log diagnostic information.
This level

severity

is

400

.

---

#### TRACE

public static final

System.Logger.Level

TRACE

TRACE

level: usually used to log diagnostic information.
This level

severity

is

400

.

DEBUG

```java
public static final
System.Logger.Level
DEBUG
```

DEBUG

level: usually used to log debug information traces.
This level

severity

is

500

.

---

#### DEBUG

public static final

System.Logger.Level

DEBUG

DEBUG

level: usually used to log debug information traces.
This level

severity

is

500

.

INFO

```java
public static final
System.Logger.Level
INFO
```

INFO

level: usually used to log information messages.
This level

severity

is

800

.

---

#### INFO

public static final

System.Logger.Level

INFO

INFO

level: usually used to log information messages.
This level

severity

is

800

.

WARNING

```java
public static final
System.Logger.Level
WARNING
```

WARNING

level: usually used to log warning messages.
This level

severity

is

900

.

---

#### WARNING

public static final

System.Logger.Level

WARNING

WARNING

level: usually used to log warning messages.
This level

severity

is

900

.

ERROR

```java
public static final
System.Logger.Level
ERROR
```

ERROR

level: usually used to log error messages.
This level

severity

is

1000

.

---

#### ERROR

public static final

System.Logger.Level

ERROR

ERROR

level: usually used to log error messages.
This level

severity

is

1000

.

OFF

```java
public static final
System.Logger.Level
OFF
```

A marker to indicate that all levels are disabled.
This level

severity

is

Integer.MAX_VALUE

.

---

#### OFF

public static final

System.Logger.Level

OFF

A marker to indicate that all levels are disabled.
This level

severity

is

Integer.MAX_VALUE

.

Method Detail

- values

```java
public static
System.Logger.Level
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (System.Logger.Level c : System.Logger.Level.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
System.Logger.Level
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

- getName

```java
public final
String
getName()
```

Returns the name of this level.

**Returns:** this level

Enum.name()

.

- getSeverity

```java
public final int getSeverity()
```

Returns the severity of this level.
A higher severity means a more severe condition.

**Returns:** this level severity.

---

#### Method Detail

values

```java
public static
System.Logger.Level
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (System.Logger.Level c : System.Logger.Level.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

System.Logger.Level

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (System.Logger.Level c : System.Logger.Level.values())
System.out.println(c);
```

for (System.Logger.Level c : System.Logger.Level.values())
System.out.println(c);

valueOf

```java
public static
System.Logger.Level
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

System.Logger.Level

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

getName

```java
public final
String
getName()
```

Returns the name of this level.

**Returns:** this level

Enum.name()

.

---

#### getName

public final

String

getName()

Returns the name of this level.

getSeverity

```java
public final int getSeverity()
```

Returns the severity of this level.
A higher severity means a more severe condition.

**Returns:** this level severity.

---

#### getSeverity

public final int getSeverity()

Returns the severity of this level.
A higher severity means a more severe condition.

---

