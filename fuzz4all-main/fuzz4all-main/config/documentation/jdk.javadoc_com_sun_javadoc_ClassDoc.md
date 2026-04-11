# Interface ClassDoc

**Source:** `jdk.javadoc\com\sun\javadoc\ClassDoc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ClassDoc

extends
ProgramElementDoc
,
Type
```

Represents a java class or interface and provides access to
information about the class, the class's comment and tags, and the
members of the class. A ClassDoc only exists if it was
processed in this run of javadoc. References to classes
which may or may not have been processed in this run are
referred to using Type (which can be converted to ClassDoc,
if possible).

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

ProgramElementDoc

,

Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isAbstract()

Return true if this class is abstract. Return true
for all interfaces.

**Returns:**
- true if this class is abstract. Return true
for all interfaces.

---

#### boolean isSerializable()

Return true if this class implements or interface extends

java.io.Serializable

.

Since

java.io.Externalizable

extends

java.io.Serializable

,
Externalizable objects are also Serializable.

**Returns:**
- true if this class implements or interface extends

java.io.Serializable

.

---

#### boolean isExternalizable()

Return true if this class implements or interface extends

java.io.Externalizable

.

**Returns:**
- true if this class implements or interface extends

java.io.Externalizable

.

---

#### MethodDoc
[] serializationMethods()

Return the serialization methods for this class or
interface.

**Returns:**
- an array of MethodDoc objects that represents
the serialization methods for this class or interface.

---

#### FieldDoc
[] serializableFields()

Return the Serializable fields of this class or interface.

Return either a list of default fields documented by

serial

tag

or return a single

FieldDoc

for

serialPersistentField

member.
There should be a

serialField

tag for
each Serializable field defined by an

ObjectStreamField

array component of

serialPersistentField

.

**Returns:**
- an array of

FieldDoc

objects for the Serializable
fields of this class or interface.

**See Also:**
- definesSerializableFields()

,

SerialFieldTag

---

#### boolean definesSerializableFields()

Return true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.

**Returns:**
- true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.

**See Also:**
- serializableFields()

,

SerialFieldTag

---

#### ClassDoc
superclass()

Return the superclass of this class. Return null if this is an
interface.

This method cannot accommodate certain generic type constructs.
The

superclassType

method should be used instead.

**Returns:**
- the ClassDoc for the superclass of this class, null if
there is no superclass.

**See Also:**
- superclassType()

---

#### Type
superclassType()

Return the superclass of this class. Return null if this is an
interface. A superclass is represented by either a

ClassDoc

or a

ParametrizedType

.

**Returns:**
- the superclass of this class, or null if there is no superclass.

**Since:**
- 1.5

---

#### boolean subclassOf​(
ClassDoc
cd)

Test whether this class is a subclass of the specified class.
If this is an interface, return false for all classes except

java.lang.Object

(we must keep this unexpected
behavior for compatibility reasons).

**Parameters:**
- cd

- the candidate superclass.

**Returns:**
- true if cd is a superclass of this class.

---

#### ClassDoc
[] interfaces()

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

This method cannot accommodate certain generic type constructs.
The

interfaceTypes

method should be used instead.

**Returns:**
- an array of ClassDoc objects representing the interfaces.

**See Also:**
- interfaceTypes()

---

#### Type
[] interfaceTypes()

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

**Returns:**
- an array of interfaces, each represented by a

ClassDoc

or a

ParametrizedType

.

**Since:**
- 1.5

---

#### TypeVariable
[] typeParameters()

Return the formal type parameters of this class or interface.
Return an empty array if there are none.

**Returns:**
- the formal type parameters of this class or interface.

**Since:**
- 1.5

---

#### ParamTag
[] typeParamTags()

Return the type parameter tags of this class or interface.
Return an empty array if there are none.

**Returns:**
- the type parameter tags of this class or interface.

**Since:**
- 1.5

---

#### FieldDoc
[] fields()

Return

included

fields in this class or interface.
Excludes enum constants if this is an enum type.

**Returns:**
- an array of FieldDoc objects representing the included
fields in this class or interface.

---

#### FieldDoc
[] fields​(boolean filter)

Return fields in this class or interface, filtered to the specified

access
modifier option

.
Excludes enum constants if this is an enum type.

**Parameters:**
- filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all fields regardless of
access modifier option.

**Returns:**
- an array of FieldDoc objects representing the included
fields in this class or interface.

---

#### FieldDoc
[] enumConstants()

Return the enum constants if this is an enum type.
Return an empty array if there are no enum constants, or if
this is not an enum type.

**Returns:**
- the enum constants if this is an enum type.

---

#### MethodDoc
[] methods()

Return

included

methods in this class or interface.
Same as

methods(true)

.

**Returns:**
- an array of MethodDoc objects representing the included
methods in this class or interface. Does not include
constructors or annotation type elements.

---

#### MethodDoc
[] methods​(boolean filter)

Return methods in this class or interface, filtered to the specified

access
modifier option

. Does not include constructors or annotation
type elements.

**Parameters:**
- filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all methods regardless of
access modifier option.

**Returns:**
- an array of MethodDoc objects representing the included
methods in this class or interface.

---

#### ConstructorDoc
[] constructors()

Return

included

constructors in this class. An array containing the default
no-arg constructor is returned if no other constructors exist.
Return empty array if this is an interface.

