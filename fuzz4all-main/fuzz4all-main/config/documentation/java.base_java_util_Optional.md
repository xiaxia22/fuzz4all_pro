# Class Optional<T>

**Source:** `java.base\java\util\Optional.html`

### Class Description

```java
public final class
Optional<T>

extends
Object
```

A container object which may or may not contain a non-

null

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

Optional

may have unpredictable results and should be avoided.

**Type Parameters:** T

- the type of value

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static <T>
Optional
<T> empty()

Returns an empty

Optional

instance. No value is present for this

Optional

.

**Returns:**
- an empty

Optional

**API Note:**
- Though it may be tempting to do so, avoid testing if an object is empty
by comparing with

==

against instances returned by

Optional.empty()

. There is no guarantee that it is a singleton.
Instead, use

isPresent()

.

**Type Parameters:**
- T

- The type of the non-existent value

---

#### public static <T>
Optional
<T> of​(T value)

Returns an

Optional

describing the given non-

null

value.

**Parameters:**
- value

- the value to describe, which must be non-

null

**Returns:**
- an

Optional

with the value present

**Throws:**
- NullPointerException

- if value is

null

**Type Parameters:**
- T

- the type of the value

---

#### public static <T>
Optional
<T> ofNullable​(T value)

Returns an

Optional

describing the given value, if
non-

null

, otherwise returns an empty

Optional

.

**Parameters:**
- value

- the possibly-

null

value to describe

**Returns:**
- an

Optional

with a present value if the specified value
is non-

null

, otherwise an empty

Optional

**Type Parameters:**
- T

- the type of the value

---

#### public
T
get()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:**
- the non-

null

value described by this

Optional

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
Consumer
<? super
T
> action)

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
Consumer
<? super
T
> action,

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
Optional
<
T
> filter​(
Predicate
<? super
T
> predicate)

If a value is present, and the value matches the given predicate,
returns an

Optional

describing the value, otherwise returns an
empty

Optional

.

**Parameters:**
- predicate

- the predicate to apply to a value, if present

**Returns:**
- an

Optional

describing the value of this

Optional

, if a value is present and the value matches the
given predicate, otherwise an empty

Optional

**Throws:**
- NullPointerException

- if the predicate is

null

---

#### public <U>
Optional
<U> map​(
Function
<? super
T
,​? extends U> mapper)

If a value is present, returns an

Optional

describing (as if by

ofNullable(T)

) the result of applying the given mapping function to
the value, otherwise returns an empty

Optional

.

If the mapping function returns a

null

result then this method
returns an empty

Optional

.

**Parameters:**
- mapper

- the mapping function to apply to a value, if present

**Returns:**
- an

Optional

describing the result of applying a mapping
function to the value of this

Optional

, if a value is
present, otherwise an empty

Optional

**Throws:**
- NullPointerException

- if the mapping function is

null

**API Note:**
- This method supports post-processing on

Optional

values, without
the need to explicitly check for a return status. For example, the
following code traverses a stream of URIs, selects one that has not
yet been processed, and creates a path from that URI, returning
an

Optional<Path>

:

```java
Optional<Path> p =
uris.stream().filter(uri -> !isProcessedYet(uri))
.findFirst()
.map(Paths::get);
```

Here,

findFirst

returns an

Optional<URI>

, and then

map

returns an

Optional<Path>

for the desired
URI if one exists.

**Type Parameters:**
- U

- The type of the value returned from the mapping function

---

#### public <U>
Optional
<U> flatMap​(
Function
<? super
T
,​? extends
Optional
<? extends U>> mapper)

If a value is present, returns the result of applying the given

Optional

-bearing mapping function to the value, otherwise returns
an empty

Optional

.

This method is similar to

map(Function)

, but the mapping
function is one whose result is already an

Optional

, and if
invoked,

flatMap

does not wrap it within an additional

Optional

.

**Parameters:**
- mapper

- the mapping function to apply to a value, if present

**Returns:**
- the result of applying an

Optional

-bearing mapping
function to the value of this

Optional

, if a value is
present, otherwise an empty

Optional

**Throws:**
- NullPointerException

- if the mapping function is

null

or
returns a

null

result

