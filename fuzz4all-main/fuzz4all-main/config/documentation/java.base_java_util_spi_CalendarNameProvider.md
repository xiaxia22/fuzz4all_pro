# Class CalendarNameProvider

**Source:** `java.base\java\util\spi\CalendarNameProvider.html`

### Class Description

```java
public abstract class
CalendarNameProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that provide localized string
representations (display names) of

Calendar

field values.

Calendar Types

Calendar types are used to specify calendar systems for which the

getDisplayName

and

getDisplayNames

methods provide
calendar field value names. See

Calendar.getCalendarType()

for details.

Calendar Fields

Calendar fields are specified with the constants defined in

Calendar

. The following are calendar-common fields and their values to be
supported for each calendar system.

Field values

Field

Value

Description

Calendar.MONTH

Calendar.JANUARY

to

Calendar.UNDECIMBER

Month numbering is 0-based (e.g., 0 - January, ..., 11 -
December). Some calendar systems have 13 months. Month
names need to be supported in both the formatting and
stand-alone forms if required by the supported locales. If there's
no distinction in the two forms, the same names should be returned
in both of the forms.

Calendar.DAY_OF_WEEK

Calendar.SUNDAY

to

Calendar.SATURDAY

Day-of-week numbering is 1-based starting from Sunday (i.e., 1 - Sunday,
..., 7 - Saturday).

Calendar.AM_PM

Calendar.AM

to

Calendar.PM

0 - AM, 1 - PM

The following are calendar-specific fields and their values to be supported.

Calendar type and field values

Calendar Type

Field

Value

Description

"gregory"

Calendar.ERA

0

GregorianCalendar.BC

(BCE)

1

GregorianCalendar.AD

(CE)

"buddhist"

Calendar.ERA

0

BC (BCE)

1

B.E. (Buddhist Era)

"japanese"

Calendar.ERA

0

Seireki (Before Meiji)

1

Meiji

2

Taisho

3

Showa

4

Heisei

Calendar.YEAR

1

the first year in each era. It should be returned when a long
style (

Calendar.LONG_FORMAT

or

Calendar.LONG_STANDALONE

) is
specified. See also the

Year representation in

SimpleDateFormat

.

"roc"

Calendar.ERA

0

Before R.O.C.

1

R.O.C.

"islamic"

Calendar.ERA

0

Before AH

1

Anno Hijrah (AH)

Calendar field value names for

"gregory"

must be consistent with
the date-time symbols provided by

DateFormatSymbolsProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

**Since:** 1.8
**See Also:** CalendarDataProvider

,

Locale.getUnicodeLocaleType(String)

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CalendarNameProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract
String
getDisplayName​(
String
calendarType,
int field,
int value,
int style,

Locale
locale)

Returns the string representation (display name) of the calendar

field value

in the given

style

and

locale

. If no string representation is
applicable,

null

is returned.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are
specified.

value

is the numeric representation of the

field

value.
For example, if

field

is

Calendar.DAY_OF_WEEK

, the valid
values are

Calendar.SUNDAY

to

Calendar.SATURDAY

(inclusive).

style

gives the style of the string representation. It is one
of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

.

For example, the following call will return

"Sunday"

.

```java
getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);
```

**Parameters:**
- calendarType

- the calendar type. (Any calendar type given by

locale

is ignored.)
- field

- the

Calendar

field index,
such as

Calendar.DAY_OF_WEEK
- value

- the value of the

Calendar field

,
such as

Calendar.MONDAY
- style

- the string representation style: one of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

,
or

Calendar.NARROW_STANDALONE
- locale

- the desired locale

**Returns:**
- the string representation of the

field value

, or

null

if the string representation is not applicable or
the given calendar type is unknown

**Throws:**
- IllegalArgumentException

- if

field

or

style

is invalid
- NullPointerException

- if

locale

is

null

**See Also:**
- TimeZoneNameProvider

,

Calendar.get(int)

,

Calendar.getDisplayName(int, int, Locale)

---

#### public abstract
Map
<
String
,​
Integer
> getDisplayNames​(
String
calendarType,
int field,
int style,

Locale
locale)

Returns a

Map

containing all string representations (display
names) of the

Calendar

field

in the given

style

and

locale

and their corresponding field values.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are specified.

style

gives the style of the string representation. It must be
one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

. Note that narrow names may
not be unique due to use of single characters, such as "S" for Sunday
and Saturday, and that no narrow names are included in that case.

For example, the following call will return a

Map

containing

"January"

to

Calendar.JANUARY

,

"Jan"

to

Calendar.JANUARY

,

"February"

to

Calendar.FEBRUARY

,

"Feb"

to

Calendar.FEBRUARY

, and so on.

```java
getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
```

**Parameters:**
- calendarType

- the calendar type. (Any calendar type given by

locale

is ignored.)
- field

- the calendar field for which the display names are returned
- style

- the style applied to the display names; one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

,
or

Calendar.NARROW_STANDALONE
- locale

- the desired locale

**Returns:**
- a

Map

containing all display names of

field

in

style

and

locale

and their

field

values,
or

null

if no display names are defined for

field

**Throws:**
- NullPointerException

- if

locale

is

null

**See Also:**
- Calendar.getDisplayNames(int, int, Locale)

---

### Additional Sections

#### Class CalendarNameProvider

java.lang.Object

- java.util.spi.LocaleServiceProvider
- - java.util.spi.CalendarNameProvider

java.util.spi.LocaleServiceProvider

- java.util.spi.CalendarNameProvider

java.util.spi.CalendarNameProvider

```java
public abstract class
CalendarNameProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that provide localized string
representations (display names) of

