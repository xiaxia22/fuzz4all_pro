# Class Guards

**Source:** `jdk.dynalink\jdk\dynalink\linker\support\Guards.html`

### Class Description

```java
public final class
Guards

extends
Object
```

Utility methods for creating typical guards for

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

and for adjusting their method types.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
MethodHandle
isOfClass​(
Class
<?> clazz,

MethodType
type)

Creates a guard method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is of the specified class (exactly of it, not a subclass). The rest of the
arguments will be ignored.

**Parameters:**
- clazz

- the class of the first argument to test for
- type

- the method type

**Returns:**
- a method handle testing whether its first argument is of the specified class.

---

#### public static
MethodHandle
isInstance​(
Class
<?> clazz,

MethodType
type)

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

**Parameters:**
- clazz

- the class of the first argument to test for
- type

- the method type

**Returns:**
- a method handle testing whether its first argument is of the specified class or subclass.

---

#### public static
MethodHandle
isInstance​(
Class
<?> clazz,
int pos,

MethodType
type)

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the n'th argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

**Parameters:**
- clazz

- the class of the first argument to test for
- pos

- the position on the argument list to test
- type

- the method type

**Returns:**
- a method handle testing whether its first argument is of the specified class or subclass.

---

#### public static
MethodHandle
isArray​(int pos,

MethodType
type)

Creates a method handle that returns true if the argument in the specified position is a Java array.

**Parameters:**
- pos

- the position in the argument lit
- type

- the method type of the handle

**Returns:**
- a method handle that returns true if the argument in the specified position is a Java array; the rest of
the arguments are ignored.

---

#### public static
MethodHandle
asType​(
MethodHandle
test,

MethodType
type)

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

MethodHandle.asType(MethodType)

to convert types and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

**Parameters:**
- test

- the test method handle
- type

- the type to adapt the method handle to

**Returns:**
- the adapted method handle

---

#### public static
MethodHandle
asType​(
LinkerServices
linkerServices,

MethodHandle
test,

MethodType
type)

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

LinkerServices.asType(MethodHandle, MethodType)

to convert types
and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

**Parameters:**
- linkerServices

- the linker services to use for type conversions
- test

- the test method handle
- type

- the type to adapt the method handle to

**Returns:**
- the adapted method handle

---

#### public static
MethodHandle
getClassGuard​(
Class
<?> clazz)

Creates a guard method that tests its only argument for being of an exact particular class.

**Parameters:**
- clazz

- the class to test for.

**Returns:**
- the desired guard method.

---

#### public static
MethodHandle
getInstanceOfGuard​(
Class
<?> clazz)

Creates a guard method that tests its only argument for being an instance of a particular class.

**Parameters:**
- clazz

- the class to test for.

**Returns:**
- the desired guard method.

---

#### public static
MethodHandle
getIdentityGuard​(
Object
obj)

Creates a guard method that tests its only argument for being referentially identical to another object

**Parameters:**
- obj

- the object used as referential identity test

**Returns:**
- the desired guard method.

---

#### public static
MethodHandle
isNull()

Returns a guard that tests whether the first argument is null.

**Returns:**
- a guard that tests whether the first argument is null.

---

#### public static
MethodHandle
isNotNull()

Returns a guard that tests whether the first argument is not null.

**Returns:**
- a guard that tests whether the first argument is not null.

---

### Additional Sections

#### Class Guards

java.lang.Object

- jdk.dynalink.linker.support.Guards

jdk.dynalink.linker.support.Guards

```java
public final class
Guards

extends
Object
```

Utility methods for creating typical guards for

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

and for adjusting their method types.

public final class

Guards

extends

Object

Utility methods for creating typical guards for

MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)

and for adjusting their method types.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

MethodHandle

asType

​(

MethodHandle

test,

MethodType

type)

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean.

static

MethodHandle

asType

​(

LinkerServices

linkerServices,

MethodHandle

test,

MethodType

type)

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean.

static

MethodHandle

getClassGuard

​(

Class

<?> clazz)

Creates a guard method that tests its only argument for being of an exact particular class.

static

MethodHandle

getIdentityGuard

​(

Object

obj)

Creates a guard method that tests its only argument for being referentially identical to another object

static

MethodHandle

getInstanceOfGuard

​(

Class

<?> clazz)

Creates a guard method that tests its only argument for being an instance of a particular class.

static

MethodHandle

isArray

​(int pos,

MethodType

type)

Creates a method handle that returns true if the argument in the specified position is a Java array.

static

MethodHandle

isInstance

​(

Class

<?> clazz,
int pos,

MethodType

type)

Creates a method handle with arguments of a specified type, but with boolean return value.

static

MethodHandle

isInstance

​(

Class

<?> clazz,

MethodType

type)

Creates a method handle with arguments of a specified type, but with boolean return value.