**Returns:**
- an array of ConstructorDoc objects representing the included
constructors in this class.

---

#### ConstructorDoc
[] constructors​(boolean filter)

Return constructors in this class, filtered to the specified

access
modifier option

. Return an array containing the default
no-arg constructor if no other constructors exist.

**Parameters:**
- filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all constructors regardless of
access modifier option.

**Returns:**
- an array of ConstructorDoc objects representing the included
constructors in this class.

---

#### ClassDoc
[] innerClasses()

Return

included

nested classes and interfaces within this class or interface.
This includes both static and non-static nested classes.
(This method should have been named

nestedClasses()

,
as inner classes are technically non-static.) Anonymous and local classes
or interfaces are not included.

**Returns:**
- an array of ClassDoc objects representing the included classes
and interfaces defined in this class or interface.

---

#### ClassDoc
[] innerClasses​(boolean filter)

Return nested classes and interfaces within this class or interface
filtered to the specified

access
modifier option

.
This includes both static and non-static nested classes.
Anonymous and local classes are not included.

**Parameters:**
- filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all nested classes regardless of
access modifier option.

**Returns:**
- a filtered array of ClassDoc objects representing the included
classes and interfaces defined in this class or interface.

---

#### ClassDoc
findClass​(
String
className)

Find the specified class or interface within the context of this class doc.
Search order: 1) qualified name, 2) nested in this class or interface,
3) in this package, 4) in the class imports, 5) in the package imports.
Return the ClassDoc if found, null if not found.

**Parameters:**
- className

- Specify the class name to find as a String.

**Returns:**
- the ClassDoc if found, null if not found.

---

#### @Deprecated
(
since
="9",

forRemoval
=true)

ClassDoc
[] importedClasses()

Get the list of classes and interfaces declared as imported.
These are called "single-type-import declarations" in

The Java™ Language Specification

.

**Returns:**
- an array of ClassDoc representing the imported classes.

---

#### @Deprecated
(
since
="9",

forRemoval
=true)

PackageDoc
[] importedPackages()

Get the list of packages declared as imported.
These are called "type-import-on-demand declarations" in

The Java™ Language Specification

.

**Returns:**
- an array of PackageDoc representing the imported packages.

---

### Additional Sections

#### Interface ClassDoc

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

ProgramElementDoc

,

Type

**All Known Subinterfaces:** AnnotationTypeDoc

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ClassDoc

extends
ProgramElementDoc
,
Type
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a java class or interface and provides access to
information about the class, the class's comment and tags, and the
members of the class. A ClassDoc only exists if it was
processed in this run of javadoc. References to classes
which may or may not have been processed in this run are
referred to using Type (which can be converted to ClassDoc,
if possible).

**Since:** 1.2
**See Also:** Type

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

ClassDoc

extends

ProgramElementDoc

,

Type

Represents a java class or interface and provides access to
information about the class, the class's comment and tags, and the
members of the class. A ClassDoc only exists if it was
processed in this run of javadoc. References to classes
which may or may not have been processed in this run are
referred to using Type (which can be converted to ClassDoc,
if possible).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ConstructorDoc

[]

constructors

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

constructors in this class.

ConstructorDoc

[]

constructors

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Return constructors in this class, filtered to the specified

access
modifier option

.

boolean

definesSerializableFields

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.

FieldDoc

[]

enumConstants

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the enum constants if this is an enum type.

FieldDoc

[]

fields

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

fields in this class or interface.

FieldDoc

[]

fields

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Return fields in this class or interface, filtered to the specified

access
modifier option

.

ClassDoc

findClass

​(

String

className)

Deprecated, for removal: This API element is subject to removal in a future version.

Find the specified class or interface within the context of this class doc.

ClassDoc

[]

importedClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here.

PackageDoc

[]

importedPackages

()

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here.

ClassDoc

[]

innerClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

nested classes and interfaces within this class or interface.

ClassDoc

[]

innerClasses

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Return nested classes and interfaces within this class or interface
filtered to the specified

access
modifier option

.

ClassDoc

[]

interfaces

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface.

Type

[]

interfaceTypes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface.

boolean

isAbstract

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class is abstract.

boolean

isExternalizable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Externalizable

.

boolean

isSerializable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Serializable

.

MethodDoc

[]

methods

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

methods in this class or interface.

MethodDoc

[]

methods

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Return methods in this class or interface, filtered to the specified

access
modifier option

.

FieldDoc

[]

serializableFields

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the Serializable fields of this class or interface.

MethodDoc

[]

serializationMethods

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialization methods for this class or
interface.

boolean

subclassOf

​(

ClassDoc

cd)

Deprecated, for removal: This API element is subject to removal in a future version.

Test whether this class is a subclass of the specified class.

ClassDoc

superclass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class.

Type

superclassType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class.

TypeVariable

[]

typeParameters

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this class or interface.

ParamTag

[]

typeParamTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags of this class or interface.

- Methods declared in interface com.sun.javadoc.

Doc

commentText

,

compareTo

,

firstSentenceTags

,

getRawCommentText

,

inlineTags

,

isAnnotationType

,

isAnnotationTypeElement

,

isClass

,

isConstructor

,

isEnum

,

isEnumConstant

,

isError

,

isException

,

isField

,

