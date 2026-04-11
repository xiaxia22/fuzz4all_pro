# Enum ResolverStyle

**Source:** `java.base\java\time\format\ResolverStyle.html`

### Class Description

```java
public enum
ResolverStyle

extends
Enum
<
ResolverStyle
>
```

Enumeration of different ways to resolve dates and times.

Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
This style is used to control how phase 2, resolving, happens.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ResolverStyle

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ResolverStyle
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ResolverStyle c : ResolverStyle.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ResolverStyle
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

#### Enum ResolverStyle

java.lang.Object

- java.lang.Enum

<

ResolverStyle

>
- - java.time.format.ResolverStyle

java.lang.Enum

<

ResolverStyle

>

- java.time.format.ResolverStyle

java.time.format.ResolverStyle

**All Implemented Interfaces:** Serializable

,

Comparable

<

ResolverStyle

>

```java
public enum
ResolverStyle

extends
Enum
<
ResolverStyle
>
```

Enumeration of different ways to resolve dates and times.

Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
This style is used to control how phase 2, resolving, happens.

**Implementation Requirements:** This is an immutable and thread-safe enum.
**Since:** 1.8

public enum

ResolverStyle

extends

Enum

<

ResolverStyle

>

Enumeration of different ways to resolve dates and times.

Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
This style is used to control how phase 2, resolving, happens.

Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
This style is used to control how phase 2, resolving, happens.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

LENIENT

Style to resolve dates and times leniently.

SMART

Style to resolve dates and times in a smart, or intelligent, manner.

STRICT

Style to resolve dates and times strictly.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ResolverStyle

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ResolverStyle

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

LENIENT

Style to resolve dates and times leniently.

SMART

Style to resolve dates and times in a smart, or intelligent, manner.

STRICT

Style to resolve dates and times strictly.

---

#### Enum Constant Summary

Style to resolve dates and times leniently.

Style to resolve dates and times in a smart, or intelligent, manner.

Style to resolve dates and times strictly.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ResolverStyle

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ResolverStyle

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

- STRICT

```java
public static final
ResolverStyle
STRICT
```

Style to resolve dates and times strictly.

Using strict resolution will ensure that all parsed values are within
the outer range of valid values for the field. Individual fields may
be further processed for strictness.

For example, resolving year-month and day-of-month in the ISO calendar
system using strict mode will ensure that the day-of-month is valid
for the year-month, rejecting invalid values.

- SMART

```java
public static final
ResolverStyle
SMART
```

Style to resolve dates and times in a smart, or intelligent, manner.

Using smart resolution will perform the sensible default for each
field, which may be the same as strict, the same as lenient, or a third
behavior. Individual fields will interpret this differently.

For example, resolving year-month and day-of-month in the ISO calendar
system using smart mode will ensure that the day-of-month is from
1 to 31, converting any value beyond the last valid day-of-month to be
the last valid day-of-month.

- LENIENT

```java
public static final
ResolverStyle
LENIENT
```

Style to resolve dates and times leniently.

Using lenient resolution will resolve the values in an appropriate
lenient manner. Individual fields will interpret this differently.

For example, lenient mode allows the month in the ISO calendar system
to be outside the range 1 to 12.
For example, month 15 is treated as being 3 months after month 12.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ResolverStyle
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ResolverStyle c : ResolverStyle.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ResolverStyle
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

- STRICT

```java
public static final
ResolverStyle
STRICT
```

Style to resolve dates and times strictly.

Using strict resolution will ensure that all parsed values are within
the outer range of valid values for the field. Individual fields may
be further processed for strictness.

For example, resolving year-month and day-of-month in the ISO calendar
system using strict mode will ensure that the day-of-month is valid
for the year-month, rejecting invalid values.

- SMART

```java
public static final
ResolverStyle
SMART
```

Style to resolve dates and times in a smart, or intelligent, manner.

Using smart resolution will perform the sensible default for each
field, which may be the same as strict, the same as lenient, or a third
behavior. Individual fields will interpret this differently.

For example, resolving year-month and day-of-month in the ISO calendar
system using smart mode will ensure that the day-of-month is from
1 to 31, converting any value beyond the last valid day-of-month to be
the last valid day-of-month.

- LENIENT

```java
public static final
ResolverStyle
LENIENT
```

Style to resolve dates and times leniently.

Using lenient resolution will resolve the values in an appropriate
lenient manner. Individual fields will interpret this differently.