static

MethodHandle

isNotNull

()

Returns a guard that tests whether the first argument is not null.

static

MethodHandle

isNull

()

Returns a guard that tests whether the first argument is null.

static

MethodHandle

isOfClass

​(

Class

<?> clazz,

MethodType

type)

Creates a guard method handle with arguments of a specified type, but with boolean return value.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

MethodHandle

asType

​(

MethodHandle

test,

MethodType

type)

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean.

static

MethodHandle

asType

​(

LinkerServices

linkerServices,

MethodHandle

test,

MethodType

type)

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean.

static

MethodHandle

getClassGuard

​(

Class

<?> clazz)

Creates a guard method that tests its only argument for being of an exact particular class.

static

MethodHandle

getIdentityGuard

​(

Object

obj)

Creates a guard method that tests its only argument for being referentially identical to another object

static

MethodHandle

getInstanceOfGuard

​(

Class

<?> clazz)

Creates a guard method that tests its only argument for being an instance of a particular class.

static

MethodHandle

isArray

​(int pos,

MethodType

type)

Creates a method handle that returns true if the argument in the specified position is a Java array.

static

MethodHandle

isInstance

​(

Class

<?> clazz,
int pos,

MethodType

type)

Creates a method handle with arguments of a specified type, but with boolean return value.

static

MethodHandle

isInstance

​(

Class

<?> clazz,

MethodType

type)

Creates a method handle with arguments of a specified type, but with boolean return value.

static

MethodHandle

isNotNull

()

Returns a guard that tests whether the first argument is not null.

static

MethodHandle

isNull

()

Returns a guard that tests whether the first argument is null.

static

MethodHandle

isOfClass

​(

Class

<?> clazz,

MethodType

type)

Creates a guard method handle with arguments of a specified type, but with boolean return value.

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

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean.

Creates a guard method that tests its only argument for being of an exact particular class.

Creates a guard method that tests its only argument for being referentially identical to another object

Creates a guard method that tests its only argument for being an instance of a particular class.

Creates a method handle that returns true if the argument in the specified position is a Java array.

Creates a method handle with arguments of a specified type, but with boolean return value.

Returns a guard that tests whether the first argument is not null.

Returns a guard that tests whether the first argument is null.

Creates a guard method handle with arguments of a specified type, but with boolean return value.

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

============ METHOD DETAIL ==========

- Method Detail

- isOfClass

```java
public static
MethodHandle
isOfClass​(
Class
<?> clazz,

MethodType
type)
```

Creates a guard method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is of the specified class (exactly of it, not a subclass). The rest of the
arguments will be ignored.

**Parameters:** clazz

- the class of the first argument to test for
**Parameters:** type

- the method type
**Returns:** a method handle testing whether its first argument is of the specified class.

- isInstance

```java
public static
MethodHandle
isInstance​(
Class
<?> clazz,

MethodType
type)
```

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

**Parameters:** clazz

- the class of the first argument to test for
**Parameters:** type

- the method type
**Returns:** a method handle testing whether its first argument is of the specified class or subclass.

- isInstance

```java
public static
MethodHandle
isInstance​(
Class
<?> clazz,
int pos,

MethodType
type)
```

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the n'th argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

**Parameters:** clazz

- the class of the first argument to test for
**Parameters:** pos

- the position on the argument list to test
**Parameters:** type

- the method type
**Returns:** a method handle testing whether its first argument is of the specified class or subclass.

- isArray

```java
public static
MethodHandle
isArray​(int pos,

MethodType
type)
```

Creates a method handle that returns true if the argument in the specified position is a Java array.

**Parameters:** pos

- the position in the argument lit
**Parameters:** type

- the method type of the handle
**Returns:** a method handle that returns true if the argument in the specified position is a Java array; the rest of
the arguments are ignored.

- asType

```java
public static
MethodHandle
asType​(
MethodHandle
test,

MethodType
type)
```

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

MethodHandle.asType(MethodType)

to convert types and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

**Parameters:** test

- the test method handle
**Parameters:** type

- the type to adapt the method handle to
**Returns:** the adapted method handle

- asType

```java
public static
MethodHandle
asType​(
LinkerServices
linkerServices,

MethodHandle
test,

MethodType
type)
```

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

LinkerServices.asType(MethodHandle, MethodType)

to convert types
and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

**Parameters:** linkerServices

- the linker services to use for type conversions
**Parameters:** test

- the test method handle
**Parameters:** type

- the type to adapt the method handle to
**Returns:** the adapted method handle

- getClassGuard

```java
public static
MethodHandle
getClassGuard​(
Class
<?> clazz)
```

Creates a guard method that tests its only argument for being of an exact particular class.

**Parameters:** clazz

- the class to test for.
**Returns:** the desired guard method.

- getInstanceOfGuard