**Type Parameters:**
- U

- The type of value of the

Optional

returned by the
mapping function

---

#### public
Optional
<
T
> or​(
Supplier
<? extends
Optional
<? extends
T
>> supplier)

If a value is present, returns an

Optional

describing the value,
otherwise returns an

Optional

produced by the supplying function.

**Parameters:**
- supplier

- the supplying function that produces an

Optional

to be returned

**Returns:**
- returns an

Optional

describing the value of this

Optional

, if a value is present, otherwise an

Optional

produced by the supplying function.

**Throws:**
- NullPointerException

- if the supplying function is

null

or
produces a

null

result

**Since:**
- 9

---

#### public
Stream
<
T
> stream()

If a value is present, returns a sequential

Stream

containing
only that value, otherwise returns an empty

Stream

.

**Returns:**
- the optional value as a

Stream

**Since:**
- 9

**API Note:**
- This method can be used to transform a

Stream

of optional
elements to a

Stream

of present value elements:

```java
Stream<Optional<T>> os = ..
Stream<T> s = os.flatMap(Optional::stream)
```

---

#### public
T
orElse​(
T
other)

If a value is present, returns the value, otherwise returns

other

.

**Parameters:**
- other

- the value to be returned, if no value is present.
May be

null

.

**Returns:**
- the value, if present, otherwise

other

---

#### public
T
orElseGet​(
Supplier
<? extends
T
> supplier)

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

#### public
T
orElseThrow()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:**
- the non-

null

value described by this

Optional

**Throws:**
- NoSuchElementException

- if no value is present

**Since:**
- 10

---

#### public <X extends
Throwable
>
T
orElseThrow​(
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

Optional

.
The other object is considered equal if:

- it is also an

Optional

and;

both instances have no value present or;

the present values are "equal to" each other via

equals()

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

Optional

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

Optional

s must be unambiguously
differentiable.

---

### Additional Sections

#### Class Optional<T>

java.lang.Object

- java.util.Optional<T>

java.util.Optional<T>

**Type Parameters:** T

- the type of value

```java
public final class
Optional<T>

extends
Object
```

A container object which may or may not contain a non-

null

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

Optional

may have unpredictable results and should be avoided.

**API Note:** Optional

is primarily intended for use as a method return type where
there is a clear need to represent "no result," and where using

null

is likely to cause errors. A variable whose type is

Optional

should
never itself be

null

; it should always point to an

Optional

instance.
**Since:** 1.8

public final class

Optional<T>

extends

Object

A container object which may or may not contain a non-

null

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

Optional

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

Optional

may have unpredictable results and should be avoided.

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

Optional

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

static <T>

Optional

<T>

empty

()

Returns an empty

Optional

instance.

boolean

equals

​(

Object

obj)

Indicates whether some other object is "equal to" this

Optional

.

Optional

<

T

>

filter

​(

Predicate

<? super

T

> predicate)

If a value is present, and the value matches the given predicate,
returns an

Optional

describing the value, otherwise returns an
empty

Optional

.

<U>

Optional

<U>

flatMap

​(

Function

<? super

T

,​? extends

Optional

<? extends U>> mapper)

If a value is present, returns the result of applying the given

Optional

-bearing mapping function to the value, otherwise returns
an empty

Optional

.

T

get

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

Consumer

<? super

T

> action)

If a value is present, performs the given action with the value,
otherwise does nothing.

void

ifPresentOrElse

