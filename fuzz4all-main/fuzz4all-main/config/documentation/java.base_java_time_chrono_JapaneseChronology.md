# Class JapaneseChronology

**Source:** `java.base\java\time\chrono\JapaneseChronology.html`

### Class Description

```java
public final class
JapaneseChronology

extends
AbstractChronology

implements
Serializable
```

The Japanese Imperial calendar system.

This chronology defines the rules of the Japanese Imperial calendar system.
This calendar system is primarily used in Japan.
The Japanese Imperial calendar system is the same as the ISO calendar system
apart from the era-based year numbering.

Japan introduced the Gregorian calendar starting with Meiji 6.
Only Meiji and later eras are supported;
dates before Meiji 6, January 1 are not supported.

The supported

ChronoField

instances are:

- DAY_OF_WEEK

DAY_OF_MONTH

DAY_OF_YEAR

EPOCH_DAY

MONTH_OF_YEAR

PROLEPTIC_MONTH

YEAR_OF_ERA

YEAR

ERA

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
JapaneseChronology
INSTANCE

Singleton instance for Japanese chronology.

---

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getId()

Gets the ID of the chronology - 'Japanese'.

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
- the chronology ID - 'Japanese'

**See Also:**
- getCalendarType()

---

#### public
String
getCalendarType()

Gets the calendar type of the underlying calendar system - 'japanese'.

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
- the calendar system type - 'japanese'

**See Also:**
- getId()

---

#### public
JapaneseDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Japanese calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

The Japanese month and day-of-month are the same as those in the
ISO calendar system. They are not reset when the era changes.
For example:

```java
6th Jan Showa 64 = ISO 1989-01-06
7th Jan Showa 64 = ISO 1989-01-07
8th Jan Heisei 1 = ISO 1989-01-08
9th Jan Heisei 1 = ISO 1989-01-09
```

**Specified by:**
- date

in interface

Chronology

**Parameters:**
- era

- the Japanese era, not null
- yearOfEra

- the year-of-era
- month

- the month-of-year
- dayOfMonth

- the day-of-month

**Returns:**
- the Japanese local date, not null

**Throws:**
- DateTimeException

- if unable to create the date
- ClassCastException

- if the

era

is not a

JapaneseEra

---

#### public
JapaneseDate
date​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Japanese calendar system from the
proleptic-year, month-of-year and day-of-month fields.

The Japanese proleptic year, month and day-of-month are the same as those
in the ISO calendar system. They are not reset when the era changes.

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
- the Japanese local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public
JapaneseDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Japanese calendar system from the
era, year-of-era and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the year-of-era.
This definition changes the normal meaning of day-of-year only in those years
where the year-of-era is reset to one due to a change in the era.
For example:

```java
6th Jan Showa 64 = day-of-year 6
7th Jan Showa 64 = day-of-year 7
8th Jan Heisei 1 = day-of-year 1
9th Jan Heisei 1 = day-of-year 2
```

**Specified by:**
- dateYearDay

in interface

Chronology

**Parameters:**
- era

- the Japanese era, not null
- yearOfEra

- the year-of-era
- dayOfYear

- the day-of-year

**Returns:**
- the Japanese local date, not null

**Throws:**
- DateTimeException

- if unable to create the date
- ClassCastException

- if the

era

is not a

JapaneseEra

---

#### public
JapaneseDate
dateYearDay​(int prolepticYear,
int dayOfYear)

Obtains a local date in Japanese calendar system from the
proleptic-year and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the proleptic year.
The Japanese proleptic year and day-of-year are the same as those in the ISO calendar system.
They are not reset when the era changes.

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
- the Japanese local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public
JapaneseDate
dateEpochDay​(long epochDay)

Obtains a local date in the Japanese calendar system from the epoch-day.

**Specified by:**
- dateEpochDay

in interface

Chronology

**Parameters:**
- epochDay

- the epoch day

**Returns:**
- the Japanese local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public boolean isLeapYear​(long prolepticYear)

Checks if the specified year is a leap year.

Japanese calendar leap years occur exactly in line with ISO leap years.
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

#### public
JapaneseEra
eraOf​(int eraValue)

Returns the calendar system era object from the given numeric value.

See the description of each Era for the numeric values of:

JapaneseEra.HEISEI

,

JapaneseEra.SHOWA

,

JapaneseEra.TAISHO

,

JapaneseEra.MEIJI

), only Meiji and later eras are supported.

**Specified by:**
- eraOf

in interface

Chronology

**Parameters:**
- eraValue

- the era value

**Returns:**
- the Japanese

Era

for the given numeric era value

**Throws:**
- DateTimeException

- if

eraValue

