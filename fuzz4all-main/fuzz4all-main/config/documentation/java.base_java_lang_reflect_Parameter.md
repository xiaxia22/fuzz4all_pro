# Class Parameter

**Source:** `java.base\java\lang\reflect\Parameter.html`

### Class Description

```java
public final class
Parameter

extends
Object

implements
AnnotatedElement
```

Information about method parameters.

A

Parameter

provides information about method parameters,
including its name and modifiers. It also provides an alternate
means of obtaining attributes for the parameter.

**All Implemented Interfaces:** AnnotatedElement

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public boolean equals​(
Object
obj)

Compares based on the executable and the index.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The object to compare.

**Returns:**
- Whether or not this is equal to the argument.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code based on the executable's hash code and the
index.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- A hash code based on the executable's hash code.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean isNamePresent()

Returns true if the parameter has a name according to the class
file; returns false otherwise. Whether a parameter has a name
is determined by the MethodParameters attribute of
the method which declares the parameter.

**Returns:**
- true if and only if the parameter has a name according
to the class file.

---

#### public
String
toString()

Returns a string describing this parameter. The format is the
modifiers for the parameter, if any, in canonical order as
recommended by

The Java™ Language
Specification

, followed by the fully- qualified type of
the parameter (excluding the last [] if the parameter is
variable arity), followed by "..." if the parameter is variable
arity, followed by a space, followed by the name of the
parameter.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string representation of the parameter and associated
information.

---

#### public
Executable
getDeclaringExecutable()

Return the

Executable

which declares this parameter.

**Returns:**
- The

Executable

declaring this parameter.

---

#### public int getModifiers()

Get the modifier flags for this the parameter represented by
this

Parameter

object.

**Returns:**
- The modifier flags for this parameter.

---

#### public
String
getName()

Returns the name of the parameter. If the parameter's name is

present

, then this method returns
the name provided by the class file. Otherwise, this method
synthesizes a name of the form argN, where N is the index of
the parameter in the descriptor of the method which declares
the parameter.

**Returns:**
- The name of the parameter, either provided by the class
file or synthesized if the class file does not provide
a name.

---

#### public
Type
getParameterizedType()

Returns a

Type

object that identifies the parameterized
type for the parameter represented by this

Parameter

object.

**Returns:**
- a

Type

object identifying the parameterized
type of the parameter represented by this object

---

#### public
Class
<?> getType()

Returns a

Class

object that identifies the
declared type for the parameter represented by this

Parameter

object.

**Returns:**
- a

Class

object identifying the declared
type of the parameter represented by this object

---

#### public
AnnotatedType
getAnnotatedType()

Returns an AnnotatedType object that represents the use of a type to
specify the type of the formal parameter represented by this Parameter.

**Returns:**
- an

AnnotatedType

object representing the use of a type
to specify the type of the formal parameter represented by this
Parameter

---

#### public boolean isImplicit()

Returns

true

if this parameter is implicitly declared
in source code; returns

false

otherwise.

**Returns:**
- true if and only if this parameter is implicitly
declared as defined by

The Java™ Language
Specification

.

---

#### public boolean isSynthetic()

Returns

true

if this parameter is neither implicitly
nor explicitly declared in source code; returns

false

otherwise.

**Returns:**
- true if and only if this parameter is a synthetic
construct as defined by

The Java™ Language Specification

.

**See The Java™ Language Specification :**
- 13.1 The Form of a Binary

---

#### public boolean isVarArgs()

Returns

true

if this parameter represents a variable
argument list; returns

false

otherwise.

**Returns:**
- true

if an only if this parameter represents a
variable argument list.

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

#### public <T extends
Annotation
> T getDeclaredAnnotation​(
Class
<T> annotationClass)

Description copied from interface:

AnnotatedElement

**Specified by:**
- getDeclaredAnnotation

in interface

AnnotatedElement

**Parameters:**
- annotationClass

- the Class object corresponding to the
annotation type

**Returns:**
- this element's annotation for the specified annotation type if
directly present on this element, else null

**Throws:**
- NullPointerException

- if the given annotation class is null

