# Class OptionalLong

**Source:** `java.base\java\util\OptionalLong.html`

### Class Description

```java
public final class
OptionalLong

extends
Object
```

A container object which may or may not contain a

long

value.
If a value is present,

isPresent()

returns

true

. If no
value is present, the object is considered

empty

and

isPresent()

returns

false

.

Additional methods that depend on the presence or absence of a contained
value are provided, such as

orElse()

(returns a default value if no value is present) and

ifPresent()

(performs an
action if a value is present).

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

OptionalLong

may have unpredictable results and should be avoided.

**API Note:** OptionalLong

is primarily intended for use as a method return type where
there is a clear need to represent "no result." A variable whose type is

OptionalLong

should never itself be

null

; it should always point
to an

OptionalLong

instance.
**Since:** 1.8

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
OptionalLong
empty()

Returns an empty

OptionalLong

instance. No value is present for
this

OptionalLong

.

**Returns:**
- an empty

OptionalLong

.

**API Note:**
- Though it may be tempting to do so, avoid testing if an object is empty
by comparing with

==

against instances returned by

OptionalLong.empty()

. There is no guarantee that it is a singleton.
Instead, use

isPresent()

.

---

#### public static
OptionalLong
of​(long value)

Returns an

OptionalLong

describing the given value.

**Parameters:**
- value

- the value to describe

**Returns:**
- an

OptionalLong

with the value present

---

#### public long getAsLong()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:**
- the value described by this

OptionalLong

**Throws:**
- NoSuchElementException

- if no value is present

**API Note:**
- The preferred alternative to this method is

orElseThrow()

.

---

#### public boolean isPresent()

If a value is present, returns

true

, otherwise

false

.

**Returns:**
- true

if a value is present, otherwise

false

---

#### public boolean isEmpty()

If a value is not present, returns

true

, otherwise

false

.

**Returns:**
- true

if a value is not present, otherwise

false

**Since:**
- 11

---

#### public void ifPresent​(
LongConsumer
action)

If a value is present, performs the given action with the value,
otherwise does nothing.

**Parameters:**
- action

- the action to be performed, if a value is present

**Throws:**
- NullPointerException

- if value is present and the given action is

null

---

#### public void ifPresentOrElse​(
LongConsumer
action,

Runnable
emptyAction)

If a value is present, performs the given action with the value,
otherwise performs the given empty-based action.

**Parameters:**
- action

- the action to be performed, if a value is present
- emptyAction

- the empty-based action to be performed, if no value is
present

**Throws:**
- NullPointerException

- if a value is present and the given action
is

null

, or no value is present and the given empty-based
action is

null

.

**Since:**
- 9

---

#### public
LongStream
stream()

If a value is present, returns a sequential

LongStream

containing
only that value, otherwise returns an empty

LongStream

.

**Returns:**
- the optional value as an

LongStream

**Since:**
- 9

**API Note:**
- This method can be used to transform a

Stream

of optional longs
to an

LongStream

of present longs:

```java
Stream<OptionalLong> os = ..
LongStream s = os.flatMapToLong(OptionalLong::stream)
```

---

#### public long orElse​(long other)

If a value is present, returns the value, otherwise returns

other

.

**Parameters:**
- other

- the value to be returned, if no value is present

**Returns:**
- the value, if present, otherwise

other

---

#### public long orElseGet​(
LongSupplier
supplier)

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

**Parameters:**
- supplier

- the supplying function that produces a value to be returned

**Returns:**
- the value, if present, otherwise the result produced by the
supplying function

**Throws:**
- NullPointerException

- if no value is present and the supplying
function is

null

---

#### public long orElseThrow()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:**
- the value described by this

OptionalLong

**Throws:**
- NoSuchElementException

- if no value is present

**Since:**
- 10

---

#### public <X extends
Throwable
> long orElseThrow​(
Supplier
<? extends X> exceptionSupplier)
throws X

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

**Parameters:**
- exceptionSupplier

- the supplying function that produces an
exception to be thrown

**Returns:**
- the value, if present

**Throws:**
- X

- if no value is present
- NullPointerException

- if no value is present and the exception
supplying function is

null
- X extends

Throwable

**API Note:**
- A method reference to the exception constructor with an empty argument
list can be used as the supplier. For example,

IllegalStateException::new

**Type Parameters:**
- X

- Type of the exception to be thrown