is invalid

---

### Additional Sections

#### Class JapaneseChronology

java.lang.Object

- java.time.chrono.AbstractChronology
- - java.time.chrono.JapaneseChronology

java.time.chrono.AbstractChronology

- java.time.chrono.JapaneseChronology

java.time.chrono.JapaneseChronology

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
JapaneseChronology

extends
AbstractChronology

implements
Serializable
```

The Japanese Imperial calendar system.

This chronology defines the rules of the Japanese Imperial calendar system.
This calendar system is primarily used in Japan.
The Japanese Imperial calendar system is the same as the ISO calendar system
apart from the era-based year numbering.

Japan introduced the Gregorian calendar starting with Meiji 6.
Only Meiji and later eras are supported;
dates before Meiji 6, January 1 are not supported.

The supported

ChronoField

instances are:

- DAY_OF_WEEK

DAY_OF_MONTH

DAY_OF_YEAR

EPOCH_DAY

MONTH_OF_YEAR

PROLEPTIC_MONTH

YEAR_OF_ERA

YEAR

ERA

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8
**See Also:** Serialized Form

public final class

JapaneseChronology

extends

AbstractChronology

implements

Serializable

The Japanese Imperial calendar system.

This chronology defines the rules of the Japanese Imperial calendar system.
This calendar system is primarily used in Japan.
The Japanese Imperial calendar system is the same as the ISO calendar system
apart from the era-based year numbering.

Japan introduced the Gregorian calendar starting with Meiji 6.
Only Meiji and later eras are supported;
dates before Meiji 6, January 1 are not supported.

The supported

ChronoField

instances are:

- DAY_OF_WEEK

DAY_OF_MONTH

DAY_OF_YEAR

EPOCH_DAY

MONTH_OF_YEAR

PROLEPTIC_MONTH

YEAR_OF_ERA

YEAR

ERA

This chronology defines the rules of the Japanese Imperial calendar system.
This calendar system is primarily used in Japan.
The Japanese Imperial calendar system is the same as the ISO calendar system
apart from the era-based year numbering.

Japan introduced the Gregorian calendar starting with Meiji 6.
Only Meiji and later eras are supported;
dates before Meiji 6, January 1 are not supported.

The supported

ChronoField

instances are:

- DAY_OF_WEEK

DAY_OF_MONTH

DAY_OF_YEAR

EPOCH_DAY

MONTH_OF_YEAR

PROLEPTIC_MONTH

YEAR_OF_ERA

YEAR

ERA

Japan introduced the Gregorian calendar starting with Meiji 6.
Only Meiji and later eras are supported;
dates before Meiji 6, January 1 are not supported.

The supported

ChronoField

instances are:

- DAY_OF_WEEK

DAY_OF_MONTH

DAY_OF_YEAR

EPOCH_DAY

MONTH_OF_YEAR

PROLEPTIC_MONTH

YEAR_OF_ERA

YEAR

ERA

The supported

ChronoField

instances are:

- DAY_OF_WEEK

DAY_OF_MONTH

DAY_OF_YEAR

EPOCH_DAY

MONTH_OF_YEAR

PROLEPTIC_MONTH

YEAR_OF_ERA

YEAR

ERA

DAY_OF_WEEK

DAY_OF_MONTH

DAY_OF_YEAR

EPOCH_DAY

MONTH_OF_YEAR

PROLEPTIC_MONTH

YEAR_OF_ERA

YEAR

ERA

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

JapaneseChronology

INSTANCE

Singleton instance for Japanese chronology.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JapaneseDate

date

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Japanese calendar system from the
proleptic-year, month-of-year and day-of-month fields.

JapaneseDate

date

​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Japanese calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

JapaneseDate

dateEpochDay

​(long epochDay)

Obtains a local date in the Japanese calendar system from the epoch-day.

JapaneseDate

dateYearDay

​(int prolepticYear,
int dayOfYear)

Obtains a local date in Japanese calendar system from the
proleptic-year and day-of-year fields.

JapaneseDate

dateYearDay

​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Japanese calendar system from the
era, year-of-era and day-of-year fields.

JapaneseEra

eraOf

​(int eraValue)

Returns the calendar system era object from the given numeric value.

String

getCalendarType

()

Gets the calendar type of the underlying calendar system - 'japanese'.

String

getId

()

Gets the ID of the chronology - 'Japanese'.

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

JapaneseChronology

INSTANCE

Singleton instance for Japanese chronology.

---

#### Field Summary

Singleton instance for Japanese chronology.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JapaneseDate

date

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Japanese calendar system from the
proleptic-year, month-of-year and day-of-month fields.

JapaneseDate

date

​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Japanese calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

JapaneseDate

dateEpochDay

​(long epochDay)

Obtains a local date in the Japanese calendar system from the epoch-day.

JapaneseDate

dateYearDay

​(int prolepticYear,
int dayOfYear)

Obtains a local date in Japanese calendar system from the
proleptic-year and day-of-year fields.

JapaneseDate

dateYearDay

​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Japanese calendar system from the
era, year-of-era and day-of-year fields.

JapaneseEra

eraOf

​(int eraValue)

Returns the calendar system era object from the given numeric value.

String

getCalendarType

()

Gets the calendar type of the underlying calendar system - 'japanese'.

String

getId

()

Gets the ID of the chronology - 'Japanese'.

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

Obtains a local date in Japanese calendar system from the
proleptic-year, month-of-year and day-of-month fields.

Obtains a local date in Japanese calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

Obtains a local date in the Japanese calendar system from the epoch-day.

Obtains a local date in Japanese calendar system from the
proleptic-year and day-of-year fields.

Obtains a local date in Japanese calendar system from the
era, year-of-era and day-of-year fields.

Returns the calendar system era object from the given numeric value.

Gets the calendar type of the underlying calendar system - 'japanese'.

Gets the ID of the chronology - 'Japanese'.

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
JapaneseChronology
INSTANCE
```

