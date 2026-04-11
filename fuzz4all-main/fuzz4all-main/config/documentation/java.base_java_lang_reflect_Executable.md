# Class Executable

**Source:** `java.base\java\lang\reflect\Executable.html`

### Class Description

```java
public abstract class
Executable

extends
AccessibleObject

implements
Member
,
GenericDeclaration
```

A shared superclass for the common functionality of

Method

and

Constructor

.

**All Implemented Interfaces:** AnnotatedElement

,

GenericDeclaration

,

Member

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public abstract
Class
<?> getDeclaringClass()

Returns the

Class

object representing the class or interface
that declares the executable represented by this object.

**Specified by:**
- getDeclaringClass

in interface

Member

**Returns:**
- an object representing the declaring class of the
underlying member

---

#### public abstract
String
getName()

Returns the name of the executable represented by this object.

**Specified by:**
- getName

in interface

Member

**Returns:**
- the simple name of the underlying member

---

#### public abstract int getModifiers()

Returns the Java language

modifiers

for
the executable represented by this object.

**Specified by:**
- getModifiers

in interface

Member

**Returns:**
- the Java language modifiers for the underlying member

**See Also:**
- Modifier

---

#### public abstract
TypeVariable
<?>[] getTypeParameters()

Returns an array of

TypeVariable

objects that represent the
type variables declared by the generic declaration represented by this

GenericDeclaration

object, in declaration order. Returns an
array of length 0 if the underlying generic declaration declares no type
variables.

**Specified by:**
- getTypeParameters

in interface

GenericDeclaration

**Returns:**
- an array of

TypeVariable

objects that represent
the type variables declared by this generic declaration

**Throws:**
- GenericSignatureFormatError

- if the generic
signature of this generic declaration does not conform to
the format specified in

The Java™ Virtual Machine Specification

---

#### public abstract
Class
<?>[] getParameterTypes()

Returns an array of

Class

objects that represent the formal
parameter types, in declaration order, of the executable
represented by this object. Returns an array of length
0 if the underlying executable takes no parameters.

**Returns:**
- the parameter types for the executable this object
represents

---

#### public int getParameterCount()

Returns the number of formal parameters (whether explicitly
declared or implicitly declared or neither) for the executable
represented by this object.

**Returns:**
- The number of formal parameters for the executable this
object represents

---

#### public
Type
[] getGenericParameterTypes()

Returns an array of

Type

objects that represent the formal
parameter types, in declaration order, of the executable represented by
this object. Returns an array of length 0 if the
underlying executable takes no parameters.

If a formal parameter type is a parameterized type,
the

Type

object returned for it must accurately reflect
the actual type parameters used in the source code.

If a formal parameter type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

**Returns:**
- an array of

Type

s that represent the formal
parameter types of the underlying executable, in declaration order

**Throws:**
- GenericSignatureFormatError

- if the generic method signature does not conform to the format
specified in

The Java™ Virtual Machine Specification
- TypeNotPresentException

- if any of the parameter
types of the underlying executable refers to a non-existent type
declaration
- MalformedParameterizedTypeException

- if any of
the underlying executable's parameter types refer to a parameterized
type that cannot be instantiated for any reason

---

#### public
Parameter
[] getParameters()

Returns an array of

Parameter

objects that represent
all the parameters to the underlying executable represented by
this object. Returns an array of length 0 if the executable
has no parameters.

The parameters of the underlying executable do not necessarily
have unique names, or names that are legal identifiers in the
Java programming language (JLS 3.8).

**Returns:**
- an array of

Parameter

objects representing all
the parameters to the executable this object represents.

**Throws:**
- MalformedParametersException

- if the class file contains
a MethodParameters attribute that is improperly formatted.

---

#### public abstract
Class
<?>[] getExceptionTypes()

Returns an array of

Class

objects that represent the
types of exceptions declared to be thrown by the underlying
executable represented by this object. Returns an array of
length 0 if the executable declares no exceptions in its

throws

clause.

**Returns:**
- the exception types declared as being thrown by the
executable this object represents

---

#### public
Type
[] getGenericExceptionTypes()

Returns an array of

Type

objects that represent the
exceptions declared to be thrown by this executable object.
Returns an array of length 0 if the underlying executable declares
no exceptions in its

throws

clause.

If an exception type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

**Returns:**
- an array of Types that represent the exception types
thrown by the underlying executable

**Throws:**
- GenericSignatureFormatError

- if the generic method signature does not conform to the format
specified in

The Java™ Virtual Machine Specification
- TypeNotPresentException

- if the underlying executable's

throws

clause refers to a non-existent type declaration
- MalformedParameterizedTypeException

- if
the underlying executable's

throws

clause refers to a
parameterized type that cannot be instantiated for any reason

---

#### public abstract
String
toGenericString()

Returns a string describing this

Executable

, including
any type parameters.

**Returns:**
- a string describing this

Executable

, including
any type parameters

---

#### public boolean isVarArgs()

Returns

true

if this executable was declared to take a
variable number of arguments; returns

false

otherwise.

**Returns:**
- true

if an only if this executable was declared
to take a variable number of arguments.

---

#### public boolean isSynthetic()

Returns

true

if this executable is a synthetic
construct; returns

false

otherwise.

**Specified by:**
- isSynthetic

in interface

Member

**Returns:**
- true if and only if this executable is a synthetic
construct as defined by

The Java™ Language Specification

.

**See The Java™ Language Specification :**
- 13.1 The Form of a Binary

---

#### public abstract
Annotation
[][] getParameterAnnotations()

Returns an array of arrays of

Annotation

s that
represent the annotations on the formal parameters, in
declaration order, of the

Executable

represented by
this object. Synthetic and mandated parameters (see
explanation below), such as the outer "this" parameter to an
inner class constructor will be represented in the returned
array. If the executable has no parameters (meaning no formal,
no synthetic, and no mandated parameters), a zero-length array
will be returned. If the

Executable

has one or more
parameters, a nested array of length zero is returned for each
parameter with no annotations. The annotation objects contained
in the returned arrays are serializable. The caller of this
method is free to modify the returned arrays; it will have no
effect on the arrays returned to other callers.

A compiler may add extra parameters that are implicitly
declared in source ("mandated"), as well as parameters that
are neither implicitly nor explicitly declared in source
("synthetic") to the parameter list for a method. See

Parameter

for more information.

**Returns:**
- an array of arrays that represent the annotations on
the formal and implicit parameters, in declaration order, of
the executable represented by this object

**See Also:**
- Parameter

,

AnnotatedElement.getAnnotations()

---

