# Enum Month

**Source:** `java.base\java\time\Month.html`

### Class Description

```java
public enum
Month

extends
Enum
<
Month
>
implements
TemporalAccessor
,
TemporalAdjuster
```

A month-of-year, such as 'July'.

Month

is an enum representing the 12 months of the year -
January, February, March, April, May, June, July, August, September, October,
November and December.

In addition to the textual enum name, each month-of-year has an

int

value.
The

int

value follows normal usage and the ISO-8601 standard,
from 1 (January) to 12 (December). It is recommended that applications use the enum
rather than the

int

value to ensure code clarity.

Do not use

ordinal()

to obtain the numeric representation of

Month

.
Use

getValue()

instead.

This enum represents a common concept that is found in many calendar systems.
As such, this enum may be used by any calendar system that has the month-of-year
concept defined exactly equivalent to the ISO-8601 calendar system.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Month

>

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
Month
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Month c : Month.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Month
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

#### public static
Month
of​(int month)

Obtains an instance of

Month

from an

int

value.

Month

is an enum representing the 12 months of the year.
This factory allows the enum to be obtained from the

int

value.
The

int

value follows the ISO-8601 standard, from 1 (January) to 12 (December).

**Parameters:**
- month

- the month-of-year to represent, from 1 (January) to 12 (December)

**Returns:**
- the month-of-year, not null

**Throws:**
- DateTimeException

- if the month-of-year is invalid

---

#### public static
Month
from​(
TemporalAccessor
temporal)

Obtains an instance of

Month

from a temporal object.

This obtains a month based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

Month

.

The conversion extracts the

MONTH_OF_YEAR

field.
The extraction is only permitted if the temporal object has an ISO
chronology, or can be converted to a

LocalDate

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

Month::from

.

**Parameters:**
- temporal

- the temporal object to convert, not null

**Returns:**
- the month-of-year, not null

**Throws:**
- DateTimeException

- if unable to convert to a

Month

---

#### public int getValue()

Gets the month-of-year

int

value.

The values are numbered following the ISO-8601 standard,
from 1 (January) to 12 (December).

**Returns:**
- the month-of-year, from 1 (January) to 12 (December)

---

#### public
String
getDisplayName​(
TextStyle
style,

Locale
locale)

Gets the textual representation, such as 'Jan' or 'December'.

This returns the textual name used to identify the month-of-year,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

**Parameters:**
- style

- the length of the text required, not null
- locale

- the locale to use, not null

**Returns:**
- the text value of the month-of-year, not null

---

#### public boolean isSupported​(
TemporalField
field)

Checks if the specified field is supported.

This checks if this month-of-year can be queried for the specified field.
If false, then calling the

range

and

get

methods will throw an exception.

If the field is

MONTH_OF_YEAR

then
this method returns true.
All other

ChronoField

instances will return false.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.isSupportedBy(TemporalAccessor)

passing

this

as the argument.
Whether the field is supported is determined by the field.

**Specified by:**
- isSupported

in interface

TemporalAccessor

**Parameters:**
- field

- the field to check, null returns false

**Returns:**
- true if the field is supported on this month-of-year, false if not

---

#### public
ValueRange
range​(
TemporalField
field)

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This month is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
range of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

**Specified by:**
- range

in interface

TemporalAccessor

**Parameters:**
- field

- the field to query the range for, not null

**Returns:**
- the range of valid values for the field, not null

**Throws:**
- DateTimeException

- if the range for the field cannot be obtained
- UnsupportedTemporalTypeException

- if the field is not supported

---

#### public int get​(
TemporalField
field)

Gets the value of the specified field from this month-of-year as an

int

.

This queries this month for the value of the specified field.
The returned value will always be within the valid range of values for the field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

**Specified by:**
- get

in interface

TemporalAccessor

**Parameters:**
- field

- the field to get, not null

**Returns:**
- the value for the field, within the valid range of values

**Throws:**
- DateTimeException

- if a value for the field cannot be obtained or
the value is outside the range of valid values for the field
- UnsupportedTemporalTypeException

- if the field is not supported or
the range of values exceeds an

int
- ArithmeticException

- if numeric overflow occurs

---

#### public long getLong​(
TemporalField
field)

Gets the value of the specified field from this month-of-year as a

long

.

This queries this month for the value of the specified field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

**Specified by:**
- getLong

in interface

TemporalAccessor

**Parameters:**
- field

- the field to get, not null

**Returns:**
- the value for the field

**Throws:**
- DateTimeException

- if a value for the field cannot be obtained
- UnsupportedTemporalTypeException

- if the field is not supported
- ArithmeticException

- if numeric overflow occurs

---

#### public
Month
plus​(long months)

Returns the month-of-year that is the specified number of months after this one.

The calculation rolls around the end of the year from December to January.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

**Parameters:**
- months

- the months to add, positive or negative

**Returns:**
- the resulting month, not null

---

#### public
Month
minus​(long months)

Returns the month-of-year that is the specified number of months before this one.

The calculation rolls around the start of the year from January to December.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

**Parameters:**
- months

- the months to subtract, positive or negative

**Returns:**
- the resulting month, not null

---

#### public int length​(boolean leapYear)

Gets the length of this month in days.

This takes a flag to determine whether to return the length for a leap year or not.

February has 28 days in a standard year and 29 days in a leap year.
April, June, September and November have 30 days.
All other months have 31 days.

**Parameters:**
- leapYear

- true if the length is required for a leap year

**Returns:**
- the length of this month in days, from 28 to 31

---

#### public int minLength()

Gets the minimum length of this month in days.

February has a minimum length of 28 days.
April, June, September and November have 30 days.
All other months have 31 days.

**Returns:**
- the minimum length of this month in days, from 28 to 31

---

#### public int maxLength()

Gets the maximum length of this month in days.

February has a maximum length of 29 days.
April, June, September and November have 30 days.
All other months have 31 days.

**Returns:**
- the maximum length of this month in days, from 29 to 31

---

#### public int firstDayOfYear​(boolean leapYear)

Gets the day-of-year corresponding to the first day of this month.

This returns the day-of-year that this month begins on, using the leap
year flag to determine the length of February.

**Parameters:**
- leapYear

- true if the length is required for a leap year

**Returns:**
- the day of year corresponding to the first day of this month, from 1 to 336

---

#### public
Month
firstMonthOfQuarter()

Gets the month corresponding to the first month of this quarter.

The year can be divided into four quarters.
This method returns the first month of the quarter for the base month.
January, February and March return January.
April, May and June return April.
July, August and September return July.
October, November and December return October.

**Returns:**
- the first month of the quarter corresponding to this month, not null

---

#### public <R> R query​(
TemporalQuery
<R> query)

Queries this month-of-year using the specified query.

This queries this month-of-year using the specified query strategy object.
The

TemporalQuery

object defines the logic to be used to
obtain the result. Read the documentation of the query to understand
what the result of this method will be.

The result of this method is obtained by invoking the

TemporalQuery.queryFrom(TemporalAccessor)

method on the
specified query passing

this

as the argument.

**Specified by:**
- query

in interface

TemporalAccessor

**Parameters:**
- query

- the query to invoke, not null

**Returns:**
- the query result, null may be returned (defined by the query)

**Throws:**
- DateTimeException

- if unable to query (defined by the query)
- ArithmeticException

- if numeric overflow occurs (defined by the query)

