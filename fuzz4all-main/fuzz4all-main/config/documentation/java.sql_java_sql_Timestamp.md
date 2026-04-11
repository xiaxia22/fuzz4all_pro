# Class Timestamp

**Source:** `java.sql\java\sql\Timestamp.html`

### Class Description

```java
public class
Timestamp

extends
Date
```

A thin wrapper around

java.util.Date

that allows
the JDBC API to identify this as an SQL

TIMESTAMP

value.
It adds the ability
to hold the SQL

TIMESTAMP

fractional seconds value, by allowing
the specification of fractional seconds to a precision of nanoseconds.
A Timestamp also provides formatting and
parsing operations to support the JDBC escape syntax for timestamp values.

The precision of a Timestamp object is calculated to be either:

- 19

, which is the number of characters in yyyy-mm-dd hh:mm:ss

20 + s

, which is the number
of characters in the yyyy-mm-dd hh:mm:ss.[fff...] and

s

represents the scale of the given Timestamp,
its fractional seconds precision.

Note:

This type is a composite of a

java.util.Date

and a
separate nanoseconds value. Only integral seconds are stored in the

java.util.Date

component. The fractional seconds - the nanos - are
separate. The

Timestamp.equals(Object)

method never returns

true

when passed an object
that isn't an instance of

java.sql.Timestamp

,
because the nanos component of a date is unknown.
As a result, the

Timestamp.equals(Object)

method is not symmetric with respect to the

java.util.Date.equals(Object)

method. Also, the

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

Due to the differences between the

Timestamp

class
and the

java.util.Date

class mentioned above, it is recommended that code not view

Timestamp

values generically as an instance of

java.util.Date

. The
inheritance relationship between

Timestamp

and

java.util.Date

really
denotes implementation inheritance, and not type inheritance.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Comparable

<

Date

>

---

### Field Details

*No entries found.*

### Constructor Details

#### @Deprecated
(
since
="1.2")
public Timestamp​(int year,
int month,
int date,
int hour,
int minute,
int second,
int nano)

Constructs a

Timestamp

object initialized
with the given values.

**Parameters:**
- year

- the year minus 1900
- month

- 0 to 11
- date

- 1 to 31
- hour

- 0 to 23
- minute

- 0 to 59
- second

- 0 to 59
- nano

- 0 to 999,999,999

**Throws:**
- IllegalArgumentException

- if the nano argument is out of bounds

---

#### public Timestamp​(long time)

Constructs a

Timestamp

object
using a milliseconds time value. The
integral seconds are stored in the underlying date value; the
fractional seconds are stored in the

nanos

field of
the

Timestamp

object.

**Parameters:**
- time

- milliseconds since January 1, 1970, 00:00:00 GMT.
A negative number is the number of milliseconds before
January 1, 1970, 00:00:00 GMT.

**See Also:**
- Calendar

---

### Method Details

#### public void setTime​(long time)

Sets this

Timestamp

object to represent a point in time that is

time

milliseconds after January 1, 1970 00:00:00 GMT.

**Overrides:**
- setTime

in class

Date

**Parameters:**
- time

- the number of milliseconds.

**See Also:**
- getTime()

,

Timestamp(long time)

,

Calendar

---

#### public long getTime()

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this

Timestamp

object.

**Overrides:**
- getTime

in class

Date

**Returns:**
- the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this date.

**See Also:**
- setTime(long)

---

#### public static
Timestamp
valueOf​(
String
s)

Converts a

String

object in JDBC timestamp escape format to a

Timestamp

value.

**Parameters:**
- s

- timestamp in format

yyyy-[m]m-[d]d hh:mm:ss[.f...]

. The
fractional seconds may be omitted. The leading zero for

mm

and

dd

may also be omitted.

**Returns:**
- corresponding

Timestamp

value

**Throws:**
- IllegalArgumentException

- if the given argument
does not have the format

yyyy-[m]m-[d]d hh:mm:ss[.f...]

---

#### public
String
toString()

Formats a timestamp in JDBC timestamp escape format.

yyyy-mm-dd hh:mm:ss.fffffffff

,
where

fffffffff

indicates nanoseconds.

**Overrides:**
- toString

in class

Date

**Returns:**
- a

String

object in

yyyy-mm-dd hh:mm:ss.fffffffff

format

**See Also:**
- Date.toLocaleString()

,

Date.toGMTString()

---

#### public int getNanos()

Gets this

Timestamp

object's

nanos

value.

**Returns:**
- this

Timestamp

object's fractional seconds component

**See Also:**
- setNanos(int)

---

#### public void setNanos​(int n)

Sets this

Timestamp

object's

nanos

field
to the given value.

**Parameters:**
- n

- the new fractional seconds component

**Throws:**
- IllegalArgumentException

- if the given argument
is greater than 999999999 or less than 0

**See Also:**
- getNanos()

---

#### public boolean equals​(
Timestamp
ts)

Tests to see if this

Timestamp

object is
equal to the given

Timestamp

object.

**Parameters:**
- ts

- the

Timestamp

value to compare with

**Returns:**
- true

if the given

Timestamp

object is equal to this

Timestamp

object;

false

otherwise

---

#### public boolean equals​(
Object
ts)

Tests to see if this

Timestamp

object is
equal to the given object.

This version of the method

equals

has been added
to fix the incorrect
signature of

Timestamp.equals(Timestamp)

and to preserve backward
compatibility with existing class files.

Note: This method is not symmetric with respect to the

equals(Object)

method in the base class.

**Overrides:**
- equals

in class

Date

**Parameters:**
- ts

- the

Object

value to compare with

**Returns:**
- true

if the given

Object

is an instance
of a

Timestamp

that
is equal to this

Timestamp

object;

false

otherwise

**See Also:**
- Date.getTime()

---

#### public boolean before​(
Timestamp
ts)

Indicates whether this

Timestamp

object is
earlier than the given

Timestamp

object.

**Parameters:**
- ts

- the

Timestamp

value to compare with

**Returns:**
- true

if this

Timestamp

object is earlier;

false

otherwise

---

#### public boolean after​(
Timestamp
ts)