​(

Consumer

<? super

T

> action,

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

<U>

Optional

<U>

map

​(

Function

<? super

T

,​? extends U> mapper)

If a value is present, returns an

Optional

describing (as if by

ofNullable(T)

) the result of applying the given mapping function to
the value, otherwise returns an empty

Optional

.

static <T>

Optional

<T>

of

​(T value)

Returns an

Optional

describing the given non-

null

value.

static <T>

Optional

<T>

ofNullable

​(T value)

Returns an

Optional

describing the given value, if
non-

null

, otherwise returns an empty

Optional

.

Optional

<

T

>

or

​(

Supplier

<? extends

Optional

<? extends

T

>> supplier)

If a value is present, returns an

Optional

describing the value,
otherwise returns an

Optional

produced by the supplying function.

T

orElse

​(

T

other)

If a value is present, returns the value, otherwise returns

other

.

T

orElseGet

​(

Supplier

<? extends

T

> supplier)

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

T

orElseThrow

()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

<X extends

Throwable

>

T

orElseThrow

​(

Supplier

<? extends X> exceptionSupplier)

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

Stream

<

T

>

stream

()

If a value is present, returns a sequential

Stream

containing
only that value, otherwise returns an empty

Stream

.

String

toString

()

Returns a non-empty string representation of this

Optional

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

static <T>

Optional

<T>

empty

()

Returns an empty

Optional

instance.

boolean

equals

​(

Object

obj)

Indicates whether some other object is "equal to" this

Optional

.

Optional

<

T

>

filter

​(

Predicate

<? super

T

> predicate)

If a value is present, and the value matches the given predicate,
returns an

Optional

describing the value, otherwise returns an
empty

Optional

.

<U>

Optional

<U>

flatMap

​(

Function

<? super

T

,​? extends

Optional

<? extends U>> mapper)

If a value is present, returns the result of applying the given

Optional

-bearing mapping function to the value, otherwise returns
an empty

Optional

.

T

get

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

Consumer

<? super

T

> action)

If a value is present, performs the given action with the value,
otherwise does nothing.

void

ifPresentOrElse

​(

Consumer

<? super

T

> action,

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

<U>

Optional

<U>

map

​(

Function

<? super

T

,​? extends U> mapper)

If a value is present, returns an

Optional

describing (as if by

ofNullable(T)

) the result of applying the given mapping function to
the value, otherwise returns an empty

Optional

.

static <T>

Optional

<T>

of

​(T value)

Returns an

Optional

describing the given non-

null

value.

static <T>

Optional

<T>

ofNullable

​(T value)

Returns an

Optional

describing the given value, if
non-

null

, otherwise returns an empty

Optional

.

Optional

<

T

>

or

​(

Supplier

<? extends

Optional

<? extends

T

>> supplier)

If a value is present, returns an

Optional

describing the value,
otherwise returns an

Optional

produced by the supplying function.

T

orElse

​(

T

other)

If a value is present, returns the value, otherwise returns

other

.

T

orElseGet

​(

Supplier

<? extends

T

> supplier)

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

T

orElseThrow

()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

<X extends

Throwable

>

T

orElseThrow

​(

Supplier

<? extends X> exceptionSupplier)

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

Stream

<

T

>

stream

()

If a value is present, returns a sequential

Stream

containing
only that value, otherwise returns an empty

Stream

.

String

toString

()

Returns a non-empty string representation of this

Optional

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

Optional

instance.

Indicates whether some other object is "equal to" this

Optional

.

If a value is present, and the value matches the given predicate,
returns an

Optional

describing the value, otherwise returns an
empty

Optional

.

If a value is present, returns the result of applying the given

Optional

-bearing mapping function to the value, otherwise returns
an empty

Optional

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

If a value is present, returns an

Optional

describing (as if by

ofNullable(T)

) the result of applying the given mapping function to
the value, otherwise returns an empty

Optional

.

Returns an

Optional

describing the given non-

null

value.

Returns an

Optional

describing the given value, if
non-

null

, otherwise returns an empty

Optional

.

If a value is present, returns an

Optional

describing the value,
otherwise returns an

Optional

produced by the supplying function.

If a value is present, returns the value, otherwise returns

other

.

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

If a value is present, returns the value, otherwise throws an exception
produced by the exception supplying function.

If a value is present, returns a sequential

Stream

containing
only that value, otherwise returns an empty

Stream

.

Returns a non-empty string representation of this

Optional

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
public static <T>
Optional
<T> empty()
```

Returns an empty

Optional

instance. No value is present for this

Optional

.

**API Note:** Though it may be tempting to do so, avoid testing if an object is empty
by comparing with

==

against instances returned by

Optional.empty()

. There is no guarantee that it is a singleton.
Instead, use

isPresent()

.
**Type Parameters:** T

- The type of the non-existent value
**Returns:** an empty

Optional

- of

```java
public static <T>
Optional
<T> of​(T value)
```

Returns an

Optional

describing the given non-

null

value.

**Type Parameters:** T

- the type of the value
**Parameters:** value

- the value to describe, which must be non-

null
**Returns:** an

Optional

with the value present
**Throws:** NullPointerException

- if value is

null

- ofNullable

```java
public static <T>
Optional
<T> ofNullable​(T value)
```

Returns an

Optional

describing the given value, if
non-

null

, otherwise returns an empty

Optional

.

**Type Parameters:** T

- the type of the value
**Parameters:** value

- the possibly-

null

value to describe
**Returns:** an

Optional

with a present value if the specified value
is non-

null

, otherwise an empty

Optional

- get

```java
public
T
get()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**API Note:** The preferred alternative to this method is

orElseThrow()

.
**Returns:** the non-

null

value described by this

Optional
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
Consumer
<? super
T
> action)
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
Consumer
<? super
T
> action,

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

