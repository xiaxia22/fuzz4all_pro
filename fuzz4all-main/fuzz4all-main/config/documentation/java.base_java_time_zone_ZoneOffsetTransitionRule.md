# Class ZoneOffsetTransitionRule

**Source:** `java.base\java\time\zone\ZoneOffsetTransitionRule.html`

### Class Description

```java
public final class
ZoneOffsetTransitionRule

extends
Object

implements
Serializable
```

A rule expressing how to create a transition.

This class allows rules for identifying future transitions to be expressed.
A rule might be written in many forms:

- the 16th March

the Sunday on or after the 16th March

the Sunday on or before the 16th March

the last Sunday in February

These different rule types can be expressed and queried.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ZoneOffsetTransitionRule
of​(
Month
month,
int dayOfMonthIndicator,

DayOfWeek
dayOfWeek,

LocalTime
time,
boolean timeEndOfDay,

ZoneOffsetTransitionRule.TimeDefinition
timeDefnition,

ZoneOffset
standardOffset,

ZoneOffset
offsetBefore,

ZoneOffset
offsetAfter)

Obtains an instance defining the yearly rule to create transitions between two offsets.

Applications should normally obtain an instance from

ZoneRules

.
This factory is only intended for use when creating

ZoneRules

.

**Parameters:**
- month

- the month of the month-day of the first day of the cutover week, not null
- dayOfMonthIndicator

- the day of the month-day of the cutover week, positive if the week is that
day or later, negative if the week is that day or earlier, counting from the last day of the month,
from -28 to 31 excluding 0
- dayOfWeek

- the required day-of-week, null if the month-day should not be changed
- time

- the cutover time in the 'before' offset, not null
- timeEndOfDay

- whether the time is midnight at the end of day
- timeDefnition

- how to interpret the cutover
- standardOffset

- the standard offset in force at the cutover, not null
- offsetBefore

- the offset before the cutover, not null
- offsetAfter

- the offset after the cutover, not null

**Returns:**
- the rule, not null

**Throws:**
- IllegalArgumentException

- if the day of month indicator is invalid
- IllegalArgumentException

- if the end of day flag is true when the time is not midnight
- IllegalArgumentException

- if

time.getNano()

returns non-zero value

---

#### public
Month
getMonth()

Gets the month of the transition.

If the rule defines an exact date then the month is the month of that date.

If the rule defines a week where the transition might occur, then the month
if the month of either the earliest or latest possible date of the cutover.

**Returns:**
- the month of the transition, not null

---

#### public int getDayOfMonthIndicator()

Gets the indicator of the day-of-month of the transition.

If the rule defines an exact date then the day is the month of that date.

If the rule defines a week where the transition might occur, then the day
defines either the start of the end of the transition week.

If the value is positive, then it represents a normal day-of-month, and is the
earliest possible date that the transition can be.
The date may refer to 29th February which should be treated as 1st March in non-leap years.

If the value is negative, then it represents the number of days back from the
end of the month where

-1

is the last day of the month.
In this case, the day identified is the latest possible date that the transition can be.

**Returns:**
- the day-of-month indicator, from -28 to 31 excluding 0

---

#### public
DayOfWeek
getDayOfWeek()

Gets the day-of-week of the transition.

If the rule defines an exact date then this returns null.

If the rule defines a week where the cutover might occur, then this method
returns the day-of-week that the month-day will be adjusted to.
If the day is positive then the adjustment is later.
If the day is negative then the adjustment is earlier.

**Returns:**
- the day-of-week that the transition occurs, null if the rule defines an exact date

---

#### public
LocalTime
getLocalTime()

Gets the local time of day of the transition which must be checked with

isMidnightEndOfDay()

.

The time is converted into an instant using the time definition.

**Returns:**
- the local time of day of the transition, not null

---

#### public boolean isMidnightEndOfDay()

Is the transition local time midnight at the end of day.

The transition may be represented as occurring at 24:00.

