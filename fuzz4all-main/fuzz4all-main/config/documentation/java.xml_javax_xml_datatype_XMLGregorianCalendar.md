# Class XMLGregorianCalendar

**Source:** `java.xml\javax\xml\datatype\XMLGregorianCalendar.html`

### Class Description

```java
public abstract class
XMLGregorianCalendar

extends
Object

implements
Cloneable
```

Representation for W3C XML Schema 1.0 date/time datatypes.
Specifically, these date/time datatypes are

DatatypeConstants.DATETIME

,

DatatypeConstants.TIME

,

DatatypeConstants.DATE

,

DatatypeConstants.GYEARMONTH

,

DatatypeConstants.GMONTHDAY

,

DatatypeConstants.GYEAR

,

DatatypeConstants.GMONTH

, and

DatatypeConstants.GDAY

defined in the XML Namespace

"http://www.w3.org/2001/XMLSchema"

.
These datatypes are normatively defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7-14

.

The table below defines the mapping between XML Schema 1.0
date/time datatype fields and this class' fields. It also summarizes
the value constraints for the date and time fields defined in

W3C XML Schema 1.0 Part 2, Appendix D,

ISO 8601 Date and Time Formats

.

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

XML Schema 1.0

datatype

field

Related

XMLGregorianCalendar

Accessor(s)

Value Range

year

getYear()

+

getEon()

or

getEonAndYear()

getYear()

is a value between -(10^9-1) to (10^9)-1
or

DatatypeConstants.FIELD_UNDEFINED

.

getEon()

is high order year value in billion of years.

getEon()

has values greater than or equal to (10^9) or less than or equal to -(10^9).
A value of null indicates field is undefined.

Given that

XML Schema 1.0 errata

states that the year zero
will be a valid lexical value in a future version of XML Schema,
this class allows the year field to be set to zero. Otherwise,
the year field value is handled exactly as described
in the errata and [ISO-8601-1988]. Note that W3C XML Schema 1.0
validation does not allow for the year field to have a value of zero.

month

getMonth()

1 to 12 or

DatatypeConstants.FIELD_UNDEFINED

day

getDay()

Independent of month, max range is 1 to 31 or

DatatypeConstants.FIELD_UNDEFINED

.

The normative value constraint stated relative to month
field's value is in

W3C XML Schema 1.0 Part 2, Appendix D

.

hour

getHour()

0 to 23 or

DatatypeConstants.FIELD_UNDEFINED

.
An hour value of 24 is allowed to be set in the lexical space provided the minute and second
field values are zero. However, an hour value of 24 is not allowed in value space and will be
transformed to represent the value of the first instance of the following day as per

XML Schema Part 2: Datatypes Second Edition, 3.2 Primitive datatypes

.

minute

getMinute()

0 to 59 or

DatatypeConstants.FIELD_UNDEFINED

second

getSecond()

+

getMillisecond()

/1000 or

getSecond()

+

getFractionalSecond()

getSecond()

from 0 to 60 or

DatatypeConstants.FIELD_UNDEFINED

.

(Note: 60 only allowable for leap second.)

getFractionalSecond()

allows for infinite precision over the range from 0.0 to 1.0 when
the

getSecond()

is defined.

FractionalSecond

is optional and has a value of

null

when it is undefined.

getMillisecond()

is the convenience
millisecond precision of value of

getFractionalSecond()

.

timezone

getTimezone()

Number of minutes or

DatatypeConstants.FIELD_UNDEFINED

.
Value range from -14 hours (-14 * 60 minutes) to 14 hours (14 * 60 minutes).

All maximum value space constraints listed for the fields in the table
above are checked by factory methods,

DatatypeFactory

,
setter methods and parse methods of
this class.

IllegalArgumentException

is thrown when a
parameter's value is outside the value constraint for the field or
if the composite
values constitute an invalid XMLGregorianCalendar instance (for example, if
the 31st of June is specified).

The following operations are defined for this class:

- accessors/mutators for independent date/time fields
- conversion between this class and W3C XML Schema 1.0 lexical representation,

toString()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)
- conversion between this class and

GregorianCalendar

,

toGregorianCalendar(java.util.TimeZone timezone, java.util.Locale aLocale, XMLGregorianCalendar defaults)

,

DatatypeFactory
- partial order relation comparator method,

compare(XMLGregorianCalendar xmlGregorianCalendar)
- equals(Object)

defined relative to

compare(XMLGregorianCalendar xmlGregorianCalendar)

.
- addition operation with

Duration

instance as defined in

W3C XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public XMLGregorianCalendar()

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

XMLGregorianCalendar

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

---

### Method Details

#### public abstract void clear()

Unset all fields to undefined.

Set all int fields to

DatatypeConstants.FIELD_UNDEFINED

and reference fields
to null.

---

#### public abstract void reset()

Reset this

XMLGregorianCalendar

to its original values.

XMLGregorianCalendar

is reset to the same values as when it was created with

DatatypeFactory.newXMLGregorianCalendar()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)

,

DatatypeFactory.newXMLGregorianCalendar(
BigInteger year,
int month,
int day,
int hour,
int minute,
int second,
BigDecimal fractionalSecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(
int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(GregorianCalendar cal)

,

DatatypeFactory.newXMLGregorianCalendarDate(
int year,
int month,
int day,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
BigDecimal fractionalSecond,
int timezone)

or

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

.

reset()

is designed to allow the reuse of existing

XMLGregorianCalendar

s
thus saving resources associated with the creation of new

XMLGregorianCalendar

s.

---

#### public abstract void setYear​(
BigInteger
year)

Set low and high order component of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

null

.

**Parameters:**
- year

- value constraints summarized in

year field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if

year

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### public abstract void setYear​(int year)

Set year of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Note: if the absolute value of the

year

parameter
is less than 10^9, the eon component of the XSD year field is set to

null

by this method.

**Parameters:**
- year

- value constraints are summarized in

year field of date/time field mapping table

.
If year is

DatatypeConstants.FIELD_UNDEFINED

, then eon is set to

null

.

---

#### public abstract void setMonth​(int month)

Set month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:**
- month

- value constraints summarized in

month field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if

month

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### public abstract void setDay​(int day)

Set days in month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:**
- day

- value constraints summarized in

day field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if

day

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### public abstract void setTimezone​(int offset)

Set the number of minutes in the timezone offset.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:**
- offset

- value constraints summarized in

timezone field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if

offset

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### public void setTime​(int hour,
int minute,
int second)

Set time as one unit.

**Parameters:**
- hour

- value constraints are summarized in

hour field of date/time field mapping table

.
- minute

- value constraints are summarized in

minute field of date/time field mapping table

.
- second

- value constraints are summarized in

second field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

**See Also:**
- setTime(int, int, int, BigDecimal)

---

#### public abstract void setHour​(int hour)

Set hours.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:**
- hour

- value constraints summarized in

hour field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if

hour

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

---

#### public abstract void setMinute​(int minute)

Set minutes.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:**
- minute

- value constraints summarized in

minute field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if

minute

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

---

#### public abstract void setSecond​(int second)

Set seconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:**
- second

- value constraints summarized in

second field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if

second

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

---

#### public abstract void setMillisecond​(int millisecond)

Set milliseconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:**
- millisecond

- value constraints summarized in

second field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if

millisecond

parameter is outside value constraints for the field as specified
in

date/time field mapping table

.

---

#### public abstract void setFractionalSecond​(
BigDecimal
fractional)

Set fractional seconds.

Unset this field by invoking the setter with a parameter value of

null

.

**Parameters:**
- fractional

- value constraints summarized in

second field of date/time field mapping table

.

**Throws:**
- IllegalArgumentException

- if

fractional

parameter is outside value constraints for the field as specified
in

date/time field mapping table

.

---

#### public void setTime​(int hour,
int minute,
int second,

BigDecimal
fractional)

Set time as one unit, including the optional infinite precision
fractional seconds.

**Parameters:**
- hour

- value constraints are summarized in

hour field of date/time field mapping table

.
- minute

- value constraints are summarized in

minute field of date/time field mapping table

.
- second

- value constraints are summarized in

second field of date/time field mapping table

.
- fractional

- value of

null

indicates this optional
field is not set.

**Throws:**
- IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### public void setTime​(int hour,
int minute,
int second,
int millisecond)

Set time as one unit, including optional milliseconds.

**Parameters:**
- hour

- value constraints are summarized in

hour field of date/time field mapping table

.
- minute

- value constraints are summarized in

minute field of date/time field mapping table

.
- second

- value constraints are summarized in

second field of date/time field mapping table

.
- millisecond

- value of

DatatypeConstants.FIELD_UNDEFINED

indicates this
optional field is not set.

**Throws:**
- IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### public abstract
BigInteger
getEon()

Returns the high order component for XML Schema 1.0 dateTime datatype field for

year

.

null

if this optional part of the year field is not defined.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:**
- The eon of this

XMLGregorianCalendar

. The value
returned is an integer multiple of 10^9.

**See Also:**
- getYear()

,

getEonAndYear()

---

#### public abstract int getYear()

Returns the low order component for XML Schema 1.0 dateTime datatype field for

year

or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:**
- The year of this

XMLGregorianCalendar

.

**See Also:**
- getEon()

,

getEonAndYear()

---

#### public abstract
BigInteger
getEonAndYear()

Returns the XML Schema 1.0 dateTime datatype field for

year

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:**
- sum of

eon

and

BigInteger.valueOf(year)

when both fields are defined. When only

year

is defined,
return it. When both

eon

and

year

are not
defined, return

null

.

**See Also:**
- getEon()

,

getYear()

---

#### public abstract int getMonth()

Returns the month of this calendar or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

month field of date/time field mapping table

.

**Returns:**
- The month of this

XMLGregorianCalendar

, from 1 to 12.

---

#### public abstract int getDay()

Returns the day of month or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

day field of date/time field mapping table

.

**Returns:**
- The day of month of this

XMLGregorianCalendar

, from 1 to 31.

**See Also:**
- setDay(int)

---

#### public abstract int getTimezone()

Returns the Timezone offset in minutes or

DatatypeConstants.FIELD_UNDEFINED

if this optional field is not defined.

Value constraints for this value are summarized in

timezone field of date/time field mapping table

.

**Returns:**
- The Timezone offset in minutes of this

XMLGregorianCalendar

.

**See Also:**
- setTimezone(int)

---

#### public abstract int getHour()

Returns the hour of day or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

hour field of date/time field mapping table

.

**Returns:**
- The hour of day of this

XMLGregorianCalendar

, from 0 to 23.

**See Also:**
- setTime(int, int, int)

---

#### public abstract int getMinute()

Returns the minute of hour or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

minute field of date/time field mapping table

.

**Returns:**
- The minute of hour of this

XMLGregorianCalendar

, from 0 to 59.

**See Also:**
- setTime(int, int, int)

---

#### public abstract int getSecond()

Returns the second of minute or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.
When this field is not defined, the optional xs:dateTime
fractional seconds field, represented by

getFractionalSecond()

and

getMillisecond()

,
must not be defined.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

**Returns:**
- The second of minute of this

XMLGregorianCalendar

, from 0 to 59.

**See Also:**
- getFractionalSecond()

,

getMillisecond()

,

setTime(int, int, int)

---

#### public int getMillisecond()

Returns the millisecond precision of

getFractionalSecond()

.

This method represents a convenience accessor to infinite
precision fractional second value returned by

getFractionalSecond()

. The returned value is the rounded
down to milliseconds value of

getFractionalSecond()

. When

getFractionalSecond()

returns

null

, this method must return

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

**Returns:**
- The millisecond precision of this

XMLGregorianCalendar

.

**See Also:**
- getFractionalSecond()

,

setTime(int, int, int)

---

#### public abstract
BigDecimal
getFractionalSecond()

Returns fractional seconds.

null

is returned when this optional field is not defined.

Value constraints are detailed in

second field of date/time field mapping table

.

This optional field can only have a defined value when the
xs:dateTime second field, represented by

getSecond()

,
does not return

DatatypeConstants.FIELD_UNDEFINED

.

**Returns:**
- Fractional seconds of this

XMLGregorianCalendar

.

**See Also:**
- getSecond()

,

setTime(int, int, int, BigDecimal)

---

#### public abstract int compare​(
XMLGregorianCalendar
xmlGregorianCalendar)

Compare two instances of W3C XML Schema 1.0 date/time datatypes
according to partial order relation defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7.3,

Order relation on dateTime

.

xsd:dateTime

datatype field mapping to accessors of
this class are defined in

date/time field mapping table

.

**Parameters:**
- xmlGregorianCalendar

- Instance of

XMLGregorianCalendar

to compare

**Returns:**
- The relationship between

this

XMLGregorianCalendar

and
the specified

xmlGregorianCalendar

as

DatatypeConstants.LESSER

,

DatatypeConstants.EQUAL

,

DatatypeConstants.GREATER

or

DatatypeConstants.INDETERMINATE

.

**Throws:**
- NullPointerException

- if

xmlGregorianCalendar

is null.

---

#### public abstract
XMLGregorianCalendar
normalize()

Normalize this instance to UTC.

2000-03-04T23:00:00+03:00 normalizes to 2000-03-04T20:00:00Z

Implements W3C XML Schema Part 2, Section 3.2.7.3 (A).

**Returns:**
- this

XMLGregorianCalendar

normalized to UTC.

---

#### public boolean equals​(
Object
obj)

Compares this calendar to the specified object. The result is

true

if and only if the argument is not null and is an

XMLGregorianCalendar

