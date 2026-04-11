# Enum ElementKind

**Source:** `java.compiler\javax\lang\model\element\ElementKind.html`

### Class Description

```java
public enum
ElementKind

extends
Enum
<
ElementKind
>
```

The

kind

of an element.

Note that it is possible additional element kinds will be added
to accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

**All Implemented Interfaces:** Serializable

,

Comparable

<

ElementKind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ElementKind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementKind c : ElementKind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
ElementKind
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

#### public boolean isClass()

Returns

true

if this is a kind of class:
either

CLASS

or

ENUM

.

**Returns:**
- true

if this is a kind of class

---

#### public boolean isInterface()

Returns

true

if this is a kind of interface:
either

INTERFACE

or

ANNOTATION_TYPE

.

**Returns:**
- true

if this is a kind of interface

---

#### public boolean isField()

Returns

true

if this is a kind of field:
either

FIELD

or

ENUM_CONSTANT

.

**Returns:**
- true

if this is a kind of field

---

### Additional Sections

#### Enum ElementKind

java.lang.Object

- java.lang.Enum

<

ElementKind

>
- - javax.lang.model.element.ElementKind

java.lang.Enum

<

ElementKind

>

- javax.lang.model.element.ElementKind

javax.lang.model.element.ElementKind

**All Implemented Interfaces:** Serializable

,

Comparable

<

ElementKind

>

```java
public enum
ElementKind

extends
Enum
<
ElementKind
>
```

The

kind

of an element.

Note that it is possible additional element kinds will be added
to accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

**Since:** 1.6
**See Also:** Element

public enum

ElementKind

extends

Enum

<

ElementKind

>

The

kind

of an element.

Note that it is possible additional element kinds will be added
to accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

Note that it is possible additional element kinds will be added
to accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ANNOTATION_TYPE

An annotation type.

CLASS

A class not described by a more specific kind (like

ENUM

).

CONSTRUCTOR

A constructor.

ENUM

An enum type.

ENUM_CONSTANT

An enum constant.

EXCEPTION_PARAMETER

A parameter of an exception handler.

FIELD

A field not described by a more specific kind (like

ENUM_CONSTANT

).

INSTANCE_INIT

An instance initializer.

INTERFACE

An interface not described by a more specific kind (like

ANNOTATION_TYPE

).

LOCAL_VARIABLE

A local variable.

METHOD

A method.

MODULE

A module.

OTHER

An implementation-reserved element.

PACKAGE

A package.

PARAMETER

A parameter of a method or constructor.

RESOURCE_VARIABLE

A resource variable.

STATIC_INIT

A static initializer.

TYPE_PARAMETER

A type parameter.

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

isClass

()

Returns

true

if this is a kind of class:
either

CLASS

or

ENUM

.

boolean

isField

()

Returns

true

if this is a kind of field:
either

FIELD

or

ENUM_CONSTANT

.

boolean

isInterface

()

Returns

true

if this is a kind of interface:
either

INTERFACE

or

ANNOTATION_TYPE

.

static

ElementKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ElementKind

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

ANNOTATION_TYPE

An annotation type.

CLASS

A class not described by a more specific kind (like

ENUM

).

CONSTRUCTOR

A constructor.

ENUM

An enum type.

ENUM_CONSTANT

An enum constant.

EXCEPTION_PARAMETER

A parameter of an exception handler.

FIELD

A field not described by a more specific kind (like

ENUM_CONSTANT

).

INSTANCE_INIT

An instance initializer.

INTERFACE

An interface not described by a more specific kind (like

ANNOTATION_TYPE

).

LOCAL_VARIABLE

A local variable.

METHOD

A method.

MODULE

A module.

OTHER

An implementation-reserved element.

PACKAGE

A package.

PARAMETER

A parameter of a method or constructor.

RESOURCE_VARIABLE

A resource variable.

STATIC_INIT

A static initializer.

TYPE_PARAMETER

A type parameter.

---

#### Enum Constant Summary

