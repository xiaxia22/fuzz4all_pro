# Enum TypeKind

**Source:** `java.compiler\javax\lang\model\type\TypeKind.html`

### Class Description

```java
public enum
TypeKind

extends
Enum
<
TypeKind
>
```

The kind of a type mirror.

Note that it is possible additional type kinds will be added to
accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

**All Implemented Interfaces:** Serializable

,

Comparable

<

TypeKind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
TypeKind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TypeKind c : TypeKind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
TypeKind
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

#### public boolean isPrimitive()

Returns

true

if this kind corresponds to a primitive
type and

false

otherwise.

**Returns:**
- true

if this kind corresponds to a primitive type

---

### Additional Sections

#### Enum TypeKind

java.lang.Object

- java.lang.Enum

<

TypeKind

>
- - javax.lang.model.type.TypeKind

java.lang.Enum

<

TypeKind

>

- javax.lang.model.type.TypeKind

javax.lang.model.type.TypeKind

**All Implemented Interfaces:** Serializable

,

Comparable

<

TypeKind

>

```java
public enum
TypeKind

extends
Enum
<
TypeKind
>
```

The kind of a type mirror.

Note that it is possible additional type kinds will be added to
accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

**Since:** 1.6
**See Also:** TypeMirror

public enum

TypeKind

extends

Enum

<

TypeKind

>

The kind of a type mirror.

Note that it is possible additional type kinds will be added to
accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

Note that it is possible additional type kinds will be added to
accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ARRAY

An array type.

BOOLEAN

The primitive type

boolean

.

BYTE

The primitive type

byte

.

CHAR

The primitive type

char

.

DECLARED

A class or interface type.

DOUBLE

The primitive type

double

.

ERROR

A class or interface type that could not be resolved.

EXECUTABLE

A method, constructor, or initializer.

FLOAT

The primitive type

float

.

INT

The primitive type

int

.

INTERSECTION

An intersection type.

LONG

The primitive type

long

.

MODULE

A pseudo-type corresponding to a module element.

NONE

A pseudo-type used where no actual type is appropriate.

NULL

The null type.

OTHER

An implementation-reserved type.

PACKAGE

A pseudo-type corresponding to a package element.

SHORT

The primitive type

short

.

TYPEVAR

A type variable.

UNION

A union type.

VOID

The pseudo-type corresponding to the keyword

void

.

WILDCARD

A wildcard type argument.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isPrimitive

()

Returns

true

if this kind corresponds to a primitive
type and

false

otherwise.

static

TypeKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

TypeKind

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Enum Constant Summary

Enum Constants

Enum Constant

Description

ARRAY

An array type.

BOOLEAN

The primitive type

boolean

.

BYTE

The primitive type

byte

.

CHAR

The primitive type

char

.

DECLARED

A class or interface type.

DOUBLE

The primitive type

double

.

ERROR

A class or interface type that could not be resolved.

EXECUTABLE

A method, constructor, or initializer.

FLOAT

The primitive type

float

.

INT

The primitive type

int

.

INTERSECTION

An intersection type.

LONG

The primitive type

long

.

MODULE

A pseudo-type corresponding to a module element.

NONE

A pseudo-type used where no actual type is appropriate.

NULL

The null type.

OTHER

An implementation-reserved type.

PACKAGE

A pseudo-type corresponding to a package element.

SHORT

The primitive type

short

.

TYPEVAR

A type variable.

UNION

A union type.

VOID

The pseudo-type corresponding to the keyword

void

.

WILDCARD

A wildcard type argument.

---

#### Enum Constant Summary

An array type.

The primitive type

boolean

.

The primitive type

byte

.

The primitive type

char

.

A class or interface type.

The primitive type

double

.

A class or interface type that could not be resolved.

A method, constructor, or initializer.

The primitive type

float

.

The primitive type

int

.

An intersection type.

The primitive type

long

.

A pseudo-type corresponding to a module element.

A pseudo-type used where no actual type is appropriate.

The null type.

An implementation-reserved type.

A pseudo-type corresponding to a package element.

The primitive type

short

.

A type variable.

A union type.

The pseudo-type corresponding to the keyword

void

.

A wildcard type argument.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isPrimitive

()

Returns

true

if this kind corresponds to a primitive
type and

false

otherwise.

static

TypeKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

TypeKind

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns

true

if this kind corresponds to a primitive
type and

false

otherwise.

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- BOOLEAN

```java
public static final
TypeKind
BOOLEAN
```

The primitive type

boolean

.

- BYTE

```java
public static final
TypeKind
BYTE
```

The primitive type

byte

.

- SHORT

```java
public static final
TypeKind
SHORT
```

The primitive type

short

.

- INT

```java
public static final
TypeKind
INT
```

The primitive type

int

.

- LONG

```java
public static final
TypeKind
LONG
```

The primitive type

long

.

- CHAR

