# Class Date

**Source:** `java.sql\java\sql\Date.html`

### Class Description

```java
public class
Date

extends
Date
```

A thin wrapper around a millisecond value that allows
JDBC to identify this as an SQL

DATE

value. A
milliseconds value represents the number of milliseconds that
have passed since January 1, 1970 00:00:00.000 GMT.

To conform with the definition of SQL

DATE

, the
millisecond values wrapped by a

java.sql.Date

instance
must be 'normalized' by setting the
hours, minutes, seconds, and milliseconds to zero in the particular
time zone with which the instance is associated.

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
public Date​(int year,
int month,
int day)

Constructs a

Date

object initialized with the given
year, month, and day.

The result is undefined if a given argument is out of bounds.

**Parameters:**
- year

- the year minus 1900; must be 0 to 8099. (Note that
8099 is 9999 minus 1900.)
- month

- 0 to 11
- day

- 1 to 31

---

#### public Date​(long date)

Constructs a

Date

object using the given milliseconds
time value. If the given milliseconds value contains time
information, the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

**Parameters:**
- date

- milliseconds since January 1, 1970, 00:00:00 GMT not
to exceed the milliseconds representation for the year 8099.
A negative number indicates the number of milliseconds
before January 1, 1970, 00:00:00 GMT.

---

### Method Details

#### public void setTime​(long date)

Sets an existing

Date

object
using the given milliseconds time value.
If the given milliseconds value contains time information,
the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

**Overrides:**
- setTime

in class

Date

**Parameters:**
- date

- milliseconds since January 1, 1970, 00:00:00 GMT not
to exceed the milliseconds representation for the year 8099.
A negative number indicates the number of milliseconds
before January 1, 1970, 00:00:00 GMT.

---

#### public static
Date
valueOf​(
String
s)

Converts a string in JDBC date escape format to
a

Date

value.

**Parameters:**
- s

- a

String

object representing a date in
in the format "yyyy-[m]m-[d]d". The leading zero for

mm

and

dd

may also be omitted.

**Returns:**
- a

java.sql.Date

object representing the
given date

**Throws:**
- IllegalArgumentException

- if the date given is not in the
JDBC date escape format (yyyy-[m]m-[d]d)

---

#### public
String
toString()

Formats a date in the date escape format yyyy-mm-dd.

**Overrides:**
- toString

in class

Date

**Returns:**
- a String in yyyy-mm-dd format

**See Also:**
- Date.toLocaleString()

,

Date.toGMTString()

---

#### @Deprecated
(
since
="1.2")
public int getHours()

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:**
- getHours

in class

Date

**Returns:**
- the hour represented by this date.

**Throws:**
- IllegalArgumentException

- if this method is invoked

**See Also:**
- setHours(int)

---

#### @Deprecated
(
since
="1.2")
public int getMinutes()

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:**
- getMinutes

in class

Date

**Returns:**
- the number of minutes past the hour represented by this date.

**Throws:**
- IllegalArgumentException

- if this method is invoked

**See Also:**
- setMinutes(int)

---

#### @Deprecated
(
since
="1.2")
public int getSeconds()

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:**
- getSeconds

in class

Date

**Returns:**
- the number of seconds past the minute represented by this date.

**Throws:**
- IllegalArgumentException

- if this method is invoked

**See Also:**
- setSeconds(int)

---

#### @Deprecated
(
since
="1.2")
public void setHours​(int i)

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:**
- setHours

in class

Date

**Parameters:**
- i

- the hour value.

**Throws:**
- IllegalArgumentException

- if this method is invoked

**See Also:**
- getHours()

---

#### @Deprecated
(
since
="1.2")
public void setMinutes​(int i)

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:**
- setMinutes

in class

Date

**Parameters:**
- i

- the value of the minutes.

**Throws:**
- IllegalArgumentException

- if this method is invoked

**See Also:**
- getMinutes()

---

#### @Deprecated
(
since
="1.2")
public void setSeconds​(int i)

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:**
- setSeconds

in class

Date

**Parameters:**
- i

- the seconds value.

**Throws:**
- IllegalArgumentException

- if this method is invoked

**See Also:**
- getSeconds()

---

#### public static
Date
valueOf​(
LocalDate
date)

Obtains an instance of

Date

from a

LocalDate

