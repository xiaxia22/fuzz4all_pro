# Enum ChronoUnit

**Source:** `java.base\java\time\temporal\ChronoUnit.html`

### Class Description

```java
public enum
ChronoUnit

extends
Enum
<
ChronoUnit
>
implements
TemporalUnit
```

A standard set of date periods units.

This set of units provide unit-based access to manipulate a date, time or date-time.
The standard set of units can be extended by implementing

TemporalUnit

.

These units are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define units of years, months and days,
just with slightly different rules.
The documentation of each unit explains how it operates.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ChronoUnit

>

,

TemporalUnit

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ChronoUnit
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoUnit c : ChronoUnit.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ChronoUnit
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
Duration
getDuration()

Gets the estimated duration of this unit in the ISO calendar system.

All of the units in this class have an estimated duration.
Days vary due to daylight saving time, while months have different lengths.

**Specified by:**
- getDuration

in interface

TemporalUnit

**Returns:**
- the estimated duration of this unit, not null

---

#### public boolean isDurationEstimated()

Checks if the duration of the unit is an estimate.

All time units in this class are considered to be accurate, while all date
units in this class are considered to be estimated.

This definition ignores leap seconds, but considers that Days vary due to
daylight saving time and months have different lengths.

**Specified by:**
- isDurationEstimated

in interface

TemporalUnit

**Returns:**
- true if the duration is estimated, false if accurate

---

#### public boolean isDateBased()

Checks if this unit is a date unit.

All units from days to eras inclusive are date-based.
Time-based units and

FOREVER

return false.

**Specified by:**
- isDateBased

in interface

TemporalUnit

**Returns:**
- true if a date unit, false if a time unit

---

#### public boolean isTimeBased()

Checks if this unit is a time unit.

All units from nanos to half-days inclusive are time-based.
Date-based units and

FOREVER

return false.

**Specified by:**
- isTimeBased

in interface

TemporalUnit

**Returns:**
- true if a time unit, false if a date unit

---

### Additional Sections

#### Enum ChronoUnit

java.lang.Object

- java.lang.Enum

<

ChronoUnit

>
- - java.time.temporal.ChronoUnit

java.lang.Enum

<

ChronoUnit

>

- java.time.temporal.ChronoUnit

java.time.temporal.ChronoUnit

**All Implemented Interfaces:** Serializable

,

Comparable

<

ChronoUnit

>

,

TemporalUnit

```java
public enum
ChronoUnit

extends
Enum
<
ChronoUnit
>
implements
TemporalUnit
```

A standard set of date periods units.

This set of units provide unit-based access to manipulate a date, time or date-time.
The standard set of units can be extended by implementing

TemporalUnit

.

These units are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define units of years, months and days,
just with slightly different rules.
The documentation of each unit explains how it operates.

**Implementation Requirements:** This is a final, immutable and thread-safe enum.
**Since:** 1.8

public enum

ChronoUnit

extends

Enum

<

ChronoUnit

>
implements

TemporalUnit

A standard set of date periods units.

This set of units provide unit-based access to manipulate a date, time or date-time.
The standard set of units can be extended by implementing

TemporalUnit

.

These units are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define units of years, months and days,
just with slightly different rules.
The documentation of each unit explains how it operates.

This set of units provide unit-based access to manipulate a date, time or date-time.
The standard set of units can be extended by implementing

TemporalUnit

.

These units are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define units of years, months and days,
just with slightly different rules.
The documentation of each unit explains how it operates.

These units are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define units of years, months and days,
just with slightly different rules.
The documentation of each unit explains how it operates.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CENTURIES

Unit that represents the concept of a century.

DAYS

Unit that represents the concept of a day.

DECADES

Unit that represents the concept of a decade.

ERAS

Unit that represents the concept of an era.

FOREVER

Artificial unit that represents the concept of forever.

HALF_DAYS

Unit that represents the concept of half a day, as used in AM/PM.

HOURS

Unit that represents the concept of an hour.

MICROS

Unit that represents the concept of a microsecond.

MILLENNIA

Unit that represents the concept of a millennium.

MILLIS

Unit that represents the concept of a millisecond.

