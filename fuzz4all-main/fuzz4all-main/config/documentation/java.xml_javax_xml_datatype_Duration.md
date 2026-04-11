# Class Duration

**Source:** `java.xml\javax\xml\datatype\Duration.html`

### Class Description

```java
public abstract class
Duration

extends
Object
```

Immutable representation of a time span as defined in
the W3C XML Schema 1.0 specification.

A Duration object represents a period of Gregorian time,
which consists of six fields (years, months, days, hours,
minutes, and seconds) plus a sign (+/-) field.

The first five fields have non-negative (>=0) integers or null
(which represents that the field is not set),
and the seconds field has a non-negative decimal or null.
A negative sign indicates a negative duration.

This class provides a number of methods that make it easy
to use for the duration datatype of XML Schema 1.0 with
the errata.

Order relationship

Duration objects only have partial order, where two values A and B
maybe either:

- A<B (A is shorter than B)

A>B (A is longer than B)

A==B (A and B are of the same duration)

A<>B (Comparison between A and B is indeterminate)

For example, 30 days cannot be meaningfully compared to one month.
The

compare(Duration duration)

method implements this
relationship.

See the

isLongerThan(Duration)

method for details about
the order relationship among

Duration

objects.

Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

**Since:** 1.5
**See Also:** XMLGregorianCalendar.add(Duration)

---

### Field Details

*No entries found.*

### Constructor Details

#### public Duration()

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

Duration

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

---

### Method Details

#### public
QName
getXMLSchemaType()

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set,
i.e.

isSet(DatatypeConstants.Field field)

==

true

.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DURATION

X

X

X

X

X

X

DatatypeConstants.DURATION_DAYTIME

X

X

X

X

DatatypeConstants.DURATION_YEARMONTH

X

X

**Returns:**
- one of the following constants:

DatatypeConstants.DURATION

,

DatatypeConstants.DURATION_DAYTIME

or

DatatypeConstants.DURATION_YEARMONTH

.

**Throws:**
- IllegalStateException

- If the combination of set fields does not match one of the XML Schema date/time datatypes.

---

#### public abstract int getSign()

Returns the sign of this duration in -1,0, or 1.

**Returns:**
- -1 if this duration is negative, 0 if the duration is zero,
and 1 if the duration is positive.

---

#### public int getYears()

Get the years value of this

Duration

as an

int

or

0

if not present.

getYears()

is a convenience method for

getField(DatatypeConstants.YEARS)

.

As the return value is an

int

, an incorrect value will be returned for

Duration

s
with years that go beyond the range of an

int

.
Use

getField(DatatypeConstants.YEARS)

to avoid possible loss of precision.

**Returns:**
- If the years field is present, return its value as an

int

, else return

0

.

---

#### public int getMonths()

Obtains the value of the MONTHS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MONTHS field.

**Returns:**
- Months of this

Duration

.

---

#### public int getDays()

Obtains the value of the DAYS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the DAYS field.

**Returns:**
- Days of this

Duration

.

---

#### public int getHours()

Obtains the value of the HOURS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the HOURS field.

**Returns:**
- Hours of this

Duration

.

---

#### public int getMinutes()

Obtains the value of the MINUTES field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MINUTES field.

**Returns:**
- Minutes of this

Duration

.

---

#### public int getSeconds()

Obtains the value of the SECONDS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the SECONDS field.

**Returns:**
- seconds in the integer value. The fraction of seconds
will be discarded (for example, if the actual value is 2.5,
this method returns 2)

---

#### public long getTimeInMillis​(
Calendar
startInstant)

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any Calendar value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Calendar)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Calendar)

method for details.

**Parameters:**
- startInstant

- The length of a month/year varies. The

startInstant

is
used to disambiguate this variance. Specifically, this method
returns the difference between

startInstant

and

startInstant+duration

**Returns:**
- milliseconds between

startInstant

and

startInstant

plus this

Duration

**Throws:**
- NullPointerException

- if

startInstant

parameter
is null.

---

#### public long getTimeInMillis​(
Date
startInstant)

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any

Date

value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Date)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Date)

method for details.

**Parameters:**
- startInstant

- The length of a month/year varies. The

startInstant

is
used to disambiguate this variance. Specifically, this method
returns the difference between

startInstant

and

startInstant+duration

.

**Returns:**
- milliseconds between

startInstant

and

startInstant

plus this

Duration

**Throws:**
- NullPointerException

- If the startInstant parameter is null.

**See Also:**
- getTimeInMillis(Calendar)

---

#### public abstract
Number
getField​(
DatatypeConstants.Field
field)

Gets the value of a field.

Fields of a duration object may contain arbitrary large value.
Therefore this method is designed to return a

Number

object.

In case of YEARS, MONTHS, DAYS, HOURS, and MINUTES, the returned
number will be a non-negative integer. In case of seconds,
the returned number may be a non-negative decimal value.

**Parameters:**
- field

- one of the six Field constants (YEARS,MONTHS,DAYS,HOURS,
MINUTES, or SECONDS.)

**Returns:**
- If the specified field is present, this method returns
a non-null non-negative

Number

object that
represents its value. If it is not present, return null.
For YEARS, MONTHS, DAYS, HOURS, and MINUTES, this method
returns a

BigInteger

object. For SECONDS, this
method returns a

BigDecimal

.

**Throws:**
- NullPointerException

- If the

field

is

null

.

---

#### public abstract boolean isSet​(
DatatypeConstants.Field
field)

Checks if a field is set.

A field of a duration object may or may not be present.
This method can be used to test if a field is present.

**Parameters:**
- field

- one of the six Field constants (YEARS,MONTHS,DAYS,HOURS,
MINUTES, or SECONDS.)

**Returns:**
- true if the field is present. false if not.

**Throws:**
- NullPointerException

- If the field parameter is null.

---

#### public abstract
Duration
add​(
Duration
rhs)

Computes a new duration whose value is

this+rhs

.

For example,

```java
"1 day" + "-3 days" = "-2 days"
"1 year" + "1 day" = "1 year and 1 day"
"-(1 hour,50 minutes)" + "-20 minutes" = "-(1 hours,70 minutes)"
"15 hours" + "-3 days" = "-(2 days,9 hours)"
"1 year" + "-1 day" = IllegalStateException
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally, the computation is defined as follows.

Firstly, we can assume that two

Duration

s to be added
are both positive without losing generality (i.e.,

(-X)+Y=Y-X

,

X+(-Y)=X-Y

,

(-X)+(-Y)=-(X+Y)

)

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

**Parameters:**
- rhs

-

Duration

to add to this

Duration

**Returns:**
- non-null valid Duration object.

**Throws:**
- NullPointerException

- If the rhs parameter is null.
- IllegalStateException

- If two durations cannot be meaningfully added. For
example, adding negative one day to one month causes
this exception.

**See Also:**
- subtract(Duration)

---

#### public abstract void addTo​(
Calendar
calendar)

Adds this duration to a

Calendar

object.

Calls

Calendar.add(int,int)

in the
order of YEARS, MONTHS, DAYS, HOURS, MINUTES, SECONDS, and MILLISECONDS
if those fields are present. Because the

Calendar

class
uses int to hold values, there are cases where this method
won't work correctly (for example if values of fields
exceed the range of int.)

Also, since this duration class is a Gregorian duration, this
method will not work correctly if the given

Calendar

object is based on some other calendar systems.

Any fractional parts of this

Duration

object
beyond milliseconds will be simply ignored. For example, if
this duration is "P1.23456S", then 1 is added to SECONDS,
234 is added to MILLISECONDS, and the rest will be unused.

Note that because

Calendar.add(int, int)

is using

int

,

Duration

with values beyond the
range of

int

in its fields
will cause overflow/underflow to the given

Calendar

.

XMLGregorianCalendar.add(Duration)

provides the same
basic operation as this method while avoiding
the overflow/underflow issues.

**Parameters:**
- calendar

- A calendar object whose value will be modified.

**Throws:**
- NullPointerException

- if the calendar parameter is null.

---

#### public void addTo​(
Date
date)

Adds this duration to a

Date

object.

The given date is first converted into
a

GregorianCalendar

, then the duration
is added exactly like the

addTo(Calendar)

method.

The updated time instant is then converted back into a

Date

object and used to update the given

Date

object.

This somewhat redundant computation is necessary to unambiguously
determine the duration of months and years.

**Parameters:**
- date

- A date object whose value will be modified.

**Throws:**
- NullPointerException

- if the date parameter is null.

---

#### public
Duration
subtract​(
Duration
rhs)

Computes a new duration whose value is

this-rhs

.

For example:

```java
"1 day" - "-3 days" = "4 days"
"1 year" - "1 day" = IllegalStateException
"-(1 hour,50 minutes)" - "-20 minutes" = "-(1hours,30 minutes)"
"15 hours" - "-3 days" = "3 days and 15 hours"
"1 year" - "-1 day" = "1 year and 1 day"
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally the computation is defined as follows.
First, we can assume that two

Duration

s are both positive
without losing generality. (i.e.,

(-X)-Y=-(X+Y)

,

X-(-Y)=X+Y

,

(-X)-(-Y)=-(X-Y)

)

Then two durations are subtracted field by field.
If the sign of any non-zero field

F

is different from
the sign of the most significant field,
1 (if

F

is negative) or -1 (otherwise)
will be borrowed from the next bigger unit of

F

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

**Parameters:**
- rhs

-

Duration

to subtract from this

Duration

.

**Returns:**
- New

Duration

created from subtracting

rhs

from this

Duration

.

**Throws:**
- IllegalStateException

- If two durations cannot be meaningfully subtracted. For
example, subtracting one day from one month causes
this exception.
- NullPointerException

- If the rhs parameter is null.

**See Also:**
- add(Duration)

---

#### public
Duration
multiply​(int factor)

Computes a new duration whose value is

factor

times
longer than the value of this duration.

This method is provided for the convenience.
It is functionally equivalent to the following code:

```java
multiply(new BigDecimal(String.valueOf(factor)))
```

**Parameters:**
- factor

- Factor times longer of new

Duration

to create.

**Returns:**
- New

Duration

that is

factor

times longer than this

Duration

.

**See Also:**
- multiply(BigDecimal)

---

#### public abstract
Duration
multiply​(
BigDecimal
factor)

Computes a new duration whose value is

factor

times
longer than the value of this duration.

For example,

```java
"P1M" (1 month) * "12" = "P12M" (12 months)
"PT1M" (1 min) * "0.3" = "PT18S" (18 seconds)
"P1M" (1 month) * "1.5" = IllegalStateException
```

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

The operation will be performed field by field with the precision
of

BigDecimal

. Since all the fields except seconds are
restricted to hold integers,
any fraction produced by the computation will be
carried down toward the next lower unit. For example,
if you multiply "P1D" (1 day) with "0.5", then it will be 0.5 day,
which will be carried down to "PT12H" (12 hours).
When fractions of month cannot be meaningfully carried down
to days, or year to months, this will cause an

IllegalStateException

to be thrown.
For example if you multiple one month by 0.5.

To avoid

IllegalStateException

, use
the

normalizeWith(Calendar)

method to remove the years
and months fields.

**Parameters:**
- factor

- to multiply by

**Returns:**
- returns a non-null valid

Duration

object

**Throws:**
- IllegalStateException

- if operation produces fraction in
the months field.
- NullPointerException

- if the

factor

parameter is

null

.

---

#### public abstract
Duration
negate()

Returns a new

Duration

object whose
value is

-this

.

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

**Returns:**
- always return a non-null valid

Duration

object.

---

#### public abstract
Duration
normalizeWith​(
Calendar
startTimeInstant)

Converts the years and months fields into the days field
by using a specific time instant as the reference point.

For example, duration of one month normalizes to 31 days
given the start time instance "July 8th 2003, 17:40:32".

Formally, the computation is done as follows:

- the given Calendar object is cloned
- the years, months and days fields will be added to the

Calendar

object
by using the

Calendar.add(int,int)

method
- the difference between the two Calendars in computed in milliseconds and converted to days,
if a remainder occurs due to Daylight Savings Time, it is discarded
- the computed days, along with the hours, minutes and seconds
fields of this duration object is used to construct a new
Duration object.

Note that since the Calendar class uses

int

to
hold the value of year and month, this method may produce
an unexpected result if this duration object holds
a very large value in the years or months fields.

**Parameters:**
- startTimeInstant

-

Calendar

reference point.

**Returns:**
- Duration

of years and months of this

Duration

as days.

**Throws:**
- NullPointerException

- If the startTimeInstant parameter is null.

---