For example, lenient mode allows the month in the ISO calendar system
to be outside the range 1 to 12.
For example, month 15 is treated as being 3 months after month 12.

---

#### Enum Constant Detail

STRICT

```java
public static final
ResolverStyle
STRICT
```

Style to resolve dates and times strictly.

Using strict resolution will ensure that all parsed values are within
the outer range of valid values for the field. Individual fields may
be further processed for strictness.

For example, resolving year-month and day-of-month in the ISO calendar
system using strict mode will ensure that the day-of-month is valid
for the year-month, rejecting invalid values.

---

#### STRICT

public static final

ResolverStyle

STRICT

Style to resolve dates and times strictly.

Using strict resolution will ensure that all parsed values are within
the outer range of valid values for the field. Individual fields may
be further processed for strictness.

For example, resolving year-month and day-of-month in the ISO calendar
system using strict mode will ensure that the day-of-month is valid
for the year-month, rejecting invalid values.

Using strict resolution will ensure that all parsed values are within
the outer range of valid values for the field. Individual fields may
be further processed for strictness.

For example, resolving year-month and day-of-month in the ISO calendar
system using strict mode will ensure that the day-of-month is valid
for the year-month, rejecting invalid values.

For example, resolving year-month and day-of-month in the ISO calendar
system using strict mode will ensure that the day-of-month is valid
for the year-month, rejecting invalid values.

SMART

```java
public static final
ResolverStyle
SMART
```

Style to resolve dates and times in a smart, or intelligent, manner.

Using smart resolution will perform the sensible default for each
field, which may be the same as strict, the same as lenient, or a third
behavior. Individual fields will interpret this differently.

For example, resolving year-month and day-of-month in the ISO calendar
system using smart mode will ensure that the day-of-month is from
1 to 31, converting any value beyond the last valid day-of-month to be
the last valid day-of-month.

---

#### SMART

public static final

ResolverStyle

SMART

Style to resolve dates and times in a smart, or intelligent, manner.

Using smart resolution will perform the sensible default for each
field, which may be the same as strict, the same as lenient, or a third
behavior. Individual fields will interpret this differently.

For example, resolving year-month and day-of-month in the ISO calendar
system using smart mode will ensure that the day-of-month is from
1 to 31, converting any value beyond the last valid day-of-month to be
the last valid day-of-month.

Using smart resolution will perform the sensible default for each
field, which may be the same as strict, the same as lenient, or a third
behavior. Individual fields will interpret this differently.

For example, resolving year-month and day-of-month in the ISO calendar
system using smart mode will ensure that the day-of-month is from
1 to 31, converting any value beyond the last valid day-of-month to be
the last valid day-of-month.

For example, resolving year-month and day-of-month in the ISO calendar
system using smart mode will ensure that the day-of-month is from
1 to 31, converting any value beyond the last valid day-of-month to be
the last valid day-of-month.

LENIENT

```java
public static final
ResolverStyle
LENIENT
```

Style to resolve dates and times leniently.

Using lenient resolution will resolve the values in an appropriate
lenient manner. Individual fields will interpret this differently.

For example, lenient mode allows the month in the ISO calendar system
to be outside the range 1 to 12.
For example, month 15 is treated as being 3 months after month 12.

---

#### LENIENT

public static final

ResolverStyle

LENIENT

Style to resolve dates and times leniently.

Using lenient resolution will resolve the values in an appropriate
lenient manner. Individual fields will interpret this differently.

For example, lenient mode allows the month in the ISO calendar system
to be outside the range 1 to 12.
For example, month 15 is treated as being 3 months after month 12.

Using lenient resolution will resolve the values in an appropriate
lenient manner. Individual fields will interpret this differently.

For example, lenient mode allows the month in the ISO calendar system
to be outside the range 1 to 12.
For example, month 15 is treated as being 3 months after month 12.

For example, lenient mode allows the month in the ISO calendar system
to be outside the range 1 to 12.
For example, month 15 is treated as being 3 months after month 12.

Method Detail

- values

```java
public static
ResolverStyle
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ResolverStyle c : ResolverStyle.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ResolverStyle
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
ResolverStyle
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ResolverStyle c : ResolverStyle.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ResolverStyle

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ResolverStyle c : ResolverStyle.values())
System.out.println(c);
```

for (ResolverStyle c : ResolverStyle.values())
System.out.println(c);

valueOf

```java
public static
ResolverStyle
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

ResolverStyle

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

