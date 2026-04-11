# Interface Field

**Source:** `jdk.jdi\com\sun\jdi\Field.html`

### Class Description

```java
public interface
Field

extends
TypeComponent
,
Comparable
<
Field
>
```

A class or instance variable in the target VM.
See

TypeComponent

for general information about Field and Method mirrors.

**All Superinterfaces:** Accessible

,

Comparable

<

Field

>

,

Mirror

,

TypeComponent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
typeName()

Returns a text representation of the type
of this field.
Where the type is the type specified in the declaration
of this field.

This type name is always available even if
the type has not yet been created or loaded.

**Returns:**
- a String representing the
type of this field.

---

#### Type
type()
throws
ClassNotLoadedException

Returns the type of this field.
Where the type is the type specified in the declaration
of this field.

For example, if a target class defines:

```java
short s;
Date d;
byte[] ba;
```

And the JDI client defines these

Field

objects:

```java
Field sField = targetClass.fieldByName("s");
Field dField = targetClass.fieldByName("d");
Field baField = targetClass.fieldByName("ba");
```

to mirror the corresponding fields, then

sField.type()

is a

ShortType

,

dField.type()

is the

ReferenceType

for

java.util.Date

and

((ArrayType)(baField.type())).componentType()

is a

ByteType

.

Note: if the type of this field is a reference type (class,
interface, or array) and it has not been created or loaded
by the declaring type's class loader - that is,

declaringType()

.classLoader()

,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:**
- the

Type

of this field.

**Throws:**
- ClassNotLoadedException

- if the type has not yet been loaded
or created through the appropriate class loader.

**See Also:**
- Type

---

#### boolean isTransient()

Determine if this is a transient field.

**Returns:**
- true

if this field is transient;

false

otherwise.

---

#### boolean isVolatile()

Determine if this is a volatile field.

**Returns:**
- true

if this field is volatile;

false

otherwise.

---

#### boolean isEnumConstant()

Determine if this is a field that represents an enum constant.

**Returns:**
- true

if this field represents an enum constant;

false

otherwise.

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this field for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if the Object is a Field and if both
mirror the same field (declared in the same class or interface, in
the same VM).

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this Field.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the integer hash code.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Interface Field

**All Superinterfaces:** Accessible

,

Comparable

<

Field

>

,

Mirror

,

TypeComponent

```java
public interface
Field

extends
TypeComponent
,
Comparable
<
Field
>
```

A class or instance variable in the target VM.
See

TypeComponent

for general information about Field and Method mirrors.

**Since:** 1.3
**See Also:** ObjectReference

,

ReferenceType

public interface

Field

extends

TypeComponent

,

Comparable

<

Field

>

A class or instance variable in the target VM.
See

TypeComponent

for general information about Field and Method mirrors.

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

Compares the specified Object with this field for equality.

int

hashCode

()

Returns the hash code value for this Field.

boolean

isEnumConstant

()

Determine if this is a field that represents an enum constant.

boolean

isTransient

()

Determine if this is a transient field.

boolean

isVolatile

()

Determine if this is a volatile field.

Type

type

()

Returns the type of this field.

String

typeName

()

Returns a text representation of the type
of this field.

- Methods declared in interface com.sun.jdi.

Accessible

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

modifiers

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

TypeComponent

declaringType

,

genericSignature

,

isFinal

,

isStatic

,

isSynthetic

,

name

,

signature

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

Compares the specified Object with this field for equality.

int

hashCode

()

Returns the hash code value for this Field.

boolean

isEnumConstant

()

Determine if this is a field that represents an enum constant.

boolean

isTransient

()

Determine if this is a transient field.

boolean

isVolatile

()

Determine if this is a volatile field.

Type

type

()

Returns the type of this field.

String

typeName

()

Returns a text representation of the type
of this field.

- Methods declared in interface com.sun.jdi.

Accessible

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

modifiers

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

TypeComponent

declaringType

,

genericSignature

,

isFinal

,

isStatic

,

isSynthetic

,

name

,

signature

---

#### Method Summary

Compares the specified Object with this field for equality.

Returns the hash code value for this Field.

Determine if this is a field that represents an enum constant.

Determine if this is a transient field.

Determine if this is a volatile field.

