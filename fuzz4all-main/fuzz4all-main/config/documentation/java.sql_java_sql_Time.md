# Class Time

**Source:** `java.sql\java\sql\Time.html`

### Class Description

```java
public class
Time

extends
Date
```

A thin wrapper around the

java.util.Date

class that allows the JDBC
API to identify this as an SQL

TIME

value. The

Time

class adds formatting and
parsing operations to support the JDBC escape syntax for time
values.

The date components should be set to the "zero epoch"
value of January 1, 1970 and should not be accessed.

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
public Time​(int hour,
int minute,
int second)

Constructs a

Time

object initialized with the
given values for the hour, minute, and second.
The driver sets the date components to January 1, 1970.
Any method that attempts to access the date components of a

Time

object will throw a

java.lang.IllegalArgumentException

.

The result is undefined if a given argument is out of bounds.

**Parameters:**
- hour

- 0 to 23
- minute

- 0 to 59
- second

- 0 to 59

---

#### public Time​(long time)

Constructs a

Time

object using a milliseconds time value.

**Parameters:**
- time

- milliseconds since January 1, 1970, 00:00:00 GMT;
a negative number is milliseconds before
January 1, 1970, 00:00:00 GMT

---

### Method Details

#### public void setTime​(long time)

Sets a

Time

object using a milliseconds time value.

**Overrides:**
- setTime

in class

Date

**Parameters:**
- time

- milliseconds since January 1, 1970, 00:00:00 GMT;
a negative number is milliseconds before
January 1, 1970, 00:00:00 GMT

---

#### public static
Time
valueOf​(
String
s)

Converts a string in JDBC time escape format to a

Time

value.

**Parameters:**
- s

- time in format "hh:mm:ss"

**Returns:**
- a corresponding

Time

object

---

#### public
String
toString()

Formats a time in JDBC time escape format.

**Overrides:**
- toString

in class

Date

**Returns:**
- a

String

in hh:mm:ss format

**See Also:**
- Date.toLocaleString()

,

Date.toGMTString()

---

#### @Deprecated
(
since
="1.2")
public int getYear()

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

**Overrides:**
- getYear

in class

Date

**Returns:**
- the year represented by this date, minus 1900.

**Throws:**
- IllegalArgumentException

- if this
method is invoked

**See Also:**
- setYear(int)

---

#### @Deprecated
(
since
="1.2")
public int getMonth()

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

**Overrides:**
- getMonth

in class

Date

**Returns:**
- the month represented by this date.

**Throws:**
- IllegalArgumentException

- if this
method is invoked

**See Also:**
- setMonth(int)

---

#### @Deprecated
(
since
="1.2")
public int getDay()

This method is deprecated and should not be used because SQL

TIME

values do not have a day component.

**Overrides:**
- getDay

in class

Date

**Returns:**
- the day of the week represented by this date.

**Throws:**
- IllegalArgumentException

- if this
method is invoked

**See Also:**
- Calendar

---

#### @Deprecated
(
since
="1.2")
public int getDate()

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

**Overrides:**
- getDate

in class

Date

**Returns:**
- the day of the month represented by this date.

**Throws:**
- IllegalArgumentException

- if this
method is invoked

**See Also:**
- setDate(int)

---

#### @Deprecated
(
since
="1.2")
public void setYear​(int i)

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

**Overrides:**
- setYear

in class

Date

**Parameters:**
- i

- the year value.

**Throws:**
- IllegalArgumentException

- if this
method is invoked

**See Also:**
- getYear()

---

#### @Deprecated
(
since
="1.2")
public void setMonth​(int i)

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

**Overrides:**
- setMonth

in class

Date

**Parameters:**
- i

- the month value between 0-11.

**Throws:**
- IllegalArgumentException

- if this
method is invoked

**See Also:**
- getMonth()

---

#### @Deprecated
(
since
="1.2")
public void setDate​(int i)

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

**Overrides:**
- setDate

in class

Date

**Parameters:**
- i

- the day of the month value between 1-31.

