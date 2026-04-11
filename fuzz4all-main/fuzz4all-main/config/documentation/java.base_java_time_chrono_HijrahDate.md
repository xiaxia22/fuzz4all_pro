# Class HijrahDate

**Source:** `java.base\java\time\chrono\HijrahDate.html`

### Class Description

```java
public final class
HijrahDate

extends
Object

implements
ChronoLocalDate
,
Serializable
```

A date in the Hijrah calendar system.

This date operates using one of several variants of the

Hijrah calendar

.

The Hijrah calendar has a different total of days in a year than
Gregorian calendar, and the length of each month is based on the period
of a complete revolution of the moon around the earth
(as between successive new moons).
Refer to the

HijrahChronology

for details of supported variants.

Each HijrahDate is created bound to a particular HijrahChronology,
The same chronology is propagated to each HijrahDate computed from the date.
To use a different Hijrah variant, its HijrahChronology can be used
to create new HijrahDate instances.
Alternatively, the

withVariant(java.time.chrono.HijrahChronology)

method can be used to convert
to a new HijrahChronology.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

HijrahDate

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
HijrahDate
now()

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the default time-zone.

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
HijrahDate
now​(
ZoneId
zone)

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the specified time-zone.

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
HijrahDate
now​(
Clock
clock)

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
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
HijrahDate
of​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar
from the proleptic-year, month-of-year and day-of-month fields.

This returns a

HijrahDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

**Parameters:**
- prolepticYear

- the Hijrah proleptic-year
- month

- the Hijrah month-of-year, from 1 to 12
- dayOfMonth

- the Hijrah day-of-month, from 1 to 30

**Returns:**
- the date in Hijrah calendar system, not null

**Throws:**
- DateTimeException

- if the value of any field is out of range,
or if the day-of-month is invalid for the month-year

---

#### public static
HijrahDate
from​(
TemporalAccessor
temporal)

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar from a temporal object.

This obtains a date in the Hijrah calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

HijrahDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

HijrahDate::from

.

**Parameters:**
- temporal

- the temporal object to convert, not null

**Returns:**
- the date in Hijrah calendar system, not null

**Throws:**
- DateTimeException

- if unable to convert to a

HijrahDate

**See Also:**
- Chronology.date(TemporalAccessor)

---

#### public
HijrahChronology
getChronology()

Gets the chronology of this date, which is the Hijrah calendar system.

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
- the Hijrah chronology, not null

---

#### public
HijrahEra
getEra()

Gets the era applicable at this date.

The Hijrah calendar system has one era, 'AH',
defined by

HijrahEra

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
Month lengths in the Hijrah calendar system vary between 29 and 30 days.

**Specified by:**
- lengthOfMonth

in interface

ChronoLocalDate

**Returns:**
- the length of the month in days

---

#### public int lengthOfYear()

Returns the length of the year represented by this date.

This returns the length of the year in days.
A Hijrah calendar system year is typically shorter than
that of the ISO calendar system.

**Specified by:**
- lengthOfYear

in interface

ChronoLocalDate

**Returns:**
- the length of the year in days

---

#### public
HijrahDate
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

- if unable to make the adjustment.
For example, if the adjuster requires an ISO chronology
- ArithmeticException

- if numeric overflow occurs

---

#### public
HijrahDate
withVariant​(
HijrahChronology
chronology)

Returns a

HijrahDate

with the Chronology requested.

The year, month, and day are checked against the new requested
HijrahChronology. If the chronology has a shorter month length
for the month, the day is reduced to be the last day of the month.

**Parameters:**
- chronology

- the new HijrahChonology, non-null

**Returns:**
- a HijrahDate with the requested HijrahChronology, non-null

---

#### public
HijrahDate
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
HijrahDate
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

#### public boolean isLeapYear()

Checks if the year is a leap year, according to the Hijrah calendar system rules.

**Specified by:**
- isLeapYear

in interface

ChronoLocalDate

**Returns:**
- true if this date is in a leap year

---

#### public boolean equals​(
Object
obj)

Compares this date to another date, including the chronology.

Compares this

HijrahDate

with another ensuring that the date is the same.

Only objects of type