Indicates whether this

Timestamp

object is
later than the given

Timestamp

object.

**Parameters:**
- ts

- the

Timestamp

value to compare with

**Returns:**
- true

if this

Timestamp

object is later;

false

otherwise

---

#### public int compareTo​(
Timestamp
ts)

Compares this

Timestamp

object to the given

Timestamp

object.

**Parameters:**
- ts

- the

Timestamp

object to be compared to
this

Timestamp

object

**Returns:**
- the value

0

if the two

Timestamp

objects are equal; a value less than

0

if this

Timestamp

object is before the given argument;
and a value greater than

0

if this

Timestamp

object is after the given argument.

**Since:**
- 1.4

---

#### public int compareTo​(
Date
o)

Compares this

Timestamp

object to the given

Date

object.

**Specified by:**
- compareTo

in interface

Comparable

<

Date

>

**Overrides:**
- compareTo

in class

Date

**Parameters:**
- o

- the

Date

to be compared to
this

Timestamp

object

**Returns:**
- the value

0

if this

Timestamp

object
and the given object are equal; a value less than

0

if this

Timestamp

object is before the given argument;
and a value greater than

0

if this

Timestamp

object is after the given argument.

**Since:**
- 1.5

---

#### public int hashCode()

Returns a hash code value for this object. The result is the
exclusive OR of the two halves of the primitive

long

value returned by the

Date.getTime()

method. That is, the hash code is the value of the expression:

```java
(int)(this.getTime()^(this.getTime() >>> 32))
```

The

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

**Overrides:**
- hashCode

in class

Date

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public static
Timestamp
valueOf​(
LocalDateTime
dateTime)

Obtains an instance of

Timestamp

from a

LocalDateTime

object, with the same year, month, day of month, hours, minutes,
seconds and nanos date-time value as the provided

LocalDateTime

.

The provided

LocalDateTime

is interpreted as the local
date-time in the local time zone.

**Parameters:**
- dateTime

- a

LocalDateTime

to convert

**Returns:**
- a

Timestamp

object

**Throws:**
- NullPointerException

- if

dateTime

is null.

**Since:**
- 1.8

---

#### public
LocalDateTime
toLocalDateTime()

Converts this

Timestamp

object to a

LocalDateTime

.

The conversion creates a

LocalDateTime

that represents the
same year, month, day of month, hours, minutes, seconds and nanos
date-time value as this

Timestamp

in the local time zone.

**Returns:**
- a

LocalDateTime

object representing the same date-time value

**Since:**
- 1.8

---

#### public static
Timestamp
from​(
Instant
instant)

Obtains an instance of

Timestamp

from an

Instant

object.

Instant

can store points on the time-line further in the future
and further in the past than

Date

. In this scenario, this method
will throw an exception.

**Parameters:**
- instant

- the instant to convert

**Returns:**
- an

Timestamp

representing the same point on the time-line as
the provided instant

**Throws:**
- NullPointerException

- if

instant

is null.
- IllegalArgumentException

- if the instant is too large to
represent as a

Timestamp

**Since:**
- 1.8

---

#### public
Instant
toInstant()

Converts this

Timestamp

object to an

Instant

.

The conversion creates an

Instant

that represents the same
point on the time-line as this

Timestamp

.

**Overrides:**
- toInstant

in class

Date

**Returns:**
- an instant representing the same point on the time-line

**Since:**
- 1.8

---

### Additional Sections

#### Class Timestamp

java.lang.Object

- java.util.Date
- - java.sql.Timestamp

java.util.Date

- java.sql.Timestamp

java.sql.Timestamp

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Comparable

<

Date

>

```java
public class
Timestamp

extends
Date
```

A thin wrapper around

java.util.Date

that allows
the JDBC API to identify this as an SQL

TIMESTAMP

value.
It adds the ability
to hold the SQL

TIMESTAMP

fractional seconds value, by allowing
the specification of fractional seconds to a precision of nanoseconds.
A Timestamp also provides formatting and
parsing operations to support the JDBC escape syntax for timestamp values.

The precision of a Timestamp object is calculated to be either:

- 19

, which is the number of characters in yyyy-mm-dd hh:mm:ss

20 + s

, which is the number
of characters in the yyyy-mm-dd hh:mm:ss.[fff...] and

s

represents the scale of the given Timestamp,
its fractional seconds precision.

Note:

This type is a composite of a

java.util.Date

and a
separate nanoseconds value. Only integral seconds are stored in the

java.util.Date

component. The fractional seconds - the nanos - are
separate. The

Timestamp.equals(Object)

method never returns

true

when passed an object
that isn't an instance of

java.sql.Timestamp

,
because the nanos component of a date is unknown.
As a result, the

Timestamp.equals(Object)

method is not symmetric with respect to the

java.util.Date.equals(Object)

method. Also, the

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

Due to the differences between the

Timestamp

class
and the

java.util.Date

class mentioned above, it is recommended that code not view

Timestamp

values generically as an instance of

java.util.Date

. The
inheritance relationship between

Timestamp

and

java.util.Date

really
denotes implementation inheritance, and not type inheritance.

**Since:** 1.1
**See Also:** Serialized Form

public class

Timestamp

extends

Date

A thin wrapper around

java.util.Date

that allows
the JDBC API to identify this as an SQL

TIMESTAMP

value.
It adds the ability
to hold the SQL

TIMESTAMP

fractional seconds value, by allowing
the specification of fractional seconds to a precision of nanoseconds.
A Timestamp also provides formatting and
parsing operations to support the JDBC escape syntax for timestamp values.

The precision of a Timestamp object is calculated to be either:

- 19

, which is the number of characters in yyyy-mm-dd hh:mm:ss

20 + s

, which is the number
of characters in the yyyy-mm-dd hh:mm:ss.[fff...] and

s

represents the scale of the given Timestamp,
its fractional seconds precision.

Note:

This type is a composite of a

java.util.Date

and a
separate nanoseconds value. Only integral seconds are stored in the

java.util.Date

component. The fractional seconds - the nanos - are
separate. The

Timestamp.equals(Object)

method never returns

true

