# Interface VoidValue

**Source:** `jdk.jdi\com\sun\jdi\VoidValue.html`

### Class Description

```java
public interface
VoidValue

extends
Value
```

Provides access to a primitive

void

value in
the target VM.

**All Superinterfaces:** Mirror

,

Value

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean equals​(
Object
obj)

Compares the specified Object with this VoidValue for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is a VoidValue; false
otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this VoidValue.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Interface VoidValue

**All Superinterfaces:** Mirror

,

Value

```java
public interface
VoidValue

extends
Value
```

Provides access to a primitive

void

value in
the target VM.

**Since:** 1.3

public interface

VoidValue

extends

Value

Provides access to a primitive

void

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

Compares the specified Object with this VoidValue for equality.

int

hashCode

()

Returns the hash code value for this VoidValue.

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

equals

​(

Object

obj)

Compares the specified Object with this VoidValue for equality.

int

hashCode

()

Returns the hash code value for this VoidValue.

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

Compares the specified Object with this VoidValue for equality.

Returns the hash code value for this VoidValue.

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

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this VoidValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a VoidValue; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this VoidValue.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Method Detail

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this VoidValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a VoidValue; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this VoidValue.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this VoidValue for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a VoidValue; false
otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Compares the specified Object with this VoidValue for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this VoidValue.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this VoidValue.

---