**Returns:**
- whether a local time of midnight is at the start or end of the day

---

#### public
ZoneOffsetTransitionRule.TimeDefinition
getTimeDefinition()

Gets the time definition, specifying how to convert the time to an instant.

The local time can be converted to an instant using the standard offset,
the wall offset or UTC.

**Returns:**
- the time definition, not null

---

#### public
ZoneOffset
getStandardOffset()

Gets the standard offset in force at the transition.

**Returns:**
- the standard offset, not null

---

#### public
ZoneOffset
getOffsetBefore()

Gets the offset before the transition.

**Returns:**
- the offset before, not null

---

#### public
ZoneOffset
getOffsetAfter()

Gets the offset after the transition.

**Returns:**
- the offset after, not null

---

#### public
ZoneOffsetTransition
createTransition​(int year)

Creates a transition instance for the specified year.

Calculations are performed using the ISO-8601 chronology.

**Parameters:**
- year

- the year to create a transition for, not null

**Returns:**
- the transition instance, not null

---

#### public boolean equals​(
Object
otherRule)

Checks if this object equals another.

The entire state of the object is compared.

**Overrides:**
- equals

in class

Object

**Parameters:**
- otherRule

- the other object to compare to, null returns false

**Returns:**
- true if equal

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a suitable hash code.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string describing this object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string for debugging, not null

---

### Additional Sections

#### Class ZoneOffsetTransitionRule

java.lang.Object

- java.time.zone.ZoneOffsetTransitionRule

java.time.zone.ZoneOffsetTransitionRule

**All Implemented Interfaces:** Serializable

```java
public final class
ZoneOffsetTransitionRule

extends
Object

implements
Serializable
```

A rule expressing how to create a transition.

This class allows rules for identifying future transitions to be expressed.
A rule might be written in many forms:

- the 16th March

the Sunday on or after the 16th March

the Sunday on or before the 16th March

the last Sunday in February

These different rule types can be expressed and queried.

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8
**See Also:** Serialized Form

public final class

ZoneOffsetTransitionRule

extends

Object

implements

Serializable

A rule expressing how to create a transition.

This class allows rules for identifying future transitions to be expressed.
A rule might be written in many forms:

- the 16th March

the Sunday on or after the 16th March

the Sunday on or before the 16th March

the last Sunday in February

These different rule types can be expressed and queried.

This class allows rules for identifying future transitions to be expressed.
A rule might be written in many forms:

- the 16th March

the Sunday on or after the 16th March

the Sunday on or before the 16th March

the last Sunday in February

These different rule types can be expressed and queried.

the 16th March

the Sunday on or after the 16th March

the Sunday on or before the 16th March

the last Sunday in February

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ZoneOffsetTransitionRule.TimeDefinition

A definition of the way a local time can be converted to the actual
transition date-time.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ZoneOffsetTransition

createTransition

​(int year)

Creates a transition instance for the specified year.

boolean

equals

​(

Object

otherRule)

Checks if this object equals another.

int

getDayOfMonthIndicator

()

Gets the indicator of the day-of-month of the transition.

DayOfWeek

getDayOfWeek

()

Gets the day-of-week of the transition.

LocalTime

getLocalTime

()

Gets the local time of day of the transition which must be checked with

isMidnightEndOfDay()

.

Month

getMonth

()

Gets the month of the transition.

ZoneOffset

getOffsetAfter

()

Gets the offset after the transition.

ZoneOffset

getOffsetBefore

()

Gets the offset before the transition.

ZoneOffset

getStandardOffset

()

Gets the standard offset in force at the transition.

ZoneOffsetTransitionRule.TimeDefinition

getTimeDefinition

()

Gets the time definition, specifying how to convert the time to an instant.

int

hashCode

()

Returns a suitable hash code.

boolean

isMidnightEndOfDay

()

Is the transition local time midnight at the end of day.

static

ZoneOffsetTransitionRule