when passed an object
that isn't an instance of

java.sql.Timestamp

,
because the nanos component of a date is unknown.
As a result, the

Timestamp.equals(Object)

method is not symmetric with respect to the

java.util.Date.equals(Object)

method. Also, the

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

Due to the differences between the

Timestamp

class
and the

java.util.Date

class mentioned above, it is recommended that code not view

Timestamp

values generically as an instance of

java.util.Date

. The
inheritance relationship between

Timestamp

and

java.util.Date

really
denotes implementation inheritance, and not type inheritance.

The precision of a Timestamp object is calculated to be either:

- 19

, which is the number of characters in yyyy-mm-dd hh:mm:ss

20 + s

, which is the number
of characters in the yyyy-mm-dd hh:mm:ss.[fff...] and

s

represents the scale of the given Timestamp,
its fractional seconds precision.

Note:

This type is a composite of a

java.util.Date

and a
separate nanoseconds value. Only integral seconds are stored in the

java.util.Date

component. The fractional seconds - the nanos - are
separate. The

Timestamp.equals(Object)

method never returns

true

when passed an object
that isn't an instance of

java.sql.Timestamp

,
because the nanos component of a date is unknown.
As a result, the

Timestamp.equals(Object)

method is not symmetric with respect to the

java.util.Date.equals(Object)

method. Also, the

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

Due to the differences between the

Timestamp

class
and the

java.util.Date

class mentioned above, it is recommended that code not view

Timestamp

values generically as an instance of

java.util.Date

. The
inheritance relationship between

Timestamp

and

java.util.Date

really
denotes implementation inheritance, and not type inheritance.

19

, which is the number of characters in yyyy-mm-dd hh:mm:ss

20 + s

, which is the number
of characters in the yyyy-mm-dd hh:mm:ss.[fff...] and

s

represents the scale of the given Timestamp,
its fractional seconds precision.

Note:

This type is a composite of a

java.util.Date

and a
separate nanoseconds value. Only integral seconds are stored in the

java.util.Date

component. The fractional seconds - the nanos - are
separate. The

Timestamp.equals(Object)

method never returns

true

when passed an object
that isn't an instance of

java.sql.Timestamp

,
because the nanos component of a date is unknown.
As a result, the

Timestamp.equals(Object)

method is not symmetric with respect to the

java.util.Date.equals(Object)

method. Also, the

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

Due to the differences between the

Timestamp

class
and the

java.util.Date

class mentioned above, it is recommended that code not view

Timestamp

values generically as an instance of

java.util.Date

. The
inheritance relationship between

Timestamp

and

java.util.Date

really
denotes implementation inheritance, and not type inheritance.

Due to the differences between the

Timestamp

class
and the

java.util.Date

class mentioned above, it is recommended that code not view

Timestamp

values generically as an instance of

java.util.Date

. The
inheritance relationship between

Timestamp

and

java.util.Date

really
denotes implementation inheritance, and not type inheritance.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Timestamp

​(int year,
int month,
int date,
int hour,
int minute,
int second,
int nano)

Deprecated.

instead use the constructor

Timestamp(long millis)

Timestamp

​(long time)

Constructs a

Timestamp

object
using a milliseconds time value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

after

​(

Timestamp

ts)

Indicates whether this

Timestamp

object is
later than the given

Timestamp

object.

boolean

before

​(

Timestamp

ts)

Indicates whether this

Timestamp

object is
earlier than the given

Timestamp

object.

int

compareTo

​(

Timestamp

ts)

Compares this

Timestamp

object to the given

Timestamp

object.

int

compareTo

​(

Date

o)

Compares this

Timestamp

object to the given

Date

object.

boolean

equals

​(

Object

ts)

Tests to see if this

Timestamp

object is
equal to the given object.

boolean

equals

​(

Timestamp

ts)

Tests to see if this

Timestamp

object is
equal to the given

Timestamp

object.

static

Timestamp

from

​(

Instant

instant)

Obtains an instance of

Timestamp

from an

Instant

object.

int

getNanos

()

Gets this

Timestamp

object's

nanos

value.

long

getTime

()

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this

Timestamp

object.

int

hashCode

()

Returns a hash code value for this object.

void

setNanos

​(int n)

Sets this

Timestamp

object's

nanos

field
to the given value.

void

setTime

​(long time)

Sets this

Timestamp

object to represent a point in time that is

time

milliseconds after January 1, 1970 00:00:00 GMT.

Instant

toInstant

()

Converts this

Timestamp

object to an

Instant

.

LocalDateTime

toLocalDateTime

()

Converts this

Timestamp

object to a

LocalDateTime

.

String

toString

()

Formats a timestamp in JDBC timestamp escape format.

static

Timestamp

valueOf

​(

String

s)

Converts a

String

object in JDBC timestamp escape format to a

Timestamp

value.

static

Timestamp

valueOf

​(

LocalDateTime

dateTime)

Obtains an instance of

Timestamp

from a

LocalDateTime

object, with the same year, month, day of month, hours, minutes,
seconds and nanos date-time value as the provided

LocalDateTime

.

- Methods declared in class java.util.

Date

after

,

before

,

clone

,

getDate

,

getDay

,

getHours

,

getMinutes

,

getMonth

,

getSeconds

,

getTimezoneOffset

,

getYear

,

parse

,

setDate

,

setHours

,

setMinutes

,

setMonth

,

setSeconds

,

setYear

,

toGMTString

,

toLocaleString

,

UTC

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

Timestamp

​(int year,
int month,
int date,
int hour,
int minute,
int second,
int nano)

Deprecated.

instead use the constructor

Timestamp(long millis)

Timestamp

​(long time)

Constructs a

Timestamp

object
using a milliseconds time value.

---

#### Constructor Summary

Deprecated.

instead use the constructor

Timestamp(long millis)

Constructs a

Timestamp

object
using a milliseconds time value.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

after

​(

Timestamp

ts)

Indicates whether this

Timestamp

object is
later than the given

Timestamp

object.

boolean

before

​(

Timestamp

ts)

Indicates whether this

Timestamp

object is
earlier than the given

Timestamp

