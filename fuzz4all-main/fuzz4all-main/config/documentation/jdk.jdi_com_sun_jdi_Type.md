# Interface Type

**Source:** `jdk.jdi\com\sun\jdi\Type.html`

### Class Description

```java
public interface
Type

extends
Mirror
```

The mirror for a type in the target VM.
This interface is the root of a type hierarchy encompassing primitive
types and reference types.

A Type may be used to represent a run-time type:

Value

.type()

or a compile-time type:

Field.type()

Method.returnType()

Method.argumentTypes()

LocalVariable.type()

ArrayType.componentType()

The following tables illustrate which subinterfaces of Type
are used to mirror types in the target VM --

Subinterfaces of

PrimitiveType

Type declared in target as

Is mirrored as an instance of

boolean

BooleanType

byte

ByteType

char

CharType

double

DoubleType

float

FloatType

int

IntegerType

long

LongType

short

ShortType

void

VoidType

Subinterfaces of

ReferenceType

Type declared in target as

For example

Is mirrored as an instance of

a class

Date

ClassType

an interface

Runnable

InterfaceType

an array

(any)

ArrayType

<TH scope="row"><I>an array</I></TH>

int[]

ArrayType

whose

componentType()

is

IntegerType

<TH scope="row"><I>an array</I></TH>

Date[]

ArrayType

whose

componentType()

is

ClassType

<TH scope="row"><I>an array</I></TH>

Runnable[]

ArrayType

whose

componentType()

is

InterfaceType

**All Superinterfaces:** Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
signature()

Returns the JNI-style signature for this type.

For primitive classes
the returned signature is the signature of the corresponding primitive
type; for example, "I" is returned as the signature of the class
represented by

Integer.TYPE

.

**Returns:**
- the string containing the type signature.

**See Also:**
- Type Signatures

---

#### String
name()

**Returns:**
- a text representation of this type.

---

### Additional Sections

#### Interface Type

**All Superinterfaces:** Mirror

**All Known Subinterfaces:** ArrayType

,

BooleanType

,

ByteType

,

CharType

,

ClassType

,

DoubleType

,

FloatType

,

IntegerType

,

InterfaceType

,

LongType

,

PrimitiveType

,

ReferenceType

,

ShortType

,

VoidType

```java
public interface
Type

extends
Mirror
```

The mirror for a type in the target VM.
This interface is the root of a type hierarchy encompassing primitive
types and reference types.

A Type may be used to represent a run-time type:

Value

.type()

or a compile-time type:

Field.type()

Method.returnType()

Method.argumentTypes()

LocalVariable.type()

ArrayType.componentType()

The following tables illustrate which subinterfaces of Type
are used to mirror types in the target VM --

Subinterfaces of

PrimitiveType

Type declared in target as

Is mirrored as an instance of

boolean

BooleanType

byte

ByteType

char

CharType

double

DoubleType

float

FloatType

int

IntegerType

long

LongType

short

ShortType

void

VoidType

Subinterfaces of

ReferenceType

Type declared in target as

For example

Is mirrored as an instance of

a class

Date

ClassType

an interface

Runnable

InterfaceType

an array

(any)

ArrayType

<TH scope="row"><I>an array</I></TH>

int[]

ArrayType

whose

componentType()

is

IntegerType

<TH scope="row"><I>an array</I></TH>

Date[]

ArrayType

whose

componentType()

is

ClassType

<TH scope="row"><I>an array</I></TH>

Runnable[]

ArrayType

whose

componentType()

is

InterfaceType

**Since:** 1.3
**See Also:** Subinterface PrimitiveType

,

Subinterface ReferenceType

,

Value - for relationship between Type and Value

,

Field.type() - for usage examples

public interface

Type

extends

Mirror

The mirror for a type in the target VM.
This interface is the root of a type hierarchy encompassing primitive
types and reference types.

A Type may be used to represent a run-time type:

Value

.type()

or a compile-time type:

Field.type()

Method.returnType()

Method.argumentTypes()

LocalVariable.type()

ArrayType.componentType()

The following tables illustrate which subinterfaces of Type
are used to mirror types in the target VM --

Subinterfaces of

PrimitiveType

Type declared in target as

Is mirrored as an instance of

boolean

BooleanType

byte

ByteType

char

CharType

double

DoubleType

float

FloatType

int

IntegerType

