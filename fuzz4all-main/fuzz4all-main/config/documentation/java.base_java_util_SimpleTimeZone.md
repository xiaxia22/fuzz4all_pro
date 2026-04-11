# Class SimpleTimeZone

**Source:** `java.base\java\util\SimpleTimeZone.html`

### Class Description

```java
public class
SimpleTimeZone

extends
TimeZone
```

SimpleTimeZone

is a concrete subclass of

TimeZone

that represents a time zone for use with a Gregorian calendar.
The class holds an offset from GMT, called

raw offset

, and start
and end rules for a daylight saving time schedule. Since it only holds
single values for each, it cannot handle historical changes in the offset
from GMT and the daylight saving schedule, except that the

setStartYear

method can specify the year when the daylight
saving time schedule starts in effect.

To construct a

SimpleTimeZone

with a daylight saving time
schedule, the schedule can be described with a set of rules,

start-rule

and

end-rule

. A day when daylight saving time
starts or ends is specified by a combination of

month

,

day-of-month

, and

day-of-week

values. The

month

value is represented by a Calendar

MONTH

field
value, such as

Calendar.MARCH

. The

day-of-week

value is
represented by a Calendar

DAY_OF_WEEK

value,
such as

SUNDAY

. The meanings of value combinations
are as follows.

- Exact day of month

To specify an exact day of month, set the

month

and

day-of-month

to an exact value, and

day-of-week

to zero. For
example, to specify March 1, set the

month

to

MARCH

,

day-of-month

to 1, and

day-of-week

to 0.
- Day of week on or after day of month

To specify a day of week on or after an exact day of month, set the

month

to an exact month value,

day-of-month

to the day on
or after which the rule is applied, and

day-of-week

to a negative

DAY_OF_WEEK

field value. For example, to specify the
second Sunday of April, set

month

to

APRIL

,

day-of-month

to 8, and

day-of-week

to

-

SUNDAY

.
- Day of week on or before day of month

To specify a day of the week on or before an exact day of the month, set

day-of-month

and

day-of-week

to a negative value. For
example, to specify the last Wednesday on or before the 21st of March, set

month

to

MARCH

,

day-of-month

is -21
and

day-of-week

is

-

WEDNESDAY

.
- Last day-of-week of month

To specify, the last day-of-week of the month, set

day-of-week

to a

DAY_OF_WEEK

value and

day-of-month

to
-1. For example, to specify the last Sunday of October, set

month

to

OCTOBER

,

day-of-week

to

SUNDAY

and

day-of-month

to -1.

The time of the day at which daylight saving time starts or ends is
specified by a millisecond value within the day. There are three kinds of

mode

s to specify the time:

WALL_TIME

,

STANDARD_TIME

and

UTC_TIME

. For example, if daylight
saving time ends
at 2:00 am in the wall clock time, it can be specified by 7200000
milliseconds in the

WALL_TIME

mode. In this case, the wall clock time
for an

end-rule

means the same thing as the daylight time.

The following are examples of parameters for constructing time zone objects.

```java
// Base GMT offset: -8:00
// DST starts: at 2:00am in standard time
// on the first Sunday in April
// DST ends: at 2:00am in daylight time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(-28800000,
"America/Los_Angeles",
Calendar.APRIL, 1, -Calendar.SUNDAY,
7200000,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
7200000,
3600000)

// Base GMT offset: +1:00
// DST starts: at 1:00am in UTC time
// on the last Sunday in March
// DST ends: at 1:00am in UTC time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(3600000,
"Europe/Paris",
Calendar.MARCH, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
3600000)
```

These parameter rules are also applicable to the set rule methods, such as

setStartRule

.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public static final int WALL_TIME

Constant for a mode of start or end time specified as wall clock
time. Wall clock time is standard time for the onset rule, and
daylight time for the end rule.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int STANDARD_TIME

Constant for a mode of start or end time specified as standard time.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int UTC_TIME

Constant for a mode of start or end time specified as UTC. European
Union rules are specified as UTC time, for example.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

### Constructor Details

#### public SimpleTimeZone​(int rawOffset,

String
ID)

Constructs a SimpleTimeZone with the given base time zone offset from GMT
and time zone ID with no daylight saving time schedule.

**Parameters:**
- rawOffset

- The base time zone offset in milliseconds to GMT.
- ID

- The time zone name that is given to this instance.

---

#### public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are specified to be
represented in the wall clock time. The amount of daylight saving is
assumed to be 3600000 milliseconds (i.e., one hour). This constructor is
equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
3600000)
```

**Parameters:**
- rawOffset

- The given base time zone offset from GMT.
- ID

- The time zone ID which is given to this object.
- startMonth

- The daylight saving time starting month. Month is
a

MONTH

field value (0-based. e.g., 0
for January).
- startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
- startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
- startTime

- The daylight saving time starting time in local wall clock
time (in milliseconds within the day), which is local
standard time in this case.
- endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
- endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
- endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
- endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.

**Throws:**
- IllegalArgumentException

- if the month, day, dayOfWeek, or time
parameters are out of range for the start or end rule

---

#### public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int dstSavings)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are assumed to be
represented in the wall clock time. This constructor is equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
dstSavings)
```

**Parameters:**
- rawOffset

- The given base time zone offset from GMT.
- ID

- The time zone ID which is given to this object.
- startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
- startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
- startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
- startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
- endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
- endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
- endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
- endTime

- The daylight saving ending time in local wall clock time,
which is local daylight time in this case.
- dstSavings

- The amount of time in milliseconds saved during
daylight saving time.

**Throws:**
- IllegalArgumentException

- if the month, day, dayOfWeek, or time
parameters are out of range for the start or end rule

**Since:**
- 1.2

---

#### public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int startTimeMode,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int endTimeMode,
int dstSavings)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
This constructor takes the full set of the start and end rules
parameters, including modes of

startTime

and

endTime

. The mode specifies either

wall
time

or

standard time

or

UTC
time

.

**Parameters:**
- rawOffset

- The given base time zone offset from GMT.
- ID

- The time zone ID which is given to this object.
- startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
- startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
- startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
- startTime

- The daylight saving time starting time in the time mode
specified by

startTimeMode

.
- startTimeMode

- The mode of the start time specified by startTime.
- endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
- endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
- endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
- endTime

- The daylight saving ending time in time time mode
specified by

endTimeMode

.
- endTimeMode

- The mode of the end time specified by endTime
- dstSavings

- The amount of time in milliseconds saved during
daylight saving time.

**Throws:**
- IllegalArgumentException

- if the month, day, dayOfWeek, time more, or
time parameters are out of range for the start or end rule, or if a time mode
value is invalid.

**See Also:**
- WALL_TIME

,

STANDARD_TIME

,

UTC_TIME

**Since:**
- 1.4

---

### Method Details

#### public void setStartYear​(int year)

Sets the daylight saving time starting year.

**Parameters:**
- year

- The daylight saving starting year.

---

#### public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime)

Sets the daylight saving time start rule. For example, if daylight saving
time starts on the first Sunday in April at 2 am in local wall clock
time, you can set the start rule by calling:

```java
setStartRule(Calendar.APRIL, 1, Calendar.SUNDAY, 2*60*60*1000);
```

**Parameters:**
- startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
- startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
- startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
- startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.

**Throws:**
- IllegalArgumentException

- if the

startMonth

,

startDay

,

startDayOfWeek

, or

startTime

parameters are out of range

---

#### public void setStartRule​(int startMonth,
int startDay,
int startTime)

Sets the daylight saving time start rule to a fixed date within a month.
This method is equivalent to:

```java
setStartRule(startMonth, startDay, 0, startTime)
```

**Parameters:**
- startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
- startDay

- The day of the month on which the daylight saving time starts.
- startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
See the class description for the special cases of this parameter.

**Throws:**
- IllegalArgumentException

- if the

startMonth

,

startDayOfMonth

, or

startTime

parameters are out of range

**Since:**
- 1.2

---

#### public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
boolean after)

Sets the daylight saving time start rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

**Parameters:**
- startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
- startDay

- The day of the month on which the daylight saving time starts.
- startDayOfWeek

- The daylight saving time starting day-of-week.
- startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
- after

- If true, this rule selects the first

dayOfWeek

on or

after

dayOfMonth

. If false, this rule
selects the last

dayOfWeek

on or

before

dayOfMonth

.

**Throws:**
- IllegalArgumentException

- if the

startMonth

,

startDay

,

startDayOfWeek

, or

startTime

parameters are out of range

**Since:**
- 1.2

---

#### public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime)

Sets the daylight saving time end rule. For example, if daylight saving time
ends on the last Sunday in October at 2 am in wall clock time,
you can set the end rule by calling:

setEndRule(Calendar.OCTOBER, -1, Calendar.SUNDAY, 2*60*60*1000);

**Parameters:**
- endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
- endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
- endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
- endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.

**Throws:**
- IllegalArgumentException

- if the

endMonth

,

endDay

,

endDayOfWeek

, or

endTime

parameters are out of range

---

#### public void setEndRule​(int endMonth,
int endDay,
int endTime)

Sets the daylight saving time end rule to a fixed date within a month.
This method is equivalent to:

```java
setEndRule(endMonth, endDay, 0, endTime)
```

**Parameters:**
- endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
- endDay

- The day of the month on which the daylight saving time ends.
- endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.

**Throws:**
- IllegalArgumentException

- the

endMonth

,

endDay

,
or

endTime

parameters are out of range

**Since:**
- 1.2

---

#### public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
boolean after)