An annotation type.

A class not described by a more specific kind (like

ENUM

).

A constructor.

An enum type.

An enum constant.

A parameter of an exception handler.

A field not described by a more specific kind (like

ENUM_CONSTANT

).

An instance initializer.

An interface not described by a more specific kind (like

ANNOTATION_TYPE

).

A local variable.

A method.

A module.

An implementation-reserved element.

A package.

A parameter of a method or constructor.

A resource variable.

A static initializer.

A type parameter.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isClass

()

Returns

true

if this is a kind of class:
either

CLASS

or

ENUM

.

boolean

isField

()

Returns

true

if this is a kind of field:
either

FIELD

or

ENUM_CONSTANT

.

boolean

isInterface

()

Returns

true

if this is a kind of interface:
either

INTERFACE

or

ANNOTATION_TYPE

.

static

ElementKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

ElementKind

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

if this is a kind of class:
either

CLASS

or

ENUM

.

Returns

true

if this is a kind of field:
either

FIELD

or

ENUM_CONSTANT

.

Returns

true

if this is a kind of interface:
either

INTERFACE

or

ANNOTATION_TYPE

.

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

- PACKAGE

```java
public static final
ElementKind
PACKAGE
```

A package.

- ENUM

```java
public static final
ElementKind
ENUM
```

An enum type.

- CLASS

```java
public static final
ElementKind
CLASS
```

A class not described by a more specific kind (like

ENUM

).

- ANNOTATION_TYPE

```java
public static final
ElementKind
ANNOTATION_TYPE
```

An annotation type.

- INTERFACE

```java
public static final
ElementKind
INTERFACE
```

An interface not described by a more specific kind (like

ANNOTATION_TYPE

).

- ENUM_CONSTANT

```java
public static final
ElementKind
ENUM_CONSTANT
```

An enum constant.

- FIELD

```java
public static final
ElementKind
FIELD
```

A field not described by a more specific kind (like

ENUM_CONSTANT

).

- PARAMETER

```java
public static final
ElementKind
PARAMETER
```

A parameter of a method or constructor.

- LOCAL_VARIABLE

```java
public static final
ElementKind
LOCAL_VARIABLE
```

A local variable.

- EXCEPTION_PARAMETER

```java
public static final
ElementKind
EXCEPTION_PARAMETER
```

A parameter of an exception handler.

- METHOD

```java
public static final
ElementKind
METHOD
```

A method.

- CONSTRUCTOR

```java
public static final
ElementKind
CONSTRUCTOR
```

A constructor.

- STATIC_INIT

```java
public static final
ElementKind
STATIC_INIT
```

A static initializer.

- INSTANCE_INIT

```java
public static final
ElementKind
INSTANCE_INIT
```

An instance initializer.

- TYPE_PARAMETER

```java
public static final
ElementKind
TYPE_PARAMETER
```

A type parameter.

- OTHER

```java
public static final
ElementKind
OTHER
```

An implementation-reserved element. This is not the element
you are looking for.

- RESOURCE_VARIABLE

```java
public static final
ElementKind
RESOURCE_VARIABLE
```

A resource variable.

**Since:** 1.7

- MODULE

```java
public static final
ElementKind
MODULE
```

A module.

**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
ElementKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementKind c : ElementKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ElementKind
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

- isClass

```java
public boolean isClass()
```

Returns

true

if this is a kind of class:
either

CLASS

or

ENUM

.

**Returns:** true

if this is a kind of class

- isInterface

```java
public boolean isInterface()
```

Returns

true

if this is a kind of interface:
either

INTERFACE

or

ANNOTATION_TYPE

.

**Returns:** true

if this is a kind of interface

- isField

```java
public boolean isField()
```

Returns

true

if this is a kind of field:
either

FIELD

or

ENUM_CONSTANT

.

**Returns:** true

if this is a kind of field

Enum Constant Detail

- PACKAGE

```java
public static final
ElementKind
PACKAGE
```

A package.

- ENUM

