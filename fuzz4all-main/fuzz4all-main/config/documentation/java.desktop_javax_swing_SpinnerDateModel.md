# Class SpinnerDateModel

**Source:** `java.desktop\javax\swing\SpinnerDateModel.html`

### Class Description

```java
public class
SpinnerDateModel

extends
AbstractSpinnerModel

implements
Serializable
```

A

SpinnerModel

for sequences of

Date

s.
The upper and lower bounds of the sequence are defined by properties called

start

and

end

and the size
of the increase or decrease computed by the

nextValue

and

previousValue

methods is defined by a property
called

calendarField

. The

start

and

end

properties can be

null

to
indicate that the sequence has no lower or upper limit.

The value of the

calendarField

property must be one of the

java.util.Calendar

constants that specify a field
within a

Calendar

. The

getNextValue

and

getPreviousValue

methods change the date forward or backwards by this amount.
For example, if

calendarField

is

Calendar.DAY_OF_WEEK

,
then

nextValue

produces a

Date

that's 24
hours after the current

value

, and

previousValue

produces a

Date

that's 24 hours earlier.

The legal values for

calendarField

are:

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

However some UIs may set the calendarField before committing the edit
to spin the field under the cursor. If you only want one field to
spin you can subclass and ignore the setCalendarField calls.

This model inherits a

ChangeListener

. The

ChangeListeners

are notified whenever the models

value

,

calendarField

,

start

, or

end

properties changes.

**All Implemented Interfaces:** Serializable

,

SpinnerModel

---

### Field Details

*No entries found.*

### Constructor Details

#### public SpinnerDateModel​(
Date
value,

Comparable
<
Date
> start,

Comparable
<
Date
> end,
int calendarField)

Creates a

SpinnerDateModel

that represents a sequence of dates
between

start

and

end

. The

nextValue

and

previousValue

methods
compute elements of the sequence by advancing or reversing
the current date

value

by the

calendarField

time unit. For a precise description
of what it means to increment or decrement a

Calendar

field

, see the

add

method in

java.util.Calendar

.

The

start

and

end

parameters can be

null

to indicate that the range doesn't have an
upper or lower bound. If

value

or

calendarField

is

null

, or if both

start

and

end

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum)

is false,
an IllegalArgumentException is thrown.

**Parameters:**
- value

- the current (non

null

) value of the model
- start

- the first date in the sequence or

null
- end

- the last date in the sequence or

null
- calendarField

- one of

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

**Throws:**
- IllegalArgumentException

- if

value

or

calendarField

are

null

,
if

calendarField

isn't valid,
or if the following expression is
false:

(start <= value <= end)

.

**See Also:**
- Calendar.add(int, int)

,

setValue(java.lang.Object)

,

setStart(java.lang.Comparable<java.util.Date>)

,

setEnd(java.lang.Comparable<java.util.Date>)

,

setCalendarField(int)

---

#### public SpinnerDateModel()

Constructs a

SpinnerDateModel

whose initial

value

is the current date,

calendarField

is equal to

Calendar.DAY_OF_MONTH

, and for which
there are no

start

/

end

limits.

---

### Method Details

#### public void setStart​(
Comparable
<
Date
> start)

Changes the lower limit for Dates in this sequence.
If

start

is

null

,
then there is no lower limit. No bounds checking is done here:
the new start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use
a

Comparable

with a

compareTo

method for Dates.
For example

start

might be an instance of a class like this:

```java
MyStartDate implements Comparable {
long t = 12345;
public int compareTo(Date d) {
return (t < d.getTime() ? -1 : (t == d.getTime() ? 0 : 1));
}
public int compareTo(Object o) {
return compareTo((Date)o);
}
}
```

Note that the above example will throw a

ClassCastException

if the

Object

passed to

compareTo(Object)

is not a

Date

.

This method fires a

ChangeEvent

if the

start

has changed.

**Parameters:**
- start

- defines the first date in the sequence

**See Also:**
- getStart()

,

setEnd(java.lang.Comparable<java.util.Date>)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### public
Comparable
<
Date
> getStart()

Returns the first

Date

in the sequence.

**Returns:**
- the value of the

start

property

**See Also:**
- setStart(java.lang.Comparable<java.util.Date>)

---

#### public void setEnd​(
Comparable
<
Date
> end)

Changes the upper limit for

Date

s in this sequence.
If

start

is

null

, then there is no upper
limit. No bounds checking is done here: the new
start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally, one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use

Comparable

with a

compareTo

method for

Date

s. See

setStart

for an example.

This method fires a

ChangeEvent

if the

end

has changed.

**Parameters:**
- end

- defines the last date in the sequence

**See Also:**
- getEnd()

,

setStart(java.lang.Comparable<java.util.Date>)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### public
Comparable
<
Date
> getEnd()

Returns the last

Date

in the sequence.

**Returns:**
- the value of the

end

property

**See Also:**
- setEnd(java.lang.Comparable<java.util.Date>)

---

#### public void setCalendarField​(int calendarField)

Changes the size of the date value change computed
by the

nextValue

and

previousValue

methods.
The

calendarField

parameter must be one of the

Calendar

field constants like

Calendar.MONTH

or

Calendar.MINUTE

.
The

nextValue

and

previousValue

methods
simply move the specified

Calendar

field forward or backward
by one unit with the

Calendar.add