Sets the daylight saving time end rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

**Parameters:**
- endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
- endDay

- The day of the month on which the daylight saving time ends.
- endDayOfWeek

- The daylight saving time ending day-of-week.
- endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
- after

- If true, this rule selects the first

endDayOfWeek

on
or

after

endDay

. If false, this rule
selects the last

endDayOfWeek

on or before

endDay

of the month.

**Throws:**
- IllegalArgumentException

- the

endMonth

,

endDay

,

endDayOfWeek

, or

endTime

parameters are out of range

**Since:**
- 1.2

---

#### public int getOffset​(long date)

Returns the offset of this time zone from UTC at the given
time. If daylight saving time is in effect at the given time,
the offset value is adjusted with the amount of daylight
saving.

**Overrides:**
- getOffset

in class

TimeZone

**Parameters:**
- date

- the time at which the time zone offset is found

**Returns:**
- the amount of time in milliseconds to add to UTC to get
local time.

**See Also:**
- Calendar.ZONE_OFFSET

,

Calendar.DST_OFFSET

**Since:**
- 1.4

---

#### public int getOffset​(int era,
int year,
int month,
int day,
int dayOfWeek,
int millis)

Returns the difference in milliseconds between local time and
UTC, taking into account both the raw offset and the effect of
daylight saving, for the specified date and time. This method
assumes that the start and end month are distinct. It also
uses a default

GregorianCalendar

object as its
underlying calendar, such as for determining leap years. Do
not use the result of this method with a calendar other than a
default

GregorianCalendar

.

Note: In general, clients should use

Calendar.get(ZONE_OFFSET) + Calendar.get(DST_OFFSET)

instead of calling this method.

**Specified by:**
- getOffset

in class

TimeZone

**Parameters:**
- era

- The era of the given date.
- year

- The year in the given date.
- month

- The month in the given date. Month is 0-based. e.g.,
0 for January.
- day

- The day-in-month of the given date.
- dayOfWeek

- The day-of-week of the given date.
- millis

- The milliseconds in day in

standard

local time.

**Returns:**
- The milliseconds to add to UTC to get local time.

**Throws:**
- IllegalArgumentException

- the

era

,

month

,

day

,

dayOfWeek

,
or

millis

parameters are out of range

**See Also:**
- Calendar.ZONE_OFFSET

,

Calendar.DST_OFFSET

---

#### public int getRawOffset()

Gets the GMT offset for this time zone.

**Specified by:**
- getRawOffset

in class

TimeZone

**Returns:**
- the GMT offset value in milliseconds

**See Also:**
- setRawOffset(int)

---

#### public void setRawOffset​(int offsetMillis)

Sets the base time zone offset to GMT.
This is the offset to add to UTC to get local time.

**Specified by:**
- setRawOffset

in class

TimeZone

**Parameters:**
- offsetMillis

- the given base time zone offset to GMT.

**See Also:**
- getRawOffset()

---

#### public void setDSTSavings​(int millisSavedDuringDST)

Sets the amount of time in milliseconds that the clock is advanced
during daylight saving time.

**Parameters:**
- millisSavedDuringDST

- the number of milliseconds the time is
advanced with respect to standard time when the daylight saving time rules
are in effect. A positive number, typically one hour (3600000).

**See Also:**
- getDSTSavings()

**Since:**
- 1.2

---

#### public int getDSTSavings()

Returns the amount of time in milliseconds that the clock is
advanced during daylight saving time.

**Overrides:**
- getDSTSavings

in class

TimeZone

**Returns:**
- the number of milliseconds the time is advanced with
respect to standard time when the daylight saving rules are in
effect, or 0 (zero) if this time zone doesn't observe daylight
saving time.

**See Also:**
- setDSTSavings(int)

**Since:**
- 1.2

---

#### public boolean useDaylightTime()

Queries if this time zone uses daylight saving time.

**Specified by:**
- useDaylightTime

in class

TimeZone

**Returns:**
- true if this time zone uses daylight saving time;
false otherwise.

**See Also:**
- TimeZone.inDaylightTime(Date)

,

Calendar.DST_OFFSET

---

#### public boolean observesDaylightTime()

Returns

true

if this

SimpleTimeZone

observes
Daylight Saving Time. This method is equivalent to

useDaylightTime()

.

**Overrides:**
- observesDaylightTime

in class

TimeZone

**Returns:**
- true

if this

SimpleTimeZone

observes
Daylight Saving Time;

false

otherwise.

**See Also:**
- TimeZone.useDaylightTime()

,

TimeZone.inDaylightTime(Date)

,

Calendar.DST_OFFSET

**Since:**
- 1.7

---

#### public boolean inDaylightTime​(
Date
date)

Queries if the given date is in daylight saving time.

**Specified by:**
- inDaylightTime

in class

TimeZone

**Parameters:**
- date

- the given Date.

**Returns:**
- true if daylight saving time is in effective at the
given date; false otherwise.

---

#### public
Object
clone()

Returns a clone of this

SimpleTimeZone

instance.

**Overrides:**
- clone

in class

TimeZone

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

#### public int hashCode()

Generates the hash code for the SimpleDateFormat object.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code for this object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Compares the equality of two

SimpleTimeZone

objects.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The

SimpleTimeZone

object to be compared with.

**Returns:**
- True if the given

obj

is the same as this

SimpleTimeZone

object; false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public boolean hasSameRules​(
TimeZone
other)

Returns

true

if this zone has the same rules and offset as another zone.

**Overrides:**
- hasSameRules

in class

TimeZone

**Parameters:**
- other

- the TimeZone object to be compared with

**Returns:**
- true

if the given zone is a SimpleTimeZone and has the
same rules and offset as this one

**Since:**
- 1.2

---

#### public
String
toString()

Returns a string representation of this time zone.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this time zone.

---

### Additional Sections

#### Class SimpleTimeZone

java.lang.Object

- java.util.TimeZone
- - java.util.SimpleTimeZone

java.util.TimeZone

- java.util.SimpleTimeZone

java.util.SimpleTimeZone

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
SimpleTimeZone

extends
TimeZone
```

SimpleTimeZone

is a concrete subclass of

TimeZone

that represents a time zone for use with a Gregorian calendar.
The class holds an offset from GMT, called

raw offset

, and start
and end rules for a daylight saving time schedule. Since it only holds
single values for each, it cannot handle historical changes in the offset
from GMT and the daylight saving schedule, except that the

setStartYear

method can specify the year when the daylight
saving time schedule starts in effect.

To construct a

SimpleTimeZone

with a daylight saving time
schedule, the schedule can be described with a set of rules,

start-rule

and

end-rule

. A day when daylight saving time
starts or ends is specified by a combination of

month

,

day-of-month

, and

day-of-week

values. The

month

value is represented by a Calendar

MONTH

field
value, such as

Calendar.MARCH

. The

day-of-week

value is
represented by a Calendar

DAY_OF_WEEK

value,
such as

SUNDAY

. The meanings of value combinations
are as follows.

- Exact day of month

To specify an exact day of month, set the

month

and

day-of-month

to an exact value, and

day-of-week

to zero. For
example, to specify March 1, set the

month

to

MARCH

,

day-of-month

to 1, and

day-of-week

to 0.
- Day of week on or after day of month

To specify a day of week on or after an exact day of month, set the

month

to an exact month value,

day-of-month

to the day on
or after which the rule is applied, and

day-of-week

to a negative

DAY_OF_WEEK

field value. For example, to specify the
second Sunday of April, set

month

to

APRIL

,

day-of-month

to 8, and

day-of-week

to

-

SUNDAY

.
- Day of week on or before day of month

To specify a day of the week on or before an exact day of the month, set

day-of-month

and

day-of-week

to a negative value. For
example, to specify the last Wednesday on or before the 21st of March, set

month

to

MARCH

,

day-of-month

is -21
and

day-of-week

is

-

WEDNESDAY

.
- Last day-of-week of month

To specify, the last day-of-week of the month, set

day-of-week

to a

DAY_OF_WEEK

value and

day-of-month

to
-1. For example, to specify the last Sunday of October, set

month

to

OCTOBER

,

day-of-week

to

SUNDAY

and

day-of-month

to -1.

The time of the day at which daylight saving time starts or ends is
specified by a millisecond value within the day. There are three kinds of

mode

s to specify the time:

WALL_TIME

,

STANDARD_TIME

and

UTC_TIME

. For example, if daylight
saving time ends
at 2:00 am in the wall clock time, it can be specified by 7200000
milliseconds in the

WALL_TIME

mode. In this case, the wall clock time
for an

end-rule

means the same thing as the daylight time.

The following are examples of parameters for constructing time zone objects.

```java
// Base GMT offset: -8:00
// DST starts: at 2:00am in standard time
// on the first Sunday in April
// DST ends: at 2:00am in daylight time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(-28800000,
"America/Los_Angeles",
Calendar.APRIL, 1, -Calendar.SUNDAY,
7200000,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
7200000,
3600000)

