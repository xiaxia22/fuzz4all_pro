# Class ConstantBootstraps

**Source:** `java.base\java\lang\invoke\ConstantBootstraps.html`

### Class Description

```java
public final class
ConstantBootstraps

extends
Object
```

Bootstrap methods for dynamically-computed constants.

The bootstrap methods in this class will throw a

NullPointerException

for any reference argument that is

null

,
unless the argument is specified to be unused or specified to accept a

null

value.

**Since:** 11

---

### Field Details

*No entries found.*

### Constructor Details

#### public ConstantBootstraps()

*No description found.*

---

### Method Details

#### public static
Object
nullConstant​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)

Returns a

null

object reference for the reference type specified
by

type

.

**Parameters:**
- lookup

- unused
- name

- unused
- type

- a reference type

**Returns:**
- a

null

value

**Throws:**
- IllegalArgumentException

- if

type

is not a reference type

---

#### public static
Class
<?> primitiveClass​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)

Returns a

Class

mirror for the primitive type whose type
descriptor is specified by

name

.

**Parameters:**
- lookup

- unused
- name

- the descriptor (JVMS 4.3) of the desired primitive type
- type

- the required result type (must be

Class.class

)

**Returns:**
- the

Class

mirror

**Throws:**
- IllegalArgumentException

- if the name is not a descriptor for a
primitive type or the type is not

Class.class

---

#### public static <E extends
Enum
<E>> E enumConstant​(
MethodHandles.Lookup
lookup,

String
name,

Class
<E> type)

Returns an

enum

constant of the type specified by

type

with the name specified by

name

.

**Parameters:**
- lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
- name

- the name of the constant to return, which must exactly match
an enum constant in the specified type.
- type

- the

Class

object describing the enum type for which
a constant is to be returned

**Returns:**
- the enum constant of the specified enum type with the
specified name

**Throws:**
- IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
- IllegalArgumentException

- if the specified enum type has
no constant with the specified name, or the specified
class object does not represent an enum type

**See Also:**
- Enum.valueOf(Class, String)

**Type Parameters:**
- E

- The enum type for which a constant value is to be returned

---

#### public static
Object
getStaticFinal​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type,

Class
<?> declaringClass)

Returns the value of a static final field.

**Parameters:**
- lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
- name

- the name of the field
- type

- the type of the field
- declaringClass

- the class in which the field is declared

**Returns:**
- the value of the field

**Throws:**
- IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
- NoSuchFieldError

- if the specified field does not exist
- IncompatibleClassChangeError

- if the specified field is not

final

---

#### public static
Object
getStaticFinal​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)

Returns the value of a static final field declared in the class which
is the same as the field's type (or, for primitive-valued fields,
declared in the wrapper class.) This is a simplified form of

getStaticFinal(MethodHandles.Lookup, String, Class, Class)

for the case where a class declares distinguished constant instances of
itself.

**Parameters:**
- lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
- name

- the name of the field
- type

- the type of the field

**Returns:**
- the value of the field

**Throws:**
- IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
- NoSuchFieldError

- if the specified field does not exist
- IncompatibleClassChangeError

- if the specified field is not

final

**See Also:**
- getStaticFinal(MethodHandles.Lookup, String, Class, Class)

---

#### public static
Object
invoke​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type,

MethodHandle
handle,

Object
... args)
throws
Throwable

Returns the result of invoking a method handle with the provided
arguments.

This method behaves as if the method handle to be invoked is the result
of adapting the given method handle, via

MethodHandle.asType(java.lang.invoke.MethodType)

, to
adjust the return type to the desired type.

**Parameters:**
- lookup

- unused
- name

- unused
- type

- the desired type of the value to be returned, which must be
compatible with the return type of the method handle
- handle

- the method handle to be invoked
- args

- the arguments to pass to the method handle, as if with

MethodHandle.invokeWithArguments(java.lang.Object...)

. Each argument may be

null

.

**Returns:**
- the result of invoking the method handle