of

​(

Month

month,
int dayOfMonthIndicator,

DayOfWeek

dayOfWeek,

LocalTime

time,
boolean timeEndOfDay,

ZoneOffsetTransitionRule.TimeDefinition

timeDefnition,

ZoneOffset

standardOffset,

ZoneOffset

offsetBefore,

ZoneOffset

offsetAfter)

Obtains an instance defining the yearly rule to create transitions between two offsets.

String

toString

()

Returns a string describing this object.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ZoneOffsetTransitionRule.TimeDefinition

A definition of the way a local time can be converted to the actual
transition date-time.

---

#### Nested Class Summary

A definition of the way a local time can be converted to the actual
transition date-time.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ZoneOffsetTransition

createTransition

​(int year)

Creates a transition instance for the specified year.

boolean

equals

​(

Object

otherRule)

Checks if this object equals another.

int

getDayOfMonthIndicator

()

Gets the indicator of the day-of-month of the transition.

DayOfWeek

getDayOfWeek

()

Gets the day-of-week of the transition.

LocalTime

getLocalTime

()

Gets the local time of day of the transition which must be checked with

isMidnightEndOfDay()

.

Month

getMonth

()

Gets the month of the transition.

ZoneOffset

getOffsetAfter

()

Gets the offset after the transition.

ZoneOffset

getOffsetBefore

()

Gets the offset before the transition.

ZoneOffset

getStandardOffset

()

Gets the standard offset in force at the transition.

ZoneOffsetTransitionRule.TimeDefinition

getTimeDefinition

()

Gets the time definition, specifying how to convert the time to an instant.

int

hashCode

()

Returns a suitable hash code.

boolean

isMidnightEndOfDay

()

Is the transition local time midnight at the end of day.

static

ZoneOffsetTransitionRule

of

​(

Month

month,
int dayOfMonthIndicator,

DayOfWeek

dayOfWeek,

LocalTime

time,
boolean timeEndOfDay,

ZoneOffsetTransitionRule.TimeDefinition

timeDefnition,

ZoneOffset

standardOffset,

ZoneOffset

offsetBefore,

ZoneOffset

offsetAfter)

Obtains an instance defining the yearly rule to create transitions between two offsets.

String

toString

()

Returns a string describing this object.

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

Creates a transition instance for the specified year.

Checks if this object equals another.

Gets the indicator of the day-of-month of the transition.

Gets the day-of-week of the transition.

Gets the local time of day of the transition which must be checked with

isMidnightEndOfDay()

.

Gets the month of the transition.

Gets the offset after the transition.

Gets the offset before the transition.

Gets the standard offset in force at the transition.

Gets the time definition, specifying how to convert the time to an instant.

Returns a suitable hash code.

Is the transition local time midnight at the end of day.

Obtains an instance defining the yearly rule to create transitions between two offsets.

Returns a string describing this object.

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

============ METHOD DETAIL ==========

- Method Detail

- of

```java
public static
ZoneOffsetTransitionRule
of​(
Month
month,
int dayOfMonthIndicator,

DayOfWeek
dayOfWeek,

LocalTime
time,
boolean timeEndOfDay,

ZoneOffsetTransitionRule.TimeDefinition
timeDefnition,

ZoneOffset
standardOffset,

ZoneOffset
offsetBefore,

ZoneOffset
offsetAfter)
```

Obtains an instance defining the yearly rule to create transitions between two offsets.

Applications should normally obtain an instance from

ZoneRules

.
This factory is only intended for use when creating

ZoneRules

.

**Parameters:** month

- the month of the month-day of the first day of the cutover week, not null
**Parameters:** dayOfMonthIndicator

- the day of the month-day of the cutover week, positive if the week is that
day or later, negative if the week is that day or earlier, counting from the last day of the month,
from -28 to 31 excluding 0
**Parameters:** dayOfWeek

- the required day-of-week, null if the month-day should not be changed
**Parameters:** time

