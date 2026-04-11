# Class IntSummaryStatistics

**Source:** `java.base\java\util\IntSummaryStatistics.html`

### Class Description

```java
public class
IntSummaryStatistics

extends
Object

implements
IntConsumer
```

A state object for collecting statistics such as count, min, max, sum, and
average.

This class is designed to work with (though does not require)

streams

. For example, you can compute
summary statistics on a stream of ints with:

```java
IntSummaryStatistics stats = intStream.collect(IntSummaryStatistics::new,
IntSummaryStatistics::accept,
IntSummaryStatistics::combine);
```

IntSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
IntSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingInt(Person::getDependents));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their number of dependents.

**All Implemented Interfaces:** IntConsumer

---

### Field Details

*No entries found.*

### Constructor Details

#### public IntSummaryStatistics()

Constructs an empty instance with zero count, zero sum,

Integer.MAX_VALUE

min,

Integer.MIN_VALUE

max and zero
average.

---

#### public IntSummaryStatistics​(long count,
int min,
int max,
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

IntSummaryStatistics

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

Records a new value into the summary information

**Specified by:**
- accept

in interface

IntConsumer

**Parameters:**
- value

- the input value

---

#### public void combine​(
IntSummaryStatistics
other)

Combines the state of another

IntSummaryStatistics

into this one.

**Parameters:**
- other

- another

IntSummaryStatistics

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

#### public final int getMin()

Returns the minimum value recorded, or

Integer.MAX_VALUE

if no
values have been recorded.

**Returns:**
- the minimum value, or

Integer.MAX_VALUE

if none

---

#### public final int getMax()

Returns the maximum value recorded, or

Integer.MIN_VALUE

if no
values have been recorded.

**Returns:**
- the maximum value, or

Integer.MIN_VALUE

if none

---

#### public final double getAverage()

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

**Returns:**
- the arithmetic mean of values, or zero if none

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

#### Class IntSummaryStatistics

java.lang.Object

- java.util.IntSummaryStatistics

java.util.IntSummaryStatistics

**All Implemented Interfaces:** IntConsumer

```java
public class
IntSummaryStatistics

extends
Object

implements
IntConsumer
```

A state object for collecting statistics such as count, min, max, sum, and
average.

This class is designed to work with (though does not require)

streams

. For example, you can compute
summary statistics on a stream of ints with:

```java
IntSummaryStatistics stats = intStream.collect(IntSummaryStatistics::new,
IntSummaryStatistics::accept,
IntSummaryStatistics::combine);
```

IntSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
IntSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingInt(Person::getDependents));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their number of dependents.

**Implementation Note:** This implementation is not thread safe. However, it is safe to use

Collectors.summarizingInt()

on a parallel stream, because the parallel
implementation of

Stream.collect()

provides the necessary partitioning, isolation, and merging of results for
safe and efficient parallel execution.

This implementation does not check for overflow of the sum.
**Since:** 1.8

public class

IntSummaryStatistics

extends

Object

implements

IntConsumer

A state object for collecting statistics such as count, min, max, sum, and
average.

This class is designed to work with (though does not require)

streams

. For example, you can compute
summary statistics on a stream of ints with:

```java
IntSummaryStatistics stats = intStream.collect(IntSummaryStatistics::new,
IntSummaryStatistics::accept,
IntSummaryStatistics::combine);
```

IntSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
IntSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingInt(Person::getDependents));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their number of dependents.

This class is designed to work with (though does not require)

streams

. For example, you can compute
summary statistics on a stream of ints with:

```java
IntSummaryStatistics stats = intStream.collect(IntSummaryStatistics::new,
IntSummaryStatistics::accept,
IntSummaryStatistics::combine);
```

IntSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
IntSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingInt(Person::getDependents));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their number of dependents.

IntSummaryStatistics stats = intStream.collect(IntSummaryStatistics::new,
IntSummaryStatistics::accept,
IntSummaryStatistics::combine);

IntSummaryStatistics

can be used as a

reduction

target for a

stream

. For example:

```java
IntSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingInt(Person::getDependents));
```

This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their number of dependents.

IntSummaryStatistics stats = people.stream()
.collect(Collectors.summarizingInt(Person::getDependents));

This implementation does not check for overflow of the sum.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IntSummaryStatistics

()

Constructs an empty instance with zero count, zero sum,

Integer.MAX_VALUE

min,

Integer.MIN_VALUE

max and zero
average.

IntSummaryStatistics