method.
You should use this method with care as some UIs may set the
calendarField before committing the edit to spin the field under
the cursor. If you only want one field to spin you can subclass
and ignore the setCalendarField calls.

**Parameters:**
- calendarField

- one of

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

This method fires a

ChangeEvent

if the

calendarField

has changed.

**See Also:**
- getCalendarField()

,

getNextValue()

,

getPreviousValue()

,

Calendar.add(int, int)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### public int getCalendarField()

Returns the

Calendar

field that is added to or subtracted from
by the

nextValue

and

previousValue

methods.

**Returns:**
- the value of the

calendarField

property

**See Also:**
- setCalendarField(int)

---

#### public
Object
getNextValue()

Returns the next

Date

in the sequence, or

null

if
the next date is after

end

.

**Specified by:**
- getNextValue

in interface

SpinnerModel

**Returns:**
- the next

Date

in the sequence, or

null

if
the next date is after

end

.

**See Also:**
- SpinnerModel.getNextValue()

,

getPreviousValue()

,

setCalendarField(int)

---

#### public
Object
getPreviousValue()

Returns the previous

Date

in the sequence, or

null

if the previous date is before

start

.

**Specified by:**
- getPreviousValue

in interface

SpinnerModel

**Returns:**
- the previous

Date

in the sequence, or

null

if the previous date
is before

start

**See Also:**
- SpinnerModel.getPreviousValue()

,

getNextValue()

,

setCalendarField(int)

---

#### public
Date
getDate()

Returns the current element in this sequence of

Date

s.
This method is equivalent to

(Date)getValue

.

**Returns:**
- the

value

property

**See Also:**
- setValue(java.lang.Object)

---

#### public
Object
getValue()

Returns the current element in this sequence of

Date

s.

**Specified by:**
- getValue

in interface

SpinnerModel

**Returns:**
- the

value

property

**See Also:**
- setValue(java.lang.Object)

,

getDate()

---

#### public void setValue​(
Object
value)

Sets the current

Date

for this sequence.
If

value

is

null

,
an

IllegalArgumentException

is thrown. No bounds
checking is done here:
the new value may invalidate the

(start <= value < end)

invariant enforced by the constructors. Naturally, one should ensure
that the

(start <= value <= maximum)

invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

This method fires a

ChangeEvent

if the

value

has changed.

**Specified by:**
- setValue

in interface

SpinnerModel

**Parameters:**
- value

- the current (non

null

)

Date

for this sequence

**Throws:**
- IllegalArgumentException

- if value is

null

or not a

Date

**See Also:**
- getDate()

,

getValue()

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

### Additional Sections

#### Class SpinnerDateModel

java.lang.Object

- javax.swing.AbstractSpinnerModel
- - javax.swing.SpinnerDateModel

javax.swing.AbstractSpinnerModel

- javax.swing.SpinnerDateModel

javax.swing.SpinnerDateModel

**All Implemented Interfaces:** Serializable

,

SpinnerModel

```java
public class
SpinnerDateModel

extends
AbstractSpinnerModel

implements
Serializable
```

A

SpinnerModel

for sequences of

Date

s.
The upper and lower bounds of the sequence are defined by properties called

start

and

end

and the size
of the increase or decrease computed by the

nextValue

and

previousValue

methods is defined by a property
called

calendarField

. The

start

and

end

properties can be

null

to
indicate that the sequence has no lower or upper limit.

The value of the

calendarField

property must be one of the

java.util.Calendar

constants that specify a field
within a

Calendar

. The

getNextValue

and

getPreviousValue

methods change the date forward or backwards by this amount.
For example, if

calendarField

is

Calendar.DAY_OF_WEEK

,
then

nextValue

produces a

Date

that's 24
hours after the current

value

, and

previousValue

produces a

Date

that's 24 hours earlier.

The legal values for

calendarField

are:

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

However some UIs may set the calendarField before committing the edit
to spin the field under the cursor. If you only want one field to
spin you can subclass and ignore the setCalendarField calls.

This model inherits a

ChangeListener

. The

ChangeListeners

are notified whenever the models

value

,

calendarField

,

start

, or

end

properties changes.

**Since:** 1.4
**See Also:** JSpinner

,

SpinnerModel

,

AbstractSpinnerModel

,

SpinnerListModel

,

SpinnerNumberModel

,

Calendar.add(int, int)

,

Serialized Form

public class

SpinnerDateModel

extends

AbstractSpinnerModel

implements

Serializable

A

SpinnerModel

for sequences of

Date

s.
The upper and lower bounds of the sequence are defined by properties called

start

and

end

and the size
of the increase or decrease computed by the

nextValue

and

previousValue

methods is defined by a property
called

calendarField

. The

start

and

end

properties can be

null

to
indicate that the sequence has no lower or upper limit.

The value of the

calendarField

property must be one of the

java.util.Calendar

constants that specify a field
within a

Calendar

. The

getNextValue

and

getPreviousValue

methods change the date forward or backwards by this amount.
For example, if

calendarField

is

Calendar.DAY_OF_WEEK

,
then

nextValue

produces a

Date

that's 24
hours after the current

value

, and

previousValue

produces a

Date

that's 24 hours earlier.

The legal values for

calendarField

are:

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

However some UIs may set the calendarField before committing the edit
to spin the field under the cursor. If you only want one field to
spin you can subclass and ignore the setCalendarField calls.

This model inherits a