---

#### public boolean equals​(
Object
obj)

Indicates whether some other object is "equal to" this

OptionalLong

. The other object is considered equal if:

- it is also an

OptionalLong

and;

both instances have no value present or;

the present values are "equal to" each other via

==

.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- an object to be tested for equality

**Returns:**
- true

if the other object is "equal to" this object
otherwise

false

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code of the value, if present, otherwise

0

(zero) if no value is present.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- hash code value of the present value or

0

if no value is
present

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a non-empty string representation of this

OptionalLong

suitable for debugging. The exact presentation format is unspecified and
may vary between implementations and versions.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation of this instance

**Implementation Requirements:**
- If a value is present the result must include its string representation
in the result. Empty and present

OptionalLong

s must be
unambiguously differentiable.

---

### Additional Sections

#### Class OptionalLong

java.lang.Object

- java.util.OptionalLong

java.util.OptionalLong

```java
public final class
OptionalLong

extends
Object
```

A container object which may or may not contain a

long

value.
If a value is present,

isPresent()

returns

true

. If no
value is present, the object is considered

empty

and

isPresent()

returns

false

.

Additional methods that depend on the presence or absence of a contained
value are provided, such as

orElse()

(returns a default value if no value is present) and

ifPresent()

(performs an
action if a value is present).

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

OptionalLong

may have unpredictable results and should be avoided.

**API Note:** OptionalLong

is primarily intended for use as a method return type where
there is a clear need to represent "no result." A variable whose type is

OptionalLong

should never itself be

null

; it should always point
to an

OptionalLong

instance.
**Since:** 1.8

public final class

OptionalLong

extends

Object

A container object which may or may not contain a

long

value.
If a value is present,

isPresent()

returns

true

. If no
value is present, the object is considered

empty

and

isPresent()

returns

false

.

Additional methods that depend on the presence or absence of a contained
value are provided, such as

orElse()

(returns a default value if no value is present) and

ifPresent()

(performs an
action if a value is present).

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

OptionalLong

may have unpredictable results and should be avoided.

Additional methods that depend on the presence or absence of a contained
value are provided, such as

orElse()

(returns a default value if no value is present) and

ifPresent()

(performs an
action if a value is present).

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

OptionalLong

may have unpredictable results and should be avoided.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

OptionalLong

may have unpredictable results and should be avoided.

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

OptionalLong

empty

()

Returns an empty

OptionalLong

instance.

boolean

equals

​(

Object

obj)

Indicates whether some other object is "equal to" this

OptionalLong

.

long

getAsLong

()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

int

hashCode

()

Returns the hash code of the value, if present, otherwise

0

(zero) if no value is present.

void

ifPresent

​(

LongConsumer

action)

If a value is present, performs the given action with the value,
otherwise does nothing.

void

ifPresentOrElse

​(

LongConsumer

action,

Runnable

emptyAction)

If a value is present, performs the given action with the value,
otherwise performs the given empty-based action.

boolean

isEmpty

()

If a value is not present, returns

true

, otherwise

false

.

boolean

isPresent

()

If a value is present, returns

true

, otherwise

false

.

static

OptionalLong

of

​(long value)

Returns an

OptionalLong

describing the given value.

long

orElse

​(long other)

If a value is present, returns the value, otherwise returns

other

.

long

orElseGet

​(

LongSupplier

supplier)

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

long

orElseThrow

()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

<X extends

Throwable

>

long

orElseThrow

​(

Supplier

<? extends X> exceptionSupplier)

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

LongStream

stream

()

If a value is present, returns a sequential

LongStream

containing
only that value, otherwise returns an empty

LongStream

.

String

toString

()

Returns a non-empty string representation of this

OptionalLong

suitable for debugging.

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

OptionalLong

empty

()

Returns an empty

OptionalLong

instance.

boolean

equals

​(

Object

obj)

Indicates whether some other object is "equal to" this

OptionalLong

.

long

getAsLong

()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

int

hashCode

()

Returns the hash code of the value, if present, otherwise

0

(zero) if no value is present.

void

ifPresent

​(

LongConsumer

action)

If a value is present, performs the given action with the value,
otherwise does nothing.

void

ifPresentOrElse

​(

LongConsumer

action,

Runnable

emptyAction)

If a value is present, performs the given action with the value,
otherwise performs the given empty-based action.

boolean