**Throws:**
- WrongMethodTypeException

- if the handle's method type cannot be
adjusted to take the given number of arguments, or if the handle's return
type cannot be adjusted to the desired type
- ClassCastException

- if an argument or the result produced by
invoking the handle cannot be converted by reference casting
- Throwable

- anything thrown by the method handle invocation

---

#### public static
VarHandle
fieldVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> declaringClass,

Class
<?> fieldType)

Finds a

VarHandle

for an instance field.

**Parameters:**
- lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
- name

- the name of the field
- type

- the required result type (must be

Class<VarHandle>

)
- declaringClass

- the class in which the field is declared
- fieldType

- the type of the field

**Returns:**
- the

VarHandle

**Throws:**
- IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
- NoSuchFieldError

- if the specified field does not exist
- IllegalArgumentException

- if the type is not

VarHandle

---

#### public static
VarHandle
staticFieldVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> declaringClass,

Class
<?> fieldType)

Finds a

VarHandle

for a static field.

**Parameters:**
- lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
- name

- the name of the field
- type

- the required result type (must be

Class<VarHandle>

)
- declaringClass

- the class in which the field is declared
- fieldType

- the type of the field

**Returns:**
- the

VarHandle

**Throws:**
- IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
- NoSuchFieldError

- if the specified field does not exist
- IllegalArgumentException

- if the type is not

VarHandle

---

#### public static
VarHandle
arrayVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> arrayClass)

Finds a

VarHandle

for an array type.

**Parameters:**
- lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
- name

- unused
- type

- the required result type (must be

Class<VarHandle>

)
- arrayClass

- the type of the array

**Returns:**
- the

VarHandle

**Throws:**
- IllegalAccessError

- if the component type of the array is not
accessible to the class performing the operation
- IllegalArgumentException

- if the type is not

VarHandle

---

### Additional Sections

#### Class ConstantBootstraps

java.lang.Object

- java.lang.invoke.ConstantBootstraps

java.lang.invoke.ConstantBootstraps

```java
public final class
ConstantBootstraps

extends
Object
```

Bootstrap methods for dynamically-computed constants.

The bootstrap methods in this class will throw a

NullPointerException

for any reference argument that is

null

,
unless the argument is specified to be unused or specified to accept a

null

value.

**Since:** 11

public final class

ConstantBootstraps

extends

Object

Bootstrap methods for dynamically-computed constants.

The bootstrap methods in this class will throw a

NullPointerException

for any reference argument that is

null

,
unless the argument is specified to be unused or specified to accept a

null

value.

The bootstrap methods in this class will throw a

NullPointerException

for any reference argument that is

null

,
unless the argument is specified to be unused or specified to accept a

null

value.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ConstantBootstraps

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

VarHandle

arrayVarHandle

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<

VarHandle

> type,

Class

<?> arrayClass)

Finds a

VarHandle

for an array type.

static <E extends

Enum

<E>>

E

enumConstant

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<E> type)

Returns an

enum

constant of the type specified by

type

with the name specified by

name

.

static

VarHandle

fieldVarHandle

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<

VarHandle

> type,

Class

<?> declaringClass,

Class

<?> fieldType)

Finds a

VarHandle

for an instance field.

static

Object

getStaticFinal

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type)

Returns the value of a static final field declared in the class which
is the same as the field's type (or, for primitive-valued fields,
declared in the wrapper class.)

static

Object

getStaticFinal

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type,

Class

<?> declaringClass)

Returns the value of a static final field.

static

Object

invoke

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type,

MethodHandle

handle,

Object

... args)

Returns the result of invoking a method handle with the provided
arguments.

static

Object

nullConstant

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type)

Returns a

null

object reference for the reference type specified
by

type

.

static

Class

<?>

primitiveClass

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type)

Returns a

Class

mirror for the primitive type whose type
descriptor is specified by

name

.

static

VarHandle

staticFieldVarHandle

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<

VarHandle

> type,

Class

<?> declaringClass,