**Type Parameters:**
- R

- the type of the result

---

#### public
Temporal
adjustInto​(
Temporal
temporal)

Adjusts the specified temporal object to have this month-of-year.

This returns a temporal object of the same observable type as the input
with the month-of-year changed to be the same as this.

The adjustment is equivalent to using

Temporal.with(TemporalField, long)

passing

ChronoField.MONTH_OF_YEAR

as the field.
If the specified temporal object does not use the ISO calendar system then
a

DateTimeException

is thrown.

In most cases, it is clearer to reverse the calling pattern by using

Temporal.with(TemporalAdjuster)

:

```java
// these two lines are equivalent, but the second approach is recommended
temporal = thisMonth.adjustInto(temporal);
temporal = temporal.with(thisMonth);
```

For example, given a date in May, the following are output:

```java
dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later
```

This instance is immutable and unaffected by this method call.

**Specified by:**
- adjustInto

in interface

TemporalAdjuster

**Parameters:**
- temporal

- the target object to be adjusted, not null

**Returns:**
- the adjusted object, not null

**Throws:**
- DateTimeException

- if unable to make the adjustment
- ArithmeticException

- if numeric overflow occurs

---

### Additional Sections

#### Enum Month

java.lang.Object

- java.lang.Enum

<

Month

>
- - java.time.Month

java.lang.Enum

<

Month

>

- java.time.Month

java.time.Month

**All Implemented Interfaces:** Serializable

,

Comparable

<

Month

>

,

TemporalAccessor

,

TemporalAdjuster

```java
public enum
Month

extends
Enum
<
Month
>
implements
TemporalAccessor
,
TemporalAdjuster
```

A month-of-year, such as 'July'.

Month

is an enum representing the 12 months of the year -
January, February, March, April, May, June, July, August, September, October,
November and December.

In addition to the textual enum name, each month-of-year has an

int

value.
The

int

value follows normal usage and the ISO-8601 standard,
from 1 (January) to 12 (December). It is recommended that applications use the enum
rather than the

int

value to ensure code clarity.

Do not use

ordinal()

to obtain the numeric representation of

Month

.
Use

getValue()

instead.

This enum represents a common concept that is found in many calendar systems.
As such, this enum may be used by any calendar system that has the month-of-year
concept defined exactly equivalent to the ISO-8601 calendar system.

**Implementation Requirements:** This is an immutable and thread-safe enum.
**Since:** 1.8

public enum

Month

extends

Enum

<

Month

>
implements

TemporalAccessor

,

TemporalAdjuster

A month-of-year, such as 'July'.

Month

is an enum representing the 12 months of the year -
January, February, March, April, May, June, July, August, September, October,
November and December.

In addition to the textual enum name, each month-of-year has an

int

value.
The

int

value follows normal usage and the ISO-8601 standard,
from 1 (January) to 12 (December). It is recommended that applications use the enum
rather than the

int

value to ensure code clarity.

Do not use

ordinal()

to obtain the numeric representation of

Month

.
Use

getValue()

instead.

This enum represents a common concept that is found in many calendar systems.
As such, this enum may be used by any calendar system that has the month-of-year
concept defined exactly equivalent to the ISO-8601 calendar system.

Month

is an enum representing the 12 months of the year -
January, February, March, April, May, June, July, August, September, October,
November and December.

In addition to the textual enum name, each month-of-year has an

int

value.
The

int

value follows normal usage and the ISO-8601 standard,
from 1 (January) to 12 (December). It is recommended that applications use the enum
rather than the

int

value to ensure code clarity.

Do not use

ordinal()

to obtain the numeric representation of

Month

.
Use

getValue()

instead.

This enum represents a common concept that is found in many calendar systems.
As such, this enum may be used by any calendar system that has the month-of-year
concept defined exactly equivalent to the ISO-8601 calendar system.

In addition to the textual enum name, each month-of-year has an

int

value.
The

int

value follows normal usage and the ISO-8601 standard,
from 1 (January) to 12 (December). It is recommended that applications use the enum
rather than the

int

value to ensure code clarity.

Do not use

ordinal()

to obtain the numeric representation of

Month

.
Use

getValue()

instead.

This enum represents a common concept that is found in many calendar systems.
As such, this enum may be used by any calendar system that has the month-of-year
concept defined exactly equivalent to the ISO-8601 calendar system.

Do not use

ordinal()

to obtain the numeric representation of

Month

.
Use

getValue()

instead.

This enum represents a common concept that is found in many calendar systems.
As such, this enum may be used by any calendar system that has the month-of-year
concept defined exactly equivalent to the ISO-8601 calendar system.

This enum represents a common concept that is found in many calendar systems.
As such, this enum may be used by any calendar system that has the month-of-year
concept defined exactly equivalent to the ISO-8601 calendar system.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

APRIL

The singleton instance for the month of April with 30 days.

AUGUST

The singleton instance for the month of August with 31 days.

DECEMBER

The singleton instance for the month of December with 31 days.

FEBRUARY

The singleton instance for the month of February with 28 days, or 29 in a leap year.

JANUARY

The singleton instance for the month of January with 31 days.

JULY

The singleton instance for the month of July with 31 days.

JUNE

The singleton instance for the month of June with 30 days.

MARCH

The singleton instance for the month of March with 31 days.

MAY

The singleton instance for the month of May with 31 days.

NOVEMBER

The singleton instance for the month of November with 30 days.

OCTOBER

The singleton instance for the month of October with 31 days.

SEPTEMBER

The singleton instance for the month of September with 30 days.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Temporal

adjustInto

​(

Temporal

temporal)

Adjusts the specified temporal object to have this month-of-year.

int

firstDayOfYear

​(boolean leapYear)

Gets the day-of-year corresponding to the first day of this month.

Month

firstMonthOfQuarter

()

Gets the month corresponding to the first month of this quarter.

static

Month

from

​(

TemporalAccessor

temporal)

Obtains an instance of

Month

from a temporal object.

int

get

​(

TemporalField

field)

Gets the value of the specified field from this month-of-year as an

int

.

String

getDisplayName

​(

TextStyle

style,

Locale

locale)

Gets the textual representation, such as 'Jan' or 'December'.

long

getLong

​(

TemporalField

field)

Gets the value of the specified field from this month-of-year as a

long

.

int

getValue

()

Gets the month-of-year

int

value.

boolean

isSupported

​(

TemporalField

field)

Checks if the specified field is supported.

int

length

​(boolean leapYear)

Gets the length of this month in days.

int

maxLength

()

Gets the maximum length of this month in days.

int

minLength

()

Gets the minimum length of this month in days.

Month

minus

​(long months)

Returns the month-of-year that is the specified number of months before this one.

static

Month

of

​(int month)

Obtains an instance of

Month

from an

int

value.

Month

plus

​(long months)

Returns the month-of-year that is the specified number of months after this one.

<R> R

query

​(

TemporalQuery

<R> query)

Queries this month-of-year using the specified query.

ValueRange

range

​(

TemporalField

field)

Gets the range of valid values for the specified field.

static

Month

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Month

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

APRIL

The singleton instance for the month of April with 30 days.

AUGUST

The singleton instance for the month of August with 31 days.

DECEMBER

The singleton instance for the month of December with 31 days.

FEBRUARY

The singleton instance for the month of February with 28 days, or 29 in a leap year.

