# Class HijrahChronology

**Source:** `java.base\java\time\chrono\HijrahChronology.html`

### Class Description

```java
public final class
HijrahChronology

extends
AbstractChronology

implements
Serializable
```

The Hijrah calendar is a lunar calendar supporting Islamic calendars.

The HijrahChronology follows the rules of the Hijrah calendar system. The Hijrah
calendar has several variants based on differences in when the new moon is
determined to have occurred and where the observation is made.
In some variants the length of each month is
computed algorithmically from the astronomical data for the moon and earth and
in others the length of the month is determined by an authorized sighting
of the new moon. For the algorithmically based calendars the calendar
can project into the future.
For sighting based calendars only historical data from past
sightings is available.

The length of each month is 29 or 30 days.
Ordinary years have 354 days; leap years have 355 days.

CLDR and LDML identify variants:

Variants of Hijrah Calendars

Chronology ID

Calendar Type

Locale extension, see

Locale

Description

Hijrah-umalqura

islamic-umalqura

ca-islamic-umalqura

Islamic - Umm Al-Qura calendar of Saudi Arabia

Additional variants may be available through

Chronology.getAvailableChronologies()

.

Example

Selecting the chronology from the locale uses

Chronology.ofLocale(java.util.Locale)

to find the Chronology based on Locale supported BCP 47 extension mechanism
to request a specific calendar ("ca"). For example,

```java
Locale locale = Locale.forLanguageTag("en-US-u-ca-islamic-umalqura");
Chronology chrono = Chronology.ofLocale(locale);
```

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
HijrahChronology
INSTANCE

Singleton instance of the Islamic Umm Al-Qura calendar of Saudi Arabia.
Other Hijrah chronology variants may be available from

Chronology.getAvailableChronologies()

.

---

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getId()

Gets the ID of the chronology.

The ID uniquely identifies the

Chronology

. It can be used to
lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:**
- getId

in interface

Chronology

**Returns:**
- the chronology ID, non-null

**See Also:**
- getCalendarType()

---

#### public
String
getCalendarType()

Gets the calendar type of the Islamic calendar.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:**
- getCalendarType

in interface

Chronology

**Returns:**
- the calendar system type; non-null if the calendar has
a standard type, otherwise null

**See Also:**
- getId()

---

#### public
HijrahDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Hijrah calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:**
- date

in interface

Chronology

**Parameters:**
- era

- the Hijrah era, not null
- yearOfEra

- the year-of-era
- month

- the month-of-year
- dayOfMonth

- the day-of-month

**Returns:**
- the Hijrah local date, not null

**Throws:**
- DateTimeException

- if unable to create the date
- ClassCastException

- if the

era

is not a

HijrahEra

---

#### public
HijrahDate
date​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Hijrah calendar system from the
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
- the Hijrah local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public
HijrahDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Hijrah calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:**
- dateYearDay

in interface

Chronology

**Parameters:**
- era

- the Hijrah era, not null
- yearOfEra

- the year-of-era
- dayOfYear

- the day-of-year

**Returns:**
- the Hijrah local date, not null

**Throws:**
- DateTimeException

- if unable to create the date
- ClassCastException

- if the

era

is not a

HijrahEra

---

#### public
HijrahDate
dateYearDay​(int prolepticYear,
int dayOfYear)

Obtains a local date in Hijrah calendar system from the
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
- the Hijrah local date, not null

**Throws:**
- DateTimeException

- if the value of the year is out of range,
or if the day-of-year is invalid for the year

---

#### public
HijrahDate
dateEpochDay​(long epochDay)

Obtains a local date in the Hijrah calendar system from the epoch-day.

**Specified by:**
- dateEpochDay

in interface

Chronology

**Parameters:**
- epochDay

- the epoch day

**Returns:**
- the Hijrah local date, not null

**Throws:**
- DateTimeException

- if unable to create the date

---

#### public
HijrahEra
eraOf​(int eraValue)

Creates the HijrahEra object from the numeric value.
The Hijrah calendar system has only one era covering the
proleptic years greater than zero.
This method returns the singleton HijrahEra for the value 1.