**Throws:**
- IllegalArgumentException

- if this
method is invoked

**See Also:**
- getDate()

---

#### public static
Time
valueOf​(
LocalTime
time)

Obtains an instance of

Time

from a

LocalTime

object
with the same hour, minute and second time value as the given

LocalTime

. The nanosecond field from

LocalTime

is
not part of the newly created

Time

object.

**Parameters:**
- time

- a

LocalTime

to convert

**Returns:**
- a

Time

object

**Throws:**
- NullPointerException

- if

time

is null

**Since:**
- 1.8

---

#### public
LocalTime
toLocalTime()

Converts this

Time

object to a

LocalTime

.

The conversion creates a

LocalTime

that represents the same
hour, minute, and second time value as this

Time

. The
nanosecond

LocalTime

field will be set to zero.

**Returns:**
- a

LocalTime

object representing the same time value

**Since:**
- 1.8

---

#### public
Instant
toInstant()

This method always throws an UnsupportedOperationException and should
not be used because SQL

Time

values do not have a date
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

#### Class Time

java.lang.Object

- java.util.Date
- - java.sql.Time

java.util.Date

- java.sql.Time

java.sql.Time

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
Time

extends
Date
```

A thin wrapper around the

java.util.Date

class that allows the JDBC
API to identify this as an SQL

TIME

value. The

Time

class adds formatting and
parsing operations to support the JDBC escape syntax for time
values.

The date components should be set to the "zero epoch"
value of January 1, 1970 and should not be accessed.

**Since:** 1.1
**See Also:** Serialized Form

public class

Time

extends

Date

A thin wrapper around the

java.util.Date

class that allows the JDBC
API to identify this as an SQL

TIME

value. The

Time

class adds formatting and
parsing operations to support the JDBC escape syntax for time
values.

The date components should be set to the "zero epoch"
value of January 1, 1970 and should not be accessed.

The date components should be set to the "zero epoch"
value of January 1, 1970 and should not be accessed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Time

​(int hour,
int minute,
int second)

Deprecated.

Use the constructor that takes a milliseconds value
in place of this constructor

Time

​(long time)

Constructs a

Time

object using a milliseconds time value.

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

getDate

()

Deprecated.

int

getDay

()

Deprecated.

int

getMonth

()

Deprecated.

int

getYear

()

Deprecated.

void

setDate

​(int i)

Deprecated.

void

setMonth

​(int i)

Deprecated.

void

setTime

​(long time)

Sets a

Time

object using a milliseconds time value.

void

setYear

​(int i)

Deprecated.

Instant

toInstant

()

This method always throws an UnsupportedOperationException and should
not be used because SQL

Time

values do not have a date
component.

LocalTime

toLocalTime

()

Converts this

Time

object to a

LocalTime

.

String

toString

()

Formats a time in JDBC time escape format.

static

Time

valueOf

​(

String

s)

Converts a string in JDBC time escape format to a

Time

value.

static

Time

valueOf

​(

LocalTime

time)

Obtains an instance of

Time

from a

LocalTime

object
with the same hour, minute and second time value as the given

LocalTime

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

getHours

,

getMinutes

,

getSeconds

,

getTime

,

getTimezoneOffset

,

hashCode

,

parse

,

setHours

,

setMinutes

,

setSeconds

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

Time

​(int hour,
int minute,
int second)

Deprecated.

Use the constructor that takes a milliseconds value
in place of this constructor

Time

​(long time)

Constructs a

Time

object using a milliseconds time value.

---

#### Constructor Summary

Deprecated.

Use the constructor that takes a milliseconds value
in place of this constructor

Constructs a

Time

object using a milliseconds time value.

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

getDate

()

Deprecated.

int

getDay

()

Deprecated.

int

getMonth

()

Deprecated.

int

getYear

()

Deprecated.

void

setDate

​(int i)

Deprecated.

void

setMonth

​(int i)

Deprecated.

void

setTime

​(long time)

Sets a

Time

object using a milliseconds time value.

void

setYear

​(int i)

Deprecated.

Instant

toInstant

()

This method always throws an UnsupportedOperationException and should
not be used because SQL

Time

values do not have a date
component.

LocalTime

toLocalTime

()

Converts this

Time

object to a

LocalTime

.

String

toString

()

Formats a time in JDBC time escape format.

static

Time

valueOf

​(

String

s)

Converts a string in JDBC time escape format to a

Time

value.

static

Time

valueOf

​(

LocalTime

time)

Obtains an instance of

Time

from a

LocalTime

object
with the same hour, minute and second time value as the given

LocalTime

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

getHours

,

getMinutes

,

getSeconds

,

getTime

,

getTimezoneOffset

,

hashCode

,

parse

,

setHours

,

setMinutes

,

setSeconds

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

Sets a

Time

object using a milliseconds time value.

This method always throws an UnsupportedOperationException and should
not be used because SQL

Time

values do not have a date
component.

Converts this

Time

object to a

LocalTime

.

Formats a time in JDBC time escape format.

Converts a string in JDBC time escape format to a

Time

value.

Obtains an instance of

Time

from a

LocalTime

object
with the same hour, minute and second time value as the given

LocalTime

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

getHours

,

getMinutes

,

getSeconds

,

getTime

,

getTimezoneOffset

,

hashCode

,

parse

,

setHours

,

setMinutes

,

setSeconds

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

- Time

```java
@Deprecated
(
since
="1.2")
public Time​(int hour,
int minute,
int second)
```

Deprecated.

Use the constructor that takes a milliseconds value
in place of this constructor

Constructs a

Time

object initialized with the
given values for the hour, minute, and second.
The driver sets the date components to January 1, 1970.
Any method that attempts to access the date components of a

Time

object will throw a

java.lang.IllegalArgumentException

.

The result is undefined if a given argument is out of bounds.

**Parameters:** hour

- 0 to 23
**Parameters:** minute

- 0 to 59
**Parameters:** second

- 0 to 59

- Time

```java
public Time​(long time)
```

Constructs a

Time

object using a milliseconds time value.

**Parameters:** time

- milliseconds since January 1, 1970, 00:00:00 GMT;
a negative number is milliseconds before
January 1, 1970, 00:00:00 GMT

============ METHOD DETAIL ==========

- Method Detail

- setTime

```java
public void setTime​(long time)
```

Sets a

Time

object using a milliseconds time value.

**Overrides:** setTime

in class

Date
**Parameters:** time

- milliseconds since January 1, 1970, 00:00:00 GMT;
a negative number is milliseconds before
January 1, 1970, 00:00:00 GMT

- valueOf

```java
public static
Time
valueOf​(
String
s)
```

Converts a string in JDBC time escape format to a

Time

value.

**Parameters:** s

- time in format "hh:mm:ss"
**Returns:** a corresponding

Time

object

- toString

```java
public
String
toString()
```

Formats a time in JDBC time escape format.

**Overrides:** toString

in class

Date
**Returns:** a

String

in hh:mm:ss format
**See Also:** Date.toLocaleString()

,

Date.toGMTString()

- getYear

```java
@Deprecated
(
since
="1.2")
public int getYear()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