Returns the type of this field.

Returns a text representation of the type
of this field.

Methods declared in interface com.sun.jdi.

Accessible

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

modifiers

---

#### Methods declared in interface com.sun.jdi. Accessible

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

TypeComponent

declaringType

,

genericSignature

,

isFinal

,

isStatic

,

isSynthetic

,

name

,

signature

---

#### Methods declared in interface com.sun.jdi. TypeComponent

============ METHOD DETAIL ==========

- Method Detail

- typeName

```java
String
typeName()
```

Returns a text representation of the type
of this field.
Where the type is the type specified in the declaration
of this field.

This type name is always available even if
the type has not yet been created or loaded.

**Returns:** a String representing the
type of this field.

- type

```java
Type
type()
throws
ClassNotLoadedException
```

Returns the type of this field.
Where the type is the type specified in the declaration
of this field.

For example, if a target class defines:

```java
short s;
Date d;
byte[] ba;
```

And the JDI client defines these

Field

objects:

```java
Field sField = targetClass.fieldByName("s");
Field dField = targetClass.fieldByName("d");
Field baField = targetClass.fieldByName("ba");
```

to mirror the corresponding fields, then

sField.type()

is a

ShortType

,

dField.type()

is the

ReferenceType

for

java.util.Date

and

((ArrayType)(baField.type())).componentType()

is a

ByteType

.

Note: if the type of this field is a reference type (class,
interface, or array) and it has not been created or loaded
by the declaring type's class loader - that is,

declaringType()

.classLoader()

,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:** the

Type

of this field.
**Throws:** ClassNotLoadedException

- if the type has not yet been loaded
or created through the appropriate class loader.
**See Also:** Type

- isTransient

```java
boolean isTransient()
```

Determine if this is a transient field.

**Returns:** true

if this field is transient;

false

otherwise.

- isVolatile

```java
boolean isVolatile()
```

Determine if this is a volatile field.

**Returns:** true

if this field is volatile;

false

otherwise.

- isEnumConstant

```java
boolean isEnumConstant()
```

Determine if this is a field that represents an enum constant.

**Returns:** true

if this field represents an enum constant;

false

otherwise.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this field for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if the Object is a Field and if both
mirror the same field (declared in the same class or interface, in
the same VM).
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this Field.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Method Detail

- typeName

```java
String
typeName()
```

Returns a text representation of the type
of this field.
Where the type is the type specified in the declaration
of this field.

This type name is always available even if
the type has not yet been created or loaded.

**Returns:** a String representing the
type of this field.

- type

```java
Type
type()
throws
ClassNotLoadedException
```

Returns the type of this field.
Where the type is the type specified in the declaration
of this field.

For example, if a target class defines:

```java
short s;
Date d;
byte[] ba;
```

And the JDI client defines these

Field

objects:

```java
Field sField = targetClass.fieldByName("s");
Field dField = targetClass.fieldByName("d");
Field baField = targetClass.fieldByName("ba");
```

to mirror the corresponding fields, then

sField.type()

is a

ShortType

,

dField.type()

is the

ReferenceType

for

java.util.Date

and

((ArrayType)(baField.type())).componentType()

is a

ByteType

.

Note: if the type of this field is a reference type (class,
interface, or array) and it has not been created or loaded
by the declaring type's class loader - that is,

declaringType()

.classLoader()

,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:** the

Type

of this field.
**Throws:** ClassNotLoadedException

- if the type has not yet been loaded
or created through the appropriate class loader.
**See Also:** Type

- isTransient

```java
boolean isTransient()
```

Determine if this is a transient field.

**Returns:** true

if this field is transient;

false

otherwise.

- isVolatile

```java
boolean isVolatile()
```

Determine if this is a volatile field.

**Returns:** true

if this field is volatile;

false

otherwise.

- isEnumConstant

```java
boolean isEnumConstant()
```

Determine if this is a field that represents an enum constant.

**Returns:** true

if this field represents an enum constant;

false

otherwise.

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this field for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if the Object is a Field and if both
mirror the same field (declared in the same class or interface, in
the same VM).
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this Field.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

typeName

```java
String
typeName()
```

Returns a text representation of the type
of this field.
Where the type is the type specified in the declaration
of this field.

