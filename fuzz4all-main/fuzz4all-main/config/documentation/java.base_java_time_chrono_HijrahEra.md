# Enum HijrahEra

**Source:** `java.base\java\time\chrono\HijrahEra.html`

### Class Description

```java
public enum
HijrahEra

extends
Enum
<
HijrahEra
>
implements
Era
```

An era in the Hijrah calendar system.

The Hijrah calendar system has only one era covering the
proleptic years greater than zero.

Do not use

ordinal()

to obtain the numeric representation of

HijrahEra

.
Use

getValue()

instead.

**All Implemented Interfaces:** Serializable

,

Comparable

<

HijrahEra

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
HijrahEra
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HijrahEra c : HijrahEra.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
HijrahEra
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
HijrahEra
of​(int hijrahEra)

Obtains an instance of

HijrahEra

from an

int

value.

The current era, which is the only accepted value, has the value 1

**Parameters:**
- hijrahEra

- the era to represent, only 1 supported

**Returns:**
- the HijrahEra.AH singleton, not null

**Throws:**
- DateTimeException

- if the value is invalid

---

#### public int getValue()

Gets the numeric era

int

value.

The era AH has the value 1.

**Specified by:**
- getValue

in interface

Era

**Returns:**
- the era value, 1 (AH)

---

#### public
ValueRange
range​(
TemporalField
field)

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This era is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is a

ChronoField

then the query is implemented here.
The

ERA

field returns the range.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

The

ERA

field returns a range for the one valid Hijrah era.

**Specified by:**
- range

in interface

Era
- range

in interface

TemporalAccessor

**Parameters:**
- field

- the field to query the range for, not null

**Returns:**
- the range of valid values for the field, not null

**Throws:**
- DateTimeException

- if the range for the field cannot be obtained
- UnsupportedTemporalTypeException

- if the unit is not supported

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

#### Enum HijrahEra

java.lang.Object

- java.lang.Enum

<

HijrahEra

>
- - java.time.chrono.HijrahEra

java.lang.Enum

<

HijrahEra

>

- java.time.chrono.HijrahEra

java.time.chrono.HijrahEra

**All Implemented Interfaces:** Serializable

,

Comparable

<

HijrahEra

>

,

Era

,

TemporalAccessor

,

TemporalAdjuster

```java
public enum
HijrahEra

extends
Enum
<
HijrahEra
>
implements
Era
```

An era in the Hijrah calendar system.

The Hijrah calendar system has only one era covering the
proleptic years greater than zero.

Do not use

ordinal()

to obtain the numeric representation of

HijrahEra

.
Use

getValue()

instead.

**Implementation Requirements:** This is an immutable and thread-safe enum.
**Since:** 1.8

public enum

HijrahEra

extends

Enum

<

HijrahEra

>
implements

Era

An era in the Hijrah calendar system.

The Hijrah calendar system has only one era covering the
proleptic years greater than zero.

Do not use

ordinal()

to obtain the numeric representation of

HijrahEra

.
Use

getValue()

instead.

The Hijrah calendar system has only one era covering the
proleptic years greater than zero.

Do not use

ordinal()

to obtain the numeric representation of

HijrahEra

.
Use

getValue()

instead.

Do not use

ordinal()

to obtain the numeric representation of

HijrahEra

.
Use

getValue()

instead.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

AH

The singleton instance for the current era, 'Anno Hegirae',
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

HijrahEra

of

​(int hijrahEra)

Obtains an instance of

HijrahEra

from an

int

value.

ValueRange

range

​(

TemporalField

field)

Gets the range of valid values for the specified field.

static

HijrahEra

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

HijrahEra

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

AH

The singleton instance for the current era, 'Anno Hegirae',
which has the numeric value 1.

---

#### Enum Constant Summary

The singleton instance for the current era, 'Anno Hegirae',
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

HijrahEra

of

​(int hijrahEra)

Obtains an instance of

HijrahEra

from an

int

value.

ValueRange

range

​(

TemporalField

field)

Gets the range of valid values for the specified field.

static

HijrahEra

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

HijrahEra

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

---

#### Method Summary

Gets the textual representation of this era.

Gets the numeric era

int

value.

Obtains an instance of

HijrahEra

from an

int

value.

Gets the range of valid values for the specified field.

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

---

#### Methods declared in interface java.time.chrono. Era

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- AH

```java
public static final
HijrahEra
AH
```