isEmpty

()

If a value is not present, returns

true

, otherwise

false

.

boolean

isPresent

()

If a value is present, returns

true

, otherwise

false

.

static

OptionalLong

of

​(long value)

Returns an

OptionalLong

describing the given value.

long

orElse

​(long other)

If a value is present, returns the value, otherwise returns

other

.

long

orElseGet

​(

LongSupplier

supplier)

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

long

orElseThrow

()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

<X extends

Throwable

>

long

orElseThrow

​(

Supplier

<? extends X> exceptionSupplier)

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

LongStream

stream

()

If a value is present, returns a sequential

LongStream

containing
only that value, otherwise returns an empty

LongStream

.

String

toString

()

Returns a non-empty string representation of this

OptionalLong

suitable for debugging.

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

Returns an empty

OptionalLong

instance.

Indicates whether some other object is "equal to" this

OptionalLong

.

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

Returns the hash code of the value, if present, otherwise

0

(zero) if no value is present.

If a value is present, performs the given action with the value,
otherwise does nothing.

If a value is present, performs the given action with the value,
otherwise performs the given empty-based action.

If a value is not present, returns

true

, otherwise

false

.

If a value is present, returns

true

, otherwise

false

.

Returns an

OptionalLong

describing the given value.

If a value is present, returns the value, otherwise returns

other

.

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

If a value is present, returns a sequential

LongStream

containing
only that value, otherwise returns an empty

LongStream

.

Returns a non-empty string representation of this

OptionalLong

suitable for debugging.

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

- empty

```java
public static
OptionalLong
empty()
```

Returns an empty

OptionalLong

instance. No value is present for
this

OptionalLong

.

**API Note:** Though it may be tempting to do so, avoid testing if an object is empty
by comparing with

==

against instances returned by

OptionalLong.empty()

. There is no guarantee that it is a singleton.
Instead, use

isPresent()

.
**Returns:** an empty

OptionalLong

.

- of

```java
public static
OptionalLong
of​(long value)
```

Returns an

OptionalLong

describing the given value.

**Parameters:** value

- the value to describe
**Returns:** an

OptionalLong

with the value present

- getAsLong

```java
public long getAsLong()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**API Note:** The preferred alternative to this method is

orElseThrow()

.
**Returns:** the value described by this

OptionalLong
**Throws:** NoSuchElementException

- if no value is present

- isPresent

```java
public boolean isPresent()
```

If a value is present, returns

true

, otherwise

false

.

**Returns:** true

if a value is present, otherwise

false

- isEmpty

```java
public boolean isEmpty()
```

If a value is not present, returns

true

, otherwise

false

.

**Returns:** true

if a value is not present, otherwise

false
**Since:** 11

- ifPresent

```java
public void ifPresent​(
LongConsumer
action)
```

If a value is present, performs the given action with the value,
otherwise does nothing.

**Parameters:** action

- the action to be performed, if a value is present
**Throws:** NullPointerException

- if value is present and the given action is

null

- ifPresentOrElse

```java
public void ifPresentOrElse​(
LongConsumer
action,

Runnable
emptyAction)
```

If a value is present, performs the given action with the value,
otherwise performs the given empty-based action.

**Parameters:** action

- the action to be performed, if a value is present
**Parameters:** emptyAction

- the empty-based action to be performed, if no value is
present
**Throws:** NullPointerException

- if a value is present and the given action
is

null

, or no value is present and the given empty-based
action is

null

.
**Since:** 9

- stream

```java
public
LongStream
stream()
```

If a value is present, returns a sequential

LongStream

containing
only that value, otherwise returns an empty

LongStream

.

**API Note:** This method can be used to transform a

Stream

of optional longs
to an

LongStream

of present longs:

```java
Stream<OptionalLong> os = ..
LongStream s = os.flatMapToLong(OptionalLong::stream)
```
**Returns:** the optional value as an

LongStream
**Since:** 9

- orElse

```java
public long orElse​(long other)
```

If a value is present, returns the value, otherwise returns

other

.

**Parameters:** other

- the value to be returned, if no value is present
**Returns:** the value, if present, otherwise

other

- orElseGet

```java
public long orElseGet​(
LongSupplier
supplier)
```

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

**Parameters:** supplier

- the supplying function that produces a value to be returned
**Returns:** the value, if present, otherwise the result produced by the
supplying function
**Throws:** NullPointerException

- if no value is present and the supplying
function is

null

- orElseThrow

```java
public long orElseThrow()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:** the value described by this