- the cutover time in the 'before' offset, not null
**Parameters:** timeEndOfDay

- whether the time is midnight at the end of day
**Parameters:** timeDefnition

- how to interpret the cutover
**Parameters:** standardOffset

- the standard offset in force at the cutover, not null
**Parameters:** offsetBefore

- the offset before the cutover, not null
**Parameters:** offsetAfter

- the offset after the cutover, not null
**Returns:** the rule, not null
**Throws:** IllegalArgumentException

- if the day of month indicator is invalid
**Throws:** IllegalArgumentException

- if the end of day flag is true when the time is not midnight
**Throws:** IllegalArgumentException

- if

time.getNano()

returns non-zero value

- getMonth

```java
public
Month
getMonth()
```

Gets the month of the transition.

If the rule defines an exact date then the month is the month of that date.

If the rule defines a week where the transition might occur, then the month
if the month of either the earliest or latest possible date of the cutover.

**Returns:** the month of the transition, not null

- getDayOfMonthIndicator

```java
public int getDayOfMonthIndicator()
```

Gets the indicator of the day-of-month of the transition.

If the rule defines an exact date then the day is the month of that date.

If the rule defines a week where the transition might occur, then the day
defines either the start of the end of the transition week.

If the value is positive, then it represents a normal day-of-month, and is the
earliest possible date that the transition can be.
The date may refer to 29th February which should be treated as 1st March in non-leap years.

If the value is negative, then it represents the number of days back from the
end of the month where

-1

is the last day of the month.
In this case, the day identified is the latest possible date that the transition can be.

**Returns:** the day-of-month indicator, from -28 to 31 excluding 0

- getDayOfWeek

```java
public
DayOfWeek
getDayOfWeek()
```

Gets the day-of-week of the transition.

If the rule defines an exact date then this returns null.

If the rule defines a week where the cutover might occur, then this method
returns the day-of-week that the month-day will be adjusted to.
If the day is positive then the adjustment is later.
If the day is negative then the adjustment is earlier.

**Returns:** the day-of-week that the transition occurs, null if the rule defines an exact date

- getLocalTime

```java
public
LocalTime
getLocalTime()
```

Gets the local time of day of the transition which must be checked with

isMidnightEndOfDay()

.

The time is converted into an instant using the time definition.

**Returns:** the local time of day of the transition, not null

- isMidnightEndOfDay

```java
public boolean isMidnightEndOfDay()
```

Is the transition local time midnight at the end of day.

The transition may be represented as occurring at 24:00.

**Returns:** whether a local time of midnight is at the start or end of the day

- getTimeDefinition

```java
public
ZoneOffsetTransitionRule.TimeDefinition
getTimeDefinition()
```

Gets the time definition, specifying how to convert the time to an instant.

The local time can be converted to an instant using the standard offset,
the wall offset or UTC.

**Returns:** the time definition, not null

- getStandardOffset

```java
public
ZoneOffset
getStandardOffset()
```

Gets the standard offset in force at the transition.

**Returns:** the standard offset, not null

- getOffsetBefore

```java
public
ZoneOffset
getOffsetBefore()
```

Gets the offset before the transition.

**Returns:** the offset before, not null

- getOffsetAfter

```java
public
ZoneOffset
getOffsetAfter()
```

Gets the offset after the transition.

**Returns:** the offset after, not null

- createTransition

```java
public
ZoneOffsetTransition
createTransition​(int year)
```

Creates a transition instance for the specified year.

Calculations are performed using the ISO-8601 chronology.

**Parameters:** year

- the year to create a transition for, not null
**Returns:** the transition instance, not null

- equals

```java
public boolean equals​(
Object
otherRule)
```

Checks if this object equals another.

The entire state of the object is compared.

**Overrides:** equals

in class

Object
**Parameters:** otherRule

- the other object to compare to, null returns false
**Returns:** true if equal
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a suitable hash code.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string describing this object.

