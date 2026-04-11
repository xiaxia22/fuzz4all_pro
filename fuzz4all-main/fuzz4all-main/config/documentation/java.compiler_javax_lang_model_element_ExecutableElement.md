# Interface ExecutableElement

**Source:** `java.compiler\javax\lang\model\element\ExecutableElement.html`

### Class Description

```java
public interface
ExecutableElement

extends
Element
,
Parameterizable
```

Represents a method, constructor, or initializer (static or
instance) of a class or interface, including annotation type
elements.

**All Superinterfaces:** AnnotatedConstruct

,

Element

,

Parameterizable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
TypeParameterElement
> getTypeParameters()

Returns the formal type parameters of this executable
in declaration order.

**Specified by:**
- getTypeParameters

in interface

Parameterizable

**Returns:**
- the formal type parameters, or an empty list
if there are none

---

#### TypeMirror
getReturnType()

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

**Returns:**
- the return type of this executable

---

#### List
<? extends
VariableElement
> getParameters()

Returns the formal parameters of this executable.
They are returned in declaration order.

**Returns:**
- the formal parameters,
or an empty list if there are none

---

#### TypeMirror
getReceiverType()

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

**Returns:**
- the receiver type of this executable

**Since:**
- 1.8

---

#### boolean isVarArgs()

Returns

true

if this method or constructor accepts a variable
number of arguments and returns

false

otherwise.

**Returns:**
- true

if this method or constructor accepts a variable
number of arguments and

false

otherwise

---

#### boolean isDefault()

Returns

true

if this method is a default method and
returns

false

otherwise.

**Returns:**
- true

if this method is a default method and

false

otherwise

**Since:**
- 1.8

---

#### List
<? extends
TypeMirror
> getThrownTypes()

Returns the exceptions and other throwables listed in this
method or constructor's

throws

clause in declaration
order.

**Returns:**
- the exceptions and other throwables listed in the

throws

clause, or an empty list if there are none

---

#### AnnotationValue
getDefaultValue()

Returns the default value if this executable is an annotation
type element. Returns

null

if this method is not an
annotation type element, or if it is an annotation type element
with no default value.

**Returns:**
- the default value, or

null

if none

---

#### Name
getSimpleName()

Returns the simple name of a constructor, method, or
initializer. For a constructor, the name

"<init>"

is
returned, for a static initializer, the name

"<clinit>"

is returned, and for an anonymous class or instance
initializer, an empty name is returned.

**Specified by:**
- getSimpleName

in interface

Element

**Returns:**
- the simple name of a constructor, method, or
initializer

**See Also:**
- PackageElement.getSimpleName()

,

getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

---

### Additional Sections

#### Interface ExecutableElement

**All Superinterfaces:** AnnotatedConstruct

,

Element

,

Parameterizable

```java
public interface
ExecutableElement

extends
Element
,
Parameterizable
```

Represents a method, constructor, or initializer (static or
instance) of a class or interface, including annotation type
elements.

**Since:** 1.6
**See Also:** ExecutableType

public interface

ExecutableElement

extends

Element

,

Parameterizable

Represents a method, constructor, or initializer (static or
instance) of a class or interface, including annotation type
elements.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AnnotationValue

getDefaultValue

()

Returns the default value if this executable is an annotation
type element.

List

<? extends

VariableElement

>

getParameters

()

Returns the formal parameters of this executable.

TypeMirror

getReceiverType

()

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

TypeMirror

getReturnType

()

Returns the return type of this executable.

Name

getSimpleName

()

Returns the simple name of a constructor, method, or
initializer.

List

<? extends

TypeMirror

>

getThrownTypes

()

Returns the exceptions and other throwables listed in this
method or constructor's

throws

clause in declaration
order.

List

<? extends

TypeParameterElement

>

getTypeParameters

()

Returns the formal type parameters of this executable
in declaration order.

boolean

isDefault

()

Returns

true

if this method is a default method and
returns

false

otherwise.

boolean

isVarArgs

()

Returns

true

if this method or constructor accepts a variable
number of arguments and returns

false

otherwise.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

- Methods declared in interface javax.lang.model.element.

Element

accept

,

asType

,

equals

,

getAnnotation

,

getAnnotationMirrors

,

getEnclosedElements

,

getEnclosingElement

,

getKind

,

getModifiers

,

hashCode

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AnnotationValue

getDefaultValue

()

Returns the default value if this executable is an annotation
type element.

List

<? extends

VariableElement

>

getParameters

()

Returns the formal parameters of this executable.

TypeMirror

getReceiverType

()

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

TypeMirror

getReturnType

()

Returns the return type of this executable.

Name

getSimpleName

()

Returns the simple name of a constructor, method, or
initializer.

List

<? extends

TypeMirror

>

getThrownTypes

()