object
with the same year, month and day of month value as the given

LocalDate

.

The provided

LocalDate

is interpreted as the local date
in the local time zone.

**Parameters:**
- date

- a

LocalDate

to convert

**Returns:**
- a

Date

object

**Throws:**
- NullPointerException

- if

date

is null

**Since:**
- 1.8

---

#### public
LocalDate
toLocalDate()

Creates a

LocalDate

instance using the year, month and day
from this

Date

object.

**Returns:**
- a

LocalDate

object representing the same date value

**Since:**
- 1.8

---

#### public
Instant
toInstant()

This method always throws an UnsupportedOperationException and should
not be used because SQL

Date

values do not have a time
component.

**Overrides:**
- toInstant

in class

Date

**Returns:**
- an instant representing the same point on the time-line as
this

Date

object

**Throws:**
- UnsupportedOperationException

- if this method is invoked

---

### Additional Sections

#### Class Date

java.lang.Object

- java.util.Date
- - java.sql.Date

java.util.Date

- java.sql.Date

java.sql.Date

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
Date

extends
Date
```

A thin wrapper around a millisecond value that allows
JDBC to identify this as an SQL

DATE

value. A
milliseconds value represents the number of milliseconds that
have passed since January 1, 1970 00:00:00.000 GMT.

To conform with the definition of SQL

DATE

, the
millisecond values wrapped by a

java.sql.Date

instance
must be 'normalized' by setting the
hours, minutes, seconds, and milliseconds to zero in the particular
time zone with which the instance is associated.

**Since:** 1.1
**See Also:** Serialized Form

public class

Date

extends

Date

A thin wrapper around a millisecond value that allows
JDBC to identify this as an SQL

DATE

value. A
milliseconds value represents the number of milliseconds that
have passed since January 1, 1970 00:00:00.000 GMT.

To conform with the definition of SQL

DATE

, the
millisecond values wrapped by a

java.sql.Date

instance
must be 'normalized' by setting the
hours, minutes, seconds, and milliseconds to zero in the particular
time zone with which the instance is associated.

To conform with the definition of SQL

DATE

, the
millisecond values wrapped by a

java.sql.Date

instance
must be 'normalized' by setting the
hours, minutes, seconds, and milliseconds to zero in the particular
time zone with which the instance is associated.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Date

​(int year,
int month,
int day)

Deprecated.

instead use the constructor

Date(long date)

Date

​(long date)

Constructs a

Date

object using the given milliseconds
time value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

getHours

()

Deprecated.

int

getMinutes

()

Deprecated.

int

getSeconds

()

Deprecated.

void

setHours

​(int i)

Deprecated.

void

setMinutes

​(int i)

Deprecated.

void

setSeconds

​(int i)

Deprecated.

void

setTime

​(long date)

Sets an existing

Date

object
using the given milliseconds time value.

Instant

toInstant

()

This method always throws an UnsupportedOperationException and should
not be used because SQL

Date

values do not have a time
component.

LocalDate

toLocalDate

()

Creates a

LocalDate

instance using the year, month and day
from this

Date

object.

String

toString

()

Formats a date in the date escape format yyyy-mm-dd.

static

Date

valueOf

​(

String

s)

Converts a string in JDBC date escape format to
a

Date

value.

static

Date

valueOf

​(

LocalDate

date)

Obtains an instance of

Date

from a

LocalDate

object
with the same year, month and day of month value as the given

LocalDate

.

- Methods declared in class java.util.

Date

after

,

before

,

clone

,

compareTo

,

equals

,

from

,

getDate

,

getDay

,

getMonth

,

getTime

,

getTimezoneOffset

,

getYear

,

hashCode

,

parse

,

setDate

,

setMonth

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

Date

​(int year,
int month,
int day)

Deprecated.

instead use the constructor

Date(long date)

Date

​(long date)

Constructs a

Date

object using the given milliseconds
time value.

---

#### Constructor Summary

Deprecated.

instead use the constructor

Date(long date)

Constructs a

Date

object using the given milliseconds
time value.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

getHours

()

Deprecated.

int

getMinutes

()

Deprecated.

int

getSeconds

()

Deprecated.

void

setHours

​(int i)

Deprecated.

void

setMinutes

​(int i)

Deprecated.

void

setSeconds

​(int i)

Deprecated.

void

setTime

​(long date)

Sets an existing

Date

object
using the given milliseconds time value.

Instant

toInstant

()

This method always throws an UnsupportedOperationException and should
not be used because SQL

Date

values do not have a time
component.

LocalDate

toLocalDate

()

Creates a

LocalDate

instance using the year, month and day
from this

Date

object.

String

toString

()

Formats a date in the date escape format yyyy-mm-dd.

static

Date

valueOf

​(

String

s)

Converts a string in JDBC date escape format to
a

Date

value.

static

Date

valueOf

​(

LocalDate

date)

Obtains an instance of

Date

from a

LocalDate

object
with the same year, month and day of month value as the given

LocalDate

.

- Methods declared in class java.util.

Date

after

,

before

,

clone

,

compareTo

,

equals

,

from

,

getDate

,

getDay

,

getMonth

,

getTime

,

getTimezoneOffset

,

getYear

,

hashCode

,

parse

,

setDate

,

setMonth

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

Deprecated.

Sets an existing

Date

object
using the given milliseconds time value.

This method always throws an UnsupportedOperationException and should
not be used because SQL

Date

values do not have a time
component.

Creates a

LocalDate

instance using the year, month and day
from this

Date

object.

Formats a date in the date escape format yyyy-mm-dd.

Converts a string in JDBC date escape format to
a

Date

value.

Obtains an instance of

Date

from a

LocalDate

object
with the same year, month and day of month value as the given

LocalDate

.

Methods declared in class java.util.

Date

after

,

before

,

clone

,

compareTo

,

equals

,

from

,

getDate

,

getDay

,

getMonth

,

getTime

,

getTimezoneOffset

,

getYear

,

hashCode

,

parse

,

setDate

,

setMonth

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

- Date

```java
@Deprecated
(
since
="1.2")
public Date​(int year,
int month,
int day)
```

Deprecated.

instead use the constructor

Date(long date)

Constructs a

Date

object initialized with the given
year, month, and day.

The result is undefined if a given argument is out of bounds.

**Parameters:** year

- the year minus 1900; must be 0 to 8099. (Note that
8099 is 9999 minus 1900.)
**Parameters:** month

- 0 to 11
**Parameters:** day

- 1 to 31

- Date

```java
public Date​(long date)
```

Constructs a

Date

object using the given milliseconds
time value. If the given milliseconds value contains time
information, the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

**Parameters:** date

- milliseconds since January 1, 1970, 00:00:00 GMT not
to exceed the milliseconds representation for the year 8099.
A negative number indicates the number of milliseconds
before January 1, 1970, 00:00:00 GMT.

============ METHOD DETAIL ==========

- Method Detail

- setTime

```java
public void setTime​(long date)
```

Sets an existing

Date

object
using the given milliseconds time value.
If the given milliseconds value contains time information,
the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

**Overrides:** setTime

in class

Date
**Parameters:** date

- milliseconds since January 1, 1970, 00:00:00 GMT not
to exceed the milliseconds representation for the year 8099.
A negative number indicates the number of milliseconds
before January 1, 1970, 00:00:00 GMT.

- valueOf

```java
public static
Date
valueOf​(
String
s)
```

Converts a string in JDBC date escape format to
a

Date

value.

**Parameters:** s

- a

String

object representing a date in
in the format "yyyy-[m]m-[d]d". The leading zero for

mm

and

dd

may also be omitted.
**Returns:** a

java.sql.Date

object representing the
given date
**Throws:** IllegalArgumentException

- if the date given is not in the
JDBC date escape format (yyyy-[m]m-[d]d)

- toString

```java
public
String
toString()
```

Formats a date in the date escape format yyyy-mm-dd.

**Overrides:** toString

in class

Date
**Returns:** a String in yyyy-mm-dd format
**See Also:** Date.toLocaleString()

,

Date.toGMTString()

- getHours

```java
@Deprecated
(
since
="1.2")
public int getHours()
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** getHours