JANUARY

The singleton instance for the month of January with 31 days.

JULY

The singleton instance for the month of July with 31 days.

JUNE

The singleton instance for the month of June with 30 days.

MARCH

The singleton instance for the month of March with 31 days.

MAY

The singleton instance for the month of May with 31 days.

NOVEMBER

The singleton instance for the month of November with 30 days.

OCTOBER

The singleton instance for the month of October with 31 days.

SEPTEMBER

The singleton instance for the month of September with 30 days.

---

#### Enum Constant Summary

The singleton instance for the month of April with 30 days.

The singleton instance for the month of August with 31 days.

The singleton instance for the month of December with 31 days.

The singleton instance for the month of February with 28 days, or 29 in a leap year.

The singleton instance for the month of January with 31 days.

The singleton instance for the month of July with 31 days.

The singleton instance for the month of June with 30 days.

The singleton instance for the month of March with 31 days.

The singleton instance for the month of May with 31 days.

The singleton instance for the month of November with 30 days.

The singleton instance for the month of October with 31 days.

The singleton instance for the month of September with 30 days.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Temporal

adjustInto

​(

Temporal

temporal)

Adjusts the specified temporal object to have this month-of-year.

int

firstDayOfYear

​(boolean leapYear)

Gets the day-of-year corresponding to the first day of this month.

Month

firstMonthOfQuarter

()

Gets the month corresponding to the first month of this quarter.

static

Month

from

​(

TemporalAccessor

temporal)

Obtains an instance of

Month

from a temporal object.

int

get

​(

TemporalField

field)

Gets the value of the specified field from this month-of-year as an

int

.

String

getDisplayName

​(

TextStyle

style,

Locale

locale)

Gets the textual representation, such as 'Jan' or 'December'.

long

getLong

​(

TemporalField

field)

Gets the value of the specified field from this month-of-year as a

long

.

int

getValue

()

Gets the month-of-year

int

value.

boolean

isSupported

​(

TemporalField

field)

Checks if the specified field is supported.

int

length

​(boolean leapYear)

Gets the length of this month in days.

int

maxLength

()

Gets the maximum length of this month in days.

int

minLength

()

Gets the minimum length of this month in days.

Month

minus

​(long months)

Returns the month-of-year that is the specified number of months before this one.

static

Month

of

​(int month)

Obtains an instance of

Month

from an

int

value.

Month

plus

​(long months)

Returns the month-of-year that is the specified number of months after this one.

<R> R

query

​(

TemporalQuery

<R> query)

Queries this month-of-year using the specified query.

ValueRange

range

​(

TemporalField

field)

Gets the range of valid values for the specified field.

static

Month

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Month

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

---

#### Method Summary

Adjusts the specified temporal object to have this month-of-year.

Gets the day-of-year corresponding to the first day of this month.

Gets the month corresponding to the first month of this quarter.

Obtains an instance of

Month

from a temporal object.

Gets the value of the specified field from this month-of-year as an

int

.

Gets the textual representation, such as 'Jan' or 'December'.

Gets the value of the specified field from this month-of-year as a

long

.

Gets the month-of-year

int

value.

Checks if the specified field is supported.

Gets the length of this month in days.

Gets the maximum length of this month in days.

Gets the minimum length of this month in days.

Returns the month-of-year that is the specified number of months before this one.

Obtains an instance of

Month

from an

int

value.

Returns the month-of-year that is the specified number of months after this one.

Queries this month-of-year using the specified query.

Gets the range of valid values for the specified field.

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- JANUARY

```java
public static final
Month
JANUARY
```

The singleton instance for the month of January with 31 days.
This has the numeric value of

1

.

- FEBRUARY

```java
public static final
Month
FEBRUARY
```

The singleton instance for the month of February with 28 days, or 29 in a leap year.
This has the numeric value of

2

.

- MARCH

```java
public static final
Month
MARCH
```

The singleton instance for the month of March with 31 days.
This has the numeric value of

3

.

- APRIL

```java
public static final
Month
APRIL
```

The singleton instance for the month of April with 30 days.
This has the numeric value of

4

.

- MAY

```java
public static final
Month
MAY
```

The singleton instance for the month of May with 31 days.
This has the numeric value of

5

.

- JUNE

```java
public static final
Month
JUNE
```

The singleton instance for the month of June with 30 days.
This has the numeric value of

6

.

- JULY

```java
public static final
Month
JULY
```

The singleton instance for the month of July with 31 days.
This has the numeric value of

7

.

- AUGUST

```java
public static final
Month
AUGUST
```

The singleton instance for the month of August with 31 days.
This has the numeric value of

8

.

- SEPTEMBER

```java
public static final
Month
SEPTEMBER
```

The singleton instance for the month of September with 30 days.
This has the numeric value of

9

.

- OCTOBER

```java
public static final
Month
OCTOBER
```

The singleton instance for the month of October with 31 days.
This has the numeric value of

10

.

- NOVEMBER

```java
public static final
Month
NOVEMBER
```

The singleton instance for the month of November with 30 days.
This has the numeric value of

11

.

- DECEMBER

```java
public static final
Month
DECEMBER
```

The singleton instance for the month of December with 31 days.
This has the numeric value of

12

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Month
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Month c : Month.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Month
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

- of

```java
public static
Month
of​(int month)
```

Obtains an instance of

Month

from an

int

value.

Month

is an enum representing the 12 months of the year.
This factory allows the enum to be obtained from the

int

value.
The

int

value follows the ISO-8601 standard, from 1 (January) to 12 (December).

**Parameters:** month

- the month-of-year to represent, from 1 (January) to 12 (December)
**Returns:** the month-of-year, not null
**Throws:** DateTimeException

- if the month-of-year is invalid

- from

```java
public static
Month
from​(
TemporalAccessor
temporal)
```

Obtains an instance of

Month

from a temporal object.

This obtains a month based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

Month

.

The conversion extracts the

MONTH_OF_YEAR

field.
The extraction is only permitted if the temporal object has an ISO
chronology, or can be converted to a

LocalDate

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

Month::from

.

**Parameters:** temporal

- the temporal object to convert, not null
**Returns:** the month-of-year, not null
**Throws:** DateTimeException

- if unable to convert to a

Month

- getValue

```java
public int getValue()
```

Gets the month-of-year

int

value.

The values are numbered following the ISO-8601 standard,
from 1 (January) to 12 (December).

**Returns:** the month-of-year, from 1 (January) to 12 (December)

- getDisplayName

```java
public
String
getDisplayName​(
TextStyle
style,

Locale
locale)
```

Gets the textual representation, such as 'Jan' or 'December'.

This returns the textual name used to identify the month-of-year,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

**Parameters:** style

- the length of the text required, not null
**Parameters:** locale

- the locale to use, not null
**Returns:** the text value of the month-of-year, not null

- isSupported

```java
public boolean isSupported​(
TemporalField
field)
```

Checks if the specified field is supported.

This checks if this month-of-year can be queried for the specified field.
If false, then calling the

range

and

get

methods will throw an exception.

If the field is

MONTH_OF_YEAR

then
this method returns true.
All other

ChronoField

instances will return false.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.isSupportedBy(TemporalAccessor)

passing

this

as the argument.
Whether the field is supported is determined by the field.

**Specified by:** isSupported

in interface

TemporalAccessor
**Parameters:** field