Calendar

field values.

Calendar Types

Calendar types are used to specify calendar systems for which the

getDisplayName

and

getDisplayNames

methods provide
calendar field value names. See

Calendar.getCalendarType()

for details.

Calendar Fields

Calendar fields are specified with the constants defined in

Calendar

. The following are calendar-common fields and their values to be
supported for each calendar system.

Field values

Field

Value

Description

Calendar.MONTH

Calendar.JANUARY

to

Calendar.UNDECIMBER

Month numbering is 0-based (e.g., 0 - January, ..., 11 -
December). Some calendar systems have 13 months. Month
names need to be supported in both the formatting and
stand-alone forms if required by the supported locales. If there's
no distinction in the two forms, the same names should be returned
in both of the forms.

Calendar.DAY_OF_WEEK

Calendar.SUNDAY

to

Calendar.SATURDAY

Day-of-week numbering is 1-based starting from Sunday (i.e., 1 - Sunday,
..., 7 - Saturday).

Calendar.AM_PM

Calendar.AM

to

Calendar.PM

0 - AM, 1 - PM

The following are calendar-specific fields and their values to be supported.

Calendar type and field values

Calendar Type

Field

Value

Description

"gregory"

Calendar.ERA

0

GregorianCalendar.BC

(BCE)

1

GregorianCalendar.AD

(CE)

"buddhist"

Calendar.ERA

0

BC (BCE)

1

B.E. (Buddhist Era)

"japanese"

Calendar.ERA

0

Seireki (Before Meiji)

1

Meiji

2

Taisho

3

Showa

4

Heisei

Calendar.YEAR

1

the first year in each era. It should be returned when a long
style (

Calendar.LONG_FORMAT

or

Calendar.LONG_STANDALONE

) is
specified. See also the

Year representation in

SimpleDateFormat

.

"roc"

Calendar.ERA

0

Before R.O.C.

1

R.O.C.

"islamic"

Calendar.ERA

0

Before AH

1

Anno Hijrah (AH)

Calendar field value names for

"gregory"

must be consistent with
the date-time symbols provided by

DateFormatSymbolsProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

**Since:** 1.8
**See Also:** CalendarDataProvider

,

Locale.getUnicodeLocaleType(String)

public abstract class

CalendarNameProvider

extends

LocaleServiceProvider

An abstract class for service providers that provide localized string
representations (display names) of

Calendar

field values.

Calendar Types

Calendar types are used to specify calendar systems for which the

getDisplayName

and

getDisplayNames

methods provide
calendar field value names. See

Calendar.getCalendarType()

for details.

Calendar Fields

Calendar fields are specified with the constants defined in