- filter

```java
public
Optional
<
T
> filter​(
Predicate
<? super
T
> predicate)
```

If a value is present, and the value matches the given predicate,
returns an

Optional

describing the value, otherwise returns an
empty

Optional

.

**Parameters:** predicate

- the predicate to apply to a value, if present
**Returns:** an

Optional

describing the value of this

Optional

, if a value is present and the value matches the
given predicate, otherwise an empty

Optional
**Throws:** NullPointerException

- if the predicate is

null

- map

```java
public <U>
Optional
<U> map​(
Function
<? super
T
,​? extends U> mapper)
```

If a value is present, returns an

Optional

describing (as if by

ofNullable(T)

) the result of applying the given mapping function to
the value, otherwise returns an empty

Optional

.

If the mapping function returns a

null

result then this method
returns an empty

Optional

.

**API Note:** This method supports post-processing on

Optional

values, without
the need to explicitly check for a return status. For example, the
following code traverses a stream of URIs, selects one that has not
yet been processed, and creates a path from that URI, returning
an

Optional<Path>

:

```java
Optional<Path> p =
uris.stream().filter(uri -> !isProcessedYet(uri))
.findFirst()
.map(Paths::get);
```

Here,

findFirst

returns an

Optional<URI>

, and then

map

returns an

Optional<Path>

for the desired
URI if one exists.
**Type Parameters:** U

- The type of the value returned from the mapping function
**Parameters:** mapper

- the mapping function to apply to a value, if present
**Returns:** an

Optional

describing the result of applying a mapping
function to the value of this

Optional

, if a value is
present, otherwise an empty

Optional
**Throws:** NullPointerException

- if the mapping function is

null

- flatMap

```java
public <U>
Optional
<U> flatMap​(
Function
<? super
T
,​? extends
Optional
<? extends U>> mapper)
```

If a value is present, returns the result of applying the given

Optional

-bearing mapping function to the value, otherwise returns
an empty

Optional

.

This method is similar to

map(Function)

, but the mapping
function is one whose result is already an

Optional

, and if
invoked,

flatMap

does not wrap it within an additional

Optional

.

**Type Parameters:** U

- The type of value of the

Optional

returned by the
mapping function
**Parameters:** mapper

- the mapping function to apply to a value, if present
**Returns:** the result of applying an

Optional

-bearing mapping
function to the value of this

Optional

, if a value is
present, otherwise an empty

Optional
**Throws:** NullPointerException

- if the mapping function is

null

or
returns a

null

result

- or

```java
public
Optional
<
T
> or​(
Supplier
<? extends
Optional
<? extends
T
>> supplier)
```

If a value is present, returns an

Optional

describing the value,
otherwise returns an

Optional

produced by the supplying function.

**Parameters:** supplier

- the supplying function that produces an

Optional

to be returned
**Returns:** returns an

Optional

describing the value of this

Optional

, if a value is present, otherwise an

Optional

produced by the supplying function.
**Throws:** NullPointerException

- if the supplying function is

null

or
produces a

null

result
**Since:** 9

- stream

```java
public
Stream
<
T
> stream()
```

If a value is present, returns a sequential

Stream

containing
only that value, otherwise returns an empty

Stream

.

**API Note:** This method can be used to transform a

Stream

of optional
elements to a

Stream

