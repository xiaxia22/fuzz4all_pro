# Class MinguoChronology

**Source:** `java.base\java\time\chrono\MinguoChronology.html`

### Class Description

```java
public final class
MinguoChronology

extends
AbstractChronology

implements
Serializable
```

The Minguo calendar system.

This chronology defines the rules of the Minguo calendar system.
This calendar system is primarily used in the Republic of China, often known as Taiwan.
Dates are aligned such that

0001-01-01 (Minguo)

is

1912-01-01 (ISO)

.

The fields are defined as follows:

- era - There are two eras, the current 'Republic' (ERA_ROC) and the previous era (ERA_BEFORE_ROC).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year minus 1911.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year minus 1911.

month-of-year - The Minguo month-of-year exactly matches ISO.

day-of-month - The Minguo day-of-month exactly matches ISO.

day-of-year - The Minguo day-of-year exactly matches ISO.

leap-year - The Minguo leap-year pattern exactly matches ISO, such that the two calendars
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
MinguoChronology
INSTANCE

Singleton instance for the Minguo chronology.

---

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getId()

Gets the ID of the chronology - 'Minguo'.

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
- the chronology ID - 'Minguo'

**See Also:**
- getCalendarType()

---

#### public
String
getCalendarType()

Gets the calendar type of the underlying calendar system - 'roc'.

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
- the calendar system type - 'roc'

**See Also:**
- getId()

---

#### public
MinguoDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Minguo calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:**
- date

in interface

Chronology

**Parameters:**
- era

- the Minguo era, not null
- yearOfEra

- the year-of-era
- month

- the month-of-year
- dayOfMonth

- the day-of-month

**Returns:**
- the Minguo local date, not null

**Throws:**
- DateTimeException

- if unable to create the date
- ClassCastException

- if the

era

is not a

MinguoEra

---

#### public
MinguoDate
date​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Minguo calendar system from the
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
- the Minguo local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public
MinguoDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Minguo calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:**
- dateYearDay

in interface

Chronology

**Parameters:**
- era

- the Minguo era, not null
- yearOfEra

- the year-of-era
- dayOfYear

- the day-of-year

**Returns:**
- the Minguo local date, not null

**Throws:**
- DateTimeException

- if unable to create the date
- ClassCastException

- if the

era

is not a

MinguoEra

---

#### public
MinguoDate
dateYearDay​(int prolepticYear,
int dayOfYear)

Obtains a local date in Minguo calendar system from the
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
- the Minguo local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public
MinguoDate
dateEpochDay​(long epochDay)

Obtains a local date in the Minguo calendar system from the epoch-day.

**Specified by:**
- dateEpochDay

in interface

Chronology

**Parameters:**
- epochDay

- the epoch day

**Returns:**
- the Minguo local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public boolean isLeapYear​(long prolepticYear)

Checks if the specified year is a leap year.

Minguo leap years occur exactly in line with ISO leap years.
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

#### Class MinguoChronology

java.lang.Object

- java.time.chrono.AbstractChronology
- - java.time.chrono.MinguoChronology

java.time.chrono.AbstractChronology

- java.time.chrono.MinguoChronology

java.time.chrono.MinguoChronology

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
MinguoChronology

extends
AbstractChronology