```java
public static
MethodHandle
getInstanceOfGuard​(
Class
<?> clazz)
```

Creates a guard method that tests its only argument for being an instance of a particular class.

**Parameters:** clazz

- the class to test for.
**Returns:** the desired guard method.

- getIdentityGuard

```java
public static
MethodHandle
getIdentityGuard​(
Object
obj)
```

Creates a guard method that tests its only argument for being referentially identical to another object

**Parameters:** obj

- the object used as referential identity test
**Returns:** the desired guard method.

- isNull

```java
public static
MethodHandle
isNull()
```

Returns a guard that tests whether the first argument is null.

**Returns:** a guard that tests whether the first argument is null.

- isNotNull

```java
public static
MethodHandle
isNotNull()
```

Returns a guard that tests whether the first argument is not null.

**Returns:** a guard that tests whether the first argument is not null.

Method Detail

- isOfClass

```java
public static
MethodHandle
isOfClass​(
Class
<?> clazz,

MethodType
type)
```

Creates a guard method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is of the specified class (exactly of it, not a subclass). The rest of the
arguments will be ignored.

**Parameters:** clazz

- the class of the first argument to test for
**Parameters:** type

- the method type
**Returns:** a method handle testing whether its first argument is of the specified class.

- isInstance

```java
public static
MethodHandle
isInstance​(
Class
<?> clazz,

MethodType
type)
```

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

**Parameters:** clazz

- the class of the first argument to test for
**Parameters:** type

- the method type
**Returns:** a method handle testing whether its first argument is of the specified class or subclass.

- isInstance

```java
public static
MethodHandle
isInstance​(
Class
<?> clazz,
int pos,

MethodType
type)
```

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the n'th argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

**Parameters:** clazz

- the class of the first argument to test for
**Parameters:** pos

- the position on the argument list to test
**Parameters:** type

- the method type
**Returns:** a method handle testing whether its first argument is of the specified class or subclass.

- isArray

```java
public static
MethodHandle
isArray​(int pos,

MethodType
type)
```

Creates a method handle that returns true if the argument in the specified position is a Java array.

**Parameters:** pos

- the position in the argument lit
**Parameters:** type

- the method type of the handle
**Returns:** a method handle that returns true if the argument in the specified position is a Java array; the rest of
the arguments are ignored.

- asType

```java
public static
MethodHandle
asType​(
MethodHandle
test,

MethodType
type)
```

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

MethodHandle.asType(MethodType)

to convert types and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

**Parameters:** test

- the test method handle
**Parameters:** type

- the type to adapt the method handle to
**Returns:** the adapted method handle

- asType

```java
public static
MethodHandle
asType​(
LinkerServices
linkerServices,

MethodHandle
test,

MethodType
type)
```

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

LinkerServices.asType(MethodHandle, MethodType)

to convert types
and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

**Parameters:** linkerServices

- the linker services to use for type conversions
**Parameters:** test

- the test method handle
**Parameters:** type

- the type to adapt the method handle to
**Returns:** the adapted method handle

- getClassGuard

```java
public static
MethodHandle
getClassGuard​(
Class
<?> clazz)
```

Creates a guard method that tests its only argument for being of an exact particular class.

**Parameters:** clazz

- the class to test for.
**Returns:** the desired guard method.

- getInstanceOfGuard

```java
public static
MethodHandle
getInstanceOfGuard​(
Class
<?> clazz)
```

Creates a guard method that tests its only argument for being an instance of a particular class.

**Parameters:** clazz

- the class to test for.
**Returns:** the desired guard method.

- getIdentityGuard

```java
public static
MethodHandle
getIdentityGuard​(
Object
obj)
```

Creates a guard method that tests its only argument for being referentially identical to another object

**Parameters:** obj

- the object used as referential identity test
**Returns:** the desired guard method.

- isNull

```java
public static
MethodHandle
isNull()
```

Returns a guard that tests whether the first argument is null.

**Returns:** a guard that tests whether the first argument is null.

- isNotNull

```java
public static
MethodHandle
isNotNull()
```

Returns a guard that tests whether the first argument is not null.

**Returns:** a guard that tests whether the first argument is not null.

---

#### Method Detail

isOfClass

```java
public static
MethodHandle
isOfClass​(
Class
<?> clazz,

MethodType
type)
```

Creates a guard method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is of the specified class (exactly of it, not a subclass). The rest of the
arguments will be ignored.

**Parameters:** clazz

- the class of the first argument to test for
**Parameters:** type

- the method type
**Returns:** a method handle testing whether its first argument is of the specified class.

---

#### isOfClass

public static

MethodHandle

isOfClass​(

Class

<?> clazz,

MethodType

type)

Creates a guard method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is of the specified class (exactly of it, not a subclass). The rest of the
arguments will be ignored.

