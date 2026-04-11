# Interface ByteValue

**Source:** `jdk.jdi\com\sun\jdi\ByteValue.html`

### Class Description

```java
public interface
ByteValue

extends
PrimitiveValue
,
Comparable
<
ByteValue
>
```

Provides access to a primitive

byte

value in the target VM.

**All Superinterfaces:** Comparable

<

ByteValue

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

#### byte value()

Returns this ByteValue as a

byte

.

**Returns:**
- the

byte

mirrored by this object.

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this ByteValue for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is a ByteValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this BooleanValue.

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

#### Interface ByteValue

**All Superinterfaces:** Comparable

<

ByteValue

>

,

Mirror

,

PrimitiveValue

,

Value

```java
public interface
ByteValue

extends
PrimitiveValue
,
Comparable
<
ByteValue
>
```

Provides access to a primitive

byte

value in the target VM.

**Since:** 1.3

public interface

ByteValue

extends

PrimitiveValue

,

Comparable

<

ByteValue

>

Provides access to a primitive

byte

value in the target VM.

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

Compares the specified Object with this ByteValue for equality.

int

hashCode

()

Returns the hash code value for this BooleanValue.

byte

value

()

Returns this ByteValue as a

byte

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

Compares the specified Object with this ByteValue for equality.

int

hashCode

()

Returns the hash code value for this BooleanValue.

byte

value

()

Returns this ByteValue as a

byte

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

Compares the specified Object with this ByteValue for equality.

Returns the hash code value for this BooleanValue.

Returns this ByteValue as a

byte

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
byte value()
```

Returns this ByteValue as a

byte

.

**Returns:** the

byte

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this ByteValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a ByteValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this BooleanValue.

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
byte value()
```

Returns this ByteValue as a

byte

.

**Returns:** the

byte

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this ByteValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a ByteValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this BooleanValue.

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
byte value()
```

Returns this ByteValue as a

byte

.

**Returns:** the

byte

mirrored by this object.

---

#### value

byte value()

Returns this ByteValue as a

byte

.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this ByteValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a ByteValue and if applying "=="
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

Compares the specified Object with this ByteValue for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this BooleanValue.

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

Returns the hash code value for this BooleanValue.

---