// Base GMT offset: +1:00
// DST starts: at 1:00am in UTC time
// on the last Sunday in March
// DST ends: at 1:00am in UTC time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(3600000,
"Europe/Paris",
Calendar.MARCH, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
3600000)
```

These parameter rules are also applicable to the set rule methods, such as

setStartRule

.

**Since:** 1.1
**See Also:** Calendar

,

GregorianCalendar

,

TimeZone

,

Serialized Form

public class

SimpleTimeZone

extends

TimeZone

SimpleTimeZone

is a concrete subclass of

TimeZone

that represents a time zone for use with a Gregorian calendar.
The class holds an offset from GMT, called

raw offset

, and start
and end rules for a daylight saving time schedule. Since it only holds
single values for each, it cannot handle historical changes in the offset
from GMT and the daylight saving schedule, except that the

setStartYear

method can specify the year when the daylight
saving time schedule starts in effect.

To construct a

SimpleTimeZone

with a daylight saving time
schedule, the schedule can be described with a set of rules,

start-rule

and

end-rule

. A day when daylight saving time
starts or ends is specified by a combination of

month

,

day-of-month

, and

day-of-week

values. The

month

value is represented by a Calendar

MONTH

field
value, such as

Calendar.MARCH

. The

day-of-week

value is
represented by a Calendar

DAY_OF_WEEK

value,
such as

SUNDAY

. The meanings of value combinations
are as follows.

- Exact day of month

To specify an exact day of month, set the

month

and

day-of-month

to an exact value, and

day-of-week

to zero. For
example, to specify March 1, set the

month

to

MARCH

,

day-of-month

to 1, and

day-of-week

to 0.
- Day of week on or after day of month

To specify a day of week on or after an exact day of month, set the

month

to an exact month value,

day-of-month

to the day on
or after which the rule is applied, and

day-of-week

to a negative

DAY_OF_WEEK

field value. For example, to specify the
second Sunday of April, set

month

to

APRIL

,

day-of-month

to 8, and

day-of-week

to

-

SUNDAY

.
- Day of week on or before day of month

To specify a day of the week on or before an exact day of the month, set

day-of-month

and

day-of-week

to a negative value. For
example, to specify the last Wednesday on or before the 21st of March, set

month

to

MARCH

,

day-of-month

is -21
and

day-of-week

is

-

WEDNESDAY

.
- Last day-of-week of month

To specify, the last day-of-week of the month, set

day-of-week

to a

DAY_OF_WEEK

value and

day-of-month

to
-1. For example, to specify the last Sunday of October, set

month

to

OCTOBER

,

day-of-week

to

SUNDAY

and

day-of-month

to -1.

The time of the day at which daylight saving time starts or ends is
specified by a millisecond value within the day. There are three kinds of

mode

s to specify the time:

WALL_TIME

,

STANDARD_TIME

and

UTC_TIME

. For example, if daylight
saving time ends
at 2:00 am in the wall clock time, it can be specified by 7200000
milliseconds in the

WALL_TIME

mode. In this case, the wall clock time
for an

end-rule

means the same thing as the daylight time.

The following are examples of parameters for constructing time zone objects.

```java
// Base GMT offset: -8:00
// DST starts: at 2:00am in standard time
// on the first Sunday in April
// DST ends: at 2:00am in daylight time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(-28800000,
"America/Los_Angeles",
Calendar.APRIL, 1, -Calendar.SUNDAY,
7200000,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
7200000,
3600000)

// Base GMT offset: +1:00
// DST starts: at 1:00am in UTC time
// on the last Sunday in March
// DST ends: at 1:00am in UTC time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(3600000,
"Europe/Paris",
Calendar.MARCH, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
3600000)
```

These parameter rules are also applicable to the set rule methods, such as

setStartRule

.

To construct a

SimpleTimeZone

with a daylight saving time
schedule, the schedule can be described with a set of rules,

start-rule

and

end-rule

. A day when daylight saving time
starts or ends is specified by a combination of

month

,

day-of-month

, and

day-of-week

values. The

month

value is represented by a Calendar

MONTH

field
value, such as

Calendar.MARCH

. The

day-of-week

value is
represented by a Calendar

DAY_OF_WEEK

value,
such as

SUNDAY

. The meanings of value combinations
are as follows.

- Exact day of month

To specify an exact day of month, set the

month

and

day-of-month

to an exact value, and

day-of-week

to zero. For
example, to specify March 1, set the

month

to

MARCH

,

day-of-month

to 1, and

day-of-week

to 0.
- Day of week on or after day of month

To specify a day of week on or after an exact day of month, set the

month

to an exact month value,

day-of-month

to the day on
or after which the rule is applied, and

day-of-week

to a negative

DAY_OF_WEEK

field value. For example, to specify the
second Sunday of April, set

month

to

APRIL

,

day-of-month

to 8, and

day-of-week

to

-

SUNDAY

.
- Day of week on or before day of month

To specify a day of the week on or before an exact day of the month, set

day-of-month

and

day-of-week

to a negative value. For
example, to specify the last Wednesday on or before the 21st of March, set

month

to

MARCH

,

day-of-month

is -21
and

day-of-week

is

-

WEDNESDAY

.
- Last day-of-week of month

To specify, the last day-of-week of the month, set

day-of-week

to a

DAY_OF_WEEK

value and

day-of-month

to
-1. For example, to specify the last Sunday of October, set

month

to

OCTOBER

,

day-of-week

to

SUNDAY

and

day-of-month

to -1.

The time of the day at which daylight saving time starts or ends is
specified by a millisecond value within the day. There are three kinds of

mode

s to specify the time:

WALL_TIME

,

STANDARD_TIME

and

UTC_TIME

. For example, if daylight
saving time ends
at 2:00 am in the wall clock time, it can be specified by 7200000
milliseconds in the

WALL_TIME

mode. In this case, the wall clock time
for an

end-rule

means the same thing as the daylight time.

The following are examples of parameters for constructing time zone objects.

```java
// Base GMT offset: -8:00
// DST starts: at 2:00am in standard time
// on the first Sunday in April
// DST ends: at 2:00am in daylight time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(-28800000,
"America/Los_Angeles",
Calendar.APRIL, 1, -Calendar.SUNDAY,
7200000,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
7200000,
3600000)

// Base GMT offset: +1:00
// DST starts: at 1:00am in UTC time
// on the last Sunday in March
// DST ends: at 1:00am in UTC time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(3600000,
"Europe/Paris",
Calendar.MARCH, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
3600000)
```

These parameter rules are also applicable to the set rule methods, such as

setStartRule

.

Exact day of month

To specify an exact day of month, set the

month

and

day-of-month

to an exact value, and

day-of-week

to zero. For
example, to specify March 1, set the

month

to

MARCH

,

day-of-month

to 1, and

day-of-week

to 0.

Day of week on or after day of month

To specify a day of week on or after an exact day of month, set the

month

to an exact month value,

day-of-month

to the day on
or after which the rule is applied, and

day-of-week

to a negative

DAY_OF_WEEK

field value. For example, to specify the
second Sunday of April, set

month

to

APRIL

,

day-of-month

to 8, and

day-of-week

to

-

SUNDAY

.

Day of week on or before day of month

To specify a day of the week on or before an exact day of the month, set

day-of-month

and

day-of-week

to a negative value. For
example, to specify the last Wednesday on or before the 21st of March, set

month

to

MARCH

,

day-of-month

is -21
and

day-of-week

is

-

WEDNESDAY

.

Last day-of-week of month

To specify, the last day-of-week of the month, set

day-of-week

to a

DAY_OF_WEEK

value and

day-of-month

to
-1. For example, to specify the last Sunday of October, set

month

to

OCTOBER

,

day-of-week

to

SUNDAY

and

day-of-month

to -1.

The following are examples of parameters for constructing time zone objects.

```java
// Base GMT offset: -8:00
// DST starts: at 2:00am in standard time
// on the first Sunday in April
// DST ends: at 2:00am in daylight time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(-28800000,
"America/Los_Angeles",
Calendar.APRIL, 1, -Calendar.SUNDAY,
7200000,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
7200000,
3600000)