**Overrides:** toString

in class

Object
**Returns:** a string for debugging, not null

Method Detail

- of

```java
public static
ZoneOffsetTransitionRule
of​(
Month
month,
int dayOfMonthIndicator,

DayOfWeek
dayOfWeek,

LocalTime
time,
boolean timeEndOfDay,

ZoneOffsetTransitionRule.TimeDefinition
timeDefnition,

ZoneOffset
standardOffset,

ZoneOffset
offsetBefore,

ZoneOffset
offsetAfter)
```

Obtains an instance defining the yearly rule to create transitions between two offsets.

Applications should normally obtain an instance from

ZoneRules

.
This factory is only intended for use when creating

ZoneRules

.

**Parameters:** month

- the month of the month-day of the first day of the cutover week, not null
**Parameters:** dayOfMonthIndicator

- the day of the month-day of the cutover week, positive if the week is that
day or later, negative if the week is that day or earlier, counting from the last day of the month,
from -28 to 31 excluding 0
**Parameters:** dayOfWeek

- the required day-of-week, null if the month-day should not be changed
**Parameters:** time

- the cutover time in the 'before' offset, not null
**Parameters:** timeEndOfDay

- whether the time is midnight at the end of day
**Parameters:** timeDefnition

- how to interpret the cutover
**Parameters:** standardOffset

- the standard offset in force at the cutover, not null
**Parameters:** offsetBefore

- the offset before the cutover, not null
**Parameters:** offsetAfter

- the offset after the cutover, not null
**Returns:** the rule, not null
**Throws:** IllegalArgumentException

- if the day of month indicator is invalid
**Throws:** IllegalArgumentException

- if the end of day flag is true when the time is not midnight
**Throws:** IllegalArgumentException

- if

time.getNano()

returns non-zero value

- getMonth

```java
public
Month
getMonth()
```

Gets the month of the transition.

If the rule defines an exact date then the month is the month of that date.

If the rule defines a week where the transition might occur, then the month
if the month of either the earliest or latest possible date of the cutover.

**Returns:** the month of the transition, not null

- getDayOfMonthIndicator

```java
public int getDayOfMonthIndicator()
```

Gets the indicator of the day-of-month of the transition.

If the rule defines an exact date then the day is the month of that date.

If the rule defines a week where the transition might occur, then the day
defines either the start of the end of the transition week.

If the value is positive, then it represents a normal day-of-month, and is the
earliest possible date that the transition can be.
The date may refer to 29th February which should be treated as 1st March in non-leap years.

If the value is negative, then it represents the number of days back from the
end of the month where

-1

is the last day of the month.
In this case, the day identified is the latest possible date that the transition can be.

**Returns:** the day-of-month indicator, from -28 to 31 excluding 0

- getDayOfWeek

```java
public
DayOfWeek
getDayOfWeek()
```

Gets the day-of-week of the transition.

If the rule defines an exact date then this returns null.

If the rule defines a week where the cutover might occur, then this method
returns the day-of-week that the month-day will be adjusted to.
If the day is positive then the adjustment is later.
If the day is negative then the adjustment is earlier.

**Returns:** the day-of-week that the transition occurs, null if the rule defines an exact date

- getLocalTime

```java
public
LocalTime
getLocalTime()
```

Gets the local time of day of the transition which must be checked with

isMidnightEndOfDay()

.

The time is converted into an instant using the time definition.

**Returns:** the local time of day of the transition, not null

- isMidnightEndOfDay

```java
public boolean isMidnightEndOfDay()
```

Is the transition local time midnight at the end of day.

The transition may be represented as occurring at 24:00.

**Returns:** whether a local time of midnight is at the start or end of the day

- getTimeDefinition

```java
public
ZoneOffsetTransitionRule.TimeDefinition
getTimeDefinition()
```

Gets the time definition, specifying how to convert the time to an instant.

The local time can be converted to an instant using the standard offset,
the wall offset or UTC.