​(long count,
int min,
int max,
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

Records a new value into the summary information

void

combine

​(

IntSummaryStatistics

other)

Combines the state of another

IntSummaryStatistics

into this one.

double

getAverage

()

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

long

getCount

()

Returns the count of values recorded.

int

getMax

()

Returns the maximum value recorded, or

Integer.MIN_VALUE

if no
values have been recorded.

int

getMin

()

Returns the minimum value recorded, or

Integer.MAX_VALUE

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

Constructor Summary

Constructors

Constructor

Description

IntSummaryStatistics

()

Constructs an empty instance with zero count, zero sum,

Integer.MAX_VALUE

min,

Integer.MIN_VALUE

max and zero
average.

IntSummaryStatistics

​(long count,
int min,
int max,
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

Integer.MAX_VALUE

min,

Integer.MIN_VALUE

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

Records a new value into the summary information

void

combine

​(

IntSummaryStatistics

other)

Combines the state of another

IntSummaryStatistics

into this one.

double

getAverage

()

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

long

getCount

()

Returns the count of values recorded.

int

getMax

()

Returns the maximum value recorded, or

Integer.MIN_VALUE

if no
values have been recorded.

int

getMin

()

Returns the minimum value recorded, or

Integer.MAX_VALUE

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

---

#### Method Summary

Records a new value into the summary information

Combines the state of another

IntSummaryStatistics

into this one.

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

Returns the count of values recorded.

Returns the maximum value recorded, or

Integer.MIN_VALUE

if no
values have been recorded.

Returns the minimum value recorded, or

Integer.MAX_VALUE

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- IntSummaryStatistics

```java
public IntSummaryStatistics()
```

Constructs an empty instance with zero count, zero sum,

Integer.MAX_VALUE

min,

Integer.MIN_VALUE

max and zero
average.

- IntSummaryStatistics

```java
public IntSummaryStatistics​(long count,
int min,
int max,
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

IntSummaryStatistics

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

Records a new value into the summary information

**Specified by:** accept

in interface

IntConsumer
**Parameters:** value

- the input value

- combine

```java
public void combine​(
IntSummaryStatistics
other)
```

Combines the state of another

IntSummaryStatistics

into this one.

**Parameters:** other

- another

IntSummaryStatistics
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
public final int getMin()
```

Returns the minimum value recorded, or

Integer.MAX_VALUE

if no
values have been recorded.

**Returns:** the minimum value, or

Integer.MAX_VALUE

if none

- getMax

```java
public final int getMax()
```

Returns the maximum value recorded, or

Integer.MIN_VALUE

if no
values have been recorded.

**Returns:** the maximum value, or

Integer.MIN_VALUE

if none

- getAverage

```java
public final double getAverage()
```

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

**Returns:** the arithmetic mean of values, or zero if none

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

- IntSummaryStatistics

```java
public IntSummaryStatistics()
```

Constructs an empty instance with zero count, zero sum,

Integer.MAX_VALUE

min,

Integer.MIN_VALUE

max and zero
average.

- IntSummaryStatistics

```java
public IntSummaryStatistics​(long count,
int min,
int max,
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

IntSummaryStatistics

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

IntSummaryStatistics

```java
public IntSummaryStatistics()
```

Constructs an empty instance with zero count, zero sum,

Integer.MAX_VALUE

min,

Integer.MIN_VALUE

max and zero
average.

---

#### IntSummaryStatistics

public IntSummaryStatistics()

Constructs an empty instance with zero count, zero sum,

Integer.MAX_VALUE

min,

Integer.MIN_VALUE

max and zero
average.

IntSummaryStatistics

```java
public IntSummaryStatistics​(long count,
int min,
int max,
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

IntSummaryStatistics

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

#### IntSummaryStatistics

public IntSummaryStatistics​(long count,
int min,
int max,
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

Records a new value into the summary information

**Specified by:** accept

in interface

IntConsumer
**Parameters:** value

- the input value

- combine

```java
public void combine​(
IntSummaryStatistics
other)
```

Combines the state of another

IntSummaryStatistics

into this one.

**Parameters:** other

- another

IntSummaryStatistics
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
public final int getMin()
```

Returns the minimum value recorded, or

Integer.MAX_VALUE

if no
values have been recorded.

**Returns:** the minimum value, or

Integer.MAX_VALUE

if none

- getMax

```java
public final int getMax()
```

Returns the maximum value recorded, or

Integer.MIN_VALUE

if no
values have been recorded.

**Returns:** the maximum value, or

Integer.MIN_VALUE

if none

- getAverage

```java
public final double getAverage()
```

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

**Returns:** the arithmetic mean of values, or zero if none

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

Records a new value into the summary information

**Specified by:** accept

in interface

IntConsumer
**Parameters:** value

- the input value

---

#### accept

public void accept​(int value)

Records a new value into the summary information

combine

```java
public void combine​(
IntSummaryStatistics
other)
```

Combines the state of another

IntSummaryStatistics

into this one.

**Parameters:** other

- another

IntSummaryStatistics
**Throws:** NullPointerException

- if

other

is null

---

#### combine

public void combine​(

IntSummaryStatistics

other)

Combines the state of another

IntSummaryStatistics

into this one.

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
public final int getMin()
```

Returns the minimum value recorded, or

Integer.MAX_VALUE

if no
values have been recorded.

**Returns:** the minimum value, or

Integer.MAX_VALUE

if none

---

#### getMin

public final int getMin()

Returns the minimum value recorded, or

Integer.MAX_VALUE

if no
values have been recorded.

getMax

```java
public final int getMax()
```

Returns the maximum value recorded, or

Integer.MIN_VALUE

if no
values have been recorded.

**Returns:** the maximum value, or

Integer.MIN_VALUE

if none

---

#### getMax

public final int getMax()

Returns the maximum value recorded, or

Integer.MIN_VALUE

if no
values have been recorded.

getAverage

```java
public final double getAverage()
```

Returns the arithmetic mean of values recorded, or zero if no values have been
recorded.

**Returns:** the arithmetic mean of values, or zero if none

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

