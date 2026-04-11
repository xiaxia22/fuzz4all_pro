# Class DoubleAdder

**Source:** `java.base\java\util\concurrent\atomic\DoubleAdder.html`

### Class Description

```java
public class
DoubleAdder

extends
Number

implements
Serializable
```

One or more variables that together maintain an initially zero

double

sum. When updates (method

add(double)

) are
contended across threads, the set of variables may grow dynamically
to reduce contention. Method

sum()

(or, equivalently

doubleValue()

) returns the current total combined across the
variables maintaining the sum. The order of accumulation within or
across threads is not guaranteed. Thus, this class may not be
applicable if numerical stability is required, especially when
combining values of substantially different orders of magnitude.

This class is usually preferable to alternatives when multiple
threads update a common value that is used for purposes such as
summary statistics that are frequently updated but less frequently
read.

This class extends

Number

, but does

not

define
methods such as

equals

,

hashCode

and

compareTo

because instances are expected to be mutated, and so are
not useful as collection keys.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DoubleAdder()

Creates a new adder with initial sum of zero.

---

### Method Details

#### public void add​(double x)

Adds the given value.

**Parameters:**
- x

- the value to add

---

#### public double sum()

Returns the current sum. The returned value is

NOT

an
atomic snapshot; invocation in the absence of concurrent
updates returns an accurate result, but concurrent updates that
occur while the sum is being calculated might not be
incorporated. Also, because floating-point arithmetic is not
strictly associative, the returned result need not be identical
to the value that would be obtained in a sequential series of
updates to a single variable.

**Returns:**
- the sum

---

#### public void reset()

Resets variables maintaining the sum to zero. This method may
be a useful alternative to creating a new adder, but is only
effective if there are no concurrent updates. Because this
method is intrinsically racy, it should only be used when it is
known that no threads are concurrently updating.

---

#### public double sumThenReset()

Equivalent in effect to

sum()

followed by

reset()

. This method may apply for example during quiescent
points between multithreaded computations. If there are
updates concurrent with this method, the returned value is

not

guaranteed to be the final value occurring before
the reset.

**Returns:**
- the sum

---

#### public
String
toString()

Returns the String representation of the

sum()

.

**Overrides:**
- toString

in class

Object

**Returns:**
- the String representation of the

sum()

---

#### public double doubleValue()

Equivalent to

sum()

.

**Specified by:**
- doubleValue

in class

Number

**Returns:**
- the sum

---

#### public long longValue()

Returns the

sum()

as a

long

after a
narrowing primitive conversion.

**Specified by:**
- longValue

in class

Number

**Returns:**
- the numeric value represented by this object after conversion
to type

long

.

---

#### public int intValue()

Returns the

sum()

as an

int

after a
narrowing primitive conversion.

**Specified by:**
- intValue

in class

Number

**Returns:**
- the numeric value represented by this object after conversion
to type

int

.

---

#### public float floatValue()

Returns the

sum()

as a

float

after a narrowing primitive conversion.

**Specified by:**
- floatValue

in class

Number

**Returns:**
- the numeric value represented by this object after conversion
to type

float

.

---

### Additional Sections

#### Class DoubleAdder

java.lang.Object

- java.lang.Number
- - java.util.concurrent.atomic.DoubleAdder

java.lang.Number

- java.util.concurrent.atomic.DoubleAdder

java.util.concurrent.atomic.DoubleAdder

**All Implemented Interfaces:** Serializable

```java
public class
DoubleAdder

extends
Number

implements
Serializable
```

One or more variables that together maintain an initially zero

double

sum. When updates (method

add(double)

) are
contended across threads, the set of variables may grow dynamically
to reduce contention. Method

sum()

(or, equivalently

doubleValue()

) returns the current total combined across the
variables maintaining the sum. The order of accumulation within or
across threads is not guaranteed. Thus, this class may not be
applicable if numerical stability is required, especially when
combining values of substantially different orders of magnitude.

This class is usually preferable to alternatives when multiple
threads update a common value that is used for purposes such as
summary statistics that are frequently updated but less frequently
read.

This class extends

Number

, but does

not

define
methods such as

equals

,

hashCode

and

compareTo

because instances are expected to be mutated, and so are
not useful as collection keys.

**Since:** 1.8
**See Also:** Serialized Form

public class

DoubleAdder

extends

Number

implements

Serializable

One or more variables that together maintain an initially zero

double

sum. When updates (method

add(double)

) are
contended across threads, the set of variables may grow dynamically
to reduce contention. Method

sum()

(or, equivalently

doubleValue()

) returns the current total combined across the
variables maintaining the sum. The order of accumulation within or
across threads is not guaranteed. Thus, this class may not be
applicable if numerical stability is required, especially when
combining values of substantially different orders of magnitude.

This class is usually preferable to alternatives when multiple
threads update a common value that is used for purposes such as
summary statistics that are frequently updated but less frequently
read.

This class extends

Number

, but does

not

define
methods such as

equals

,

hashCode

and

compareTo

because instances are expected to be mutated, and so are
not useful as collection keys.