**Returns:** the time definition, not null

- getStandardOffset

```java
public
ZoneOffset
getStandardOffset()
```

Gets the standard offset in force at the transition.

**Returns:** the standard offset, not null

- getOffsetBefore

```java
public
ZoneOffset
getOffsetBefore()
```

Gets the offset before the transition.

**Returns:** the offset before, not null

- getOffsetAfter

```java
public
ZoneOffset
getOffsetAfter()
```

Gets the offset after the transition.

**Returns:** the offset after, not null

- createTransition

```java
public
ZoneOffsetTransition
createTransition​(int year)
```

Creates a transition instance for the specified year.

Calculations are performed using the ISO-8601 chronology.

**Parameters:** year

- the year to create a transition for, not null
**Returns:** the transition instance, not null

- equals

```java
public boolean equals​(
Object
otherRule)
```

Checks if this object equals another.

The entire state of the object is compared.

**Overrides:** equals

in class

Object
**Parameters:** otherRule

- the other object to compare to, null returns false
**Returns:** true if equal
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a suitable hash code.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string describing this object.

**Overrides:** toString

in class

Object
**Returns:** a string for debugging, not null

---

#### Method Detail

of

```java
public static
ZoneOffsetTransitionRule
of​(
Month
month,
int dayOfMonthIndicator,

DayOfWeek
dayOfWeek,

LocalTime
time,
boolean timeEndOfDay,

ZoneOffsetTransitionRule.TimeDefinition
timeDefnition,

ZoneOffset
standardOffset,

ZoneOffset
offsetBefore,

ZoneOffset
offsetAfter)
```

Obtains an instance defining the yearly rule to create transitions between two offsets.

Applications should normally obtain an instance from

ZoneRules

.
This factory is only intended for use when creating

ZoneRules

.

**Parameters:** month

- the month of the month-day of the first day of the cutover week, not null
**Parameters:** dayOfMonthIndicator

- the day of the month-day of the cutover week, positive if the week is that
day or later, negative if the week is that day or earlier, counting from the last day of the month,
from -28 to 31 excluding 0
**Parameters:** dayOfWeek

- the required day-of-week, null if the month-day should not be changed
**Parameters:** time

- the cutover time in the 'before' offset, not null
**Parameters:** timeEndOfDay

- whether the time is midnight at the end of day
**Parameters:** timeDefnition

- how to interpret the cutover
**Parameters:** standardOffset

- the standard offset in force at the cutover, not null
**Parameters:** offsetBefore

- the offset before the cutover, not null
**Parameters:** offsetAfter

- the offset after the cutover, not null
**Returns:** the rule, not null
**Throws:** IllegalArgumentException

- if the day of month indicator is invalid
**Throws:** IllegalArgumentException

- if the end of day flag is true when the time is not midnight
**Throws:** IllegalArgumentException

- if

time.getNano()

returns non-zero value

---

#### of

public static

ZoneOffsetTransitionRule

of​(

Month

month,
int dayOfMonthIndicator,

DayOfWeek

dayOfWeek,

LocalTime

time,
boolean timeEndOfDay,

ZoneOffsetTransitionRule.TimeDefinition

timeDefnition,

ZoneOffset

standardOffset,

ZoneOffset

offsetBefore,

ZoneOffset

offsetAfter)

Obtains an instance defining the yearly rule to create transitions between two offsets.

Applications should normally obtain an instance from

ZoneRules

.
This factory is only intended for use when creating

ZoneRules

.

Applications should normally obtain an instance from

ZoneRules

.
This factory is only intended for use when creating

ZoneRules

.

getMonth

```java
public
Month
getMonth()
```

Gets the month of the transition.

If the rule defines an exact date then the month is the month of that date.

If the rule defines a week where the transition might occur, then the month
if the month of either the earliest or latest possible date of the cutover.

**Returns:** the month of the transition, not null

---

#### getMonth

public

Month