in class

Date
**Returns:** the hour represented by this date.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** setHours(int)

- getMinutes

```java
@Deprecated
(
since
="1.2")
public int getMinutes()
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** getMinutes

in class

Date
**Returns:** the number of minutes past the hour represented by this date.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** setMinutes(int)

- getSeconds

```java
@Deprecated
(
since
="1.2")
public int getSeconds()
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** getSeconds

in class

Date
**Returns:** the number of seconds past the minute represented by this date.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** setSeconds(int)

- setHours

```java
@Deprecated
(
since
="1.2")
public void setHours​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** setHours

in class

Date
**Parameters:** i

- the hour value.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** getHours()

- setMinutes

```java
@Deprecated
(
since
="1.2")
public void setMinutes​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** setMinutes

in class

Date
**Parameters:** i

- the value of the minutes.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** getMinutes()

- setSeconds

```java
@Deprecated
(
since
="1.2")
public void setSeconds​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** setSeconds

in class

Date
**Parameters:** i

- the seconds value.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** getSeconds()

- valueOf

```java
public static
Date
valueOf​(
LocalDate
date)
```

Obtains an instance of

Date

from a

LocalDate

object
with the same year, month and day of month value as the given

LocalDate

.

The provided

LocalDate

is interpreted as the local date
in the local time zone.

**Parameters:** date

- a

LocalDate

to convert
**Returns:** a

Date

object
**Throws:** NullPointerException

- if

date

is null
**Since:** 1.8

- toLocalDate

```java
public
LocalDate
toLocalDate()
```

Creates a

LocalDate

instance using the year, month and day
from this

Date

object.

**Returns:** a

LocalDate

object representing the same date value
**Since:** 1.8

- toInstant

```java
public
Instant
toInstant()
```

This method always throws an UnsupportedOperationException and should
not be used because SQL

Date

values do not have a time
component.

**Overrides:** toInstant

in class

Date
**Returns:** an instant representing the same point on the time-line as
this

Date

object
**Throws:** UnsupportedOperationException

- if this method is invoked

Constructor Detail

- Date

```java
@Deprecated
(
since
="1.2")
public Date​(int year,
int month,
int day)
```

Deprecated.

instead use the constructor

Date(long date)

Constructs a

Date

object initialized with the given
year, month, and day.

The result is undefined if a given argument is out of bounds.

**Parameters:** year

- the year minus 1900; must be 0 to 8099. (Note that
8099 is 9999 minus 1900.)
**Parameters:** month

- 0 to 11
**Parameters:** day

- 1 to 31

- Date

```java
public Date​(long date)
```

Constructs a

Date

object using the given milliseconds
time value. If the given milliseconds value contains time
information, the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

**Parameters:** date

- milliseconds since January 1, 1970, 00:00:00 GMT not
to exceed the milliseconds representation for the year 8099.
A negative number indicates the number of milliseconds
before January 1, 1970, 00:00:00 GMT.

---

#### Constructor Detail

Date

```java
@Deprecated
(
since
="1.2")
public Date​(int year,
int month,
int day)
```

Deprecated.

instead use the constructor

Date(long date)

Constructs a

Date

object initialized with the given
year, month, and day.

The result is undefined if a given argument is out of bounds.

**Parameters:** year

- the year minus 1900; must be 0 to 8099. (Note that
8099 is 9999 minus 1900.)
**Parameters:** month

- 0 to 11
**Parameters:** day

- 1 to 31

---

#### Date

@Deprecated

(

since

="1.2")
public Date​(int year,
int month,
int day)

Constructs a

Date

object initialized with the given
year, month, and day.

The result is undefined if a given argument is out of bounds.

The result is undefined if a given argument is out of bounds.

Date

```java
public Date​(long date)
```

Constructs a

Date

object using the given milliseconds
time value. If the given milliseconds value contains time
information, the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

**Parameters:** date

- milliseconds since January 1, 1970, 00:00:00 GMT not
to exceed the milliseconds representation for the year 8099.
A negative number indicates the number of milliseconds
before January 1, 1970, 00:00:00 GMT.

---

#### Date

public Date​(long date)

Constructs a

Date

object using the given milliseconds
time value. If the given milliseconds value contains time
information, the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

Method Detail

- setTime

```java
public void setTime​(long date)
```

Sets an existing

Date

object
using the given milliseconds time value.
If the given milliseconds value contains time information,
the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

**Overrides:** setTime

in class

Date
**Parameters:** date

- milliseconds since January 1, 1970, 00:00:00 GMT not
to exceed the milliseconds representation for the year 8099.
A negative number indicates the number of milliseconds
before January 1, 1970, 00:00:00 GMT.

- valueOf

```java
public static
Date
valueOf​(
String
s)
```

Converts a string in JDBC date escape format to
a

Date

value.

**Parameters:** s

- a

String

object representing a date in
in the format "yyyy-[m]m-[d]d". The leading zero for

mm

and

dd

may also be omitted.
**Returns:** a

java.sql.Date

object representing the
given date
**Throws:** IllegalArgumentException

- if the date given is not in the
JDBC date escape format (yyyy-[m]m-[d]d)

- toString

```java
public
String
toString()
```

Formats a date in the date escape format yyyy-mm-dd.

**Overrides:** toString

in class

Date
**Returns:** a String in yyyy-mm-dd format
**See Also:** Date.toLocaleString()

,

Date.toGMTString()

- getHours

```java
@Deprecated
(
since
="1.2")
public int getHours()
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** getHours