This class is usually preferable to alternatives when multiple
threads update a common value that is used for purposes such as
summary statistics that are frequently updated but less frequently
read.

This class extends

Number

, but does

not

define
methods such as

equals

,

hashCode

and

compareTo

because instances are expected to be mutated, and so are
not useful as collection keys.

This class extends

Number

, but does

not

define
methods such as

equals

,

hashCode

and

compareTo

because instances are expected to be mutated, and so are
not useful as collection keys.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DoubleAdder

()

Creates a new adder with initial sum of zero.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(double x)

Adds the given value.

double

doubleValue

()

Equivalent to

sum()

.

float

floatValue

()

Returns the

sum()

as a

float

after a narrowing primitive conversion.

int

intValue

()

Returns the

sum()

as an

int

after a
narrowing primitive conversion.

long

longValue

()

Returns the

sum()

as a

long

after a
narrowing primitive conversion.

void

reset

()

Resets variables maintaining the sum to zero.

double

sum

()

Returns the current sum.

double

sumThenReset

()

Equivalent in effect to

sum()

followed by

reset()

.

String

toString

()

Returns the String representation of the

sum()

.

- Methods declared in class java.lang.

Number

byteValue

,

shortValue

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

Constructor Summary

Constructors

Constructor

Description

DoubleAdder

()

Creates a new adder with initial sum of zero.

---

#### Constructor Summary

Creates a new adder with initial sum of zero.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(double x)

Adds the given value.

double

doubleValue

()

Equivalent to

sum()

.

float

floatValue

()

Returns the

sum()

as a

float

after a narrowing primitive conversion.

int

intValue

()

Returns the

sum()

as an

int

after a
narrowing primitive conversion.

long

longValue

()

Returns the

sum()

as a

long

after a
narrowing primitive conversion.

void

reset

()

Resets variables maintaining the sum to zero.

double

sum

()

Returns the current sum.

double

sumThenReset

()

Equivalent in effect to

sum()

followed by

reset()

.

String

toString

()

Returns the String representation of the

sum()

.

- Methods declared in class java.lang.

Number

byteValue

,

shortValue

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

---

#### Method Summary

Adds the given value.

Equivalent to

sum()

.

Returns the

sum()

as a

float

after a narrowing primitive conversion.

Returns the

sum()

as an

int

after a
narrowing primitive conversion.

Returns the

sum()

as a

long

after a
narrowing primitive conversion.

Resets variables maintaining the sum to zero.

Returns the current sum.

Equivalent in effect to

sum()

followed by

reset()

.

Returns the String representation of the

sum()

.

Methods declared in class java.lang.

Number

byteValue

,

shortValue

---

#### Methods declared in class java.lang. Number

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DoubleAdder

```java
public DoubleAdder()
```

Creates a new adder with initial sum of zero.

============ METHOD DETAIL ==========

- Method Detail

- add

```java
public void add​(double x)
```

Adds the given value.

**Parameters:** x

- the value to add

- sum

```java
public double sum()
```

Returns the current sum. The returned value is

NOT

an
atomic snapshot; invocation in the absence of concurrent
updates returns an accurate result, but concurrent updates that
occur while the sum is being calculated might not be
incorporated. Also, because floating-point arithmetic is not
strictly associative, the returned result need not be identical
to the value that would be obtained in a sequential series of
updates to a single variable.

**Returns:** the sum

- reset

```java
public void reset()
```

Resets variables maintaining the sum to zero. This method may
be a useful alternative to creating a new adder, but is only
effective if there are no concurrent updates. Because this
method is intrinsically racy, it should only be used when it is
known that no threads are concurrently updating.

- sumThenReset

```java
public double sumThenReset()
```

Equivalent in effect to

sum()

followed by

reset()

. This method may apply for example during quiescent
points between multithreaded computations. If there are
updates concurrent with this method, the returned value is

not

guaranteed to be the final value occurring before
the reset.

**Returns:** the sum

- toString

```java
public
String
toString()
```

Returns the String representation of the

sum()

.

**Overrides:** toString

in class

Object
**Returns:** the String representation of the

sum()

- doubleValue

```java
public double doubleValue()
```

Equivalent to

sum()

.

**Specified by:** doubleValue

in class

Number
**Returns:** the sum

- longValue

```java
public long longValue()
```

Returns the

sum()

as a

long

after a
narrowing primitive conversion.

**Specified by:** longValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

long

.

- intValue

```java
public int intValue()
```

Returns the

sum()

as an

int

after a
narrowing primitive conversion.

**Specified by:** intValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

int

.

- floatValue

```java
public float floatValue()
```

Returns the

sum()

as a

float

after a narrowing primitive conversion.

**Specified by:** floatValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

float

.

Constructor Detail

- DoubleAdder

```java
public DoubleAdder()
```

Creates a new adder with initial sum of zero.

---

#### Constructor Detail

DoubleAdder

```java
public DoubleAdder()
```

Creates a new adder with initial sum of zero.

---

#### DoubleAdder

public DoubleAdder()

Creates a new adder with initial sum of zero.

Method Detail

- add

```java
public void add​(double x)
```

Adds the given value.

**Parameters:** x