HijrahDate

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
- true if this is equal to the other date and the Chronologies are equal

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

#### Class HijrahDate

java.lang.Object

- java.time.chrono.HijrahDate

java.time.chrono.HijrahDate

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
HijrahDate

extends
Object

implements
ChronoLocalDate
,
Serializable
```

A date in the Hijrah calendar system.

This date operates using one of several variants of the

Hijrah calendar

.

The Hijrah calendar has a different total of days in a year than
Gregorian calendar, and the length of each month is based on the period
of a complete revolution of the moon around the earth
(as between successive new moons).
Refer to the

HijrahChronology

for details of supported variants.

Each HijrahDate is created bound to a particular HijrahChronology,
The same chronology is propagated to each HijrahDate computed from the date.
To use a different Hijrah variant, its HijrahChronology can be used
to create new HijrahDate instances.
Alternatively, the

withVariant(java.time.chrono.HijrahChronology)

method can be used to convert
to a new HijrahChronology.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

HijrahDate

may have unpredictable results and should be avoided.
The

equals

method should be used for comparisons.

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8
**See Also:** Serialized Form

public final class

HijrahDate

extends

Object

implements

ChronoLocalDate

,

Serializable

A date in the Hijrah calendar system.

This date operates using one of several variants of the

Hijrah calendar

.

The Hijrah calendar has a different total of days in a year than
Gregorian calendar, and the length of each month is based on the period
of a complete revolution of the moon around the earth
(as between successive new moons).
Refer to the

HijrahChronology

for details of supported variants.

Each HijrahDate is created bound to a particular HijrahChronology,
The same chronology is propagated to each HijrahDate computed from the date.
To use a different Hijrah variant, its HijrahChronology can be used
to create new HijrahDate instances.
Alternatively, the

withVariant(java.time.chrono.HijrahChronology)

method can be used to convert
to a new HijrahChronology.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

HijrahDate

may have unpredictable results and should be avoided.
The

equals

method should be used for comparisons.

This date operates using one of several variants of the

Hijrah calendar

.

The Hijrah calendar has a different total of days in a year than
Gregorian calendar, and the length of each month is based on the period
of a complete revolution of the moon around the earth
(as between successive new moons).
Refer to the

HijrahChronology

for details of supported variants.

Each HijrahDate is created bound to a particular HijrahChronology,
The same chronology is propagated to each HijrahDate computed from the date.
To use a different Hijrah variant, its HijrahChronology can be used
to create new HijrahDate instances.
Alternatively, the

withVariant(java.time.chrono.HijrahChronology)

method can be used to convert
to a new HijrahChronology.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

HijrahDate

may have unpredictable results and should be avoided.
The

equals

method should be used for comparisons.

The Hijrah calendar has a different total of days in a year than
Gregorian calendar, and the length of each month is based on the period
of a complete revolution of the moon around the earth
(as between successive new moons).
Refer to the

HijrahChronology

for details of supported variants.

Each HijrahDate is created bound to a particular HijrahChronology,
The same chronology is propagated to each HijrahDate computed from the date.
To use a different Hijrah variant, its HijrahChronology can be used
to create new HijrahDate instances.
Alternatively, the

withVariant(java.time.chrono.HijrahChronology)

method can be used to convert
to a new HijrahChronology.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

HijrahDate

may have unpredictable results and should be avoided.
The

equals

method should be used for comparisons.

Each HijrahDate is created bound to a particular HijrahChronology,
The same chronology is propagated to each HijrahDate computed from the date.
To use a different Hijrah variant, its HijrahChronology can be used
to create new HijrahDate instances.
Alternatively, the

withVariant(java.time.chrono.HijrahChronology)

method can be used to convert
to a new HijrahChronology.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

HijrahDate

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

HijrahDate

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

HijrahDate

from

​(

TemporalAccessor

temporal)

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar from a temporal object.

HijrahChronology

getChronology

()

Gets the chronology of this date, which is the Hijrah calendar system.

HijrahEra

getEra

()

Gets the era applicable at this date.

int

hashCode

()

A hash code for this date.

boolean

isLeapYear

()

Checks if the year is a leap year, according to the Hijrah calendar system rules.

int

lengthOfMonth

()

Returns the length of the month represented by this date.

int

lengthOfYear

()

Returns the length of the year represented by this date.

HijrahDate

minus

​(

TemporalAmount

amount)

Returns an object of the same type as this object with an amount subtracted.

static

HijrahDate

now

()

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the default time-zone.

static

HijrahDate

now

​(

Clock

clock)

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
from the specified clock.

static

HijrahDate

now

​(

ZoneId

zone)

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the specified time-zone.

static

HijrahDate

of

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar
from the proleptic-year, month-of-year and day-of-month fields.

HijrahDate

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

HijrahDate

with

​(

TemporalAdjuster

adjuster)

Returns an adjusted object of the same type as this object with the adjustment made.

HijrahDate

withVariant

​(

HijrahChronology

chronology)

Returns a

HijrahDate

with the Chronology requested.

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

isSupported

,

isSupported

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

HijrahDate

from

​(

TemporalAccessor

temporal)

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar from a temporal object.

HijrahChronology

getChronology

()

Gets the chronology of this date, which is the Hijrah calendar system.

HijrahEra

getEra

()

Gets the era applicable at this date.

int

hashCode

()

A hash code for this date.

boolean

isLeapYear

()

Checks if the year is a leap year, according to the Hijrah calendar system rules.

int

lengthOfMonth

()

Returns the length of the month represented by this date.

int

lengthOfYear

()

Returns the length of the year represented by this date.

HijrahDate

minus

​(

TemporalAmount

amount)

Returns an object of the same type as this object with an amount subtracted.

static

HijrahDate

now

()

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the default time-zone.

static

HijrahDate

now

​(

Clock

clock)

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
from the specified clock.

static

HijrahDate

now

​(

ZoneId

zone)

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the specified time-zone.

static

HijrahDate

of

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar
from the proleptic-year, month-of-year and day-of-month fields.

HijrahDate

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

HijrahDate

with

​(

TemporalAdjuster

adjuster)

Returns an adjusted object of the same type as this object with the adjustment made.

HijrahDate

withVariant

​(

HijrahChronology

chronology)

Returns a

HijrahDate

with the Chronology requested.

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

isSupported

,

isSupported

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

HijrahDate

of the Islamic Umm Al-Qura calendar from a temporal object.

Gets the chronology of this date, which is the Hijrah calendar system.

Gets the era applicable at this date.

A hash code for this date.

Checks if the year is a leap year, according to the Hijrah calendar system rules.

Returns the length of the month represented by this date.

Returns the length of the year represented by this date.

Returns an object of the same type as this object with an amount subtracted.

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the default time-zone.

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
from the specified clock.

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the specified time-zone.

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar
from the proleptic-year, month-of-year and day-of-month fields.

Returns an object of the same type as this object with an amount added.

Returns a string representation of the object.

Calculates the amount of time until another date in terms of the specified unit.

Returns an adjusted object of the same type as this object with the adjustment made.

Returns a

HijrahDate

with the Chronology requested.

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

isSupported

,

isSupported

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
HijrahDate
now()
```

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the default time-zone.

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
HijrahDate
now​(
ZoneId
zone)
```

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the specified time-zone.

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
HijrahDate
now​(
Clock
clock)
```

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
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
HijrahDate
of​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar
from the proleptic-year, month-of-year and day-of-month fields.