Singleton instance for Japanese chronology.

============ METHOD DETAIL ==========

- Method Detail

- getId

```java
public
String
getId()
```

Gets the ID of the chronology - 'Japanese'.

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
**Returns:** the chronology ID - 'Japanese'
**See Also:** getCalendarType()

- getCalendarType

```java
public
String
getCalendarType()
```

Gets the calendar type of the underlying calendar system - 'japanese'.

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
**Returns:** the calendar system type - 'japanese'
**See Also:** getId()

- date

```java
public
JapaneseDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Japanese calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

The Japanese month and day-of-month are the same as those in the
ISO calendar system. They are not reset when the era changes.
For example:

```java
6th Jan Showa 64 = ISO 1989-01-06
7th Jan Showa 64 = ISO 1989-01-07
8th Jan Heisei 1 = ISO 1989-01-08
9th Jan Heisei 1 = ISO 1989-01-09
```

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Japanese era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

JapaneseEra

- date

```java
public
JapaneseDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Japanese calendar system from the
proleptic-year, month-of-year and day-of-month fields.

The Japanese proleptic year, month and day-of-month are the same as those
in the ISO calendar system. They are not reset when the era changes.

**Specified by:** date

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateYearDay

```java
public
JapaneseDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Japanese calendar system from the
era, year-of-era and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the year-of-era.
This definition changes the normal meaning of day-of-year only in those years
where the year-of-era is reset to one due to a change in the era.
For example:

```java
6th Jan Showa 64 = day-of-year 6
7th Jan Showa 64 = day-of-year 7
8th Jan Heisei 1 = day-of-year 1
9th Jan Heisei 1 = day-of-year 2
```

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Japanese era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

JapaneseEra

- dateYearDay

```java
public
JapaneseDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Japanese calendar system from the
proleptic-year and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the proleptic year.
The Japanese proleptic year and day-of-year are the same as those in the ISO calendar system.
They are not reset when the era changes.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateEpochDay

```java
public
JapaneseDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Japanese calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date

- isLeapYear

```java
public boolean isLeapYear​(long prolepticYear)
```

Checks if the specified year is a leap year.

Japanese calendar leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

**Specified by:** isLeapYear

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year to check, not validated for range
**Returns:** true if the year is a leap year

- eraOf

```java
public
JapaneseEra
eraOf​(int eraValue)
```

Returns the calendar system era object from the given numeric value.

See the description of each Era for the numeric values of:

JapaneseEra.HEISEI

,

JapaneseEra.SHOWA

,

JapaneseEra.TAISHO

,

JapaneseEra.MEIJI

), only Meiji and later eras are supported.

**Specified by:** eraOf

in interface

Chronology
**Parameters:** eraValue

- the era value
**Returns:** the Japanese

Era

for the given numeric era value
**Throws:** DateTimeException

- if

eraValue

is invalid

Field Detail

- INSTANCE

```java
public static final
JapaneseChronology
INSTANCE
```

Singleton instance for Japanese chronology.

---

#### Field Detail

INSTANCE

```java
public static final
JapaneseChronology
INSTANCE
```

Singleton instance for Japanese chronology.

---

#### INSTANCE

public static final

JapaneseChronology

INSTANCE

Singleton instance for Japanese chronology.

Method Detail

- getId

```java
public
String
getId()
```

Gets the ID of the chronology - 'Japanese'.

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
**Returns:** the chronology ID - 'Japanese'
**See Also:** getCalendarType()

- getCalendarType

```java
public
String
getCalendarType()
```

Gets the calendar type of the underlying calendar system - 'japanese'.

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
**Returns:** the calendar system type - 'japanese'
**See Also:** getId()

- date

```java
public
JapaneseDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Japanese calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