```java
public static final
TypeKind
CHAR
```

The primitive type

char

.

- FLOAT

```java
public static final
TypeKind
FLOAT
```

The primitive type

float

.

- DOUBLE

```java
public static final
TypeKind
DOUBLE
```

The primitive type

double

.

- VOID

```java
public static final
TypeKind
VOID
```

The pseudo-type corresponding to the keyword

void

.

**See Also:** NoType

- NONE

```java
public static final
TypeKind
NONE
```

A pseudo-type used where no actual type is appropriate.

**See Also:** NoType

- NULL

```java
public static final
TypeKind
NULL
```

The null type.

- ARRAY

```java
public static final
TypeKind
ARRAY
```

An array type.

- DECLARED

```java
public static final
TypeKind
DECLARED
```

A class or interface type.

- ERROR

```java
public static final
TypeKind
ERROR
```

A class or interface type that could not be resolved.

- TYPEVAR

```java
public static final
TypeKind
TYPEVAR
```

A type variable.

- WILDCARD

```java
public static final
TypeKind
WILDCARD
```

A wildcard type argument.

- PACKAGE

```java
public static final
TypeKind
PACKAGE
```

A pseudo-type corresponding to a package element.

**See Also:** NoType

- EXECUTABLE

```java
public static final
TypeKind
EXECUTABLE
```

A method, constructor, or initializer.

- OTHER

```java
public static final
TypeKind
OTHER
```

An implementation-reserved type.
This is not the type you are looking for.

- UNION

```java
public static final
TypeKind
UNION
```

A union type.

**Since:** 1.7

- INTERSECTION

```java
public static final
TypeKind
INTERSECTION
```

An intersection type.

**Since:** 1.8

- MODULE

```java
public static final
TypeKind
MODULE
```

A pseudo-type corresponding to a module element.

**Since:** 9
**See Also:** NoType

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
TypeKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TypeKind c : TypeKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
TypeKind
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- isPrimitive

```java
public boolean isPrimitive()
```

Returns

true

if this kind corresponds to a primitive
type and

false

otherwise.

**Returns:** true

if this kind corresponds to a primitive type

Enum Constant Detail

- BOOLEAN

```java
public static final
TypeKind
BOOLEAN
```

The primitive type

boolean

.

- BYTE

```java
public static final
TypeKind
BYTE
```

The primitive type

byte

.

- SHORT

```java
public static final
TypeKind
SHORT
```

The primitive type

short

.

- INT

```java
public static final
TypeKind
INT
```

The primitive type

int

.

- LONG

```java
public static final
TypeKind
LONG
```

The primitive type

long

.

- CHAR

```java
public static final
TypeKind
CHAR
```

The primitive type

char

.

- FLOAT

```java
public static final
TypeKind
FLOAT
```

The primitive type

float

.

- DOUBLE

```java
public static final
TypeKind
DOUBLE
```

The primitive type

double

.

- VOID

```java
public static final
TypeKind
VOID
```

The pseudo-type corresponding to the keyword

void

.

**See Also:** NoType

- NONE

```java
public static final
TypeKind
NONE
```

A pseudo-type used where no actual type is appropriate.

**See Also:** NoType

- NULL

```java
public static final
TypeKind
NULL
```

The null type.

- ARRAY

```java
public static final
TypeKind
ARRAY
```

An array type.

- DECLARED

```java
public static final
TypeKind
DECLARED
```

A class or interface type.

- ERROR

```java
public static final
TypeKind
ERROR
```

A class or interface type that could not be resolved.

- TYPEVAR

```java
public static final
TypeKind
TYPEVAR
```

A type variable.

- WILDCARD

```java
public static final
TypeKind
WILDCARD
```

A wildcard type argument.

- PACKAGE

```java
public static final
TypeKind
PACKAGE
```

A pseudo-type corresponding to a package element.

**See Also:** NoType

- EXECUTABLE

```java
public static final
TypeKind
EXECUTABLE
```

A method, constructor, or initializer.

- OTHER

```java
public static final
TypeKind
OTHER
```

An implementation-reserved type.
This is not the type you are looking for.

- UNION

```java
public static final
TypeKind
UNION
```

A union type.

**Since:** 1.7

- INTERSECTION

```java
public static final
TypeKind
INTERSECTION
```

An intersection type.

**Since:** 1.8

- MODULE

```java
public static final
TypeKind
MODULE
```

A pseudo-type corresponding to a module element.

**Since:** 9
**See Also:** NoType

---

#### Enum Constant Detail

BOOLEAN

```java
public static final
TypeKind
BOOLEAN
```

The primitive type

boolean

.

---

#### BOOLEAN

public static final

TypeKind

BOOLEAN

The primitive type

boolean

.

BYTE

```java
public static final
TypeKind
BYTE
```

The primitive type

byte

.

---

#### BYTE

public static final

TypeKind

BYTE

The primitive type