#### public <T extends
Annotation
> T getAnnotation​(
Class
<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

**Specified by:**
- getAnnotation

in interface

AnnotatedElement

**Overrides:**
- getAnnotation

in class

AccessibleObject

**Parameters:**
- annotationClass

- the Class object corresponding to the
annotation type

**Returns:**
- this element's annotation for the specified annotation type if
present on this element, else null

**Throws:**
- NullPointerException

- if the given annotation class is null

**Type Parameters:**
- T

- the type of the annotation to query for and return if present

---

#### public <T extends
Annotation
> T[] getAnnotationsByType​(
Class
<T> annotationClass)

Returns annotations that are

associated

with this element.

If there are no annotations

associated

with this element, the return
value is an array of length 0.

The difference between this method and

AnnotatedElement.getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

(JLS 9.6), and if so, attempts to find one or
more annotations of that type by "looking through" a container
annotation.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.

**Specified by:**
- getAnnotationsByType

in interface

AnnotatedElement

**Overrides:**
- getAnnotationsByType

in class

AccessibleObject

**Parameters:**
- annotationClass

- the Class object corresponding to the
annotation type

**Returns:**
- all this element's annotations for the specified annotation type if
associated with this element, else an array of length zero

**Throws:**
- NullPointerException

- if the given annotation class is null

**Type Parameters:**
- T

- the type of the annotation to query for and return if present

---

#### public abstract
AnnotatedType
getAnnotatedReturnType()

Returns an

AnnotatedType

object that represents the use of a type to
specify the return type of the method/constructor represented by this
Executable.

If this

Executable

object represents a constructor, the

AnnotatedType

object represents the type of the constructed object.

If this

Executable

object represents a method, the

AnnotatedType

object represents the use of a type to specify the return
type of the method.

**Returns:**
- an object representing the return type of the method
or constructor represented by this

Executable

---

#### public
AnnotatedType
getAnnotatedReceiverType()

Returns an

AnnotatedType

object that represents the use of a
type to specify the receiver type of the method/constructor represented
by this

Executable

object.

The receiver type of a method/constructor is available only if the
method/constructor has a receiver parameter (JLS 8.4.1). If this

Executable

object

represents an instance method or represents a
constructor of an inner member class

, and the
method/constructor

either

has no receiver parameter or has a
receiver parameter with no annotations on its type, then the return
value is an

AnnotatedType

object representing an element with no
annotations.

If this

Executable

object represents a static method or
represents a constructor of a top level, static member, local, or
anonymous class, then the return value is null.

**Returns:**
- an object representing the receiver type of the method or
constructor represented by this

Executable

or

null

if
this

Executable

can not have a receiver parameter

---

#### public
AnnotatedType
[] getAnnotatedParameterTypes()

Returns an array of

AnnotatedType

objects that represent the use
of types to specify formal parameter types of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the formal parameter types in the
declaration of the method/constructor.

Returns an array of length 0 if the method/constructor declares no
parameters.

**Returns:**
- an array of objects representing the types of the
formal parameters of the method or constructor represented by this

Executable

---

#### public
AnnotatedType
[] getAnnotatedExceptionTypes()

Returns an array of

AnnotatedType

objects that represent the use
of types to specify the declared exceptions of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the exception types in the declaration of
the method/constructor.

Returns an array of length 0 if the method/constructor declares no
exceptions.

**Returns:**
- an array of objects representing the declared
exceptions of the method or constructor represented by this

Executable

---

### Additional Sections

#### Class Executable

java.lang.Object

- java.lang.reflect.AccessibleObject
- - java.lang.reflect.Executable

java.lang.reflect.AccessibleObject

- java.lang.reflect.Executable

java.lang.reflect.Executable

**All Implemented Interfaces:** AnnotatedElement

,

GenericDeclaration

,

Member

**Direct Known Subclasses:** Constructor

,

Method

```java
public abstract class
Executable

extends
AccessibleObject

implements
Member
,
GenericDeclaration
```

A shared superclass for the common functionality of

Method

and

Constructor

.

**Since:** 1.8

public abstract class

Executable

extends

AccessibleObject

implements

Member

,

GenericDeclaration

A shared superclass for the common functionality of

Method

and

Constructor

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.lang.reflect.

Member

DECLARED

,

PUBLIC

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

AnnotatedType

[]

getAnnotatedExceptionTypes

()

Returns an array of

AnnotatedType

objects that represent the use
of types to specify the declared exceptions of the method/constructor
represented by this Executable.

AnnotatedType

[]

getAnnotatedParameterTypes

()

Returns an array of

AnnotatedType

objects that represent the use
of types to specify formal parameter types of the method/constructor
represented by this Executable.

AnnotatedType

getAnnotatedReceiverType

()

Returns an

AnnotatedType

object that represents the use of a
type to specify the receiver type of the method/constructor represented
by this

Executable

object.

abstract

AnnotatedType

getAnnotatedReturnType

()

Returns an

AnnotatedType

object that represents the use of a type to
specify the return type of the method/constructor represented by this
Executable.

<T extends

Annotation

>

T

getAnnotation

​(

Class

<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

<T extends

Annotation

>

T[]

getAnnotationsByType

​(

Class

<T> annotationClass)

Returns annotations that are

associated

with this element.

abstract

Class

<?>

getDeclaringClass

()

Returns the

Class

object representing the class or interface
that declares the executable represented by this object.

abstract

Class

<?>[]

getExceptionTypes

()

Returns an array of

Class

objects that represent the
types of exceptions declared to be thrown by the underlying
executable represented by this object.

Type

[]

getGenericExceptionTypes

()

Returns an array of

Type

objects that represent the
exceptions declared to be thrown by this executable object.

Type

[]

getGenericParameterTypes

()

Returns an array of

Type

objects that represent the formal
parameter types, in declaration order, of the executable represented by
this object.

abstract int

getModifiers

()

Returns the Java language

modifiers

for
the executable represented by this object.

abstract

String

getName

()

Returns the name of the executable represented by this object.

abstract

Annotation

[][]

getParameterAnnotations

()

Returns an array of arrays of

Annotation

s that
represent the annotations on the formal parameters, in
declaration order, of the

Executable

represented by
this object.

int

getParameterCount

()

Returns the number of formal parameters (whether explicitly
declared or implicitly declared or neither) for the executable
represented by this object.

Parameter

[]

getParameters

()

Returns an array of

Parameter

objects that represent
all the parameters to the underlying executable represented by
this object.

abstract

Class

<?>[]

getParameterTypes

()

Returns an array of

Class

objects that represent the formal
parameter types, in declaration order, of the executable
represented by this object.

abstract

TypeVariable

<?>[]

getTypeParameters

()

Returns an array of

TypeVariable

objects that represent the
type variables declared by the generic declaration represented by this

GenericDeclaration

object, in declaration order.

boolean

isSynthetic

()

Returns

true

if this executable is a synthetic
construct; returns

false

otherwise.

boolean

isVarArgs

()

Returns

true

if this executable was declared to take a
variable number of arguments; returns

false

otherwise.

abstract

String

toGenericString

()

Returns a string describing this

Executable

, including
any type parameters.

- Methods declared in class java.lang.reflect.

AccessibleObject

canAccess

,

getAnnotations

,

getDeclaredAnnotation

,

getDeclaredAnnotations

,

getDeclaredAnnotationsByType

,

isAccessible

,

isAnnotationPresent

,

setAccessible

,

setAccessible

,

trySetAccessible

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

- Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotations

,

getDeclaredAnnotation

,

getDeclaredAnnotations

,

getDeclaredAnnotationsByType

,

isAnnotationPresent

Field Summary

- Fields declared in interface java.lang.reflect.

Member

DECLARED

,

PUBLIC

---

#### Field Summary

Fields declared in interface java.lang.reflect.

Member

DECLARED

,

PUBLIC

---

#### Fields declared in interface java.lang.reflect. Member

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

AnnotatedType

[]

getAnnotatedExceptionTypes

()

Returns an array of

AnnotatedType

objects that represent the use
of types to specify the declared exceptions of the method/constructor
represented by this Executable.

AnnotatedType

[]

getAnnotatedParameterTypes

()

Returns an array of

AnnotatedType

objects that represent the use
of types to specify formal parameter types of the method/constructor
represented by this Executable.

AnnotatedType

getAnnotatedReceiverType

()

Returns an

AnnotatedType

object that represents the use of a
type to specify the receiver type of the method/constructor represented
by this

Executable

object.

abstract

AnnotatedType

getAnnotatedReturnType

()

Returns an

AnnotatedType

object that represents the use of a type to
specify the return type of the method/constructor represented by this
Executable.

<T extends

Annotation

>

T

getAnnotation

​(

Class

<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

<T extends

Annotation

>

T[]

getAnnotationsByType

​(

Class

<T> annotationClass)

Returns annotations that are

associated

with this element.

abstract

Class

<?>

getDeclaringClass

()

Returns the

Class

object representing the class or interface
that declares the executable represented by this object.

abstract

Class

<?>[]

getExceptionTypes

()

Returns an array of

Class

objects that represent the
types of exceptions declared to be thrown by the underlying
executable represented by this object.

Type

[]

getGenericExceptionTypes

()

Returns an array of

Type

objects that represent the
exceptions declared to be thrown by this executable object.

Type

[]

getGenericParameterTypes

()

Returns an array of

Type

objects that represent the formal
parameter types, in declaration order, of the executable represented by
this object.

abstract int

getModifiers

()

Returns the Java language

modifiers

for
the executable represented by this object.

abstract

String

getName

()

Returns the name of the executable represented by this object.

abstract

Annotation

[][]

getParameterAnnotations

()

Returns an array of arrays of

Annotation

s that
represent the annotations on the formal parameters, in
declaration order, of the

Executable

represented by
this object.

int

getParameterCount

()

Returns the number of formal parameters (whether explicitly
declared or implicitly declared or neither) for the executable
represented by this object.

Parameter

[]

getParameters

()

Returns an array of

Parameter

objects that represent
all the parameters to the underlying executable represented by
this object.

abstract

Class

<?>[]

getParameterTypes

()

Returns an array of

Class

objects that represent the formal
parameter types, in declaration order, of the executable
represented by this object.

abstract

TypeVariable

<?>[]

getTypeParameters

()

Returns an array of

TypeVariable

objects that represent the
type variables declared by the generic declaration represented by this

GenericDeclaration

object, in declaration order.

boolean

isSynthetic

()

Returns

true

if this executable is a synthetic
construct; returns

false

otherwise.

boolean

isVarArgs

()

Returns

true

if this executable was declared to take a
variable number of arguments; returns

false

otherwise.

abstract

String

toGenericString

()

Returns a string describing this

Executable

, including
any type parameters.

- Methods declared in class java.lang.reflect.

AccessibleObject

canAccess

,

getAnnotations

,

getDeclaredAnnotation

,

getDeclaredAnnotations

,

getDeclaredAnnotationsByType

,

isAccessible

,

isAnnotationPresent

,

setAccessible

,

setAccessible

,

trySetAccessible

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

- Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotations

,

getDeclaredAnnotation

,

getDeclaredAnnotations

,

getDeclaredAnnotationsByType

,

isAnnotationPresent

---

#### Method Summary

Returns an array of

AnnotatedType

objects that represent the use
of types to specify the declared exceptions of the method/constructor
represented by this Executable.

Returns an array of

AnnotatedType

objects that represent the use
of types to specify formal parameter types of the method/constructor
represented by this Executable.

Returns an

AnnotatedType

object that represents the use of a
type to specify the receiver type of the method/constructor represented
by this

Executable

object.

Returns an

AnnotatedType

object that represents the use of a type to
specify the return type of the method/constructor represented by this
Executable.

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

Returns annotations that are

associated

with this element.

Returns the

Class

object representing the class or interface
that declares the executable represented by this object.

Returns an array of

Class

objects that represent the
types of exceptions declared to be thrown by the underlying
executable represented by this object.

Returns an array of

Type

objects that represent the
exceptions declared to be thrown by this executable object.

Returns an array of

Type

objects that represent the formal
parameter types, in declaration order, of the executable represented by
this object.

Returns the Java language

modifiers

for
the executable represented by this object.

Returns the name of the executable represented by this object.

Returns an array of arrays of

Annotation

s that
represent the annotations on the formal parameters, in
declaration order, of the

Executable

represented by
this object.

Returns the number of formal parameters (whether explicitly
declared or implicitly declared or neither) for the executable
represented by this object.

Returns an array of

Parameter

objects that represent
all the parameters to the underlying executable represented by
this object.

Returns an array of

Class

objects that represent the formal
parameter types, in declaration order, of the executable
represented by this object.

Returns an array of

TypeVariable

objects that represent the
type variables declared by the generic declaration represented by this

GenericDeclaration

object, in declaration order.

Returns

true

if this executable is a synthetic
construct; returns

false

otherwise.

Returns

true

if this executable was declared to take a
variable number of arguments; returns

false

otherwise.

Returns a string describing this

Executable

, including
any type parameters.

Methods declared in class java.lang.reflect.

AccessibleObject

canAccess

,

getAnnotations

,

getDeclaredAnnotation

,

getDeclaredAnnotations

,

getDeclaredAnnotationsByType

,

isAccessible

,

isAnnotationPresent

,

setAccessible

,

setAccessible

,

trySetAccessible

---

#### Methods declared in class java.lang.reflect. AccessibleObject

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

Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotations

,

getDeclaredAnnotation

,

getDeclaredAnnotations

,

getDeclaredAnnotationsByType

,

isAnnotationPresent

---

#### Methods declared in interface java.lang.reflect. AnnotatedElement

============ METHOD DETAIL ==========

- Method Detail

- getDeclaringClass

```java
public abstract
Class
<?> getDeclaringClass()
```

Returns the

Class

object representing the class or interface
that declares the executable represented by this object.

**Specified by:** getDeclaringClass

in interface

Member
**Returns:** an object representing the declaring class of the
underlying member

- getName

```java
public abstract
String
getName()
```

Returns the name of the executable represented by this object.

**Specified by:** getName

in interface

Member
**Returns:** the simple name of the underlying member

- getModifiers

```java
public abstract int getModifiers()
```

Returns the Java language

modifiers

for
the executable represented by this object.

**Specified by:** getModifiers

in interface

Member
**Returns:** the Java language modifiers for the underlying member
**See Also:** Modifier

- getTypeParameters

```java
public abstract
TypeVariable
<?>[] getTypeParameters()
```

Returns an array of

TypeVariable

objects that represent the
type variables declared by the generic declaration represented by this

GenericDeclaration

object, in declaration order. Returns an
array of length 0 if the underlying generic declaration declares no type
variables.

**Specified by:** getTypeParameters

in interface

GenericDeclaration
**Returns:** an array of

TypeVariable

objects that represent
the type variables declared by this generic declaration
**Throws:** GenericSignatureFormatError

- if the generic
signature of this generic declaration does not conform to
the format specified in

The Java™ Virtual Machine Specification

- getParameterTypes

```java
public abstract
Class
<?>[] getParameterTypes()
```

Returns an array of

Class

objects that represent the formal
parameter types, in declaration order, of the executable
represented by this object. Returns an array of length
0 if the underlying executable takes no parameters.

**Returns:** the parameter types for the executable this object
represents

- getParameterCount

```java
public int getParameterCount()
```

Returns the number of formal parameters (whether explicitly
declared or implicitly declared or neither) for the executable
represented by this object.

**Returns:** The number of formal parameters for the executable this
object represents

- getGenericParameterTypes

```java
public
Type
[] getGenericParameterTypes()
```

Returns an array of

Type

objects that represent the formal
parameter types, in declaration order, of the executable represented by
this object. Returns an array of length 0 if the
underlying executable takes no parameters.

If a formal parameter type is a parameterized type,
the

Type

object returned for it must accurately reflect
the actual type parameters used in the source code.

If a formal parameter type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

**Returns:** an array of

Type

s that represent the formal
parameter types of the underlying executable, in declaration order
**Throws:** GenericSignatureFormatError

- if the generic method signature does not conform to the format
specified in

The Java™ Virtual Machine Specification
**Throws:** TypeNotPresentException

- if any of the parameter
types of the underlying executable refers to a non-existent type
declaration
**Throws:** MalformedParameterizedTypeException

- if any of
the underlying executable's parameter types refer to a parameterized
type that cannot be instantiated for any reason

- getParameters

```java
public
Parameter
[] getParameters()
```

Returns an array of

Parameter

objects that represent
all the parameters to the underlying executable represented by
this object. Returns an array of length 0 if the executable
has no parameters.

The parameters of the underlying executable do not necessarily
have unique names, or names that are legal identifiers in the
Java programming language (JLS 3.8).

**Returns:** an array of

Parameter

objects representing all
the parameters to the executable this object represents.
**Throws:** MalformedParametersException

- if the class file contains
a MethodParameters attribute that is improperly formatted.

- getExceptionTypes

```java
public abstract
Class
<?>[] getExceptionTypes()
```

Returns an array of

Class

objects that represent the
types of exceptions declared to be thrown by the underlying
executable represented by this object. Returns an array of
length 0 if the executable declares no exceptions in its

throws

clause.

**Returns:** the exception types declared as being thrown by the
executable this object represents

- getGenericExceptionTypes

```java
public
Type
[] getGenericExceptionTypes()
```

Returns an array of

Type

objects that represent the
exceptions declared to be thrown by this executable object.
Returns an array of length 0 if the underlying executable declares
no exceptions in its

throws

clause.

If an exception type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

**Returns:** an array of Types that represent the exception types
thrown by the underlying executable
**Throws:** GenericSignatureFormatError

- if the generic method signature does not conform to the format
specified in

The Java™ Virtual Machine Specification
**Throws:** TypeNotPresentException

- if the underlying executable's

throws

clause refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if
the underlying executable's

throws

clause refers to a
parameterized type that cannot be instantiated for any reason

- toGenericString

```java
public abstract
String
toGenericString()
```

Returns a string describing this

Executable

, including
any type parameters.

**Returns:** a string describing this

Executable

, including
any type parameters

- isVarArgs

```java
public boolean isVarArgs()
```

Returns

true

if this executable was declared to take a
variable number of arguments; returns

false

otherwise.

**Returns:** true

if an only if this executable was declared
to take a variable number of arguments.

- isSynthetic

```java
public boolean isSynthetic()
```

Returns

true

if this executable is a synthetic
construct; returns

false

otherwise.

**Specified by:** isSynthetic

in interface

Member
**Returns:** true if and only if this executable is a synthetic
construct as defined by

The Java™ Language Specification

.
**See The Java™ Language Specification :** 13.1 The Form of a Binary

- getParameterAnnotations

```java
public abstract
Annotation
[][] getParameterAnnotations()
```

Returns an array of arrays of

Annotation

s that
represent the annotations on the formal parameters, in
declaration order, of the

Executable

represented by
this object. Synthetic and mandated parameters (see
explanation below), such as the outer "this" parameter to an
inner class constructor will be represented in the returned
array. If the executable has no parameters (meaning no formal,
no synthetic, and no mandated parameters), a zero-length array
will be returned. If the

Executable

has one or more
parameters, a nested array of length zero is returned for each
parameter with no annotations. The annotation objects contained
in the returned arrays are serializable. The caller of this
method is free to modify the returned arrays; it will have no
effect on the arrays returned to other callers.

A compiler may add extra parameters that are implicitly
declared in source ("mandated"), as well as parameters that
are neither implicitly nor explicitly declared in source
("synthetic") to the parameter list for a method. See

Parameter

for more information.

**Returns:** an array of arrays that represent the annotations on
the formal and implicit parameters, in declaration order, of
the executable represented by this object
**See Also:** Parameter

,

AnnotatedElement.getAnnotations()

- getAnnotation

```java
public <T extends
Annotation
> T getAnnotation​(
Class
<T> annotationClass)
```

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

**Specified by:** getAnnotation

in interface

AnnotatedElement
**Overrides:** getAnnotation

in class

AccessibleObject
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** this element's annotation for the specified annotation type if
present on this element, else null
**Throws:** NullPointerException

- if the given annotation class is null

- getAnnotationsByType

```java
public <T extends
Annotation
> T[] getAnnotationsByType​(
Class
<T> annotationClass)
```

Returns annotations that are

associated

with this element.

If there are no annotations

associated

with this element, the return
value is an array of length 0.

The difference between this method and

AnnotatedElement.getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

(JLS 9.6), and if so, attempts to find one or
more annotations of that type by "looking through" a container
annotation.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.

**Specified by:** getAnnotationsByType

in interface

AnnotatedElement
**Overrides:** getAnnotationsByType

in class

AccessibleObject
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** all this element's annotations for the specified annotation type if
associated with this element, else an array of length zero
**Throws:** NullPointerException

- if the given annotation class is null

- getAnnotatedReturnType

```java
public abstract
AnnotatedType
getAnnotatedReturnType()
```

Returns an

AnnotatedType

object that represents the use of a type to
specify the return type of the method/constructor represented by this
Executable.

If this

Executable

object represents a constructor, the

AnnotatedType

object represents the type of the constructed object.

If this

Executable

object represents a method, the

AnnotatedType

object represents the use of a type to specify the return
type of the method.

**Returns:** an object representing the return type of the method
or constructor represented by this

Executable

- getAnnotatedReceiverType

```java
public
AnnotatedType
getAnnotatedReceiverType()
```

Returns an

AnnotatedType

object that represents the use of a
type to specify the receiver type of the method/constructor represented
by this

Executable

object.

The receiver type of a method/constructor is available only if the
method/constructor has a receiver parameter (JLS 8.4.1). If this

Executable

object

represents an instance method or represents a
constructor of an inner member class

, and the
method/constructor

either

has no receiver parameter or has a
receiver parameter with no annotations on its type, then the return
value is an

AnnotatedType

object representing an element with no
annotations.

If this

Executable

object represents a static method or
represents a constructor of a top level, static member, local, or
anonymous class, then the return value is null.

**Returns:** an object representing the receiver type of the method or
constructor represented by this

Executable

or

null

if
this

Executable

can not have a receiver parameter

- getAnnotatedParameterTypes

```java
public
AnnotatedType
[] getAnnotatedParameterTypes()
```

Returns an array of

AnnotatedType

objects that represent the use
of types to specify formal parameter types of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the formal parameter types in the
declaration of the method/constructor.

Returns an array of length 0 if the method/constructor declares no
parameters.

**Returns:** an array of objects representing the types of the
formal parameters of the method or constructor represented by this

Executable

- getAnnotatedExceptionTypes

```java
public
AnnotatedType
[] getAnnotatedExceptionTypes()
```

Returns an array of

AnnotatedType

objects that represent the use
of types to specify the declared exceptions of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the exception types in the declaration of
the method/constructor.

Returns an array of length 0 if the method/constructor declares no
exceptions.

**Returns:** an array of objects representing the declared
exceptions of the method or constructor represented by this

Executable

Method Detail

- getDeclaringClass

```java
public abstract
Class
<?> getDeclaringClass()
```

Returns the

Class

object representing the class or interface
that declares the executable represented by this object.

**Specified by:** getDeclaringClass

in interface

Member
**Returns:** an object representing the declaring class of the
underlying member

- getName

```java
public abstract
String
getName()
```

Returns the name of the executable represented by this object.

**Specified by:** getName

in interface

Member
**Returns:** the simple name of the underlying member

- getModifiers

```java
public abstract int getModifiers()
```

Returns the Java language

modifiers

for
the executable represented by this object.

**Specified by:** getModifiers

in interface

Member
**Returns:** the Java language modifiers for the underlying member
**See Also:** Modifier

- getTypeParameters

```java
public abstract
TypeVariable
<?>[] getTypeParameters()
```

Returns an array of

TypeVariable

objects that represent the
type variables declared by the generic declaration represented by this

GenericDeclaration

object, in declaration order. Returns an
array of length 0 if the underlying generic declaration declares no type
variables.

**Specified by:** getTypeParameters

in interface

GenericDeclaration
**Returns:** an array of

TypeVariable

objects that represent
the type variables declared by this generic declaration
**Throws:** GenericSignatureFormatError

- if the generic
signature of this generic declaration does not conform to
the format specified in

The Java™ Virtual Machine Specification

- getParameterTypes

```java
public abstract
Class
<?>[] getParameterTypes()
```

Returns an array of

Class

objects that represent the formal
parameter types, in declaration order, of the executable
represented by this object. Returns an array of length
0 if the underlying executable takes no parameters.

**Returns:** the parameter types for the executable this object
represents

- getParameterCount

```java
public int getParameterCount()
```

Returns the number of formal parameters (whether explicitly
declared or implicitly declared or neither) for the executable
represented by this object.

**Returns:** The number of formal parameters for the executable this
object represents

- getGenericParameterTypes

```java
public
Type
[] getGenericParameterTypes()
```

Returns an array of

Type

objects that represent the formal
parameter types, in declaration order, of the executable represented by
this object. Returns an array of length 0 if the
underlying executable takes no parameters.

If a formal parameter type is a parameterized type,
the

Type

object returned for it must accurately reflect
the actual type parameters used in the source code.

If a formal parameter type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

**Returns:** an array of

Type

s that represent the formal
parameter types of the underlying executable, in declaration order
**Throws:** GenericSignatureFormatError

- if the generic method signature does not conform to the format
specified in

The Java™ Virtual Machine Specification
**Throws:** TypeNotPresentException

- if any of the parameter
types of the underlying executable refers to a non-existent type
declaration
**Throws:** MalformedParameterizedTypeException

- if any of
the underlying executable's parameter types refer to a parameterized
type that cannot be instantiated for any reason

- getParameters

```java
public
Parameter
[] getParameters()
```

Returns an array of

Parameter

objects that represent
all the parameters to the underlying executable represented by
this object. Returns an array of length 0 if the executable
has no parameters.

The parameters of the underlying executable do not necessarily
have unique names, or names that are legal identifiers in the
Java programming language (JLS 3.8).

**Returns:** an array of

Parameter

objects representing all
the parameters to the executable this object represents.
**Throws:** MalformedParametersException

- if the class file contains
a MethodParameters attribute that is improperly formatted.

- getExceptionTypes

```java
public abstract
Class
<?>[] getExceptionTypes()
```

Returns an array of

Class

objects that represent the
types of exceptions declared to be thrown by the underlying
executable represented by this object. Returns an array of
length 0 if the executable declares no exceptions in its

throws

clause.

**Returns:** the exception types declared as being thrown by the
executable this object represents

- getGenericExceptionTypes

```java
public
Type
[] getGenericExceptionTypes()
```

Returns an array of

Type

objects that represent the
exceptions declared to be thrown by this executable object.
Returns an array of length 0 if the underlying executable declares
no exceptions in its

throws

clause.

If an exception type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

**Returns:** an array of Types that represent the exception types
thrown by the underlying executable
**Throws:** GenericSignatureFormatError

- if the generic method signature does not conform to the format
specified in

The Java™ Virtual Machine Specification
**Throws:** TypeNotPresentException

- if the underlying executable's

throws

clause refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if
the underlying executable's

throws

clause refers to a
parameterized type that cannot be instantiated for any reason

- toGenericString

```java
public abstract
String
toGenericString()
```

Returns a string describing this

Executable

, including
any type parameters.

**Returns:** a string describing this

Executable

, including
any type parameters

- isVarArgs

```java
public boolean isVarArgs()
```

Returns

true

if this executable was declared to take a
variable number of arguments; returns

false

otherwise.

**Returns:** true

if an only if this executable was declared
to take a variable number of arguments.

- isSynthetic

```java
public boolean isSynthetic()
```

Returns

true

if this executable is a synthetic
construct; returns

false

otherwise.

**Specified by:** isSynthetic

in interface

Member
**Returns:** true if and only if this executable is a synthetic
construct as defined by

The Java™ Language Specification

.
**See The Java™ Language Specification :** 13.1 The Form of a Binary

- getParameterAnnotations

```java
public abstract
Annotation
[][] getParameterAnnotations()
```

Returns an array of arrays of

Annotation

s that
represent the annotations on the formal parameters, in
declaration order, of the

Executable

represented by
this object. Synthetic and mandated parameters (see
explanation below), such as the outer "this" parameter to an
inner class constructor will be represented in the returned
array. If the executable has no parameters (meaning no formal,
no synthetic, and no mandated parameters), a zero-length array
will be returned. If the

Executable

has one or more
parameters, a nested array of length zero is returned for each
parameter with no annotations. The annotation objects contained
in the returned arrays are serializable. The caller of this
method is free to modify the returned arrays; it will have no
effect on the arrays returned to other callers.

A compiler may add extra parameters that are implicitly
declared in source ("mandated"), as well as parameters that
are neither implicitly nor explicitly declared in source
("synthetic") to the parameter list for a method. See

Parameter

for more information.

**Returns:** an array of arrays that represent the annotations on
the formal and implicit parameters, in declaration order, of
the executable represented by this object
**See Also:** Parameter

,

AnnotatedElement.getAnnotations()

- getAnnotation

```java
public <T extends
Annotation
> T getAnnotation​(
Class
<T> annotationClass)
```

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

**Specified by:** getAnnotation

in interface

AnnotatedElement
**Overrides:** getAnnotation

in class

AccessibleObject
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** this element's annotation for the specified annotation type if
present on this element, else null
**Throws:** NullPointerException

- if the given annotation class is null

- getAnnotationsByType

```java
public <T extends
Annotation
> T[] getAnnotationsByType​(
Class
<T> annotationClass)
```

Returns annotations that are

associated

with this element.

If there are no annotations

associated

with this element, the return
value is an array of length 0.

The difference between this method and

AnnotatedElement.getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

(JLS 9.6), and if so, attempts to find one or
more annotations of that type by "looking through" a container
annotation.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.

**Specified by:** getAnnotationsByType

in interface

AnnotatedElement
**Overrides:** getAnnotationsByType

in class

AccessibleObject
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** all this element's annotations for the specified annotation type if
associated with this element, else an array of length zero
**Throws:** NullPointerException

- if the given annotation class is null

- getAnnotatedReturnType

```java
public abstract
AnnotatedType
getAnnotatedReturnType()
```

Returns an

AnnotatedType

object that represents the use of a type to
specify the return type of the method/constructor represented by this
Executable.

If this

Executable

object represents a constructor, the

AnnotatedType

object represents the type of the constructed object.

If this

Executable

object represents a method, the

AnnotatedType

object represents the use of a type to specify the return
type of the method.

**Returns:** an object representing the return type of the method
or constructor represented by this

Executable

- getAnnotatedReceiverType

```java
public
AnnotatedType
getAnnotatedReceiverType()
```

Returns an

AnnotatedType

object that represents the use of a
type to specify the receiver type of the method/constructor represented
by this

Executable

object.

The receiver type of a method/constructor is available only if the
method/constructor has a receiver parameter (JLS 8.4.1). If this

Executable

object

represents an instance method or represents a
constructor of an inner member class

, and the
method/constructor

either

has no receiver parameter or has a
receiver parameter with no annotations on its type, then the return
value is an

AnnotatedType

object representing an element with no
annotations.

If this

Executable

object represents a static method or
represents a constructor of a top level, static member, local, or
anonymous class, then the return value is null.

**Returns:** an object representing the receiver type of the method or
constructor represented by this

Executable

or

null

if
this

Executable

can not have a receiver parameter

- getAnnotatedParameterTypes

```java
public
AnnotatedType
[] getAnnotatedParameterTypes()
```

Returns an array of

AnnotatedType

objects that represent the use
of types to specify formal parameter types of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the formal parameter types in the
declaration of the method/constructor.

Returns an array of length 0 if the method/constructor declares no
parameters.

**Returns:** an array of objects representing the types of the
formal parameters of the method or constructor represented by this

Executable

- getAnnotatedExceptionTypes

```java
public
AnnotatedType
[] getAnnotatedExceptionTypes()
```

Returns an array of

AnnotatedType

objects that represent the use
of types to specify the declared exceptions of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the exception types in the declaration of
the method/constructor.

Returns an array of length 0 if the method/constructor declares no
exceptions.

**Returns:** an array of objects representing the declared
exceptions of the method or constructor represented by this

Executable

---

#### Method Detail

getDeclaringClass

```java
public abstract
Class
<?> getDeclaringClass()
```

Returns the

Class

object representing the class or interface
that declares the executable represented by this object.

**Specified by:** getDeclaringClass

in interface

Member
**Returns:** an object representing the declaring class of the
underlying member

---

#### getDeclaringClass

public abstract

Class

<?> getDeclaringClass()

Returns the

Class

object representing the class or interface
that declares the executable represented by this object.

getName

```java
public abstract
String
getName()
```

Returns the name of the executable represented by this object.

**Specified by:** getName

in interface

Member
**Returns:** the simple name of the underlying member

---

#### getName

public abstract

String

getName()

Returns the name of the executable represented by this object.

getModifiers

```java
public abstract int getModifiers()
```

Returns the Java language

modifiers

for
the executable represented by this object.

**Specified by:** getModifiers

in interface

Member
**Returns:** the Java language modifiers for the underlying member
**See Also:** Modifier

---

#### getModifiers

public abstract int getModifiers()

Returns the Java language

modifiers

for
the executable represented by this object.

getTypeParameters

```java
public abstract
TypeVariable
<?>[] getTypeParameters()
```

Returns an array of

TypeVariable

objects that represent the
type variables declared by the generic declaration represented by this

GenericDeclaration

object, in declaration order. Returns an
array of length 0 if the underlying generic declaration declares no type
variables.

**Specified by:** getTypeParameters

in interface

GenericDeclaration
**Returns:** an array of

TypeVariable

objects that represent
the type variables declared by this generic declaration
**Throws:** GenericSignatureFormatError

- if the generic
signature of this generic declaration does not conform to
the format specified in

The Java™ Virtual Machine Specification

---

#### getTypeParameters

public abstract

TypeVariable

<?>[] getTypeParameters()

Returns an array of

TypeVariable

objects that represent the
type variables declared by the generic declaration represented by this

GenericDeclaration

object, in declaration order. Returns an
array of length 0 if the underlying generic declaration declares no type
variables.

getParameterTypes

```java
public abstract
Class
<?>[] getParameterTypes()
```

Returns an array of

Class

objects that represent the formal
parameter types, in declaration order, of the executable
represented by this object. Returns an array of length
0 if the underlying executable takes no parameters.

**Returns:** the parameter types for the executable this object
represents

---

#### getParameterTypes

public abstract

Class

<?>[] getParameterTypes()

Returns an array of

Class

objects that represent the formal
parameter types, in declaration order, of the executable
represented by this object. Returns an array of length
0 if the underlying executable takes no parameters.

getParameterCount

```java
public int getParameterCount()
```

Returns the number of formal parameters (whether explicitly
declared or implicitly declared or neither) for the executable
represented by this object.

**Returns:** The number of formal parameters for the executable this
object represents

---

#### getParameterCount

public int getParameterCount()

Returns the number of formal parameters (whether explicitly
declared or implicitly declared or neither) for the executable
represented by this object.

getGenericParameterTypes

```java
public
Type
[] getGenericParameterTypes()
```

Returns an array of

Type

objects that represent the formal
parameter types, in declaration order, of the executable represented by
this object. Returns an array of length 0 if the
underlying executable takes no parameters.

If a formal parameter type is a parameterized type,
the

Type

object returned for it must accurately reflect
the actual type parameters used in the source code.

If a formal parameter type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

**Returns:** an array of

Type

s that represent the formal
parameter types of the underlying executable, in declaration order
**Throws:** GenericSignatureFormatError

- if the generic method signature does not conform to the format
specified in

The Java™ Virtual Machine Specification
**Throws:** TypeNotPresentException

- if any of the parameter
types of the underlying executable refers to a non-existent type
declaration
**Throws:** MalformedParameterizedTypeException

- if any of
the underlying executable's parameter types refer to a parameterized
type that cannot be instantiated for any reason

---

#### getGenericParameterTypes

public

Type

[] getGenericParameterTypes()

Returns an array of

Type

objects that represent the formal
parameter types, in declaration order, of the executable represented by
this object. Returns an array of length 0 if the
underlying executable takes no parameters.

If a formal parameter type is a parameterized type,
the

Type

object returned for it must accurately reflect
the actual type parameters used in the source code.

If a formal parameter type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

If a formal parameter type is a parameterized type,
the

Type

object returned for it must accurately reflect
the actual type parameters used in the source code.

If a formal parameter type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

If a formal parameter type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

getParameters

```java
public
Parameter
[] getParameters()
```

Returns an array of

Parameter

objects that represent
all the parameters to the underlying executable represented by
this object. Returns an array of length 0 if the executable
has no parameters.

The parameters of the underlying executable do not necessarily
have unique names, or names that are legal identifiers in the
Java programming language (JLS 3.8).

**Returns:** an array of

Parameter

objects representing all
the parameters to the executable this object represents.
**Throws:** MalformedParametersException

- if the class file contains
a MethodParameters attribute that is improperly formatted.

---

#### getParameters

public

Parameter

[] getParameters()

Returns an array of

Parameter

objects that represent
all the parameters to the underlying executable represented by
this object. Returns an array of length 0 if the executable
has no parameters.

The parameters of the underlying executable do not necessarily
have unique names, or names that are legal identifiers in the
Java programming language (JLS 3.8).

The parameters of the underlying executable do not necessarily
have unique names, or names that are legal identifiers in the
Java programming language (JLS 3.8).

getExceptionTypes

```java
public abstract
Class
<?>[] getExceptionTypes()
```

Returns an array of

Class

objects that represent the
types of exceptions declared to be thrown by the underlying
executable represented by this object. Returns an array of
length 0 if the executable declares no exceptions in its

throws

clause.

**Returns:** the exception types declared as being thrown by the
executable this object represents

---

#### getExceptionTypes

public abstract

Class

<?>[] getExceptionTypes()

Returns an array of

Class

objects that represent the
types of exceptions declared to be thrown by the underlying
executable represented by this object. Returns an array of
length 0 if the executable declares no exceptions in its

throws

clause.

getGenericExceptionTypes

```java
public
Type
[] getGenericExceptionTypes()
```

Returns an array of

Type

objects that represent the
exceptions declared to be thrown by this executable object.
Returns an array of length 0 if the underlying executable declares
no exceptions in its

throws

clause.

If an exception type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

**Returns:** an array of Types that represent the exception types
thrown by the underlying executable
**Throws:** GenericSignatureFormatError

- if the generic method signature does not conform to the format
specified in

The Java™ Virtual Machine Specification
**Throws:** TypeNotPresentException

- if the underlying executable's

throws

clause refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if
the underlying executable's

throws

clause refers to a
parameterized type that cannot be instantiated for any reason

---

#### getGenericExceptionTypes

public

Type

[] getGenericExceptionTypes()

Returns an array of

Type

objects that represent the
exceptions declared to be thrown by this executable object.
Returns an array of length 0 if the underlying executable declares
no exceptions in its

throws

clause.

If an exception type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

If an exception type is a type variable or a parameterized
type, it is created. Otherwise, it is resolved.

toGenericString

```java
public abstract
String
toGenericString()
```

Returns a string describing this

Executable

, including
any type parameters.

**Returns:** a string describing this

Executable

, including
any type parameters

---

#### toGenericString

public abstract

String

toGenericString()

Returns a string describing this

Executable

, including
any type parameters.

isVarArgs

```java
public boolean isVarArgs()
```

Returns

true

if this executable was declared to take a
variable number of arguments; returns

false

otherwise.

**Returns:** true

if an only if this executable was declared
to take a variable number of arguments.

---

#### isVarArgs

public boolean isVarArgs()

Returns

true

if this executable was declared to take a
variable number of arguments; returns

false

otherwise.

isSynthetic

```java
public boolean isSynthetic()
```

Returns

true

if this executable is a synthetic
construct; returns

false

otherwise.

**Specified by:** isSynthetic

in interface

Member
**Returns:** true if and only if this executable is a synthetic
construct as defined by

The Java™ Language Specification

.
**See The Java™ Language Specification :** 13.1 The Form of a Binary

---

#### isSynthetic

public boolean isSynthetic()

Returns

true

if this executable is a synthetic
construct; returns

false

otherwise.

getParameterAnnotations

```java
public abstract
Annotation
[][] getParameterAnnotations()
```

Returns an array of arrays of

Annotation

s that
represent the annotations on the formal parameters, in
declaration order, of the

Executable

represented by
this object. Synthetic and mandated parameters (see
explanation below), such as the outer "this" parameter to an
inner class constructor will be represented in the returned
array. If the executable has no parameters (meaning no formal,
no synthetic, and no mandated parameters), a zero-length array
will be returned. If the

Executable

has one or more
parameters, a nested array of length zero is returned for each
parameter with no annotations. The annotation objects contained
in the returned arrays are serializable. The caller of this
method is free to modify the returned arrays; it will have no
effect on the arrays returned to other callers.

A compiler may add extra parameters that are implicitly
declared in source ("mandated"), as well as parameters that
are neither implicitly nor explicitly declared in source
("synthetic") to the parameter list for a method. See

Parameter

for more information.

**Returns:** an array of arrays that represent the annotations on
the formal and implicit parameters, in declaration order, of
the executable represented by this object
**See Also:** Parameter

,

AnnotatedElement.getAnnotations()

---

#### getParameterAnnotations

public abstract

Annotation

[][] getParameterAnnotations()

Returns an array of arrays of

Annotation

s that
represent the annotations on the formal parameters, in
declaration order, of the

Executable

represented by
this object. Synthetic and mandated parameters (see
explanation below), such as the outer "this" parameter to an
inner class constructor will be represented in the returned
array. If the executable has no parameters (meaning no formal,
no synthetic, and no mandated parameters), a zero-length array
will be returned. If the

Executable

has one or more
parameters, a nested array of length zero is returned for each
parameter with no annotations. The annotation objects contained
in the returned arrays are serializable. The caller of this
method is free to modify the returned arrays; it will have no
effect on the arrays returned to other callers.

A compiler may add extra parameters that are implicitly
declared in source ("mandated"), as well as parameters that
are neither implicitly nor explicitly declared in source
("synthetic") to the parameter list for a method. See

Parameter

for more information.

getAnnotation

```java
public <T extends
Annotation
> T getAnnotation​(
Class
<T> annotationClass)
```

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

**Specified by:** getAnnotation

in interface

AnnotatedElement
**Overrides:** getAnnotation

in class

AccessibleObject
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** this element's annotation for the specified annotation type if
present on this element, else null
**Throws:** NullPointerException

- if the given annotation class is null

---

#### getAnnotation

public <T extends

Annotation

> T getAnnotation​(

Class

<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

getAnnotationsByType

```java
public <T extends
Annotation
> T[] getAnnotationsByType​(
Class
<T> annotationClass)
```

Returns annotations that are

associated

with this element.

If there are no annotations

associated

with this element, the return
value is an array of length 0.

The difference between this method and

AnnotatedElement.getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

(JLS 9.6), and if so, attempts to find one or
more annotations of that type by "looking through" a container
annotation.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.

**Specified by:** getAnnotationsByType

in interface

AnnotatedElement
**Overrides:** getAnnotationsByType

in class

AccessibleObject
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** all this element's annotations for the specified annotation type if
associated with this element, else an array of length zero
**Throws:** NullPointerException

- if the given annotation class is null

---

#### getAnnotationsByType

public <T extends

Annotation

> T[] getAnnotationsByType​(

Class

<T> annotationClass)

Returns annotations that are

associated

with this element.

If there are no annotations

associated

with this element, the return
value is an array of length 0.

The difference between this method and

AnnotatedElement.getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

(JLS 9.6), and if so, attempts to find one or
more annotations of that type by "looking through" a container
annotation.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.

getAnnotatedReturnType

```java
public abstract
AnnotatedType
getAnnotatedReturnType()
```

Returns an

AnnotatedType

object that represents the use of a type to
specify the return type of the method/constructor represented by this
Executable.

If this

Executable

object represents a constructor, the

AnnotatedType

object represents the type of the constructed object.

If this

Executable

object represents a method, the

AnnotatedType

object represents the use of a type to specify the return
type of the method.

**Returns:** an object representing the return type of the method
or constructor represented by this

Executable

---

#### getAnnotatedReturnType

public abstract

AnnotatedType

getAnnotatedReturnType()

Returns an

AnnotatedType

object that represents the use of a type to
specify the return type of the method/constructor represented by this
Executable.

If this

Executable

object represents a constructor, the

AnnotatedType

object represents the type of the constructed object.

If this

Executable

object represents a method, the

AnnotatedType

object represents the use of a type to specify the return
type of the method.

getAnnotatedReceiverType

```java
public
AnnotatedType
getAnnotatedReceiverType()
```

Returns an

AnnotatedType

object that represents the use of a
type to specify the receiver type of the method/constructor represented
by this

Executable

object.

The receiver type of a method/constructor is available only if the
method/constructor has a receiver parameter (JLS 8.4.1). If this

Executable

object

represents an instance method or represents a
constructor of an inner member class

, and the
method/constructor

either

has no receiver parameter or has a
receiver parameter with no annotations on its type, then the return
value is an

AnnotatedType

object representing an element with no
annotations.

If this

Executable

object represents a static method or
represents a constructor of a top level, static member, local, or
anonymous class, then the return value is null.

**Returns:** an object representing the receiver type of the method or
constructor represented by this

Executable

or

null

if
this

Executable

can not have a receiver parameter

---

#### getAnnotatedReceiverType

public

AnnotatedType

getAnnotatedReceiverType()

Returns an

AnnotatedType

object that represents the use of a
type to specify the receiver type of the method/constructor represented
by this

Executable

object.

The receiver type of a method/constructor is available only if the
method/constructor has a receiver parameter (JLS 8.4.1). If this

Executable

object

represents an instance method or represents a
constructor of an inner member class

, and the
method/constructor

either

has no receiver parameter or has a
receiver parameter with no annotations on its type, then the return
value is an

AnnotatedType

object representing an element with no
annotations.

If this

Executable

object represents a static method or
represents a constructor of a top level, static member, local, or
anonymous class, then the return value is null.

getAnnotatedParameterTypes

```java
public
AnnotatedType
[] getAnnotatedParameterTypes()
```

Returns an array of

AnnotatedType

objects that represent the use
of types to specify formal parameter types of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the formal parameter types in the
declaration of the method/constructor.

Returns an array of length 0 if the method/constructor declares no
parameters.

**Returns:** an array of objects representing the types of the
formal parameters of the method or constructor represented by this

Executable

---

#### getAnnotatedParameterTypes

public

AnnotatedType

[] getAnnotatedParameterTypes()

Returns an array of

AnnotatedType

objects that represent the use
of types to specify formal parameter types of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the formal parameter types in the
declaration of the method/constructor.

Returns an array of length 0 if the method/constructor declares no
parameters.

getAnnotatedExceptionTypes

```java
public
AnnotatedType
[] getAnnotatedExceptionTypes()
```

Returns an array of

AnnotatedType

objects that represent the use
of types to specify the declared exceptions of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the exception types in the declaration of
the method/constructor.

Returns an array of length 0 if the method/constructor declares no
exceptions.

**Returns:** an array of objects representing the declared
exceptions of the method or constructor represented by this

Executable

---

#### getAnnotatedExceptionTypes

public

AnnotatedType

[] getAnnotatedExceptionTypes()

Returns an array of

AnnotatedType

objects that represent the use
of types to specify the declared exceptions of the method/constructor
represented by this Executable. The order of the objects in the array
corresponds to the order of the exception types in the declaration of
the method/constructor.

Returns an array of length 0 if the method/constructor declares no
exceptions.

---