object.

int

compareTo

​(

Timestamp

ts)

Compares this

Timestamp

object to the given

Timestamp

object.

int

compareTo

​(

Date

o)

Compares this

Timestamp

object to the given

Date

object.

boolean

equals

​(

Object

ts)

Tests to see if this

Timestamp

object is
equal to the given object.

boolean

equals

​(

Timestamp

ts)

Tests to see if this

Timestamp

object is
equal to the given

Timestamp

object.

static

Timestamp

from

​(

Instant

instant)

Obtains an instance of

Timestamp

from an

Instant

object.

int

getNanos

()

Gets this

Timestamp

object's

nanos

value.

long

getTime

()

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this

Timestamp

object.

int

hashCode

()

Returns a hash code value for this object.

void

setNanos

​(int n)

Sets this

Timestamp

object's

nanos

field
to the given value.

void

setTime

​(long time)

Sets this

Timestamp

object to represent a point in time that is

time

milliseconds after January 1, 1970 00:00:00 GMT.

Instant

toInstant

()

Converts this

Timestamp

object to an

Instant

.

LocalDateTime

toLocalDateTime

()

Converts this

Timestamp

object to a

LocalDateTime

.

String

toString

()

Formats a timestamp in JDBC timestamp escape format.

static

Timestamp

valueOf

​(

String

s)

Converts a

String

object in JDBC timestamp escape format to a

Timestamp

value.

static

Timestamp

valueOf

​(

LocalDateTime

dateTime)

Obtains an instance of

Timestamp

from a

LocalDateTime

object, with the same year, month, day of month, hours, minutes,
seconds and nanos date-time value as the provided

LocalDateTime

.

- Methods declared in class java.util.

Date

after

,

before

,

clone

,

getDate

,

getDay

,

getHours

,

getMinutes

,

getMonth

,

getSeconds

,

getTimezoneOffset

,

getYear

,

parse

,

setDate

,

setHours

,

setMinutes

,

setMonth

,

setSeconds

,

setYear

,

toGMTString

,

toLocaleString

,

UTC

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

Indicates whether this

Timestamp

object is
later than the given

Timestamp

object.

Indicates whether this

Timestamp

object is
earlier than the given

Timestamp

object.

Compares this

Timestamp

object to the given

Timestamp

object.

Compares this

Timestamp

object to the given

Date

object.

Tests to see if this

Timestamp

object is
equal to the given object.

Tests to see if this

Timestamp

object is
equal to the given

Timestamp

object.

Obtains an instance of

Timestamp

from an

Instant

object.

Gets this

Timestamp

object's

nanos

value.

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this

Timestamp

object.

Returns a hash code value for this object.

Sets this

Timestamp

object's

nanos

field
to the given value.

Sets this

Timestamp

object to represent a point in time that is

time

milliseconds after January 1, 1970 00:00:00 GMT.

Converts this

Timestamp

object to an

Instant

.

Converts this

Timestamp

object to a

LocalDateTime

.

Formats a timestamp in JDBC timestamp escape format.

Converts a

String

object in JDBC timestamp escape format to a

Timestamp

value.

Obtains an instance of

Timestamp

from a

LocalDateTime

object, with the same year, month, day of month, hours, minutes,
seconds and nanos date-time value as the provided

LocalDateTime

.

Methods declared in class java.util.

Date

after

,

before

,

clone

,

getDate

,

getDay

,

getHours

,

getMinutes

,

getMonth

,

getSeconds

,

getTimezoneOffset

,

getYear

,

parse

,

setDate

,

setHours

,

setMinutes

,

setMonth

,

setSeconds

,

setYear

,

toGMTString

,

toLocaleString

,

UTC

---

#### Methods declared in class java.util. Date

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

- Timestamp

```java
@Deprecated
(
since
="1.2")
public Timestamp​(int year,
int month,
int date,
int hour,
int minute,
int second,
int nano)
```

Deprecated.

instead use the constructor

Timestamp(long millis)

Constructs a

Timestamp

object initialized
with the given values.

**Parameters:** year

- the year minus 1900
**Parameters:** month

- 0 to 11
**Parameters:** date

- 1 to 31
**Parameters:** hour

- 0 to 23
**Parameters:** minute

- 0 to 59
**Parameters:** second

- 0 to 59
**Parameters:** nano

- 0 to 999,999,999
**Throws:** IllegalArgumentException

- if the nano argument is out of bounds

- Timestamp

```java
public Timestamp​(long time)
```

Constructs a

Timestamp

object
using a milliseconds time value. The
integral seconds are stored in the underlying date value; the
fractional seconds are stored in the

nanos

field of
the

Timestamp

object.

**Parameters:** time

- milliseconds since January 1, 1970, 00:00:00 GMT.
A negative number is the number of milliseconds before
January 1, 1970, 00:00:00 GMT.
**See Also:** Calendar

============ METHOD DETAIL ==========

- Method Detail

- setTime

```java
public void setTime​(long time)
```

Sets this

Timestamp

object to represent a point in time that is

time

milliseconds after January 1, 1970 00:00:00 GMT.

**Overrides:** setTime

in class

Date
**Parameters:** time

- the number of milliseconds.
**See Also:** getTime()

,

Timestamp(long time)

,

Calendar

- getTime

```java
public long getTime()
```

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this

Timestamp

object.

**Overrides:** getTime

in class

Date
**Returns:** the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this date.
**See Also:** setTime(long)

- valueOf

```java
public static
Timestamp
valueOf​(
String
s)
```

Converts a

String

object in JDBC timestamp escape format to a

Timestamp

value.

**Parameters:** s

- timestamp in format

yyyy-[m]m-[d]d hh:mm:ss[.f...]

. The
fractional seconds may be omitted. The leading zero for

mm

and

dd

may also be omitted.
**Returns:** corresponding

Timestamp

value
**Throws:** IllegalArgumentException

- if the given argument
does not have the format

yyyy-[m]m-[d]d hh:mm:ss[.f...]

- toString

```java
public
String
toString()
```

Formats a timestamp in JDBC timestamp escape format.

yyyy-mm-dd hh:mm:ss.fffffffff

