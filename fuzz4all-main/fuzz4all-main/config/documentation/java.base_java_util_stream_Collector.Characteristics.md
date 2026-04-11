# Enum Collector.Characteristics

**Source:** `java.base\java\util\stream\Collector.Characteristics.html`

### Class Description

```java
public static enum
Collector.Characteristics

extends
Enum
<
Collector.Characteristics
>
```

Characteristics indicating properties of a

Collector

, which can
be used to optimize reduction implementations.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Collector.Characteristics

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Collector.Characteristics
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Collector.Characteristics c : Collector.Characteristics.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Collector.Characteristics
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

#### Enum Collector.Characteristics

java.lang.Object

- java.lang.Enum

<

Collector.Characteristics

>
- - java.util.stream.Collector.Characteristics

java.lang.Enum

<

Collector.Characteristics

>

- java.util.stream.Collector.Characteristics

java.util.stream.Collector.Characteristics

**All Implemented Interfaces:** Serializable

,

Comparable

<

Collector.Characteristics

>

**Enclosing interface:** Collector

<

T

,​

A

,​

R

>

```java
public static enum
Collector.Characteristics

extends
Enum
<
Collector.Characteristics
>
```

Characteristics indicating properties of a

Collector

, which can
be used to optimize reduction implementations.

public static enum

Collector.Characteristics

extends

Enum

<

Collector.Characteristics

>

Characteristics indicating properties of a

Collector

, which can
be used to optimize reduction implementations.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CONCURRENT

Indicates that this collector is

concurrent

, meaning that
the result container can support the accumulator function being
called concurrently with the same result container from multiple
threads.

IDENTITY_FINISH

Indicates that the finisher function is the identity function and
can be elided.

UNORDERED

Indicates that the collection operation does not commit to preserving
the encounter order of input elements.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Collector.Characteristics

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Collector.Characteristics

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

CONCURRENT

Indicates that this collector is

concurrent

, meaning that
the result container can support the accumulator function being
called concurrently with the same result container from multiple
threads.

IDENTITY_FINISH

Indicates that the finisher function is the identity function and
can be elided.

UNORDERED

Indicates that the collection operation does not commit to preserving
the encounter order of input elements.

---

#### Enum Constant Summary

Indicates that this collector is

concurrent

, meaning that
the result container can support the accumulator function being
called concurrently with the same result container from multiple
threads.

Indicates that the finisher function is the identity function and
can be elided.

Indicates that the collection operation does not commit to preserving
the encounter order of input elements.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Collector.Characteristics

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Collector.Characteristics

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

- CONCURRENT

```java
public static final
Collector.Characteristics
CONCURRENT
```

Indicates that this collector is

concurrent

, meaning that
the result container can support the accumulator function being
called concurrently with the same result container from multiple
threads.

If a

CONCURRENT

collector is not also

UNORDERED

,
then it should only be evaluated concurrently if applied to an
unordered data source.

- UNORDERED

```java
public static final
Collector.Characteristics
UNORDERED
```

Indicates that the collection operation does not commit to preserving
the encounter order of input elements. (This might be true if the
result container has no intrinsic order, such as a

Set

.)

- IDENTITY_FINISH

```java
public static final
Collector.Characteristics
IDENTITY_FINISH
```

Indicates that the finisher function is the identity function and
can be elided. If set, it must be the case that an unchecked cast
from A to R will succeed.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Collector.Characteristics
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Collector.Characteristics c : Collector.Characteristics.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Collector.Characteristics
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

- CONCURRENT

```java
public static final
Collector.Characteristics
CONCURRENT
```

Indicates that this collector is

concurrent

, meaning that
the result container can support the accumulator function being
called concurrently with the same result container from multiple
threads.

If a

CONCURRENT

collector is not also

UNORDERED

,
then it should only be evaluated concurrently if applied to an
unordered data source.

- UNORDERED

```java
public static final
Collector.Characteristics
UNORDERED
```

Indicates that the collection operation does not commit to preserving
the encounter order of input elements. (This might be true if the
result container has no intrinsic order, such as a

Set

.)

- IDENTITY_FINISH

```java
public static final
Collector.Characteristics
IDENTITY_FINISH
```

Indicates that the finisher function is the identity function and
can be elided. If set, it must be the case that an unchecked cast
from A to R will succeed.

---

#### Enum Constant Detail

CONCURRENT

```java
public static final
Collector.Characteristics
CONCURRENT
```

Indicates that this collector is

concurrent

, meaning that
the result container can support the accumulator function being
called concurrently with the same result container from multiple
threads.

If a

CONCURRENT

collector is not also

UNORDERED

,
then it should only be evaluated concurrently if applied to an
unordered data source.

---

#### CONCURRENT

public static final

Collector.Characteristics

CONCURRENT

Indicates that this collector is

concurrent

, meaning that
the result container can support the accumulator function being
called concurrently with the same result container from multiple
threads.

If a

CONCURRENT

collector is not also

UNORDERED

,
then it should only be evaluated concurrently if applied to an
unordered data source.

If a

CONCURRENT

collector is not also

UNORDERED

,
then it should only be evaluated concurrently if applied to an
unordered data source.

UNORDERED

```java
public static final
Collector.Characteristics
UNORDERED
```

Indicates that the collection operation does not commit to preserving
the encounter order of input elements. (This might be true if the
result container has no intrinsic order, such as a

Set

.)

---

#### UNORDERED

public static final

Collector.Characteristics

UNORDERED

Indicates that the collection operation does not commit to preserving
the encounter order of input elements. (This might be true if the
result container has no intrinsic order, such as a

Set

.)

IDENTITY_FINISH

```java
public static final
Collector.Characteristics
IDENTITY_FINISH
```

Indicates that the finisher function is the identity function and
can be elided. If set, it must be the case that an unchecked cast
from A to R will succeed.

---

#### IDENTITY_FINISH

public static final

Collector.Characteristics

IDENTITY_FINISH

Indicates that the finisher function is the identity function and
can be elided. If set, it must be the case that an unchecked cast
from A to R will succeed.

Method Detail

- values

```java
public static
Collector.Characteristics
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Collector.Characteristics c : Collector.Characteristics.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Collector.Characteristics
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
Collector.Characteristics
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Collector.Characteristics c : Collector.Characteristics.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Collector.Characteristics

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Collector.Characteristics c : Collector.Characteristics.values())
System.out.println(c);
```

for (Collector.Characteristics c : Collector.Characteristics.values())
System.out.println(c);

valueOf

```java
public static
Collector.Characteristics
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

Collector.Characteristics

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

