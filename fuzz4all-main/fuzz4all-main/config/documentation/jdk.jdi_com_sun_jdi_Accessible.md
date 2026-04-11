# Interface Accessible

**Source:** `jdk.jdi\com\sun\jdi\Accessible.html`

### Class Description

```java
public interface
Accessible
```

Provides information on the accessibility of a type or type component.
Mirrors for program elements which allow an
an access specifier (private, protected, public) provide information
on that part of the declaration through this interface.

**All Known Subinterfaces:** ArrayType

,

ClassType

,

Field

,

InterfaceType

,

Method

,

ReferenceType

,

TypeComponent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int modifiers()

Returns the Java™ programming language modifiers, encoded
in an integer.

The modifier encodings are defined in

The Java™ Virtual Machine Specification

in the

access_flag

tables for classes(section 4.1), fields(section 4.5), and methods(section 4.6).

---

#### boolean isPrivate()

Determines if this object mirrors a private item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:**
- true

for items with private access;

false

otherwise.

---

#### boolean isPackagePrivate()

Determines if this object mirrors a package private item.
A package private item is declared with no access specifier.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:**
- true

for items with package private access;

false

otherwise.

---

#### boolean isProtected()

Determines if this object mirrors a protected item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:**
- true

for items with private access;

false

otherwise.

---

#### boolean isPublic()

Determines if this object mirrors a public item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always true. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always true.

**Returns:**
- true

for items with public access;

false

otherwise.

---

### Additional Sections

#### Interface Accessible

**All Known Subinterfaces:** ArrayType

,

ClassType

,

Field

,

InterfaceType

,

Method

,

ReferenceType

,

TypeComponent

```java
public interface
Accessible
```

Provides information on the accessibility of a type or type component.
Mirrors for program elements which allow an
an access specifier (private, protected, public) provide information
on that part of the declaration through this interface.

**Since:** 1.3

public interface

Accessible

Provides information on the accessibility of a type or type component.
Mirrors for program elements which allow an
an access specifier (private, protected, public) provide information
on that part of the declaration through this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isPackagePrivate

()

Determines if this object mirrors a package private item.

boolean

isPrivate

()

Determines if this object mirrors a private item.

boolean

isProtected

()

Determines if this object mirrors a protected item.

boolean

isPublic

()

Determines if this object mirrors a public item.

int

modifiers

()

Returns the Java™ programming language modifiers, encoded
in an integer.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isPackagePrivate

()

Determines if this object mirrors a package private item.

boolean

isPrivate

()

Determines if this object mirrors a private item.

boolean

isProtected

()

Determines if this object mirrors a protected item.

boolean

isPublic

()

Determines if this object mirrors a public item.

int

modifiers

()

Returns the Java™ programming language modifiers, encoded
in an integer.

---

#### Method Summary

Determines if this object mirrors a package private item.

Determines if this object mirrors a private item.

Determines if this object mirrors a protected item.

Determines if this object mirrors a public item.

Returns the Java™ programming language modifiers, encoded
in an integer.

============ METHOD DETAIL ==========

- Method Detail

- modifiers

```java
int modifiers()
```

Returns the Java™ programming language modifiers, encoded
in an integer.

The modifier encodings are defined in

The Java™ Virtual Machine Specification

in the

access_flag

tables for classes(section 4.1), fields(section 4.5), and methods(section 4.6).

- isPrivate

```java
boolean isPrivate()
```

Determines if this object mirrors a private item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:** true

for items with private access;

false

otherwise.

- isPackagePrivate

```java
boolean isPackagePrivate()
```

Determines if this object mirrors a package private item.
A package private item is declared with no access specifier.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:** true

for items with package private access;

false

otherwise.

- isProtected

```java
boolean isProtected()
```

Determines if this object mirrors a protected item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:** true

for items with private access;

false

otherwise.

- isPublic

```java
boolean isPublic()
```

Determines if this object mirrors a public item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always true. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always true.

**Returns:** true

for items with public access;

false

otherwise.

Method Detail

- modifiers

```java
int modifiers()
```

Returns the Java™ programming language modifiers, encoded
in an integer.

The modifier encodings are defined in

The Java™ Virtual Machine Specification

in the

access_flag

tables for classes(section 4.1), fields(section 4.5), and methods(section 4.6).

- isPrivate

```java
boolean isPrivate()
```

Determines if this object mirrors a private item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:** true

for items with private access;

false

otherwise.

- isPackagePrivate

```java
boolean isPackagePrivate()
```

Determines if this object mirrors a package private item.
A package private item is declared with no access specifier.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:** true

for items with package private access;

false

otherwise.

- isProtected

```java
boolean isProtected()
```

Determines if this object mirrors a protected item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:** true

for items with private access;

false

otherwise.

- isPublic

```java
boolean isPublic()
```

Determines if this object mirrors a public item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always true. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always true.

**Returns:** true

for items with public access;

false

otherwise.

---

#### Method Detail

modifiers

```java
int modifiers()
```

Returns the Java™ programming language modifiers, encoded
in an integer.

The modifier encodings are defined in

The Java™ Virtual Machine Specification

in the

access_flag

tables for classes(section 4.1), fields(section 4.5), and methods(section 4.6).

---

#### modifiers

int modifiers()

Returns the Java™ programming language modifiers, encoded
in an integer.

The modifier encodings are defined in

The Java™ Virtual Machine Specification

in the

access_flag

tables for classes(section 4.1), fields(section 4.5), and methods(section 4.6).

The modifier encodings are defined in

The Java™ Virtual Machine Specification

in the

access_flag

tables for classes(section 4.1), fields(section 4.5), and methods(section 4.6).

isPrivate

```java
boolean isPrivate()
```

Determines if this object mirrors a private item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:** true

for items with private access;

false

otherwise.

---

#### isPrivate

boolean isPrivate()

Determines if this object mirrors a private item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

isPackagePrivate

```java
boolean isPackagePrivate()
```

Determines if this object mirrors a package private item.
A package private item is declared with no access specifier.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:** true

for items with package private access;

false

otherwise.

---

#### isPackagePrivate

boolean isPackagePrivate()

Determines if this object mirrors a package private item.
A package private item is declared with no access specifier.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

isProtected

```java
boolean isProtected()
```

Determines if this object mirrors a protected item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

**Returns:** true

for items with private access;

false

otherwise.

---

#### isProtected

boolean isProtected()

Determines if this object mirrors a protected item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always false. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always false.

isPublic

```java
boolean isPublic()
```

Determines if this object mirrors a public item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always true. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always true.

**Returns:** true

for items with public access;

false

otherwise.

---

#### isPublic

boolean isPublic()

Determines if this object mirrors a public item.
For

ArrayType

, the return value depends on the
array component type. For primitive arrays the return value
is always true. For object arrays, the return value is the
same as would be returned for the component type.
For primitive classes, such as

Integer.TYPE

,
the return value is always true.

---