- the value to add

- sum

```java
public double sum()
```

Returns the current sum. The returned value is

NOT

an
atomic snapshot; invocation in the absence of concurrent
updates returns an accurate result, but concurrent updates that
occur while the sum is being calculated might not be
incorporated. Also, because floating-point arithmetic is not
strictly associative, the returned result need not be identical
to the value that would be obtained in a sequential series of
updates to a single variable.

**Returns:** the sum

- reset

```java
public void reset()
```

Resets variables maintaining the sum to zero. This method may
be a useful alternative to creating a new adder, but is only
effective if there are no concurrent updates. Because this
method is intrinsically racy, it should only be used when it is
known that no threads are concurrently updating.

- sumThenReset

```java
public double sumThenReset()
```

Equivalent in effect to

sum()

followed by

reset()

. This method may apply for example during quiescent
points between multithreaded computations. If there are
updates concurrent with this method, the returned value is

not

guaranteed to be the final value occurring before
the reset.

**Returns:** the sum

- toString

```java
public
String
toString()
```

Returns the String representation of the

sum()

.

**Overrides:** toString

in class

Object
**Returns:** the String representation of the

sum()

- doubleValue

```java
public double doubleValue()
```

Equivalent to

sum()

.

**Specified by:** doubleValue

in class

Number
**Returns:** the sum

- longValue

```java
public long longValue()
```

Returns the

sum()

as a

long

after a
narrowing primitive conversion.

**Specified by:** longValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

long

.

- intValue

```java
public int intValue()
```

Returns the

sum()

as an

int

after a
narrowing primitive conversion.

**Specified by:** intValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

int

.

- floatValue

```java
public float floatValue()
```

Returns the

sum()

as a

float

after a narrowing primitive conversion.

**Specified by:** floatValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

float

.

---

#### Method Detail

add

```java
public void add​(double x)
```

Adds the given value.

**Parameters:** x

- the value to add

---

#### add

public void add​(double x)

Adds the given value.

sum

```java
public double sum()
```

Returns the current sum. The returned value is

NOT

an
atomic snapshot; invocation in the absence of concurrent
updates returns an accurate result, but concurrent updates that
occur while the sum is being calculated might not be
incorporated. Also, because floating-point arithmetic is not
strictly associative, the returned result need not be identical
to the value that would be obtained in a sequential series of
updates to a single variable.

**Returns:** the sum

---

#### sum

public double sum()

Returns the current sum. The returned value is

NOT

an
atomic snapshot; invocation in the absence of concurrent
updates returns an accurate result, but concurrent updates that
occur while the sum is being calculated might not be
incorporated. Also, because floating-point arithmetic is not
strictly associative, the returned result need not be identical
to the value that would be obtained in a sequential series of
updates to a single variable.

reset

```java
public void reset()
```

Resets variables maintaining the sum to zero. This method may
be a useful alternative to creating a new adder, but is only
effective if there are no concurrent updates. Because this
method is intrinsically racy, it should only be used when it is
known that no threads are concurrently updating.

---

#### reset

public void reset()

Resets variables maintaining the sum to zero. This method may
be a useful alternative to creating a new adder, but is only
effective if there are no concurrent updates. Because this
method is intrinsically racy, it should only be used when it is
known that no threads are concurrently updating.

sumThenReset

```java
public double sumThenReset()
```

Equivalent in effect to

sum()

followed by

reset()

. This method may apply for example during quiescent
points between multithreaded computations. If there are
updates concurrent with this method, the returned value is

not

guaranteed to be the final value occurring before
the reset.

**Returns:** the sum

---

#### sumThenReset

public double sumThenReset()

Equivalent in effect to

sum()

followed by

reset()

. This method may apply for example during quiescent
points between multithreaded computations. If there are
updates concurrent with this method, the returned value is

not

guaranteed to be the final value occurring before
the reset.

toString

```java
public
String
toString()
```

Returns the String representation of the

sum()

.

**Overrides:** toString

in class

Object
**Returns:** the String representation of the

sum()

---

#### toString

public

String

toString()

Returns the String representation of the

sum()

.

doubleValue

```java
public double doubleValue()
```

Equivalent to

sum()

.

**Specified by:** doubleValue

in class

Number
**Returns:** the sum

---

#### doubleValue

public double doubleValue()

Equivalent to

sum()

.

longValue

```java
public long longValue()
```

Returns the

sum()

as a

long

after a
narrowing primitive conversion.

**Specified by:** longValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

long

.

---

#### longValue

public long longValue()

Returns the

sum()

as a

long

after a
narrowing primitive conversion.

intValue

```java
public int intValue()
```

Returns the

sum()

as an

int

after a
narrowing primitive conversion.

**Specified by:** intValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

int

.

---

#### intValue

public int intValue()

Returns the

sum()

as an

int

after a
narrowing primitive conversion.

floatValue

```java
public float floatValue()
```

Returns the

sum()

as a

float

after a narrowing primitive conversion.

**Specified by:** floatValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

float

.

---

#### floatValue

public float floatValue()

Returns the

sum()

as a

float

after a narrowing primitive conversion.

---

