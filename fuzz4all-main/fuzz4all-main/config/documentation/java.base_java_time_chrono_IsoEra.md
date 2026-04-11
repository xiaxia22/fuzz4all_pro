# Enum IsoEra

**Source:** `java.base\java\time\chrono\IsoEra.html`

### Class Description

```java
public enum
IsoEra

extends
Enum
<
IsoEra
>
implements
Era
```

An era in the ISO calendar system.

The ISO-8601 standard does not define eras.
A definition has therefore been created with two eras - 'Current era' (CE) for
years on or after 0001-01-01 (ISO), and 'Before current era' (BCE) for years before that.

ISO years and eras

year-of-era

era

proleptic-year

2

CE

2

1

CE

1

1

BCE

0

2

BCE

-1

Do not use

ordinal()

to obtain the numeric representation of

IsoEra

.
Use

getValue()

instead.

**All Implemented Interfaces:** Serializable

,

Comparable

<

IsoEra

>

,

Era

,

TemporalAccessor

,

TemporalAdjuster

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
IsoEra
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (IsoEra c : IsoEra.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
IsoEra
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

#### public static
IsoEra
of​(int isoEra)

Obtains an instance of

IsoEra

from an

int

value.

IsoEra

is an enum representing the ISO eras of BCE/CE.
This factory allows the enum to be obtained from the

int

value.

**Parameters:**
- isoEra

- the BCE/CE value to represent, from 0 (BCE) to 1 (CE)

**Returns:**
- the era singleton, not null

**Throws:**
- DateTimeException

- if the value is invalid

---

#### public int getValue()

Gets the numeric era

int

value.

The era BCE has the value 0, while the era CE has the value 1.

**Specified by:**
- getValue

in interface

Era

**Returns:**
- the era value, from 0 (BCE) to 1 (CE)

---

### Additional Sections

#### Enum IsoEra

java.lang.Object

- java.lang.Enum

<

IsoEra

>
- - java.time.chrono.IsoEra

java.lang.Enum

<

IsoEra

>

- java.time.chrono.IsoEra

java.time.chrono.IsoEra

**All Implemented Interfaces:** Serializable

,

Comparable

<

IsoEra

>

,

Era

,

TemporalAccessor

,

TemporalAdjuster

```java
public enum
IsoEra

extends
Enum
<
IsoEra
>
implements
Era
```

An era in the ISO calendar system.

The ISO-8601 standard does not define eras.
A definition has therefore been created with two eras - 'Current era' (CE) for
years on or after 0001-01-01 (ISO), and 'Before current era' (BCE) for years before that.

ISO years and eras

year-of-era

era

proleptic-year

2

CE

2

1

CE

1

1

BCE

0

2

BCE

-1

Do not use

ordinal()

to obtain the numeric representation of

IsoEra

.
Use

getValue()

instead.

**Implementation Requirements:** This is an immutable and thread-safe enum.
**Since:** 1.8

public enum

IsoEra

extends

Enum

<

IsoEra

>
implements

Era

An era in the ISO calendar system.

The ISO-8601 standard does not define eras.
A definition has therefore been created with two eras - 'Current era' (CE) for
years on or after 0001-01-01 (ISO), and 'Before current era' (BCE) for years before that.

ISO years and eras

year-of-era

era

proleptic-year

2

CE

2

1

CE

1

1

BCE

0

2

BCE

-1

Do not use

ordinal()

to obtain the numeric representation of

IsoEra

.
Use

getValue()

instead.

The ISO-8601 standard does not define eras.
A definition has therefore been created with two eras - 'Current era' (CE) for
years on or after 0001-01-01 (ISO), and 'Before current era' (BCE) for years before that.

ISO years and eras

year-of-era

era

proleptic-year

2

CE

2

1

CE

1

1

BCE

0

2

BCE

-1

Do not use

ordinal()

to obtain the numeric representation of

IsoEra

.
Use

getValue()

instead.

Do not use

ordinal()

to obtain the numeric representation of

IsoEra

.
Use

getValue()

instead.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

BCE

The singleton instance for the era before the current one, 'Before Current Era',
which has the numeric value 0.

CE

The singleton instance for the current era, 'Current Era',
which has the numeric value 1.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getValue

()

Gets the numeric era

int

value.

static

IsoEra

of

​(int isoEra)

Obtains an instance of

IsoEra

from an

int

value.

static

IsoEra

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

IsoEra

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

- Methods declared in interface java.time.chrono.

Era

adjustInto

,

get

,

getDisplayName

,

getLong

,

isSupported

,

query

,

range

Enum Constant Summary

Enum Constants

Enum Constant

Description

BCE

The singleton instance for the era before the current one, 'Before Current Era',
which has the numeric value 0.

CE

The singleton instance for the current era, 'Current Era',
which has the numeric value 1.

---

#### Enum Constant Summary

The singleton instance for the era before the current one, 'Before Current Era',
which has the numeric value 0.

The singleton instance for the current era, 'Current Era',
which has the numeric value 1.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getValue

()

Gets the numeric era

int

value.

static

IsoEra

of

​(int isoEra)

Obtains an instance of

IsoEra

from an

int

value.

static

IsoEra

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

IsoEra

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

- Methods declared in interface java.time.chrono.

Era

adjustInto

,

get

,

getDisplayName

,

getLong

,

isSupported

,

query

,

range

---

#### Method Summary

Gets the numeric era

int

value.

Obtains an instance of

IsoEra

from an

int

value.

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

Methods declared in interface java.time.chrono.

Era

adjustInto

,

get

,

getDisplayName

,

getLong

,

isSupported

,

query

,

range

---

#### Methods declared in interface java.time.chrono. Era

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- BCE

```java
public static final
IsoEra
BCE
```

The singleton instance for the era before the current one, 'Before Current Era',
which has the numeric value 0.

- CE

```java
public static final
IsoEra
CE
```

The singleton instance for the current era, 'Current Era',
which has the numeric value 1.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
IsoEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (IsoEra c : IsoEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
IsoEra
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

- of

```java
public static
IsoEra
of​(int isoEra)
```

Obtains an instance of

IsoEra

from an

int

value.

IsoEra

is an enum representing the ISO eras of BCE/CE.
This factory allows the enum to be obtained from the

int

value.

**Parameters:** isoEra

- the BCE/CE value to represent, from 0 (BCE) to 1 (CE)
**Returns:** the era singleton, not null
**Throws:** DateTimeException

- if the value is invalid

- getValue

```java
public int getValue()
```

Gets the numeric era

int

value.

The era BCE has the value 0, while the era CE has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, from 0 (BCE) to 1 (CE)

Enum Constant Detail

- BCE

```java
public static final
IsoEra
BCE
```

The singleton instance for the era before the current one, 'Before Current Era',
which has the numeric value 0.

- CE

```java
public static final
IsoEra
CE
```

The singleton instance for the current era, 'Current Era',
which has the numeric value 1.

---

#### Enum Constant Detail

BCE

```java
public static final
IsoEra
BCE
```

The singleton instance for the era before the current one, 'Before Current Era',
which has the numeric value 0.

---

#### BCE

public static final

IsoEra

BCE

The singleton instance for the era before the current one, 'Before Current Era',
which has the numeric value 0.

CE

```java
public static final
IsoEra
CE
```

The singleton instance for the current era, 'Current Era',
which has the numeric value 1.

---

#### CE

public static final

IsoEra

CE

The singleton instance for the current era, 'Current Era',
which has the numeric value 1.

Method Detail

- values

```java
public static
IsoEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (IsoEra c : IsoEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
IsoEra
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

- of

```java
public static
IsoEra
of​(int isoEra)
```

Obtains an instance of

IsoEra

from an

int

value.

IsoEra

is an enum representing the ISO eras of BCE/CE.
This factory allows the enum to be obtained from the

int

value.

**Parameters:** isoEra

- the BCE/CE value to represent, from 0 (BCE) to 1 (CE)
**Returns:** the era singleton, not null
**Throws:** DateTimeException

- if the value is invalid

- getValue

```java
public int getValue()
```

Gets the numeric era

int

value.

The era BCE has the value 0, while the era CE has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, from 0 (BCE) to 1 (CE)

---

#### Method Detail

values

```java
public static
IsoEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (IsoEra c : IsoEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

IsoEra

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (IsoEra c : IsoEra.values())
System.out.println(c);
```

for (IsoEra c : IsoEra.values())
System.out.println(c);

valueOf

```java
public static
IsoEra
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

IsoEra

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

of

```java
public static
IsoEra
of​(int isoEra)
```

Obtains an instance of

IsoEra

from an

int

value.

IsoEra

is an enum representing the ISO eras of BCE/CE.
This factory allows the enum to be obtained from the

int

value.

**Parameters:** isoEra

- the BCE/CE value to represent, from 0 (BCE) to 1 (CE)
**Returns:** the era singleton, not null
**Throws:** DateTimeException

- if the value is invalid

---

#### of

public static

IsoEra

of​(int isoEra)

Obtains an instance of

IsoEra

from an

int

value.

IsoEra

is an enum representing the ISO eras of BCE/CE.
This factory allows the enum to be obtained from the

int

value.

IsoEra

is an enum representing the ISO eras of BCE/CE.
This factory allows the enum to be obtained from the

int

value.

getValue

```java
public int getValue()
```

Gets the numeric era

int

value.

The era BCE has the value 0, while the era CE has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, from 0 (BCE) to 1 (CE)

---

#### getValue

public int getValue()

Gets the numeric era

int

value.

The era BCE has the value 0, while the era CE has the value 1.

The era BCE has the value 0, while the era CE has the value 1.

---