Calendar

. The following are calendar-common fields and their values to be
supported for each calendar system.

Field values

Field

Value

Description

Calendar.MONTH

Calendar.JANUARY

to

Calendar.UNDECIMBER

Month numbering is 0-based (e.g., 0 - January, ..., 11 -
December). Some calendar systems have 13 months. Month
names need to be supported in both the formatting and
stand-alone forms if required by the supported locales. If there's
no distinction in the two forms, the same names should be returned
in both of the forms.

Calendar.DAY_OF_WEEK

Calendar.SUNDAY

to

Calendar.SATURDAY

Day-of-week numbering is 1-based starting from Sunday (i.e., 1 - Sunday,
..., 7 - Saturday).

Calendar.AM_PM

Calendar.AM

to

Calendar.PM

0 - AM, 1 - PM

The following are calendar-specific fields and their values to be supported.

Calendar type and field values

Calendar Type

Field

Value

Description

"gregory"

Calendar.ERA

0

GregorianCalendar.BC

(BCE)

1

GregorianCalendar.AD

(CE)

"buddhist"

Calendar.ERA

0

BC (BCE)

1

B.E. (Buddhist Era)

"japanese"

Calendar.ERA

0

Seireki (Before Meiji)

1

Meiji

2

Taisho

3

Showa

4

Heisei

Calendar.YEAR

1

the first year in each era. It should be returned when a long
style (

Calendar.LONG_FORMAT

or

Calendar.LONG_STANDALONE

) is
specified. See also the

Year representation in

SimpleDateFormat

.

"roc"

Calendar.ERA

0

Before R.O.C.

1

R.O.C.

"islamic"

Calendar.ERA

0

Before AH

1

Anno Hijrah (AH)

Calendar field value names for

"gregory"

must be consistent with
the date-time symbols provided by

DateFormatSymbolsProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

Calendar Types

Calendar types are used to specify calendar systems for which the

getDisplayName

and

getDisplayNames

methods provide
calendar field value names. See

Calendar.getCalendarType()

for details.

Calendar Fields

Calendar fields are specified with the constants defined in

Calendar

. The following are calendar-common fields and their values to be
supported for each calendar system.

Field values

Field

Value

Description

Calendar.MONTH

Calendar.JANUARY

to

Calendar.UNDECIMBER

Month numbering is 0-based (e.g., 0 - January, ..., 11 -
December). Some calendar systems have 13 months. Month
names need to be supported in both the formatting and
stand-alone forms if required by the supported locales. If there's
no distinction in the two forms, the same names should be returned
in both of the forms.

Calendar.DAY_OF_WEEK

Calendar.SUNDAY

to

Calendar.SATURDAY

Day-of-week numbering is 1-based starting from Sunday (i.e., 1 - Sunday,
..., 7 - Saturday).

Calendar.AM_PM

Calendar.AM

to

Calendar.PM

0 - AM, 1 - PM

The following are calendar-specific fields and their values to be supported.

Calendar type and field values

Calendar Type

Field

Value

Description

"gregory"

Calendar.ERA

0

GregorianCalendar.BC

(BCE)

1

GregorianCalendar.AD

(CE)

"buddhist"

Calendar.ERA

0

BC (BCE)

1

B.E. (Buddhist Era)

"japanese"

Calendar.ERA

0

Seireki (Before Meiji)

1

Meiji

2

Taisho

3

Showa

4

Heisei

Calendar.YEAR

1

the first year in each era. It should be returned when a long
style (

Calendar.LONG_FORMAT

or

Calendar.LONG_STANDALONE

) is
specified. See also the

Year representation in

SimpleDateFormat

.

"roc"

Calendar.ERA

0

Before R.O.C.

1

R.O.C.

"islamic"

Calendar.ERA

0

Before AH

1

Anno Hijrah (AH)

Calendar field value names for

"gregory"

must be consistent with
the date-time symbols provided by

DateFormatSymbolsProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

Calendar types are used to specify calendar systems for which the

getDisplayName

and

getDisplayNames

methods provide
calendar field value names. See

Calendar.getCalendarType()

for details.

Calendar Fields