#### public abstract int compare​(
Duration
duration)

Partial order relation comparison with this

Duration

instance.

Comparison result must be in accordance with

W3C XML Schema 1.0 Part 2, Section 3.2.7.6.2,

Order relation on duration

.

Return:

- DatatypeConstants.LESSER

if this

Duration

is shorter than

duration

parameter
- DatatypeConstants.EQUAL

if this

Duration

is equal to

duration

parameter
- DatatypeConstants.GREATER

if this

Duration

is longer than

duration

parameter
- DatatypeConstants.INDETERMINATE

if a conclusive partial order relation cannot be determined

**Parameters:**
- duration

- to compare

**Returns:**
- the relationship between

this Duration

and

duration

parameter as

DatatypeConstants.LESSER

,

DatatypeConstants.EQUAL

,

DatatypeConstants.GREATER

or

DatatypeConstants.INDETERMINATE

.

**Throws:**
- UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
- NullPointerException

- if

duration

is

null

.

**See Also:**
- isShorterThan(Duration)

,

isLongerThan(Duration)

---

#### public boolean isLongerThan​(
Duration
duration)

Checks if this duration object is strictly longer than
another

Duration

object.

Duration X is "longer" than Y if and only if X > Y
as defined in the section 3.2.6.2 of the XML Schema 1.0
specification.

For example, "P1D" (one day) > "PT12H" (12 hours) and
"P2Y" (two years) > "P23M" (23 months).

**Parameters:**
- duration

-

Duration

to test this

Duration

against.

**Returns:**
- true if the duration represented by this object
is longer than the given duration. false otherwise.

**Throws:**
- UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
- NullPointerException

- If

duration

is null.

**See Also:**
- isShorterThan(Duration)

,

compare(Duration duration)

---

#### public boolean isShorterThan​(
Duration
duration)

Checks if this duration object is strictly shorter than
another

Duration

object.

**Parameters:**
- duration

-

Duration

to test this

Duration

against.

**Returns:**
- true

if

duration

parameter is shorter than this

Duration

,
else

false

.

**Throws:**
- UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
- NullPointerException

- if

duration

is null.

**See Also:**
- isLongerThan(Duration duration)

,

compare(Duration duration)

---

#### public boolean equals​(
Object
duration)

Checks if this duration object has the same duration
as another

Duration

object.

For example, "P1D" (1 day) is equal to "PT24H" (24 hours).

Duration X is equal to Y if and only if time instant
t+X and t+Y are the same for all the test time instants
specified in the section 3.2.6.2 of the XML Schema 1.0
specification.

Note that there are cases where two

Duration

s are
"incomparable" to each other, like one month and 30 days.
For example,

```java
!new Duration("P1M").isShorterThan(new Duration("P30D"))
!new Duration("P1M").isLongerThan(new Duration("P30D"))
!new Duration("P1M").equals(new Duration("P30D"))
```

**Overrides:**
- equals

in class

Object

**Parameters:**
- duration

- The object to compare this

Duration

against.

**Returns:**
- true

if this duration is the same length as

duration

.

false

if

duration

is

null

,
is not a

Duration

object,
or its length is different from this duration.

**Throws:**
- UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.

**See Also:**
- compare(Duration duration)

---

#### public abstract int hashCode()

Returns a hash code consistent with the definition of the equals method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.hashCode()

---

#### public
String
toString()

Returns a

String

representation of this

Duration Object

.

The result is formatted according to the XML Schema 1.0 spec
and can be always parsed back later into the
equivalent

Duration Object

by

DatatypeFactory.newDuration(String lexicalRepresentation)

.

Formally, the following holds for any

Duration

Object

x:

```java
new Duration(x.toString()).equals(x)
```

**Overrides:**
- toString

in class

Object

**Returns:**
- A non-

null

valid

String

representation of this

Duration

.

---

### Additional Sections

#### Class Duration

java.lang.Object

- javax.xml.datatype.Duration

javax.xml.datatype.Duration

```java
public abstract class
Duration

extends
Object
```

Immutable representation of a time span as defined in
the W3C XML Schema 1.0 specification.

A Duration object represents a period of Gregorian time,
which consists of six fields (years, months, days, hours,
minutes, and seconds) plus a sign (+/-) field.

The first five fields have non-negative (>=0) integers or null
(which represents that the field is not set),
and the seconds field has a non-negative decimal or null.
A negative sign indicates a negative duration.

This class provides a number of methods that make it easy
to use for the duration datatype of XML Schema 1.0 with
the errata.

Order relationship

Duration objects only have partial order, where two values A and B
maybe either:

- A<B (A is shorter than B)

A>B (A is longer than B)

A==B (A and B are of the same duration)

A<>B (Comparison between A and B is indeterminate)

For example, 30 days cannot be meaningfully compared to one month.
The

compare(Duration duration)

method implements this
relationship.

See the

isLongerThan(Duration)

method for details about
the order relationship among

Duration

objects.

Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

**Since:** 1.5
**See Also:** XMLGregorianCalendar.add(Duration)

public abstract class

Duration

extends

Object

Immutable representation of a time span as defined in
the W3C XML Schema 1.0 specification.

A Duration object represents a period of Gregorian time,
which consists of six fields (years, months, days, hours,
minutes, and seconds) plus a sign (+/-) field.

The first five fields have non-negative (>=0) integers or null
(which represents that the field is not set),
and the seconds field has a non-negative decimal or null.
A negative sign indicates a negative duration.

This class provides a number of methods that make it easy
to use for the duration datatype of XML Schema 1.0 with
the errata.

Order relationship

Duration objects only have partial order, where two values A and B
maybe either:

- A<B (A is shorter than B)

A>B (A is longer than B)

A==B (A and B are of the same duration)

A<>B (Comparison between A and B is indeterminate)

For example, 30 days cannot be meaningfully compared to one month.
The

compare(Duration duration)

method implements this
relationship.

See the

isLongerThan(Duration)

method for details about
the order relationship among

Duration

objects.

Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

A Duration object represents a period of Gregorian time,
which consists of six fields (years, months, days, hours,
minutes, and seconds) plus a sign (+/-) field.

The first five fields have non-negative (>=0) integers or null
(which represents that the field is not set),
and the seconds field has a non-negative decimal or null.
A negative sign indicates a negative duration.

This class provides a number of methods that make it easy
to use for the duration datatype of XML Schema 1.0 with
the errata.

Order relationship

Duration objects only have partial order, where two values A and B
maybe either:

- A<B (A is shorter than B)

A>B (A is longer than B)

A==B (A and B are of the same duration)

A<>B (Comparison between A and B is indeterminate)

For example, 30 days cannot be meaningfully compared to one month.
The

compare(Duration duration)

method implements this
relationship.

See the

isLongerThan(Duration)

method for details about
the order relationship among

Duration

objects.

Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

The first five fields have non-negative (>=0) integers or null
(which represents that the field is not set),
and the seconds field has a non-negative decimal or null.
A negative sign indicates a negative duration.

This class provides a number of methods that make it easy
to use for the duration datatype of XML Schema 1.0 with
the errata.

Order relationship

Duration objects only have partial order, where two values A and B
maybe either:

- A<B (A is shorter than B)

A>B (A is longer than B)

A==B (A and B are of the same duration)

A<>B (Comparison between A and B is indeterminate)

For example, 30 days cannot be meaningfully compared to one month.
The

compare(Duration duration)

method implements this
relationship.

See the

isLongerThan(Duration)

method for details about
the order relationship among

Duration

objects.

Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

This class provides a number of methods that make it easy
to use for the duration datatype of XML Schema 1.0 with
the errata.

Order relationship

Duration objects only have partial order, where two values A and B
maybe either:

- A<B (A is shorter than B)

A>B (A is longer than B)

A==B (A and B are of the same duration)

A<>B (Comparison between A and B is indeterminate)

For example, 30 days cannot be meaningfully compared to one month.
The

compare(Duration duration)

method implements this
relationship.

See the

isLongerThan(Duration)

method for details about
the order relationship among

Duration

objects.

Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

---

#### Order relationship

Duration objects only have partial order, where two values A and B
maybe either:

- A<B (A is shorter than B)

A>B (A is longer than B)

A==B (A and B are of the same duration)

A<>B (Comparison between A and B is indeterminate)

For example, 30 days cannot be meaningfully compared to one month.
The

compare(Duration duration)

method implements this
relationship.

See the

isLongerThan(Duration)

method for details about
the order relationship among

Duration

objects.

Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

A<B (A is shorter than B)

A>B (A is longer than B)

A==B (A and B are of the same duration)

A<>B (Comparison between A and B is indeterminate)

For example, 30 days cannot be meaningfully compared to one month.
The

compare(Duration duration)

method implements this
relationship.

See the

isLongerThan(Duration)

method for details about
the order relationship among

Duration

objects.

Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

See the

isLongerThan(Duration)

method for details about
the order relationship among

Duration

objects.

Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

---

#### Operations over Duration

This class provides a set of basic arithmetic operations, such
as addition, subtraction and multiplication.
Because durations don't have total order, an operation could
fail for some combinations of operations. For example, you cannot
subtract 15 days from 1 month. See the javadoc of those methods
for detailed conditions where this could happen.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

Also, division of a duration by a number is not provided because
the

Duration

class can only deal with finite precision
decimal numbers. For example, one cannot represent 1 sec divided by 3.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

However, you could substitute a division by 3 with multiplying
by numbers such as 0.3 or 0.333.

Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

---

#### Range of allowed values

Because some operations of

Duration

rely on

Calendar

even though

Duration

can hold very large or very small values,
some of the methods may not work correctly on such

Duration

s.
The impacted methods document their dependency on

Calendar

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Duration

()

Default no-arg constructor.

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

Duration

add

​(

Duration

rhs)

Computes a new duration whose value is

this+rhs

.

abstract void

addTo

​(

Calendar

calendar)

Adds this duration to a

Calendar

object.

void

addTo

​(

Date

date)

Adds this duration to a

Date

object.

abstract int

compare

​(

Duration

duration)

Partial order relation comparison with this

Duration

instance.

boolean

equals

​(

Object

duration)

Checks if this duration object has the same duration
as another

Duration

object.

int

getDays

()

Obtains the value of the DAYS field as an integer value,
or 0 if not present.

abstract

Number

getField

​(

DatatypeConstants.Field

field)

Gets the value of a field.

int

getHours

()

Obtains the value of the HOURS field as an integer value,
or 0 if not present.

int

getMinutes

()

Obtains the value of the MINUTES field as an integer value,
or 0 if not present.

int

getMonths

()

Obtains the value of the MONTHS field as an integer value,
or 0 if not present.

int

getSeconds

()

Obtains the value of the SECONDS field as an integer value,
or 0 if not present.

abstract int

getSign

()

Returns the sign of this duration in -1,0, or 1.

long

getTimeInMillis

​(

Calendar

startInstant)

Returns the length of the duration in milli-seconds.

long

getTimeInMillis

​(

Date

startInstant)

Returns the length of the duration in milli-seconds.

QName

getXMLSchemaType

()

Return the name of the XML Schema date/time type that this instance
maps to.

int

getYears

()

Get the years value of this

Duration

as an

int

or

0

if not present.

abstract int

hashCode

()

Returns a hash code consistent with the definition of the equals method.

boolean

isLongerThan

​(

Duration

duration)

Checks if this duration object is strictly longer than
another

Duration

object.

abstract boolean

isSet

​(

DatatypeConstants.Field

field)

Checks if a field is set.

boolean

isShorterThan

​(

Duration

duration)

Checks if this duration object is strictly shorter than
another

Duration

object.

Duration

multiply

​(int factor)

Computes a new duration whose value is

factor

times
longer than the value of this duration.

abstract

Duration

multiply

​(

BigDecimal

factor)

Computes a new duration whose value is

factor

times
longer than the value of this duration.

abstract

Duration

negate

()

Returns a new

Duration

object whose
value is

-this

.

abstract

Duration

normalizeWith

​(

Calendar

startTimeInstant)

Converts the years and months fields into the days field
by using a specific time instant as the reference point.

Duration

subtract

​(

Duration

rhs)

Computes a new duration whose value is

this-rhs

.

String

toString

()

Returns a

String

representation of this

Duration Object

.

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

Constructor Summary

Constructors

Constructor

Description

Duration

()

Default no-arg constructor.

---

#### Constructor Summary

Default no-arg constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Duration

add

​(

Duration

rhs)

Computes a new duration whose value is

this+rhs

.

abstract void

addTo

​(

Calendar

calendar)

Adds this duration to a

Calendar

object.

void

addTo

​(

Date

date)