getMonth()

Gets the month of the transition.

If the rule defines an exact date then the month is the month of that date.

If the rule defines a week where the transition might occur, then the month
if the month of either the earliest or latest possible date of the cutover.

If the rule defines an exact date then the month is the month of that date.

If the rule defines a week where the transition might occur, then the month
if the month of either the earliest or latest possible date of the cutover.

If the rule defines a week where the transition might occur, then the month
if the month of either the earliest or latest possible date of the cutover.

getDayOfMonthIndicator

```java
public int getDayOfMonthIndicator()
```

Gets the indicator of the day-of-month of the transition.

If the rule defines an exact date then the day is the month of that date.

If the rule defines a week where the transition might occur, then the day
defines either the start of the end of the transition week.

If the value is positive, then it represents a normal day-of-month, and is the
earliest possible date that the transition can be.
The date may refer to 29th February which should be treated as 1st March in non-leap years.

If the value is negative, then it represents the number of days back from the
end of the month where

-1

is the last day of the month.
In this case, the day identified is the latest possible date that the transition can be.

**Returns:** the day-of-month indicator, from -28 to 31 excluding 0

---

#### getDayOfMonthIndicator

public int getDayOfMonthIndicator()

Gets the indicator of the day-of-month of the transition.

If the rule defines an exact date then the day is the month of that date.

If the rule defines a week where the transition might occur, then the day
defines either the start of the end of the transition week.

If the value is positive, then it represents a normal day-of-month, and is the
earliest possible date that the transition can be.
The date may refer to 29th February which should be treated as 1st March in non-leap years.

If the value is negative, then it represents the number of days back from the
end of the month where

-1

is the last day of the month.
In this case, the day identified is the latest possible date that the transition can be.

If the rule defines an exact date then the day is the month of that date.

If the rule defines a week where the transition might occur, then the day
defines either the start of the end of the transition week.

If the value is positive, then it represents a normal day-of-month, and is the
earliest possible date that the transition can be.
The date may refer to 29th February which should be treated as 1st March in non-leap years.

If the value is negative, then it represents the number of days back from the
end of the month where

-1

is the last day of the month.
In this case, the day identified is the latest possible date that the transition can be.

If the rule defines a week where the transition might occur, then the day
defines either the start of the end of the transition week.

If the value is positive, then it represents a normal day-of-month, and is the
earliest possible date that the transition can be.
The date may refer to 29th February which should be treated as 1st March in non-leap years.

If the value is negative, then it represents the number of days back from the
end of the month where

-1

is the last day of the month.
In this case, the day identified is the latest possible date that the transition can be.

If the value is positive, then it represents a normal day-of-month, and is the
earliest possible date that the transition can be.
The date may refer to 29th February which should be treated as 1st March in non-leap years.

If the value is negative, then it represents the number of days back from the
end of the month where

-1

is the last day of the month.
In this case, the day identified is the latest possible date that the transition can be.

If the value is negative, then it represents the number of days back from the
end of the month where

-1

is the last day of the month.
In this case, the day identified is the latest possible date that the transition can be.

getDayOfWeek

```java
public
DayOfWeek
getDayOfWeek()
```

Gets the day-of-week of the transition.

If the rule defines an exact date then this returns null.

If the rule defines a week where the cutover might occur, then this method
returns the day-of-week that the month-day will be adjusted to.
If the day is positive then the adjustment is later.
If the day is negative then the adjustment is earlier.

**Returns:** the day-of-week that the transition occurs, null if the rule defines an exact date

---

#### getDayOfWeek

public

DayOfWeek

getDayOfWeek()

Gets the day-of-week of the transition.

If the rule defines an exact date then this returns null.

If the rule defines a week where the cutover might occur, then this method
returns the day-of-week that the month-day will be adjusted to.
If the day is positive then the adjustment is later.
If the day is negative then the adjustment is earlier.

If the rule defines an exact date then this returns null.

