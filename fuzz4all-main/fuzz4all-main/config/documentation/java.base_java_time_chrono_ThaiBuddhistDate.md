# Class ThaiBuddhistDate

**Source:** `java.base\java\time\chrono\ThaiBuddhistDate.html`

### Class Description

```java
public final class
ThaiBuddhistDate

extends
Object

implements
ChronoLocalDate
,
Serializable
```

A date in the Thai Buddhist calendar system.

This date operates using the

Thai Buddhist calendar

.
This calendar system is primarily used in Thailand.
Dates are aligned such that

2484-01-01 (Buddhist)

is

1941-01-01 (ISO)

.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

ThaiBuddhistDate

may have unpredictable results and should be avoided.
The

equals

method should be used for comparisons.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ChronoLocalDate

>

,

ChronoLocalDate

,

Temporal

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
ThaiBuddhistDate
now()

Obtains the current

ThaiBuddhistDate

from the system clock in the default time-zone.

This will query the

system clock

in the default
time-zone to obtain the current date.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

**Returns:**
- the current date using the system clock and default time-zone, not null

---

#### public static
ThaiBuddhistDate
now​(
ZoneId
zone)

Obtains the current

ThaiBuddhistDate

from the system clock in the specified time-zone.

This will query the

system clock

to obtain the current date.
Specifying the time-zone avoids dependence on the default time-zone.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

**Parameters:**
- zone

- the zone ID to use, not null

**Returns:**
- the current date using the system clock, not null

---

#### public static
ThaiBuddhistDate
now​(
Clock
clock)

Obtains the current

ThaiBuddhistDate

from the specified clock.

This will query the specified clock to obtain the current date - today.
Using this method allows the use of an alternate clock for testing.
The alternate clock may be introduced using

dependency injection

.

**Parameters:**
- clock

- the clock to use, not null

**Returns:**
- the current date, not null

**Throws:**
- DateTimeException

- if the current date cannot be obtained

---

#### public static
ThaiBuddhistDate
of​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a

ThaiBuddhistDate

representing a date in the Thai Buddhist calendar
system from the proleptic-year, month-of-year and day-of-month fields.

This returns a

ThaiBuddhistDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

**Parameters:**
- prolepticYear

- the Thai Buddhist proleptic-year
- month

- the Thai Buddhist month-of-year, from 1 to 12
- dayOfMonth

- the Thai Buddhist day-of-month, from 1 to 31

**Returns:**
- the date in Thai Buddhist calendar system, not null

**Throws:**
- DateTimeException

- if the value of any field is out of range,
or if the day-of-month is invalid for the month-year

---

#### public static
ThaiBuddhistDate
from​(
TemporalAccessor
temporal)

Obtains a

ThaiBuddhistDate

from a temporal object.

This obtains a date in the Thai Buddhist calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

ThaiBuddhistDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

ThaiBuddhistDate::from

.

**Parameters:**
- temporal

- the temporal object to convert, not null

**Returns:**
- the date in Thai Buddhist calendar system, not null

**Throws:**
- DateTimeException

- if unable to convert to a

ThaiBuddhistDate

**See Also:**
- Chronology.date(TemporalAccessor)

---

#### public
ThaiBuddhistChronology
getChronology()

Gets the chronology of this date, which is the Thai Buddhist calendar system.

The

Chronology

represents the calendar system in use.
The era and other fields in

ChronoField

are defined by the chronology.

**Specified by:**
- getChronology

in interface

ChronoLocalDate

**Returns:**
- the Thai Buddhist chronology, not null

---

#### public
ThaiBuddhistEra
getEra()

Gets the era applicable at this date.

The Thai Buddhist calendar system has two eras, 'BE' and 'BEFORE_BE',
defined by

ThaiBuddhistEra

.

**Specified by:**
- getEra

in interface

ChronoLocalDate

**Returns:**
- the era applicable at this date, not null

---

#### public int lengthOfMonth()

Returns the length of the month represented by this date.

This returns the length of the month in days.
Month lengths match those of the ISO calendar system.

**Specified by:**
- lengthOfMonth

in interface

ChronoLocalDate

**Returns:**
- the length of the month in days

---

#### public
ThaiBuddhistDate
with​(
TemporalAdjuster
adjuster)

Returns an adjusted object of the same type as this object with the adjustment made.

This adjusts this date-time according to the rules of the specified adjuster.
A simple adjuster might simply set the one of the fields, such as the year field.
A more complex adjuster might set the date to the last day of the month.
A selection of common adjustments is provided in

TemporalAdjusters

.
These include finding the "last day of the month" and "next Wednesday".
The adjuster is responsible for handling special cases, such as the varying
lengths of month and leap years.

Some example code indicating how and why this method is used:

```java
date = date.with(Month.JULY); // most key classes implement TemporalAdjuster
date = date.with(lastDayOfMonth()); // static import from Adjusters
date = date.with(next(WEDNESDAY)); // static import from Adjusters and DayOfWeek
```

**Specified by:**
- with

in interface

ChronoLocalDate
- with

in interface

Temporal

**Parameters:**
- adjuster

- the adjuster to use, not null

**Returns:**
- an object of the same type with the specified adjustment made, not null

**Throws:**
- DateTimeException

- if unable to make the adjustment
- ArithmeticException

- if numeric overflow occurs

---

#### public
ThaiBuddhistDate
plus​(
TemporalAmount
amount)

Returns an object of the same type as this object with an amount added.

This adjusts this temporal, adding according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.plus(period); // add a Period instance
date = date.plus(duration); // add a Duration instance
date = date.plus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

**Specified by:**
- plus

in interface

ChronoLocalDate
- plus

in interface

Temporal

**Parameters:**
- amount

- the amount to add, not null

**Returns:**
- an object of the same type with the specified adjustment made, not null

**Throws:**
- DateTimeException

- if the addition cannot be made
- ArithmeticException

- if numeric overflow occurs

---

#### public
ThaiBuddhistDate
minus​(
TemporalAmount
amount)

Returns an object of the same type as this object with an amount subtracted.

This adjusts this temporal, subtracting according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.minus(period); // subtract a Period instance
date = date.minus(duration); // subtract a Duration instance
date = date.minus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

**Specified by:**
- minus

in interface

ChronoLocalDate
- minus

in interface

Temporal

**Parameters:**
- amount

- the amount to subtract, not null

**Returns:**
- an object of the same type with the specified adjustment made, not null

**Throws:**
- DateTimeException

- if the subtraction cannot be made
- ArithmeticException

- if numeric overflow occurs

---

#### public boolean equals​(
Object
obj)

