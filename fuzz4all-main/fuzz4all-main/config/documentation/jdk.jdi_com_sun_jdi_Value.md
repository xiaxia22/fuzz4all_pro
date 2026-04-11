# Interface Value

**Source:** `jdk.jdi\com\sun\jdi\Value.html`

### Class Description

```java
public interface
Value

extends
Mirror
```

The mirror for a value in the target VM.
This interface is the root of a
value hierarchy encompassing primitive values and object values.

Some examples of where values may be accessed:

ObjectReference.getValue(Field)

- value of a field

StackFrame.getValue(LocalVariable)

- value of a variable

VirtualMachine.mirrorOf(double)

- created in the target VM by the JDI client

ModificationWatchpointEvent.valueToBe()

- returned with an event

The following tables illustrate which subinterfaces of Value
are used to mirror values in the target VM --

Subinterfaces of

PrimitiveValue

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a boolean

true

BooleanValue

BooleanType

a byte

(byte)4

ByteValue

ByteType

a char

'a'

CharValue

CharType

a double

3.1415926

DoubleValue

DoubleType

a float

2.5f

FloatValue

FloatType

an int

22

IntegerValue

IntegerType

a long

1024L

LongValue

LongType

a short

(short)12

ShortValue

ShortType

a void

VoidValue

VoidType

Subinterfaces of

ObjectReference

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a class instance

this

ObjectReference

ClassType

an array

new int[5]

ArrayReference

ArrayType

a string

"hello"

StringReference

ClassType

a thread

Thread.currentThread()

ThreadReference

ClassType

a thread group

Thread.currentThread()

.getThreadGroup()

ThreadGroupReference

ClassType

a

java.lang.Class

instance

this.getClass()

ClassObjectReference

ClassType

a class loader

this.getClass()

.getClassLoader()

ClassLoaderReference

ClassType

Other values

Kind of value

For example -

expression in target

Is mirrored as

Type

of value

null

null

null

n/a

**All Superinterfaces:** Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Type
type()

Returns the run-time type of this value.

**Returns:**
- a

Type

which mirrors the value's type in the
target VM.

**See Also:**
- Type

---

### Additional Sections

#### Interface Value

**All Superinterfaces:** Mirror

**All Known Subinterfaces:** ArrayReference

,

BooleanValue

,

ByteValue

,

CharValue

,

ClassLoaderReference

,

ClassObjectReference

,

DoubleValue

,

FloatValue

,

IntegerValue

,

LongValue

,

ModuleReference

,

ObjectReference

,

PrimitiveValue

,

ShortValue

,

StringReference

,

ThreadGroupReference

,

ThreadReference

,

VoidValue

```java
public interface
Value

extends
Mirror
```

The mirror for a value in the target VM.
This interface is the root of a
value hierarchy encompassing primitive values and object values.

Some examples of where values may be accessed:

ObjectReference.getValue(Field)

- value of a field

StackFrame.getValue(LocalVariable)

- value of a variable

VirtualMachine.mirrorOf(double)

- created in the target VM by the JDI client

ModificationWatchpointEvent.valueToBe()

- returned with an event

The following tables illustrate which subinterfaces of Value
are used to mirror values in the target VM --

Subinterfaces of

PrimitiveValue

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a boolean

true

BooleanValue

BooleanType

a byte

(byte)4

ByteValue

ByteType

a char

'a'

CharValue

CharType

a double

3.1415926

DoubleValue

DoubleType

a float

2.5f

FloatValue

FloatType

an int

22

IntegerValue

IntegerType

a long

1024L

LongValue

LongType

a short

(short)12

ShortValue

ShortType

a void

VoidValue

VoidType

Subinterfaces of

ObjectReference

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a class instance

this

ObjectReference

ClassType

an array

new int[5]

ArrayReference

ArrayType

a string

"hello"

StringReference

ClassType

a thread

Thread.currentThread()

ThreadReference

ClassType

a thread group

Thread.currentThread()

.getThreadGroup()

ThreadGroupReference

ClassType

a

java.lang.Class

instance

this.getClass()

ClassObjectReference

ClassType

a class loader

this.getClass()

.getClassLoader()

ClassLoaderReference

ClassType

Other values

Kind of value

For example -

expression in target

Is mirrored as

Type

of value

null

null

null

n/a

**Since:** 1.3

public interface

Value

extends

Mirror

The mirror for a value in the target VM.
This interface is the root of a
value hierarchy encompassing primitive values and object values.

Some examples of where values may be accessed:

ObjectReference.getValue(Field)

- value of a field

StackFrame.getValue(LocalVariable)

- value of a variable

VirtualMachine.mirrorOf(double)

- created in the target VM by the JDI client

ModificationWatchpointEvent.valueToBe()

