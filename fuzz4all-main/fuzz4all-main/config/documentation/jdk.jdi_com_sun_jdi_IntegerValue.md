# Interface IntegerValue

**Source:** `jdk.jdi\com\sun\jdi\IntegerValue.html`

### Class Description

```java
public interface
IntegerValue

extends
PrimitiveValue
,
Comparable
<
IntegerValue
>
```

Provides access to a primitive

int

value in
the target VM.

**All Superinterfaces:** Comparable

<

IntegerValue

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

#### int value()

Returns this IntegerValue as an int.

**Returns:**
- the

int

mirrored by this object.

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this IntegerValue for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is an IntegerValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this IntegerValue.

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

#### Interface IntegerValue

**All Superinterfaces:** Comparable

<

IntegerValue

>

,

Mirror

,

PrimitiveValue

,

Value

```java
public interface
IntegerValue

extends
PrimitiveValue
,
Comparable
<
IntegerValue
>
```

Provides access to a primitive

int

value in
the target VM.

**Since:** 1.3

public interface

IntegerValue

extends

PrimitiveValue

,

Comparable

<

IntegerValue

>

Provides access to a primitive

int

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

Compares the specified Object with this IntegerValue for equality.

int

hashCode

()

Returns the hash code value for this IntegerValue.

int

value

()

Returns this IntegerValue as an int.

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

Compares the specified Object with this IntegerValue for equality.

int

hashCode

()

Returns the hash code value for this IntegerValue.

int

value

()

Returns this IntegerValue as an int.

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

Compares the specified Object with this IntegerValue for equality.

Returns the hash code value for this IntegerValue.

Returns this IntegerValue as an int.

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
int value()
```

Returns this IntegerValue as an int.

**Returns:** the

int

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this IntegerValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is an IntegerValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this IntegerValue.

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
int value()
```

Returns this IntegerValue as an int.

**Returns:** the

int

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this IntegerValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is an IntegerValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this IntegerValue.

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
int value()
```

Returns this IntegerValue as an int.

**Returns:** the

int

mirrored by this object.

---

#### value

int value()

Returns this IntegerValue as an int.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this IntegerValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is an IntegerValue and if applying "=="
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

Compares the specified Object with this IntegerValue for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this IntegerValue.

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

Returns the hash code value for this IntegerValue.

---

