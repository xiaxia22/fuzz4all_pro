# Interface ArrayType

**Source:** `jdk.jdi\com\sun\jdi\ArrayType.html`

### Class Description

```java
public interface
ArrayType

extends
ReferenceType
```

Provides access to the class of an array and the type of
its components in the target VM.

**All Superinterfaces:** Accessible

,

Comparable

<

ReferenceType

>

,

Mirror

,

ReferenceType

,

Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ArrayReference
newInstance​(int length)

Creates a new instance of this array class in the target VM.
The array is created with the given length and each component
is initialized to is standard default value.

**Parameters:**
- length

- the number of components in the new array

**Returns:**
- the newly created

ArrayReference

mirroring
the new object in the target VM.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### String
componentSignature()

Gets the JNI signature of the components of this
array class. The signature
describes the declared type of the components. If the components
are objects, their actual type in a particular run-time context
may be a subclass of the declared class.

**Returns:**
- a string containing the JNI signature of array components.

---

#### String
componentTypeName()

Returns a text representation of the component
type of this array.

**Returns:**
- a text representation of the component type.

---

#### Type
componentType()
throws
ClassNotLoadedException

Returns the component type of this array,
as specified in the array declaration.

Note: The component type of a array will always be
created or loaded before the array - see

The Java™ Virtual Machine Specification

,
section 5.3.3 - Creating Array Classes.
However, although the component type will be loaded it may
not yet be prepared, in which case the type will be returned
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

of this array's components.

**Throws:**
- ClassNotLoadedException

**See Also:**
- Type

,

Field.type() - for usage examples

---

### Additional Sections

#### Interface ArrayType

**All Superinterfaces:** Accessible

,

Comparable

<

ReferenceType

>

,

Mirror

,

ReferenceType

,

Type

```java
public interface
ArrayType

extends
ReferenceType
```

Provides access to the class of an array and the type of
its components in the target VM.

**Since:** 1.3
**See Also:** ArrayReference

public interface

ArrayType

extends

ReferenceType

Provides access to the class of an array and the type of
its components in the target VM.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

componentSignature

()

Gets the JNI signature of the components of this
array class.

Type

componentType

()

Returns the component type of this array,
as specified in the array declaration.

String

componentTypeName

()

Returns a text representation of the component
type of this array.

ArrayReference

newInstance

​(int length)

Creates a new instance of this array class in the target VM.

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

ReferenceType

allFields

,

allLineLocations

,

allLineLocations

,

allMethods

,

availableStrata

,

classLoader

,

classObject

,

constantPool

,

constantPoolCount

,

defaultStratum

,

equals

,

failedToInitialize

,

fieldByName

,

fields

,

genericSignature

,

getValue

,

getValues

,

hashCode

,

instances

,

isAbstract

,

isFinal

,

isInitialized

,

isPrepared

,

isStatic

,

isVerified

,

locationsOfLine

,

locationsOfLine

,

majorVersion

,

methods

,

methodsByName

,

methodsByName

,

minorVersion

,

module

,

name

,

nestedTypes

,

sourceDebugExtension

,

sourceName

,

sourceNames

,

sourcePaths

,

visibleFields

,

visibleMethods

- Methods declared in interface com.sun.jdi.

Type

signature

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

componentSignature

()

Gets the JNI signature of the components of this
array class.

Type

componentType

()

Returns the component type of this array,
as specified in the array declaration.

String

componentTypeName

()

Returns a text representation of the component
type of this array.

ArrayReference

newInstance

​(int length)

Creates a new instance of this array class in the target VM.

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

ReferenceType

allFields

,

allLineLocations

,

allLineLocations

,

allMethods

,

availableStrata

,

classLoader

,

classObject

,

constantPool

,

constantPoolCount

,

defaultStratum

,

equals

,

failedToInitialize

,

fieldByName

,

fields

,

genericSignature

,

getValue

,

getValues

,

hashCode

,

instances

,

isAbstract

,

isFinal

,

isInitialized

,

isPrepared

,

isStatic

,

isVerified

,

locationsOfLine

,

locationsOfLine

,

majorVersion

,

methods

,

methodsByName

,

methodsByName

,

minorVersion

,

module

,

name

,

nestedTypes

,

sourceDebugExtension

,

sourceName

,

sourceNames

,

sourcePaths

,

visibleFields

,

visibleMethods

- Methods declared in interface com.sun.jdi.

Type

signature

---

#### Method Summary

Gets the JNI signature of the components of this
array class.

Returns the component type of this array,
as specified in the array declaration.

Returns a text representation of the component
type of this array.

Creates a new instance of this array class in the target VM.

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

ReferenceType

allFields

,

allLineLocations

,

allLineLocations

,

allMethods

,

availableStrata

,

classLoader

,

classObject

,

constantPool

,

constantPoolCount

,

defaultStratum

,

equals

,

failedToInitialize

,

fieldByName

,

fields

,

genericSignature

,

getValue

,

getValues

,

hashCode

,

instances

,

isAbstract

,

isFinal

,

isInitialized

,

isPrepared

,

isStatic

,

isVerified

,

locationsOfLine

,

locationsOfLine

,

majorVersion

,

methods

,

methodsByName

