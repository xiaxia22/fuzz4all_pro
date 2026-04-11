# Class DatatypeFactory

**Source:** `java.xml\javax\xml\datatype\DatatypeFactory.html`

### Class Description

```java
public abstract class
DatatypeFactory

extends
Object
```

Factory that creates new

javax.xml.datatype

Object

s that map XML to/from Java

Object

s.

A new instance of the

DatatypeFactory

is created through the

newInstance()

method
that uses the following implementation resolution mechanisms to determine an implementation:

- If the system property specified by

DATATYPEFACTORY_PROPERTY

, "

javax.xml.datatype.DatatypeFactory

",
exists, a class with the name of the property value is instantiated.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt
to locate and load an implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

In case of

service
configuration error

, a

DatatypeConfigurationException

will be thrown.
- The final mechanism is to attempt to instantiate the

Class

specified by

DATATYPEFACTORY_IMPLEMENTATION_CLASS

.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.

**Since:** 1.5

---

### Field Details

#### public static final
String
DATATYPEFACTORY_PROPERTY

Default property name as defined in JSR 206: Java(TM) API for XML Processing (JAXP) 1.3.

Default value is

javax.xml.datatype.DatatypeFactory

.

**See Also:**
- Constant Field Values

---

#### public static final
String
DATATYPEFACTORY_IMPLEMENTATION_CLASS

Default implementation class name as defined in

JSR 206: Java(TM) API for XML Processing (JAXP) 1.3

.

Implementers should specify the name of an appropriate class
to be instantiated if no other implementation resolution mechanism
succeeds.

Users should not refer to this field; it is intended only to
document a factory implementation detail.

---

### Constructor Details

#### protected DatatypeFactory()

Protected constructor to prevent instantiation outside of package.

Use

newInstance()

to create a

DatatypeFactory

.

---

### Method Details

#### public static
DatatypeFactory
newDefaultInstance()

Creates a new instance of the

DatatypeFactory

builtin system-default
implementation

.

**Returns:**
- A new instance of the

DatatypeFactory

builtin
system-default implementation.

**Since:**
- 9

---

#### public static
DatatypeFactory
newInstance()
throws
DatatypeConfigurationException

Obtain a new instance of a

DatatypeFactory

.

The implementation resolution mechanisms are

defined

in this

Class

's documentation.

**Returns:**
- New instance of a

DatatypeFactory

**Throws:**
- DatatypeConfigurationException

- If the implementation is not
available or cannot be instantiated.

**See Also:**
- newInstance(String factoryClassName, ClassLoader classLoader)

---

#### public static
DatatypeFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
throws
DatatypeConfigurationException

Obtain a new instance of a

DatatypeFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DatatypeFactory

it can use the factory to configure and obtain datatype instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:**
- factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.datatype.DatatypeFactory

.
- classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.

**Returns:**
- New instance of a

DatatypeFactory

**Throws:**
- DatatypeConfigurationException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.

**See Also:**
- newInstance()

**Since:**
- 1.6

---

#### public abstract
Duration
newDuration​(
String
lexicalRepresentation)

Obtain a new instance of a

Duration

specifying the

Duration

as its string representation, "PnYnMnDTnHnMnS",
as defined in XML Schema 1.0 section 3.2.6.1.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:**
- lexicalRepresentation

-

String

representation of a

Duration

.

**Returns:**
- New

Duration

created from parsing the

lexicalRepresentation

.

**Throws:**
- IllegalArgumentException

- If

lexicalRepresentation

is not a valid representation of a

Duration

.
- UnsupportedOperationException

- If implementation cannot support requested values.
- NullPointerException

- if

lexicalRepresentation

is

null

.

---

#### public abstract
Duration
newDuration​(long durationInMilliSeconds)

Obtain a new instance of a

Duration

specifying the

Duration

as milliseconds.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

and

Duration.getDays()

can be influenced.

**Parameters:**
- durationInMilliSeconds

- Duration in milliseconds to create.

**Returns:**
- New

Duration

representing

durationInMilliSeconds

.

---

#### public abstract
Duration
newDuration​(boolean isPositive,

BigInteger
years,

BigInteger
months,

BigInteger
days,

BigInteger
hours,

BigInteger
minutes,

BigDecimal
seconds)

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:**
- isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
- years

- of this

Duration
- months

- of this

Duration
- days

- of this

Duration
- hours

- of this

Duration
- minutes

- of this

Duration
- seconds

- of this

Duration

**Returns:**
- New

Duration

created from the specified values.

**Throws:**
- IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all the fields (years, months, ...) are null or
if any of the fields is negative.
- UnsupportedOperationException

- If implementation cannot support requested values.

---

#### public
Duration
newDuration​(boolean isPositive,
int years,
int months,
int days,
int hours,
int minutes,
int seconds)

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:**
- isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
- years

- of this

Duration
- months

- of this

Duration
- days

- of this

Duration
- hours

- of this

Duration
- minutes

- of this

Duration
- seconds

- of this

Duration

**Returns:**
- New

Duration

created from the specified values.

**Throws:**
- IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields is negative.

**See Also:**
- newDuration(
boolean isPositive,
BigInteger years,
BigInteger months,
BigInteger days,
BigInteger hours,
BigInteger minutes,
BigDecimal seconds)

---

#### public
Duration
newDurationDayTime​(
String
lexicalRepresentation)

Create a

Duration

of type

xdt:dayTimeDuration

by parsing its

String

representation,
"

PnDTnHnMnS

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:**
- lexicalRepresentation

- Lexical representation of a duration.

**Returns:**
- New

Duration

created using the specified

lexicalRepresentation

.

**Throws:**
- IllegalArgumentException

- If

lexicalRepresentation

is
not a valid representation of a

Duration

expressed only in terms of days and time.
- UnsupportedOperationException

- If implementation cannot support requested values.
- NullPointerException

- If

lexicalRepresentation

is

null

.

---

#### public
Duration
newDurationDayTime​(long durationInMilliseconds)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getDays()

can be influenced.

Any remaining milliseconds after determining the day, hour, minute and second are discarded.

**Parameters:**
- durationInMilliseconds

- Milliseconds of

Duration

to create.

**Returns:**
- New

Duration

created with the specified

durationInMilliseconds

.

**See Also:**
- XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

---

#### public
Duration
newDurationDayTime​(boolean isPositive,

BigInteger
day,

BigInteger
hour,

BigInteger
minute,

BigInteger
second)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:**
- isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
- day

- Day of

Duration

.
- hour

- Hour of

Duration

.
- minute

- Minute of

Duration

.
- second

- Second of

Duration

.

**Returns:**
- New

Duration

created with the specified

day

,

hour

,

minute

and

second

.

**Throws:**
- IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all the fields (day, hour, ...) are null or
if any of the fields is negative.
- UnsupportedOperationException

- If implementation cannot support requested values.

---

#### public
Duration
newDurationDayTime​(boolean isPositive,
int day,
int hour,
int minute,
int second)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:**
- isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
- day

- Day of

Duration

.
- hour

- Hour of

Duration

.
- minute

- Minute of

Duration

.
- second

- Second of

Duration

.

**Returns:**
- New

Duration

created with the specified

day

,

hour

,

minute

and

second

.

**Throws:**
- IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields (day, hour, ...) is negative.

---

#### public
Duration
newDurationYearMonth​(
String
lexicalRepresentation)

Create a

Duration

of type

xdt:yearMonthDuration

by parsing its

String

representation,
"

PnYnM

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting
arbitrarily large and/or small values. An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:**
- lexicalRepresentation

- Lexical representation of a duration.

**Returns:**
- New

Duration

created using the specified

lexicalRepresentation

.

**Throws:**
- IllegalArgumentException

- If

lexicalRepresentation

is not a valid representation of a

Duration

expressed only in terms of years and months.
- UnsupportedOperationException

- If implementation cannot support requested values.
- NullPointerException

- If

lexicalRepresentation

is

null

.

---

#### public
Duration
newDurationYearMonth​(long durationInMilliseconds)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

can be influenced.

Any remaining milliseconds after determining the year and month are discarded.

**Parameters:**
- durationInMilliseconds

- Milliseconds of

Duration

to create.

**Returns:**
- New

Duration

created using the specified

durationInMilliseconds

.

---

#### public
Duration
newDurationYearMonth​(boolean isPositive,

BigInteger
year,

BigInteger
month)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:**
- isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
- year

- Year of

Duration

.
- month

- Month of

Duration

.

**Returns:**
- New

Duration

created using the specified

year

and

month

.

**Throws:**
- IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all of the fields (year, month) are null or
if any of the fields is negative.
- UnsupportedOperationException

- If implementation cannot support requested values.

---

#### public
Duration
newDurationYearMonth​(boolean isPositive,
int year,
int month)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:**
- isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
- year

- Year of

Duration

.
- month

- Month of

Duration

.

**Returns:**
- New

Duration

created using the specified

year

and

month

.

**Throws:**
- IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields (year, month) is negative.

---

#### public abstract
XMLGregorianCalendar
newXMLGregorianCalendar()

Create a new instance of an

XMLGregorianCalendar

.

All date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

**Returns:**
- New

XMLGregorianCalendar

with all date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

---

#### public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
String
lexicalRepresentation)

Create a new XMLGregorianCalendar by parsing the String as a lexical representation.

Parsing the lexical string representation is defined in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

.

The string representation may not have any leading and trailing whitespaces.

The parsing is done field by field so that
the following holds for any lexically correct String x:

```java
newXMLGregorianCalendar(x).toXMLFormat().equals(x)
```

Except for the noted lexical/canonical representation mismatches
listed in

XML Schema 1.0 errata, Section 3.2.7.2

.

**Parameters:**
- lexicalRepresentation

- Lexical representation of one the eight XML Schema date/time datatypes.

**Returns:**
- XMLGregorianCalendar

created from the

lexicalRepresentation

.

**Throws:**
- IllegalArgumentException

- If the

lexicalRepresentation

is not a valid

XMLGregorianCalendar

.
- NullPointerException

- If

lexicalRepresentation

is

null

.

---

#### public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
GregorianCalendar
cal)

Create an

XMLGregorianCalendar

from a

GregorianCalendar

.

Field by Field Conversion from

GregorianCalendar

to an

XMLGregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA == GregorianCalendar.BC ? -YEAR : YEAR

XMLGregorianCalendar.setYear(int year)

MONTH + 1

XMLGregorianCalendar.setMonth(int month)

DAY_OF_MONTH