Adds this duration to a

Date

object.

abstract int

compare

​(

Duration

duration)

Partial order relation comparison with this

Duration

instance.

boolean

equals

​(

Object

duration)

Checks if this duration object has the same duration
as another

Duration

object.

int

getDays

()

Obtains the value of the DAYS field as an integer value,
or 0 if not present.

abstract

Number

getField

​(

DatatypeConstants.Field

field)

Gets the value of a field.

int

getHours

()

Obtains the value of the HOURS field as an integer value,
or 0 if not present.

int

getMinutes

()

Obtains the value of the MINUTES field as an integer value,
or 0 if not present.

int

getMonths

()

Obtains the value of the MONTHS field as an integer value,
or 0 if not present.

int

getSeconds

()

Obtains the value of the SECONDS field as an integer value,
or 0 if not present.

abstract int

getSign

()

Returns the sign of this duration in -1,0, or 1.

long

getTimeInMillis

​(

Calendar

startInstant)

Returns the length of the duration in milli-seconds.

long

getTimeInMillis

​(

Date

startInstant)

Returns the length of the duration in milli-seconds.

QName

getXMLSchemaType

()

Return the name of the XML Schema date/time type that this instance
maps to.

int

getYears

()

Get the years value of this

Duration

as an

int

or

0

if not present.

abstract int

hashCode

()

Returns a hash code consistent with the definition of the equals method.

boolean

isLongerThan

​(

Duration

duration)

Checks if this duration object is strictly longer than
another

Duration

object.

abstract boolean

isSet

​(

DatatypeConstants.Field

field)

Checks if a field is set.

boolean

isShorterThan

​(

Duration

duration)

Checks if this duration object is strictly shorter than
another

Duration

object.

Duration

multiply

​(int factor)

Computes a new duration whose value is

factor

times
longer than the value of this duration.

abstract

Duration

multiply

​(

BigDecimal

factor)

Computes a new duration whose value is

factor

times
longer than the value of this duration.

abstract

Duration

negate

()

Returns a new

Duration

object whose
value is

-this

.

abstract

Duration

normalizeWith

​(

Calendar

startTimeInstant)

Converts the years and months fields into the days field
by using a specific time instant as the reference point.

Duration

subtract

​(

Duration

rhs)

Computes a new duration whose value is

this-rhs

.

String

toString

()

Returns a

String

representation of this

Duration Object

.

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

---

#### Method Summary

Computes a new duration whose value is

this+rhs

.

Adds this duration to a

Calendar

object.

Adds this duration to a

Date

object.

Partial order relation comparison with this

Duration

instance.

Checks if this duration object has the same duration
as another

Duration

object.

Obtains the value of the DAYS field as an integer value,
or 0 if not present.

Gets the value of a field.

Obtains the value of the HOURS field as an integer value,
or 0 if not present.

Obtains the value of the MINUTES field as an integer value,
or 0 if not present.

Obtains the value of the MONTHS field as an integer value,
or 0 if not present.

Obtains the value of the SECONDS field as an integer value,
or 0 if not present.

Returns the sign of this duration in -1,0, or 1.

Returns the length of the duration in milli-seconds.

Return the name of the XML Schema date/time type that this instance
maps to.

Get the years value of this

Duration

as an

int

or

0

if not present.

Returns a hash code consistent with the definition of the equals method.

Checks if this duration object is strictly longer than
another

Duration

object.

Checks if a field is set.

Checks if this duration object is strictly shorter than
another

Duration

object.

Computes a new duration whose value is

factor

times
longer than the value of this duration.

Returns a new

Duration

object whose
value is

-this

.

Converts the years and months fields into the days field
by using a specific time instant as the reference point.

Computes a new duration whose value is

this-rhs

.

Returns a

String

representation of this

Duration Object

.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Duration

```java
public Duration()
```

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

Duration

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

============ METHOD DETAIL ==========

- Method Detail

- getXMLSchemaType

```java
public
QName
getXMLSchemaType()
```

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set,
i.e.

isSet(DatatypeConstants.Field field)

==

true

.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DURATION

X

X

X

X

X

X

DatatypeConstants.DURATION_DAYTIME

X

X

X

X

DatatypeConstants.DURATION_YEARMONTH

X

X

**Returns:** one of the following constants:

DatatypeConstants.DURATION

,

DatatypeConstants.DURATION_DAYTIME

or

DatatypeConstants.DURATION_YEARMONTH

.
**Throws:** IllegalStateException

- If the combination of set fields does not match one of the XML Schema date/time datatypes.

- getSign

```java
public abstract int getSign()
```

Returns the sign of this duration in -1,0, or 1.

**Returns:** -1 if this duration is negative, 0 if the duration is zero,
and 1 if the duration is positive.

- getYears

```java
public int getYears()
```

Get the years value of this

Duration

as an

int

or

0

if not present.

getYears()

is a convenience method for

getField(DatatypeConstants.YEARS)

.

As the return value is an

int

, an incorrect value will be returned for

Duration

s
with years that go beyond the range of an

int

.
Use

getField(DatatypeConstants.YEARS)

to avoid possible loss of precision.

**Returns:** If the years field is present, return its value as an

int

, else return

0

.

- getMonths

```java
public int getMonths()
```

Obtains the value of the MONTHS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MONTHS field.

**Returns:** Months of this

Duration

.

- getDays

```java
public int getDays()
```

Obtains the value of the DAYS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the DAYS field.

**Returns:** Days of this

Duration

.

- getHours

```java
public int getHours()
```

Obtains the value of the HOURS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the HOURS field.

**Returns:** Hours of this

Duration

.

- getMinutes

```java
public int getMinutes()
```

Obtains the value of the MINUTES field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MINUTES field.

**Returns:** Minutes of this

Duration

.

- getSeconds

```java
public int getSeconds()
```

Obtains the value of the SECONDS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the SECONDS field.

**Returns:** seconds in the integer value. The fraction of seconds
will be discarded (for example, if the actual value is 2.5,
this method returns 2)

- getTimeInMillis

```java
public long getTimeInMillis​(
Calendar
startInstant)
```

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any Calendar value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Calendar)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Calendar)

method for details.

**Parameters:** startInstant

- The length of a month/year varies. The

startInstant

is
used to disambiguate this variance. Specifically, this method
returns the difference between

startInstant

and

startInstant+duration
**Returns:** milliseconds between

startInstant

and

startInstant

plus this

Duration
**Throws:** NullPointerException

- if

startInstant

parameter
is null.

- getTimeInMillis

```java
public long getTimeInMillis​(
Date
startInstant)
```

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any

Date

value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Date)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Date)

method for details.

**Parameters:** startInstant

- The length of a month/year varies. The

startInstant

is
used to disambiguate this variance. Specifically, this method
returns the difference between

startInstant

and

startInstant+duration

.
**Returns:** milliseconds between

startInstant

and

startInstant

plus this

Duration
**Throws:** NullPointerException

- If the startInstant parameter is null.
**See Also:** getTimeInMillis(Calendar)

- getField

```java
public abstract
Number
getField​(
DatatypeConstants.Field
field)
```

Gets the value of a field.

Fields of a duration object may contain arbitrary large value.
Therefore this method is designed to return a

Number

object.

In case of YEARS, MONTHS, DAYS, HOURS, and MINUTES, the returned
number will be a non-negative integer. In case of seconds,
the returned number may be a non-negative decimal value.

**Parameters:** field

- one of the six Field constants (YEARS,MONTHS,DAYS,HOURS,
MINUTES, or SECONDS.)
**Returns:** If the specified field is present, this method returns
a non-null non-negative

Number

object that
represents its value. If it is not present, return null.
For YEARS, MONTHS, DAYS, HOURS, and MINUTES, this method
returns a

BigInteger

object. For SECONDS, this
method returns a

BigDecimal

.
**Throws:** NullPointerException

- If the

field

is

null

.

- isSet

```java
public abstract boolean isSet​(
DatatypeConstants.Field
field)
```

Checks if a field is set.

A field of a duration object may or may not be present.
This method can be used to test if a field is present.

**Parameters:** field

- one of the six Field constants (YEARS,MONTHS,DAYS,HOURS,
MINUTES, or SECONDS.)
**Returns:** true if the field is present. false if not.
**Throws:** NullPointerException

- If the field parameter is null.

- add

```java
public abstract
Duration
add​(
Duration
rhs)
```

Computes a new duration whose value is

this+rhs

.

For example,

```java
"1 day" + "-3 days" = "-2 days"
"1 year" + "1 day" = "1 year and 1 day"
"-(1 hour,50 minutes)" + "-20 minutes" = "-(1 hours,70 minutes)"
"15 hours" + "-3 days" = "-(2 days,9 hours)"
"1 year" + "-1 day" = IllegalStateException
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally, the computation is defined as follows.

Firstly, we can assume that two

Duration

s to be added
are both positive without losing generality (i.e.,

(-X)+Y=Y-X

,

X+(-Y)=X-Y

,

(-X)+(-Y)=-(X+Y)

)

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

**Parameters:** rhs

-

Duration

to add to this

Duration
**Returns:** non-null valid Duration object.
**Throws:** NullPointerException

- If the rhs parameter is null.
**Throws:** IllegalStateException

- If two durations cannot be meaningfully added. For
example, adding negative one day to one month causes
this exception.
**See Also:** subtract(Duration)

- addTo

```java
public abstract void addTo​(
Calendar
calendar)
```

Adds this duration to a

Calendar

object.

Calls

Calendar.add(int,int)

in the
order of YEARS, MONTHS, DAYS, HOURS, MINUTES, SECONDS, and MILLISECONDS
if those fields are present. Because the

Calendar

class
uses int to hold values, there are cases where this method
won't work correctly (for example if values of fields
exceed the range of int.)

Also, since this duration class is a Gregorian duration, this
method will not work correctly if the given

Calendar

object is based on some other calendar systems.

Any fractional parts of this

Duration

object
beyond milliseconds will be simply ignored. For example, if
this duration is "P1.23456S", then 1 is added to SECONDS,
234 is added to MILLISECONDS, and the rest will be unused.

Note that because

Calendar.add(int, int)

is using

int

,

Duration

with values beyond the
range of

int

in its fields
will cause overflow/underflow to the given

Calendar

.

XMLGregorianCalendar.add(Duration)

provides the same
basic operation as this method while avoiding
the overflow/underflow issues.

**Parameters:** calendar

- A calendar object whose value will be modified.
**Throws:** NullPointerException

- if the calendar parameter is null.

- addTo

```java
public void addTo​(
Date
date)
```

Adds this duration to a

Date

object.

The given date is first converted into
a

GregorianCalendar

, then the duration
is added exactly like the

addTo(Calendar)

method.

The updated time instant is then converted back into a

Date

object and used to update the given

Date

object.

This somewhat redundant computation is necessary to unambiguously
determine the duration of months and years.

**Parameters:** date

- A date object whose value will be modified.
**Throws:** NullPointerException

- if the date parameter is null.

- subtract

```java
public
Duration
subtract​(
Duration
rhs)
```

Computes a new duration whose value is

this-rhs

.

For example:

```java
"1 day" - "-3 days" = "4 days"
"1 year" - "1 day" = IllegalStateException
"-(1 hour,50 minutes)" - "-20 minutes" = "-(1hours,30 minutes)"
"15 hours" - "-3 days" = "3 days and 15 hours"
"1 year" - "-1 day" = "1 year and 1 day"
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally the computation is defined as follows.
First, we can assume that two

Duration

s are both positive
without losing generality. (i.e.,

(-X)-Y=-(X+Y)

,

X-(-Y)=X+Y

,

(-X)-(-Y)=-(X-Y)

)

Then two durations are subtracted field by field.
If the sign of any non-zero field

F

is different from
the sign of the most significant field,
1 (if

F

is negative) or -1 (otherwise)
will be borrowed from the next bigger unit of

F

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

**Parameters:** rhs

-

Duration

to subtract from this

Duration

.
**Returns:** New

Duration

created from subtracting

rhs

from this

Duration

.
**Throws:** IllegalStateException

- If two durations cannot be meaningfully subtracted. For
example, subtracting one day from one month causes
this exception.
**Throws:** NullPointerException

- If the rhs parameter is null.
**See Also:** add(Duration)

- multiply

```java
public
Duration
multiply​(int factor)
```

Computes a new duration whose value is

factor

times
longer than the value of this duration.

This method is provided for the convenience.
It is functionally equivalent to the following code:

```java
multiply(new BigDecimal(String.valueOf(factor)))
```

**Parameters:** factor

- Factor times longer of new

Duration