MINUTES

Unit that represents the concept of a minute.

MONTHS

Unit that represents the concept of a month.

NANOS

Unit that represents the concept of a nanosecond, the smallest supported unit of time.

SECONDS

Unit that represents the concept of a second.

WEEKS

Unit that represents the concept of a week.

YEARS

Unit that represents the concept of a year.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Duration

getDuration

()

Gets the estimated duration of this unit in the ISO calendar system.

boolean

isDateBased

()

Checks if this unit is a date unit.

boolean

isDurationEstimated

()

Checks if the duration of the unit is an estimate.

boolean

isTimeBased

()

Checks if this unit is a time unit.

static

ChronoUnit

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ChronoUnit

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

- Methods declared in interface java.time.temporal.

TemporalUnit

addTo

,

between

,

isSupportedBy

,

toString

Enum Constant Summary

Enum Constants

Enum Constant

Description

CENTURIES

Unit that represents the concept of a century.

DAYS

Unit that represents the concept of a day.

DECADES

Unit that represents the concept of a decade.

ERAS

Unit that represents the concept of an era.

FOREVER

Artificial unit that represents the concept of forever.

HALF_DAYS

Unit that represents the concept of half a day, as used in AM/PM.

HOURS

Unit that represents the concept of an hour.

MICROS

Unit that represents the concept of a microsecond.

MILLENNIA

Unit that represents the concept of a millennium.

MILLIS

Unit that represents the concept of a millisecond.

MINUTES

Unit that represents the concept of a minute.

MONTHS

Unit that represents the concept of a month.

NANOS

Unit that represents the concept of a nanosecond, the smallest supported unit of time.

SECONDS

Unit that represents the concept of a second.

WEEKS

Unit that represents the concept of a week.

YEARS

Unit that represents the concept of a year.

---

#### Enum Constant Summary

Unit that represents the concept of a century.

Unit that represents the concept of a day.

Unit that represents the concept of a decade.

Unit that represents the concept of an era.

Artificial unit that represents the concept of forever.

Unit that represents the concept of half a day, as used in AM/PM.

Unit that represents the concept of an hour.

Unit that represents the concept of a microsecond.

Unit that represents the concept of a millennium.

Unit that represents the concept of a millisecond.

Unit that represents the concept of a minute.

Unit that represents the concept of a month.

Unit that represents the concept of a nanosecond, the smallest supported unit of time.

Unit that represents the concept of a second.

Unit that represents the concept of a week.

Unit that represents the concept of a year.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Duration

getDuration

()

Gets the estimated duration of this unit in the ISO calendar system.

boolean

isDateBased

()

Checks if this unit is a date unit.

boolean

isDurationEstimated

()

Checks if the duration of the unit is an estimate.

boolean

isTimeBased

()

Checks if this unit is a time unit.

static

ChronoUnit

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ChronoUnit

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

- Methods declared in interface java.time.temporal.

TemporalUnit

addTo

,

between

,

isSupportedBy

,

toString

---

#### Method Summary

Gets the estimated duration of this unit in the ISO calendar system.

Checks if this unit is a date unit.

Checks if the duration of the unit is an estimate.

Checks if this unit is a time unit.

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

Methods declared in interface java.time.temporal.

TemporalUnit

addTo

,

between

,

isSupportedBy

,

toString

---

#### Methods declared in interface java.time.temporal. TemporalUnit

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- NANOS

```java
public static final
ChronoUnit
NANOS
```

Unit that represents the concept of a nanosecond, the smallest supported unit of time.
For the ISO calendar system, it is equal to the 1,000,000,000th part of the second unit.

- MICROS

```java
public static final
ChronoUnit
MICROS
```

Unit that represents the concept of a microsecond.
For the ISO calendar system, it is equal to the 1,000,000th part of the second unit.

- MILLIS

```java
public static final
ChronoUnit
MILLIS
```

Unit that represents the concept of a millisecond.
For the ISO calendar system, it is equal to the 1000th part of the second unit.

- SECONDS

```java
public static final
ChronoUnit
SECONDS
```

Unit that represents the concept of a second.
For the ISO calendar system, it is equal to the second in the SI system
of units, except around a leap-second.

