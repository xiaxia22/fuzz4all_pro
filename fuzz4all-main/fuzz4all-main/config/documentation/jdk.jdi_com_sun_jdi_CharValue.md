# Interface CharValue

**Source:** `jdk.jdi\com\sun\jdi\CharValue.html`

### Class Description

```java
public interface
CharValue

extends
PrimitiveValue
,
Comparable
<
CharValue
>
```

Provides access to a primitive

char

value in
the target VM.

**All Superinterfaces:** Comparable

<

CharValue

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

#### char value()

Returns this CharValue as a

char

.

**Returns:**
- the

char

mirrored by this object.

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this CharValue for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is a CharValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this CharValue.

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

#### Interface CharValue

**All Superinterfaces:** Comparable

<

CharValue

>

,

Mirror

,

PrimitiveValue

,

Value

```java
public interface
CharValue

extends
PrimitiveValue
,
Comparable
<
CharValue
>
```

Provides access to a primitive

char

value in
the target VM.

**Since:** 1.3

public interface

CharValue

extends

PrimitiveValue

,

Comparable

<

CharValue

>

Provides access to a primitive

char

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

Compares the specified Object with this CharValue for equality.

int

hashCode

()

Returns the hash code value for this CharValue.

char

value

()

Returns this CharValue as a

char

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

Compares the specified Object with this CharValue for equality.

int

hashCode

()

Returns the hash code value for this CharValue.

char

value

()

Returns this CharValue as a

char

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

Compares the specified Object with this CharValue for equality.

Returns the hash code value for this CharValue.

Returns this CharValue as a

char

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
char value()
```

Returns this CharValue as a

char

.

**Returns:** the

char

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this CharValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a CharValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this CharValue.

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
char value()
```

Returns this CharValue as a

char

.

**Returns:** the

char

mirrored by this object.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this CharValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a CharValue and if applying "=="
to the two mirrored primitives would evaluate to true; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this CharValue.

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
char value()
```

Returns this CharValue as a

char

.

**Returns:** the

char

mirrored by this object.

---

#### value

char value()

Returns this CharValue as a

char

.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this CharValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a CharValue and if applying "=="
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

Compares the specified Object with this CharValue for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this CharValue.

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

Returns the hash code value for this CharValue.

---

