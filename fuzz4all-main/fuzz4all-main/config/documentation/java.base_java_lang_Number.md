# Class Number

**Source:** `java.base\java\lang\Number.html`

### Class Description

```java
public abstract class
Number

extends
Object

implements
Serializable
```

The abstract class

Number

is the superclass of platform
classes representing numeric values that are convertible to the
primitive types

byte

,

double

,

float

,

int

,

long

, and

short

.

The specific semantics of the conversion from the numeric value of
a particular

Number

implementation to a given primitive
type is defined by the

Number

implementation in question.

For platform classes, the conversion is often analogous to a
narrowing primitive conversion or a widening primitive conversion
as defined in

The Java™ Language Specification

for converting between primitive types. Therefore, conversions may
lose information about the overall magnitude of a numeric value, may
lose precision, and may even return a result of a different sign
than the input.

See the documentation of a given

Number

implementation for
conversion details.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Number()

*No description found.*

---

### Method Details

#### public abstract int intValue()

Returns the value of the specified number as an

int

.

**Returns:**
- the numeric value represented by this object after conversion
to type

int

.

---

#### public abstract long longValue()

Returns the value of the specified number as a

long

.

**Returns:**
- the numeric value represented by this object after conversion
to type

long

.

---

#### public abstract float floatValue()

Returns the value of the specified number as a

float

.

**Returns:**
- the numeric value represented by this object after conversion
to type

float

.

---

#### public abstract double doubleValue()

Returns the value of the specified number as a

double

.

**Returns:**
- the numeric value represented by this object after conversion
to type

double

.

---

#### public byte byteValue()

Returns the value of the specified number as a

byte

.

This implementation returns the result of

intValue()

cast
to a

byte

.

**Returns:**
- the numeric value represented by this object after conversion
to type

byte

.

**Since:**
- 1.1

---

#### public short shortValue()

Returns the value of the specified number as a

short

.

This implementation returns the result of

intValue()

cast
to a

short

.

**Returns:**
- the numeric value represented by this object after conversion
to type

short

.

**Since:**
- 1.1

---

### Additional Sections

#### Class Number

java.lang.Object

- java.lang.Number

java.lang.Number

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AtomicInteger

,

AtomicLong

,

BigDecimal

,

BigInteger

,

Byte

,

Double

,

DoubleAccumulator

,

DoubleAdder

,

Float

,

Integer

,

Long

,

LongAccumulator

,

LongAdder

,

Short

```java
public abstract class
Number

extends
Object

implements
Serializable
```

The abstract class

Number

is the superclass of platform
classes representing numeric values that are convertible to the
primitive types

byte

,

double

,

float

,

int

,

long

, and

short

.

The specific semantics of the conversion from the numeric value of
a particular

Number

implementation to a given primitive
type is defined by the

Number

implementation in question.

For platform classes, the conversion is often analogous to a
narrowing primitive conversion or a widening primitive conversion
as defined in

The Java™ Language Specification

for converting between primitive types. Therefore, conversions may
lose information about the overall magnitude of a numeric value, may
lose precision, and may even return a result of a different sign
than the input.

See the documentation of a given

Number

implementation for
conversion details.

**Since:** 1.0
**See Also:** Serialized Form
**See The Java™ Language Specification :** 5.1.2 Widening Primitive Conversions, 5.1.3 Narrowing Primitive Conversions

public abstract class

Number

extends

Object

implements

Serializable

The abstract class

Number

is the superclass of platform
classes representing numeric values that are convertible to the
primitive types

byte

,

double

,

float

,

int

,

long

, and

short

.

The specific semantics of the conversion from the numeric value of
a particular

Number

implementation to a given primitive
type is defined by the

Number

implementation in question.

For platform classes, the conversion is often analogous to a
narrowing primitive conversion or a widening primitive conversion
as defined in

The Java™ Language Specification

for converting between primitive types. Therefore, conversions may
lose information about the overall magnitude of a numeric value, may
lose precision, and may even return a result of a different sign
than the input.

See the documentation of a given

Number

implementation for
conversion details.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Number

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

byte

byteValue

()

Returns the value of the specified number as a

byte

.

abstract double

doubleValue

()

Returns the value of the specified number as a

double

.

abstract float

floatValue

()

Returns the value of the specified number as a

float

.

abstract int

intValue

()

Returns the value of the specified number as an

int

.

abstract long

longValue

()

Returns the value of the specified number as a

long

.

short

shortValue

()

Returns the value of the specified number as a

short

.

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

Constructor Summary

Constructors

Constructor

Description

Number

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

byte

byteValue

()

Returns the value of the specified number as a

byte

.

abstract double

doubleValue

()

Returns the value of the specified number as a

double

.

abstract float

floatValue

()

Returns the value of the specified number as a

float

.

abstract int

intValue

()

Returns the value of the specified number as an

int

.

abstract long

longValue

()

Returns the value of the specified number as a

long

.

short

