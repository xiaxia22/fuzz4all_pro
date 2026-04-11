# Interface PrimitiveValue

**Source:** `jdk.jdi\com\sun\jdi\PrimitiveValue.html`

### Class Description

```java
public interface
PrimitiveValue

extends
Value
```

The value assigned to a field or variable of primitive type in a
target VM. Each primitive values is accessed through a subinterface
of this interface.

**All Superinterfaces:** Mirror

,

Value

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean booleanValue()

Converts this value to a BooleanValue and returns the result
as a boolean.

**Returns:**
- true

if this value is non-zero (or

true

if already a BooleanValue); false otherwise.

---

#### byte byteValue()

Converts this value to a ByteValue and returns the result
as a byte. The value will be narrowed as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a byte).

**Returns:**
- the value, converted to byte

---

#### char charValue()

Converts this value to a CharValue and returns the result
as a char. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a char,
in the narrowing case).

**Returns:**
- the value, converted to char

---

#### short shortValue()

Converts this value to a ShortValue and returns the result
as a short. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a short,
in the narrowing case).

**Returns:**
- the value, converted to short

---

#### int intValue()

Converts this value to an IntegerValue and returns the result
as an int. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to an int,
in the narrowing case).

**Returns:**
- the value, converted to int

---

#### long longValue()

Converts this value to a LongValue and returns the result
as a long. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a long,
in the narrowing case).

**Returns:**
- the value, converted to long

---

#### float floatValue()

Converts this value to a FloatValue and returns the result
as a float. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a float,
in the narrowing case).

**Returns:**
- the value, converted to float

---

#### double doubleValue()

Converts this value to a DoubleValue and returns the result
as a double. The value will be widened as
necessary, and precision information
may be lost.

**Returns:**
- the value, converted to double

---

### Additional Sections

#### Interface PrimitiveValue

**All Superinterfaces:** Mirror

,

Value

**All Known Subinterfaces:** BooleanValue

,

ByteValue

,

CharValue

,

DoubleValue

,

FloatValue

,

IntegerValue

,

LongValue

,

ShortValue

```java
public interface
PrimitiveValue

extends
Value
```

The value assigned to a field or variable of primitive type in a
target VM. Each primitive values is accessed through a subinterface
of this interface.

**Since:** 1.3

public interface

PrimitiveValue

extends

Value

The value assigned to a field or variable of primitive type in a
target VM. Each primitive values is accessed through a subinterface
of this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

booleanValue

()

Converts this value to a BooleanValue and returns the result
as a boolean.

byte

byteValue

()

Converts this value to a ByteValue and returns the result
as a byte.

char

charValue

()

Converts this value to a CharValue and returns the result
as a char.

double

doubleValue

()

Converts this value to a DoubleValue and returns the result
as a double.

float

floatValue

()

Converts this value to a FloatValue and returns the result
as a float.

int

intValue

()

Converts this value to an IntegerValue and returns the result
as an int.

long

longValue

()

Converts this value to a LongValue and returns the result
as a long.

short

shortValue

()

Converts this value to a ShortValue and returns the result
as a short.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

Value

type

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

booleanValue

()

Converts this value to a BooleanValue and returns the result
as a boolean.

byte

byteValue

()

Converts this value to a ByteValue and returns the result
as a byte.

char

charValue

()

Converts this value to a CharValue and returns the result
as a char.

double

doubleValue

()

Converts this value to a DoubleValue and returns the result
as a double.

float

floatValue

()

Converts this value to a FloatValue and returns the result
as a float.

int

intValue

()

Converts this value to an IntegerValue and returns the result
as an int.

long

longValue

()

Converts this value to a LongValue and returns the result
as a long.

short

shortValue

()

Converts this value to a ShortValue and returns the result
as a short.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

Value

type

---

#### Method Summary

Converts this value to a BooleanValue and returns the result
as a boolean.

Converts this value to a ByteValue and returns the result
as a byte.

Converts this value to a CharValue and returns the result
as a char.

Converts this value to a DoubleValue and returns the result
as a double.

Converts this value to a FloatValue and returns the result
as a float.

Converts this value to an IntegerValue and returns the result
as an int.

Converts this value to a LongValue and returns the result
as a long.

Converts this value to a ShortValue and returns the result
as a short.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface com.sun.jdi.

Value

type

---

#### Methods declared in interface com.sun.jdi. Value

============ METHOD DETAIL ==========

- Method Detail

- booleanValue

```java
boolean booleanValue()
```

Converts this value to a BooleanValue and returns the result
as a boolean.

**Returns:** true

if this value is non-zero (or

true

if already a BooleanValue); false otherwise.

- byteValue

```java
byte byteValue()
```

Converts this value to a ByteValue and returns the result
as a byte. The value will be narrowed as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a byte).

**Returns:** the value, converted to byte

- charValue

```java
char charValue()
```

Converts this value to a CharValue and returns the result
as a char. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a char,
in the narrowing case).