byte

.

SHORT

```java
public static final
TypeKind
SHORT
```

The primitive type

short

.

---

#### SHORT

public static final

TypeKind

SHORT

The primitive type

short

.

INT

```java
public static final
TypeKind
INT
```

The primitive type

int

.

---

#### INT

public static final

TypeKind

INT

The primitive type

int

.

LONG

```java
public static final
TypeKind
LONG
```

The primitive type

long

.

---

#### LONG

public static final

TypeKind

LONG

The primitive type

long

.

CHAR

```java
public static final
TypeKind
CHAR
```

The primitive type

char

.

---

#### CHAR

public static final

TypeKind

CHAR

The primitive type

char

.

FLOAT

```java
public static final
TypeKind
FLOAT
```

The primitive type

float

.

---

#### FLOAT

public static final

TypeKind

FLOAT

The primitive type

float

.

DOUBLE

```java
public static final
TypeKind
DOUBLE
```

The primitive type

double

.

---

#### DOUBLE

public static final

TypeKind

DOUBLE

The primitive type

double

.

VOID

```java
public static final
TypeKind
VOID
```

The pseudo-type corresponding to the keyword

void

.

**See Also:** NoType

---

#### VOID

public static final

TypeKind

VOID

The pseudo-type corresponding to the keyword

void

.

NONE

```java
public static final
TypeKind
NONE
```

A pseudo-type used where no actual type is appropriate.

**See Also:** NoType

---

#### NONE

public static final

TypeKind

NONE

A pseudo-type used where no actual type is appropriate.

NULL

```java
public static final
TypeKind
NULL
```

The null type.

---

#### NULL

public static final

TypeKind

NULL

The null type.

ARRAY

```java
public static final
TypeKind
ARRAY
```

An array type.

---

#### ARRAY

public static final

TypeKind

ARRAY

An array type.

DECLARED

```java
public static final
TypeKind
DECLARED
```

A class or interface type.

---

#### DECLARED

public static final

TypeKind

DECLARED

A class or interface type.

ERROR

```java
public static final
TypeKind
ERROR
```

A class or interface type that could not be resolved.

---

#### ERROR

public static final

TypeKind

ERROR

A class or interface type that could not be resolved.

TYPEVAR

```java
public static final
TypeKind
TYPEVAR
```

A type variable.

---

#### TYPEVAR

public static final

TypeKind

TYPEVAR

A type variable.

WILDCARD

```java
public static final
TypeKind
WILDCARD
```

A wildcard type argument.

---

#### WILDCARD

public static final

TypeKind

WILDCARD

A wildcard type argument.

PACKAGE

```java
public static final
TypeKind
PACKAGE
```

A pseudo-type corresponding to a package element.

**See Also:** NoType

---

#### PACKAGE

public static final

TypeKind

PACKAGE

A pseudo-type corresponding to a package element.

EXECUTABLE

```java
public static final
TypeKind
EXECUTABLE
```

A method, constructor, or initializer.

---

#### EXECUTABLE

public static final

TypeKind

EXECUTABLE

A method, constructor, or initializer.

OTHER

```java
public static final
TypeKind
OTHER
```

An implementation-reserved type.
This is not the type you are looking for.

---

#### OTHER

public static final

TypeKind

OTHER

An implementation-reserved type.
This is not the type you are looking for.

UNION

```java
public static final
TypeKind
UNION
```

A union type.

**Since:** 1.7

---

#### UNION

public static final

TypeKind

UNION

A union type.

INTERSECTION

```java
public static final
TypeKind
INTERSECTION
```

An intersection type.

**Since:** 1.8

---

#### INTERSECTION

public static final

TypeKind

INTERSECTION

An intersection type.

MODULE

```java
public static final
TypeKind
MODULE
```

A pseudo-type corresponding to a module element.

**Since:** 9
**See Also:** NoType

---

#### MODULE

public static final

TypeKind

MODULE

A pseudo-type corresponding to a module element.

Method Detail

- values

```java
public static
TypeKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TypeKind c : TypeKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
TypeKind
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- isPrimitive

```java
public boolean isPrimitive()
```

Returns

true

if this kind corresponds to a primitive
type and

false

otherwise.

**Returns:** true

if this kind corresponds to a primitive type

---

#### Method Detail

values

```java
public static
TypeKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TypeKind c : TypeKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

TypeKind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TypeKind c : TypeKind.values())
System.out.println(c);
```

for (TypeKind c : TypeKind.values())
System.out.println(c);

valueOf

```java
public static
TypeKind
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

TypeKind

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

isPrimitive

```java
public boolean isPrimitive()
```

Returns

true

if this kind corresponds to a primitive
type and

false

otherwise.

**Returns:** true

if this kind corresponds to a primitive type

---

#### isPrimitive

public boolean isPrimitive()

Returns

true

if this kind corresponds to a primitive
type and

false

otherwise.

---