Class

<?> fieldType)

Finds a

VarHandle

for a static field.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

ConstantBootstraps

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

VarHandle

arrayVarHandle

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<

VarHandle

> type,

Class

<?> arrayClass)

Finds a

VarHandle

for an array type.

static <E extends

Enum

<E>>

E

enumConstant

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<E> type)

Returns an

enum

constant of the type specified by

type

with the name specified by

name

.

static

VarHandle

fieldVarHandle

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<

VarHandle

> type,

Class

<?> declaringClass,

Class

<?> fieldType)

Finds a

VarHandle

for an instance field.

static

Object

getStaticFinal

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type)

Returns the value of a static final field declared in the class which
is the same as the field's type (or, for primitive-valued fields,
declared in the wrapper class.)

static

Object

getStaticFinal

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type,

Class

<?> declaringClass)

Returns the value of a static final field.

static

Object

invoke

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type,

MethodHandle

handle,

Object

... args)

Returns the result of invoking a method handle with the provided
arguments.

static

Object

nullConstant

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type)

Returns a

null

object reference for the reference type specified
by

type

.

static

Class

<?>

primitiveClass

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type)

Returns a

Class

mirror for the primitive type whose type
descriptor is specified by

name

.

static

VarHandle

staticFieldVarHandle

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<

VarHandle

> type,

Class

<?> declaringClass,

Class

<?> fieldType)

Finds a

VarHandle

for a static field.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Finds a

VarHandle

for an array type.

Returns an

enum

constant of the type specified by

type

with the name specified by

name

.

Finds a

VarHandle

for an instance field.

Returns the value of a static final field declared in the class which
is the same as the field's type (or, for primitive-valued fields,
declared in the wrapper class.)

Returns the value of a static final field.

Returns the result of invoking a method handle with the provided
arguments.

Returns a

null

object reference for the reference type specified
by

type

.

Returns a

Class

mirror for the primitive type whose type
descriptor is specified by

name

.

Finds a

VarHandle

for a static field.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ConstantBootstraps

```java
public ConstantBootstraps()
```

============ METHOD DETAIL ==========

- Method Detail

- nullConstant

```java
public static
Object
nullConstant​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)
```

Returns a

null

object reference for the reference type specified
by

type

.

**Parameters:** lookup

- unused
**Parameters:** name

- unused
**Parameters:** type

- a reference type
**Returns:** a

null

value
**Throws:** IllegalArgumentException

- if

type

is not a reference type

- primitiveClass

```java
public static
Class
<?> primitiveClass​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)
```

Returns a

Class

mirror for the primitive type whose type
descriptor is specified by

name

.

**Parameters:** lookup

- unused
**Parameters:** name

- the descriptor (JVMS 4.3) of the desired primitive type
**Parameters:** type

- the required result type (must be

Class.class

)
**Returns:** the

Class

mirror
**Throws:** IllegalArgumentException

- if the name is not a descriptor for a
primitive type or the type is not

Class.class

- enumConstant

```java
public static <E extends
Enum
<E>> E enumConstant​(
MethodHandles.Lookup
lookup,

String
name,

Class
<E> type)
```

Returns an

enum

constant of the type specified by

type

with the name specified by

name

.

**Type Parameters:** E

- The enum type for which a constant value is to be returned
**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the constant to return, which must exactly match
an enum constant in the specified type.
**Parameters:** type

- the

Class

object describing the enum type for which
a constant is to be returned
**Returns:** the enum constant of the specified enum type with the
specified name
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** IllegalArgumentException

- if the specified enum type has
no constant with the specified name, or the specified
class object does not represent an enum type
**See Also:** Enum.valueOf(Class, String)

- getStaticFinal

```java
public static
Object
getStaticFinal​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type,

Class
<?> declaringClass)
```

Returns the value of a static final field.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Parameters:** declaringClass

- the class in which the field is declared
**Returns:** the value of the field
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IncompatibleClassChangeError

- if the specified field is not

final