object that represents the same
instant in time as this object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- to compare.

**Returns:**
- true

when

obj

is an instance of

XMLGregorianCalendar

and

compare(XMLGregorianCalendar obj)

returns

DatatypeConstants.EQUAL

,
otherwise

false

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code consistent with the definition of the equals method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- hash code of this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public abstract
String
toXMLFormat()

Return the lexical representation of

this

instance.
The format is specified in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

".

Specific target lexical representation format is determined by

getXMLSchemaType()

.

**Returns:**
- XML, as

String

, representation of this

XMLGregorianCalendar

**Throws:**
- IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin date/time datatypes.

---

#### public abstract
QName
getXMLSchemaType()

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DATETIME

X

X

X

X

X

X

DatatypeConstants.DATE

X

X

X

DatatypeConstants.TIME

X

X

X

DatatypeConstants.GYEARMONTH

X

X

DatatypeConstants.GMONTHDAY

X

X

DatatypeConstants.GYEAR

X

DatatypeConstants.GMONTH

X

DatatypeConstants.GDAY

X

**Returns:**
- One of the following class constants:

DatatypeConstants.DATETIME

,

DatatypeConstants.TIME

,

DatatypeConstants.DATE

,

DatatypeConstants.GYEARMONTH

,

DatatypeConstants.GMONTHDAY

,

DatatypeConstants.GYEAR

,

DatatypeConstants.GMONTH

or

DatatypeConstants.GDAY

.

**Throws:**
- IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin
date/time datatypes.

---

#### public
String
toString()

Returns a

String

representation of this

XMLGregorianCalendar

Object

.

The result is a lexical representation generated by

toXMLFormat()

.

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

XMLGregorianCalendar

.

**Throws:**
- IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin date/time datatypes.

**See Also:**
- toXMLFormat()

---

#### public abstract boolean isValid()

Validate instance by

getXMLSchemaType()

constraints.

**Returns:**
- true if data values are valid.

---

#### public abstract void add​(
Duration
duration)

Add

duration

to this instance.

The computation is specified in

XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

date/time field mapping table

defines the mapping from XML Schema 1.0

dateTime

fields
to this class' representation of those fields.

**Parameters:**
- duration

- Duration to add to this

XMLGregorianCalendar

.

**Throws:**
- NullPointerException

- when

duration

parameter is

null

.

---

#### public abstract
GregorianCalendar
toGregorianCalendar()

Convert this

XMLGregorianCalendar

to a

GregorianCalendar

.

When

this

instance has an undefined field, this
conversion relies on the

java.util.GregorianCalendar

default
for its corresponding field. A notable difference between
XML Schema 1.0 date/time datatypes and

java.util.GregorianCalendar

is that Timezone value is optional for date/time datatypes and it is
a required field for

java.util.GregorianCalendar

. See javadoc
for

java.util.TimeZone.getDefault()

on how the default
is determined. To explicitly specify the

TimeZone

instance, see

toGregorianCalendar(TimeZone, Locale, XMLGregorianCalendar)

.

Field by Field Conversion from this class to

java.util.GregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA

getEonAndYear()

.signum() < 0 ? GregorianCalendar.BC : GregorianCalendar.AD

YEAR

getEonAndYear()

.abs().intValue()

*

MONTH

getMonth()

-

DatatypeConstants.JANUARY

+

Calendar.JANUARY

DAY_OF_MONTH

getDay()

HOUR_OF_DAY

getHour()

MINUTE

getMinute()

SECOND

getSecond()

MILLISECOND

get millisecond order from

getFractionalSecond()

*

GregorianCalendar.setTimeZone(TimeZone)

getTimezone()

formatted into Custom timezone id

*

designates possible loss of precision during the conversion due
to source datatype having higher precision than target datatype.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Using

timeZone

value as defined above, create a new

java.util.GregorianCalendar(timeZone,Locale.getDefault())

.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()

.
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

**Returns:**
- An instance of

GregorianCalendar

.

**See Also:**
- toGregorianCalendar(java.util.TimeZone, java.util.Locale, XMLGregorianCalendar)

---

#### public abstract
GregorianCalendar
toGregorianCalendar​(
TimeZone
timezone,

Locale
aLocale,

XMLGregorianCalendar
defaults)

Convert this

XMLGregorianCalendar

along with provided parameters
to a

GregorianCalendar

instance.

Since XML Schema 1.0 date/time datetypes has no concept of
timezone ids or daylight savings timezone ids, this conversion operation
allows the user to explicitly specify one with

timezone

parameter.

To compute the return value's

TimeZone

field,

- when parameter

timeZone

is non-null,
it is the timezone field.
- else when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else when

defaults.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using

defaults.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Create a new

java.util.GregorianCalendar(TimeZone,
Locale)

with TimeZone set as specified above and the

Locale

parameter.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

**Parameters:**
- timezone

- provide Timezone.

null

is a legal value.
- aLocale

- provide explicit Locale. Use default GregorianCalendar locale if
value is

null

.
- defaults

- provide default field values to use when corresponding
field for this instance is FIELD_UNDEFINED or null.
If

defaults

is

null

or a field
within the specified

defaults

is undefined,
just use

java.util.GregorianCalendar

defaults.

**Returns:**
- a java.util.GregorianCalendar conversion of this instance.

---

#### public abstract
TimeZone
getTimeZone​(int defaultZoneoffset)

Returns a

java.util.TimeZone

for this class.

If timezone field is defined for this instance,
returns TimeZone initialized with custom timezone id
of zoneoffset. If timezone field is undefined,
try the defaultZoneoffset that was passed in.
If defaultZoneoffset is FIELD_UNDEFINED, return
default timezone for this host.
(Same default as java.util.GregorianCalendar).

**Parameters:**
- defaultZoneoffset

- default zoneoffset if this zoneoffset is

DatatypeConstants.FIELD_UNDEFINED

.

**Returns:**
- TimeZone for this.

---

#### public abstract
Object
clone()

Creates and returns a copy of this object.

**Overrides:**
- clone

in class

Object

**Returns:**
- copy of this

Object

**See Also:**
- Cloneable

---

### Additional Sections

#### Class XMLGregorianCalendar

java.lang.Object

- javax.xml.datatype.XMLGregorianCalendar

javax.xml.datatype.XMLGregorianCalendar

**All Implemented Interfaces:** Cloneable

```java
public abstract class
XMLGregorianCalendar

extends
Object

implements
Cloneable
```

Representation for W3C XML Schema 1.0 date/time datatypes.
Specifically, these date/time datatypes are

DatatypeConstants.DATETIME

,

DatatypeConstants.TIME

,

DatatypeConstants.DATE

,

DatatypeConstants.GYEARMONTH

,

DatatypeConstants.GMONTHDAY

,

DatatypeConstants.GYEAR

,

DatatypeConstants.GMONTH

, and

DatatypeConstants.GDAY

defined in the XML Namespace

"http://www.w3.org/2001/XMLSchema"

.
These datatypes are normatively defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7-14

.

The table below defines the mapping between XML Schema 1.0
date/time datatype fields and this class' fields. It also summarizes
the value constraints for the date and time fields defined in

W3C XML Schema 1.0 Part 2, Appendix D,

ISO 8601 Date and Time Formats

.

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

XML Schema 1.0

datatype

field

Related

XMLGregorianCalendar

Accessor(s)

Value Range

year

getYear()

+

getEon()

or

getEonAndYear()

getYear()

is a value between -(10^9-1) to (10^9)-1
or

DatatypeConstants.FIELD_UNDEFINED

.

getEon()

is high order year value in billion of years.

getEon()

has values greater than or equal to (10^9) or less than or equal to -(10^9).
A value of null indicates field is undefined.

Given that

XML Schema 1.0 errata

states that the year zero
will be a valid lexical value in a future version of XML Schema,
this class allows the year field to be set to zero. Otherwise,
the year field value is handled exactly as described
in the errata and [ISO-8601-1988]. Note that W3C XML Schema 1.0
validation does not allow for the year field to have a value of zero.

month

getMonth()

1 to 12 or

DatatypeConstants.FIELD_UNDEFINED

day

getDay()

Independent of month, max range is 1 to 31 or

DatatypeConstants.FIELD_UNDEFINED

.

The normative value constraint stated relative to month
field's value is in

W3C XML Schema 1.0 Part 2, Appendix D

.

hour

getHour()

0 to 23 or

DatatypeConstants.FIELD_UNDEFINED

.
An hour value of 24 is allowed to be set in the lexical space provided the minute and second
field values are zero. However, an hour value of 24 is not allowed in value space and will be
transformed to represent the value of the first instance of the following day as per

XML Schema Part 2: Datatypes Second Edition, 3.2 Primitive datatypes

.

minute

getMinute()

0 to 59 or

DatatypeConstants.FIELD_UNDEFINED

second

getSecond()

+

getMillisecond()

/1000 or

getSecond()

+

getFractionalSecond()

getSecond()

from 0 to 60 or

DatatypeConstants.FIELD_UNDEFINED

.

(Note: 60 only allowable for leap second.)

getFractionalSecond()

allows for infinite precision over the range from 0.0 to 1.0 when
the

getSecond()

is defined.

FractionalSecond

is optional and has a value of

null

when it is undefined.

getMillisecond()

is the convenience
millisecond precision of value of

getFractionalSecond()

.

timezone

getTimezone()

Number of minutes or

DatatypeConstants.FIELD_UNDEFINED

.
Value range from -14 hours (-14 * 60 minutes) to 14 hours (14 * 60 minutes).

All maximum value space constraints listed for the fields in the table
above are checked by factory methods,

DatatypeFactory

,
setter methods and parse methods of
this class.

IllegalArgumentException

is thrown when a
parameter's value is outside the value constraint for the field or
if the composite
values constitute an invalid XMLGregorianCalendar instance (for example, if
the 31st of June is specified).

The following operations are defined for this class:

- accessors/mutators for independent date/time fields
- conversion between this class and W3C XML Schema 1.0 lexical representation,

toString()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)
- conversion between this class and

GregorianCalendar

,

toGregorianCalendar(java.util.TimeZone timezone, java.util.Locale aLocale, XMLGregorianCalendar defaults)

,

DatatypeFactory
- partial order relation comparator method,

compare(XMLGregorianCalendar xmlGregorianCalendar)
- equals(Object)

defined relative to

compare(XMLGregorianCalendar xmlGregorianCalendar)

.
- addition operation with

Duration

instance as defined in

W3C XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

**Since:** 1.5
**See Also:** Duration

,

DatatypeFactory

public abstract class

XMLGregorianCalendar

extends

Object

implements

Cloneable

Representation for W3C XML Schema 1.0 date/time datatypes.
Specifically, these date/time datatypes are

DatatypeConstants.DATETIME

,

DatatypeConstants.TIME

,

DatatypeConstants.DATE

,

DatatypeConstants.GYEARMONTH

,

DatatypeConstants.GMONTHDAY

,

DatatypeConstants.GYEAR

,

DatatypeConstants.GMONTH

, and

DatatypeConstants.GDAY

defined in the XML Namespace

"http://www.w3.org/2001/XMLSchema"

.
These datatypes are normatively defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7-14

.

The table below defines the mapping between XML Schema 1.0
date/time datatype fields and this class' fields. It also summarizes
the value constraints for the date and time fields defined in

W3C XML Schema 1.0 Part 2, Appendix D,

ISO 8601 Date and Time Formats

.

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

XML Schema 1.0

datatype

field

Related

XMLGregorianCalendar

Accessor(s)

Value Range

year

getYear()

+

getEon()

or

getEonAndYear()

getYear()

is a value between -(10^9-1) to (10^9)-1
or

DatatypeConstants.FIELD_UNDEFINED

.

getEon()

is high order year value in billion of years.

getEon()

has values greater than or equal to (10^9) or less than or equal to -(10^9).
A value of null indicates field is undefined.

Given that

XML Schema 1.0 errata

states that the year zero
will be a valid lexical value in a future version of XML Schema,
this class allows the year field to be set to zero. Otherwise,
the year field value is handled exactly as described
in the errata and [ISO-8601-1988]. Note that W3C XML Schema 1.0
validation does not allow for the year field to have a value of zero.

month

getMonth()

1 to 12 or

DatatypeConstants.FIELD_UNDEFINED

day

getDay()

Independent of month, max range is 1 to 31 or

DatatypeConstants.FIELD_UNDEFINED

.

The normative value constraint stated relative to month
field's value is in

W3C XML Schema 1.0 Part 2, Appendix D

.

hour

getHour()

0 to 23 or

DatatypeConstants.FIELD_UNDEFINED

.
An hour value of 24 is allowed to be set in the lexical space provided the minute and second
field values are zero. However, an hour value of 24 is not allowed in value space and will be
transformed to represent the value of the first instance of the following day as per

XML Schema Part 2: Datatypes Second Edition, 3.2 Primitive datatypes

.

minute

getMinute()

0 to 59 or

DatatypeConstants.FIELD_UNDEFINED

second

getSecond()

+

getMillisecond()

/1000 or

getSecond()

+

getFractionalSecond()

getSecond()

from 0 to 60 or

DatatypeConstants.FIELD_UNDEFINED

.

(Note: 60 only allowable for leap second.)

getFractionalSecond()

allows for infinite precision over the range from 0.0 to 1.0 when
the

getSecond()

is defined.

FractionalSecond

is optional and has a value of

null

when it is undefined.

getMillisecond()

is the convenience
millisecond precision of value of

getFractionalSecond()

.

timezone

getTimezone()

Number of minutes or