isIncluded

,

isInterface

,

isMethod

,

isOrdinaryClass

,

name

,

position

,

seeTags

,

setRawCommentText

,

tags

,

tags

- Methods declared in interface com.sun.javadoc.

ProgramElementDoc

annotations

,

containingClass

,

containingPackage

,

isFinal

,

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

isStatic

,

modifiers

,

modifierSpecifier

,

qualifiedName

- Methods declared in interface com.sun.javadoc.

Type

asAnnotatedType

,

asAnnotationTypeDoc

,

asClassDoc

,

asParameterizedType

,

asTypeVariable

,

asWildcardType

,

dimension

,

getElementType

,

isPrimitive

,

qualifiedTypeName

,

simpleTypeName

,

toString

,

typeName

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ConstructorDoc

[]

constructors

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

constructors in this class.

ConstructorDoc

[]

constructors

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Return constructors in this class, filtered to the specified

access
modifier option

.

boolean

definesSerializableFields

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.

FieldDoc

[]

enumConstants

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the enum constants if this is an enum type.

FieldDoc

[]

fields

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

fields in this class or interface.

FieldDoc

[]

fields

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Return fields in this class or interface, filtered to the specified

access
modifier option

.

ClassDoc

findClass

​(

String

className)

Deprecated, for removal: This API element is subject to removal in a future version.

Find the specified class or interface within the context of this class doc.

ClassDoc

[]

importedClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here.

PackageDoc

[]

importedPackages

()

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here.

ClassDoc

[]

innerClasses

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

nested classes and interfaces within this class or interface.

ClassDoc

[]

innerClasses

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Return nested classes and interfaces within this class or interface
filtered to the specified

access
modifier option

.

ClassDoc

[]

interfaces

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface.

Type

[]

interfaceTypes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface.

boolean

isAbstract

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class is abstract.

boolean

isExternalizable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Externalizable

.

boolean

isSerializable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Serializable

.

MethodDoc

[]

methods

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

methods in this class or interface.

MethodDoc

[]

methods

​(boolean filter)

Deprecated, for removal: This API element is subject to removal in a future version.

Return methods in this class or interface, filtered to the specified

access
modifier option

.

FieldDoc

[]

serializableFields

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the Serializable fields of this class or interface.

MethodDoc

[]

serializationMethods

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialization methods for this class or
interface.

boolean

subclassOf

​(

ClassDoc

cd)

Deprecated, for removal: This API element is subject to removal in a future version.

Test whether this class is a subclass of the specified class.

ClassDoc

superclass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class.

Type

superclassType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class.

TypeVariable

[]

typeParameters

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this class or interface.

ParamTag

[]

typeParamTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags of this class or interface.

- Methods declared in interface com.sun.javadoc.

Doc

commentText

,

compareTo

,

firstSentenceTags

,

getRawCommentText

,

inlineTags

,

isAnnotationType

,

isAnnotationTypeElement

,

isClass

,

isConstructor

,

isEnum

,

isEnumConstant

,

isError

,

isException

,

isField

,

isIncluded

,

isInterface

,

isMethod

,

isOrdinaryClass

,

name

,

position

,

seeTags

,

setRawCommentText

,

tags

,

tags

- Methods declared in interface com.sun.javadoc.

ProgramElementDoc

annotations

,

containingClass

,

containingPackage

,

isFinal

,

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

isStatic

,

modifiers

,

modifierSpecifier

,

qualifiedName

- Methods declared in interface com.sun.javadoc.

Type

asAnnotatedType

,

asAnnotationTypeDoc

,

asClassDoc

,

asParameterizedType

,

asTypeVariable

,

asWildcardType

,

dimension

,

getElementType

,

isPrimitive

,

qualifiedTypeName

,

simpleTypeName

,

toString

,

typeName

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

constructors in this class.

Return constructors in this class, filtered to the specified

access
modifier option

.

Return true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.

Return the enum constants if this is an enum type.

Return

included

fields in this class or interface.

Return fields in this class or interface, filtered to the specified

access
modifier option

.

Find the specified class or interface within the context of this class doc.

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here.

Return

included

nested classes and interfaces within this class or interface.

Return nested classes and interfaces within this class or interface
filtered to the specified

access
modifier option

.

Return interfaces implemented by this class or interfaces extended
by this interface.

Return true if this class is abstract.

Return true if this class implements or interface extends

java.io.Externalizable

.

Return true if this class implements or interface extends

java.io.Serializable

.

Return

included

methods in this class or interface.

Return methods in this class or interface, filtered to the specified

access
modifier option

.

Return the Serializable fields of this class or interface.

Return the serialization methods for this class or
interface.

Test whether this class is a subclass of the specified class.

Return the superclass of this class.

Return the formal type parameters of this class or interface.

Return the type parameter tags of this class or interface.

Methods declared in interface com.sun.javadoc.

Doc

commentText

,

compareTo

,

firstSentenceTags

,

getRawCommentText

,

inlineTags

,

isAnnotationType

,

isAnnotationTypeElement

,

isClass

,

isConstructor

,

isEnum

,

isEnumConstant

,

isError

,

isException

,

isField

,

isIncluded

,

isInterface

,

isMethod

,

isOrdinaryClass

,

name

,

position

,

seeTags

,

setRawCommentText

,

tags

,