- getStaticFinal

```java
public static
Object
getStaticFinal​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)
```

Returns the value of a static final field declared in the class which
is the same as the field's type (or, for primitive-valued fields,
declared in the wrapper class.) This is a simplified form of

getStaticFinal(MethodHandles.Lookup, String, Class, Class)

for the case where a class declares distinguished constant instances of
itself.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Returns:** the value of the field
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IncompatibleClassChangeError

- if the specified field is not

final
**See Also:** getStaticFinal(MethodHandles.Lookup, String, Class, Class)

- invoke

```java
public static
Object
invoke​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type,

MethodHandle
handle,

Object
... args)
throws
Throwable
```

Returns the result of invoking a method handle with the provided
arguments.

This method behaves as if the method handle to be invoked is the result
of adapting the given method handle, via

MethodHandle.asType(java.lang.invoke.MethodType)

, to
adjust the return type to the desired type.

**Parameters:** lookup

- unused
**Parameters:** name

- unused
**Parameters:** type

- the desired type of the value to be returned, which must be
compatible with the return type of the method handle
**Parameters:** handle

- the method handle to be invoked
**Parameters:** args

- the arguments to pass to the method handle, as if with

MethodHandle.invokeWithArguments(java.lang.Object...)

. Each argument may be

null

.
**Returns:** the result of invoking the method handle
**Throws:** WrongMethodTypeException

- if the handle's method type cannot be
adjusted to take the given number of arguments, or if the handle's return
type cannot be adjusted to the desired type
**Throws:** ClassCastException

- if an argument or the result produced by
invoking the handle cannot be converted by reference casting
**Throws:** Throwable

- anything thrown by the method handle invocation

- fieldVarHandle

```java
public static
VarHandle
fieldVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> declaringClass,

Class
<?> fieldType)
```

Finds a

VarHandle

for an instance field.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the required result type (must be

Class<VarHandle>

)
**Parameters:** declaringClass

- the class in which the field is declared
**Parameters:** fieldType

- the type of the field
**Returns:** the

VarHandle
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IllegalArgumentException

- if the type is not

VarHandle

- staticFieldVarHandle

```java
public static
VarHandle
staticFieldVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> declaringClass,

Class
<?> fieldType)
```

Finds a

VarHandle

for a static field.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the required result type (must be

Class<VarHandle>

)
**Parameters:** declaringClass

- the class in which the field is declared
**Parameters:** fieldType

- the type of the field
**Returns:** the

VarHandle
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IllegalArgumentException

- if the type is not

VarHandle

- arrayVarHandle

```java
public static
VarHandle
arrayVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> arrayClass)
```

Finds a

VarHandle

for an array type.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- unused
**Parameters:** type

- the required result type (must be

Class<VarHandle>

)
**Parameters:** arrayClass

- the type of the array
**Returns:** the

VarHandle
**Throws:** IllegalAccessError

- if the component type of the array is not
accessible to the class performing the operation
**Throws:** IllegalArgumentException

- if the type is not

VarHandle

Constructor Detail

- ConstantBootstraps

```java
public ConstantBootstraps()
```

---

#### Constructor Detail

ConstantBootstraps

```java
public ConstantBootstraps()
```

---

#### ConstantBootstraps

public ConstantBootstraps()

Method Detail

- nullConstant

```java
public static
Object
nullConstant​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)
```

Returns a

null

object reference for the reference type specified
by

type

.

**Parameters:** lookup

- unused
**Parameters:** name

- unused
**Parameters:** type

- a reference type
**Returns:** a

null

value
**Throws:** IllegalArgumentException

- if

type

is not a reference type

- primitiveClass

```java
public static
Class
<?> primitiveClass​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)
```

Returns a

Class

mirror for the primitive type whose type
descriptor is specified by

name

.

**Parameters:** lookup

- unused
**Parameters:** name

- the descriptor (JVMS 4.3) of the desired primitive type
**Parameters:** type

- the required result type (must be

Class.class

)
**Returns:** the