- MINUTES

```java
public static final
ChronoUnit
MINUTES
```

Unit that represents the concept of a minute.
For the ISO calendar system, it is equal to 60 seconds.

- HOURS

```java
public static final
ChronoUnit
HOURS
```

Unit that represents the concept of an hour.
For the ISO calendar system, it is equal to 60 minutes.

- HALF_DAYS

```java
public static final
ChronoUnit
HALF_DAYS
```

Unit that represents the concept of half a day, as used in AM/PM.
For the ISO calendar system, it is equal to 12 hours.

- DAYS

```java
public static final
ChronoUnit
DAYS
```

Unit that represents the concept of a day.
For the ISO calendar system, it is the standard day from midnight to midnight.
The estimated duration of a day is

24 Hours

.

When used with other calendar systems it must correspond to the day defined by
the rising and setting of the Sun on Earth. It is not required that days begin
at midnight - when converting between calendar systems, the date should be
equivalent at midday.

- WEEKS

```java
public static final
ChronoUnit
WEEKS
```

Unit that represents the concept of a week.
For the ISO calendar system, it is equal to 7 days.

When used with other calendar systems it must correspond to an integral number of days.

- MONTHS

```java
public static final
ChronoUnit
MONTHS
```

Unit that represents the concept of a month.
For the ISO calendar system, the length of the month varies by month-of-year.
The estimated duration of a month is one twelfth of

365.2425 Days

.

When used with other calendar systems it must correspond to an integral number of days.

- YEARS

```java
public static final
ChronoUnit
YEARS
```

Unit that represents the concept of a year.
For the ISO calendar system, it is equal to 12 months.
The estimated duration of a year is

365.2425 Days

.

When used with other calendar systems it must correspond to an integral number of days
or months roughly equal to a year defined by the passage of the Earth around the Sun.

- DECADES

```java
public static final
ChronoUnit
DECADES
```

Unit that represents the concept of a decade.
For the ISO calendar system, it is equal to 10 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

- CENTURIES

```java
public static final
ChronoUnit
CENTURIES
```

Unit that represents the concept of a century.
For the ISO calendar system, it is equal to 100 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

- MILLENNIA

```java
public static final
ChronoUnit
MILLENNIA
```

Unit that represents the concept of a millennium.
For the ISO calendar system, it is equal to 1000 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

- ERAS

```java
public static final
ChronoUnit
ERAS
```

Unit that represents the concept of an era.
The ISO calendar system doesn't have eras thus it is impossible to add
an era to a date or date-time.
The estimated duration of the era is artificially defined as

1,000,000,000 Years

.

When used with other calendar systems there are no restrictions on the unit.

- FOREVER

```java
public static final
ChronoUnit
FOREVER
```

Artificial unit that represents the concept of forever.
This is primarily used with

TemporalField

to represent unbounded fields
such as the year or era.
The estimated duration of this unit is artificially defined as the largest duration
supported by

Duration

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ChronoUnit
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoUnit c : ChronoUnit.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ChronoUnit
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

- getDuration

```java
public
Duration
getDuration()
```

Gets the estimated duration of this unit in the ISO calendar system.

All of the units in this class have an estimated duration.
Days vary due to daylight saving time, while months have different lengths.

**Specified by:** getDuration

in interface

TemporalUnit
**Returns:** the estimated duration of this unit, not null

- isDurationEstimated

```java
public boolean isDurationEstimated()
```

Checks if the duration of the unit is an estimate.

All time units in this class are considered to be accurate, while all date
units in this class are considered to be estimated.

This definition ignores leap seconds, but considers that Days vary due to
daylight saving time and months have different lengths.

**Specified by:** isDurationEstimated

in interface

TemporalUnit
**Returns:** true if the duration is estimated, false if accurate

- isDateBased

```java
public boolean isDateBased()
```

Checks if this unit is a date unit.

All units from days to eras inclusive are date-based.
Time-based units and

FOREVER

return false.

**Specified by:** isDateBased

in interface

TemporalUnit
**Returns:** true if a date unit, false if a time unit

- isTimeBased

```java
public boolean isTimeBased()
```