Compares this date to another date, including the chronology.

Compares this

ThaiBuddhistDate

with another ensuring that the date is the same.

Only objects of type

ThaiBuddhistDate

are compared, other types return false.
To compare the dates of two

TemporalAccessor

instances, including dates
in two different chronologies, use

ChronoField.EPOCH_DAY

as a comparator.

**Specified by:**
- equals

in interface

ChronoLocalDate

**Parameters:**
- obj

- the object to check, null returns false

**Returns:**
- true if this is equal to the other date

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

A hash code for this date.

**Specified by:**
- hashCode

in interface

ChronoLocalDate

**Returns:**
- a suitable hash code based only on the Chronology and the date

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public long until​(
Temporal
endExclusive,

TemporalUnit
unit)

Description copied from interface:

ChronoLocalDate

**Specified by:**
- until

in interface

ChronoLocalDate
- until

in interface

Temporal

**Parameters:**
- endExclusive

- the end date, exclusive, which is converted to a

ChronoLocalDate

in the same chronology, not null
- unit

- the unit to measure the amount in, not null

**Returns:**
- the amount of time between this date and the end date

---

#### public
String
toString()

Description copied from class:

Object

**Specified by:**
- toString

in interface

ChronoLocalDate

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class ThaiBuddhistDate

java.lang.Object

- java.time.chrono.ThaiBuddhistDate

java.time.chrono.ThaiBuddhistDate

**All Implemented Interfaces:** Serializable

,

Comparable

<

ChronoLocalDate

>

,

ChronoLocalDate

,

Temporal

,

TemporalAccessor

,

TemporalAdjuster

```java
public final class
ThaiBuddhistDate

extends
Object

implements
ChronoLocalDate
,
Serializable
```

A date in the Thai Buddhist calendar system.

This date operates using the

Thai Buddhist calendar

.
This calendar system is primarily used in Thailand.
Dates are aligned such that

2484-01-01 (Buddhist)

is

1941-01-01 (ISO)

.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

ThaiBuddhistDate

may have unpredictable results and should be avoided.
The

equals

method should be used for comparisons.

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8
**See Also:** Serialized Form

public final class

ThaiBuddhistDate

extends

Object

implements

ChronoLocalDate

,

Serializable

A date in the Thai Buddhist calendar system.

This date operates using the

Thai Buddhist calendar

.
This calendar system is primarily used in Thailand.
Dates are aligned such that

2484-01-01 (Buddhist)

is

1941-01-01 (ISO)

.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

ThaiBuddhistDate

may have unpredictable results and should be avoided.
The

equals

method should be used for comparisons.

This date operates using the

Thai Buddhist calendar

.
This calendar system is primarily used in Thailand.
Dates are aligned such that

2484-01-01 (Buddhist)

is

1941-01-01 (ISO)

.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

ThaiBuddhistDate

may have unpredictable results and should be avoided.
The

equals

method should be used for comparisons.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

ThaiBuddhistDate

may have unpredictable results and should be avoided.
The

equals

method should be used for comparisons.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this date to another date, including the chronology.

static

ThaiBuddhistDate

from

​(

TemporalAccessor

temporal)

Obtains a

ThaiBuddhistDate

from a temporal object.

ThaiBuddhistChronology

getChronology

()

Gets the chronology of this date, which is the Thai Buddhist calendar system.

ThaiBuddhistEra

getEra

()

Gets the era applicable at this date.

int

hashCode

()

A hash code for this date.

int

lengthOfMonth

()

Returns the length of the month represented by this date.

ThaiBuddhistDate

minus

​(

TemporalAmount

amount)

Returns an object of the same type as this object with an amount subtracted.

static

ThaiBuddhistDate

now

()

Obtains the current

ThaiBuddhistDate

from the system clock in the default time-zone.

static

ThaiBuddhistDate

now

​(

Clock

clock)

Obtains the current

ThaiBuddhistDate

from the specified clock.

static

ThaiBuddhistDate

now

​(

ZoneId

zone)

Obtains the current

ThaiBuddhistDate

from the system clock in the specified time-zone.

static

ThaiBuddhistDate

of

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a

ThaiBuddhistDate

representing a date in the Thai Buddhist calendar
system from the proleptic-year, month-of-year and day-of-month fields.

ThaiBuddhistDate

plus

​(

TemporalAmount

amount)

Returns an object of the same type as this object with an amount added.

String

toString

()

Returns a string representation of the object.

long

until

​(

Temporal

endExclusive,

TemporalUnit

unit)

Calculates the amount of time until another date in terms of the specified unit.

ThaiBuddhistDate

with

​(

TemporalAdjuster

adjuster)

Returns an adjusted object of the same type as this object with the adjustment made.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

ChronoLocalDate

adjustInto

,

atTime

,

compareTo

,

format

,

isAfter

,

isBefore

,

isEqual

,

isLeapYear

,

isSupported

,

isSupported

,

lengthOfYear

,

minus

,

plus

,

query

,

toEpochDay

,

toString

,

until

,

until

,

with

- Methods declared in interface java.time.temporal.

TemporalAccessor

get

,

getLong

,

range

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this date to another date, including the chronology.

static

ThaiBuddhistDate

from

​(

TemporalAccessor

temporal)

Obtains a

ThaiBuddhistDate

from a temporal object.

ThaiBuddhistChronology

getChronology

()

Gets the chronology of this date, which is the Thai Buddhist calendar system.

ThaiBuddhistEra

getEra

()

Gets the era applicable at this date.

int

hashCode

()

A hash code for this date.

int

lengthOfMonth

()

Returns the length of the month represented by this date.

ThaiBuddhistDate

minus

​(

TemporalAmount

amount)

Returns an object of the same type as this object with an amount subtracted.

static

ThaiBuddhistDate

now

()

Obtains the current

ThaiBuddhistDate

from the system clock in the default time-zone.

static

ThaiBuddhistDate

now

​(

Clock

clock)

Obtains the current

ThaiBuddhistDate

from the specified clock.

static

ThaiBuddhistDate

now

​(

ZoneId

zone)

Obtains the current

ThaiBuddhistDate

from the system clock in the specified time-zone.

static

ThaiBuddhistDate

of

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a

ThaiBuddhistDate

representing a date in the Thai Buddhist calendar
system from the proleptic-year, month-of-year and day-of-month fields.

ThaiBuddhistDate

plus

​(

TemporalAmount

amount)

Returns an object of the same type as this object with an amount added.

String

toString

()

Returns a string representation of the object.

long

until

​(

Temporal

endExclusive,

TemporalUnit

unit)