**Specified by:**
- eraOf

in interface

Chronology

**Parameters:**
- eraValue

- the era value

**Returns:**
- the calendar system era, not null

**Throws:**
- DateTimeException

- if unable to create the era

---

### Additional Sections

#### Class HijrahChronology

java.lang.Object

- java.time.chrono.AbstractChronology
- - java.time.chrono.HijrahChronology

java.time.chrono.AbstractChronology

- java.time.chrono.HijrahChronology

java.time.chrono.HijrahChronology

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
HijrahChronology

extends
AbstractChronology

implements
Serializable
```

The Hijrah calendar is a lunar calendar supporting Islamic calendars.

The HijrahChronology follows the rules of the Hijrah calendar system. The Hijrah
calendar has several variants based on differences in when the new moon is
determined to have occurred and where the observation is made.
In some variants the length of each month is
computed algorithmically from the astronomical data for the moon and earth and
in others the length of the month is determined by an authorized sighting
of the new moon. For the algorithmically based calendars the calendar
can project into the future.
For sighting based calendars only historical data from past
sightings is available.

The length of each month is 29 or 30 days.
Ordinary years have 354 days; leap years have 355 days.

CLDR and LDML identify variants:

Variants of Hijrah Calendars

Chronology ID

Calendar Type

Locale extension, see

Locale

Description

Hijrah-umalqura

islamic-umalqura

ca-islamic-umalqura

Islamic - Umm Al-Qura calendar of Saudi Arabia

Additional variants may be available through

Chronology.getAvailableChronologies()

.

Example

Selecting the chronology from the locale uses

Chronology.ofLocale(java.util.Locale)

to find the Chronology based on Locale supported BCP 47 extension mechanism
to request a specific calendar ("ca"). For example,

```java
Locale locale = Locale.forLanguageTag("en-US-u-ca-islamic-umalqura");
Chronology chrono = Chronology.ofLocale(locale);
```

**Implementation Requirements:** This class is immutable and thread-safe.
**Implementation Note:** Each Hijrah variant is configured individually. Each variant is defined by a
property resource that defines the

ID

, the

calendar type

,
the start of the calendar, the alignment with the
ISO calendar, and the length of each month for a range of years.
The variants are loaded by HijrahChronology as a resource from
hijrah-config-<calendar type>.properties.

The Hijrah property resource is a set of properties that describe the calendar.
The syntax is defined by

java.util.Properties#load(Reader)

.

Configuration of Hijrah Calendar

Property Name

Property value

Description

id

Chronology Id, for example, "Hijrah-umalqura"

The Id of the calendar in common usage

type

Calendar type, for example, "islamic-umalqura"

LDML defines the calendar types

version

Version, for example: "1.8.0_1"

The version of the Hijrah variant data

iso-start

ISO start date, formatted as

yyyy-MM-dd

, for example: "1900-04-30"

The ISO date of the first day of the minimum Hijrah year.

yyyy - a numeric 4 digit year, for example "1434"

The value is a sequence of 12 month lengths,
for example: "29 30 29 30 29 30 30 30 29 30 29 29"

The lengths of the 12 months of the year separated by whitespace.
A numeric year property must be present for every year without any gaps.
The month lengths must be between 29-32 inclusive.
**Since:** 1.8
**See Also:** Serialized Form

public final class

HijrahChronology

extends

AbstractChronology

implements

Serializable

The Hijrah calendar is a lunar calendar supporting Islamic calendars.

The HijrahChronology follows the rules of the Hijrah calendar system. The Hijrah
calendar has several variants based on differences in when the new moon is
determined to have occurred and where the observation is made.
In some variants the length of each month is
computed algorithmically from the astronomical data for the moon and earth and
in others the length of the month is determined by an authorized sighting
of the new moon. For the algorithmically based calendars the calendar
can project into the future.
For sighting based calendars only historical data from past
sightings is available.

The length of each month is 29 or 30 days.
Ordinary years have 354 days; leap years have 355 days.

CLDR and LDML identify variants:

Variants of Hijrah Calendars

Chronology ID

Calendar Type

Locale extension, see

Locale

Description

Hijrah-umalqura

islamic-umalqura

ca-islamic-umalqura

Islamic - Umm Al-Qura calendar of Saudi Arabia

Additional variants may be available through

Chronology.getAvailableChronologies()

.

Example

Selecting the chronology from the locale uses

Chronology.ofLocale(java.util.Locale)

to find the Chronology based on Locale supported BCP 47 extension mechanism
to request a specific calendar ("ca"). For example,

```java
Locale locale = Locale.forLanguageTag("en-US-u-ca-islamic-umalqura");
Chronology chrono = Chronology.ofLocale(locale);
```

The HijrahChronology follows the rules of the Hijrah calendar system. The Hijrah
calendar has several variants based on differences in when the new moon is
determined to have occurred and where the observation is made.
In some variants the length of each month is
computed algorithmically from the astronomical data for the moon and earth and
in others the length of the month is determined by an authorized sighting
of the new moon. For the algorithmically based calendars the calendar
can project into the future.
For sighting based calendars only historical data from past
sightings is available.

The length of each month is 29 or 30 days.
Ordinary years have 354 days; leap years have 355 days.

CLDR and LDML identify variants:

Variants of Hijrah Calendars

Chronology ID

Calendar Type

Locale extension, see

Locale

Description

Hijrah-umalqura

islamic-umalqura

ca-islamic-umalqura

Islamic - Umm Al-Qura calendar of Saudi Arabia

Additional variants may be available through

Chronology.getAvailableChronologies()

.

Example

Selecting the chronology from the locale uses

Chronology.ofLocale(java.util.Locale)

to find the Chronology based on Locale supported BCP 47 extension mechanism
to request a specific calendar ("ca"). For example,

```java
Locale locale = Locale.forLanguageTag("en-US-u-ca-islamic-umalqura");
Chronology chrono = Chronology.ofLocale(locale);
```

The length of each month is 29 or 30 days.
Ordinary years have 354 days; leap years have 355 days.

CLDR and LDML identify variants:

Variants of Hijrah Calendars

Chronology ID

Calendar Type

Locale extension, see

Locale

Description

Hijrah-umalqura

islamic-umalqura

ca-islamic-umalqura

Islamic - Umm Al-Qura calendar of Saudi Arabia

Additional variants may be available through

Chronology.getAvailableChronologies()

.

Example

Selecting the chronology from the locale uses

Chronology.ofLocale(java.util.Locale)

to find the Chronology based on Locale supported BCP 47 extension mechanism
to request a specific calendar ("ca"). For example,

```java
Locale locale = Locale.forLanguageTag("en-US-u-ca-islamic-umalqura");
Chronology chrono = Chronology.ofLocale(locale);
```

CLDR and LDML identify variants:

Variants of Hijrah Calendars

Chronology ID

Calendar Type

Locale extension, see

Locale

Description

Hijrah-umalqura

islamic-umalqura

ca-islamic-umalqura

Islamic - Umm Al-Qura calendar of Saudi Arabia

Additional variants may be available through

Chronology.getAvailableChronologies()

.

Example

Selecting the chronology from the locale uses

Chronology.ofLocale(java.util.Locale)

to find the Chronology based on Locale supported BCP 47 extension mechanism
to request a specific calendar ("ca"). For example,

```java
Locale locale = Locale.forLanguageTag("en-US-u-ca-islamic-umalqura");
Chronology chrono = Chronology.ofLocale(locale);
```

Additional variants may be available through

Chronology.getAvailableChronologies()

.

Example

Selecting the chronology from the locale uses

Chronology.ofLocale(java.util.Locale)

to find the Chronology based on Locale supported BCP 47 extension mechanism
to request a specific calendar ("ca"). For example,

```java
Locale locale = Locale.forLanguageTag("en-US-u-ca-islamic-umalqura");
Chronology chrono = Chronology.ofLocale(locale);
```

Example

Selecting the chronology from the locale uses

Chronology.ofLocale(java.util.Locale)

to find the Chronology based on Locale supported BCP 47 extension mechanism
to request a specific calendar ("ca"). For example,

Locale locale = Locale.forLanguageTag("en-US-u-ca-islamic-umalqura");
Chronology chrono = Chronology.ofLocale(locale);

The Hijrah property resource is a set of properties that describe the calendar.
The syntax is defined by

java.util.Properties#load(Reader)

.

Configuration of Hijrah Calendar

Property Name

Property value

Description

id

Chronology Id, for example, "Hijrah-umalqura"

The Id of the calendar in common usage

type

Calendar type, for example, "islamic-umalqura"

LDML defines the calendar types

version

Version, for example: "1.8.0_1"

The version of the Hijrah variant data

iso-start

ISO start date, formatted as

yyyy-MM-dd

, for example: "1900-04-30"

The ISO date of the first day of the minimum Hijrah year.

yyyy - a numeric 4 digit year, for example "1434"

The value is a sequence of 12 month lengths,
for example: "29 30 29 30 29 30 30 30 29 30 29 29"

The lengths of the 12 months of the year separated by whitespace.
A numeric year property must be present for every year without any gaps.
The month lengths must be between 29-32 inclusive.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

HijrahChronology

INSTANCE

Singleton instance of the Islamic Umm Al-Qura calendar of Saudi Arabia.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

HijrahDate

date

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Hijrah calendar system from the
proleptic-year, month-of-year and day-of-month fields.

HijrahDate

date

​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Hijrah calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

HijrahDate

dateEpochDay

​(long epochDay)

Obtains a local date in the Hijrah calendar system from the epoch-day.

HijrahDate

dateYearDay

​(int prolepticYear,
int dayOfYear)

Obtains a local date in Hijrah calendar system from the
proleptic-year and day-of-year fields.

HijrahDate

dateYearDay

​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Hijrah calendar system from the
era, year-of-era and day-of-year fields.

HijrahEra

eraOf

​(int eraValue)

Creates the HijrahEra object from the numeric value.

String

getCalendarType

()

Gets the calendar type of the Islamic calendar.

String

getId

()

Gets the ID of the chronology.

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

isLeapYear

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

HijrahChronology

INSTANCE

Singleton instance of the Islamic Umm Al-Qura calendar of Saudi Arabia.

---

#### Field Summary

Singleton instance of the Islamic Umm Al-Qura calendar of Saudi Arabia.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

HijrahDate

date

​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Hijrah calendar system from the
proleptic-year, month-of-year and day-of-month fields.

HijrahDate

date

​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Hijrah calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

HijrahDate

dateEpochDay

​(long epochDay)

Obtains a local date in the Hijrah calendar system from the epoch-day.

HijrahDate

dateYearDay

​(int prolepticYear,
int dayOfYear)

Obtains a local date in Hijrah calendar system from the
proleptic-year and day-of-year fields.

HijrahDate

dateYearDay

​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Hijrah calendar system from the
era, year-of-era and day-of-year fields.

HijrahEra

eraOf

​(int eraValue)

Creates the HijrahEra object from the numeric value.

String

getCalendarType

()

Gets the calendar type of the Islamic calendar.

String

getId

()

Gets the ID of the chronology.

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

isLeapYear

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

Obtains a local date in Hijrah calendar system from the
proleptic-year, month-of-year and day-of-month fields.

Obtains a local date in Hijrah calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

Obtains a local date in the Hijrah calendar system from the epoch-day.

Obtains a local date in Hijrah calendar system from the
proleptic-year and day-of-year fields.

Obtains a local date in Hijrah calendar system from the
era, year-of-era and day-of-year fields.

Creates the HijrahEra object from the numeric value.

Gets the calendar type of the Islamic calendar.

Gets the ID of the chronology.

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

isLeapYear

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
HijrahChronology
INSTANCE
```

