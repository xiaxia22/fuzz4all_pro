# Class DateFormat.Field

**Source:** `java.base\java\text\DateFormat.Field.html`

### Class Description

```java
public static class
DateFormat.Field

extends
Format.Field
```

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

DateFormat.formatToCharacterIterator

and as
field identifiers in

FieldPosition

.

The class also provides two methods to map
between its constants and the corresponding Calendar constants.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
DateFormat.Field
ERA

Constant identifying the era field.

---

#### public static final
DateFormat.Field
YEAR

Constant identifying the year field.

---

#### public static final
DateFormat.Field
MONTH

Constant identifying the month field.

---

#### public static final
DateFormat.Field
DAY_OF_MONTH

Constant identifying the day of month field.

---

#### public static final
DateFormat.Field
HOUR_OF_DAY1

Constant identifying the hour of day field, where the legal values
are 1 to 24.

---

#### public static final
DateFormat.Field
HOUR_OF_DAY0

Constant identifying the hour of day field, where the legal values
are 0 to 23.

---

#### public static final
DateFormat.Field
MINUTE

Constant identifying the minute field.

---

#### public static final
DateFormat.Field
SECOND

Constant identifying the second field.

---

#### public static final
DateFormat.Field
MILLISECOND

Constant identifying the millisecond field.

---

#### public static final
DateFormat.Field
DAY_OF_WEEK

Constant identifying the day of week field.

---

#### public static final
DateFormat.Field
DAY_OF_YEAR

Constant identifying the day of year field.

---

#### public static final
DateFormat.Field
DAY_OF_WEEK_IN_MONTH

Constant identifying the day of week field.

---

#### public static final
DateFormat.Field
WEEK_OF_YEAR

Constant identifying the week of year field.

---

#### public static final
DateFormat.Field
WEEK_OF_MONTH

Constant identifying the week of month field.

---

#### public static final
DateFormat.Field
AM_PM

Constant identifying the time of day indicator
(e.g. "a.m." or "p.m.") field.

---

#### public static final
DateFormat.Field
HOUR1

Constant identifying the hour field, where the legal values are
1 to 12.

---

#### public static final
DateFormat.Field
HOUR0

Constant identifying the hour field, where the legal values are
0 to 11.

---

#### public static final
DateFormat.Field
TIME_ZONE

Constant identifying the time zone field.

---

### Constructor Details

#### protected Field​(
String
name,
int calendarField)

Creates a

Field

.

**Parameters:**
- name

- the name of the

Field
- calendarField

- the

Calendar

constant this

Field

corresponds to; any value, even one
outside the range of legal

Calendar

values may
be used, but

-1

should be used for values
that don't correspond to legal

Calendar

values

---

### Method Details

#### public static
DateFormat.Field
ofCalendarField​(int calendarField)

Returns the

Field

constant that corresponds to
the

Calendar

constant

calendarField

.
If there is no direct mapping between the

Calendar

constant and a

Field

, null is returned.

**Parameters:**
- calendarField

- Calendar field constant

**Returns:**
- Field instance representing calendarField.

**Throws:**
- IllegalArgumentException

- if

calendarField

is
not the value of a

Calendar

field constant.

**See Also:**
- Calendar

---

#### public int getCalendarField()

Returns the

Calendar

field associated with this
attribute. For example, if this represents the hours field of
a

Calendar

, this would return

Calendar.HOUR

. If there is no corresponding

Calendar

constant, this will return -1.

**Returns:**
- Calendar constant for this field

**See Also:**
- Calendar

---

#### protected
Object
readResolve()
throws
InvalidObjectException

Resolves instances being deserialized to the predefined constants.

**Overrides:**
- readResolve

in class

AttributedCharacterIterator.Attribute

**Returns:**
- resolved DateFormat.Field constant

**Throws:**
- InvalidObjectException

- if the constant could not be
resolved.

---

### Additional Sections

#### Class DateFormat.Field

java.lang.Object

- java.text.AttributedCharacterIterator.Attribute
- - java.text.Format.Field
- - java.text.DateFormat.Field

java.text.AttributedCharacterIterator.Attribute

- java.text.Format.Field
- - java.text.DateFormat.Field

java.text.Format.Field

- java.text.DateFormat.Field

java.text.DateFormat.Field

**All Implemented Interfaces:** Serializable

**Enclosing class:** DateFormat

