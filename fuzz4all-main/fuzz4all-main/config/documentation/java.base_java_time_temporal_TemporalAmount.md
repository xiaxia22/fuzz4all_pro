# Interface TemporalAmount

**Source:** `java.base\java\time\temporal\TemporalAmount.html`

### Class Description

```java
public interface
TemporalAmount
```

Framework-level interface defining an amount of time, such as
"6 hours", "8 days" or "2 years and 3 months".

This is the base interface type for amounts of time.
An amount is distinct from a date or time-of-day in that it is not tied
to any specific point on the time-line.

The amount can be thought of as a

Map

of

TemporalUnit

to

long

, exposed via

getUnits()

and

get(TemporalUnit)

.
A simple case might have a single unit-value pair, such as "6 hours".
A more complex case may have multiple unit-value pairs, such as
"7 years, 3 months and 5 days".

There are two common implementations.

Period

is a date-based implementation, storing years, months and days.

Duration

is a time-based implementation, storing seconds and nanoseconds,
but providing some access using other duration based units such as minutes,
hours and fixed 24-hour days.

This interface is a framework-level interface that should not be widely
used in application code. Instead, applications should create and pass
around instances of concrete types, such as

Period

and

Duration

.

**All Known Subinterfaces:** ChronoPeriod

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long get​(
TemporalUnit
unit)

Returns the value of the requested unit.
The units returned from

getUnits()

uniquely define the
value of the

TemporalAmount

. A value must be returned
for each unit listed in

getUnits

.

**Parameters:**
- unit

- the

TemporalUnit

for which to return the value

**Returns:**
- the long value of the unit

**Throws:**
- DateTimeException

- if a value for the unit cannot be obtained
- UnsupportedTemporalTypeException

- if the

unit

is not supported

**Implementation Requirements:**
- Implementations may declare support for units not listed by

getUnits()

.
Typically, the implementation would define additional units
as conversions for the convenience of developers.

---

#### List
<
TemporalUnit
> getUnits()

Returns the list of units uniquely defining the value of this TemporalAmount.
The list of

TemporalUnits

is defined by the implementation class.
The list is a snapshot of the units at the time

getUnits

is called and is not mutable.
The units are ordered from longest duration to the shortest duration
of the unit.

**Returns:**
- the List of

TemporalUnits

; not null

**Implementation Requirements:**
- The list of units completely and uniquely represents the
state of the object without omissions, overlaps or duplication.
The units are in order from longest duration to shortest.

---

#### Temporal
addTo​(
Temporal
temporal)

Adds to the specified temporal object.

Adds the amount to the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.plus(TemporalAmount)

:

```java
// These two lines are equivalent, but the second approach is recommended
dateTime = amount.addTo(dateTime);
dateTime = dateTime.plus(adder);
```

It is recommended to use the second approach,

plus(TemporalAmount)

,
as it is a lot clearer to read in code.

**Parameters:**
- temporal

- the temporal object to add the amount to, not null

**Returns:**
- an object of the same observable type with the addition made, not null

**Throws:**
- DateTimeException

- if unable to add
- ArithmeticException

- if numeric overflow occurs

**Implementation Requirements:**
- The implementation must take the input object and add to it.
The implementation defines the logic of the addition and is responsible for
documenting that logic. It may use any method on

Temporal

to
query the temporal object and perform the addition.
The returned object must have the same observable type as the input object

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.

---

#### Temporal
subtractFrom​(
Temporal
temporal)

Subtracts this object from the specified temporal object.

Subtracts the amount from the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.minus(TemporalAmount)

:

```java
// these two lines are equivalent, but the second approach is recommended
dateTime = amount.subtractFrom(dateTime);
dateTime = dateTime.minus(amount);
```

It is recommended to use the second approach,

minus(TemporalAmount)

,
as it is a lot clearer to read in code.

**Parameters:**
- temporal

- the temporal object to subtract the amount from, not null

**Returns:**
- an object of the same observable type with the subtraction made, not null

**Throws:**
- DateTimeException

- if unable to subtract
- ArithmeticException

- if numeric overflow occurs

**Implementation Requirements:**
- The implementation must take the input object and subtract from it.
The implementation defines the logic of the subtraction and is responsible for
documenting that logic. It may use any method on

Temporal

to
query the temporal object and perform the subtraction.
The returned object must have the same observable type as the input object

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.

---

### Additional Sections

#### Interface TemporalAmount