Singleton instance of the Islamic Umm Al-Qura calendar of Saudi Arabia.
Other Hijrah chronology variants may be available from

Chronology.getAvailableChronologies()

.

============ METHOD DETAIL ==========

- Method Detail

- getId

```java
public
String
getId()
```

Gets the ID of the chronology.

The ID uniquely identifies the

Chronology

. It can be used to
lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:** getId

in interface

Chronology
**Returns:** the chronology ID, non-null
**See Also:** getCalendarType()

- getCalendarType

```java
public
String
getCalendarType()
```

Gets the calendar type of the Islamic calendar.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:** getCalendarType

in interface

Chronology
**Returns:** the calendar system type; non-null if the calendar has
a standard type, otherwise null
**See Also:** getId()

- date

```java
public
HijrahDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Hijrah calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Hijrah era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

HijrahEra

- date

```java
public
HijrahDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Hijrah calendar system from the
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
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateYearDay

```java
public
HijrahDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Hijrah calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Hijrah era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

HijrahEra

- dateYearDay

```java
public
HijrahDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Hijrah calendar system from the
proleptic-year and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if the value of the year is out of range,
or if the day-of-year is invalid for the year

- dateEpochDay

```java
public
HijrahDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Hijrah calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date

- eraOf

```java
public
HijrahEra
eraOf​(int eraValue)
```

Creates the HijrahEra object from the numeric value.
The Hijrah calendar system has only one era covering the
proleptic years greater than zero.
This method returns the singleton HijrahEra for the value 1.

**Specified by:** eraOf

in interface

Chronology
**Parameters:** eraValue

- the era value
**Returns:** the calendar system era, not null
**Throws:** DateTimeException

- if unable to create the era

Field Detail

- INSTANCE

```java
public static final
HijrahChronology
INSTANCE
```

Singleton instance of the Islamic Umm Al-Qura calendar of Saudi Arabia.
Other Hijrah chronology variants may be available from

Chronology.getAvailableChronologies()

.

---

#### Field Detail

INSTANCE

```java
public static final
HijrahChronology
INSTANCE
```

Singleton instance of the Islamic Umm Al-Qura calendar of Saudi Arabia.
Other Hijrah chronology variants may be available from

Chronology.getAvailableChronologies()

.

---

#### INSTANCE

public static final

HijrahChronology

INSTANCE

Singleton instance of the Islamic Umm Al-Qura calendar of Saudi Arabia.
Other Hijrah chronology variants may be available from

Chronology.getAvailableChronologies()

.

Method Detail

- getId

```java
public
String
getId()
```

Gets the ID of the chronology.

The ID uniquely identifies the

Chronology

. It can be used to
lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:** getId

in interface

Chronology
**Returns:** the chronology ID, non-null
**See Also:** getCalendarType()

- getCalendarType

```java
public
String
getCalendarType()
```

Gets the calendar type of the Islamic calendar.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:** getCalendarType

in interface

Chronology
**Returns:** the calendar system type; non-null if the calendar has
a standard type, otherwise null
**See Also:** getId()

- date

```java
public
HijrahDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Hijrah calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Hijrah era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