Calendar fields are specified with the constants defined in

Calendar

. The following are calendar-common fields and their values to be
supported for each calendar system.

Field values

Field

Value

Description

Calendar.MONTH

Calendar.JANUARY

to

Calendar.UNDECIMBER

Month numbering is 0-based (e.g., 0 - January, ..., 11 -
December). Some calendar systems have 13 months. Month
names need to be supported in both the formatting and
stand-alone forms if required by the supported locales. If there's
no distinction in the two forms, the same names should be returned
in both of the forms.

Calendar.DAY_OF_WEEK

Calendar.SUNDAY

to

Calendar.SATURDAY

Day-of-week numbering is 1-based starting from Sunday (i.e., 1 - Sunday,
..., 7 - Saturday).

Calendar.AM_PM

Calendar.AM

to

Calendar.PM

0 - AM, 1 - PM

The following are calendar-specific fields and their values to be supported.

Calendar type and field values

Calendar Type

Field

Value

Description

"gregory"

Calendar.ERA

0

GregorianCalendar.BC

(BCE)

1

GregorianCalendar.AD

(CE)

"buddhist"

Calendar.ERA

0

BC (BCE)

1

B.E. (Buddhist Era)

"japanese"

Calendar.ERA

0

Seireki (Before Meiji)

1

Meiji

2

Taisho

3

Showa

4

Heisei

Calendar.YEAR

1

the first year in each era. It should be returned when a long
style (

Calendar.LONG_FORMAT

or

Calendar.LONG_STANDALONE

) is
specified. See also the

Year representation in

SimpleDateFormat

.

"roc"

Calendar.ERA

0

Before R.O.C.

1

R.O.C.

"islamic"

Calendar.ERA

0

Before AH

1

Anno Hijrah (AH)

Calendar field value names for

"gregory"

must be consistent with
the date-time symbols provided by

DateFormatSymbolsProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

Calendar Fields

Calendar fields are specified with the constants defined in

Calendar

. The following are calendar-common fields and their values to be
supported for each calendar system.

Field values

Field

Value

Description

Calendar.MONTH

Calendar.JANUARY

to

Calendar.UNDECIMBER

Month numbering is 0-based (e.g., 0 - January, ..., 11 -
December). Some calendar systems have 13 months. Month
names need to be supported in both the formatting and
stand-alone forms if required by the supported locales. If there's
no distinction in the two forms, the same names should be returned
in both of the forms.

Calendar.DAY_OF_WEEK

Calendar.SUNDAY

to

Calendar.SATURDAY

Day-of-week numbering is 1-based starting from Sunday (i.e., 1 - Sunday,
..., 7 - Saturday).

Calendar.AM_PM

Calendar.AM

to

Calendar.PM

0 - AM, 1 - PM

The following are calendar-specific fields and their values to be supported.

Calendar type and field values

Calendar Type

Field

Value

Description

"gregory"

Calendar.ERA

0

GregorianCalendar.BC

(BCE)

1

GregorianCalendar.AD

(CE)

"buddhist"

Calendar.ERA

0

BC (BCE)

1

B.E. (Buddhist Era)

"japanese"

Calendar.ERA

0

Seireki (Before Meiji)

1

Meiji

2

Taisho

3

Showa

4

Heisei

Calendar.YEAR

1

the first year in each era. It should be returned when a long
style (

Calendar.LONG_FORMAT

or

Calendar.LONG_STANDALONE

) is
specified. See also the

Year representation in

SimpleDateFormat

.

"roc"

Calendar.ERA

0

Before R.O.C.

1

R.O.C.

"islamic"

Calendar.ERA

0

Before AH

1

Anno Hijrah (AH)

Calendar field value names for

"gregory"

must be consistent with
the date-time symbols provided by

DateFormatSymbolsProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

Calendar fields are specified with the constants defined in

Calendar

. The following are calendar-common fields and their values to be
supported for each calendar system.

Field values

Field

Value

Description

Calendar.MONTH

Calendar.JANUARY

to

Calendar.UNDECIMBER