XMLGregorianCalendar.setDay(int day)

HOUR_OF_DAY, MINUTE, SECOND, MILLISECOND

XMLGregorianCalendar.setTime(int hour, int minute, int second, BigDecimal fractional)

(ZONE_OFFSET + DST_OFFSET) / (60*1000)

(in minutes)

XMLGregorianCalendar.setTimezone(int offset)

*

*

conversion loss of information. It is not possible to represent
a

java.util.GregorianCalendar

daylight savings timezone id in the
XML Schema 1.0 date/time datatype representation.

To compute the return value's

TimeZone

field,

- when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

**Parameters:**
- cal

-

java.util.GregorianCalendar

used to create

XMLGregorianCalendar

**Returns:**
- XMLGregorianCalendar

created from

java.util.GregorianCalendar

**Throws:**
- NullPointerException

- If

cal

is

null

.

---

#### public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
BigInteger
year,
int month,
int day,
int hour,
int minute,
int second,

BigDecimal
fractionalSecond,
int timezone)

Constructor allowing for complete value spaces allowed by
W3C XML Schema 1.0 recommendation for xsd:dateTime and related
builtin datatypes. Note that

year

parameter supports
arbitrarily large numbers and fractionalSecond has infinite
precision.

A

null

value indicates that field is not set.

**Parameters:**
- year

- of

XMLGregorianCalendar

to be created.
- month

- of

XMLGregorianCalendar

to be created.
- day

- of

XMLGregorianCalendar

to be created.
- hour

- of

XMLGregorianCalendar

to be created.
- minute

- of

XMLGregorianCalendar

to be created.
- second

- of

XMLGregorianCalendar

to be created.
- fractionalSecond

- of

XMLGregorianCalendar

to be created.
- timezone

- of

XMLGregorianCalendar

to be created.

**Returns:**
- XMLGregorianCalendar

created from specified values.

**Throws:**
- IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

---

#### public
XMLGregorianCalendar
newXMLGregorianCalendar​(int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

Constructor of value spaces that a

java.util.GregorianCalendar

instance would need to convert to an

XMLGregorianCalendar

instance.

XMLGregorianCalendar eon

and

fractionalSecond

are set to

null

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:**
- year

- of

XMLGregorianCalendar

to be created.
- month

- of

XMLGregorianCalendar

to be created.
- day

- of

XMLGregorianCalendar

to be created.
- hour

- of

XMLGregorianCalendar

to be created.
- minute

- of

XMLGregorianCalendar

to be created.
- second

- of

XMLGregorianCalendar

to be created.
- millisecond

- of

XMLGregorianCalendar

to be created.
- timezone

- of

XMLGregorianCalendar

to be created.

**Returns:**
- XMLGregorianCalendar

created from specified values.

**Throws:**
- IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

---

#### public
XMLGregorianCalendar
newXMLGregorianCalendarDate​(int year,
int month,
int day,
int timezone)

Create a Java representation of XML Schema builtin datatype

date

or

g*

.

For example, an instance of

gYear

can be created invoking this factory
with

month

and

day

parameters set to

DatatypeConstants.FIELD_UNDEFINED

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:**
- year

- of

XMLGregorianCalendar

to be created.
- month

- of

XMLGregorianCalendar

to be created.
- day

- of

XMLGregorianCalendar

to be created.
- timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.

**Returns:**
- XMLGregorianCalendar

created from parameter values.

**Throws:**
- IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

**See Also:**
- DatatypeConstants.FIELD_UNDEFINED

---

#### public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int timezone)

Create a Java instance of XML Schema builtin datatype

time

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:**
- hours

- number of hours
- minutes

- number of minutes
- seconds

- number of seconds
- timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.

**Returns:**
- XMLGregorianCalendar

created from parameter values.

**Throws:**
- IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

**See Also:**
- DatatypeConstants.FIELD_UNDEFINED

---

#### public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,

BigDecimal
fractionalSecond,
int timezone)

Create a Java instance of XML Schema builtin datatype time.

A

null

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:**
- hours

- number of hours
- minutes

- number of minutes
- seconds

- number of seconds
- fractionalSecond

- value of

null

indicates that this optional field is not set.
- timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.

**Returns:**
- XMLGregorianCalendar

created from parameter values.

**Throws:**
- IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

**See Also:**
- DatatypeConstants.FIELD_UNDEFINED

---

#### public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

Create a Java instance of XML Schema builtin datatype time.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:**
- hours

- number of hours
- minutes

- number of minutes
- seconds

- number of seconds
- milliseconds

- number of milliseconds
- timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.

**Returns:**
- XMLGregorianCalendar

created from parameter values.

**Throws:**
- IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

**See Also:**
- DatatypeConstants.FIELD_UNDEFINED

---

### Additional Sections

#### Class DatatypeFactory

java.lang.Object

- javax.xml.datatype.DatatypeFactory

javax.xml.datatype.DatatypeFactory

```java
public abstract class
DatatypeFactory

extends
Object
```

Factory that creates new

javax.xml.datatype

Object

s that map XML to/from Java

Object

s.

A new instance of the

DatatypeFactory

is created through the

newInstance()

method
that uses the following implementation resolution mechanisms to determine an implementation:

- If the system property specified by

DATATYPEFACTORY_PROPERTY

, "

javax.xml.datatype.DatatypeFactory

",
exists, a class with the name of the property value is instantiated.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt
to locate and load an implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

In case of

service
configuration error

, a

DatatypeConfigurationException

will be thrown.
- The final mechanism is to attempt to instantiate the

Class

specified by

DATATYPEFACTORY_IMPLEMENTATION_CLASS

.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.

**Since:** 1.5

public abstract class

DatatypeFactory

extends

Object

Factory that creates new

javax.xml.datatype

Object

s that map XML to/from Java

Object

s.

A new instance of the

DatatypeFactory

is created through the

newInstance()

method
that uses the following implementation resolution mechanisms to determine an implementation:

- If the system property specified by

DATATYPEFACTORY_PROPERTY

, "

javax.xml.datatype.DatatypeFactory

",
exists, a class with the name of the property value is instantiated.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt
to locate and load an implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

In case of

service
configuration error

, a

DatatypeConfigurationException

will be thrown.
- The final mechanism is to attempt to instantiate the

Class

specified by

DATATYPEFACTORY_IMPLEMENTATION_CLASS

.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.

A new instance of the

DatatypeFactory

is created through the

newInstance()

method
that uses the following implementation resolution mechanisms to determine an implementation:

- If the system property specified by

DATATYPEFACTORY_PROPERTY

, "

javax.xml.datatype.DatatypeFactory

",
exists, a class with the name of the property value is instantiated.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt
to locate and load an implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

In case of

service
configuration error

, a

DatatypeConfigurationException

will be thrown.
- The final mechanism is to attempt to instantiate the

Class

specified by

DATATYPEFACTORY_IMPLEMENTATION_CLASS

.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.

If the system property specified by

DATATYPEFACTORY_PROPERTY

, "

javax.xml.datatype.DatatypeFactory

",
exists, a class with the name of the property value is instantiated.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.

Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.

Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt
to locate and load an implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

In case of

service
configuration error

, a

DatatypeConfigurationException

will be thrown.

The final mechanism is to attempt to instantiate the

Class

specified by

DATATYPEFACTORY_IMPLEMENTATION_CLASS

.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.

Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.

Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt
to locate and load an implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

In case of

service
configuration error

, a

DatatypeConfigurationException

will be thrown.

In case of

service
configuration error

, a

DatatypeConfigurationException

will be thrown.

The final mechanism is to attempt to instantiate the

Class

specified by

DATATYPEFACTORY_IMPLEMENTATION_CLASS

.
Any Exception thrown during the instantiation process is wrapped as a

DatatypeConfigurationException

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

DATATYPEFACTORY_IMPLEMENTATION_CLASS

Default implementation class name as defined in

JSR 206: Java(TM) API for XML Processing (JAXP) 1.3

.

static

String

DATATYPEFACTORY_PROPERTY

Default property name as defined in JSR 206: Java(TM) API for XML Processing (JAXP) 1.3.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DatatypeFactory

()

Protected constructor to prevent instantiation outside of package.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

DatatypeFactory

newDefaultInstance

()

Creates a new instance of the

DatatypeFactory

builtin system-default
implementation

.

Duration

newDuration

​(boolean isPositive,
int years,
int months,
int days,
int hours,
int minutes,
int seconds)

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

abstract

Duration

newDuration

​(boolean isPositive,

BigInteger

years,

BigInteger

months,

BigInteger

days,

BigInteger

hours,

BigInteger

minutes,

BigDecimal

seconds)

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

abstract

Duration

newDuration

​(long durationInMilliSeconds)

Obtain a new instance of a

Duration

specifying the

Duration

as milliseconds.

abstract

Duration

newDuration

​(

String

lexicalRepresentation)

Obtain a new instance of a

Duration

specifying the

Duration

as its string representation, "PnYnMnDTnHnMnS",
as defined in XML Schema 1.0 section 3.2.6.1.

Duration

newDurationDayTime

​(boolean isPositive,
int day,
int hour,
int minute,
int second)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Duration

newDurationDayTime

​(boolean isPositive,

BigInteger

day,

BigInteger

hour,

BigInteger

minute,

BigInteger

second)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Duration

newDurationDayTime

​(long durationInMilliseconds)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Duration

newDurationDayTime

​(

String

lexicalRepresentation)

Create a

Duration

of type

xdt:dayTimeDuration

by parsing its

String

representation,
"

PnDTnHnMnS

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Duration

newDurationYearMonth

​(boolean isPositive,
int year,
int month)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

Duration

newDurationYearMonth

​(boolean isPositive,

BigInteger

year,

BigInteger

month)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

Duration

newDurationYearMonth

​(long durationInMilliseconds)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

Duration

newDurationYearMonth

​(

String

lexicalRepresentation)

Create a

Duration

of type

xdt:yearMonthDuration

by parsing its

String

representation,
"

PnYnM

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

static

DatatypeFactory

newInstance

()

Obtain a new instance of a

DatatypeFactory

.

static

DatatypeFactory

newInstance