**Returns:** the value, converted to char

- shortValue

```java
short shortValue()
```

Converts this value to a ShortValue and returns the result
as a short. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a short,
in the narrowing case).

**Returns:** the value, converted to short

- intValue

```java
int intValue()
```

Converts this value to an IntegerValue and returns the result
as an int. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to an int,
in the narrowing case).

**Returns:** the value, converted to int

- longValue

```java
long longValue()
```

Converts this value to a LongValue and returns the result
as a long. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a long,
in the narrowing case).

**Returns:** the value, converted to long

- floatValue

```java
float floatValue()
```

Converts this value to a FloatValue and returns the result
as a float. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a float,
in the narrowing case).

**Returns:** the value, converted to float

- doubleValue

```java
double doubleValue()
```

Converts this value to a DoubleValue and returns the result
as a double. The value will be widened as
necessary, and precision information
may be lost.

**Returns:** the value, converted to double

Method Detail

- booleanValue

```java
boolean booleanValue()
```

Converts this value to a BooleanValue and returns the result
as a boolean.

**Returns:** true

if this value is non-zero (or

true

if already a BooleanValue); false otherwise.

- byteValue

```java
byte byteValue()
```

Converts this value to a ByteValue and returns the result
as a byte. The value will be narrowed as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a byte).

**Returns:** the value, converted to byte

- charValue

```java
char charValue()
```

Converts this value to a CharValue and returns the result
as a char. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a char,
in the narrowing case).

**Returns:** the value, converted to char

- shortValue

```java
short shortValue()
```

Converts this value to a ShortValue and returns the result
as a short. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a short,
in the narrowing case).

**Returns:** the value, converted to short

- intValue

```java
int intValue()
```

Converts this value to an IntegerValue and returns the result
as an int. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to an int,
in the narrowing case).

**Returns:** the value, converted to int

- longValue

```java
long longValue()
```

Converts this value to a LongValue and returns the result
as a long. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a long,
in the narrowing case).

**Returns:** the value, converted to long

- floatValue

```java
float floatValue()
```

Converts this value to a FloatValue and returns the result
as a float. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a float,
in the narrowing case).

**Returns:** the value, converted to float

- doubleValue

```java
double doubleValue()
```

Converts this value to a DoubleValue and returns the result
as a double. The value will be widened as
necessary, and precision information
may be lost.

**Returns:** the value, converted to double

---

#### Method Detail

booleanValue

```java
boolean booleanValue()
```

Converts this value to a BooleanValue and returns the result
as a boolean.

**Returns:** true

if this value is non-zero (or

true

if already a BooleanValue); false otherwise.

---

#### booleanValue

boolean booleanValue()

Converts this value to a BooleanValue and returns the result
as a boolean.

byteValue

```java
byte byteValue()
```

Converts this value to a ByteValue and returns the result
as a byte. The value will be narrowed as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a byte).

**Returns:** the value, converted to byte

---

#### byteValue

byte byteValue()

Converts this value to a ByteValue and returns the result
as a byte. The value will be narrowed as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a byte).

charValue

```java
char charValue()
```

Converts this value to a CharValue and returns the result
as a char. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a char,
in the narrowing case).

**Returns:** the value, converted to char

---

#### charValue

char charValue()

Converts this value to a CharValue and returns the result
as a char. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a char,
in the narrowing case).

shortValue

```java
short shortValue()
```

Converts this value to a ShortValue and returns the result
as a short. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a short,
in the narrowing case).

**Returns:** the value, converted to short

---

#### shortValue

short shortValue()

Converts this value to a ShortValue and returns the result
as a short. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a short,
in the narrowing case).

intValue

```java
int intValue()
```

Converts this value to an IntegerValue and returns the result
as an int. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to an int,
in the narrowing case).

**Returns:** the value, converted to int

---

#### intValue

int intValue()

Converts this value to an IntegerValue and returns the result
as an int. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to an int,
in the narrowing case).

longValue

```java
long longValue()
```

Converts this value to a LongValue and returns the result
as a long. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a long,
in the narrowing case).

**Returns:** the value, converted to long

---

#### longValue

long longValue()

Converts this value to a LongValue and returns the result
as a long. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a long,
in the narrowing case).

floatValue

```java
float floatValue()
```

Converts this value to a FloatValue and returns the result
as a float. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a float,
in the narrowing case).

**Returns:** the value, converted to float

---

#### floatValue

float floatValue()

Converts this value to a FloatValue and returns the result
as a float. The value will be narrowed or widened as
necessary, and magnitude or precision information
may be lost (as if the primitive had been cast to a float,
in the narrowing case).

doubleValue

```java
double doubleValue()
```

Converts this value to a DoubleValue and returns the result
as a double. The value will be widened as
necessary, and precision information
may be lost.

**Returns:** the value, converted to double

---

#### doubleValue

double doubleValue()

Converts this value to a DoubleValue and returns the result
as a double. The value will be widened as
necessary, and precision information
may be lost.

---