long

LongType

short

ShortType

void

VoidType

Subinterfaces of

ReferenceType

Type declared in target as

For example

Is mirrored as an instance of

a class

Date

ClassType

an interface

Runnable

InterfaceType

an array

(any)

ArrayType

<TH scope="row"><I>an array</I></TH>

int[]

ArrayType

whose

componentType()

is

IntegerType

<TH scope="row"><I>an array</I></TH>

Date[]

ArrayType

whose

componentType()

is

ClassType

<TH scope="row"><I>an array</I></TH>

Runnable[]

ArrayType

whose

componentType()

is

InterfaceType

A Type may be used to represent a run-time type:

Value

.type()

or a compile-time type:

Field.type()

Method.returnType()

Method.argumentTypes()

LocalVariable.type()

ArrayType.componentType()

The following tables illustrate which subinterfaces of Type
are used to mirror types in the target VM --

Subinterfaces of

PrimitiveType

Type declared in target as

Is mirrored as an instance of

boolean

BooleanType

byte

ByteType

char

CharType

double

DoubleType

float

FloatType

int

IntegerType

long

LongType

short

ShortType

void

VoidType

Subinterfaces of

ReferenceType

Type declared in target as

For example

Is mirrored as an instance of

a class

Date

ClassType

an interface

Runnable

InterfaceType

an array

(any)

ArrayType

<TH scope="row"><I>an array</I></TH>

int[]

ArrayType

whose

componentType()

is

IntegerType

<TH scope="row"><I>an array</I></TH>

Date[]

ArrayType

whose

componentType()

is

ClassType

<TH scope="row"><I>an array</I></TH>

Runnable[]

ArrayType

whose

componentType()

is

InterfaceType

The following tables illustrate which subinterfaces of Type
are used to mirror types in the target VM --

Subinterfaces of

PrimitiveType

Type declared in target as

Is mirrored as an instance of

boolean

BooleanType

byte

ByteType

char

CharType

double

DoubleType

float

FloatType

int

IntegerType

long

LongType

short

ShortType

void

VoidType

Subinterfaces of

ReferenceType

Type declared in target as

For example

Is mirrored as an instance of

a class

Date

ClassType

an interface

Runnable

InterfaceType

an array

(any)

ArrayType

<TH scope="row"><I>an array</I></TH>

int[]

ArrayType

whose

componentType()

is

IntegerType

<TH scope="row"><I>an array</I></TH>

Date[]

ArrayType

whose

componentType()

is

ClassType

<TH scope="row"><I>an array</I></TH>

Runnable[]

ArrayType

whose

componentType()

is

InterfaceType

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

String

signature

()

Returns the JNI-style signature for this type.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

String

signature

()

Returns the JNI-style signature for this type.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Returns the JNI-style signature for this type.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- signature

```java
String
signature()
```

Returns the JNI-style signature for this type.

For primitive classes
the returned signature is the signature of the corresponding primitive
type; for example, "I" is returned as the signature of the class
represented by

Integer.TYPE

.

**Returns:** the string containing the type signature.
**See Also:** Type Signatures

- name

```java
String
name()
```

**Returns:** a text representation of this type.

Method Detail

- signature

```java
String
signature()
```

Returns the JNI-style signature for this type.

For primitive classes
the returned signature is the signature of the corresponding primitive
type; for example, "I" is returned as the signature of the class
represented by

Integer.TYPE

.

**Returns:** the string containing the type signature.
**See Also:** Type Signatures

- name

```java
String
name()
```

**Returns:** a text representation of this type.

---

#### Method Detail

signature

```java
String
signature()
```

Returns the JNI-style signature for this type.

For primitive classes
the returned signature is the signature of the corresponding primitive
type; for example, "I" is returned as the signature of the class
represented by

Integer.TYPE

.

**Returns:** the string containing the type signature.
**See Also:** Type Signatures

---

#### signature

String

signature()

Returns the JNI-style signature for this type.

For primitive classes
the returned signature is the signature of the corresponding primitive
type; for example, "I" is returned as the signature of the class
represented by

Integer.TYPE

.

For primitive classes
the returned signature is the signature of the corresponding primitive
type; for example, "I" is returned as the signature of the class
represented by

Integer.TYPE

.

name

```java
String
name()
```

**Returns:** a text representation of this type.

---

#### name

String

name()

---