​(

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

DatatypeFactory

from class name.

abstract

XMLGregorianCalendar

newXMLGregorianCalendar

()

Create a new instance of an

XMLGregorianCalendar

.

XMLGregorianCalendar

newXMLGregorianCalendar

​(int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

Constructor of value spaces that a

java.util.GregorianCalendar

instance would need to convert to an

XMLGregorianCalendar

instance.

abstract

XMLGregorianCalendar

newXMLGregorianCalendar

​(

String

lexicalRepresentation)

Create a new XMLGregorianCalendar by parsing the String as a lexical representation.

abstract

XMLGregorianCalendar

newXMLGregorianCalendar

​(

BigInteger

year,
int month,
int day,
int hour,
int minute,
int second,

BigDecimal

fractionalSecond,
int timezone)

Constructor allowing for complete value spaces allowed by
W3C XML Schema 1.0 recommendation for xsd:dateTime and related
builtin datatypes.

abstract

XMLGregorianCalendar

newXMLGregorianCalendar

​(

GregorianCalendar

cal)

Create an

XMLGregorianCalendar

from a

GregorianCalendar

.

XMLGregorianCalendar

newXMLGregorianCalendarDate

​(int year,
int month,
int day,
int timezone)

Create a Java representation of XML Schema builtin datatype

date

or

g*

.

XMLGregorianCalendar

newXMLGregorianCalendarTime

​(int hours,
int minutes,
int seconds,
int timezone)

Create a Java instance of XML Schema builtin datatype

time

.

XMLGregorianCalendar

newXMLGregorianCalendarTime

​(int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

Create a Java instance of XML Schema builtin datatype time.

XMLGregorianCalendar

newXMLGregorianCalendarTime

​(int hours,
int minutes,
int seconds,

BigDecimal

fractionalSecond,
int timezone)

Create a Java instance of XML Schema builtin datatype time.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

DATATYPEFACTORY_IMPLEMENTATION_CLASS

Default implementation class name as defined in

JSR 206: Java(TM) API for XML Processing (JAXP) 1.3

.

static

String

DATATYPEFACTORY_PROPERTY

Default property name as defined in JSR 206: Java(TM) API for XML Processing (JAXP) 1.3.

---

#### Field Summary

Default implementation class name as defined in

JSR 206: Java(TM) API for XML Processing (JAXP) 1.3

.

Default property name as defined in JSR 206: Java(TM) API for XML Processing (JAXP) 1.3.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DatatypeFactory

()

Protected constructor to prevent instantiation outside of package.

---

#### Constructor Summary

Protected constructor to prevent instantiation outside of package.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

DatatypeFactory

newDefaultInstance

()

Creates a new instance of the

DatatypeFactory

builtin system-default
implementation

.

Duration

newDuration

​(boolean isPositive,
int years,
int months,
int days,
int hours,
int minutes,
int seconds)

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

abstract

Duration

newDuration

​(boolean isPositive,

BigInteger

years,

BigInteger

months,

BigInteger

days,

BigInteger

hours,

BigInteger

minutes,

BigDecimal

seconds)

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

abstract

Duration

newDuration

​(long durationInMilliSeconds)

Obtain a new instance of a

Duration

specifying the

Duration

as milliseconds.

abstract

Duration

newDuration

​(

String

lexicalRepresentation)

Obtain a new instance of a

Duration

specifying the

Duration

as its string representation, "PnYnMnDTnHnMnS",
as defined in XML Schema 1.0 section 3.2.6.1.

Duration

newDurationDayTime

​(boolean isPositive,
int day,
int hour,
int minute,
int second)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Duration

newDurationDayTime

​(boolean isPositive,

BigInteger

day,

BigInteger

hour,

BigInteger

minute,

BigInteger

second)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Duration

newDurationDayTime

​(long durationInMilliseconds)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Duration

newDurationDayTime

​(

String

lexicalRepresentation)

Create a

Duration

of type

xdt:dayTimeDuration

by parsing its

String

representation,
"

PnDTnHnMnS

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Duration

newDurationYearMonth

​(boolean isPositive,
int year,
int month)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

Duration

newDurationYearMonth

​(boolean isPositive,

BigInteger

year,

BigInteger

month)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

Duration

newDurationYearMonth

​(long durationInMilliseconds)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

Duration

newDurationYearMonth

​(

String

lexicalRepresentation)

Create a

Duration

of type

xdt:yearMonthDuration

by parsing its

String

representation,
"

PnYnM

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

static

DatatypeFactory

newInstance

()

Obtain a new instance of a

DatatypeFactory

.

static

DatatypeFactory

newInstance

​(

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

DatatypeFactory

from class name.

abstract

XMLGregorianCalendar

newXMLGregorianCalendar

()

Create a new instance of an

XMLGregorianCalendar

.

XMLGregorianCalendar

newXMLGregorianCalendar

​(int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

Constructor of value spaces that a

java.util.GregorianCalendar

instance would need to convert to an

XMLGregorianCalendar

instance.

abstract

XMLGregorianCalendar

newXMLGregorianCalendar

​(

String

lexicalRepresentation)

Create a new XMLGregorianCalendar by parsing the String as a lexical representation.

abstract

XMLGregorianCalendar

newXMLGregorianCalendar

​(

BigInteger

year,
int month,
int day,
int hour,
int minute,
int second,

BigDecimal

fractionalSecond,
int timezone)

Constructor allowing for complete value spaces allowed by
W3C XML Schema 1.0 recommendation for xsd:dateTime and related
builtin datatypes.

abstract

XMLGregorianCalendar

newXMLGregorianCalendar

​(

GregorianCalendar

cal)

Create an

XMLGregorianCalendar

from a

GregorianCalendar

.

XMLGregorianCalendar

newXMLGregorianCalendarDate

​(int year,
int month,
int day,
int timezone)

Create a Java representation of XML Schema builtin datatype

date

or

g*

.

XMLGregorianCalendar

newXMLGregorianCalendarTime

​(int hours,
int minutes,
int seconds,
int timezone)

Create a Java instance of XML Schema builtin datatype

time

.

XMLGregorianCalendar

newXMLGregorianCalendarTime

​(int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

Create a Java instance of XML Schema builtin datatype time.

XMLGregorianCalendar

newXMLGregorianCalendarTime

​(int hours,
int minutes,
int seconds,

BigDecimal

fractionalSecond,
int timezone)

Create a Java instance of XML Schema builtin datatype time.

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

Creates a new instance of the

DatatypeFactory

builtin system-default
implementation

.

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

Obtain a new instance of a

Duration

specifying the

Duration

as milliseconds.

Obtain a new instance of a

Duration

specifying the

Duration

as its string representation, "PnYnMnDTnHnMnS",
as defined in XML Schema 1.0 section 3.2.6.1.

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Create a

Duration

of type

xdt:dayTimeDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Create a

Duration

of type

xdt:dayTimeDuration

by parsing its

String

representation,
"

PnDTnHnMnS

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

Create a

Duration

of type

xdt:yearMonthDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

Create a

Duration

of type

xdt:yearMonthDuration

by parsing its

String

representation,
"

PnYnM

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

Obtain a new instance of a

DatatypeFactory

.

Obtain a new instance of a

DatatypeFactory

from class name.

Create a new instance of an

XMLGregorianCalendar

.

Constructor of value spaces that a

java.util.GregorianCalendar

instance would need to convert to an

XMLGregorianCalendar

instance.

Create a new XMLGregorianCalendar by parsing the String as a lexical representation.

Constructor allowing for complete value spaces allowed by
W3C XML Schema 1.0 recommendation for xsd:dateTime and related
builtin datatypes.

Create an

XMLGregorianCalendar

from a

GregorianCalendar

.

Create a Java representation of XML Schema builtin datatype

date

or

g*

.

Create a Java instance of XML Schema builtin datatype

time

.

Create a Java instance of XML Schema builtin datatype time.

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

============ FIELD DETAIL ===========

- Field Detail

- DATATYPEFACTORY_PROPERTY

```java
public static final
String
DATATYPEFACTORY_PROPERTY
```

Default property name as defined in JSR 206: Java(TM) API for XML Processing (JAXP) 1.3.

Default value is

javax.xml.datatype.DatatypeFactory

.

**See Also:** Constant Field Values

- DATATYPEFACTORY_IMPLEMENTATION_CLASS

```java
public static final
String
DATATYPEFACTORY_IMPLEMENTATION_CLASS
```

Default implementation class name as defined in

JSR 206: Java(TM) API for XML Processing (JAXP) 1.3

.

Implementers should specify the name of an appropriate class
to be instantiated if no other implementation resolution mechanism
succeeds.

Users should not refer to this field; it is intended only to
document a factory implementation detail.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DatatypeFactory

```java
protected DatatypeFactory()
```

Protected constructor to prevent instantiation outside of package.

Use

newInstance()

to create a

DatatypeFactory

.

============ METHOD DETAIL ==========

- Method Detail

- newDefaultInstance

```java
public static
DatatypeFactory
newDefaultInstance()
```

Creates a new instance of the

DatatypeFactory

builtin system-default
implementation

.

**Returns:** A new instance of the

DatatypeFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
DatatypeFactory
newInstance()
throws
DatatypeConfigurationException
```

Obtain a new instance of a

DatatypeFactory

.

The implementation resolution mechanisms are

defined

in this

Class

's documentation.

**Returns:** New instance of a

DatatypeFactory
**Throws:** DatatypeConfigurationException

- If the implementation is not
available or cannot be instantiated.
**See Also:** newInstance(String factoryClassName, ClassLoader classLoader)

- newInstance

```java
public static
DatatypeFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
throws
DatatypeConfigurationException
```

Obtain a new instance of a

DatatypeFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DatatypeFactory

it can use the factory to configure and obtain datatype instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.datatype.DatatypeFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** New instance of a

DatatypeFactory
**Throws:** DatatypeConfigurationException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.
**Since:** 1.6
**See Also:** newInstance()

- newDuration

```java
public abstract
Duration
newDuration​(
String
lexicalRepresentation)
```

Obtain a new instance of a

Duration

specifying the

Duration

as its string representation, "PnYnMnDTnHnMnS",
as defined in XML Schema 1.0 section 3.2.6.1.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:** lexicalRepresentation

-

String

representation of a

Duration

.
**Returns:** New

Duration

created from parsing the

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If

lexicalRepresentation

is not a valid representation of a

Duration

.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.
**Throws:** NullPointerException

- if

lexicalRepresentation

is

null

.

- newDuration

```java
public abstract
Duration
newDuration​(long durationInMilliSeconds)
```

Obtain a new instance of a

Duration

specifying the

Duration

as milliseconds.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

and

Duration.getDays()

can be influenced.

**Parameters:** durationInMilliSeconds

- Duration in milliseconds to create.
**Returns:** New

Duration

representing

durationInMilliSeconds

.

- newDuration

```java
public abstract
Duration
newDuration​(boolean isPositive,

BigInteger
years,

BigInteger
months,

BigInteger
days,

BigInteger
hours,

BigInteger
minutes,

BigDecimal
seconds)
```

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** years

- of this

Duration
**Parameters:** months

- of this

Duration
**Parameters:** days

- of this

Duration
**Parameters:** hours

- of this

Duration
**Parameters:** minutes

- of this

Duration
**Parameters:** seconds

- of this

Duration
**Returns:** New

Duration

created from the specified values.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all the fields (years, months, ...) are null or
if any of the fields is negative.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.

- newDuration

```java
public
Duration
newDuration​(boolean isPositive,
int years,
int months,
int days,
int hours,
int minutes,
int seconds)
```

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** years

- of this

Duration
**Parameters:** months

- of this

Duration
**Parameters:** days

- of this

Duration
**Parameters:** hours

- of this

Duration
**Parameters:** minutes

- of this

Duration
**Parameters:** seconds

- of this

Duration
**Returns:** New

Duration

created from the specified values.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields is negative.
**See Also:** newDuration(
boolean isPositive,
BigInteger years,
BigInteger months,
BigInteger days,
BigInteger hours,
BigInteger minutes,
BigDecimal seconds)

- newDurationDayTime

```java
public
Duration
newDurationDayTime​(
String
lexicalRepresentation)
```

Create a

Duration

of type

xdt:dayTimeDuration

by parsing its

String

representation,
"

PnDTnHnMnS

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:** lexicalRepresentation

- Lexical representation of a duration.
**Returns:** New

Duration

created using the specified

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If

lexicalRepresentation

is
not a valid representation of a

Duration

expressed only in terms of days and time.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.
**Throws:** NullPointerException

- If

lexicalRepresentation

is

null

.

- newDurationDayTime

```java
public
Duration
newDurationDayTime​(long durationInMilliseconds)
```

Create a

Duration

of type

xdt:dayTimeDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getDays()

can be influenced.

Any remaining milliseconds after determining the day, hour, minute and second are discarded.

**Parameters:** durationInMilliseconds

- Milliseconds of

Duration

to create.
**Returns:** New

Duration

created with the specified

durationInMilliseconds

.
**See Also:** XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

- newDurationDayTime

```java
public
Duration
newDurationDayTime​(boolean isPositive,

BigInteger
day,

BigInteger
hour,

BigInteger
minute,

BigInteger
second)
```

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** day

- Day of

Duration

.
**Parameters:** hour

- Hour of

Duration

.
**Parameters:** minute

- Minute of

Duration

.
**Parameters:** second

- Second of

Duration

.
**Returns:** New

Duration

created with the specified

day

,

hour

,

minute

and

second

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all the fields (day, hour, ...) are null or
if any of the fields is negative.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.

- newDurationDayTime

```java
public
Duration
newDurationDayTime​(boolean isPositive,
int day,
int hour,
int minute,
int second)
```

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** day

- Day of

Duration

.
**Parameters:** hour

- Hour of

Duration

.
**Parameters:** minute

- Minute of

Duration

.
**Parameters:** second

- Second of

Duration

.
**Returns:** New

Duration

created with the specified

day

,

hour

,

minute

and

second

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields (day, hour, ...) is negative.

- newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(
String
lexicalRepresentation)
```

Create a

Duration

of type

xdt:yearMonthDuration

by parsing its

String

representation,
"

PnYnM

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting
arbitrarily large and/or small values. An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:** lexicalRepresentation

- Lexical representation of a duration.
**Returns:** New

Duration

created using the specified

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If

lexicalRepresentation

is not a valid representation of a

Duration

expressed only in terms of years and months.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.
**Throws:** NullPointerException

- If

lexicalRepresentation

is

null

.

- newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(long durationInMilliseconds)
```

Create a

Duration

of type

xdt:yearMonthDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

can be influenced.

Any remaining milliseconds after determining the year and month are discarded.

**Parameters:** durationInMilliseconds

- Milliseconds of

Duration

to create.
**Returns:** New

Duration

created using the specified

durationInMilliseconds

.

- newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(boolean isPositive,

BigInteger
year,

BigInteger
month)
```

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** year

- Year of

Duration

.
**Parameters:** month

- Month of

Duration

.
**Returns:** New

Duration

created using the specified

year

and

month

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all of the fields (year, month) are null or
if any of the fields is negative.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.

- newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(boolean isPositive,
int year,
int month)
```

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** year

- Year of

Duration

.
**Parameters:** month

- Month of

Duration

.
**Returns:** New

Duration

created using the specified

year

and

month

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields (year, month) is negative.

- newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar()
```

Create a new instance of an

XMLGregorianCalendar

.

All date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

**Returns:** New

XMLGregorianCalendar

with all date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

- newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
String
lexicalRepresentation)
```

Create a new XMLGregorianCalendar by parsing the String as a lexical representation.

Parsing the lexical string representation is defined in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

.

The string representation may not have any leading and trailing whitespaces.

The parsing is done field by field so that
the following holds for any lexically correct String x:

```java
newXMLGregorianCalendar(x).toXMLFormat().equals(x)
```

Except for the noted lexical/canonical representation mismatches
listed in

XML Schema 1.0 errata, Section 3.2.7.2

.

**Parameters:** lexicalRepresentation

- Lexical representation of one the eight XML Schema date/time datatypes.
**Returns:** XMLGregorianCalendar

created from the

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If the

lexicalRepresentation

is not a valid

XMLGregorianCalendar

.
**Throws:** NullPointerException

- If

lexicalRepresentation

is

null

.

- newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
GregorianCalendar
cal)
```

Create an

XMLGregorianCalendar

from a

GregorianCalendar

.

Field by Field Conversion from

GregorianCalendar

to an

XMLGregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA == GregorianCalendar.BC ? -YEAR : YEAR

XMLGregorianCalendar.setYear(int year)

MONTH + 1

XMLGregorianCalendar.setMonth(int month)

DAY_OF_MONTH

XMLGregorianCalendar.setDay(int day)

HOUR_OF_DAY, MINUTE, SECOND, MILLISECOND

XMLGregorianCalendar.setTime(int hour, int minute, int second, BigDecimal fractional)

(ZONE_OFFSET + DST_OFFSET) / (60*1000)

(in minutes)

XMLGregorianCalendar.setTimezone(int offset)

*

*

conversion loss of information. It is not possible to represent
a

java.util.GregorianCalendar

daylight savings timezone id in the
XML Schema 1.0 date/time datatype representation.

To compute the return value's

TimeZone

field,

- when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

**Parameters:** cal

-

java.util.GregorianCalendar

used to create

XMLGregorianCalendar
**Returns:** XMLGregorianCalendar

created from

java.util.GregorianCalendar
**Throws:** NullPointerException

- If

cal

is

null

.

- newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
BigInteger
year,
int month,
int day,
int hour,
int minute,
int second,

BigDecimal
fractionalSecond,
int timezone)
```

Constructor allowing for complete value spaces allowed by
W3C XML Schema 1.0 recommendation for xsd:dateTime and related
builtin datatypes. Note that

year

parameter supports
arbitrarily large numbers and fractionalSecond has infinite
precision.

A

null

value indicates that field is not set.

**Parameters:** year

- of

XMLGregorianCalendar

to be created.
**Parameters:** month

- of

XMLGregorianCalendar

to be created.
**Parameters:** day

- of

XMLGregorianCalendar

to be created.
**Parameters:** hour

- of

XMLGregorianCalendar

to be created.
**Parameters:** minute

- of

XMLGregorianCalendar

to be created.
**Parameters:** second

- of

XMLGregorianCalendar

to be created.
**Parameters:** fractionalSecond

- of

XMLGregorianCalendar

to be created.
**Parameters:** timezone

- of

XMLGregorianCalendar

to be created.
**Returns:** XMLGregorianCalendar

created from specified values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

- newXMLGregorianCalendar

```java
public
XMLGregorianCalendar
newXMLGregorianCalendar​(int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)
```

Constructor of value spaces that a

java.util.GregorianCalendar

instance would need to convert to an

XMLGregorianCalendar

instance.

XMLGregorianCalendar eon

and

fractionalSecond

are set to

null

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** year

- of

XMLGregorianCalendar

to be created.
**Parameters:** month

- of

XMLGregorianCalendar

to be created.
**Parameters:** day

- of

XMLGregorianCalendar

to be created.
**Parameters:** hour

- of

XMLGregorianCalendar

to be created.
**Parameters:** minute

- of

XMLGregorianCalendar

to be created.
**Parameters:** second

- of

XMLGregorianCalendar

to be created.
**Parameters:** millisecond

- of

XMLGregorianCalendar

to be created.
**Parameters:** timezone

- of

XMLGregorianCalendar

to be created.
**Returns:** XMLGregorianCalendar

created from specified values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

- newXMLGregorianCalendarDate

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarDate​(int year,
int month,
int day,
int timezone)
```

Create a Java representation of XML Schema builtin datatype

date

or

g*

.

For example, an instance of

gYear

can be created invoking this factory
with

month

and

day

parameters set to

DatatypeConstants.FIELD_UNDEFINED

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** year

- of

XMLGregorianCalendar

to be created.
**Parameters:** month

- of

XMLGregorianCalendar

to be created.
**Parameters:** day

- of

XMLGregorianCalendar

to be created.
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

- newXMLGregorianCalendarTime

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int timezone)
```

Create a Java instance of XML Schema builtin datatype

time

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** hours

- number of hours
**Parameters:** minutes

- number of minutes
**Parameters:** seconds

- number of seconds
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

- newXMLGregorianCalendarTime

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,

BigDecimal
fractionalSecond,
int timezone)
```

Create a Java instance of XML Schema builtin datatype time.

A

null

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** hours

- number of hours
**Parameters:** minutes

- number of minutes
**Parameters:** seconds

- number of seconds
**Parameters:** fractionalSecond

- value of

null

indicates that this optional field is not set.
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

- newXMLGregorianCalendarTime

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)
```

Create a Java instance of XML Schema builtin datatype time.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** hours

- number of hours
**Parameters:** minutes

- number of minutes
**Parameters:** seconds

- number of seconds
**Parameters:** milliseconds

- number of milliseconds
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

Field Detail

- DATATYPEFACTORY_PROPERTY

```java
public static final
String
DATATYPEFACTORY_PROPERTY
```

Default property name as defined in JSR 206: Java(TM) API for XML Processing (JAXP) 1.3.

Default value is

javax.xml.datatype.DatatypeFactory

.

**See Also:** Constant Field Values

- DATATYPEFACTORY_IMPLEMENTATION_CLASS

```java
public static final
String
DATATYPEFACTORY_IMPLEMENTATION_CLASS
```

Default implementation class name as defined in

JSR 206: Java(TM) API for XML Processing (JAXP) 1.3

.

Implementers should specify the name of an appropriate class
to be instantiated if no other implementation resolution mechanism
succeeds.

Users should not refer to this field; it is intended only to
document a factory implementation detail.

---

#### Field Detail

DATATYPEFACTORY_PROPERTY

```java
public static final
String
DATATYPEFACTORY_PROPERTY
```

Default property name as defined in JSR 206: Java(TM) API for XML Processing (JAXP) 1.3.

Default value is

javax.xml.datatype.DatatypeFactory

.

**See Also:** Constant Field Values

---

#### DATATYPEFACTORY_PROPERTY

public static final

String

DATATYPEFACTORY_PROPERTY

Default property name as defined in JSR 206: Java(TM) API for XML Processing (JAXP) 1.3.

Default value is

javax.xml.datatype.DatatypeFactory

.

Default value is

javax.xml.datatype.DatatypeFactory

.

DATATYPEFACTORY_IMPLEMENTATION_CLASS

```java
public static final
String
DATATYPEFACTORY_IMPLEMENTATION_CLASS
```

Default implementation class name as defined in

JSR 206: Java(TM) API for XML Processing (JAXP) 1.3

.

Implementers should specify the name of an appropriate class
to be instantiated if no other implementation resolution mechanism
succeeds.

Users should not refer to this field; it is intended only to
document a factory implementation detail.

---

#### DATATYPEFACTORY_IMPLEMENTATION_CLASS

public static final

String

DATATYPEFACTORY_IMPLEMENTATION_CLASS

Default implementation class name as defined in

JSR 206: Java(TM) API for XML Processing (JAXP) 1.3

.

Implementers should specify the name of an appropriate class
to be instantiated if no other implementation resolution mechanism
succeeds.

Users should not refer to this field; it is intended only to
document a factory implementation detail.

Implementers should specify the name of an appropriate class
to be instantiated if no other implementation resolution mechanism
succeeds.

Users should not refer to this field; it is intended only to
document a factory implementation detail.

Users should not refer to this field; it is intended only to
document a factory implementation detail.

Constructor Detail

- DatatypeFactory

```java
protected DatatypeFactory()
```

Protected constructor to prevent instantiation outside of package.

Use

newInstance()

to create a

DatatypeFactory

.

---

#### Constructor Detail

DatatypeFactory

```java
protected DatatypeFactory()
```

Protected constructor to prevent instantiation outside of package.

Use

newInstance()

to create a

DatatypeFactory

.

---

#### DatatypeFactory

protected DatatypeFactory()

Protected constructor to prevent instantiation outside of package.

Use

newInstance()

to create a

DatatypeFactory

.

Use

newInstance()

to create a

DatatypeFactory

.

Method Detail

- newDefaultInstance

```java
public static
DatatypeFactory
newDefaultInstance()
```

Creates a new instance of the

DatatypeFactory

builtin system-default
implementation

.

**Returns:** A new instance of the

DatatypeFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
DatatypeFactory
newInstance()
throws
DatatypeConfigurationException
```

Obtain a new instance of a

DatatypeFactory

.

The implementation resolution mechanisms are

defined

in this

Class

's documentation.

**Returns:** New instance of a

DatatypeFactory
**Throws:** DatatypeConfigurationException

- If the implementation is not
available or cannot be instantiated.
**See Also:** newInstance(String factoryClassName, ClassLoader classLoader)

- newInstance

```java
public static
DatatypeFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
throws
DatatypeConfigurationException
```

Obtain a new instance of a

DatatypeFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DatatypeFactory

it can use the factory to configure and obtain datatype instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.datatype.DatatypeFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** New instance of a

DatatypeFactory
**Throws:** DatatypeConfigurationException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.
**Since:** 1.6
**See Also:** newInstance()

- newDuration

```java
public abstract
Duration
newDuration​(
String
lexicalRepresentation)
```

Obtain a new instance of a

Duration

specifying the

Duration

as its string representation, "PnYnMnDTnHnMnS",
as defined in XML Schema 1.0 section 3.2.6.1.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:** lexicalRepresentation

-

String

representation of a

Duration

.
**Returns:** New

Duration

created from parsing the

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If

lexicalRepresentation

is not a valid representation of a

Duration

.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.
**Throws:** NullPointerException

- if

lexicalRepresentation

is

null

.

- newDuration

```java
public abstract
Duration
newDuration​(long durationInMilliSeconds)
```

Obtain a new instance of a

Duration

specifying the

Duration

as milliseconds.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

and

Duration.getDays()

can be influenced.

**Parameters:** durationInMilliSeconds

- Duration in milliseconds to create.
**Returns:** New

Duration

representing

durationInMilliSeconds

.

- newDuration

```java
public abstract
Duration
newDuration​(boolean isPositive,

BigInteger
years,

BigInteger
months,

BigInteger
days,

BigInteger
hours,

BigInteger
minutes,

BigDecimal
seconds)
```

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** years

- of this

Duration
**Parameters:** months

- of this

Duration
**Parameters:** days

- of this

Duration
**Parameters:** hours

- of this

Duration
**Parameters:** minutes

- of this

Duration
**Parameters:** seconds

- of this

Duration
**Returns:** New

Duration

created from the specified values.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all the fields (years, months, ...) are null or
if any of the fields is negative.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.

- newDuration

```java
public
Duration
newDuration​(boolean isPositive,
int years,
int months,
int days,
int hours,
int minutes,
int seconds)
```

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** years

- of this

Duration
**Parameters:** months

- of this

Duration
**Parameters:** days

- of this

Duration
**Parameters:** hours

- of this

Duration
**Parameters:** minutes

- of this

Duration
**Parameters:** seconds

- of this

Duration
**Returns:** New

Duration

created from the specified values.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields is negative.
**See Also:** newDuration(
boolean isPositive,
BigInteger years,
BigInteger months,
BigInteger days,
BigInteger hours,
BigInteger minutes,
BigDecimal seconds)

- newDurationDayTime

```java
public
Duration
newDurationDayTime​(
String
lexicalRepresentation)
```

Create a

Duration

of type

xdt:dayTimeDuration

by parsing its

String

representation,
"

PnDTnHnMnS

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:** lexicalRepresentation

- Lexical representation of a duration.
**Returns:** New

Duration

created using the specified

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If

lexicalRepresentation

is
not a valid representation of a

Duration

expressed only in terms of days and time.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.
**Throws:** NullPointerException

- If

lexicalRepresentation

is

null

.

- newDurationDayTime

```java
public
Duration
newDurationDayTime​(long durationInMilliseconds)
```

Create a

Duration

of type

xdt:dayTimeDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getDays()

can be influenced.

Any remaining milliseconds after determining the day, hour, minute and second are discarded.

**Parameters:** durationInMilliseconds

- Milliseconds of

Duration

to create.
**Returns:** New

Duration

created with the specified

durationInMilliseconds

.
**See Also:** XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

- newDurationDayTime

```java
public
Duration
newDurationDayTime​(boolean isPositive,

BigInteger
day,

BigInteger
hour,

BigInteger
minute,

BigInteger
second)
```

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** day

- Day of

Duration

.
**Parameters:** hour

- Hour of

Duration

.
**Parameters:** minute

- Minute of

Duration

.
**Parameters:** second

- Second of

Duration

.
**Returns:** New

Duration

created with the specified

day

,

hour

,

minute

and

second

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all the fields (day, hour, ...) are null or
if any of the fields is negative.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.

- newDurationDayTime

```java
public
Duration
newDurationDayTime​(boolean isPositive,
int day,
int hour,
int minute,
int second)
```

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** day

- Day of

Duration

.
**Parameters:** hour

- Hour of

Duration

.
**Parameters:** minute

- Minute of

Duration

.
**Parameters:** second

- Second of

Duration

.
**Returns:** New

Duration

created with the specified

day

,

hour

,

minute

and

second

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields (day, hour, ...) is negative.

- newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(
String
lexicalRepresentation)
```

Create a

Duration

of type

xdt:yearMonthDuration

by parsing its

String

representation,
"

PnYnM

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting
arbitrarily large and/or small values. An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:** lexicalRepresentation

- Lexical representation of a duration.
**Returns:** New

Duration

created using the specified

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If

lexicalRepresentation

is not a valid representation of a

Duration

expressed only in terms of years and months.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.
**Throws:** NullPointerException

- If

lexicalRepresentation

is

null

.

- newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(long durationInMilliseconds)
```

Create a

Duration

of type

xdt:yearMonthDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

can be influenced.

Any remaining milliseconds after determining the year and month are discarded.

**Parameters:** durationInMilliseconds

- Milliseconds of

Duration

to create.
**Returns:** New

Duration

created using the specified

durationInMilliseconds

.

- newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(boolean isPositive,

BigInteger
year,

BigInteger
month)
```

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** year

- Year of

Duration

.
**Parameters:** month

- Month of

Duration

.
**Returns:** New

Duration

created using the specified

year

and

month

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all of the fields (year, month) are null or
if any of the fields is negative.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.

- newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(boolean isPositive,
int year,
int month)
```

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** year

- Year of

Duration

.
**Parameters:** month

- Month of

Duration

.
**Returns:** New

Duration

created using the specified

year

and

month

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields (year, month) is negative.

- newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar()
```

Create a new instance of an

XMLGregorianCalendar

.

All date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

**Returns:** New

XMLGregorianCalendar

with all date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

- newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
String
lexicalRepresentation)
```

Create a new XMLGregorianCalendar by parsing the String as a lexical representation.

Parsing the lexical string representation is defined in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

.

The string representation may not have any leading and trailing whitespaces.

The parsing is done field by field so that
the following holds for any lexically correct String x:

```java
newXMLGregorianCalendar(x).toXMLFormat().equals(x)
```

Except for the noted lexical/canonical representation mismatches
listed in

XML Schema 1.0 errata, Section 3.2.7.2

.

**Parameters:** lexicalRepresentation

- Lexical representation of one the eight XML Schema date/time datatypes.
**Returns:** XMLGregorianCalendar

created from the

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If the

lexicalRepresentation

is not a valid

XMLGregorianCalendar

.
**Throws:** NullPointerException

- If

lexicalRepresentation

is

null

.

- newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
GregorianCalendar
cal)
```

Create an

XMLGregorianCalendar

from a

GregorianCalendar

.

Field by Field Conversion from

GregorianCalendar

to an

XMLGregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA == GregorianCalendar.BC ? -YEAR : YEAR

XMLGregorianCalendar.setYear(int year)

MONTH + 1

XMLGregorianCalendar.setMonth(int month)

DAY_OF_MONTH

XMLGregorianCalendar.setDay(int day)

HOUR_OF_DAY, MINUTE, SECOND, MILLISECOND

XMLGregorianCalendar.setTime(int hour, int minute, int second, BigDecimal fractional)

(ZONE_OFFSET + DST_OFFSET) / (60*1000)

(in minutes)

XMLGregorianCalendar.setTimezone(int offset)

*

*

conversion loss of information. It is not possible to represent
a

java.util.GregorianCalendar

daylight savings timezone id in the
XML Schema 1.0 date/time datatype representation.

To compute the return value's

TimeZone

field,

- when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

**Parameters:** cal

-

java.util.GregorianCalendar

used to create

XMLGregorianCalendar
**Returns:** XMLGregorianCalendar

created from

java.util.GregorianCalendar
**Throws:** NullPointerException

- If

cal

is

null

.

- newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
BigInteger
year,
int month,
int day,
int hour,
int minute,
int second,

BigDecimal
fractionalSecond,
int timezone)
```

Constructor allowing for complete value spaces allowed by
W3C XML Schema 1.0 recommendation for xsd:dateTime and related
builtin datatypes. Note that

year

parameter supports
arbitrarily large numbers and fractionalSecond has infinite
precision.

A

null

value indicates that field is not set.

**Parameters:** year

- of

XMLGregorianCalendar

to be created.
**Parameters:** month

- of

XMLGregorianCalendar

to be created.
**Parameters:** day

- of

XMLGregorianCalendar

to be created.
**Parameters:** hour

- of

XMLGregorianCalendar

to be created.
**Parameters:** minute

- of

XMLGregorianCalendar

to be created.
**Parameters:** second

- of

XMLGregorianCalendar

to be created.
**Parameters:** fractionalSecond

- of

XMLGregorianCalendar

to be created.
**Parameters:** timezone

- of

XMLGregorianCalendar

to be created.
**Returns:** XMLGregorianCalendar

created from specified values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

- newXMLGregorianCalendar

```java
public
XMLGregorianCalendar
newXMLGregorianCalendar​(int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)
```

Constructor of value spaces that a

java.util.GregorianCalendar

instance would need to convert to an

XMLGregorianCalendar

instance.

XMLGregorianCalendar eon

and

fractionalSecond

are set to

null

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** year

- of

XMLGregorianCalendar

to be created.
**Parameters:** month

- of

XMLGregorianCalendar

to be created.
**Parameters:** day

- of

XMLGregorianCalendar

to be created.
**Parameters:** hour

- of

XMLGregorianCalendar

to be created.
**Parameters:** minute

- of

XMLGregorianCalendar

to be created.
**Parameters:** second

- of

XMLGregorianCalendar

to be created.
**Parameters:** millisecond

- of

XMLGregorianCalendar

to be created.
**Parameters:** timezone

- of

XMLGregorianCalendar

to be created.
**Returns:** XMLGregorianCalendar

created from specified values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

- newXMLGregorianCalendarDate

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarDate​(int year,
int month,
int day,
int timezone)
```

Create a Java representation of XML Schema builtin datatype

date

or

g*

.

For example, an instance of

gYear

can be created invoking this factory
with

month

and

day

parameters set to

DatatypeConstants.FIELD_UNDEFINED

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** year

- of

XMLGregorianCalendar

to be created.
**Parameters:** month

- of

XMLGregorianCalendar

to be created.
**Parameters:** day

- of

XMLGregorianCalendar

to be created.
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

- newXMLGregorianCalendarTime

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int timezone)
```

Create a Java instance of XML Schema builtin datatype

time

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** hours

- number of hours
**Parameters:** minutes

- number of minutes
**Parameters:** seconds

- number of seconds
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

- newXMLGregorianCalendarTime

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,

BigDecimal
fractionalSecond,
int timezone)
```

Create a Java instance of XML Schema builtin datatype time.

A

null

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** hours

- number of hours
**Parameters:** minutes

- number of minutes
**Parameters:** seconds

- number of seconds
**Parameters:** fractionalSecond

- value of

null

indicates that this optional field is not set.
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

- newXMLGregorianCalendarTime

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)
```