DatatypeConstants.FIELD_UNDEFINED

.
Value range from -14 hours (-14 * 60 minutes) to 14 hours (14 * 60 minutes).

All maximum value space constraints listed for the fields in the table
above are checked by factory methods,

DatatypeFactory

,
setter methods and parse methods of
this class.

IllegalArgumentException

is thrown when a
parameter's value is outside the value constraint for the field or
if the composite
values constitute an invalid XMLGregorianCalendar instance (for example, if
the 31st of June is specified).

The following operations are defined for this class:

- accessors/mutators for independent date/time fields
- conversion between this class and W3C XML Schema 1.0 lexical representation,

toString()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)
- conversion between this class and

GregorianCalendar

,

toGregorianCalendar(java.util.TimeZone timezone, java.util.Locale aLocale, XMLGregorianCalendar defaults)

,

DatatypeFactory
- partial order relation comparator method,

compare(XMLGregorianCalendar xmlGregorianCalendar)
- equals(Object)

defined relative to

compare(XMLGregorianCalendar xmlGregorianCalendar)

.
- addition operation with

Duration

instance as defined in

W3C XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

The table below defines the mapping between XML Schema 1.0
date/time datatype fields and this class' fields. It also summarizes
the value constraints for the date and time fields defined in

W3C XML Schema 1.0 Part 2, Appendix D,

ISO 8601 Date and Time Formats

.

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

XML Schema 1.0

datatype

field

Related

XMLGregorianCalendar

Accessor(s)

Value Range

year

getYear()

+

getEon()

or

getEonAndYear()

getYear()

is a value between -(10^9-1) to (10^9)-1
or

DatatypeConstants.FIELD_UNDEFINED

.

getEon()

is high order year value in billion of years.

getEon()

has values greater than or equal to (10^9) or less than or equal to -(10^9).
A value of null indicates field is undefined.

Given that

XML Schema 1.0 errata

states that the year zero
will be a valid lexical value in a future version of XML Schema,
this class allows the year field to be set to zero. Otherwise,
the year field value is handled exactly as described
in the errata and [ISO-8601-1988]. Note that W3C XML Schema 1.0
validation does not allow for the year field to have a value of zero.

month

getMonth()

1 to 12 or

DatatypeConstants.FIELD_UNDEFINED

day

getDay()

Independent of month, max range is 1 to 31 or

DatatypeConstants.FIELD_UNDEFINED

.

The normative value constraint stated relative to month
field's value is in

W3C XML Schema 1.0 Part 2, Appendix D

.

hour

getHour()

0 to 23 or

DatatypeConstants.FIELD_UNDEFINED

.
An hour value of 24 is allowed to be set in the lexical space provided the minute and second
field values are zero. However, an hour value of 24 is not allowed in value space and will be
transformed to represent the value of the first instance of the following day as per

XML Schema Part 2: Datatypes Second Edition, 3.2 Primitive datatypes

.

minute

getMinute()

0 to 59 or

DatatypeConstants.FIELD_UNDEFINED

second

getSecond()

+

getMillisecond()

/1000 or

getSecond()

+

getFractionalSecond()

getSecond()

from 0 to 60 or

DatatypeConstants.FIELD_UNDEFINED

.

(Note: 60 only allowable for leap second.)

getFractionalSecond()

allows for infinite precision over the range from 0.0 to 1.0 when
the

getSecond()

is defined.

FractionalSecond

is optional and has a value of

null

when it is undefined.

getMillisecond()

is the convenience
millisecond precision of value of

getFractionalSecond()

.

timezone

getTimezone()

Number of minutes or

DatatypeConstants.FIELD_UNDEFINED

.
Value range from -14 hours (-14 * 60 minutes) to 14 hours (14 * 60 minutes).

All maximum value space constraints listed for the fields in the table
above are checked by factory methods,

DatatypeFactory

,
setter methods and parse methods of
this class.

IllegalArgumentException

is thrown when a
parameter's value is outside the value constraint for the field or
if the composite
values constitute an invalid XMLGregorianCalendar instance (for example, if
the 31st of June is specified).

The following operations are defined for this class:

- accessors/mutators for independent date/time fields
- conversion between this class and W3C XML Schema 1.0 lexical representation,

toString()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)
- conversion between this class and

GregorianCalendar

,

toGregorianCalendar(java.util.TimeZone timezone, java.util.Locale aLocale, XMLGregorianCalendar defaults)

,

DatatypeFactory
- partial order relation comparator method,

compare(XMLGregorianCalendar xmlGregorianCalendar)
- equals(Object)

defined relative to

compare(XMLGregorianCalendar xmlGregorianCalendar)

.
- addition operation with

Duration

instance as defined in

W3C XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

All maximum value space constraints listed for the fields in the table
above are checked by factory methods,

DatatypeFactory

,
setter methods and parse methods of
this class.

IllegalArgumentException

is thrown when a
parameter's value is outside the value constraint for the field or
if the composite
values constitute an invalid XMLGregorianCalendar instance (for example, if
the 31st of June is specified).

The following operations are defined for this class:

- accessors/mutators for independent date/time fields
- conversion between this class and W3C XML Schema 1.0 lexical representation,

toString()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)
- conversion between this class and

GregorianCalendar

,

toGregorianCalendar(java.util.TimeZone timezone, java.util.Locale aLocale, XMLGregorianCalendar defaults)

,

DatatypeFactory
- partial order relation comparator method,

compare(XMLGregorianCalendar xmlGregorianCalendar)
- equals(Object)

defined relative to

compare(XMLGregorianCalendar xmlGregorianCalendar)

.
- addition operation with

Duration

instance as defined in

W3C XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

The following operations are defined for this class:

- accessors/mutators for independent date/time fields
- conversion between this class and W3C XML Schema 1.0 lexical representation,

toString()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)
- conversion between this class and

GregorianCalendar

,

toGregorianCalendar(java.util.TimeZone timezone, java.util.Locale aLocale, XMLGregorianCalendar defaults)

,

DatatypeFactory
- partial order relation comparator method,

compare(XMLGregorianCalendar xmlGregorianCalendar)
- equals(Object)

defined relative to

compare(XMLGregorianCalendar xmlGregorianCalendar)

.
- addition operation with

Duration

instance as defined in

W3C XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

accessors/mutators for independent date/time fields

conversion between this class and W3C XML Schema 1.0 lexical representation,

toString()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)

conversion between this class and

GregorianCalendar

,

toGregorianCalendar(java.util.TimeZone timezone, java.util.Locale aLocale, XMLGregorianCalendar defaults)

,

DatatypeFactory

partial order relation comparator method,

compare(XMLGregorianCalendar xmlGregorianCalendar)

equals(Object)

defined relative to

compare(XMLGregorianCalendar xmlGregorianCalendar)

.

addition operation with

Duration

instance as defined in

W3C XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XMLGregorianCalendar

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

abstract void

add

​(

Duration

duration)

Add

duration

to this instance.

abstract void

clear

()

Unset all fields to undefined.

abstract

Object

clone

()

Creates and returns a copy of this object.

abstract int

compare

​(

XMLGregorianCalendar

xmlGregorianCalendar)

Compare two instances of W3C XML Schema 1.0 date/time datatypes
according to partial order relation defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7.3,

Order relation on dateTime

.

boolean

equals

​(

Object

obj)

Compares this calendar to the specified object.

abstract int

getDay

()

Returns the day of month or

DatatypeConstants.FIELD_UNDEFINED

.

abstract

BigInteger

getEon

()

Returns the high order component for XML Schema 1.0 dateTime datatype field for

year

.

abstract

BigInteger

getEonAndYear

()

Returns the XML Schema 1.0 dateTime datatype field for

year

.

abstract

BigDecimal

getFractionalSecond

()

Returns fractional seconds.

abstract int

getHour

()

Returns the hour of day or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

int

getMillisecond

()

Returns the millisecond precision of

getFractionalSecond()

.

abstract int

getMinute

()

Returns the minute of hour or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

abstract int

getMonth

()

Returns the month of this calendar or

DatatypeConstants.FIELD_UNDEFINED

.

abstract int

getSecond

()

Returns the second of minute or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

abstract int

getTimezone

()

Returns the Timezone offset in minutes or

DatatypeConstants.FIELD_UNDEFINED

if this optional field is not defined.

abstract

TimeZone

getTimeZone

​(int defaultZoneoffset)

Returns a

java.util.TimeZone

for this class.

abstract

QName

getXMLSchemaType

()

Return the name of the XML Schema date/time type that this instance
maps to.

abstract int

getYear

()

Returns the low order component for XML Schema 1.0 dateTime datatype field for

year

or

DatatypeConstants.FIELD_UNDEFINED

.

int

hashCode

()

Returns a hash code consistent with the definition of the equals method.

abstract boolean

isValid

()

Validate instance by

getXMLSchemaType()

constraints.

abstract

XMLGregorianCalendar

normalize

()

Normalize this instance to UTC.

abstract void

reset

()

Reset this

XMLGregorianCalendar

to its original values.

abstract void

setDay

​(int day)

Set days in month.

abstract void

setFractionalSecond

​(

BigDecimal

fractional)

Set fractional seconds.

abstract void

setHour

​(int hour)

Set hours.

abstract void

setMillisecond

​(int millisecond)

Set milliseconds.

abstract void

setMinute

​(int minute)

Set minutes.

abstract void

setMonth

​(int month)

Set month.

abstract void

setSecond

​(int second)

Set seconds.

void

setTime

​(int hour,
int minute,
int second)

Set time as one unit.

void

setTime

​(int hour,
int minute,
int second,
int millisecond)

Set time as one unit, including optional milliseconds.

void

setTime

​(int hour,
int minute,
int second,

BigDecimal

fractional)

Set time as one unit, including the optional infinite precision
fractional seconds.

abstract void

setTimezone

​(int offset)

Set the number of minutes in the timezone offset.

abstract void

setYear

​(int year)

Set year of XSD

dateTime

year field.

abstract void

setYear

​(

BigInteger

year)

Set low and high order component of XSD

dateTime

year field.

abstract

GregorianCalendar

toGregorianCalendar

()

Convert this

XMLGregorianCalendar

to a

GregorianCalendar

.

abstract

GregorianCalendar

toGregorianCalendar

​(

TimeZone

timezone,

Locale

aLocale,

XMLGregorianCalendar

defaults)

Convert this

XMLGregorianCalendar

along with provided parameters
to a

GregorianCalendar

instance.

String

toString

()

Returns a

String

representation of this

XMLGregorianCalendar

Object

.

abstract

String

toXMLFormat

()

Return the lexical representation of

this

instance.

- Methods declared in class java.lang.

Object

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

XMLGregorianCalendar

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

abstract void

add

​(

Duration

duration)

Add

duration

to this instance.

abstract void

clear

()

Unset all fields to undefined.

abstract

Object

clone

()

Creates and returns a copy of this object.

abstract int

compare

​(

XMLGregorianCalendar

xmlGregorianCalendar)

Compare two instances of W3C XML Schema 1.0 date/time datatypes
according to partial order relation defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7.3,

Order relation on dateTime

.

boolean

equals

​(

Object

obj)

Compares this calendar to the specified object.

abstract int

getDay

()

Returns the day of month or

DatatypeConstants.FIELD_UNDEFINED

.

abstract

BigInteger

getEon

()

Returns the high order component for XML Schema 1.0 dateTime datatype field for

year

.

abstract

BigInteger

getEonAndYear

()

Returns the XML Schema 1.0 dateTime datatype field for

year

.

abstract

BigDecimal

getFractionalSecond

()

Returns fractional seconds.

abstract int

getHour

()

Returns the hour of day or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

int

getMillisecond

()

Returns the millisecond precision of

getFractionalSecond()

.

abstract int

getMinute

()

Returns the minute of hour or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

abstract int

getMonth

()

Returns the month of this calendar or

DatatypeConstants.FIELD_UNDEFINED

.

abstract int

getSecond

()

Returns the second of minute or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

abstract int

getTimezone

()

Returns the Timezone offset in minutes or

DatatypeConstants.FIELD_UNDEFINED

if this optional field is not defined.

abstract

TimeZone

getTimeZone

​(int defaultZoneoffset)

Returns a

java.util.TimeZone

for this class.

abstract

QName

getXMLSchemaType

()

Return the name of the XML Schema date/time type that this instance
maps to.

abstract int

getYear

()

Returns the low order component for XML Schema 1.0 dateTime datatype field for

year

or

DatatypeConstants.FIELD_UNDEFINED

.

int

hashCode

()

Returns a hash code consistent with the definition of the equals method.

abstract boolean

isValid

()

Validate instance by

getXMLSchemaType()

constraints.

abstract

XMLGregorianCalendar

normalize

()

Normalize this instance to UTC.

abstract void

reset

()

Reset this

XMLGregorianCalendar

to its original values.

abstract void

setDay

​(int day)

Set days in month.

abstract void

setFractionalSecond

​(

BigDecimal

fractional)

Set fractional seconds.

abstract void

setHour

​(int hour)

Set hours.

abstract void

setMillisecond

​(int millisecond)

Set milliseconds.

abstract void

setMinute

​(int minute)

Set minutes.

abstract void

setMonth

​(int month)

Set month.

abstract void

setSecond

​(int second)

Set seconds.

void

setTime

​(int hour,
int minute,
int second)

Set time as one unit.

void

setTime

​(int hour,
int minute,
int second,
int millisecond)

Set time as one unit, including optional milliseconds.

void

setTime

​(int hour,
int minute,
int second,

BigDecimal

fractional)