**All Known Subinterfaces:** ChronoPeriod

**All Known Implementing Classes:** Duration

,

Period

```java
public interface
TemporalAmount
```

Framework-level interface defining an amount of time, such as
"6 hours", "8 days" or "2 years and 3 months".

This is the base interface type for amounts of time.
An amount is distinct from a date or time-of-day in that it is not tied
to any specific point on the time-line.

The amount can be thought of as a

Map

of

TemporalUnit

to

long

, exposed via

getUnits()

and

get(TemporalUnit)

.
A simple case might have a single unit-value pair, such as "6 hours".
A more complex case may have multiple unit-value pairs, such as
"7 years, 3 months and 5 days".

There are two common implementations.

Period

is a date-based implementation, storing years, months and days.

Duration

is a time-based implementation, storing seconds and nanoseconds,
but providing some access using other duration based units such as minutes,
hours and fixed 24-hour days.

This interface is a framework-level interface that should not be widely
used in application code. Instead, applications should create and pass
around instances of concrete types, such as

Period

and

Duration

.

**Implementation Requirements:** This interface places no restrictions on the mutability of implementations,
however immutability is strongly recommended.
**Since:** 1.8

public interface

TemporalAmount

Framework-level interface defining an amount of time, such as
"6 hours", "8 days" or "2 years and 3 months".

This is the base interface type for amounts of time.
An amount is distinct from a date or time-of-day in that it is not tied
to any specific point on the time-line.

The amount can be thought of as a

Map

of

TemporalUnit

to

long

, exposed via

getUnits()

and

get(TemporalUnit)

.
A simple case might have a single unit-value pair, such as "6 hours".
A more complex case may have multiple unit-value pairs, such as
"7 years, 3 months and 5 days".

There are two common implementations.

Period

is a date-based implementation, storing years, months and days.

Duration

is a time-based implementation, storing seconds and nanoseconds,
but providing some access using other duration based units such as minutes,
hours and fixed 24-hour days.

This interface is a framework-level interface that should not be widely
used in application code. Instead, applications should create and pass
around instances of concrete types, such as

Period

and

Duration

.

This is the base interface type for amounts of time.
An amount is distinct from a date or time-of-day in that it is not tied
to any specific point on the time-line.

The amount can be thought of as a

Map

of

TemporalUnit

to

long

, exposed via

getUnits()

and

get(TemporalUnit)

.
A simple case might have a single unit-value pair, such as "6 hours".
A more complex case may have multiple unit-value pairs, such as
"7 years, 3 months and 5 days".

There are two common implementations.

Period

is a date-based implementation, storing years, months and days.

Duration

is a time-based implementation, storing seconds and nanoseconds,
but providing some access using other duration based units such as minutes,
hours and fixed 24-hour days.

This interface is a framework-level interface that should not be widely
used in application code. Instead, applications should create and pass
around instances of concrete types, such as

Period

and

Duration

.

The amount can be thought of as a

Map

of

TemporalUnit

to

long

, exposed via

getUnits()

and

get(TemporalUnit)

.
A simple case might have a single unit-value pair, such as "6 hours".
A more complex case may have multiple unit-value pairs, such as
"7 years, 3 months and 5 days".

There are two common implementations.

Period

is a date-based implementation, storing years, months and days.

Duration

is a time-based implementation, storing seconds and nanoseconds,
but providing some access using other duration based units such as minutes,
hours and fixed 24-hour days.

This interface is a framework-level interface that should not be widely
used in application code. Instead, applications should create and pass
around instances of concrete types, such as

Period

and

Duration

.

There are two common implementations.

Period

is a date-based implementation, storing years, months and days.

Duration

is a time-based implementation, storing seconds and nanoseconds,
but providing some access using other duration based units such as minutes,
hours and fixed 24-hour days.

This interface is a framework-level interface that should not be widely
used in application code. Instead, applications should create and pass
around instances of concrete types, such as

Period

and

Duration

.

This interface is a framework-level interface that should not be widely
used in application code. Instead, applications should create and pass
around instances of concrete types, such as

Period

and

Duration

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Temporal

addTo

​(

Temporal

temporal)

Adds to the specified temporal object.

long

get

​(

TemporalUnit

unit)

Returns the value of the requested unit.

List

<

TemporalUnit

>

getUnits

()

Returns the list of units uniquely defining the value of this TemporalAmount.

Temporal

subtractFrom

​(

Temporal

temporal)

Subtracts this object from the specified temporal object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Temporal

