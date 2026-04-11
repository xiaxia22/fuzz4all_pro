# Enum ChronoField

**Source:** `java.base\java\time\temporal\ChronoField.html`

### Class Description

```java
public enum
ChronoField

extends
Enum
<
ChronoField
>
implements
TemporalField
```

A standard set of fields.

This set of fields provide field-based access to manipulate a date, time or date-time.
The standard set of fields can be extended by implementing

TemporalField

.

These fields are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define dates as a year, month and day,
just with slightly different rules.
The documentation of each field explains how it operates.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ChronoField

>

,

TemporalField

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ChronoField
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoField c : ChronoField.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ChronoField
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
ValueRange
range()

Gets the range of valid values for the field.

All fields can be expressed as a

long

integer.
This method returns an object that describes the valid range for that value.

This method returns the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

Note that the result only describes the minimum and maximum valid values
and it is important not to read too much into them. For example, there
could be values within the range that are invalid for the field.

**Specified by:**
- range

in interface

TemporalField

**Returns:**
- the range of valid values for the field, not null

---

#### public boolean isDateBased()

Checks if this field represents a component of a date.

Fields from day-of-week to era are date-based.

**Specified by:**
- isDateBased

in interface

TemporalField

**Returns:**
- true if it is a component of a date

---

#### public boolean isTimeBased()

Checks if this field represents a component of a time.

Fields from nano-of-second to am-pm-of-day are time-based.

**Specified by:**
- isTimeBased

in interface

TemporalField

**Returns:**
- true if it is a component of a time

---

#### public long checkValidValue​(long value)

Checks that the specified value is valid for this field.

This validates that the value is within the outer range of valid values
returned by

range()

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

**Parameters:**
- value

- the value to check

**Returns:**
- the value that was passed in

---

#### public int checkValidIntValue​(long value)

Checks that the specified value is valid and fits in an

int

.

This validates that the value is within the outer range of valid values
returned by

range()

.
It also checks that all valid values are within the bounds of an

int

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

**Parameters:**
- value

- the value to check

**Returns:**
- the value that was passed in

---

### Additional Sections

#### Enum ChronoField

java.lang.Object

- java.lang.Enum

<

ChronoField

>
- - java.time.temporal.ChronoField

java.lang.Enum

<

ChronoField

>

- java.time.temporal.ChronoField

java.time.temporal.ChronoField

**All Implemented Interfaces:** Serializable

,

Comparable

<

ChronoField

>

,

TemporalField

```java
public enum
ChronoField

extends
Enum
<
ChronoField
>
implements
TemporalField
```

A standard set of fields.

This set of fields provide field-based access to manipulate a date, time or date-time.
The standard set of fields can be extended by implementing

TemporalField

.

These fields are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define dates as a year, month and day,
just with slightly different rules.
The documentation of each field explains how it operates.

**Implementation Requirements:** This is a final, immutable and thread-safe enum.
**Since:** 1.8

public enum

ChronoField

extends

Enum

<

ChronoField

>
implements

TemporalField

A standard set of fields.

This set of fields provide field-based access to manipulate a date, time or date-time.
The standard set of fields can be extended by implementing

TemporalField

.

These fields are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define dates as a year, month and day,
just with slightly different rules.
The documentation of each field explains how it operates.

This set of fields provide field-based access to manipulate a date, time or date-time.
The standard set of fields can be extended by implementing

TemporalField

.

These fields are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define dates as a year, month and day,
just with slightly different rules.
The documentation of each field explains how it operates.

These fields are intended to be applicable in multiple calendar systems.
For example, most non-ISO calendar systems define dates as a year, month and day,
just with slightly different rules.
The documentation of each field explains how it operates.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ALIGNED_DAY_OF_WEEK_IN_MONTH

The aligned day-of-week within a month.

ALIGNED_DAY_OF_WEEK_IN_YEAR

The aligned day-of-week within a year.

ALIGNED_WEEK_OF_MONTH

The aligned week within a month.

ALIGNED_WEEK_OF_YEAR

The aligned week within a year.

AMPM_OF_DAY

The am-pm-of-day.

CLOCK_HOUR_OF_AMPM

The clock-hour-of-am-pm.

CLOCK_HOUR_OF_DAY

The clock-hour-of-day.

DAY_OF_MONTH

The day-of-month.

DAY_OF_WEEK

The day-of-week, such as Tuesday.

DAY_OF_YEAR

The day-of-year.

EPOCH_DAY

The epoch-day, based on the Java epoch of 1970-01-01 (ISO).

ERA

The era.

HOUR_OF_AMPM

The hour-of-am-pm.

HOUR_OF_DAY

The hour-of-day.

INSTANT_SECONDS

The instant epoch-seconds.

MICRO_OF_DAY

The micro-of-day.

MICRO_OF_SECOND

The micro-of-second.

MILLI_OF_DAY

The milli-of-day.

MILLI_OF_SECOND

The milli-of-second.

MINUTE_OF_DAY

The minute-of-day.

MINUTE_OF_HOUR

The minute-of-hour.

MONTH_OF_YEAR

The month-of-year, such as March.

NANO_OF_DAY

The nano-of-day.

NANO_OF_SECOND

The nano-of-second.

OFFSET_SECONDS

The offset from UTC/Greenwich.

PROLEPTIC_MONTH

The proleptic-month based, counting months sequentially from year 0.

SECOND_OF_DAY

The second-of-day.

SECOND_OF_MINUTE

The second-of-minute.

YEAR

The proleptic year, such as 2012.

YEAR_OF_ERA

The year within the era.

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

checkValidIntValue

​(long value)

Checks that the specified value is valid and fits in an

int

.

long

checkValidValue

​(long value)

Checks that the specified value is valid for this field.

boolean

isDateBased

()

Checks if this field represents a component of a date.

boolean

isTimeBased

()

Checks if this field represents a component of a time.

ValueRange

range

()

Gets the range of valid values for the field.

static

ChronoField

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ChronoField

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

TemporalField

adjustInto

,

getBaseUnit

,

getDisplayName

,

getFrom

,

getRangeUnit

,

isSupportedBy

,

rangeRefinedBy

,

resolve

,

toString

Enum Constant Summary

Enum Constants

Enum Constant

Description

ALIGNED_DAY_OF_WEEK_IN_MONTH

The aligned day-of-week within a month.

ALIGNED_DAY_OF_WEEK_IN_YEAR

The aligned day-of-week within a year.

ALIGNED_WEEK_OF_MONTH

The aligned week within a month.

ALIGNED_WEEK_OF_YEAR

The aligned week within a year.

AMPM_OF_DAY

The am-pm-of-day.

CLOCK_HOUR_OF_AMPM

The clock-hour-of-am-pm.

CLOCK_HOUR_OF_DAY

The clock-hour-of-day.

DAY_OF_MONTH

The day-of-month.

DAY_OF_WEEK

The day-of-week, such as Tuesday.

DAY_OF_YEAR

The day-of-year.

EPOCH_DAY

The epoch-day, based on the Java epoch of 1970-01-01 (ISO).

ERA

The era.

HOUR_OF_AMPM

The hour-of-am-pm.

HOUR_OF_DAY

The hour-of-day.

INSTANT_SECONDS

The instant epoch-seconds.

MICRO_OF_DAY

The micro-of-day.

MICRO_OF_SECOND

The micro-of-second.

MILLI_OF_DAY

The milli-of-day.

MILLI_OF_SECOND

The milli-of-second.

MINUTE_OF_DAY

The minute-of-day.

MINUTE_OF_HOUR

The minute-of-hour.

MONTH_OF_YEAR

The month-of-year, such as March.

NANO_OF_DAY

The nano-of-day.

NANO_OF_SECOND

The nano-of-second.

OFFSET_SECONDS

The offset from UTC/Greenwich.

PROLEPTIC_MONTH

The proleptic-month based, counting months sequentially from year 0.

SECOND_OF_DAY

The second-of-day.

SECOND_OF_MINUTE

The second-of-minute.

YEAR

The proleptic year, such as 2012.

YEAR_OF_ERA

The year within the era.

---

#### Enum Constant Summary

The aligned day-of-week within a month.

The aligned day-of-week within a year.

The aligned week within a month.

The aligned week within a year.

The am-pm-of-day.

The clock-hour-of-am-pm.

The clock-hour-of-day.

The day-of-month.

The day-of-week, such as Tuesday.

The day-of-year.

The epoch-day, based on the Java epoch of 1970-01-01 (ISO).

The era.

The hour-of-am-pm.

The hour-of-day.

The instant epoch-seconds.

The micro-of-day.

The micro-of-second.

The milli-of-day.

The milli-of-second.

The minute-of-day.

The minute-of-hour.

The month-of-year, such as March.

The nano-of-day.

The nano-of-second.

The offset from UTC/Greenwich.

The proleptic-month based, counting months sequentially from year 0.

The second-of-day.

The second-of-minute.

The proleptic year, such as 2012.

The year within the era.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

checkValidIntValue

​(long value)

Checks that the specified value is valid and fits in an

int

.

long

checkValidValue

​(long value)

Checks that the specified value is valid for this field.

boolean

isDateBased

()

Checks if this field represents a component of a date.

boolean

isTimeBased

()

Checks if this field represents a component of a time.

ValueRange

range

()

Gets the range of valid values for the field.

static

ChronoField

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ChronoField

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

TemporalField

adjustInto

,

getBaseUnit

,

getDisplayName

,

getFrom

,

getRangeUnit

,

isSupportedBy

,

rangeRefinedBy

,

resolve

,

toString

---

#### Method Summary

Checks that the specified value is valid and fits in an

int

.

Checks that the specified value is valid for this field.

Checks if this field represents a component of a date.

Checks if this field represents a component of a time.

Gets the range of valid values for the field.

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

TemporalField

adjustInto

,

getBaseUnit

,

getDisplayName

,

getFrom

,

getRangeUnit

,

isSupportedBy

,

rangeRefinedBy

,

resolve

,

toString

---

#### Methods declared in interface java.time.temporal. TemporalField

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- NANO_OF_SECOND

```java
public static final
ChronoField
NANO_OF_SECOND
```

The nano-of-second.

This counts the nanosecond within the second, from 0 to 999,999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should set as much precision as the
object stores, using integer division to remove excess precision.
For example, if the

TemporalAccessor