Calculates the amount of time until another date in terms of the specified unit.

ThaiBuddhistDate

with

​(

TemporalAdjuster

adjuster)

Returns an adjusted object of the same type as this object with the adjustment made.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

ChronoLocalDate

adjustInto

,

atTime

,

compareTo

,

format

,

isAfter

,

isBefore

,

isEqual

,

isLeapYear

,

isSupported

,

isSupported

,

lengthOfYear

,

minus

,

plus

,

query

,

toEpochDay

,

toString

,

until

,

until

,

with

- Methods declared in interface java.time.temporal.

TemporalAccessor

get

,

getLong

,

range

---

#### Method Summary

Compares this date to another date, including the chronology.

Obtains a

ThaiBuddhistDate

from a temporal object.

Gets the chronology of this date, which is the Thai Buddhist calendar system.

Gets the era applicable at this date.

A hash code for this date.

Returns the length of the month represented by this date.

Returns an object of the same type as this object with an amount subtracted.

Obtains the current

ThaiBuddhistDate

from the system clock in the default time-zone.

Obtains the current

ThaiBuddhistDate

from the specified clock.

Obtains the current

ThaiBuddhistDate

from the system clock in the specified time-zone.

Obtains a

ThaiBuddhistDate

representing a date in the Thai Buddhist calendar
system from the proleptic-year, month-of-year and day-of-month fields.

Returns an object of the same type as this object with an amount added.

Returns a string representation of the object.

Calculates the amount of time until another date in terms of the specified unit.

Returns an adjusted object of the same type as this object with the adjustment made.

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

ChronoLocalDate

adjustInto

,

atTime

,

compareTo

,

format

,

isAfter

,

isBefore

,

isEqual

,

isLeapYear

,

isSupported

,

isSupported

,

lengthOfYear

,

minus

,

plus

,

query

,

toEpochDay

,

toString

,

until

,

until

,

with

---

#### Methods declared in interface java.time.chrono. ChronoLocalDate

Methods declared in interface java.time.temporal.

TemporalAccessor

get

,

getLong

,

range

---

#### Methods declared in interface java.time.temporal. TemporalAccessor

============ METHOD DETAIL ==========

- Method Detail

- now

```java
public static
ThaiBuddhistDate
now()
```

Obtains the current

ThaiBuddhistDate

from the system clock in the default time-zone.

This will query the

system clock

in the default
time-zone to obtain the current date.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

**Returns:** the current date using the system clock and default time-zone, not null

- now

```java
public static
ThaiBuddhistDate
now​(
ZoneId
zone)
```

Obtains the current

ThaiBuddhistDate

from the system clock in the specified time-zone.

This will query the

system clock

to obtain the current date.
Specifying the time-zone avoids dependence on the default time-zone.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

**Parameters:** zone

- the zone ID to use, not null
**Returns:** the current date using the system clock, not null

- now

```java
public static
ThaiBuddhistDate
now​(
Clock
clock)
```

Obtains the current

ThaiBuddhistDate

from the specified clock.

This will query the specified clock to obtain the current date - today.
Using this method allows the use of an alternate clock for testing.
The alternate clock may be introduced using

dependency injection

.

**Parameters:** clock

- the clock to use, not null
**Returns:** the current date, not null
**Throws:** DateTimeException

- if the current date cannot be obtained

- of