addTo

​(

Temporal

temporal)

Adds to the specified temporal object.

long

get

​(

TemporalUnit

unit)

Returns the value of the requested unit.

List

<

TemporalUnit

>

getUnits

()

Returns the list of units uniquely defining the value of this TemporalAmount.

Temporal

subtractFrom

​(

Temporal

temporal)

Subtracts this object from the specified temporal object.

---

#### Method Summary

Adds to the specified temporal object.

Returns the value of the requested unit.

Returns the list of units uniquely defining the value of this TemporalAmount.

Subtracts this object from the specified temporal object.

============ METHOD DETAIL ==========

- Method Detail

- get

```java
long get​(
TemporalUnit
unit)
```

Returns the value of the requested unit.
The units returned from

getUnits()

uniquely define the
value of the

TemporalAmount

. A value must be returned
for each unit listed in

getUnits

.

**Implementation Requirements:** Implementations may declare support for units not listed by

getUnits()

.
Typically, the implementation would define additional units
as conversions for the convenience of developers.
**Parameters:** unit

- the

TemporalUnit

for which to return the value
**Returns:** the long value of the unit
**Throws:** DateTimeException

- if a value for the unit cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the

unit

is not supported

- getUnits

```java
List
<
TemporalUnit
> getUnits()
```

Returns the list of units uniquely defining the value of this TemporalAmount.
The list of

TemporalUnits

is defined by the implementation class.
The list is a snapshot of the units at the time

getUnits

is called and is not mutable.
The units are ordered from longest duration to the shortest duration
of the unit.

**Implementation Requirements:** The list of units completely and uniquely represents the
state of the object without omissions, overlaps or duplication.
The units are in order from longest duration to shortest.
**Returns:** the List of

TemporalUnits

; not null

- addTo

```java
Temporal
addTo​(
Temporal
temporal)
```

Adds to the specified temporal object.

Adds the amount to the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.plus(TemporalAmount)

:

```java
// These two lines are equivalent, but the second approach is recommended
dateTime = amount.addTo(dateTime);
dateTime = dateTime.plus(adder);
```

It is recommended to use the second approach,

plus(TemporalAmount)

,
as it is a lot clearer to read in code.

**Implementation Requirements:** The implementation must take the input object and add to it.
The implementation defines the logic of the addition and is responsible for
documenting that logic. It may use any method on

Temporal

to
query the temporal object and perform the addition.
The returned object must have the same observable type as the input object

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.
**Parameters:** temporal

- the temporal object to add the amount to, not null
**Returns:** an object of the same observable type with the addition made, not null
**Throws:** DateTimeException

- if unable to add
**Throws:** ArithmeticException

- if numeric overflow occurs

- subtractFrom

```java
Temporal
subtractFrom​(
Temporal
temporal)
```

Subtracts this object from the specified temporal object.

Subtracts the amount from the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.minus(TemporalAmount)

:

```java
// these two lines are equivalent, but the second approach is recommended
dateTime = amount.subtractFrom(dateTime);
dateTime = dateTime.minus(amount);
```

It is recommended to use the second approach,

minus(TemporalAmount)

,
as it is a lot clearer to read in code.

**Implementation Requirements:** The implementation must take the input object and subtract from it.
The implementation defines the logic of the subtraction and is responsible for
documenting that logic. It may use any method on

Temporal

to
query the temporal object and perform the subtraction.
The returned object must have the same observable type as the input object

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.
**Parameters:** temporal

- the temporal object to subtract the amount from, not null
**Returns:** an object of the same observable type with the subtraction made, not null
**Throws:** DateTimeException

- if unable to subtract
**Throws:** ArithmeticException

- if numeric overflow occurs

Method Detail

- get

```java
long get​(
TemporalUnit
unit)
```

Returns the value of the requested unit.
The units returned from

getUnits()

uniquely define the
value of the

TemporalAmount

. A value must be returned
for each unit listed in

getUnits

.

**Implementation Requirements:** Implementations may declare support for units not listed by

getUnits()

.
Typically, the implementation would define additional units
as conversions for the convenience of developers.
**Parameters:** unit

- the

TemporalUnit

for which to return the value
**Returns:** the long value of the unit
**Throws:** DateTimeException

- if a value for the unit cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the

unit

is not supported

- getUnits

```java
List
<
TemporalUnit
> getUnits()
```

Returns the list of units uniquely defining the value of this TemporalAmount.
The list of