tags

---

#### Methods declared in interface com.sun.javadoc. Doc

Methods declared in interface com.sun.javadoc.

ProgramElementDoc

annotations

,

containingClass

,

containingPackage

,

isFinal

,

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

isStatic

,

modifiers

,

modifierSpecifier

,

qualifiedName

---

#### Methods declared in interface com.sun.javadoc. ProgramElementDoc

Methods declared in interface com.sun.javadoc.

Type

asAnnotatedType

,

asAnnotationTypeDoc

,

asClassDoc

,

asParameterizedType

,

asTypeVariable

,

asWildcardType

,

dimension

,

getElementType

,

isPrimitive

,

qualifiedTypeName

,

simpleTypeName

,

toString

,

typeName

---

#### Methods declared in interface com.sun.javadoc. Type

============ METHOD DETAIL ==========

- Method Detail

- isAbstract

```java
boolean isAbstract()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class is abstract. Return true
for all interfaces.

**Returns:** true if this class is abstract. Return true
for all interfaces.

- isSerializable

```java
boolean isSerializable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Serializable

.

Since

java.io.Externalizable

extends

java.io.Serializable

,
Externalizable objects are also Serializable.

**Returns:** true if this class implements or interface extends

java.io.Serializable

.

- isExternalizable

```java
boolean isExternalizable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Externalizable

.

**Returns:** true if this class implements or interface extends

java.io.Externalizable

.

- serializationMethods

```java
MethodDoc
[] serializationMethods()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialization methods for this class or
interface.

**Returns:** an array of MethodDoc objects that represents
the serialization methods for this class or interface.

- serializableFields

```java
FieldDoc
[] serializableFields()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the Serializable fields of this class or interface.

Return either a list of default fields documented by

serial

tag

or return a single

FieldDoc

for

serialPersistentField

member.
There should be a

serialField

tag for
each Serializable field defined by an

ObjectStreamField

array component of

serialPersistentField

.

**Returns:** an array of

FieldDoc

objects for the Serializable
fields of this class or interface.
**See Also:** definesSerializableFields()

,

SerialFieldTag

- definesSerializableFields

```java
boolean definesSerializableFields()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.

**Returns:** true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.
**See Also:** serializableFields()

,

SerialFieldTag

- superclass

```java
ClassDoc
superclass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class. Return null if this is an
interface.

This method cannot accommodate certain generic type constructs.
The

superclassType

method should be used instead.

**Returns:** the ClassDoc for the superclass of this class, null if
there is no superclass.
**See Also:** superclassType()

- superclassType

```java
Type
superclassType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class. Return null if this is an
interface. A superclass is represented by either a

ClassDoc

or a

ParametrizedType

.

**Returns:** the superclass of this class, or null if there is no superclass.
**Since:** 1.5

- subclassOf

```java
boolean subclassOf​(
ClassDoc
cd)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Test whether this class is a subclass of the specified class.
If this is an interface, return false for all classes except

java.lang.Object

(we must keep this unexpected
behavior for compatibility reasons).

**Parameters:** cd

- the candidate superclass.
**Returns:** true if cd is a superclass of this class.

- interfaces

```java
ClassDoc
[] interfaces()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

This method cannot accommodate certain generic type constructs.
The

interfaceTypes

method should be used instead.

**Returns:** an array of ClassDoc objects representing the interfaces.
**See Also:** interfaceTypes()

- interfaceTypes

```java
Type
[] interfaceTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

**Returns:** an array of interfaces, each represented by a

ClassDoc

or a

ParametrizedType

.
**Since:** 1.5

- typeParameters

```java
TypeVariable
[] typeParameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this class or interface.
Return an empty array if there are none.

**Returns:** the formal type parameters of this class or interface.
**Since:** 1.5

- typeParamTags

```java
ParamTag
[] typeParamTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags of this class or interface.
Return an empty array if there are none.

**Returns:** the type parameter tags of this class or interface.
**Since:** 1.5

- fields

```java
FieldDoc
[] fields()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

fields in this class or interface.
Excludes enum constants if this is an enum type.

**Returns:** an array of FieldDoc objects representing the included
fields in this class or interface.

- fields

```java
FieldDoc
[] fields​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return fields in this class or interface, filtered to the specified

access
modifier option

.
Excludes enum constants if this is an enum type.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all fields regardless of
access modifier option.
**Returns:** an array of FieldDoc objects representing the included
fields in this class or interface.

- enumConstants

```java
FieldDoc
[] enumConstants()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the enum constants if this is an enum type.
Return an empty array if there are no enum constants, or if
this is not an enum type.

**Returns:** the enum constants if this is an enum type.

- methods

```java
MethodDoc
[] methods()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

methods in this class or interface.
Same as

methods(true)

.

**Returns:** an array of MethodDoc objects representing the included
methods in this class or interface. Does not include
constructors or annotation type elements.

- methods

```java
MethodDoc
[] methods​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return methods in this class or interface, filtered to the specified

access
modifier option

. Does not include constructors or annotation
type elements.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all methods regardless of
access modifier option.
**Returns:** an array of MethodDoc objects representing the included
methods in this class or interface.

- constructors