```java
public static
ThaiBuddhistDate
of​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a

ThaiBuddhistDate

representing a date in the Thai Buddhist calendar
system from the proleptic-year, month-of-year and day-of-month fields.

This returns a

ThaiBuddhistDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

**Parameters:** prolepticYear

- the Thai Buddhist proleptic-year
**Parameters:** month

- the Thai Buddhist month-of-year, from 1 to 12
**Parameters:** dayOfMonth

- the Thai Buddhist day-of-month, from 1 to 31
**Returns:** the date in Thai Buddhist calendar system, not null
**Throws:** DateTimeException

- if the value of any field is out of range,
or if the day-of-month is invalid for the month-year

- from

```java
public static
ThaiBuddhistDate
from​(
TemporalAccessor
temporal)
```

Obtains a

ThaiBuddhistDate

from a temporal object.

This obtains a date in the Thai Buddhist calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

ThaiBuddhistDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

ThaiBuddhistDate::from

.

**Parameters:** temporal

- the temporal object to convert, not null
**Returns:** the date in Thai Buddhist calendar system, not null
**Throws:** DateTimeException

- if unable to convert to a

ThaiBuddhistDate
**See Also:** Chronology.date(TemporalAccessor)

- getChronology

```java
public
ThaiBuddhistChronology
getChronology()
```

Gets the chronology of this date, which is the Thai Buddhist calendar system.

The

Chronology

represents the calendar system in use.
The era and other fields in

ChronoField

are defined by the chronology.

**Specified by:** getChronology

in interface

ChronoLocalDate
**Returns:** the Thai Buddhist chronology, not null

- getEra

```java
public
ThaiBuddhistEra
getEra()
```

Gets the era applicable at this date.

The Thai Buddhist calendar system has two eras, 'BE' and 'BEFORE_BE',
defined by

ThaiBuddhistEra

.

**Specified by:** getEra

in interface

ChronoLocalDate
**Returns:** the era applicable at this date, not null

- lengthOfMonth

```java
public int lengthOfMonth()
```

Returns the length of the month represented by this date.

This returns the length of the month in days.
Month lengths match those of the ISO calendar system.

**Specified by:** lengthOfMonth

in interface

ChronoLocalDate
**Returns:** the length of the month in days

- with

```java
public
ThaiBuddhistDate
with​(
TemporalAdjuster
adjuster)
```

Returns an adjusted object of the same type as this object with the adjustment made.

This adjusts this date-time according to the rules of the specified adjuster.
A simple adjuster might simply set the one of the fields, such as the year field.
A more complex adjuster might set the date to the last day of the month.
A selection of common adjustments is provided in

TemporalAdjusters

.
These include finding the "last day of the month" and "next Wednesday".
The adjuster is responsible for handling special cases, such as the varying
lengths of month and leap years.

Some example code indicating how and why this method is used:

```java
date = date.with(Month.JULY); // most key classes implement TemporalAdjuster
date = date.with(lastDayOfMonth()); // static import from Adjusters
date = date.with(next(WEDNESDAY)); // static import from Adjusters and DayOfWeek
```

**Specified by:** with

in interface

ChronoLocalDate
**Specified by:** with

in interface

Temporal
**Parameters:** adjuster

- the adjuster to use, not null
**Returns:** an object of the same type with the specified adjustment made, not null
**Throws:** DateTimeException

- if unable to make the adjustment
**Throws:** ArithmeticException

- if numeric overflow occurs

- plus

```java
public
ThaiBuddhistDate
plus​(
TemporalAmount
amount)
```

Returns an object of the same type as this object with an amount added.

This adjusts this temporal, adding according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.plus(period); // add a Period instance
date = date.plus(duration); // add a Duration instance
date = date.plus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

**Specified by:** plus

in interface

ChronoLocalDate
**Specified by:** plus

in interface

Temporal
**Parameters:** amount

- the amount to add, not null
**Returns:** an object of the same type with the specified adjustment made, not null
**Throws:** DateTimeException

- if the addition cannot be made
**Throws:** ArithmeticException

- if numeric overflow occurs

- minus

```java
public
ThaiBuddhistDate
minus​(
TemporalAmount
amount)
```

Returns an object of the same type as this object with an amount subtracted.

This adjusts this temporal, subtracting according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.minus(period); // subtract a Period instance
date = date.minus(duration); // subtract a Duration instance
date = date.minus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

**Specified by:** minus

in interface

ChronoLocalDate
**Specified by:** minus

in interface

Temporal
**Parameters:** amount

- the amount to subtract, not null
**Returns:** an object of the same type with the specified adjustment made, not null
**Throws:** DateTimeException

- if the subtraction cannot be made
**Throws:** ArithmeticException

- if numeric overflow occurs

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this date to another date, including the chronology.

Compares this

ThaiBuddhistDate

with another ensuring that the date is the same.

Only objects of type

ThaiBuddhistDate

are compared, other types return false.
To compare the dates of two

TemporalAccessor

instances, including dates
in two different chronologies, use

ChronoField.EPOCH_DAY

as a comparator.

**Specified by:** equals

in interface

ChronoLocalDate
**Parameters:** obj

- the object to check, null returns false
**Returns:** true if this is equal to the other date
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

A hash code for this date.

**Specified by:** hashCode

in interface

ChronoLocalDate
**Returns:** a suitable hash code based only on the Chronology and the date
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- until

```java
public long until​(
Temporal
endExclusive,

TemporalUnit
unit)
```

Description copied from interface:

ChronoLocalDate

Calculates the amount of time until another date in terms of the specified unit.

This calculates the amount of time between two

ChronoLocalDate

objects in terms of a single

TemporalUnit

.
The start and end points are

this

and the specified date.
The result will be negative if the end is before the start.
The

Temporal

passed to this method is converted to a

ChronoLocalDate

using

Chronology.date(TemporalAccessor)

.
The calculation returns a whole number, representing the number of
complete units between the two dates.
For example, the amount in days between two dates can be calculated
using

startDate.until(endDate, DAYS)

.

There are two equivalent ways of using this method.
The first is to invoke this method.
The second is to use

TemporalUnit.between(Temporal, Temporal)

:

```java
// these two lines are equivalent
amount = start.until(end, MONTHS);
amount = MONTHS.between(start, end);
```

The choice should be made based on which makes the code more readable.

The calculation is implemented in this method for

ChronoUnit

.
The units

DAYS

,

WEEKS

,

MONTHS

,

YEARS

,

DECADES

,

CENTURIES

,

MILLENNIA

and

ERAS

should be supported by all implementations.
Other

ChronoUnit

values will throw an exception.

If the unit is not a

ChronoUnit

, then the result of this method
is obtained by invoking

TemporalUnit.between(Temporal, Temporal)

passing

this

as the first argument and the converted input temporal as
the second argument.

This instance is immutable and unaffected by this method call.

**Specified by:** until

in interface

ChronoLocalDate
**Specified by:** until

in interface

Temporal
**Parameters:** endExclusive

- the end date, exclusive, which is converted to a

ChronoLocalDate

in the same chronology, not null
**Parameters:** unit

- the unit to measure the amount in, not null
**Returns:** the amount of time between this date and the end date

- toString

```java
public
String
toString()
```

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

**Specified by:** toString

in interface

ChronoLocalDate
**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Method Detail

- now

```java
public static
ThaiBuddhistDate
now()
```

Obtains the current

ThaiBuddhistDate

from the system clock in the default time-zone.

This will query the

system clock

in the default
time-zone to obtain the current date.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

**Returns:** the current date using the system clock and default time-zone, not null

- now

```java
public static
ThaiBuddhistDate
now​(
ZoneId
zone)
```

Obtains the current

ThaiBuddhistDate

from the system clock in the specified time-zone.

This will query the

system clock

to obtain the current date.
Specifying the time-zone avoids dependence on the default time-zone.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

**Parameters:** zone

- the zone ID to use, not null
**Returns:** the current date using the system clock, not null

- now

```java
public static
ThaiBuddhistDate
now​(
Clock
clock)
```

Obtains the current

ThaiBuddhistDate

from the specified clock.

This will query the specified clock to obtain the current date - today.
Using this method allows the use of an alternate clock for testing.
The alternate clock may be introduced using

dependency injection

.

**Parameters:** clock

- the clock to use, not null
**Returns:** the current date, not null
**Throws:** DateTimeException

- if the current date cannot be obtained

- of

```java
public static
ThaiBuddhistDate
of​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a

ThaiBuddhistDate

representing a date in the Thai Buddhist calendar
system from the proleptic-year, month-of-year and day-of-month fields.

This returns a

ThaiBuddhistDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

**Parameters:** prolepticYear

- the Thai Buddhist proleptic-year
**Parameters:** month

- the Thai Buddhist month-of-year, from 1 to 12
**Parameters:** dayOfMonth

- the Thai Buddhist day-of-month, from 1 to 31
**Returns:** the date in Thai Buddhist calendar system, not null
**Throws:** DateTimeException

- if the value of any field is out of range,
or if the day-of-month is invalid for the month-year

- from

```java
public static
ThaiBuddhistDate
from​(
TemporalAccessor
temporal)
```

Obtains a

ThaiBuddhistDate

from a temporal object.

This obtains a date in the Thai Buddhist calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

ThaiBuddhistDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

ThaiBuddhistDate::from

.

**Parameters:** temporal

- the temporal object to convert, not null
**Returns:** the date in Thai Buddhist calendar system, not null
**Throws:** DateTimeException

- if unable to convert to a

ThaiBuddhistDate
**See Also:** Chronology.date(TemporalAccessor)

- getChronology

```java
public
ThaiBuddhistChronology
getChronology()
```

Gets the chronology of this date, which is the Thai Buddhist calendar system.

The

Chronology

represents the calendar system in use.
The era and other fields in