This returns a

HijrahDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

**Parameters:** prolepticYear

- the Hijrah proleptic-year
**Parameters:** month

- the Hijrah month-of-year, from 1 to 12
**Parameters:** dayOfMonth

- the Hijrah day-of-month, from 1 to 30
**Returns:** the date in Hijrah calendar system, not null
**Throws:** DateTimeException

- if the value of any field is out of range,
or if the day-of-month is invalid for the month-year

- from

```java
public static
HijrahDate
from​(
TemporalAccessor
temporal)
```

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar from a temporal object.

This obtains a date in the Hijrah calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

HijrahDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

HijrahDate::from

.

**Parameters:** temporal

- the temporal object to convert, not null
**Returns:** the date in Hijrah calendar system, not null
**Throws:** DateTimeException

- if unable to convert to a

HijrahDate
**See Also:** Chronology.date(TemporalAccessor)

- getChronology

```java
public
HijrahChronology
getChronology()
```

Gets the chronology of this date, which is the Hijrah calendar system.

The

Chronology

represents the calendar system in use.
The era and other fields in

ChronoField

are defined by the chronology.

**Specified by:** getChronology

in interface

ChronoLocalDate
**Returns:** the Hijrah chronology, not null

- getEra

```java
public
HijrahEra
getEra()
```