in class

Date
**Returns:** the hour represented by this date.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** setHours(int)

- getMinutes

```java
@Deprecated
(
since
="1.2")
public int getMinutes()
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** getMinutes

in class

Date
**Returns:** the number of minutes past the hour represented by this date.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** setMinutes(int)

- getSeconds

```java
@Deprecated
(
since
="1.2")
public int getSeconds()
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** getSeconds

in class

Date
**Returns:** the number of seconds past the minute represented by this date.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** setSeconds(int)

- setHours

```java
@Deprecated
(
since
="1.2")
public void setHours​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** setHours

in class

Date
**Parameters:** i

- the hour value.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** getHours()

- setMinutes

```java
@Deprecated
(
since
="1.2")
public void setMinutes​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** setMinutes

in class

Date
**Parameters:** i

- the value of the minutes.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** getMinutes()

- setSeconds

```java
@Deprecated
(
since
="1.2")
public void setSeconds​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** setSeconds

in class

Date
**Parameters:** i

- the seconds value.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** getSeconds()

- valueOf

```java
public static
Date
valueOf​(
LocalDate
date)
```

Obtains an instance of

Date

from a

LocalDate

object
with the same year, month and day of month value as the given

LocalDate

.

The provided

LocalDate

is interpreted as the local date
in the local time zone.

**Parameters:** date

- a

LocalDate

to convert
**Returns:** a

Date

object
**Throws:** NullPointerException

- if

date

is null
**Since:** 1.8

- toLocalDate

```java
public
LocalDate
toLocalDate()
```

Creates a

LocalDate

instance using the year, month and day
from this

Date

object.

**Returns:** a

LocalDate

object representing the same date value
**Since:** 1.8

- toInstant

```java
public
Instant
toInstant()
```

This method always throws an UnsupportedOperationException and should
not be used because SQL

Date

values do not have a time
component.

**Overrides:** toInstant

in class

Date
**Returns:** an instant representing the same point on the time-line as
this

Date

object
**Throws:** UnsupportedOperationException

- if this method is invoked

---

#### Method Detail

setTime

```java
public void setTime​(long date)
```

Sets an existing

Date

object
using the given milliseconds time value.
If the given milliseconds value contains time information,
the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

**Overrides:** setTime

in class

Date
**Parameters:** date

- milliseconds since January 1, 1970, 00:00:00 GMT not
to exceed the milliseconds representation for the year 8099.
A negative number indicates the number of milliseconds
before January 1, 1970, 00:00:00 GMT.

---

#### setTime

public void setTime​(long date)

Sets an existing

Date

object
using the given milliseconds time value.
If the given milliseconds value contains time information,
the driver will set the time components to the
time in the default time zone (the time zone of the Java virtual
machine running the application) that corresponds to zero GMT.

valueOf

```java
public static
Date
valueOf​(
String
s)
```

Converts a string in JDBC date escape format to
a

Date

value.

**Parameters:** s

- a

String

object representing a date in
in the format "yyyy-[m]m-[d]d". The leading zero for

mm

and

dd

may also be omitted.
**Returns:** a

java.sql.Date

object representing the
given date
**Throws:** IllegalArgumentException

- if the date given is not in the
JDBC date escape format (yyyy-[m]m-[d]d)

---

#### valueOf

public static

Date

valueOf​(

String

s)

Converts a string in JDBC date escape format to
a

Date

value.

toString

```java
public
String
toString()
```

Formats a date in the date escape format yyyy-mm-dd.

**Overrides:** toString

in class

Date
**Returns:** a String in yyyy-mm-dd format
**See Also:** Date.toLocaleString()

,

Date.toGMTString()

---

#### toString

public

String

toString()

Formats a date in the date escape format yyyy-mm-dd.

getHours

```java
@Deprecated
(
since
="1.2")
public int getHours()
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** getHours