,
where

fffffffff

indicates nanoseconds.

**Overrides:** toString

in class

Date
**Returns:** a

String

object in

yyyy-mm-dd hh:mm:ss.fffffffff

format
**See Also:** Date.toLocaleString()

,

Date.toGMTString()

- getNanos

```java
public int getNanos()
```

Gets this

Timestamp

object's

nanos

value.

**Returns:** this

Timestamp

object's fractional seconds component
**See Also:** setNanos(int)

- setNanos

```java
public void setNanos​(int n)
```

Sets this

Timestamp

object's

nanos

field
to the given value.

**Parameters:** n

- the new fractional seconds component
**Throws:** IllegalArgumentException

- if the given argument
is greater than 999999999 or less than 0
**See Also:** getNanos()

- equals

```java
public boolean equals​(
Timestamp
ts)
```

Tests to see if this

Timestamp

object is
equal to the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

value to compare with
**Returns:** true

if the given

Timestamp

object is equal to this

Timestamp

object;

false

otherwise

- equals

```java
public boolean equals​(
Object
ts)
```

Tests to see if this

Timestamp

object is
equal to the given object.

This version of the method

equals

has been added
to fix the incorrect
signature of

Timestamp.equals(Timestamp)

and to preserve backward
compatibility with existing class files.

Note: This method is not symmetric with respect to the

equals(Object)

method in the base class.

**Overrides:** equals

in class

Date
**Parameters:** ts

- the

Object

value to compare with
**Returns:** true

if the given

Object

is an instance
of a

Timestamp

that
is equal to this

Timestamp

object;

false

otherwise
**See Also:** Date.getTime()

- before

```java
public boolean before​(
Timestamp
ts)
```

Indicates whether this

Timestamp

object is
earlier than the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

value to compare with
**Returns:** true

if this

Timestamp

object is earlier;

false

otherwise

- after

```java
public boolean after​(
Timestamp
ts)
```

Indicates whether this

Timestamp

object is
later than the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

value to compare with
**Returns:** true

if this

Timestamp

object is later;

false

otherwise

- compareTo

```java
public int compareTo​(
Timestamp
ts)
```

Compares this

Timestamp

object to the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

object to be compared to
this

Timestamp

object
**Returns:** the value

0

if the two

Timestamp

objects are equal; a value less than

0

if this

Timestamp

object is before the given argument;
and a value greater than

0

if this

Timestamp

object is after the given argument.
**Since:** 1.4

- compareTo

```java
public int compareTo​(
Date
o)
```

Compares this

Timestamp

object to the given

Date

object.

**Specified by:** compareTo

in interface

Comparable

<

Date

>
**Overrides:** compareTo

in class

Date
**Parameters:** o

- the

Date

to be compared to
this

Timestamp

object
**Returns:** the value

0

if this

Timestamp

object
and the given object are equal; a value less than

0

if this

Timestamp

object is before the given argument;
and a value greater than

0

if this

Timestamp

object is after the given argument.
**Since:** 1.5

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this object. The result is the
exclusive OR of the two halves of the primitive

long

value returned by the

Date.getTime()

method. That is, the hash code is the value of the expression:

```java
(int)(this.getTime()^(this.getTime() >>> 32))
```

The

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

**Overrides:** hashCode

in class

Date
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- valueOf

```java
public static
Timestamp
valueOf​(
LocalDateTime
dateTime)
```

Obtains an instance of

Timestamp

from a

LocalDateTime

object, with the same year, month, day of month, hours, minutes,
seconds and nanos date-time value as the provided

LocalDateTime

.

The provided

LocalDateTime

is interpreted as the local
date-time in the local time zone.

**Parameters:** dateTime

- a

LocalDateTime

to convert
**Returns:** a

Timestamp

object
**Throws:** NullPointerException

- if

dateTime

is null.
**Since:** 1.8

- toLocalDateTime

```java
public
LocalDateTime
toLocalDateTime()
```

Converts this

Timestamp

object to a

LocalDateTime

.

The conversion creates a

LocalDateTime

that represents the
same year, month, day of month, hours, minutes, seconds and nanos
date-time value as this

Timestamp

in the local time zone.

**Returns:** a

LocalDateTime

object representing the same date-time value
**Since:** 1.8

- from

```java
public static
Timestamp
from​(
Instant
instant)
```

Obtains an instance of

Timestamp

from an

Instant

object.

Instant

can store points on the time-line further in the future
and further in the past than

Date

. In this scenario, this method
will throw an exception.

**Parameters:** instant

- the instant to convert
**Returns:** an

Timestamp

representing the same point on the time-line as
the provided instant
**Throws:** NullPointerException

- if

instant

is null.
**Throws:** IllegalArgumentException

- if the instant is too large to
represent as a

Timestamp
**Since:** 1.8

- toInstant

```java
public
Instant
toInstant()
```

Converts this

Timestamp

object to an

Instant

.

The conversion creates an

Instant

that represents the same
point on the time-line as this

Timestamp

.

**Overrides:** toInstant

in class

Date
**Returns:** an instant representing the same point on the time-line
**Since:** 1.8

Constructor Detail

- Timestamp

```java
@Deprecated
(
since
="1.2")
public Timestamp​(int year,
int month,
int date,
int hour,
int minute,
int second,
int nano)
```

Deprecated.

instead use the constructor

Timestamp(long millis)

Constructs a

Timestamp

object initialized
with the given values.

**Parameters:** year

- the year minus 1900
**Parameters:** month

- 0 to 11
**Parameters:** date

- 1 to 31
**Parameters:** hour

- 0 to 23
**Parameters:** minute

- 0 to 59
**Parameters:** second

- 0 to 59
**Parameters:** nano

- 0 to 999,999,999
**Throws:** IllegalArgumentException

- if the nano argument is out of bounds

- Timestamp

```java
public Timestamp​(long time)
```

Constructs a

Timestamp

object
using a milliseconds time value. The
integral seconds are stored in the underlying date value; the
fractional seconds are stored in the

nanos

field of
the

Timestamp

object.

**Parameters:** time