of present value elements:

```java
Stream<Optional<T>> os = ..
Stream<T> s = os.flatMap(Optional::stream)
```
**Returns:** the optional value as a

Stream
**Since:** 9

- orElse

```java
public
T
orElse​(
T
other)
```

If a value is present, returns the value, otherwise returns

other

.

**Parameters:** other

- the value to be returned, if no value is present.
May be

null

.
**Returns:** the value, if present, otherwise

other

- orElseGet

```java
public
T
orElseGet​(
Supplier
<? extends
T
> supplier)
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
public
T
orElseThrow()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:** the non-

null

value described by this

Optional
**Throws:** NoSuchElementException

- if no value is present
**Since:** 10

- orElseThrow

```java
public <X extends
Throwable
>
T
orElseThrow​(
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

Optional

.
The other object is considered equal if:

- it is also an

Optional

and;

both instances have no value present or;

the present values are "equal to" each other via

equals()

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

Optional

suitable for debugging. The exact presentation format is unspecified and
may vary between implementations and versions.

**Overrides:** toString

in class

Object
**Implementation Requirements:** If a value is present the result must include its string representation
in the result. Empty and present

Optional

s must be unambiguously
differentiable.
**Returns:** the string representation of this instance

Method Detail

- empty

```java
public static <T>
Optional
<T> empty()
```

Returns an empty

Optional

instance. No value is present for this

Optional

.

**API Note:** Though it may be tempting to do so, avoid testing if an object is empty
by comparing with

==

against instances returned by

Optional.empty()

. There is no guarantee that it is a singleton.
Instead, use

isPresent()

.
**Type Parameters:** T

- The type of the non-existent value
**Returns:** an empty

Optional

- of

```java
public static <T>
Optional
<T> of​(T value)
```

Returns an

Optional

describing the given non-

null

value.

**Type Parameters:** T

- the type of the value
**Parameters:** value

- the value to describe, which must be non-

null
**Returns:** an

Optional

with the value present
**Throws:** NullPointerException

- if value is

null

- ofNullable

```java
public static <T>
Optional
<T> ofNullable​(T value)
```

Returns an

Optional

describing the given value, if
non-

null

, otherwise returns an empty

Optional

.

**Type Parameters:** T

- the type of the value
**Parameters:** value

- the possibly-

null

value to describe
**Returns:** an

Optional

with a present value if the specified value
is non-

null

, otherwise an empty

Optional

- get

```java
public
T
get()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**API Note:** The preferred alternative to this method is

orElseThrow()

.
**Returns:** the non-

null

value described by this

Optional
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
Consumer
<? super
T
> action)
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
Consumer
<? super
T
> action,

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

- filter

```java
public
Optional
<
T
> filter​(
Predicate
<? super
T
> predicate)
```

If a value is present, and the value matches the given predicate,
returns an

Optional

describing the value, otherwise returns an
empty

Optional

.

**Parameters:** predicate

- the predicate to apply to a value, if present
**Returns:** an

Optional

describing the value of this

Optional

, if a value is present and the value matches the
given predicate, otherwise an empty

Optional
**Throws:** NullPointerException

- if the predicate is

null

- map

```java
public <U>
Optional
<U> map​(
Function
<? super
T
,​? extends U> mapper)
```

If a value is present, returns an

Optional

describing (as if by

ofNullable(T)

) the result of applying the given mapping function to
the value, otherwise returns an empty

Optional

.

If the mapping function returns a

null

result then this method
returns an empty

Optional

.

**API Note:** This method supports post-processing on

Optional

values, without
the need to explicitly check for a return status. For example, the
following code traverses a stream of URIs, selects one that has not
yet been processed, and creates a path from that URI, returning
an

Optional<Path>

:

```java
Optional<Path> p =
uris.stream().filter(uri -> !isProcessedYet(uri))
.findFirst()
.map(Paths::get);
```

Here,

findFirst

returns an

Optional<URI>

, and then

map

returns an

Optional<Path>

for the desired
URI if one exists.
**Type Parameters:** U

- The type of the value returned from the mapping function
**Parameters:** mapper

- the mapping function to apply to a value, if present
**Returns:** an

Optional

describing the result of applying a mapping
function to the value of this

Optional

, if a value is
present, otherwise an empty

Optional
**Throws:** NullPointerException

- if the mapping function is

null

- flatMap

```java
public <U>
Optional
<U> flatMap​(
Function
<? super
T
,​? extends
Optional
<? extends U>> mapper)
```

If a value is present, returns the result of applying the given

Optional

-bearing mapping function to the value, otherwise returns
an empty

Optional

.

This method is similar to

map(Function)

, but the mapping
function is one whose result is already an

Optional

, and if
invoked,

flatMap

does not wrap it within an additional

Optional

.

**Type Parameters:** U

- The type of value of the

Optional

returned by the
mapping function
**Parameters:** mapper

- the mapping function to apply to a value, if present
**Returns:** the result of applying an

Optional

-bearing mapping
function to the value of this

Optional

, if a value is
present, otherwise an empty

Optional
**Throws:** NullPointerException

- if the mapping function is

null

or
returns a

null

result

- or

```java
public
Optional
<
T
> or​(
Supplier
<? extends
Optional
<? extends
T
>> supplier)
```

If a value is present, returns an

Optional

describing the value,
otherwise returns an

Optional

produced by the supplying function.

**Parameters:** supplier

- the supplying function that produces an

Optional

to be returned
**Returns:** returns an

Optional

describing the value of this

Optional

, if a value is present, otherwise an

Optional

produced by the supplying function.
**Throws:** NullPointerException

- if the supplying function is

null

or
produces a

null

result
**Since:** 9

- stream

```java
public
Stream
<
T
> stream()
```

If a value is present, returns a sequential

Stream

containing
only that value, otherwise returns an empty

Stream

.

**API Note:** This method can be used to transform a

Stream

of optional
elements to a

Stream

of present value elements:

```java
Stream<Optional<T>> os = ..
Stream<T> s = os.flatMap(Optional::stream)
```
**Returns:** the optional value as a

Stream
**Since:** 9

- orElse

```java
public
T
orElse​(
T
other)
```

If a value is present, returns the value, otherwise returns

other

.

**Parameters:** other

- the value to be returned, if no value is present.
May be

null

.
**Returns:** the value, if present, otherwise

other

- orElseGet

```java
public
T
orElseGet​(
Supplier
<? extends
T
> supplier)
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
public
T
orElseThrow()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:** the non-

null

value described by this

Optional
**Throws:** NoSuchElementException

- if no value is present
**Since:** 10

- orElseThrow

```java
public <X extends
Throwable
>
T
orElseThrow​(
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

Optional

.
The other object is considered equal if:

- it is also an

Optional

and;

both instances have no value present or;

the present values are "equal to" each other via

equals()

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

Optional

suitable for debugging. The exact presentation format is unspecified and
may vary between implementations and versions.

**Overrides:** toString

in class

Object
**Implementation Requirements:** If a value is present the result must include its string representation
in the result. Empty and present

Optional

s must be unambiguously
differentiable.
**Returns:** the string representation of this instance

---

#### Method Detail

empty

```java
public static <T>
Optional
<T> empty()
```

Returns an empty

Optional

instance. No value is present for this

Optional

.

**API Note:** Though it may be tempting to do so, avoid testing if an object is empty
by comparing with

==

against instances returned by

Optional.empty()

. There is no guarantee that it is a singleton.
Instead, use

isPresent()

.
**Type Parameters:** T

- The type of the non-existent value
**Returns:** an empty

Optional

---

#### empty

public static <T>

Optional

<T> empty()

Returns an empty

Optional

instance. No value is present for this

Optional

.

of

```java
public static <T>
Optional
<T> of​(T value)
```

Returns an

Optional

describing the given non-

null

value.

**Type Parameters:** T

- the type of the value
**Parameters:** value

- the value to describe, which must be non-

null
**Returns:** an

Optional

with the value present
**Throws:** NullPointerException

- if value is

null

---

#### of

public static <T>

Optional

<T> of​(T value)

Returns an

Optional

describing the given non-

null

value.

ofNullable

```java
public static <T>
Optional
<T> ofNullable​(T value)
```

Returns an

Optional

describing the given value, if
non-

null

, otherwise returns an empty

Optional

.

**Type Parameters:** T

- the type of the value
**Parameters:** value

- the possibly-

null

value to describe
**Returns:** an

Optional

with a present value if the specified value
is non-

null

, otherwise an empty

Optional

---

#### ofNullable

public static <T>

Optional

<T> ofNullable​(T value)

Returns an

Optional

describing the given value, if
non-

null

, otherwise returns an empty

Optional

.

get

```java
public
T
get()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**API Note:** The preferred alternative to this method is

orElseThrow()

.
**Returns:** the non-

null

value described by this

Optional
**Throws:** NoSuchElementException

- if no value is present

---

#### get

public

T

get()

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
Consumer
<? super
T
> action)
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