- returned with an event

The following tables illustrate which subinterfaces of Value
are used to mirror values in the target VM --

Subinterfaces of

PrimitiveValue

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a boolean

true

BooleanValue

BooleanType

a byte

(byte)4

ByteValue

ByteType

a char

'a'

CharValue

CharType

a double

3.1415926

DoubleValue

DoubleType

a float

2.5f

FloatValue

FloatType

an int

22

IntegerValue

IntegerType

a long

1024L

LongValue

LongType

a short

(short)12

ShortValue

ShortType

a void

VoidValue

VoidType

Subinterfaces of

ObjectReference

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a class instance

this

ObjectReference

ClassType

an array

new int[5]

ArrayReference

ArrayType

a string

"hello"

StringReference

ClassType

a thread

Thread.currentThread()

ThreadReference

ClassType

a thread group

Thread.currentThread()

.getThreadGroup()

ThreadGroupReference

ClassType

a

java.lang.Class

instance

this.getClass()

ClassObjectReference

ClassType

a class loader

this.getClass()

.getClassLoader()

ClassLoaderReference

ClassType

Other values

Kind of value

For example -

expression in target

Is mirrored as

Type

of value

null

null

null

n/a

Some examples of where values may be accessed:

ObjectReference.getValue(Field)

- value of a field

StackFrame.getValue(LocalVariable)

- value of a variable

VirtualMachine.mirrorOf(double)

- created in the target VM by the JDI client

ModificationWatchpointEvent.valueToBe()

- returned with an event

The following tables illustrate which subinterfaces of Value
are used to mirror values in the target VM --

Subinterfaces of

PrimitiveValue

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a boolean

true

BooleanValue

BooleanType

a byte

(byte)4

ByteValue

ByteType

a char

'a'

CharValue

CharType

a double

3.1415926

DoubleValue

DoubleType

a float

2.5f

FloatValue

FloatType

an int

22

IntegerValue

IntegerType

a long

1024L

LongValue

LongType

a short

(short)12

ShortValue

ShortType

a void

VoidValue

VoidType

Subinterfaces of

ObjectReference

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a class instance

this

ObjectReference

ClassType

an array

new int[5]

ArrayReference

ArrayType

a string

"hello"

StringReference

ClassType

a thread

Thread.currentThread()

ThreadReference

ClassType

a thread group

Thread.currentThread()

.getThreadGroup()

ThreadGroupReference

ClassType

a

java.lang.Class

instance

this.getClass()

ClassObjectReference

ClassType

a class loader

this.getClass()

.getClassLoader()

ClassLoaderReference

ClassType

Other values

Kind of value

For example -

expression in target

Is mirrored as

Type

of value

null

null

null

n/a

The following tables illustrate which subinterfaces of Value
are used to mirror values in the target VM --

Subinterfaces of

PrimitiveValue

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a boolean

true

BooleanValue

BooleanType

a byte

(byte)4

ByteValue

ByteType

a char

'a'

CharValue

CharType

a double

3.1415926

DoubleValue

DoubleType

a float

2.5f

FloatValue

FloatType

an int

22

IntegerValue

IntegerType

a long

1024L

LongValue

LongType

a short

(short)12

ShortValue

ShortType

a void

VoidValue

VoidType

Subinterfaces of

ObjectReference

Kind of value

For example -

expression in target

Is mirrored as an

instance of

Type

of value

Value.type()

a class instance

this

ObjectReference

ClassType

an array

new int[5]

ArrayReference

ArrayType

a string

"hello"

StringReference

ClassType

a thread

Thread.currentThread()

ThreadReference

ClassType

a thread group

Thread.currentThread()

.getThreadGroup()

ThreadGroupReference

ClassType

a

java.lang.Class

instance

this.getClass()

ClassObjectReference

ClassType

a class loader

this.getClass()

.getClassLoader()

ClassLoaderReference

ClassType

Other values

Kind of value

For example -

expression in target

Is mirrored as

Type

of value

null

null

null

n/a

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Type

type

()

Returns the run-time type of this value.

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

Type

type

()

Returns the run-time type of this value.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Returns the run-time type of this value.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- type

```java
Type
type()
```

Returns the run-time type of this value.

**Returns:** a

Type

which mirrors the value's type in the
target VM.
**See Also:** Type

Method Detail

- type

```java
Type
type()
```

Returns the run-time type of this value.

**Returns:** a

Type

which mirrors the value's type in the
target VM.
**See Also:** Type

---

#### Method Detail

type

```java
Type
type()
```

Returns the run-time type of this value.

**Returns:** a

Type

which mirrors the value's type in the
target VM.
**See Also:** Type

---

#### type

Type

type()

Returns the run-time type of this value.

---