stores time to millisecond precision,
then the nano-of-second must be divided by 1,000,000 before replacing the milli-of-second.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

and

MICRO_OF_SECOND

.

- NANO_OF_DAY

```java
public static final
ChronoField
NANO_OF_DAY
```

The nano-of-day.

This counts the nanosecond within the day, from 0 to (24 * 60 * 60 * 1,000,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

NANO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- MICRO_OF_SECOND

```java
public static final
ChronoField
MICRO_OF_SECOND
```

The micro-of-second.

This counts the microsecond within the second, from 0 to 999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

to produce

NANO_OF_SECOND

.

- MICRO_OF_DAY

```java
public static final
ChronoField
MICRO_OF_DAY
```

The micro-of-day.

This counts the microsecond within the day, from 0 to (24 * 60 * 60 * 1,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MICRO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- MILLI_OF_SECOND

```java
public static final
ChronoField
MILLI_OF_SECOND
```

The milli-of-second.

This counts the millisecond within the second, from 0 to 999.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MICRO_OF_SECOND

to produce

NANO_OF_SECOND

.

- MILLI_OF_DAY

```java
public static final
ChronoField
MILLI_OF_DAY
```

The milli-of-day.

This counts the millisecond within the day, from 0 to (24 * 60 * 60 * 1,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MILLI_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- SECOND_OF_MINUTE

```java
public static final
ChronoField
SECOND_OF_MINUTE
```

The second-of-minute.

This counts the second within the minute, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

- SECOND_OF_DAY

```java
public static final
ChronoField
SECOND_OF_DAY
```

The second-of-day.

This counts the second within the day, from 0 to (24 * 60 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- MINUTE_OF_HOUR

```java
public static final
ChronoField
MINUTE_OF_HOUR
```

The minute-of-hour.

This counts the minute within the hour, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

- MINUTE_OF_DAY

```java
public static final
ChronoField
MINUTE_OF_DAY
```

The minute-of-day.

This counts the minute within the day, from 0 to (24 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- HOUR_OF_AMPM

```java
public static final
ChronoField
HOUR_OF_AMPM
```

The hour-of-am-pm.

This counts the hour within the AM/PM, from 0 to 11.
This is the hour that would be observed on a standard 12-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 11 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

AMPM_OF_DAY

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

See

CLOCK_HOUR_OF_AMPM

for the related field that counts hours from 1 to 12.

- CLOCK_HOUR_OF_AMPM

```java
public static final
ChronoField
CLOCK_HOUR_OF_AMPM
```

The clock-hour-of-am-pm.

This counts the hour within the AM/PM, from 1 to 12.
This is the hour that would be observed on a standard 12-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 12 in strict mode and from
0 to 12 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_AMPM

with the same value,
unless the value is 12, in which case it is converted to 0.

See

HOUR_OF_AMPM

for the related field that counts hours from 0 to 11.

- HOUR_OF_DAY

```java
public static final
ChronoField
HOUR_OF_DAY
```

The hour-of-day.

This counts the hour within the day, from 0 to 23.
This is the hour that would be observed on a standard 24-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is combined with

MINUTE_OF_HOUR

,

SECOND_OF_MINUTE

and

NANO_OF_SECOND

to produce a

LocalTime

.
In lenient mode, any excess days are added to the parsed date, or
made available via

DateTimeFormatter.parsedExcessDays()

.

See

CLOCK_HOUR_OF_DAY

for the related field that counts hours from 1 to 24.

- CLOCK_HOUR_OF_DAY

```java
public static final
ChronoField
CLOCK_HOUR_OF_DAY
```

The clock-hour-of-day.

This counts the hour within the day, from 1 to 24.
This is the hour that would be observed on a 24-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 24 in strict mode and from
0 to 24 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_DAY

with the same value,
unless the value is 24, in which case it is converted to 0.

See

HOUR_OF_DAY

for the related field that counts hours from 0 to 23.

- AMPM_OF_DAY

```java
public static final
ChronoField
AMPM_OF_DAY
```

The am-pm-of-day.

This counts the AM/PM within the day, from 0 (AM) to 1 (PM).
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 1 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

HOUR_OF_AMPM

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

- DAY_OF_WEEK

```java
public static final
ChronoField
DAY_OF_WEEK
```

The day-of-week, such as Tuesday.

This represents the standard concept of the day of the week.
In the default ISO calendar system, this has values from Monday (1) to Sunday (7).
The

DayOfWeek

class can be used to interpret the result.

Most non-ISO calendar systems also define a seven day week that aligns with ISO.
Those calendar systems must also use the same numbering system, from Monday (1) to
Sunday (7), which allows

DayOfWeek

to be used.

Calendar systems that do not have a standard seven day week should implement this field
if they have a similar concept of named or numbered days within a period similar
to a week. It is recommended that the numbering starts from 1.

- ALIGNED_DAY_OF_WEEK_IN_MONTH

```java
public static final
ChronoField
ALIGNED_DAY_OF_WEEK_IN_MONTH
```

The aligned day-of-week within a month.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_WEEK_OF_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-month 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-month 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

- ALIGNED_DAY_OF_WEEK_IN_YEAR

```java
public static final
ChronoField
ALIGNED_DAY_OF_WEEK_IN_YEAR
```

The aligned day-of-week within a year.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_WEEK_OF_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-year 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-year 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

- DAY_OF_MONTH

```java
public static final
ChronoField
DAY_OF_MONTH
```

The day-of-month.

This represents the concept of the day within the month.
In the default ISO calendar system, this has values from 1 to 31 in most months.
April, June, September, November have days from 1 to 30, while February has days
from 1 to 28, or 29 in a leap year.

Non-ISO calendar systems should implement this field using the most recognized
day-of-month values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the month.

- DAY_OF_YEAR

```java
public static final
ChronoField
DAY_OF_YEAR
```

The day-of-year.

This represents the concept of the day within the year.
In the default ISO calendar system, this has values from 1 to 365 in standard
years and 1 to 366 in leap years.

Non-ISO calendar systems should implement this field using the most recognized
day-of-year values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the year.

Note that a non-ISO calendar system may have year numbering system that changes
at a different point to the natural reset in the month numbering. An example
of this is the Japanese calendar system where a change of era, which resets
the year number to 1, can happen on any date. The era and year reset also cause
the day-of-year to be reset to 1, but not the month-of-year or day-of-month.

- EPOCH_DAY

```java
public static final
ChronoField
EPOCH_DAY
```

The epoch-day, based on the Java epoch of 1970-01-01 (ISO).

This field is the sequential count of days where 1970-01-01 (ISO) is zero.
Note that this uses the

local

time-line, ignoring offset and time-zone.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

Range of EpochDay is between (LocalDate.MIN.toEpochDay(), LocalDate.MAX.toEpochDay())
both inclusive.

- ALIGNED_WEEK_OF_MONTH

```java
public static final
ChronoField
ALIGNED_WEEK_OF_MONTH
```

The aligned week within a month.

This represents concept of the count of weeks within the period of a month
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Thus, day-of-month values 1 to 7 are in aligned-week 1, while day-of-month values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

- ALIGNED_WEEK_OF_YEAR

```java
public static final
ChronoField
ALIGNED_WEEK_OF_YEAR
```

The aligned week within a year.

This represents concept of the count of weeks within the period of a year
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Thus, day-of-year values 1 to 7 are in aligned-week 1, while day-of-year values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

- MONTH_OF_YEAR

```java
public static final
ChronoField
MONTH_OF_YEAR
```

The month-of-year, such as March.

This represents the concept of the month within the year.
In the default ISO calendar system, this has values from January (1) to December (12).

Non-ISO calendar systems should implement this field using the most recognized
month-of-year values for users of the calendar system.
Normally, this is a count of months starting from 1.

- PROLEPTIC_MONTH

```java
public static final
ChronoField
PROLEPTIC_MONTH
```

The proleptic-month based, counting months sequentially from year 0.

This field is the sequential count of months where the first month
in proleptic-year zero has the value zero.
Later months have increasingly larger values.
Earlier months have increasingly small values.
There are no gaps or breaks in the sequence of months.
Note that this uses the

local

time-line, ignoring offset and time-zone.

In the default ISO calendar system, June 2012 would have the value

(2012 * 12 + 6 - 1)

. This field is primarily for internal use.

Non-ISO calendar systems must implement this field as per the definition above.
It is just a simple zero-based count of elapsed months from the start of proleptic-year 0.
All calendar systems with a full proleptic-year definition will have a year zero.
If the calendar system has a minimum year that excludes year zero, then one must
be extrapolated in order for this method to be defined.

- YEAR_OF_ERA

```java
public static final
ChronoField
YEAR_OF_ERA
```

The year within the era.

This represents the concept of the year within the era.
This field is typically used with

ERA

.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.

For example, subtracting a year each time yield the following:

- year-proleptic 2 = 'CE' year-of-era 2

- year-proleptic 1 = 'CE' year-of-era 1

- year-proleptic 0 = 'BCE' year-of-era 1

- year-proleptic -1 = 'BCE' year-of-era 2

Note that the ISO-8601 standard does not actually define eras.
Note also that the ISO eras do not align with the well-known AD/BC eras due to the
change between the Julian and Gregorian calendar systems.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

- YEAR

```java
public static final
ChronoField
YEAR
```

The proleptic year, such as 2012.

This represents the concept of the year, counting sequentially and using negative numbers.
The proleptic year is not interpreted in terms of the era.
See

YEAR_OF_ERA

for an example showing the mapping from proleptic year to year-of-era.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR_OF_ERA

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

Non-ISO calendar systems should implement this field as follows.
If the calendar system has only two eras, before and after a fixed date, then the
proleptic-year value must be the same as the year-of-era value for the later era,
and increasingly negative for the earlier era.
If the calendar system has more than two eras, then the proleptic-year value may be
defined with any appropriate value, although defining it to be the same as ISO may be
the best option.

- ERA

```java
public static final
ChronoField
ERA
```

The era.

This represents the concept of the era, which is the largest division of the time-line.
This field is typically used with

YEAR_OF_ERA

.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.
See

YEAR_OF_ERA

for a full example.

Non-ISO calendar systems should implement this field to define eras.
The value of the era that was active on 1970-01-01 (ISO) must be assigned the value 1.
Earlier eras must have sequentially smaller values.
Later eras must have sequentially larger values,

- INSTANT_SECONDS

```java
public static final
ChronoField
INSTANT_SECONDS
```

The instant epoch-seconds.

This represents the concept of the sequential count of seconds where
1970-01-01T00:00Z (ISO) is zero.
This field may be used with

NANO_OF_SECOND

to represent the fraction of the second.

An

Instant

represents an instantaneous point on the time-line.
On their own, an instant has insufficient information to allow a local date-time to be obtained.
Only when paired with an offset or time-zone can the local date or time be calculated.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

- OFFSET_SECONDS

```java
public static final
ChronoField
OFFSET_SECONDS
```

The offset from UTC/Greenwich.

This represents the concept of the offset in seconds of local time from UTC/Greenwich.

A

ZoneOffset

represents the period of time that local time differs from UTC/Greenwich.
This is usually a fixed number of hours and minutes.
It is equivalent to the

total amount

of the offset in seconds.
For example, during the winter Paris has an offset of

+01:00

, which is 3600 seconds.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ChronoField
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoField c : ChronoField.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ChronoField
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

- range

```java
public
ValueRange
range()
```

Gets the range of valid values for the field.

All fields can be expressed as a

long

integer.
This method returns an object that describes the valid range for that value.

This method returns the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

Note that the result only describes the minimum and maximum valid values
and it is important not to read too much into them. For example, there
could be values within the range that are invalid for the field.

**Specified by:** range

in interface

TemporalField
**Returns:** the range of valid values for the field, not null

- isDateBased

```java
public boolean isDateBased()
```

Checks if this field represents a component of a date.

Fields from day-of-week to era are date-based.

**Specified by:** isDateBased

in interface

TemporalField
**Returns:** true if it is a component of a date

- isTimeBased

```java
public boolean isTimeBased()
```

Checks if this field represents a component of a time.

Fields from nano-of-second to am-pm-of-day are time-based.

**Specified by:** isTimeBased

in interface

TemporalField
**Returns:** true if it is a component of a time

- checkValidValue

```java
public long checkValidValue​(long value)
```

Checks that the specified value is valid for this field.

This validates that the value is within the outer range of valid values
returned by

range()

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

**Parameters:** value

- the value to check
**Returns:** the value that was passed in

- checkValidIntValue

```java
public int checkValidIntValue​(long value)
```

Checks that the specified value is valid and fits in an

int

.

This validates that the value is within the outer range of valid values
returned by

range()

.
It also checks that all valid values are within the bounds of an

int

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

**Parameters:** value

- the value to check
**Returns:** the value that was passed in

Enum Constant Detail

- NANO_OF_SECOND

```java
public static final
ChronoField
NANO_OF_SECOND
```

The nano-of-second.

This counts the nanosecond within the second, from 0 to 999,999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should set as much precision as the
object stores, using integer division to remove excess precision.
For example, if the

TemporalAccessor

stores time to millisecond precision,
then the nano-of-second must be divided by 1,000,000 before replacing the milli-of-second.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

and

MICRO_OF_SECOND

.

- NANO_OF_DAY

```java
public static final
ChronoField
NANO_OF_DAY
```

The nano-of-day.

This counts the nanosecond within the day, from 0 to (24 * 60 * 60 * 1,000,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

NANO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- MICRO_OF_SECOND

```java
public static final
ChronoField
MICRO_OF_SECOND
```

The micro-of-second.

This counts the microsecond within the second, from 0 to 999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

to produce

NANO_OF_SECOND

.

- MICRO_OF_DAY

```java
public static final
ChronoField
MICRO_OF_DAY
```

The micro-of-day.

This counts the microsecond within the day, from 0 to (24 * 60 * 60 * 1,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MICRO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- MILLI_OF_SECOND

```java
public static final
ChronoField
MILLI_OF_SECOND
```

The milli-of-second.

This counts the millisecond within the second, from 0 to 999.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MICRO_OF_SECOND

to produce

NANO_OF_SECOND

.

- MILLI_OF_DAY

```java
public static final
ChronoField
MILLI_OF_DAY
```

The milli-of-day.

This counts the millisecond within the day, from 0 to (24 * 60 * 60 * 1,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MILLI_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- SECOND_OF_MINUTE

```java
public static final
ChronoField
SECOND_OF_MINUTE
```

The second-of-minute.

This counts the second within the minute, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

- SECOND_OF_DAY

```java
public static final
ChronoField
SECOND_OF_DAY
```

The second-of-day.

This counts the second within the day, from 0 to (24 * 60 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- MINUTE_OF_HOUR

```java
public static final
ChronoField
MINUTE_OF_HOUR
```

The minute-of-hour.

This counts the minute within the hour, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

- MINUTE_OF_DAY

```java
public static final
ChronoField
MINUTE_OF_DAY
```

The minute-of-day.

This counts the minute within the day, from 0 to (24 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

- HOUR_OF_AMPM

```java
public static final
ChronoField
HOUR_OF_AMPM
```

The hour-of-am-pm.

This counts the hour within the AM/PM, from 0 to 11.
This is the hour that would be observed on a standard 12-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 11 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

AMPM_OF_DAY

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

See

CLOCK_HOUR_OF_AMPM

for the related field that counts hours from 1 to 12.

- CLOCK_HOUR_OF_AMPM

```java
public static final
ChronoField
CLOCK_HOUR_OF_AMPM
```

The clock-hour-of-am-pm.

This counts the hour within the AM/PM, from 1 to 12.
This is the hour that would be observed on a standard 12-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 12 in strict mode and from
0 to 12 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_AMPM

with the same value,
unless the value is 12, in which case it is converted to 0.

See

HOUR_OF_AMPM

for the related field that counts hours from 0 to 11.

- HOUR_OF_DAY

```java
public static final
ChronoField
HOUR_OF_DAY
```

The hour-of-day.

This counts the hour within the day, from 0 to 23.
This is the hour that would be observed on a standard 24-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is combined with

MINUTE_OF_HOUR

,

SECOND_OF_MINUTE

and

NANO_OF_SECOND

to produce a

LocalTime

.
In lenient mode, any excess days are added to the parsed date, or
made available via

DateTimeFormatter.parsedExcessDays()

.

See

CLOCK_HOUR_OF_DAY

for the related field that counts hours from 1 to 24.

- CLOCK_HOUR_OF_DAY

```java
public static final
ChronoField
CLOCK_HOUR_OF_DAY
```

The clock-hour-of-day.

This counts the hour within the day, from 1 to 24.
This is the hour that would be observed on a 24-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 24 in strict mode and from
0 to 24 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_DAY

with the same value,
unless the value is 24, in which case it is converted to 0.

See

HOUR_OF_DAY

for the related field that counts hours from 0 to 23.

- AMPM_OF_DAY

```java
public static final
ChronoField
AMPM_OF_DAY
```

The am-pm-of-day.

This counts the AM/PM within the day, from 0 (AM) to 1 (PM).
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 1 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

HOUR_OF_AMPM

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

- DAY_OF_WEEK

```java
public static final
ChronoField
DAY_OF_WEEK
```

The day-of-week, such as Tuesday.

This represents the standard concept of the day of the week.
In the default ISO calendar system, this has values from Monday (1) to Sunday (7).
The

DayOfWeek

class can be used to interpret the result.

Most non-ISO calendar systems also define a seven day week that aligns with ISO.
Those calendar systems must also use the same numbering system, from Monday (1) to
Sunday (7), which allows

DayOfWeek

to be used.

Calendar systems that do not have a standard seven day week should implement this field
if they have a similar concept of named or numbered days within a period similar
to a week. It is recommended that the numbering starts from 1.

- ALIGNED_DAY_OF_WEEK_IN_MONTH

```java
public static final
ChronoField
ALIGNED_DAY_OF_WEEK_IN_MONTH
```

The aligned day-of-week within a month.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_WEEK_OF_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-month 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-month 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

- ALIGNED_DAY_OF_WEEK_IN_YEAR

```java
public static final
ChronoField
ALIGNED_DAY_OF_WEEK_IN_YEAR
```

The aligned day-of-week within a year.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_WEEK_OF_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-year 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-year 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

- DAY_OF_MONTH

```java
public static final
ChronoField
DAY_OF_MONTH
```

The day-of-month.

This represents the concept of the day within the month.
In the default ISO calendar system, this has values from 1 to 31 in most months.
April, June, September, November have days from 1 to 30, while February has days
from 1 to 28, or 29 in a leap year.

Non-ISO calendar systems should implement this field using the most recognized
day-of-month values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the month.

- DAY_OF_YEAR

```java
public static final
ChronoField
DAY_OF_YEAR
```

The day-of-year.

This represents the concept of the day within the year.
In the default ISO calendar system, this has values from 1 to 365 in standard
years and 1 to 366 in leap years.

Non-ISO calendar systems should implement this field using the most recognized
day-of-year values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the year.

Note that a non-ISO calendar system may have year numbering system that changes
at a different point to the natural reset in the month numbering. An example
of this is the Japanese calendar system where a change of era, which resets
the year number to 1, can happen on any date. The era and year reset also cause
the day-of-year to be reset to 1, but not the month-of-year or day-of-month.

- EPOCH_DAY

```java
public static final
ChronoField
EPOCH_DAY
```

The epoch-day, based on the Java epoch of 1970-01-01 (ISO).

This field is the sequential count of days where 1970-01-01 (ISO) is zero.
Note that this uses the

local

time-line, ignoring offset and time-zone.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

Range of EpochDay is between (LocalDate.MIN.toEpochDay(), LocalDate.MAX.toEpochDay())
both inclusive.

- ALIGNED_WEEK_OF_MONTH

```java
public static final
ChronoField
ALIGNED_WEEK_OF_MONTH
```

The aligned week within a month.

This represents concept of the count of weeks within the period of a month
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Thus, day-of-month values 1 to 7 are in aligned-week 1, while day-of-month values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

- ALIGNED_WEEK_OF_YEAR

```java
public static final
ChronoField
ALIGNED_WEEK_OF_YEAR
```

The aligned week within a year.

This represents concept of the count of weeks within the period of a year
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Thus, day-of-year values 1 to 7 are in aligned-week 1, while day-of-year values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

- MONTH_OF_YEAR

```java
public static final
ChronoField
MONTH_OF_YEAR
```

The month-of-year, such as March.

This represents the concept of the month within the year.
In the default ISO calendar system, this has values from January (1) to December (12).

Non-ISO calendar systems should implement this field using the most recognized
month-of-year values for users of the calendar system.
Normally, this is a count of months starting from 1.

- PROLEPTIC_MONTH

```java
public static final
ChronoField
PROLEPTIC_MONTH
```

The proleptic-month based, counting months sequentially from year 0.

This field is the sequential count of months where the first month
in proleptic-year zero has the value zero.
Later months have increasingly larger values.
Earlier months have increasingly small values.
There are no gaps or breaks in the sequence of months.
Note that this uses the

local

time-line, ignoring offset and time-zone.

In the default ISO calendar system, June 2012 would have the value

(2012 * 12 + 6 - 1)

. This field is primarily for internal use.

Non-ISO calendar systems must implement this field as per the definition above.
It is just a simple zero-based count of elapsed months from the start of proleptic-year 0.
All calendar systems with a full proleptic-year definition will have a year zero.
If the calendar system has a minimum year that excludes year zero, then one must
be extrapolated in order for this method to be defined.

- YEAR_OF_ERA

```java
public static final
ChronoField
YEAR_OF_ERA
```

The year within the era.

This represents the concept of the year within the era.
This field is typically used with

ERA

.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.

For example, subtracting a year each time yield the following:

- year-proleptic 2 = 'CE' year-of-era 2

- year-proleptic 1 = 'CE' year-of-era 1

- year-proleptic 0 = 'BCE' year-of-era 1

- year-proleptic -1 = 'BCE' year-of-era 2

Note that the ISO-8601 standard does not actually define eras.
Note also that the ISO eras do not align with the well-known AD/BC eras due to the
change between the Julian and Gregorian calendar systems.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

- YEAR

```java
public static final
ChronoField
YEAR
```

The proleptic year, such as 2012.

This represents the concept of the year, counting sequentially and using negative numbers.
The proleptic year is not interpreted in terms of the era.
See

YEAR_OF_ERA

for an example showing the mapping from proleptic year to year-of-era.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR_OF_ERA

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

Non-ISO calendar systems should implement this field as follows.
If the calendar system has only two eras, before and after a fixed date, then the
proleptic-year value must be the same as the year-of-era value for the later era,
and increasingly negative for the earlier era.
If the calendar system has more than two eras, then the proleptic-year value may be
defined with any appropriate value, although defining it to be the same as ISO may be
the best option.

- ERA

```java
public static final
ChronoField
ERA
```

The era.

This represents the concept of the era, which is the largest division of the time-line.
This field is typically used with

YEAR_OF_ERA

.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.
See

YEAR_OF_ERA

for a full example.

Non-ISO calendar systems should implement this field to define eras.
The value of the era that was active on 1970-01-01 (ISO) must be assigned the value 1.
Earlier eras must have sequentially smaller values.
Later eras must have sequentially larger values,

- INSTANT_SECONDS

```java
public static final
ChronoField
INSTANT_SECONDS
```

The instant epoch-seconds.

This represents the concept of the sequential count of seconds where
1970-01-01T00:00Z (ISO) is zero.
This field may be used with

NANO_OF_SECOND

to represent the fraction of the second.

An

Instant

represents an instantaneous point on the time-line.
On their own, an instant has insufficient information to allow a local date-time to be obtained.
Only when paired with an offset or time-zone can the local date or time be calculated.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

- OFFSET_SECONDS

```java
public static final
ChronoField
OFFSET_SECONDS
```

The offset from UTC/Greenwich.

This represents the concept of the offset in seconds of local time from UTC/Greenwich.

A

ZoneOffset

represents the period of time that local time differs from UTC/Greenwich.
This is usually a fixed number of hours and minutes.
It is equivalent to the

total amount

of the offset in seconds.
For example, during the winter Paris has an offset of

+01:00

, which is 3600 seconds.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

---

#### Enum Constant Detail

NANO_OF_SECOND

```java
public static final
ChronoField
NANO_OF_SECOND
```

The nano-of-second.

This counts the nanosecond within the second, from 0 to 999,999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should set as much precision as the
object stores, using integer division to remove excess precision.
For example, if the

TemporalAccessor

stores time to millisecond precision,
then the nano-of-second must be divided by 1,000,000 before replacing the milli-of-second.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

and

MICRO_OF_SECOND

.

---

#### NANO_OF_SECOND

public static final

ChronoField

NANO_OF_SECOND

The nano-of-second.

This counts the nanosecond within the second, from 0 to 999,999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should set as much precision as the
object stores, using integer division to remove excess precision.
For example, if the

TemporalAccessor

stores time to millisecond precision,
then the nano-of-second must be divided by 1,000,000 before replacing the milli-of-second.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

and

MICRO_OF_SECOND

.

This counts the nanosecond within the second, from 0 to 999,999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should set as much precision as the
object stores, using integer division to remove excess precision.
For example, if the

TemporalAccessor

stores time to millisecond precision,
then the nano-of-second must be divided by 1,000,000 before replacing the milli-of-second.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

and

MICRO_OF_SECOND

.

This field is used to represent the nano-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should set as much precision as the
object stores, using integer division to remove excess precision.
For example, if the

TemporalAccessor

stores time to millisecond precision,
then the nano-of-second must be divided by 1,000,000 before replacing the milli-of-second.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

and

MICRO_OF_SECOND

.

When this field is used for setting a value, it should set as much precision as the
object stores, using integer division to remove excess precision.
For example, if the

TemporalAccessor

stores time to millisecond precision,
then the nano-of-second must be divided by 1,000,000 before replacing the milli-of-second.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

and

MICRO_OF_SECOND

.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

and

MICRO_OF_SECOND

.

NANO_OF_DAY

```java
public static final
ChronoField
NANO_OF_DAY
```

The nano-of-day.

This counts the nanosecond within the day, from 0 to (24 * 60 * 60 * 1,000,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

NANO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

---

#### NANO_OF_DAY

public static final

ChronoField

NANO_OF_DAY

The nano-of-day.

This counts the nanosecond within the day, from 0 to (24 * 60 * 60 * 1,000,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

NANO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

This counts the nanosecond within the day, from 0 to (24 * 60 * 60 * 1,000,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the nano-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

NANO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

This field is used to represent the nano-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

NANO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

NANO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

MICRO_OF_SECOND

```java
public static final
ChronoField
MICRO_OF_SECOND
```

The micro-of-second.

This counts the microsecond within the second, from 0 to 999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

to produce

NANO_OF_SECOND

.

---

#### MICRO_OF_SECOND

public static final

ChronoField

MICRO_OF_SECOND

The micro-of-second.

This counts the microsecond within the second, from 0 to 999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

to produce

NANO_OF_SECOND

.

This counts the microsecond within the second, from 0 to 999,999.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

to produce

NANO_OF_SECOND

.

This field is used to represent the micro-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

to produce

NANO_OF_SECOND

.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

to produce

NANO_OF_SECOND

.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MILLI_OF_SECOND

to produce

NANO_OF_SECOND

.

MICRO_OF_DAY

```java
public static final
ChronoField
MICRO_OF_DAY
```

The micro-of-day.

This counts the microsecond within the day, from 0 to (24 * 60 * 60 * 1,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MICRO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

---

#### MICRO_OF_DAY

public static final

ChronoField

MICRO_OF_DAY

The micro-of-day.

This counts the microsecond within the day, from 0 to (24 * 60 * 60 * 1,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MICRO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

This counts the microsecond within the day, from 0 to (24 * 60 * 60 * 1,000,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the micro-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MICRO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

This field is used to represent the micro-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MICRO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MICRO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MICRO_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

MILLI_OF_SECOND

```java
public static final
ChronoField
MILLI_OF_SECOND
```

The milli-of-second.

This counts the millisecond within the second, from 0 to 999.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MICRO_OF_SECOND

to produce

NANO_OF_SECOND

.

---

#### MILLI_OF_SECOND

public static final

ChronoField

MILLI_OF_SECOND

The milli-of-second.

This counts the millisecond within the second, from 0 to 999.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MICRO_OF_SECOND

to produce

NANO_OF_SECOND

.

This counts the millisecond within the second, from 0 to 999.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MICRO_OF_SECOND

to produce

NANO_OF_SECOND

.

This field is used to represent the milli-of-second handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_MINUTE

,

SECOND_OF_DAY

or

INSTANT_SECONDS

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MICRO_OF_SECOND

to produce

NANO_OF_SECOND

.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_SECOND

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MICRO_OF_SECOND

to produce

NANO_OF_SECOND

.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is resolved in combination with

MICRO_OF_SECOND

to produce

NANO_OF_SECOND

.

MILLI_OF_DAY

```java
public static final
ChronoField
MILLI_OF_DAY
```

The milli-of-day.

This counts the millisecond within the day, from 0 to (24 * 60 * 60 * 1,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MILLI_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

---

#### MILLI_OF_DAY

public static final

ChronoField

MILLI_OF_DAY

The milli-of-day.

This counts the millisecond within the day, from 0 to (24 * 60 * 60 * 1,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MILLI_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

This counts the millisecond within the day, from 0 to (24 * 60 * 60 * 1,000) - 1.
This field has the same meaning for all calendar systems.

This field is used to represent the milli-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MILLI_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

This field is used to represent the milli-of-day handling any fraction of the second.
Implementations of

TemporalAccessor

should provide a value for this field if
they can return a value for

SECOND_OF_DAY

filling unknown precision with zero.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MILLI_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

When this field is used for setting a value, it should behave in the same way as
setting

NANO_OF_DAY

with the value multiplied by 1,000,000.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MILLI_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MILLI_OF_SECOND

,

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

SECOND_OF_MINUTE

```java
public static final
ChronoField
SECOND_OF_MINUTE
```

The second-of-minute.

This counts the second within the minute, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

---

#### SECOND_OF_MINUTE

public static final

ChronoField

SECOND_OF_MINUTE

The second-of-minute.

This counts the second within the minute, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

This counts the second within the minute, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

SECOND_OF_DAY

```java
public static final
ChronoField
SECOND_OF_DAY
```

The second-of-day.

This counts the second within the day, from 0 to (24 * 60 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

---

#### SECOND_OF_DAY

public static final

ChronoField

SECOND_OF_DAY

The second-of-day.

This counts the second within the day, from 0 to (24 * 60 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

This counts the second within the day, from 0 to (24 * 60 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

SECOND_OF_MINUTE

,

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

MINUTE_OF_HOUR

```java
public static final
ChronoField
MINUTE_OF_HOUR
```

The minute-of-hour.

This counts the minute within the hour, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

---

#### MINUTE_OF_HOUR

public static final

ChronoField

MINUTE_OF_HOUR

The minute-of-hour.

This counts the minute within the hour, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

This counts the minute within the hour, from 0 to 59.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.

MINUTE_OF_DAY

```java
public static final
ChronoField
MINUTE_OF_DAY
```

The minute-of-day.

This counts the minute within the day, from 0 to (24 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

---

#### MINUTE_OF_DAY

public static final

ChronoField

MINUTE_OF_DAY

The minute-of-day.

This counts the minute within the day, from 0 to (24 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

This counts the minute within the day, from 0 to (24 * 60) - 1.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The value is split to form

MINUTE_OF_HOUR

and

HOUR_OF_DAY

fields.

HOUR_OF_AMPM

```java
public static final
ChronoField
HOUR_OF_AMPM
```

The hour-of-am-pm.

This counts the hour within the AM/PM, from 0 to 11.
This is the hour that would be observed on a standard 12-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 11 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

AMPM_OF_DAY

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

See

CLOCK_HOUR_OF_AMPM

for the related field that counts hours from 1 to 12.

---

#### HOUR_OF_AMPM

public static final

ChronoField

HOUR_OF_AMPM

The hour-of-am-pm.

This counts the hour within the AM/PM, from 0 to 11.
This is the hour that would be observed on a standard 12-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 11 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

AMPM_OF_DAY

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

See

CLOCK_HOUR_OF_AMPM

for the related field that counts hours from 1 to 12.

This counts the hour within the AM/PM, from 0 to 11.
This is the hour that would be observed on a standard 12-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 11 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

AMPM_OF_DAY

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

See

CLOCK_HOUR_OF_AMPM

for the related field that counts hours from 1 to 12.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 11 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

AMPM_OF_DAY

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

See

CLOCK_HOUR_OF_AMPM

for the related field that counts hours from 1 to 12.

See

CLOCK_HOUR_OF_AMPM

for the related field that counts hours from 1 to 12.

CLOCK_HOUR_OF_AMPM

```java
public static final
ChronoField
CLOCK_HOUR_OF_AMPM
```

The clock-hour-of-am-pm.

This counts the hour within the AM/PM, from 1 to 12.
This is the hour that would be observed on a standard 12-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 12 in strict mode and from
0 to 12 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_AMPM

with the same value,
unless the value is 12, in which case it is converted to 0.

See

HOUR_OF_AMPM

for the related field that counts hours from 0 to 11.

---

#### CLOCK_HOUR_OF_AMPM

public static final

ChronoField

CLOCK_HOUR_OF_AMPM

The clock-hour-of-am-pm.

This counts the hour within the AM/PM, from 1 to 12.
This is the hour that would be observed on a standard 12-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 12 in strict mode and from
0 to 12 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_AMPM

with the same value,
unless the value is 12, in which case it is converted to 0.

See

HOUR_OF_AMPM

for the related field that counts hours from 0 to 11.

This counts the hour within the AM/PM, from 1 to 12.
This is the hour that would be observed on a standard 12-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 12 in strict mode and from
0 to 12 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_AMPM

with the same value,
unless the value is 12, in which case it is converted to 0.

See

HOUR_OF_AMPM

for the related field that counts hours from 0 to 11.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 12 in strict mode and from
0 to 12 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_AMPM

with the same value,
unless the value is 12, in which case it is converted to 0.

See

HOUR_OF_AMPM

for the related field that counts hours from 0 to 11.

See

HOUR_OF_AMPM

for the related field that counts hours from 0 to 11.

HOUR_OF_DAY

```java
public static final
ChronoField
HOUR_OF_DAY
```

The hour-of-day.

This counts the hour within the day, from 0 to 23.
This is the hour that would be observed on a standard 24-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is combined with

MINUTE_OF_HOUR

,

SECOND_OF_MINUTE

and

NANO_OF_SECOND

to produce a

LocalTime

.
In lenient mode, any excess days are added to the parsed date, or
made available via

DateTimeFormatter.parsedExcessDays()

.

See

CLOCK_HOUR_OF_DAY

for the related field that counts hours from 1 to 24.

---

#### HOUR_OF_DAY

public static final

ChronoField

HOUR_OF_DAY

The hour-of-day.

This counts the hour within the day, from 0 to 23.
This is the hour that would be observed on a standard 24-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is combined with

MINUTE_OF_HOUR

,

SECOND_OF_MINUTE

and

NANO_OF_SECOND

to produce a

LocalTime

.
In lenient mode, any excess days are added to the parsed date, or
made available via

DateTimeFormatter.parsedExcessDays()

.

See

CLOCK_HOUR_OF_DAY

for the related field that counts hours from 1 to 24.

This counts the hour within the day, from 0 to 23.
This is the hour that would be observed on a standard 24-hour digital clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is combined with

MINUTE_OF_HOUR

,

SECOND_OF_MINUTE

and

NANO_OF_SECOND

to produce a

LocalTime

.
In lenient mode, any excess days are added to the parsed date, or
made available via

DateTimeFormatter.parsedExcessDays()

.

See

CLOCK_HOUR_OF_DAY

for the related field that counts hours from 1 to 24.

When parsing this field it behaves equivalent to the following:
The value is validated in strict and smart mode but not in lenient mode.
The field is combined with

MINUTE_OF_HOUR

,

SECOND_OF_MINUTE

and

NANO_OF_SECOND

to produce a

LocalTime

.
In lenient mode, any excess days are added to the parsed date, or
made available via

DateTimeFormatter.parsedExcessDays()

.

See

CLOCK_HOUR_OF_DAY

for the related field that counts hours from 1 to 24.

See

CLOCK_HOUR_OF_DAY

for the related field that counts hours from 1 to 24.

CLOCK_HOUR_OF_DAY

```java
public static final
ChronoField
CLOCK_HOUR_OF_DAY
```

The clock-hour-of-day.

This counts the hour within the day, from 1 to 24.
This is the hour that would be observed on a 24-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 24 in strict mode and from
0 to 24 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_DAY

with the same value,
unless the value is 24, in which case it is converted to 0.

See

HOUR_OF_DAY

for the related field that counts hours from 0 to 23.

---

#### CLOCK_HOUR_OF_DAY

public static final

ChronoField

CLOCK_HOUR_OF_DAY

The clock-hour-of-day.

This counts the hour within the day, from 1 to 24.
This is the hour that would be observed on a 24-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 24 in strict mode and from
0 to 24 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_DAY

with the same value,
unless the value is 24, in which case it is converted to 0.

See

HOUR_OF_DAY

for the related field that counts hours from 0 to 23.

This counts the hour within the day, from 1 to 24.
This is the hour that would be observed on a 24-hour analog wall clock.
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 24 in strict mode and from
0 to 24 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_DAY

with the same value,
unless the value is 24, in which case it is converted to 0.

See

HOUR_OF_DAY

for the related field that counts hours from 0 to 23.

When parsing this field it behaves equivalent to the following:
The value is validated from 1 to 24 in strict mode and from
0 to 24 in smart mode. In lenient mode the value is not validated.
The field is converted to an

HOUR_OF_DAY

with the same value,
unless the value is 24, in which case it is converted to 0.

See

HOUR_OF_DAY

for the related field that counts hours from 0 to 23.

See

HOUR_OF_DAY

for the related field that counts hours from 0 to 23.

AMPM_OF_DAY

```java
public static final
ChronoField
AMPM_OF_DAY
```

The am-pm-of-day.

This counts the AM/PM within the day, from 0 (AM) to 1 (PM).
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 1 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

HOUR_OF_AMPM

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

---

#### AMPM_OF_DAY

public static final

ChronoField

AMPM_OF_DAY

The am-pm-of-day.

This counts the AM/PM within the day, from 0 (AM) to 1 (PM).
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 1 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

HOUR_OF_AMPM

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

This counts the AM/PM within the day, from 0 (AM) to 1 (PM).
This field has the same meaning for all calendar systems.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 1 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

HOUR_OF_AMPM

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

When parsing this field it behaves equivalent to the following:
The value is validated from 0 to 1 in strict and smart mode.
In lenient mode the value is not validated. It is combined with

HOUR_OF_AMPM

to form

HOUR_OF_DAY

by multiplying
the {AMPM_OF_DAY} value by 12.

DAY_OF_WEEK

```java
public static final
ChronoField
DAY_OF_WEEK
```

The day-of-week, such as Tuesday.

This represents the standard concept of the day of the week.
In the default ISO calendar system, this has values from Monday (1) to Sunday (7).
The

DayOfWeek

class can be used to interpret the result.

Most non-ISO calendar systems also define a seven day week that aligns with ISO.
Those calendar systems must also use the same numbering system, from Monday (1) to
Sunday (7), which allows

DayOfWeek

to be used.

Calendar systems that do not have a standard seven day week should implement this field
if they have a similar concept of named or numbered days within a period similar
to a week. It is recommended that the numbering starts from 1.

---

#### DAY_OF_WEEK

public static final

ChronoField

DAY_OF_WEEK

The day-of-week, such as Tuesday.

This represents the standard concept of the day of the week.
In the default ISO calendar system, this has values from Monday (1) to Sunday (7).
The

DayOfWeek

class can be used to interpret the result.

Most non-ISO calendar systems also define a seven day week that aligns with ISO.
Those calendar systems must also use the same numbering system, from Monday (1) to
Sunday (7), which allows

DayOfWeek

to be used.

Calendar systems that do not have a standard seven day week should implement this field
if they have a similar concept of named or numbered days within a period similar
to a week. It is recommended that the numbering starts from 1.

This represents the standard concept of the day of the week.
In the default ISO calendar system, this has values from Monday (1) to Sunday (7).
The

DayOfWeek

class can be used to interpret the result.

Most non-ISO calendar systems also define a seven day week that aligns with ISO.
Those calendar systems must also use the same numbering system, from Monday (1) to
Sunday (7), which allows

DayOfWeek

to be used.

Calendar systems that do not have a standard seven day week should implement this field
if they have a similar concept of named or numbered days within a period similar
to a week. It is recommended that the numbering starts from 1.

Most non-ISO calendar systems also define a seven day week that aligns with ISO.
Those calendar systems must also use the same numbering system, from Monday (1) to
Sunday (7), which allows

DayOfWeek

to be used.

Calendar systems that do not have a standard seven day week should implement this field
if they have a similar concept of named or numbered days within a period similar
to a week. It is recommended that the numbering starts from 1.

Calendar systems that do not have a standard seven day week should implement this field
if they have a similar concept of named or numbered days within a period similar
to a week. It is recommended that the numbering starts from 1.

ALIGNED_DAY_OF_WEEK_IN_MONTH

```java
public static final
ChronoField
ALIGNED_DAY_OF_WEEK_IN_MONTH
```

The aligned day-of-week within a month.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_WEEK_OF_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-month 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-month 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

---

#### ALIGNED_DAY_OF_WEEK_IN_MONTH

public static final

ChronoField

ALIGNED_DAY_OF_WEEK_IN_MONTH

The aligned day-of-week within a month.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_WEEK_OF_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-month 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-month 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_WEEK_OF_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-month 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-month 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-month 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-month 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

ALIGNED_DAY_OF_WEEK_IN_YEAR

```java
public static final
ChronoField
ALIGNED_DAY_OF_WEEK_IN_YEAR
```

The aligned day-of-week within a year.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_WEEK_OF_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-year 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-year 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

---

#### ALIGNED_DAY_OF_WEEK_IN_YEAR

public static final

ChronoField

ALIGNED_DAY_OF_WEEK_IN_YEAR

The aligned day-of-week within a year.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_WEEK_OF_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-year 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-year 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

This represents concept of the count of days within the period of a week
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_WEEK_OF_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-year 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-year 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Within each of these aligned-weeks, the days are numbered from 1 to 7 and returned
as the value of this field.
As such, day-of-year 1 to 7 will have aligned-day-of-week values from 1 to 7.
And day-of-year 8 to 14 will repeat this with aligned-day-of-week values from 1 to 7.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

DAY_OF_MONTH

```java
public static final
ChronoField
DAY_OF_MONTH
```

The day-of-month.

This represents the concept of the day within the month.
In the default ISO calendar system, this has values from 1 to 31 in most months.
April, June, September, November have days from 1 to 30, while February has days
from 1 to 28, or 29 in a leap year.

Non-ISO calendar systems should implement this field using the most recognized
day-of-month values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the month.

---

#### DAY_OF_MONTH

public static final

ChronoField

DAY_OF_MONTH

The day-of-month.

This represents the concept of the day within the month.
In the default ISO calendar system, this has values from 1 to 31 in most months.
April, June, September, November have days from 1 to 30, while February has days
from 1 to 28, or 29 in a leap year.

Non-ISO calendar systems should implement this field using the most recognized
day-of-month values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the month.

This represents the concept of the day within the month.
In the default ISO calendar system, this has values from 1 to 31 in most months.
April, June, September, November have days from 1 to 30, while February has days
from 1 to 28, or 29 in a leap year.

Non-ISO calendar systems should implement this field using the most recognized
day-of-month values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the month.

Non-ISO calendar systems should implement this field using the most recognized
day-of-month values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the month.

DAY_OF_YEAR

```java
public static final
ChronoField
DAY_OF_YEAR
```

The day-of-year.

This represents the concept of the day within the year.
In the default ISO calendar system, this has values from 1 to 365 in standard
years and 1 to 366 in leap years.

Non-ISO calendar systems should implement this field using the most recognized
day-of-year values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the year.

Note that a non-ISO calendar system may have year numbering system that changes
at a different point to the natural reset in the month numbering. An example
of this is the Japanese calendar system where a change of era, which resets
the year number to 1, can happen on any date. The era and year reset also cause
the day-of-year to be reset to 1, but not the month-of-year or day-of-month.

---

#### DAY_OF_YEAR

public static final

ChronoField

DAY_OF_YEAR

The day-of-year.

This represents the concept of the day within the year.
In the default ISO calendar system, this has values from 1 to 365 in standard
years and 1 to 366 in leap years.

Non-ISO calendar systems should implement this field using the most recognized
day-of-year values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the year.

Note that a non-ISO calendar system may have year numbering system that changes
at a different point to the natural reset in the month numbering. An example
of this is the Japanese calendar system where a change of era, which resets
the year number to 1, can happen on any date. The era and year reset also cause
the day-of-year to be reset to 1, but not the month-of-year or day-of-month.

This represents the concept of the day within the year.
In the default ISO calendar system, this has values from 1 to 365 in standard
years and 1 to 366 in leap years.

Non-ISO calendar systems should implement this field using the most recognized
day-of-year values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the year.

Note that a non-ISO calendar system may have year numbering system that changes
at a different point to the natural reset in the month numbering. An example
of this is the Japanese calendar system where a change of era, which resets
the year number to 1, can happen on any date. The era and year reset also cause
the day-of-year to be reset to 1, but not the month-of-year or day-of-month.

Non-ISO calendar systems should implement this field using the most recognized
day-of-year values for users of the calendar system.
Normally, this is a count of days from 1 to the length of the year.

Note that a non-ISO calendar system may have year numbering system that changes
at a different point to the natural reset in the month numbering. An example
of this is the Japanese calendar system where a change of era, which resets
the year number to 1, can happen on any date. The era and year reset also cause
the day-of-year to be reset to 1, but not the month-of-year or day-of-month.

Note that a non-ISO calendar system may have year numbering system that changes
at a different point to the natural reset in the month numbering. An example
of this is the Japanese calendar system where a change of era, which resets
the year number to 1, can happen on any date. The era and year reset also cause
the day-of-year to be reset to 1, but not the month-of-year or day-of-month.

EPOCH_DAY

```java
public static final
ChronoField
EPOCH_DAY
```

The epoch-day, based on the Java epoch of 1970-01-01 (ISO).

This field is the sequential count of days where 1970-01-01 (ISO) is zero.
Note that this uses the

local

time-line, ignoring offset and time-zone.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

Range of EpochDay is between (LocalDate.MIN.toEpochDay(), LocalDate.MAX.toEpochDay())
both inclusive.

---

#### EPOCH_DAY

public static final

ChronoField

EPOCH_DAY

The epoch-day, based on the Java epoch of 1970-01-01 (ISO).

This field is the sequential count of days where 1970-01-01 (ISO) is zero.
Note that this uses the

local

time-line, ignoring offset and time-zone.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

Range of EpochDay is between (LocalDate.MIN.toEpochDay(), LocalDate.MAX.toEpochDay())
both inclusive.

This field is the sequential count of days where 1970-01-01 (ISO) is zero.
Note that this uses the

local

time-line, ignoring offset and time-zone.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

Range of EpochDay is between (LocalDate.MIN.toEpochDay(), LocalDate.MAX.toEpochDay())
both inclusive.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

Range of EpochDay is between (LocalDate.MIN.toEpochDay(), LocalDate.MAX.toEpochDay())
both inclusive.

Range of EpochDay is between (LocalDate.MIN.toEpochDay(), LocalDate.MAX.toEpochDay())
both inclusive.

ALIGNED_WEEK_OF_MONTH

```java
public static final
ChronoField
ALIGNED_WEEK_OF_MONTH
```

The aligned week within a month.

This represents concept of the count of weeks within the period of a month
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Thus, day-of-month values 1 to 7 are in aligned-week 1, while day-of-month values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

---

#### ALIGNED_WEEK_OF_MONTH

public static final

ChronoField

ALIGNED_WEEK_OF_MONTH

The aligned week within a month.

This represents concept of the count of weeks within the period of a month
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Thus, day-of-month values 1 to 7 are in aligned-week 1, while day-of-month values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

This represents concept of the count of weeks within the period of a month
where the weeks are aligned to the start of the month.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_MONTH

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Thus, day-of-month values 1 to 7 are in aligned-week 1, while day-of-month values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

For example, in a calendar systems with a seven day week, the first aligned-week-of-month
starts on day-of-month 1, the second aligned-week starts on day-of-month 8, and so on.
Thus, day-of-month values 1 to 7 are in aligned-week 1, while day-of-month values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

ALIGNED_WEEK_OF_YEAR

```java
public static final
ChronoField
ALIGNED_WEEK_OF_YEAR
```

The aligned week within a year.

This represents concept of the count of weeks within the period of a year
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Thus, day-of-year values 1 to 7 are in aligned-week 1, while day-of-year values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

---

#### ALIGNED_WEEK_OF_YEAR

public static final

ChronoField

ALIGNED_WEEK_OF_YEAR

The aligned week within a year.

This represents concept of the count of weeks within the period of a year
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Thus, day-of-year values 1 to 7 are in aligned-week 1, while day-of-year values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

This represents concept of the count of weeks within the period of a year
where the weeks are aligned to the start of the year.
This field is typically used with

ALIGNED_DAY_OF_WEEK_IN_YEAR

.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Thus, day-of-year values 1 to 7 are in aligned-week 1, while day-of-year values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

For example, in a calendar systems with a seven day week, the first aligned-week-of-year
starts on day-of-year 1, the second aligned-week starts on day-of-year 8, and so on.
Thus, day-of-year values 1 to 7 are in aligned-week 1, while day-of-year values
8 to 14 are in aligned-week 2, and so on.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

Calendar systems that do not have a seven day week should typically implement this
field in the same way, but using the alternate week length.

MONTH_OF_YEAR

```java
public static final
ChronoField
MONTH_OF_YEAR
```

The month-of-year, such as March.

This represents the concept of the month within the year.
In the default ISO calendar system, this has values from January (1) to December (12).

Non-ISO calendar systems should implement this field using the most recognized
month-of-year values for users of the calendar system.
Normally, this is a count of months starting from 1.

---

#### MONTH_OF_YEAR

public static final

ChronoField

MONTH_OF_YEAR

The month-of-year, such as March.

This represents the concept of the month within the year.
In the default ISO calendar system, this has values from January (1) to December (12).

Non-ISO calendar systems should implement this field using the most recognized
month-of-year values for users of the calendar system.
Normally, this is a count of months starting from 1.

This represents the concept of the month within the year.
In the default ISO calendar system, this has values from January (1) to December (12).

Non-ISO calendar systems should implement this field using the most recognized
month-of-year values for users of the calendar system.
Normally, this is a count of months starting from 1.

Non-ISO calendar systems should implement this field using the most recognized
month-of-year values for users of the calendar system.
Normally, this is a count of months starting from 1.

PROLEPTIC_MONTH

```java
public static final
ChronoField
PROLEPTIC_MONTH
```

The proleptic-month based, counting months sequentially from year 0.

This field is the sequential count of months where the first month
in proleptic-year zero has the value zero.
Later months have increasingly larger values.
Earlier months have increasingly small values.
There are no gaps or breaks in the sequence of months.
Note that this uses the

local

time-line, ignoring offset and time-zone.

In the default ISO calendar system, June 2012 would have the value

(2012 * 12 + 6 - 1)

. This field is primarily for internal use.

Non-ISO calendar systems must implement this field as per the definition above.
It is just a simple zero-based count of elapsed months from the start of proleptic-year 0.
All calendar systems with a full proleptic-year definition will have a year zero.
If the calendar system has a minimum year that excludes year zero, then one must
be extrapolated in order for this method to be defined.

---

#### PROLEPTIC_MONTH

public static final

ChronoField

PROLEPTIC_MONTH

The proleptic-month based, counting months sequentially from year 0.

This field is the sequential count of months where the first month
in proleptic-year zero has the value zero.
Later months have increasingly larger values.
Earlier months have increasingly small values.
There are no gaps or breaks in the sequence of months.
Note that this uses the

local

time-line, ignoring offset and time-zone.

In the default ISO calendar system, June 2012 would have the value

(2012 * 12 + 6 - 1)

. This field is primarily for internal use.

Non-ISO calendar systems must implement this field as per the definition above.
It is just a simple zero-based count of elapsed months from the start of proleptic-year 0.
All calendar systems with a full proleptic-year definition will have a year zero.
If the calendar system has a minimum year that excludes year zero, then one must
be extrapolated in order for this method to be defined.

This field is the sequential count of months where the first month
in proleptic-year zero has the value zero.
Later months have increasingly larger values.
Earlier months have increasingly small values.
There are no gaps or breaks in the sequence of months.
Note that this uses the

local

time-line, ignoring offset and time-zone.

In the default ISO calendar system, June 2012 would have the value

(2012 * 12 + 6 - 1)

. This field is primarily for internal use.

Non-ISO calendar systems must implement this field as per the definition above.
It is just a simple zero-based count of elapsed months from the start of proleptic-year 0.
All calendar systems with a full proleptic-year definition will have a year zero.
If the calendar system has a minimum year that excludes year zero, then one must
be extrapolated in order for this method to be defined.

In the default ISO calendar system, June 2012 would have the value

(2012 * 12 + 6 - 1)

. This field is primarily for internal use.

Non-ISO calendar systems must implement this field as per the definition above.
It is just a simple zero-based count of elapsed months from the start of proleptic-year 0.
All calendar systems with a full proleptic-year definition will have a year zero.
If the calendar system has a minimum year that excludes year zero, then one must
be extrapolated in order for this method to be defined.

Non-ISO calendar systems must implement this field as per the definition above.
It is just a simple zero-based count of elapsed months from the start of proleptic-year 0.
All calendar systems with a full proleptic-year definition will have a year zero.
If the calendar system has a minimum year that excludes year zero, then one must
be extrapolated in order for this method to be defined.

YEAR_OF_ERA

```java
public static final
ChronoField
YEAR_OF_ERA
```

The year within the era.

This represents the concept of the year within the era.
This field is typically used with

ERA

.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.

For example, subtracting a year each time yield the following:

- year-proleptic 2 = 'CE' year-of-era 2

- year-proleptic 1 = 'CE' year-of-era 1

- year-proleptic 0 = 'BCE' year-of-era 1

- year-proleptic -1 = 'BCE' year-of-era 2

Note that the ISO-8601 standard does not actually define eras.
Note also that the ISO eras do not align with the well-known AD/BC eras due to the
change between the Julian and Gregorian calendar systems.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

---

#### YEAR_OF_ERA

public static final

ChronoField

YEAR_OF_ERA

The year within the era.

This represents the concept of the year within the era.
This field is typically used with

ERA

.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.

For example, subtracting a year each time yield the following:

- year-proleptic 2 = 'CE' year-of-era 2

- year-proleptic 1 = 'CE' year-of-era 1

- year-proleptic 0 = 'BCE' year-of-era 1

- year-proleptic -1 = 'BCE' year-of-era 2

Note that the ISO-8601 standard does not actually define eras.
Note also that the ISO eras do not align with the well-known AD/BC eras due to the
change between the Julian and Gregorian calendar systems.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

This represents the concept of the year within the era.
This field is typically used with

ERA

.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.

For example, subtracting a year each time yield the following:

- year-proleptic 2 = 'CE' year-of-era 2

- year-proleptic 1 = 'CE' year-of-era 1

- year-proleptic 0 = 'BCE' year-of-era 1

- year-proleptic -1 = 'BCE' year-of-era 2

Note that the ISO-8601 standard does not actually define eras.
Note also that the ISO eras do not align with the well-known AD/BC eras due to the
change between the Julian and Gregorian calendar systems.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.

For example, subtracting a year each time yield the following:

- year-proleptic 2 = 'CE' year-of-era 2

- year-proleptic 1 = 'CE' year-of-era 1

- year-proleptic 0 = 'BCE' year-of-era 1

- year-proleptic -1 = 'BCE' year-of-era 2

Note that the ISO-8601 standard does not actually define eras.
Note also that the ISO eras do not align with the well-known AD/BC eras due to the
change between the Julian and Gregorian calendar systems.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.

For example, subtracting a year each time yield the following:

- year-proleptic 2 = 'CE' year-of-era 2

- year-proleptic 1 = 'CE' year-of-era 1

- year-proleptic 0 = 'BCE' year-of-era 1

- year-proleptic -1 = 'BCE' year-of-era 2

Note that the ISO-8601 standard does not actually define eras.
Note also that the ISO eras do not align with the well-known AD/BC eras due to the
change between the Julian and Gregorian calendar systems.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

For example, subtracting a year each time yield the following:

- year-proleptic 2 = 'CE' year-of-era 2

- year-proleptic 1 = 'CE' year-of-era 1

- year-proleptic 0 = 'BCE' year-of-era 1

- year-proleptic -1 = 'BCE' year-of-era 2

Note that the ISO-8601 standard does not actually define eras.
Note also that the ISO eras do not align with the well-known AD/BC eras due to the
change between the Julian and Gregorian calendar systems.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

Note that the ISO-8601 standard does not actually define eras.
Note also that the ISO eras do not align with the well-known AD/BC eras due to the
change between the Julian and Gregorian calendar systems.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

Non-ISO calendar systems should implement this field using the most recognized
year-of-era value for users of the calendar system.
Since most calendar systems have only two eras, the year-of-era numbering approach
will typically be the same as that used by the ISO calendar system.
The year-of-era value should typically always be positive, however this is not required.

YEAR

```java
public static final
ChronoField
YEAR
```

The proleptic year, such as 2012.

This represents the concept of the year, counting sequentially and using negative numbers.
The proleptic year is not interpreted in terms of the era.
See

YEAR_OF_ERA

for an example showing the mapping from proleptic year to year-of-era.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR_OF_ERA

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

Non-ISO calendar systems should implement this field as follows.
If the calendar system has only two eras, before and after a fixed date, then the
proleptic-year value must be the same as the year-of-era value for the later era,
and increasingly negative for the earlier era.
If the calendar system has more than two eras, then the proleptic-year value may be
defined with any appropriate value, although defining it to be the same as ISO may be
the best option.

---

#### YEAR

public static final

ChronoField

YEAR

The proleptic year, such as 2012.

This represents the concept of the year, counting sequentially and using negative numbers.
The proleptic year is not interpreted in terms of the era.
See

YEAR_OF_ERA

for an example showing the mapping from proleptic year to year-of-era.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR_OF_ERA

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

Non-ISO calendar systems should implement this field as follows.
If the calendar system has only two eras, before and after a fixed date, then the
proleptic-year value must be the same as the year-of-era value for the later era,
and increasingly negative for the earlier era.
If the calendar system has more than two eras, then the proleptic-year value may be
defined with any appropriate value, although defining it to be the same as ISO may be
the best option.

This represents the concept of the year, counting sequentially and using negative numbers.
The proleptic year is not interpreted in terms of the era.
See

YEAR_OF_ERA

for an example showing the mapping from proleptic year to year-of-era.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR_OF_ERA

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

Non-ISO calendar systems should implement this field as follows.
If the calendar system has only two eras, before and after a fixed date, then the
proleptic-year value must be the same as the year-of-era value for the later era,
and increasingly negative for the earlier era.
If the calendar system has more than two eras, then the proleptic-year value may be
defined with any appropriate value, although defining it to be the same as ISO may be
the best option.

The standard mental model for a date is based on three concepts - year, month and day.
These map onto the

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Note that there is no reference to eras.
The full model for a date requires four concepts - era, year, month and day. These map onto
the

ERA

,

YEAR_OF_ERA

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

fields.
Whether this field or

YEAR_OF_ERA

is used depends on which mental model is being used.
See

ChronoLocalDate

for more discussion on this topic.

Non-ISO calendar systems should implement this field as follows.
If the calendar system has only two eras, before and after a fixed date, then the
proleptic-year value must be the same as the year-of-era value for the later era,
and increasingly negative for the earlier era.
If the calendar system has more than two eras, then the proleptic-year value may be
defined with any appropriate value, although defining it to be the same as ISO may be
the best option.

Non-ISO calendar systems should implement this field as follows.
If the calendar system has only two eras, before and after a fixed date, then the
proleptic-year value must be the same as the year-of-era value for the later era,
and increasingly negative for the earlier era.
If the calendar system has more than two eras, then the proleptic-year value may be
defined with any appropriate value, although defining it to be the same as ISO may be
the best option.

ERA

```java
public static final
ChronoField
ERA
```

The era.

This represents the concept of the era, which is the largest division of the time-line.
This field is typically used with

YEAR_OF_ERA

.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.
See

YEAR_OF_ERA

for a full example.

Non-ISO calendar systems should implement this field to define eras.
The value of the era that was active on 1970-01-01 (ISO) must be assigned the value 1.
Earlier eras must have sequentially smaller values.
Later eras must have sequentially larger values,

---

#### ERA

public static final

ChronoField

ERA

The era.

This represents the concept of the era, which is the largest division of the time-line.
This field is typically used with

YEAR_OF_ERA

.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.
See

YEAR_OF_ERA

for a full example.

Non-ISO calendar systems should implement this field to define eras.
The value of the era that was active on 1970-01-01 (ISO) must be assigned the value 1.
Earlier eras must have sequentially smaller values.
Later eras must have sequentially larger values,

This represents the concept of the era, which is the largest division of the time-line.
This field is typically used with

YEAR_OF_ERA

.

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.
See

YEAR_OF_ERA

for a full example.

Non-ISO calendar systems should implement this field to define eras.
The value of the era that was active on 1970-01-01 (ISO) must be assigned the value 1.
Earlier eras must have sequentially smaller values.
Later eras must have sequentially larger values,

In the default ISO calendar system, there are two eras defined, 'BCE' and 'CE'.
The era 'CE' is the one currently in use and year-of-era runs from 1 to the maximum value.
The era 'BCE' is the previous era, and the year-of-era runs backwards.
See

YEAR_OF_ERA

for a full example.

Non-ISO calendar systems should implement this field to define eras.
The value of the era that was active on 1970-01-01 (ISO) must be assigned the value 1.
Earlier eras must have sequentially smaller values.
Later eras must have sequentially larger values,

Non-ISO calendar systems should implement this field to define eras.
The value of the era that was active on 1970-01-01 (ISO) must be assigned the value 1.
Earlier eras must have sequentially smaller values.
Later eras must have sequentially larger values,

INSTANT_SECONDS

```java
public static final
ChronoField
INSTANT_SECONDS
```

The instant epoch-seconds.

This represents the concept of the sequential count of seconds where
1970-01-01T00:00Z (ISO) is zero.
This field may be used with

NANO_OF_SECOND

to represent the fraction of the second.

An

Instant

represents an instantaneous point on the time-line.
On their own, an instant has insufficient information to allow a local date-time to be obtained.
Only when paired with an offset or time-zone can the local date or time be calculated.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

---

#### INSTANT_SECONDS

public static final

ChronoField

INSTANT_SECONDS

The instant epoch-seconds.

This represents the concept of the sequential count of seconds where
1970-01-01T00:00Z (ISO) is zero.
This field may be used with

NANO_OF_SECOND

to represent the fraction of the second.

An

Instant

represents an instantaneous point on the time-line.
On their own, an instant has insufficient information to allow a local date-time to be obtained.
Only when paired with an offset or time-zone can the local date or time be calculated.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

This represents the concept of the sequential count of seconds where
1970-01-01T00:00Z (ISO) is zero.
This field may be used with

NANO_OF_SECOND

to represent the fraction of the second.

An

Instant

represents an instantaneous point on the time-line.
On their own, an instant has insufficient information to allow a local date-time to be obtained.
Only when paired with an offset or time-zone can the local date or time be calculated.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

An

Instant

represents an instantaneous point on the time-line.
On their own, an instant has insufficient information to allow a local date-time to be obtained.
Only when paired with an offset or time-zone can the local date or time be calculated.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

OFFSET_SECONDS

```java
public static final
ChronoField
OFFSET_SECONDS
```

The offset from UTC/Greenwich.

This represents the concept of the offset in seconds of local time from UTC/Greenwich.

A

ZoneOffset

represents the period of time that local time differs from UTC/Greenwich.
This is usually a fixed number of hours and minutes.
It is equivalent to the

total amount

of the offset in seconds.
For example, during the winter Paris has an offset of

+01:00

, which is 3600 seconds.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

---

#### OFFSET_SECONDS

public static final

ChronoField

OFFSET_SECONDS

The offset from UTC/Greenwich.

This represents the concept of the offset in seconds of local time from UTC/Greenwich.

A

ZoneOffset

represents the period of time that local time differs from UTC/Greenwich.
This is usually a fixed number of hours and minutes.
It is equivalent to the

total amount

of the offset in seconds.
For example, during the winter Paris has an offset of

+01:00

, which is 3600 seconds.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

This represents the concept of the offset in seconds of local time from UTC/Greenwich.

A

ZoneOffset

represents the period of time that local time differs from UTC/Greenwich.
This is usually a fixed number of hours and minutes.
It is equivalent to the

total amount

of the offset in seconds.
For example, during the winter Paris has an offset of

+01:00

, which is 3600 seconds.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

A

ZoneOffset

represents the period of time that local time differs from UTC/Greenwich.
This is usually a fixed number of hours and minutes.
It is equivalent to the

total amount

of the offset in seconds.
For example, during the winter Paris has an offset of

+01:00

, which is 3600 seconds.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

This field is strictly defined to have the same meaning in all calendar systems.
This is necessary to ensure interoperation between calendars.

Method Detail

- values

```java
public static
ChronoField
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoField c : ChronoField.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ChronoField
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

- range

```java
public
ValueRange
range()
```

Gets the range of valid values for the field.

All fields can be expressed as a

long

integer.
This method returns an object that describes the valid range for that value.

This method returns the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

Note that the result only describes the minimum and maximum valid values
and it is important not to read too much into them. For example, there
could be values within the range that are invalid for the field.

**Specified by:** range

in interface

TemporalField
**Returns:** the range of valid values for the field, not null

- isDateBased

```java
public boolean isDateBased()
```

Checks if this field represents a component of a date.

Fields from day-of-week to era are date-based.

**Specified by:** isDateBased

in interface

TemporalField
**Returns:** true if it is a component of a date

- isTimeBased

```java
public boolean isTimeBased()
```

Checks if this field represents a component of a time.

Fields from nano-of-second to am-pm-of-day are time-based.

**Specified by:** isTimeBased

in interface

TemporalField
**Returns:** true if it is a component of a time

- checkValidValue

```java
public long checkValidValue​(long value)
```

Checks that the specified value is valid for this field.

This validates that the value is within the outer range of valid values
returned by

range()

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

**Parameters:** value

- the value to check
**Returns:** the value that was passed in

- checkValidIntValue

```java
public int checkValidIntValue​(long value)
```

Checks that the specified value is valid and fits in an

int

.

This validates that the value is within the outer range of valid values
returned by

range()

.
It also checks that all valid values are within the bounds of an

int

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

**Parameters:** value

- the value to check
**Returns:** the value that was passed in

---

#### Method Detail

values

```java
public static
ChronoField
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoField c : ChronoField.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ChronoField

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ChronoField c : ChronoField.values())
System.out.println(c);
```

for (ChronoField c : ChronoField.values())
System.out.println(c);

valueOf

```java
public static
ChronoField
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

ChronoField

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

range

```java
public
ValueRange
range()
```

Gets the range of valid values for the field.

All fields can be expressed as a

long

integer.
This method returns an object that describes the valid range for that value.

This method returns the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

Note that the result only describes the minimum and maximum valid values
and it is important not to read too much into them. For example, there
could be values within the range that are invalid for the field.

**Specified by:** range

in interface

TemporalField
**Returns:** the range of valid values for the field, not null

---

#### range

public

ValueRange

range()

Gets the range of valid values for the field.

All fields can be expressed as a

long

integer.
This method returns an object that describes the valid range for that value.

This method returns the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

Note that the result only describes the minimum and maximum valid values
and it is important not to read too much into them. For example, there
could be values within the range that are invalid for the field.

All fields can be expressed as a

long

integer.
This method returns an object that describes the valid range for that value.

This method returns the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

Note that the result only describes the minimum and maximum valid values
and it is important not to read too much into them. For example, there
could be values within the range that are invalid for the field.

This method returns the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

Note that the result only describes the minimum and maximum valid values
and it is important not to read too much into them. For example, there
could be values within the range that are invalid for the field.

Note that the result only describes the minimum and maximum valid values
and it is important not to read too much into them. For example, there
could be values within the range that are invalid for the field.

isDateBased

```java
public boolean isDateBased()
```

Checks if this field represents a component of a date.

Fields from day-of-week to era are date-based.

**Specified by:** isDateBased

in interface

TemporalField
**Returns:** true if it is a component of a date

---

#### isDateBased

public boolean isDateBased()

Checks if this field represents a component of a date.

Fields from day-of-week to era are date-based.

Fields from day-of-week to era are date-based.

isTimeBased

```java
public boolean isTimeBased()
```

Checks if this field represents a component of a time.

Fields from nano-of-second to am-pm-of-day are time-based.

**Specified by:** isTimeBased

in interface

TemporalField
**Returns:** true if it is a component of a time

---

#### isTimeBased

public boolean isTimeBased()

Checks if this field represents a component of a time.

Fields from nano-of-second to am-pm-of-day are time-based.

Fields from nano-of-second to am-pm-of-day are time-based.

checkValidValue

```java
public long checkValidValue​(long value)
```

Checks that the specified value is valid for this field.

This validates that the value is within the outer range of valid values
returned by

range()

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

**Parameters:** value

- the value to check
**Returns:** the value that was passed in

---

#### checkValidValue

public long checkValidValue​(long value)

Checks that the specified value is valid for this field.

This validates that the value is within the outer range of valid values
returned by

range()

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

This validates that the value is within the outer range of valid values
returned by

range()

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

checkValidIntValue

```java
public int checkValidIntValue​(long value)
```

Checks that the specified value is valid and fits in an

int

.

This validates that the value is within the outer range of valid values
returned by

range()

.
It also checks that all valid values are within the bounds of an

int

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

**Parameters:** value

- the value to check
**Returns:** the value that was passed in

---

#### checkValidIntValue

public int checkValidIntValue​(long value)

Checks that the specified value is valid and fits in an

int

.

This validates that the value is within the outer range of valid values
returned by

range()

.
It also checks that all valid values are within the bounds of an

int

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

This validates that the value is within the outer range of valid values
returned by

range()

.
It also checks that all valid values are within the bounds of an

int

.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

This method checks against the range of the field in the ISO-8601 calendar system.
This range may be incorrect for other calendar systems.
Use

Chronology.range(ChronoField)

to access the correct range
for a different calendar system.

---