- the field to check, null returns false
**Returns:** true if the field is supported on this month-of-year, false if not

- range

```java
public
ValueRange
range​(
TemporalField
field)
```

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This month is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
range of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

**Specified by:** range

in interface

TemporalAccessor
**Parameters:** field

- the field to query the range for, not null
**Returns:** the range of valid values for the field, not null
**Throws:** DateTimeException

- if the range for the field cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the field is not supported

- get

```java
public int get​(
TemporalField
field)
```

Gets the value of the specified field from this month-of-year as an

int

.

This queries this month for the value of the specified field.
The returned value will always be within the valid range of values for the field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

**Specified by:** get

in interface

TemporalAccessor
**Parameters:** field

- the field to get, not null
**Returns:** the value for the field, within the valid range of values
**Throws:** DateTimeException

- if a value for the field cannot be obtained or
the value is outside the range of valid values for the field
**Throws:** UnsupportedTemporalTypeException

- if the field is not supported or
the range of values exceeds an

int
**Throws:** ArithmeticException

- if numeric overflow occurs

- getLong

```java
public long getLong​(
TemporalField
field)
```

Gets the value of the specified field from this month-of-year as a

long

.

This queries this month for the value of the specified field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

**Specified by:** getLong

in interface

TemporalAccessor
**Parameters:** field

- the field to get, not null
**Returns:** the value for the field
**Throws:** DateTimeException

- if a value for the field cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the field is not supported
**Throws:** ArithmeticException

- if numeric overflow occurs

- plus

```java
public
Month
plus​(long months)
```

Returns the month-of-year that is the specified number of months after this one.

The calculation rolls around the end of the year from December to January.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

**Parameters:** months

- the months to add, positive or negative
**Returns:** the resulting month, not null

- minus

```java
public
Month
minus​(long months)
```

Returns the month-of-year that is the specified number of months before this one.

The calculation rolls around the start of the year from January to December.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

**Parameters:** months

- the months to subtract, positive or negative
**Returns:** the resulting month, not null

- length

```java
public int length​(boolean leapYear)
```

Gets the length of this month in days.

This takes a flag to determine whether to return the length for a leap year or not.

February has 28 days in a standard year and 29 days in a leap year.
April, June, September and November have 30 days.
All other months have 31 days.

**Parameters:** leapYear

- true if the length is required for a leap year
**Returns:** the length of this month in days, from 28 to 31

- minLength

```java
public int minLength()
```

Gets the minimum length of this month in days.

February has a minimum length of 28 days.
April, June, September and November have 30 days.
All other months have 31 days.

**Returns:** the minimum length of this month in days, from 28 to 31

- maxLength

```java
public int maxLength()
```

Gets the maximum length of this month in days.

February has a maximum length of 29 days.
April, June, September and November have 30 days.
All other months have 31 days.

**Returns:** the maximum length of this month in days, from 29 to 31

- firstDayOfYear

```java
public int firstDayOfYear​(boolean leapYear)
```

Gets the day-of-year corresponding to the first day of this month.

This returns the day-of-year that this month begins on, using the leap
year flag to determine the length of February.

**Parameters:** leapYear

- true if the length is required for a leap year
**Returns:** the day of year corresponding to the first day of this month, from 1 to 336

- firstMonthOfQuarter

```java
public
Month
firstMonthOfQuarter()
```

Gets the month corresponding to the first month of this quarter.

The year can be divided into four quarters.
This method returns the first month of the quarter for the base month.
January, February and March return January.
April, May and June return April.
July, August and September return July.
October, November and December return October.

**Returns:** the first month of the quarter corresponding to this month, not null

- query

```java
public <R> R query​(
TemporalQuery
<R> query)
```

Queries this month-of-year using the specified query.

This queries this month-of-year using the specified query strategy object.
The

TemporalQuery

object defines the logic to be used to
obtain the result. Read the documentation of the query to understand
what the result of this method will be.

The result of this method is obtained by invoking the

TemporalQuery.queryFrom(TemporalAccessor)

method on the
specified query passing

this

as the argument.

**Specified by:** query

in interface

TemporalAccessor
**Type Parameters:** R

- the type of the result
**Parameters:** query

- the query to invoke, not null
**Returns:** the query result, null may be returned (defined by the query)
**Throws:** DateTimeException

- if unable to query (defined by the query)
**Throws:** ArithmeticException

- if numeric overflow occurs (defined by the query)

- adjustInto

```java
public
Temporal
adjustInto​(
Temporal
temporal)
```

Adjusts the specified temporal object to have this month-of-year.

This returns a temporal object of the same observable type as the input
with the month-of-year changed to be the same as this.

The adjustment is equivalent to using

Temporal.with(TemporalField, long)

passing

ChronoField.MONTH_OF_YEAR

as the field.
If the specified temporal object does not use the ISO calendar system then
a

DateTimeException

is thrown.

In most cases, it is clearer to reverse the calling pattern by using

Temporal.with(TemporalAdjuster)

:

```java
// these two lines are equivalent, but the second approach is recommended
temporal = thisMonth.adjustInto(temporal);
temporal = temporal.with(thisMonth);
```

For example, given a date in May, the following are output:

```java
dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later
```

This instance is immutable and unaffected by this method call.

**Specified by:** adjustInto

in interface

TemporalAdjuster
**Parameters:** temporal

- the target object to be adjusted, not null
**Returns:** the adjusted object, not null
**Throws:** DateTimeException

- if unable to make the adjustment
**Throws:** ArithmeticException

- if numeric overflow occurs

Enum Constant Detail

- JANUARY

```java
public static final
Month
JANUARY
```

The singleton instance for the month of January with 31 days.
This has the numeric value of

1

.

- FEBRUARY

```java
public static final
Month
FEBRUARY
```

The singleton instance for the month of February with 28 days, or 29 in a leap year.
This has the numeric value of

2

.

- MARCH

```java
public static final
Month
MARCH
```

The singleton instance for the month of March with 31 days.
This has the numeric value of

3

.

- APRIL

```java
public static final
Month
APRIL
```

The singleton instance for the month of April with 30 days.
This has the numeric value of

4

.

- MAY

```java
public static final
Month
MAY
```

The singleton instance for the month of May with 31 days.
This has the numeric value of

5

.

- JUNE

```java
public static final
Month
JUNE
```

The singleton instance for the month of June with 30 days.
This has the numeric value of

6

.

- JULY

```java
public static final
Month
JULY
```

The singleton instance for the month of July with 31 days.
This has the numeric value of

7

.

- AUGUST

```java
public static final
Month
AUGUST
```

The singleton instance for the month of August with 31 days.
This has the numeric value of

8

.

- SEPTEMBER

```java
public static final
Month
SEPTEMBER
```

The singleton instance for the month of September with 30 days.
This has the numeric value of

9

.

- OCTOBER

```java
public static final
Month
OCTOBER
```

The singleton instance for the month of October with 31 days.
This has the numeric value of

10

.

- NOVEMBER

```java
public static final
Month
NOVEMBER
```

The singleton instance for the month of November with 30 days.
This has the numeric value of

11

.

- DECEMBER

```java
public static final
Month
DECEMBER
```

The singleton instance for the month of December with 31 days.
This has the numeric value of

12

.

---

#### Enum Constant Detail

JANUARY

```java
public static final
Month
JANUARY
```

The singleton instance for the month of January with 31 days.
This has the numeric value of

