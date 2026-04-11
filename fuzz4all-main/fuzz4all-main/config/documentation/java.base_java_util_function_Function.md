# Interface Function<T,​R>

**Source:** `java.base\java\util\function\Function.html`

### Class Description

```java
@FunctionalInterface

public interface
Function<T,​R>
```

Represents a function that accepts one argument and produces a result.

This is a

functional interface

whose functional method is

apply(Object)

.

**Type Parameters:** T

- the type of the input to the function
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
t)

Applies this function to the given argument.

**Parameters:**
- t

- the function argument

**Returns:**
- the function result

---

#### default <V>
Function
<V,​
R
> compose​(
Function
<? super V,​? extends
T
> before)

Returns a composed function that first applies the

before

function to its input, and then applies this function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

**Parameters:**
- before

- the function to apply before this function is applied

**Returns:**
- a composed function that first applies the

before

function and then applies this function

**Throws:**
- NullPointerException

- if before is null

**See Also:**
- andThen(Function)

**Type Parameters:**
- V

- the type of input to the

before

function, and to the
composed function

---

#### default <V>
Function
<
T
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

**See Also:**
- compose(Function)

**Type Parameters:**
- V

- the type of output of the

after

function, and of the
composed function

---

#### static <T>
Function
<T,​T> identity()

Returns a function that always returns its input argument.

**Returns:**
- a function that always returns its input argument

**Type Parameters:**
- T

- the type of the input and output objects to the function

---

### Additional Sections

#### Interface Function<T,​R>

**Type Parameters:** T

- the type of the input to the function
**Type Parameters:** R

- the type of the result of the function

**All Known Subinterfaces:** UnaryOperator

<T>

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
Function<T,​R>
```

Represents a function that accepts one argument and produces a result.

This is a

functional interface

whose functional method is

apply(Object)

.

**Since:** 1.8

@FunctionalInterface

public interface

Function<T,​R>

Represents a function that accepts one argument and produces a result.

This is a

functional interface

whose functional method is

apply(Object)

.

This is a

functional interface

whose functional method is

apply(Object)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default <V>

Function

<

T

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

t)

Applies this function to the given argument.

default <V>

Function

<V,​

R

>

compose

​(

Function

<? super V,​? extends

T

> before)

Returns a composed function that first applies the

before

function to its input, and then applies this function to the result.

static <T>

Function

<T,​T>

identity

()

Returns a function that always returns its input argument.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default <V>

Function

<

T

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

t)

Applies this function to the given argument.

default <V>

Function

<V,​

R

>

compose

​(

Function

<? super V,​? extends

T

> before)

Returns a composed function that first applies the

before

function to its input, and then applies this function to the result.

static <T>

Function

<T,​T>

identity

()

Returns a function that always returns its input argument.

---

#### Method Summary

Returns a composed function that first applies this function to
its input, and then applies the

after

function to the result.

Applies this function to the given argument.

Returns a composed function that first applies the

before

function to its input, and then applies this function to the result.

Returns a function that always returns its input argument.

============ METHOD DETAIL ==========

- Method Detail

- apply

```java
R
apply​(
T
t)
```

Applies this function to the given argument.

**Parameters:** t

- the function argument
**Returns:** the function result

- compose

```java
default <V>
Function
<V,​
R
> compose​(
Function
<? super V,​? extends
T
> before)
```

Returns a composed function that first applies the

before

function to its input, and then applies this function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

**Type Parameters:** V

- the type of input to the

before

function, and to the
composed function
**Parameters:** before

- the function to apply before this function is applied
**Returns:** a composed function that first applies the

before

function and then applies this function
**Throws:** NullPointerException

- if before is null
**See Also:** andThen(Function)

- andThen

```java
default <V>
Function
<
T
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
**See Also:** compose(Function)

- identity

```java
static <T>
Function
<T,​T> identity()
```

Returns a function that always returns its input argument.

**Type Parameters:** T

- the type of the input and output objects to the function
**Returns:** a function that always returns its input argument

Method Detail

- apply

```java
R
apply​(
T
t)
```

Applies this function to the given argument.

**Parameters:** t

- the function argument
**Returns:** the function result

- compose

```java
default <V>
Function
<V,​
R
> compose​(
Function
<? super V,​? extends
T
> before)
```

Returns a composed function that first applies the

before

function to its input, and then applies this function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

**Type Parameters:** V

- the type of input to the

before

function, and to the
composed function
**Parameters:** before

- the function to apply before this function is applied
**Returns:** a composed function that first applies the

before

function and then applies this function
**Throws:** NullPointerException

- if before is null
**See Also:** andThen(Function)

- andThen

```java
default <V>
Function
<
T
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
**See Also:** compose(Function)

- identity

```java
static <T>
Function
<T,​T> identity()
```

Returns a function that always returns its input argument.

**Type Parameters:** T

- the type of the input and output objects to the function
**Returns:** a function that always returns its input argument

---

#### Method Detail

apply

```java
R
apply​(
T
t)
```

Applies this function to the given argument.

**Parameters:** t

- the function argument
**Returns:** the function result

---

#### apply

R

apply​(

T

t)

Applies this function to the given argument.

compose

```java
default <V>
Function
<V,​
R
> compose​(
Function
<? super V,​? extends
T
> before)
```

Returns a composed function that first applies the

before

function to its input, and then applies this function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

**Type Parameters:** V

- the type of input to the

before

function, and to the
composed function
**Parameters:** before

- the function to apply before this function is applied
**Returns:** a composed function that first applies the

before

function and then applies this function
**Throws:** NullPointerException

- if before is null
**See Also:** andThen(Function)

---

#### compose

default <V>

Function

<V,​

R

> compose​(

Function

<? super V,​? extends

T

> before)

Returns a composed function that first applies the

before

function to its input, and then applies this function to the result.
If evaluation of either function throws an exception, it is relayed to
the caller of the composed function.

andThen

```java
default <V>
Function
<
T
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
**See Also:** compose(Function)

---

#### andThen

default <V>

Function

<

T

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

identity

```java
static <T>
Function
<T,​T> identity()
```

Returns a function that always returns its input argument.

**Type Parameters:** T

- the type of the input and output objects to the function
**Returns:** a function that always returns its input argument

---

#### identity

static <T>

Function

<T,​T> identity()

Returns a function that always returns its input argument.

---