```java
public static final
ElementKind
ENUM
```

An enum type.

- CLASS

```java
public static final
ElementKind
CLASS
```

A class not described by a more specific kind (like

ENUM

).

- ANNOTATION_TYPE

```java
public static final
ElementKind
ANNOTATION_TYPE
```

An annotation type.

- INTERFACE

```java
public static final
ElementKind
INTERFACE
```

An interface not described by a more specific kind (like

ANNOTATION_TYPE

).

- ENUM_CONSTANT

```java
public static final
ElementKind
ENUM_CONSTANT
```

An enum constant.

- FIELD

```java
public static final
ElementKind
FIELD
```

A field not described by a more specific kind (like

ENUM_CONSTANT

).

- PARAMETER

```java
public static final
ElementKind
PARAMETER
```

A parameter of a method or constructor.

- LOCAL_VARIABLE

```java
public static final
ElementKind
LOCAL_VARIABLE
```

A local variable.

- EXCEPTION_PARAMETER

```java
public static final
ElementKind
EXCEPTION_PARAMETER
```

A parameter of an exception handler.

- METHOD

```java
public static final
ElementKind
METHOD
```

A method.

- CONSTRUCTOR

```java
public static final
ElementKind
CONSTRUCTOR
```

A constructor.

- STATIC_INIT

```java
public static final
ElementKind
STATIC_INIT
```

A static initializer.

- INSTANCE_INIT

```java
public static final
ElementKind
INSTANCE_INIT
```

An instance initializer.

- TYPE_PARAMETER

```java
public static final
ElementKind
TYPE_PARAMETER
```

A type parameter.

- OTHER

```java
public static final
ElementKind
OTHER
```

An implementation-reserved element. This is not the element
you are looking for.

- RESOURCE_VARIABLE

```java
public static final
ElementKind
RESOURCE_VARIABLE
```

A resource variable.

**Since:** 1.7

- MODULE

```java
public static final
ElementKind
MODULE
```

A module.

**Since:** 9

---

#### Enum Constant Detail

PACKAGE

```java
public static final
ElementKind
PACKAGE
```

A package.

---

#### PACKAGE

public static final

ElementKind

PACKAGE

A package.

ENUM

```java
public static final
ElementKind
ENUM
```

An enum type.

---

#### ENUM

public static final

ElementKind

ENUM

An enum type.

CLASS

```java
public static final
ElementKind
CLASS
```

A class not described by a more specific kind (like

ENUM

).

---

#### CLASS

public static final

ElementKind

CLASS

A class not described by a more specific kind (like

ENUM

).

ANNOTATION_TYPE

```java
public static final
ElementKind
ANNOTATION_TYPE
```

An annotation type.

---

#### ANNOTATION_TYPE

public static final

ElementKind

ANNOTATION_TYPE

An annotation type.

INTERFACE

```java
public static final
ElementKind
INTERFACE
```

An interface not described by a more specific kind (like

ANNOTATION_TYPE

).

---

#### INTERFACE

public static final

ElementKind

INTERFACE

An interface not described by a more specific kind (like

ANNOTATION_TYPE

).

ENUM_CONSTANT

```java
public static final
ElementKind
ENUM_CONSTANT
```

An enum constant.

---

#### ENUM_CONSTANT

public static final

ElementKind

ENUM_CONSTANT

An enum constant.

FIELD

```java
public static final
ElementKind
FIELD
```

A field not described by a more specific kind (like

ENUM_CONSTANT

).

---

#### FIELD

public static final

ElementKind

FIELD

A field not described by a more specific kind (like

ENUM_CONSTANT

).

PARAMETER

```java
public static final
ElementKind
PARAMETER
```

A parameter of a method or constructor.

---

#### PARAMETER

public static final

ElementKind

PARAMETER

A parameter of a method or constructor.

LOCAL_VARIABLE

```java
public static final
ElementKind
LOCAL_VARIABLE
```

A local variable.

---

#### LOCAL_VARIABLE

public static final

ElementKind