Class

mirror
**Throws:** IllegalArgumentException

- if the name is not a descriptor for a
primitive type or the type is not

Class.class

- enumConstant

```java
public static <E extends
Enum
<E>> E enumConstant​(
MethodHandles.Lookup
lookup,

String
name,

Class
<E> type)
```

Returns an

enum

constant of the type specified by

type

with the name specified by

name

.

**Type Parameters:** E

- The enum type for which a constant value is to be returned
**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the constant to return, which must exactly match
an enum constant in the specified type.
**Parameters:** type

- the

Class

object describing the enum type for which
a constant is to be returned
**Returns:** the enum constant of the specified enum type with the
specified name
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** IllegalArgumentException

- if the specified enum type has
no constant with the specified name, or the specified
class object does not represent an enum type
**See Also:** Enum.valueOf(Class, String)

- getStaticFinal

```java
public static
Object
getStaticFinal​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type,

Class
<?> declaringClass)
```

Returns the value of a static final field.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Parameters:** declaringClass

- the class in which the field is declared
**Returns:** the value of the field
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IncompatibleClassChangeError

- if the specified field is not

final

- getStaticFinal

```java
public static
Object
getStaticFinal​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)
```

Returns the value of a static final field declared in the class which
is the same as the field's type (or, for primitive-valued fields,
declared in the wrapper class.) This is a simplified form of

getStaticFinal(MethodHandles.Lookup, String, Class, Class)

for the case where a class declares distinguished constant instances of
itself.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Returns:** the value of the field
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IncompatibleClassChangeError

- if the specified field is not

final
**See Also:** getStaticFinal(MethodHandles.Lookup, String, Class, Class)

- invoke

```java
public static
Object
invoke​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type,

MethodHandle
handle,

Object
... args)
throws
Throwable
```

Returns the result of invoking a method handle with the provided
arguments.

This method behaves as if the method handle to be invoked is the result
of adapting the given method handle, via

MethodHandle.asType(java.lang.invoke.MethodType)

, to
adjust the return type to the desired type.

**Parameters:** lookup

- unused
**Parameters:** name

- unused
**Parameters:** type

- the desired type of the value to be returned, which must be
compatible with the return type of the method handle
**Parameters:** handle

- the method handle to be invoked
**Parameters:** args

- the arguments to pass to the method handle, as if with

MethodHandle.invokeWithArguments(java.lang.Object...)

. Each argument may be

null

.
**Returns:** the result of invoking the method handle
**Throws:** WrongMethodTypeException

- if the handle's method type cannot be
adjusted to take the given number of arguments, or if the handle's return
type cannot be adjusted to the desired type
**Throws:** ClassCastException

- if an argument or the result produced by
invoking the handle cannot be converted by reference casting
**Throws:** Throwable

- anything thrown by the method handle invocation

- fieldVarHandle

```java
public static
VarHandle
fieldVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> declaringClass,

Class
<?> fieldType)
```

Finds a

VarHandle

for an instance field.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the required result type (must be

Class<VarHandle>

)
**Parameters:** declaringClass

- the class in which the field is declared
**Parameters:** fieldType

- the type of the field
**Returns:** the

VarHandle
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IllegalArgumentException

- if the type is not

VarHandle

- staticFieldVarHandle

```java
public static
VarHandle
staticFieldVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> declaringClass,

Class
<?> fieldType)
```

Finds a

VarHandle

for a static field.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the required result type (must be

Class<VarHandle>

)
**Parameters:** declaringClass

- the class in which the field is declared
**Parameters:** fieldType

- the type of the field
**Returns:** the

VarHandle
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IllegalArgumentException

- if the type is not

VarHandle

- arrayVarHandle

```java
public static
VarHandle
arrayVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> arrayClass)
```

Finds a

VarHandle

for an array type.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- unused
**Parameters:** type

- the required result type (must be

Class<VarHandle>

)
**Parameters:** arrayClass

- the type of the array
**Returns:** the

