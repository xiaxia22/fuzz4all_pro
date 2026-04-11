# Class ThaiBuddhistChronology

**Source:** `java.base\java\time\chrono\ThaiBuddhistChronology.html`

### Class Description

```java
public final class
ThaiBuddhistChronology

extends
AbstractChronology

implements
Serializable
```

The Thai Buddhist calendar system.

This chronology defines the rules of the Thai Buddhist calendar system.
This calendar system is primarily used in Thailand.
Dates are aligned such that

2484-01-01 (Buddhist)

is

1941-01-01 (ISO)

.

The fields are defined as follows:

- era - There are two eras, the current 'Buddhist' (ERA_BE) and the previous era (ERA_BEFORE_BE).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year plus 543.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year plus 543.

month-of-year - The ThaiBuddhist month-of-year exactly matches ISO.

day-of-month - The ThaiBuddhist day-of-month exactly matches ISO.

day-of-year - The ThaiBuddhist day-of-year exactly matches ISO.

leap-year - The ThaiBuddhist leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Chronology

>

,

Chronology

---

### Field Details

#### public static final
ThaiBuddhistChronology
INSTANCE

Singleton instance of the Buddhist chronology.

---

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getId()

Gets the ID of the chronology - 'ThaiBuddhist'.

The ID uniquely identifies the

Chronology

.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:**
- getId

in interface

Chronology

**Returns:**
- the chronology ID - 'ThaiBuddhist'

**See Also:**
- getCalendarType()

---

#### public
String
getCalendarType()

Gets the calendar type of the underlying calendar system - 'buddhist'.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.
It can also be used as part of a locale, accessible via

Locale.getUnicodeLocaleType(String)

with the key 'ca'.

**Specified by:**
- getCalendarType

in interface

Chronology

**Returns:**
- the calendar system type - 'buddhist'

**See Also:**
- getId()

---

#### public
ThaiBuddhistDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:**
- date

in interface

Chronology

**Parameters:**
- era

- the Thai Buddhist era, not null
- yearOfEra

- the year-of-era
- month

- the month-of-year
- dayOfMonth

- the day-of-month

**Returns:**
- the Thai Buddhist local date, not null

**Throws:**
- DateTimeException

- if unable to create the date
- ClassCastException

- if the

era

is not a

ThaiBuddhistEra

---

#### public
ThaiBuddhistDate
date​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year, month-of-year and day-of-month fields.

**Specified by:**
- date

in interface

Chronology

**Parameters:**
- prolepticYear

- the proleptic-year
- month

- the month-of-year
- dayOfMonth

- the day-of-month

**Returns:**
- the Thai Buddhist local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public
ThaiBuddhistDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:**
- dateYearDay

in interface

Chronology

**Parameters:**
- era

- the Thai Buddhist era, not null
- yearOfEra

- the year-of-era
- dayOfYear

- the day-of-year

**Returns:**
- the Thai Buddhist local date, not null

**Throws:**
- DateTimeException

- if unable to create the date
- ClassCastException

- if the

era

is not a

ThaiBuddhistEra

---

#### public
ThaiBuddhistDate
dateYearDay​(int prolepticYear,
int dayOfYear)

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year and day-of-year fields.

**Specified by:**
- dateYearDay

in interface

Chronology

**Parameters:**
- prolepticYear

- the proleptic-year
- dayOfYear

- the day-of-year

**Returns:**
- the Thai Buddhist local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public
ThaiBuddhistDate
dateEpochDay​(long epochDay)

Obtains a local date in the Thai Buddhist calendar system from the epoch-day.

**Specified by:**
- dateEpochDay

in interface

Chronology

**Parameters:**
- epochDay

- the epoch day

**Returns:**
- the Thai Buddhist local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public boolean isLeapYear​(long prolepticYear)

Checks if the specified year is a leap year.

Thai Buddhist leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

**Specified by:**
- isLeapYear

in interface

Chronology

**Parameters:**
- prolepticYear

- the proleptic-year to check, not validated for range

**Returns:**
- true if the year is a leap year

---

### Additional Sections

#### Class ThaiBuddhistChronology

java.lang.Object

- java.time.chrono.AbstractChronology
- - java.time.chrono.ThaiBuddhistChronology

java.time.chrono.AbstractChronology

- java.time.chrono.ThaiBuddhistChronology

java.time.chrono.ThaiBuddhistChronology