ChronoField

are defined by the chronology.

**Specified by:** getChronology

in interface

ChronoLocalDate
**Returns:** the Thai Buddhist chronology, not null

- getEra

```java
public
ThaiBuddhistEra
getEra()
```

Gets the era applicable at this date.

The Thai Buddhist calendar system has two eras, 'BE' and 'BEFORE_BE',
defined by

ThaiBuddhistEra

.

**Specified by:** getEra

in interface

ChronoLocalDate
**Returns:** the era applicable at this date, not null

- lengthOfMonth

```java
public int lengthOfMonth()
```

Returns the length of the month represented by this date.

This returns the length of the month in days.
Month lengths match those of the ISO calendar system.

**Specified by:** lengthOfMonth

in interface

ChronoLocalDate
**Returns:** the length of the month in days

- with

```java
public
ThaiBuddhistDate
with​(
TemporalAdjuster
adjuster)
```

Returns an adjusted object of the same type as this object with the adjustment made.

This adjusts this date-time according to the rules of the specified adjuster.
A simple adjuster might simply set the one of the fields, such as the year field.
A more complex adjuster might set the date to the last day of the month.
A selection of common adjustments is provided in

TemporalAdjusters

.
These include finding the "last day of the month" and "next Wednesday".
The adjuster is responsible for handling special cases, such as the varying
lengths of month and leap years.

Some example code indicating how and why this method is used:

```java
date = date.with(Month.JULY); // most key classes implement TemporalAdjuster
date = date.with(lastDayOfMonth()); // static import from Adjusters
date = date.with(next(WEDNESDAY)); // static import from Adjusters and DayOfWeek
```

**Specified by:** with

in interface

ChronoLocalDate
**Specified by:** with

in interface

Temporal
**Parameters:** adjuster

- the adjuster to use, not null
**Returns:** an object of the same type with the specified adjustment made, not null
**Throws:** DateTimeException

- if unable to make the adjustment
**Throws:** ArithmeticException

- if numeric overflow occurs

- plus

```java
public
ThaiBuddhistDate
plus​(
TemporalAmount
amount)
```

Returns an object of the same type as this object with an amount added.

This adjusts this temporal, adding according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.plus(period); // add a Period instance
date = date.plus(duration); // add a Duration instance
date = date.plus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

**Specified by:** plus

in interface

ChronoLocalDate
**Specified by:** plus

in interface

Temporal
**Parameters:** amount

- the amount to add, not null
**Returns:** an object of the same type with the specified adjustment made, not null
**Throws:** DateTimeException

- if the addition cannot be made
**Throws:** ArithmeticException

- if numeric overflow occurs

- minus

```java
public
ThaiBuddhistDate
minus​(
TemporalAmount
amount)
```

Returns an object of the same type as this object with an amount subtracted.

This adjusts this temporal, subtracting according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.minus(period); // subtract a Period instance
date = date.minus(duration); // subtract a Duration instance
date = date.minus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

**Specified by:** minus

in interface

ChronoLocalDate
**Specified by:** minus

in interface

Temporal
**Parameters:** amount

- the amount to subtract, not null
**Returns:** an object of the same type with the specified adjustment made, not null
**Throws:** DateTimeException

- if the subtraction cannot be made
**Throws:** ArithmeticException

- if numeric overflow occurs

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this date to another date, including the chronology.

Compares this

ThaiBuddhistDate

with another ensuring that the date is the same.

Only objects of type

ThaiBuddhistDate

are compared, other types return false.
To compare the dates of two

TemporalAccessor

instances, including dates
in two different chronologies, use

ChronoField.EPOCH_DAY

as a comparator.

**Specified by:** equals

in interface

ChronoLocalDate
**Parameters:** obj

- the object to check, null returns false
**Returns:** true if this is equal to the other date
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

A hash code for this date.

**Specified by:** hashCode

in interface

ChronoLocalDate
**Returns:** a suitable hash code based only on the Chronology and the date
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- until

```java
public long until​(
Temporal
endExclusive,

TemporalUnit
unit)
```

Description copied from interface:

ChronoLocalDate

Calculates the amount of time until another date in terms of the specified unit.

This calculates the amount of time between two

ChronoLocalDate

objects in terms of a single

TemporalUnit

.
The start and end points are

this

and the specified date.
The result will be negative if the end is before the start.
The

Temporal

passed to this method is converted to a

ChronoLocalDate

using

Chronology.date(TemporalAccessor)

.
The calculation returns a whole number, representing the number of
complete units between the two dates.
For example, the amount in days between two dates can be calculated
using

startDate.until(endDate, DAYS)

.

There are two equivalent ways of using this method.
The first is to invoke this method.
The second is to use

TemporalUnit.between(Temporal, Temporal)

:

```java
// these two lines are equivalent
amount = start.until(end, MONTHS);
amount = MONTHS.between(start, end);
```

The choice should be made based on which makes the code more readable.

The calculation is implemented in this method for

ChronoUnit

.
The units

DAYS

,

WEEKS

,

MONTHS

,

YEARS

,

DECADES

,

CENTURIES

,

MILLENNIA

and

ERAS

should be supported by all implementations.
Other

ChronoUnit

values will throw an exception.

If the unit is not a

ChronoUnit

, then the result of this method
is obtained by invoking

TemporalUnit.between(Temporal, Temporal)

passing

this

as the first argument and the converted input temporal as
the second argument.

This instance is immutable and unaffected by this method call.

**Specified by:** until

in interface

ChronoLocalDate
**Specified by:** until

in interface

Temporal
**Parameters:** endExclusive

- the end date, exclusive, which is converted to a

ChronoLocalDate

in the same chronology, not null
**Parameters:** unit

- the unit to measure the amount in, not null
**Returns:** the amount of time between this date and the end date

- toString

```java
public
String
toString()
```

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

**Specified by:** toString

in interface

ChronoLocalDate
**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

now

```java
public static
ThaiBuddhistDate
now()
```

Obtains the current

ThaiBuddhistDate

from the system clock in the default time-zone.

This will query the

system clock

in the default
time-zone to obtain the current date.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

**Returns:** the current date using the system clock and default time-zone, not null

---

#### now

public static

ThaiBuddhistDate

now()

Obtains the current

ThaiBuddhistDate

from the system clock in the default time-zone.

This will query the

system clock

in the default
time-zone to obtain the current date.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

This will query the

system clock

in the default
time-zone to obtain the current date.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

now

```java
public static
ThaiBuddhistDate
now​(
ZoneId
zone)
```

Obtains the current

ThaiBuddhistDate

from the system clock in the specified time-zone.