ChangeListener

. The

ChangeListeners

are notified whenever the models

value

,

calendarField

,

start

, or

end

properties changes.

The value of the

calendarField

property must be one of the

java.util.Calendar

constants that specify a field
within a

Calendar

. The

getNextValue

and

getPreviousValue

methods change the date forward or backwards by this amount.
For example, if

calendarField

is

Calendar.DAY_OF_WEEK

,
then

nextValue

produces a

Date

that's 24
hours after the current

value

, and

previousValue

produces a

Date

that's 24 hours earlier.

The legal values for

calendarField

are:

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

However some UIs may set the calendarField before committing the edit
to spin the field under the cursor. If you only want one field to
spin you can subclass and ignore the setCalendarField calls.

This model inherits a

ChangeListener

. The

ChangeListeners

are notified whenever the models

value

,

calendarField

,

start

, or

end

properties changes.

The legal values for

calendarField

are:

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

However some UIs may set the calendarField before committing the edit
to spin the field under the cursor. If you only want one field to
spin you can subclass and ignore the setCalendarField calls.

This model inherits a

ChangeListener

. The

ChangeListeners

are notified whenever the models

value

,

calendarField

,

start

, or

end

properties changes.

Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

This model inherits a

ChangeListener

. The

ChangeListeners

are notified whenever the models

value

,

calendarField

,

start

, or

end

properties changes.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.

AbstractSpinnerModel

listenerList

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SpinnerDateModel

()

Constructs a

SpinnerDateModel

whose initial

value

is the current date,

calendarField

is equal to

Calendar.DAY_OF_MONTH

, and for which
there are no

start

/

end

limits.

SpinnerDateModel

​(

Date

value,

Comparable

<

Date

> start,

Comparable

<

Date

> end,
int calendarField)

Creates a

SpinnerDateModel

that represents a sequence of dates
between

start

and

end

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

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

field that is added to or subtracted from
by the

nextValue

and

previousValue

methods.

Date

getDate

()

Returns the current element in this sequence of

Date

s.

Comparable

<

Date

>

getEnd

()

Returns the last

Date

in the sequence.

Object

getNextValue

()

Returns the next

Date

in the sequence, or

null

if
the next date is after

end

.

Object

getPreviousValue

()

Returns the previous

Date

in the sequence, or

null

if the previous date is before

start

.

Comparable

<

Date

>

getStart

()

Returns the first

Date

in the sequence.

Object

getValue

()

Returns the current element in this sequence of

Date

s.

void

setCalendarField

​(int calendarField)

Changes the size of the date value change computed
by the

nextValue

and

previousValue

methods.

void

setEnd

​(

Comparable

<

Date

> end)

Changes the upper limit for

Date

s in this sequence.

void

setStart

​(

Comparable

<

Date

> start)

Changes the lower limit for Dates in this sequence.

void

setValue

​(

Object

value)

Sets the current

Date

for this sequence.

- Methods declared in class javax.swing.

AbstractSpinnerModel

addChangeListener

,

fireStateChanged

,

getChangeListeners

,

getListeners

,

removeChangeListener

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

- Fields declared in class javax.swing.

AbstractSpinnerModel

listenerList

---

#### Field Summary

Fields declared in class javax.swing.

AbstractSpinnerModel

listenerList

---

#### Fields declared in class javax.swing. AbstractSpinnerModel

Constructor Summary

Constructors

Constructor

Description

SpinnerDateModel

()

Constructs a

SpinnerDateModel

whose initial

value

is the current date,

calendarField

is equal to

Calendar.DAY_OF_MONTH

, and for which
there are no

start

/

end

limits.

SpinnerDateModel

​(

Date

value,

Comparable

<

Date

> start,

Comparable

<

Date

> end,
int calendarField)

Creates a

SpinnerDateModel

that represents a sequence of dates
between

start

and

end

.

---

#### Constructor Summary

Constructs a

SpinnerDateModel

whose initial

value

is the current date,

calendarField

is equal to

Calendar.DAY_OF_MONTH

, and for which
there are no

start

/

end

limits.

Creates a

SpinnerDateModel

that represents a sequence of dates
between

start

and

end

.

Method Summary

All Methods

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

field that is added to or subtracted from
by the

nextValue

and

previousValue

methods.

Date

getDate

()

Returns the current element in this sequence of

Date

s.

Comparable

<

Date

>

getEnd

()

Returns the last

Date

in the sequence.

Object

getNextValue

()

Returns the next

Date

in the sequence, or

null

if
the next date is after

end

.

Object

getPreviousValue

()

Returns the previous

Date

in the sequence, or

null

if the previous date is before

start

.

Comparable

<

Date

>

getStart

()

Returns the first

Date

in the sequence.

Object

getValue

()

Returns the current element in this sequence of

Date

s.

void

setCalendarField

​(int calendarField)

Changes the size of the date value change computed
by the

nextValue

and

previousValue

methods.

void

setEnd

​(

Comparable

<

Date

> end)

Changes the upper limit for

Date

s in this sequence.

void

setStart

​(

Comparable

<

Date

> start)

Changes the lower limit for Dates in this sequence.

void

setValue

​(

Object

value)

Sets the current

Date

for this sequence.

- Methods declared in class javax.swing.

AbstractSpinnerModel

addChangeListener

,

fireStateChanged

,

getChangeListeners

,

getListeners

,