// Base GMT offset: +1:00
// DST starts: at 1:00am in UTC time
// on the last Sunday in March
// DST ends: at 1:00am in UTC time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(3600000,
"Europe/Paris",
Calendar.MARCH, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
3600000)
```

These parameter rules are also applicable to the set rule methods, such as

setStartRule

.

// Base GMT offset: -8:00
// DST starts: at 2:00am in standard time
// on the first Sunday in April
// DST ends: at 2:00am in daylight time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(-28800000,
"America/Los_Angeles",
Calendar.APRIL, 1, -Calendar.SUNDAY,
7200000,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
7200000,
3600000)

// Base GMT offset: +1:00
// DST starts: at 1:00am in UTC time
// on the last Sunday in March
// DST ends: at 1:00am in UTC time
// on the last Sunday in October
// Save: 1 hour
SimpleTimeZone(3600000,
"Europe/Paris",
Calendar.MARCH, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
Calendar.OCTOBER, -1, Calendar.SUNDAY,
3600000, SimpleTimeZone.UTC_TIME,
3600000)

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

STANDARD_TIME

Constant for a mode of start or end time specified as standard time.

static int

UTC_TIME

Constant for a mode of start or end time specified as UTC.

static int

WALL_TIME

Constant for a mode of start or end time specified as wall clock
time.

- Fields declared in class java.util.

TimeZone

LONG

,

SHORT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleTimeZone

​(int rawOffset,

String

ID)

Constructs a SimpleTimeZone with the given base time zone offset from GMT
and time zone ID with no daylight saving time schedule.

SimpleTimeZone

​(int rawOffset,

String

ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.

SimpleTimeZone

​(int rawOffset,

String

ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int dstSavings)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.

SimpleTimeZone

​(int rawOffset,

String

ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int startTimeMode,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int endTimeMode,
int dstSavings)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this

SimpleTimeZone

instance.

boolean

equals

​(

Object

obj)

Compares the equality of two

SimpleTimeZone

objects.

int

getDSTSavings

()

Returns the amount of time in milliseconds that the clock is
advanced during daylight saving time.

int

getOffset

​(int era,
int year,
int month,
int day,
int dayOfWeek,
int millis)

Returns the difference in milliseconds between local time and
UTC, taking into account both the raw offset and the effect of
daylight saving, for the specified date and time.

int

getOffset

​(long date)

Returns the offset of this time zone from UTC at the given
time.

int

getRawOffset

()

Gets the GMT offset for this time zone.

int

hashCode

()

Generates the hash code for the SimpleDateFormat object.

boolean

hasSameRules

​(

TimeZone

other)

Returns

true

if this zone has the same rules and offset as another zone.

boolean

inDaylightTime

​(

Date

date)

Queries if the given date is in daylight saving time.

boolean

observesDaylightTime

()

Returns

true

if this

SimpleTimeZone

observes
Daylight Saving Time.

void

setDSTSavings

​(int millisSavedDuringDST)

Sets the amount of time in milliseconds that the clock is advanced
during daylight saving time.

void

setEndRule

​(int endMonth,
int endDay,
int endTime)

Sets the daylight saving time end rule to a fixed date within a month.

void

setEndRule

​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime)

Sets the daylight saving time end rule.

void

setEndRule

​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
boolean after)

Sets the daylight saving time end rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

void

setRawOffset

​(int offsetMillis)

Sets the base time zone offset to GMT.

void

setStartRule

​(int startMonth,
int startDay,
int startTime)

Sets the daylight saving time start rule to a fixed date within a month.

void

setStartRule

​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime)

Sets the daylight saving time start rule.

void

setStartRule

​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
boolean after)

Sets the daylight saving time start rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

void

setStartYear

​(int year)

Sets the daylight saving time starting year.

String

toString

()

Returns a string representation of this time zone.

boolean

useDaylightTime

()

Queries if this time zone uses daylight saving time.

- Methods declared in class java.util.

TimeZone

getAvailableIDs

,

getAvailableIDs

,

getDefault

,

getDisplayName

,

getDisplayName

,

getDisplayName

,

getDisplayName

,

getID

,

getTimeZone

,

getTimeZone

,

setDefault

,

setID

,

toZoneId

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

STANDARD_TIME

Constant for a mode of start or end time specified as standard time.

static int

UTC_TIME

Constant for a mode of start or end time specified as UTC.

static int

WALL_TIME

Constant for a mode of start or end time specified as wall clock
time.

- Fields declared in class java.util.

TimeZone

LONG

,

SHORT

---

#### Field Summary

Constant for a mode of start or end time specified as standard time.

Constant for a mode of start or end time specified as UTC.

Constant for a mode of start or end time specified as wall clock
time.

Fields declared in class java.util.

TimeZone

LONG

,

SHORT

---

#### Fields declared in class java.util. TimeZone

Constructor Summary

Constructors

Constructor

Description

SimpleTimeZone

​(int rawOffset,

String

ID)

Constructs a SimpleTimeZone with the given base time zone offset from GMT
and time zone ID with no daylight saving time schedule.

SimpleTimeZone

​(int rawOffset,

String

ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.

SimpleTimeZone

​(int rawOffset,

String

ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int dstSavings)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.

SimpleTimeZone

​(int rawOffset,

String

ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int startTimeMode,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int endTimeMode,
int dstSavings)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.

---

#### Constructor Summary

Constructs a SimpleTimeZone with the given base time zone offset from GMT
and time zone ID with no daylight saving time schedule.

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this

SimpleTimeZone

instance.

boolean

equals

​(

Object

obj)

Compares the equality of two

SimpleTimeZone

objects.

int

getDSTSavings

()

Returns the amount of time in milliseconds that the clock is
advanced during daylight saving time.

int

getOffset

​(int era,
int year,
int month,
int day,
int dayOfWeek,
int millis)

Returns the difference in milliseconds between local time and
UTC, taking into account both the raw offset and the effect of
daylight saving, for the specified date and time.

int

getOffset

​(long date)

Returns the offset of this time zone from UTC at the given
time.

int

getRawOffset

()

Gets the GMT offset for this time zone.

int

hashCode

()

Generates the hash code for the SimpleDateFormat object.

boolean

hasSameRules

​(

TimeZone

other)

Returns

true

if this zone has the same rules and offset as another zone.

boolean

inDaylightTime

​(

Date

date)

Queries if the given date is in daylight saving time.

boolean

observesDaylightTime

()

Returns

true

if this

SimpleTimeZone

observes
Daylight Saving Time.

void

setDSTSavings

​(int millisSavedDuringDST)

Sets the amount of time in milliseconds that the clock is advanced
during daylight saving time.

void

setEndRule

​(int endMonth,
int endDay,
int endTime)

Sets the daylight saving time end rule to a fixed date within a month.

void

setEndRule

​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime)

Sets the daylight saving time end rule.

void

setEndRule

​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
boolean after)

Sets the daylight saving time end rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

void

setRawOffset

​(int offsetMillis)

Sets the base time zone offset to GMT.

void

setStartRule

​(int startMonth,
int startDay,
int startTime)

Sets the daylight saving time start rule to a fixed date within a month.

void

setStartRule

​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime)

Sets the daylight saving time start rule.

void

setStartRule

​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
boolean after)

Sets the daylight saving time start rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

void

setStartYear

​(int year)

Sets the daylight saving time starting year.

String

toString

()

Returns a string representation of this time zone.

boolean

useDaylightTime

()

Queries if this time zone uses daylight saving time.

- Methods declared in class java.util.

TimeZone

getAvailableIDs

,

getAvailableIDs

,

getDefault

,

getDisplayName

,

getDisplayName

,

getDisplayName

,

getDisplayName

,

getID

,

getTimeZone

,

getTimeZone

,

setDefault

,

setID

,

toZoneId

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

Returns a clone of this

SimpleTimeZone

instance.

Compares the equality of two

SimpleTimeZone

objects.

Returns the amount of time in milliseconds that the clock is
advanced during daylight saving time.

Returns the difference in milliseconds between local time and
UTC, taking into account both the raw offset and the effect of
daylight saving, for the specified date and time.

Returns the offset of this time zone from UTC at the given
time.

Gets the GMT offset for this time zone.

Generates the hash code for the SimpleDateFormat object.

Returns

true

if this zone has the same rules and offset as another zone.

Queries if the given date is in daylight saving time.

Returns

true

if this

SimpleTimeZone

observes
Daylight Saving Time.

Sets the amount of time in milliseconds that the clock is advanced
during daylight saving time.

Sets the daylight saving time end rule to a fixed date within a month.

Sets the daylight saving time end rule.

Sets the daylight saving time end rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

Sets the base time zone offset to GMT.

Sets the daylight saving time start rule to a fixed date within a month.

Sets the daylight saving time start rule.

Sets the daylight saving time start rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

Sets the daylight saving time starting year.

Returns a string representation of this time zone.

Queries if this time zone uses daylight saving time.

Methods declared in class java.util.

TimeZone

getAvailableIDs

,

getAvailableIDs

,

getDefault

,

getDisplayName

,

getDisplayName

,

getDisplayName

,

getDisplayName

,

getID

,

getTimeZone

,

getTimeZone

,

setDefault

,

setID

,

toZoneId

---

#### Methods declared in class java.util. TimeZone

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

============ FIELD DETAIL ===========

- Field Detail

- WALL_TIME

```java
public static final int WALL_TIME
```

Constant for a mode of start or end time specified as wall clock
time. Wall clock time is standard time for the onset rule, and
daylight time for the end rule.

**Since:** 1.4
**See Also:** Constant Field Values

- STANDARD_TIME

```java
public static final int STANDARD_TIME
```

Constant for a mode of start or end time specified as standard time.

**Since:** 1.4
**See Also:** Constant Field Values

- UTC_TIME

```java
public static final int UTC_TIME
```

Constant for a mode of start or end time specified as UTC. European
Union rules are specified as UTC time, for example.

**Since:** 1.4
**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID)
```

Constructs a SimpleTimeZone with the given base time zone offset from GMT
and time zone ID with no daylight saving time schedule.

**Parameters:** rawOffset

- The base time zone offset in milliseconds to GMT.
**Parameters:** ID

- The time zone name that is given to this instance.

- SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime)
```

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are specified to be
represented in the wall clock time. The amount of daylight saving is
assumed to be 3600000 milliseconds (i.e., one hour). This constructor is
equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
3600000)
```

**Parameters:** rawOffset

- The given base time zone offset from GMT.
**Parameters:** ID

- The time zone ID which is given to this object.
**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field value (0-based. e.g., 0
for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time (in milliseconds within the day), which is local
standard time in this case.
**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Throws:** IllegalArgumentException

- if the month, day, dayOfWeek, or time
parameters are out of range for the start or end rule

- SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int dstSavings)
```

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are assumed to be
represented in the wall clock time. This constructor is equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
dstSavings)
```

**Parameters:** rawOffset

- The given base time zone offset from GMT.
**Parameters:** ID

- The time zone ID which is given to this object.
**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
which is local daylight time in this case.
**Parameters:** dstSavings

- The amount of time in milliseconds saved during
daylight saving time.
**Throws:** IllegalArgumentException

- if the month, day, dayOfWeek, or time
parameters are out of range for the start or end rule
**Since:** 1.2

- SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int startTimeMode,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int endTimeMode,
int dstSavings)
```

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
This constructor takes the full set of the start and end rules
parameters, including modes of

startTime

and

endTime

. The mode specifies either

wall
time

or

standard time

or

UTC
time

.

**Parameters:** rawOffset

- The given base time zone offset from GMT.
**Parameters:** ID

- The time zone ID which is given to this object.
**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in the time mode
specified by

startTimeMode

.
**Parameters:** startTimeMode

- The mode of the start time specified by startTime.
**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in time time mode
specified by

endTimeMode

.
**Parameters:** endTimeMode

- The mode of the end time specified by endTime
**Parameters:** dstSavings

- The amount of time in milliseconds saved during
daylight saving time.
**Throws:** IllegalArgumentException

- if the month, day, dayOfWeek, time more, or
time parameters are out of range for the start or end rule, or if a time mode
value is invalid.
**Since:** 1.4
**See Also:** WALL_TIME

,

STANDARD_TIME

,

UTC_TIME

============ METHOD DETAIL ==========

- Method Detail

- setStartYear

```java
public void setStartYear​(int year)
```

Sets the daylight saving time starting year.

**Parameters:** year

- The daylight saving starting year.

- setStartRule

```java
public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime)
```

Sets the daylight saving time start rule. For example, if daylight saving
time starts on the first Sunday in April at 2 am in local wall clock
time, you can set the start rule by calling:

```java
setStartRule(Calendar.APRIL, 1, Calendar.SUNDAY, 2*60*60*1000);
```

**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
**Throws:** IllegalArgumentException

- if the

startMonth

,

startDay

,

startDayOfWeek

, or

startTime

parameters are out of range

- setStartRule

```java
public void setStartRule​(int startMonth,
int startDay,
int startTime)
```

Sets the daylight saving time start rule to a fixed date within a month.
This method is equivalent to:

```java
setStartRule(startMonth, startDay, 0, startTime)
```

**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
See the class description for the special cases of this parameter.
**Throws:** IllegalArgumentException

- if the

startMonth

,

startDayOfMonth

, or

startTime

parameters are out of range
**Since:** 1.2

- setStartRule

```java
public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
boolean after)
```

Sets the daylight saving time start rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
**Parameters:** after

- If true, this rule selects the first

dayOfWeek

on or

after

dayOfMonth

. If false, this rule
selects the last

dayOfWeek

on or

before

dayOfMonth

.
**Throws:** IllegalArgumentException

- if the

startMonth

,

startDay

,

startDayOfWeek

, or

startTime

parameters are out of range
**Since:** 1.2

- setEndRule

```java
public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime)
```

Sets the daylight saving time end rule. For example, if daylight saving time
ends on the last Sunday in October at 2 am in wall clock time,
you can set the end rule by calling:

setEndRule(Calendar.OCTOBER, -1, Calendar.SUNDAY, 2*60*60*1000);

**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Throws:** IllegalArgumentException

- if the

endMonth

,

endDay

,

endDayOfWeek

, or

endTime

parameters are out of range

- setEndRule

```java
public void setEndRule​(int endMonth,
int endDay,
int endTime)
```

Sets the daylight saving time end rule to a fixed date within a month.
This method is equivalent to:

```java
setEndRule(endMonth, endDay, 0, endTime)
```

**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Throws:** IllegalArgumentException

- the

endMonth

,

endDay

,
or

endTime

parameters are out of range
**Since:** 1.2

- setEndRule

```java
public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
boolean after)
```

Sets the daylight saving time end rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Parameters:** after

- If true, this rule selects the first

endDayOfWeek

on
or

after

endDay

. If false, this rule
selects the last

endDayOfWeek

on or before

endDay

of the month.
**Throws:** IllegalArgumentException

- the

endMonth

,

endDay

,

endDayOfWeek

, or

endTime

parameters are out of range
**Since:** 1.2

- getOffset

```java
public int getOffset​(long date)
```

Returns the offset of this time zone from UTC at the given
time. If daylight saving time is in effect at the given time,
the offset value is adjusted with the amount of daylight
saving.

**Overrides:** getOffset

in class

TimeZone
**Parameters:** date

- the time at which the time zone offset is found
**Returns:** the amount of time in milliseconds to add to UTC to get
local time.
**Since:** 1.4
**See Also:** Calendar.ZONE_OFFSET

,

Calendar.DST_OFFSET

- getOffset

```java
public int getOffset​(int era,
int year,
int month,
int day,
int dayOfWeek,
int millis)
```

Returns the difference in milliseconds between local time and
UTC, taking into account both the raw offset and the effect of
daylight saving, for the specified date and time. This method
assumes that the start and end month are distinct. It also
uses a default

GregorianCalendar

object as its
underlying calendar, such as for determining leap years. Do
not use the result of this method with a calendar other than a
default

GregorianCalendar

.

Note: In general, clients should use

Calendar.get(ZONE_OFFSET) + Calendar.get(DST_OFFSET)

instead of calling this method.

**Specified by:** getOffset

in class

TimeZone
**Parameters:** era

- The era of the given date.
**Parameters:** year

- The year in the given date.
**Parameters:** month

- The month in the given date. Month is 0-based. e.g.,
0 for January.
**Parameters:** day

- The day-in-month of the given date.
**Parameters:** dayOfWeek

- The day-of-week of the given date.
**Parameters:** millis

- The milliseconds in day in

standard

local time.
**Returns:** The milliseconds to add to UTC to get local time.
**Throws:** IllegalArgumentException

- the

era

,

month

,

day

,

dayOfWeek

,
or

millis

parameters are out of range
**See Also:** Calendar.ZONE_OFFSET

,

Calendar.DST_OFFSET

- getRawOffset

```java
public int getRawOffset()
```

Gets the GMT offset for this time zone.

**Specified by:** getRawOffset

in class

TimeZone
**Returns:** the GMT offset value in milliseconds
**See Also:** setRawOffset(int)

- setRawOffset

```java
public void setRawOffset​(int offsetMillis)
```

Sets the base time zone offset to GMT.
This is the offset to add to UTC to get local time.

**Specified by:** setRawOffset

in class

TimeZone
**Parameters:** offsetMillis

- the given base time zone offset to GMT.
**See Also:** getRawOffset()

- setDSTSavings

```java
public void setDSTSavings​(int millisSavedDuringDST)
```

Sets the amount of time in milliseconds that the clock is advanced
during daylight saving time.

**Parameters:** millisSavedDuringDST

- the number of milliseconds the time is
advanced with respect to standard time when the daylight saving time rules
are in effect. A positive number, typically one hour (3600000).
**Since:** 1.2
**See Also:** getDSTSavings()

- getDSTSavings

```java
public int getDSTSavings()
```

Returns the amount of time in milliseconds that the clock is
advanced during daylight saving time.

**Overrides:** getDSTSavings

in class

TimeZone
**Returns:** the number of milliseconds the time is advanced with
respect to standard time when the daylight saving rules are in
effect, or 0 (zero) if this time zone doesn't observe daylight
saving time.
**Since:** 1.2
**See Also:** setDSTSavings(int)

- useDaylightTime

```java
public boolean useDaylightTime()
```

Queries if this time zone uses daylight saving time.

**Specified by:** useDaylightTime

in class

TimeZone
**Returns:** true if this time zone uses daylight saving time;
false otherwise.
**See Also:** TimeZone.inDaylightTime(Date)

,

Calendar.DST_OFFSET

- observesDaylightTime

```java
public boolean observesDaylightTime()
```

Returns

true

if this

SimpleTimeZone

observes
Daylight Saving Time. This method is equivalent to

useDaylightTime()

.

**Overrides:** observesDaylightTime

in class

TimeZone
**Returns:** true

if this

SimpleTimeZone

observes
Daylight Saving Time;

false

otherwise.
**Since:** 1.7
**See Also:** TimeZone.useDaylightTime()

,

TimeZone.inDaylightTime(Date)

,

Calendar.DST_OFFSET

- inDaylightTime

```java
public boolean inDaylightTime​(
Date
date)
```

Queries if the given date is in daylight saving time.

**Specified by:** inDaylightTime

in class

TimeZone
**Parameters:** date

- the given Date.
**Returns:** true if daylight saving time is in effective at the
given date; false otherwise.

- clone

```java
public
Object
clone()
```

Returns a clone of this

SimpleTimeZone

instance.

**Overrides:** clone

in class

TimeZone
**Returns:** a clone of this instance.
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Generates the hash code for the SimpleDateFormat object.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the equality of two

SimpleTimeZone

objects.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The

SimpleTimeZone

object to be compared with.
**Returns:** True if the given

obj

is the same as this

SimpleTimeZone

object; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hasSameRules

```java
public boolean hasSameRules​(
TimeZone
other)
```

Returns

true

if this zone has the same rules and offset as another zone.

**Overrides:** hasSameRules

in class

TimeZone
**Parameters:** other

- the TimeZone object to be compared with
**Returns:** true

if the given zone is a SimpleTimeZone and has the
same rules and offset as this one
**Since:** 1.2

- toString

```java
public
String
toString()
```

Returns a string representation of this time zone.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this time zone.

Field Detail

- WALL_TIME

```java
public static final int WALL_TIME
```

Constant for a mode of start or end time specified as wall clock
time. Wall clock time is standard time for the onset rule, and
daylight time for the end rule.

**Since:** 1.4
**See Also:** Constant Field Values

- STANDARD_TIME

```java
public static final int STANDARD_TIME
```

Constant for a mode of start or end time specified as standard time.

**Since:** 1.4
**See Also:** Constant Field Values

- UTC_TIME

```java
public static final int UTC_TIME
```

Constant for a mode of start or end time specified as UTC. European
Union rules are specified as UTC time, for example.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### Field Detail

WALL_TIME

```java
public static final int WALL_TIME
```

Constant for a mode of start or end time specified as wall clock
time. Wall clock time is standard time for the onset rule, and
daylight time for the end rule.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### WALL_TIME

public static final int WALL_TIME

Constant for a mode of start or end time specified as wall clock
time. Wall clock time is standard time for the onset rule, and
daylight time for the end rule.

STANDARD_TIME

```java
public static final int STANDARD_TIME
```

Constant for a mode of start or end time specified as standard time.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### STANDARD_TIME

public static final int STANDARD_TIME

Constant for a mode of start or end time specified as standard time.

UTC_TIME

```java
public static final int UTC_TIME
```

Constant for a mode of start or end time specified as UTC. European
Union rules are specified as UTC time, for example.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### UTC_TIME

public static final int UTC_TIME

Constant for a mode of start or end time specified as UTC. European
Union rules are specified as UTC time, for example.

Constructor Detail

- SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID)
```