Set time as one unit, including the optional infinite precision
fractional seconds.

abstract void

setTimezone

​(int offset)

Set the number of minutes in the timezone offset.

abstract void

setYear

​(int year)

Set year of XSD

dateTime

year field.

abstract void

setYear

​(

BigInteger

year)

Set low and high order component of XSD

dateTime

year field.

abstract

GregorianCalendar

toGregorianCalendar

()

Convert this

XMLGregorianCalendar

to a

GregorianCalendar

.

abstract

GregorianCalendar

toGregorianCalendar

​(

TimeZone

timezone,

Locale

aLocale,

XMLGregorianCalendar

defaults)

Convert this

XMLGregorianCalendar

along with provided parameters
to a

GregorianCalendar

instance.

String

toString

()

Returns a

String

representation of this

XMLGregorianCalendar

Object

.

abstract

String

toXMLFormat

()

Return the lexical representation of

this

instance.

- Methods declared in class java.lang.

Object

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

Add

duration

to this instance.

Unset all fields to undefined.

Creates and returns a copy of this object.

Compare two instances of W3C XML Schema 1.0 date/time datatypes
according to partial order relation defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7.3,

Order relation on dateTime

.

Compares this calendar to the specified object.

Returns the day of month or

DatatypeConstants.FIELD_UNDEFINED

.

Returns the high order component for XML Schema 1.0 dateTime datatype field for

year

.

Returns the XML Schema 1.0 dateTime datatype field for

year

.

Returns fractional seconds.

Returns the hour of day or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Returns the millisecond precision of

getFractionalSecond()

.

Returns the minute of hour or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Returns the month of this calendar or

DatatypeConstants.FIELD_UNDEFINED

.

Returns the second of minute or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Returns the Timezone offset in minutes or

DatatypeConstants.FIELD_UNDEFINED

if this optional field is not defined.

Returns a

java.util.TimeZone

for this class.

Return the name of the XML Schema date/time type that this instance
maps to.

Returns the low order component for XML Schema 1.0 dateTime datatype field for

year

or

DatatypeConstants.FIELD_UNDEFINED

.

Returns a hash code consistent with the definition of the equals method.

Validate instance by

getXMLSchemaType()

constraints.

Normalize this instance to UTC.

Reset this

XMLGregorianCalendar

to its original values.

Set days in month.

Set fractional seconds.

Set hours.

Set milliseconds.

Set minutes.

Set month.

Set seconds.

Set time as one unit.

Set time as one unit, including optional milliseconds.

Set time as one unit, including the optional infinite precision
fractional seconds.

Set the number of minutes in the timezone offset.

Set year of XSD

dateTime

year field.

Set low and high order component of XSD

dateTime

year field.

Convert this

XMLGregorianCalendar

to a

GregorianCalendar

.

Convert this

XMLGregorianCalendar

along with provided parameters
to a

GregorianCalendar

instance.

Returns a

String

representation of this

XMLGregorianCalendar

Object

.

Return the lexical representation of

this

instance.

Methods declared in class java.lang.

Object

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

- XMLGregorianCalendar

```java
public XMLGregorianCalendar()
```

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

XMLGregorianCalendar

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

============ METHOD DETAIL ==========

- Method Detail

- clear

```java
public abstract void clear()
```

Unset all fields to undefined.

Set all int fields to

DatatypeConstants.FIELD_UNDEFINED

and reference fields
to null.

- reset

```java
public abstract void reset()
```

Reset this

XMLGregorianCalendar

to its original values.

XMLGregorianCalendar

is reset to the same values as when it was created with

DatatypeFactory.newXMLGregorianCalendar()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)

,