Create a Java instance of XML Schema builtin datatype time.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** hours

- number of hours
**Parameters:** minutes

- number of minutes
**Parameters:** seconds

- number of seconds
**Parameters:** milliseconds

- number of milliseconds
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

---

#### Method Detail

newDefaultInstance

```java
public static
DatatypeFactory
newDefaultInstance()
```

Creates a new instance of the

DatatypeFactory

builtin system-default
implementation

.

**Returns:** A new instance of the

DatatypeFactory

builtin
system-default implementation.
**Since:** 9

---

#### newDefaultInstance

public static

DatatypeFactory

newDefaultInstance()

Creates a new instance of the

DatatypeFactory

builtin system-default
implementation

.

newInstance

```java
public static
DatatypeFactory
newInstance()
throws
DatatypeConfigurationException
```

Obtain a new instance of a

DatatypeFactory

.

The implementation resolution mechanisms are

defined

in this

Class

's documentation.

**Returns:** New instance of a

DatatypeFactory
**Throws:** DatatypeConfigurationException

- If the implementation is not
available or cannot be instantiated.
**See Also:** newInstance(String factoryClassName, ClassLoader classLoader)

---

#### newInstance

public static

DatatypeFactory

newInstance()
throws

DatatypeConfigurationException

Obtain a new instance of a