removeChangeListener

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

Returns the

Calendar

field that is added to or subtracted from
by the

nextValue

and

previousValue

methods.

Returns the current element in this sequence of

Date

s.

Returns the last

Date

in the sequence.

Returns the next

Date

in the sequence, or

null

if
the next date is after

end

.

Returns the previous

Date

in the sequence, or

null

if the previous date is before

start

.

Returns the first

Date

in the sequence.

Changes the size of the date value change computed
by the

nextValue

and

previousValue

methods.

Changes the upper limit for

Date

s in this sequence.

Changes the lower limit for Dates in this sequence.

Sets the current

Date

for this sequence.

Methods declared in class javax.swing.

AbstractSpinnerModel

addChangeListener

,

fireStateChanged

,

getChangeListeners

,

getListeners

,

removeChangeListener

---

#### Methods declared in class javax.swing. AbstractSpinnerModel

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SpinnerDateModel

```java
public SpinnerDateModel​(
Date
value,

Comparable
<
Date
> start,

Comparable
<
Date
> end,
int calendarField)
```

Creates a

SpinnerDateModel

that represents a sequence of dates
between

start

and

end

. The

nextValue

and

previousValue

methods
compute elements of the sequence by advancing or reversing
the current date

value

by the

calendarField

time unit. For a precise description
of what it means to increment or decrement a

Calendar

field

, see the

add

method in

java.util.Calendar

.

The

start

and

end

parameters can be

null

to indicate that the range doesn't have an
upper or lower bound. If

value

or

calendarField

is

null

, or if both

start

and

end

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum)

is false,
an IllegalArgumentException is thrown.

**Parameters:** value

- the current (non

null

) value of the model
**Parameters:** start

- the first date in the sequence or

null
**Parameters:** end

- the last date in the sequence or

null
**Parameters:** calendarField

- one of

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND
**Throws:** IllegalArgumentException

- if

value

or

calendarField

are

null

,
if

calendarField

isn't valid,
or if the following expression is
false:

(start <= value <= end)

.
**See Also:** Calendar.add(int, int)

,

setValue(java.lang.Object)

,

setStart(java.lang.Comparable<java.util.Date>)

,

setEnd(java.lang.Comparable<java.util.Date>)

,

setCalendarField(int)

- SpinnerDateModel

```java
public SpinnerDateModel()
```

Constructs a

SpinnerDateModel

whose initial

value

is the current date,

calendarField

is equal to

Calendar.DAY_OF_MONTH

, and for which
there are no

start

/

end

limits.

============ METHOD DETAIL ==========

- Method Detail

- setStart

```java
public void setStart​(
Comparable
<
Date
> start)
```

Changes the lower limit for Dates in this sequence.
If

start

is

null

,
then there is no lower limit. No bounds checking is done here:
the new start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use
a

Comparable

with a

compareTo

method for Dates.
For example

start

might be an instance of a class like this:

```java
MyStartDate implements Comparable {
long t = 12345;
public int compareTo(Date d) {
return (t < d.getTime() ? -1 : (t == d.getTime() ? 0 : 1));
}
public int compareTo(Object o) {
return compareTo((Date)o);
}
}
```

Note that the above example will throw a

ClassCastException

if the

Object

passed to

compareTo(Object)

is not a

Date

.

This method fires a

ChangeEvent

if the

start

has changed.

**Parameters:** start

- defines the first date in the sequence
**See Also:** getStart()

,

setEnd(java.lang.Comparable<java.util.Date>)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getStart

```java
public
Comparable
<
Date
> getStart()
```

Returns the first

Date

in the sequence.

**Returns:** the value of the

start

property
**See Also:** setStart(java.lang.Comparable<java.util.Date>)

- setEnd

```java
public void setEnd​(
Comparable
<
Date
> end)
```

Changes the upper limit for

Date

s in this sequence.
If

start

is

null

, then there is no upper
limit. No bounds checking is done here: the new
start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally, one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use

Comparable

with a

compareTo

method for

Date

s. See

setStart

for an example.

This method fires a

ChangeEvent

if the

end

has changed.

**Parameters:** end

- defines the last date in the sequence
**See Also:** getEnd()

,

setStart(java.lang.Comparable<java.util.Date>)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getEnd

```java
public
Comparable
<
Date
> getEnd()
```

Returns the last

Date

in the sequence.

**Returns:** the value of the

end

property
**See Also:** setEnd(java.lang.Comparable<java.util.Date>)

- setCalendarField

```java
public void setCalendarField​(int calendarField)
```

Changes the size of the date value change computed
by the

nextValue

and

previousValue

methods.
The

calendarField

parameter must be one of the

Calendar

field constants like

Calendar.MONTH

or

Calendar.MINUTE

.
The

nextValue

and

previousValue

methods
simply move the specified

Calendar

field forward or backward
by one unit with the

Calendar.add

method.
You should use this method with care as some UIs may set the
calendarField before committing the edit to spin the field under
the cursor. If you only want one field to spin you can subclass
and ignore the setCalendarField calls.

**Parameters:** calendarField

- one of

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

This method fires a

ChangeEvent

if the

calendarField

has changed.
**See Also:** getCalendarField()

,

getNextValue()

,

getPreviousValue()

,

Calendar.add(int, int)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getCalendarField

```java
public int getCalendarField()
```

Returns the

Calendar