Checks if this unit is a time unit.

All units from nanos to half-days inclusive are time-based.
Date-based units and

FOREVER

return false.

**Specified by:** isTimeBased

in interface

TemporalUnit
**Returns:** true if a time unit, false if a date unit

Enum Constant Detail

- NANOS

```java
public static final
ChronoUnit
NANOS
```

Unit that represents the concept of a nanosecond, the smallest supported unit of time.
For the ISO calendar system, it is equal to the 1,000,000,000th part of the second unit.

- MICROS

```java
public static final
ChronoUnit
MICROS
```

Unit that represents the concept of a microsecond.
For the ISO calendar system, it is equal to the 1,000,000th part of the second unit.

- MILLIS

```java
public static final
ChronoUnit
MILLIS
```

Unit that represents the concept of a millisecond.
For the ISO calendar system, it is equal to the 1000th part of the second unit.

- SECONDS

```java
public static final
ChronoUnit
SECONDS
```

Unit that represents the concept of a second.
For the ISO calendar system, it is equal to the second in the SI system
of units, except around a leap-second.

- MINUTES

```java
public static final
ChronoUnit
MINUTES
```

Unit that represents the concept of a minute.
For the ISO calendar system, it is equal to 60 seconds.

- HOURS

```java
public static final
ChronoUnit
HOURS
```

Unit that represents the concept of an hour.
For the ISO calendar system, it is equal to 60 minutes.

- HALF_DAYS

```java
public static final
ChronoUnit
HALF_DAYS
```

Unit that represents the concept of half a day, as used in AM/PM.
For the ISO calendar system, it is equal to 12 hours.

- DAYS

```java
public static final
ChronoUnit
DAYS
```

Unit that represents the concept of a day.
For the ISO calendar system, it is the standard day from midnight to midnight.
The estimated duration of a day is

24 Hours

.

When used with other calendar systems it must correspond to the day defined by
the rising and setting of the Sun on Earth. It is not required that days begin
at midnight - when converting between calendar systems, the date should be
equivalent at midday.

- WEEKS

```java
public static final
ChronoUnit
WEEKS
```

Unit that represents the concept of a week.
For the ISO calendar system, it is equal to 7 days.

When used with other calendar systems it must correspond to an integral number of days.

- MONTHS

```java
public static final
ChronoUnit
MONTHS
```

Unit that represents the concept of a month.
For the ISO calendar system, the length of the month varies by month-of-year.
The estimated duration of a month is one twelfth of

365.2425 Days

.

When used with other calendar systems it must correspond to an integral number of days.

- YEARS

```java
public static final
ChronoUnit
YEARS
```

Unit that represents the concept of a year.
For the ISO calendar system, it is equal to 12 months.
The estimated duration of a year is

365.2425 Days

.

When used with other calendar systems it must correspond to an integral number of days
or months roughly equal to a year defined by the passage of the Earth around the Sun.

- DECADES

```java
public static final
ChronoUnit
DECADES
```

Unit that represents the concept of a decade.
For the ISO calendar system, it is equal to 10 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

- CENTURIES

```java
public static final
ChronoUnit
CENTURIES
```

Unit that represents the concept of a century.
For the ISO calendar system, it is equal to 100 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

- MILLENNIA

```java
public static final
ChronoUnit
MILLENNIA
```

Unit that represents the concept of a millennium.
For the ISO calendar system, it is equal to 1000 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

- ERAS

```java
public static final
ChronoUnit
ERAS
```

Unit that represents the concept of an era.
The ISO calendar system doesn't have eras thus it is impossible to add
an era to a date or date-time.
The estimated duration of the era is artificially defined as

1,000,000,000 Years

.

When used with other calendar systems there are no restrictions on the unit.

- FOREVER

```java
public static final
ChronoUnit
FOREVER
```

Artificial unit that represents the concept of forever.
This is primarily used with

TemporalField

to represent unbounded fields
such as the year or era.
The estimated duration of this unit is artificially defined as the largest duration
supported by

Duration

.

---

#### Enum Constant Detail

NANOS

```java
public static final
ChronoUnit
NANOS
```