HijrahEra

- date

```java
public
HijrahDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Hijrah calendar system from the
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
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date

- dateYearDay

```java
public
HijrahDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Hijrah calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Hijrah era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

HijrahEra

- dateYearDay

```java
public
HijrahDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Hijrah calendar system from the
proleptic-year and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if the value of the year is out of range,
or if the day-of-year is invalid for the year

- dateEpochDay

```java
public
HijrahDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Hijrah calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date

- eraOf

```java
public
HijrahEra
eraOf​(int eraValue)
```

Creates the HijrahEra object from the numeric value.
The Hijrah calendar system has only one era covering the
proleptic years greater than zero.
This method returns the singleton HijrahEra for the value 1.

**Specified by:** eraOf

in interface

Chronology
**Parameters:** eraValue

- the era value
**Returns:** the calendar system era, not null
**Throws:** DateTimeException

- if unable to create the era

---

#### Method Detail

getId

```java
public
String
getId()
```

Gets the ID of the chronology.

The ID uniquely identifies the

Chronology

. It can be used to
lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:** getId

in interface

Chronology
**Returns:** the chronology ID, non-null
**See Also:** getCalendarType()

---

#### getId

public

String

getId()

Gets the ID of the chronology.

The ID uniquely identifies the

Chronology

. It can be used to
lookup the