The Japanese month and day-of-month are the same as those in the
ISO calendar system. They are not reset when the era changes.
For example:

```java
6th Jan Showa 64 = ISO 1989-01-06
7th Jan Showa 64 = ISO 1989-01-07
8th Jan Heisei 1 = ISO 1989-01-08
9th Jan Heisei 1 = ISO 1989-01-09
```

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Japanese era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

JapaneseEra

- date

```java
public
JapaneseDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Japanese calendar system from the
proleptic-year, month-of-year and day-of-month fields.

The Japanese proleptic year, month and day-of-month are the same as those
in the ISO calendar system. They are not reset when the era changes.

**Specified by:** date

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateYearDay

```java
public
JapaneseDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Japanese calendar system from the
era, year-of-era and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the year-of-era.
This definition changes the normal meaning of day-of-year only in those years
where the year-of-era is reset to one due to a change in the era.
For example:

```java
6th Jan Showa 64 = day-of-year 6
7th Jan Showa 64 = day-of-year 7
8th Jan Heisei 1 = day-of-year 1
9th Jan Heisei 1 = day-of-year 2
```

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Japanese era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

JapaneseEra

- dateYearDay

```java
public
JapaneseDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Japanese calendar system from the
proleptic-year and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the proleptic year.
The Japanese proleptic year and day-of-year are the same as those in the ISO calendar system.
They are not reset when the era changes.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateEpochDay

```java
public
JapaneseDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Japanese calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date

- isLeapYear

```java
public boolean isLeapYear​(long prolepticYear)
```

Checks if the specified year is a leap year.

Japanese calendar leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

**Specified by:** isLeapYear

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year to check, not validated for range
**Returns:** true if the year is a leap year

- eraOf

```java
public
JapaneseEra
eraOf​(int eraValue)
```

Returns the calendar system era object from the given numeric value.

See the description of each Era for the numeric values of:

JapaneseEra.HEISEI

,

JapaneseEra.SHOWA

,

JapaneseEra.TAISHO

,

JapaneseEra.MEIJI

), only Meiji and later eras are supported.

**Specified by:** eraOf

in interface

Chronology
**Parameters:** eraValue

- the era value
**Returns:** the Japanese

Era

for the given numeric era value
**Throws:** DateTimeException

- if

eraValue

is invalid

---

#### Method Detail

getId

```java
public
String
getId()
```

Gets the ID of the chronology - 'Japanese'.

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
**Returns:** the chronology ID - 'Japanese'
**See Also:** getCalendarType()

---

#### getId

public

String

getId()

Gets the ID of the chronology - 'Japanese'.

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

Gets the calendar type of the underlying calendar system - 'japanese'.

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
**Returns:** the calendar system type - 'japanese'
**See Also:** getId()

---

#### getCalendarType

public

String

getCalendarType()

Gets the calendar type of the underlying calendar system - 'japanese'.

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
JapaneseDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Japanese calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

The Japanese month and day-of-month are the same as those in the
ISO calendar system. They are not reset when the era changes.
For example:

```java
6th Jan Showa 64 = ISO 1989-01-06
7th Jan Showa 64 = ISO 1989-01-07
8th Jan Heisei 1 = ISO 1989-01-08
9th Jan Heisei 1 = ISO 1989-01-09
```

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Japanese era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

JapaneseEra

---

#### date

public

JapaneseDate

date​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Japanese calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

The Japanese month and day-of-month are the same as those in the
ISO calendar system. They are not reset when the era changes.
For example:

```java
6th Jan Showa 64 = ISO 1989-01-06
7th Jan Showa 64 = ISO 1989-01-07
8th Jan Heisei 1 = ISO 1989-01-08
9th Jan Heisei 1 = ISO 1989-01-09
```

The Japanese month and day-of-month are the same as those in the
ISO calendar system. They are not reset when the era changes.
For example:

```java
6th Jan Showa 64 = ISO 1989-01-06
7th Jan Showa 64 = ISO 1989-01-07
8th Jan Heisei 1 = ISO 1989-01-08
9th Jan Heisei 1 = ISO 1989-01-09
```

6th Jan Showa 64 = ISO 1989-01-06
7th Jan Showa 64 = ISO 1989-01-07
8th Jan Heisei 1 = ISO 1989-01-08
9th Jan Heisei 1 = ISO 1989-01-09