implements
Serializable
```

The Minguo calendar system.

This chronology defines the rules of the Minguo calendar system.
This calendar system is primarily used in the Republic of China, often known as Taiwan.
Dates are aligned such that

0001-01-01 (Minguo)

is

1912-01-01 (ISO)

.

The fields are defined as follows:

- era - There are two eras, the current 'Republic' (ERA_ROC) and the previous era (ERA_BEFORE_ROC).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year minus 1911.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year minus 1911.

month-of-year - The Minguo month-of-year exactly matches ISO.

day-of-month - The Minguo day-of-month exactly matches ISO.

day-of-year - The Minguo day-of-year exactly matches ISO.

leap-year - The Minguo leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8
**See Also:** Serialized Form

public final class

MinguoChronology

extends

AbstractChronology

implements

Serializable

The Minguo calendar system.

This chronology defines the rules of the Minguo calendar system.
This calendar system is primarily used in the Republic of China, often known as Taiwan.
Dates are aligned such that

0001-01-01 (Minguo)

is

1912-01-01 (ISO)

.

The fields are defined as follows:

- era - There are two eras, the current 'Republic' (ERA_ROC) and the previous era (ERA_BEFORE_ROC).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year minus 1911.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year minus 1911.

month-of-year - The Minguo month-of-year exactly matches ISO.

day-of-month - The Minguo day-of-month exactly matches ISO.

day-of-year - The Minguo day-of-year exactly matches ISO.

leap-year - The Minguo leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

This chronology defines the rules of the Minguo calendar system.
This calendar system is primarily used in the Republic of China, often known as Taiwan.
Dates are aligned such that

0001-01-01 (Minguo)

is

1912-01-01 (ISO)

.

The fields are defined as follows:

- era - There are two eras, the current 'Republic' (ERA_ROC) and the previous era (ERA_BEFORE_ROC).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year minus 1911.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year minus 1911.

month-of-year - The Minguo month-of-year exactly matches ISO.

day-of-month - The Minguo day-of-month exactly matches ISO.

day-of-year - The Minguo day-of-year exactly matches ISO.

leap-year - The Minguo leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

The fields are defined as follows:

- era - There are two eras, the current 'Republic' (ERA_ROC) and the previous era (ERA_BEFORE_ROC).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year minus 1911.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year minus 1911.

month-of-year - The Minguo month-of-year exactly matches ISO.

day-of-month - The Minguo day-of-month exactly matches ISO.

day-of-year - The Minguo day-of-year exactly matches ISO.

leap-year - The Minguo leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

era - There are two eras, the current 'Republic' (ERA_ROC) and the previous era (ERA_BEFORE_ROC).

year-of-era - The year-of-era for the current era increases uniformly from the epoch at year one.
For the previous era the year increases from one as time goes backwards.
The value for the current era is equal to the ISO proleptic-year minus 1911.

proleptic-year - The proleptic year is the same as the year-of-era for the
current era. For the previous era, years have zero, then negative values.
The value is equal to the ISO proleptic-year minus 1911.

month-of-year - The Minguo month-of-year exactly matches ISO.

day-of-month - The Minguo day-of-month exactly matches ISO.

day-of-year - The Minguo day-of-year exactly matches ISO.

leap-year - The Minguo leap-year pattern exactly matches ISO, such that the two calendars
are never out of step.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

MinguoChronology

INSTANCE

Singleton instance for the Minguo chronology.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MinguoDate

date

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Minguo calendar system from the
proleptic-year, month-of-year and day-of-month fields.

MinguoDate

date

​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Minguo calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

MinguoDate

dateEpochDay

​(long epochDay)

Obtains a local date in the Minguo calendar system from the epoch-day.

MinguoDate

dateYearDay

​(int prolepticYear,
int dayOfYear)

Obtains a local date in Minguo calendar system from the
proleptic-year and day-of-year fields.

MinguoDate

dateYearDay

​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Minguo calendar system from the
era, year-of-era and day-of-year fields.

String

getCalendarType

()

Gets the calendar type of the underlying calendar system - 'roc'.

String

getId

()

Gets the ID of the chronology - 'Minguo'.

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

MinguoChronology

INSTANCE

Singleton instance for the Minguo chronology.

---

#### Field Summary

Singleton instance for the Minguo chronology.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MinguoDate

date

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Minguo calendar system from the
proleptic-year, month-of-year and day-of-month fields.

MinguoDate

date

​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Minguo calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

MinguoDate

dateEpochDay

​(long epochDay)

Obtains a local date in the Minguo calendar system from the epoch-day.

MinguoDate

dateYearDay

​(int prolepticYear,
int dayOfYear)

Obtains a local date in Minguo calendar system from the
proleptic-year and day-of-year fields.

MinguoDate

dateYearDay

​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Minguo calendar system from the
era, year-of-era and day-of-year fields.

String

getCalendarType

()

Gets the calendar type of the underlying calendar system - 'roc'.

String

getId

()

Gets the ID of the chronology - 'Minguo'.

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

Obtains a local date in Minguo calendar system from the
proleptic-year, month-of-year and day-of-month fields.

Obtains a local date in Minguo calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

Obtains a local date in the Minguo calendar system from the epoch-day.

Obtains a local date in Minguo calendar system from the
proleptic-year and day-of-year fields.

Obtains a local date in Minguo calendar system from the
era, year-of-era and day-of-year fields.

Gets the calendar type of the underlying calendar system - 'roc'.

Gets the ID of the chronology - 'Minguo'.

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
MinguoChronology
INSTANCE
```

