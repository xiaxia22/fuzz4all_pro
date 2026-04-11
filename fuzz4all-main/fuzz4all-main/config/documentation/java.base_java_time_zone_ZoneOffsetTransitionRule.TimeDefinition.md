# Enum ZoneOffsetTransitionRule.TimeDefinition

**Source:** `java.base\java\time\zone\ZoneOffsetTransitionRule.TimeDefinition.html`

### Class Description

```java
public static enum
ZoneOffsetTransitionRule.TimeDefinition

extends
Enum
<
ZoneOffsetTransitionRule.TimeDefinition
>
```

A definition of the way a local time can be converted to the actual
transition date-time.

Time zone rules are expressed in one of three ways:

- Relative to UTC
- Relative to the standard offset in force
- Relative to the wall offset (what you would see on a clock on the wall)

**All Implemented Interfaces:** Serializable

,

Comparable

<

ZoneOffsetTransitionRule.TimeDefinition

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ZoneOffsetTransitionRule.TimeDefinition
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ZoneOffsetTransitionRule.TimeDefinition c : ZoneOffsetTransitionRule.TimeDefinition.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ZoneOffsetTransitionRule.TimeDefinition
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

#### public
LocalDateTime
createDateTime​(
LocalDateTime
dateTime,

ZoneOffset
standardOffset,

ZoneOffset
wallOffset)

Converts the specified local date-time to the local date-time actually
seen on a wall clock.

This method converts using the type of this enum.
The output is defined relative to the 'before' offset of the transition.

The UTC type uses the UTC offset.
The STANDARD type uses the standard offset.
The WALL type returns the input date-time.
The result is intended for use with the wall-offset.

**Parameters:**
- dateTime

- the local date-time, not null
- standardOffset

- the standard offset, not null
- wallOffset

- the wall offset, not null

**Returns:**
- the date-time relative to the wall/before offset, not null

---

### Additional Sections

#### Enum ZoneOffsetTransitionRule.TimeDefinition

java.lang.Object

- java.lang.Enum

<

ZoneOffsetTransitionRule.TimeDefinition

>
- - java.time.zone.ZoneOffsetTransitionRule.TimeDefinition

java.lang.Enum

<

ZoneOffsetTransitionRule.TimeDefinition

>

- java.time.zone.ZoneOffsetTransitionRule.TimeDefinition

java.time.zone.ZoneOffsetTransitionRule.TimeDefinition

**All Implemented Interfaces:** Serializable

,

Comparable

<

ZoneOffsetTransitionRule.TimeDefinition

>

**Enclosing class:** ZoneOffsetTransitionRule

```java
public static enum
ZoneOffsetTransitionRule.TimeDefinition

extends
Enum
<
ZoneOffsetTransitionRule.TimeDefinition
>
```

A definition of the way a local time can be converted to the actual
transition date-time.

Time zone rules are expressed in one of three ways:

- Relative to UTC
- Relative to the standard offset in force
- Relative to the wall offset (what you would see on a clock on the wall)

public static enum

ZoneOffsetTransitionRule.TimeDefinition

extends

Enum

<

ZoneOffsetTransitionRule.TimeDefinition

>

A definition of the way a local time can be converted to the actual
transition date-time.

Time zone rules are expressed in one of three ways:

- Relative to UTC
- Relative to the standard offset in force
- Relative to the wall offset (what you would see on a clock on the wall)

Time zone rules are expressed in one of three ways:

- Relative to UTC
- Relative to the standard offset in force
- Relative to the wall offset (what you would see on a clock on the wall)

Relative to UTC

Relative to the standard offset in force

Relative to the wall offset (what you would see on a clock on the wall)

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

STANDARD

The local date-time is expressed in terms of the standard offset.

UTC

The local date-time is expressed in terms of the UTC offset.

WALL

The local date-time is expressed in terms of the wall offset.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

LocalDateTime

createDateTime

​(

LocalDateTime

dateTime,

ZoneOffset

standardOffset,

ZoneOffset

wallOffset)

Converts the specified local date-time to the local date-time actually
seen on a wall clock.

static

ZoneOffsetTransitionRule.TimeDefinition

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ZoneOffsetTransitionRule.TimeDefinition

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

STANDARD

The local date-time is expressed in terms of the standard offset.

UTC

The local date-time is expressed in terms of the UTC offset.

WALL

The local date-time is expressed in terms of the wall offset.

---

#### Enum Constant Summary

The local date-time is expressed in terms of the standard offset.

The local date-time is expressed in terms of the UTC offset.

The local date-time is expressed in terms of the wall offset.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

LocalDateTime

createDateTime

​(

LocalDateTime

dateTime,

ZoneOffset

standardOffset,

ZoneOffset

wallOffset)

Converts the specified local date-time to the local date-time actually
seen on a wall clock.

static

ZoneOffsetTransitionRule.TimeDefinition

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ZoneOffsetTransitionRule.TimeDefinition

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

Converts the specified local date-time to the local date-time actually
seen on a wall clock.

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

- UTC

```java
public static final
ZoneOffsetTransitionRule.TimeDefinition
UTC
```

The local date-time is expressed in terms of the UTC offset.

- WALL

```java
public static final
ZoneOffsetTransitionRule.TimeDefinition
WALL
```

The local date-time is expressed in terms of the wall offset.

- STANDARD

```java
public static final
ZoneOffsetTransitionRule.TimeDefinition
STANDARD
```

The local date-time is expressed in terms of the standard offset.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ZoneOffsetTransitionRule.TimeDefinition
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ZoneOffsetTransitionRule.TimeDefinition c : ZoneOffsetTransitionRule.TimeDefinition.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ZoneOffsetTransitionRule.TimeDefinition
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