1

.

---

#### JANUARY

public static final

Month

JANUARY

The singleton instance for the month of January with 31 days.
This has the numeric value of

1

.

FEBRUARY

```java
public static final
Month
FEBRUARY
```

The singleton instance for the month of February with 28 days, or 29 in a leap year.
This has the numeric value of

2

.

---

#### FEBRUARY

public static final

Month

FEBRUARY

The singleton instance for the month of February with 28 days, or 29 in a leap year.
This has the numeric value of

2

.

MARCH

```java
public static final
Month
MARCH
```

The singleton instance for the month of March with 31 days.
This has the numeric value of

3

.

---

#### MARCH

public static final

Month

MARCH

The singleton instance for the month of March with 31 days.
This has the numeric value of

3

.

APRIL

```java
public static final
Month
APRIL
```

The singleton instance for the month of April with 30 days.
This has the numeric value of

4

.

---

#### APRIL

public static final

Month

APRIL

The singleton instance for the month of April with 30 days.
This has the numeric value of

4

.

MAY

```java
public static final
Month
MAY
```

The singleton instance for the month of May with 31 days.
This has the numeric value of

5

.

---

#### MAY

public static final

Month

MAY

The singleton instance for the month of May with 31 days.
This has the numeric value of

5

.

JUNE

```java
public static final
Month
JUNE
```

The singleton instance for the month of June with 30 days.
This has the numeric value of

6

.

---

#### JUNE

public static final

Month

JUNE

The singleton instance for the month of June with 30 days.
This has the numeric value of

6

.

JULY

```java
public static final
Month
JULY
```

The singleton instance for the month of July with 31 days.
This has the numeric value of

7

.

---

#### JULY

public static final

Month

JULY

The singleton instance for the month of July with 31 days.
This has the numeric value of

7

.

AUGUST

```java
public static final
Month
AUGUST
```

The singleton instance for the month of August with 31 days.
This has the numeric value of

8

.

---

#### AUGUST

public static final

Month

AUGUST

The singleton instance for the month of August with 31 days.
This has the numeric value of

8

.

SEPTEMBER

```java
public static final
Month
SEPTEMBER
```

The singleton instance for the month of September with 30 days.
This has the numeric value of

9

.

---

#### SEPTEMBER

public static final

Month

SEPTEMBER

The singleton instance for the month of September with 30 days.
This has the numeric value of

9

.

OCTOBER

```java
public static final
Month
OCTOBER
```

The singleton instance for the month of October with 31 days.
This has the numeric value of

10

.

---

#### OCTOBER

public static final

Month

OCTOBER

The singleton instance for the month of October with 31 days.
This has the numeric value of

10

.

NOVEMBER

```java
public static final
Month
NOVEMBER
```

The singleton instance for the month of November with 30 days.
This has the numeric value of

11

.

---

#### NOVEMBER

public static final

Month

NOVEMBER

The singleton instance for the month of November with 30 days.
This has the numeric value of

11

.

DECEMBER

```java
public static final
Month
DECEMBER
```

The singleton instance for the month of December with 31 days.
This has the numeric value of

12

.

---

#### DECEMBER

public static final

Month

DECEMBER

The singleton instance for the month of December with 31 days.
This has the numeric value of

12

.

Method Detail

- values

```java
public static
Month
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Month c : Month.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Month
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

- of

```java
public static
Month
of​(int month)
```

Obtains an instance of

Month

from an

int

value.

Month

is an enum representing the 12 months of the year.
This factory allows the enum to be obtained from the

int

value.
The

int

value follows the ISO-8601 standard, from 1 (January) to 12 (December).

**Parameters:** month

- the month-of-year to represent, from 1 (January) to 12 (December)
**Returns:** the month-of-year, not null
**Throws:** DateTimeException

- if the month-of-year is invalid

- from

```java
public static
Month
from​(
TemporalAccessor
temporal)
```

Obtains an instance of

Month

from a temporal object.

This obtains a month based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

Month

.

The conversion extracts the

MONTH_OF_YEAR

field.
The extraction is only permitted if the temporal object has an ISO
chronology, or can be converted to a

LocalDate

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

Month::from

.

**Parameters:** temporal

- the temporal object to convert, not null
**Returns:** the month-of-year, not null
**Throws:** DateTimeException

- if unable to convert to a

Month

- getValue

```java
public int getValue()
```

Gets the month-of-year

int

value.

The values are numbered following the ISO-8601 standard,
from 1 (January) to 12 (December).

**Returns:** the month-of-year, from 1 (January) to 12 (December)

- getDisplayName

```java
public
String
getDisplayName​(
TextStyle
style,

Locale
locale)
```

Gets the textual representation, such as 'Jan' or 'December'.

This returns the textual name used to identify the month-of-year,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

**Parameters:** style

- the length of the text required, not null
**Parameters:** locale

- the locale to use, not null
**Returns:** the text value of the month-of-year, not null

- isSupported

```java
public boolean isSupported​(
TemporalField
field)
```

Checks if the specified field is supported.

This checks if this month-of-year can be queried for the specified field.
If false, then calling the

range

and

get

methods will throw an exception.

If the field is

MONTH_OF_YEAR

then
this method returns true.
All other

ChronoField

instances will return false.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.isSupportedBy(TemporalAccessor)

passing

this

as the argument.
Whether the field is supported is determined by the field.

**Specified by:** isSupported

in interface

TemporalAccessor
**Parameters:** field

- the field to check, null returns false
**Returns:** true if the field is supported on this month-of-year, false if not

- range

```java
public
ValueRange
range​(
TemporalField
field)
```

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This month is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
range of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

**Specified by:** range

in interface

TemporalAccessor
**Parameters:** field

- the field to query the range for, not null
**Returns:** the range of valid values for the field, not null
**Throws:** DateTimeException

- if the range for the field cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the field is not supported

- get

```java
public int get​(
TemporalField
field)
```

Gets the value of the specified field from this month-of-year as an

int

.

This queries this month for the value of the specified field.
The returned value will always be within the valid range of values for the field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

**Specified by:** get

in interface

TemporalAccessor
**Parameters:** field

- the field to get, not null
**Returns:** the value for the field, within the valid range of values
**Throws:** DateTimeException

- if a value for the field cannot be obtained or
the value is outside the range of valid values for the field
**Throws:** UnsupportedTemporalTypeException

- if the field is not supported or
the range of values exceeds an

int
**Throws:** ArithmeticException

- if numeric overflow occurs

- getLong

```java
public long getLong​(
TemporalField
field)
```

Gets the value of the specified field from this month-of-year as a

long

.

This queries this month for the value of the specified field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

**Specified by:** getLong

in interface

TemporalAccessor
**Parameters:** field

- the field to get, not null
**Returns:** the value for the field
**Throws:** DateTimeException

- if a value for the field cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the field is not supported
**Throws:** ArithmeticException

- if numeric overflow occurs

- plus

```java
public
Month
plus​(long months)
```

Returns the month-of-year that is the specified number of months after this one.

The calculation rolls around the end of the year from December to January.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

**Parameters:** months

- the months to add, positive or negative
**Returns:** the resulting month, not null

- minus

```java
public
Month
minus​(long months)
```

Returns the month-of-year that is the specified number of months before this one.

The calculation rolls around the start of the year from January to December.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

**Parameters:** months

- the months to subtract, positive or negative
**Returns:** the resulting month, not null

- length

```java
public int length​(boolean leapYear)
```

Gets the length of this month in days.

This takes a flag to determine whether to return the length for a leap year or not.

February has 28 days in a standard year and 29 days in a leap year.
April, June, September and November have 30 days.
All other months have 31 days.

**Parameters:** leapYear

- true if the length is required for a leap year
**Returns:** the length of this month in days, from 28 to 31

- minLength

```java
public int minLength()
```

Gets the minimum length of this month in days.

February has a minimum length of 28 days.
April, June, September and November have 30 days.
All other months have 31 days.

**Returns:** the minimum length of this month in days, from 28 to 31

- maxLength

```java
public int maxLength()
```

Gets the maximum length of this month in days.

February has a maximum length of 29 days.
April, June, September and November have 30 days.
All other months have 31 days.

**Returns:** the maximum length of this month in days, from 29 to 31

- firstDayOfYear

```java
public int firstDayOfYear​(boolean leapYear)
```

Gets the day-of-year corresponding to the first day of this month.

This returns the day-of-year that this month begins on, using the leap
year flag to determine the length of February.

**Parameters:** leapYear

- true if the length is required for a leap year
**Returns:** the day of year corresponding to the first day of this month, from 1 to 336

- firstMonthOfQuarter

```java
public
Month
firstMonthOfQuarter()
```

Gets the month corresponding to the first month of this quarter.

The year can be divided into four quarters.
This method returns the first month of the quarter for the base month.
January, February and March return January.
April, May and June return April.
July, August and September return July.
October, November and December return October.

**Returns:** the first month of the quarter corresponding to this month, not null

- query

```java
public <R> R query​(
TemporalQuery
<R> query)
```

Queries this month-of-year using the specified query.

This queries this month-of-year using the specified query strategy object.
The

TemporalQuery

object defines the logic to be used to
obtain the result. Read the documentation of the query to understand
what the result of this method will be.

The result of this method is obtained by invoking the

TemporalQuery.queryFrom(TemporalAccessor)

method on the
specified query passing

this

as the argument.

**Specified by:** query

in interface

TemporalAccessor
**Type Parameters:** R

- the type of the result
**Parameters:** query

- the query to invoke, not null
**Returns:** the query result, null may be returned (defined by the query)
**Throws:** DateTimeException

- if unable to query (defined by the query)
**Throws:** ArithmeticException

- if numeric overflow occurs (defined by the query)

- adjustInto

```java
public
Temporal
adjustInto​(
Temporal
temporal)
```

Adjusts the specified temporal object to have this month-of-year.

This returns a temporal object of the same observable type as the input
with the month-of-year changed to be the same as this.

The adjustment is equivalent to using

Temporal.with(TemporalField, long)

passing

ChronoField.MONTH_OF_YEAR

as the field.
If the specified temporal object does not use the ISO calendar system then
a

DateTimeException

is thrown.

In most cases, it is clearer to reverse the calling pattern by using

Temporal.with(TemporalAdjuster)

:

```java
// these two lines are equivalent, but the second approach is recommended
temporal = thisMonth.adjustInto(temporal);
temporal = temporal.with(thisMonth);
```

For example, given a date in May, the following are output:

```java
dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later
```

This instance is immutable and unaffected by this method call.

**Specified by:** adjustInto

in interface

TemporalAdjuster
**Parameters:** temporal

- the target object to be adjusted, not null
**Returns:** the adjusted object, not null
**Throws:** DateTimeException

- if unable to make the adjustment
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### Method Detail

values

```java
public static
Month
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Month c : Month.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Month

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Month c : Month.values())
System.out.println(c);
```

for (Month c : Month.values())
System.out.println(c);

valueOf

```java
public static
Month
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