TemporalUnits

is defined by the implementation class.
The list is a snapshot of the units at the time

getUnits

is called and is not mutable.
The units are ordered from longest duration to the shortest duration
of the unit.

**Implementation Requirements:** The list of units completely and uniquely represents the
state of the object without omissions, overlaps or duplication.
The units are in order from longest duration to shortest.
**Returns:** the List of

TemporalUnits

; not null

- addTo

```java
Temporal
addTo​(
Temporal
temporal)
```

Adds to the specified temporal object.

Adds the amount to the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.plus(TemporalAmount)

:

```java
// These two lines are equivalent, but the second approach is recommended
dateTime = amount.addTo(dateTime);
dateTime = dateTime.plus(adder);
```

It is recommended to use the second approach,

plus(TemporalAmount)

,
as it is a lot clearer to read in code.

**Implementation Requirements:** The implementation must take the input object and add to it.
The implementation defines the logic of the addition and is responsible for
documenting that logic. It may use any method on

Temporal

to
query the temporal object and perform the addition.
The returned object must have the same observable type as the input object

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.
**Parameters:** temporal

- the temporal object to add the amount to, not null
**Returns:** an object of the same observable type with the addition made, not null
**Throws:** DateTimeException

- if unable to add
**Throws:** ArithmeticException

- if numeric overflow occurs

- subtractFrom

```java
Temporal
subtractFrom​(
Temporal
temporal)
```

Subtracts this object from the specified temporal object.

Subtracts the amount from the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.minus(TemporalAmount)

:

```java
// these two lines are equivalent, but the second approach is recommended
dateTime = amount.subtractFrom(dateTime);
dateTime = dateTime.minus(amount);
```

It is recommended to use the second approach,

minus(TemporalAmount)

,
as it is a lot clearer to read in code.

**Implementation Requirements:** The implementation must take the input object and subtract from it.
The implementation defines the logic of the subtraction and is responsible for
documenting that logic. It may use any method on

Temporal

to
query the temporal object and perform the subtraction.
The returned object must have the same observable type as the input object

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.
**Parameters:** temporal

- the temporal object to subtract the amount from, not null
**Returns:** an object of the same observable type with the subtraction made, not null
**Throws:** DateTimeException

- if unable to subtract
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### Method Detail

get

```java
long get​(
TemporalUnit
unit)
```

Returns the value of the requested unit.
The units returned from

getUnits()

uniquely define the
value of the

TemporalAmount

. A value must be returned
for each unit listed in

getUnits

.

**Implementation Requirements:** Implementations may declare support for units not listed by

getUnits()

.
Typically, the implementation would define additional units
as conversions for the convenience of developers.
**Parameters:** unit

- the

TemporalUnit

for which to return the value
**Returns:** the long value of the unit
**Throws:** DateTimeException

- if a value for the unit cannot be obtained
**Throws:** UnsupportedTemporalTypeException

- if the

unit

is not supported

---

#### get

long get​(

TemporalUnit

unit)

Returns the value of the requested unit.
The units returned from

getUnits()

uniquely define the
value of the

TemporalAmount

. A value must be returned
for each unit listed in

getUnits

.

getUnits

```java
List
<
TemporalUnit
> getUnits()
```

Returns the list of units uniquely defining the value of this TemporalAmount.
The list of

TemporalUnits

is defined by the implementation class.
The list is a snapshot of the units at the time

getUnits

is called and is not mutable.
The units are ordered from longest duration to the shortest duration
of the unit.

**Implementation Requirements:** The list of units completely and uniquely represents the
state of the object without omissions, overlaps or duplication.
The units are in order from longest duration to shortest.
**Returns:** the List of

TemporalUnits

; not null

---

#### getUnits

List

<

TemporalUnit

> getUnits()

Returns the list of units uniquely defining the value of this TemporalAmount.
The list of

TemporalUnits

is defined by the implementation class.
The list is a snapshot of the units at the time

getUnits

is called and is not mutable.
The units are ordered from longest duration to the shortest duration
of the unit.

addTo

```java
Temporal
addTo​(
Temporal
temporal)
```

Adds to the specified temporal object.

Adds the amount to the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.plus(TemporalAmount)

:

```java
// These two lines are equivalent, but the second approach is recommended
dateTime = amount.addTo(dateTime);
dateTime = dateTime.plus(adder);
```

It is recommended to use the second approach,

plus(TemporalAmount)

,
as it is a lot clearer to read in code.