Consumer

<? super

T

> action)

If a value is present, performs the given action with the value,
otherwise does nothing.

ifPresentOrElse

```java
public void ifPresentOrElse​(
Consumer
<? super
T
> action,

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

Consumer

<? super

T

> action,

Runnable

emptyAction)

If a value is present, performs the given action with the value,
otherwise performs the given empty-based action.

filter

```java
public
Optional
<
T
> filter​(
Predicate
<? super
T
> predicate)
```

If a value is present, and the value matches the given predicate,
returns an

Optional

describing the value, otherwise returns an
empty

Optional

.

**Parameters:** predicate

- the predicate to apply to a value, if present
**Returns:** an

Optional

describing the value of this

Optional

, if a value is present and the value matches the
given predicate, otherwise an empty

Optional
**Throws:** NullPointerException

- if the predicate is

null

---

#### filter

public

Optional

<

T

> filter​(

Predicate

<? super

T

> predicate)

If a value is present, and the value matches the given predicate,
returns an

Optional

describing the value, otherwise returns an
empty

Optional

.

map

```java
public <U>
Optional
<U> map​(
Function
<? super
T
,​? extends U> mapper)
```

If a value is present, returns an

Optional

describing (as if by

ofNullable(T)

) the result of applying the given mapping function to
the value, otherwise returns an empty

Optional

.

If the mapping function returns a

null

result then this method
returns an empty

Optional

.

**API Note:** This method supports post-processing on

Optional

values, without
the need to explicitly check for a return status. For example, the
following code traverses a stream of URIs, selects one that has not
yet been processed, and creates a path from that URI, returning
an

Optional<Path>

:

```java
Optional<Path> p =
uris.stream().filter(uri -> !isProcessedYet(uri))
.findFirst()
.map(Paths::get);
```

Here,

findFirst

returns an

Optional<URI>

, and then

map

returns an

Optional<Path>

for the desired
URI if one exists.
**Type Parameters:** U

- The type of the value returned from the mapping function
**Parameters:** mapper

- the mapping function to apply to a value, if present
**Returns:** an

Optional

describing the result of applying a mapping
function to the value of this

Optional

, if a value is
present, otherwise an empty

Optional
**Throws:** NullPointerException

- if the mapping function is

null

---

#### map

public <U>

Optional

<U> map​(

Function

<? super

T

,​? extends U> mapper)

If a value is present, returns an

Optional

describing (as if by

ofNullable(T)

) the result of applying the given mapping function to
the value, otherwise returns an empty

Optional

.

If the mapping function returns a

null

result then this method
returns an empty

Optional

.

If the mapping function returns a

null

result then this method
returns an empty

Optional

.

Optional<Path> p =
uris.stream().filter(uri -> !isProcessedYet(uri))
.findFirst()
.map(Paths::get);

flatMap

```java
public <U>
Optional
<U> flatMap​(
Function
<? super
T
,​? extends
Optional
<? extends U>> mapper)
```

If a value is present, returns the result of applying the given

Optional

-bearing mapping function to the value, otherwise returns
an empty

Optional

.

This method is similar to

map(Function)

, but the mapping
function is one whose result is already an

Optional

, and if
invoked,

flatMap

does not wrap it within an additional

Optional

.

**Type Parameters:** U

- The type of value of the

Optional

returned by the
mapping function
**Parameters:** mapper

- the mapping function to apply to a value, if present
**Returns:** the result of applying an

Optional

-bearing mapping
function to the value of this

Optional

, if a value is
present, otherwise an empty

Optional
**Throws:** NullPointerException

- if the mapping function is

null

or
returns a

null

result

---

#### flatMap

public <U>

Optional

<U> flatMap​(

Function

<? super

T

,​? extends

Optional

<? extends U>> mapper)

If a value is present, returns the result of applying the given

Optional

-bearing mapping function to the value, otherwise returns
an empty

Optional

.

This method is similar to

map(Function)

, but the mapping
function is one whose result is already an

Optional

, and if
invoked,

flatMap

does not wrap it within an additional

Optional

.

This method is similar to

map(Function)

, but the mapping
function is one whose result is already an

Optional

, and if
invoked,

flatMap

does not wrap it within an additional

Optional

.

or

```java
public
Optional
<
T
> or​(
Supplier
<? extends
Optional
<? extends
T
>> supplier)
```

If a value is present, returns an

Optional

describing the value,
otherwise returns an

Optional

produced by the supplying function.

**Parameters:** supplier

- the supplying function that produces an

Optional

to be returned
**Returns:** returns an

Optional

describing the value of this

Optional

, if a value is present, otherwise an

Optional

produced by the supplying function.
**Throws:** NullPointerException

- if the supplying function is

null

or
produces a

null

result
**Since:** 9

---

#### or

public

Optional

<

T

> or​(

Supplier

<? extends

Optional

<? extends

T

>> supplier)

If a value is present, returns an

Optional

describing the value,
otherwise returns an

Optional

produced by the supplying function.

stream

```java
public
Stream
<
T
> stream()
```

If a value is present, returns a sequential

Stream

containing
only that value, otherwise returns an empty

Stream

.

**API Note:** This method can be used to transform a

Stream

of optional
elements to a

Stream

of present value elements:

```java
Stream<Optional<T>> os = ..
Stream<T> s = os.flatMap(Optional::stream)
```
**Returns:** the optional value as a

Stream
**Since:** 9

---

#### stream

public

Stream

<

T

> stream()

If a value is present, returns a sequential

Stream

containing
only that value, otherwise returns an empty

Stream

.

Stream<Optional<T>> os = ..
Stream<T> s = os.flatMap(Optional::stream)

orElse

```java
public
T
orElse​(
T
other)
```

If a value is present, returns the value, otherwise returns

other

.

**Parameters:** other

- the value to be returned, if no value is present.
May be

null

.
**Returns:** the value, if present, otherwise

other

---

#### orElse

public

T

orElse​(

T

other)

If a value is present, returns the value, otherwise returns

other

.

orElseGet

```java
public
T
orElseGet​(
Supplier
<? extends
T
> supplier)
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