DatatypeFactory

.

The implementation resolution mechanisms are

defined

in this

Class

's documentation.

The implementation resolution mechanisms are

defined

in this

Class

's documentation.

newInstance

```java
public static
DatatypeFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
throws
DatatypeConfigurationException
```

Obtain a new instance of a

DatatypeFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DatatypeFactory

it can use the factory to configure and obtain datatype instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.datatype.DatatypeFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** New instance of a

DatatypeFactory
**Throws:** DatatypeConfigurationException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.
**Since:** 1.6
**See Also:** newInstance()

---

#### newInstance

public static

DatatypeFactory

newInstance​(

String

factoryClassName,

ClassLoader

classLoader)
throws

DatatypeConfigurationException

Obtain a new instance of a

DatatypeFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DatatypeFactory

it can use the factory to configure and obtain datatype instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

Once an application has obtained a reference to a

DatatypeFactory

it can use the factory to configure and obtain datatype instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

---

#### Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

java -Djaxp.debug=1 YourProgram ....

newDuration

```java
public abstract
Duration
newDuration​(
String
lexicalRepresentation)
```

Obtain a new instance of a

Duration

specifying the

Duration

as its string representation, "PnYnMnDTnHnMnS",
as defined in XML Schema 1.0 section 3.2.6.1.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:** lexicalRepresentation