shortValue

()

Returns the value of the specified number as a

short

.

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

Returns the value of the specified number as a

byte

.

Returns the value of the specified number as a

double

.

Returns the value of the specified number as a

float

.

Returns the value of the specified number as an

int

.

Returns the value of the specified number as a

long

.

Returns the value of the specified number as a

short

.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Number

```java
public Number()
```

============ METHOD DETAIL ==========

- Method Detail

- intValue

```java
public abstract int intValue()
```

Returns the value of the specified number as an

int

.

**Returns:** the numeric value represented by this object after conversion
to type

int

.

- longValue

```java
public abstract long longValue()
```

Returns the value of the specified number as a

long

.

**Returns:** the numeric value represented by this object after conversion
to type

long

.

- floatValue

```java
public abstract float floatValue()
```

Returns the value of the specified number as a

float

.

**Returns:** the numeric value represented by this object after conversion
to type

float

.

- doubleValue

```java
public abstract double doubleValue()
```

Returns the value of the specified number as a

double

.

**Returns:** the numeric value represented by this object after conversion
to type

double

.

- byteValue

```java
public byte byteValue()
```

Returns the value of the specified number as a

byte

.

This implementation returns the result of

intValue()

cast
to a

byte

.

**Returns:** the numeric value represented by this object after conversion
to type

byte

.
**Since:** 1.1

- shortValue

```java
public short shortValue()
```

Returns the value of the specified number as a

short

.

This implementation returns the result of

intValue()

cast
to a

short

.

**Returns:** the numeric value represented by this object after conversion
to type

short

.
**Since:** 1.1

Constructor Detail

- Number

```java
public Number()
```

---

#### Constructor Detail

Number

```java
public Number()
```

---

#### Number

public Number()

Method Detail

- intValue

```java
public abstract int intValue()
```

Returns the value of the specified number as an

int

.

**Returns:** the numeric value represented by this object after conversion
to type

int

.

- longValue

```java
public abstract long longValue()
```

Returns the value of the specified number as a

long

.

**Returns:** the numeric value represented by this object after conversion
to type

long

.

- floatValue

```java
public abstract float floatValue()
```

Returns the value of the specified number as a

float

.

**Returns:** the numeric value represented by this object after conversion
to type

float

.

- doubleValue

```java
public abstract double doubleValue()
```

Returns the value of the specified number as a

double

.

**Returns:** the numeric value represented by this object after conversion
to type

double

.

- byteValue

```java
public byte byteValue()
```

Returns the value of the specified number as a

byte

.

This implementation returns the result of

intValue()

cast
to a

byte

.

**Returns:** the numeric value represented by this object after conversion
to type

byte

.
**Since:** 1.1

- shortValue

```java
public short shortValue()
```

Returns the value of the specified number as a

short

.

This implementation returns the result of

intValue()

cast
to a

short

.

**Returns:** the numeric value represented by this object after conversion
to type

short

.
**Since:** 1.1

---

#### Method Detail

intValue

```java
public abstract int intValue()
```

Returns the value of the specified number as an

int

.

**Returns:** the numeric value represented by this object after conversion
to type

int

.

---

#### intValue

public abstract int intValue()

Returns the value of the specified number as an

int

.

longValue

```java
public abstract long longValue()
```

Returns the value of the specified number as a

long

.

**Returns:** the numeric value represented by this object after conversion
to type

long

.

---

#### longValue

public abstract long longValue()

Returns the value of the specified number as a

long

.

floatValue

```java
public abstract float floatValue()
```

Returns the value of the specified number as a

float

.

**Returns:** the numeric value represented by this object after conversion
to type

float

.

---

#### floatValue

public abstract float floatValue()

Returns the value of the specified number as a

float

.

doubleValue

```java
public abstract double doubleValue()
```

Returns the value of the specified number as a

double

.

**Returns:** the numeric value represented by this object after conversion
to type

double

.

---

#### doubleValue

public abstract double doubleValue()

Returns the value of the specified number as a

double

.

byteValue

```java
public byte byteValue()
```

Returns the value of the specified number as a

byte

.

This implementation returns the result of

intValue()

cast
to a

byte

.

**Returns:** the numeric value represented by this object after conversion
to type

byte

.
**Since:** 1.1

---

#### byteValue

public byte byteValue()

Returns the value of the specified number as a

byte

.

This implementation returns the result of

intValue()

cast
to a

byte

.

This implementation returns the result of

intValue()

cast
to a

byte

.

shortValue

```java
public short shortValue()
```

Returns the value of the specified number as a

short

.

This implementation returns the result of

intValue()

cast
to a

short

.

**Returns:** the numeric value represented by this object after conversion
to type

short

.
**Since:** 1.1

---

#### shortValue

public short shortValue()

Returns the value of the specified number as a

short

.

This implementation returns the result of

intValue()

cast
to a

short

.

This implementation returns the result of

intValue()

cast
to a

short

.

---