field that is added to or subtracted from
by the

nextValue

and

previousValue

methods.

**Returns:** the value of the

calendarField

property
**See Also:** setCalendarField(int)

- getNextValue

```java
public
Object
getNextValue()
```

Returns the next

Date

in the sequence, or

null

if
the next date is after

end

.

**Specified by:** getNextValue

in interface

SpinnerModel
**Returns:** the next

Date

in the sequence, or

null

if
the next date is after

end

.
**See Also:** SpinnerModel.getNextValue()

,

getPreviousValue()

,

setCalendarField(int)

- getPreviousValue

```java
public
Object
getPreviousValue()
```

Returns the previous

Date

in the sequence, or

null

if the previous date is before

start

.

**Specified by:** getPreviousValue

in interface

SpinnerModel
**Returns:** the previous

Date

in the sequence, or

null

if the previous date
is before

start
**See Also:** SpinnerModel.getPreviousValue()

,

getNextValue()

,

setCalendarField(int)

- getDate

```java
public
Date
getDate()
```

Returns the current element in this sequence of

Date

s.
This method is equivalent to

(Date)getValue

.

**Returns:** the

value

property
**See Also:** setValue(java.lang.Object)

- getValue

```java
public
Object
getValue()
```

Returns the current element in this sequence of

Date

s.

**Specified by:** getValue

in interface

SpinnerModel
**Returns:** the

value

property
**See Also:** setValue(java.lang.Object)

,

getDate()

- setValue

```java
public void setValue​(
Object
value)
```

Sets the current

Date

for this sequence.
If

value

is

null

,
an

IllegalArgumentException

is thrown. No bounds
checking is done here:
the new value may invalidate the

(start <= value < end)

invariant enforced by the constructors. Naturally, one should ensure
that the

(start <= value <= maximum)

invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

This method fires a

ChangeEvent

if the

value

has changed.

**Specified by:** setValue

in interface

SpinnerModel
**Parameters:** value

- the current (non

null

)

Date

for this sequence
**Throws:** IllegalArgumentException

- if value is

null

or not a

Date
**See Also:** getDate()

,

getValue()

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

Constructor Detail

- SpinnerDateModel

```java
public SpinnerDateModel​(
Date
value,

Comparable
<
Date
> start,

Comparable
<
Date
> end,
int calendarField)
```

Creates a

SpinnerDateModel

that represents a sequence of dates
between

start

and

end

. The

nextValue

and

previousValue

methods
compute elements of the sequence by advancing or reversing
the current date

value

by the

calendarField

time unit. For a precise description
of what it means to increment or decrement a

Calendar

field

, see the

add

method in

java.util.Calendar

.

The

start

and

end

parameters can be

null

to indicate that the range doesn't have an
upper or lower bound. If

value

or

calendarField

is

null

, or if both

start

and

end

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum)

is false,
an IllegalArgumentException is thrown.

**Parameters:** value

- the current (non

null

) value of the model
**Parameters:** start

- the first date in the sequence or

null
**Parameters:** end

- the last date in the sequence or

null
**Parameters:** calendarField

- one of

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND
**Throws:** IllegalArgumentException

- if

value

or

calendarField

are

null

,
if

calendarField

isn't valid,
or if the following expression is
false:

(start <= value <= end)

.
**See Also:** Calendar.add(int, int)

,

setValue(java.lang.Object)

,

setStart(java.lang.Comparable<java.util.Date>)

,

setEnd(java.lang.Comparable<java.util.Date>)

,

setCalendarField(int)

- SpinnerDateModel

```java
public SpinnerDateModel()
```

Constructs a

SpinnerDateModel

whose initial

value

is the current date,

calendarField

is equal to

Calendar.DAY_OF_MONTH

, and for which
there are no

start

/

end

limits.

---

#### Constructor Detail

SpinnerDateModel

```java
public SpinnerDateModel​(
Date
value,

Comparable
<
Date
> start,

Comparable
<
Date
> end,
int calendarField)
```

Creates a

SpinnerDateModel

that represents a sequence of dates
between

start

and

end

. The

nextValue

and

previousValue

methods
compute elements of the sequence by advancing or reversing
the current date

value

by the

calendarField

time unit. For a precise description
of what it means to increment or decrement a

Calendar

field

, see the

add

method in

java.util.Calendar

.

The

start

and

end

parameters can be

null

to indicate that the range doesn't have an
upper or lower bound. If

value

or

calendarField

is

null

, or if both

start

and

end

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum)

is false,
an IllegalArgumentException is thrown.

**Parameters:** value

- the current (non

null

) value of the model
**Parameters:** start

- the first date in the sequence or

null
**Parameters:** end

- the last date in the sequence or

null
**Parameters:** calendarField

- one of

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND
**Throws:** IllegalArgumentException

- if

value

or

calendarField

are

null

,
if

calendarField

isn't valid,
or if the following expression is
false:

(start <= value <= end)

.
**See Also:** Calendar.add(int, int)

,

setValue(java.lang.Object)

,

setStart(java.lang.Comparable<java.util.Date>)

,

setEnd(java.lang.Comparable<java.util.Date>)

,

setCalendarField(int)

---

#### SpinnerDateModel

public SpinnerDateModel​(

Date

value,

Comparable

<

Date

> start,

Comparable

<

Date

> end,
int calendarField)

Creates a

SpinnerDateModel