VarHandle
**Throws:** IllegalAccessError

- if the component type of the array is not
accessible to the class performing the operation
**Throws:** IllegalArgumentException

- if the type is not

VarHandle

---

#### Method Detail

nullConstant

```java
public static
Object
nullConstant​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)
```

Returns a

null

object reference for the reference type specified
by

type

.

**Parameters:** lookup

- unused
**Parameters:** name

- unused
**Parameters:** type

- a reference type
**Returns:** a

null

value
**Throws:** IllegalArgumentException

- if

type

is not a reference type

---

#### nullConstant

public static

Object

nullConstant​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type)

Returns a

null

object reference for the reference type specified
by

type

.

primitiveClass

```java
public static
Class
<?> primitiveClass​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)
```

Returns a

Class

mirror for the primitive type whose type
descriptor is specified by

name

.

**Parameters:** lookup

- unused
**Parameters:** name

- the descriptor (JVMS 4.3) of the desired primitive type
**Parameters:** type

- the required result type (must be

Class.class

)
**Returns:** the

Class

mirror
**Throws:** IllegalArgumentException

- if the name is not a descriptor for a
primitive type or the type is not

Class.class

---

#### primitiveClass

public static

Class

<?> primitiveClass​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type)

Returns a

Class

mirror for the primitive type whose type
descriptor is specified by

name

.

enumConstant

```java
public static <E extends
Enum
<E>> E enumConstant​(
MethodHandles.Lookup
lookup,

String
name,

Class
<E> type)
```

Returns an

enum

constant of the type specified by

type

with the name specified by

name

.

**Type Parameters:** E

- The enum type for which a constant value is to be returned
**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the constant to return, which must exactly match
an enum constant in the specified type.
**Parameters:** type

- the

Class

object describing the enum type for which
a constant is to be returned
**Returns:** the enum constant of the specified enum type with the
specified name
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** IllegalArgumentException

- if the specified enum type has
no constant with the specified name, or the specified
class object does not represent an enum type
**See Also:** Enum.valueOf(Class, String)

---

#### enumConstant

public static <E extends

Enum

<E>> E enumConstant​(

MethodHandles.Lookup

lookup,

String

name,

Class

<E> type)

Returns an

enum

constant of the type specified by

type

with the name specified by

name

.

getStaticFinal

```java
public static
Object
getStaticFinal​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type,

Class
<?> declaringClass)
```

Returns the value of a static final field.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Parameters:** declaringClass

- the class in which the field is declared
**Returns:** the value of the field
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IncompatibleClassChangeError

- if the specified field is not

final

---

#### getStaticFinal

public static

Object

getStaticFinal​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type,

Class

<?> declaringClass)

Returns the value of a static final field.

getStaticFinal

```java
public static
Object
getStaticFinal​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type)
```

Returns the value of a static final field declared in the class which
is the same as the field's type (or, for primitive-valued fields,
declared in the wrapper class.) This is a simplified form of

getStaticFinal(MethodHandles.Lookup, String, Class, Class)

for the case where a class declares distinguished constant instances of
itself.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Returns:** the value of the field
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IncompatibleClassChangeError

- if the specified field is not

final
**See Also:** getStaticFinal(MethodHandles.Lookup, String, Class, Class)

---

#### getStaticFinal

public static

Object

getStaticFinal​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type)

Returns the value of a static final field declared in the class which
is the same as the field's type (or, for primitive-valued fields,
declared in the wrapper class.) This is a simplified form of

getStaticFinal(MethodHandles.Lookup, String, Class, Class)

for the case where a class declares distinguished constant instances of
itself.

invoke

```java
public static
Object
invoke​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> type,

MethodHandle
handle,

Object
... args)
throws
Throwable
```

Returns the result of invoking a method handle with the provided
arguments.

This method behaves as if the method handle to be invoked is the result
of adapting the given method handle, via

MethodHandle.asType(java.lang.invoke.MethodType)

, to
adjust the return type to the desired type.