OptionalLong
**Throws:** NoSuchElementException

- if no value is present
**Since:** 10

- orElseThrow

```java
public <X extends
Throwable
> long orElseThrow​(
Supplier
<? extends X> exceptionSupplier)
throws X
```

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

**API Note:** A method reference to the exception constructor with an empty argument
list can be used as the supplier. For example,

IllegalStateException::new
**Type Parameters:** X

- Type of the exception to be thrown
**Parameters:** exceptionSupplier

- the supplying function that produces an
exception to be thrown
**Returns:** the value, if present
**Throws:** X

- if no value is present
**Throws:** NullPointerException

- if no value is present and the exception
supplying function is

null
**Throws:** X extends

Throwable

- equals

```java
public boolean equals​(
Object
obj)
```

Indicates whether some other object is "equal to" this

OptionalLong

. The other object is considered equal if:

- it is also an

OptionalLong

and;

both instances have no value present or;

the present values are "equal to" each other via

==

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- an object to be tested for equality
**Returns:** true

if the other object is "equal to" this object
otherwise

false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of the value, if present, otherwise

0

(zero) if no value is present.

**Overrides:** hashCode

in class

Object
**Returns:** hash code value of the present value or

0

if no value is
present
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a non-empty string representation of this

OptionalLong

suitable for debugging. The exact presentation format is unspecified and
may vary between implementations and versions.

**Overrides:** toString

in class

Object
**Implementation Requirements:** If a value is present the result must include its string representation
in the result. Empty and present

OptionalLong

s must be
unambiguously differentiable.
**Returns:** the string representation of this instance

Method Detail

- empty

```java
public static
OptionalLong
empty()
```

Returns an empty

OptionalLong

instance. No value is present for
this

OptionalLong

.

**API Note:** Though it may be tempting to do so, avoid testing if an object is empty
by comparing with

==

against instances returned by

OptionalLong.empty()

. There is no guarantee that it is a singleton.
Instead, use

isPresent()

.
**Returns:** an empty

OptionalLong

.

- of

```java
public static
OptionalLong
of​(long value)
```

Returns an

OptionalLong

describing the given value.

**Parameters:** value

- the value to describe
**Returns:** an

OptionalLong

with the value present

- getAsLong

```java
public long getAsLong()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**API Note:** The preferred alternative to this method is

orElseThrow()

.
**Returns:** the value described by this

OptionalLong
**Throws:** NoSuchElementException

- if no value is present

- isPresent

```java
public boolean isPresent()
```

If a value is present, returns

true

, otherwise

false

.

**Returns:** true

if a value is present, otherwise

false

- isEmpty

```java
public boolean isEmpty()
```

If a value is not present, returns

true

, otherwise

false

.

**Returns:** true

if a value is not present, otherwise

false
**Since:** 11

- ifPresent

```java
public void ifPresent​(
LongConsumer
action)
```

If a value is present, performs the given action with the value,
otherwise does nothing.

**Parameters:** action

- the action to be performed, if a value is present
**Throws:** NullPointerException

- if value is present and the given action is

null

- ifPresentOrElse

```java
public void ifPresentOrElse​(
LongConsumer
action,

Runnable
emptyAction)
```

If a value is present, performs the given action with the value,
otherwise performs the given empty-based action.

**Parameters:** action

- the action to be performed, if a value is present
**Parameters:** emptyAction

- the empty-based action to be performed, if no value is
present
**Throws:** NullPointerException

- if a value is present and the given action
is

null

, or no value is present and the given empty-based
action is

null

.
**Since:** 9

- stream

```java
public
LongStream
stream()
```

If a value is present, returns a sequential

LongStream

containing
only that value, otherwise returns an empty

LongStream

.

**API Note:** This method can be used to transform a

Stream

of optional longs
to an

LongStream

of present longs:

```java
Stream<OptionalLong> os = ..
LongStream s = os.flatMapToLong(OptionalLong::stream)
```
**Returns:** the optional value as an

LongStream
**Since:** 9

- orElse

```java
public long orElse​(long other)
```

If a value is present, returns the value, otherwise returns

other

.

**Parameters:** other

- the value to be returned, if no value is present
**Returns:** the value, if present, otherwise

other

- orElseGet

```java
public long orElseGet​(
LongSupplier
supplier)
```

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

**Parameters:** supplier

- the supplying function that produces a value to be returned
**Returns:** the value, if present, otherwise the result produced by the
supplying function
**Throws:** NullPointerException

- if no value is present and the supplying
function is

null

- orElseThrow

```java
public long orElseThrow()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:** the value described by this