**Type Parameters:**
- T

- the type of the annotation to query for and return if directly present

---

#### public <T extends
Annotation
> T[] getDeclaredAnnotationsByType​(
Class
<T> annotationClass)

Description copied from interface:

AnnotatedElement

**Specified by:**
- getDeclaredAnnotationsByType

in interface

AnnotatedElement

**Parameters:**
- annotationClass

- the Class object corresponding to the
annotation type

**Returns:**
- all this element's annotations for the specified annotation type if
directly or indirectly present on this element, else an array of length zero

**Throws:**
- NullPointerException

- if the given annotation class is null

**Type Parameters:**
- T

- the type of the annotation to query for and return
if directly or indirectly present

---

### Additional Sections

#### Class Parameter

java.lang.Object

- java.lang.reflect.Parameter

java.lang.reflect.Parameter

**All Implemented Interfaces:** AnnotatedElement

```java
public final class
Parameter

extends
Object

implements
AnnotatedElement
```

Information about method parameters.

A

Parameter

provides information about method parameters,
including its name and modifiers. It also provides an alternate
means of obtaining attributes for the parameter.

**Since:** 1.8

public final class

Parameter

extends

Object

implements

AnnotatedElement

Information about method parameters.

A

Parameter

provides information about method parameters,
including its name and modifiers. It also provides an alternate
means of obtaining attributes for the parameter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares based on the executable and the index.

AnnotatedType

getAnnotatedType

()

Returns an AnnotatedType object that represents the use of a type to
specify the type of the formal parameter represented by this Parameter.

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

<T extends

Annotation

>

T

getDeclaredAnnotation

