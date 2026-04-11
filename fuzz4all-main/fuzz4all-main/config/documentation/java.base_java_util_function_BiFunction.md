# Interface BiFunction<T,​U,​R>

**Source:** `java.base\java\util\function\BiFunction.html`

### Class Description

```java
@FunctionalInterface

public interface
BiFunction<T,​U,​R>
```

Represents a function that accepts two arguments and produces a result.
This is the two-arity specialization of

Function

.

This is a

functional interface

whose functional method is

apply(Object, Object)

.

**Type Parameters:** T

- the type of the first argument to the function
**Type Parameters:** U

- the type of the second argument to the function
**Type Parameters:** R

- the type of the result of the function

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### R
apply​(
T
t,

U
u)

Applies this function to the given arguments.

**Parameters:**
- t

- the first function argument
- u

- the second function argument

**Returns:**
- the function result

---

#### default <V>
BiFunction
<
T
,​
U
,​V> andThen​(
Function
<? super
R
,​? extends V> after)

Returns a composed function that first applies this function to
its input, and then applies the

after

function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

**Parameters:**
- after

- the function to apply after this function is applied

**Returns:**
- a composed function that first applies this function and then
applies the

after

function

**Throws:**
- NullPointerException

- if after is null

**Type Parameters:**
- V

- the type of output of the

after

function, and of the
composed function

---

### Additional Sections

#### Interface BiFunction<T,​U,​R>

**Type Parameters:** T

- the type of the first argument to the function
**Type Parameters:** U

- the type of the second argument to the function
**Type Parameters:** R

- the type of the result of the function

**All Known Subinterfaces:** BinaryOperator

<T>

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
BiFunction<T,​U,​R>
```

Represents a function that accepts two arguments and produces a result.
This is the two-arity specialization of

Function

.

This is a

functional interface

whose functional method is

apply(Object, Object)

.

**Since:** 1.8
**See Also:** Function

@FunctionalInterface

public interface

BiFunction<T,​U,​R>

Represents a function that accepts two arguments and produces a result.
This is the two-arity specialization of

Function

.

This is a

functional interface

whose functional method is

apply(Object, Object)

.

This is a

functional interface

whose functional method is

apply(Object, Object)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default <V>

BiFunction

<

T

,​

U

,​V>

andThen

​(

Function

<? super

R

,​? extends V> after)

Returns a composed function that first applies this function to
its input, and then applies the

after

function to the result.

R

apply

​(

T

t,

U

u)

Applies this function to the given arguments.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default <V>

BiFunction

<

T

,​

U

,​V>

andThen

​(

Function

<? super

R

,​? extends V> after)

Returns a composed function that first applies this function to
its input, and then applies the

after

function to the result.

R

apply

​(

T

t,

U

u)

Applies this function to the given arguments.

---

#### Method Summary

Returns a composed function that first applies this function to
its input, and then applies the

after

function to the result.

Applies this function to the given arguments.

============ METHOD DETAIL ==========

- Method Detail

- apply

```java
R
apply​(
T
t,

U
u)
```

Applies this function to the given arguments.

**Parameters:** t

- the first function argument
**Parameters:** u

- the second function argument
**Returns:** the function result

- andThen

```java
default <V>
BiFunction
<
T
,​
U
,​V> andThen​(
Function
<? super
R
,​? extends V> after)
```

Returns a composed function that first applies this function to
its input, and then applies the

after

function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

**Type Parameters:** V

- the type of output of the

after

function, and of the
composed function
**Parameters:** after

- the function to apply after this function is applied
**Returns:** a composed function that first applies this function and then
applies the

after

function
**Throws:** NullPointerException

- if after is null

Method Detail

- apply

```java
R
apply​(
T
t,

U
u)
```

Applies this function to the given arguments.

**Parameters:** t

- the first function argument
**Parameters:** u

- the second function argument
**Returns:** the function result

- andThen

```java
default <V>
BiFunction
<
T
,​
U
,​V> andThen​(
Function
<? super
R
,​? extends V> after)
```

Returns a composed function that first applies this function to
its input, and then applies the

after

function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

**Type Parameters:** V

- the type of output of the

after

function, and of the
composed function
**Parameters:** after

- the function to apply after this function is applied
**Returns:** a composed function that first applies this function and then
applies the

after

function
**Throws:** NullPointerException

- if after is null

---

#### Method Detail

apply

```java
R
apply​(
T
t,

U
u)
```

Applies this function to the given arguments.

**Parameters:** t

- the first function argument
**Parameters:** u

- the second function argument
**Returns:** the function result

---

#### apply

R

apply​(

T

t,

U

u)

Applies this function to the given arguments.

andThen

```java
default <V>
BiFunction
<
T
,​
U
,​V> andThen​(
Function
<? super
R
,​? extends V> after)
```

Returns a composed function that first applies this function to
its input, and then applies the

after

function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

**Type Parameters:** V

- the type of output of the

after

function, and of the
composed function
**Parameters:** after

- the function to apply after this function is applied
**Returns:** a composed function that first applies this function and then
applies the

after

function
**Throws:** NullPointerException

- if after is null

---

#### andThen

default <V>

BiFunction

<

T

,​

U

,​V> andThen​(

Function

<? super

R

,​? extends V> after)

Returns a composed function that first applies this function to
its input, and then applies the

after

function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

---

