# Enum ThaiBuddhistEra

**Source:** `java.base\java\time\chrono\ThaiBuddhistEra.html`

### Class Description

```java
public enum
ThaiBuddhistEra

extends
Enum
<
ThaiBuddhistEra
>
implements
Era
```

An era in the Thai Buddhist calendar system.

The Thai Buddhist calendar system has two eras.
The current era, for years from 1 onwards, is known as the 'Buddhist' era.
All previous years, zero or earlier in the proleptic count or one and greater
in the year-of-era count, are part of the 'Before Buddhist' era.

Buddhist years and eras

year-of-era

era

proleptic-year

ISO proleptic-year

2

BE

2

-542

1

BE

1

-543

1

BEFORE_BE

0

-544

2

BEFORE_BE

-1

-545

Do not use

ordinal()

to obtain the numeric representation of

ThaiBuddhistEra

.
Use

getValue()

instead.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ThaiBuddhistEra

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
ThaiBuddhistEra
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ThaiBuddhistEra c : ThaiBuddhistEra.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ThaiBuddhistEra
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
ThaiBuddhistEra
of​(int thaiBuddhistEra)

Obtains an instance of

ThaiBuddhistEra

from an

int

value.

ThaiBuddhistEra

is an enum representing the Thai Buddhist eras of BEFORE_BE/BE.
This factory allows the enum to be obtained from the

int

value.

**Parameters:**
- thaiBuddhistEra

- the era to represent, from 0 to 1

**Returns:**
- the BuddhistEra singleton, never null

**Throws:**
- DateTimeException

- if the era is invalid

---

#### public int getValue()

Gets the numeric era

int

value.

The era BEFORE_BE has the value 0, while the era BE has the value 1.

**Specified by:**
- getValue

in interface

Era

**Returns:**
- the era value, from 0 (BEFORE_BE) to 1 (BE)

---

#### public
String
getDisplayName​(
TextStyle
style,

Locale
locale)

Gets the textual representation of this era.

This returns the textual name used to identify the era,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

**Specified by:**
- getDisplayName

in interface

Era

**Parameters:**
- style

- the style of the text required, not null
- locale

- the locale to use, not null

**Returns:**
- the text value of the era, not null

---

### Additional Sections

#### Enum ThaiBuddhistEra

java.lang.Object

- java.lang.Enum

<

ThaiBuddhistEra

>
- - java.time.chrono.ThaiBuddhistEra

java.lang.Enum

<

ThaiBuddhistEra

>

- java.time.chrono.ThaiBuddhistEra

java.time.chrono.ThaiBuddhistEra

**All Implemented Interfaces:** Serializable

,

Comparable

<

ThaiBuddhistEra

>

,

Era

,

TemporalAccessor

,

TemporalAdjuster

```java
public enum
ThaiBuddhistEra

extends
Enum
<
ThaiBuddhistEra
>
implements
Era
```

An era in the Thai Buddhist calendar system.

The Thai Buddhist calendar system has two eras.
The current era, for years from 1 onwards, is known as the 'Buddhist' era.
All previous years, zero or earlier in the proleptic count or one and greater
in the year-of-era count, are part of the 'Before Buddhist' era.

Buddhist years and eras

year-of-era

era

proleptic-year

ISO proleptic-year

2

BE

2

-542

1

BE

1

-543

1

BEFORE_BE

0

-544

2

BEFORE_BE

-1

-545

Do not use

ordinal()

to obtain the numeric representation of

ThaiBuddhistEra

.
Use

getValue()

instead.

**Implementation Requirements:** This is an immutable and thread-safe enum.
**Since:** 1.8

public enum

ThaiBuddhistEra

extends

Enum

<

ThaiBuddhistEra

>
implements

Era

An era in the Thai Buddhist calendar system.

The Thai Buddhist calendar system has two eras.
The current era, for years from 1 onwards, is known as the 'Buddhist' era.
All previous years, zero or earlier in the proleptic count or one and greater
in the year-of-era count, are part of the 'Before Buddhist' era.

Buddhist years and eras

year-of-era

era

proleptic-year

ISO proleptic-year

2

BE

2

-542

1

BE

1

-543

1

BEFORE_BE

0

-544

2

BEFORE_BE

-1

-545

Do not use

ordinal()

to obtain the numeric representation of