OptionalLong
**Throws:** NoSuchElementException

- if no value is present
**Since:** 10

- orElseThrow

```java
public <X extends
Throwable
> long orElseThrow​(
Supplier
<? extends X> exceptionSupplier)
throws X
```

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

**API Note:** A method reference to the exception constructor with an empty argument
list can be used as the supplier. For example,

IllegalStateException::new
**Type Parameters:** X

- Type of the exception to be thrown
**Parameters:** exceptionSupplier

- the supplying function that produces an
exception to be thrown
**Returns:** the value, if present
**Throws:** X

- if no value is present
**Throws:** NullPointerException

- if no value is present and the exception
supplying function is

null
**Throws:** X extends

Throwable

- equals

```java
public boolean equals​(
Object
obj)
```

Indicates whether some other object is "equal to" this

OptionalLong

. The other object is considered equal if:

- it is also an

OptionalLong

and;

both instances have no value present or;

the present values are "equal to" each other via

==

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- an object to be tested for equality
**Returns:** true

if the other object is "equal to" this object
otherwise

false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of the value, if present, otherwise

0

(zero) if no value is present.

**Overrides:** hashCode

in class

Object
**Returns:** hash code value of the present value or

0

if no value is
present
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a non-empty string representation of this

OptionalLong

suitable for debugging. The exact presentation format is unspecified and
may vary between implementations and versions.

**Overrides:** toString

in class

Object
**Implementation Requirements:** If a value is present the result must include its string representation
in the result. Empty and present

OptionalLong

s must be
unambiguously differentiable.
**Returns:** the string representation of this instance

---

#### Method Detail

empty

```java
public static
OptionalLong
empty()
```

Returns an empty

OptionalLong

instance. No value is present for
this

OptionalLong

.

**API Note:** Though it may be tempting to do so, avoid testing if an object is empty
by comparing with

==

against instances returned by

OptionalLong.empty()

. There is no guarantee that it is a singleton.
Instead, use

isPresent()

.
**Returns:** an empty

OptionalLong

.

---

#### empty

public static

OptionalLong

empty()

Returns an empty

OptionalLong

instance. No value is present for
this

OptionalLong

.

of

```java
public static
OptionalLong
of​(long value)
```

Returns an

OptionalLong

describing the given value.

**Parameters:** value

- the value to describe
**Returns:** an

OptionalLong

with the value present

---

#### of

public static

OptionalLong

of​(long value)

Returns an

OptionalLong

describing the given value.

getAsLong