**Implementation Requirements:** The implementation must take the input object and add to it.
The implementation defines the logic of the addition and is responsible for
documenting that logic. It may use any method on

Temporal

to
query the temporal object and perform the addition.
The returned object must have the same observable type as the input object

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.
**Parameters:** temporal

- the temporal object to add the amount to, not null
**Returns:** an object of the same observable type with the addition made, not null
**Throws:** DateTimeException

- if unable to add
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### addTo

Temporal

addTo​(

Temporal

temporal)

Adds to the specified temporal object.

Adds the amount to the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.plus(TemporalAmount)

:

```java
// These two lines are equivalent, but the second approach is recommended
dateTime = amount.addTo(dateTime);
dateTime = dateTime.plus(adder);
```

It is recommended to use the second approach,

plus(TemporalAmount)

,
as it is a lot clearer to read in code.

Adds the amount to the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.plus(TemporalAmount)

:

```java
// These two lines are equivalent, but the second approach is recommended
dateTime = amount.addTo(dateTime);
dateTime = dateTime.plus(adder);
```

It is recommended to use the second approach,

plus(TemporalAmount)

,
as it is a lot clearer to read in code.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.plus(TemporalAmount)

:

```java
// These two lines are equivalent, but the second approach is recommended
dateTime = amount.addTo(dateTime);
dateTime = dateTime.plus(adder);
```

It is recommended to use the second approach,

plus(TemporalAmount)

,
as it is a lot clearer to read in code.

// These two lines are equivalent, but the second approach is recommended
dateTime = amount.addTo(dateTime);
dateTime = dateTime.plus(adder);

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.

subtractFrom

```java
Temporal
subtractFrom​(
Temporal
temporal)
```

Subtracts this object from the specified temporal object.

Subtracts the amount from the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.minus(TemporalAmount)

:

```java
// these two lines are equivalent, but the second approach is recommended
dateTime = amount.subtractFrom(dateTime);
dateTime = dateTime.minus(amount);
```

It is recommended to use the second approach,

minus(TemporalAmount)

,
as it is a lot clearer to read in code.

**Implementation Requirements:** The implementation must take the input object and subtract from it.
The implementation defines the logic of the subtraction and is responsible for
documenting that logic. It may use any method on

Temporal

to
query the temporal object and perform the subtraction.
The returned object must have the same observable type as the input object

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.
**Parameters:** temporal

- the temporal object to subtract the amount from, not null
**Returns:** an object of the same observable type with the subtraction made, not null
**Throws:** DateTimeException

- if unable to subtract
**Throws:** ArithmeticException

- if numeric overflow occurs

---

#### subtractFrom

Temporal

subtractFrom​(

Temporal

temporal)

Subtracts this object from the specified temporal object.

Subtracts the amount from the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.minus(TemporalAmount)

:

```java
// these two lines are equivalent, but the second approach is recommended
dateTime = amount.subtractFrom(dateTime);
dateTime = dateTime.minus(amount);
```

It is recommended to use the second approach,

minus(TemporalAmount)

,
as it is a lot clearer to read in code.

Subtracts the amount from the specified temporal object using the logic
encapsulated in the implementing class.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.minus(TemporalAmount)

:

```java
// these two lines are equivalent, but the second approach is recommended
dateTime = amount.subtractFrom(dateTime);
dateTime = dateTime.minus(amount);
```

It is recommended to use the second approach,

minus(TemporalAmount)

,
as it is a lot clearer to read in code.

There are two equivalent ways of using this method.
The first is to invoke this method directly.
The second is to use

Temporal.minus(TemporalAmount)

:

```java
// these two lines are equivalent, but the second approach is recommended
dateTime = amount.subtractFrom(dateTime);
dateTime = dateTime.minus(amount);
```

It is recommended to use the second approach,

minus(TemporalAmount)

,
as it is a lot clearer to read in code.

// these two lines are equivalent, but the second approach is recommended
dateTime = amount.subtractFrom(dateTime);
dateTime = dateTime.minus(amount);

The input object must not be altered.
Instead, an adjusted copy of the original must be returned.
This provides equivalent, safe behavior for immutable and mutable temporal objects.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.

The input temporal object may be in a calendar system other than ISO.
Implementations may choose to document compatibility with other calendar systems,
or reject non-ISO temporal objects by

querying the chronology

.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.

This method may be called from multiple threads in parallel.
It must be thread-safe when invoked.

---