This will query the

system clock

to obtain the current date.
Specifying the time-zone avoids dependence on the default time-zone.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

**Parameters:** zone

- the zone ID to use, not null
**Returns:** the current date using the system clock, not null

---

#### now

public static

ThaiBuddhistDate

now​(

ZoneId

zone)

Obtains the current

ThaiBuddhistDate

from the system clock in the specified time-zone.

This will query the

system clock

to obtain the current date.
Specifying the time-zone avoids dependence on the default time-zone.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

This will query the

system clock

to obtain the current date.
Specifying the time-zone avoids dependence on the default time-zone.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

Using this method will prevent the ability to use an alternate clock for testing
because the clock is hard-coded.

now

```java
public static
ThaiBuddhistDate
now​(
Clock
clock)
```

Obtains the current

ThaiBuddhistDate

from the specified clock.

This will query the specified clock to obtain the current date - today.
Using this method allows the use of an alternate clock for testing.
The alternate clock may be introduced using

dependency injection

.

**Parameters:** clock

- the clock to use, not null
**Returns:** the current date, not null
**Throws:** DateTimeException

- if the current date cannot be obtained

---

#### now

public static

ThaiBuddhistDate

now​(

Clock

clock)

Obtains the current

ThaiBuddhistDate

from the specified clock.

This will query the specified clock to obtain the current date - today.
Using this method allows the use of an alternate clock for testing.
The alternate clock may be introduced using

dependency injection

.

This will query the specified clock to obtain the current date - today.
Using this method allows the use of an alternate clock for testing.
The alternate clock may be introduced using

dependency injection

.

of

```java
public static
ThaiBuddhistDate
of​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a

ThaiBuddhistDate

representing a date in the Thai Buddhist calendar
system from the proleptic-year, month-of-year and day-of-month fields.

This returns a

ThaiBuddhistDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

**Parameters:** prolepticYear

- the Thai Buddhist proleptic-year
**Parameters:** month

- the Thai Buddhist month-of-year, from 1 to 12
**Parameters:** dayOfMonth

- the Thai Buddhist day-of-month, from 1 to 31
**Returns:** the date in Thai Buddhist calendar system, not null
**Throws:** DateTimeException

- if the value of any field is out of range,
or if the day-of-month is invalid for the month-year

---

#### of

public static

ThaiBuddhistDate

of​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a

ThaiBuddhistDate

representing a date in the Thai Buddhist calendar
system from the proleptic-year, month-of-year and day-of-month fields.

This returns a

ThaiBuddhistDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

This returns a

ThaiBuddhistDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

from

```java
public static
ThaiBuddhistDate
from​(
TemporalAccessor
temporal)
```

Obtains a

ThaiBuddhistDate

from a temporal object.

This obtains a date in the Thai Buddhist calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

ThaiBuddhistDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

ThaiBuddhistDate::from

.

**Parameters:** temporal

- the temporal object to convert, not null
**Returns:** the date in Thai Buddhist calendar system, not null
**Throws:** DateTimeException

- if unable to convert to a

ThaiBuddhistDate
**See Also:** Chronology.date(TemporalAccessor)

---

#### from

public static

ThaiBuddhistDate

from​(

TemporalAccessor

temporal)

Obtains a

ThaiBuddhistDate

from a temporal object.

This obtains a date in the Thai Buddhist calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

ThaiBuddhistDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

ThaiBuddhistDate::from

.

This obtains a date in the Thai Buddhist calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

ThaiBuddhistDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

ThaiBuddhistDate::from

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

ThaiBuddhistDate::from

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

ThaiBuddhistDate::from

.

getChronology

```java
public
ThaiBuddhistChronology
getChronology()
```

Gets the chronology of this date, which is the Thai Buddhist calendar system.

The

Chronology

represents the calendar system in use.
The era and other fields in

ChronoField

are defined by the chronology.

**Specified by:** getChronology

in interface

ChronoLocalDate
**Returns:** the Thai Buddhist chronology, not null

---

#### getChronology

public

ThaiBuddhistChronology

getChronology()

Gets the chronology of this date, which is the Thai Buddhist calendar system.

The

Chronology

represents the calendar system in use.
The era and other fields in

ChronoField

are defined by the chronology.

The

Chronology

represents the calendar system in use.
The era and other fields in

ChronoField

are defined by the chronology.

getEra

```java
public
ThaiBuddhistEra
getEra()
```

Gets the era applicable at this date.

The Thai Buddhist calendar system has two eras, 'BE' and 'BEFORE_BE',
defined by

ThaiBuddhistEra

.

**Specified by:** getEra

in interface

ChronoLocalDate
**Returns:** the era applicable at this date, not null

---

#### getEra

public

ThaiBuddhistEra

getEra()

Gets the era applicable at this date.

The Thai Buddhist calendar system has two eras, 'BE' and 'BEFORE_BE',
defined by

ThaiBuddhistEra

.

The Thai Buddhist calendar system has two eras, 'BE' and 'BEFORE_BE',
defined by

ThaiBuddhistEra

.

lengthOfMonth

```java
public int lengthOfMonth()
```

Returns the length of the month represented by this date.

This returns the length of the month in days.
Month lengths match those of the ISO calendar system.

**Specified by:** lengthOfMonth

in interface

ChronoLocalDate
**Returns:** the length of the month in days

---

#### lengthOfMonth

public int lengthOfMonth()

Returns the length of the month represented by this date.

This returns the length of the month in days.
Month lengths match those of the ISO calendar system.

This returns the length of the month in days.
Month lengths match those of the ISO calendar system.

with

```java
public
ThaiBuddhistDate
with​(
TemporalAdjuster
adjuster)
```

Returns an adjusted object of the same type as this object with the adjustment made.

This adjusts this date-time according to the rules of the specified adjuster.
A simple adjuster might simply set the one of the fields, such as the year field.
A more complex adjuster might set the date to the last day of the month.
A selection of common adjustments is provided in

TemporalAdjusters

.
These include finding the "last day of the month" and "next Wednesday".
The adjuster is responsible for handling special cases, such as the varying
lengths of month and leap years.

Some example code indicating how and why this method is used:

```java
date = date.with(Month.JULY); // most key classes implement TemporalAdjuster
date = date.with(lastDayOfMonth()); // static import from Adjusters
date = date.with(next(WEDNESDAY)); // static import from Adjusters and DayOfWeek
```

**Specified by:** with

in interface

ChronoLocalDate
**Specified by:** with

in interface

Temporal
**Parameters:** adjuster

- the adjuster to use, not null
**Returns:** an object of the same type with the specified adjustment made, not null
**Throws:** DateTimeException

- if unable to make the adjustment
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### with

public

ThaiBuddhistDate

with​(

TemporalAdjuster

adjuster)

Returns an adjusted object of the same type as this object with the adjustment made.

This adjusts this date-time according to the rules of the specified adjuster.
A simple adjuster might simply set the one of the fields, such as the year field.
A more complex adjuster might set the date to the last day of the month.
A selection of common adjustments is provided in

TemporalAdjusters

.
These include finding the "last day of the month" and "next Wednesday".
The adjuster is responsible for handling special cases, such as the varying
lengths of month and leap years.

Some example code indicating how and why this method is used:

```java
date = date.with(Month.JULY); // most key classes implement TemporalAdjuster
date = date.with(lastDayOfMonth()); // static import from Adjusters
date = date.with(next(WEDNESDAY)); // static import from Adjusters and DayOfWeek
```

This adjusts this date-time according to the rules of the specified adjuster.
A simple adjuster might simply set the one of the fields, such as the year field.
A more complex adjuster might set the date to the last day of the month.
A selection of common adjustments is provided in

TemporalAdjusters

.
These include finding the "last day of the month" and "next Wednesday".
The adjuster is responsible for handling special cases, such as the varying
lengths of month and leap years.

Some example code indicating how and why this method is used:

```java
date = date.with(Month.JULY); // most key classes implement TemporalAdjuster
date = date.with(lastDayOfMonth()); // static import from Adjusters
date = date.with(next(WEDNESDAY)); // static import from Adjusters and DayOfWeek
```

Some example code indicating how and why this method is used:

```java
date = date.with(Month.JULY); // most key classes implement TemporalAdjuster
date = date.with(lastDayOfMonth()); // static import from Adjusters
date = date.with(next(WEDNESDAY)); // static import from Adjusters and DayOfWeek
```

date = date.with(Month.JULY); // most key classes implement TemporalAdjuster
date = date.with(lastDayOfMonth()); // static import from Adjusters
date = date.with(next(WEDNESDAY)); // static import from Adjusters and DayOfWeek

plus

```java
public
ThaiBuddhistDate
plus​(
TemporalAmount
amount)
```

Returns an object of the same type as this object with an amount added.

This adjusts this temporal, adding according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.plus(period); // add a Period instance
date = date.plus(duration); // add a Duration instance
date = date.plus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

**Specified by:** plus

in interface

ChronoLocalDate
**Specified by:** plus

in interface

Temporal
**Parameters:** amount

- the amount to add, not null
**Returns:** an object of the same type with the specified adjustment made, not null
**Throws:** DateTimeException

- if the addition cannot be made
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### plus

public

ThaiBuddhistDate

plus​(

TemporalAmount

amount)

Returns an object of the same type as this object with an amount added.

This adjusts this temporal, adding according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.plus(period); // add a Period instance
date = date.plus(duration); // add a Duration instance
date = date.plus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

This adjusts this temporal, adding according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.plus(period); // add a Period instance
date = date.plus(duration); // add a Duration instance
date = date.plus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

Some example code indicating how and why this method is used:

```java
date = date.plus(period); // add a Period instance
date = date.plus(duration); // add a Duration instance
date = date.plus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