**Overrides:** getYear

in class

Date
**Returns:** the year represented by this date, minus 1900.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** setYear(int)

- getMonth

```java
@Deprecated
(
since
="1.2")
public int getMonth()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

**Overrides:** getMonth

in class

Date
**Returns:** the month represented by this date.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** setMonth(int)

- getDay

```java
@Deprecated
(
since
="1.2")
public int getDay()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a day component.

**Overrides:** getDay

in class

Date
**Returns:** the day of the week represented by this date.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** Calendar

- getDate

```java
@Deprecated
(
since
="1.2")
public int getDate()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

**Overrides:** getDate

in class

Date
**Returns:** the day of the month represented by this date.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** setDate(int)

- setYear

```java
@Deprecated
(
since
="1.2")
public void setYear​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

**Overrides:** setYear

in class

Date
**Parameters:** i

- the year value.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** getYear()

- setMonth

```java
@Deprecated
(
since
="1.2")
public void setMonth​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

**Overrides:** setMonth

in class

Date
**Parameters:** i

- the month value between 0-11.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** getMonth()

- setDate

```java
@Deprecated
(
since
="1.2")
public void setDate​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

**Overrides:** setDate

in class

Date
**Parameters:** i

- the day of the month value between 1-31.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** getDate()

- valueOf