Month

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

of

```java
public static
Month
of​(int month)
```

Obtains an instance of

Month

from an

int

value.

Month

is an enum representing the 12 months of the year.
This factory allows the enum to be obtained from the

int

value.
The

int

value follows the ISO-8601 standard, from 1 (January) to 12 (December).

**Parameters:** month

- the month-of-year to represent, from 1 (January) to 12 (December)
**Returns:** the month-of-year, not null
**Throws:** DateTimeException

- if the month-of-year is invalid

---

#### of

public static

Month

of​(int month)

Obtains an instance of

Month

from an

int

value.

Month

is an enum representing the 12 months of the year.
This factory allows the enum to be obtained from the

int

value.
The

int

value follows the ISO-8601 standard, from 1 (January) to 12 (December).

Month

is an enum representing the 12 months of the year.
This factory allows the enum to be obtained from the

int

value.
The

int

value follows the ISO-8601 standard, from 1 (January) to 12 (December).

from

```java
public static
Month
from​(
TemporalAccessor
temporal)
```

Obtains an instance of

Month

from a temporal object.

This obtains a month based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

Month

.

The conversion extracts the

MONTH_OF_YEAR

field.
The extraction is only permitted if the temporal object has an ISO
chronology, or can be converted to a

LocalDate

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

Month::from

.

**Parameters:** temporal

- the temporal object to convert, not null
**Returns:** the month-of-year, not null
**Throws:** DateTimeException

- if unable to convert to a

Month

---

#### from

public static

Month

from​(

TemporalAccessor

temporal)

Obtains an instance of

Month

from a temporal object.

This obtains a month based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

Month

.

The conversion extracts the

MONTH_OF_YEAR

field.
The extraction is only permitted if the temporal object has an ISO
chronology, or can be converted to a

LocalDate

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

Month::from

.

This obtains a month based on the specified temporal.
A

TemporalAccessor

represents an arbitrary set of date and time information,
which this factory converts to an instance of

Month

.

The conversion extracts the

MONTH_OF_YEAR

field.
The extraction is only permitted if the temporal object has an ISO
chronology, or can be converted to a

LocalDate

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

Month::from

.

The conversion extracts the

MONTH_OF_YEAR

field.
The extraction is only permitted if the temporal object has an ISO
chronology, or can be converted to a

LocalDate

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

Month::from

.

This method matches the signature of the functional interface

TemporalQuery

allowing it to be used as a query via method reference,

Month::from

.

getValue

```java
public int getValue()
```

Gets the month-of-year

int

value.

The values are numbered following the ISO-8601 standard,
from 1 (January) to 12 (December).

**Returns:** the month-of-year, from 1 (January) to 12 (December)

---

#### getValue

public int getValue()

Gets the month-of-year

int

value.

The values are numbered following the ISO-8601 standard,
from 1 (January) to 12 (December).

The values are numbered following the ISO-8601 standard,
from 1 (January) to 12 (December).

getDisplayName

```java
public
String
getDisplayName​(
TextStyle
style,

Locale
locale)
```

Gets the textual representation, such as 'Jan' or 'December'.

This returns the textual name used to identify the month-of-year,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

**Parameters:** style

- the length of the text required, not null
**Parameters:** locale

- the locale to use, not null
**Returns:** the text value of the month-of-year, not null

---

#### getDisplayName

public

String

getDisplayName​(

TextStyle

style,

Locale

locale)

Gets the textual representation, such as 'Jan' or 'December'.

This returns the textual name used to identify the month-of-year,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

This returns the textual name used to identify the month-of-year,
suitable for presentation to the user.
The parameters control the style of the returned text and the locale.

If no textual mapping is found then the