Unit that represents the concept of a nanosecond, the smallest supported unit of time.
For the ISO calendar system, it is equal to the 1,000,000,000th part of the second unit.

---

#### NANOS

public static final

ChronoUnit

NANOS

Unit that represents the concept of a nanosecond, the smallest supported unit of time.
For the ISO calendar system, it is equal to the 1,000,000,000th part of the second unit.

MICROS

```java
public static final
ChronoUnit
MICROS
```

Unit that represents the concept of a microsecond.
For the ISO calendar system, it is equal to the 1,000,000th part of the second unit.

---

#### MICROS

public static final

ChronoUnit

MICROS

Unit that represents the concept of a microsecond.
For the ISO calendar system, it is equal to the 1,000,000th part of the second unit.

MILLIS

```java
public static final
ChronoUnit
MILLIS
```

Unit that represents the concept of a millisecond.
For the ISO calendar system, it is equal to the 1000th part of the second unit.

---

#### MILLIS

public static final

ChronoUnit

MILLIS

Unit that represents the concept of a millisecond.
For the ISO calendar system, it is equal to the 1000th part of the second unit.

SECONDS

```java
public static final
ChronoUnit
SECONDS
```

Unit that represents the concept of a second.
For the ISO calendar system, it is equal to the second in the SI system
of units, except around a leap-second.

---

#### SECONDS

public static final

ChronoUnit

SECONDS

Unit that represents the concept of a second.
For the ISO calendar system, it is equal to the second in the SI system
of units, except around a leap-second.

MINUTES

```java
public static final
ChronoUnit
MINUTES
```

Unit that represents the concept of a minute.
For the ISO calendar system, it is equal to 60 seconds.

---

#### MINUTES

public static final

ChronoUnit

MINUTES

Unit that represents the concept of a minute.
For the ISO calendar system, it is equal to 60 seconds.

HOURS

```java
public static final
ChronoUnit
HOURS
```

Unit that represents the concept of an hour.
For the ISO calendar system, it is equal to 60 minutes.

---

#### HOURS

public static final

ChronoUnit

HOURS

Unit that represents the concept of an hour.
For the ISO calendar system, it is equal to 60 minutes.

HALF_DAYS

```java
public static final
ChronoUnit
HALF_DAYS
```

Unit that represents the concept of half a day, as used in AM/PM.
For the ISO calendar system, it is equal to 12 hours.

---

#### HALF_DAYS

public static final

ChronoUnit

HALF_DAYS

Unit that represents the concept of half a day, as used in AM/PM.
For the ISO calendar system, it is equal to 12 hours.

DAYS

```java
public static final
ChronoUnit
DAYS
```

Unit that represents the concept of a day.
For the ISO calendar system, it is the standard day from midnight to midnight.
The estimated duration of a day is

24 Hours

.

When used with other calendar systems it must correspond to the day defined by
the rising and setting of the Sun on Earth. It is not required that days begin
at midnight - when converting between calendar systems, the date should be
equivalent at midday.

---

#### DAYS

public static final

ChronoUnit

DAYS

Unit that represents the concept of a day.
For the ISO calendar system, it is the standard day from midnight to midnight.
The estimated duration of a day is

24 Hours

.

When used with other calendar systems it must correspond to the day defined by
the rising and setting of the Sun on Earth. It is not required that days begin
at midnight - when converting between calendar systems, the date should be
equivalent at midday.

When used with other calendar systems it must correspond to the day defined by
the rising and setting of the Sun on Earth. It is not required that days begin
at midnight - when converting between calendar systems, the date should be
equivalent at midday.

WEEKS

```java
public static final
ChronoUnit
WEEKS
```

Unit that represents the concept of a week.
For the ISO calendar system, it is equal to 7 days.

When used with other calendar systems it must correspond to an integral number of days.

---

#### WEEKS

public static final

ChronoUnit

WEEKS

Unit that represents the concept of a week.
For the ISO calendar system, it is equal to 7 days.

When used with other calendar systems it must correspond to an integral number of days.

When used with other calendar systems it must correspond to an integral number of days.

MONTHS

```java
public static final
ChronoUnit
MONTHS
```