Month numbering is 0-based (e.g., 0 - January, ..., 11 -
December). Some calendar systems have 13 months. Month
names need to be supported in both the formatting and
stand-alone forms if required by the supported locales. If there's
no distinction in the two forms, the same names should be returned
in both of the forms.

Calendar.DAY_OF_WEEK

Calendar.SUNDAY

to

Calendar.SATURDAY

Day-of-week numbering is 1-based starting from Sunday (i.e., 1 - Sunday,
..., 7 - Saturday).

Calendar.AM_PM

Calendar.AM

to

Calendar.PM

0 - AM, 1 - PM

The following are calendar-specific fields and their values to be supported.

Calendar type and field values

Calendar Type

Field

Value

Description

"gregory"

Calendar.ERA

0

GregorianCalendar.BC

(BCE)

1

GregorianCalendar.AD

(CE)

"buddhist"

Calendar.ERA

0

BC (BCE)

1

B.E. (Buddhist Era)

"japanese"

Calendar.ERA

0

Seireki (Before Meiji)

1

Meiji

2

Taisho

3

Showa

4

Heisei

Calendar.YEAR

1

the first year in each era. It should be returned when a long
style (

Calendar.LONG_FORMAT

or

Calendar.LONG_STANDALONE

) is
specified. See also the

Year representation in

SimpleDateFormat

.

"roc"

Calendar.ERA

0

Before R.O.C.

1

R.O.C.

"islamic"

Calendar.ERA

0

Before AH

1

Anno Hijrah (AH)

Calendar field value names for

"gregory"

must be consistent with
the date-time symbols provided by

DateFormatSymbolsProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

The following are calendar-specific fields and their values to be supported.

Calendar type and field values

Calendar Type

Field

Value

Description

"gregory"

Calendar.ERA

0

GregorianCalendar.BC

(BCE)

1

GregorianCalendar.AD

(CE)

"buddhist"

Calendar.ERA

0

BC (BCE)

1

B.E. (Buddhist Era)

"japanese"

Calendar.ERA

0

Seireki (Before Meiji)

1

Meiji

2

Taisho

3

Showa

4

Heisei

Calendar.YEAR

1

the first year in each era. It should be returned when a long
style (

Calendar.LONG_FORMAT

or

Calendar.LONG_STANDALONE

) is
specified. See also the

Year representation in

SimpleDateFormat

.

"roc"

Calendar.ERA

0

Before R.O.C.

1

R.O.C.

"islamic"

Calendar.ERA

0

Before AH

1

Anno Hijrah (AH)

Calendar field value names for

"gregory"

must be consistent with
the date-time symbols provided by

DateFormatSymbolsProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

Calendar field value names for

"gregory"

must be consistent with
the date-time symbols provided by

DateFormatSymbolsProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

Time zone names are supported by

TimeZoneNameProvider

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CalendarNameProvider

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

getDisplayName

​(

String

calendarType,
int field,
int value,
int style,

Locale

locale)

Returns the string representation (display name) of the calendar

field value

in the given

style

and

locale

.

abstract

Map

<

String

,​

Integer

>

getDisplayNames

​(

String

calendarType,
int field,
int style,

Locale

locale)

Returns a

Map

containing all string representations (display
names) of the

Calendar

field

in the given

style

and

locale

and their corresponding field values.

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

CalendarNameProvider

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

getDisplayName

​(

String

calendarType,
int field,
int value,
int style,

Locale

locale)

Returns the string representation (display name) of the calendar

field value

in the given

style

and

locale

.

abstract

Map

<

String

,​

Integer

>

getDisplayNames

​(

String

calendarType,
int field,
int style,

Locale

locale)

Returns a

Map

containing all string representations (display
names) of the

Calendar

field

in the given

style

and

locale

and their corresponding field values.

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

Returns the string representation (display name) of the calendar

field value

in the given

style

and

locale

.

Returns a

Map

containing all string representations (display
names) of the

Calendar

field

in the given

style

and

locale

and their corresponding field values.

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

- CalendarNameProvider

```java
protected CalendarNameProvider()
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
calendarType,
int field,
int value,
int style,

Locale
locale)
```

Returns the string representation (display name) of the calendar

field value

in the given

style

and

locale

. If no string representation is
applicable,

null