-

String

representation of a

Duration

.
**Returns:** New

Duration

created from parsing the

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If

lexicalRepresentation

is not a valid representation of a

Duration

.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.
**Throws:** NullPointerException

- if

lexicalRepresentation

is

null

.

---

#### newDuration

public abstract

Duration

newDuration​(

String

lexicalRepresentation)

Obtain a new instance of a

Duration

specifying the

Duration

as its string representation, "PnYnMnDTnHnMnS",
as defined in XML Schema 1.0 section 3.2.6.1.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

All six values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

newDuration

```java
public abstract
Duration
newDuration​(long durationInMilliSeconds)
```

Obtain a new instance of a

Duration

specifying the

Duration

as milliseconds.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

and

Duration.getDays()

can be influenced.

**Parameters:** durationInMilliSeconds

- Duration in milliseconds to create.
**Returns:** New

Duration

representing

durationInMilliSeconds

.

---

#### newDuration

public abstract

Duration

newDuration​(long durationInMilliSeconds)

Obtain a new instance of a

Duration

specifying the

Duration

as milliseconds.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

and

Duration.getDays()

can be influenced.

XML Schema Part 2: Datatypes, 3.2.6 duration, defines

duration

as:

duration represents a duration of time.
The value space of duration is a six-dimensional space where the coordinates designate the
Gregorian year, month, day, hour, minute, and second components defined in Section 5.5.3.2 of [ISO 8601], respectively.
These components are ordered in their significance by their order of appearance i.e. as
year, month, day, hour, minute, and second.

All six values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

and

Duration.getDays()

can be influenced.

All six values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

and

Duration.getDays()

can be influenced.

ISO 8601:2000(E) Section 5.5.3.2 Alternative format

W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats

XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

and

Duration.getDays()

can be influenced.

newDuration

```java
public abstract
Duration
newDuration​(boolean isPositive,

BigInteger
years,

BigInteger
months,

BigInteger
days,

BigInteger
hours,

BigInteger
minutes,

BigDecimal
seconds)
```

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** years

- of this

Duration
**Parameters:** months

- of this

Duration
**Parameters:** days

- of this

Duration
**Parameters:** hours

- of this

Duration
**Parameters:** minutes

- of this

Duration
**Parameters:** seconds

- of this

Duration
**Returns:** New

Duration

created from the specified values.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all the fields (years, months, ...) are null or
if any of the fields is negative.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.

---

#### newDuration

public abstract

Duration

newDuration​(boolean isPositive,

BigInteger

years,

BigInteger

months,

BigInteger

days,

BigInteger

hours,

BigInteger

minutes,

BigDecimal

seconds)

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

A

null

value indicates that field is not set.

newDuration

```java
public
Duration
newDuration​(boolean isPositive,
int years,
int months,
int days,
int hours,
int minutes,
int seconds)
```

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** years

- of this

Duration
**Parameters:** months

- of this

Duration
**Parameters:** days

- of this

Duration
**Parameters:** hours

- of this

Duration
**Parameters:** minutes

- of this

Duration
**Parameters:** seconds

- of this

Duration
**Returns:** New

Duration

created from the specified values.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields is negative.
**See Also:** newDuration(
boolean isPositive,
BigInteger years,
BigInteger months,
BigInteger days,
BigInteger hours,
BigInteger minutes,
BigDecimal seconds)

---

#### newDuration

public

Duration