- milliseconds since January 1, 1970, 00:00:00 GMT.
A negative number is the number of milliseconds before
January 1, 1970, 00:00:00 GMT.
**See Also:** Calendar

---

#### Constructor Detail

Timestamp

```java
@Deprecated
(
since
="1.2")
public Timestamp​(int year,
int month,
int date,
int hour,
int minute,
int second,
int nano)
```

Deprecated.

instead use the constructor

Timestamp(long millis)

Constructs a

Timestamp

object initialized
with the given values.

**Parameters:** year

- the year minus 1900
**Parameters:** month

- 0 to 11
**Parameters:** date

- 1 to 31
**Parameters:** hour

- 0 to 23
**Parameters:** minute

- 0 to 59
**Parameters:** second

- 0 to 59
**Parameters:** nano

- 0 to 999,999,999
**Throws:** IllegalArgumentException

- if the nano argument is out of bounds

---

#### Timestamp

@Deprecated

(

since

="1.2")
public Timestamp​(int year,
int month,
int date,
int hour,
int minute,
int second,
int nano)

Constructs a

Timestamp

object initialized
with the given values.

Timestamp

```java
public Timestamp​(long time)
```

Constructs a

Timestamp

object
using a milliseconds time value. The
integral seconds are stored in the underlying date value; the
fractional seconds are stored in the

nanos

field of
the

Timestamp

object.

**Parameters:** time

- milliseconds since January 1, 1970, 00:00:00 GMT.
A negative number is the number of milliseconds before
January 1, 1970, 00:00:00 GMT.
**See Also:** Calendar

---

#### Timestamp

public Timestamp​(long time)

Constructs a

Timestamp

object
using a milliseconds time value. The
integral seconds are stored in the underlying date value; the
fractional seconds are stored in the

nanos

field of
the

Timestamp

object.

Method Detail

- setTime

```java
public void setTime​(long time)
```

Sets this

Timestamp

object to represent a point in time that is

time

milliseconds after January 1, 1970 00:00:00 GMT.

**Overrides:** setTime

in class

Date
**Parameters:** time

- the number of milliseconds.
**See Also:** getTime()

,

Timestamp(long time)

,

Calendar

- getTime

```java
public long getTime()
```

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this

Timestamp

object.

**Overrides:** getTime

in class

Date
**Returns:** the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this date.
**See Also:** setTime(long)

- valueOf

```java
public static
Timestamp
valueOf​(
String
s)
```

Converts a

String

object in JDBC timestamp escape format to a

Timestamp

value.

**Parameters:** s

- timestamp in format

yyyy-[m]m-[d]d hh:mm:ss[.f...]

. The
fractional seconds may be omitted. The leading zero for

mm

and

dd

may also be omitted.
**Returns:** corresponding

Timestamp

value
**Throws:** IllegalArgumentException

- if the given argument
does not have the format

yyyy-[m]m-[d]d hh:mm:ss[.f...]

- toString

```java
public
String
toString()
```

Formats a timestamp in JDBC timestamp escape format.

yyyy-mm-dd hh:mm:ss.fffffffff

,
where

fffffffff

indicates nanoseconds.

**Overrides:** toString

in class

Date
**Returns:** a

String

object in

yyyy-mm-dd hh:mm:ss.fffffffff

format
**See Also:** Date.toLocaleString()

,

Date.toGMTString()

- getNanos

```java
public int getNanos()
```

Gets this

Timestamp

object's

nanos

value.

**Returns:** this

Timestamp

object's fractional seconds component
**See Also:** setNanos(int)

- setNanos

```java
public void setNanos​(int n)
```

Sets this

Timestamp

object's

nanos

field
to the given value.

**Parameters:** n

- the new fractional seconds component
**Throws:** IllegalArgumentException

- if the given argument
is greater than 999999999 or less than 0
**See Also:** getNanos()

- equals

```java
public boolean equals​(
Timestamp
ts)
```

Tests to see if this

Timestamp

object is
equal to the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

value to compare with
**Returns:** true

if the given

Timestamp

object is equal to this

Timestamp

object;

false

otherwise

- equals

```java
public boolean equals​(
Object
ts)
```

Tests to see if this

Timestamp

object is
equal to the given object.

This version of the method

equals

has been added
to fix the incorrect
signature of

Timestamp.equals(Timestamp)

and to preserve backward
compatibility with existing class files.

Note: This method is not symmetric with respect to the

equals(Object)

method in the base class.

**Overrides:** equals

in class

Date
**Parameters:** ts

- the

Object

value to compare with
**Returns:** true

if the given

Object

is an instance
of a

Timestamp

that
is equal to this

Timestamp

object;

false

otherwise
**See Also:** Date.getTime()

- before

```java
public boolean before​(
Timestamp
ts)
```

Indicates whether this

Timestamp

object is
earlier than the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

value to compare with
**Returns:** true

if this

Timestamp

object is earlier;

false

otherwise

- after

```java
public boolean after​(
Timestamp
ts)
```

Indicates whether this

Timestamp

object is
later than the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

value to compare with
**Returns:** true

if this

Timestamp

object is later;

false

otherwise

- compareTo

```java
public int compareTo​(
Timestamp
ts)
```

Compares this

Timestamp

object to the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

object to be compared to
this

Timestamp

object
**Returns:** the value

0

if the two

Timestamp

objects are equal; a value less than

0

if this

Timestamp

object is before the given argument;
and a value greater than

0

if this

Timestamp

object is after the given argument.
**Since:** 1.4

- compareTo

```java
public int compareTo​(
Date
o)
```

Compares this

Timestamp

object to the given

Date

object.

**Specified by:** compareTo

in interface

Comparable

<

Date

>
**Overrides:** compareTo

in class

Date
**Parameters:** o

- the

Date

to be compared to
this

Timestamp

object
**Returns:** the value

0

if this

Timestamp

object
and the given object are equal; a value less than

0

if this

Timestamp

object is before the given argument;
and a value greater than

0

if this

Timestamp

object is after the given argument.
**Since:** 1.5

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this object. The result is the
exclusive OR of the two halves of the primitive

long

value returned by the