date

```java
public
JapaneseDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Japanese calendar system from the
proleptic-year, month-of-year and day-of-month fields.

The Japanese proleptic year, month and day-of-month are the same as those
in the ISO calendar system. They are not reset when the era changes.

**Specified by:** date

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### date

public

JapaneseDate

date​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Japanese calendar system from the
proleptic-year, month-of-year and day-of-month fields.

The Japanese proleptic year, month and day-of-month are the same as those
in the ISO calendar system. They are not reset when the era changes.

The Japanese proleptic year, month and day-of-month are the same as those
in the ISO calendar system. They are not reset when the era changes.

dateYearDay

```java
public
JapaneseDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Japanese calendar system from the
era, year-of-era and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the year-of-era.
This definition changes the normal meaning of day-of-year only in those years
where the year-of-era is reset to one due to a change in the era.
For example:

```java
6th Jan Showa 64 = day-of-year 6
7th Jan Showa 64 = day-of-year 7
8th Jan Heisei 1 = day-of-year 1
9th Jan Heisei 1 = day-of-year 2
```

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Japanese era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

JapaneseEra

---

#### dateYearDay

public

JapaneseDate

dateYearDay​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Japanese calendar system from the
era, year-of-era and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the year-of-era.
This definition changes the normal meaning of day-of-year only in those years
where the year-of-era is reset to one due to a change in the era.
For example:

```java
6th Jan Showa 64 = day-of-year 6
7th Jan Showa 64 = day-of-year 7
8th Jan Heisei 1 = day-of-year 1
9th Jan Heisei 1 = day-of-year 2
```

The day-of-year in this factory is expressed relative to the start of the year-of-era.
This definition changes the normal meaning of day-of-year only in those years
where the year-of-era is reset to one due to a change in the era.
For example:

```java
6th Jan Showa 64 = day-of-year 6
7th Jan Showa 64 = day-of-year 7
8th Jan Heisei 1 = day-of-year 1
9th Jan Heisei 1 = day-of-year 2
```

6th Jan Showa 64 = day-of-year 6
7th Jan Showa 64 = day-of-year 7
8th Jan Heisei 1 = day-of-year 1
9th Jan Heisei 1 = day-of-year 2

dateYearDay

```java
public
JapaneseDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Japanese calendar system from the
proleptic-year and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the proleptic year.
The Japanese proleptic year and day-of-year are the same as those in the ISO calendar system.
They are not reset when the era changes.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### dateYearDay

public

JapaneseDate

dateYearDay​(int prolepticYear,
int dayOfYear)

Obtains a local date in Japanese calendar system from the
proleptic-year and day-of-year fields.

The day-of-year in this factory is expressed relative to the start of the proleptic year.
The Japanese proleptic year and day-of-year are the same as those in the ISO calendar system.
They are not reset when the era changes.

The day-of-year in this factory is expressed relative to the start of the proleptic year.
The Japanese proleptic year and day-of-year are the same as those in the ISO calendar system.
They are not reset when the era changes.

dateEpochDay

```java
public
JapaneseDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Japanese calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Japanese local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### dateEpochDay

public

JapaneseDate

dateEpochDay​(long epochDay)

Obtains a local date in the Japanese calendar system from the epoch-day.

isLeapYear

```java
public boolean isLeapYear​(long prolepticYear)
```

Checks if the specified year is a leap year.

Japanese calendar leap years occur exactly in line with ISO leap years.
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

Japanese calendar leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

Japanese calendar leap years occur exactly in line with ISO leap years.
This method does not validate the year passed in, and only has a
well-defined result for years in the supported range.

eraOf

```java
public
JapaneseEra
eraOf​(int eraValue)
```

Returns the calendar system era object from the given numeric value.

See the description of each Era for the numeric values of:

JapaneseEra.HEISEI

,

JapaneseEra.SHOWA

,

JapaneseEra.TAISHO

,

JapaneseEra.MEIJI

), only Meiji and later eras are supported.

**Specified by:** eraOf

in interface

Chronology
**Parameters:** eraValue

- the era value
**Returns:** the Japanese

Era

for the given numeric era value
**Throws:** DateTimeException

- if

eraValue

is invalid

---

#### eraOf

public

JapaneseEra

eraOf​(int eraValue)

Returns the calendar system era object from the given numeric value.

See the description of each Era for the numeric values of:

JapaneseEra.HEISEI

,

JapaneseEra.SHOWA

,

JapaneseEra.TAISHO

,

JapaneseEra.MEIJI

), only Meiji and later eras are supported.

---