ThaiBuddhistEra

.
Use

getValue()

instead.

The Thai Buddhist calendar system has two eras.
The current era, for years from 1 onwards, is known as the 'Buddhist' era.
All previous years, zero or earlier in the proleptic count or one and greater
in the year-of-era count, are part of the 'Before Buddhist' era.

Buddhist years and eras

year-of-era

era

proleptic-year

ISO proleptic-year

2

BE

2

-542

1

BE

1

-543

1

BEFORE_BE

0

-544

2

BEFORE_BE

-1

-545

Do not use

ordinal()

to obtain the numeric representation of

ThaiBuddhistEra

.
Use

getValue()

instead.

Do not use

ordinal()

to obtain the numeric representation of

ThaiBuddhistEra

.
Use

getValue()

instead.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

BE

The singleton instance for the current era, 'Buddhist Era',
which has the numeric value 1.

BEFORE_BE

The singleton instance for the era before the current one, 'Before Buddhist Era',
which has the numeric value 0.

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

getDisplayName

​(

TextStyle

style,

Locale

locale)

Gets the textual representation of this era.

int

getValue

()

Gets the numeric era

int

value.

static

ThaiBuddhistEra

of

​(int thaiBuddhistEra)

Obtains an instance of

ThaiBuddhistEra

from an

int

value.

static

ThaiBuddhistEra

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ThaiBuddhistEra

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

BE

The singleton instance for the current era, 'Buddhist Era',
which has the numeric value 1.

BEFORE_BE

The singleton instance for the era before the current one, 'Before Buddhist Era',
which has the numeric value 0.

---

#### Enum Constant Summary

The singleton instance for the current era, 'Buddhist Era',
which has the numeric value 1.

The singleton instance for the era before the current one, 'Before Buddhist Era',
which has the numeric value 0.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDisplayName

​(

TextStyle

style,

Locale

locale)

Gets the textual representation of this era.

int

getValue

()

Gets the numeric era

int

value.

static

ThaiBuddhistEra

of

​(int thaiBuddhistEra)

Obtains an instance of

ThaiBuddhistEra

from an

int

value.

static

ThaiBuddhistEra

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ThaiBuddhistEra

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

getLong

,

isSupported

,

query

,

range

---

#### Method Summary

Gets the textual representation of this era.

Gets the numeric era

int

value.

Obtains an instance of

ThaiBuddhistEra

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

- BEFORE_BE

```java
public static final
ThaiBuddhistEra
BEFORE_BE
```

The singleton instance for the era before the current one, 'Before Buddhist Era',
which has the numeric value 0.

- BE

```java
public static final
ThaiBuddhistEra
BE
```

