# Class Lookup

**Source:** `jdk.dynalink\jdk\dynalink\linker\support\Lookup.html`

### Class Description

```java
public final class
Lookup

extends
Object
```

A wrapper around

MethodHandles.Lookup

that masks
checked exceptions. It is useful in those cases when you're looking up
methods within your own codebase (therefore it is an error if they are not
present).

---

### Field Details

#### public static final
Lookup
PUBLIC

A canonical Lookup object that wraps

MethodHandles.publicLookup()

.

---

### Constructor Details

#### public Lookup​(
MethodHandles.Lookup
lookup)

Creates a new instance, bound to an instance of

MethodHandles.Lookup

.

**Parameters:**
- lookup

- the

MethodHandles.Lookup

it delegates to.

---

### Method Details

#### public
MethodHandle
unreflect​(
Method
m)

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:**
- m

- the method to unreflect

**Returns:**
- the unreflected method handle.

**Throws:**
- IllegalAccessError

- if the method is inaccessible.

---

#### public static
MethodHandle
unreflect​(
MethodHandles.Lookup
lookup,

Method
m)

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:**
- lookup

- the lookup used to unreflect
- m

- the method to unreflect

**Returns:**
- the unreflected method handle.

**Throws:**
- IllegalAccessError

- if the method is inaccessible.

---

#### public
MethodHandle
unreflectGetter​(
Field
f)

Performs a

MethodHandles.Lookup.unreflectGetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:**
- f

- the field for which a getter is unreflected

**Returns:**
- the unreflected field getter handle.

**Throws:**
- IllegalAccessError

- if the getter is inaccessible.

---

#### public
MethodHandle
findGetter​(
Class
<?> refc,

String
name,

Class
<?> type)

Performs a

MethodHandles.Lookup.findGetter(Class, String, Class)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchFieldException

into a

NoSuchFieldError

.

**Parameters:**
- refc

- the class declaring the field
- name

- the name of the field
- type

- the type of the field

**Returns:**
- the unreflected field getter handle.

**Throws:**
- IllegalAccessError

- if the field is inaccessible.
- NoSuchFieldError

- if the field does not exist.

---

#### public
MethodHandle
unreflectSetter​(
Field
f)

Performs a

MethodHandles.Lookup.unreflectSetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:**
- f

- the field for which a setter is unreflected

**Returns:**
- the unreflected field setter handle.

**Throws:**
- IllegalAccessError

- if the field is inaccessible.
- NoSuchFieldError

- if the field does not exist.

---

#### public
MethodHandle
unreflectConstructor​(
Constructor
<?> c)

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:**
- c

- the constructor to unreflect

**Returns:**
- the unreflected constructor handle.

**Throws:**
- IllegalAccessError

- if the constructor is inaccessible.

---

#### public static
MethodHandle
unreflectConstructor​(
MethodHandles.Lookup
lookup,

Constructor
<?> c)

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:**
- lookup

- the lookup used to unreflect
- c

- the constructor to unreflect

**Returns:**
- the unreflected constructor handle.

**Throws:**
- IllegalAccessError

- if the constructor is inaccessible.

---

#### public
MethodHandle
findSpecial​(
Class
<?> declaringClass,

String
name,

MethodType
type)

Performs a

MethodHandles.Lookup.findSpecial(Class, String, MethodType, Class)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:**
- declaringClass

- class declaring the method
- name

- the name of the method
- type

- the type of the method

**Returns:**
- a method handle for the method

**Throws:**
- IllegalAccessError

- if the method is inaccessible.
- NoSuchMethodError

- if the method does not exist.

---

#### public
MethodHandle
findStatic​(
Class
<?> declaringClass,

String
name,

MethodType
type)

Performs a