​(

Class

<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

directly present

, else null.

<T extends

Annotation

>

T[]

getDeclaredAnnotationsByType

​(

Class

<T> annotationClass)

Returns this element's annotation(s) for the specified type if
such annotations are either

directly present

or

indirectly present

.

Executable

getDeclaringExecutable

()

Return the

Executable

which declares this parameter.

int

getModifiers

()

Get the modifier flags for this the parameter represented by
this

Parameter

object.

String

getName

()

Returns the name of the parameter.

Type

getParameterizedType

()

Returns a

Type

object that identifies the parameterized
type for the parameter represented by this

Parameter

object.

Class

<?>

getType

()

Returns a

Class

object that identifies the
declared type for the parameter represented by this

Parameter

object.

int

hashCode

()

Returns a hash code based on the executable's hash code and the
index.

boolean

isImplicit

()

Returns

true

if this parameter is implicitly declared
in source code; returns

false

otherwise.

boolean

isNamePresent

()

Returns true if the parameter has a name according to the class
file; returns false otherwise.

boolean

isSynthetic

()

Returns

true

if this parameter is neither implicitly
nor explicitly declared in source code; returns

false

otherwise.

boolean

isVarArgs

()

Returns

true

if this parameter represents a variable
argument list; returns

false

otherwise.

String

toString

()

Returns a string describing this parameter.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

- Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotations

,

getDeclaredAnnotations

,

isAnnotationPresent

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares based on the executable and the index.

AnnotatedType

getAnnotatedType

()

Returns an AnnotatedType object that represents the use of a type to
specify the type of the formal parameter represented by this Parameter.

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

<T extends

Annotation

>

T

getDeclaredAnnotation

​(

Class

<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

directly present

, else null.

<T extends

Annotation

>

T[]

getDeclaredAnnotationsByType

​(

Class

<T> annotationClass)

Returns this element's annotation(s) for the specified type if
such annotations are either

directly present

or

indirectly present

.

Executable

getDeclaringExecutable

()

Return the

Executable

which declares this parameter.

int

getModifiers

()

Get the modifier flags for this the parameter represented by
this

Parameter

object.

String

getName

()

Returns the name of the parameter.

Type

getParameterizedType

()

Returns a

Type

object that identifies the parameterized
type for the parameter represented by this

Parameter

object.

Class

<?>

getType

()

Returns a

Class

object that identifies the
declared type for the parameter represented by this

Parameter

object.

int

hashCode

()

Returns a hash code based on the executable's hash code and the
index.

boolean

isImplicit

()

Returns

true

if this parameter is implicitly declared
in source code; returns

false

otherwise.

boolean

isNamePresent

()

Returns true if the parameter has a name according to the class
file; returns false otherwise.

boolean

isSynthetic

()

Returns

true

if this parameter is neither implicitly
nor explicitly declared in source code; returns

false

otherwise.

boolean

isVarArgs

()

Returns

true

if this parameter represents a variable
argument list; returns

false

otherwise.

String

toString

()

Returns a string describing this parameter.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

- Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotations

,

getDeclaredAnnotations

,

isAnnotationPresent

---

#### Method Summary

Compares based on the executable and the index.

Returns an AnnotatedType object that represents the use of a type to
specify the type of the formal parameter represented by this Parameter.

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

Returns annotations that are

associated

with this element.

Returns this element's annotation for the specified type if
such an annotation is

directly present

, else null.

Returns this element's annotation(s) for the specified type if
such annotations are either

directly present

or

indirectly present

.

Return the

Executable

which declares this parameter.

Get the modifier flags for this the parameter represented by
this

Parameter

object.

Returns the name of the parameter.

Returns a

Type

object that identifies the parameterized
type for the parameter represented by this

Parameter

object.

Returns a

Class

object that identifies the
declared type for the parameter represented by this

Parameter

object.

Returns a hash code based on the executable's hash code and the
index.

Returns

true

if this parameter is implicitly declared
in source code; returns

false

otherwise.

Returns true if the parameter has a name according to the class
file; returns false otherwise.

Returns

true

if this parameter is neither implicitly
nor explicitly declared in source code; returns

false

otherwise.

Returns

true

if this parameter represents a variable
argument list; returns

false

otherwise.

Returns a string describing this parameter.

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotations

,

getDeclaredAnnotations

,

isAnnotationPresent

---

#### Methods declared in interface java.lang.reflect. AnnotatedElement

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
obj)
```

Compares based on the executable and the index.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare.
**Returns:** Whether or not this is equal to the argument.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code based on the executable's hash code and the
index.

**Overrides:** hashCode

in class

Object
**Returns:** A hash code based on the executable's hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- isNamePresent

```java
public boolean isNamePresent()
```

Returns true if the parameter has a name according to the class
file; returns false otherwise. Whether a parameter has a name
is determined by the MethodParameters attribute of
the method which declares the parameter.

**Returns:** true if and only if the parameter has a name according
to the class file.

- toString

```java
public
String
toString()
```

Returns a string describing this parameter. The format is the
modifiers for the parameter, if any, in canonical order as
recommended by

The Java™ Language
Specification

, followed by the fully- qualified type of
the parameter (excluding the last [] if the parameter is
variable arity), followed by "..." if the parameter is variable
arity, followed by a space, followed by the name of the
parameter.

**Overrides:** toString

in class

Object
**Returns:** A string representation of the parameter and associated
information.

- getDeclaringExecutable

```java
public
Executable
getDeclaringExecutable()
```

Return the

Executable

which declares this parameter.

**Returns:** The

Executable

declaring this parameter.

- getModifiers

```java
public int getModifiers()
```

Get the modifier flags for this the parameter represented by
this

Parameter

object.

**Returns:** The modifier flags for this parameter.

- getName

```java
public
String
getName()
```

Returns the name of the parameter. If the parameter's name is

present

, then this method returns
the name provided by the class file. Otherwise, this method
synthesizes a name of the form argN, where N is the index of
the parameter in the descriptor of the method which declares
the parameter.

**Returns:** The name of the parameter, either provided by the class
file or synthesized if the class file does not provide
a name.

- getParameterizedType

```java
public
Type
getParameterizedType()
```

Returns a

Type

object that identifies the parameterized
type for the parameter represented by this

Parameter

object.

**Returns:** a

Type

object identifying the parameterized
type of the parameter represented by this object

- getType

```java
public
Class
<?> getType()
```

Returns a

Class

object that identifies the
declared type for the parameter represented by this

Parameter

object.

**Returns:** a

Class

object identifying the declared
type of the parameter represented by this object

- getAnnotatedType

```java
public
AnnotatedType
getAnnotatedType()
```

Returns an AnnotatedType object that represents the use of a type to
specify the type of the formal parameter represented by this Parameter.

**Returns:** an

AnnotatedType

object representing the use of a type
to specify the type of the formal parameter represented by this
Parameter

- isImplicit

```java
public boolean isImplicit()
```

Returns

true

if this parameter is implicitly declared
in source code; returns

false

otherwise.

**Returns:** true if and only if this parameter is implicitly
declared as defined by

The Java™ Language
Specification

.

- isSynthetic

```java
public boolean isSynthetic()
```

Returns

true

if this parameter is neither implicitly
nor explicitly declared in source code; returns

false

otherwise.

**Returns:** true if and only if this parameter is a synthetic
construct as defined by

The Java™ Language Specification

.
**See The Java™ Language Specification :** 13.1 The Form of a Binary

- isVarArgs

```java
public boolean isVarArgs()
```

Returns

true

if this parameter represents a variable
argument list; returns

false

otherwise.

**Returns:** true

if an only if this parameter represents a
variable argument list.

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
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** all this element's annotations for the specified annotation type if
associated with this element, else an array of length zero
**Throws:** NullPointerException

- if the given annotation class is null

- getDeclaredAnnotation

```java
public <T extends
Annotation
> T getDeclaredAnnotation​(
Class
<T> annotationClass)
```

Description copied from interface:

AnnotatedElement

Returns this element's annotation for the specified type if
such an annotation is

directly present

, else null.

This method ignores inherited annotations. (Returns null if no
annotations are directly present on this element.)

**Specified by:** getDeclaredAnnotation

in interface

AnnotatedElement
**Type Parameters:** T

- the type of the annotation to query for and return if directly present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** this element's annotation for the specified annotation type if
directly present on this element, else null
**Throws:** NullPointerException

- if the given annotation class is null

- getDeclaredAnnotationsByType

```java
public <T extends
Annotation
> T[] getDeclaredAnnotationsByType​(
Class
<T> annotationClass)
```

Description copied from interface:

AnnotatedElement

Returns this element's annotation(s) for the specified type if
such annotations are either

directly present

or

indirectly present

. This method ignores inherited
annotations.

If there are no specified annotations directly or indirectly
present on this element, the return value is an array of length
0.

The difference between this method and

AnnotatedElement.getDeclaredAnnotation(Class)

is that this method detects if its
argument is a

repeatable annotation type

(JLS 9.6), and if so,
attempts to find one or more annotations of that type by "looking
through" a container annotation if one is present.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.

**Specified by:** getDeclaredAnnotationsByType

in interface

AnnotatedElement
**Type Parameters:** T

- the type of the annotation to query for and return
if directly or indirectly present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** all this element's annotations for the specified annotation type if
directly or indirectly present on this element, else an array of length zero
**Throws:** NullPointerException

- if the given annotation class is null

Method Detail

- equals

```java
public boolean equals​(
Object
obj)
```

Compares based on the executable and the index.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare.
**Returns:** Whether or not this is equal to the argument.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code based on the executable's hash code and the
index.

**Overrides:** hashCode

in class

Object
**Returns:** A hash code based on the executable's hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- isNamePresent

```java
public boolean isNamePresent()
```

Returns true if the parameter has a name according to the class
file; returns false otherwise. Whether a parameter has a name
is determined by the MethodParameters attribute of
the method which declares the parameter.

**Returns:** true if and only if the parameter has a name according
to the class file.

- toString

```java
public
String
toString()
```

Returns a string describing this parameter. The format is the
modifiers for the parameter, if any, in canonical order as
recommended by

The Java™ Language
Specification

, followed by the fully- qualified type of
the parameter (excluding the last [] if the parameter is
variable arity), followed by "..." if the parameter is variable
arity, followed by a space, followed by the name of the
parameter.

**Overrides:** toString

in class

Object
**Returns:** A string representation of the parameter and associated
information.

- getDeclaringExecutable

```java
public
Executable
getDeclaringExecutable()
```

Return the

Executable

which declares this parameter.

**Returns:** The

Executable

declaring this parameter.

- getModifiers

```java
public int getModifiers()
```

Get the modifier flags for this the parameter represented by
this

Parameter

object.

**Returns:** The modifier flags for this parameter.

- getName

```java
public
String
getName()
```

Returns the name of the parameter. If the parameter's name is

present

, then this method returns
the name provided by the class file. Otherwise, this method
synthesizes a name of the form argN, where N is the index of
the parameter in the descriptor of the method which declares
the parameter.

**Returns:** The name of the parameter, either provided by the class
file or synthesized if the class file does not provide
a name.

- getParameterizedType

```java
public
Type
getParameterizedType()
```

Returns a

Type

object that identifies the parameterized
type for the parameter represented by this

Parameter

object.

**Returns:** a

Type

object identifying the parameterized
type of the parameter represented by this object

- getType

```java
public
Class
<?> getType()
```

Returns a

Class

object that identifies the
declared type for the parameter represented by this

Parameter

object.

**Returns:** a

Class

object identifying the declared
type of the parameter represented by this object

- getAnnotatedType

```java
public
AnnotatedType
getAnnotatedType()
```

Returns an AnnotatedType object that represents the use of a type to
specify the type of the formal parameter represented by this Parameter.

**Returns:** an

AnnotatedType

object representing the use of a type
to specify the type of the formal parameter represented by this
Parameter

- isImplicit

```java
public boolean isImplicit()
```

Returns

true

if this parameter is implicitly declared
in source code; returns

false

otherwise.

**Returns:** true if and only if this parameter is implicitly
declared as defined by

The Java™ Language
Specification

.

- isSynthetic

```java
public boolean isSynthetic()
```

Returns

true

if this parameter is neither implicitly
nor explicitly declared in source code; returns

false

otherwise.

**Returns:** true if and only if this parameter is a synthetic
construct as defined by

The Java™ Language Specification

.
**See The Java™ Language Specification :** 13.1 The Form of a Binary

- isVarArgs

```java
public boolean isVarArgs()
```

Returns

true

if this parameter represents a variable
argument list; returns

false

otherwise.

**Returns:** true

if an only if this parameter represents a
variable argument list.

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
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** all this element's annotations for the specified annotation type if
associated with this element, else an array of length zero
**Throws:** NullPointerException

- if the given annotation class is null

- getDeclaredAnnotation

```java
public <T extends
Annotation
> T getDeclaredAnnotation​(
Class
<T> annotationClass)
```

Description copied from interface:

AnnotatedElement

Returns this element's annotation for the specified type if
such an annotation is

directly present

, else null.

This method ignores inherited annotations. (Returns null if no
annotations are directly present on this element.)

**Specified by:** getDeclaredAnnotation

in interface

AnnotatedElement
**Type Parameters:** T

- the type of the annotation to query for and return if directly present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** this element's annotation for the specified annotation type if
directly present on this element, else null
**Throws:** NullPointerException

- if the given annotation class is null

- getDeclaredAnnotationsByType

```java
public <T extends
Annotation
> T[] getDeclaredAnnotationsByType​(
Class
<T> annotationClass)
```

Description copied from interface:

AnnotatedElement

Returns this element's annotation(s) for the specified type if
such annotations are either

directly present

or

indirectly present

. This method ignores inherited
annotations.

If there are no specified annotations directly or indirectly
present on this element, the return value is an array of length
0.

The difference between this method and

AnnotatedElement.getDeclaredAnnotation(Class)

is that this method detects if its
argument is a

repeatable annotation type

(JLS 9.6), and if so,
attempts to find one or more annotations of that type by "looking
through" a container annotation if one is present.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.

**Specified by:** getDeclaredAnnotationsByType

in interface

AnnotatedElement
**Type Parameters:** T

- the type of the annotation to query for and return
if directly or indirectly present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** all this element's annotations for the specified annotation type if
directly or indirectly present on this element, else an array of length zero
**Throws:** NullPointerException

- if the given annotation class is null

---

#### Method Detail

equals

```java
public boolean equals​(
Object
obj)
```

Compares based on the executable and the index.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare.
**Returns:** Whether or not this is equal to the argument.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares based on the executable and the index.

hashCode

```java
public int hashCode()
```

Returns a hash code based on the executable's hash code and the
index.

**Overrides:** hashCode

in class

Object
**Returns:** A hash code based on the executable's hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code based on the executable's hash code and the
index.

isNamePresent

```java
public boolean isNamePresent()
```

Returns true if the parameter has a name according to the class
file; returns false otherwise. Whether a parameter has a name
is determined by the MethodParameters attribute of
the method which declares the parameter.

**Returns:** true if and only if the parameter has a name according
to the class file.

---

#### isNamePresent

public boolean isNamePresent()

Returns true if the parameter has a name according to the class
file; returns false otherwise. Whether a parameter has a name
is determined by the MethodParameters attribute of
the method which declares the parameter.

toString

```java
public
String
toString()
```

Returns a string describing this parameter. The format is the
modifiers for the parameter, if any, in canonical order as
recommended by

The Java™ Language
Specification

, followed by the fully- qualified type of
the parameter (excluding the last [] if the parameter is
variable arity), followed by "..." if the parameter is variable
arity, followed by a space, followed by the name of the
parameter.

**Overrides:** toString

in class

Object
**Returns:** A string representation of the parameter and associated
information.

---

#### toString

public

String

toString()

Returns a string describing this parameter. The format is the
modifiers for the parameter, if any, in canonical order as
recommended by

The Java™ Language
Specification

, followed by the fully- qualified type of
the parameter (excluding the last [] if the parameter is
variable arity), followed by "..." if the parameter is variable
arity, followed by a space, followed by the name of the
parameter.

getDeclaringExecutable

```java
public
Executable
getDeclaringExecutable()
```

Return the

Executable

which declares this parameter.

**Returns:** The

Executable

declaring this parameter.

---

#### getDeclaringExecutable

public

Executable

getDeclaringExecutable()

Return the

Executable

which declares this parameter.

getModifiers

```java
public int getModifiers()
```

Get the modifier flags for this the parameter represented by
this

Parameter

object.

**Returns:** The modifier flags for this parameter.

---

#### getModifiers

public int getModifiers()

Get the modifier flags for this the parameter represented by
this

Parameter

object.

getName

```java
public
String
getName()
```

Returns the name of the parameter. If the parameter's name is

present

, then this method returns
the name provided by the class file. Otherwise, this method
synthesizes a name of the form argN, where N is the index of
the parameter in the descriptor of the method which declares
the parameter.

**Returns:** The name of the parameter, either provided by the class
file or synthesized if the class file does not provide
a name.

---

#### getName

public

String

getName()

Returns the name of the parameter. If the parameter's name is

present

, then this method returns
the name provided by the class file. Otherwise, this method
synthesizes a name of the form argN, where N is the index of
the parameter in the descriptor of the method which declares
the parameter.

getParameterizedType

```java
public
Type
getParameterizedType()
```

Returns a

Type

object that identifies the parameterized
type for the parameter represented by this

Parameter

object.

**Returns:** a

Type

object identifying the parameterized
type of the parameter represented by this object

---

#### getParameterizedType

public

Type

getParameterizedType()

Returns a

Type

object that identifies the parameterized
type for the parameter represented by this

Parameter

object.

getType

```java
public
Class
<?> getType()
```

Returns a

Class

object that identifies the
declared type for the parameter represented by this

Parameter

object.

**Returns:** a

Class

object identifying the declared
type of the parameter represented by this object

---

#### getType

public

Class

<?> getType()

Returns a

Class

object that identifies the
declared type for the parameter represented by this

Parameter

object.

getAnnotatedType

```java
public
AnnotatedType
getAnnotatedType()
```

Returns an AnnotatedType object that represents the use of a type to
specify the type of the formal parameter represented by this Parameter.

**Returns:** an

AnnotatedType

object representing the use of a type
to specify the type of the formal parameter represented by this
Parameter

---

#### getAnnotatedType

public

AnnotatedType

getAnnotatedType()

Returns an AnnotatedType object that represents the use of a type to
specify the type of the formal parameter represented by this Parameter.

isImplicit

```java
public boolean isImplicit()
```

Returns

true

if this parameter is implicitly declared
in source code; returns

false

otherwise.

**Returns:** true if and only if this parameter is implicitly
declared as defined by

The Java™ Language
Specification

.

---

#### isImplicit

public boolean isImplicit()

Returns

true

if this parameter is implicitly declared
in source code; returns

false

otherwise.

isSynthetic

```java
public boolean isSynthetic()
```

Returns

true

if this parameter is neither implicitly
nor explicitly declared in source code; returns

false

otherwise.

**Returns:** true if and only if this parameter is a synthetic
construct as defined by

The Java™ Language Specification

.
**See The Java™ Language Specification :** 13.1 The Form of a Binary

---

#### isSynthetic

public boolean isSynthetic()

Returns

true

if this parameter is neither implicitly
nor explicitly declared in source code; returns

false

otherwise.

isVarArgs

```java
public boolean isVarArgs()
```

Returns

true

if this parameter represents a variable
argument list; returns

false

otherwise.

**Returns:** true

if an only if this parameter represents a
variable argument list.

---

#### isVarArgs

public boolean isVarArgs()

Returns

true

if this parameter represents a variable
argument list; returns

false

otherwise.

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

getDeclaredAnnotation

```java
public <T extends
Annotation
> T getDeclaredAnnotation​(
Class
<T> annotationClass)
```

Description copied from interface:

AnnotatedElement

Returns this element's annotation for the specified type if
such an annotation is

directly present

, else null.

This method ignores inherited annotations. (Returns null if no
annotations are directly present on this element.)

**Specified by:** getDeclaredAnnotation

in interface

AnnotatedElement
**Type Parameters:** T

- the type of the annotation to query for and return if directly present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** this element's annotation for the specified annotation type if
directly present on this element, else null
**Throws:** NullPointerException

- if the given annotation class is null

---

#### getDeclaredAnnotation

public <T extends

Annotation

> T getDeclaredAnnotation​(

Class

<T> annotationClass)

Description copied from interface:

AnnotatedElement

Returns this element's annotation for the specified type if
such an annotation is

directly present

, else null.

This method ignores inherited annotations. (Returns null if no
annotations are directly present on this element.)

getDeclaredAnnotationsByType

```java
public <T extends
Annotation
> T[] getDeclaredAnnotationsByType​(
Class
<T> annotationClass)
```

Description copied from interface:

AnnotatedElement

Returns this element's annotation(s) for the specified type if
such annotations are either

directly present

or

indirectly present

. This method ignores inherited
annotations.

If there are no specified annotations directly or indirectly
present on this element, the return value is an array of length
0.

The difference between this method and

AnnotatedElement.getDeclaredAnnotation(Class)

is that this method detects if its
argument is a

repeatable annotation type

(JLS 9.6), and if so,
attempts to find one or more annotations of that type by "looking
through" a container annotation if one is present.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.

**Specified by:** getDeclaredAnnotationsByType

in interface

AnnotatedElement
**Type Parameters:** T

- the type of the annotation to query for and return
if directly or indirectly present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** all this element's annotations for the specified annotation type if
directly or indirectly present on this element, else an array of length zero
**Throws:** NullPointerException

- if the given annotation class is null

---

#### getDeclaredAnnotationsByType

public <T extends

Annotation

> T[] getDeclaredAnnotationsByType​(

Class

<T> annotationClass)

Description copied from interface:

AnnotatedElement

Returns this element's annotation(s) for the specified type if
such annotations are either

directly present

or

indirectly present

. This method ignores inherited
annotations.

If there are no specified annotations directly or indirectly
present on this element, the return value is an array of length
0.

The difference between this method and

AnnotatedElement.getDeclaredAnnotation(Class)

is that this method detects if its
argument is a

repeatable annotation type

(JLS 9.6), and if so,
attempts to find one or more annotations of that type by "looking
through" a container annotation if one is present.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.

---