to create.
**Returns:** New

Duration

that is

factor

times longer than this

Duration

.
**See Also:** multiply(BigDecimal)

- multiply

```java
public abstract
Duration
multiply​(
BigDecimal
factor)
```

Computes a new duration whose value is

factor

times
longer than the value of this duration.

For example,

```java
"P1M" (1 month) * "12" = "P12M" (12 months)
"PT1M" (1 min) * "0.3" = "PT18S" (18 seconds)
"P1M" (1 month) * "1.5" = IllegalStateException
```

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

The operation will be performed field by field with the precision
of

BigDecimal

. Since all the fields except seconds are
restricted to hold integers,
any fraction produced by the computation will be
carried down toward the next lower unit. For example,
if you multiply "P1D" (1 day) with "0.5", then it will be 0.5 day,
which will be carried down to "PT12H" (12 hours).
When fractions of month cannot be meaningfully carried down
to days, or year to months, this will cause an

IllegalStateException

to be thrown.
For example if you multiple one month by 0.5.

To avoid

IllegalStateException

, use
the

normalizeWith(Calendar)

method to remove the years
and months fields.

**Parameters:** factor

- to multiply by
**Returns:** returns a non-null valid

Duration

object
**Throws:** IllegalStateException

- if operation produces fraction in
the months field.
**Throws:** NullPointerException

- if the

factor

parameter is

null

.

- negate

```java
public abstract
Duration
negate()
```

Returns a new

Duration

object whose
value is

-this

.

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

**Returns:** always return a non-null valid

Duration

object.

- normalizeWith

```java
public abstract
Duration
normalizeWith​(
Calendar
startTimeInstant)
```

Converts the years and months fields into the days field
by using a specific time instant as the reference point.

For example, duration of one month normalizes to 31 days
given the start time instance "July 8th 2003, 17:40:32".

Formally, the computation is done as follows:

- the given Calendar object is cloned
- the years, months and days fields will be added to the

Calendar

object
by using the

Calendar.add(int,int)

method
- the difference between the two Calendars in computed in milliseconds and converted to days,
if a remainder occurs due to Daylight Savings Time, it is discarded
- the computed days, along with the hours, minutes and seconds
fields of this duration object is used to construct a new
Duration object.

Note that since the Calendar class uses

int

to
hold the value of year and month, this method may produce
an unexpected result if this duration object holds
a very large value in the years or months fields.

**Parameters:** startTimeInstant

-

Calendar

reference point.
**Returns:** Duration

of years and months of this

Duration

as days.
**Throws:** NullPointerException

- If the startTimeInstant parameter is null.

- compare

```java
public abstract int compare​(
Duration
duration)
```

Partial order relation comparison with this

Duration

instance.

Comparison result must be in accordance with

W3C XML Schema 1.0 Part 2, Section 3.2.7.6.2,

Order relation on duration

.

Return:

- DatatypeConstants.LESSER

if this

Duration

is shorter than

duration

parameter
- DatatypeConstants.EQUAL

if this

Duration

is equal to

duration

parameter
- DatatypeConstants.GREATER

if this

Duration

is longer than

duration

parameter
- DatatypeConstants.INDETERMINATE

if a conclusive partial order relation cannot be determined

**Parameters:** duration

- to compare
**Returns:** the relationship between

this Duration

and

duration

parameter as

DatatypeConstants.LESSER

,

DatatypeConstants.EQUAL

,

DatatypeConstants.GREATER

or

DatatypeConstants.INDETERMINATE

.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**Throws:** NullPointerException

- if

duration

is

null

.
**See Also:** isShorterThan(Duration)

,

isLongerThan(Duration)

- isLongerThan

```java
public boolean isLongerThan​(
Duration
duration)
```

Checks if this duration object is strictly longer than
another

Duration

object.

Duration X is "longer" than Y if and only if X > Y
as defined in the section 3.2.6.2 of the XML Schema 1.0
specification.

For example, "P1D" (one day) > "PT12H" (12 hours) and
"P2Y" (two years) > "P23M" (23 months).

**Parameters:** duration

-

Duration

to test this

Duration

against.
**Returns:** true if the duration represented by this object
is longer than the given duration. false otherwise.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**Throws:** NullPointerException

- If

duration

is null.
**See Also:** isShorterThan(Duration)

,

compare(Duration duration)

- isShorterThan

```java
public boolean isShorterThan​(
Duration
duration)
```

Checks if this duration object is strictly shorter than
another

Duration

object.

**Parameters:** duration

-

Duration

to test this

Duration

against.
**Returns:** true

if

duration

parameter is shorter than this

Duration

,
else

false

.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**Throws:** NullPointerException

- if

duration

is null.
**See Also:** isLongerThan(Duration duration)

,

compare(Duration duration)

- equals

```java
public boolean equals​(
Object
duration)
```

Checks if this duration object has the same duration
as another

Duration

object.

For example, "P1D" (1 day) is equal to "PT24H" (24 hours).

Duration X is equal to Y if and only if time instant
t+X and t+Y are the same for all the test time instants
specified in the section 3.2.6.2 of the XML Schema 1.0
specification.

Note that there are cases where two

Duration

s are
"incomparable" to each other, like one month and 30 days.
For example,

```java
!new Duration("P1M").isShorterThan(new Duration("P30D"))
!new Duration("P1M").isLongerThan(new Duration("P30D"))
!new Duration("P1M").equals(new Duration("P30D"))
```

**Overrides:** equals

in class

Object
**Parameters:** duration

- The object to compare this

Duration

against.
**Returns:** true

if this duration is the same length as

duration

.

false

if

duration

is

null

,
is not a

Duration

object,
or its length is different from this duration.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**See Also:** compare(Duration duration)

- hashCode

```java
public abstract int hashCode()
```

Returns a hash code consistent with the definition of the equals method.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.hashCode()

- toString

```java
public
String
toString()
```

Returns a

String

representation of this

Duration Object

.

The result is formatted according to the XML Schema 1.0 spec
and can be always parsed back later into the
equivalent

Duration Object

by

DatatypeFactory.newDuration(String lexicalRepresentation)

.

Formally, the following holds for any

Duration

Object

x:

```java
new Duration(x.toString()).equals(x)
```

**Overrides:** toString

in class

Object
**Returns:** A non-

null

valid

String

representation of this

Duration

.

Constructor Detail

- Duration

```java
public Duration()
```

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

Duration

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

---

#### Constructor Detail

Duration

```java
public Duration()
```

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

Duration

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

---

#### Duration

public Duration()

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

Duration

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

Note: Always use the

DatatypeFactory

to
construct an instance of

Duration

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

Method Detail

- getXMLSchemaType

```java
public
QName
getXMLSchemaType()
```

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set,
i.e.

isSet(DatatypeConstants.Field field)

==

true

.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DURATION

X

X

X

X

X

X

DatatypeConstants.DURATION_DAYTIME

X

X

X

X

DatatypeConstants.DURATION_YEARMONTH

X

X

**Returns:** one of the following constants:

DatatypeConstants.DURATION

,

DatatypeConstants.DURATION_DAYTIME

or

DatatypeConstants.DURATION_YEARMONTH

.
**Throws:** IllegalStateException

- If the combination of set fields does not match one of the XML Schema date/time datatypes.

- getSign

```java
public abstract int getSign()
```

Returns the sign of this duration in -1,0, or 1.

**Returns:** -1 if this duration is negative, 0 if the duration is zero,
and 1 if the duration is positive.

- getYears

```java
public int getYears()
```

Get the years value of this

Duration

as an

int

or

0

if not present.

getYears()

is a convenience method for

getField(DatatypeConstants.YEARS)

.

As the return value is an

int

, an incorrect value will be returned for

Duration

s
with years that go beyond the range of an

int

.
Use

getField(DatatypeConstants.YEARS)

to avoid possible loss of precision.

**Returns:** If the years field is present, return its value as an

int

, else return

0

.

- getMonths

```java
public int getMonths()
```

Obtains the value of the MONTHS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MONTHS field.

**Returns:** Months of this

Duration

.

- getDays

```java
public int getDays()
```

Obtains the value of the DAYS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the DAYS field.

**Returns:** Days of this

Duration

.

- getHours

```java
public int getHours()
```

Obtains the value of the HOURS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the HOURS field.

**Returns:** Hours of this

Duration

.

- getMinutes

```java
public int getMinutes()
```

Obtains the value of the MINUTES field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MINUTES field.

**Returns:** Minutes of this

Duration

.

- getSeconds

```java
public int getSeconds()
```

Obtains the value of the SECONDS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the SECONDS field.

**Returns:** seconds in the integer value. The fraction of seconds
will be discarded (for example, if the actual value is 2.5,
this method returns 2)

- getTimeInMillis

```java
public long getTimeInMillis​(
Calendar
startInstant)
```

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any Calendar value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Calendar)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Calendar)

method for details.

**Parameters:** startInstant

- The length of a month/year varies. The

startInstant

is
used to disambiguate this variance. Specifically, this method
returns the difference between

startInstant

and

startInstant+duration
**Returns:** milliseconds between

startInstant

and

startInstant

plus this

Duration
**Throws:** NullPointerException

- if

startInstant

parameter
is null.

- getTimeInMillis

```java
public long getTimeInMillis​(
Date
startInstant)
```

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any

Date

value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Date)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Date)

method for details.

**Parameters:** startInstant

- The length of a month/year varies. The

startInstant

is
used to disambiguate this variance. Specifically, this method
returns the difference between

startInstant

and

startInstant+duration

.
**Returns:** milliseconds between

startInstant

and

startInstant

plus this

Duration
**Throws:** NullPointerException

- If the startInstant parameter is null.
**See Also:** getTimeInMillis(Calendar)

- getField

```java
public abstract
Number
getField​(
DatatypeConstants.Field
field)
```

Gets the value of a field.

Fields of a duration object may contain arbitrary large value.
Therefore this method is designed to return a

Number

object.

In case of YEARS, MONTHS, DAYS, HOURS, and MINUTES, the returned
number will be a non-negative integer. In case of seconds,
the returned number may be a non-negative decimal value.

**Parameters:** field

- one of the six Field constants (YEARS,MONTHS,DAYS,HOURS,
MINUTES, or SECONDS.)
**Returns:** If the specified field is present, this method returns
a non-null non-negative

Number

object that
represents its value. If it is not present, return null.
For YEARS, MONTHS, DAYS, HOURS, and MINUTES, this method
returns a

BigInteger

object. For SECONDS, this
method returns a

BigDecimal

.
**Throws:** NullPointerException

- If the

field

is

null

.

- isSet

```java
public abstract boolean isSet​(
DatatypeConstants.Field
field)
```

Checks if a field is set.

A field of a duration object may or may not be present.
This method can be used to test if a field is present.

**Parameters:** field

- one of the six Field constants (YEARS,MONTHS,DAYS,HOURS,
MINUTES, or SECONDS.)
**Returns:** true if the field is present. false if not.
**Throws:** NullPointerException

- If the field parameter is null.

- add

```java
public abstract
Duration
add​(
Duration
rhs)
```

Computes a new duration whose value is

this+rhs

.

For example,