- createDateTime

```java
public
LocalDateTime
createDateTime​(
LocalDateTime
dateTime,

ZoneOffset
standardOffset,

ZoneOffset
wallOffset)
```

Converts the specified local date-time to the local date-time actually
seen on a wall clock.

This method converts using the type of this enum.
The output is defined relative to the 'before' offset of the transition.

The UTC type uses the UTC offset.
The STANDARD type uses the standard offset.
The WALL type returns the input date-time.
The result is intended for use with the wall-offset.

**Parameters:** dateTime

- the local date-time, not null
**Parameters:** standardOffset

- the standard offset, not null
**Parameters:** wallOffset

- the wall offset, not null
**Returns:** the date-time relative to the wall/before offset, not null

Enum Constant Detail

- UTC

```java
public static final
ZoneOffsetTransitionRule.TimeDefinition
UTC
```

The local date-time is expressed in terms of the UTC offset.

- WALL

```java
public static final
ZoneOffsetTransitionRule.TimeDefinition
WALL
```

The local date-time is expressed in terms of the wall offset.

- STANDARD

```java
public static final
ZoneOffsetTransitionRule.TimeDefinition
STANDARD
```

The local date-time is expressed in terms of the standard offset.

---

#### Enum Constant Detail

UTC

```java
public static final
ZoneOffsetTransitionRule.TimeDefinition
UTC
```

The local date-time is expressed in terms of the UTC offset.

---

#### UTC

public static final

ZoneOffsetTransitionRule.TimeDefinition

UTC

The local date-time is expressed in terms of the UTC offset.

WALL

```java
public static final
ZoneOffsetTransitionRule.TimeDefinition
WALL
```

The local date-time is expressed in terms of the wall offset.

---

#### WALL

public static final

ZoneOffsetTransitionRule.TimeDefinition

WALL

The local date-time is expressed in terms of the wall offset.

STANDARD

```java
public static final
ZoneOffsetTransitionRule.TimeDefinition
STANDARD
```

The local date-time is expressed in terms of the standard offset.

---

#### STANDARD

public static final

ZoneOffsetTransitionRule.TimeDefinition

STANDARD

The local date-time is expressed in terms of the standard offset.

Method Detail

- values

```java
public static
ZoneOffsetTransitionRule.TimeDefinition
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ZoneOffsetTransitionRule.TimeDefinition c : ZoneOffsetTransitionRule.TimeDefinition.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ZoneOffsetTransitionRule.TimeDefinition
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

- createDateTime

```java
public
LocalDateTime
createDateTime​(
LocalDateTime
dateTime,

ZoneOffset
standardOffset,

ZoneOffset
wallOffset)
```

Converts the specified local date-time to the local date-time actually
seen on a wall clock.

This method converts using the type of this enum.
The output is defined relative to the 'before' offset of the transition.

The UTC type uses the UTC offset.
The STANDARD type uses the standard offset.
The WALL type returns the input date-time.
The result is intended for use with the wall-offset.

**Parameters:** dateTime

- the local date-time, not null
**Parameters:** standardOffset

- the standard offset, not null
**Parameters:** wallOffset

- the wall offset, not null
**Returns:** the date-time relative to the wall/before offset, not null

---

#### Method Detail

values

```java
public static
ZoneOffsetTransitionRule.TimeDefinition
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ZoneOffsetTransitionRule.TimeDefinition c : ZoneOffsetTransitionRule.TimeDefinition.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ZoneOffsetTransitionRule.TimeDefinition

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ZoneOffsetTransitionRule.TimeDefinition c : ZoneOffsetTransitionRule.TimeDefinition.values())
System.out.println(c);
```

for (ZoneOffsetTransitionRule.TimeDefinition c : ZoneOffsetTransitionRule.TimeDefinition.values())
System.out.println(c);

valueOf

```java
public static
ZoneOffsetTransitionRule.TimeDefinition
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

ZoneOffsetTransitionRule.TimeDefinition

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

createDateTime

```java
public
LocalDateTime
createDateTime​(
LocalDateTime
dateTime,

ZoneOffset
standardOffset,

ZoneOffset
wallOffset)
```

Converts the specified local date-time to the local date-time actually
seen on a wall clock.

This method converts using the type of this enum.
The output is defined relative to the 'before' offset of the transition.

The UTC type uses the UTC offset.
The STANDARD type uses the standard offset.
The WALL type returns the input date-time.
The result is intended for use with the wall-offset.

**Parameters:** dateTime

- the local date-time, not null
**Parameters:** standardOffset

- the standard offset, not null
**Parameters:** wallOffset

- the wall offset, not null
**Returns:** the date-time relative to the wall/before offset, not null

---

#### createDateTime

public

LocalDateTime

createDateTime​(

LocalDateTime

dateTime,

ZoneOffset

standardOffset,

ZoneOffset

wallOffset)

Converts the specified local date-time to the local date-time actually
seen on a wall clock.

This method converts using the type of this enum.
The output is defined relative to the 'before' offset of the transition.

The UTC type uses the UTC offset.
The STANDARD type uses the standard offset.
The WALL type returns the input date-time.
The result is intended for use with the wall-offset.

This method converts using the type of this enum.
The output is defined relative to the 'before' offset of the transition.

The UTC type uses the UTC offset.
The STANDARD type uses the standard offset.
The WALL type returns the input date-time.
The result is intended for use with the wall-offset.

The UTC type uses the UTC offset.
The STANDARD type uses the standard offset.
The WALL type returns the input date-time.
The result is intended for use with the wall-offset.

---

