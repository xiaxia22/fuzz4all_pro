# Enum MinguoEra

**Source:** `java.base\java\time\chrono\MinguoEra.html`

### Class Description

```java
public enum
MinguoEra

extends
Enum
<
MinguoEra
>
implements
Era
```

An era in the Minguo calendar system.

The Minguo calendar system has two eras.
The current era, for years from 1 onwards, is known as the 'Republic of China' era.
All previous years, zero or earlier in the proleptic count or one and greater
in the year-of-era count, are part of the 'Before Republic of China' era.

Minguo years and eras

year-of-era

era

proleptic-year

ISO proleptic-year

2

ROC

2

1913

1

ROC

1

1912

1

BEFORE_ROC

0

1911

2

BEFORE_ROC

-1

1910

Do not use

ordinal()

to obtain the numeric representation of

MinguoEra

.
Use

getValue()

instead.

**All Implemented Interfaces:** Serializable

,

Comparable

<

MinguoEra

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
MinguoEra
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MinguoEra c : MinguoEra.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
MinguoEra
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
MinguoEra
of​(int minguoEra)

Obtains an instance of

MinguoEra

from an

int

value.

MinguoEra

is an enum representing the Minguo eras of BEFORE_ROC/ROC.
This factory allows the enum to be obtained from the

int

value.

**Parameters:**
- minguoEra

- the BEFORE_ROC/ROC value to represent, from 0 (BEFORE_ROC) to 1 (ROC)

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

The era BEFORE_ROC has the value 0, while the era ROC has the value 1.

**Specified by:**
- getValue

in interface

Era

**Returns:**
- the era value, from 0 (BEFORE_ROC) to 1 (ROC)

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

#### Enum MinguoEra

java.lang.Object

- java.lang.Enum

<

MinguoEra

>
- - java.time.chrono.MinguoEra

java.lang.Enum

<

MinguoEra

>

- java.time.chrono.MinguoEra

java.time.chrono.MinguoEra

**All Implemented Interfaces:** Serializable

,

Comparable

<

MinguoEra

>

,

Era

,

TemporalAccessor

,

TemporalAdjuster

```java
public enum
MinguoEra

extends
Enum
<
MinguoEra
>
implements
Era
```

An era in the Minguo calendar system.

The Minguo calendar system has two eras.
The current era, for years from 1 onwards, is known as the 'Republic of China' era.
All previous years, zero or earlier in the proleptic count or one and greater
in the year-of-era count, are part of the 'Before Republic of China' era.

Minguo years and eras

year-of-era

era

proleptic-year

ISO proleptic-year

2

ROC

2

1913

1

ROC

1

1912

1

BEFORE_ROC

0

1911

2

BEFORE_ROC

-1

1910

Do not use

ordinal()

to obtain the numeric representation of

MinguoEra

.
Use

getValue()

instead.

**Implementation Requirements:** This is an immutable and thread-safe enum.
**Since:** 1.8

public enum

MinguoEra

extends

Enum

<

MinguoEra

>
implements

Era

An era in the Minguo calendar system.

The Minguo calendar system has two eras.
The current era, for years from 1 onwards, is known as the 'Republic of China' era.
All previous years, zero or earlier in the proleptic count or one and greater
in the year-of-era count, are part of the 'Before Republic of China' era.

Minguo years and eras

year-of-era

era

proleptic-year

ISO proleptic-year

2

ROC

2

1913

1

ROC

1

1912

1

BEFORE_ROC

0

1911

2

BEFORE_ROC

-1

1910

Do not use

ordinal()

to obtain the numeric representation of

MinguoEra

.
Use

getValue()

instead.

The Minguo calendar system has two eras.
The current era, for years from 1 onwards, is known as the 'Republic of China' era.
All previous years, zero or earlier in the proleptic count or one and greater
in the year-of-era count, are part of the 'Before Republic of China' era.

Minguo years and eras

year-of-era

era

proleptic-year

ISO proleptic-year

2

ROC

2

1913

1

ROC

1

1912

1

BEFORE_ROC

0

1911

2

BEFORE_ROC

-1

1910

Do not use

ordinal()

to obtain the numeric representation of

MinguoEra

.
Use

getValue()

instead.

Do not use

ordinal()

to obtain the numeric representation of

MinguoEra

.
Use

getValue()

instead.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

BEFORE_ROC

The singleton instance for the era before the current one, 'Before Republic of China Era',
which has the numeric value 0.

ROC

The singleton instance for the current era, 'Republic of China Era',
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

MinguoEra

of

​(int minguoEra)

Obtains an instance of

MinguoEra

from an

int

value.

static

MinguoEra

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MinguoEra

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

BEFORE_ROC