is returned.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are
specified.

value

is the numeric representation of the

field

value.
For example, if

field

is

Calendar.DAY_OF_WEEK

, the valid
values are

Calendar.SUNDAY

to

Calendar.SATURDAY

(inclusive).

style

gives the style of the string representation. It is one
of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

.

For example, the following call will return

"Sunday"

.

```java
getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);
```

**Parameters:** calendarType

- the calendar type. (Any calendar type given by

locale

is ignored.)
**Parameters:** field

- the

Calendar

field index,
such as

Calendar.DAY_OF_WEEK
**Parameters:** value

- the value of the

Calendar field

,
such as

Calendar.MONDAY
**Parameters:** style

- the string representation style: one of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

,
or

Calendar.NARROW_STANDALONE
**Parameters:** locale

- the desired locale
**Returns:** the string representation of the

field value

, or

null

if the string representation is not applicable or
the given calendar type is unknown
**Throws:** IllegalArgumentException

- if

field

or

style

is invalid
**Throws:** NullPointerException

- if

locale

is

null
**See Also:** TimeZoneNameProvider

,

Calendar.get(int)

,

Calendar.getDisplayName(int, int, Locale)

- getDisplayNames

```java
public abstract
Map
<
String
,​
Integer
> getDisplayNames​(
String
calendarType,
int field,
int style,

Locale
locale)
```

Returns a

Map

containing all string representations (display
names) of the

Calendar

field

in the given

style

and

locale

and their corresponding field values.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are specified.

style

gives the style of the string representation. It must be
one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

. Note that narrow names may
not be unique due to use of single characters, such as "S" for Sunday
and Saturday, and that no narrow names are included in that case.

For example, the following call will return a

Map

containing

"January"

to

Calendar.JANUARY

,

"Jan"

to

Calendar.JANUARY

,

"February"

to

Calendar.FEBRUARY

,

"Feb"

to

Calendar.FEBRUARY

, and so on.

```java
getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
```

**Parameters:** calendarType

- the calendar type. (Any calendar type given by

locale

is ignored.)
**Parameters:** field

- the calendar field for which the display names are returned
**Parameters:** style

- the style applied to the display names; one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

,
or

Calendar.NARROW_STANDALONE
**Parameters:** locale

- the desired locale
**Returns:** a

Map

containing all display names of

field

in

style

and

locale

and their

field

values,
or

null

if no display names are defined for

field
**Throws:** NullPointerException

- if

locale

is

null
**See Also:** Calendar.getDisplayNames(int, int, Locale)

Constructor Detail

- CalendarNameProvider

```java
protected CalendarNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

CalendarNameProvider

```java
protected CalendarNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### CalendarNameProvider

protected CalendarNameProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getDisplayName

```java
public abstract
String
getDisplayName​(
String
calendarType,
int field,
int value,
int style,

Locale
locale)
```

Returns the string representation (display name) of the calendar

field value

in the given

style

and

locale

. If no string representation is
applicable,

null

is returned.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are
specified.

value

is the numeric representation of the

field

value.
For example, if

field

is

Calendar.DAY_OF_WEEK

, the valid
values are

Calendar.SUNDAY

to

Calendar.SATURDAY

(inclusive).

style

gives the style of the string representation. It is one
of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

.

For example, the following call will return

"Sunday"

.

```java
getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);
```

**Parameters:** calendarType

- the calendar type. (Any calendar type given by

locale

is ignored.)
**Parameters:** field

- the

Calendar

field index,
such as

Calendar.DAY_OF_WEEK
**Parameters:** value

- the value of the

Calendar field

,
such as

Calendar.MONDAY
**Parameters:** style

- the string representation style: one of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

,
or

Calendar.NARROW_STANDALONE
**Parameters:** locale

- the desired locale
**Returns:** the string representation of the

field value

, or

null

if the string representation is not applicable or
the given calendar type is unknown
**Throws:** IllegalArgumentException

- if

field

or

style

is invalid
**Throws:** NullPointerException

- if

locale

is

null
**See Also:** TimeZoneNameProvider

,

Calendar.get(int)

,

Calendar.getDisplayName(int, int, Locale)

