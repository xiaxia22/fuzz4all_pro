# Interface FloatValue

**Source:** `jdk.jdi\com\sun\jdi\FloatValue.html`

### Class Description

```java
public interface
FloatValue

extends
PrimitiveValue
,
Comparable
<
FloatValue
>
```

Provides access to a primitive

float

value in
the target VM.

**All Superinterfaces:** Comparable

<

FloatValue

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

#### float value()

Returns this FloatValue as a float.

**Returns:**
- the

float

mirrored by this object.

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this FloatValue for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is a FloatValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this FloatValue.

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

#### Interface FloatValue

**All Superinterfaces:** Comparable

<

FloatValue

>

,

Mirror

,

PrimitiveValue

,

Value

```java
public interface
FloatValue

extends
PrimitiveValue
,
Comparable
<
FloatValue
>
```

Provides access to a primitive

float

value in
the target VM.

**Since:** 1.3

public interface

FloatValue

extends

PrimitiveValue

,

Comparable

<

FloatValue

>

Provides access to a primitive

float

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

Compares the specified Object with this FloatValue for equality.

int

hashCode

()

Returns the hash code value for this FloatValue.

float

value

()

Returns this FloatValue as a float.

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

Compares the specified Object with this FloatValue for equality.

int

hashCode

()

Returns the hash code value for this FloatValue.

float

value

()

Returns this FloatValue as a float.

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

Compares the specified Object with this FloatValue for equality.

Returns the hash code value for this FloatValue.

Returns this FloatValue as a float.

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
float value()
```

Returns this FloatValue as a float.

**Returns:** the

float

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this FloatValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a FloatValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this FloatValue.

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
float value()
```

Returns this FloatValue as a float.

**Returns:** the

float

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this FloatValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a FloatValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this FloatValue.

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
float value()
```

Returns this FloatValue as a float.

**Returns:** the

float

mirrored by this object.

---

#### value

float value()

Returns this FloatValue as a float.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this FloatValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a FloatValue and if applying "=="
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

Compares the specified Object with this FloatValue for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this FloatValue.

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

Returns the hash code value for this FloatValue.

---

