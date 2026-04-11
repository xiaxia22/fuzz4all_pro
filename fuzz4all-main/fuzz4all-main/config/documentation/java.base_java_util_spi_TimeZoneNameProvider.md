# Class TimeZoneNameProvider

**Source:** `java.base\java\util\spi\TimeZoneNameProvider.html`

### Class Description

```java
public abstract class
TimeZoneNameProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide localized time zone names for the

TimeZone

class.
The localized time zone names available from the implementations of
this class are also the source for the

DateFormatSymbols.getZoneStrings()

method.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected TimeZoneNameProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract
String
getDisplayName​(
String
ID,
boolean daylight,
int style,

Locale
locale)

Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale. The given time
zone ID is "GMT" or one of the names defined using "Zone" entries
in the "tz database", a public domain time zone database at

ftp://elsie.nci.nih.gov/pub/

.
The data of this database is contained in a file whose name starts with
"tzdata", and the specification of the data format is part of the zic.8
man page, which is contained in a file whose name starts with "tzcode".

If

daylight

is true, the method should return a name
appropriate for daylight saving time even if the specified time zone
has not observed daylight saving time in the past.

**Parameters:**
- ID

- a time zone ID string
- daylight

- if true, return the daylight saving name.
- style

- either

TimeZone.LONG

or

TimeZone.SHORT
- locale

- the desired locale

**Returns:**
- the human-readable name of the given time zone in the
given locale, or null if it's not available.

**Throws:**
- IllegalArgumentException

- if

style

is invalid,
or

locale

isn't one of the locales returned from

getAvailableLocales()

.
- NullPointerException

- if

ID

or

locale

is null

**See Also:**
- TimeZone.getDisplayName(boolean, int, java.util.Locale)

---

#### public
String
getGenericDisplayName​(
String
ID,
int style,

Locale
locale)

Returns a generic name for the given time zone

ID

that's suitable
for presentation to the user in the specified

locale

. Generic
time zone names are neutral from standard time and daylight saving
time. For example, "PT" is the short generic name of time zone ID

America/Los_Angeles

, while its short standard time and daylight saving
time names are "PST" and "PDT", respectively. Refer to

getDisplayName

for valid time zone IDs.

The default implementation of this method returns

null

.

**Parameters:**
- ID

- a time zone ID string
- style

- either

TimeZone.LONG

or

TimeZone.SHORT
- locale

- the desired locale

**Returns:**
- the human-readable generic name of the given time zone in the
given locale, or

null

if it's not available.

**Throws:**
- IllegalArgumentException

- if

style

is invalid,
or

locale

isn't one of the locales returned from

getAvailableLocales()

.
- NullPointerException

- if

ID

or

locale

is

null

**Since:**
- 1.8

---

### Additional Sections

#### Class TimeZoneNameProvider

java.lang.Object

- java.util.spi.LocaleServiceProvider
- - java.util.spi.TimeZoneNameProvider

java.util.spi.LocaleServiceProvider

- java.util.spi.TimeZoneNameProvider

java.util.spi.TimeZoneNameProvider

```java
public abstract class
TimeZoneNameProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide localized time zone names for the

TimeZone

class.
The localized time zone names available from the implementations of
this class are also the source for the

DateFormatSymbols.getZoneStrings()

method.

**Since:** 1.6

public abstract class

TimeZoneNameProvider

extends

LocaleServiceProvider

An abstract class for service providers that
provide localized time zone names for the

TimeZone

class.
The localized time zone names available from the implementations of
this class are also the source for the

DateFormatSymbols.getZoneStrings()

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TimeZoneNameProvider

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

getDisplayName

​(

String

ID,
boolean daylight,
int style,

Locale

locale)

Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale.

String

getGenericDisplayName

​(

String

ID,
int style,

Locale

locale)

Returns a generic name for the given time zone

ID

that's suitable
for presentation to the user in the specified

locale

.

- Methods declared in class java.util.spi.

LocaleServiceProvider

getAvailableLocales

,

isSupportedLocale

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TimeZoneNameProvider

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

getDisplayName

​(

String

ID,
boolean daylight,
int style,

Locale

locale)

Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale.

String

getGenericDisplayName

​(

String

ID,
int style,

Locale

locale)

Returns a generic name for the given time zone

ID

that's suitable
for presentation to the user in the specified

locale

.

- Methods declared in class java.util.spi.

LocaleServiceProvider