- getDisplayNames

```java
public abstract
Map
<
String
,​
Integer
> getDisplayNames​(
String
calendarType,
int field,
int style,

Locale
locale)
```

Returns a

Map

containing all string representations (display
names) of the

Calendar

field

in the given

style

and

locale

and their corresponding field values.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are specified.

style

gives the style of the string representation. It must be
one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

. Note that narrow names may
not be unique due to use of single characters, such as "S" for Sunday
and Saturday, and that no narrow names are included in that case.

For example, the following call will return a

Map

containing

"January"

to

Calendar.JANUARY

,

"Jan"

to

Calendar.JANUARY

,

"February"

to

Calendar.FEBRUARY

,

"Feb"

to

Calendar.FEBRUARY

, and so on.

```java
getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
```

**Parameters:** calendarType

- the calendar type. (Any calendar type given by

locale

is ignored.)
**Parameters:** field

- the calendar field for which the display names are returned
**Parameters:** style

- the style applied to the display names; one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

,
or

Calendar.NARROW_STANDALONE
**Parameters:** locale

- the desired locale
**Returns:** a

Map

containing all display names of

field

in

style

and

locale

and their

field

values,
or

null

if no display names are defined for

field
**Throws:** NullPointerException

- if

locale

is

null
**See Also:** Calendar.getDisplayNames(int, int, Locale)

---

#### Method Detail

getDisplayName

```java
public abstract
String
getDisplayName​(
String
calendarType,
int field,
int value,
int style,

Locale
locale)
```

Returns the string representation (display name) of the calendar

field value

in the given

style

and

locale

. If no string representation is
applicable,

null

is returned.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are
specified.

value

is the numeric representation of the

field

value.
For example, if

field

is

Calendar.DAY_OF_WEEK

, the valid
values are

Calendar.SUNDAY

to

Calendar.SATURDAY

(inclusive).

style

gives the style of the string representation. It is one
of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

.

For example, the following call will return

"Sunday"

.

```java
getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);
```

**Parameters:** calendarType

- the calendar type. (Any calendar type given by

locale

is ignored.)
**Parameters:** field

- the

Calendar

field index,
such as

Calendar.DAY_OF_WEEK
**Parameters:** value

- the value of the

Calendar field

,
such as

Calendar.MONDAY
**Parameters:** style

- the string representation style: one of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

,
or

Calendar.NARROW_STANDALONE
**Parameters:** locale

- the desired locale
**Returns:** the string representation of the

field value

, or

null

if the string representation is not applicable or
the given calendar type is unknown
**Throws:** IllegalArgumentException

- if

field

or

style

is invalid
**Throws:** NullPointerException

- if

locale

is

null
**See Also:** TimeZoneNameProvider

,

Calendar.get(int)

,

Calendar.getDisplayName(int, int, Locale)

---

#### getDisplayName

public abstract

String

getDisplayName​(

String

calendarType,
int field,
int value,
int style,

Locale

locale)

Returns the string representation (display name) of the calendar

field value

in the given

style

and

locale

. If no string representation is
applicable,

null

is returned.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are
specified.

value

is the numeric representation of the

field

value.
For example, if

field

is

Calendar.DAY_OF_WEEK

, the valid
values are

Calendar.SUNDAY

to

Calendar.SATURDAY

(inclusive).

style

gives the style of the string representation. It is one
of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

.

For example, the following call will return

"Sunday"

.

```java
getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);
```

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are
specified.

value

is the numeric representation of the

field

value.
For example, if

field

is

Calendar.DAY_OF_WEEK

, the valid
values are

Calendar.SUNDAY

to

Calendar.SATURDAY

(inclusive).

style

gives the style of the string representation. It is one
of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

.

For example, the following call will return

"Sunday"

.

```java
getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);
```

value

is the numeric representation of the

field

value.
For example, if

field

is

Calendar.DAY_OF_WEEK

, the valid
values are

Calendar.SUNDAY

to

Calendar.SATURDAY

(inclusive).

style

gives the style of the string representation. It is one
of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

.

For example, the following call will return

"Sunday"

.

```java
getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);
```

style

gives the style of the string representation. It is one
of

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