```java
ConstructorDoc
[] constructors()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

constructors in this class. An array containing the default
no-arg constructor is returned if no other constructors exist.
Return empty array if this is an interface.

**Returns:** an array of ConstructorDoc objects representing the included
constructors in this class.

- constructors

```java
ConstructorDoc
[] constructors​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return constructors in this class, filtered to the specified

access
modifier option

. Return an array containing the default
no-arg constructor if no other constructors exist.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all constructors regardless of
access modifier option.
**Returns:** an array of ConstructorDoc objects representing the included
constructors in this class.

- innerClasses

```java
ClassDoc
[] innerClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

nested classes and interfaces within this class or interface.
This includes both static and non-static nested classes.
(This method should have been named

nestedClasses()

,
as inner classes are technically non-static.) Anonymous and local classes
or interfaces are not included.

**Returns:** an array of ClassDoc objects representing the included classes
and interfaces defined in this class or interface.

- innerClasses

```java
ClassDoc
[] innerClasses​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return nested classes and interfaces within this class or interface
filtered to the specified

access
modifier option

.
This includes both static and non-static nested classes.
Anonymous and local classes are not included.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all nested classes regardless of
access modifier option.
**Returns:** a filtered array of ClassDoc objects representing the included
classes and interfaces defined in this class or interface.

- findClass

```java
ClassDoc
findClass​(
String
className)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Find the specified class or interface within the context of this class doc.
Search order: 1) qualified name, 2) nested in this class or interface,
3) in this package, 4) in the class imports, 5) in the package imports.
Return the ClassDoc if found, null if not found.

**Parameters:** className

- Specify the class name to find as a String.
**Returns:** the ClassDoc if found, null if not found.

- importedClasses

```java
@Deprecated
(
since
="9",

forRemoval
=true)

ClassDoc
[] importedClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here. In addition, not all imported
classes are imported through single-type-import declarations.

Get the list of classes and interfaces declared as imported.
These are called "single-type-import declarations" in

The Java™ Language Specification

.

**Returns:** an array of ClassDoc representing the imported classes.

- importedPackages

```java
@Deprecated
(
since
="9",

forRemoval
=true)

PackageDoc
[] importedPackages()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here. In addition, this method's
return type does not allow for all type-import-on-demand
declarations to be returned.

Get the list of packages declared as imported.
These are called "type-import-on-demand declarations" in

The Java™ Language Specification

.

**Returns:** an array of PackageDoc representing the imported packages.

Method Detail

- isAbstract

```java
boolean isAbstract()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class is abstract. Return true
for all interfaces.

**Returns:** true if this class is abstract. Return true
for all interfaces.

- isSerializable

```java
boolean isSerializable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Serializable

.

Since

java.io.Externalizable

extends

java.io.Serializable

,
Externalizable objects are also Serializable.

**Returns:** true if this class implements or interface extends

java.io.Serializable

.

- isExternalizable

```java
boolean isExternalizable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Externalizable

.

**Returns:** true if this class implements or interface extends

java.io.Externalizable

.

- serializationMethods

```java
MethodDoc
[] serializationMethods()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialization methods for this class or
interface.

**Returns:** an array of MethodDoc objects that represents
the serialization methods for this class or interface.

- serializableFields

```java
FieldDoc
[] serializableFields()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the Serializable fields of this class or interface.

Return either a list of default fields documented by

serial

tag

or return a single

FieldDoc

for

serialPersistentField

member.
There should be a

serialField

tag for
each Serializable field defined by an

ObjectStreamField

array component of

serialPersistentField

.

**Returns:** an array of

FieldDoc

objects for the Serializable
fields of this class or interface.
**See Also:** definesSerializableFields()

,

SerialFieldTag

- definesSerializableFields

```java
boolean definesSerializableFields()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.

**Returns:** true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.
**See Also:** serializableFields()

,

SerialFieldTag

- superclass

```java
ClassDoc
superclass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class. Return null if this is an
interface.

This method cannot accommodate certain generic type constructs.
The

superclassType

method should be used instead.

**Returns:** the ClassDoc for the superclass of this class, null if
there is no superclass.
**See Also:** superclassType()

- superclassType

```java
Type
superclassType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class. Return null if this is an
interface. A superclass is represented by either a

ClassDoc

or a

ParametrizedType

.

**Returns:** the superclass of this class, or null if there is no superclass.
**Since:** 1.5

- subclassOf

```java
boolean subclassOf​(
ClassDoc
cd)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Test whether this class is a subclass of the specified class.
If this is an interface, return false for all classes except

java.lang.Object

(we must keep this unexpected
behavior for compatibility reasons).

**Parameters:** cd

- the candidate superclass.
**Returns:** true if cd is a superclass of this class.

- interfaces

```java
ClassDoc
[] interfaces()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

This method cannot accommodate certain generic type constructs.
The

interfaceTypes

method should be used instead.

**Returns:** an array of ClassDoc objects representing the interfaces.
**See Also:** interfaceTypes()

- interfaceTypes

```java
Type
[] interfaceTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

**Returns:** an array of interfaces, each represented by a

ClassDoc

or a

ParametrizedType

.
**Since:** 1.5

- typeParameters

```java
TypeVariable
[] typeParameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this class or interface.
Return an empty array if there are none.

**Returns:** the formal type parameters of this class or interface.
**Since:** 1.5

- typeParamTags

```java
ParamTag
[] typeParamTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags of this class or interface.
Return an empty array if there are none.