Returns the exceptions and other throwables listed in this
method or constructor's

throws

clause in declaration
order.

List

<? extends

TypeParameterElement

>

getTypeParameters

()

Returns the formal type parameters of this executable
in declaration order.

boolean

isDefault

()

Returns

true

if this method is a default method and
returns

false

otherwise.

boolean

isVarArgs

()

Returns

true

if this method or constructor accepts a variable
number of arguments and returns

false

otherwise.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

- Methods declared in interface javax.lang.model.element.

Element

accept

,

asType

,

equals

,

getAnnotation

,

getAnnotationMirrors

,

getEnclosedElements

,

getEnclosingElement

,

getKind

,

getModifiers

,

hashCode

---

#### Method Summary

Returns the default value if this executable is an annotation
type element.

Returns the formal parameters of this executable.

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

Returns the return type of this executable.

Returns the simple name of a constructor, method, or
initializer.

Returns the exceptions and other throwables listed in this
method or constructor's

throws

clause in declaration
order.

Returns the formal type parameters of this executable
in declaration order.

Returns

true

if this method is a default method and
returns

false

otherwise.

Returns

true

if this method or constructor accepts a variable
number of arguments and returns

false

otherwise.

Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

---

#### Methods declared in interface javax.lang.model. AnnotatedConstruct

Methods declared in interface javax.lang.model.element.

Element

accept

,

asType

,

equals

,

getAnnotation

,

getAnnotationMirrors

,

getEnclosedElements

,

getEnclosingElement

,

getKind

,

getModifiers

,

hashCode

---

#### Methods declared in interface javax.lang.model.element. Element

============ METHOD DETAIL ==========

- Method Detail

- getTypeParameters

```java
List
<? extends
TypeParameterElement
> getTypeParameters()
```

Returns the formal type parameters of this executable
in declaration order.

**Specified by:** getTypeParameters

in interface

Parameterizable
**Returns:** the formal type parameters, or an empty list
if there are none

- getReturnType

```java
TypeMirror
getReturnType()
```

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

**Returns:** the return type of this executable

- getParameters

```java
List
<? extends
VariableElement
> getParameters()
```

Returns the formal parameters of this executable.
They are returned in declaration order.

**Returns:** the formal parameters,
or an empty list if there are none

- getReceiverType

```java
TypeMirror
getReceiverType()
```

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

**Returns:** the receiver type of this executable
**Since:** 1.8

- isVarArgs

```java
boolean isVarArgs()
```

Returns

true

if this method or constructor accepts a variable
number of arguments and returns

false

otherwise.

**Returns:** true

if this method or constructor accepts a variable
number of arguments and

false

otherwise

- isDefault

```java
boolean isDefault()
```

Returns

true

if this method is a default method and
returns

false

otherwise.

**Returns:** true

if this method is a default method and

false

otherwise
**Since:** 1.8

- getThrownTypes

```java
List
<? extends
TypeMirror
> getThrownTypes()
```

Returns the exceptions and other throwables listed in this
method or constructor's

throws

clause in declaration
order.

**Returns:** the exceptions and other throwables listed in the

throws

clause, or an empty list if there are none

- getDefaultValue

```java
AnnotationValue
getDefaultValue()
```

Returns the default value if this executable is an annotation
type element. Returns

null

if this method is not an
annotation type element, or if it is an annotation type element
with no default value.

**Returns:** the default value, or

null

if none

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of a constructor, method, or
initializer. For a constructor, the name

"<init>"

is
returned, for a static initializer, the name

"<clinit>"

is returned, and for an anonymous class or instance
initializer, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**Returns:** the simple name of a constructor, method, or
initializer
**See Also:** PackageElement.getSimpleName()

,

getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

Method Detail

- getTypeParameters

```java
List
<? extends
TypeParameterElement
> getTypeParameters()
```

Returns the formal type parameters of this executable
in declaration order.

**Specified by:** getTypeParameters

in interface

Parameterizable
**Returns:** the formal type parameters, or an empty list
if there are none

- getReturnType

```java
TypeMirror
getReturnType()
```

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

**Returns:** the return type of this executable

- getParameters

```java
List
<? extends
VariableElement
> getParameters()
```

Returns the formal parameters of this executable.
They are returned in declaration order.

**Returns:** the formal parameters,
or an empty list if there are none

- getReceiverType

```java
TypeMirror
getReceiverType()
```

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

**Returns:** the receiver type of this executable
**Since:** 1.8

- isVarArgs

```java
boolean isVarArgs()
```

Returns

true

if this method or constructor accepts a variable
number of arguments and returns

false

otherwise.

**Returns:** true

if this method or constructor accepts a variable
number of arguments and

false

otherwise

- isDefault

```java
boolean isDefault()
```

Returns

true

if this method is a default method and
returns

false