Gets the era applicable at this date.

The Hijrah calendar system has one era, 'AH',
defined by

HijrahEra

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
Month lengths in the Hijrah calendar system vary between 29 and 30 days.

**Specified by:** lengthOfMonth

in interface

ChronoLocalDate
**Returns:** the length of the month in days

- lengthOfYear

```java
public int lengthOfYear()
```

Returns the length of the year represented by this date.

This returns the length of the year in days.
A Hijrah calendar system year is typically shorter than
that of the ISO calendar system.

**Specified by:** lengthOfYear

in interface

ChronoLocalDate
**Returns:** the length of the year in days

- with

```java
public
HijrahDate
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

- if unable to make the adjustment.
For example, if the adjuster requires an ISO chronology
**Throws:** ArithmeticException

- if numeric overflow occurs

- withVariant

```java
public
HijrahDate
withVariant​(
HijrahChronology
chronology)
```

Returns a

HijrahDate

with the Chronology requested.

The year, month, and day are checked against the new requested
HijrahChronology. If the chronology has a shorter month length
for the month, the day is reduced to be the last day of the month.

**Parameters:** chronology

- the new HijrahChonology, non-null
**Returns:** a HijrahDate with the requested HijrahChronology, non-null

- plus

```java
public
HijrahDate
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
HijrahDate
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

- isLeapYear

```java
public boolean isLeapYear()
```

Checks if the year is a leap year, according to the Hijrah calendar system rules.

**Specified by:** isLeapYear

in interface

ChronoLocalDate
**Returns:** true if this date is in a leap year

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this date to another date, including the chronology.

Compares this

HijrahDate

with another ensuring that the date is the same.

Only objects of type

HijrahDate

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
**Returns:** true if this is equal to the other date and the Chronologies are equal
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
HijrahDate
now()
```

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the default time-zone.

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
HijrahDate
now​(
ZoneId
zone)
```

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the specified time-zone.

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
HijrahDate
now​(
Clock
clock)
```

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
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
HijrahDate
of​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar
from the proleptic-year, month-of-year and day-of-month fields.

This returns a

HijrahDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

**Parameters:** prolepticYear

- the Hijrah proleptic-year
**Parameters:** month

- the Hijrah month-of-year, from 1 to 12
**Parameters:** dayOfMonth

- the Hijrah day-of-month, from 1 to 30
**Returns:** the date in Hijrah calendar system, not null
**Throws:** DateTimeException

- if the value of any field is out of range,
or if the day-of-month is invalid for the month-year

- from

```java
public static
HijrahDate
from​(
TemporalAccessor
temporal)
```

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar from a temporal object.

This obtains a date in the Hijrah calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

HijrahDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

HijrahDate::from

.

**Parameters:** temporal

- the temporal object to convert, not null
**Returns:** the date in Hijrah calendar system, not null
**Throws:** DateTimeException

- if unable to convert to a

HijrahDate
**See Also:** Chronology.date(TemporalAccessor)

- getChronology

```java
public
HijrahChronology
getChronology()
```

Gets the chronology of this date, which is the Hijrah calendar system.

The

Chronology

represents the calendar system in use.
The era and other fields in

ChronoField

are defined by the chronology.

**Specified by:** getChronology

in interface

ChronoLocalDate
**Returns:** the Hijrah chronology, not null

- getEra

```java
public
HijrahEra
getEra()
```

Gets the era applicable at this date.

The Hijrah calendar system has one era, 'AH',
defined by

HijrahEra

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
Month lengths in the Hijrah calendar system vary between 29 and 30 days.

**Specified by:** lengthOfMonth

in interface

ChronoLocalDate
**Returns:** the length of the month in days

- lengthOfYear

```java
public int lengthOfYear()
```

Returns the length of the year represented by this date.

This returns the length of the year in days.
A Hijrah calendar system year is typically shorter than
that of the ISO calendar system.

**Specified by:** lengthOfYear

in interface

ChronoLocalDate
**Returns:** the length of the year in days

- with

```java
public
HijrahDate
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