Constructs a SimpleTimeZone with the given base time zone offset from GMT
and time zone ID with no daylight saving time schedule.

**Parameters:** rawOffset

- The base time zone offset in milliseconds to GMT.
**Parameters:** ID

- The time zone name that is given to this instance.

- SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime)
```

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are specified to be
represented in the wall clock time. The amount of daylight saving is
assumed to be 3600000 milliseconds (i.e., one hour). This constructor is
equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
3600000)
```

**Parameters:** rawOffset

- The given base time zone offset from GMT.
**Parameters:** ID

- The time zone ID which is given to this object.
**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field value (0-based. e.g., 0
for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time (in milliseconds within the day), which is local
standard time in this case.
**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Throws:** IllegalArgumentException

- if the month, day, dayOfWeek, or time
parameters are out of range for the start or end rule

- SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int dstSavings)
```

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are assumed to be
represented in the wall clock time. This constructor is equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
dstSavings)
```

**Parameters:** rawOffset

- The given base time zone offset from GMT.
**Parameters:** ID

- The time zone ID which is given to this object.
**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
which is local daylight time in this case.
**Parameters:** dstSavings

- The amount of time in milliseconds saved during
daylight saving time.
**Throws:** IllegalArgumentException

- if the month, day, dayOfWeek, or time
parameters are out of range for the start or end rule
**Since:** 1.2

- SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int startTimeMode,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int endTimeMode,
int dstSavings)
```

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
This constructor takes the full set of the start and end rules
parameters, including modes of

startTime

and

endTime

. The mode specifies either

wall
time

or

standard time

or

UTC
time

.

**Parameters:** rawOffset

- The given base time zone offset from GMT.
**Parameters:** ID

- The time zone ID which is given to this object.
**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in the time mode
specified by

startTimeMode

.
**Parameters:** startTimeMode

- The mode of the start time specified by startTime.
**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in time time mode
specified by

endTimeMode

.
**Parameters:** endTimeMode

- The mode of the end time specified by endTime
**Parameters:** dstSavings

- The amount of time in milliseconds saved during
daylight saving time.
**Throws:** IllegalArgumentException

- if the month, day, dayOfWeek, time more, or
time parameters are out of range for the start or end rule, or if a time mode
value is invalid.
**Since:** 1.4
**See Also:** WALL_TIME

,

STANDARD_TIME

,

UTC_TIME

---

#### Constructor Detail

SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID)
```

Constructs a SimpleTimeZone with the given base time zone offset from GMT
and time zone ID with no daylight saving time schedule.

**Parameters:** rawOffset

- The base time zone offset in milliseconds to GMT.
**Parameters:** ID

- The time zone name that is given to this instance.

---

#### SimpleTimeZone

public SimpleTimeZone​(int rawOffset,

String

ID)

Constructs a SimpleTimeZone with the given base time zone offset from GMT
and time zone ID with no daylight saving time schedule.

SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime)
```

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are specified to be
represented in the wall clock time. The amount of daylight saving is
assumed to be 3600000 milliseconds (i.e., one hour). This constructor is
equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
3600000)
```

**Parameters:** rawOffset

- The given base time zone offset from GMT.
**Parameters:** ID