Unit that represents the concept of a month.
For the ISO calendar system, the length of the month varies by month-of-year.
The estimated duration of a month is one twelfth of

365.2425 Days

.

When used with other calendar systems it must correspond to an integral number of days.

---

#### MONTHS

public static final

ChronoUnit

MONTHS

Unit that represents the concept of a month.
For the ISO calendar system, the length of the month varies by month-of-year.
The estimated duration of a month is one twelfth of

365.2425 Days

.

When used with other calendar systems it must correspond to an integral number of days.

When used with other calendar systems it must correspond to an integral number of days.

YEARS

```java
public static final
ChronoUnit
YEARS
```

Unit that represents the concept of a year.
For the ISO calendar system, it is equal to 12 months.
The estimated duration of a year is

365.2425 Days

.

When used with other calendar systems it must correspond to an integral number of days
or months roughly equal to a year defined by the passage of the Earth around the Sun.

---

#### YEARS

public static final

ChronoUnit

YEARS

Unit that represents the concept of a year.
For the ISO calendar system, it is equal to 12 months.
The estimated duration of a year is

365.2425 Days

.

When used with other calendar systems it must correspond to an integral number of days
or months roughly equal to a year defined by the passage of the Earth around the Sun.

When used with other calendar systems it must correspond to an integral number of days
or months roughly equal to a year defined by the passage of the Earth around the Sun.

DECADES

```java
public static final
ChronoUnit
DECADES
```

Unit that represents the concept of a decade.
For the ISO calendar system, it is equal to 10 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

---

#### DECADES

public static final

ChronoUnit

DECADES

Unit that represents the concept of a decade.
For the ISO calendar system, it is equal to 10 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

CENTURIES

```java
public static final
ChronoUnit
CENTURIES
```

Unit that represents the concept of a century.
For the ISO calendar system, it is equal to 100 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

---

#### CENTURIES

public static final

ChronoUnit

CENTURIES

Unit that represents the concept of a century.
For the ISO calendar system, it is equal to 100 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

MILLENNIA

```java
public static final
ChronoUnit
MILLENNIA
```

Unit that represents the concept of a millennium.
For the ISO calendar system, it is equal to 1000 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

---

#### MILLENNIA

public static final

ChronoUnit

MILLENNIA

Unit that represents the concept of a millennium.
For the ISO calendar system, it is equal to 1000 years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

When used with other calendar systems it must correspond to an integral number of days
and is normally an integral number of years.

ERAS

```java
public static final
ChronoUnit
ERAS
```

Unit that represents the concept of an era.
The ISO calendar system doesn't have eras thus it is impossible to add
an era to a date or date-time.
The estimated duration of the era is artificially defined as

1,000,000,000 Years

.

When used with other calendar systems there are no restrictions on the unit.

---

#### ERAS

public static final

ChronoUnit

ERAS

Unit that represents the concept of an era.
The ISO calendar system doesn't have eras thus it is impossible to add
an era to a date or date-time.
The estimated duration of the era is artificially defined as

1,000,000,000 Years

.

When used with other calendar systems there are no restrictions on the unit.

When used with other calendar systems there are no restrictions on the unit.

FOREVER

```java
public static final
ChronoUnit
FOREVER
```

Artificial unit that represents the concept of forever.
This is primarily used with

TemporalField

to represent unbounded fields
such as the year or era.
The estimated duration of this unit is artificially defined as the largest duration
supported by

Duration

.

---

#### FOREVER

public static final

ChronoUnit

FOREVER

Artificial unit that represents the concept of forever.
This is primarily used with

TemporalField

to represent unbounded fields
such as the year or era.
The estimated duration of this unit is artificially defined as the largest duration
supported by

Duration

.

Method Detail

- values

