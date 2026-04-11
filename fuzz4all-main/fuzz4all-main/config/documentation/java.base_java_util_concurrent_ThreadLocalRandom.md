# Class ThreadLocalRandom

**Source:** `java.base\java\util\concurrent\ThreadLocalRandom.html`

### Class Description

```java
public class
ThreadLocalRandom

extends
Random
```

A random number generator isolated to the current thread. Like the
global

Random

generator used by the

Math

class, a

ThreadLocalRandom

is initialized
with an internally generated seed that may not otherwise be
modified. When applicable, use of

ThreadLocalRandom

rather
than shared

Random

objects in concurrent programs will
typically encounter much less overhead and contention. Use of

ThreadLocalRandom

is particularly appropriate when multiple
tasks (for example, each a

ForkJoinTask

) use random numbers
in parallel in thread pools.

Usages of this class should typically be of the form:

ThreadLocalRandom.current().nextX(...)

(where

X

is

Int

,

Long

, etc).
When all usages are of this form, it is never possible to
accidentally share a

ThreadLocalRandom

across multiple threads.

This class also provides additional commonly used bounded random
generation methods.

Instances of

ThreadLocalRandom

are not cryptographically
secure. Consider instead using

SecureRandom

in security-sensitive applications. Additionally,
default-constructed instances do not use a cryptographically random
seed unless the

system property

java.util.secureRandomSeed

is set to

true

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ThreadLocalRandom
current()

Returns the current thread's

ThreadLocalRandom

.

**Returns:**
- the current thread's

ThreadLocalRandom

---

#### public void setSeed​(long seed)

Throws

UnsupportedOperationException

. Setting seeds in
this generator is not supported.

**Overrides:**
- setSeed

in class

Random

**Parameters:**
- seed

- the initial seed

**Throws:**
- UnsupportedOperationException

- always

---

#### protected int next​(int bits)

Generates a pseudorandom number with the indicated number of
low-order bits. Because this class has no subclasses, this
method cannot be invoked or overridden.

**Overrides:**
- next

in class

Random

**Parameters:**
- bits

- random bits

**Returns:**
- the next pseudorandom value from this random number
generator's sequence

---

#### public int nextInt()

Returns a pseudorandom

int

value.

**Overrides:**
- nextInt

in class

Random

**Returns:**
- a pseudorandom

int

value

---

#### public int nextInt​(int bound)

Returns a pseudorandom

int

value between zero (inclusive)
and the specified bound (exclusive).

**Overrides:**
- nextInt

in class

Random

**Parameters:**
- bound

- the upper bound (exclusive). Must be positive.

**Returns:**
- a pseudorandom

int

value between zero
(inclusive) and the bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

bound

is not positive

---

#### public int nextInt​(int origin,
int bound)

Returns a pseudorandom

int

value between the specified
origin (inclusive) and the specified bound (exclusive).

**Parameters:**
- origin

- the least value returned
- bound

- the upper bound (exclusive)

**Returns:**
- a pseudorandom

int

value between the origin
(inclusive) and the bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

origin

is greater than
or equal to

bound

---

#### public long nextLong()

Returns a pseudorandom

long

value.

**Overrides:**
- nextLong

in class

Random

**Returns:**
- a pseudorandom

long

value

---

#### public long nextLong​(long bound)

Returns a pseudorandom

long

value between zero (inclusive)
and the specified bound (exclusive).

**Parameters:**
- bound

- the upper bound (exclusive). Must be positive.

**Returns:**
- a pseudorandom

long

value between zero
(inclusive) and the bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

bound

is not positive

---

#### public long nextLong​(long origin,
long bound)

Returns a pseudorandom

long

value between the specified
origin (inclusive) and the specified bound (exclusive).

**Parameters:**
- origin

- the least value returned
- bound

- the upper bound (exclusive)

**Returns:**
- a pseudorandom

long

value between the origin
(inclusive) and the bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

origin

is greater than
or equal to

bound

---

#### public double nextDouble()

Returns a pseudorandom

double

value between zero
(inclusive) and one (exclusive).

**Overrides:**
- nextDouble

in class

Random

**Returns:**
- a pseudorandom

double

value between zero
(inclusive) and one (exclusive)

**See Also:**
- Math.random()

---

#### public double nextDouble​(double bound)

Returns a pseudorandom

double

value between 0.0
(inclusive) and the specified bound (exclusive).

**Parameters:**
- bound

- the upper bound (exclusive). Must be positive.

**Returns:**
- a pseudorandom

double

value between zero
(inclusive) and the bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

bound

is not positive

---

#### public double nextDouble​(double origin,
double bound)

Returns a pseudorandom

double

value between the specified
origin (inclusive) and bound (exclusive).

**Parameters:**
- origin

- the least value returned
- bound

- the upper bound (exclusive)

**Returns:**
- a pseudorandom

double

value between the origin
(inclusive) and the bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

origin

is greater than
or equal to

bound

---

#### public boolean nextBoolean()

Returns a pseudorandom

boolean

value.

**Overrides:**
- nextBoolean

in class

Random

**Returns:**
- a pseudorandom

boolean

value

---

#### public float nextFloat()

Returns a pseudorandom

float

value between zero
(inclusive) and one (exclusive).

**Overrides:**
- nextFloat

in class

Random

**Returns:**
- a pseudorandom

float

value between zero
(inclusive) and one (exclusive)

---

#### public
IntStream
ints​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

int

values.

**Overrides:**
- ints

in class

Random

**Parameters:**
- streamSize

- the number of values to generate

**Returns:**
- a stream of pseudorandom

int

values

**Throws:**
- IllegalArgumentException

- if

streamSize

is
less than zero

**Since:**
- 1.8

---

#### public
IntStream
ints()

Returns an effectively unlimited stream of pseudorandom

int

values.

**Overrides:**
- ints

in class

Random

**Returns:**
- a stream of pseudorandom

int

values

**Since:**
- 1.8

**Implementation Note:**
- This method is implemented to be equivalent to

ints(Long.MAX_VALUE)

.

---