DatatypeFactory.newXMLGregorianCalendar(
BigInteger year,
int month,
int day,
int hour,
int minute,
int second,
BigDecimal fractionalSecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(
int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(GregorianCalendar cal)

,

DatatypeFactory.newXMLGregorianCalendarDate(
int year,
int month,
int day,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
BigDecimal fractionalSecond,
int timezone)

or

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

.

reset()

is designed to allow the reuse of existing

XMLGregorianCalendar

s
thus saving resources associated with the creation of new

XMLGregorianCalendar

s.

- setYear

```java
public abstract void setYear​(
BigInteger
year)
```

Set low and high order component of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

null

.

**Parameters:** year

- value constraints summarized in

year field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

year

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setYear

```java
public abstract void setYear​(int year)
```

Set year of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Note: if the absolute value of the

year

parameter
is less than 10^9, the eon component of the XSD year field is set to

null

by this method.

**Parameters:** year

- value constraints are summarized in

year field of date/time field mapping table

.
If year is

DatatypeConstants.FIELD_UNDEFINED

, then eon is set to

null

.

- setMonth

```java
public abstract void setMonth​(int month)
```

Set month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** month

- value constraints summarized in

month field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

month

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setDay

```java
public abstract void setDay​(int day)
```

Set days in month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** day

- value constraints summarized in

day field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

day

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setTimezone

```java
public abstract void setTimezone​(int offset)
```

Set the number of minutes in the timezone offset.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** offset

- value constraints summarized in

timezone field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

offset

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setTime

```java
public void setTime​(int hour,
int minute,
int second)
```

Set time as one unit.

**Parameters:** hour

- value constraints are summarized in

hour field of date/time field mapping table

.
**Parameters:** minute

- value constraints are summarized in

minute field of date/time field mapping table

.
**Parameters:** second

- value constraints are summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.
**See Also:** setTime(int, int, int, BigDecimal)

- setHour

```java
public abstract void setHour​(int hour)
```

Set hours.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** hour

- value constraints summarized in

hour field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

hour

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

- setMinute

```java
public abstract void setMinute​(int minute)
```

Set minutes.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** minute

- value constraints summarized in

minute field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

minute

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

- setSecond

```java
public abstract void setSecond​(int second)
```

Set seconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** second

- value constraints summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

second

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

- setMillisecond

```java
public abstract void setMillisecond​(int millisecond)
```

Set milliseconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** millisecond

- value constraints summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

millisecond

parameter is outside value constraints for the field as specified
in

date/time field mapping table

.

- setFractionalSecond

```java
public abstract void setFractionalSecond​(
BigDecimal
fractional)
```

Set fractional seconds.

Unset this field by invoking the setter with a parameter value of

null

.

**Parameters:** fractional

- value constraints summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

fractional

parameter is outside value constraints for the field as specified
in

date/time field mapping table

.

- setTime

```java
public void setTime​(int hour,
int minute,
int second,

BigDecimal
fractional)
```

Set time as one unit, including the optional infinite precision
fractional seconds.

**Parameters:** hour

- value constraints are summarized in

hour field of date/time field mapping table

.
**Parameters:** minute

- value constraints are summarized in

minute field of date/time field mapping table

.
**Parameters:** second

- value constraints are summarized in

second field of date/time field mapping table

.
**Parameters:** fractional

- value of

null

indicates this optional
field is not set.
**Throws:** IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setTime

```java
public void setTime​(int hour,
int minute,
int second,
int millisecond)
```

Set time as one unit, including optional milliseconds.

**Parameters:** hour

- value constraints are summarized in

hour field of date/time field mapping table

.
**Parameters:** minute

- value constraints are summarized in

minute field of date/time field mapping table

.
**Parameters:** second

- value constraints are summarized in

second field of date/time field mapping table

.
**Parameters:** millisecond

- value of

DatatypeConstants.FIELD_UNDEFINED

indicates this
optional field is not set.
**Throws:** IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- getEon

```java
public abstract
BigInteger
getEon()
```

Returns the high order component for XML Schema 1.0 dateTime datatype field for

year

.

null

if this optional part of the year field is not defined.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:** The eon of this

XMLGregorianCalendar

. The value
returned is an integer multiple of 10^9.
**See Also:** getYear()

,

getEonAndYear()

- getYear

```java
public abstract int getYear()
```

Returns the low order component for XML Schema 1.0 dateTime datatype field for

year

or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:** The year of this

XMLGregorianCalendar

.
**See Also:** getEon()

,

getEonAndYear()

- getEonAndYear

```java
public abstract
BigInteger
getEonAndYear()
```

Returns the XML Schema 1.0 dateTime datatype field for

year

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:** sum of

eon

and

BigInteger.valueOf(year)

when both fields are defined. When only

year

is defined,
return it. When both

eon

and

year

are not
defined, return

null

.
**See Also:** getEon()

,

getYear()

- getMonth

```java
public abstract int getMonth()
```

Returns the month of this calendar or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

month field of date/time field mapping table

.

**Returns:** The month of this

XMLGregorianCalendar

, from 1 to 12.

- getDay

```java
public abstract int getDay()
```

Returns the day of month or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

day field of date/time field mapping table

.

**Returns:** The day of month of this

XMLGregorianCalendar

, from 1 to 31.
**See Also:** setDay(int)

- getTimezone

```java
public abstract int getTimezone()
```

Returns the Timezone offset in minutes or

DatatypeConstants.FIELD_UNDEFINED

if this optional field is not defined.

Value constraints for this value are summarized in

timezone field of date/time field mapping table

.

**Returns:** The Timezone offset in minutes of this

XMLGregorianCalendar

.
**See Also:** setTimezone(int)

- getHour

```java
public abstract int getHour()
```

Returns the hour of day or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

hour field of date/time field mapping table

.

**Returns:** The hour of day of this

XMLGregorianCalendar

, from 0 to 23.
**See Also:** setTime(int, int, int)

- getMinute

```java
public abstract int getMinute()
```

Returns the minute of hour or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

minute field of date/time field mapping table

.

**Returns:** The minute of hour of this

XMLGregorianCalendar

, from 0 to 59.
**See Also:** setTime(int, int, int)

- getSecond

```java
public abstract int getSecond()
```

Returns the second of minute or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.
When this field is not defined, the optional xs:dateTime
fractional seconds field, represented by

getFractionalSecond()

and

getMillisecond()

,
must not be defined.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

**Returns:** The second of minute of this

XMLGregorianCalendar

, from 0 to 59.
**See Also:** getFractionalSecond()

,

getMillisecond()

,

setTime(int, int, int)

- getMillisecond

```java
public int getMillisecond()
```

Returns the millisecond precision of

getFractionalSecond()

.

This method represents a convenience accessor to infinite
precision fractional second value returned by

getFractionalSecond()

. The returned value is the rounded
down to milliseconds value of

getFractionalSecond()

. When

getFractionalSecond()

returns

null

, this method must return

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

**Returns:** The millisecond precision of this

XMLGregorianCalendar

.
**See Also:** getFractionalSecond()

,

setTime(int, int, int)

- getFractionalSecond

```java
public abstract
BigDecimal
getFractionalSecond()
```

Returns fractional seconds.

null

is returned when this optional field is not defined.

Value constraints are detailed in

second field of date/time field mapping table

.

This optional field can only have a defined value when the
xs:dateTime second field, represented by

getSecond()

,
does not return

DatatypeConstants.FIELD_UNDEFINED

.

**Returns:** Fractional seconds of this

XMLGregorianCalendar

.
**See Also:** getSecond()

,

setTime(int, int, int, BigDecimal)

- compare

```java
public abstract int compare​(
XMLGregorianCalendar
xmlGregorianCalendar)
```

Compare two instances of W3C XML Schema 1.0 date/time datatypes
according to partial order relation defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7.3,

Order relation on dateTime

.

xsd:dateTime

datatype field mapping to accessors of
this class are defined in

date/time field mapping table

.

**Parameters:** xmlGregorianCalendar

- Instance of

XMLGregorianCalendar

to compare
**Returns:** The relationship between

this

XMLGregorianCalendar

and
the specified

xmlGregorianCalendar

as

DatatypeConstants.LESSER

,

DatatypeConstants.EQUAL

,

DatatypeConstants.GREATER

or

DatatypeConstants.INDETERMINATE

.
**Throws:** NullPointerException

- if

xmlGregorianCalendar

is null.

- normalize

```java
public abstract
XMLGregorianCalendar
normalize()
```

Normalize this instance to UTC.

2000-03-04T23:00:00+03:00 normalizes to 2000-03-04T20:00:00Z

Implements W3C XML Schema Part 2, Section 3.2.7.3 (A).

**Returns:** this

XMLGregorianCalendar

normalized to UTC.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this calendar to the specified object. The result is

true

if and only if the argument is not null and is an

XMLGregorianCalendar

object that represents the same
instant in time as this object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- to compare.
**Returns:** true

when

obj

is an instance of

XMLGregorianCalendar

and

compare(XMLGregorianCalendar obj)

returns

DatatypeConstants.EQUAL

,
otherwise

false

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code consistent with the definition of the equals method.

**Overrides:** hashCode

in class

Object
**Returns:** hash code of this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toXMLFormat

```java
public abstract
String
toXMLFormat()
```

Return the lexical representation of

this

instance.
The format is specified in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

".

Specific target lexical representation format is determined by

getXMLSchemaType()

.

**Returns:** XML, as

String

, representation of this

XMLGregorianCalendar
**Throws:** IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin date/time datatypes.

- getXMLSchemaType

```java
public abstract
QName
getXMLSchemaType()
```

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DATETIME

X

X

X

X

X

X

DatatypeConstants.DATE

X

X

X

DatatypeConstants.TIME

X

X

X

DatatypeConstants.GYEARMONTH

X

X

DatatypeConstants.GMONTHDAY

X

X

DatatypeConstants.GYEAR

X

DatatypeConstants.GMONTH

X

DatatypeConstants.GDAY

X

**Returns:** One of the following class constants:

DatatypeConstants.DATETIME

,

DatatypeConstants.TIME

,

DatatypeConstants.DATE

,

DatatypeConstants.GYEARMONTH

,

DatatypeConstants.GMONTHDAY

,

DatatypeConstants.GYEAR

,

DatatypeConstants.GMONTH

or

DatatypeConstants.GDAY

.
**Throws:** IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin
date/time datatypes.

- toString

```java
public
String
toString()
```

Returns a

String

representation of this

XMLGregorianCalendar

Object

.

The result is a lexical representation generated by

toXMLFormat()

.

**Overrides:** toString

in class

Object
**Returns:** A non-

null

valid

String

representation of this

XMLGregorianCalendar

.
**Throws:** IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin date/time datatypes.
**See Also:** toXMLFormat()

- isValid

```java
public abstract boolean isValid()
```

Validate instance by

getXMLSchemaType()

constraints.

**Returns:** true if data values are valid.

- add

```java
public abstract void add​(
Duration
duration)
```

Add

duration

to this instance.

The computation is specified in

XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

date/time field mapping table

defines the mapping from XML Schema 1.0

dateTime

fields
to this class' representation of those fields.

**Parameters:** duration

- Duration to add to this

XMLGregorianCalendar

.
**Throws:** NullPointerException

- when

duration

parameter is

null

.

- toGregorianCalendar

```java
public abstract
GregorianCalendar
toGregorianCalendar()
```

Convert this

XMLGregorianCalendar

to a

GregorianCalendar

.

When

this

instance has an undefined field, this
conversion relies on the

java.util.GregorianCalendar

default
for its corresponding field. A notable difference between
XML Schema 1.0 date/time datatypes and

java.util.GregorianCalendar

is that Timezone value is optional for date/time datatypes and it is
a required field for

java.util.GregorianCalendar

. See javadoc
for

java.util.TimeZone.getDefault()

on how the default
is determined. To explicitly specify the

TimeZone

instance, see

toGregorianCalendar(TimeZone, Locale, XMLGregorianCalendar)

.

Field by Field Conversion from this class to

java.util.GregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA

getEonAndYear()

.signum() < 0 ? GregorianCalendar.BC : GregorianCalendar.AD

YEAR

getEonAndYear()

.abs().intValue()

*

MONTH

getMonth()

-

DatatypeConstants.JANUARY

+

Calendar.JANUARY

DAY_OF_MONTH

getDay()

HOUR_OF_DAY

getHour()

MINUTE

getMinute()

SECOND

getSecond()

MILLISECOND

get millisecond order from

getFractionalSecond()

*

GregorianCalendar.setTimeZone(TimeZone)

getTimezone()

formatted into Custom timezone id

*

designates possible loss of precision during the conversion due
to source datatype having higher precision than target datatype.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Using

timeZone

value as defined above, create a new

java.util.GregorianCalendar(timeZone,Locale.getDefault())

.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()

.
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

**Returns:** An instance of

GregorianCalendar

.
**See Also:** toGregorianCalendar(java.util.TimeZone, java.util.Locale, XMLGregorianCalendar)

- toGregorianCalendar

```java
public abstract
GregorianCalendar
toGregorianCalendar​(
TimeZone
timezone,

Locale
aLocale,

XMLGregorianCalendar
defaults)
```

Convert this

XMLGregorianCalendar

along with provided parameters
to a

GregorianCalendar

instance.

Since XML Schema 1.0 date/time datetypes has no concept of
timezone ids or daylight savings timezone ids, this conversion operation
allows the user to explicitly specify one with

timezone

parameter.

To compute the return value's

TimeZone

field,

- when parameter

timeZone

is non-null,
it is the timezone field.
- else when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else when

defaults.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using

defaults.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Create a new

java.util.GregorianCalendar(TimeZone,
Locale)

with TimeZone set as specified above and the

Locale

parameter.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

**Parameters:** timezone

- provide Timezone.

null

is a legal value.
**Parameters:** aLocale

- provide explicit Locale. Use default GregorianCalendar locale if
value is

null

.
**Parameters:** defaults

- provide default field values to use when corresponding
field for this instance is FIELD_UNDEFINED or null.
If

defaults

is

null

or a field
within the specified

defaults

is undefined,
just use

java.util.GregorianCalendar

defaults.
**Returns:** a java.util.GregorianCalendar conversion of this instance.

- getTimeZone

```java
public abstract
TimeZone
getTimeZone​(int defaultZoneoffset)
```

Returns a

java.util.TimeZone

for this class.

If timezone field is defined for this instance,
returns TimeZone initialized with custom timezone id
of zoneoffset. If timezone field is undefined,
try the defaultZoneoffset that was passed in.
If defaultZoneoffset is FIELD_UNDEFINED, return
default timezone for this host.
(Same default as java.util.GregorianCalendar).

**Parameters:** defaultZoneoffset

- default zoneoffset if this zoneoffset is

DatatypeConstants.FIELD_UNDEFINED

.
**Returns:** TimeZone for this.

- clone

```java
public abstract
Object
clone()
```

Creates and returns a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** copy of this

Object
**See Also:** Cloneable

Constructor Detail

- XMLGregorianCalendar

```java
public XMLGregorianCalendar()
```

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

XMLGregorianCalendar

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

---

#### Constructor Detail

XMLGregorianCalendar

```java
public XMLGregorianCalendar()
```

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

XMLGregorianCalendar

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

---

#### XMLGregorianCalendar

public XMLGregorianCalendar()

Default no-arg constructor.

Note: Always use the

DatatypeFactory

to
construct an instance of

XMLGregorianCalendar

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

Note: Always use the

DatatypeFactory

to
construct an instance of

XMLGregorianCalendar

.
The constructor on this class cannot be guaranteed to
produce an object with a consistent state and may be
removed in the future.

Method Detail

- clear

```java
public abstract void clear()
```

Unset all fields to undefined.

Set all int fields to

DatatypeConstants.FIELD_UNDEFINED

and reference fields
to null.

- reset

```java
public abstract void reset()
```

Reset this

XMLGregorianCalendar

to its original values.

XMLGregorianCalendar

is reset to the same values as when it was created with

DatatypeFactory.newXMLGregorianCalendar()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)

,

DatatypeFactory.newXMLGregorianCalendar(
BigInteger year,
int month,
int day,
int hour,
int minute,
int second,
BigDecimal fractionalSecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(
int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(GregorianCalendar cal)

,

DatatypeFactory.newXMLGregorianCalendarDate(
int year,
int month,
int day,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
BigDecimal fractionalSecond,
int timezone)

or

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

.

reset()

is designed to allow the reuse of existing

XMLGregorianCalendar

s
thus saving resources associated with the creation of new

XMLGregorianCalendar

s.

- setYear

```java
public abstract void setYear​(
BigInteger
year)
```

Set low and high order component of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

null

.

**Parameters:** year

- value constraints summarized in

year field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

year

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setYear

```java
public abstract void setYear​(int year)
```

Set year of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Note: if the absolute value of the

year

parameter
is less than 10^9, the eon component of the XSD year field is set to

null

by this method.

**Parameters:** year

- value constraints are summarized in

year field of date/time field mapping table

.
If year is

DatatypeConstants.FIELD_UNDEFINED

, then eon is set to

null

.

- setMonth

```java
public abstract void setMonth​(int month)
```

Set month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** month

- value constraints summarized in

month field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

month

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setDay

```java
public abstract void setDay​(int day)
```

Set days in month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** day

- value constraints summarized in

day field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

day

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setTimezone

```java
public abstract void setTimezone​(int offset)
```

Set the number of minutes in the timezone offset.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** offset

- value constraints summarized in

timezone field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

offset

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setTime

```java
public void setTime​(int hour,
int minute,
int second)
```

Set time as one unit.

**Parameters:** hour

- value constraints are summarized in

hour field of date/time field mapping table

.
**Parameters:** minute

- value constraints are summarized in

minute field of date/time field mapping table

.
**Parameters:** second

- value constraints are summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.
**See Also:** setTime(int, int, int, BigDecimal)

- setHour

```java
public abstract void setHour​(int hour)
```

Set hours.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** hour

- value constraints summarized in

hour field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

hour

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

- setMinute

```java
public abstract void setMinute​(int minute)
```

Set minutes.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** minute

- value constraints summarized in

minute field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

minute

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

- setSecond

```java
public abstract void setSecond​(int second)
```

Set seconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** second

- value constraints summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

second

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

- setMillisecond

```java
public abstract void setMillisecond​(int millisecond)
```

Set milliseconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** millisecond

- value constraints summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

millisecond

parameter is outside value constraints for the field as specified
in

date/time field mapping table

.

- setFractionalSecond

```java
public abstract void setFractionalSecond​(
BigDecimal
fractional)
```

Set fractional seconds.

Unset this field by invoking the setter with a parameter value of

null

.

**Parameters:** fractional

- value constraints summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

fractional

parameter is outside value constraints for the field as specified
in

date/time field mapping table

.

- setTime

```java
public void setTime​(int hour,
int minute,
int second,

BigDecimal
fractional)
```

Set time as one unit, including the optional infinite precision
fractional seconds.

**Parameters:** hour

- value constraints are summarized in

hour field of date/time field mapping table

.
**Parameters:** minute

- value constraints are summarized in

minute field of date/time field mapping table

.
**Parameters:** second

- value constraints are summarized in

second field of date/time field mapping table

.
**Parameters:** fractional

- value of

null

indicates this optional
field is not set.
**Throws:** IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- setTime

```java
public void setTime​(int hour,
int minute,
int second,
int millisecond)
```

Set time as one unit, including optional milliseconds.

**Parameters:** hour

- value constraints are summarized in

hour field of date/time field mapping table

.
**Parameters:** minute

- value constraints are summarized in

minute field of date/time field mapping table

.
**Parameters:** second

- value constraints are summarized in

second field of date/time field mapping table

.
**Parameters:** millisecond

- value of

DatatypeConstants.FIELD_UNDEFINED

indicates this
optional field is not set.
**Throws:** IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

- getEon

```java
public abstract
BigInteger
getEon()
```

Returns the high order component for XML Schema 1.0 dateTime datatype field for

year

.

null

if this optional part of the year field is not defined.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:** The eon of this

XMLGregorianCalendar

. The value
returned is an integer multiple of 10^9.
**See Also:** getYear()

,

getEonAndYear()

- getYear

```java
public abstract int getYear()
```

Returns the low order component for XML Schema 1.0 dateTime datatype field for

year

or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:** The year of this

XMLGregorianCalendar

.
**See Also:** getEon()

,

getEonAndYear()

- getEonAndYear

```java
public abstract
BigInteger
getEonAndYear()
```

Returns the XML Schema 1.0 dateTime datatype field for

year

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:** sum of

eon

and

BigInteger.valueOf(year)

when both fields are defined. When only

year

is defined,
return it. When both

eon

and

year

are not
defined, return

null

.
**See Also:** getEon()

,

getYear()

- getMonth

```java
public abstract int getMonth()
```

Returns the month of this calendar or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

month field of date/time field mapping table

.

**Returns:** The month of this

XMLGregorianCalendar

, from 1 to 12.

- getDay

```java
public abstract int getDay()
```

Returns the day of month or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

day field of date/time field mapping table

.

**Returns:** The day of month of this

XMLGregorianCalendar

, from 1 to 31.
**See Also:** setDay(int)

- getTimezone

```java
public abstract int getTimezone()
```

Returns the Timezone offset in minutes or

DatatypeConstants.FIELD_UNDEFINED

if this optional field is not defined.

Value constraints for this value are summarized in

timezone field of date/time field mapping table

.

**Returns:** The Timezone offset in minutes of this

XMLGregorianCalendar

.
**See Also:** setTimezone(int)

- getHour

```java
public abstract int getHour()
```

Returns the hour of day or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

hour field of date/time field mapping table

.

**Returns:** The hour of day of this

XMLGregorianCalendar

, from 0 to 23.
**See Also:** setTime(int, int, int)

- getMinute

```java
public abstract int getMinute()
```

Returns the minute of hour or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

minute field of date/time field mapping table

.

**Returns:** The minute of hour of this

XMLGregorianCalendar

, from 0 to 59.
**See Also:** setTime(int, int, int)

- getSecond

```java
public abstract int getSecond()
```

Returns the second of minute or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.
When this field is not defined, the optional xs:dateTime
fractional seconds field, represented by

getFractionalSecond()

and

getMillisecond()

,
must not be defined.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

**Returns:** The second of minute of this

XMLGregorianCalendar

, from 0 to 59.
**See Also:** getFractionalSecond()

,

getMillisecond()

,

setTime(int, int, int)

- getMillisecond

```java
public int getMillisecond()
```

Returns the millisecond precision of

getFractionalSecond()

.

This method represents a convenience accessor to infinite
precision fractional second value returned by

getFractionalSecond()

. The returned value is the rounded
down to milliseconds value of

getFractionalSecond()

. When

getFractionalSecond()

returns

null

, this method must return

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

**Returns:** The millisecond precision of this

XMLGregorianCalendar

.
**See Also:** getFractionalSecond()

,

setTime(int, int, int)

- getFractionalSecond

```java
public abstract
BigDecimal
getFractionalSecond()
```

Returns fractional seconds.

null

is returned when this optional field is not defined.

Value constraints are detailed in

second field of date/time field mapping table

.

This optional field can only have a defined value when the
xs:dateTime second field, represented by

getSecond()

,
does not return

DatatypeConstants.FIELD_UNDEFINED

.

**Returns:** Fractional seconds of this

XMLGregorianCalendar

.
**See Also:** getSecond()

,

setTime(int, int, int, BigDecimal)

- compare

```java
public abstract int compare​(
XMLGregorianCalendar
xmlGregorianCalendar)
```

Compare two instances of W3C XML Schema 1.0 date/time datatypes
according to partial order relation defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7.3,

Order relation on dateTime

.

xsd:dateTime

datatype field mapping to accessors of
this class are defined in

date/time field mapping table

.

**Parameters:** xmlGregorianCalendar

- Instance of

XMLGregorianCalendar

to compare
**Returns:** The relationship between

this

XMLGregorianCalendar

and
the specified

xmlGregorianCalendar

as

DatatypeConstants.LESSER

,

DatatypeConstants.EQUAL

,

DatatypeConstants.GREATER

or

DatatypeConstants.INDETERMINATE

.
**Throws:** NullPointerException

- if

xmlGregorianCalendar

is null.

- normalize

```java
public abstract
XMLGregorianCalendar
normalize()
```

Normalize this instance to UTC.

2000-03-04T23:00:00+03:00 normalizes to 2000-03-04T20:00:00Z

Implements W3C XML Schema Part 2, Section 3.2.7.3 (A).

**Returns:** this

XMLGregorianCalendar

normalized to UTC.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this calendar to the specified object. The result is

true

if and only if the argument is not null and is an

XMLGregorianCalendar

object that represents the same
instant in time as this object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- to compare.
**Returns:** true

when

obj

is an instance of

XMLGregorianCalendar

and

compare(XMLGregorianCalendar obj)

returns

DatatypeConstants.EQUAL

,
otherwise

false

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code consistent with the definition of the equals method.

**Overrides:** hashCode

in class

Object
**Returns:** hash code of this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toXMLFormat

```java
public abstract
String
toXMLFormat()
```

Return the lexical representation of

this

instance.
The format is specified in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

".

Specific target lexical representation format is determined by

getXMLSchemaType()

.

**Returns:** XML, as

String

, representation of this

XMLGregorianCalendar
**Throws:** IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin date/time datatypes.

- getXMLSchemaType

```java
public abstract
QName
getXMLSchemaType()
```

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DATETIME

X

X

X

X

X

X

DatatypeConstants.DATE

X

X

X

DatatypeConstants.TIME

X

X

X

DatatypeConstants.GYEARMONTH

X

X

DatatypeConstants.GMONTHDAY

X

X

DatatypeConstants.GYEAR

X

DatatypeConstants.GMONTH

X

DatatypeConstants.GDAY

X

**Returns:** One of the following class constants:

DatatypeConstants.DATETIME

,

DatatypeConstants.TIME

,

DatatypeConstants.DATE

,

DatatypeConstants.GYEARMONTH

,

DatatypeConstants.GMONTHDAY

,

DatatypeConstants.GYEAR

,

DatatypeConstants.GMONTH

or

DatatypeConstants.GDAY

.
**Throws:** IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin
date/time datatypes.

- toString

```java
public
String
toString()
```

Returns a

String

representation of this

XMLGregorianCalendar

Object

.

The result is a lexical representation generated by

toXMLFormat()

.

**Overrides:** toString

in class

Object
**Returns:** A non-

null

valid

String

representation of this

XMLGregorianCalendar

.
**Throws:** IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin date/time datatypes.
**See Also:** toXMLFormat()

- isValid

```java
public abstract boolean isValid()
```

Validate instance by

getXMLSchemaType()

constraints.

**Returns:** true if data values are valid.

- add

```java
public abstract void add​(
Duration
duration)
```

Add

duration

to this instance.

The computation is specified in

XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

date/time field mapping table

defines the mapping from XML Schema 1.0

dateTime

fields
to this class' representation of those fields.

**Parameters:** duration

- Duration to add to this

XMLGregorianCalendar

.
**Throws:** NullPointerException

- when

duration

parameter is

null

.

- toGregorianCalendar

```java
public abstract
GregorianCalendar
toGregorianCalendar()
```

Convert this

XMLGregorianCalendar

to a

GregorianCalendar

.

When

this

instance has an undefined field, this
conversion relies on the

java.util.GregorianCalendar

default
for its corresponding field. A notable difference between
XML Schema 1.0 date/time datatypes and

java.util.GregorianCalendar

is that Timezone value is optional for date/time datatypes and it is
a required field for

java.util.GregorianCalendar

. See javadoc
for

java.util.TimeZone.getDefault()

on how the default
is determined. To explicitly specify the

TimeZone

instance, see

toGregorianCalendar(TimeZone, Locale, XMLGregorianCalendar)

.

Field by Field Conversion from this class to

java.util.GregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA

getEonAndYear()

.signum() < 0 ? GregorianCalendar.BC : GregorianCalendar.AD

YEAR

getEonAndYear()

.abs().intValue()

*

MONTH

getMonth()

-

DatatypeConstants.JANUARY

+

Calendar.JANUARY

DAY_OF_MONTH

getDay()

HOUR_OF_DAY

getHour()

MINUTE

getMinute()

SECOND

getSecond()

MILLISECOND

get millisecond order from

getFractionalSecond()

*

GregorianCalendar.setTimeZone(TimeZone)

getTimezone()

formatted into Custom timezone id

*

designates possible loss of precision during the conversion due
to source datatype having higher precision than target datatype.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Using

timeZone

value as defined above, create a new

java.util.GregorianCalendar(timeZone,Locale.getDefault())

.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()

.
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

**Returns:** An instance of

GregorianCalendar

.
**See Also:** toGregorianCalendar(java.util.TimeZone, java.util.Locale, XMLGregorianCalendar)

- toGregorianCalendar

```java
public abstract
GregorianCalendar
toGregorianCalendar​(
TimeZone
timezone,

Locale
aLocale,

XMLGregorianCalendar
defaults)
```

Convert this

XMLGregorianCalendar

along with provided parameters
to a

GregorianCalendar

instance.

Since XML Schema 1.0 date/time datetypes has no concept of
timezone ids or daylight savings timezone ids, this conversion operation
allows the user to explicitly specify one with

timezone

parameter.

To compute the return value's

TimeZone

field,

- when parameter

timeZone

is non-null,
it is the timezone field.
- else when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else when

defaults.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using

defaults.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Create a new

java.util.GregorianCalendar(TimeZone,
Locale)

with TimeZone set as specified above and the

Locale

parameter.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

**Parameters:** timezone

- provide Timezone.

null

is a legal value.
**Parameters:** aLocale

- provide explicit Locale. Use default GregorianCalendar locale if
value is

null

.
**Parameters:** defaults

- provide default field values to use when corresponding
field for this instance is FIELD_UNDEFINED or null.
If

defaults

is

null

or a field
within the specified

defaults

is undefined,
just use

java.util.GregorianCalendar

defaults.
**Returns:** a java.util.GregorianCalendar conversion of this instance.

- getTimeZone

```java
public abstract
TimeZone
getTimeZone​(int defaultZoneoffset)
```

Returns a

java.util.TimeZone

for this class.

If timezone field is defined for this instance,
returns TimeZone initialized with custom timezone id
of zoneoffset. If timezone field is undefined,
try the defaultZoneoffset that was passed in.
If defaultZoneoffset is FIELD_UNDEFINED, return
default timezone for this host.
(Same default as java.util.GregorianCalendar).

**Parameters:** defaultZoneoffset

- default zoneoffset if this zoneoffset is

DatatypeConstants.FIELD_UNDEFINED

.
**Returns:** TimeZone for this.

- clone

```java
public abstract
Object
clone()
```

Creates and returns a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** copy of this

Object
**See Also:** Cloneable

---

#### Method Detail

clear

```java
public abstract void clear()
```

Unset all fields to undefined.

Set all int fields to

DatatypeConstants.FIELD_UNDEFINED

and reference fields
to null.

---

#### clear

public abstract void clear()

Unset all fields to undefined.

Set all int fields to

DatatypeConstants.FIELD_UNDEFINED

and reference fields
to null.

Set all int fields to

DatatypeConstants.FIELD_UNDEFINED

and reference fields
to null.

reset

```java
public abstract void reset()
```

Reset this

XMLGregorianCalendar

to its original values.

XMLGregorianCalendar

is reset to the same values as when it was created with

DatatypeFactory.newXMLGregorianCalendar()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)

,

DatatypeFactory.newXMLGregorianCalendar(
BigInteger year,
int month,
int day,
int hour,
int minute,
int second,
BigDecimal fractionalSecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(
int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(GregorianCalendar cal)

,

DatatypeFactory.newXMLGregorianCalendarDate(
int year,
int month,
int day,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
BigDecimal fractionalSecond,
int timezone)

or

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

.

reset()

is designed to allow the reuse of existing

XMLGregorianCalendar

s
thus saving resources associated with the creation of new

XMLGregorianCalendar

s.

---

#### reset

public abstract void reset()

Reset this

XMLGregorianCalendar

to its original values.

XMLGregorianCalendar

is reset to the same values as when it was created with

DatatypeFactory.newXMLGregorianCalendar()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)

,

DatatypeFactory.newXMLGregorianCalendar(
BigInteger year,
int month,
int day,
int hour,
int minute,
int second,
BigDecimal fractionalSecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(
int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(GregorianCalendar cal)

,

DatatypeFactory.newXMLGregorianCalendarDate(
int year,
int month,
int day,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
BigDecimal fractionalSecond,
int timezone)

or

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

.

reset()

is designed to allow the reuse of existing

XMLGregorianCalendar

s
thus saving resources associated with the creation of new

XMLGregorianCalendar

s.

XMLGregorianCalendar

is reset to the same values as when it was created with

DatatypeFactory.newXMLGregorianCalendar()

,

DatatypeFactory.newXMLGregorianCalendar(String lexicalRepresentation)

,

DatatypeFactory.newXMLGregorianCalendar(
BigInteger year,
int month,
int day,
int hour,
int minute,
int second,
BigDecimal fractionalSecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(
int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendar(GregorianCalendar cal)

,

DatatypeFactory.newXMLGregorianCalendarDate(
int year,
int month,
int day,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int timezone)

,

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
BigDecimal fractionalSecond,
int timezone)

or

DatatypeFactory.newXMLGregorianCalendarTime(
int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

.

reset()

is designed to allow the reuse of existing

XMLGregorianCalendar

s
thus saving resources associated with the creation of new

XMLGregorianCalendar

s.

reset()

is designed to allow the reuse of existing

XMLGregorianCalendar

s
thus saving resources associated with the creation of new

XMLGregorianCalendar

s.

setYear

```java
public abstract void setYear​(
BigInteger
year)
```

Set low and high order component of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

null

.

**Parameters:** year

- value constraints summarized in

year field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

year

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### setYear

public abstract void setYear​(

BigInteger

year)

Set low and high order component of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

null

.

Unset this field by invoking the setter with a parameter value of

null

.

setYear

```java
public abstract void setYear​(int year)
```

Set year of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Note: if the absolute value of the

year

parameter
is less than 10^9, the eon component of the XSD year field is set to

null

by this method.

**Parameters:** year

- value constraints are summarized in

year field of date/time field mapping table

.
If year is

DatatypeConstants.FIELD_UNDEFINED

, then eon is set to

null

.

---

#### setYear

public abstract void setYear​(int year)

Set year of XSD

dateTime

year field.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Note: if the absolute value of the

year

parameter
is less than 10^9, the eon component of the XSD year field is set to

null

by this method.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Note: if the absolute value of the

year

parameter
is less than 10^9, the eon component of the XSD year field is set to

null

by this method.

Note: if the absolute value of the

year

parameter
is less than 10^9, the eon component of the XSD year field is set to

null

by this method.

setMonth

```java
public abstract void setMonth​(int month)
```

Set month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** month

- value constraints summarized in

month field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

month

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### setMonth

public abstract void setMonth​(int month)

Set month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

setDay

```java
public abstract void setDay​(int day)
```

Set days in month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** day

- value constraints summarized in

day field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

day

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### setDay

public abstract void setDay​(int day)

Set days in month.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

setTimezone

```java
public abstract void setTimezone​(int offset)
```

Set the number of minutes in the timezone offset.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** offset

- value constraints summarized in

timezone field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

offset

parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### setTimezone

public abstract void setTimezone​(int offset)

Set the number of minutes in the timezone offset.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

setTime

```java
public void setTime​(int hour,
int minute,
int second)
```

Set time as one unit.

**Parameters:** hour

- value constraints are summarized in

hour field of date/time field mapping table

.
**Parameters:** minute

- value constraints are summarized in

minute field of date/time field mapping table

.
**Parameters:** second

- value constraints are summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.
**See Also:** setTime(int, int, int, BigDecimal)

---

#### setTime

public void setTime​(int hour,
int minute,
int second)

Set time as one unit.

setHour

```java
public abstract void setHour​(int hour)
```

Set hours.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** hour

- value constraints summarized in

hour field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

hour

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

---

#### setHour

public abstract void setHour​(int hour)

Set hours.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

setMinute

```java
public abstract void setMinute​(int minute)
```

Set minutes.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** minute

- value constraints summarized in

minute field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

minute

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

---

#### setMinute

public abstract void setMinute​(int minute)

Set minutes.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

setSecond

```java
public abstract void setSecond​(int second)
```

Set seconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** second

- value constraints summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

second

parameter is outside value constraints for the field as specified in

date/time field mapping table

.

---

#### setSecond

public abstract void setSecond​(int second)

Set seconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

setMillisecond

```java
public abstract void setMillisecond​(int millisecond)
```

Set milliseconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

**Parameters:** millisecond

- value constraints summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

millisecond

parameter is outside value constraints for the field as specified
in

date/time field mapping table

.

---

#### setMillisecond

public abstract void setMillisecond​(int millisecond)

Set milliseconds.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

Unset this field by invoking the setter with a parameter value of

DatatypeConstants.FIELD_UNDEFINED

.

setFractionalSecond

```java
public abstract void setFractionalSecond​(
BigDecimal
fractional)
```

Set fractional seconds.

Unset this field by invoking the setter with a parameter value of

null

.

**Parameters:** fractional

- value constraints summarized in

second field of date/time field mapping table

.
**Throws:** IllegalArgumentException

- if

fractional

parameter is outside value constraints for the field as specified
in

date/time field mapping table

.

---

#### setFractionalSecond

public abstract void setFractionalSecond​(

BigDecimal

fractional)

Set fractional seconds.

Unset this field by invoking the setter with a parameter value of

null

.

Unset this field by invoking the setter with a parameter value of

null

.

setTime

```java
public void setTime​(int hour,
int minute,
int second,

BigDecimal
fractional)
```

Set time as one unit, including the optional infinite precision
fractional seconds.

**Parameters:** hour

- value constraints are summarized in

hour field of date/time field mapping table

.
**Parameters:** minute

- value constraints are summarized in

minute field of date/time field mapping table

.
**Parameters:** second

- value constraints are summarized in

second field of date/time field mapping table

.
**Parameters:** fractional

- value of

null

indicates this optional
field is not set.
**Throws:** IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### setTime

public void setTime​(int hour,
int minute,
int second,

BigDecimal

fractional)

Set time as one unit, including the optional infinite precision
fractional seconds.

setTime

```java
public void setTime​(int hour,
int minute,
int second,
int millisecond)
```

Set time as one unit, including optional milliseconds.

**Parameters:** hour

- value constraints are summarized in

hour field of date/time field mapping table

.
**Parameters:** minute

- value constraints are summarized in

minute field of date/time field mapping table

.
**Parameters:** second

- value constraints are summarized in

second field of date/time field mapping table

.
**Parameters:** millisecond

- value of

DatatypeConstants.FIELD_UNDEFINED

indicates this
optional field is not set.
**Throws:** IllegalArgumentException

- if any parameter is
outside value constraints for the field as specified in

date/time field mapping table

.

---

#### setTime

public void setTime​(int hour,
int minute,
int second,
int millisecond)

Set time as one unit, including optional milliseconds.

getEon

```java
public abstract
BigInteger
getEon()
```

Returns the high order component for XML Schema 1.0 dateTime datatype field for

year

.

null

if this optional part of the year field is not defined.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:** The eon of this

XMLGregorianCalendar

. The value
returned is an integer multiple of 10^9.
**See Also:** getYear()

,

getEonAndYear()

---

#### getEon

public abstract

BigInteger

getEon()

Returns the high order component for XML Schema 1.0 dateTime datatype field for

year

.

null

if this optional part of the year field is not defined.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

getYear

```java
public abstract int getYear()
```

Returns the low order component for XML Schema 1.0 dateTime datatype field for

year

or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:** The year of this

XMLGregorianCalendar

.
**See Also:** getEon()

,

getEonAndYear()

---

#### getYear

public abstract int getYear()

Returns the low order component for XML Schema 1.0 dateTime datatype field for

year

or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

getEonAndYear

```java
public abstract
BigInteger
getEonAndYear()
```

Returns the XML Schema 1.0 dateTime datatype field for

year

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

**Returns:** sum of

eon

and

BigInteger.valueOf(year)

when both fields are defined. When only

year

is defined,
return it. When both

eon

and

year

are not
defined, return

null

.
**See Also:** getEon()

,

getYear()

---

#### getEonAndYear

public abstract

BigInteger

getEonAndYear()

Returns the XML Schema 1.0 dateTime datatype field for

year

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

Value constraints for this value are summarized in

year field of date/time field mapping table

.

getMonth

```java
public abstract int getMonth()
```

Returns the month of this calendar or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

month field of date/time field mapping table

.

**Returns:** The month of this

XMLGregorianCalendar

, from 1 to 12.

---

#### getMonth

public abstract int getMonth()

Returns the month of this calendar or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

month field of date/time field mapping table

.

Value constraints for this value are summarized in

month field of date/time field mapping table

.

getDay

```java
public abstract int getDay()
```

Returns the day of month or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

day field of date/time field mapping table

.

**Returns:** The day of month of this

XMLGregorianCalendar

, from 1 to 31.
**See Also:** setDay(int)

---

#### getDay

public abstract int getDay()

Returns the day of month or

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

day field of date/time field mapping table

.

Value constraints for this value are summarized in

day field of date/time field mapping table

.

getTimezone

```java
public abstract int getTimezone()
```

Returns the Timezone offset in minutes or

DatatypeConstants.FIELD_UNDEFINED

if this optional field is not defined.

Value constraints for this value are summarized in

timezone field of date/time field mapping table

.

**Returns:** The Timezone offset in minutes of this

XMLGregorianCalendar

.
**See Also:** setTimezone(int)

---

#### getTimezone

public abstract int getTimezone()

Returns the Timezone offset in minutes or

DatatypeConstants.FIELD_UNDEFINED

if this optional field is not defined.

Value constraints for this value are summarized in

timezone field of date/time field mapping table

.

Value constraints for this value are summarized in

timezone field of date/time field mapping table

.

getHour

```java
public abstract int getHour()
```

Returns the hour of day or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

hour field of date/time field mapping table

.

**Returns:** The hour of day of this

XMLGregorianCalendar

, from 0 to 23.
**See Also:** setTime(int, int, int)

---

#### getHour

public abstract int getHour()

Returns the hour of day or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

hour field of date/time field mapping table

.

Value constraints for this value are summarized in

hour field of date/time field mapping table

.

getMinute

```java
public abstract int getMinute()
```

Returns the minute of hour or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

minute field of date/time field mapping table

.

**Returns:** The minute of hour of this

XMLGregorianCalendar

, from 0 to 59.
**See Also:** setTime(int, int, int)

---

#### getMinute

public abstract int getMinute()

Returns the minute of hour or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.

Value constraints for this value are summarized in

minute field of date/time field mapping table

.

Value constraints for this value are summarized in

minute field of date/time field mapping table

.

getSecond

```java
public abstract int getSecond()
```

Returns the second of minute or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.
When this field is not defined, the optional xs:dateTime
fractional seconds field, represented by

getFractionalSecond()

and

getMillisecond()

,
must not be defined.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

**Returns:** The second of minute of this

XMLGregorianCalendar

, from 0 to 59.
**See Also:** getFractionalSecond()

,

getMillisecond()

,

setTime(int, int, int)

---

#### getSecond

public abstract int getSecond()

Returns the second of minute or

DatatypeConstants.FIELD_UNDEFINED

if this field is not defined.
When this field is not defined, the optional xs:dateTime
fractional seconds field, represented by

getFractionalSecond()

and

getMillisecond()

,
must not be defined.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

getMillisecond

```java
public int getMillisecond()
```

Returns the millisecond precision of

getFractionalSecond()

.

This method represents a convenience accessor to infinite
precision fractional second value returned by

getFractionalSecond()

. The returned value is the rounded
down to milliseconds value of

getFractionalSecond()

. When

getFractionalSecond()

returns

null

, this method must return

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

**Returns:** The millisecond precision of this

XMLGregorianCalendar

.
**See Also:** getFractionalSecond()

,

setTime(int, int, int)

---

#### getMillisecond

public int getMillisecond()

Returns the millisecond precision of

getFractionalSecond()

.

This method represents a convenience accessor to infinite
precision fractional second value returned by

getFractionalSecond()

. The returned value is the rounded
down to milliseconds value of

getFractionalSecond()

. When

getFractionalSecond()

returns

null

, this method must return

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

This method represents a convenience accessor to infinite
precision fractional second value returned by

getFractionalSecond()

. The returned value is the rounded
down to milliseconds value of

getFractionalSecond()

. When

getFractionalSecond()

returns

null

, this method must return

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

Value constraints for this value are summarized in

second field of date/time field mapping table

.

getFractionalSecond

```java
public abstract
BigDecimal
getFractionalSecond()
```

Returns fractional seconds.

null

is returned when this optional field is not defined.

Value constraints are detailed in

second field of date/time field mapping table

.

This optional field can only have a defined value when the
xs:dateTime second field, represented by

getSecond()

,
does not return

DatatypeConstants.FIELD_UNDEFINED

.

**Returns:** Fractional seconds of this

XMLGregorianCalendar

.
**See Also:** getSecond()

,

setTime(int, int, int, BigDecimal)

---

#### getFractionalSecond

public abstract

BigDecimal

getFractionalSecond()

Returns fractional seconds.

null

is returned when this optional field is not defined.

Value constraints are detailed in

second field of date/time field mapping table

.

This optional field can only have a defined value when the
xs:dateTime second field, represented by

getSecond()

,
does not return

DatatypeConstants.FIELD_UNDEFINED

.

null

is returned when this optional field is not defined.

Value constraints are detailed in

second field of date/time field mapping table

.

This optional field can only have a defined value when the
xs:dateTime second field, represented by

getSecond()

,
does not return

DatatypeConstants.FIELD_UNDEFINED

.

Value constraints are detailed in

second field of date/time field mapping table

.

This optional field can only have a defined value when the
xs:dateTime second field, represented by

getSecond()

,
does not return

DatatypeConstants.FIELD_UNDEFINED

.

This optional field can only have a defined value when the
xs:dateTime second field, represented by

getSecond()

,
does not return

DatatypeConstants.FIELD_UNDEFINED

.

compare

```java
public abstract int compare​(
XMLGregorianCalendar
xmlGregorianCalendar)
```

Compare two instances of W3C XML Schema 1.0 date/time datatypes
according to partial order relation defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7.3,

Order relation on dateTime

.

xsd:dateTime

datatype field mapping to accessors of
this class are defined in

date/time field mapping table

.

**Parameters:** xmlGregorianCalendar

- Instance of

XMLGregorianCalendar

to compare
**Returns:** The relationship between

this

XMLGregorianCalendar

and
the specified

xmlGregorianCalendar

as

DatatypeConstants.LESSER

,

DatatypeConstants.EQUAL

,

DatatypeConstants.GREATER

or

DatatypeConstants.INDETERMINATE

.
**Throws:** NullPointerException

- if

xmlGregorianCalendar

is null.

---

#### compare

public abstract int compare​(

XMLGregorianCalendar

xmlGregorianCalendar)

Compare two instances of W3C XML Schema 1.0 date/time datatypes
according to partial order relation defined in

W3C XML Schema 1.0 Part 2, Section 3.2.7.3,

Order relation on dateTime

.

xsd:dateTime

datatype field mapping to accessors of
this class are defined in

date/time field mapping table

.

xsd:dateTime

datatype field mapping to accessors of
this class are defined in

date/time field mapping table

.

normalize

```java
public abstract
XMLGregorianCalendar
normalize()
```

Normalize this instance to UTC.

2000-03-04T23:00:00+03:00 normalizes to 2000-03-04T20:00:00Z

Implements W3C XML Schema Part 2, Section 3.2.7.3 (A).

**Returns:** this

XMLGregorianCalendar

normalized to UTC.

---

#### normalize

public abstract

XMLGregorianCalendar

normalize()

Normalize this instance to UTC.

2000-03-04T23:00:00+03:00 normalizes to 2000-03-04T20:00:00Z

Implements W3C XML Schema Part 2, Section 3.2.7.3 (A).

2000-03-04T23:00:00+03:00 normalizes to 2000-03-04T20:00:00Z

Implements W3C XML Schema Part 2, Section 3.2.7.3 (A).

Implements W3C XML Schema Part 2, Section 3.2.7.3 (A).

equals

```java
public boolean equals​(
Object
obj)
```

Compares this calendar to the specified object. The result is

true

if and only if the argument is not null and is an

XMLGregorianCalendar

object that represents the same
instant in time as this object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- to compare.
**Returns:** true

when

obj

is an instance of

XMLGregorianCalendar

and

compare(XMLGregorianCalendar obj)

returns

DatatypeConstants.EQUAL

,
otherwise

false

.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this calendar to the specified object. The result is

true

if and only if the argument is not null and is an

XMLGregorianCalendar

object that represents the same
instant in time as this object.

hashCode

```java
public int hashCode()
```

Returns a hash code consistent with the definition of the equals method.

**Overrides:** hashCode

in class

Object
**Returns:** hash code of this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code consistent with the definition of the equals method.

toXMLFormat

```java
public abstract
String
toXMLFormat()
```

Return the lexical representation of

this

instance.
The format is specified in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

".

Specific target lexical representation format is determined by

getXMLSchemaType()

.

**Returns:** XML, as

String

, representation of this

XMLGregorianCalendar
**Throws:** IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin date/time datatypes.

---

#### toXMLFormat

public abstract

String

toXMLFormat()

Return the lexical representation of

this

instance.
The format is specified in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

".

Specific target lexical representation format is determined by

getXMLSchemaType()

.

Specific target lexical representation format is determined by

getXMLSchemaType()

.

getXMLSchemaType

```java
public abstract
QName
getXMLSchemaType()
```

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DATETIME

X

X

X

X

X

X

DatatypeConstants.DATE

X

X

X

DatatypeConstants.TIME

X

X

X

DatatypeConstants.GYEARMONTH

X

X

DatatypeConstants.GMONTHDAY

X

X

DatatypeConstants.GYEAR

X

DatatypeConstants.GMONTH

X

DatatypeConstants.GDAY

X

**Returns:** One of the following class constants:

DatatypeConstants.DATETIME

,

DatatypeConstants.TIME

,

DatatypeConstants.DATE

,

DatatypeConstants.GYEARMONTH

,

DatatypeConstants.GMONTHDAY

,

DatatypeConstants.GYEAR

,

DatatypeConstants.GMONTH

or

DatatypeConstants.GDAY

.
**Throws:** IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin
date/time datatypes.

---

#### getXMLSchemaType

public abstract

QName

getXMLSchemaType()

Return the name of the XML Schema date/time type that this instance
maps to. Type is computed based on fields that are set.

Required fields for XML Schema 1.0 Date/Time Datatypes.

(timezone is optional for all date/time datatypes)

Datatype

year

month

day

hour

minute

second

DatatypeConstants.DATETIME

X

X

X

X

X

X

DatatypeConstants.DATE

X

X

X

DatatypeConstants.TIME

X

X

X

DatatypeConstants.GYEARMONTH

X

X

DatatypeConstants.GMONTHDAY

X

X

DatatypeConstants.GYEAR

X

DatatypeConstants.GMONTH

X

DatatypeConstants.GDAY

X

toString

```java
public
String
toString()
```

Returns a

String

representation of this

XMLGregorianCalendar

Object

.

The result is a lexical representation generated by

toXMLFormat()

.

**Overrides:** toString

in class

Object
**Returns:** A non-

null

valid

String

representation of this

XMLGregorianCalendar

.
**Throws:** IllegalStateException

- if the combination of set fields
does not match one of the eight defined XML Schema builtin date/time datatypes.
**See Also:** toXMLFormat()

---

#### toString

public

String

toString()

Returns a

String

representation of this

XMLGregorianCalendar

Object

.

The result is a lexical representation generated by

toXMLFormat()

.

The result is a lexical representation generated by

toXMLFormat()

.

isValid

```java
public abstract boolean isValid()
```

Validate instance by

getXMLSchemaType()

constraints.

**Returns:** true if data values are valid.

---

#### isValid

public abstract boolean isValid()

Validate instance by

getXMLSchemaType()

constraints.

add

```java
public abstract void add​(
Duration
duration)
```

Add

duration

to this instance.

The computation is specified in

XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

date/time field mapping table

defines the mapping from XML Schema 1.0

dateTime

fields
to this class' representation of those fields.

**Parameters:** duration

- Duration to add to this

XMLGregorianCalendar

.
**Throws:** NullPointerException

- when

duration

parameter is

null

.

---

#### add

public abstract void add​(

Duration

duration)

Add

duration

to this instance.

The computation is specified in

XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

date/time field mapping table

defines the mapping from XML Schema 1.0

dateTime

fields
to this class' representation of those fields.

The computation is specified in

XML Schema 1.0 Part 2, Appendix E,

Adding durations to dateTimes

.

date/time field mapping table

defines the mapping from XML Schema 1.0

dateTime

fields
to this class' representation of those fields.

toGregorianCalendar

```java
public abstract
GregorianCalendar
toGregorianCalendar()
```

Convert this

XMLGregorianCalendar

to a

GregorianCalendar

.

When

this

instance has an undefined field, this
conversion relies on the

java.util.GregorianCalendar

default
for its corresponding field. A notable difference between
XML Schema 1.0 date/time datatypes and

java.util.GregorianCalendar

is that Timezone value is optional for date/time datatypes and it is
a required field for

java.util.GregorianCalendar

. See javadoc
for

java.util.TimeZone.getDefault()

on how the default
is determined. To explicitly specify the

TimeZone

instance, see

toGregorianCalendar(TimeZone, Locale, XMLGregorianCalendar)

.

Field by Field Conversion from this class to

java.util.GregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA

getEonAndYear()

.signum() < 0 ? GregorianCalendar.BC : GregorianCalendar.AD

YEAR

getEonAndYear()

.abs().intValue()

*

MONTH

getMonth()

-

DatatypeConstants.JANUARY

+

Calendar.JANUARY

DAY_OF_MONTH

getDay()

HOUR_OF_DAY

getHour()

MINUTE

getMinute()

SECOND

getSecond()

MILLISECOND

get millisecond order from

getFractionalSecond()

*

GregorianCalendar.setTimeZone(TimeZone)

getTimezone()

formatted into Custom timezone id

*

designates possible loss of precision during the conversion due
to source datatype having higher precision than target datatype.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Using

timeZone

value as defined above, create a new

java.util.GregorianCalendar(timeZone,Locale.getDefault())

.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()

.
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

**Returns:** An instance of

GregorianCalendar

.
**See Also:** toGregorianCalendar(java.util.TimeZone, java.util.Locale, XMLGregorianCalendar)

---

#### toGregorianCalendar

public abstract

GregorianCalendar

toGregorianCalendar()

Convert this

XMLGregorianCalendar

to a

GregorianCalendar

.

When

this

instance has an undefined field, this
conversion relies on the

java.util.GregorianCalendar

default
for its corresponding field. A notable difference between
XML Schema 1.0 date/time datatypes and

java.util.GregorianCalendar

is that Timezone value is optional for date/time datatypes and it is
a required field for

java.util.GregorianCalendar

. See javadoc
for

java.util.TimeZone.getDefault()

on how the default
is determined. To explicitly specify the

TimeZone

instance, see

toGregorianCalendar(TimeZone, Locale, XMLGregorianCalendar)

.

Field by Field Conversion from this class to

java.util.GregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA

getEonAndYear()

.signum() < 0 ? GregorianCalendar.BC : GregorianCalendar.AD

YEAR

getEonAndYear()

.abs().intValue()

*

MONTH

getMonth()

-

DatatypeConstants.JANUARY

+

Calendar.JANUARY

DAY_OF_MONTH

getDay()

HOUR_OF_DAY

getHour()

MINUTE

getMinute()

SECOND

getSecond()

MILLISECOND

get millisecond order from

getFractionalSecond()

*

GregorianCalendar.setTimeZone(TimeZone)

getTimezone()

formatted into Custom timezone id

*

designates possible loss of precision during the conversion due
to source datatype having higher precision than target datatype.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Using

timeZone

value as defined above, create a new

java.util.GregorianCalendar(timeZone,Locale.getDefault())

.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()

.
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

When

this

instance has an undefined field, this
conversion relies on the

java.util.GregorianCalendar

default
for its corresponding field. A notable difference between
XML Schema 1.0 date/time datatypes and

java.util.GregorianCalendar

is that Timezone value is optional for date/time datatypes and it is
a required field for

java.util.GregorianCalendar

. See javadoc
for

java.util.TimeZone.getDefault()

on how the default
is determined. To explicitly specify the

TimeZone

instance, see

toGregorianCalendar(TimeZone, Locale, XMLGregorianCalendar)

.

Field by Field Conversion from this class to

java.util.GregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA

getEonAndYear()

.signum() < 0 ? GregorianCalendar.BC : GregorianCalendar.AD

YEAR

getEonAndYear()

.abs().intValue()

*

MONTH

getMonth()

-

DatatypeConstants.JANUARY

+

Calendar.JANUARY

DAY_OF_MONTH

getDay()

HOUR_OF_DAY

getHour()

MINUTE

getMinute()

SECOND

getSecond()

MILLISECOND

get millisecond order from

getFractionalSecond()

*

GregorianCalendar.setTimeZone(TimeZone)

getTimezone()

formatted into Custom timezone id

*

designates possible loss of precision during the conversion due
to source datatype having higher precision than target datatype.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Using

timeZone

value as defined above, create a new

java.util.GregorianCalendar(timeZone,Locale.getDefault())

.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()

.
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Using

timeZone

value as defined above, create a new

java.util.GregorianCalendar(timeZone,Locale.getDefault())

.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()

.
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

Using

timeZone

value as defined above, create a new

java.util.GregorianCalendar(timeZone,Locale.getDefault())

.

Initialize all GregorianCalendar fields by calling

Calendar.clear()

.

Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.

Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

toGregorianCalendar

```java
public abstract
GregorianCalendar
toGregorianCalendar​(
TimeZone
timezone,

Locale
aLocale,

XMLGregorianCalendar
defaults)
```

Convert this

XMLGregorianCalendar

along with provided parameters
to a

GregorianCalendar

instance.

Since XML Schema 1.0 date/time datetypes has no concept of
timezone ids or daylight savings timezone ids, this conversion operation
allows the user to explicitly specify one with

timezone

parameter.

To compute the return value's

TimeZone

field,

- when parameter

timeZone

is non-null,
it is the timezone field.
- else when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else when

defaults.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using

defaults.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Create a new

java.util.GregorianCalendar(TimeZone,
Locale)

with TimeZone set as specified above and the

Locale

parameter.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

**Parameters:** timezone

- provide Timezone.

null

is a legal value.
**Parameters:** aLocale

- provide explicit Locale. Use default GregorianCalendar locale if
value is

null

.
**Parameters:** defaults

- provide default field values to use when corresponding
field for this instance is FIELD_UNDEFINED or null.
If

defaults

is

null

or a field
within the specified

defaults

is undefined,
just use

java.util.GregorianCalendar

defaults.
**Returns:** a java.util.GregorianCalendar conversion of this instance.

---

#### toGregorianCalendar

public abstract

GregorianCalendar

toGregorianCalendar​(

TimeZone

timezone,

Locale

aLocale,

XMLGregorianCalendar

defaults)

Convert this

XMLGregorianCalendar

along with provided parameters
to a

GregorianCalendar

instance.

Since XML Schema 1.0 date/time datetypes has no concept of
timezone ids or daylight savings timezone ids, this conversion operation
allows the user to explicitly specify one with

timezone

parameter.

To compute the return value's

TimeZone

field,

- when parameter

timeZone

is non-null,
it is the timezone field.
- else when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else when

defaults.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using

defaults.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Create a new

java.util.GregorianCalendar(TimeZone,
Locale)

with TimeZone set as specified above and the

Locale

parameter.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

Since XML Schema 1.0 date/time datetypes has no concept of
timezone ids or daylight savings timezone ids, this conversion operation
allows the user to explicitly specify one with

timezone

parameter.

To compute the return value's

TimeZone

field,

- when parameter

timeZone

is non-null,
it is the timezone field.
- else when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else when

defaults.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using

defaults.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Create a new

java.util.GregorianCalendar(TimeZone,
Locale)

with TimeZone set as specified above and the

Locale

parameter.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

To compute the return value's

TimeZone

field,

- when parameter

timeZone

is non-null,
it is the timezone field.
- else when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else when

defaults.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using

defaults.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Create a new

java.util.GregorianCalendar(TimeZone,
Locale)

with TimeZone set as specified above and the

Locale

parameter.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

when parameter

timeZone

is non-null,
it is the timezone field.

else when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.

else when

defaults.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using

defaults.getTimezone()

.

else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

To ensure consistency in conversion implementations, the new

GregorianCalendar

should be instantiated in following
manner.

- Create a new

java.util.GregorianCalendar(TimeZone,
Locale)

with TimeZone set as specified above and the

Locale

parameter.
- Initialize all GregorianCalendar fields by calling

Calendar.clear()
- Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.
- Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

Create a new

java.util.GregorianCalendar(TimeZone,
Locale)

with TimeZone set as specified above and the

Locale

parameter.

Initialize all GregorianCalendar fields by calling

Calendar.clear()

Obtain a pure Gregorian Calendar by invoking

GregorianCalendar.setGregorianChange(
new Date(Long.MIN_VALUE))

.

Its fields ERA, YEAR, MONTH, DAY_OF_MONTH, HOUR_OF_DAY,
MINUTE, SECOND and MILLISECOND are set using the method

Calendar.set(int,int)

getTimeZone

```java
public abstract
TimeZone
getTimeZone​(int defaultZoneoffset)
```

Returns a

java.util.TimeZone

for this class.

If timezone field is defined for this instance,
returns TimeZone initialized with custom timezone id
of zoneoffset. If timezone field is undefined,
try the defaultZoneoffset that was passed in.
If defaultZoneoffset is FIELD_UNDEFINED, return
default timezone for this host.
(Same default as java.util.GregorianCalendar).

**Parameters:** defaultZoneoffset

- default zoneoffset if this zoneoffset is

DatatypeConstants.FIELD_UNDEFINED

.
**Returns:** TimeZone for this.

---

#### getTimeZone

public abstract

TimeZone

getTimeZone​(int defaultZoneoffset)

Returns a

java.util.TimeZone

for this class.

If timezone field is defined for this instance,
returns TimeZone initialized with custom timezone id
of zoneoffset. If timezone field is undefined,
try the defaultZoneoffset that was passed in.
If defaultZoneoffset is FIELD_UNDEFINED, return
default timezone for this host.
(Same default as java.util.GregorianCalendar).

If timezone field is defined for this instance,
returns TimeZone initialized with custom timezone id
of zoneoffset. If timezone field is undefined,
try the defaultZoneoffset that was passed in.
If defaultZoneoffset is FIELD_UNDEFINED, return
default timezone for this host.
(Same default as java.util.GregorianCalendar).

clone

```java
public abstract
Object
clone()
```

Creates and returns a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** copy of this

Object
**See Also:** Cloneable

---

#### clone

public abstract

Object

clone()

Creates and returns a copy of this object.

---