```java
public static
ChronoUnit
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoUnit c : ChronoUnit.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ChronoUnit
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

- getDuration

```java
public
Duration
getDuration()
```

Gets the estimated duration of this unit in the ISO calendar system.

All of the units in this class have an estimated duration.
Days vary due to daylight saving time, while months have different lengths.

**Specified by:** getDuration

in interface

TemporalUnit
**Returns:** the estimated duration of this unit, not null

- isDurationEstimated

```java
public boolean isDurationEstimated()
```

Checks if the duration of the unit is an estimate.

All time units in this class are considered to be accurate, while all date
units in this class are considered to be estimated.

This definition ignores leap seconds, but considers that Days vary due to
daylight saving time and months have different lengths.

**Specified by:** isDurationEstimated

in interface

TemporalUnit
**Returns:** true if the duration is estimated, false if accurate

- isDateBased

```java
public boolean isDateBased()
```

Checks if this unit is a date unit.

All units from days to eras inclusive are date-based.
Time-based units and

FOREVER

return false.

**Specified by:** isDateBased

in interface

TemporalUnit
**Returns:** true if a date unit, false if a time unit

- isTimeBased

```java
public boolean isTimeBased()
```

Checks if this unit is a time unit.

All units from nanos to half-days inclusive are time-based.
Date-based units and

FOREVER

return false.

**Specified by:** isTimeBased

in interface

TemporalUnit
**Returns:** true if a time unit, false if a date unit

---

#### Method Detail

values

```java
public static
ChronoUnit
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoUnit c : ChronoUnit.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ChronoUnit

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoUnit c : ChronoUnit.values())
System.out.println(c);
```

for (ChronoUnit c : ChronoUnit.values())
System.out.println(c);

valueOf

```java
public static
ChronoUnit
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

ChronoUnit

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

getDuration

```java
public
Duration
getDuration()
```

Gets the estimated duration of this unit in the ISO calendar system.

All of the units in this class have an estimated duration.
Days vary due to daylight saving time, while months have different lengths.

**Specified by:** getDuration

in interface

TemporalUnit
**Returns:** the estimated duration of this unit, not null

---

#### getDuration

public

Duration

getDuration()

Gets the estimated duration of this unit in the ISO calendar system.

All of the units in this class have an estimated duration.
Days vary due to daylight saving time, while months have different lengths.

All of the units in this class have an estimated duration.
Days vary due to daylight saving time, while months have different lengths.

isDurationEstimated

```java
public boolean isDurationEstimated()
```

Checks if the duration of the unit is an estimate.

All time units in this class are considered to be accurate, while all date
units in this class are considered to be estimated.

This definition ignores leap seconds, but considers that Days vary due to
daylight saving time and months have different lengths.

**Specified by:** isDurationEstimated

in interface

TemporalUnit
**Returns:** true if the duration is estimated, false if accurate

---

#### isDurationEstimated

public boolean isDurationEstimated()

Checks if the duration of the unit is an estimate.

All time units in this class are considered to be accurate, while all date
units in this class are considered to be estimated.

This definition ignores leap seconds, but considers that Days vary due to
daylight saving time and months have different lengths.

All time units in this class are considered to be accurate, while all date
units in this class are considered to be estimated.

This definition ignores leap seconds, but considers that Days vary due to
daylight saving time and months have different lengths.

This definition ignores leap seconds, but considers that Days vary due to
daylight saving time and months have different lengths.

isDateBased

```java
public boolean isDateBased()
```

Checks if this unit is a date unit.

All units from days to eras inclusive are date-based.
Time-based units and

FOREVER

return false.

**Specified by:** isDateBased

in interface

TemporalUnit
**Returns:** true if a date unit, false if a time unit

---

#### isDateBased

public boolean isDateBased()

Checks if this unit is a date unit.

All units from days to eras inclusive are date-based.
Time-based units and

FOREVER

return false.

All units from days to eras inclusive are date-based.
Time-based units and

FOREVER

return false.

isTimeBased

```java
public boolean isTimeBased()
```

Checks if this unit is a time unit.

All units from nanos to half-days inclusive are time-based.
Date-based units and

FOREVER

return false.

**Specified by:** isTimeBased

in interface

TemporalUnit
**Returns:** true if a time unit, false if a date unit

---

#### isTimeBased

public boolean isTimeBased()

Checks if this unit is a time unit.

All units from nanos to half-days inclusive are time-based.
Date-based units and

FOREVER

return false.

All units from nanos to half-days inclusive are time-based.
Date-based units and

FOREVER

return false.

---