```java
"1 day" + "-3 days" = "-2 days"
"1 year" + "1 day" = "1 year and 1 day"
"-(1 hour,50 minutes)" + "-20 minutes" = "-(1 hours,70 minutes)"
"15 hours" + "-3 days" = "-(2 days,9 hours)"
"1 year" + "-1 day" = IllegalStateException
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally, the computation is defined as follows.

Firstly, we can assume that two

Duration

s to be added
are both positive without losing generality (i.e.,

(-X)+Y=Y-X

,

X+(-Y)=X-Y

,

(-X)+(-Y)=-(X+Y)

)

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

**Parameters:** rhs

-

Duration

to add to this

Duration
**Returns:** non-null valid Duration object.
**Throws:** NullPointerException

- If the rhs parameter is null.
**Throws:** IllegalStateException

- If two durations cannot be meaningfully added. For
example, adding negative one day to one month causes
this exception.
**See Also:** subtract(Duration)

- addTo

```java
public abstract void addTo​(
Calendar
calendar)
```

Adds this duration to a

Calendar

object.

Calls

Calendar.add(int,int)

in the
order of YEARS, MONTHS, DAYS, HOURS, MINUTES, SECONDS, and MILLISECONDS
if those fields are present. Because the

Calendar

class
uses int to hold values, there are cases where this method
won't work correctly (for example if values of fields
exceed the range of int.)

Also, since this duration class is a Gregorian duration, this
method will not work correctly if the given

Calendar

object is based on some other calendar systems.

Any fractional parts of this

Duration

object
beyond milliseconds will be simply ignored. For example, if
this duration is "P1.23456S", then 1 is added to SECONDS,
234 is added to MILLISECONDS, and the rest will be unused.

Note that because

Calendar.add(int, int)

is using

int

,

Duration

with values beyond the
range of

int

in its fields
will cause overflow/underflow to the given

Calendar

.

XMLGregorianCalendar.add(Duration)

provides the same
basic operation as this method while avoiding
the overflow/underflow issues.

**Parameters:** calendar

- A calendar object whose value will be modified.
**Throws:** NullPointerException

- if the calendar parameter is null.

- addTo

```java
public void addTo​(
Date
date)
```

Adds this duration to a

Date

object.

The given date is first converted into
a

GregorianCalendar

, then the duration
is added exactly like the

addTo(Calendar)

method.

The updated time instant is then converted back into a

Date

object and used to update the given

Date

object.

This somewhat redundant computation is necessary to unambiguously
determine the duration of months and years.

**Parameters:** date

- A date object whose value will be modified.
**Throws:** NullPointerException

- if the date parameter is null.

- subtract

```java
public
Duration
subtract​(
Duration
rhs)
```

Computes a new duration whose value is

this-rhs

.

For example:

```java
"1 day" - "-3 days" = "4 days"
"1 year" - "1 day" = IllegalStateException
"-(1 hour,50 minutes)" - "-20 minutes" = "-(1hours,30 minutes)"
"15 hours" - "-3 days" = "3 days and 15 hours"
"1 year" - "-1 day" = "1 year and 1 day"
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally the computation is defined as follows.
First, we can assume that two

Duration

s are both positive
without losing generality. (i.e.,

(-X)-Y=-(X+Y)

,

X-(-Y)=X+Y

,

(-X)-(-Y)=-(X-Y)

)

Then two durations are subtracted field by field.
If the sign of any non-zero field

F

is different from
the sign of the most significant field,
1 (if

F

is negative) or -1 (otherwise)
will be borrowed from the next bigger unit of

F

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

**Parameters:** rhs

-

Duration

to subtract from this

Duration

.
**Returns:** New

Duration

created from subtracting

rhs

from this

Duration

.
**Throws:** IllegalStateException

- If two durations cannot be meaningfully subtracted. For
example, subtracting one day from one month causes
this exception.
**Throws:** NullPointerException

- If the rhs parameter is null.
**See Also:** add(Duration)

- multiply

```java
public
Duration
multiply​(int factor)
```

Computes a new duration whose value is

factor

times
longer than the value of this duration.

This method is provided for the convenience.
It is functionally equivalent to the following code:

```java
multiply(new BigDecimal(String.valueOf(factor)))
```

**Parameters:** factor

- Factor times longer of new

Duration

to create.
**Returns:** New

Duration

that is

factor

times longer than this

Duration

.
**See Also:** multiply(BigDecimal)

- multiply

```java
public abstract
Duration
multiply​(
BigDecimal
factor)
```

Computes a new duration whose value is

factor

times
longer than the value of this duration.

For example,

```java
"P1M" (1 month) * "12" = "P12M" (12 months)
"PT1M" (1 min) * "0.3" = "PT18S" (18 seconds)
"P1M" (1 month) * "1.5" = IllegalStateException
```

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

The operation will be performed field by field with the precision
of

BigDecimal

. Since all the fields except seconds are
restricted to hold integers,
any fraction produced by the computation will be
carried down toward the next lower unit. For example,
if you multiply "P1D" (1 day) with "0.5", then it will be 0.5 day,
which will be carried down to "PT12H" (12 hours).
When fractions of month cannot be meaningfully carried down
to days, or year to months, this will cause an

IllegalStateException

to be thrown.
For example if you multiple one month by 0.5.

To avoid

IllegalStateException

, use
the

normalizeWith(Calendar)

method to remove the years
and months fields.

**Parameters:** factor

- to multiply by
**Returns:** returns a non-null valid

Duration

object
**Throws:** IllegalStateException

- if operation produces fraction in
the months field.
**Throws:** NullPointerException

- if the

factor

parameter is

null

.

- negate

```java
public abstract
Duration
negate()
```

Returns a new

Duration

object whose
value is

-this

.

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

**Returns:** always return a non-null valid

Duration

object.

- normalizeWith

```java
public abstract
Duration
normalizeWith​(
Calendar
startTimeInstant)
```

Converts the years and months fields into the days field
by using a specific time instant as the reference point.

For example, duration of one month normalizes to 31 days
given the start time instance "July 8th 2003, 17:40:32".

Formally, the computation is done as follows:

- the given Calendar object is cloned
- the years, months and days fields will be added to the

Calendar

object
by using the

Calendar.add(int,int)

method
- the difference between the two Calendars in computed in milliseconds and converted to days,
if a remainder occurs due to Daylight Savings Time, it is discarded
- the computed days, along with the hours, minutes and seconds
fields of this duration object is used to construct a new
Duration object.

Note that since the Calendar class uses

int

to
hold the value of year and month, this method may produce
an unexpected result if this duration object holds
a very large value in the years or months fields.

**Parameters:** startTimeInstant

-

Calendar

reference point.
**Returns:** Duration

of years and months of this

Duration

as days.
**Throws:** NullPointerException

- If the startTimeInstant parameter is null.

- compare

```java
public abstract int compare​(
Duration
duration)
```

Partial order relation comparison with this

Duration

instance.

Comparison result must be in accordance with

W3C XML Schema 1.0 Part 2, Section 3.2.7.6.2,

Order relation on duration

.

Return:

- DatatypeConstants.LESSER

if this

Duration

is shorter than

duration

parameter
- DatatypeConstants.EQUAL

if this

Duration

is equal to

duration

parameter
- DatatypeConstants.GREATER

if this

Duration

is longer than

duration

parameter
- DatatypeConstants.INDETERMINATE

if a conclusive partial order relation cannot be determined

**Parameters:** duration

- to compare
**Returns:** the relationship between

this Duration

and

duration

parameter as

DatatypeConstants.LESSER

,

DatatypeConstants.EQUAL

,

DatatypeConstants.GREATER

or

DatatypeConstants.INDETERMINATE

.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**Throws:** NullPointerException

- if

duration

is

null

.
**See Also:** isShorterThan(Duration)

,

isLongerThan(Duration)

- isLongerThan

```java
public boolean isLongerThan​(
Duration
duration)
```

Checks if this duration object is strictly longer than
another

Duration

object.

Duration X is "longer" than Y if and only if X > Y
as defined in the section 3.2.6.2 of the XML Schema 1.0
specification.

For example, "P1D" (one day) > "PT12H" (12 hours) and
"P2Y" (two years) > "P23M" (23 months).

**Parameters:** duration

-

Duration

to test this

Duration

against.
**Returns:** true if the duration represented by this object
is longer than the given duration. false otherwise.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**Throws:** NullPointerException

- If

duration

is null.
**See Also:** isShorterThan(Duration)

,

compare(Duration duration)

- isShorterThan

```java
public boolean isShorterThan​(
Duration
duration)
```

Checks if this duration object is strictly shorter than
another

Duration

object.

**Parameters:** duration

-

Duration

to test this

Duration

against.
**Returns:** true

if

duration

parameter is shorter than this

Duration

,
else

false

.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**Throws:** NullPointerException

- if

duration

is null.
**See Also:** isLongerThan(Duration duration)

,

compare(Duration duration)

- equals

```java
public boolean equals​(
Object
duration)
```

Checks if this duration object has the same duration
as another

Duration

object.

For example, "P1D" (1 day) is equal to "PT24H" (24 hours).

Duration X is equal to Y if and only if time instant
t+X and t+Y are the same for all the test time instants
specified in the section 3.2.6.2 of the XML Schema 1.0
specification.

Note that there are cases where two

Duration

s are
"incomparable" to each other, like one month and 30 days.
For example,

```java
!new Duration("P1M").isShorterThan(new Duration("P30D"))
!new Duration("P1M").isLongerThan(new Duration("P30D"))
!new Duration("P1M").equals(new Duration("P30D"))
```

**Overrides:** equals

in class

Object
**Parameters:** duration

- The object to compare this

Duration

against.
**Returns:** true

if this duration is the same length as

duration

.

false

if

duration

is

null

,
is not a

Duration

object,
or its length is different from this duration.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**See Also:** compare(Duration duration)

- hashCode

```java
public abstract int hashCode()
```

Returns a hash code consistent with the definition of the equals method.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.hashCode()

- toString

```java
public
String
toString()
```

Returns a

String

representation of this

Duration Object

.

The result is formatted according to the XML Schema 1.0 spec
and can be always parsed back later into the
equivalent

Duration Object

by

DatatypeFactory.newDuration(String lexicalRepresentation)

.

Formally, the following holds for any

Duration

Object

x:

```java
new Duration(x.toString()).equals(x)
```

**Overrides:** toString

in class

Object
**Returns:** A non-

null

valid

String

representation of this

Duration

.

---

#### Method Detail

getXMLSchemaType

```java
public
QName
getXMLSchemaType()
```

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set,
i.e.

isSet(DatatypeConstants.Field field)

==

true

.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DURATION

X

X

X

X

X

X

DatatypeConstants.DURATION_DAYTIME

X

X

X

X

DatatypeConstants.DURATION_YEARMONTH

X

X

**Returns:** one of the following constants:

DatatypeConstants.DURATION

,

DatatypeConstants.DURATION_DAYTIME

or

DatatypeConstants.DURATION_YEARMONTH

.
**Throws:** IllegalStateException

- If the combination of set fields does not match one of the XML Schema date/time datatypes.

---

#### getXMLSchemaType

public

QName

getXMLSchemaType()

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set,
i.e.

isSet(DatatypeConstants.Field field)

==

true

.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DURATION

X

X

X

X

X

X

DatatypeConstants.DURATION_DAYTIME

X

X

X

X

DatatypeConstants.DURATION_YEARMONTH

X

X

getSign

```java
public abstract int getSign()
```

Returns the sign of this duration in -1,0, or 1.

**Returns:** -1 if this duration is negative, 0 if the duration is zero,
and 1 if the duration is positive.

---

#### getSign

public abstract int getSign()

Returns the sign of this duration in -1,0, or 1.

getYears

```java
public int getYears()
```

Get the years value of this

Duration

as an

int

or

0

if not present.

getYears()

is a convenience method for

getField(DatatypeConstants.YEARS)

.

As the return value is an

int

, an incorrect value will be returned for

Duration

s
with years that go beyond the range of an

int

.
Use

getField(DatatypeConstants.YEARS)

to avoid possible loss of precision.

**Returns:** If the years field is present, return its value as an

int

, else return

0

.

---

#### getYears

public int getYears()

Get the years value of this

Duration

as an

int

or

0

if not present.

getYears()

is a convenience method for

getField(DatatypeConstants.YEARS)

.

As the return value is an

int

, an incorrect value will be returned for

Duration

s
with years that go beyond the range of an

int

.
Use

getField(DatatypeConstants.YEARS)

to avoid possible loss of precision.

getYears()

is a convenience method for

getField(DatatypeConstants.YEARS)

.

As the return value is an

int

, an incorrect value will be returned for

Duration

s
with years that go beyond the range of an

int

.
Use

getField(DatatypeConstants.YEARS)

to avoid possible loss of precision.

As the return value is an

int

, an incorrect value will be returned for

Duration

s
with years that go beyond the range of an

int

.
Use

getField(DatatypeConstants.YEARS)

to avoid possible loss of precision.

getMonths

```java
public int getMonths()
```

Obtains the value of the MONTHS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MONTHS field.

**Returns:** Months of this

Duration

.

---

#### getMonths

public int getMonths()

Obtains the value of the MONTHS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MONTHS field.

getDays

```java
public int getDays()
```

Obtains the value of the DAYS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the DAYS field.

**Returns:** Days of this

Duration

.

---

#### getDays

public int getDays()

Obtains the value of the DAYS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the DAYS field.

getHours

```java
public int getHours()
```

Obtains the value of the HOURS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the HOURS field.

**Returns:** Hours of this

Duration

.

---

#### getHours

public int getHours()

Obtains the value of the HOURS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the HOURS field.

getMinutes

```java
public int getMinutes()
```

Obtains the value of the MINUTES field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MINUTES field.

**Returns:** Minutes of this

Duration

.

---

#### getMinutes

public int getMinutes()

Obtains the value of the MINUTES field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the MINUTES field.

getSeconds

```java
public int getSeconds()
```