that represents a sequence of dates
between

start

and

end

. The

nextValue

and

previousValue

methods
compute elements of the sequence by advancing or reversing
the current date

value

by the

calendarField

time unit. For a precise description
of what it means to increment or decrement a

Calendar

field

, see the

add

method in

java.util.Calendar

.

The

start

and

end

parameters can be

null

to indicate that the range doesn't have an
upper or lower bound. If

value

or

calendarField

is

null

, or if both

start

and

end

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum)

is false,
an IllegalArgumentException is thrown.

The

start

and

end

parameters can be

null

to indicate that the range doesn't have an
upper or lower bound. If

value

or

calendarField

is

null

, or if both

start

and

end

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum)

is false,
an IllegalArgumentException is thrown.

Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

SpinnerDateModel

```java
public SpinnerDateModel()
```

Constructs a

SpinnerDateModel

whose initial

value

is the current date,

calendarField

is equal to

Calendar.DAY_OF_MONTH

, and for which
there are no

start

/

end

limits.

---

#### SpinnerDateModel

public SpinnerDateModel()

Constructs a

SpinnerDateModel

whose initial

value

is the current date,

calendarField

is equal to

Calendar.DAY_OF_MONTH

, and for which
there are no

start

/

end

limits.

Method Detail

- setStart

```java
public void setStart​(
Comparable
<
Date
> start)
```

Changes the lower limit for Dates in this sequence.
If

start

is

null

,
then there is no lower limit. No bounds checking is done here:
the new start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use
a

Comparable

with a

compareTo

method for Dates.
For example

start

might be an instance of a class like this:

```java
MyStartDate implements Comparable {
long t = 12345;
public int compareTo(Date d) {
return (t < d.getTime() ? -1 : (t == d.getTime() ? 0 : 1));
}
public int compareTo(Object o) {
return compareTo((Date)o);
}
}
```

Note that the above example will throw a

ClassCastException

if the

Object

passed to

compareTo(Object)

is not a

Date

.

This method fires a

ChangeEvent

if the

start

has changed.

**Parameters:** start

- defines the first date in the sequence
**See Also:** getStart()

,

setEnd(java.lang.Comparable<java.util.Date>)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getStart

```java
public
Comparable
<
Date
> getStart()
```

Returns the first

Date

in the sequence.

**Returns:** the value of the

start

property
**See Also:** setStart(java.lang.Comparable<java.util.Date>)

- setEnd

```java
public void setEnd​(
Comparable
<
Date
> end)
```

Changes the upper limit for

Date

s in this sequence.
If

start

is

null

, then there is no upper
limit. No bounds checking is done here: the new
start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally, one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use

Comparable

with a

compareTo

method for

Date

s. See

setStart

for an example.

This method fires a

ChangeEvent

if the

end

has changed.

**Parameters:** end

- defines the last date in the sequence
**See Also:** getEnd()

,

setStart(java.lang.Comparable<java.util.Date>)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getEnd

```java
public
Comparable
<
Date
> getEnd()
```

Returns the last

Date

in the sequence.

**Returns:** the value of the

end

property
**See Also:** setEnd(java.lang.Comparable<java.util.Date>)

- setCalendarField

```java
public void setCalendarField​(int calendarField)
```

Changes the size of the date value change computed
by the

nextValue

and

previousValue

methods.
The

calendarField

parameter must be one of the

Calendar

field constants like

Calendar.MONTH

or

Calendar.MINUTE

.
The

nextValue

and

previousValue

methods
simply move the specified

Calendar

field forward or backward
by one unit with the

Calendar.add

method.
You should use this method with care as some UIs may set the
calendarField before committing the edit to spin the field under
the cursor. If you only want one field to spin you can subclass
and ignore the setCalendarField calls.

**Parameters:** calendarField

- one of

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

This method fires a

ChangeEvent

if the

calendarField

has changed.
**See Also:** getCalendarField()

,

getNextValue()

,

getPreviousValue()

,

Calendar.add(int, int)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getCalendarField

```java
public int getCalendarField()
```

Returns the

Calendar

field that is added to or subtracted from
by the

nextValue

and

previousValue

methods.

**Returns:** the value of the

calendarField

property
**See Also:** setCalendarField(int)

- getNextValue

```java
public
Object
getNextValue()
```

Returns the next

Date

in the sequence, or

null

if
the next date is after

end

.

**Specified by:** getNextValue

in interface

SpinnerModel
**Returns:** the next

Date

in the sequence, or

null

if
the next date is after

end

.
**See Also:** SpinnerModel.getNextValue()

,

getPreviousValue()

,

setCalendarField(int)

- getPreviousValue

```java
public
Object
getPreviousValue()
```

Returns the previous

Date

in the sequence, or

null

if the previous date is before

start

.

**Specified by:** getPreviousValue

in interface

SpinnerModel
**Returns:** the previous

Date

in the sequence, or

null

if the previous date
is before

start
**See Also:** SpinnerModel.getPreviousValue()

,

getNextValue()

,

setCalendarField(int)

- getDate

```java
public
Date
getDate()
```

Returns the current element in this sequence of

Date

s.
This method is equivalent to

(Date)getValue

.

**Returns:** the

value

property
**See Also:** setValue(java.lang.Object)

- getValue

```java
public
Object
getValue()
```

Returns the current element in this sequence of

Date

s.

**Specified by:** getValue

in interface