otherwise.

**Returns:** true

if this method is a default method and

false

otherwise
**Since:** 1.8

- getThrownTypes

```java
List
<? extends
TypeMirror
> getThrownTypes()
```

Returns the exceptions and other throwables listed in this
method or constructor's

throws

clause in declaration
order.

**Returns:** the exceptions and other throwables listed in the

throws

clause, or an empty list if there are none

- getDefaultValue

```java
AnnotationValue
getDefaultValue()
```

Returns the default value if this executable is an annotation
type element. Returns

null

if this method is not an
annotation type element, or if it is an annotation type element
with no default value.

**Returns:** the default value, or

null

if none

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of a constructor, method, or
initializer. For a constructor, the name

"<init>"

is
returned, for a static initializer, the name

"<clinit>"

is returned, and for an anonymous class or instance
initializer, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**Returns:** the simple name of a constructor, method, or
initializer
**See Also:** PackageElement.getSimpleName()

,

getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

---

#### Method Detail

getTypeParameters

```java
List
<? extends
TypeParameterElement
> getTypeParameters()
```

Returns the formal type parameters of this executable
in declaration order.

**Specified by:** getTypeParameters

in interface

Parameterizable
**Returns:** the formal type parameters, or an empty list
if there are none

---

#### getTypeParameters

List

<? extends

TypeParameterElement

> getTypeParameters()

Returns the formal type parameters of this executable
in declaration order.

getReturnType

```java
TypeMirror
getReturnType()
```

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

**Returns:** the return type of this executable

---

#### getReturnType

TypeMirror

getReturnType()

Returns the return type of this executable.
Returns a

NoType

with kind

VOID

if this executable is not a method, or is a method that does not
return a value.

getParameters

```java
List
<? extends
VariableElement
> getParameters()
```

Returns the formal parameters of this executable.
They are returned in declaration order.

**Returns:** the formal parameters,
or an empty list if there are none

---

#### getParameters

List

<? extends

VariableElement

> getParameters()

Returns the formal parameters of this executable.
They are returned in declaration order.

getReceiverType

```java
TypeMirror
getReceiverType()
```

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

**Returns:** the receiver type of this executable
**Since:** 1.8

---

#### getReceiverType

TypeMirror

getReceiverType()

Returns the receiver type of this executable,
or

NoType

with
kind

NONE

if the executable has no receiver type.

An executable which is an instance method, or a constructor of an
inner class, has a receiver type derived from the

declaring type

.

An executable which is a static method, or a constructor of a
non-inner class, or an initializer (static or instance), has no
receiver type.

isVarArgs

```java
boolean isVarArgs()
```

Returns

true

if this method or constructor accepts a variable
number of arguments and returns

false

otherwise.

**Returns:** true

if this method or constructor accepts a variable
number of arguments and

false

otherwise

---

#### isVarArgs

boolean isVarArgs()

Returns

true

if this method or constructor accepts a variable
number of arguments and returns

false

otherwise.

isDefault

```java
boolean isDefault()
```

Returns

true

if this method is a default method and
returns

false

otherwise.

**Returns:** true

if this method is a default method and

false

otherwise
**Since:** 1.8

---

#### isDefault

boolean isDefault()

Returns

true

if this method is a default method and
returns

false

otherwise.

getThrownTypes

```java
List
<? extends
TypeMirror
> getThrownTypes()
```

Returns the exceptions and other throwables listed in this
method or constructor's

throws

clause in declaration
order.

**Returns:** the exceptions and other throwables listed in the

throws

clause, or an empty list if there are none

---

#### getThrownTypes

List

<? extends

TypeMirror

> getThrownTypes()

Returns the exceptions and other throwables listed in this
method or constructor's

throws

clause in declaration
order.

getDefaultValue

```java
AnnotationValue
getDefaultValue()
```

Returns the default value if this executable is an annotation
type element. Returns

null

if this method is not an
annotation type element, or if it is an annotation type element
with no default value.

**Returns:** the default value, or

null

if none

---

#### getDefaultValue

AnnotationValue

getDefaultValue()

Returns the default value if this executable is an annotation
type element. Returns

null

if this method is not an
annotation type element, or if it is an annotation type element
with no default value.

getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of a constructor, method, or
initializer. For a constructor, the name

"<init>"

is
returned, for a static initializer, the name

"<clinit>"

is returned, and for an anonymous class or instance
initializer, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**Returns:** the simple name of a constructor, method, or
initializer
**See Also:** PackageElement.getSimpleName()

,

getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

---

#### getSimpleName

Name

getSimpleName()

Returns the simple name of a constructor, method, or
initializer. For a constructor, the name

"<init>"

is
returned, for a static initializer, the name

"<clinit>"

is returned, and for an anonymous class or instance
initializer, an empty name is returned.

---