If the rule defines a week where the cutover might occur, then this method
returns the day-of-week that the month-day will be adjusted to.
If the day is positive then the adjustment is later.
If the day is negative then the adjustment is earlier.

If the rule defines a week where the cutover might occur, then this method
returns the day-of-week that the month-day will be adjusted to.
If the day is positive then the adjustment is later.
If the day is negative then the adjustment is earlier.

getLocalTime

```java
public
LocalTime
getLocalTime()
```

Gets the local time of day of the transition which must be checked with

isMidnightEndOfDay()

.

The time is converted into an instant using the time definition.

**Returns:** the local time of day of the transition, not null

---

#### getLocalTime

public

LocalTime

getLocalTime()

Gets the local time of day of the transition which must be checked with

isMidnightEndOfDay()

.

The time is converted into an instant using the time definition.

The time is converted into an instant using the time definition.

isMidnightEndOfDay

```java
public boolean isMidnightEndOfDay()
```

Is the transition local time midnight at the end of day.

The transition may be represented as occurring at 24:00.

**Returns:** whether a local time of midnight is at the start or end of the day

---

#### isMidnightEndOfDay

public boolean isMidnightEndOfDay()

Is the transition local time midnight at the end of day.

The transition may be represented as occurring at 24:00.

The transition may be represented as occurring at 24:00.

getTimeDefinition

```java
public
ZoneOffsetTransitionRule.TimeDefinition
getTimeDefinition()
```

Gets the time definition, specifying how to convert the time to an instant.

The local time can be converted to an instant using the standard offset,
the wall offset or UTC.

**Returns:** the time definition, not null

---

#### getTimeDefinition

public

ZoneOffsetTransitionRule.TimeDefinition

getTimeDefinition()

Gets the time definition, specifying how to convert the time to an instant.

The local time can be converted to an instant using the standard offset,
the wall offset or UTC.

The local time can be converted to an instant using the standard offset,
the wall offset or UTC.

getStandardOffset

```java
public
ZoneOffset
getStandardOffset()
```

Gets the standard offset in force at the transition.

**Returns:** the standard offset, not null

---

#### getStandardOffset

public

ZoneOffset

getStandardOffset()

Gets the standard offset in force at the transition.

getOffsetBefore

```java
public
ZoneOffset
getOffsetBefore()
```

Gets the offset before the transition.

**Returns:** the offset before, not null

---

#### getOffsetBefore

public

ZoneOffset

getOffsetBefore()

Gets the offset before the transition.

getOffsetAfter

```java
public
ZoneOffset
getOffsetAfter()
```

Gets the offset after the transition.

**Returns:** the offset after, not null

---

#### getOffsetAfter

public

ZoneOffset

getOffsetAfter()

Gets the offset after the transition.

createTransition

```java
public
ZoneOffsetTransition
createTransition​(int year)
```

Creates a transition instance for the specified year.

Calculations are performed using the ISO-8601 chronology.

**Parameters:** year

- the year to create a transition for, not null
**Returns:** the transition instance, not null

---

#### createTransition

public

ZoneOffsetTransition

createTransition​(int year)

Creates a transition instance for the specified year.

Calculations are performed using the ISO-8601 chronology.

Calculations are performed using the ISO-8601 chronology.

equals

```java
public boolean equals​(
Object
otherRule)
```

Checks if this object equals another.

The entire state of the object is compared.

**Overrides:** equals

in class

Object
**Parameters:** otherRule

- the other object to compare to, null returns false
**Returns:** true if equal
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

otherRule)

Checks if this object equals another.

The entire state of the object is compared.

The entire state of the object is compared.

hashCode

```java
public int hashCode()
```

Returns a suitable hash code.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a suitable hash code.

toString

```java
public
String
toString()
```

Returns a string describing this object.

**Overrides:** toString

in class

Object
**Returns:** a string for debugging, not null

---

#### toString

public

String

toString()

Returns a string describing this object.

---