,

methodsByName

,

minorVersion

,

module

,

name

,

nestedTypes

,

sourceDebugExtension

,

sourceName

,

sourceNames

,

sourcePaths

,

visibleFields

,

visibleMethods

---

#### Methods declared in interface com.sun.jdi. ReferenceType

Methods declared in interface com.sun.jdi.

Type

signature

---

#### Methods declared in interface com.sun.jdi. Type

============ METHOD DETAIL ==========

- Method Detail

- newInstance

```java
ArrayReference
newInstance​(int length)
```

Creates a new instance of this array class in the target VM.
The array is created with the given length and each component
is initialized to is standard default value.

**Parameters:** length

- the number of components in the new array
**Returns:** the newly created

ArrayReference

mirroring
the new object in the target VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- componentSignature

```java
String
componentSignature()
```

Gets the JNI signature of the components of this
array class. The signature
describes the declared type of the components. If the components
are objects, their actual type in a particular run-time context
may be a subclass of the declared class.

**Returns:** a string containing the JNI signature of array components.

- componentTypeName

```java
String
componentTypeName()
```

Returns a text representation of the component
type of this array.

**Returns:** a text representation of the component type.

- componentType

```java
Type
componentType()
throws
ClassNotLoadedException
```

Returns the component type of this array,
as specified in the array declaration.

Note: The component type of a array will always be
created or loaded before the array - see

The Java™ Virtual Machine Specification

,
section 5.3.3 - Creating Array Classes.
However, although the component type will be loaded it may
not yet be prepared, in which case the type will be returned
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

of this array's components.
**Throws:** ClassNotLoadedException
**See Also:** Type

,

Field.type() - for usage examples

Method Detail

- newInstance

```java
ArrayReference
newInstance​(int length)
```

Creates a new instance of this array class in the target VM.
The array is created with the given length and each component
is initialized to is standard default value.

**Parameters:** length

- the number of components in the new array
**Returns:** the newly created

ArrayReference

mirroring
the new object in the target VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- componentSignature

```java
String
componentSignature()
```

Gets the JNI signature of the components of this
array class. The signature
describes the declared type of the components. If the components
are objects, their actual type in a particular run-time context
may be a subclass of the declared class.

**Returns:** a string containing the JNI signature of array components.

- componentTypeName

```java
String
componentTypeName()
```

Returns a text representation of the component
type of this array.

**Returns:** a text representation of the component type.

- componentType

```java
Type
componentType()
throws
ClassNotLoadedException
```

Returns the component type of this array,
as specified in the array declaration.

Note: The component type of a array will always be
created or loaded before the array - see

The Java™ Virtual Machine Specification

,
section 5.3.3 - Creating Array Classes.
However, although the component type will be loaded it may
not yet be prepared, in which case the type will be returned
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

of this array's components.
**Throws:** ClassNotLoadedException
**See Also:** Type

,

Field.type() - for usage examples

---

#### Method Detail

newInstance

```java
ArrayReference
newInstance​(int length)
```

Creates a new instance of this array class in the target VM.
The array is created with the given length and each component
is initialized to is standard default value.

**Parameters:** length

- the number of components in the new array
**Returns:** the newly created

ArrayReference

mirroring
the new object in the target VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### newInstance

ArrayReference

newInstance​(int length)

Creates a new instance of this array class in the target VM.
The array is created with the given length and each component
is initialized to is standard default value.

componentSignature

```java
String
componentSignature()
```

Gets the JNI signature of the components of this
array class. The signature
describes the declared type of the components. If the components
are objects, their actual type in a particular run-time context
may be a subclass of the declared class.

**Returns:** a string containing the JNI signature of array components.

---

#### componentSignature

String

componentSignature()

Gets the JNI signature of the components of this
array class. The signature
describes the declared type of the components. If the components
are objects, their actual type in a particular run-time context
may be a subclass of the declared class.

componentTypeName

```java
String
componentTypeName()
```

Returns a text representation of the component
type of this array.

**Returns:** a text representation of the component type.

---

#### componentTypeName

String

componentTypeName()

Returns a text representation of the component
type of this array.

componentType

```java
Type
componentType()
throws
ClassNotLoadedException
```

Returns the component type of this array,
as specified in the array declaration.

Note: The component type of a array will always be
created or loaded before the array - see

The Java™ Virtual Machine Specification

,
section 5.3.3 - Creating Array Classes.
However, although the component type will be loaded it may
not yet be prepared, in which case the type will be returned
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

of this array's components.
**Throws:** ClassNotLoadedException
**See Also:** Type

,

Field.type() - for usage examples

---

#### componentType

Type

componentType()
throws

ClassNotLoadedException

Returns the component type of this array,
as specified in the array declaration.

Note: The component type of a array will always be
created or loaded before the array - see

The Java™ Virtual Machine Specification

,
section 5.3.3 - Creating Array Classes.
However, although the component type will be loaded it may
not yet be prepared, in which case the type will be returned
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

Note: The component type of a array will always be
created or loaded before the array - see

The Java™ Virtual Machine Specification

,
section 5.3.3 - Creating Array Classes.
However, although the component type will be loaded it may
not yet be prepared, in which case the type will be returned
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

---