Singleton instance for the Minguo chronology.

============ METHOD DETAIL ==========

- Method Detail

- getId

```java
public
String
getId()
```

Gets the ID of the chronology - 'Minguo'.

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
**Returns:** the chronology ID - 'Minguo'
**See Also:** getCalendarType()

- getCalendarType

```java
public
String
getCalendarType()
```

Gets the calendar type of the underlying calendar system - 'roc'.

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
**Returns:** the calendar system type - 'roc'
**See Also:** getId()

- date

```java
public
MinguoDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Minguo calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Minguo era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

MinguoEra

- date

```java
public
MinguoDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Minguo calendar system from the
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
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateYearDay

```java
public
MinguoDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Minguo calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Minguo era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

MinguoEra

- dateYearDay

```java
public
MinguoDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Minguo calendar system from the
proleptic-year and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateEpochDay

```java
public
MinguoDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Minguo calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date

- isLeapYear

```java
public boolean isLeapYear​(long prolepticYear)
```

Checks if the specified year is a leap year.

Minguo leap years occur exactly in line with ISO leap years.
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
MinguoChronology
INSTANCE
```

Singleton instance for the Minguo chronology.

---

#### Field Detail

INSTANCE

```java
public static final
MinguoChronology
INSTANCE
```

Singleton instance for the Minguo chronology.

---

#### INSTANCE

public static final

MinguoChronology

INSTANCE

Singleton instance for the Minguo chronology.

Method Detail

- getId

```java
public
String
getId()
```

Gets the ID of the chronology - 'Minguo'.

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
**Returns:** the chronology ID - 'Minguo'
**See Also:** getCalendarType()

- getCalendarType

```java
public
String
getCalendarType()
```

Gets the calendar type of the underlying calendar system - 'roc'.

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
**Returns:** the calendar system type - 'roc'
**See Also:** getId()

- date

```java
public
MinguoDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Minguo calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Minguo era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

MinguoEra

- date

```java
public
MinguoDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Minguo calendar system from the
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
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateYearDay

```java
public
MinguoDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Minguo calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Minguo era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

MinguoEra

- dateYearDay

```java
public
MinguoDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Minguo calendar system from the
proleptic-year and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateEpochDay

```java
public
MinguoDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Minguo calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date

- isLeapYear

```java
public boolean isLeapYear​(long prolepticYear)
```

Checks if the specified year is a leap year.

Minguo leap years occur exactly in line with ISO leap years.
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

Gets the ID of the chronology - 'Minguo'.

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
**Returns:** the chronology ID - 'Minguo'
**See Also:** getCalendarType()

---

#### getId

public

String

getId()

Gets the ID of the chronology - 'Minguo'.

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

Gets the calendar type of the underlying calendar system - 'roc'.

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
**Returns:** the calendar system type - 'roc'
**See Also:** getId()

---

#### getCalendarType

public

String

getCalendarType()

Gets the calendar type of the underlying calendar system - 'roc'.

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
MinguoDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Minguo calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Minguo era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

MinguoEra

---

#### date

public

MinguoDate

date​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Minguo calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

date

```java
public
MinguoDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Minguo calendar system from the
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
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### date

public

MinguoDate

date​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Minguo calendar system from the
proleptic-year, month-of-year and day-of-month fields.

dateYearDay

```java
public
MinguoDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Minguo calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Minguo era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

MinguoEra

---

#### dateYearDay

public

MinguoDate

dateYearDay​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Minguo calendar system from the
era, year-of-era and day-of-year fields.

dateYearDay

```java
public
MinguoDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Minguo calendar system from the
proleptic-year and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### dateYearDay

public

MinguoDate

dateYearDay​(int prolepticYear,
int dayOfYear)

Obtains a local date in Minguo calendar system from the
proleptic-year and day-of-year fields.

dateEpochDay

```java
public
MinguoDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Minguo calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Minguo local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### dateEpochDay

public

MinguoDate

dateEpochDay​(long epochDay)

Obtains a local date in the Minguo calendar system from the epoch-day.

isLeapYear

```java
public boolean isLeapYear​(long prolepticYear)
```

Checks if the specified year is a leap year.

Minguo leap years occur exactly in line with ISO leap years.
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

Minguo leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

Minguo leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

---