```java
public static
Time
valueOf​(
LocalTime
time)
```

Obtains an instance of

Time

from a

LocalTime

object
with the same hour, minute and second time value as the given

LocalTime

. The nanosecond field from

LocalTime

is
not part of the newly created

Time

object.

**Parameters:** time

- a

LocalTime

to convert
**Returns:** a

Time

object
**Throws:** NullPointerException

- if

time

is null
**Since:** 1.8

- toLocalTime

```java
public
LocalTime
toLocalTime()
```

Converts this

Time

object to a

LocalTime

.

The conversion creates a

LocalTime

that represents the same
hour, minute, and second time value as this

Time

. The
nanosecond

LocalTime

field will be set to zero.

**Returns:** a

LocalTime

object representing the same time value
**Since:** 1.8

- toInstant

```java
public
Instant
toInstant()
```

This method always throws an UnsupportedOperationException and should
not be used because SQL

Time

values do not have a date
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

- Time

```java
@Deprecated
(
since
="1.2")
public Time​(int hour,
int minute,
int second)
```

Deprecated.

Use the constructor that takes a milliseconds value
in place of this constructor

Constructs a

Time

object initialized with the
given values for the hour, minute, and second.
The driver sets the date components to January 1, 1970.
Any method that attempts to access the date components of a

Time

object will throw a

java.lang.IllegalArgumentException

.

The result is undefined if a given argument is out of bounds.

**Parameters:** hour

- 0 to 23
**Parameters:** minute

- 0 to 59
**Parameters:** second

- 0 to 59

- Time

```java
public Time​(long time)
```

Constructs a

Time

object using a milliseconds time value.

**Parameters:** time

- milliseconds since January 1, 1970, 00:00:00 GMT;
a negative number is milliseconds before
January 1, 1970, 00:00:00 GMT

---

#### Constructor Detail

Time

```java
@Deprecated
(
since
="1.2")
public Time​(int hour,
int minute,
int second)
```

Deprecated.

Use the constructor that takes a milliseconds value
in place of this constructor

Constructs a

Time

object initialized with the
given values for the hour, minute, and second.
The driver sets the date components to January 1, 1970.
Any method that attempts to access the date components of a

Time

object will throw a

java.lang.IllegalArgumentException

.

The result is undefined if a given argument is out of bounds.

**Parameters:** hour

- 0 to 23
**Parameters:** minute

- 0 to 59
**Parameters:** second

- 0 to 59

---

#### Time

@Deprecated

(

since

="1.2")
public Time​(int hour,
int minute,
int second)

Constructs a

Time

object initialized with the
given values for the hour, minute, and second.
The driver sets the date components to January 1, 1970.
Any method that attempts to access the date components of a

Time

object will throw a

java.lang.IllegalArgumentException

.

The result is undefined if a given argument is out of bounds.

The result is undefined if a given argument is out of bounds.

Time

```java
public Time​(long time)
```

Constructs a

Time

object using a milliseconds time value.

**Parameters:** time

- milliseconds since January 1, 1970, 00:00:00 GMT;
a negative number is milliseconds before
January 1, 1970, 00:00:00 GMT

---

#### Time

public Time​(long time)

Constructs a

Time

object using a milliseconds time value.

Method Detail

- setTime

```java
public void setTime​(long time)
```

Sets a

Time

object using a milliseconds time value.

**Overrides:** setTime

in class

Date
**Parameters:** time

- milliseconds since January 1, 1970, 00:00:00 GMT;
a negative number is milliseconds before
January 1, 1970, 00:00:00 GMT

