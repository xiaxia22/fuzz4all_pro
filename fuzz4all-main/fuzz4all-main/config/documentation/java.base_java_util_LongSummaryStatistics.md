# Class LongSummaryStatistics

**Source:** `java.base\java\util\LongSummaryStatistics.html`

### Class Description

```java
public class
LongSummaryStatistics

extends
Object

implements
LongConsumer
,
IntConsumer
```

A state object for collecting statistics such as count, min, max, sum, and
average.

This class is designed to work with (though does not require)

streams

. For example, you can compute
summary statistics on a stream of longs with:

```java
LongSummaryStatistics stats = longStream.collect(LongSummaryStatistics::new,
LongSummaryStatistics::accept,
LongSummaryStatistics::combine);
```

LongSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
LongSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingLong(Person::getAge));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their ages.

**All Implemented Interfaces:** IntConsumer

,

LongConsumer

---

### Field Details

*No entries found.*

### Constructor Details

#### public LongSummaryStatistics()

Constructs an empty instance with zero count, zero sum,

Long.MAX_VALUE

min,

Long.MIN_VALUE

max and zero
average.

---

#### public LongSummaryStatistics​(long count,
long min,
long max,
long sum)
throws
IllegalArgumentException

Constructs a non-empty instance with the specified

count

,

min

,

max

, and

sum

.

If

count

is zero then the remaining arguments are ignored and
an empty instance is constructed.

If the arguments are inconsistent then an

IllegalArgumentException

is thrown. The necessary consistent argument conditions are:

- count >= 0
- min <= max

**Parameters:**
- count

- the count of values
- min

- the minimum value
- max

- the maximum value
- sum

- the sum of all values

**Throws:**
- IllegalArgumentException

- if the arguments are inconsistent

**Since:**
- 10

**API Note:**
- The enforcement of argument correctness means that the retrieved set of
recorded values obtained from a

LongSummaryStatistics

source
instance may not be a legal set of arguments for this constructor due to
arithmetic overflow of the source's recorded count of values.
The consistent argument conditions are not sufficient to prevent the
creation of an internally inconsistent instance. An example of such a
state would be an instance with:

count

= 2,

min

= 1,

max

= 2, and

sum

= 0.

---

### Method Details

#### public void accept​(int value)

Records a new

int

value into the summary information.

**Specified by:**
- accept

in interface

IntConsumer

**Parameters:**
- value

- the input value

---

#### public void accept​(long value)

Records a new

long

value into the summary information.

**Specified by:**
- accept

in interface

LongConsumer

**Parameters:**
- value

- the input value

---

#### public void combine​(
LongSummaryStatistics
other)

Combines the state of another

LongSummaryStatistics

into this
one.

**Parameters:**
- other

- another

LongSummaryStatistics

**Throws:**
- NullPointerException

- if

other

is null

---

#### public final long getCount()

Returns the count of values recorded.

**Returns:**
- the count of values

---

#### public final long getSum()

Returns the sum of values recorded, or zero if no values have been
recorded.

**Returns:**
- the sum of values, or zero if none

---

#### public final long getMin()

Returns the minimum value recorded, or

Long.MAX_VALUE

if no
values have been recorded.

**Returns:**
- the minimum value, or

Long.MAX_VALUE

if none

---

#### public final long getMax()

Returns the maximum value recorded, or

Long.MIN_VALUE

if no
values have been recorded

**Returns:**
- the maximum value, or

Long.MIN_VALUE

if none

---

#### public final double getAverage()

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

**Returns:**
- The arithmetic mean of values, or zero if none

---

#### public
String
toString()

Returns a non-empty string representation of this object suitable for
debugging. The exact presentation format is unspecified and may vary
between implementations and versions.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class LongSummaryStatistics

java.lang.Object

- java.util.LongSummaryStatistics

java.util.LongSummaryStatistics

**All Implemented Interfaces:** IntConsumer

,

LongConsumer

```java
public class
LongSummaryStatistics

extends
Object

implements
LongConsumer
,
IntConsumer
```