SpinnerModel
**Returns:** the

value

property
**See Also:** setValue(java.lang.Object)

,

getDate()

- setValue

```java
public void setValue​(
Object
value)
```

Sets the current

Date

for this sequence.
If

value

is

null

,
an

IllegalArgumentException

is thrown. No bounds
checking is done here:
the new value may invalidate the

(start <= value < end)

invariant enforced by the constructors. Naturally, one should ensure
that the

(start <= value <= maximum)

invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

This method fires a

ChangeEvent

if the

value

has changed.

**Specified by:** setValue

in interface

SpinnerModel
**Parameters:** value

- the current (non

null

)

Date

for this sequence
**Throws:** IllegalArgumentException

- if value is

null

or not a

Date
**See Also:** getDate()

,

getValue()

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### Method Detail

setStart

```java
public void setStart​(
Comparable
<
Date
> start)
```

Changes the lower limit for Dates in this sequence.
If

start

is

null

,
then there is no lower limit. No bounds checking is done here:
the new start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use
a

Comparable

with a

compareTo

method for Dates.
For example

start

might be an instance of a class like this:

```java
MyStartDate implements Comparable {
long t = 12345;
public int compareTo(Date d) {
return (t < d.getTime() ? -1 : (t == d.getTime() ? 0 : 1));
}
public int compareTo(Object o) {
return compareTo((Date)o);
}
}
```

Note that the above example will throw a

ClassCastException

if the

Object

passed to

compareTo(Object)

is not a

Date

.

This method fires a

ChangeEvent

if the

start

has changed.

**Parameters:** start

- defines the first date in the sequence
**See Also:** getStart()

,

setEnd(java.lang.Comparable<java.util.Date>)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### setStart

public void setStart​(

Comparable

<

Date

> start)

Changes the lower limit for Dates in this sequence.
If

start

is

null

,
then there is no lower limit. No bounds checking is done here:
the new start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use
a

Comparable

with a

compareTo

method for Dates.
For example

start

might be an instance of a class like this:

```java
MyStartDate implements Comparable {
long t = 12345;
public int compareTo(Date d) {
return (t < d.getTime() ? -1 : (t == d.getTime() ? 0 : 1));
}
public int compareTo(Object o) {
return compareTo((Date)o);
}
}
```

Note that the above example will throw a

ClassCastException

if the

Object

passed to

compareTo(Object)

is not a

Date

.

This method fires a

ChangeEvent

if the

start

has changed.

Typically this property is a

Date

however it's possible to use
a

Comparable

with a

compareTo

method for Dates.
For example

start

might be an instance of a class like this:

```java
MyStartDate implements Comparable {
long t = 12345;
public int compareTo(Date d) {
return (t < d.getTime() ? -1 : (t == d.getTime() ? 0 : 1));
}
public int compareTo(Object o) {
return compareTo((Date)o);
}
}
```

Note that the above example will throw a

ClassCastException

if the

Object

passed to

compareTo(Object)

is not a

Date

.

This method fires a

ChangeEvent

if the

start

has changed.

MyStartDate implements Comparable {
long t = 12345;
public int compareTo(Date d) {
return (t < d.getTime() ? -1 : (t == d.getTime() ? 0 : 1));
}
public int compareTo(Object o) {
return compareTo((Date)o);
}
}

This method fires a

ChangeEvent

if the

start

has changed.

getStart

```java
public
Comparable
<
Date
> getStart()
```

Returns the first

Date

in the sequence.

**Returns:** the value of the

start

property
**See Also:** setStart(java.lang.Comparable<java.util.Date>)

---

#### getStart

public

Comparable

<

Date

> getStart()

Returns the first

Date

in the sequence.

setEnd

```java
public void setEnd​(
Comparable
<
Date
> end)
```

Changes the upper limit for

Date

s in this sequence.
If

start

is

null

, then there is no upper
limit. No bounds checking is done here: the new
start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally, one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use

Comparable

with a

compareTo

method for

Date

s. See

setStart

for an example.

This method fires a

ChangeEvent

if the

end

has changed.

**Parameters:** end

- defines the last date in the sequence
**See Also:** getEnd()

,

setStart(java.lang.Comparable<java.util.Date>)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### setEnd

public void setEnd​(

Comparable

<

Date

> end)

Changes the upper limit for

Date

s in this sequence.
If

start

is

null

, then there is no upper
limit. No bounds checking is done here: the new
start value may invalidate the

(start <= value <= end)

invariant enforced by the constructors. This is to simplify updating
the model. Naturally, one should ensure that the invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

Typically this property is a

Date

however it's possible to use

Comparable

with a

compareTo

method for

Date

s. See

setStart

for an example.

This method fires a

ChangeEvent

if the

end

has changed.

Typically this property is a

Date

however it's possible to use

Comparable

with a

compareTo

method for

Date

s. See

setStart

for an example.

This method fires a

ChangeEvent

if the

end

has changed.

This method fires a

ChangeEvent

if the

end

has changed.

getEnd

```java
public
Comparable
<
Date
> getEnd()
```

Returns the last

Date

in the sequence.

**Returns:** the value of the

end

property
**See Also:** setEnd(java.lang.Comparable<java.util.Date>)

---

#### getEnd

public

Comparable

<

Date

> getEnd()

Returns the last

Date

in the sequence.

setCalendarField