**All Implemented Interfaces:** Serializable

,

Comparable

<

Chronology

>

,

Chronology

```java
public final class
ThaiBuddhistChronology

extends
AbstractChronology

implements
Serializable
```

The Thai Buddhist calendar system.

This chronology defines the rules of the Thai Buddhist calendar system.
This calendar system is primarily used in Thailand.
Dates are aligned such that

2484-01-01 (Buddhist)

is

1941-01-01 (ISO)

.

The fields are defined as follows:

- era - There are two eras, the current 'Buddhist' (ERA_BE) and the previous era (ERA_BEFORE_BE).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year plus 543.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year plus 543.

month-of-year - The ThaiBuddhist month-of-year exactly matches ISO.

day-of-month - The ThaiBuddhist day-of-month exactly matches ISO.

day-of-year - The ThaiBuddhist day-of-year exactly matches ISO.

leap-year - The ThaiBuddhist leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8
**See Also:** Serialized Form

public final class

ThaiBuddhistChronology

extends

AbstractChronology

implements

Serializable

The Thai Buddhist calendar system.

This chronology defines the rules of the Thai Buddhist calendar system.
This calendar system is primarily used in Thailand.
Dates are aligned such that

2484-01-01 (Buddhist)

is

1941-01-01 (ISO)

.

The fields are defined as follows:

- era - There are two eras, the current 'Buddhist' (ERA_BE) and the previous era (ERA_BEFORE_BE).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year plus 543.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year plus 543.

month-of-year - The ThaiBuddhist month-of-year exactly matches ISO.

day-of-month - The ThaiBuddhist day-of-month exactly matches ISO.

day-of-year - The ThaiBuddhist day-of-year exactly matches ISO.

leap-year - The ThaiBuddhist leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

This chronology defines the rules of the Thai Buddhist calendar system.
This calendar system is primarily used in Thailand.
Dates are aligned such that

2484-01-01 (Buddhist)

is

1941-01-01 (ISO)

.

The fields are defined as follows:

- era - There are two eras, the current 'Buddhist' (ERA_BE) and the previous era (ERA_BEFORE_BE).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year plus 543.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year plus 543.

month-of-year - The ThaiBuddhist month-of-year exactly matches ISO.

day-of-month - The ThaiBuddhist day-of-month exactly matches ISO.

day-of-year - The ThaiBuddhist day-of-year exactly matches ISO.

leap-year - The ThaiBuddhist leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

The fields are defined as follows:

- era - There are two eras, the current 'Buddhist' (ERA_BE) and the previous era (ERA_BEFORE_BE).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year plus 543.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year plus 543.

month-of-year - The ThaiBuddhist month-of-year exactly matches ISO.

day-of-month - The ThaiBuddhist day-of-month exactly matches ISO.

day-of-year - The ThaiBuddhist day-of-year exactly matches ISO.

leap-year - The ThaiBuddhist leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

era - There are two eras, the current 'Buddhist' (ERA_BE) and the previous era (ERA_BEFORE_BE).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year plus 543.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year plus 543.

month-of-year - The ThaiBuddhist month-of-year exactly matches ISO.

day-of-month - The ThaiBuddhist day-of-month exactly matches ISO.

day-of-year - The ThaiBuddhist day-of-year exactly matches ISO.

leap-year - The ThaiBuddhist leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ThaiBuddhistChronology

INSTANCE

Singleton instance of the Buddhist chronology.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ThaiBuddhistDate

date

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year, month-of-year and day-of-month fields.

ThaiBuddhistDate

date

​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

ThaiBuddhistDate

dateEpochDay

​(long epochDay)

Obtains a local date in the Thai Buddhist calendar system from the epoch-day.

ThaiBuddhistDate

dateYearDay

​(int prolepticYear,
int dayOfYear)

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year and day-of-year fields.

ThaiBuddhistDate

dateYearDay

​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era and day-of-year fields.

String

getCalendarType

()

Gets the calendar type of the underlying calendar system - 'buddhist'.

String

getId

()

Gets the ID of the chronology - 'ThaiBuddhist'.

boolean

isLeapYear

​(long prolepticYear)

Checks if the specified year is a leap year.

- Methods declared in class java.time.chrono.

AbstractChronology

compareTo

,

equals

,

hashCode

,

resolveDate

,

toString

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

Chronology

date

,

dateNow

,

dateNow

,

dateNow

,

epochSecond

,

epochSecond