date = date.plus(period); // add a Period instance
date = date.plus(duration); // add a Duration instance
date = date.plus(workingDays(6)); // example user-written workingDays method

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

minus

```java
public
ThaiBuddhistDate
minus​(
TemporalAmount
amount)
```

Returns an object of the same type as this object with an amount subtracted.

This adjusts this temporal, subtracting according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.minus(period); // subtract a Period instance
date = date.minus(duration); // subtract a Duration instance
date = date.minus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

**Specified by:** minus

in interface

ChronoLocalDate
**Specified by:** minus

in interface

Temporal
**Parameters:** amount

- the amount to subtract, not null
**Returns:** an object of the same type with the specified adjustment made, not null
**Throws:** DateTimeException

- if the subtraction cannot be made
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### minus

public

ThaiBuddhistDate

minus​(

TemporalAmount

amount)

Returns an object of the same type as this object with an amount subtracted.

This adjusts this temporal, subtracting according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.minus(period); // subtract a Period instance
date = date.minus(duration); // subtract a Duration instance
date = date.minus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

This adjusts this temporal, subtracting according to the rules of the specified amount.
The amount is typically a

Period

but may be any other type implementing
the

TemporalAmount

interface, such as

Duration

.

Some example code indicating how and why this method is used:

```java
date = date.minus(period); // subtract a Period instance
date = date.minus(duration); // subtract a Duration instance
date = date.minus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

Some example code indicating how and why this method is used:

```java
date = date.minus(period); // subtract a Period instance
date = date.minus(duration); // subtract a Duration instance
date = date.minus(workingDays(6)); // example user-written workingDays method
```

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

date = date.minus(period); // subtract a Period instance
date = date.minus(duration); // subtract a Duration instance
date = date.minus(workingDays(6)); // example user-written workingDays method

Note that calling

plus

followed by

minus

is not guaranteed to
return the same date-time.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this date to another date, including the chronology.

Compares this

ThaiBuddhistDate

with another ensuring that the date is the same.

Only objects of type

ThaiBuddhistDate

are compared, other types return false.
To compare the dates of two

TemporalAccessor

instances, including dates
in two different chronologies, use

ChronoField.EPOCH_DAY

as a comparator.

**Specified by:** equals

in interface

ChronoLocalDate
**Parameters:** obj

- the object to check, null returns false
**Returns:** true if this is equal to the other date
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this date to another date, including the chronology.

Compares this

ThaiBuddhistDate

with another ensuring that the date is the same.

Only objects of type

ThaiBuddhistDate

are compared, other types return false.
To compare the dates of two

TemporalAccessor

instances, including dates
in two different chronologies, use

ChronoField.EPOCH_DAY

as a comparator.

Compares this

ThaiBuddhistDate

with another ensuring that the date is the same.

Only objects of type

ThaiBuddhistDate

are compared, other types return false.
To compare the dates of two

TemporalAccessor

instances, including dates
in two different chronologies, use

ChronoField.EPOCH_DAY

as a comparator.

Only objects of type

ThaiBuddhistDate

are compared, other types return false.
To compare the dates of two

TemporalAccessor

instances, including dates
in two different chronologies, use

ChronoField.EPOCH_DAY

as a comparator.

hashCode

```java
public int hashCode()
```

A hash code for this date.

**Specified by:** hashCode

in interface

ChronoLocalDate
**Returns:** a suitable hash code based only on the Chronology and the date
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

A hash code for this date.

until

```java
public long until​(
Temporal
endExclusive,

TemporalUnit
unit)
```

Description copied from interface:

ChronoLocalDate

Calculates the amount of time until another date in terms of the specified unit.

This calculates the amount of time between two

ChronoLocalDate

objects in terms of a single

TemporalUnit

.
The start and end points are

this

and the specified date.
The result will be negative if the end is before the start.
The

Temporal

passed to this method is converted to a

ChronoLocalDate

using

Chronology.date(TemporalAccessor)

.
The calculation returns a whole number, representing the number of
complete units between the two dates.
For example, the amount in days between two dates can be calculated
using

startDate.until(endDate, DAYS)

.

There are two equivalent ways of using this method.
The first is to invoke this method.
The second is to use

TemporalUnit.between(Temporal, Temporal)

:

```java
// these two lines are equivalent
amount = start.until(end, MONTHS);
amount = MONTHS.between(start, end);
```

The choice should be made based on which makes the code more readable.

The calculation is implemented in this method for

ChronoUnit

.
The units

DAYS

,

WEEKS

,

MONTHS

,

YEARS

,

DECADES

,

CENTURIES

,

MILLENNIA

and

ERAS

should be supported by all implementations.
Other

ChronoUnit

values will throw an exception.

If the unit is not a

ChronoUnit

, then the result of this method
is obtained by invoking

TemporalUnit.between(Temporal, Temporal)

passing

this

as the first argument and the converted input temporal as
the second argument.

This instance is immutable and unaffected by this method call.

**Specified by:** until

in interface

ChronoLocalDate
**Specified by:** until

in interface

Temporal
**Parameters:** endExclusive

- the end date, exclusive, which is converted to a

ChronoLocalDate

in the same chronology, not null
**Parameters:** unit

- the unit to measure the amount in, not null
**Returns:** the amount of time between this date and the end date

---

#### until

public long until​(

Temporal

endExclusive,

TemporalUnit

unit)

Description copied from interface:

ChronoLocalDate

Calculates the amount of time until another date in terms of the specified unit.

This calculates the amount of time between two

ChronoLocalDate

objects in terms of a single

TemporalUnit

.
The start and end points are

this

and the specified date.
The result will be negative if the end is before the start.
The

Temporal

passed to this method is converted to a

ChronoLocalDate

using

Chronology.date(TemporalAccessor)

.
The calculation returns a whole number, representing the number of
complete units between the two dates.
For example, the amount in days between two dates can be calculated
using

startDate.until(endDate, DAYS)

.

There are two equivalent ways of using this method.
The first is to invoke this method.
The second is to use

TemporalUnit.between(Temporal, Temporal)

:

```java
// these two lines are equivalent
amount = start.until(end, MONTHS);
amount = MONTHS.between(start, end);
```

The choice should be made based on which makes the code more readable.

The calculation is implemented in this method for

ChronoUnit

.
The units

DAYS

,

WEEKS

,

MONTHS

,

YEARS

,

DECADES

,

CENTURIES

,

MILLENNIA

and

ERAS

should be supported by all implementations.
Other

ChronoUnit

values will throw an exception.

If the unit is not a

ChronoUnit

, then the result of this method
is obtained by invoking

TemporalUnit.between(Temporal, Temporal)

passing

this

as the first argument and the converted input temporal as
the second argument.

This instance is immutable and unaffected by this method call.

This calculates the amount of time between two

ChronoLocalDate

objects in terms of a single

TemporalUnit

.
The start and end points are

this

and the specified date.
The result will be negative if the end is before the start.
The

Temporal

passed to this method is converted to a

ChronoLocalDate

using

Chronology.date(TemporalAccessor)

.
The calculation returns a whole number, representing the number of
complete units between the two dates.
For example, the amount in days between two dates can be calculated
using

startDate.until(endDate, DAYS)

.

There are two equivalent ways of using this method.
The first is to invoke this method.
The second is to use

TemporalUnit.between(Temporal, Temporal)

:

```java
// these two lines are equivalent
amount = start.until(end, MONTHS);
amount = MONTHS.between(start, end);
```

The choice should be made based on which makes the code more readable.

The calculation is implemented in this method for

ChronoUnit

.
The units

DAYS

,

WEEKS

,

MONTHS

,

YEARS

,

DECADES

,

CENTURIES

,

MILLENNIA

and

ERAS

should be supported by all implementations.
Other

ChronoUnit

values will throw an exception.

If the unit is not a

ChronoUnit

, then the result of this method
is obtained by invoking

TemporalUnit.between(Temporal, Temporal)

passing

this

as the first argument and the converted input temporal as
the second argument.

This instance is immutable and unaffected by this method call.

There are two equivalent ways of using this method.
The first is to invoke this method.
The second is to use

TemporalUnit.between(Temporal, Temporal)

:

```java
// these two lines are equivalent
amount = start.until(end, MONTHS);
amount = MONTHS.between(start, end);
```

The choice should be made based on which makes the code more readable.

The calculation is implemented in this method for

ChronoUnit

.
The units

DAYS

,

WEEKS

,

MONTHS

,

YEARS

,

DECADES

,

CENTURIES

,

MILLENNIA

and

ERAS

should be supported by all implementations.
Other

ChronoUnit

values will throw an exception.

If the unit is not a

ChronoUnit

, then the result of this method
is obtained by invoking

TemporalUnit.between(Temporal, Temporal)

passing

this

as the first argument and the converted input temporal as
the second argument.

This instance is immutable and unaffected by this method call.

// these two lines are equivalent
amount = start.until(end, MONTHS);
amount = MONTHS.between(start, end);

The calculation is implemented in this method for

ChronoUnit

.
The units

DAYS

,

WEEKS

,

MONTHS

,

YEARS

,

DECADES

,

CENTURIES

,

MILLENNIA

and

ERAS

should be supported by all implementations.
Other

ChronoUnit

values will throw an exception.

If the unit is not a

ChronoUnit

, then the result of this method
is obtained by invoking

TemporalUnit.between(Temporal, Temporal)

passing

this

as the first argument and the converted input temporal as
the second argument.

This instance is immutable and unaffected by this method call.

If the unit is not a

ChronoUnit

, then the result of this method
is obtained by invoking

TemporalUnit.between(Temporal, Temporal)

passing

this

as the first argument and the converted input temporal as
the second argument.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

toString

```java
public
String
toString()
```

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

**Specified by:** toString

in interface

ChronoLocalDate
**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

getClass().getName() + '@' + Integer.toHexString(hashCode())

---