- if unable to make the adjustment.
For example, if the adjuster requires an ISO chronology
**Throws:** ArithmeticException

- if numeric overflow occurs

- withVariant

```java
public
HijrahDate
withVariant​(
HijrahChronology
chronology)
```

Returns a

HijrahDate

with the Chronology requested.

The year, month, and day are checked against the new requested
HijrahChronology. If the chronology has a shorter month length
for the month, the day is reduced to be the last day of the month.

**Parameters:** chronology

- the new HijrahChonology, non-null
**Returns:** a HijrahDate with the requested HijrahChronology, non-null

- plus

```java
public
HijrahDate
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
HijrahDate
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

- isLeapYear

```java
public boolean isLeapYear()
```

Checks if the year is a leap year, according to the Hijrah calendar system rules.

**Specified by:** isLeapYear

in interface

ChronoLocalDate
**Returns:** true if this date is in a leap year

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this date to another date, including the chronology.

Compares this

HijrahDate

with another ensuring that the date is the same.

Only objects of type

HijrahDate

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
**Returns:** true if this is equal to the other date and the Chronologies are equal
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
HijrahDate
now()
```

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the default time-zone.

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

HijrahDate

now()

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the default time-zone.

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
HijrahDate
now​(
ZoneId
zone)
```

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the specified time-zone.

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

HijrahDate

now​(

ZoneId

zone)

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
in the specified time-zone.

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
HijrahDate
now​(
Clock
clock)
```

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
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

HijrahDate

now​(

Clock

clock)

Obtains the current

HijrahDate

of the Islamic Umm Al-Qura calendar
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
HijrahDate
of​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar
from the proleptic-year, month-of-year and day-of-month fields.

This returns a

HijrahDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

**Parameters:** prolepticYear

- the Hijrah proleptic-year
**Parameters:** month

- the Hijrah month-of-year, from 1 to 12
**Parameters:** dayOfMonth

- the Hijrah day-of-month, from 1 to 30
**Returns:** the date in Hijrah calendar system, not null
**Throws:** DateTimeException

- if the value of any field is out of range,
or if the day-of-month is invalid for the month-year

---

#### of

public static

HijrahDate

of​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar
from the proleptic-year, month-of-year and day-of-month fields.

This returns a

HijrahDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

This returns a

HijrahDate

with the specified fields.
The day must be valid for the year and month, otherwise an exception will be thrown.

from

```java
public static
HijrahDate
from​(
TemporalAccessor
temporal)
```

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar from a temporal object.

This obtains a date in the Hijrah calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

HijrahDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

HijrahDate::from

.

**Parameters:** temporal

- the temporal object to convert, not null
**Returns:** the date in Hijrah calendar system, not null
**Throws:** DateTimeException

- if unable to convert to a

HijrahDate
**See Also:** Chronology.date(TemporalAccessor)

---

#### from

public static

HijrahDate

from​(

TemporalAccessor

temporal)

Obtains a

HijrahDate

of the Islamic Umm Al-Qura calendar from a temporal object.

This obtains a date in the Hijrah calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

HijrahDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

HijrahDate::from

.

This obtains a date in the Hijrah calendar system based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

HijrahDate

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

HijrahDate::from

.

The conversion typically uses the

EPOCH_DAY

field, which is standardized across calendar systems.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

HijrahDate::from

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

HijrahDate::from

.

getChronology

```java
public
HijrahChronology
getChronology()
```

Gets the chronology of this date, which is the Hijrah calendar system.

The

Chronology

represents the calendar system in use.
The era and other fields in

ChronoField

are defined by the chronology.

**Specified by:** getChronology

in interface

ChronoLocalDate
**Returns:** the Hijrah chronology, not null

---

#### getChronology

public

HijrahChronology