The singleton instance for the current era, 'Buddhist Era',
which has the numeric value 1.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ThaiBuddhistEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ThaiBuddhistEra c : ThaiBuddhistEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ThaiBuddhistEra
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
ThaiBuddhistEra
of​(int thaiBuddhistEra)
```

Obtains an instance of

ThaiBuddhistEra

from an

int

value.

ThaiBuddhistEra

is an enum representing the Thai Buddhist eras of BEFORE_BE/BE.
This factory allows the enum to be obtained from the

int

value.

**Parameters:** thaiBuddhistEra

- the era to represent, from 0 to 1
**Returns:** the BuddhistEra singleton, never null
**Throws:** DateTimeException

- if the era is invalid

- getValue

```java
public int getValue()
```

Gets the numeric era

int

value.

The era BEFORE_BE has the value 0, while the era BE has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, from 0 (BEFORE_BE) to 1 (BE)

- getDisplayName

```java
public
String
getDisplayName​(
TextStyle
style,

Locale
locale)
```

Gets the textual representation of this era.

This returns the textual name used to identify the era,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

**Specified by:** getDisplayName

in interface

Era
**Parameters:** style

- the style of the text required, not null
**Parameters:** locale

- the locale to use, not null
**Returns:** the text value of the era, not null

Enum Constant Detail

- BEFORE_BE

```java
public static final
ThaiBuddhistEra
BEFORE_BE
```

The singleton instance for the era before the current one, 'Before Buddhist Era',
which has the numeric value 0.

- BE

```java
public static final
ThaiBuddhistEra
BE
```

The singleton instance for the current era, 'Buddhist Era',
which has the numeric value 1.

---

#### Enum Constant Detail

BEFORE_BE

```java
public static final
ThaiBuddhistEra
BEFORE_BE
```

The singleton instance for the era before the current one, 'Before Buddhist Era',
which has the numeric value 0.

---

#### BEFORE_BE

public static final

ThaiBuddhistEra

BEFORE_BE

The singleton instance for the era before the current one, 'Before Buddhist Era',
which has the numeric value 0.

BE

```java
public static final
ThaiBuddhistEra
BE
```

The singleton instance for the current era, 'Buddhist Era',
which has the numeric value 1.

---

#### BE

public static final

ThaiBuddhistEra

BE

The singleton instance for the current era, 'Buddhist Era',
which has the numeric value 1.

Method Detail

- values

```java
public static
ThaiBuddhistEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ThaiBuddhistEra c : ThaiBuddhistEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ThaiBuddhistEra
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
ThaiBuddhistEra
of​(int thaiBuddhistEra)
```

Obtains an instance of

ThaiBuddhistEra

from an

int

value.

ThaiBuddhistEra

is an enum representing the Thai Buddhist eras of BEFORE_BE/BE.
This factory allows the enum to be obtained from the

int

value.

**Parameters:** thaiBuddhistEra

- the era to represent, from 0 to 1
**Returns:** the BuddhistEra singleton, never null
**Throws:** DateTimeException

- if the era is invalid

- getValue

```java
public int getValue()
```

Gets the numeric era

int

value.

The era BEFORE_BE has the value 0, while the era BE has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, from 0 (BEFORE_BE) to 1 (BE)

- getDisplayName

```java
public
String
getDisplayName​(
TextStyle
style,

Locale
locale)
```

Gets the textual representation of this era.

This returns the textual name used to identify the era,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

**Specified by:** getDisplayName

in interface

Era
**Parameters:** style

- the style of the text required, not null
**Parameters:** locale

- the locale to use, not null
**Returns:** the text value of the era, not null

---

#### Method Detail

values

```java
public static
ThaiBuddhistEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ThaiBuddhistEra c : ThaiBuddhistEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ThaiBuddhistEra

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ThaiBuddhistEra c : ThaiBuddhistEra.values())
System.out.println(c);
```

for (ThaiBuddhistEra c : ThaiBuddhistEra.values())
System.out.println(c);

valueOf

```java
public static
ThaiBuddhistEra
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

ThaiBuddhistEra

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
ThaiBuddhistEra
of​(int thaiBuddhistEra)
```

Obtains an instance of

ThaiBuddhistEra

from an

int

value.

ThaiBuddhistEra

is an enum representing the Thai Buddhist eras of BEFORE_BE/BE.
This factory allows the enum to be obtained from the

int

value.

**Parameters:** thaiBuddhistEra

- the era to represent, from 0 to 1
**Returns:** the BuddhistEra singleton, never null
**Throws:** DateTimeException

- if the era is invalid

---

#### of

public static

ThaiBuddhistEra

of​(int thaiBuddhistEra)

Obtains an instance of

ThaiBuddhistEra

from an

int

value.

ThaiBuddhistEra

is an enum representing the Thai Buddhist eras of BEFORE_BE/BE.
This factory allows the enum to be obtained from the

int

value.

ThaiBuddhistEra

is an enum representing the Thai Buddhist eras of BEFORE_BE/BE.
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

The era BEFORE_BE has the value 0, while the era BE has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, from 0 (BEFORE_BE) to 1 (BE)

---

#### getValue

public int getValue()

Gets the numeric era

int

value.

The era BEFORE_BE has the value 0, while the era BE has the value 1.

The era BEFORE_BE has the value 0, while the era BE has the value 1.

getDisplayName

```java
public
String
getDisplayName​(
TextStyle
style,

Locale
locale)
```

Gets the textual representation of this era.

This returns the textual name used to identify the era,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

**Specified by:** getDisplayName

in interface

Era
**Parameters:** style

- the style of the text required, not null
**Parameters:** locale

- the locale to use, not null
**Returns:** the text value of the era, not null

---

#### getDisplayName

public

String

getDisplayName​(

TextStyle

style,

Locale

locale)

Gets the textual representation of this era.

This returns the textual name used to identify the era,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

This returns the textual name used to identify the era,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

If no textual mapping is found then the

numeric value

is returned.

---

