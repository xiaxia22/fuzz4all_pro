# Class CalendarDataProvider

**Source:** `java.base\java\util\spi\CalendarDataProvider.html`

### Class Description

```java
public abstract class
CalendarDataProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that provide locale-dependent

Calendar

parameters.

**Since:** 1.8
**See Also:** CalendarNameProvider

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CalendarDataProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract int getFirstDayOfWeek​(
Locale
locale)

Returns the first day of a week in the given

locale

. This
information is required by

Calendar

to support operations on the
week-related calendar fields.

**Parameters:**
- locale

- the desired locale

**Returns:**
- the first day of a week; one of

Calendar.SUNDAY

..

Calendar.SATURDAY

,
or 0 if the value isn't available for the

locale

**Throws:**
- NullPointerException

- if

locale

is

null

.

**See Also:**
- Calendar.getFirstDayOfWeek()

,

First Week

---

#### public abstract int getMinimalDaysInFirstWeek​(
Locale
locale)

Returns the minimal number of days required in the first week of a
year. This information is required by

Calendar

to determine the
first week of a year. Refer to the description of

how

Calendar

determines
the first week

.

**Parameters:**
- locale

- the desired locale

**Returns:**
- the minimal number of days of the first week,
or 0 if the value isn't available for the

locale

**Throws:**
- NullPointerException

- if

locale

is

null

.

**See Also:**
- Calendar.getMinimalDaysInFirstWeek()

---

### Additional Sections

#### Class CalendarDataProvider

java.lang.Object

- java.util.spi.LocaleServiceProvider
- - java.util.spi.CalendarDataProvider

java.util.spi.LocaleServiceProvider

- java.util.spi.CalendarDataProvider

java.util.spi.CalendarDataProvider

```java
public abstract class
CalendarDataProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that provide locale-dependent

Calendar

parameters.

**Since:** 1.8
**See Also:** CalendarNameProvider

public abstract class

CalendarDataProvider

extends

LocaleServiceProvider

An abstract class for service providers that provide locale-dependent

Calendar

parameters.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CalendarDataProvider

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

abstract int

getFirstDayOfWeek

​(

Locale

locale)

Returns the first day of a week in the given

locale

.

abstract int

getMinimalDaysInFirstWeek

​(

Locale

locale)

Returns the minimal number of days required in the first week of a
year.

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

CalendarDataProvider

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

abstract int

getFirstDayOfWeek

​(

Locale

locale)

Returns the first day of a week in the given

locale

.

abstract int

getMinimalDaysInFirstWeek

​(

Locale

locale)

Returns the minimal number of days required in the first week of a
year.

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

Returns the first day of a week in the given

locale

.

Returns the minimal number of days required in the first week of a
year.

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

- CalendarDataProvider

```java
protected CalendarDataProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- getFirstDayOfWeek

```java
public abstract int getFirstDayOfWeek​(
Locale
locale)
```

Returns the first day of a week in the given

locale

. This
information is required by

Calendar

to support operations on the
week-related calendar fields.

**Parameters:** locale

- the desired locale
**Returns:** the first day of a week; one of

Calendar.SUNDAY

..

Calendar.SATURDAY

,
or 0 if the value isn't available for the

locale
**Throws:** NullPointerException

- if

locale

is

null

.
**See Also:** Calendar.getFirstDayOfWeek()

,

First Week

- getMinimalDaysInFirstWeek

```java
public abstract int getMinimalDaysInFirstWeek​(
Locale
locale)
```

Returns the minimal number of days required in the first week of a
year. This information is required by

Calendar

to determine the
first week of a year. Refer to the description of

how

Calendar

determines
the first week

.

**Parameters:** locale

- the desired locale
**Returns:** the minimal number of days of the first week,
or 0 if the value isn't available for the

locale
**Throws:** NullPointerException

- if

locale

is

null

.
**See Also:** Calendar.getMinimalDaysInFirstWeek()

Constructor Detail

- CalendarDataProvider

```java
protected CalendarDataProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

CalendarDataProvider

```java
protected CalendarDataProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### CalendarDataProvider

protected CalendarDataProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getFirstDayOfWeek

```java
public abstract int getFirstDayOfWeek​(
Locale
locale)
```

Returns the first day of a week in the given

locale

. This
information is required by

Calendar

to support operations on the
week-related calendar fields.

**Parameters:** locale

- the desired locale
**Returns:** the first day of a week; one of

Calendar.SUNDAY

..

Calendar.SATURDAY

,
or 0 if the value isn't available for the

locale
**Throws:** NullPointerException

- if

locale

is

null

.
**See Also:** Calendar.getFirstDayOfWeek()

,

First Week

- getMinimalDaysInFirstWeek

```java
public abstract int getMinimalDaysInFirstWeek​(
Locale
locale)
```

Returns the minimal number of days required in the first week of a
year. This information is required by

Calendar

to determine the
first week of a year. Refer to the description of

how

Calendar

determines
the first week

.

**Parameters:** locale

- the desired locale
**Returns:** the minimal number of days of the first week,
or 0 if the value isn't available for the

locale
**Throws:** NullPointerException

- if

locale

is

null

.
**See Also:** Calendar.getMinimalDaysInFirstWeek()

---

#### Method Detail

getFirstDayOfWeek

```java
public abstract int getFirstDayOfWeek​(
Locale
locale)
```

Returns the first day of a week in the given

locale

. This
information is required by

Calendar

to support operations on the
week-related calendar fields.

**Parameters:** locale

- the desired locale
**Returns:** the first day of a week; one of

Calendar.SUNDAY

..

Calendar.SATURDAY

,
or 0 if the value isn't available for the

locale
**Throws:** NullPointerException

- if

locale

is

null

.
**See Also:** Calendar.getFirstDayOfWeek()

,

First Week

---

#### getFirstDayOfWeek

public abstract int getFirstDayOfWeek​(

Locale

locale)

Returns the first day of a week in the given

locale

. This
information is required by

Calendar

to support operations on the
week-related calendar fields.

getMinimalDaysInFirstWeek

```java
public abstract int getMinimalDaysInFirstWeek​(
Locale
locale)
```

Returns the minimal number of days required in the first week of a
year. This information is required by

Calendar

to determine the
first week of a year. Refer to the description of

how

Calendar

determines
the first week

.

**Parameters:** locale

- the desired locale
**Returns:** the minimal number of days of the first week,
or 0 if the value isn't available for the

locale
**Throws:** NullPointerException

- if

locale

is

null

.
**See Also:** Calendar.getMinimalDaysInFirstWeek()

---

#### getMinimalDaysInFirstWeek

public abstract int getMinimalDaysInFirstWeek​(

Locale

locale)

Returns the minimal number of days required in the first week of a
year. This information is required by

Calendar

to determine the
first week of a year. Refer to the description of

how

Calendar

determines
the first week

.

---