**Returns:** the type parameter tags of this class or interface.
**Since:** 1.5

- fields

```java
FieldDoc
[] fields()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

fields in this class or interface.
Excludes enum constants if this is an enum type.

**Returns:** an array of FieldDoc objects representing the included
fields in this class or interface.

- fields

```java
FieldDoc
[] fields​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return fields in this class or interface, filtered to the specified

access
modifier option

.
Excludes enum constants if this is an enum type.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all fields regardless of
access modifier option.
**Returns:** an array of FieldDoc objects representing the included
fields in this class or interface.

- enumConstants

```java
FieldDoc
[] enumConstants()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the enum constants if this is an enum type.
Return an empty array if there are no enum constants, or if
this is not an enum type.

**Returns:** the enum constants if this is an enum type.

- methods

```java
MethodDoc
[] methods()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

methods in this class or interface.
Same as

methods(true)

.

**Returns:** an array of MethodDoc objects representing the included
methods in this class or interface. Does not include
constructors or annotation type elements.

- methods

```java
MethodDoc
[] methods​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return methods in this class or interface, filtered to the specified

access
modifier option

. Does not include constructors or annotation
type elements.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all methods regardless of
access modifier option.
**Returns:** an array of MethodDoc objects representing the included
methods in this class or interface.

- constructors

```java
ConstructorDoc
[] constructors()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

constructors in this class. An array containing the default
no-arg constructor is returned if no other constructors exist.
Return empty array if this is an interface.

**Returns:** an array of ConstructorDoc objects representing the included
constructors in this class.

- constructors

```java
ConstructorDoc
[] constructors​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return constructors in this class, filtered to the specified

access
modifier option

. Return an array containing the default
no-arg constructor if no other constructors exist.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all constructors regardless of
access modifier option.
**Returns:** an array of ConstructorDoc objects representing the included
constructors in this class.

- innerClasses

```java
ClassDoc
[] innerClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

nested classes and interfaces within this class or interface.
This includes both static and non-static nested classes.
(This method should have been named

nestedClasses()

,
as inner classes are technically non-static.) Anonymous and local classes
or interfaces are not included.

**Returns:** an array of ClassDoc objects representing the included classes
and interfaces defined in this class or interface.

- innerClasses

```java
ClassDoc
[] innerClasses​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return nested classes and interfaces within this class or interface
filtered to the specified

access
modifier option

.
This includes both static and non-static nested classes.
Anonymous and local classes are not included.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all nested classes regardless of
access modifier option.
**Returns:** a filtered array of ClassDoc objects representing the included
classes and interfaces defined in this class or interface.

- findClass

```java
ClassDoc
findClass​(
String
className)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Find the specified class or interface within the context of this class doc.
Search order: 1) qualified name, 2) nested in this class or interface,
3) in this package, 4) in the class imports, 5) in the package imports.
Return the ClassDoc if found, null if not found.

**Parameters:** className

- Specify the class name to find as a String.
**Returns:** the ClassDoc if found, null if not found.

- importedClasses

```java
@Deprecated
(
since
="9",

forRemoval
=true)

ClassDoc
[] importedClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here. In addition, not all imported
classes are imported through single-type-import declarations.

Get the list of classes and interfaces declared as imported.
These are called "single-type-import declarations" in

The Java™ Language Specification

.

**Returns:** an array of ClassDoc representing the imported classes.

- importedPackages

```java
@Deprecated
(
since
="9",

forRemoval
=true)

PackageDoc
[] importedPackages()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here. In addition, this method's
return type does not allow for all type-import-on-demand
declarations to be returned.

Get the list of packages declared as imported.
These are called "type-import-on-demand declarations" in

The Java™ Language Specification

.

**Returns:** an array of PackageDoc representing the imported packages.

---

#### Method Detail

isAbstract

```java
boolean isAbstract()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class is abstract. Return true
for all interfaces.

**Returns:** true if this class is abstract. Return true
for all interfaces.

---

#### isAbstract

boolean isAbstract()

Return true if this class is abstract. Return true
for all interfaces.

isSerializable

```java
boolean isSerializable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Serializable

.

Since

java.io.Externalizable

extends

java.io.Serializable

,
Externalizable objects are also Serializable.

**Returns:** true if this class implements or interface extends

java.io.Serializable

.

---

#### isSerializable

boolean isSerializable()

Return true if this class implements or interface extends

java.io.Serializable

.

Since

java.io.Externalizable

extends

java.io.Serializable

,
Externalizable objects are also Serializable.

isExternalizable

```java
boolean isExternalizable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this class implements or interface extends

java.io.Externalizable

.

**Returns:** true if this class implements or interface extends

java.io.Externalizable

.

---

#### isExternalizable

boolean isExternalizable()

Return true if this class implements or interface extends

java.io.Externalizable

.

serializationMethods

```java
MethodDoc
[] serializationMethods()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the serialization methods for this class or
interface.

**Returns:** an array of MethodDoc objects that represents
the serialization methods for this class or interface.

---

#### serializationMethods

MethodDoc

[] serializationMethods()

Return the serialization methods for this class or
interface.

serializableFields