in class

Date
**Returns:** the hour represented by this date.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** setHours(int)

---

#### getHours

@Deprecated

(

since

="1.2")
public int getHours()

This method is deprecated and should not be used because SQL Date
values do not have a time component.

getMinutes

```java
@Deprecated
(
since
="1.2")
public int getMinutes()
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** getMinutes

in class

Date
**Returns:** the number of minutes past the hour represented by this date.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** setMinutes(int)

---

#### getMinutes

@Deprecated

(

since

="1.2")
public int getMinutes()

This method is deprecated and should not be used because SQL Date
values do not have a time component.

getSeconds

```java
@Deprecated
(
since
="1.2")
public int getSeconds()
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** getSeconds

in class

Date
**Returns:** the number of seconds past the minute represented by this date.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** setSeconds(int)

---

#### getSeconds

@Deprecated

(

since

="1.2")
public int getSeconds()

This method is deprecated and should not be used because SQL Date
values do not have a time component.

setHours

```java
@Deprecated
(
since
="1.2")
public void setHours​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** setHours

in class

Date
**Parameters:** i

- the hour value.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** getHours()

---

#### setHours

@Deprecated

(

since

="1.2")
public void setHours​(int i)

This method is deprecated and should not be used because SQL Date
values do not have a time component.

setMinutes

```java
@Deprecated
(
since
="1.2")
public void setMinutes​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** setMinutes

