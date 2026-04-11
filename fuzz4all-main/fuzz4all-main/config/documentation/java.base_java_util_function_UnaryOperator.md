# Interface UnaryOperator<T>

**Source:** `java.base\java\util\function\UnaryOperator.html`

### Class Description

```java
@FunctionalInterface

public interface
UnaryOperator<T>

extends
Function
<T,​T>
```

Represents an operation on a single operand that produces a result of the
same type as its operand. This is a specialization of

Function

for
the case where the operand and result are of the same type.

This is a

functional interface

whose functional method is

Function.apply(Object)

.

**Type Parameters:** T

- the type of the operand and result of the operator

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### static <T>
UnaryOperator
<T> identity()

Returns a unary operator that always returns its input argument.

**Returns:**
- a unary operator that always returns its input argument

**Type Parameters:**
- T

- the type of the input and output of the operator

---

### Additional Sections

#### Interface UnaryOperator<T>

**Type Parameters:** T

- the type of the operand and result of the operator

**All Superinterfaces:** Function

<T,​T>

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
UnaryOperator<T>

extends
Function
<T,​T>
```

Represents an operation on a single operand that produces a result of the
same type as its operand. This is a specialization of

Function

for
the case where the operand and result are of the same type.

This is a

functional interface

whose functional method is

Function.apply(Object)

.

**Since:** 1.8
**See Also:** Function

@FunctionalInterface

public interface

UnaryOperator<T>

extends

Function

<T,​T>

Represents an operation on a single operand that produces a result of the
same type as its operand. This is a specialization of

Function

for
the case where the operand and result are of the same type.

This is a

functional interface

whose functional method is

Function.apply(Object)

.

This is a

functional interface

whose functional method is

Function.apply(Object)

.

========== METHOD SUMMARY ===========

- Method Summary

Static Methods

Modifier and Type

Method

Description

static <T>

UnaryOperator

<T>

identity

()

Returns a unary operator that always returns its input argument.

- Methods declared in interface java.util.function.

Function

andThen

,

apply

,

compose

Method Summary

Static Methods

Modifier and Type

Method

Description

static <T>

UnaryOperator

<T>

identity

()

Returns a unary operator that always returns its input argument.

- Methods declared in interface java.util.function.

Function

andThen

,

apply

,

compose

---

#### Method Summary

Returns a unary operator that always returns its input argument.

Methods declared in interface java.util.function.

Function

andThen

,

apply

,

compose

---

#### Methods declared in interface java.util.function. Function

============ METHOD DETAIL ==========

- Method Detail

- identity

```java
static <T>
UnaryOperator
<T> identity()
```

Returns a unary operator that always returns its input argument.

**Type Parameters:** T

- the type of the input and output of the operator
**Returns:** a unary operator that always returns its input argument

Method Detail

- identity

```java
static <T>
UnaryOperator
<T> identity()
```

Returns a unary operator that always returns its input argument.

**Type Parameters:** T

- the type of the input and output of the operator
**Returns:** a unary operator that always returns its input argument

---

#### Method Detail

identity

```java
static <T>
UnaryOperator
<T> identity()
```

Returns a unary operator that always returns its input argument.

**Type Parameters:** T

- the type of the input and output of the operator
**Returns:** a unary operator that always returns its input argument

---

#### identity

static <T>

UnaryOperator

<T> identity()

Returns a unary operator that always returns its input argument.

---