getAvailableLocales

,

isSupportedLocale

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale.

Returns a generic name for the given time zone

ID

that's suitable
for presentation to the user in the specified

locale

.

Methods declared in class java.util.spi.

LocaleServiceProvider

getAvailableLocales

,

isSupportedLocale

---

#### Methods declared in class java.util.spi. LocaleServiceProvider

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TimeZoneNameProvider

```java
protected TimeZoneNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- getDisplayName

```java
public abstract
String
getDisplayName​(
String
ID,
boolean daylight,
int style,

Locale
locale)
```

Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale. The given time
zone ID is "GMT" or one of the names defined using "Zone" entries
in the "tz database", a public domain time zone database at

ftp://elsie.nci.nih.gov/pub/

.
The data of this database is contained in a file whose name starts with
"tzdata", and the specification of the data format is part of the zic.8
man page, which is contained in a file whose name starts with "tzcode".

If

daylight

is true, the method should return a name
appropriate for daylight saving time even if the specified time zone
has not observed daylight saving time in the past.

**Parameters:** ID

- a time zone ID string
**Parameters:** daylight

- if true, return the daylight saving name.
**Parameters:** style

- either

TimeZone.LONG

or

TimeZone.SHORT
**Parameters:** locale

- the desired locale
**Returns:** the human-readable name of the given time zone in the
given locale, or null if it's not available.
**Throws:** IllegalArgumentException

- if

style

is invalid,
or

locale

isn't one of the locales returned from

getAvailableLocales()

.
**Throws:** NullPointerException

- if

ID

or

locale

is null
**See Also:** TimeZone.getDisplayName(boolean, int, java.util.Locale)

- getGenericDisplayName

```java
public
String
getGenericDisplayName​(
String
ID,
int style,

Locale
locale)
```

Returns a generic name for the given time zone

ID

that's suitable
for presentation to the user in the specified

locale

. Generic
time zone names are neutral from standard time and daylight saving
time. For example, "PT" is the short generic name of time zone ID

America/Los_Angeles

, while its short standard time and daylight saving
time names are "PST" and "PDT", respectively. Refer to

getDisplayName

for valid time zone IDs.

The default implementation of this method returns

null

.

**Parameters:** ID

- a time zone ID string
**Parameters:** style

- either

TimeZone.LONG

or

TimeZone.SHORT
**Parameters:** locale

- the desired locale
**Returns:** the human-readable generic name of the given time zone in the
given locale, or

null

if it's not available.
**Throws:** IllegalArgumentException

- if

style

is invalid,
or

locale

isn't one of the locales returned from

getAvailableLocales()

.
**Throws:** NullPointerException

- if

ID

or

locale

is

null
**Since:** 1.8

Constructor Detail

- TimeZoneNameProvider

```java
protected TimeZoneNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

TimeZoneNameProvider