```java
public long getAsLong()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**API Note:** The preferred alternative to this method is

orElseThrow()

.
**Returns:** the value described by this

OptionalLong
**Throws:** NoSuchElementException

- if no value is present

---

#### getAsLong

public long getAsLong()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

isPresent

```java
public boolean isPresent()
```

If a value is present, returns

true

, otherwise

false

.

**Returns:** true

if a value is present, otherwise

false

---

#### isPresent

public boolean isPresent()

If a value is present, returns

true

, otherwise

false

.

isEmpty

```java
public boolean isEmpty()
```

If a value is not present, returns

true

, otherwise

false

.

**Returns:** true

if a value is not present, otherwise

false
**Since:** 11

---

#### isEmpty

public boolean isEmpty()

If a value is not present, returns

true

, otherwise

false

.

ifPresent

```java
public void ifPresent​(
LongConsumer
action)
```

If a value is present, performs the given action with the value,
otherwise does nothing.

**Parameters:** action

- the action to be performed, if a value is present
**Throws:** NullPointerException

- if value is present and the given action is

null

---

#### ifPresent

public void ifPresent​(

LongConsumer

action)

If a value is present, performs the given action with the value,
otherwise does nothing.

ifPresentOrElse

```java
public void ifPresentOrElse​(
LongConsumer
action,

Runnable
emptyAction)
```

If a value is present, performs the given action with the value,
otherwise performs the given empty-based action.

**Parameters:** action

- the action to be performed, if a value is present
**Parameters:** emptyAction

- the empty-based action to be performed, if no value is
present
**Throws:** NullPointerException

- if a value is present and the given action
is

null

, or no value is present and the given empty-based
action is

null

.
**Since:** 9

---

#### ifPresentOrElse

public void ifPresentOrElse​(

LongConsumer

action,

Runnable

emptyAction)

If a value is present, performs the given action with the value,
otherwise performs the given empty-based action.

stream

```java
public
LongStream
stream()
```

If a value is present, returns a sequential

LongStream

containing
only that value, otherwise returns an empty

LongStream

.

**API Note:** This method can be used to transform a

Stream

of optional longs
to an

LongStream

of present longs:

```java
Stream<OptionalLong> os = ..
LongStream s = os.flatMapToLong(OptionalLong::stream)
```
**Returns:** the optional value as an

LongStream
**Since:** 9

---

#### stream

public

LongStream

stream()

If a value is present, returns a sequential

LongStream

containing
only that value, otherwise returns an empty

LongStream

.

Stream<OptionalLong> os = ..
LongStream s = os.flatMapToLong(OptionalLong::stream)

orElse

```java
public long orElse​(long other)
```

If a value is present, returns the value, otherwise returns

other

.

**Parameters:** other

- the value to be returned, if no value is present
**Returns:** the value, if present, otherwise

other

---

#### orElse

public long orElse​(long other)

If a value is present, returns the value, otherwise returns

other

.

orElseGet

```java
public long orElseGet​(
LongSupplier
supplier)
```

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

**Parameters:** supplier

- the supplying function that produces a value to be returned
**Returns:** the value, if present, otherwise the result produced by the
supplying function
**Throws:** NullPointerException

- if no value is present and the supplying
function is

null

---

#### orElseGet

public long orElseGet​(

LongSupplier

supplier)

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

orElseThrow

```java
public long orElseThrow()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:** the value described by this

OptionalLong
**Throws:** NoSuchElementException

- if no value is present
**Since:** 10

---

#### orElseThrow

public long orElseThrow()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

orElseThrow

```java
public <X extends
Throwable
> long orElseThrow​(
Supplier
<? extends X> exceptionSupplier)
throws X
```

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

**API Note:** A method reference to the exception constructor with an empty argument
list can be used as the supplier. For example,

IllegalStateException::new
**Type Parameters:** X

- Type of the exception to be thrown
**Parameters:** exceptionSupplier

- the supplying function that produces an
exception to be thrown
**Returns:** the value, if present
**Throws:** X

- if no value is present
**Throws:** NullPointerException

- if no value is present and the exception
supplying function is

null
**Throws:** X extends

Throwable

---

#### orElseThrow

public <X extends

Throwable

> long orElseThrow​(

Supplier

<? extends X> exceptionSupplier)
throws X

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

equals

```java
public boolean equals​(
Object
obj)
```

Indicates whether some other object is "equal to" this

OptionalLong

. The other object is considered equal if:

- it is also an

OptionalLong

and;

both instances have no value present or;

the present values are "equal to" each other via

==

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- an object to be tested for equality
**Returns:** true

if the other object is "equal to" this object
otherwise

false
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Indicates whether some other object is "equal to" this

OptionalLong

. The other object is considered equal if:

- it is also an

OptionalLong

and;

both instances have no value present or;

the present values are "equal to" each other via

==

.

it is also an

OptionalLong

and;

both instances have no value present or;

the present values are "equal to" each other via

==

.

hashCode

```java
public int hashCode()
```

Returns the hash code of the value, if present, otherwise

0

(zero) if no value is present.

**Overrides:** hashCode

in class

Object
**Returns:** hash code value of the present value or

0

if no value is
present
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code of the value, if present, otherwise

0

(zero) if no value is present.

toString

```java
public
String
toString()
```

Returns a non-empty string representation of this

OptionalLong

suitable for debugging. The exact presentation format is unspecified and
may vary between implementations and versions.

**Overrides:** toString

in class

Object
**Implementation Requirements:** If a value is present the result must include its string representation
in the result. Empty and present

OptionalLong

s must be
unambiguously differentiable.
**Returns:** the string representation of this instance

---

#### toString

public

String

toString()

Returns a non-empty string representation of this

OptionalLong

suitable for debugging. The exact presentation format is unspecified and
may vary between implementations and versions.

---