MethodHandles.Lookup.findStatic(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:**
- declaringClass

- class declaring the method
- name

- the name of the method
- type

- the type of the method

**Returns:**
- a method handle for the method

**Throws:**
- IllegalAccessError

- if the method is inaccessible.
- NoSuchMethodError

- if the method does not exist.

---

#### public
MethodHandle
findVirtual​(
Class
<?> declaringClass,

String
name,

MethodType
type)

Performs a

MethodHandles.Lookup.findVirtual(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:**
- declaringClass

- class declaring the method
- name

- the name of the method
- type

- the type of the method

**Returns:**
- a method handle for the method

**Throws:**
- IllegalAccessError

- if the method is inaccessible.
- NoSuchMethodError

- if the method does not exist.

---

#### public static
MethodHandle
findOwnSpecial​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> rtype,

Class
<?>... ptypes)

Given a lookup, finds using

findSpecial(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates.

**Parameters:**
- lookup

- the lookup for the class
- name

- the name of the method
- rtype

- the return type of the method
- ptypes

- the parameter types of the method

**Returns:**
- the method handle for the method

---

#### public
MethodHandle
findOwnSpecial​(
String
name,

Class
<?> rtype,

Class
<?>... ptypes)

Finds using

findSpecial(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's also more convenient than

findSpecial

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:**
- name

- the name of the method
- rtype

- the return type of the method
- ptypes

- the parameter types of the method

**Returns:**
- the method handle for the method

---

#### public static
MethodHandle
findOwnStatic​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> rtype,

Class
<?>... ptypes)

Given a lookup, finds using

findStatic(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:**
- lookup

- the lookup for the class
- name

- the name of the method
- rtype

- the return type of the method
- ptypes

- the parameter types of the method

**Returns:**
- the method handle for the method

---

#### public
MethodHandle
findOwnStatic​(
String
name,

Class
<?> rtype,

Class
<?>... ptypes)

Finds using

findStatic(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:**
- name

- the name of the method
- rtype

- the return type of the method
- ptypes

- the parameter types of the method

**Returns:**
- the method handle for the method

---

### Additional Sections

#### Class Lookup

java.lang.Object

- jdk.dynalink.linker.support.Lookup

jdk.dynalink.linker.support.Lookup

```java
public final class
Lookup

extends
Object
```

A wrapper around

MethodHandles.Lookup

that masks
checked exceptions. It is useful in those cases when you're looking up
methods within your own codebase (therefore it is an error if they are not
present).

public final class

Lookup

extends

Object

A wrapper around

MethodHandles.Lookup

that masks
checked exceptions. It is useful in those cases when you're looking up
methods within your own codebase (therefore it is an error if they are not
present).

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Lookup

PUBLIC

A canonical Lookup object that wraps

MethodHandles.publicLookup()

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Lookup

​(

MethodHandles.Lookup

lookup)

Creates a new instance, bound to an instance of

MethodHandles.Lookup

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MethodHandle

findGetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Performs a

MethodHandles.Lookup.findGetter(Class, String, Class)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchFieldException

into a

NoSuchFieldError

.

static

MethodHandle

findOwnSpecial

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Given a lookup, finds using

findSpecial(Class, String, MethodType)

a method on that lookup's class.

MethodHandle

findOwnSpecial

​(

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Finds using

findSpecial(Class, String, MethodType)

a method on
that lookup's class.

static

MethodHandle

findOwnStatic

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Given a lookup, finds using

findStatic(Class, String, MethodType)

a method on that lookup's class.

MethodHandle

findOwnStatic

​(

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Finds using

findStatic(Class, String, MethodType)

a method on
that lookup's class.

MethodHandle

findSpecial

​(

Class

<?> declaringClass,

String

name,

MethodType

type)

Performs a

MethodHandles.Lookup.findSpecial(Class, String, MethodType, Class)

on the underlying lookup.

MethodHandle

findStatic

​(

Class

<?> declaringClass,

String

name,

MethodType

type)

Performs a

MethodHandles.Lookup.findStatic(Class, String, MethodType)

on the underlying lookup.

MethodHandle

findVirtual

​(

Class

<?> declaringClass,

String

name,

MethodType

type)

Performs a

MethodHandles.Lookup.findVirtual(Class, String, MethodType)

on the underlying lookup.

static

MethodHandle

unreflect

​(

MethodHandles.Lookup

lookup,

Method

m)

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

MethodHandle

unreflect

​(

Method

m)

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

static

MethodHandle

unreflectConstructor

​(

MethodHandles.Lookup

lookup,

Constructor

<?> c)

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

MethodHandle

unreflectConstructor

​(

Constructor

<?> c)

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

MethodHandle

unreflectGetter

​(

Field

f)

Performs a

MethodHandles.Lookup.unreflectGetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

MethodHandle

unreflectSetter

​(

Field

f)

Performs a

MethodHandles.Lookup.unreflectSetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

Lookup

PUBLIC

A canonical Lookup object that wraps

MethodHandles.publicLookup()

.

---

#### Field Summary

A canonical Lookup object that wraps

MethodHandles.publicLookup()

.

Constructor Summary

Constructors

Constructor

Description

Lookup

​(

MethodHandles.Lookup

lookup)

Creates a new instance, bound to an instance of

MethodHandles.Lookup

.

---

#### Constructor Summary

Creates a new instance, bound to an instance of

MethodHandles.Lookup

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MethodHandle

findGetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Performs a

MethodHandles.Lookup.findGetter(Class, String, Class)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchFieldException

into a

NoSuchFieldError

.

static

MethodHandle

findOwnSpecial

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Given a lookup, finds using

findSpecial(Class, String, MethodType)

a method on that lookup's class.

MethodHandle

findOwnSpecial

​(

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Finds using

findSpecial(Class, String, MethodType)

a method on
that lookup's class.

static

MethodHandle

findOwnStatic

​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Given a lookup, finds using

findStatic(Class, String, MethodType)

a method on that lookup's class.

MethodHandle

findOwnStatic

​(

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Finds using

findStatic(Class, String, MethodType)

a method on
that lookup's class.

MethodHandle

findSpecial

​(

Class

<?> declaringClass,

String

name,

MethodType

type)

Performs a

MethodHandles.Lookup.findSpecial(Class, String, MethodType, Class)

on the underlying lookup.

MethodHandle

findStatic

​(

Class

<?> declaringClass,

String

name,

MethodType

type)

Performs a

MethodHandles.Lookup.findStatic(Class, String, MethodType)

on the underlying lookup.

MethodHandle

findVirtual

​(

Class

<?> declaringClass,

String

name,

MethodType

type)

Performs a

MethodHandles.Lookup.findVirtual(Class, String, MethodType)

on the underlying lookup.

static

MethodHandle

unreflect

​(

MethodHandles.Lookup

lookup,

Method

m)

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

MethodHandle

unreflect

​(

Method

m)

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

static

MethodHandle

unreflectConstructor

​(

MethodHandles.Lookup

lookup,

Constructor

<?> c)

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

MethodHandle

unreflectConstructor

​(

Constructor

<?> c)

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

MethodHandle

unreflectGetter

​(

Field

f)

Performs a

MethodHandles.Lookup.unreflectGetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

MethodHandle

unreflectSetter

​(

Field

f)

Performs a

MethodHandles.Lookup.unreflectSetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

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

Performs a

MethodHandles.Lookup.findGetter(Class, String, Class)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchFieldException

into a

NoSuchFieldError

.

Given a lookup, finds using

findSpecial(Class, String, MethodType)

a method on that lookup's class.

Finds using

findSpecial(Class, String, MethodType)

a method on
that lookup's class.

Given a lookup, finds using

findStatic(Class, String, MethodType)

a method on that lookup's class.

Finds using

findStatic(Class, String, MethodType)

a method on
that lookup's class.

Performs a

MethodHandles.Lookup.findSpecial(Class, String, MethodType, Class)

on the underlying lookup.

Performs a

MethodHandles.Lookup.findStatic(Class, String, MethodType)

on the underlying lookup.

Performs a

MethodHandles.Lookup.findVirtual(Class, String, MethodType)

on the underlying lookup.

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

Performs a

MethodHandles.Lookup.unreflectGetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

Performs a

MethodHandles.Lookup.unreflectSetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

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

============ FIELD DETAIL ===========

- Field Detail

- PUBLIC

```java
public static final
Lookup
PUBLIC
```

A canonical Lookup object that wraps

MethodHandles.publicLookup()

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Lookup

```java
public Lookup​(
MethodHandles.Lookup
lookup)
```

Creates a new instance, bound to an instance of

MethodHandles.Lookup

.

**Parameters:** lookup

- the

MethodHandles.Lookup

it delegates to.

============ METHOD DETAIL ==========

- Method Detail

- unreflect

```java
public
MethodHandle
unreflect​(
Method
m)
```

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** m

- the method to unreflect
**Returns:** the unreflected method handle.
**Throws:** IllegalAccessError

- if the method is inaccessible.

- unreflect

```java
public static
MethodHandle
unreflect​(
MethodHandles.Lookup
lookup,

Method
m)
```

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** lookup

- the lookup used to unreflect
**Parameters:** m

- the method to unreflect
**Returns:** the unreflected method handle.
**Throws:** IllegalAccessError

- if the method is inaccessible.

- unreflectGetter

```java
public
MethodHandle
unreflectGetter​(
Field
f)
```

Performs a

MethodHandles.Lookup.unreflectGetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** f

- the field for which a getter is unreflected
**Returns:** the unreflected field getter handle.
**Throws:** IllegalAccessError

- if the getter is inaccessible.

- findGetter

```java
public
MethodHandle
findGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
```

Performs a

MethodHandles.Lookup.findGetter(Class, String, Class)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchFieldException

into a

NoSuchFieldError

.

**Parameters:** refc

- the class declaring the field
**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Returns:** the unreflected field getter handle.
**Throws:** IllegalAccessError

- if the field is inaccessible.
**Throws:** NoSuchFieldError

- if the field does not exist.

- unreflectSetter

```java
public
MethodHandle
unreflectSetter​(
Field
f)
```

Performs a

MethodHandles.Lookup.unreflectSetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** f

- the field for which a setter is unreflected
**Returns:** the unreflected field setter handle.
**Throws:** IllegalAccessError

- if the field is inaccessible.
**Throws:** NoSuchFieldError

- if the field does not exist.

- unreflectConstructor

```java
public
MethodHandle
unreflectConstructor​(
Constructor
<?> c)
```

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** c

- the constructor to unreflect
**Returns:** the unreflected constructor handle.
**Throws:** IllegalAccessError

- if the constructor is inaccessible.

- unreflectConstructor

```java
public static
MethodHandle
unreflectConstructor​(
MethodHandles.Lookup
lookup,

Constructor
<?> c)
```

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** lookup

- the lookup used to unreflect
**Parameters:** c

- the constructor to unreflect
**Returns:** the unreflected constructor handle.
**Throws:** IllegalAccessError

- if the constructor is inaccessible.

- findSpecial

```java
public
MethodHandle
findSpecial​(
Class
<?> declaringClass,

String
name,

MethodType
type)
```

Performs a

MethodHandles.Lookup.findSpecial(Class, String, MethodType, Class)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:** declaringClass

- class declaring the method
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** a method handle for the method
**Throws:** IllegalAccessError

- if the method is inaccessible.
**Throws:** NoSuchMethodError

- if the method does not exist.

- findStatic

```java
public
MethodHandle
findStatic​(
Class
<?> declaringClass,

String
name,

MethodType
type)
```

Performs a

MethodHandles.Lookup.findStatic(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:** declaringClass

- class declaring the method
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** a method handle for the method
**Throws:** IllegalAccessError

- if the method is inaccessible.
**Throws:** NoSuchMethodError

- if the method does not exist.

- findVirtual

```java
public
MethodHandle
findVirtual​(
Class
<?> declaringClass,

String
name,

MethodType
type)
```

Performs a

MethodHandles.Lookup.findVirtual(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:** declaringClass

- class declaring the method
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** a method handle for the method
**Throws:** IllegalAccessError

- if the method is inaccessible.
**Throws:** NoSuchMethodError

- if the method does not exist.

- findOwnSpecial

```java
public static
MethodHandle
findOwnSpecial​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Given a lookup, finds using

findSpecial(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates.

**Parameters:** lookup

- the lookup for the class
**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

- findOwnSpecial

```java
public
MethodHandle
findOwnSpecial​(
String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Finds using

findSpecial(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's also more convenient than

findSpecial

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

- findOwnStatic

```java
public static
MethodHandle
findOwnStatic​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Given a lookup, finds using

findStatic(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:** lookup

- the lookup for the class
**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

- findOwnStatic

```java
public
MethodHandle
findOwnStatic​(
String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Finds using

findStatic(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

Field Detail

- PUBLIC

```java
public static final
Lookup
PUBLIC
```

A canonical Lookup object that wraps

MethodHandles.publicLookup()

.

---

#### Field Detail

PUBLIC

```java
public static final
Lookup
PUBLIC
```

A canonical Lookup object that wraps

MethodHandles.publicLookup()

.

---

#### PUBLIC

public static final

Lookup

PUBLIC

A canonical Lookup object that wraps

MethodHandles.publicLookup()

.

Constructor Detail

- Lookup

```java
public Lookup​(
MethodHandles.Lookup
lookup)
```

Creates a new instance, bound to an instance of

MethodHandles.Lookup

.

**Parameters:** lookup

- the

MethodHandles.Lookup

it delegates to.

---

#### Constructor Detail

Lookup

```java
public Lookup​(
MethodHandles.Lookup
lookup)
```

Creates a new instance, bound to an instance of

MethodHandles.Lookup

.

**Parameters:** lookup

- the

MethodHandles.Lookup

it delegates to.

---

#### Lookup

public Lookup​(

MethodHandles.Lookup

lookup)

Creates a new instance, bound to an instance of

MethodHandles.Lookup

.

Method Detail

- unreflect

```java
public
MethodHandle
unreflect​(
Method
m)
```

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** m

- the method to unreflect
**Returns:** the unreflected method handle.
**Throws:** IllegalAccessError

- if the method is inaccessible.

- unreflect

```java
public static
MethodHandle
unreflect​(
MethodHandles.Lookup
lookup,

Method
m)
```

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** lookup

- the lookup used to unreflect
**Parameters:** m

- the method to unreflect
**Returns:** the unreflected method handle.
**Throws:** IllegalAccessError

- if the method is inaccessible.

- unreflectGetter

```java
public
MethodHandle
unreflectGetter​(
Field
f)
```

Performs a

MethodHandles.Lookup.unreflectGetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** f

- the field for which a getter is unreflected
**Returns:** the unreflected field getter handle.
**Throws:** IllegalAccessError

- if the getter is inaccessible.

- findGetter

```java
public
MethodHandle
findGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
```

Performs a

MethodHandles.Lookup.findGetter(Class, String, Class)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchFieldException

into a

NoSuchFieldError

.

**Parameters:** refc

- the class declaring the field
**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Returns:** the unreflected field getter handle.
**Throws:** IllegalAccessError

- if the field is inaccessible.
**Throws:** NoSuchFieldError

- if the field does not exist.

- unreflectSetter

```java
public
MethodHandle
unreflectSetter​(
Field
f)
```

Performs a

MethodHandles.Lookup.unreflectSetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** f

- the field for which a setter is unreflected
**Returns:** the unreflected field setter handle.
**Throws:** IllegalAccessError

- if the field is inaccessible.
**Throws:** NoSuchFieldError

- if the field does not exist.

- unreflectConstructor

```java
public
MethodHandle
unreflectConstructor​(
Constructor
<?> c)
```

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** c

- the constructor to unreflect
**Returns:** the unreflected constructor handle.
**Throws:** IllegalAccessError

- if the constructor is inaccessible.

- unreflectConstructor

```java
public static
MethodHandle
unreflectConstructor​(
MethodHandles.Lookup
lookup,

Constructor
<?> c)
```

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** lookup

- the lookup used to unreflect
**Parameters:** c

- the constructor to unreflect
**Returns:** the unreflected constructor handle.
**Throws:** IllegalAccessError

- if the constructor is inaccessible.

- findSpecial

```java
public
MethodHandle
findSpecial​(
Class
<?> declaringClass,

String
name,

MethodType
type)
```

Performs a

MethodHandles.Lookup.findSpecial(Class, String, MethodType, Class)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:** declaringClass

- class declaring the method
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** a method handle for the method
**Throws:** IllegalAccessError

- if the method is inaccessible.
**Throws:** NoSuchMethodError

- if the method does not exist.

- findStatic

```java
public
MethodHandle
findStatic​(
Class
<?> declaringClass,

String
name,

MethodType
type)
```

Performs a

MethodHandles.Lookup.findStatic(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:** declaringClass

- class declaring the method
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** a method handle for the method
**Throws:** IllegalAccessError

- if the method is inaccessible.
**Throws:** NoSuchMethodError

- if the method does not exist.

- findVirtual

```java
public
MethodHandle
findVirtual​(
Class
<?> declaringClass,

String
name,

MethodType
type)
```

Performs a

MethodHandles.Lookup.findVirtual(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:** declaringClass

- class declaring the method
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** a method handle for the method
**Throws:** IllegalAccessError

- if the method is inaccessible.
**Throws:** NoSuchMethodError

- if the method does not exist.

- findOwnSpecial

```java
public static
MethodHandle
findOwnSpecial​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Given a lookup, finds using

findSpecial(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates.

**Parameters:** lookup

- the lookup for the class
**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

- findOwnSpecial

```java
public
MethodHandle
findOwnSpecial​(
String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Finds using

findSpecial(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's also more convenient than

findSpecial

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

- findOwnStatic

```java
public static
MethodHandle
findOwnStatic​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Given a lookup, finds using

findStatic(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:** lookup

- the lookup for the class
**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

- findOwnStatic

```java
public
MethodHandle
findOwnStatic​(
String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Finds using

findStatic(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

---

#### Method Detail

unreflect

```java
public
MethodHandle
unreflect​(
Method
m)
```

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** m

- the method to unreflect
**Returns:** the unreflected method handle.
**Throws:** IllegalAccessError

- if the method is inaccessible.

---

#### unreflect

public

MethodHandle

unreflect​(

Method

m)

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

unreflect

```java
public static
MethodHandle
unreflect​(
MethodHandles.Lookup
lookup,

Method
m)
```

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** lookup

- the lookup used to unreflect
**Parameters:** m

- the method to unreflect
**Returns:** the unreflected method handle.
**Throws:** IllegalAccessError

- if the method is inaccessible.

---

#### unreflect

public static

MethodHandle

unreflect​(

MethodHandles.Lookup

lookup,

Method

m)

Performs a

MethodHandles.Lookup.unreflect(Method)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

unreflectGetter

```java
public
MethodHandle
unreflectGetter​(
Field
f)
```

Performs a

MethodHandles.Lookup.unreflectGetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** f

- the field for which a getter is unreflected
**Returns:** the unreflected field getter handle.
**Throws:** IllegalAccessError

- if the getter is inaccessible.

---

#### unreflectGetter

public

MethodHandle

unreflectGetter​(

Field

f)

Performs a

MethodHandles.Lookup.unreflectGetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

findGetter

```java
public
MethodHandle
findGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
```

Performs a

MethodHandles.Lookup.findGetter(Class, String, Class)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchFieldException

into a

NoSuchFieldError

.

**Parameters:** refc

- the class declaring the field
**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Returns:** the unreflected field getter handle.
**Throws:** IllegalAccessError

- if the field is inaccessible.
**Throws:** NoSuchFieldError

- if the field does not exist.

---

#### findGetter

public

MethodHandle

findGetter​(

Class

<?> refc,

String

name,

Class

<?> type)

Performs a

MethodHandles.Lookup.findGetter(Class, String, Class)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchFieldException

into a

NoSuchFieldError

.

unreflectSetter

```java
public
MethodHandle
unreflectSetter​(
Field
f)
```

Performs a

MethodHandles.Lookup.unreflectSetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** f

- the field for which a setter is unreflected
**Returns:** the unreflected field setter handle.
**Throws:** IllegalAccessError

- if the field is inaccessible.
**Throws:** NoSuchFieldError

- if the field does not exist.

---

#### unreflectSetter

public

MethodHandle

unreflectSetter​(

Field

f)

Performs a

MethodHandles.Lookup.unreflectSetter(Field)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

unreflectConstructor

```java
public
MethodHandle
unreflectConstructor​(
Constructor
<?> c)
```

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** c

- the constructor to unreflect
**Returns:** the unreflected constructor handle.
**Throws:** IllegalAccessError

- if the constructor is inaccessible.

---

#### unreflectConstructor

public

MethodHandle

unreflectConstructor​(

Constructor

<?> c)

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

unreflectConstructor

```java
public static
MethodHandle
unreflectConstructor​(
MethodHandles.Lookup
lookup,

Constructor
<?> c)
```

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

**Parameters:** lookup

- the lookup used to unreflect
**Parameters:** c

- the constructor to unreflect
**Returns:** the unreflected constructor handle.
**Throws:** IllegalAccessError

- if the constructor is inaccessible.

---

#### unreflectConstructor

public static

MethodHandle

unreflectConstructor​(

MethodHandles.Lookup

lookup,

Constructor

<?> c)

Performs a

MethodHandles.Lookup.unreflectConstructor(Constructor)

,
converting any encountered

IllegalAccessException

into an

IllegalAccessError

.

findSpecial

```java
public
MethodHandle
findSpecial​(
Class
<?> declaringClass,

String
name,

MethodType
type)
```

Performs a

MethodHandles.Lookup.findSpecial(Class, String, MethodType, Class)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:** declaringClass

- class declaring the method
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** a method handle for the method
**Throws:** IllegalAccessError

- if the method is inaccessible.
**Throws:** NoSuchMethodError

- if the method does not exist.

---

#### findSpecial

public

MethodHandle

findSpecial​(

Class

<?> declaringClass,

String

name,

MethodType

type)

Performs a

MethodHandles.Lookup.findSpecial(Class, String, MethodType, Class)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

findStatic

```java
public
MethodHandle
findStatic​(
Class
<?> declaringClass,

String
name,

MethodType
type)
```

Performs a

MethodHandles.Lookup.findStatic(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:** declaringClass

- class declaring the method
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** a method handle for the method
**Throws:** IllegalAccessError

- if the method is inaccessible.
**Throws:** NoSuchMethodError

- if the method does not exist.

---

#### findStatic

public

MethodHandle

findStatic​(

Class

<?> declaringClass,

String

name,

MethodType

type)

Performs a

MethodHandles.Lookup.findStatic(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

findVirtual

```java
public
MethodHandle
findVirtual​(
Class
<?> declaringClass,

String
name,

MethodType
type)
```

Performs a

MethodHandles.Lookup.findVirtual(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

**Parameters:** declaringClass

- class declaring the method
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** a method handle for the method
**Throws:** IllegalAccessError

- if the method is inaccessible.
**Throws:** NoSuchMethodError

- if the method does not exist.

---

#### findVirtual

public

MethodHandle

findVirtual​(

Class

<?> declaringClass,

String

name,

MethodType

type)

Performs a

MethodHandles.Lookup.findVirtual(Class, String, MethodType)

on the underlying lookup. Converts any encountered

IllegalAccessException

into an

IllegalAccessError

and

NoSuchMethodException

into a

NoSuchMethodError

.

findOwnSpecial

```java
public static
MethodHandle
findOwnSpecial​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Given a lookup, finds using

findSpecial(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates.

**Parameters:** lookup

- the lookup for the class
**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

---

#### findOwnSpecial

public static

MethodHandle

findOwnSpecial​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Given a lookup, finds using

findSpecial(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates.

findOwnSpecial

```java
public
MethodHandle
findOwnSpecial​(
String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Finds using

findSpecial(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's also more convenient than

findSpecial

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

---

#### findOwnSpecial

public

MethodHandle

findOwnSpecial​(

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Finds using

findSpecial(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's also more convenient than

findSpecial

in that you can just list the parameter types, and don't have to specify
lookup class.

findOwnStatic

```java
public static
MethodHandle
findOwnStatic​(
MethodHandles.Lookup
lookup,

String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Given a lookup, finds using

findStatic(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:** lookup

- the lookup for the class
**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

---

#### findOwnStatic

public static

MethodHandle

findOwnStatic​(

MethodHandles.Lookup

lookup,

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Given a lookup, finds using

findStatic(Class, String, MethodType)

a method on that lookup's class. Useful in classes' code for convenient
linking to their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

findOwnStatic

```java
public
MethodHandle
findOwnStatic​(
String
name,

Class
<?> rtype,

Class
<?>... ptypes)
```

Finds using

findStatic(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

**Parameters:** name

- the name of the method
**Parameters:** rtype

- the return type of the method
**Parameters:** ptypes

- the parameter types of the method
**Returns:** the method handle for the method

---

#### findOwnStatic

public

MethodHandle

findOwnStatic​(

String

name,

Class

<?> rtype,

Class

<?>... ptypes)

Finds using

findStatic(Class, String, MethodType)

a method on
that lookup's class. Useful in classes' code for convenient linking to
their own privates. It's easier to use than

findStatic

in that you can just list the parameter types, and don't have to specify
lookup class.

---

