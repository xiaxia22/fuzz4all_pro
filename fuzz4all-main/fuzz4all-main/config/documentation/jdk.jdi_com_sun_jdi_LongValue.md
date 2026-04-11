# Interface LongValue

**Source:** `jdk.jdi\com\sun\jdi\LongValue.html`

### Class Description

```java
public interface
LongValue

extends
PrimitiveValue
,
Comparable
<
LongValue
>
```

Provides access to a primitive

long

value in
the target VM.

**All Superinterfaces:** Comparable

<

LongValue

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

#### long value()

Returns this LongValue as a long.

**Returns:**
- the

long

mirrored by this object.

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this LongValue for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is a LongValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this LongValue.

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

#### Interface LongValue

**All Superinterfaces:** Comparable

<

LongValue

>

,

Mirror

,

PrimitiveValue

,

Value

```java
public interface
LongValue

extends
PrimitiveValue
,
Comparable
<
LongValue
>
```

Provides access to a primitive

long

value in
the target VM.

**Since:** 1.3

public interface

LongValue

extends

PrimitiveValue

,

Comparable

<

LongValue

>

Provides access to a primitive

long

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

Compares the specified Object with this LongValue for equality.

int

hashCode

()

Returns the hash code value for this LongValue.

long

value

()

Returns this LongValue as a long.

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

Compares the specified Object with this LongValue for equality.

int

hashCode

()

Returns the hash code value for this LongValue.

long

value

()

Returns this LongValue as a long.

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

Compares the specified Object with this LongValue for equality.

Returns the hash code value for this LongValue.

Returns this LongValue as a long.

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
long value()
```

Returns this LongValue as a long.

**Returns:** the

long

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this LongValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a LongValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this LongValue.

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
long value()
```

Returns this LongValue as a long.

**Returns:** the

long

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this LongValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a LongValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this LongValue.

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
long value()
```

Returns this LongValue as a long.

**Returns:** the

long

mirrored by this object.

---

#### value

long value()

Returns this LongValue as a long.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this LongValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a LongValue and if applying "=="
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

Compares the specified Object with this LongValue for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this LongValue.

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

Returns the hash code value for this LongValue.

---