isInstance

```java
public static
MethodHandle
isInstance​(
Class
<?> clazz,

MethodType
type)
```

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

**Parameters:** clazz

- the class of the first argument to test for
**Parameters:** type

- the method type
**Returns:** a method handle testing whether its first argument is of the specified class or subclass.

---

#### isInstance

public static

MethodHandle

isInstance​(

Class

<?> clazz,

MethodType

type)

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the first argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

isInstance

```java
public static
MethodHandle
isInstance​(
Class
<?> clazz,
int pos,

MethodType
type)
```

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the n'th argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

**Parameters:** clazz

- the class of the first argument to test for
**Parameters:** pos

- the position on the argument list to test
**Parameters:** type

- the method type
**Returns:** a method handle testing whether its first argument is of the specified class or subclass.

---

#### isInstance

public static

MethodHandle

isInstance​(

Class

<?> clazz,
int pos,

MethodType

type)

Creates a method handle with arguments of a specified type, but with boolean return value. When invoked, it
returns true if the n'th argument is instance of the specified class or its subclass). The rest of the arguments
will be ignored.

isArray

```java
public static
MethodHandle
isArray​(int pos,

MethodType
type)
```

Creates a method handle that returns true if the argument in the specified position is a Java array.

**Parameters:** pos

- the position in the argument lit
**Parameters:** type

- the method type of the handle
**Returns:** a method handle that returns true if the argument in the specified position is a Java array; the rest of
the arguments are ignored.

---

#### isArray

public static

MethodHandle

isArray​(int pos,

MethodType

type)

Creates a method handle that returns true if the argument in the specified position is a Java array.

asType

```java
public static
MethodHandle
asType​(
MethodHandle
test,

MethodType
type)
```

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

MethodHandle.asType(MethodType)

to convert types and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

**Parameters:** test

- the test method handle
**Parameters:** type

- the type to adapt the method handle to
**Returns:** the adapted method handle

---

#### asType

public static

MethodHandle

asType​(

MethodHandle

test,

MethodType

type)

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

MethodHandle.asType(MethodType)

to convert types and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

asType

```java
public static
MethodHandle
asType​(
LinkerServices
linkerServices,

MethodHandle
test,

MethodType
type)
```

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

LinkerServices.asType(MethodHandle, MethodType)

to convert types
and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

**Parameters:** linkerServices

- the linker services to use for type conversions
**Parameters:** test

- the test method handle
**Parameters:** type

- the type to adapt the method handle to
**Returns:** the adapted method handle

---

#### asType

public static

MethodHandle

asType​(

LinkerServices

linkerServices,

MethodHandle

test,

MethodType

type)

Takes a method handle intended to be used as a guard, and adapts it to
the requested type, but returning a boolean. Applies

LinkerServices.asType(MethodHandle, MethodType)

to convert types
and uses

MethodHandles.dropArguments(MethodHandle, int, Class...)

to match
the requested type arity.

getClassGuard

```java
public static
MethodHandle
getClassGuard​(
Class
<?> clazz)
```

Creates a guard method that tests its only argument for being of an exact particular class.

**Parameters:** clazz

- the class to test for.
**Returns:** the desired guard method.

---

#### getClassGuard

public static

MethodHandle

getClassGuard​(

Class

<?> clazz)

Creates a guard method that tests its only argument for being of an exact particular class.

getInstanceOfGuard

```java
public static
MethodHandle
getInstanceOfGuard​(
Class
<?> clazz)
```

Creates a guard method that tests its only argument for being an instance of a particular class.

**Parameters:** clazz

- the class to test for.
**Returns:** the desired guard method.

---

#### getInstanceOfGuard

public static

MethodHandle

getInstanceOfGuard​(

Class

<?> clazz)

Creates a guard method that tests its only argument for being an instance of a particular class.

getIdentityGuard

```java
public static
MethodHandle
getIdentityGuard​(
Object
obj)
```

Creates a guard method that tests its only argument for being referentially identical to another object

**Parameters:** obj

- the object used as referential identity test
**Returns:** the desired guard method.

---

#### getIdentityGuard

public static

MethodHandle

getIdentityGuard​(

Object

obj)

Creates a guard method that tests its only argument for being referentially identical to another object

isNull

```java
public static
MethodHandle
isNull()
```

Returns a guard that tests whether the first argument is null.

**Returns:** a guard that tests whether the first argument is null.

---

#### isNull

public static

MethodHandle

isNull()

Returns a guard that tests whether the first argument is null.

isNotNull

```java
public static
MethodHandle
isNotNull()
```

Returns a guard that tests whether the first argument is not null.

**Returns:** a guard that tests whether the first argument is not null.

---

#### isNotNull

public static

MethodHandle

isNotNull()

Returns a guard that tests whether the first argument is not null.

---