```java
protected TimeZoneNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### TimeZoneNameProvider

protected TimeZoneNameProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getDisplayName

```java
public abstract
String
getDisplayName​(
String
ID,
boolean daylight,
int style,

Locale
locale)
```

Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale. The given time
zone ID is "GMT" or one of the names defined using "Zone" entries
in the "tz database", a public domain time zone database at

ftp://elsie.nci.nih.gov/pub/

.
The data of this database is contained in a file whose name starts with
"tzdata", and the specification of the data format is part of the zic.8
man page, which is contained in a file whose name starts with "tzcode".

If

daylight

is true, the method should return a name
appropriate for daylight saving time even if the specified time zone
has not observed daylight saving time in the past.

**Parameters:** ID

- a time zone ID string
**Parameters:** daylight

- if true, return the daylight saving name.
**Parameters:** style

- either

TimeZone.LONG

or

TimeZone.SHORT
**Parameters:** locale

- the desired locale
**Returns:** the human-readable name of the given time zone in the
given locale, or null if it's not available.
**Throws:** IllegalArgumentException

- if

style

is invalid,
or

locale

isn't one of the locales returned from

getAvailableLocales()

.
**Throws:** NullPointerException

- if

ID

or

locale

is null
**See Also:** TimeZone.getDisplayName(boolean, int, java.util.Locale)

- getGenericDisplayName

```java
public
String
getGenericDisplayName​(
String
ID,
int style,

Locale
locale)
```

Returns a generic name for the given time zone

ID

that's suitable
for presentation to the user in the specified

locale

. Generic
time zone names are neutral from standard time and daylight saving
time. For example, "PT" is the short generic name of time zone ID

America/Los_Angeles

, while its short standard time and daylight saving
time names are "PST" and "PDT", respectively. Refer to

getDisplayName

for valid time zone IDs.

The default implementation of this method returns

null

.

**Parameters:** ID

- a time zone ID string
**Parameters:** style

- either

TimeZone.LONG

or

TimeZone.SHORT
**Parameters:** locale

- the desired locale
**Returns:** the human-readable generic name of the given time zone in the
given locale, or

null

if it's not available.
**Throws:** IllegalArgumentException

- if

style

is invalid,
or

locale

isn't one of the locales returned from

getAvailableLocales()

.
**Throws:** NullPointerException

- if

ID

or

locale

is

null
**Since:** 1.8

---

#### Method Detail

getDisplayName

```java
public abstract
String
getDisplayName​(
String
ID,
boolean daylight,
int style,

Locale
locale)
```

Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale. The given time
zone ID is "GMT" or one of the names defined using "Zone" entries
in the "tz database", a public domain time zone database at

ftp://elsie.nci.nih.gov/pub/

.
The data of this database is contained in a file whose name starts with
"tzdata", and the specification of the data format is part of the zic.8
man page, which is contained in a file whose name starts with "tzcode".

If

daylight

is true, the method should return a name
appropriate for daylight saving time even if the specified time zone
has not observed daylight saving time in the past.

**Parameters:** ID

- a time zone ID string
**Parameters:** daylight

- if true, return the daylight saving name.
**Parameters:** style

- either

TimeZone.LONG

or

TimeZone.SHORT
**Parameters:** locale

- the desired locale
**Returns:** the human-readable name of the given time zone in the
given locale, or null if it's not available.
**Throws:** IllegalArgumentException

- if

style

is invalid,
or

locale

isn't one of the locales returned from

getAvailableLocales()

.
**Throws:** NullPointerException

- if

ID

or

locale

is null
**See Also:** TimeZone.getDisplayName(boolean, int, java.util.Locale)

---

#### getDisplayName

public abstract

String

getDisplayName​(

String

ID,
boolean daylight,
int style,

Locale

locale)

Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale. The given time
zone ID is "GMT" or one of the names defined using "Zone" entries
in the "tz database", a public domain time zone database at

ftp://elsie.nci.nih.gov/pub/

.
The data of this database is contained in a file whose name starts with
"tzdata", and the specification of the data format is part of the zic.8
man page, which is contained in a file whose name starts with "tzcode".

If

daylight

is true, the method should return a name
appropriate for daylight saving time even if the specified time zone
has not observed daylight saving time in the past.

If

daylight

is true, the method should return a name
appropriate for daylight saving time even if the specified time zone
has not observed daylight saving time in the past.

getGenericDisplayName

```java
public
String
getGenericDisplayName​(
String
ID,
int style,

Locale
locale)
```

Returns a generic name for the given time zone

ID

that's suitable
for presentation to the user in the specified

locale

. Generic
time zone names are neutral from standard time and daylight saving
time. For example, "PT" is the short generic name of time zone ID

America/Los_Angeles

, while its short standard time and daylight saving
time names are "PST" and "PDT", respectively. Refer to

getDisplayName

for valid time zone IDs.

The default implementation of this method returns

null

.

**Parameters:** ID

- a time zone ID string
**Parameters:** style

- either

TimeZone.LONG

or

TimeZone.SHORT
**Parameters:** locale

- the desired locale
**Returns:** the human-readable generic name of the given time zone in the
given locale, or

null

if it's not available.
**Throws:** IllegalArgumentException

- if

style

is invalid,
or

locale

isn't one of the locales returned from

getAvailableLocales()

.
**Throws:** NullPointerException

- if

ID

or

locale

is

null
**Since:** 1.8

---

#### getGenericDisplayName

public

String

getGenericDisplayName​(

String

ID,
int style,

Locale

locale)

Returns a generic name for the given time zone

ID

that's suitable
for presentation to the user in the specified

locale

. Generic
time zone names are neutral from standard time and daylight saving
time. For example, "PT" is the short generic name of time zone ID

America/Los_Angeles

, while its short standard time and daylight saving
time names are "PST" and "PDT", respectively. Refer to

getDisplayName

for valid time zone IDs.

The default implementation of this method returns

null

.

The default implementation of this method returns

null

.

---