This type name is always available even if
the type has not yet been created or loaded.

**Returns:** a String representing the
type of this field.

---

#### typeName

String

typeName()

Returns a text representation of the type
of this field.
Where the type is the type specified in the declaration
of this field.

This type name is always available even if
the type has not yet been created or loaded.

This type name is always available even if
the type has not yet been created or loaded.

type

```java
Type
type()
throws
ClassNotLoadedException
```

Returns the type of this field.
Where the type is the type specified in the declaration
of this field.

For example, if a target class defines:

```java
short s;
Date d;
byte[] ba;
```

And the JDI client defines these

Field

objects:

```java
Field sField = targetClass.fieldByName("s");
Field dField = targetClass.fieldByName("d");
Field baField = targetClass.fieldByName("ba");
```

to mirror the corresponding fields, then

sField.type()

is a

ShortType

,

dField.type()

is the

ReferenceType

for

java.util.Date

and

((ArrayType)(baField.type())).componentType()

is a

ByteType

.

Note: if the type of this field is a reference type (class,
interface, or array) and it has not been created or loaded
by the declaring type's class loader - that is,

declaringType()

.classLoader()

,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:** the

Type

of this field.
**Throws:** ClassNotLoadedException

- if the type has not yet been loaded
or created through the appropriate class loader.
**See Also:** Type

---

#### type

Type

type()
throws

ClassNotLoadedException

Returns the type of this field.
Where the type is the type specified in the declaration
of this field.

For example, if a target class defines:

```java
short s;
Date d;
byte[] ba;
```

And the JDI client defines these

Field

objects:

```java
Field sField = targetClass.fieldByName("s");
Field dField = targetClass.fieldByName("d");
Field baField = targetClass.fieldByName("ba");
```

to mirror the corresponding fields, then

sField.type()

is a

ShortType

,

dField.type()

is the

ReferenceType

for

java.util.Date

and

((ArrayType)(baField.type())).componentType()

is a

ByteType

.

Note: if the type of this field is a reference type (class,
interface, or array) and it has not been created or loaded
by the declaring type's class loader - that is,

declaringType()

.classLoader()

,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

For example, if a target class defines:

```java
short s;
Date d;
byte[] ba;
```

And the JDI client defines these

Field

objects:

```java
Field sField = targetClass.fieldByName("s");
Field dField = targetClass.fieldByName("d");
Field baField = targetClass.fieldByName("ba");
```

to mirror the corresponding fields, then

sField.type()

is a

ShortType

,

dField.type()

is the

ReferenceType

for

java.util.Date

and

((ArrayType)(baField.type())).componentType()

is a

ByteType

.

Note: if the type of this field is a reference type (class,
interface, or array) and it has not been created or loaded
by the declaring type's class loader - that is,

declaringType()

.classLoader()

,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

short s;
Date d;
byte[] ba;

Field sField = targetClass.fieldByName("s");
Field dField = targetClass.fieldByName("d");
Field baField = targetClass.fieldByName("ba");

Note: if the type of this field is a reference type (class,
interface, or array) and it has not been created or loaded
by the declaring type's class loader - that is,

declaringType()

.classLoader()

,
then ClassNotLoadedException will be thrown.
Also, a reference type may have been loaded but not yet prepared,
in which case the type will be returned
but attempts to perform some operations on the returned type
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

isTransient

```java
boolean isTransient()
```

Determine if this is a transient field.

**Returns:** true

if this field is transient;

false

otherwise.

---

#### isTransient

boolean isTransient()

Determine if this is a transient field.

isVolatile

```java
boolean isVolatile()
```

Determine if this is a volatile field.

**Returns:** true

if this field is volatile;

false

otherwise.

---

#### isVolatile

boolean isVolatile()

Determine if this is a volatile field.

isEnumConstant

```java
boolean isEnumConstant()
```

Determine if this is a field that represents an enum constant.

**Returns:** true

if this field represents an enum constant;

false

otherwise.

---

#### isEnumConstant

boolean isEnumConstant()

Determine if this is a field that represents an enum constant.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this field for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if the Object is a Field and if both
mirror the same field (declared in the same class or interface, in
the same VM).
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Compares the specified Object with this field for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this Field.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this Field.

---