getChronology()

Gets the chronology of this date, which is the Hijrah calendar system.

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
HijrahEra
getEra()
```

Gets the era applicable at this date.

The Hijrah calendar system has one era, 'AH',
defined by

HijrahEra

.

**Specified by:** getEra

in interface

ChronoLocalDate
**Returns:** the era applicable at this date, not null

---

#### getEra

public

HijrahEra

getEra()

Gets the era applicable at this date.

The Hijrah calendar system has one era, 'AH',
defined by

HijrahEra

.

The Hijrah calendar system has one era, 'AH',
defined by

HijrahEra

.

lengthOfMonth

```java
public int lengthOfMonth()
```

Returns the length of the month represented by this date.

This returns the length of the month in days.
Month lengths in the Hijrah calendar system vary between 29 and 30 days.

**Specified by:** lengthOfMonth

in interface

ChronoLocalDate
**Returns:** the length of the month in days

---

#### lengthOfMonth

public int lengthOfMonth()

Returns the length of the month represented by this date.

This returns the length of the month in days.
Month lengths in the Hijrah calendar system vary between 29 and 30 days.

This returns the length of the month in days.
Month lengths in the Hijrah calendar system vary between 29 and 30 days.

lengthOfYear

```java
public int lengthOfYear()
```

Returns the length of the year represented by this date.

This returns the length of the year in days.
A Hijrah calendar system year is typically shorter than
that of the ISO calendar system.

**Specified by:** lengthOfYear

in interface

ChronoLocalDate
**Returns:** the length of the year in days

---

#### lengthOfYear

public int lengthOfYear()

Returns the length of the year represented by this date.

This returns the length of the year in days.
A Hijrah calendar system year is typically shorter than
that of the ISO calendar system.

This returns the length of the year in days.
A Hijrah calendar system year is typically shorter than
that of the ISO calendar system.

with

```java
public
HijrahDate
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

- if unable to make the adjustment.
For example, if the adjuster requires an ISO chronology
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### with

public

HijrahDate

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

withVariant

```java
public
HijrahDate
withVariant​(
HijrahChronology
chronology)
```

Returns a

HijrahDate

with the Chronology requested.

The year, month, and day are checked against the new requested
HijrahChronology. If the chronology has a shorter month length
for the month, the day is reduced to be the last day of the month.

**Parameters:** chronology

- the new HijrahChonology, non-null
**Returns:** a HijrahDate with the requested HijrahChronology, non-null

---

#### withVariant

public

HijrahDate

withVariant​(

HijrahChronology

chronology)

Returns a

HijrahDate

with the Chronology requested.

The year, month, and day are checked against the new requested
HijrahChronology. If the chronology has a shorter month length
for the month, the day is reduced to be the last day of the month.

The year, month, and day are checked against the new requested
HijrahChronology. If the chronology has a shorter month length
for the month, the day is reduced to be the last day of the month.

plus

```java
public
HijrahDate
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

HijrahDate

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
HijrahDate
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

HijrahDate

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

isLeapYear

```java
public boolean isLeapYear()
```

Checks if the year is a leap year, according to the Hijrah calendar system rules.

**Specified by:** isLeapYear

in interface

ChronoLocalDate
**Returns:** true if this date is in a leap year

---

#### isLeapYear

public boolean isLeapYear()

Checks if the year is a leap year, according to the Hijrah calendar system rules.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this date to another date, including the chronology.

Compares this

HijrahDate

with another ensuring that the date is the same.

Only objects of type

HijrahDate

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
**Returns:** true if this is equal to the other date and the Chronologies are equal
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

HijrahDate

with another ensuring that the date is the same.

Only objects of type

HijrahDate

are compared, other types return false.
To compare the dates of two

TemporalAccessor

instances, including dates
in two different chronologies, use

ChronoField.EPOCH_DAY

as a comparator.

Compares this

HijrahDate

with another ensuring that the date is the same.

Only objects of type

HijrahDate

are compared, other types return false.
To compare the dates of two

TemporalAccessor

instances, including dates
in two different chronologies, use

ChronoField.EPOCH_DAY

as a comparator.

Only objects of type

HijrahDate

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