Date.getTime()

method. That is, the hash code is the value of the expression:

```java
(int)(this.getTime()^(this.getTime() >>> 32))
```

The

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

**Overrides:** hashCode

in class

Date
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- valueOf

```java
public static
Timestamp
valueOf​(
LocalDateTime
dateTime)
```

Obtains an instance of

Timestamp

from a

LocalDateTime

object, with the same year, month, day of month, hours, minutes,
seconds and nanos date-time value as the provided

LocalDateTime

.

The provided

LocalDateTime

is interpreted as the local
date-time in the local time zone.

**Parameters:** dateTime

- a

LocalDateTime

to convert
**Returns:** a

Timestamp

object
**Throws:** NullPointerException

- if

dateTime

is null.
**Since:** 1.8

- toLocalDateTime

```java
public
LocalDateTime
toLocalDateTime()
```

Converts this

Timestamp

object to a

LocalDateTime

.

The conversion creates a

LocalDateTime

that represents the
same year, month, day of month, hours, minutes, seconds and nanos
date-time value as this

Timestamp

in the local time zone.

**Returns:** a

LocalDateTime

object representing the same date-time value
**Since:** 1.8

- from

```java
public static
Timestamp
from​(
Instant
instant)
```

Obtains an instance of

Timestamp

from an

Instant

object.

Instant

can store points on the time-line further in the future
and further in the past than

Date

. In this scenario, this method
will throw an exception.

**Parameters:** instant

- the instant to convert
**Returns:** an

Timestamp

representing the same point on the time-line as
the provided instant
**Throws:** NullPointerException

- if

instant

is null.
**Throws:** IllegalArgumentException

- if the instant is too large to
represent as a

Timestamp
**Since:** 1.8

- toInstant

```java
public
Instant
toInstant()
```

Converts this

Timestamp

object to an

Instant

.

The conversion creates an

Instant

that represents the same
point on the time-line as this

Timestamp

.

**Overrides:** toInstant

in class

Date
**Returns:** an instant representing the same point on the time-line
**Since:** 1.8

---

#### Method Detail

setTime

```java
public void setTime​(long time)
```

Sets this

Timestamp

object to represent a point in time that is

time

milliseconds after January 1, 1970 00:00:00 GMT.

**Overrides:** setTime

in class

Date
**Parameters:** time

- the number of milliseconds.
**See Also:** getTime()

,

Timestamp(long time)

,

Calendar

---

#### setTime

public void setTime​(long time)

Sets this

Timestamp

object to represent a point in time that is

time

milliseconds after January 1, 1970 00:00:00 GMT.

getTime

```java
public long getTime()
```

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this

Timestamp

object.

**Overrides:** getTime

in class

Date
**Returns:** the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this date.
**See Also:** setTime(long)

---

#### getTime

public long getTime()

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT
represented by this

Timestamp

object.

valueOf

```java
public static
Timestamp
valueOf​(
String
s)
```

Converts a

String

object in JDBC timestamp escape format to a

Timestamp

value.

**Parameters:** s

- timestamp in format

yyyy-[m]m-[d]d hh:mm:ss[.f...]

. The
fractional seconds may be omitted. The leading zero for

mm

and

dd

may also be omitted.
**Returns:** corresponding

Timestamp

value
**Throws:** IllegalArgumentException

- if the given argument
does not have the format

yyyy-[m]m-[d]d hh:mm:ss[.f...]

---

#### valueOf

public static

Timestamp

valueOf​(

String

s)

Converts a

String

object in JDBC timestamp escape format to a

Timestamp

value.

toString

```java
public
String
toString()
```

Formats a timestamp in JDBC timestamp escape format.

yyyy-mm-dd hh:mm:ss.fffffffff

,
where

fffffffff

indicates nanoseconds.

**Overrides:** toString

in class

Date
**Returns:** a

String

object in

yyyy-mm-dd hh:mm:ss.fffffffff

format
**See Also:** Date.toLocaleString()

,

Date.toGMTString()

---

#### toString

public

String

toString()

Formats a timestamp in JDBC timestamp escape format.

yyyy-mm-dd hh:mm:ss.fffffffff

,
where

fffffffff

indicates nanoseconds.

getNanos

```java
public int getNanos()
```

Gets this

Timestamp

object's

nanos

value.

**Returns:** this

Timestamp

object's fractional seconds component
**See Also:** setNanos(int)

---

#### getNanos

public int getNanos()

Gets this

Timestamp

object's

nanos

value.

setNanos

```java
public void setNanos​(int n)
```

Sets this

Timestamp

object's

nanos

field
to the given value.

**Parameters:** n

- the new fractional seconds component
**Throws:** IllegalArgumentException

- if the given argument
is greater than 999999999 or less than 0
**See Also:** getNanos()

---

#### setNanos

public void setNanos​(int n)

Sets this

Timestamp

object's

nanos

field
to the given value.

equals

```java
public boolean equals​(
Timestamp
ts)
```

Tests to see if this

Timestamp

object is
equal to the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

value to compare with
**Returns:** true

if the given

Timestamp

object is equal to this

Timestamp

object;

false

otherwise

---

#### equals

public boolean equals​(

Timestamp

ts)

Tests to see if this

Timestamp

object is
equal to the given

Timestamp

object.

equals

```java
public boolean equals​(
Object
ts)
```

Tests to see if this

Timestamp

object is
equal to the given object.

This version of the method

equals

has been added
to fix the incorrect
signature of

Timestamp.equals(Timestamp)

and to preserve backward
compatibility with existing class files.

Note: This method is not symmetric with respect to the

equals(Object)

method in the base class.

**Overrides:** equals

in class

Date
**Parameters:** ts

- the

Object

value to compare with
**Returns:** true

if the given

Object

is an instance
of a

Timestamp

that
is equal to this

Timestamp

object;

false

otherwise
**See Also:** Date.getTime()

---

#### equals

public boolean equals​(

Object

ts)

Tests to see if this

Timestamp

object is
equal to the given object.

This version of the method

equals

has been added
to fix the incorrect
signature of

Timestamp.equals(Timestamp)