.

For example, the following call will return

"Sunday"

.

```java
getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);
```

For example, the following call will return

"Sunday"

.

```java
getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);
```

getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
Calendar.LONG_STANDALONE, Locale.ENGLISH);

getDisplayNames

```java
public abstract
Map
<
String
,​
Integer
> getDisplayNames​(
String
calendarType,
int field,
int style,

Locale
locale)
```

Returns a

Map

containing all string representations (display
names) of the

Calendar

field

in the given

style

and

locale

and their corresponding field values.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are specified.

style

gives the style of the string representation. It must be
one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

. Note that narrow names may
not be unique due to use of single characters, such as "S" for Sunday
and Saturday, and that no narrow names are included in that case.

For example, the following call will return a

Map

containing

"January"

to

Calendar.JANUARY

,

"Jan"

to

Calendar.JANUARY

,

"February"

to

Calendar.FEBRUARY

,

"Feb"

to

Calendar.FEBRUARY

, and so on.

```java
getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
```

**Parameters:** calendarType

- the calendar type. (Any calendar type given by

locale

is ignored.)
**Parameters:** field

- the calendar field for which the display names are returned
**Parameters:** style

- the style applied to the display names; one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

,
or

Calendar.NARROW_STANDALONE
**Parameters:** locale

- the desired locale
**Returns:** a

Map

containing all display names of

field

in

style

and

locale

and their

field

values,
or

null

if no display names are defined for

field
**Throws:** NullPointerException

- if

locale

is

null
**See Also:** Calendar.getDisplayNames(int, int, Locale)

---

#### getDisplayNames

public abstract

Map

<

String

,​

Integer

> getDisplayNames​(

String

calendarType,
int field,
int style,

Locale

locale)

Returns a

Map

containing all string representations (display
names) of the

Calendar

field

in the given

style

and

locale

and their corresponding field values.

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are specified.

style

gives the style of the string representation. It must be
one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

. Note that narrow names may
not be unique due to use of single characters, such as "S" for Sunday
and Saturday, and that no narrow names are included in that case.

For example, the following call will return a

Map

containing

"January"

to

Calendar.JANUARY

,

"Jan"

to

Calendar.JANUARY

,

"February"

to

Calendar.FEBRUARY

,

"Feb"

to

Calendar.FEBRUARY

, and so on.

```java
getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
```

field

is a

Calendar

field index, such as

Calendar.MONTH

. The time zone fields,

Calendar.ZONE_OFFSET

and

Calendar.DST_OFFSET

, are

not

supported by this
method.

null

must be returned if any time zone fields are specified.

style

gives the style of the string representation. It must be
one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

. Note that narrow names may
not be unique due to use of single characters, such as "S" for Sunday
and Saturday, and that no narrow names are included in that case.

For example, the following call will return a

Map

containing

"January"

to

Calendar.JANUARY

,

"Jan"

to

Calendar.JANUARY

,

"February"

to

Calendar.FEBRUARY

,

"Feb"

to

Calendar.FEBRUARY

, and so on.

```java
getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
```

style

gives the style of the string representation. It must be
one of

Calendar.ALL_STYLES

,

Calendar.SHORT_FORMAT

(

SHORT

),

Calendar.SHORT_STANDALONE

,

Calendar.LONG_FORMAT

(

LONG

),

Calendar.LONG_STANDALONE

,

Calendar.NARROW_FORMAT

, or

Calendar.NARROW_STANDALONE

. Note that narrow names may
not be unique due to use of single characters, such as "S" for Sunday
and Saturday, and that no narrow names are included in that case.

For example, the following call will return a

Map

containing

"January"

to

Calendar.JANUARY

,

"Jan"

to

Calendar.JANUARY

,

"February"

to

Calendar.FEBRUARY

,

"Feb"

to

Calendar.FEBRUARY

, and so on.

```java
getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
```

For example, the following call will return a

Map

containing

"January"

to

Calendar.JANUARY

,

"Jan"

to

Calendar.JANUARY

,

"February"

to

Calendar.FEBRUARY

,

"Feb"

to

Calendar.FEBRUARY

, and so on.

```java
getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
```

getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);

---