```java
public static class
DateFormat.Field

extends
Format.Field
```

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

DateFormat.formatToCharacterIterator

and as
field identifiers in

FieldPosition

.

The class also provides two methods to map
between its constants and the corresponding Calendar constants.

**Since:** 1.4
**See Also:** Calendar

,

Serialized Form

public static class

DateFormat.Field

extends

Format.Field

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

DateFormat.formatToCharacterIterator

and as
field identifiers in

FieldPosition

.

The class also provides two methods to map
between its constants and the corresponding Calendar constants.

The class also provides two methods to map
between its constants and the corresponding Calendar constants.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

DateFormat.Field

AM_PM

Constant identifying the time of day indicator
(e.g.

static

DateFormat.Field

DAY_OF_MONTH

Constant identifying the day of month field.

static

DateFormat.Field

DAY_OF_WEEK

Constant identifying the day of week field.

static

DateFormat.Field

DAY_OF_WEEK_IN_MONTH

Constant identifying the day of week field.

static

DateFormat.Field

DAY_OF_YEAR

Constant identifying the day of year field.

static

DateFormat.Field

ERA

Constant identifying the era field.

static

DateFormat.Field

HOUR_OF_DAY0

Constant identifying the hour of day field, where the legal values
are 0 to 23.

static

DateFormat.Field

HOUR_OF_DAY1

Constant identifying the hour of day field, where the legal values
are 1 to 24.

static

DateFormat.Field

HOUR0

Constant identifying the hour field, where the legal values are
0 to 11.

static

DateFormat.Field

HOUR1

Constant identifying the hour field, where the legal values are
1 to 12.

static

DateFormat.Field

MILLISECOND

Constant identifying the millisecond field.

static

DateFormat.Field

MINUTE

Constant identifying the minute field.

static

DateFormat.Field

MONTH

Constant identifying the month field.

static

DateFormat.Field

SECOND

Constant identifying the second field.

static

DateFormat.Field

TIME_ZONE

Constant identifying the time zone field.

static

DateFormat.Field

WEEK_OF_MONTH

Constant identifying the week of month field.

static

DateFormat.Field

WEEK_OF_YEAR

Constant identifying the week of year field.

static

DateFormat.Field

YEAR

Constant identifying the year field.

- Fields declared in class java.text.

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

,

LANGUAGE

,

READING

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Field

​(

String

name,
int calendarField)

Creates a

Field

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getCalendarField

()

Returns the

Calendar

field associated with this
attribute.

static

DateFormat.Field

ofCalendarField

​(int calendarField)

Returns the

Field

constant that corresponds to
the

Calendar

constant

calendarField

.

protected

Object

readResolve

()

Resolves instances being deserialized to the predefined constants.

- Methods declared in class java.text.

AttributedCharacterIterator.Attribute

equals

,

getName

,

hashCode

,

toString

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

Field Summary

Fields

Modifier and Type

Field

Description

static

DateFormat.Field

AM_PM

Constant identifying the time of day indicator
(e.g.

static

DateFormat.Field

DAY_OF_MONTH

Constant identifying the day of month field.

static

DateFormat.Field

DAY_OF_WEEK

Constant identifying the day of week field.

static

DateFormat.Field

DAY_OF_WEEK_IN_MONTH

Constant identifying the day of week field.

static

DateFormat.Field

DAY_OF_YEAR

Constant identifying the day of year field.

static

DateFormat.Field

ERA

Constant identifying the era field.

static

DateFormat.Field

HOUR_OF_DAY0

Constant identifying the hour of day field, where the legal values
are 0 to 23.

static

DateFormat.Field

HOUR_OF_DAY1

Constant identifying the hour of day field, where the legal values
are 1 to 24.

static

DateFormat.Field

HOUR0

Constant identifying the hour field, where the legal values are
0 to 11.

static

DateFormat.Field

HOUR1

Constant identifying the hour field, where the legal values are
1 to 12.

static

DateFormat.Field

MILLISECOND

Constant identifying the millisecond field.

static

DateFormat.Field

MINUTE

Constant identifying the minute field.

static

DateFormat.Field

MONTH

Constant identifying the month field.

static

DateFormat.Field

SECOND

Constant identifying the second field.

static

DateFormat.Field

TIME_ZONE

Constant identifying the time zone field.

static

DateFormat.Field

WEEK_OF_MONTH

Constant identifying the week of month field.

static

DateFormat.Field

WEEK_OF_YEAR

Constant identifying the week of year field.

static

DateFormat.Field

YEAR

Constant identifying the year field.

- Fields declared in class java.text.

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

,

LANGUAGE

,

READING

---

#### Field Summary

Constant identifying the time of day indicator
(e.g.

Constant identifying the day of month field.

Constant identifying the day of week field.

Constant identifying the day of year field.

Constant identifying the era field.

Constant identifying the hour of day field, where the legal values
are 0 to 23.

Constant identifying the hour of day field, where the legal values
are 1 to 24.

Constant identifying the hour field, where the legal values are
0 to 11.

Constant identifying the hour field, where the legal values are
1 to 12.

Constant identifying the millisecond field.

Constant identifying the minute field.

Constant identifying the month field.

Constant identifying the second field.

Constant identifying the time zone field.

Constant identifying the week of month field.

Constant identifying the week of year field.

Constant identifying the year field.

Fields declared in class java.text.

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

,

LANGUAGE

,

READING

---

#### Fields declared in class java.text. AttributedCharacterIterator.Attribute

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Field

​(

String

name,
int calendarField)

Creates a

Field

.

---

#### Constructor Summary

Creates a

Field

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getCalendarField

()

Returns the

Calendar

field associated with this
attribute.

static

DateFormat.Field

ofCalendarField

​(int calendarField)

Returns the

Field

constant that corresponds to
the

Calendar

constant

calendarField

.

protected

Object

readResolve

()

Resolves instances being deserialized to the predefined constants.

- Methods declared in class java.text.

AttributedCharacterIterator.Attribute

equals

,

getName

,

hashCode

,

toString

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

Returns the

Calendar

field associated with this
attribute.

Returns the

Field

constant that corresponds to
the

Calendar

constant

calendarField

.

Resolves instances being deserialized to the predefined constants.

Methods declared in class java.text.

AttributedCharacterIterator.Attribute

equals

,

getName

,

hashCode

,

toString

---

#### Methods declared in class java.text. AttributedCharacterIterator.Attribute

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

============ FIELD DETAIL ===========

- Field Detail

- ERA

```java
public static final
DateFormat.Field
ERA
```

Constant identifying the era field.

- YEAR

```java
public static final
DateFormat.Field
YEAR
```

Constant identifying the year field.

- MONTH

```java
public static final
DateFormat.Field
MONTH
```

Constant identifying the month field.

- DAY_OF_MONTH

```java
public static final
DateFormat.Field
DAY_OF_MONTH
```

Constant identifying the day of month field.

- HOUR_OF_DAY1

```java
public static final
DateFormat.Field
HOUR_OF_DAY1
```

Constant identifying the hour of day field, where the legal values
are 1 to 24.

- HOUR_OF_DAY0

```java
public static final
DateFormat.Field
HOUR_OF_DAY0
```

Constant identifying the hour of day field, where the legal values
are 0 to 23.

- MINUTE

```java
public static final
DateFormat.Field
MINUTE
```

Constant identifying the minute field.

- SECOND

```java
public static final
DateFormat.Field
SECOND
```

Constant identifying the second field.

- MILLISECOND

```java
public static final
DateFormat.Field
MILLISECOND
```

Constant identifying the millisecond field.

- DAY_OF_WEEK

```java
public static final
DateFormat.Field
DAY_OF_WEEK
```

Constant identifying the day of week field.

- DAY_OF_YEAR

```java
public static final
DateFormat.Field
DAY_OF_YEAR
```

Constant identifying the day of year field.

- DAY_OF_WEEK_IN_MONTH

```java
public static final
DateFormat.Field
DAY_OF_WEEK_IN_MONTH
```

Constant identifying the day of week field.

- WEEK_OF_YEAR

```java
public static final
DateFormat.Field
WEEK_OF_YEAR
```

Constant identifying the week of year field.

- WEEK_OF_MONTH

```java
public static final
DateFormat.Field
WEEK_OF_MONTH
```

Constant identifying the week of month field.

- AM_PM

```java
public static final
DateFormat.Field
AM_PM
```

Constant identifying the time of day indicator
(e.g. "a.m." or "p.m.") field.

- HOUR1

```java
public static final
DateFormat.Field
HOUR1
```

Constant identifying the hour field, where the legal values are
1 to 12.

- HOUR0

```java
public static final
DateFormat.Field
HOUR0
```

Constant identifying the hour field, where the legal values are
0 to 11.

- TIME_ZONE

```java
public static final
DateFormat.Field
TIME_ZONE
```

Constant identifying the time zone field.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Field

```java
protected Field​(
String
name,
int calendarField)
```

Creates a

Field

.

**Parameters:** name

- the name of the

Field
**Parameters:** calendarField

- the

Calendar

constant this

Field

corresponds to; any value, even one
outside the range of legal

Calendar

values may
be used, but

-1

should be used for values
that don't correspond to legal

Calendar

values

============ METHOD DETAIL ==========

- Method Detail

- ofCalendarField

```java
public static
DateFormat.Field
ofCalendarField​(int calendarField)
```

Returns the

Field

constant that corresponds to
the

Calendar

constant

calendarField

.
If there is no direct mapping between the

Calendar

constant and a

Field

, null is returned.

**Parameters:** calendarField

- Calendar field constant
**Returns:** Field instance representing calendarField.
**Throws:** IllegalArgumentException

- if

calendarField

is
not the value of a

Calendar

field constant.
**See Also:** Calendar

- getCalendarField

```java
public int getCalendarField()
```

Returns the

Calendar

field associated with this
attribute. For example, if this represents the hours field of
a

Calendar

, this would return

Calendar.HOUR

. If there is no corresponding

Calendar

constant, this will return -1.

**Returns:** Calendar constant for this field
**See Also:** Calendar

- readResolve

```java
protected
Object
readResolve()
throws
InvalidObjectException
```

Resolves instances being deserialized to the predefined constants.

**Overrides:** readResolve

in class

AttributedCharacterIterator.Attribute
**Returns:** resolved DateFormat.Field constant
**Throws:** InvalidObjectException

- if the constant could not be
resolved.

Field Detail

- ERA

```java
public static final
DateFormat.Field
ERA
```

Constant identifying the era field.

- YEAR

```java
public static final
DateFormat.Field
YEAR
```

Constant identifying the year field.

- MONTH

```java
public static final
DateFormat.Field
MONTH
```

Constant identifying the month field.

- DAY_OF_MONTH

```java
public static final
DateFormat.Field
DAY_OF_MONTH
```

Constant identifying the day of month field.

- HOUR_OF_DAY1

```java
public static final
DateFormat.Field
HOUR_OF_DAY1
```

Constant identifying the hour of day field, where the legal values
are 1 to 24.

- HOUR_OF_DAY0

```java
public static final
DateFormat.Field
HOUR_OF_DAY0
```

Constant identifying the hour of day field, where the legal values
are 0 to 23.

- MINUTE

```java
public static final
DateFormat.Field
MINUTE
```

Constant identifying the minute field.

- SECOND

```java
public static final
DateFormat.Field
SECOND
```

Constant identifying the second field.

- MILLISECOND

```java
public static final
DateFormat.Field
MILLISECOND
```

Constant identifying the millisecond field.

- DAY_OF_WEEK

```java
public static final
DateFormat.Field
DAY_OF_WEEK
```

Constant identifying the day of week field.

- DAY_OF_YEAR

```java
public static final
DateFormat.Field
DAY_OF_YEAR
```

Constant identifying the day of year field.

- DAY_OF_WEEK_IN_MONTH

```java
public static final
DateFormat.Field
DAY_OF_WEEK_IN_MONTH
```

Constant identifying the day of week field.

- WEEK_OF_YEAR

```java
public static final
DateFormat.Field
WEEK_OF_YEAR
```

Constant identifying the week of year field.

- WEEK_OF_MONTH

```java
public static final
DateFormat.Field
WEEK_OF_MONTH
```

Constant identifying the week of month field.

- AM_PM

```java
public static final
DateFormat.Field
AM_PM
```

Constant identifying the time of day indicator
(e.g. "a.m." or "p.m.") field.

- HOUR1

```java
public static final
DateFormat.Field
HOUR1
```

Constant identifying the hour field, where the legal values are
1 to 12.

- HOUR0

```java
public static final
DateFormat.Field
HOUR0
```

Constant identifying the hour field, where the legal values are
0 to 11.

- TIME_ZONE

```java
public static final
DateFormat.Field
TIME_ZONE
```

Constant identifying the time zone field.

---

#### Field Detail

ERA

```java
public static final
DateFormat.Field
ERA
```

Constant identifying the era field.

---

#### ERA

public static final

DateFormat.Field

ERA

Constant identifying the era field.

YEAR

```java
public static final
DateFormat.Field
YEAR
```

Constant identifying the year field.

---

#### YEAR

public static final

DateFormat.Field

YEAR

Constant identifying the year field.

MONTH

```java
public static final
DateFormat.Field
MONTH
```

Constant identifying the month field.

---

#### MONTH

public static final

DateFormat.Field

MONTH

Constant identifying the month field.

DAY_OF_MONTH

```java
public static final
DateFormat.Field
DAY_OF_MONTH
```

Constant identifying the day of month field.

---

#### DAY_OF_MONTH

public static final

DateFormat.Field

DAY_OF_MONTH

Constant identifying the day of month field.

HOUR_OF_DAY1

```java
public static final
DateFormat.Field
HOUR_OF_DAY1
```

Constant identifying the hour of day field, where the legal values
are 1 to 24.

---

#### HOUR_OF_DAY1

public static final

DateFormat.Field

HOUR_OF_DAY1

Constant identifying the hour of day field, where the legal values
are 1 to 24.

HOUR_OF_DAY0

```java
public static final
DateFormat.Field
HOUR_OF_DAY0
```

Constant identifying the hour of day field, where the legal values
are 0 to 23.

---

#### HOUR_OF_DAY0

public static final

DateFormat.Field

HOUR_OF_DAY0

Constant identifying the hour of day field, where the legal values
are 0 to 23.

MINUTE

```java
public static final
DateFormat.Field
MINUTE
```

Constant identifying the minute field.

---

#### MINUTE

public static final

DateFormat.Field

MINUTE

Constant identifying the minute field.

SECOND

```java
public static final
DateFormat.Field
SECOND
```

Constant identifying the second field.

---

#### SECOND

public static final

DateFormat.Field

SECOND

Constant identifying the second field.

MILLISECOND

```java
public static final
DateFormat.Field
MILLISECOND
```

Constant identifying the millisecond field.

---

#### MILLISECOND

public static final

DateFormat.Field

MILLISECOND

Constant identifying the millisecond field.

DAY_OF_WEEK

```java
public static final
DateFormat.Field
DAY_OF_WEEK
```

Constant identifying the day of week field.

---

#### DAY_OF_WEEK

public static final

DateFormat.Field

DAY_OF_WEEK

Constant identifying the day of week field.

DAY_OF_YEAR

```java
public static final
DateFormat.Field
DAY_OF_YEAR
```

Constant identifying the day of year field.

---

#### DAY_OF_YEAR

public static final

DateFormat.Field

DAY_OF_YEAR

Constant identifying the day of year field.

DAY_OF_WEEK_IN_MONTH

```java
public static final
DateFormat.Field
DAY_OF_WEEK_IN_MONTH
```

Constant identifying the day of week field.

---

#### DAY_OF_WEEK_IN_MONTH

public static final

DateFormat.Field

DAY_OF_WEEK_IN_MONTH

Constant identifying the day of week field.

WEEK_OF_YEAR

```java
public static final
DateFormat.Field
WEEK_OF_YEAR
```

Constant identifying the week of year field.

---

#### WEEK_OF_YEAR

public static final

DateFormat.Field

WEEK_OF_YEAR

Constant identifying the week of year field.

WEEK_OF_MONTH

```java
public static final
DateFormat.Field
WEEK_OF_MONTH
```

Constant identifying the week of month field.

---

#### WEEK_OF_MONTH

public static final

DateFormat.Field

WEEK_OF_MONTH

Constant identifying the week of month field.

AM_PM

```java
public static final
DateFormat.Field
AM_PM
```

Constant identifying the time of day indicator
(e.g. "a.m." or "p.m.") field.

---

#### AM_PM

public static final

DateFormat.Field

AM_PM

Constant identifying the time of day indicator
(e.g. "a.m." or "p.m.") field.

HOUR1

```java
public static final
DateFormat.Field
HOUR1
```

Constant identifying the hour field, where the legal values are
1 to 12.

---

#### HOUR1

public static final

DateFormat.Field

HOUR1

Constant identifying the hour field, where the legal values are
1 to 12.

HOUR0

```java
public static final
DateFormat.Field
HOUR0
```

Constant identifying the hour field, where the legal values are
0 to 11.

---

#### HOUR0

public static final

DateFormat.Field

HOUR0

Constant identifying the hour field, where the legal values are
0 to 11.

TIME_ZONE

```java
public static final
DateFormat.Field
TIME_ZONE
```

Constant identifying the time zone field.

---

#### TIME_ZONE

public static final

DateFormat.Field

TIME_ZONE

Constant identifying the time zone field.

Constructor Detail

- Field

```java
protected Field​(
String
name,
int calendarField)
```

Creates a

Field

.

**Parameters:** name

- the name of the

Field
**Parameters:** calendarField

- the

Calendar

constant this

Field

corresponds to; any value, even one
outside the range of legal

Calendar

values may
be used, but

-1

should be used for values
that don't correspond to legal

Calendar

values

---

#### Constructor Detail

Field

```java
protected Field​(
String
name,
int calendarField)
```

Creates a

Field

.

**Parameters:** name

- the name of the

Field
**Parameters:** calendarField

- the

Calendar

constant this

Field

corresponds to; any value, even one
outside the range of legal

Calendar

values may
be used, but

-1

should be used for values
that don't correspond to legal

Calendar

values

---

#### Field

protected Field​(

String

name,
int calendarField)

Creates a

Field

.

Method Detail

- ofCalendarField

```java
public static
DateFormat.Field
ofCalendarField​(int calendarField)
```

Returns the

Field

constant that corresponds to
the

Calendar

constant

calendarField

.
If there is no direct mapping between the

Calendar

constant and a

Field

, null is returned.

**Parameters:** calendarField

- Calendar field constant
**Returns:** Field instance representing calendarField.
**Throws:** IllegalArgumentException

- if

calendarField

is
not the value of a

Calendar

field constant.
**See Also:** Calendar

- getCalendarField

```java
public int getCalendarField()
```

Returns the

Calendar

field associated with this
attribute. For example, if this represents the hours field of
a

Calendar

, this would return

Calendar.HOUR

. If there is no corresponding

Calendar

constant, this will return -1.

**Returns:** Calendar constant for this field
**See Also:** Calendar

- readResolve

```java
protected
Object
readResolve()
throws
InvalidObjectException
```

Resolves instances being deserialized to the predefined constants.

**Overrides:** readResolve

in class

AttributedCharacterIterator.Attribute
**Returns:** resolved DateFormat.Field constant
**Throws:** InvalidObjectException

- if the constant could not be
resolved.

---

#### Method Detail

ofCalendarField

```java
public static
DateFormat.Field
ofCalendarField​(int calendarField)
```

Returns the

Field

constant that corresponds to
the

Calendar

constant

calendarField

.
If there is no direct mapping between the

Calendar

constant and a

Field

, null is returned.

**Parameters:** calendarField

- Calendar field constant
**Returns:** Field instance representing calendarField.
**Throws:** IllegalArgumentException

- if

calendarField

is
not the value of a

Calendar

field constant.
**See Also:** Calendar

---

#### ofCalendarField

public static

DateFormat.Field

ofCalendarField​(int calendarField)

Returns the

Field

constant that corresponds to
the

Calendar

constant

calendarField

.
If there is no direct mapping between the

Calendar

constant and a

Field

, null is returned.

getCalendarField

```java
public int getCalendarField()
```

Returns the

Calendar

field associated with this
attribute. For example, if this represents the hours field of
a

Calendar

, this would return

Calendar.HOUR

. If there is no corresponding

Calendar

constant, this will return -1.

**Returns:** Calendar constant for this field
**See Also:** Calendar

---

#### getCalendarField

public int getCalendarField()

Returns the

Calendar

field associated with this
attribute. For example, if this represents the hours field of
a

Calendar

, this would return

Calendar.HOUR

. If there is no corresponding

Calendar

constant, this will return -1.

readResolve

```java
protected
Object
readResolve()
throws
InvalidObjectException
```

Resolves instances being deserialized to the predefined constants.

**Overrides:** readResolve

in class

AttributedCharacterIterator.Attribute
**Returns:** resolved DateFormat.Field constant
**Throws:** InvalidObjectException

- if the constant could not be
resolved.

---

#### readResolve

protected

Object

readResolve()
throws

InvalidObjectException

Resolves instances being deserialized to the predefined constants.

---