A state object for collecting statistics such as count, min, max, sum, and
average.

This class is designed to work with (though does not require)

streams

. For example, you can compute
summary statistics on a stream of longs with:

```java
LongSummaryStatistics stats = longStream.collect(LongSummaryStatistics::new,
LongSummaryStatistics::accept,
LongSummaryStatistics::combine);
```

LongSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
LongSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingLong(Person::getAge));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their ages.

**Implementation Note:** This implementation is not thread safe. However, it is safe to use

Collectors.summarizingLong()

on a parallel stream, because the parallel
implementation of

Stream.collect()

provides the necessary partitioning, isolation, and merging of results for
safe and efficient parallel execution.

This implementation does not check for overflow of the sum.
**Since:** 1.8

public class

LongSummaryStatistics

extends

Object

implements

LongConsumer

,

IntConsumer

A state object for collecting statistics such as count, min, max, sum, and
average.

This class is designed to work with (though does not require)

streams

. For example, you can compute
summary statistics on a stream of longs with:

```java
LongSummaryStatistics stats = longStream.collect(LongSummaryStatistics::new,
LongSummaryStatistics::accept,
LongSummaryStatistics::combine);
```

LongSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
LongSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingLong(Person::getAge));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their ages.

This class is designed to work with (though does not require)

streams

. For example, you can compute
summary statistics on a stream of longs with:

```java
LongSummaryStatistics stats = longStream.collect(LongSummaryStatistics::new,
LongSummaryStatistics::accept,
LongSummaryStatistics::combine);
```

LongSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
LongSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingLong(Person::getAge));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their ages.

LongSummaryStatistics stats = longStream.collect(LongSummaryStatistics::new,
LongSummaryStatistics::accept,
LongSummaryStatistics::combine);

LongSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
LongSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingLong(Person::getAge));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their ages.

LongSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingLong(Person::getAge));

This implementation does not check for overflow of the sum.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LongSummaryStatistics

()

Constructs an empty instance with zero count, zero sum,

Long.MAX_VALUE

min,

Long.MIN_VALUE

max and zero
average.

LongSummaryStatistics

​(long count,
long min,
long max,
long sum)

Constructs a non-empty instance with the specified

count

,

min

,

max

, and

sum

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

accept

​(int value)

Records a new

int

value into the summary information.

void

accept

​(long value)

Records a new

long

value into the summary information.

void

combine

​(

LongSummaryStatistics

other)

Combines the state of another

LongSummaryStatistics

into this
one.

double

getAverage

()

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

long

getCount

()

Returns the count of values recorded.

long

getMax

()

Returns the maximum value recorded, or

Long.MIN_VALUE

if no
values have been recorded

long

getMin

()

Returns the minimum value recorded, or

Long.MAX_VALUE

if no
values have been recorded.

long

getSum

()

Returns the sum of values recorded, or zero if no values have been
recorded.

String

toString

()

Returns a non-empty string representation of this object suitable for
debugging.

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

wait

,

wait

,

wait

- Methods declared in interface java.util.function.

IntConsumer

andThen

- Methods declared in interface java.util.function.

LongConsumer

andThen

Constructor Summary

Constructors

Constructor

Description

LongSummaryStatistics

()

Constructs an empty instance with zero count, zero sum,

Long.MAX_VALUE

min,

Long.MIN_VALUE

max and zero
average.

LongSummaryStatistics

​(long count,
long min,
long max,
long sum)

Constructs a non-empty instance with the specified

count

,

min

,

max

, and

sum

.

---

#### Constructor Summary

Constructs an empty instance with zero count, zero sum,

Long.MAX_VALUE

min,

Long.MIN_VALUE

max and zero
average.

Constructs a non-empty instance with the specified

count

,

min

,

max

, and

sum

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

accept

​(int value)

Records a new

int

value into the summary information.

void

accept

​(long value)

Records a new

long

value into the summary information.

void

combine

​(

LongSummaryStatistics

other)

Combines the state of another

LongSummaryStatistics

into this
one.

double

getAverage