```java
public void setCalendarField​(int calendarField)
```

Changes the size of the date value change computed
by the

nextValue

and

previousValue

methods.
The

calendarField

parameter must be one of the

Calendar

field constants like

Calendar.MONTH

or

Calendar.MINUTE

.
The

nextValue

and

previousValue

methods
simply move the specified

Calendar

field forward or backward
by one unit with the

Calendar.add

method.
You should use this method with care as some UIs may set the
calendarField before committing the edit to spin the field under
the cursor. If you only want one field to spin you can subclass
and ignore the setCalendarField calls.

**Parameters:** calendarField

- one of

- Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

This method fires a

ChangeEvent

if the

calendarField

has changed.
**See Also:** getCalendarField()

,

getNextValue()

,

getPreviousValue()

,

Calendar.add(int, int)

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### setCalendarField

public void setCalendarField​(int calendarField)

Changes the size of the date value change computed
by the

nextValue

and

previousValue

methods.
The

calendarField

parameter must be one of the

Calendar

field constants like

Calendar.MONTH

or

Calendar.MINUTE

.
The

nextValue

and

previousValue

methods
simply move the specified

Calendar

field forward or backward
by one unit with the

Calendar.add

method.
You should use this method with care as some UIs may set the
calendarField before committing the edit to spin the field under
the cursor. If you only want one field to spin you can subclass
and ignore the setCalendarField calls.

Calendar.ERA

Calendar.YEAR

Calendar.MONTH

Calendar.WEEK_OF_YEAR

Calendar.WEEK_OF_MONTH

Calendar.DAY_OF_MONTH

Calendar.DAY_OF_YEAR

Calendar.DAY_OF_WEEK

Calendar.DAY_OF_WEEK_IN_MONTH

Calendar.AM_PM

Calendar.HOUR

Calendar.HOUR_OF_DAY

Calendar.MINUTE

Calendar.SECOND

Calendar.MILLISECOND

This method fires a

ChangeEvent

if the

calendarField

has changed.

getCalendarField

```java
public int getCalendarField()
```

Returns the

Calendar

field that is added to or subtracted from
by the

nextValue

and

previousValue

methods.

**Returns:** the value of the

calendarField

property
**See Also:** setCalendarField(int)

---

#### getCalendarField

public int getCalendarField()

Returns the

Calendar

field that is added to or subtracted from
by the

nextValue

and

previousValue

methods.

getNextValue

```java
public
Object
getNextValue()
```

Returns the next

Date

in the sequence, or

null

if
the next date is after

end

.

**Specified by:** getNextValue

in interface

SpinnerModel
**Returns:** the next

Date

in the sequence, or

null

if
the next date is after

end

.
**See Also:** SpinnerModel.getNextValue()

,

getPreviousValue()

,

setCalendarField(int)

---

#### getNextValue

public

Object

getNextValue()

Returns the next

Date

in the sequence, or

null

if
the next date is after

end

.

getPreviousValue

```java
public
Object
getPreviousValue()
```

Returns the previous

Date

in the sequence, or

null

if the previous date is before

start

.

**Specified by:** getPreviousValue

in interface

SpinnerModel
**Returns:** the previous

Date

in the sequence, or

null

if the previous date
is before

start
**See Also:** SpinnerModel.getPreviousValue()

,

getNextValue()

,

setCalendarField(int)

---

#### getPreviousValue

public

Object

getPreviousValue()

Returns the previous

Date

in the sequence, or

null

if the previous date is before

start

.

getDate

```java
public
Date
getDate()
```

Returns the current element in this sequence of

Date

s.
This method is equivalent to

(Date)getValue

.

**Returns:** the

value

property
**See Also:** setValue(java.lang.Object)

---

#### getDate

public

Date

getDate()

Returns the current element in this sequence of

Date

s.
This method is equivalent to

(Date)getValue

.

getValue

```java
public
Object
getValue()
```

Returns the current element in this sequence of

Date

s.

**Specified by:** getValue

in interface

SpinnerModel
**Returns:** the

value

property
**See Also:** setValue(java.lang.Object)

,

getDate()

---

#### getValue

public

Object

getValue()

Returns the current element in this sequence of

Date

s.

setValue

```java
public void setValue​(
Object
value)
```

Sets the current

Date

for this sequence.
If

value

is

null

,
an

IllegalArgumentException

is thrown. No bounds
checking is done here:
the new value may invalidate the

(start <= value < end)

invariant enforced by the constructors. Naturally, one should ensure
that the

(start <= value <= maximum)

invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

This method fires a

ChangeEvent

if the

value

has changed.

**Specified by:** setValue

in interface

SpinnerModel
**Parameters:** value

- the current (non

null

)

Date

for this sequence
**Throws:** IllegalArgumentException

- if value is

null

or not a

Date
**See Also:** getDate()

,

getValue()

,

AbstractSpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### setValue

public void setValue​(

Object

value)

Sets the current

Date

for this sequence.
If

value

is

null

,
an

IllegalArgumentException

is thrown. No bounds
checking is done here:
the new value may invalidate the

(start <= value < end)

invariant enforced by the constructors. Naturally, one should ensure
that the

(start <= value <= maximum)

invariant is true
before calling the

nextValue

,

previousValue

,
or

setValue

methods.

This method fires a

ChangeEvent

if the

value

has changed.

This method fires a

ChangeEvent

if the

value

has changed.

---