The singleton instance for the era before the current one, 'Before Republic of China Era',
which has the numeric value 0.

ROC

The singleton instance for the current era, 'Republic of China Era',
which has the numeric value 1.

---

#### Enum Constant Summary

The singleton instance for the era before the current one, 'Before Republic of China Era',
which has the numeric value 0.

The singleton instance for the current era, 'Republic of China Era',
which has the numeric value 1.

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

MinguoEra

of

​(int minguoEra)

Obtains an instance of

MinguoEra

from an

int

value.

static

MinguoEra

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MinguoEra

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

MinguoEra

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

- BEFORE_ROC

```java
public static final
MinguoEra
BEFORE_ROC
```

The singleton instance for the era before the current one, 'Before Republic of China Era',
which has the numeric value 0.

- ROC

```java
public static final
MinguoEra
ROC
```

The singleton instance for the current era, 'Republic of China Era',
which has the numeric value 1.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
MinguoEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MinguoEra c : MinguoEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MinguoEra
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
MinguoEra
of​(int minguoEra)
```

Obtains an instance of

MinguoEra

from an

int

value.

MinguoEra

is an enum representing the Minguo eras of BEFORE_ROC/ROC.
This factory allows the enum to be obtained from the

int

value.

**Parameters:** minguoEra

- the BEFORE_ROC/ROC value to represent, from 0 (BEFORE_ROC) to 1 (ROC)
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

The era BEFORE_ROC has the value 0, while the era ROC has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, from 0 (BEFORE_ROC) to 1 (ROC)

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

- BEFORE_ROC

```java
public static final
MinguoEra
BEFORE_ROC
```

The singleton instance for the era before the current one, 'Before Republic of China Era',
which has the numeric value 0.

- ROC

```java
public static final
MinguoEra
ROC
```

The singleton instance for the current era, 'Republic of China Era',
which has the numeric value 1.

---

#### Enum Constant Detail

BEFORE_ROC

```java
public static final
MinguoEra
BEFORE_ROC
```

The singleton instance for the era before the current one, 'Before Republic of China Era',
which has the numeric value 0.

---

#### BEFORE_ROC

public static final

MinguoEra

BEFORE_ROC

The singleton instance for the era before the current one, 'Before Republic of China Era',
which has the numeric value 0.

ROC

```java
public static final
MinguoEra
ROC
```

The singleton instance for the current era, 'Republic of China Era',
which has the numeric value 1.

---

#### ROC

public static final

MinguoEra

ROC

The singleton instance for the current era, 'Republic of China Era',
which has the numeric value 1.

Method Detail

- values

```java
public static
MinguoEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MinguoEra c : MinguoEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MinguoEra
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
MinguoEra
of​(int minguoEra)
```

Obtains an instance of

MinguoEra

from an

int

value.

MinguoEra

is an enum representing the Minguo eras of BEFORE_ROC/ROC.
This factory allows the enum to be obtained from the

int

value.

**Parameters:** minguoEra

- the BEFORE_ROC/ROC value to represent, from 0 (BEFORE_ROC) to 1 (ROC)
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

The era BEFORE_ROC has the value 0, while the era ROC has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, from 0 (BEFORE_ROC) to 1 (ROC)

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
MinguoEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MinguoEra c : MinguoEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

MinguoEra

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MinguoEra c : MinguoEra.values())
System.out.println(c);
```

for (MinguoEra c : MinguoEra.values())
System.out.println(c);

valueOf

```java
public static
MinguoEra
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

MinguoEra

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
MinguoEra
of​(int minguoEra)
```

Obtains an instance of

MinguoEra

from an

int

value.

MinguoEra

is an enum representing the Minguo eras of BEFORE_ROC/ROC.
This factory allows the enum to be obtained from the

int

value.

**Parameters:** minguoEra

- the BEFORE_ROC/ROC value to represent, from 0 (BEFORE_ROC) to 1 (ROC)
**Returns:** the era singleton, not null
**Throws:** DateTimeException

- if the value is invalid

---

#### of

public static

MinguoEra

of​(int minguoEra)

Obtains an instance of

MinguoEra

from an

int

value.

MinguoEra

is an enum representing the Minguo eras of BEFORE_ROC/ROC.
This factory allows the enum to be obtained from the

int

value.

MinguoEra

is an enum representing the Minguo eras of BEFORE_ROC/ROC.
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

The era BEFORE_ROC has the value 0, while the era ROC has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, from 0 (BEFORE_ROC) to 1 (ROC)

---

#### getValue

public int getValue()

Gets the numeric era

int

value.

The era BEFORE_ROC has the value 0, while the era ROC has the value 1.

The era BEFORE_ROC has the value 0, while the era ROC has the value 1.

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