LOCAL_VARIABLE

A local variable.

EXCEPTION_PARAMETER

```java
public static final
ElementKind
EXCEPTION_PARAMETER
```

A parameter of an exception handler.

---

#### EXCEPTION_PARAMETER

public static final

ElementKind

EXCEPTION_PARAMETER

A parameter of an exception handler.

METHOD

```java
public static final
ElementKind
METHOD
```

A method.

---

#### METHOD

public static final

ElementKind

METHOD

A method.

CONSTRUCTOR

```java
public static final
ElementKind
CONSTRUCTOR
```

A constructor.

---

#### CONSTRUCTOR

public static final

ElementKind

CONSTRUCTOR

A constructor.

STATIC_INIT

```java
public static final
ElementKind
STATIC_INIT
```

A static initializer.

---

#### STATIC_INIT

public static final

ElementKind

STATIC_INIT

A static initializer.

INSTANCE_INIT

```java
public static final
ElementKind
INSTANCE_INIT
```

An instance initializer.

---

#### INSTANCE_INIT

public static final

ElementKind

INSTANCE_INIT

An instance initializer.

TYPE_PARAMETER

```java
public static final
ElementKind
TYPE_PARAMETER
```

A type parameter.

---

#### TYPE_PARAMETER

public static final

ElementKind

TYPE_PARAMETER

A type parameter.

OTHER

```java
public static final
ElementKind
OTHER
```

An implementation-reserved element. This is not the element
you are looking for.

---

#### OTHER

public static final

ElementKind

OTHER

An implementation-reserved element. This is not the element
you are looking for.

RESOURCE_VARIABLE

```java
public static final
ElementKind
RESOURCE_VARIABLE
```

A resource variable.

**Since:** 1.7

---

#### RESOURCE_VARIABLE

public static final

ElementKind

RESOURCE_VARIABLE

A resource variable.

MODULE

```java
public static final
ElementKind
MODULE
```

A module.

**Since:** 9

---

#### MODULE

public static final

ElementKind

MODULE

A module.

Method Detail

- values

```java
public static
ElementKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementKind c : ElementKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
ElementKind
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

- isClass

```java
public boolean isClass()
```

Returns

true

if this is a kind of class:
either

CLASS

or

ENUM

.

**Returns:** true

if this is a kind of class

- isInterface

```java
public boolean isInterface()
```

Returns

true

if this is a kind of interface:
either

INTERFACE

or

ANNOTATION_TYPE

.

**Returns:** true

if this is a kind of interface

- isField

```java
public boolean isField()
```

Returns

true

if this is a kind of field:
either

FIELD

or

ENUM_CONSTANT

.

**Returns:** true

if this is a kind of field

---

#### Method Detail

values

```java
public static
ElementKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementKind c : ElementKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

ElementKind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (ElementKind c : ElementKind.values())
System.out.println(c);
```

for (ElementKind c : ElementKind.values())
System.out.println(c);

valueOf

```java
public static
ElementKind
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

ElementKind

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

isClass

```java
public boolean isClass()
```

Returns

true

if this is a kind of class:
either

CLASS

or

ENUM

.

**Returns:** true

if this is a kind of class

---

#### isClass

public boolean isClass()

Returns

true

if this is a kind of class:
either

CLASS

or

ENUM

.

isInterface

```java
public boolean isInterface()
```

Returns

true

if this is a kind of interface:
either

INTERFACE

or

ANNOTATION_TYPE

.

**Returns:** true

if this is a kind of interface

---

#### isInterface

public boolean isInterface()

Returns

true

if this is a kind of interface:
either

INTERFACE

or

ANNOTATION_TYPE

.

isField

```java
public boolean isField()
```

Returns

true

if this is a kind of field:
either

FIELD

or

ENUM_CONSTANT

.

**Returns:** true

if this is a kind of field

---

#### isField

public boolean isField()

Returns

true

if this is a kind of field:
either

FIELD

or

ENUM_CONSTANT

.

---