- valueOf

```java
public static
Time
valueOf​(
String
s)
```

Converts a string in JDBC time escape format to a

Time

value.

**Parameters:** s

- time in format "hh:mm:ss"
**Returns:** a corresponding

Time

object

- toString

```java
public
String
toString()
```

Formats a time in JDBC time escape format.

**Overrides:** toString

in class

Date
**Returns:** a

String

in hh:mm:ss format
**See Also:** Date.toLocaleString()

,

Date.toGMTString()

- getYear

```java
@Deprecated
(
since
="1.2")
public int getYear()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

**Overrides:** getYear

in class

Date
**Returns:** the year represented by this date, minus 1900.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** setYear(int)

- getMonth

```java
@Deprecated
(
since
="1.2")
public int getMonth()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

**Overrides:** getMonth

in class

Date
**Returns:** the month represented by this date.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** setMonth(int)

- getDay

```java
@Deprecated
(
since
="1.2")
public int getDay()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a day component.

**Overrides:** getDay

in class

Date
**Returns:** the day of the week represented by this date.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** Calendar

- getDate

```java
@Deprecated
(
since
="1.2")
public int getDate()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

**Overrides:** getDate

in class

Date
**Returns:** the day of the month represented by this date.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** setDate(int)

- setYear

```java
@Deprecated
(
since
="1.2")
public void setYear​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

**Overrides:** setYear

in class

Date
**Parameters:** i

- the year value.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** getYear()

- setMonth

```java
@Deprecated
(
since
="1.2")
public void setMonth​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

**Overrides:** setMonth

in class

Date
**Parameters:** i

- the month value between 0-11.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** getMonth()

- setDate

```java
@Deprecated
(
since
="1.2")
public void setDate​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

**Overrides:** setDate

in class

Date
**Parameters:** i

- the day of the month value between 1-31.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** getDate()

- valueOf

```java
public static
Time
valueOf​(
LocalTime
time)
```

Obtains an instance of

Time

from a

LocalTime

object
with the same hour, minute and second time value as the given

LocalTime

. The nanosecond field from

LocalTime

is
not part of the newly created

Time

object.

**Parameters:** time

- a

LocalTime

to convert
**Returns:** a

Time

object
**Throws:** NullPointerException

- if

time

is null
**Since:** 1.8

- toLocalTime

```java
public
LocalTime
toLocalTime()
```

Converts this

Time

object to a

LocalTime

.

The conversion creates a

LocalTime

that represents the same
hour, minute, and second time value as this

Time

. The
nanosecond

LocalTime

field will be set to zero.

**Returns:** a

LocalTime

object representing the same time value
**Since:** 1.8

- toInstant

```java
public
Instant
toInstant()
```

This method always throws an UnsupportedOperationException and should
not be used because SQL

Time

values do not have a date
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
public void setTime​(long time)
```

Sets a

Time

object using a milliseconds time value.

**Overrides:** setTime

in class

Date
**Parameters:** time

- milliseconds since January 1, 1970, 00:00:00 GMT;
a negative number is milliseconds before
January 1, 1970, 00:00:00 GMT

---

#### setTime

public void setTime​(long time)

Sets a

Time

object using a milliseconds time value.

valueOf

```java
public static
Time
valueOf​(
String
s)
```

Converts a string in JDBC time escape format to a

Time

value.

**Parameters:** s

- time in format "hh:mm:ss"
**Returns:** a corresponding

Time

object

---

#### valueOf

public static

Time

valueOf​(

String

s)

Converts a string in JDBC time escape format to a

Time

value.

toString

```java
public
String
toString()
```

Formats a time in JDBC time escape format.

**Overrides:** toString

in class

Date
**Returns:** a

String

in hh:mm:ss format
**See Also:** Date.toLocaleString()

,

Date.toGMTString()

---

#### toString

public

String

toString()

Formats a time in JDBC time escape format.

getYear