- The time zone ID which is given to this object.
**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field value (0-based. e.g., 0
for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time (in milliseconds within the day), which is local
standard time in this case.
**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Throws:** IllegalArgumentException

- if the month, day, dayOfWeek, or time
parameters are out of range for the start or end rule

---

#### SimpleTimeZone

public SimpleTimeZone​(int rawOffset,

String

ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are specified to be
represented in the wall clock time. The amount of daylight saving is
assumed to be 3600000 milliseconds (i.e., one hour). This constructor is
equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
3600000)
```

SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.

WALL_TIME

,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.

WALL_TIME

,
3600000)

SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int dstSavings)
```

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are assumed to be
represented in the wall clock time. This constructor is equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
dstSavings)
```

**Parameters:** rawOffset

- The given base time zone offset from GMT.
**Parameters:** ID

- The time zone ID which is given to this object.
**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
which is local daylight time in this case.
**Parameters:** dstSavings

- The amount of time in milliseconds saved during
daylight saving time.
**Throws:** IllegalArgumentException

- if the month, day, dayOfWeek, or time
parameters are out of range for the start or end rule
**Since:** 1.2

---

#### SimpleTimeZone

public SimpleTimeZone​(int rawOffset,

String

ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int dstSavings)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
Both

startTime

and

endTime

are assumed to be
represented in the wall clock time. This constructor is equivalent to:

```java
SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.
WALL_TIME
,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.
WALL_TIME
,
dstSavings)
```

SimpleTimeZone(rawOffset,
ID,
startMonth,
startDay,
startDayOfWeek,
startTime,
SimpleTimeZone.

WALL_TIME

,
endMonth,
endDay,
endDayOfWeek,
endTime,
SimpleTimeZone.

WALL_TIME

,
dstSavings)

SimpleTimeZone

```java
public SimpleTimeZone​(int rawOffset,

String
ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int startTimeMode,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int endTimeMode,
int dstSavings)
```

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
This constructor takes the full set of the start and end rules
parameters, including modes of

startTime

and

endTime

. The mode specifies either

wall
time

or

standard time

or

UTC
time

.

**Parameters:** rawOffset

- The given base time zone offset from GMT.
**Parameters:** ID

- The time zone ID which is given to this object.
**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in the time mode
specified by

startTimeMode

.
**Parameters:** startTimeMode

- The mode of the start time specified by startTime.
**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in time time mode
specified by

endTimeMode

.
**Parameters:** endTimeMode

- The mode of the end time specified by endTime
**Parameters:** dstSavings

- The amount of time in milliseconds saved during
daylight saving time.
**Throws:** IllegalArgumentException

- if the month, day, dayOfWeek, time more, or
time parameters are out of range for the start or end rule, or if a time mode
value is invalid.
**Since:** 1.4
**See Also:** WALL_TIME

,

STANDARD_TIME

,

UTC_TIME

---

#### SimpleTimeZone

public SimpleTimeZone​(int rawOffset,

String

ID,
int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
int startTimeMode,
int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
int endTimeMode,
int dstSavings)

Constructs a SimpleTimeZone with the given base time zone offset from
GMT, time zone ID, and rules for starting and ending the daylight
time.
This constructor takes the full set of the start and end rules
parameters, including modes of

startTime

and

endTime

. The mode specifies either

wall
time

or

standard time

or

UTC
time

.

Method Detail

- setStartYear

```java
public void setStartYear​(int year)
```

Sets the daylight saving time starting year.

**Parameters:** year

- The daylight saving starting year.

- setStartRule

```java
public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime)
```

Sets the daylight saving time start rule. For example, if daylight saving
time starts on the first Sunday in April at 2 am in local wall clock
time, you can set the start rule by calling:

```java
setStartRule(Calendar.APRIL, 1, Calendar.SUNDAY, 2*60*60*1000);
```

**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
**Throws:** IllegalArgumentException

- if the

startMonth

,

startDay

,

startDayOfWeek

, or

startTime

parameters are out of range

- setStartRule

```java
public void setStartRule​(int startMonth,
int startDay,
int startTime)
```

Sets the daylight saving time start rule to a fixed date within a month.
This method is equivalent to:

```java
setStartRule(startMonth, startDay, 0, startTime)
```

**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
See the class description for the special cases of this parameter.
**Throws:** IllegalArgumentException

- if the

startMonth

,

startDayOfMonth

, or

startTime

parameters are out of range
**Since:** 1.2

- setStartRule

```java
public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
boolean after)
```

Sets the daylight saving time start rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
**Parameters:** after

- If true, this rule selects the first

dayOfWeek

on or

after

dayOfMonth

. If false, this rule
selects the last

dayOfWeek

on or

before

dayOfMonth

.
**Throws:** IllegalArgumentException

- if the

startMonth

,

startDay

,

startDayOfWeek

, or

startTime

parameters are out of range
**Since:** 1.2

- setEndRule

```java
public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime)
```

Sets the daylight saving time end rule. For example, if daylight saving time
ends on the last Sunday in October at 2 am in wall clock time,
you can set the end rule by calling:

setEndRule(Calendar.OCTOBER, -1, Calendar.SUNDAY, 2*60*60*1000);

**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Throws:** IllegalArgumentException

- if the

endMonth

,

endDay

,

endDayOfWeek

, or

endTime

parameters are out of range

- setEndRule

```java
public void setEndRule​(int endMonth,
int endDay,
int endTime)
```

Sets the daylight saving time end rule to a fixed date within a month.
This method is equivalent to:

```java
setEndRule(endMonth, endDay, 0, endTime)
```

**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Throws:** IllegalArgumentException

- the

endMonth

,

endDay

,
or

endTime

parameters are out of range
**Since:** 1.2

- setEndRule

```java
public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
boolean after)
```

Sets the daylight saving time end rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Parameters:** after

- If true, this rule selects the first

endDayOfWeek

on
or

after

endDay

. If false, this rule
selects the last

endDayOfWeek

on or before

endDay

of the month.
**Throws:** IllegalArgumentException

- the

endMonth

,

endDay

,

endDayOfWeek

, or

endTime

parameters are out of range
**Since:** 1.2

- getOffset

```java
public int getOffset​(long date)
```

Returns the offset of this time zone from UTC at the given
time. If daylight saving time is in effect at the given time,
the offset value is adjusted with the amount of daylight
saving.

**Overrides:** getOffset

in class

TimeZone
**Parameters:** date

- the time at which the time zone offset is found
**Returns:** the amount of time in milliseconds to add to UTC to get
local time.
**Since:** 1.4
**See Also:** Calendar.ZONE_OFFSET

,

Calendar.DST_OFFSET

- getOffset

```java
public int getOffset​(int era,
int year,
int month,
int day,
int dayOfWeek,
int millis)
```

Returns the difference in milliseconds between local time and
UTC, taking into account both the raw offset and the effect of
daylight saving, for the specified date and time. This method
assumes that the start and end month are distinct. It also
uses a default

GregorianCalendar

object as its
underlying calendar, such as for determining leap years. Do
not use the result of this method with a calendar other than a
default

GregorianCalendar

.

Note: In general, clients should use

Calendar.get(ZONE_OFFSET) + Calendar.get(DST_OFFSET)

instead of calling this method.

**Specified by:** getOffset

in class

TimeZone
**Parameters:** era

- The era of the given date.
**Parameters:** year

- The year in the given date.
**Parameters:** month

- The month in the given date. Month is 0-based. e.g.,
0 for January.
**Parameters:** day

- The day-in-month of the given date.
**Parameters:** dayOfWeek

- The day-of-week of the given date.
**Parameters:** millis

- The milliseconds in day in

standard

local time.
**Returns:** The milliseconds to add to UTC to get local time.
**Throws:** IllegalArgumentException

- the

era

,

month

,

day

,

dayOfWeek

,
or

millis

parameters are out of range
**See Also:** Calendar.ZONE_OFFSET

,

Calendar.DST_OFFSET

- getRawOffset

```java
public int getRawOffset()
```

Gets the GMT offset for this time zone.

**Specified by:** getRawOffset

in class

TimeZone
**Returns:** the GMT offset value in milliseconds
**See Also:** setRawOffset(int)

- setRawOffset

```java
public void setRawOffset​(int offsetMillis)
```

Sets the base time zone offset to GMT.
This is the offset to add to UTC to get local time.

**Specified by:** setRawOffset

in class

TimeZone
**Parameters:** offsetMillis

- the given base time zone offset to GMT.
**See Also:** getRawOffset()

- setDSTSavings

```java
public void setDSTSavings​(int millisSavedDuringDST)
```

Sets the amount of time in milliseconds that the clock is advanced
during daylight saving time.

**Parameters:** millisSavedDuringDST

- the number of milliseconds the time is
advanced with respect to standard time when the daylight saving time rules
are in effect. A positive number, typically one hour (3600000).
**Since:** 1.2
**See Also:** getDSTSavings()

- getDSTSavings

```java
public int getDSTSavings()
```

Returns the amount of time in milliseconds that the clock is
advanced during daylight saving time.

**Overrides:** getDSTSavings

in class

TimeZone
**Returns:** the number of milliseconds the time is advanced with
respect to standard time when the daylight saving rules are in
effect, or 0 (zero) if this time zone doesn't observe daylight
saving time.
**Since:** 1.2
**See Also:** setDSTSavings(int)

- useDaylightTime

```java
public boolean useDaylightTime()
```

Queries if this time zone uses daylight saving time.

**Specified by:** useDaylightTime

in class

TimeZone
**Returns:** true if this time zone uses daylight saving time;
false otherwise.
**See Also:** TimeZone.inDaylightTime(Date)

,

Calendar.DST_OFFSET

- observesDaylightTime

```java
public boolean observesDaylightTime()
```

Returns

true

if this

SimpleTimeZone

observes
Daylight Saving Time. This method is equivalent to

useDaylightTime()

.

**Overrides:** observesDaylightTime

in class

TimeZone
**Returns:** true

if this

SimpleTimeZone

observes
Daylight Saving Time;

false

otherwise.
**Since:** 1.7
**See Also:** TimeZone.useDaylightTime()

,

TimeZone.inDaylightTime(Date)

,

Calendar.DST_OFFSET

- inDaylightTime

```java
public boolean inDaylightTime​(
Date
date)
```

Queries if the given date is in daylight saving time.

**Specified by:** inDaylightTime

in class

TimeZone
**Parameters:** date

- the given Date.
**Returns:** true if daylight saving time is in effective at the
given date; false otherwise.

- clone

```java
public
Object
clone()
```

Returns a clone of this

SimpleTimeZone

instance.

**Overrides:** clone

in class

TimeZone
**Returns:** a clone of this instance.
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Generates the hash code for the SimpleDateFormat object.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the equality of two

SimpleTimeZone

objects.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The

SimpleTimeZone

object to be compared with.
**Returns:** True if the given

obj

is the same as this

SimpleTimeZone

object; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hasSameRules

```java
public boolean hasSameRules​(
TimeZone
other)
```

Returns

true

if this zone has the same rules and offset as another zone.

**Overrides:** hasSameRules

in class

TimeZone
**Parameters:** other

- the TimeZone object to be compared with
**Returns:** true

if the given zone is a SimpleTimeZone and has the
same rules and offset as this one
**Since:** 1.2

- toString

```java
public
String
toString()
```

Returns a string representation of this time zone.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this time zone.

---

#### Method Detail

setStartYear

```java
public void setStartYear​(int year)
```

Sets the daylight saving time starting year.

**Parameters:** year

- The daylight saving starting year.

---

#### setStartYear

public void setStartYear​(int year)

Sets the daylight saving time starting year.

setStartRule

```java
public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime)
```

Sets the daylight saving time start rule. For example, if daylight saving
time starts on the first Sunday in April at 2 am in local wall clock
time, you can set the start rule by calling:

```java
setStartRule(Calendar.APRIL, 1, Calendar.SUNDAY, 2*60*60*1000);
```

**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
See the class description for the special cases of this parameter.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
**Throws:** IllegalArgumentException

- if the

startMonth

,

startDay

,

startDayOfWeek

, or

startTime

parameters are out of range

---

#### setStartRule

public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime)

Sets the daylight saving time start rule. For example, if daylight saving
time starts on the first Sunday in April at 2 am in local wall clock
time, you can set the start rule by calling:

```java
setStartRule(Calendar.APRIL, 1, Calendar.SUNDAY, 2*60*60*1000);
```

setStartRule(Calendar.APRIL, 1, Calendar.SUNDAY, 2*60*60*1000);

setStartRule

```java
public void setStartRule​(int startMonth,
int startDay,
int startTime)
```

Sets the daylight saving time start rule to a fixed date within a month.
This method is equivalent to:

```java
setStartRule(startMonth, startDay, 0, startTime)
```

**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
See the class description for the special cases of this parameter.
**Throws:** IllegalArgumentException

- if the

startMonth

,

startDayOfMonth

, or

startTime

parameters are out of range
**Since:** 1.2

---

#### setStartRule

public void setStartRule​(int startMonth,
int startDay,
int startTime)

Sets the daylight saving time start rule to a fixed date within a month.
This method is equivalent to:

```java
setStartRule(startMonth, startDay, 0, startTime)
```

setStartRule(startMonth, startDay, 0, startTime)

setStartRule

```java
public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
boolean after)
```

Sets the daylight saving time start rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

**Parameters:** startMonth

- The daylight saving time starting month. Month is
a

MONTH

field
value (0-based. e.g., 0 for January).
**Parameters:** startDay

- The day of the month on which the daylight saving time starts.
**Parameters:** startDayOfWeek

- The daylight saving time starting day-of-week.
**Parameters:** startTime

- The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
**Parameters:** after

- If true, this rule selects the first

dayOfWeek

on or

after

dayOfMonth

. If false, this rule
selects the last

dayOfWeek

on or

before

dayOfMonth

.
**Throws:** IllegalArgumentException

- if the

startMonth

,

startDay

,

startDayOfWeek

, or

startTime

parameters are out of range
**Since:** 1.2

---

#### setStartRule

public void setStartRule​(int startMonth,
int startDay,
int startDayOfWeek,
int startTime,
boolean after)

Sets the daylight saving time start rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

setEndRule

```java
public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime)
```

Sets the daylight saving time end rule. For example, if daylight saving time
ends on the last Sunday in October at 2 am in wall clock time,
you can set the end rule by calling:

setEndRule(Calendar.OCTOBER, -1, Calendar.SUNDAY, 2*60*60*1000);

**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
See the class description for the special cases of this parameter.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
See the class description for the special cases of this parameter.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Throws:** IllegalArgumentException

- if the

endMonth

,

endDay

,

endDayOfWeek

, or

endTime

parameters are out of range

---

#### setEndRule

public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime)

Sets the daylight saving time end rule. For example, if daylight saving time
ends on the last Sunday in October at 2 am in wall clock time,
you can set the end rule by calling:

setEndRule(Calendar.OCTOBER, -1, Calendar.SUNDAY, 2*60*60*1000);

setEndRule

```java
public void setEndRule​(int endMonth,
int endDay,
int endTime)
```

Sets the daylight saving time end rule to a fixed date within a month.
This method is equivalent to:

```java
setEndRule(endMonth, endDay, 0, endTime)
```

**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Throws:** IllegalArgumentException

- the

endMonth

,

endDay

,
or

endTime

parameters are out of range
**Since:** 1.2

---

#### setEndRule

public void setEndRule​(int endMonth,
int endDay,
int endTime)

Sets the daylight saving time end rule to a fixed date within a month.
This method is equivalent to:

```java
setEndRule(endMonth, endDay, 0, endTime)
```

setEndRule(endMonth, endDay, 0, endTime)

setEndRule

```java
public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
boolean after)
```

Sets the daylight saving time end rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

**Parameters:** endMonth

- The daylight saving time ending month. Month is
a

MONTH

field
value (0-based. e.g., 9 for October).
**Parameters:** endDay

- The day of the month on which the daylight saving time ends.
**Parameters:** endDayOfWeek

- The daylight saving time ending day-of-week.
**Parameters:** endTime

- The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
**Parameters:** after

- If true, this rule selects the first

endDayOfWeek

on
or

after

endDay

. If false, this rule
selects the last

endDayOfWeek

on or before

endDay

of the month.
**Throws:** IllegalArgumentException

- the

endMonth

,

endDay

,

endDayOfWeek

, or

endTime

parameters are out of range
**Since:** 1.2

---

#### setEndRule

public void setEndRule​(int endMonth,
int endDay,
int endDayOfWeek,
int endTime,
boolean after)

Sets the daylight saving time end rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.

getOffset

```java
public int getOffset​(long date)
```

Returns the offset of this time zone from UTC at the given
time. If daylight saving time is in effect at the given time,
the offset value is adjusted with the amount of daylight
saving.

**Overrides:** getOffset

in class

TimeZone
**Parameters:** date

- the time at which the time zone offset is found
**Returns:** the amount of time in milliseconds to add to UTC to get
local time.
**Since:** 1.4
**See Also:** Calendar.ZONE_OFFSET

,

Calendar.DST_OFFSET

---

#### getOffset

public int getOffset​(long date)

Returns the offset of this time zone from UTC at the given
time. If daylight saving time is in effect at the given time,
the offset value is adjusted with the amount of daylight
saving.

getOffset

```java
public int getOffset​(int era,
int year,
int month,
int day,
int dayOfWeek,
int millis)
```

Returns the difference in milliseconds between local time and
UTC, taking into account both the raw offset and the effect of
daylight saving, for the specified date and time. This method
assumes that the start and end month are distinct. It also
uses a default

GregorianCalendar

object as its
underlying calendar, such as for determining leap years. Do
not use the result of this method with a calendar other than a
default

GregorianCalendar

.

Note: In general, clients should use

Calendar.get(ZONE_OFFSET) + Calendar.get(DST_OFFSET)

instead of calling this method.

**Specified by:** getOffset

in class

TimeZone
**Parameters:** era

- The era of the given date.
**Parameters:** year

- The year in the given date.
**Parameters:** month

- The month in the given date. Month is 0-based. e.g.,
0 for January.
**Parameters:** day

- The day-in-month of the given date.
**Parameters:** dayOfWeek

- The day-of-week of the given date.
**Parameters:** millis

- The milliseconds in day in

standard

local time.
**Returns:** The milliseconds to add to UTC to get local time.
**Throws:** IllegalArgumentException

- the

era

,

month

,

day

,

dayOfWeek

,
or

millis

parameters are out of range
**See Also:** Calendar.ZONE_OFFSET

,

Calendar.DST_OFFSET

---

#### getOffset

public int getOffset​(int era,
int year,
int month,
int day,
int dayOfWeek,
int millis)

Returns the difference in milliseconds between local time and
UTC, taking into account both the raw offset and the effect of
daylight saving, for the specified date and time. This method
assumes that the start and end month are distinct. It also
uses a default

GregorianCalendar

object as its
underlying calendar, such as for determining leap years. Do
not use the result of this method with a calendar other than a
default

GregorianCalendar

.

Note: In general, clients should use

Calendar.get(ZONE_OFFSET) + Calendar.get(DST_OFFSET)

instead of calling this method.

Note: In general, clients should use

Calendar.get(ZONE_OFFSET) + Calendar.get(DST_OFFSET)

instead of calling this method.

getRawOffset

```java
public int getRawOffset()
```

Gets the GMT offset for this time zone.

**Specified by:** getRawOffset

in class

TimeZone
**Returns:** the GMT offset value in milliseconds
**See Also:** setRawOffset(int)

---

#### getRawOffset

public int getRawOffset()

Gets the GMT offset for this time zone.

setRawOffset

```java
public void setRawOffset​(int offsetMillis)
```

Sets the base time zone offset to GMT.
This is the offset to add to UTC to get local time.

**Specified by:** setRawOffset

in class

TimeZone
**Parameters:** offsetMillis

- the given base time zone offset to GMT.
**See Also:** getRawOffset()

---

#### setRawOffset

public void setRawOffset​(int offsetMillis)

Sets the base time zone offset to GMT.
This is the offset to add to UTC to get local time.

setDSTSavings

```java
public void setDSTSavings​(int millisSavedDuringDST)
```

Sets the amount of time in milliseconds that the clock is advanced
during daylight saving time.

**Parameters:** millisSavedDuringDST

- the number of milliseconds the time is
advanced with respect to standard time when the daylight saving time rules
are in effect. A positive number, typically one hour (3600000).
**Since:** 1.2
**See Also:** getDSTSavings()

---

#### setDSTSavings

public void setDSTSavings​(int millisSavedDuringDST)

Sets the amount of time in milliseconds that the clock is advanced
during daylight saving time.

getDSTSavings

```java
public int getDSTSavings()
```

Returns the amount of time in milliseconds that the clock is
advanced during daylight saving time.

**Overrides:** getDSTSavings

in class

TimeZone
**Returns:** the number of milliseconds the time is advanced with
respect to standard time when the daylight saving rules are in
effect, or 0 (zero) if this time zone doesn't observe daylight
saving time.
**Since:** 1.2
**See Also:** setDSTSavings(int)

---

#### getDSTSavings

public int getDSTSavings()

Returns the amount of time in milliseconds that the clock is
advanced during daylight saving time.

useDaylightTime

```java
public boolean useDaylightTime()
```

Queries if this time zone uses daylight saving time.

**Specified by:** useDaylightTime

in class

TimeZone
**Returns:** true if this time zone uses daylight saving time;
false otherwise.
**See Also:** TimeZone.inDaylightTime(Date)

,

Calendar.DST_OFFSET

---

#### useDaylightTime

public boolean useDaylightTime()

Queries if this time zone uses daylight saving time.

observesDaylightTime

```java
public boolean observesDaylightTime()
```

Returns

true

if this

SimpleTimeZone

observes
Daylight Saving Time. This method is equivalent to

useDaylightTime()

.

**Overrides:** observesDaylightTime

in class

TimeZone
**Returns:** true

if this

SimpleTimeZone

observes
Daylight Saving Time;

false

otherwise.
**Since:** 1.7
**See Also:** TimeZone.useDaylightTime()

,

TimeZone.inDaylightTime(Date)

,

Calendar.DST_OFFSET

---

#### observesDaylightTime

public boolean observesDaylightTime()

Returns

true

if this

SimpleTimeZone

observes
Daylight Saving Time. This method is equivalent to

useDaylightTime()

.

inDaylightTime

```java
public boolean inDaylightTime​(
Date
date)
```

Queries if the given date is in daylight saving time.

**Specified by:** inDaylightTime

in class

TimeZone
**Parameters:** date

- the given Date.
**Returns:** true if daylight saving time is in effective at the
given date; false otherwise.

---

#### inDaylightTime

public boolean inDaylightTime​(

Date

date)

Queries if the given date is in daylight saving time.

clone

```java
public
Object
clone()
```

Returns a clone of this

SimpleTimeZone

instance.

**Overrides:** clone

in class

TimeZone
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a clone of this

SimpleTimeZone

instance.

hashCode

```java
public int hashCode()
```

Generates the hash code for the SimpleDateFormat object.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Generates the hash code for the SimpleDateFormat object.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the equality of two

SimpleTimeZone

objects.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The

SimpleTimeZone

object to be compared with.
**Returns:** True if the given

obj

is the same as this

SimpleTimeZone

object; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the equality of two

SimpleTimeZone

objects.

hasSameRules

```java
public boolean hasSameRules​(
TimeZone
other)
```

Returns

true

if this zone has the same rules and offset as another zone.

**Overrides:** hasSameRules

in class

TimeZone
**Parameters:** other

- the TimeZone object to be compared with
**Returns:** true

if the given zone is a SimpleTimeZone and has the
same rules and offset as this one
**Since:** 1.2

---

#### hasSameRules

public boolean hasSameRules​(

TimeZone

other)

Returns

true

if this zone has the same rules and offset as another zone.

toString

```java
public
String
toString()
```

Returns a string representation of this time zone.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this time zone.

---

#### toString

public

String

toString()

Returns a string representation of this time zone.

---