newDuration​(boolean isPositive,
int years,
int months,
int days,
int hours,
int minutes,
int seconds)

Obtain a new instance of a

Duration

specifying the

Duration

as isPositive, years, months, days, hours, minutes, seconds.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

newDurationDayTime

```java
public
Duration
newDurationDayTime​(
String
lexicalRepresentation)
```

Create a

Duration

of type

xdt:dayTimeDuration

by parsing its

String

representation,
"

PnDTnHnMnS

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:** lexicalRepresentation

- Lexical representation of a duration.
**Returns:** New

Duration

created using the specified

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If

lexicalRepresentation

is
not a valid representation of a

Duration

expressed only in terms of days and time.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.
**Throws:** NullPointerException

- If

lexicalRepresentation

is

null

.

---

#### newDurationDayTime

public

Duration

newDurationDayTime​(

String

lexicalRepresentation)

Create a

Duration

of type

xdt:dayTimeDuration

by parsing its

String

representation,
"

PnDTnHnMnS

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

All four values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

newDurationDayTime

```java
public
Duration
newDurationDayTime​(long durationInMilliseconds)
```

Create a

Duration

of type

xdt:dayTimeDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getDays()

can be influenced.

Any remaining milliseconds after determining the day, hour, minute and second are discarded.

**Parameters:** durationInMilliseconds

- Milliseconds of

Duration

to create.
**Returns:** New

Duration

created with the specified

durationInMilliseconds

.
**See Also:** XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

---

#### newDurationDayTime

public

Duration

newDurationDayTime​(long durationInMilliseconds)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getDays()

can be influenced.

Any remaining milliseconds after determining the day, hour, minute and second are discarded.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

All four values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getDays()

can be influenced.

Any remaining milliseconds after determining the day, hour, minute and second are discarded.

All four values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getDays()

can be influenced.

Any remaining milliseconds after determining the day, hour, minute and second are discarded.

ISO 8601:2000(E) Section 5.5.3.2 Alternative format

W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats

XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getDays()

can be influenced.

Any remaining milliseconds after determining the day, hour, minute and second are discarded.

Any remaining milliseconds after determining the day, hour, minute and second are discarded.

newDurationDayTime

```java
public
Duration
newDurationDayTime​(boolean isPositive,

BigInteger
day,

BigInteger
hour,

BigInteger
minute,

BigInteger
second)
```

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** day

- Day of

Duration

.
**Parameters:** hour

- Hour of

Duration

.
**Parameters:** minute

- Minute of

Duration

.
**Parameters:** second

- Second of

Duration

.
**Returns:** New

Duration

created with the specified

day

,

hour

,

minute

and

second

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all the fields (day, hour, ...) are null or
if any of the fields is negative.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.

---

#### newDurationDayTime

public

Duration

newDurationDayTime​(boolean isPositive,

BigInteger

day,

BigInteger

hour,

BigInteger

minute,

BigInteger

second)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

A

null

value indicates that field is not set.

newDurationDayTime

```java
public
Duration
newDurationDayTime​(boolean isPositive,
int day,
int hour,
int minute,
int second)
```

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** day

- Day of

Duration

.
**Parameters:** hour

- Hour of

Duration

.
**Parameters:** minute

- Minute of

Duration

.
**Parameters:** second

- Second of

Duration

.
**Returns:** New

Duration

created with the specified

day

,

hour

,

minute

and

second

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields (day, hour, ...) is negative.

---

#### newDurationDayTime

public

Duration

newDurationDayTime​(boolean isPositive,
int day,
int hour,
int minute,
int second)

Create a

Duration

of type

xdt:dayTimeDuration

using the specified

day

,

hour

,

minute

and

second

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration

.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

The datatype

xdt:dayTimeDuration

is a subtype of

xs:duration

whose lexical representation contains only day, hour, minute, and second components.
This datatype resides in the namespace

http://www.w3.org/2003/11/xpath-datatypes

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(
String
lexicalRepresentation)
```

Create a

Duration

of type

xdt:yearMonthDuration

by parsing its

String

representation,
"

PnYnM

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting
arbitrarily large and/or small values. An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

**Parameters:** lexicalRepresentation

- Lexical representation of a duration.
**Returns:** New

Duration

created using the specified

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If

lexicalRepresentation

is not a valid representation of a

Duration

expressed only in terms of years and months.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.
**Throws:** NullPointerException

- If

lexicalRepresentation

is

null

.

---

#### newDurationYearMonth

public

Duration

newDurationYearMonth​(

String

lexicalRepresentation)

Create a

Duration

of type

xdt:yearMonthDuration

by parsing its

String

representation,
"

PnYnM

",

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting
arbitrarily large and/or small values. An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting
arbitrarily large and/or small values. An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

Both values are set and available from the created

Duration

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting
arbitrarily large and/or small values. An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting
arbitrarily large and/or small values. An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(long durationInMilliseconds)
```

Create a

Duration

of type

xdt:yearMonthDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

can be influenced.

Any remaining milliseconds after determining the year and month are discarded.

**Parameters:** durationInMilliseconds

- Milliseconds of

Duration

to create.
**Returns:** New

Duration

created using the specified

durationInMilliseconds

.

---

#### newDurationYearMonth

public

Duration

newDurationYearMonth​(long durationInMilliseconds)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified milliseconds as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

can be influenced.

Any remaining milliseconds after determining the year and month are discarded.

The datatype

xdt:yearMonthDuration

is a subtype of

xs:duration

whose lexical representation contains only year and month components.
This datatype resides in the namespace

XMLConstants.W3C_XPATH_DATATYPE_NS_URI

.

Both values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

can be influenced.

Any remaining milliseconds after determining the year and month are discarded.

Both values are set by computing their values from the specified milliseconds
and are available using the

get

methods of the created

Duration

.
The values conform to and are defined by:

- ISO 8601:2000(E) Section 5.5.3.2 Alternative format
- W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats
- XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

can be influenced.

Any remaining milliseconds after determining the year and month are discarded.

ISO 8601:2000(E) Section 5.5.3.2 Alternative format

W3C XML Schema 1.0 Part 2, Appendix D, ISO 8601 Date and Time Formats

XMLGregorianCalendar

Date/Time Datatype Field Mapping Between XML Schema 1.0 and Java Representation

The default start instance is defined by

GregorianCalendar

's use of the start of the epoch: i.e.,

Calendar.YEAR

= 1970,

Calendar.MONTH

=

Calendar.JANUARY

,

Calendar.DATE

= 1, etc.
This is important as there are variations in the Gregorian Calendar,
e.g. leap years have different days in the month =

Calendar.FEBRUARY

so the result of

Duration.getMonths()

can be influenced.

Any remaining milliseconds after determining the year and month are discarded.

Any remaining milliseconds after determining the year and month are discarded.

newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(boolean isPositive,

BigInteger
year,

BigInteger
month)
```

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** year

- Year of

Duration

.
**Parameters:** month

- Month of

Duration

.
**Returns:** New

Duration

created using the specified

year

and

month

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if all of the fields (year, month) are null or
if any of the fields is negative.
**Throws:** UnsupportedOperationException

- If implementation cannot support requested values.

---

#### newDurationYearMonth

public

Duration

newDurationYearMonth​(boolean isPositive,

BigInteger

year,

BigInteger

month)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

The XML Schema specification states that values can be of an arbitrary size.
Implementations may chose not to or be incapable of supporting arbitrarily large and/or small values.
An

UnsupportedOperationException

will be thrown with a message indicating implementation limits
if implementation capacities are exceeded.

A

null

value indicates that field is not set.

A

null

value indicates that field is not set.

newDurationYearMonth

```java
public
Duration
newDurationYearMonth​(boolean isPositive,
int year,
int month)
```

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** isPositive

- Set to

false

to create a negative duration. When the length
of the duration is zero, this parameter will be ignored.
**Parameters:** year

- Year of

Duration

.
**Parameters:** month

- Month of

Duration

.
**Returns:** New

Duration

created using the specified

year

and

month

.
**Throws:** IllegalArgumentException

- If the values are not a valid representation of a

Duration

: if any of the fields (year, month) is negative.

---

#### newDurationYearMonth

public

Duration

newDurationYearMonth​(boolean isPositive,
int year,
int month)

Create a

Duration

of type

xdt:yearMonthDuration

using the specified

year

and

month

as defined in

XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar()
```

Create a new instance of an

XMLGregorianCalendar

.

All date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

**Returns:** New

XMLGregorianCalendar

with all date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

---

#### newXMLGregorianCalendar

public abstract

XMLGregorianCalendar

newXMLGregorianCalendar()

Create a new instance of an

XMLGregorianCalendar

.

All date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

All date/time datatype fields set to

DatatypeConstants.FIELD_UNDEFINED

or null.

newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
String
lexicalRepresentation)
```

Create a new XMLGregorianCalendar by parsing the String as a lexical representation.

Parsing the lexical string representation is defined in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

.

The string representation may not have any leading and trailing whitespaces.

The parsing is done field by field so that
the following holds for any lexically correct String x:

```java
newXMLGregorianCalendar(x).toXMLFormat().equals(x)
```

Except for the noted lexical/canonical representation mismatches
listed in

XML Schema 1.0 errata, Section 3.2.7.2

.

**Parameters:** lexicalRepresentation

- Lexical representation of one the eight XML Schema date/time datatypes.
**Returns:** XMLGregorianCalendar

created from the

lexicalRepresentation

.
**Throws:** IllegalArgumentException

- If the

lexicalRepresentation

is not a valid

XMLGregorianCalendar

.
**Throws:** NullPointerException

- If

lexicalRepresentation

is

null

.

---

#### newXMLGregorianCalendar

public abstract

XMLGregorianCalendar

newXMLGregorianCalendar​(

String

lexicalRepresentation)

Create a new XMLGregorianCalendar by parsing the String as a lexical representation.

Parsing the lexical string representation is defined in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

.

The string representation may not have any leading and trailing whitespaces.

The parsing is done field by field so that
the following holds for any lexically correct String x:

```java
newXMLGregorianCalendar(x).toXMLFormat().equals(x)
```

Except for the noted lexical/canonical representation mismatches
listed in

XML Schema 1.0 errata, Section 3.2.7.2

.

Parsing the lexical string representation is defined in

XML Schema 1.0 Part 2, Section 3.2.[7-14].1,

Lexical Representation

.

The string representation may not have any leading and trailing whitespaces.

The parsing is done field by field so that
the following holds for any lexically correct String x:

```java
newXMLGregorianCalendar(x).toXMLFormat().equals(x)
```

Except for the noted lexical/canonical representation mismatches
listed in

XML Schema 1.0 errata, Section 3.2.7.2

.

The string representation may not have any leading and trailing whitespaces.

The parsing is done field by field so that
the following holds for any lexically correct String x:

```java
newXMLGregorianCalendar(x).toXMLFormat().equals(x)
```

Except for the noted lexical/canonical representation mismatches
listed in

XML Schema 1.0 errata, Section 3.2.7.2

.

The parsing is done field by field so that
the following holds for any lexically correct String x:

```java
newXMLGregorianCalendar(x).toXMLFormat().equals(x)
```

Except for the noted lexical/canonical representation mismatches
listed in

XML Schema 1.0 errata, Section 3.2.7.2

.

newXMLGregorianCalendar(x).toXMLFormat().equals(x)

Except for the noted lexical/canonical representation mismatches
listed in

XML Schema 1.0 errata, Section 3.2.7.2

.

newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
GregorianCalendar
cal)
```