Chronology

using

Chronology.of(String)

.

The ID uniquely identifies the

Chronology

. It can be used to
lookup the

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

Gets the calendar type of the Islamic calendar.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

**Specified by:** getCalendarType

in interface

Chronology
**Returns:** the calendar system type; non-null if the calendar has
a standard type, otherwise null
**See Also:** getId()

---

#### getCalendarType

public

String

getCalendarType()

Gets the calendar type of the Islamic calendar.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

The calendar type is an identifier defined by the

Unicode Locale Data Markup Language (LDML)

specification.
It can be used to lookup the

Chronology

using

Chronology.of(String)

.

date

```java
public
HijrahDate
date​(
Era
era,
int yearOfEra,
int month,
int dayOfMonth)
```

Obtains a local date in Hijrah calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

**Specified by:** date

in interface

Chronology
**Parameters:** era

- the Hijrah era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** month

- the month-of-year
**Parameters:** dayOfMonth

- the day-of-month
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

HijrahEra

---

#### date

public

HijrahDate

date​(

Era

era,
int yearOfEra,
int month,
int dayOfMonth)

Obtains a local date in Hijrah calendar system from the
era, year-of-era, month-of-year and day-of-month fields.

date

```java
public
HijrahDate
date​(int prolepticYear,
int month,
int dayOfMonth)
```