public

T

orElseGet​(

Supplier

<? extends

T

> supplier)

If a value is present, returns the value, otherwise returns the result
produced by the supplying function.

orElseThrow

```java
public
T
orElseThrow()
```

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

**Returns:** the non-

null

value described by this

Optional
**Throws:** NoSuchElementException

- if no value is present
**Since:** 10

---

#### orElseThrow

public

T

orElseThrow()

If a value is present, returns the value, otherwise throws

NoSuchElementException

.

orElseThrow

```java
public <X extends
Throwable
>
T
orElseThrow​(
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

>

T

orElseThrow​(

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

Optional

.
The other object is considered equal if:

- it is also an

Optional

and;

both instances have no value present or;

the present values are "equal to" each other via

equals()

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

Optional

.
The other object is considered equal if:

- it is also an

Optional

and;

both instances have no value present or;

the present values are "equal to" each other via

equals()

.

it is also an

Optional

and;

both instances have no value present or;

the present values are "equal to" each other via

equals()

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

Optional

suitable for debugging. The exact presentation format is unspecified and
may vary between implementations and versions.

**Overrides:** toString

in class

Object
**Implementation Requirements:** If a value is present the result must include its string representation
in the result. Empty and present

Optional

s must be unambiguously
differentiable.
**Returns:** the string representation of this instance

---

#### toString

public

String

toString()

Returns a non-empty string representation of this

Optional

suitable for debugging. The exact presentation format is unspecified and
may vary between implementations and versions.

---