Create an

XMLGregorianCalendar

from a

GregorianCalendar

.

Field by Field Conversion from

GregorianCalendar

to an

XMLGregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA == GregorianCalendar.BC ? -YEAR : YEAR

XMLGregorianCalendar.setYear(int year)

MONTH + 1

XMLGregorianCalendar.setMonth(int month)

DAY_OF_MONTH

XMLGregorianCalendar.setDay(int day)

HOUR_OF_DAY, MINUTE, SECOND, MILLISECOND

XMLGregorianCalendar.setTime(int hour, int minute, int second, BigDecimal fractional)

(ZONE_OFFSET + DST_OFFSET) / (60*1000)

(in minutes)

XMLGregorianCalendar.setTimezone(int offset)

*

*

conversion loss of information. It is not possible to represent
a

java.util.GregorianCalendar

daylight savings timezone id in the
XML Schema 1.0 date/time datatype representation.

To compute the return value's

TimeZone

field,

- when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

**Parameters:** cal

-

java.util.GregorianCalendar

used to create

XMLGregorianCalendar
**Returns:** XMLGregorianCalendar

created from

java.util.GregorianCalendar
**Throws:** NullPointerException

- If

cal

is

null

.

---

#### newXMLGregorianCalendar

public abstract

XMLGregorianCalendar

newXMLGregorianCalendar​(

GregorianCalendar

cal)

Create an

XMLGregorianCalendar

from a

GregorianCalendar

.

Field by Field Conversion from

GregorianCalendar

to an

XMLGregorianCalendar

java.util.GregorianCalendar

field

javax.xml.datatype.XMLGregorianCalendar

field

ERA == GregorianCalendar.BC ? -YEAR : YEAR

XMLGregorianCalendar.setYear(int year)

MONTH + 1

XMLGregorianCalendar.setMonth(int month)

DAY_OF_MONTH

XMLGregorianCalendar.setDay(int day)

HOUR_OF_DAY, MINUTE, SECOND, MILLISECOND

XMLGregorianCalendar.setTime(int hour, int minute, int second, BigDecimal fractional)

(ZONE_OFFSET + DST_OFFSET) / (60*1000)

(in minutes)

XMLGregorianCalendar.setTimezone(int offset)

*

*

conversion loss of information. It is not possible to represent
a

java.util.GregorianCalendar

daylight savings timezone id in the
XML Schema 1.0 date/time datatype representation.

To compute the return value's

TimeZone

field,

- when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

*

conversion loss of information. It is not possible to represent
a

java.util.GregorianCalendar

daylight savings timezone id in the
XML Schema 1.0 date/time datatype representation.

To compute the return value's

TimeZone

field,

- when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

To compute the return value's

TimeZone

field,

- when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.
- else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

when

this.getTimezone() != FIELD_UNDEFINED

,
create a

java.util.TimeZone

with a custom timezone id
using the

this.getTimezone()

.

else use the

GregorianCalendar

default timezone value
for the host is defined as specified by

java.util.TimeZone.getDefault()

.

newXMLGregorianCalendar

```java
public abstract
XMLGregorianCalendar
newXMLGregorianCalendar​(
BigInteger
year,
int month,
int day,
int hour,
int minute,
int second,

BigDecimal
fractionalSecond,
int timezone)
```

Constructor allowing for complete value spaces allowed by
W3C XML Schema 1.0 recommendation for xsd:dateTime and related
builtin datatypes. Note that

year

parameter supports
arbitrarily large numbers and fractionalSecond has infinite
precision.

A

null

value indicates that field is not set.

**Parameters:** year

- of

XMLGregorianCalendar

to be created.
**Parameters:** month

- of

XMLGregorianCalendar

to be created.
**Parameters:** day

- of

XMLGregorianCalendar

to be created.
**Parameters:** hour

- of

XMLGregorianCalendar

to be created.
**Parameters:** minute

- of

XMLGregorianCalendar

to be created.
**Parameters:** second

- of

XMLGregorianCalendar

to be created.
**Parameters:** fractionalSecond

- of

XMLGregorianCalendar

to be created.
**Parameters:** timezone

- of

XMLGregorianCalendar

to be created.
**Returns:** XMLGregorianCalendar

created from specified values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

---

#### newXMLGregorianCalendar

public abstract

XMLGregorianCalendar

newXMLGregorianCalendar​(

BigInteger

year,
int month,
int day,
int hour,
int minute,
int second,

BigDecimal

fractionalSecond,
int timezone)

Constructor allowing for complete value spaces allowed by
W3C XML Schema 1.0 recommendation for xsd:dateTime and related
builtin datatypes. Note that

year

parameter supports
arbitrarily large numbers and fractionalSecond has infinite
precision.

A

null

value indicates that field is not set.

A

null

value indicates that field is not set.

newXMLGregorianCalendar

```java
public
XMLGregorianCalendar
newXMLGregorianCalendar​(int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)
```

Constructor of value spaces that a

java.util.GregorianCalendar

instance would need to convert to an

XMLGregorianCalendar

instance.

XMLGregorianCalendar eon

and

fractionalSecond

are set to

null

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** year

- of

XMLGregorianCalendar

to be created.
**Parameters:** month

- of

XMLGregorianCalendar

to be created.
**Parameters:** day

- of

XMLGregorianCalendar

to be created.
**Parameters:** hour

- of

XMLGregorianCalendar

to be created.
**Parameters:** minute

- of

XMLGregorianCalendar

to be created.
**Parameters:** second

- of

XMLGregorianCalendar

to be created.
**Parameters:** millisecond

- of

XMLGregorianCalendar

to be created.
**Parameters:** timezone

- of

XMLGregorianCalendar

to be created.
**Returns:** XMLGregorianCalendar

created from specified values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.

---

#### newXMLGregorianCalendar

public

XMLGregorianCalendar

newXMLGregorianCalendar​(int year,
int month,
int day,
int hour,
int minute,
int second,
int millisecond,
int timezone)

Constructor of value spaces that a

java.util.GregorianCalendar

instance would need to convert to an

XMLGregorianCalendar

instance.

XMLGregorianCalendar eon

and

fractionalSecond

are set to

null

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

XMLGregorianCalendar eon

and

fractionalSecond

are set to

null

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

newXMLGregorianCalendarDate

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarDate​(int year,
int month,
int day,
int timezone)
```

Create a Java representation of XML Schema builtin datatype

date

or

g*

.

For example, an instance of

gYear

can be created invoking this factory
with

month

and

day

parameters set to

DatatypeConstants.FIELD_UNDEFINED

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** year

- of

XMLGregorianCalendar

to be created.
**Parameters:** month

- of

XMLGregorianCalendar

to be created.
**Parameters:** day

- of

XMLGregorianCalendar

to be created.
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

---

#### newXMLGregorianCalendarDate

public

XMLGregorianCalendar

newXMLGregorianCalendarDate​(int year,
int month,
int day,
int timezone)

Create a Java representation of XML Schema builtin datatype

date

or

g*

.

For example, an instance of

gYear

can be created invoking this factory
with

month

and

day

parameters set to

DatatypeConstants.FIELD_UNDEFINED

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

For example, an instance of

gYear

can be created invoking this factory
with

month

and

day

parameters set to

DatatypeConstants.FIELD_UNDEFINED

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

newXMLGregorianCalendarTime

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int timezone)
```

Create a Java instance of XML Schema builtin datatype

time

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** hours

- number of hours
**Parameters:** minutes

- number of minutes
**Parameters:** seconds

- number of seconds
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

---

#### newXMLGregorianCalendarTime

public

XMLGregorianCalendar

newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int timezone)

Create a Java instance of XML Schema builtin datatype

time

.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

newXMLGregorianCalendarTime

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,

BigDecimal
fractionalSecond,
int timezone)
```

Create a Java instance of XML Schema builtin datatype time.

A

null

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** hours

- number of hours
**Parameters:** minutes

- number of minutes
**Parameters:** seconds

- number of seconds
**Parameters:** fractionalSecond

- value of

null

indicates that this optional field is not set.
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

---

#### newXMLGregorianCalendarTime

public

XMLGregorianCalendar

newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,

BigDecimal

fractionalSecond,
int timezone)

Create a Java instance of XML Schema builtin datatype time.

A

null

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

A

null

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

newXMLGregorianCalendarTime

```java
public
XMLGregorianCalendar
newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)
```

Create a Java instance of XML Schema builtin datatype time.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

**Parameters:** hours

- number of hours
**Parameters:** minutes

- number of minutes
**Parameters:** seconds

- number of seconds
**Parameters:** milliseconds

- number of milliseconds
**Parameters:** timezone

- offset in minutes.

DatatypeConstants.FIELD_UNDEFINED

indicates optional field is not set.
**Returns:** XMLGregorianCalendar

created from parameter values.
**Throws:** IllegalArgumentException

- If any individual parameter's value is outside the maximum value constraint for the field
as determined by the Date/Time Data Mapping table in

XMLGregorianCalendar

or if the composite values constitute an invalid

XMLGregorianCalendar

instance
as determined by

XMLGregorianCalendar.isValid()

.
**See Also:** DatatypeConstants.FIELD_UNDEFINED

---

#### newXMLGregorianCalendarTime

public

XMLGregorianCalendar

newXMLGregorianCalendarTime​(int hours,
int minutes,
int seconds,
int milliseconds,
int timezone)

Create a Java instance of XML Schema builtin datatype time.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

A

DatatypeConstants.FIELD_UNDEFINED

value indicates that field is not set.

---

