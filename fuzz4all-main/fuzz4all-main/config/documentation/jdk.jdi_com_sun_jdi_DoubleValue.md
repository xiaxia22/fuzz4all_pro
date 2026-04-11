# Interface DoubleValue

**Source:** `jdk.jdi\com\sun\jdi\DoubleValue.html`

### Class Description

```java
public interface
DoubleValue

extends
PrimitiveValue
,
Comparable
<
DoubleValue
>
```

Provides access to a primitive

double

value in
the target VM.

**All Superinterfaces:** Comparable

<

DoubleValue

>

,

Mirror

,

PrimitiveValue

,

Value

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### double value()

Returns this DoubleValue as a

double

.

**Returns:**
- the

double

mirrored by this object.

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this DoubleValue for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is a DoubleValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this DoubleValue.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the integer hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Interface DoubleValue

**All Superinterfaces:** Comparable

<

DoubleValue

>

,

Mirror

,

PrimitiveValue

,

Value

```java
public interface
DoubleValue

extends
PrimitiveValue
,
Comparable
<
DoubleValue
>
```

Provides access to a primitive

double

value in
the target VM.

**Since:** 1.3

public interface

DoubleValue

extends

PrimitiveValue

,

Comparable

<

DoubleValue

>

Provides access to a primitive

double

value in
the target VM.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares the specified Object with this DoubleValue for equality.

int

hashCode

()

Returns the hash code value for this DoubleValue.

double

value

()

Returns this DoubleValue as a

double

.

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

PrimitiveValue

booleanValue

,

byteValue

,

charValue

,

doubleValue

,

floatValue

,

intValue

,

longValue

,

shortValue

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

equals

​(

Object

obj)

Compares the specified Object with this DoubleValue for equality.

int

hashCode

()

Returns the hash code value for this DoubleValue.

double

value

()

Returns this DoubleValue as a

double

.

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

PrimitiveValue

booleanValue

,

byteValue

,

charValue

,

doubleValue

,

floatValue

,

intValue

,

longValue

,

shortValue

- Methods declared in interface com.sun.jdi.

Value

type

---

#### Method Summary

Compares the specified Object with this DoubleValue for equality.

Returns the hash code value for this DoubleValue.

Returns this DoubleValue as a

double

.

Methods declared in interface java.lang.

Comparable

compareTo

---

#### Methods declared in interface java.lang. Comparable

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface com.sun.jdi.

PrimitiveValue

booleanValue

,

byteValue

,

charValue

,

doubleValue

,

floatValue

,

intValue

,

longValue

,

shortValue

---

#### Methods declared in interface com.sun.jdi. PrimitiveValue

Methods declared in interface com.sun.jdi.

Value

type

---

#### Methods declared in interface com.sun.jdi. Value

============ METHOD DETAIL ==========

- Method Detail

- value

```java
double value()
```

Returns this DoubleValue as a

double

.

**Returns:** the

double

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this DoubleValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a DoubleValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this DoubleValue.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Method Detail

- value

```java
double value()
```

Returns this DoubleValue as a

double

.

**Returns:** the

double

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this DoubleValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a DoubleValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this DoubleValue.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

value

```java
double value()
```

Returns this DoubleValue as a

double

.

**Returns:** the

double

mirrored by this object.

---

#### value

double value()

Returns this DoubleValue as a

double

.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this DoubleValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a DoubleValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Compares the specified Object with this DoubleValue for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this DoubleValue.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this DoubleValue.

---