and to preserve backward
compatibility with existing class files.

Note: This method is not symmetric with respect to the

equals(Object)

method in the base class.

before

```java
public boolean before​(
Timestamp
ts)
```

Indicates whether this

Timestamp

object is
earlier than the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

value to compare with
**Returns:** true

if this

Timestamp

object is earlier;

false

otherwise

---

#### before

public boolean before​(

Timestamp

ts)

Indicates whether this

Timestamp

object is
earlier than the given

Timestamp

object.

after

```java
public boolean after​(
Timestamp
ts)
```

Indicates whether this

Timestamp

object is
later than the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

value to compare with
**Returns:** true

if this

Timestamp

object is later;

false

otherwise

---

#### after

public boolean after​(

Timestamp

ts)

Indicates whether this

Timestamp

object is
later than the given

Timestamp

object.

compareTo

```java
public int compareTo​(
Timestamp
ts)
```

Compares this

Timestamp

object to the given

Timestamp

object.

**Parameters:** ts

- the

Timestamp

object to be compared to
this

Timestamp

object
**Returns:** the value

0

if the two

Timestamp

objects are equal; a value less than

0

if this

Timestamp

object is before the given argument;
and a value greater than

0

if this

Timestamp

object is after the given argument.
**Since:** 1.4

---

#### compareTo

public int compareTo​(

Timestamp

ts)

Compares this

Timestamp

object to the given

Timestamp

object.

compareTo

```java
public int compareTo​(
Date
o)
```

Compares this

Timestamp

object to the given

Date

object.

**Specified by:** compareTo

in interface

Comparable

<

Date

>
**Overrides:** compareTo

in class

Date
**Parameters:** o

- the

Date

to be compared to
this

Timestamp

object
**Returns:** the value

0

if this

Timestamp

object
and the given object are equal; a value less than

0

if this

Timestamp

object is before the given argument;
and a value greater than

0

if this

Timestamp

object is after the given argument.
**Since:** 1.5

---

#### compareTo

public int compareTo​(

Date

o)

Compares this

Timestamp

object to the given

Date

object.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this object. The result is the
exclusive OR of the two halves of the primitive

long

value returned by the

Date.getTime()

method. That is, the hash code is the value of the expression:

```java
(int)(this.getTime()^(this.getTime() >>> 32))
```

The

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

**Overrides:** hashCode

in class

Date
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this object. The result is the
exclusive OR of the two halves of the primitive

long

value returned by the

Date.getTime()

method. That is, the hash code is the value of the expression:

```java
(int)(this.getTime()^(this.getTime() >>> 32))
```

The

hashCode

method uses the underlying

java.util.Date

implementation and therefore does not include nanos in its computation.

(int)(this.getTime()^(this.getTime() >>> 32))

valueOf

```java
public static
Timestamp
valueOf​(
LocalDateTime
dateTime)
```

Obtains an instance of

Timestamp

from a

LocalDateTime

object, with the same year, month, day of month, hours, minutes,
seconds and nanos date-time value as the provided

LocalDateTime

.

The provided

LocalDateTime

is interpreted as the local
date-time in the local time zone.

**Parameters:** dateTime

- a

LocalDateTime

to convert
**Returns:** a

Timestamp

object
**Throws:** NullPointerException

- if

dateTime

is null.
**Since:** 1.8

---

#### valueOf

public static

Timestamp

valueOf​(

LocalDateTime

dateTime)

Obtains an instance of

Timestamp

from a

LocalDateTime

object, with the same year, month, day of month, hours, minutes,
seconds and nanos date-time value as the provided

LocalDateTime

.

The provided

LocalDateTime

is interpreted as the local
date-time in the local time zone.

The provided

LocalDateTime

is interpreted as the local
date-time in the local time zone.

toLocalDateTime

```java
public
LocalDateTime
toLocalDateTime()
```

Converts this

Timestamp

object to a

LocalDateTime

.

The conversion creates a

LocalDateTime

that represents the
same year, month, day of month, hours, minutes, seconds and nanos
date-time value as this

Timestamp

in the local time zone.

**Returns:** a

LocalDateTime

object representing the same date-time value
**Since:** 1.8

---

#### toLocalDateTime

public

LocalDateTime

toLocalDateTime()

Converts this

Timestamp

object to a

LocalDateTime

.

The conversion creates a

LocalDateTime

that represents the
same year, month, day of month, hours, minutes, seconds and nanos
date-time value as this

Timestamp

in the local time zone.

The conversion creates a

LocalDateTime

that represents the
same year, month, day of month, hours, minutes, seconds and nanos
date-time value as this

Timestamp

in the local time zone.

from

```java
public static
Timestamp
from​(
Instant
instant)
```

Obtains an instance of

Timestamp

from an

Instant

object.

Instant

can store points on the time-line further in the future
and further in the past than

Date

. In this scenario, this method
will throw an exception.

**Parameters:** instant

- the instant to convert
**Returns:** an

Timestamp

representing the same point on the time-line as
the provided instant
**Throws:** NullPointerException

- if

instant

is null.
**Throws:** IllegalArgumentException

- if the instant is too large to
represent as a

Timestamp
**Since:** 1.8

---

#### from

public static

Timestamp

from​(

Instant

instant)

Obtains an instance of

Timestamp

from an

Instant

object.

Instant

can store points on the time-line further in the future
and further in the past than

Date

. In this scenario, this method
will throw an exception.

Instant

can store points on the time-line further in the future
and further in the past than

Date

. In this scenario, this method
will throw an exception.

toInstant

```java
public
Instant
toInstant()
```

Converts this

Timestamp

object to an

Instant

.

The conversion creates an

Instant

that represents the same
point on the time-line as this

Timestamp

.

**Overrides:** toInstant

in class

Date
**Returns:** an instant representing the same point on the time-line
**Since:** 1.8

---

#### toInstant

public

Instant

toInstant()

Converts this

Timestamp

object to an

Instant

.

The conversion creates an

Instant

that represents the same
point on the time-line as this

Timestamp

.

The conversion creates an

Instant

that represents the same
point on the time-line as this

Timestamp

.

---