```java
FieldDoc
[] serializableFields()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the Serializable fields of this class or interface.

Return either a list of default fields documented by

serial

tag

or return a single

FieldDoc

for

serialPersistentField

member.
There should be a

serialField

tag for
each Serializable field defined by an

ObjectStreamField

array component of

serialPersistentField

.

**Returns:** an array of

FieldDoc

objects for the Serializable
fields of this class or interface.
**See Also:** definesSerializableFields()

,

SerialFieldTag

---

#### serializableFields

FieldDoc

[] serializableFields()

Return the Serializable fields of this class or interface.

Return either a list of default fields documented by

serial

tag

or return a single

FieldDoc

for

serialPersistentField

member.
There should be a

serialField

tag for
each Serializable field defined by an

ObjectStreamField

array component of

serialPersistentField

.

Return either a list of default fields documented by

serial

tag

or return a single

FieldDoc

for

serialPersistentField

member.
There should be a

serialField

tag for
each Serializable field defined by an

ObjectStreamField

array component of

serialPersistentField

.

definesSerializableFields

```java
boolean definesSerializableFields()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.

**Returns:** true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.
**See Also:** serializableFields()

,

SerialFieldTag

---

#### definesSerializableFields

boolean definesSerializableFields()

Return true if Serializable fields are explicitly defined with
the special class member

serialPersistentFields

.

superclass

```java
ClassDoc
superclass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class. Return null if this is an
interface.

This method cannot accommodate certain generic type constructs.
The

superclassType

method should be used instead.

**Returns:** the ClassDoc for the superclass of this class, null if
there is no superclass.
**See Also:** superclassType()

---

#### superclass

ClassDoc

superclass()

Return the superclass of this class. Return null if this is an
interface.

This method cannot accommodate certain generic type constructs.
The

superclassType

method should be used instead.

This method cannot accommodate certain generic type constructs.
The

superclassType

method should be used instead.

superclassType

```java
Type
superclassType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the superclass of this class. Return null if this is an
interface. A superclass is represented by either a

ClassDoc

or a

ParametrizedType

.

**Returns:** the superclass of this class, or null if there is no superclass.
**Since:** 1.5

---

#### superclassType

Type

superclassType()

Return the superclass of this class. Return null if this is an
interface. A superclass is represented by either a

ClassDoc

or a

ParametrizedType

.

subclassOf

```java
boolean subclassOf​(
ClassDoc
cd)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Test whether this class is a subclass of the specified class.
If this is an interface, return false for all classes except

java.lang.Object

(we must keep this unexpected
behavior for compatibility reasons).

**Parameters:** cd

- the candidate superclass.
**Returns:** true if cd is a superclass of this class.

---

#### subclassOf

boolean subclassOf​(

ClassDoc

cd)

Test whether this class is a subclass of the specified class.
If this is an interface, return false for all classes except

java.lang.Object

(we must keep this unexpected
behavior for compatibility reasons).

interfaces

```java
ClassDoc
[] interfaces()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

This method cannot accommodate certain generic type constructs.
The

interfaceTypes

method should be used instead.

**Returns:** an array of ClassDoc objects representing the interfaces.
**See Also:** interfaceTypes()

---

#### interfaces

ClassDoc

[] interfaces()

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

This method cannot accommodate certain generic type constructs.
The

interfaceTypes

method should be used instead.

This method cannot accommodate certain generic type constructs.
The

interfaceTypes

method should be used instead.

interfaceTypes

```java
Type
[] interfaceTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

**Returns:** an array of interfaces, each represented by a

ClassDoc

or a

ParametrizedType

.
**Since:** 1.5

---

#### interfaceTypes

Type

[] interfaceTypes()

Return interfaces implemented by this class or interfaces extended
by this interface. Includes only directly-declared interfaces, not
inherited interfaces.
Return an empty array if there are no interfaces.

typeParameters

```java
TypeVariable
[] typeParameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this class or interface.
Return an empty array if there are none.

**Returns:** the formal type parameters of this class or interface.
**Since:** 1.5

---

#### typeParameters

TypeVariable

[] typeParameters()

Return the formal type parameters of this class or interface.
Return an empty array if there are none.

typeParamTags

```java
ParamTag
[] typeParamTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags of this class or interface.
Return an empty array if there are none.

**Returns:** the type parameter tags of this class or interface.
**Since:** 1.5

---

#### typeParamTags

ParamTag

[] typeParamTags()

Return the type parameter tags of this class or interface.
Return an empty array if there are none.

fields

```java
FieldDoc
[] fields()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

fields in this class or interface.
Excludes enum constants if this is an enum type.

**Returns:** an array of FieldDoc objects representing the included
fields in this class or interface.

---

#### fields

FieldDoc

[] fields()

Return

included

fields in this class or interface.
Excludes enum constants if this is an enum type.

fields

```java
FieldDoc
[] fields​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return fields in this class or interface, filtered to the specified

access
modifier option

.
Excludes enum constants if this is an enum type.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all fields regardless of
access modifier option.
**Returns:** an array of FieldDoc objects representing the included
fields in this class or interface.

---

#### fields

FieldDoc

[] fields​(boolean filter)

Return fields in this class or interface, filtered to the specified

access
modifier option

.
Excludes enum constants if this is an enum type.

enumConstants

```java
FieldDoc
[] enumConstants()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the enum constants if this is an enum type.
Return an empty array if there are no enum constants, or if
this is not an enum type.

**Returns:** the enum constants if this is an enum type.