```java
@Deprecated
(
since
="1.2")
public int getYear()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

**Overrides:** getYear

in class

Date
**Returns:** the year represented by this date, minus 1900.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** setYear(int)

---

#### getYear

@Deprecated

(

since

="1.2")
public int getYear()

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

getMonth

```java
@Deprecated
(
since
="1.2")
public int getMonth()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

**Overrides:** getMonth

in class

Date
**Returns:** the month represented by this date.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** setMonth(int)

---

#### getMonth

@Deprecated

(

since

="1.2")
public int getMonth()

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

getDay

```java
@Deprecated
(
since
="1.2")
public int getDay()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a day component.

**Overrides:** getDay

in class

Date
**Returns:** the day of the week represented by this date.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** Calendar

---

#### getDay

@Deprecated

(

since

="1.2")
public int getDay()

This method is deprecated and should not be used because SQL

TIME

values do not have a day component.

getDate

```java
@Deprecated
(
since
="1.2")
public int getDate()
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

**Overrides:** getDate

in class

Date
**Returns:** the day of the month represented by this date.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** setDate(int)

---

#### getDate

@Deprecated

(

since

="1.2")
public int getDate()

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

setYear

```java
@Deprecated
(
since
="1.2")
public void setYear​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

**Overrides:** setYear

in class

Date
**Parameters:** i

- the year value.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** getYear()

---

#### setYear

@Deprecated

(

since

="1.2")
public void setYear​(int i)

This method is deprecated and should not be used because SQL

TIME

values do not have a year component.

setMonth

```java
@Deprecated
(
since
="1.2")
public void setMonth​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

**Overrides:** setMonth

in class

Date
**Parameters:** i

- the month value between 0-11.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** getMonth()

---

#### setMonth

@Deprecated

(

since

="1.2")
public void setMonth​(int i)

This method is deprecated and should not be used because SQL

TIME

values do not have a month component.

setDate

```java
@Deprecated
(
since
="1.2")
public void setDate​(int i)
```

Deprecated.

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

**Overrides:** setDate

in class

Date
**Parameters:** i

- the day of the month value between 1-31.
**Throws:** IllegalArgumentException

- if this
method is invoked
**See Also:** getDate()

---

#### setDate

@Deprecated

(

since

="1.2")
public void setDate​(int i)

This method is deprecated and should not be used because SQL

TIME

values do not have a date component.

valueOf

```java
public static
Time
valueOf​(
LocalTime
time)
```

Obtains an instance of

Time

from a

LocalTime

object
with the same hour, minute and second time value as the given

LocalTime

. The nanosecond field from

LocalTime

is
not part of the newly created

Time

object.

**Parameters:** time

- a

LocalTime

to convert
**Returns:** a

Time

object
**Throws:** NullPointerException

- if

time

is null
**Since:** 1.8

---

#### valueOf

public static

Time

valueOf​(

LocalTime

time)

Obtains an instance of

Time

from a

LocalTime

object
with the same hour, minute and second time value as the given

LocalTime

. The nanosecond field from

LocalTime

is
not part of the newly created

Time

object.

toLocalTime

```java
public
LocalTime
toLocalTime()
```

Converts this

Time

object to a

LocalTime

.

The conversion creates a

LocalTime

that represents the same
hour, minute, and second time value as this

Time

. The
nanosecond

LocalTime

field will be set to zero.

**Returns:** a

LocalTime

object representing the same time value
**Since:** 1.8

---

#### toLocalTime

public

LocalTime

toLocalTime()

Converts this

Time

object to a

LocalTime

.

The conversion creates a

LocalTime

that represents the same
hour, minute, and second time value as this

Time

. The
nanosecond

LocalTime

field will be set to zero.

The conversion creates a

LocalTime

that represents the same
hour, minute, and second time value as this

Time

. The
nanosecond

LocalTime

field will be set to zero.

toInstant

```java
public
Instant
toInstant()
```

This method always throws an UnsupportedOperationException and should
not be used because SQL

Time

values do not have a date
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

Time

values do not have a date
component.

---