The singleton instance for the current era, 'Anno Hegirae',
which has the numeric value 1.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
HijrahEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HijrahEra c : HijrahEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
HijrahEra
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
HijrahEra
of​(int hijrahEra)
```

Obtains an instance of

HijrahEra

from an

int

value.

The current era, which is the only accepted value, has the value 1

**Parameters:** hijrahEra

- the era to represent, only 1 supported
**Returns:** the HijrahEra.AH singleton, not null
**Throws:** DateTimeException

- if the value is invalid

- getValue

```java
public int getValue()
```

Gets the numeric era

int

value.

The era AH has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, 1 (AH)

- range

```java
public
ValueRange
range​(
TemporalField
field)
```

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This era is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is a

ChronoField

then the query is implemented here.
The

ERA

field returns the range.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

The

ERA

field returns a range for the one valid Hijrah era.

**Specified by:** range

in interface

Era
**Specified by:** range

in interface

TemporalAccessor
**Parameters:** field

- the field to query the range for, not null
**Returns:** the range of valid values for the field, not null
**Throws:** DateTimeException

- if the range for the field cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the unit is not supported

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

- AH

```java
public static final
HijrahEra
AH
```

The singleton instance for the current era, 'Anno Hegirae',
which has the numeric value 1.

---

#### Enum Constant Detail

AH

```java
public static final
HijrahEra
AH
```

The singleton instance for the current era, 'Anno Hegirae',
which has the numeric value 1.

---

#### AH

public static final

HijrahEra

AH

The singleton instance for the current era, 'Anno Hegirae',
which has the numeric value 1.

Method Detail

- values

```java
public static
HijrahEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HijrahEra c : HijrahEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
HijrahEra
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
HijrahEra
of​(int hijrahEra)
```

Obtains an instance of

HijrahEra

from an

int

value.

The current era, which is the only accepted value, has the value 1

**Parameters:** hijrahEra

- the era to represent, only 1 supported
**Returns:** the HijrahEra.AH singleton, not null
**Throws:** DateTimeException

- if the value is invalid

- getValue

```java
public int getValue()
```

Gets the numeric era

int

value.

The era AH has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, 1 (AH)

- range

```java
public
ValueRange
range​(
TemporalField
field)
```

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This era is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is a

ChronoField

then the query is implemented here.
The

ERA

field returns the range.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

The

ERA

field returns a range for the one valid Hijrah era.

**Specified by:** range

in interface

Era
**Specified by:** range

in interface

TemporalAccessor
**Parameters:** field

- the field to query the range for, not null
**Returns:** the range of valid values for the field, not null
**Throws:** DateTimeException

- if the range for the field cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the unit is not supported

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
HijrahEra
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HijrahEra c : HijrahEra.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

HijrahEra

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HijrahEra c : HijrahEra.values())
System.out.println(c);
```

for (HijrahEra c : HijrahEra.values())
System.out.println(c);

valueOf

```java
public static
HijrahEra
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

HijrahEra

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
HijrahEra
of​(int hijrahEra)
```

Obtains an instance of

HijrahEra

from an

int

value.

The current era, which is the only accepted value, has the value 1

**Parameters:** hijrahEra

- the era to represent, only 1 supported
**Returns:** the HijrahEra.AH singleton, not null
**Throws:** DateTimeException

- if the value is invalid

---

#### of

public static

HijrahEra

of​(int hijrahEra)

Obtains an instance of

HijrahEra

from an

int

value.

The current era, which is the only accepted value, has the value 1

The current era, which is the only accepted value, has the value 1

getValue

```java
public int getValue()
```

Gets the numeric era

int

value.

The era AH has the value 1.

**Specified by:** getValue

in interface

Era
**Returns:** the era value, 1 (AH)

---

#### getValue

public int getValue()

Gets the numeric era

int

value.

The era AH has the value 1.

The era AH has the value 1.

range

```java
public
ValueRange
range​(
TemporalField
field)
```

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This era is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is a

ChronoField

then the query is implemented here.
The

ERA

field returns the range.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

The

ERA

field returns a range for the one valid Hijrah era.

**Specified by:** range

in interface

Era
**Specified by:** range

in interface

TemporalAccessor
**Parameters:** field

- the field to query the range for, not null
**Returns:** the range of valid values for the field, not null
**Throws:** DateTimeException

- if the range for the field cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the unit is not supported

---

#### range

public

ValueRange

range​(

TemporalField

field)

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This era is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is a

ChronoField

then the query is implemented here.
The

ERA

field returns the range.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

The

ERA

field returns a range for the one valid Hijrah era.

The range object expresses the minimum and maximum valid values for a field.
This era is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is a

ChronoField

then the query is implemented here.
The

ERA

field returns the range.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

The

ERA

field returns a range for the one valid Hijrah era.

If the field is a

ChronoField

then the query is implemented here.
The

ERA

field returns the range.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

The

ERA

field returns a range for the one valid Hijrah era.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

The

ERA

field returns a range for the one valid Hijrah era.

The

ERA

field returns a range for the one valid Hijrah era.

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