numeric value

is returned.

If no textual mapping is found then the

numeric value

is returned.

isSupported

```java
public boolean isSupported​(
TemporalField
field)
```

Checks if the specified field is supported.

This checks if this month-of-year can be queried for the specified field.
If false, then calling the

range

and

get

methods will throw an exception.

If the field is

MONTH_OF_YEAR

then
this method returns true.
All other

ChronoField

instances will return false.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.isSupportedBy(TemporalAccessor)

passing

this

as the argument.
Whether the field is supported is determined by the field.

**Specified by:** isSupported

in interface

TemporalAccessor
**Parameters:** field

- the field to check, null returns false
**Returns:** true if the field is supported on this month-of-year, false if not

---

#### isSupported

public boolean isSupported​(

TemporalField

field)

Checks if the specified field is supported.

This checks if this month-of-year can be queried for the specified field.
If false, then calling the

range

and

get

methods will throw an exception.

If the field is

MONTH_OF_YEAR

then
this method returns true.
All other

ChronoField

instances will return false.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.isSupportedBy(TemporalAccessor)

passing

this

as the argument.
Whether the field is supported is determined by the field.

This checks if this month-of-year can be queried for the specified field.
If false, then calling the

range

and

get

methods will throw an exception.

If the field is

MONTH_OF_YEAR

then
this method returns true.
All other

ChronoField

instances will return false.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.isSupportedBy(TemporalAccessor)

passing

this

as the argument.
Whether the field is supported is determined by the field.

If the field is

MONTH_OF_YEAR

then
this method returns true.
All other

ChronoField

instances will return false.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.isSupportedBy(TemporalAccessor)

passing

this

as the argument.
Whether the field is supported is determined by the field.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.isSupportedBy(TemporalAccessor)

passing

this

as the argument.
Whether the field is supported is determined by the field.

range

```java
public
ValueRange
range​(
TemporalField
field)
```

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This month is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
range of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

**Specified by:** range

in interface

TemporalAccessor
**Parameters:** field

- the field to query the range for, not null
**Returns:** the range of valid values for the field, not null
**Throws:** DateTimeException

- if the range for the field cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the field is not supported

---

#### range

public

ValueRange

range​(

TemporalField

field)

Gets the range of valid values for the specified field.

The range object expresses the minimum and maximum valid values for a field.
This month is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
range of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

The range object expresses the minimum and maximum valid values for a field.
This month is used to enhance the accuracy of the returned range.
If it is not possible to return the range, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
range of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

If the field is

MONTH_OF_YEAR

then the
range of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.rangeRefinedBy(TemporalAccessor)

passing

this

as the argument.
Whether the range can be obtained is determined by the field.

get

```java
public int get​(
TemporalField
field)
```

Gets the value of the specified field from this month-of-year as an

int

.

This queries this month for the value of the specified field.
The returned value will always be within the valid range of values for the field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

**Specified by:** get

in interface

TemporalAccessor
**Parameters:** field

- the field to get, not null
**Returns:** the value for the field, within the valid range of values
**Throws:** DateTimeException

- if a value for the field cannot be obtained or
the value is outside the range of valid values for the field
**Throws:** UnsupportedTemporalTypeException

- if the field is not supported or
the range of values exceeds an

int
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### get

public int get​(

TemporalField

field)

Gets the value of the specified field from this month-of-year as an

int

.

This queries this month for the value of the specified field.
The returned value will always be within the valid range of values for the field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

This queries this month for the value of the specified field.
The returned value will always be within the valid range of values for the field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

getLong

```java
public long getLong​(
TemporalField
field)
```

Gets the value of the specified field from this month-of-year as a

long

.

This queries this month for the value of the specified field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

**Specified by:** getLong

in interface

TemporalAccessor
**Parameters:** field

- the field to get, not null
**Returns:** the value for the field
**Throws:** DateTimeException

- if a value for the field cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the field is not supported
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### getLong

public long getLong​(

TemporalField

field)

Gets the value of the specified field from this month-of-year as a

long

.

This queries this month for the value of the specified field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

This queries this month for the value of the specified field.
If it is not possible to return the value, because the field is not supported
or for some other reason, an exception is thrown.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

If the field is

MONTH_OF_YEAR

then the
value of the month-of-year, from 1 to 12, will be returned.
All other

ChronoField

instances will throw an

UnsupportedTemporalTypeException

.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

If the field is not a

ChronoField

, then the result of this method
is obtained by invoking

TemporalField.getFrom(TemporalAccessor)

passing

this

as the argument. Whether the value can be obtained,
and what the value represents, is determined by the field.

plus

```java
public
Month
plus​(long months)
```

Returns the month-of-year that is the specified number of months after this one.

The calculation rolls around the end of the year from December to January.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

**Parameters:** months

- the months to add, positive or negative
**Returns:** the resulting month, not null

---

#### plus

public

Month

plus​(long months)

Returns the month-of-year that is the specified number of months after this one.

The calculation rolls around the end of the year from December to January.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

The calculation rolls around the end of the year from December to January.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

minus

```java
public
Month
minus​(long months)
```

Returns the month-of-year that is the specified number of months before this one.

The calculation rolls around the start of the year from January to December.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

**Parameters:** months

- the months to subtract, positive or negative
**Returns:** the resulting month, not null

---

#### minus

public

Month

minus​(long months)

Returns the month-of-year that is the specified number of months before this one.

The calculation rolls around the start of the year from January to December.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

The calculation rolls around the start of the year from January to December.
The specified period may be negative.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

length

```java
public int length​(boolean leapYear)
```

Gets the length of this month in days.

This takes a flag to determine whether to return the length for a leap year or not.

February has 28 days in a standard year and 29 days in a leap year.
April, June, September and November have 30 days.
All other months have 31 days.

**Parameters:** leapYear

- true if the length is required for a leap year
**Returns:** the length of this month in days, from 28 to 31

---

#### length

public int length​(boolean leapYear)

Gets the length of this month in days.

This takes a flag to determine whether to return the length for a leap year or not.

February has 28 days in a standard year and 29 days in a leap year.
April, June, September and November have 30 days.
All other months have 31 days.

This takes a flag to determine whether to return the length for a leap year or not.

February has 28 days in a standard year and 29 days in a leap year.
April, June, September and November have 30 days.
All other months have 31 days.

February has 28 days in a standard year and 29 days in a leap year.
April, June, September and November have 30 days.
All other months have 31 days.

minLength

```java
public int minLength()
```

Gets the minimum length of this month in days.

February has a minimum length of 28 days.
April, June, September and November have 30 days.
All other months have 31 days.

**Returns:** the minimum length of this month in days, from 28 to 31

---

#### minLength

public int minLength()

Gets the minimum length of this month in days.

February has a minimum length of 28 days.
April, June, September and November have 30 days.
All other months have 31 days.

February has a minimum length of 28 days.
April, June, September and November have 30 days.
All other months have 31 days.

maxLength

```java
public int maxLength()
```

Gets the maximum length of this month in days.

February has a maximum length of 29 days.
April, June, September and November have 30 days.
All other months have 31 days.

**Returns:** the maximum length of this month in days, from 29 to 31

---

#### maxLength

public int maxLength()

Gets the maximum length of this month in days.

February has a maximum length of 29 days.
April, June, September and November have 30 days.
All other months have 31 days.