Obtains a local date in Hijrah calendar system from the
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
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### date

public

HijrahDate

date​(int prolepticYear,
int month,
int dayOfMonth)

Obtains a local date in Hijrah calendar system from the
proleptic-year, month-of-year and day-of-month fields.

dateYearDay

```java
public
HijrahDate
dateYearDay​(
Era
era,
int yearOfEra,
int dayOfYear)
```

Obtains a local date in Hijrah calendar system from the
era, year-of-era and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** era

- the Hijrah era, not null
**Parameters:** yearOfEra

- the year-of-era
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date
**Throws:** ClassCastException

- if the

era

is not a

HijrahEra

---

#### dateYearDay

public

HijrahDate

dateYearDay​(

Era

era,
int yearOfEra,
int dayOfYear)

Obtains a local date in Hijrah calendar system from the
era, year-of-era and day-of-year fields.

dateYearDay

```java
public
HijrahDate
dateYearDay​(int prolepticYear,
int dayOfYear)
```

Obtains a local date in Hijrah calendar system from the
proleptic-year and day-of-year fields.

**Specified by:** dateYearDay

in interface

Chronology
**Parameters:** prolepticYear

- the proleptic-year
**Parameters:** dayOfYear

- the day-of-year
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if the value of the year is out of range,
or if the day-of-year is invalid for the year

---

#### dateYearDay

public

HijrahDate

dateYearDay​(int prolepticYear,
int dayOfYear)

Obtains a local date in Hijrah calendar system from the
proleptic-year and day-of-year fields.

dateEpochDay

```java
public
HijrahDate
dateEpochDay​(long epochDay)
```

Obtains a local date in the Hijrah calendar system from the epoch-day.

**Specified by:** dateEpochDay

in interface

Chronology
**Parameters:** epochDay

- the epoch day
**Returns:** the Hijrah local date, not null
**Throws:** DateTimeException

- if unable to create the date

---

#### dateEpochDay

public

HijrahDate

dateEpochDay​(long epochDay)

Obtains a local date in the Hijrah calendar system from the epoch-day.

eraOf

```java
public
HijrahEra
eraOf​(int eraValue)
```

Creates the HijrahEra object from the numeric value.
The Hijrah calendar system has only one era covering the
proleptic years greater than zero.
This method returns the singleton HijrahEra for the value 1.

**Specified by:** eraOf

in interface

Chronology
**Parameters:** eraValue

- the era value
**Returns:** the calendar system era, not null
**Throws:** DateTimeException

- if unable to create the era

---

#### eraOf

public

HijrahEra

eraOf​(int eraValue)

Creates the HijrahEra object from the numeric value.
The Hijrah calendar system has only one era covering the
proleptic years greater than zero.
This method returns the singleton HijrahEra for the value 1.

---