**Parameters:** lookup

- unused
**Parameters:** name

- unused
**Parameters:** type

- the desired type of the value to be returned, which must be
compatible with the return type of the method handle
**Parameters:** handle

- the method handle to be invoked
**Parameters:** args

- the arguments to pass to the method handle, as if with

MethodHandle.invokeWithArguments(java.lang.Object...)

. Each argument may be

null

.
**Returns:** the result of invoking the method handle
**Throws:** WrongMethodTypeException

- if the handle's method type cannot be
adjusted to take the given number of arguments, or if the handle's return
type cannot be adjusted to the desired type
**Throws:** ClassCastException

- if an argument or the result produced by
invoking the handle cannot be converted by reference casting
**Throws:** Throwable

- anything thrown by the method handle invocation

---

#### invoke

public static

Object

invoke​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> type,

MethodHandle

handle,

Object

... args)
throws

Throwable

Returns the result of invoking a method handle with the provided
arguments.

This method behaves as if the method handle to be invoked is the result
of adapting the given method handle, via

MethodHandle.asType(java.lang.invoke.MethodType)

, to
adjust the return type to the desired type.

This method behaves as if the method handle to be invoked is the result
of adapting the given method handle, via

MethodHandle.asType(java.lang.invoke.MethodType)

, to
adjust the return type to the desired type.

fieldVarHandle

```java
public static
VarHandle
fieldVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> declaringClass,

Class
<?> fieldType)
```

Finds a

VarHandle

for an instance field.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the required result type (must be

Class<VarHandle>

)
**Parameters:** declaringClass

- the class in which the field is declared
**Parameters:** fieldType

- the type of the field
**Returns:** the

VarHandle
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IllegalArgumentException

- if the type is not

VarHandle

---

#### fieldVarHandle

public static

VarHandle

fieldVarHandle​(

MethodHandles.Lookup

lookup,

String

name,

Class

<

VarHandle

> type,

Class

<?> declaringClass,

Class

<?> fieldType)

Finds a

VarHandle

for an instance field.

staticFieldVarHandle

```java
public static
VarHandle
staticFieldVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> declaringClass,

Class
<?> fieldType)
```

Finds a

VarHandle

for a static field.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- the name of the field
**Parameters:** type

- the required result type (must be

Class<VarHandle>

)
**Parameters:** declaringClass

- the class in which the field is declared
**Parameters:** fieldType

- the type of the field
**Returns:** the

VarHandle
**Throws:** IllegalAccessError

- if the declaring class or the field is not
accessible to the class performing the operation
**Throws:** NoSuchFieldError

- if the specified field does not exist
**Throws:** IllegalArgumentException

- if the type is not

VarHandle

---

#### staticFieldVarHandle

public static

VarHandle

staticFieldVarHandle​(

MethodHandles.Lookup

lookup,

String

name,

Class

<

VarHandle

> type,

Class

<?> declaringClass,

Class

<?> fieldType)

Finds a

VarHandle

for a static field.

arrayVarHandle

```java
public static
VarHandle
arrayVarHandle​(
MethodHandles.Lookup
lookup,

String
name,

Class
<
VarHandle
> type,

Class
<?> arrayClass)
```

Finds a

VarHandle

for an array type.

**Parameters:** lookup

- the lookup context describing the class performing the
operation (normally stacked by the JVM)
**Parameters:** name

- unused
**Parameters:** type

- the required result type (must be

Class<VarHandle>

)
**Parameters:** arrayClass

- the type of the array
**Returns:** the

VarHandle
**Throws:** IllegalAccessError

- if the component type of the array is not
accessible to the class performing the operation
**Throws:** IllegalArgumentException

- if the type is not

VarHandle

---

#### arrayVarHandle

public static

VarHandle

arrayVarHandle​(

MethodHandles.Lookup

lookup,

String

name,

Class

<

VarHandle

> type,

Class

<?> arrayClass)

Finds a

VarHandle

for an array type.

---