February has a maximum length of 29 days.
April, June, September and November have 30 days.
All other months have 31 days.

firstDayOfYear

```java
public int firstDayOfYear​(boolean leapYear)
```

Gets the day-of-year corresponding to the first day of this month.

This returns the day-of-year that this month begins on, using the leap
year flag to determine the length of February.

**Parameters:** leapYear

- true if the length is required for a leap year
**Returns:** the day of year corresponding to the first day of this month, from 1 to 336

---

#### firstDayOfYear

public int firstDayOfYear​(boolean leapYear)

Gets the day-of-year corresponding to the first day of this month.

This returns the day-of-year that this month begins on, using the leap
year flag to determine the length of February.

This returns the day-of-year that this month begins on, using the leap
year flag to determine the length of February.

firstMonthOfQuarter

```java
public
Month
firstMonthOfQuarter()
```

Gets the month corresponding to the first month of this quarter.

The year can be divided into four quarters.
This method returns the first month of the quarter for the base month.
January, February and March return January.
April, May and June return April.
July, August and September return July.
October, November and December return October.

**Returns:** the first month of the quarter corresponding to this month, not null

---

#### firstMonthOfQuarter

public

Month

firstMonthOfQuarter()

Gets the month corresponding to the first month of this quarter.

The year can be divided into four quarters.
This method returns the first month of the quarter for the base month.
January, February and March return January.
April, May and June return April.
July, August and September return July.
October, November and December return October.

The year can be divided into four quarters.
This method returns the first month of the quarter for the base month.
January, February and March return January.
April, May and June return April.
July, August and September return July.
October, November and December return October.

query

```java
public <R> R query​(
TemporalQuery
<R> query)
```

Queries this month-of-year using the specified query.

This queries this month-of-year using the specified query strategy object.
The

TemporalQuery

object defines the logic to be used to
obtain the result. Read the documentation of the query to understand
what the result of this method will be.

The result of this method is obtained by invoking the

TemporalQuery.queryFrom(TemporalAccessor)

method on the
specified query passing

this

as the argument.

**Specified by:** query

in interface

TemporalAccessor
**Type Parameters:** R

- the type of the result
**Parameters:** query

- the query to invoke, not null
**Returns:** the query result, null may be returned (defined by the query)
**Throws:** DateTimeException

- if unable to query (defined by the query)
**Throws:** ArithmeticException

- if numeric overflow occurs (defined by the query)

---

#### query

public <R> R query​(

TemporalQuery

<R> query)

Queries this month-of-year using the specified query.

This queries this month-of-year using the specified query strategy object.
The

TemporalQuery

object defines the logic to be used to
obtain the result. Read the documentation of the query to understand
what the result of this method will be.

The result of this method is obtained by invoking the

TemporalQuery.queryFrom(TemporalAccessor)

method on the
specified query passing

this

as the argument.

This queries this month-of-year using the specified query strategy object.
The

TemporalQuery

object defines the logic to be used to
obtain the result. Read the documentation of the query to understand
what the result of this method will be.

The result of this method is obtained by invoking the

TemporalQuery.queryFrom(TemporalAccessor)

method on the
specified query passing

this

as the argument.

The result of this method is obtained by invoking the

TemporalQuery.queryFrom(TemporalAccessor)

method on the
specified query passing

this

as the argument.

adjustInto

```java
public
Temporal
adjustInto​(
Temporal
temporal)
```

Adjusts the specified temporal object to have this month-of-year.

This returns a temporal object of the same observable type as the input
with the month-of-year changed to be the same as this.

The adjustment is equivalent to using

Temporal.with(TemporalField, long)

passing

ChronoField.MONTH_OF_YEAR

as the field.
If the specified temporal object does not use the ISO calendar system then
a

DateTimeException

is thrown.

In most cases, it is clearer to reverse the calling pattern by using

Temporal.with(TemporalAdjuster)

:

```java
// these two lines are equivalent, but the second approach is recommended
temporal = thisMonth.adjustInto(temporal);
temporal = temporal.with(thisMonth);
```

For example, given a date in May, the following are output:

```java
dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later
```

This instance is immutable and unaffected by this method call.

**Specified by:** adjustInto

in interface

TemporalAdjuster
**Parameters:** temporal

- the target object to be adjusted, not null
**Returns:** the adjusted object, not null
**Throws:** DateTimeException

- if unable to make the adjustment
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### adjustInto

public

Temporal

adjustInto​(

Temporal

temporal)

Adjusts the specified temporal object to have this month-of-year.

This returns a temporal object of the same observable type as the input
with the month-of-year changed to be the same as this.

The adjustment is equivalent to using

Temporal.with(TemporalField, long)

passing

ChronoField.MONTH_OF_YEAR

as the field.
If the specified temporal object does not use the ISO calendar system then
a

DateTimeException

is thrown.

In most cases, it is clearer to reverse the calling pattern by using

Temporal.with(TemporalAdjuster)

:

```java
// these two lines are equivalent, but the second approach is recommended
temporal = thisMonth.adjustInto(temporal);
temporal = temporal.with(thisMonth);
```

For example, given a date in May, the following are output:

```java
dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later
```

This instance is immutable and unaffected by this method call.

This returns a temporal object of the same observable type as the input
with the month-of-year changed to be the same as this.

The adjustment is equivalent to using

Temporal.with(TemporalField, long)

passing

ChronoField.MONTH_OF_YEAR

as the field.
If the specified temporal object does not use the ISO calendar system then
a

DateTimeException

is thrown.

In most cases, it is clearer to reverse the calling pattern by using

Temporal.with(TemporalAdjuster)

:

```java
// these two lines are equivalent, but the second approach is recommended
temporal = thisMonth.adjustInto(temporal);
temporal = temporal.with(thisMonth);
```

For example, given a date in May, the following are output:

```java
dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later
```

This instance is immutable and unaffected by this method call.

The adjustment is equivalent to using

Temporal.with(TemporalField, long)

passing

ChronoField.MONTH_OF_YEAR

as the field.
If the specified temporal object does not use the ISO calendar system then
a

DateTimeException

is thrown.

In most cases, it is clearer to reverse the calling pattern by using

Temporal.with(TemporalAdjuster)

:

```java
// these two lines are equivalent, but the second approach is recommended
temporal = thisMonth.adjustInto(temporal);
temporal = temporal.with(thisMonth);
```

For example, given a date in May, the following are output:

```java
dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later
```

This instance is immutable and unaffected by this method call.

In most cases, it is clearer to reverse the calling pattern by using

Temporal.with(TemporalAdjuster)

:

```java
// these two lines are equivalent, but the second approach is recommended
temporal = thisMonth.adjustInto(temporal);
temporal = temporal.with(thisMonth);
```

For example, given a date in May, the following are output:

```java
dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later
```

This instance is immutable and unaffected by this method call.

// these two lines are equivalent, but the second approach is recommended
temporal = thisMonth.adjustInto(temporal);
temporal = temporal.with(thisMonth);

For example, given a date in May, the following are output:

```java
dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later
```

This instance is immutable and unaffected by this method call.

dateInMay.with(JANUARY); // four months earlier
dateInMay.with(APRIL); // one months earlier
dateInMay.with(MAY); // same date
dateInMay.with(JUNE); // one month later
dateInMay.with(DECEMBER); // seven months later

This instance is immutable and unaffected by this method call.

---