in class

Date
**Parameters:** i

- the value of the minutes.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** getMinutes()

---

#### setMinutes

@Deprecated

(

since

="1.2")
public void setMinutes​(int i)

This method is deprecated and should not be used because SQL Date
values do not have a time component.

setSeconds

```java
@Deprecated
(
since
="1.2")
public void setSeconds​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL Date
values do not have a time component.

**Overrides:** setSeconds

in class

Date
**Parameters:** i

- the seconds value.
**Throws:** IllegalArgumentException

- if this method is invoked
**See Also:** getSeconds()

---

#### setSeconds

@Deprecated

(

since

="1.2")
public void setSeconds​(int i)

This method is deprecated and should not be used because SQL Date
values do not have a time component.

valueOf

```java
public static
Date
valueOf​(
LocalDate
date)
```

Obtains an instance of

Date

from a

LocalDate

object
with the same year, month and day of month value as the given

LocalDate

.

The provided

LocalDate

is interpreted as the local date
in the local time zone.

**Parameters:** date

- a

LocalDate

to convert
**Returns:** a

Date

object
**Throws:** NullPointerException

- if

date

is null
**Since:** 1.8

---

#### valueOf

public static

Date

valueOf​(

LocalDate

date)

Obtains an instance of

Date

from a

LocalDate

object
with the same year, month and day of month value as the given

LocalDate

.

The provided

LocalDate

is interpreted as the local date
in the local time zone.

The provided

LocalDate

is interpreted as the local date
in the local time zone.

toLocalDate

```java
public
LocalDate
toLocalDate()
```

Creates a

LocalDate

instance using the year, month and day
from this

Date

object.

**Returns:** a

LocalDate

object representing the same date value
**Since:** 1.8

---

#### toLocalDate

public

LocalDate

toLocalDate()

Creates a

LocalDate

instance using the year, month and day
from this

Date

object.

toInstant

```java
public
Instant
toInstant()
```

This method always throws an UnsupportedOperationException and should
not be used because SQL

Date

values do not have a time
component.

**Overrides:** toInstant

in class

Date
**Returns:** an instant representing the same point on the time-line as
this

Date

object
**Throws:** UnsupportedOperationException

- if this method is invoked

---

#### toInstant

public

Instant

toInstant()

This method always throws an UnsupportedOperationException and should
not be used because SQL

Date

values do not have a time
component.

---