#### public
IntStream
ints​(long streamSize,
int randomNumberOrigin,
int randomNumberBound)

Returns a stream producing the given

streamSize

number
of pseudorandom

int

values, each conforming to the given
origin (inclusive) and bound (exclusive).

**Overrides:**
- ints

in class

Random

**Parameters:**
- streamSize

- the number of values to generate
- randomNumberOrigin

- the origin (inclusive) of each random value
- randomNumberBound

- the bound (exclusive) of each random value

**Returns:**
- a stream of pseudorandom

int

values,
each with the given origin (inclusive) and bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound

**Since:**
- 1.8

---

#### public
IntStream
ints​(int randomNumberOrigin,
int randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

int

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:**
- ints

in class

Random

**Parameters:**
- randomNumberOrigin

- the origin (inclusive) of each random value
- randomNumberBound

- the bound (exclusive) of each random value

**Returns:**
- a stream of pseudorandom

int

values,
each with the given origin (inclusive) and bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound

**Since:**
- 1.8

**Implementation Note:**
- This method is implemented to be equivalent to

ints(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.

---

#### public
LongStream
longs​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

long

values.

**Overrides:**
- longs

in class

Random

**Parameters:**
- streamSize

- the number of values to generate

**Returns:**
- a stream of pseudorandom

long

values

**Throws:**
- IllegalArgumentException

- if

streamSize

is
less than zero

**Since:**
- 1.8

---

#### public
LongStream
longs()

Returns an effectively unlimited stream of pseudorandom

long

values.

**Overrides:**
- longs

in class

Random

**Returns:**
- a stream of pseudorandom

long

values

**Since:**
- 1.8

**Implementation Note:**
- This method is implemented to be equivalent to

longs(Long.MAX_VALUE)

.

---

#### public
LongStream
longs​(long streamSize,
long randomNumberOrigin,
long randomNumberBound)

Returns a stream producing the given

streamSize

number of
pseudorandom

long

, each conforming to the given origin
(inclusive) and bound (exclusive).

**Overrides:**
- longs

in class

Random

**Parameters:**
- streamSize

- the number of values to generate
- randomNumberOrigin

- the origin (inclusive) of each random value
- randomNumberBound

- the bound (exclusive) of each random value

**Returns:**
- a stream of pseudorandom

long

values,
each with the given origin (inclusive) and bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound

**Since:**
- 1.8

---

#### public
LongStream
longs​(long randomNumberOrigin,
long randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

long

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:**
- longs

in class

Random

**Parameters:**
- randomNumberOrigin

- the origin (inclusive) of each random value
- randomNumberBound

- the bound (exclusive) of each random value

**Returns:**
- a stream of pseudorandom

long

values,
each with the given origin (inclusive) and bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound

**Since:**
- 1.8

**Implementation Note:**
- This method is implemented to be equivalent to

longs(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.

---

#### public
DoubleStream
doubles​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each between zero
(inclusive) and one (exclusive).

**Overrides:**
- doubles

in class

Random

**Parameters:**
- streamSize

- the number of values to generate

**Returns:**
- a stream of

double

values

**Throws:**
- IllegalArgumentException

- if

streamSize

is
less than zero

**Since:**
- 1.8

---

#### public
DoubleStream
doubles()

Returns an effectively unlimited stream of pseudorandom

double

values, each between zero (inclusive) and one
(exclusive).

**Overrides:**
- doubles

in class

Random

**Returns:**
- a stream of pseudorandom

double

values

**Since:**
- 1.8

**Implementation Note:**
- This method is implemented to be equivalent to

doubles(Long.MAX_VALUE)

.

---

#### public
DoubleStream
doubles​(long streamSize,
double randomNumberOrigin,
double randomNumberBound)

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each conforming to the given origin
(inclusive) and bound (exclusive).

**Overrides:**
- doubles

in class

Random

**Parameters:**
- streamSize

- the number of values to generate
- randomNumberOrigin

- the origin (inclusive) of each random value
- randomNumberBound

- the bound (exclusive) of each random value

**Returns:**
- a stream of pseudorandom

double

values,
each with the given origin (inclusive) and bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound

**Since:**
- 1.8

---

#### public
DoubleStream
doubles​(double randomNumberOrigin,
double randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

double

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:**
- doubles

in class

Random

**Parameters:**
- randomNumberOrigin

- the origin (inclusive) of each random value
- randomNumberBound

- the bound (exclusive) of each random value

**Returns:**
- a stream of pseudorandom

double

values,
each with the given origin (inclusive) and bound (exclusive)

**Throws:**
- IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound

**Since:**
- 1.8

**Implementation Note:**
- This method is implemented to be equivalent to

doubles(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.

---

### Additional Sections

#### Class ThreadLocalRandom

java.lang.Object

- java.util.Random
- - java.util.concurrent.ThreadLocalRandom

java.util.Random

- java.util.concurrent.ThreadLocalRandom

java.util.concurrent.ThreadLocalRandom

**All Implemented Interfaces:** Serializable

```java
public class
ThreadLocalRandom

extends
Random
```

A random number generator isolated to the current thread. Like the
global

Random

generator used by the

Math

class, a

ThreadLocalRandom

is initialized
with an internally generated seed that may not otherwise be
modified. When applicable, use of

ThreadLocalRandom

rather
than shared

Random

objects in concurrent programs will
typically encounter much less overhead and contention. Use of

ThreadLocalRandom

is particularly appropriate when multiple
tasks (for example, each a

ForkJoinTask

) use random numbers
in parallel in thread pools.

Usages of this class should typically be of the form:

ThreadLocalRandom.current().nextX(...)

(where

X

is

Int

,

Long

, etc).
When all usages are of this form, it is never possible to
accidentally share a

ThreadLocalRandom

across multiple threads.

This class also provides additional commonly used bounded random
generation methods.

Instances of

ThreadLocalRandom

are not cryptographically
secure. Consider instead using

SecureRandom

in security-sensitive applications. Additionally,
default-constructed instances do not use a cryptographically random
seed unless the

system property

java.util.secureRandomSeed

is set to

true

.

**Since:** 1.7
**See Also:** Serialized Form

public class

ThreadLocalRandom

extends

Random

A random number generator isolated to the current thread. Like the
global

Random

generator used by the

Math

class, a

ThreadLocalRandom

is initialized
with an internally generated seed that may not otherwise be
modified. When applicable, use of

ThreadLocalRandom

rather
than shared

Random

objects in concurrent programs will
typically encounter much less overhead and contention. Use of

ThreadLocalRandom

is particularly appropriate when multiple
tasks (for example, each a

ForkJoinTask

) use random numbers
in parallel in thread pools.

Usages of this class should typically be of the form:

ThreadLocalRandom.current().nextX(...)

(where

X

is

Int

,

Long

, etc).
When all usages are of this form, it is never possible to
accidentally share a

ThreadLocalRandom

across multiple threads.

This class also provides additional commonly used bounded random
generation methods.

Instances of

ThreadLocalRandom

are not cryptographically
secure. Consider instead using

SecureRandom

in security-sensitive applications. Additionally,
default-constructed instances do not use a cryptographically random
seed unless the

system property

java.util.secureRandomSeed

is set to

true

.

Usages of this class should typically be of the form:

ThreadLocalRandom.current().nextX(...)

(where

X

is

Int

,

Long

, etc).
When all usages are of this form, it is never possible to
accidentally share a

ThreadLocalRandom

across multiple threads.

This class also provides additional commonly used bounded random
generation methods.

Instances of

ThreadLocalRandom

are not cryptographically
secure. Consider instead using

SecureRandom

in security-sensitive applications. Additionally,
default-constructed instances do not use a cryptographically random
seed unless the

system property

java.util.secureRandomSeed

is set to

true

.

This class also provides additional commonly used bounded random
generation methods.

Instances of

ThreadLocalRandom

are not cryptographically
secure. Consider instead using

SecureRandom

in security-sensitive applications. Additionally,
default-constructed instances do not use a cryptographically random
seed unless the

system property

java.util.secureRandomSeed

is set to

true

.

Instances of

ThreadLocalRandom

are not cryptographically
secure. Consider instead using

SecureRandom

in security-sensitive applications. Additionally,
default-constructed instances do not use a cryptographically random
seed unless the

system property

java.util.secureRandomSeed

is set to

true

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

static

ThreadLocalRandom

current

()

Returns the current thread's

ThreadLocalRandom

.

DoubleStream

doubles

()

Returns an effectively unlimited stream of pseudorandom

double

values, each between zero (inclusive) and one
(exclusive).

DoubleStream

doubles

​(double randomNumberOrigin,
double randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

double

values, each conforming to the given origin (inclusive) and bound
(exclusive).

DoubleStream

doubles

​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each between zero
(inclusive) and one (exclusive).

DoubleStream

doubles

​(long streamSize,
double randomNumberOrigin,
double randomNumberBound)

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each conforming to the given origin
(inclusive) and bound (exclusive).

IntStream

ints

()

Returns an effectively unlimited stream of pseudorandom

int

values.

IntStream

ints

​(int randomNumberOrigin,
int randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

int

values, each conforming to the given origin (inclusive) and bound
(exclusive).

IntStream

ints

​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

int

values.

IntStream

ints

​(long streamSize,
int randomNumberOrigin,
int randomNumberBound)

Returns a stream producing the given

streamSize

number
of pseudorandom

int

values, each conforming to the given
origin (inclusive) and bound (exclusive).

LongStream

longs

()

Returns an effectively unlimited stream of pseudorandom

long

values.

LongStream

longs

​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

long

values.

LongStream

longs

​(long randomNumberOrigin,
long randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

long

values, each conforming to the given origin (inclusive) and bound
(exclusive).

LongStream

longs

​(long streamSize,
long randomNumberOrigin,
long randomNumberBound)

Returns a stream producing the given

streamSize

number of
pseudorandom

long

, each conforming to the given origin
(inclusive) and bound (exclusive).

protected int

next

​(int bits)

Generates a pseudorandom number with the indicated number of
low-order bits.

boolean

nextBoolean

()

Returns a pseudorandom

boolean

value.

double

nextDouble

()

Returns a pseudorandom

double

value between zero
(inclusive) and one (exclusive).

double

nextDouble

​(double bound)

Returns a pseudorandom

double

value between 0.0
(inclusive) and the specified bound (exclusive).

double

nextDouble

​(double origin,
double bound)

Returns a pseudorandom

double

value between the specified
origin (inclusive) and bound (exclusive).

float

nextFloat

()

Returns a pseudorandom

float

value between zero
(inclusive) and one (exclusive).

int

nextInt

()

Returns a pseudorandom

int

value.

int

nextInt

​(int bound)

Returns a pseudorandom

int

value between zero (inclusive)
and the specified bound (exclusive).

int

nextInt

​(int origin,
int bound)

Returns a pseudorandom

int

value between the specified
origin (inclusive) and the specified bound (exclusive).

long

nextLong

()

Returns a pseudorandom

long

value.

long

nextLong

​(long bound)

Returns a pseudorandom

long

value between zero (inclusive)
and the specified bound (exclusive).

long

nextLong

​(long origin,
long bound)

Returns a pseudorandom

long

value between the specified
origin (inclusive) and the specified bound (exclusive).

void

setSeed

​(long seed)

Throws

UnsupportedOperationException

.

- Methods declared in class java.util.

Random

nextBytes

,

nextGaussian

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

ThreadLocalRandom

current

()

Returns the current thread's

ThreadLocalRandom

.

DoubleStream

doubles

()

Returns an effectively unlimited stream of pseudorandom

double

values, each between zero (inclusive) and one
(exclusive).

DoubleStream

doubles

​(double randomNumberOrigin,
double randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

double

values, each conforming to the given origin (inclusive) and bound
(exclusive).

DoubleStream

doubles

​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each between zero
(inclusive) and one (exclusive).

DoubleStream

doubles

​(long streamSize,
double randomNumberOrigin,
double randomNumberBound)

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each conforming to the given origin
(inclusive) and bound (exclusive).

IntStream

ints

()

Returns an effectively unlimited stream of pseudorandom

int

values.

IntStream

ints

​(int randomNumberOrigin,
int randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

int

values, each conforming to the given origin (inclusive) and bound
(exclusive).

IntStream

ints

​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

int

values.

IntStream

ints

​(long streamSize,
int randomNumberOrigin,
int randomNumberBound)

Returns a stream producing the given

streamSize

number
of pseudorandom

int

values, each conforming to the given
origin (inclusive) and bound (exclusive).

LongStream

longs

()

Returns an effectively unlimited stream of pseudorandom

long

values.

LongStream

longs

​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

long

values.

LongStream

longs

​(long randomNumberOrigin,
long randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

long

values, each conforming to the given origin (inclusive) and bound
(exclusive).

LongStream

longs

​(long streamSize,
long randomNumberOrigin,
long randomNumberBound)

Returns a stream producing the given

streamSize

number of
pseudorandom

long

, each conforming to the given origin
(inclusive) and bound (exclusive).

protected int

next

​(int bits)

Generates a pseudorandom number with the indicated number of
low-order bits.

boolean

nextBoolean

()

Returns a pseudorandom

boolean

value.

double

nextDouble

()

Returns a pseudorandom

double

value between zero
(inclusive) and one (exclusive).

double

nextDouble

​(double bound)

Returns a pseudorandom

double

value between 0.0
(inclusive) and the specified bound (exclusive).

double

nextDouble

​(double origin,
double bound)

Returns a pseudorandom

double

value between the specified
origin (inclusive) and bound (exclusive).

float

nextFloat

()

Returns a pseudorandom

float

value between zero
(inclusive) and one (exclusive).

int

nextInt

()

Returns a pseudorandom

int

value.

int

nextInt

​(int bound)

Returns a pseudorandom

int

value between zero (inclusive)
and the specified bound (exclusive).

int

nextInt

​(int origin,
int bound)

Returns a pseudorandom

int

value between the specified
origin (inclusive) and the specified bound (exclusive).

long

nextLong

()

Returns a pseudorandom

long

value.

long

nextLong

​(long bound)

Returns a pseudorandom

long

value between zero (inclusive)
and the specified bound (exclusive).

long

nextLong

​(long origin,
long bound)

Returns a pseudorandom

long

value between the specified
origin (inclusive) and the specified bound (exclusive).

void

setSeed

​(long seed)

Throws

UnsupportedOperationException

.

- Methods declared in class java.util.

Random

nextBytes

,

nextGaussian

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

Returns the current thread's

ThreadLocalRandom

.

Returns an effectively unlimited stream of pseudorandom

double

values, each between zero (inclusive) and one
(exclusive).

Returns an effectively unlimited stream of pseudorandom

double

values, each conforming to the given origin (inclusive) and bound
(exclusive).

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each between zero
(inclusive) and one (exclusive).

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each conforming to the given origin
(inclusive) and bound (exclusive).

Returns an effectively unlimited stream of pseudorandom

int

values.

Returns an effectively unlimited stream of pseudorandom

int

values, each conforming to the given origin (inclusive) and bound
(exclusive).

Returns a stream producing the given

streamSize

number of
pseudorandom

int

values.

Returns a stream producing the given

streamSize

number
of pseudorandom

int

values, each conforming to the given
origin (inclusive) and bound (exclusive).

Returns an effectively unlimited stream of pseudorandom

long

values.

Returns a stream producing the given

streamSize

number of
pseudorandom

long

values.

Returns an effectively unlimited stream of pseudorandom

long

values, each conforming to the given origin (inclusive) and bound
(exclusive).

Returns a stream producing the given

streamSize

number of
pseudorandom

long

, each conforming to the given origin
(inclusive) and bound (exclusive).

Generates a pseudorandom number with the indicated number of
low-order bits.

Returns a pseudorandom

boolean

value.

Returns a pseudorandom

double

value between zero
(inclusive) and one (exclusive).

Returns a pseudorandom

double

value between 0.0
(inclusive) and the specified bound (exclusive).

Returns a pseudorandom

double

value between the specified
origin (inclusive) and bound (exclusive).

Returns a pseudorandom

float

value between zero
(inclusive) and one (exclusive).

Returns a pseudorandom

int

value.

Returns a pseudorandom

int

value between zero (inclusive)
and the specified bound (exclusive).

Returns a pseudorandom

int

value between the specified
origin (inclusive) and the specified bound (exclusive).

Returns a pseudorandom

long

value.

Returns a pseudorandom

long

value between zero (inclusive)
and the specified bound (exclusive).

Returns a pseudorandom

long

value between the specified
origin (inclusive) and the specified bound (exclusive).

Throws

UnsupportedOperationException

.

Methods declared in class java.util.

Random

nextBytes

,

nextGaussian

---

#### Methods declared in class java.util. Random

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

============ METHOD DETAIL ==========

- Method Detail

- current

```java
public static
ThreadLocalRandom
current()
```

Returns the current thread's

ThreadLocalRandom

.

**Returns:** the current thread's

ThreadLocalRandom

- setSeed

```java
public void setSeed​(long seed)
```

Throws

UnsupportedOperationException

. Setting seeds in
this generator is not supported.

**Overrides:** setSeed

in class

Random
**Parameters:** seed

- the initial seed
**Throws:** UnsupportedOperationException

- always

- next

```java
protected int next​(int bits)
```

Generates a pseudorandom number with the indicated number of
low-order bits. Because this class has no subclasses, this
method cannot be invoked or overridden.

**Overrides:** next

in class

Random
**Parameters:** bits

- random bits
**Returns:** the next pseudorandom value from this random number
generator's sequence

- nextInt

```java
public int nextInt()
```

Returns a pseudorandom

int

value.

**Overrides:** nextInt

in class

Random
**Returns:** a pseudorandom

int

value

- nextInt

```java
public int nextInt​(int bound)
```

Returns a pseudorandom

int

value between zero (inclusive)
and the specified bound (exclusive).

**Overrides:** nextInt

in class

Random
**Parameters:** bound

- the upper bound (exclusive). Must be positive.
**Returns:** a pseudorandom

int

value between zero
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

bound

is not positive

- nextInt

```java
public int nextInt​(int origin,
int bound)
```

Returns a pseudorandom

int

value between the specified
origin (inclusive) and the specified bound (exclusive).

**Parameters:** origin

- the least value returned
**Parameters:** bound

- the upper bound (exclusive)
**Returns:** a pseudorandom

int

value between the origin
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

origin

is greater than
or equal to

bound

- nextLong

```java
public long nextLong()
```

Returns a pseudorandom

long

value.

**Overrides:** nextLong

in class

Random
**Returns:** a pseudorandom

long

value

- nextLong

```java
public long nextLong​(long bound)
```

Returns a pseudorandom

long

value between zero (inclusive)
and the specified bound (exclusive).

**Parameters:** bound

- the upper bound (exclusive). Must be positive.
**Returns:** a pseudorandom

long

value between zero
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

bound

is not positive

- nextLong

```java
public long nextLong​(long origin,
long bound)
```

Returns a pseudorandom

long

value between the specified
origin (inclusive) and the specified bound (exclusive).

**Parameters:** origin

- the least value returned
**Parameters:** bound

- the upper bound (exclusive)
**Returns:** a pseudorandom

long

value between the origin
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

origin

is greater than
or equal to

bound

- nextDouble

```java
public double nextDouble()
```

Returns a pseudorandom

double

value between zero
(inclusive) and one (exclusive).

**Overrides:** nextDouble

in class

Random
**Returns:** a pseudorandom

double

value between zero
(inclusive) and one (exclusive)
**See Also:** Math.random()

- nextDouble

```java
public double nextDouble​(double bound)
```

Returns a pseudorandom

double

value between 0.0
(inclusive) and the specified bound (exclusive).

**Parameters:** bound

- the upper bound (exclusive). Must be positive.
**Returns:** a pseudorandom

double

value between zero
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

bound

is not positive

- nextDouble

```java
public double nextDouble​(double origin,
double bound)
```

Returns a pseudorandom

double

value between the specified
origin (inclusive) and bound (exclusive).

**Parameters:** origin

- the least value returned
**Parameters:** bound

- the upper bound (exclusive)
**Returns:** a pseudorandom

double

value between the origin
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

origin

is greater than
or equal to

bound

- nextBoolean

```java
public boolean nextBoolean()
```

Returns a pseudorandom

boolean

value.

**Overrides:** nextBoolean

in class

Random
**Returns:** a pseudorandom

boolean

value

- nextFloat

```java
public float nextFloat()
```

Returns a pseudorandom

float

value between zero
(inclusive) and one (exclusive).

**Overrides:** nextFloat

in class

Random
**Returns:** a pseudorandom

float

value between zero
(inclusive) and one (exclusive)

- ints

```java
public
IntStream
ints​(long streamSize)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

int

values.

**Overrides:** ints

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Returns:** a stream of pseudorandom

int

values
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero
**Since:** 1.8

- ints

```java
public
IntStream
ints()
```

Returns an effectively unlimited stream of pseudorandom

int

values.

**Overrides:** ints

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

ints(Long.MAX_VALUE)

.
**Returns:** a stream of pseudorandom

int

values
**Since:** 1.8

- ints

```java
public
IntStream
ints​(long streamSize,
int randomNumberOrigin,
int randomNumberBound)
```

Returns a stream producing the given

streamSize

number
of pseudorandom

int

values, each conforming to the given
origin (inclusive) and bound (exclusive).

**Overrides:** ints

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

int

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- ints

```java
public
IntStream
ints​(int randomNumberOrigin,
int randomNumberBound)
```

Returns an effectively unlimited stream of pseudorandom

int

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:** ints

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

ints(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

int

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- longs

```java
public
LongStream
longs​(long streamSize)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

long

values.

**Overrides:** longs

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Returns:** a stream of pseudorandom

long

values
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero
**Since:** 1.8

- longs

```java
public
LongStream
longs()
```

Returns an effectively unlimited stream of pseudorandom

long

values.

**Overrides:** longs

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

longs(Long.MAX_VALUE)

.
**Returns:** a stream of pseudorandom

long

values
**Since:** 1.8

- longs

```java
public
LongStream
longs​(long streamSize,
long randomNumberOrigin,
long randomNumberBound)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

long

, each conforming to the given origin
(inclusive) and bound (exclusive).

**Overrides:** longs

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

long

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- longs

```java
public
LongStream
longs​(long randomNumberOrigin,
long randomNumberBound)
```

Returns an effectively unlimited stream of pseudorandom

long

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:** longs

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

longs(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

long

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- doubles

```java
public
DoubleStream
doubles​(long streamSize)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each between zero
(inclusive) and one (exclusive).

**Overrides:** doubles

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Returns:** a stream of

double

values
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero
**Since:** 1.8

- doubles

```java
public
DoubleStream
doubles()
```

Returns an effectively unlimited stream of pseudorandom

double

values, each between zero (inclusive) and one
(exclusive).

**Overrides:** doubles

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

doubles(Long.MAX_VALUE)

.
**Returns:** a stream of pseudorandom

double

values
**Since:** 1.8

- doubles

```java
public
DoubleStream
doubles​(long streamSize,
double randomNumberOrigin,
double randomNumberBound)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each conforming to the given origin
(inclusive) and bound (exclusive).

**Overrides:** doubles

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

double

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- doubles

```java
public
DoubleStream
doubles​(double randomNumberOrigin,
double randomNumberBound)
```

Returns an effectively unlimited stream of pseudorandom

double

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:** doubles

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

doubles(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

double

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

Method Detail

- current

```java
public static
ThreadLocalRandom
current()
```

Returns the current thread's

ThreadLocalRandom

.

**Returns:** the current thread's

ThreadLocalRandom

- setSeed

```java
public void setSeed​(long seed)
```

Throws

UnsupportedOperationException

. Setting seeds in
this generator is not supported.

**Overrides:** setSeed

in class

Random
**Parameters:** seed

- the initial seed
**Throws:** UnsupportedOperationException

- always

- next

```java
protected int next​(int bits)
```

Generates a pseudorandom number with the indicated number of
low-order bits. Because this class has no subclasses, this
method cannot be invoked or overridden.

**Overrides:** next

in class

Random
**Parameters:** bits

- random bits
**Returns:** the next pseudorandom value from this random number
generator's sequence

- nextInt

```java
public int nextInt()
```

Returns a pseudorandom

int

value.

**Overrides:** nextInt

in class

Random
**Returns:** a pseudorandom

int

value

- nextInt

```java
public int nextInt​(int bound)
```

Returns a pseudorandom

int

value between zero (inclusive)
and the specified bound (exclusive).

**Overrides:** nextInt

in class

Random
**Parameters:** bound

- the upper bound (exclusive). Must be positive.
**Returns:** a pseudorandom

int

value between zero
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

bound

is not positive

- nextInt

```java
public int nextInt​(int origin,
int bound)
```

Returns a pseudorandom

int

value between the specified
origin (inclusive) and the specified bound (exclusive).

**Parameters:** origin

- the least value returned
**Parameters:** bound

- the upper bound (exclusive)
**Returns:** a pseudorandom

int

value between the origin
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

origin

is greater than
or equal to

bound

- nextLong

```java
public long nextLong()
```

Returns a pseudorandom

long

value.

**Overrides:** nextLong

in class

Random
**Returns:** a pseudorandom

long

value

- nextLong

```java
public long nextLong​(long bound)
```

Returns a pseudorandom

long

value between zero (inclusive)
and the specified bound (exclusive).

**Parameters:** bound

- the upper bound (exclusive). Must be positive.
**Returns:** a pseudorandom

long

value between zero
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

bound

is not positive

- nextLong

```java
public long nextLong​(long origin,
long bound)
```

Returns a pseudorandom

long

value between the specified
origin (inclusive) and the specified bound (exclusive).

**Parameters:** origin

- the least value returned
**Parameters:** bound

- the upper bound (exclusive)
**Returns:** a pseudorandom

long

value between the origin
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

origin

is greater than
or equal to

bound

- nextDouble

```java
public double nextDouble()
```

Returns a pseudorandom

double

value between zero
(inclusive) and one (exclusive).

**Overrides:** nextDouble

in class

Random
**Returns:** a pseudorandom

double

value between zero
(inclusive) and one (exclusive)
**See Also:** Math.random()

- nextDouble

```java
public double nextDouble​(double bound)
```

Returns a pseudorandom

double

value between 0.0
(inclusive) and the specified bound (exclusive).

**Parameters:** bound

- the upper bound (exclusive). Must be positive.
**Returns:** a pseudorandom

double

value between zero
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

bound

is not positive

- nextDouble

```java
public double nextDouble​(double origin,
double bound)
```

Returns a pseudorandom

double

value between the specified
origin (inclusive) and bound (exclusive).

**Parameters:** origin

- the least value returned
**Parameters:** bound

- the upper bound (exclusive)
**Returns:** a pseudorandom

double

value between the origin
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

origin

is greater than
or equal to

bound

- nextBoolean

```java
public boolean nextBoolean()
```

Returns a pseudorandom

boolean

value.

**Overrides:** nextBoolean

in class

Random
**Returns:** a pseudorandom

boolean

value

- nextFloat

```java
public float nextFloat()
```

Returns a pseudorandom

float

value between zero
(inclusive) and one (exclusive).

**Overrides:** nextFloat

in class

Random
**Returns:** a pseudorandom

float

value between zero
(inclusive) and one (exclusive)

- ints

```java
public
IntStream
ints​(long streamSize)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

int

values.

**Overrides:** ints

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Returns:** a stream of pseudorandom

int

values
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero
**Since:** 1.8

- ints

```java
public
IntStream
ints()
```

Returns an effectively unlimited stream of pseudorandom

int

values.

**Overrides:** ints

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

ints(Long.MAX_VALUE)

.
**Returns:** a stream of pseudorandom

int

values
**Since:** 1.8

- ints

```java
public
IntStream
ints​(long streamSize,
int randomNumberOrigin,
int randomNumberBound)
```

Returns a stream producing the given

streamSize

number
of pseudorandom

int

values, each conforming to the given
origin (inclusive) and bound (exclusive).

**Overrides:** ints

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

int

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- ints

```java
public
IntStream
ints​(int randomNumberOrigin,
int randomNumberBound)
```

Returns an effectively unlimited stream of pseudorandom

int

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:** ints

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

ints(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

int

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- longs

```java
public
LongStream
longs​(long streamSize)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

long

values.

**Overrides:** longs

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Returns:** a stream of pseudorandom

long

values
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero
**Since:** 1.8

- longs

```java
public
LongStream
longs()
```

Returns an effectively unlimited stream of pseudorandom

long

values.

**Overrides:** longs

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

longs(Long.MAX_VALUE)

.
**Returns:** a stream of pseudorandom

long

values
**Since:** 1.8

- longs

```java
public
LongStream
longs​(long streamSize,
long randomNumberOrigin,
long randomNumberBound)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

long

, each conforming to the given origin
(inclusive) and bound (exclusive).

**Overrides:** longs

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

long

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- longs

```java
public
LongStream
longs​(long randomNumberOrigin,
long randomNumberBound)
```

Returns an effectively unlimited stream of pseudorandom

long

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:** longs

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

longs(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

long

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- doubles

```java
public
DoubleStream
doubles​(long streamSize)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each between zero
(inclusive) and one (exclusive).

**Overrides:** doubles

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Returns:** a stream of

double

values
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero
**Since:** 1.8

- doubles

```java
public
DoubleStream
doubles()
```

Returns an effectively unlimited stream of pseudorandom

double

values, each between zero (inclusive) and one
(exclusive).

**Overrides:** doubles

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

doubles(Long.MAX_VALUE)

.
**Returns:** a stream of pseudorandom

double

values
**Since:** 1.8

- doubles

```java
public
DoubleStream
doubles​(long streamSize,
double randomNumberOrigin,
double randomNumberBound)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each conforming to the given origin
(inclusive) and bound (exclusive).

**Overrides:** doubles

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

double

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

- doubles

```java
public
DoubleStream
doubles​(double randomNumberOrigin,
double randomNumberBound)
```

Returns an effectively unlimited stream of pseudorandom

double

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:** doubles

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

doubles(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

double

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

---

#### Method Detail

current

```java
public static
ThreadLocalRandom
current()
```

Returns the current thread's

ThreadLocalRandom

.

**Returns:** the current thread's

ThreadLocalRandom

---

#### current

public static

ThreadLocalRandom

current()

Returns the current thread's

ThreadLocalRandom

.

setSeed

```java
public void setSeed​(long seed)
```

Throws

UnsupportedOperationException

. Setting seeds in
this generator is not supported.

**Overrides:** setSeed

in class

Random
**Parameters:** seed

- the initial seed
**Throws:** UnsupportedOperationException

- always

---

#### setSeed

public void setSeed​(long seed)

Throws

UnsupportedOperationException

. Setting seeds in
this generator is not supported.

next

```java
protected int next​(int bits)
```

Generates a pseudorandom number with the indicated number of
low-order bits. Because this class has no subclasses, this
method cannot be invoked or overridden.

**Overrides:** next

in class

Random
**Parameters:** bits

- random bits
**Returns:** the next pseudorandom value from this random number
generator's sequence

---

#### next

protected int next​(int bits)

Generates a pseudorandom number with the indicated number of
low-order bits. Because this class has no subclasses, this
method cannot be invoked or overridden.

nextInt

```java
public int nextInt()
```

Returns a pseudorandom

int

value.

**Overrides:** nextInt

in class

Random
**Returns:** a pseudorandom

int

value

---

#### nextInt

public int nextInt()

Returns a pseudorandom

int

value.

nextInt

```java
public int nextInt​(int bound)
```

Returns a pseudorandom

int

value between zero (inclusive)
and the specified bound (exclusive).

**Overrides:** nextInt

in class

Random
**Parameters:** bound

- the upper bound (exclusive). Must be positive.
**Returns:** a pseudorandom

int

value between zero
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

bound

is not positive

---

#### nextInt

public int nextInt​(int bound)

Returns a pseudorandom

int

value between zero (inclusive)
and the specified bound (exclusive).

nextInt

```java
public int nextInt​(int origin,
int bound)
```

Returns a pseudorandom

int

value between the specified
origin (inclusive) and the specified bound (exclusive).

**Parameters:** origin

- the least value returned
**Parameters:** bound

- the upper bound (exclusive)
**Returns:** a pseudorandom

int

value between the origin
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

origin

is greater than
or equal to

bound

---

#### nextInt

public int nextInt​(int origin,
int bound)

Returns a pseudorandom

int

value between the specified
origin (inclusive) and the specified bound (exclusive).

nextLong

```java
public long nextLong()
```

Returns a pseudorandom

long

value.

**Overrides:** nextLong

in class

Random
**Returns:** a pseudorandom

long

value

---

#### nextLong

public long nextLong()

Returns a pseudorandom

long

value.

nextLong

```java
public long nextLong​(long bound)
```

Returns a pseudorandom

long

value between zero (inclusive)
and the specified bound (exclusive).

**Parameters:** bound

- the upper bound (exclusive). Must be positive.
**Returns:** a pseudorandom

long

value between zero
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

bound

is not positive

---

#### nextLong

public long nextLong​(long bound)

Returns a pseudorandom

long

value between zero (inclusive)
and the specified bound (exclusive).

nextLong

```java
public long nextLong​(long origin,
long bound)
```

Returns a pseudorandom

long

value between the specified
origin (inclusive) and the specified bound (exclusive).

**Parameters:** origin

- the least value returned
**Parameters:** bound

- the upper bound (exclusive)
**Returns:** a pseudorandom

long

value between the origin
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

origin

is greater than
or equal to

bound

---

#### nextLong

public long nextLong​(long origin,
long bound)

Returns a pseudorandom

long

value between the specified
origin (inclusive) and the specified bound (exclusive).

nextDouble

```java
public double nextDouble()
```

Returns a pseudorandom

double

value between zero
(inclusive) and one (exclusive).

**Overrides:** nextDouble

in class

Random
**Returns:** a pseudorandom

double

value between zero
(inclusive) and one (exclusive)
**See Also:** Math.random()

---

#### nextDouble

public double nextDouble()

Returns a pseudorandom

double

value between zero
(inclusive) and one (exclusive).

nextDouble

```java
public double nextDouble​(double bound)
```

Returns a pseudorandom

double

value between 0.0
(inclusive) and the specified bound (exclusive).

**Parameters:** bound

- the upper bound (exclusive). Must be positive.
**Returns:** a pseudorandom

double

value between zero
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

bound

is not positive

---

#### nextDouble

public double nextDouble​(double bound)

Returns a pseudorandom

double

value between 0.0
(inclusive) and the specified bound (exclusive).

nextDouble

```java
public double nextDouble​(double origin,
double bound)
```

Returns a pseudorandom

double

value between the specified
origin (inclusive) and bound (exclusive).

**Parameters:** origin

- the least value returned
**Parameters:** bound

- the upper bound (exclusive)
**Returns:** a pseudorandom

double

value between the origin
(inclusive) and the bound (exclusive)
**Throws:** IllegalArgumentException

- if

origin

is greater than
or equal to

bound

---

#### nextDouble

public double nextDouble​(double origin,
double bound)

Returns a pseudorandom

double

value between the specified
origin (inclusive) and bound (exclusive).

nextBoolean

```java
public boolean nextBoolean()
```

Returns a pseudorandom

boolean

value.

**Overrides:** nextBoolean

in class

Random
**Returns:** a pseudorandom

boolean

value

---

#### nextBoolean

public boolean nextBoolean()

Returns a pseudorandom

boolean

value.

nextFloat

```java
public float nextFloat()
```

Returns a pseudorandom

float

value between zero
(inclusive) and one (exclusive).

**Overrides:** nextFloat

in class

Random
**Returns:** a pseudorandom

float

value between zero
(inclusive) and one (exclusive)

---

#### nextFloat

public float nextFloat()

Returns a pseudorandom

float

value between zero
(inclusive) and one (exclusive).

ints

```java
public
IntStream
ints​(long streamSize)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

int

values.

**Overrides:** ints

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Returns:** a stream of pseudorandom

int

values
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero
**Since:** 1.8

---

#### ints

public

IntStream

ints​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

int

values.

ints

```java
public
IntStream
ints()
```

Returns an effectively unlimited stream of pseudorandom

int

values.

**Overrides:** ints

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

ints(Long.MAX_VALUE)

.
**Returns:** a stream of pseudorandom

int

values
**Since:** 1.8

---

#### ints

public

IntStream

ints()

Returns an effectively unlimited stream of pseudorandom

int

values.

ints

```java
public
IntStream
ints​(long streamSize,
int randomNumberOrigin,
int randomNumberBound)
```

Returns a stream producing the given

streamSize

number
of pseudorandom

int

values, each conforming to the given
origin (inclusive) and bound (exclusive).

**Overrides:** ints

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

int

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

---

#### ints

public

IntStream

ints​(long streamSize,
int randomNumberOrigin,
int randomNumberBound)

Returns a stream producing the given

streamSize

number
of pseudorandom

int

values, each conforming to the given
origin (inclusive) and bound (exclusive).

ints

```java
public
IntStream
ints​(int randomNumberOrigin,
int randomNumberBound)
```

Returns an effectively unlimited stream of pseudorandom

int

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:** ints

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

ints(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

int

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

---

#### ints

public

IntStream

ints​(int randomNumberOrigin,
int randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

int

values, each conforming to the given origin (inclusive) and bound
(exclusive).

longs

```java
public
LongStream
longs​(long streamSize)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

long

values.

**Overrides:** longs

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Returns:** a stream of pseudorandom

long

values
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero
**Since:** 1.8

---

#### longs

public

LongStream

longs​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

long

values.

longs

```java
public
LongStream
longs()
```

Returns an effectively unlimited stream of pseudorandom

long

values.

**Overrides:** longs

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

longs(Long.MAX_VALUE)

.
**Returns:** a stream of pseudorandom

long

values
**Since:** 1.8

---

#### longs

public

LongStream

longs()

Returns an effectively unlimited stream of pseudorandom

long

values.

longs

```java
public
LongStream
longs​(long streamSize,
long randomNumberOrigin,
long randomNumberBound)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

long

, each conforming to the given origin
(inclusive) and bound (exclusive).

**Overrides:** longs

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

long

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

---

#### longs

public

LongStream

longs​(long streamSize,
long randomNumberOrigin,
long randomNumberBound)

Returns a stream producing the given

streamSize

number of
pseudorandom

long

, each conforming to the given origin
(inclusive) and bound (exclusive).

longs

```java
public
LongStream
longs​(long randomNumberOrigin,
long randomNumberBound)
```

Returns an effectively unlimited stream of pseudorandom

long

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:** longs

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

longs(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

long

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

---

#### longs

public

LongStream

longs​(long randomNumberOrigin,
long randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

long

values, each conforming to the given origin (inclusive) and bound
(exclusive).

doubles

```java
public
DoubleStream
doubles​(long streamSize)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each between zero
(inclusive) and one (exclusive).

**Overrides:** doubles

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Returns:** a stream of

double

values
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero
**Since:** 1.8

---

#### doubles

public

DoubleStream

doubles​(long streamSize)

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each between zero
(inclusive) and one (exclusive).

doubles

```java
public
DoubleStream
doubles()
```

Returns an effectively unlimited stream of pseudorandom

double

values, each between zero (inclusive) and one
(exclusive).

**Overrides:** doubles

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

doubles(Long.MAX_VALUE)

.
**Returns:** a stream of pseudorandom

double

values
**Since:** 1.8

---

#### doubles

public

DoubleStream

doubles()

Returns an effectively unlimited stream of pseudorandom

double

values, each between zero (inclusive) and one
(exclusive).

doubles

```java
public
DoubleStream
doubles​(long streamSize,
double randomNumberOrigin,
double randomNumberBound)
```

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each conforming to the given origin
(inclusive) and bound (exclusive).

**Overrides:** doubles

in class

Random
**Parameters:** streamSize

- the number of values to generate
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

double

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

streamSize

is
less than zero, or

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

---

#### doubles

public

DoubleStream

doubles​(long streamSize,
double randomNumberOrigin,
double randomNumberBound)

Returns a stream producing the given

streamSize

number of
pseudorandom

double

values, each conforming to the given origin
(inclusive) and bound (exclusive).

doubles

```java
public
DoubleStream
doubles​(double randomNumberOrigin,
double randomNumberBound)
```

Returns an effectively unlimited stream of pseudorandom

double

values, each conforming to the given origin (inclusive) and bound
(exclusive).

**Overrides:** doubles

in class

Random
**Implementation Note:** This method is implemented to be equivalent to

doubles(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)

.
**Parameters:** randomNumberOrigin

- the origin (inclusive) of each random value
**Parameters:** randomNumberBound

- the bound (exclusive) of each random value
**Returns:** a stream of pseudorandom

double

values,
each with the given origin (inclusive) and bound (exclusive)
**Throws:** IllegalArgumentException

- if

randomNumberOrigin

is greater than or equal to

randomNumberBound
**Since:** 1.8

---

#### doubles

public

DoubleStream

doubles​(double randomNumberOrigin,
double randomNumberBound)

Returns an effectively unlimited stream of pseudorandom

double

values, each conforming to the given origin (inclusive) and bound
(exclusive).

---