,

eraOf

,

eras

,

getDisplayName

,

localDateTime

,

period

,

prolepticYear

,

range

,

zonedDateTime

,

zonedDateTime

Field Summary

Fields

Modifier and Type

Field

Description

static

ThaiBuddhistChronology

INSTANCE

Singleton instance of the Buddhist chronology.

---

#### Field Summary

Singleton instance of the Buddhist chronology.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ThaiBuddhistDate

date

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year, month-of-year and day-of-month fields.

ThaiBuddhistDate

date

​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

ThaiBuddhistDate

dateEpochDay

​(long epochDay)

Obtains a local date in the Thai Buddhist calendar system from the epoch-day.

ThaiBuddhistDate

dateYearDay

​(int prolepticYear,
int dayOfYear)

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year and day-of-year fields.

ThaiBuddhistDate

dateYearDay

​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era and day-of-year fields.

String

getCalendarType

()

Gets the calendar type of the underlying calendar system - 'buddhist'.

String

getId

()

Gets the ID of the chronology - 'ThaiBuddhist'.

boolean

isLeapYear

​(long prolepticYear)

Checks if the specified year is a leap year.

- Methods declared in class java.time.chrono.

AbstractChronology

compareTo

,

equals

,

hashCode

,

resolveDate

,

toString

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

Chronology

date

,

dateNow

,

dateNow

,

dateNow

,

epochSecond

,

epochSecond

,

eraOf

,

eras

,

getDisplayName

,

localDateTime

,

period

,

prolepticYear

,

range

,

zonedDateTime

,

zonedDateTime

---

#### Method Summary

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year, month-of-year and day-of-month fields.

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

Obtains a local date in the Thai Buddhist calendar system from the epoch-day.

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year and day-of-year fields.

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era and day-of-year fields.

Gets the calendar type of the underlying calendar system - 'buddhist'.

Gets the ID of the chronology - 'ThaiBuddhist'.

Checks if the specified year is a leap year.

Methods declared in class java.time.chrono.

AbstractChronology

compareTo

,

equals

,

hashCode

,

resolveDate

,

toString

---

#### Methods declared in class java.time.chrono. AbstractChronology

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

Chronology

date

,

dateNow

,

dateNow

,

dateNow

,

epochSecond

,

epochSecond

,

eraOf

,

eras

,

getDisplayName

,

localDateTime

,

period

,

prolepticYear

,

range

,

zonedDateTime

,

zonedDateTime

---

#### Methods declared in interface java.time.chrono. Chronology

============ FIELD DETAIL ===========

- Field Detail

- INSTANCE

```java
public static final
ThaiBuddhistChronology
INSTANCE
```

Singleton instance of the Buddhist chronology.

============ METHOD DETAIL ==========

- Method Detail

- getId

```java
public
String
getId()
```

Gets the ID of the chronology - 'ThaiBuddhist'.

The ID uniquely identifies the

Chronology

.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:** getId

in interface

Chronology
**Returns:** the chronology ID - 'ThaiBuddhist'
**See Also:** getCalendarType()

- getCalendarType

```java
public
String
getCalendarType()
```

Gets the calendar type of the underlying calendar system - 'buddhist'.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.
It can also be used as part of a locale, accessible via

Locale.getUnicodeLocaleType(String)

with the key 'ca'.

**Specified by:** getCalendarType

in interface

Chronology
**Returns:** the calendar system type - 'buddhist'
**See Also:** getId()

- date

```java
public
ThaiBuddhistDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Thai Buddhist era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

ThaiBuddhistEra

- date

```java
public
ThaiBuddhistDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateYearDay

```java
public
ThaiBuddhistDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Thai Buddhist era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

ThaiBuddhistEra

- dateYearDay

```java
public
ThaiBuddhistDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateEpochDay

```java
public
ThaiBuddhistDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Thai Buddhist calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date

- isLeapYear

```java
public boolean isLeapYear​(long prolepticYear)
```

Checks if the specified year is a leap year.

Thai Buddhist leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

**Specified by:** isLeapYear

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year to check, not validated for range
**Returns:** true if the year is a leap year

Field Detail

- INSTANCE

```java
public static final
ThaiBuddhistChronology
INSTANCE
```

Singleton instance of the Buddhist chronology.

---

#### Field Detail

INSTANCE

```java
public static final
ThaiBuddhistChronology
INSTANCE
```

Singleton instance of the Buddhist chronology.

---

#### INSTANCE

public static final

ThaiBuddhistChronology

INSTANCE

Singleton instance of the Buddhist chronology.

Method Detail

- getId

```java
public
String
getId()
```

Gets the ID of the chronology - 'ThaiBuddhist'.

The ID uniquely identifies the

Chronology

.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:** getId

in interface

Chronology
**Returns:** the chronology ID - 'ThaiBuddhist'
**See Also:** getCalendarType()

- getCalendarType

```java
public
String
getCalendarType()
```

Gets the calendar type of the underlying calendar system - 'buddhist'.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.
It can also be used as part of a locale, accessible via

Locale.getUnicodeLocaleType(String)

with the key 'ca'.

**Specified by:** getCalendarType

in interface

Chronology
**Returns:** the calendar system type - 'buddhist'
**See Also:** getId()

- date

```java
public
ThaiBuddhistDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Thai Buddhist era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

ThaiBuddhistEra

- date

```java
public
ThaiBuddhistDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateYearDay

```java
public
ThaiBuddhistDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Thai Buddhist era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

ThaiBuddhistEra

- dateYearDay

```java
public
ThaiBuddhistDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateEpochDay

```java
public
ThaiBuddhistDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Thai Buddhist calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date

- isLeapYear

```java
public boolean isLeapYear​(long prolepticYear)
```

Checks if the specified year is a leap year.

Thai Buddhist leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

**Specified by:** isLeapYear

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year to check, not validated for range
**Returns:** true if the year is a leap year

---

#### Method Detail

getId

```java
public
String
getId()
```

Gets the ID of the chronology - 'ThaiBuddhist'.

The ID uniquely identifies the

Chronology

.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:** getId

in interface

Chronology
**Returns:** the chronology ID - 'ThaiBuddhist'
**See Also:** getCalendarType()

---

#### getId

public

String

getId()

Gets the ID of the chronology - 'ThaiBuddhist'.

The ID uniquely identifies the

Chronology

.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

The ID uniquely identifies the

Chronology

.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

getCalendarType

```java
public
String
getCalendarType()
```

Gets the calendar type of the underlying calendar system - 'buddhist'.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.
It can also be used as part of a locale, accessible via

Locale.getUnicodeLocaleType(String)

with the key 'ca'.

**Specified by:** getCalendarType

in interface

Chronology
**Returns:** the calendar system type - 'buddhist'
**See Also:** getId()

---

#### getCalendarType

public

String

getCalendarType()

Gets the calendar type of the underlying calendar system - 'buddhist'.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.
It can also be used as part of a locale, accessible via

Locale.getUnicodeLocaleType(String)

with the key 'ca'.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.
It can also be used as part of a locale, accessible via

Locale.getUnicodeLocaleType(String)

with the key 'ca'.

date

```java
public
ThaiBuddhistDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Thai Buddhist era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

ThaiBuddhistEra

---

#### date

public

ThaiBuddhistDate

date​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

date

```java
public
ThaiBuddhistDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### date

public

ThaiBuddhistDate

date​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year, month-of-year and day-of-month fields.

dateYearDay

```java
public
ThaiBuddhistDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Thai Buddhist era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

ThaiBuddhistEra

---

#### dateYearDay

public

ThaiBuddhistDate

dateYearDay​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Thai Buddhist calendar system from the
era, year-of-era and day-of-year fields.

dateYearDay

```java
public
ThaiBuddhistDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### dateYearDay

public

ThaiBuddhistDate

dateYearDay​(int prolepticYear,
int dayOfYear)

Obtains a local date in Thai Buddhist calendar system from the
proleptic-year and day-of-year fields.

dateEpochDay

```java
public
ThaiBuddhistDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Thai Buddhist calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Thai Buddhist local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### dateEpochDay

public

ThaiBuddhistDate

dateEpochDay​(long epochDay)

Obtains a local date in the Thai Buddhist calendar system from the epoch-day.

isLeapYear

```java
public boolean isLeapYear​(long prolepticYear)
```

Checks if the specified year is a leap year.

Thai Buddhist leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

**Specified by:** isLeapYear

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year to check, not validated for range
**Returns:** true if the year is a leap year

---

#### isLeapYear

public boolean isLeapYear​(long prolepticYear)

Checks if the specified year is a leap year.

Thai Buddhist leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

Thai Buddhist leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

---