Obtains the value of the SECONDS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the SECONDS field.

**Returns:** seconds in the integer value. The fraction of seconds
will be discarded (for example, if the actual value is 2.5,
this method returns 2)

---

#### getSeconds

public int getSeconds()

Obtains the value of the SECONDS field as an integer value,
or 0 if not present.

This method works just like

getYears()

except
that this method works on the SECONDS field.

getTimeInMillis

```java
public long getTimeInMillis​(
Calendar
startInstant)
```

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any Calendar value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Calendar)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Calendar)

method for details.

**Parameters:** startInstant

- The length of a month/year varies. The

startInstant

is
used to disambiguate this variance. Specifically, this method
returns the difference between

startInstant

and

startInstant+duration
**Returns:** milliseconds between

startInstant

and

startInstant

plus this

Duration
**Throws:** NullPointerException

- if

startInstant

parameter
is null.

---

#### getTimeInMillis

public long getTimeInMillis​(

Calendar

startInstant)

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any Calendar value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Calendar)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Calendar)

method for details.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any Calendar value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Calendar)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Calendar)

method for details.

new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000

Note that this method uses the

addTo(Calendar)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Calendar)

method for details.

getTimeInMillis

```java
public long getTimeInMillis​(
Date
startInstant)
```

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any

Date

value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Date)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Date)

method for details.

**Parameters:** startInstant

- The length of a month/year varies. The

startInstant

is
used to disambiguate this variance. Specifically, this method
returns the difference between

startInstant

and

startInstant+duration

.
**Returns:** milliseconds between

startInstant

and

startInstant

plus this

Duration
**Throws:** NullPointerException

- If the startInstant parameter is null.
**See Also:** getTimeInMillis(Calendar)

---

#### getTimeInMillis

public long getTimeInMillis​(

Date

startInstant)

Returns the length of the duration in milli-seconds.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any

Date

value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Date)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Date)

method for details.

If the seconds field carries more digits than milli-second order,
those will be simply discarded (or in other words, rounded to zero.)
For example, for any

Date

value

x

,

```java
new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000
```

Note that this method uses the

addTo(Date)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Date)

method for details.

new Duration("PT10.00099S").getTimeInMills(x) == 10000

new Duration("-PT10.00099S").getTimeInMills(x) == -10000

Note that this method uses the

addTo(Date)

method,
which may work incorrectly with

Duration

objects with
very large values in its fields. See the

addTo(Date)

method for details.

getField

```java
public abstract
Number
getField​(
DatatypeConstants.Field
field)
```

Gets the value of a field.

Fields of a duration object may contain arbitrary large value.
Therefore this method is designed to return a

Number

object.

In case of YEARS, MONTHS, DAYS, HOURS, and MINUTES, the returned
number will be a non-negative integer. In case of seconds,
the returned number may be a non-negative decimal value.

**Parameters:** field

- one of the six Field constants (YEARS,MONTHS,DAYS,HOURS,
MINUTES, or SECONDS.)
**Returns:** If the specified field is present, this method returns
a non-null non-negative

Number

object that
represents its value. If it is not present, return null.
For YEARS, MONTHS, DAYS, HOURS, and MINUTES, this method
returns a

BigInteger

object. For SECONDS, this
method returns a

BigDecimal

.
**Throws:** NullPointerException

- If the

field

is

null

.

---

#### getField

public abstract

Number

getField​(

DatatypeConstants.Field

field)

Gets the value of a field.

Fields of a duration object may contain arbitrary large value.
Therefore this method is designed to return a

Number

object.

In case of YEARS, MONTHS, DAYS, HOURS, and MINUTES, the returned
number will be a non-negative integer. In case of seconds,
the returned number may be a non-negative decimal value.

isSet

```java
public abstract boolean isSet​(
DatatypeConstants.Field
field)
```

Checks if a field is set.

A field of a duration object may or may not be present.
This method can be used to test if a field is present.

**Parameters:** field

- one of the six Field constants (YEARS,MONTHS,DAYS,HOURS,
MINUTES, or SECONDS.)
**Returns:** true if the field is present. false if not.
**Throws:** NullPointerException

- If the field parameter is null.

---

#### isSet

public abstract boolean isSet​(

DatatypeConstants.Field

field)

Checks if a field is set.

A field of a duration object may or may not be present.
This method can be used to test if a field is present.

add

```java
public abstract
Duration
add​(
Duration
rhs)
```

Computes a new duration whose value is

this+rhs

.

For example,

```java
"1 day" + "-3 days" = "-2 days"
"1 year" + "1 day" = "1 year and 1 day"
"-(1 hour,50 minutes)" + "-20 minutes" = "-(1 hours,70 minutes)"
"15 hours" + "-3 days" = "-(2 days,9 hours)"
"1 year" + "-1 day" = IllegalStateException
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally, the computation is defined as follows.

Firstly, we can assume that two

Duration

s to be added
are both positive without losing generality (i.e.,

(-X)+Y=Y-X

,

X+(-Y)=X-Y

,

(-X)+(-Y)=-(X+Y)

)

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

**Parameters:** rhs

-

Duration

to add to this

Duration
**Returns:** non-null valid Duration object.
**Throws:** NullPointerException

- If the rhs parameter is null.
**Throws:** IllegalStateException

- If two durations cannot be meaningfully added. For
example, adding negative one day to one month causes
this exception.
**See Also:** subtract(Duration)

---

#### add

public abstract

Duration

add​(

Duration

rhs)

Computes a new duration whose value is

this+rhs

.

For example,

```java
"1 day" + "-3 days" = "-2 days"
"1 year" + "1 day" = "1 year and 1 day"
"-(1 hour,50 minutes)" + "-20 minutes" = "-(1 hours,70 minutes)"
"15 hours" + "-3 days" = "-(2 days,9 hours)"
"1 year" + "-1 day" = IllegalStateException
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally, the computation is defined as follows.

Firstly, we can assume that two

Duration

s to be added
are both positive without losing generality (i.e.,

(-X)+Y=Y-X

,

X+(-Y)=X-Y

,

(-X)+(-Y)=-(X+Y)

)

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

For example,

```java
"1 day" + "-3 days" = "-2 days"
"1 year" + "1 day" = "1 year and 1 day"
"-(1 hour,50 minutes)" + "-20 minutes" = "-(1 hours,70 minutes)"
"15 hours" + "-3 days" = "-(2 days,9 hours)"
"1 year" + "-1 day" = IllegalStateException
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally, the computation is defined as follows.

Firstly, we can assume that two

Duration

s to be added
are both positive without losing generality (i.e.,

(-X)+Y=Y-X

,

X+(-Y)=X-Y

,

(-X)+(-Y)=-(X+Y)

)

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

"1 day" + "-3 days" = "-2 days"
"1 year" + "1 day" = "1 year and 1 day"
"-(1 hour,50 minutes)" + "-20 minutes" = "-(1 hours,70 minutes)"
"15 hours" + "-3 days" = "-(2 days,9 hours)"
"1 year" + "-1 day" = IllegalStateException

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally, the computation is defined as follows.

Firstly, we can assume that two

Duration

s to be added
are both positive without losing generality (i.e.,

(-X)+Y=Y-X

,

X+(-Y)=X-Y

,

(-X)+(-Y)=-(X+Y)

)

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

Formally, the computation is defined as follows.

Firstly, we can assume that two

Duration

s to be added
are both positive without losing generality (i.e.,

(-X)+Y=Y-X

,

X+(-Y)=X-Y

,

(-X)+(-Y)=-(X+Y)

)

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

Firstly, we can assume that two

Duration

s to be added
are both positive without losing generality (i.e.,

(-X)+Y=Y-X

,

X+(-Y)=X-Y

,

(-X)+(-Y)=-(X+Y)

)

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

Addition of two positive

Duration

s are simply defined as
field by field addition where missing fields are treated as 0.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

A field of the resulting

Duration

will be unset if and
only if respective fields of two input

Duration

s are unset.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

Note that

lhs.add(rhs)

will be always successful if

lhs.signum()*rhs.signum()!=-1

or both of them are
normalized.

addTo

```java
public abstract void addTo​(
Calendar
calendar)
```

Adds this duration to a

Calendar

object.

Calls

Calendar.add(int,int)

in the
order of YEARS, MONTHS, DAYS, HOURS, MINUTES, SECONDS, and MILLISECONDS
if those fields are present. Because the

Calendar

class
uses int to hold values, there are cases where this method
won't work correctly (for example if values of fields
exceed the range of int.)

Also, since this duration class is a Gregorian duration, this
method will not work correctly if the given

Calendar

object is based on some other calendar systems.

Any fractional parts of this

Duration

object
beyond milliseconds will be simply ignored. For example, if
this duration is "P1.23456S", then 1 is added to SECONDS,
234 is added to MILLISECONDS, and the rest will be unused.

Note that because

Calendar.add(int, int)

is using

int

,

Duration

with values beyond the
range of

int

in its fields
will cause overflow/underflow to the given

Calendar

.

XMLGregorianCalendar.add(Duration)

provides the same
basic operation as this method while avoiding
the overflow/underflow issues.

**Parameters:** calendar

- A calendar object whose value will be modified.
**Throws:** NullPointerException

- if the calendar parameter is null.

---

#### addTo

public abstract void addTo​(

Calendar

calendar)

Adds this duration to a

Calendar

object.

Calls

Calendar.add(int,int)

in the
order of YEARS, MONTHS, DAYS, HOURS, MINUTES, SECONDS, and MILLISECONDS
if those fields are present. Because the

Calendar

class
uses int to hold values, there are cases where this method
won't work correctly (for example if values of fields
exceed the range of int.)

Also, since this duration class is a Gregorian duration, this
method will not work correctly if the given

Calendar

object is based on some other calendar systems.

Any fractional parts of this

Duration

object
beyond milliseconds will be simply ignored. For example, if
this duration is "P1.23456S", then 1 is added to SECONDS,
234 is added to MILLISECONDS, and the rest will be unused.

Note that because

Calendar.add(int, int)

is using

int

,

Duration

with values beyond the
range of

int

in its fields
will cause overflow/underflow to the given

Calendar

.

XMLGregorianCalendar.add(Duration)

provides the same
basic operation as this method while avoiding
the overflow/underflow issues.

Calls

Calendar.add(int,int)

in the
order of YEARS, MONTHS, DAYS, HOURS, MINUTES, SECONDS, and MILLISECONDS
if those fields are present. Because the

Calendar

class
uses int to hold values, there are cases where this method
won't work correctly (for example if values of fields
exceed the range of int.)

Also, since this duration class is a Gregorian duration, this
method will not work correctly if the given

Calendar

object is based on some other calendar systems.

Any fractional parts of this

Duration

object
beyond milliseconds will be simply ignored. For example, if
this duration is "P1.23456S", then 1 is added to SECONDS,
234 is added to MILLISECONDS, and the rest will be unused.

Note that because

Calendar.add(int, int)

is using

int

,

Duration

with values beyond the
range of

int

in its fields
will cause overflow/underflow to the given

Calendar

.

XMLGregorianCalendar.add(Duration)

provides the same
basic operation as this method while avoiding
the overflow/underflow issues.

Also, since this duration class is a Gregorian duration, this
method will not work correctly if the given

Calendar

object is based on some other calendar systems.

Any fractional parts of this

Duration

object
beyond milliseconds will be simply ignored. For example, if
this duration is "P1.23456S", then 1 is added to SECONDS,
234 is added to MILLISECONDS, and the rest will be unused.

Note that because

Calendar.add(int, int)

is using

int

,

Duration

with values beyond the
range of

int

in its fields
will cause overflow/underflow to the given

Calendar

.

XMLGregorianCalendar.add(Duration)

provides the same
basic operation as this method while avoiding
the overflow/underflow issues.

Any fractional parts of this

Duration

object
beyond milliseconds will be simply ignored. For example, if
this duration is "P1.23456S", then 1 is added to SECONDS,
234 is added to MILLISECONDS, and the rest will be unused.

Note that because

Calendar.add(int, int)

is using

int

,

Duration

with values beyond the
range of

int

in its fields
will cause overflow/underflow to the given

Calendar

.

XMLGregorianCalendar.add(Duration)

provides the same
basic operation as this method while avoiding
the overflow/underflow issues.

Note that because

Calendar.add(int, int)

is using

int

,

Duration

with values beyond the
range of

int

in its fields
will cause overflow/underflow to the given

Calendar

.

XMLGregorianCalendar.add(Duration)

provides the same
basic operation as this method while avoiding
the overflow/underflow issues.

addTo

```java
public void addTo​(
Date
date)
```

Adds this duration to a

Date

object.

The given date is first converted into
a

GregorianCalendar

, then the duration
is added exactly like the

addTo(Calendar)

method.

The updated time instant is then converted back into a

Date

object and used to update the given

Date

object.

This somewhat redundant computation is necessary to unambiguously
determine the duration of months and years.

**Parameters:** date

- A date object whose value will be modified.
**Throws:** NullPointerException

- if the date parameter is null.

---

#### addTo

public void addTo​(

Date

date)

Adds this duration to a

Date

object.

The given date is first converted into
a

GregorianCalendar

, then the duration
is added exactly like the

addTo(Calendar)

method.

The updated time instant is then converted back into a

Date

object and used to update the given

Date

object.

This somewhat redundant computation is necessary to unambiguously
determine the duration of months and years.

The given date is first converted into
a

GregorianCalendar

, then the duration
is added exactly like the

addTo(Calendar)

method.

The updated time instant is then converted back into a

Date

object and used to update the given

Date

object.

This somewhat redundant computation is necessary to unambiguously
determine the duration of months and years.

The updated time instant is then converted back into a

Date

object and used to update the given

Date

object.

This somewhat redundant computation is necessary to unambiguously
determine the duration of months and years.

This somewhat redundant computation is necessary to unambiguously
determine the duration of months and years.

subtract

```java
public
Duration
subtract​(
Duration
rhs)
```

Computes a new duration whose value is

this-rhs

.

For example:

```java
"1 day" - "-3 days" = "4 days"
"1 year" - "1 day" = IllegalStateException
"-(1 hour,50 minutes)" - "-20 minutes" = "-(1hours,30 minutes)"
"15 hours" - "-3 days" = "3 days and 15 hours"
"1 year" - "-1 day" = "1 year and 1 day"
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally the computation is defined as follows.
First, we can assume that two