()

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

long

getCount

()

Returns the count of values recorded.

long

getMax

()

Returns the maximum value recorded, or

Long.MIN_VALUE

if no
values have been recorded

long

getMin

()

Returns the minimum value recorded, or

Long.MAX_VALUE

if no
values have been recorded.

long

getSum

()

Returns the sum of values recorded, or zero if no values have been
recorded.

String

toString

()

Returns a non-empty string representation of this object suitable for
debugging.

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

wait

,

wait

,

wait

- Methods declared in interface java.util.function.

IntConsumer

andThen

- Methods declared in interface java.util.function.

LongConsumer

andThen

---

#### Method Summary

Records a new

int

value into the summary information.

Records a new

long

value into the summary information.

Combines the state of another

LongSummaryStatistics

into this
one.

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

Returns the count of values recorded.

Returns the maximum value recorded, or

Long.MIN_VALUE

if no
values have been recorded

Returns the minimum value recorded, or

Long.MAX_VALUE

if no
values have been recorded.

Returns the sum of values recorded, or zero if no values have been
recorded.

Returns a non-empty string representation of this object suitable for
debugging.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.util.function.

IntConsumer

andThen

---

#### Methods declared in interface java.util.function. IntConsumer

Methods declared in interface java.util.function.

LongConsumer

andThen

---

#### Methods declared in interface java.util.function. LongConsumer

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LongSummaryStatistics

```java
public LongSummaryStatistics()
```

Constructs an empty instance with zero count, zero sum,

Long.MAX_VALUE

min,

Long.MIN_VALUE

max and zero
average.

- LongSummaryStatistics

```java
public LongSummaryStatistics​(long count,
long min,
long max,
long sum)
throws
IllegalArgumentException
```

Constructs a non-empty instance with the specified

count

,

min

,

max

, and

sum

.

If

count

is zero then the remaining arguments are ignored and
an empty instance is constructed.

If the arguments are inconsistent then an

IllegalArgumentException

is thrown. The necessary consistent argument conditions are:

- count >= 0
- min <= max

**API Note:** The enforcement of argument correctness means that the retrieved set of
recorded values obtained from a

LongSummaryStatistics

source
instance may not be a legal set of arguments for this constructor due to
arithmetic overflow of the source's recorded count of values.
The consistent argument conditions are not sufficient to prevent the
creation of an internally inconsistent instance. An example of such a
state would be an instance with:

count

= 2,

min

= 1,

max

= 2, and

sum

= 0.
**Parameters:** count

- the count of values
**Parameters:** min

- the minimum value
**Parameters:** max

- the maximum value
**Parameters:** sum

- the sum of all values
**Throws:** IllegalArgumentException