---

#### enumConstants

FieldDoc

[] enumConstants()

Return the enum constants if this is an enum type.
Return an empty array if there are no enum constants, or if
this is not an enum type.

methods

```java
MethodDoc
[] methods()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

methods in this class or interface.
Same as

methods(true)

.

**Returns:** an array of MethodDoc objects representing the included
methods in this class or interface. Does not include
constructors or annotation type elements.

---

#### methods

MethodDoc

[] methods()

Return

included

methods in this class or interface.
Same as

methods(true)

.

methods

```java
MethodDoc
[] methods​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return methods in this class or interface, filtered to the specified

access
modifier option

. Does not include constructors or annotation
type elements.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all methods regardless of
access modifier option.
**Returns:** an array of MethodDoc objects representing the included
methods in this class or interface.

---

#### methods

MethodDoc

[] methods​(boolean filter)

Return methods in this class or interface, filtered to the specified

access
modifier option

. Does not include constructors or annotation
type elements.

constructors

```java
ConstructorDoc
[] constructors()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

constructors in this class. An array containing the default
no-arg constructor is returned if no other constructors exist.
Return empty array if this is an interface.

**Returns:** an array of ConstructorDoc objects representing the included
constructors in this class.

---

#### constructors

ConstructorDoc

[] constructors()

Return

included

constructors in this class. An array containing the default
no-arg constructor is returned if no other constructors exist.
Return empty array if this is an interface.

constructors

```java
ConstructorDoc
[] constructors​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return constructors in this class, filtered to the specified

access
modifier option

. Return an array containing the default
no-arg constructor if no other constructors exist.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all constructors regardless of
access modifier option.
**Returns:** an array of ConstructorDoc objects representing the included
constructors in this class.

---

#### constructors

ConstructorDoc

[] constructors​(boolean filter)

Return constructors in this class, filtered to the specified

access
modifier option

. Return an array containing the default
no-arg constructor if no other constructors exist.

innerClasses

```java
ClassDoc
[] innerClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return

included

nested classes and interfaces within this class or interface.
This includes both static and non-static nested classes.
(This method should have been named

nestedClasses()

,
as inner classes are technically non-static.) Anonymous and local classes
or interfaces are not included.

**Returns:** an array of ClassDoc objects representing the included classes
and interfaces defined in this class or interface.

---

#### innerClasses

ClassDoc

[] innerClasses()

Return

included

nested classes and interfaces within this class or interface.
This includes both static and non-static nested classes.
(This method should have been named

nestedClasses()

,
as inner classes are technically non-static.) Anonymous and local classes
or interfaces are not included.

innerClasses

```java
ClassDoc
[] innerClasses​(boolean filter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return nested classes and interfaces within this class or interface
filtered to the specified

access
modifier option

.
This includes both static and non-static nested classes.
Anonymous and local classes are not included.

**Parameters:** filter

- Specify true to filter according to the specified access
modifier option.
Specify false to include all nested classes regardless of
access modifier option.
**Returns:** a filtered array of ClassDoc objects representing the included
classes and interfaces defined in this class or interface.

---

#### innerClasses

ClassDoc

[] innerClasses​(boolean filter)

Return nested classes and interfaces within this class or interface
filtered to the specified

access
modifier option

.
This includes both static and non-static nested classes.
Anonymous and local classes are not included.

findClass

```java
ClassDoc
findClass​(
String
className)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Find the specified class or interface within the context of this class doc.
Search order: 1) qualified name, 2) nested in this class or interface,
3) in this package, 4) in the class imports, 5) in the package imports.
Return the ClassDoc if found, null if not found.

**Parameters:** className

- Specify the class name to find as a String.
**Returns:** the ClassDoc if found, null if not found.

---

#### findClass

ClassDoc

findClass​(

String

className)

Find the specified class or interface within the context of this class doc.
Search order: 1) qualified name, 2) nested in this class or interface,
3) in this package, 4) in the class imports, 5) in the package imports.
Return the ClassDoc if found, null if not found.

importedClasses

```java
@Deprecated
(
since
="9",

forRemoval
=true)

ClassDoc
[] importedClasses()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here. In addition, not all imported
classes are imported through single-type-import declarations.

Get the list of classes and interfaces declared as imported.
These are called "single-type-import declarations" in

The Java™ Language Specification

.

**Returns:** an array of ClassDoc representing the imported classes.

---

#### importedClasses

@Deprecated

(

since

="9",

forRemoval

=true)

ClassDoc

[] importedClasses()

Get the list of classes and interfaces declared as imported.
These are called "single-type-import declarations" in

The Java™ Language Specification

.

importedPackages

```java
@Deprecated
(
since
="9",

forRemoval
=true)

PackageDoc
[] importedPackages()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Import declarations are implementation details that
should not be exposed here. In addition, this method's
return type does not allow for all type-import-on-demand
declarations to be returned.

Get the list of packages declared as imported.
These are called "type-import-on-demand declarations" in

The Java™ Language Specification

.

**Returns:** an array of PackageDoc representing the imported packages.

---

#### importedPackages

@Deprecated

(

since

="9",

forRemoval

=true)

PackageDoc

[] importedPackages()

Get the list of packages declared as imported.
These are called "type-import-on-demand declarations" in

The Java™ Language Specification

.

---