Duration

s are both positive
without losing generality. (i.e.,

(-X)-Y=-(X+Y)

,

X-(-Y)=X+Y

,

(-X)-(-Y)=-(X-Y)

)

Then two durations are subtracted field by field.
If the sign of any non-zero field

F

is different from
the sign of the most significant field,
1 (if

F

is negative) or -1 (otherwise)
will be borrowed from the next bigger unit of

F

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

**Parameters:** rhs

-

Duration

to subtract from this

Duration

.
**Returns:** New

Duration

created from subtracting

rhs

from this

Duration

.
**Throws:** IllegalStateException

- If two durations cannot be meaningfully subtracted. For
example, subtracting one day from one month causes
this exception.
**Throws:** NullPointerException

- If the rhs parameter is null.
**See Also:** add(Duration)

---

#### subtract

public

Duration

subtract​(

Duration

rhs)

Computes a new duration whose value is

this-rhs

.

For example:

```java
"1 day" - "-3 days" = "4 days"
"1 year" - "1 day" = IllegalStateException
"-(1 hour,50 minutes)" - "-20 minutes" = "-(1hours,30 minutes)"
"15 hours" - "-3 days" = "3 days and 15 hours"
"1 year" - "-1 day" = "1 year and 1 day"
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally the computation is defined as follows.
First, we can assume that two

Duration

s are both positive
without losing generality. (i.e.,

(-X)-Y=-(X+Y)

,

X-(-Y)=X+Y

,

(-X)-(-Y)=-(X-Y)

)

Then two durations are subtracted field by field.
If the sign of any non-zero field

F

is different from
the sign of the most significant field,
1 (if

F

is negative) or -1 (otherwise)
will be borrowed from the next bigger unit of

F

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

For example:

```java
"1 day" - "-3 days" = "4 days"
"1 year" - "1 day" = IllegalStateException
"-(1 hour,50 minutes)" - "-20 minutes" = "-(1hours,30 minutes)"
"15 hours" - "-3 days" = "3 days and 15 hours"
"1 year" - "-1 day" = "1 year and 1 day"
```

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally the computation is defined as follows.
First, we can assume that two

Duration

s are both positive
without losing generality. (i.e.,

(-X)-Y=-(X+Y)

,

X-(-Y)=X+Y

,

(-X)-(-Y)=-(X-Y)

)

Then two durations are subtracted field by field.
If the sign of any non-zero field

F

is different from
the sign of the most significant field,
1 (if

F

is negative) or -1 (otherwise)
will be borrowed from the next bigger unit of

F

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

"1 day" - "-3 days" = "4 days"
"1 year" - "1 day" = IllegalStateException
"-(1 hour,50 minutes)" - "-20 minutes" = "-(1hours,30 minutes)"
"15 hours" - "-3 days" = "3 days and 15 hours"
"1 year" - "-1 day" = "1 year and 1 day"

Since there's no way to meaningfully subtract 1 day from 1 month,
there are cases where the operation fails in

IllegalStateException

.

Formally the computation is defined as follows.
First, we can assume that two

Duration

s are both positive
without losing generality. (i.e.,

(-X)-Y=-(X+Y)

,

X-(-Y)=X+Y

,

(-X)-(-Y)=-(X-Y)

)

Then two durations are subtracted field by field.
If the sign of any non-zero field

F

is different from
the sign of the most significant field,
1 (if

F

is negative) or -1 (otherwise)
will be borrowed from the next bigger unit of

F

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

Formally the computation is defined as follows.
First, we can assume that two

Duration

s are both positive
without losing generality. (i.e.,

(-X)-Y=-(X+Y)

,

X-(-Y)=X+Y

,

(-X)-(-Y)=-(X-Y)

)

Then two durations are subtracted field by field.
If the sign of any non-zero field

F

is different from
the sign of the most significant field,
1 (if

F

is negative) or -1 (otherwise)
will be borrowed from the next bigger unit of

F

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

Then two durations are subtracted field by field.
If the sign of any non-zero field

F

is different from
the sign of the most significant field,
1 (if

F

is negative) or -1 (otherwise)
will be borrowed from the next bigger unit of

F

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

This process is repeated until all the non-zero fields have
the same sign.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

If a borrow occurs in the days field (in other words, if
the computation needs to borrow 1 or -1 month to compensate
days), then the computation fails by throwing an

IllegalStateException

.

multiply

```java
public
Duration
multiply​(int factor)
```

Computes a new duration whose value is

factor

times
longer than the value of this duration.

This method is provided for the convenience.
It is functionally equivalent to the following code:

```java
multiply(new BigDecimal(String.valueOf(factor)))
```

**Parameters:** factor

- Factor times longer of new

Duration

to create.
**Returns:** New

Duration

that is

factor

times longer than this

Duration

.
**See Also:** multiply(BigDecimal)

---

#### multiply

public

Duration

multiply​(int factor)

Computes a new duration whose value is

factor

times
longer than the value of this duration.

This method is provided for the convenience.
It is functionally equivalent to the following code:

```java
multiply(new BigDecimal(String.valueOf(factor)))
```

This method is provided for the convenience.
It is functionally equivalent to the following code:

```java
multiply(new BigDecimal(String.valueOf(factor)))
```

multiply(new BigDecimal(String.valueOf(factor)))

multiply

```java
public abstract
Duration
multiply​(
BigDecimal
factor)
```

Computes a new duration whose value is

factor

times
longer than the value of this duration.

For example,

```java
"P1M" (1 month) * "12" = "P12M" (12 months)
"PT1M" (1 min) * "0.3" = "PT18S" (18 seconds)
"P1M" (1 month) * "1.5" = IllegalStateException
```

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

The operation will be performed field by field with the precision
of

BigDecimal

. Since all the fields except seconds are
restricted to hold integers,
any fraction produced by the computation will be
carried down toward the next lower unit. For example,
if you multiply "P1D" (1 day) with "0.5", then it will be 0.5 day,
which will be carried down to "PT12H" (12 hours).
When fractions of month cannot be meaningfully carried down
to days, or year to months, this will cause an

IllegalStateException

to be thrown.
For example if you multiple one month by 0.5.

To avoid

IllegalStateException

, use
the

normalizeWith(Calendar)

method to remove the years
and months fields.

**Parameters:** factor

- to multiply by
**Returns:** returns a non-null valid

Duration

object
**Throws:** IllegalStateException

- if operation produces fraction in
the months field.
**Throws:** NullPointerException

- if the

factor

parameter is

null

.

---

#### multiply

public abstract

Duration

multiply​(

BigDecimal

factor)

Computes a new duration whose value is

factor

times
longer than the value of this duration.

For example,

```java
"P1M" (1 month) * "12" = "P12M" (12 months)
"PT1M" (1 min) * "0.3" = "PT18S" (18 seconds)
"P1M" (1 month) * "1.5" = IllegalStateException
```

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

The operation will be performed field by field with the precision
of

BigDecimal

. Since all the fields except seconds are
restricted to hold integers,
any fraction produced by the computation will be
carried down toward the next lower unit. For example,
if you multiply "P1D" (1 day) with "0.5", then it will be 0.5 day,
which will be carried down to "PT12H" (12 hours).
When fractions of month cannot be meaningfully carried down
to days, or year to months, this will cause an

IllegalStateException

to be thrown.
For example if you multiple one month by 0.5.

To avoid

IllegalStateException

, use
the

normalizeWith(Calendar)

method to remove the years
and months fields.

For example,

```java
"P1M" (1 month) * "12" = "P12M" (12 months)
"PT1M" (1 min) * "0.3" = "PT18S" (18 seconds)
"P1M" (1 month) * "1.5" = IllegalStateException
```

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

The operation will be performed field by field with the precision
of

BigDecimal

. Since all the fields except seconds are
restricted to hold integers,
any fraction produced by the computation will be
carried down toward the next lower unit. For example,
if you multiply "P1D" (1 day) with "0.5", then it will be 0.5 day,
which will be carried down to "PT12H" (12 hours).
When fractions of month cannot be meaningfully carried down
to days, or year to months, this will cause an

IllegalStateException

to be thrown.
For example if you multiple one month by 0.5.

To avoid

IllegalStateException

, use
the

normalizeWith(Calendar)

method to remove the years
and months fields.

"P1M" (1 month) * "12" = "P12M" (12 months)
"PT1M" (1 min) * "0.3" = "PT18S" (18 seconds)
"P1M" (1 month) * "1.5" = IllegalStateException

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

The operation will be performed field by field with the precision
of

BigDecimal

. Since all the fields except seconds are
restricted to hold integers,
any fraction produced by the computation will be
carried down toward the next lower unit. For example,
if you multiply "P1D" (1 day) with "0.5", then it will be 0.5 day,
which will be carried down to "PT12H" (12 hours).
When fractions of month cannot be meaningfully carried down
to days, or year to months, this will cause an

IllegalStateException

to be thrown.
For example if you multiple one month by 0.5.

To avoid

IllegalStateException

, use
the

normalizeWith(Calendar)

method to remove the years
and months fields.

The operation will be performed field by field with the precision
of

BigDecimal

. Since all the fields except seconds are
restricted to hold integers,
any fraction produced by the computation will be
carried down toward the next lower unit. For example,
if you multiply "P1D" (1 day) with "0.5", then it will be 0.5 day,
which will be carried down to "PT12H" (12 hours).
When fractions of month cannot be meaningfully carried down
to days, or year to months, this will cause an

IllegalStateException

to be thrown.
For example if you multiple one month by 0.5.

To avoid

IllegalStateException

, use
the

normalizeWith(Calendar)

method to remove the years
and months fields.

To avoid

IllegalStateException

, use
the

normalizeWith(Calendar)

method to remove the years
and months fields.

negate

```java
public abstract
Duration
negate()
```

Returns a new

Duration

object whose
value is

-this

.

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

**Returns:** always return a non-null valid

Duration

object.

---

#### negate

public abstract

Duration

negate()

Returns a new

Duration

object whose
value is

-this

.

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

Since the

Duration

class is immutable, this method
doesn't change the value of this object. It simply computes
a new Duration object and returns it.

normalizeWith

```java
public abstract
Duration
normalizeWith​(
Calendar
startTimeInstant)
```

Converts the years and months fields into the days field
by using a specific time instant as the reference point.

For example, duration of one month normalizes to 31 days
given the start time instance "July 8th 2003, 17:40:32".

Formally, the computation is done as follows:

- the given Calendar object is cloned
- the years, months and days fields will be added to the

Calendar

object
by using the

Calendar.add(int,int)

method
- the difference between the two Calendars in computed in milliseconds and converted to days,
if a remainder occurs due to Daylight Savings Time, it is discarded
- the computed days, along with the hours, minutes and seconds
fields of this duration object is used to construct a new
Duration object.

Note that since the Calendar class uses

int

to
hold the value of year and month, this method may produce
an unexpected result if this duration object holds
a very large value in the years or months fields.

**Parameters:** startTimeInstant

-

Calendar

reference point.
**Returns:** Duration

of years and months of this

Duration

as days.
**Throws:** NullPointerException

- If the startTimeInstant parameter is null.

---

#### normalizeWith

public abstract

Duration

normalizeWith​(

Calendar

startTimeInstant)

Converts the years and months fields into the days field
by using a specific time instant as the reference point.

For example, duration of one month normalizes to 31 days
given the start time instance "July 8th 2003, 17:40:32".

Formally, the computation is done as follows:

- the given Calendar object is cloned
- the years, months and days fields will be added to the

Calendar

object
by using the

Calendar.add(int,int)

method
- the difference between the two Calendars in computed in milliseconds and converted to days,
if a remainder occurs due to Daylight Savings Time, it is discarded
- the computed days, along with the hours, minutes and seconds
fields of this duration object is used to construct a new
Duration object.

Note that since the Calendar class uses

int

to
hold the value of year and month, this method may produce
an unexpected result if this duration object holds
a very large value in the years or months fields.

For example, duration of one month normalizes to 31 days
given the start time instance "July 8th 2003, 17:40:32".

Formally, the computation is done as follows:

- the given Calendar object is cloned
- the years, months and days fields will be added to the

Calendar

object
by using the

Calendar.add(int,int)

method
- the difference between the two Calendars in computed in milliseconds and converted to days,
if a remainder occurs due to Daylight Savings Time, it is discarded
- the computed days, along with the hours, minutes and seconds
fields of this duration object is used to construct a new
Duration object.

Note that since the Calendar class uses

int

to
hold the value of year and month, this method may produce
an unexpected result if this duration object holds
a very large value in the years or months fields.

Formally, the computation is done as follows:

- the given Calendar object is cloned
- the years, months and days fields will be added to the

Calendar

object
by using the

Calendar.add(int,int)

method
- the difference between the two Calendars in computed in milliseconds and converted to days,
if a remainder occurs due to Daylight Savings Time, it is discarded
- the computed days, along with the hours, minutes and seconds
fields of this duration object is used to construct a new
Duration object.

Note that since the Calendar class uses

int

to
hold the value of year and month, this method may produce
an unexpected result if this duration object holds
a very large value in the years or months fields.

the given Calendar object is cloned

the years, months and days fields will be added to the

Calendar

object
by using the

Calendar.add(int,int)

method

the difference between the two Calendars in computed in milliseconds and converted to days,
if a remainder occurs due to Daylight Savings Time, it is discarded

the computed days, along with the hours, minutes and seconds
fields of this duration object is used to construct a new
Duration object.

Note that since the Calendar class uses

int

to
hold the value of year and month, this method may produce
an unexpected result if this duration object holds
a very large value in the years or months fields.

compare

```java
public abstract int compare​(
Duration
duration)
```

Partial order relation comparison with this

Duration

instance.

Comparison result must be in accordance with

W3C XML Schema 1.0 Part 2, Section 3.2.7.6.2,

Order relation on duration

.

Return:

- DatatypeConstants.LESSER

if this

Duration

is shorter than

duration

parameter
- DatatypeConstants.EQUAL

if this

Duration

is equal to

duration

parameter
- DatatypeConstants.GREATER

if this

Duration

is longer than

duration

parameter
- DatatypeConstants.INDETERMINATE

if a conclusive partial order relation cannot be determined

**Parameters:** duration

- to compare
**Returns:** the relationship between

this Duration

and

duration

parameter as

DatatypeConstants.LESSER

,

DatatypeConstants.EQUAL

,

DatatypeConstants.GREATER

or

DatatypeConstants.INDETERMINATE

.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**Throws:** NullPointerException

- if

duration

is

null

.
**See Also:** isShorterThan(Duration)

,

isLongerThan(Duration)

---

#### compare

public abstract int compare​(

Duration

duration)

Partial order relation comparison with this

Duration

instance.

Comparison result must be in accordance with

W3C XML Schema 1.0 Part 2, Section 3.2.7.6.2,

Order relation on duration

.

Return:

- DatatypeConstants.LESSER

if this

Duration

is shorter than

duration

parameter
- DatatypeConstants.EQUAL

if this

Duration

is equal to

duration

parameter
- DatatypeConstants.GREATER

if this

Duration

is longer than

duration

parameter
- DatatypeConstants.INDETERMINATE

if a conclusive partial order relation cannot be determined

Comparison result must be in accordance with

W3C XML Schema 1.0 Part 2, Section 3.2.7.6.2,

Order relation on duration

.

Return:

- DatatypeConstants.LESSER

if this

Duration

is shorter than

duration

parameter
- DatatypeConstants.EQUAL

if this

Duration

is equal to

duration

parameter
- DatatypeConstants.GREATER

if this

Duration

is longer than

duration

parameter
- DatatypeConstants.INDETERMINATE

if a conclusive partial order relation cannot be determined

Return:

- DatatypeConstants.LESSER

if this

Duration

is shorter than

duration

parameter
- DatatypeConstants.EQUAL

if this

Duration

is equal to

duration

parameter
- DatatypeConstants.GREATER

if this

Duration

is longer than

duration

parameter
- DatatypeConstants.INDETERMINATE

if a conclusive partial order relation cannot be determined

DatatypeConstants.LESSER

if this

Duration

is shorter than

duration

parameter

DatatypeConstants.EQUAL

if this

Duration

is equal to

duration

parameter

DatatypeConstants.GREATER

if this

Duration

is longer than

duration

parameter

DatatypeConstants.INDETERMINATE

if a conclusive partial order relation cannot be determined

isLongerThan

```java
public boolean isLongerThan​(
Duration
duration)
```

Checks if this duration object is strictly longer than
another

Duration

object.

Duration X is "longer" than Y if and only if X > Y
as defined in the section 3.2.6.2 of the XML Schema 1.0
specification.

For example, "P1D" (one day) > "PT12H" (12 hours) and
"P2Y" (two years) > "P23M" (23 months).

**Parameters:** duration

-

Duration

to test this

Duration

against.
**Returns:** true if the duration represented by this object
is longer than the given duration. false otherwise.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**Throws:** NullPointerException

- If

duration

is null.
**See Also:** isShorterThan(Duration)

,

compare(Duration duration)

---

#### isLongerThan

public boolean isLongerThan​(

Duration

duration)

Checks if this duration object is strictly longer than
another

Duration

object.

Duration X is "longer" than Y if and only if X > Y
as defined in the section 3.2.6.2 of the XML Schema 1.0
specification.

For example, "P1D" (one day) > "PT12H" (12 hours) and
"P2Y" (two years) > "P23M" (23 months).

Duration X is "longer" than Y if and only if X > Y
as defined in the section 3.2.6.2 of the XML Schema 1.0
specification.

For example, "P1D" (one day) > "PT12H" (12 hours) and
"P2Y" (two years) > "P23M" (23 months).

For example, "P1D" (one day) > "PT12H" (12 hours) and
"P2Y" (two years) > "P23M" (23 months).

isShorterThan

```java
public boolean isShorterThan​(
Duration
duration)
```

Checks if this duration object is strictly shorter than
another

Duration

object.

**Parameters:** duration

-

Duration

to test this

Duration

against.
**Returns:** true

if

duration

parameter is shorter than this

Duration

,
else

false

.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**Throws:** NullPointerException

- if

duration

is null.
**See Also:** isLongerThan(Duration duration)

,

compare(Duration duration)

---

#### isShorterThan

public boolean isShorterThan​(

Duration

duration)

Checks if this duration object is strictly shorter than
another

Duration

object.

equals

```java
public boolean equals​(
Object
duration)
```

Checks if this duration object has the same duration
as another

Duration

object.

For example, "P1D" (1 day) is equal to "PT24H" (24 hours).

Duration X is equal to Y if and only if time instant
t+X and t+Y are the same for all the test time instants
specified in the section 3.2.6.2 of the XML Schema 1.0
specification.

Note that there are cases where two

Duration

s are
"incomparable" to each other, like one month and 30 days.
For example,

```java
!new Duration("P1M").isShorterThan(new Duration("P30D"))
!new Duration("P1M").isLongerThan(new Duration("P30D"))
!new Duration("P1M").equals(new Duration("P30D"))
```

**Overrides:** equals

in class

Object
**Parameters:** duration

- The object to compare this

Duration

against.
**Returns:** true

if this duration is the same length as

duration

.

false

if

duration

is

null

,
is not a

Duration

object,
or its length is different from this duration.
**Throws:** UnsupportedOperationException

- If the underlying implementation
cannot reasonably process the request, e.g. W3C XML Schema allows for
arbitrarily large/small/precise values, the request may be beyond the
implementations capability.
**See Also:** compare(Duration duration)

---

#### equals

public boolean equals​(

Object

duration)

Checks if this duration object has the same duration
as another

Duration

object.

For example, "P1D" (1 day) is equal to "PT24H" (24 hours).

Duration X is equal to Y if and only if time instant
t+X and t+Y are the same for all the test time instants
specified in the section 3.2.6.2 of the XML Schema 1.0
specification.

Note that there are cases where two

Duration

s are
"incomparable" to each other, like one month and 30 days.
For example,

```java
!new Duration("P1M").isShorterThan(new Duration("P30D"))
!new Duration("P1M").isLongerThan(new Duration("P30D"))
!new Duration("P1M").equals(new Duration("P30D"))
```

For example, "P1D" (1 day) is equal to "PT24H" (24 hours).

Duration X is equal to Y if and only if time instant
t+X and t+Y are the same for all the test time instants
specified in the section 3.2.6.2 of the XML Schema 1.0
specification.

Note that there are cases where two

Duration

s are
"incomparable" to each other, like one month and 30 days.
For example,

```java
!new Duration("P1M").isShorterThan(new Duration("P30D"))
!new Duration("P1M").isLongerThan(new Duration("P30D"))
!new Duration("P1M").equals(new Duration("P30D"))
```

Duration X is equal to Y if and only if time instant
t+X and t+Y are the same for all the test time instants
specified in the section 3.2.6.2 of the XML Schema 1.0
specification.

Note that there are cases where two

Duration

s are
"incomparable" to each other, like one month and 30 days.
For example,

```java
!new Duration("P1M").isShorterThan(new Duration("P30D"))
!new Duration("P1M").isLongerThan(new Duration("P30D"))
!new Duration("P1M").equals(new Duration("P30D"))
```

Note that there are cases where two

Duration

s are
"incomparable" to each other, like one month and 30 days.
For example,

```java
!new Duration("P1M").isShorterThan(new Duration("P30D"))
!new Duration("P1M").isLongerThan(new Duration("P30D"))
!new Duration("P1M").equals(new Duration("P30D"))
```

!new Duration("P1M").isShorterThan(new Duration("P30D"))
!new Duration("P1M").isLongerThan(new Duration("P30D"))
!new Duration("P1M").equals(new Duration("P30D"))

hashCode

```java
public abstract int hashCode()
```

Returns a hash code consistent with the definition of the equals method.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.hashCode()

---

#### hashCode

public abstract int hashCode()

Returns a hash code consistent with the definition of the equals method.

toString

```java
public
String
toString()
```

Returns a

String

representation of this

Duration Object

.

The result is formatted according to the XML Schema 1.0 spec
and can be always parsed back later into the
equivalent

Duration Object

by

DatatypeFactory.newDuration(String lexicalRepresentation)

.

Formally, the following holds for any

Duration

Object

x:

```java
new Duration(x.toString()).equals(x)
```

**Overrides:** toString

in class

Object
**Returns:** A non-

null

valid

String

representation of this

Duration

.

---

#### toString

public

String

toString()

Returns a

String

representation of this

Duration Object

.

The result is formatted according to the XML Schema 1.0 spec
and can be always parsed back later into the
equivalent

Duration Object

by

DatatypeFactory.newDuration(String lexicalRepresentation)

.

Formally, the following holds for any

Duration

Object

x:

```java
new Duration(x.toString()).equals(x)
```

The result is formatted according to the XML Schema 1.0 spec
and can be always parsed back later into the
equivalent

Duration Object

by

DatatypeFactory.newDuration(String lexicalRepresentation)

.

Formally, the following holds for any

Duration

Object

x:

```java
new Duration(x.toString()).equals(x)
```

Formally, the following holds for any

Duration

Object

x:

```java
new Duration(x.toString()).equals(x)
```

new Duration(x.toString()).equals(x)

---