- if the arguments are inconsistent
**Since:** 10

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
public void accept​(int value)
```

Records a new

int

value into the summary information.

**Specified by:** accept

in interface

IntConsumer
**Parameters:** value

- the input value

- accept

```java
public void accept​(long value)
```

Records a new

long

value into the summary information.

**Specified by:** accept

in interface

LongConsumer
**Parameters:** value

- the input value

- combine

```java
public void combine​(
LongSummaryStatistics
other)
```

Combines the state of another

LongSummaryStatistics

into this
one.

**Parameters:** other

- another

LongSummaryStatistics
**Throws:** NullPointerException

- if

other

is null

- getCount

```java
public final long getCount()
```

Returns the count of values recorded.

**Returns:** the count of values

- getSum

```java
public final long getSum()
```

Returns the sum of values recorded, or zero if no values have been
recorded.

**Returns:** the sum of values, or zero if none

- getMin

```java
public final long getMin()
```

Returns the minimum value recorded, or

Long.MAX_VALUE

if no
values have been recorded.

**Returns:** the minimum value, or

Long.MAX_VALUE

if none

- getMax

```java
public final long getMax()
```

Returns the maximum value recorded, or

Long.MIN_VALUE

if no
values have been recorded

**Returns:** the maximum value, or

Long.MIN_VALUE

if none

- getAverage

```java
public final double getAverage()
```

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

**Returns:** The arithmetic mean of values, or zero if none

- toString

```java
public
String
toString()
```

Returns a non-empty string representation of this object suitable for
debugging. The exact presentation format is unspecified and may vary
between implementations and versions.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- LongSummaryStatistics

```java
public LongSummaryStatistics()
```

Constructs an empty instance with zero count, zero sum,

Long.MAX_VALUE

min,

Long.MIN_VALUE

max and zero
average.

- LongSummaryStatistics

```java
public LongSummaryStatistics​(long count,
long min,
long max,
long sum)
throws
IllegalArgumentException
```

Constructs a non-empty instance with the specified

count

,

min

,

max

, and

sum

.

If

count

is zero then the remaining arguments are ignored and
an empty instance is constructed.

If the arguments are inconsistent then an

IllegalArgumentException

is thrown. The necessary consistent argument conditions are:

- count >= 0
- min <= max

**API Note:** The enforcement of argument correctness means that the retrieved set of
recorded values obtained from a

LongSummaryStatistics

source
instance may not be a legal set of arguments for this constructor due to
arithmetic overflow of the source's recorded count of values.
The consistent argument conditions are not sufficient to prevent the
creation of an internally inconsistent instance. An example of such a
state would be an instance with:

count

= 2,

min

= 1,

max

= 2, and

sum

= 0.
**Parameters:** count

- the count of values
**Parameters:** min

- the minimum value
**Parameters:** max

- the maximum value
**Parameters:** sum

- the sum of all values
**Throws:** IllegalArgumentException

- if the arguments are inconsistent
**Since:** 10

---

#### Constructor Detail

LongSummaryStatistics

```java
public LongSummaryStatistics()
```

Constructs an empty instance with zero count, zero sum,

Long.MAX_VALUE

min,

Long.MIN_VALUE

max and zero
average.

---

#### LongSummaryStatistics

public LongSummaryStatistics()

Constructs an empty instance with zero count, zero sum,

Long.MAX_VALUE

min,

Long.MIN_VALUE

max and zero
average.

LongSummaryStatistics

```java
public LongSummaryStatistics​(long count,
long min,
long max,
long sum)
throws
IllegalArgumentException
```

Constructs a non-empty instance with the specified

count

,

min

,

max

, and

sum

.

If

count

is zero then the remaining arguments are ignored and
an empty instance is constructed.

If the arguments are inconsistent then an

IllegalArgumentException

is thrown. The necessary consistent argument conditions are:

- count >= 0
- min <= max

**API Note:** The enforcement of argument correctness means that the retrieved set of
recorded values obtained from a

LongSummaryStatistics

source
instance may not be a legal set of arguments for this constructor due to
arithmetic overflow of the source's recorded count of values.
The consistent argument conditions are not sufficient to prevent the
creation of an internally inconsistent instance. An example of such a
state would be an instance with:

count

= 2,

min

= 1,

max

= 2, and

sum

= 0.
**Parameters:** count

- the count of values
**Parameters:** min

- the minimum value
**Parameters:** max

- the maximum value
**Parameters:** sum

- the sum of all values
**Throws:** IllegalArgumentException

- if the arguments are inconsistent
**Since:** 10

---

#### LongSummaryStatistics

public LongSummaryStatistics​(long count,
long min,
long max,
long sum)
throws

IllegalArgumentException

Constructs a non-empty instance with the specified

count

,

min

,

max

, and

sum

.

If

count

is zero then the remaining arguments are ignored and
an empty instance is constructed.

If the arguments are inconsistent then an

IllegalArgumentException

is thrown. The necessary consistent argument conditions are:

- count >= 0
- min <= max

If

count

is zero then the remaining arguments are ignored and
an empty instance is constructed.

If the arguments are inconsistent then an

IllegalArgumentException

is thrown. The necessary consistent argument conditions are:

- count >= 0
- min <= max

If the arguments are inconsistent then an

IllegalArgumentException

is thrown. The necessary consistent argument conditions are:

- count >= 0
- min <= max

count >= 0

min <= max

Method Detail

- accept

```java
public void accept​(int value)
```

Records a new

int

value into the summary information.

**Specified by:** accept

in interface

IntConsumer
**Parameters:** value

- the input value

- accept

```java
public void accept​(long value)
```

Records a new

long

value into the summary information.

**Specified by:** accept

in interface

LongConsumer
**Parameters:** value

- the input value

- combine

```java
public void combine​(
LongSummaryStatistics
other)
```

Combines the state of another

LongSummaryStatistics

into this
one.

**Parameters:** other

- another

LongSummaryStatistics
**Throws:** NullPointerException

- if

other

is null

- getCount

```java
public final long getCount()
```

Returns the count of values recorded.

**Returns:** the count of values

- getSum

```java
public final long getSum()
```

Returns the sum of values recorded, or zero if no values have been
recorded.

**Returns:** the sum of values, or zero if none

- getMin

```java
public final long getMin()
```

Returns the minimum value recorded, or

Long.MAX_VALUE

if no
values have been recorded.

**Returns:** the minimum value, or

Long.MAX_VALUE

if none

- getMax

```java
public final long getMax()
```

Returns the maximum value recorded, or

Long.MIN_VALUE

if no
values have been recorded

**Returns:** the maximum value, or

Long.MIN_VALUE

if none

- getAverage

```java
public final double getAverage()
```

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

**Returns:** The arithmetic mean of values, or zero if none

- toString

```java
public
String
toString()
```

Returns a non-empty string representation of this object suitable for
debugging. The exact presentation format is unspecified and may vary
between implementations and versions.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

accept

```java
public void accept​(int value)
```

Records a new

int

value into the summary information.

**Specified by:** accept

in interface

IntConsumer
**Parameters:** value

- the input value

---

#### accept

public void accept​(int value)

Records a new

int

value into the summary information.

accept

```java
public void accept​(long value)
```

Records a new

long

value into the summary information.

**Specified by:** accept

in interface

LongConsumer
**Parameters:** value

- the input value

---

#### accept

public void accept​(long value)

Records a new

long

value into the summary information.

combine

```java
public void combine​(
LongSummaryStatistics
other)
```

Combines the state of another

LongSummaryStatistics

into this
one.

**Parameters:** other

- another

LongSummaryStatistics
**Throws:** NullPointerException

- if

other

is null

---

#### combine

public void combine​(

LongSummaryStatistics

other)

Combines the state of another

LongSummaryStatistics

into this
one.

getCount

```java
public final long getCount()
```

Returns the count of values recorded.

**Returns:** the count of values

---

#### getCount

public final long getCount()

Returns the count of values recorded.

getSum

```java
public final long getSum()
```

Returns the sum of values recorded, or zero if no values have been
recorded.

**Returns:** the sum of values, or zero if none

---

#### getSum

public final long getSum()

Returns the sum of values recorded, or zero if no values have been
recorded.

getMin

```java
public final long getMin()
```

Returns the minimum value recorded, or

Long.MAX_VALUE

if no
values have been recorded.

**Returns:** the minimum value, or

Long.MAX_VALUE

if none

---

#### getMin

public final long getMin()

Returns the minimum value recorded, or

Long.MAX_VALUE

if no
values have been recorded.

getMax

```java
public final long getMax()
```

Returns the maximum value recorded, or

Long.MIN_VALUE

if no
values have been recorded

**Returns:** the maximum value, or

Long.MIN_VALUE

if none

---

#### getMax

public final long getMax()

Returns the maximum value recorded, or

Long.MIN_VALUE

if no
values have been recorded

getAverage

```java
public final double getAverage()
```

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

**Returns:** The arithmetic mean of values, or zero if none

---

#### getAverage

public final double getAverage()

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

toString

```java
public
String
toString()
```

Returns a non-empty string representation of this object suitable for
debugging. The exact presentation format is unspecified and may vary
between implementations and versions.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a non-empty string representation of this object suitable for
debugging. The exact presentation format is unspecified and may vary
between implementations and versions.

---

