# Interface MethodDoc

**Source:** `jdk.javadoc\com\sun\javadoc\MethodDoc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
MethodDoc

extends
ExecutableMemberDoc
```

Represents a method of a java class.

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

ExecutableMemberDoc

,

MemberDoc

,

ProgramElementDoc

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isAbstract()

Return true if this method is abstract

**Returns:**
- true if this method is abstract

---

#### boolean isDefault()

Return true if this method is default

**Returns:**
- true if this method is default

---

#### Type
returnType()

Get return type.

**Returns:**
- the return type of this method, null if it
is a constructor.

---

#### ClassDoc
overriddenClass()

Return the class containing the method that this method overrides.

The

overriddenClass

method cannot
accommodate certain generic type constructs. The

overriddenType

method should be used instead.

**Returns:**
- a ClassDoc representing the superclass
defining a method that this method overrides, or null if
this method does not override.

---

#### Type
overriddenType()

Return the type containing the method that this method overrides.
It may be a

ClassDoc

or a

ParameterizedType

.

**Returns:**
- the supertype whose method is overridden, or null if this
method does not override another in a superclass

**Since:**
- 1.5

---

#### MethodDoc
overriddenMethod()

Return the method that this method overrides.

**Returns:**
- a MethodDoc representing a method definition
in a superclass this method overrides, null if
this method does not override.

---

#### boolean overrides​(
MethodDoc
meth)

Tests whether this method overrides another.
The overridden method may be one declared in a superclass or
a superinterface (unlike

overriddenMethod()

).

When a non-abstract method overrides an abstract one, it is
also said to

implement

the other.

**Parameters:**
- meth

- the other method to examine

**Returns:**
- true

if this method overrides the other

**Since:**
- 1.5

---

### Additional Sections

#### Interface MethodDoc

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

ExecutableMemberDoc

,

MemberDoc

,

ProgramElementDoc

**All Known Subinterfaces:** AnnotationTypeElementDoc

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
MethodDoc

extends
ExecutableMemberDoc
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a method of a java class.

**Since:** 1.2

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

MethodDoc

extends

ExecutableMemberDoc

Represents a method of a java class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

isAbstract

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is abstract

boolean

isDefault

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is default

ClassDoc

overriddenClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class containing the method that this method overrides.

MethodDoc

overriddenMethod

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the method that this method overrides.

Type

overriddenType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type containing the method that this method overrides.

boolean

overrides

​(

MethodDoc

meth)

Deprecated, for removal: This API element is subject to removal in a future version.

Tests whether this method overrides another.

Type

returnType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get return type.

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

ExecutableMemberDoc

flatSignature

,

isNative

,

isSynchronized

,

isVarArgs

,

parameters

,

paramTags

,

receiverType

,

signature

,

thrownExceptions

,

thrownExceptionTypes

,

throwsTags

,

typeParameters

,

typeParamTags

- Methods declared in interface com.sun.javadoc.

MemberDoc

isSynthetic

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

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

isAbstract

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is abstract

boolean

isDefault

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is default

ClassDoc

overriddenClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class containing the method that this method overrides.

MethodDoc

overriddenMethod

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the method that this method overrides.

Type

overriddenType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type containing the method that this method overrides.

boolean

overrides

​(

MethodDoc

meth)

Deprecated, for removal: This API element is subject to removal in a future version.

Tests whether this method overrides another.

Type

returnType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get return type.

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

ExecutableMemberDoc

flatSignature

,

isNative

,

isSynchronized

,

isVarArgs

,

parameters

,

paramTags

,

receiverType

,

signature

,

thrownExceptions

,

thrownExceptionTypes

,

throwsTags

,

typeParameters

,

typeParamTags

- Methods declared in interface com.sun.javadoc.

MemberDoc

isSynthetic

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

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is abstract

Return true if this method is default

Return the class containing the method that this method overrides.

Return the method that this method overrides.

Return the type containing the method that this method overrides.

Tests whether this method overrides another.

Get return type.

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

ExecutableMemberDoc

flatSignature

,

isNative

,

isSynchronized

,

isVarArgs

,

parameters

,

paramTags

,

receiverType

,

signature

,

thrownExceptions

,

thrownExceptionTypes

,

throwsTags

,

typeParameters

,

typeParamTags

---

#### Methods declared in interface com.sun.javadoc. ExecutableMemberDoc

Methods declared in interface com.sun.javadoc.

MemberDoc

isSynthetic

---

#### Methods declared in interface com.sun.javadoc. MemberDoc

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

============ METHOD DETAIL ==========

- Method Detail

- isAbstract

```java
boolean isAbstract()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is abstract

**Returns:** true if this method is abstract

- isDefault

```java
boolean isDefault()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is default

**Returns:** true if this method is default

- returnType

```java
Type
returnType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get return type.

**Returns:** the return type of this method, null if it
is a constructor.

- overriddenClass

```java
ClassDoc
overriddenClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class containing the method that this method overrides.

The

overriddenClass

method cannot
accommodate certain generic type constructs. The

overriddenType

method should be used instead.

**Returns:** a ClassDoc representing the superclass
defining a method that this method overrides, or null if
this method does not override.

- overriddenType

```java
Type
overriddenType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type containing the method that this method overrides.
It may be a

ClassDoc

or a

ParameterizedType

.

**Returns:** the supertype whose method is overridden, or null if this
method does not override another in a superclass
**Since:** 1.5

- overriddenMethod

```java
MethodDoc
overriddenMethod()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the method that this method overrides.

**Returns:** a MethodDoc representing a method definition
in a superclass this method overrides, null if
this method does not override.

- overrides

```java
boolean overrides​(
MethodDoc
meth)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Tests whether this method overrides another.
The overridden method may be one declared in a superclass or
a superinterface (unlike

overriddenMethod()

).

When a non-abstract method overrides an abstract one, it is
also said to

implement

the other.

**Parameters:** meth

- the other method to examine
**Returns:** true

if this method overrides the other
**Since:** 1.5

Method Detail

- isAbstract

```java
boolean isAbstract()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is abstract

**Returns:** true if this method is abstract

- isDefault

```java
boolean isDefault()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is default

**Returns:** true if this method is default

- returnType

```java
Type
returnType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get return type.

**Returns:** the return type of this method, null if it
is a constructor.

- overriddenClass

```java
ClassDoc
overriddenClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class containing the method that this method overrides.

The

overriddenClass

method cannot
accommodate certain generic type constructs. The

overriddenType

method should be used instead.

**Returns:** a ClassDoc representing the superclass
defining a method that this method overrides, or null if
this method does not override.

- overriddenType

```java
Type
overriddenType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type containing the method that this method overrides.
It may be a

ClassDoc

or a

ParameterizedType

.

**Returns:** the supertype whose method is overridden, or null if this
method does not override another in a superclass
**Since:** 1.5

- overriddenMethod

```java
MethodDoc
overriddenMethod()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the method that this method overrides.

**Returns:** a MethodDoc representing a method definition
in a superclass this method overrides, null if
this method does not override.

- overrides

```java
boolean overrides​(
MethodDoc
meth)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Tests whether this method overrides another.
The overridden method may be one declared in a superclass or
a superinterface (unlike

overriddenMethod()

).

When a non-abstract method overrides an abstract one, it is
also said to

implement

the other.

**Parameters:** meth

- the other method to examine
**Returns:** true

if this method overrides the other
**Since:** 1.5

---

#### Method Detail

isAbstract

```java
boolean isAbstract()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is abstract

**Returns:** true if this method is abstract

---

#### isAbstract

boolean isAbstract()

Return true if this method is abstract

isDefault

```java
boolean isDefault()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is default

**Returns:** true if this method is default

---

#### isDefault

boolean isDefault()

Return true if this method is default

returnType

```java
Type
returnType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get return type.

**Returns:** the return type of this method, null if it
is a constructor.

---

#### returnType

Type

returnType()

Get return type.

overriddenClass

```java
ClassDoc
overriddenClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class containing the method that this method overrides.

The

overriddenClass

method cannot
accommodate certain generic type constructs. The

overriddenType

method should be used instead.

**Returns:** a ClassDoc representing the superclass
defining a method that this method overrides, or null if
this method does not override.

---

#### overriddenClass

ClassDoc

overriddenClass()

Return the class containing the method that this method overrides.

The

overriddenClass

method cannot
accommodate certain generic type constructs. The

overriddenType

method should be used instead.

The

overriddenClass

method cannot
accommodate certain generic type constructs. The

overriddenType

method should be used instead.

overriddenType

```java
Type
overriddenType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type containing the method that this method overrides.
It may be a

ClassDoc

or a

ParameterizedType

.

**Returns:** the supertype whose method is overridden, or null if this
method does not override another in a superclass
**Since:** 1.5

---

#### overriddenType

Type

overriddenType()

Return the type containing the method that this method overrides.
It may be a

ClassDoc

or a

ParameterizedType

.

overriddenMethod

```java
MethodDoc
overriddenMethod()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the method that this method overrides.

**Returns:** a MethodDoc representing a method definition
in a superclass this method overrides, null if
this method does not override.

---

#### overriddenMethod

MethodDoc

overriddenMethod()

Return the method that this method overrides.

overrides

```java
boolean overrides​(
MethodDoc
meth)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Tests whether this method overrides another.
The overridden method may be one declared in a superclass or
a superinterface (unlike

overriddenMethod()

).

When a non-abstract method overrides an abstract one, it is
also said to

implement

the other.

**Parameters:** meth

- the other method to examine
**Returns:** true

if this method overrides the other
**Since:** 1.5

---

#### overrides

boolean overrides​(

MethodDoc

meth)

Tests whether this method overrides another.
The overridden method may be one declared in a superclass or
a superinterface (unlike

overriddenMethod()

).

When a non-abstract method overrides an abstract one, it is
also said to

implement

the other.

When a non-abstract method overrides an abstract one, it is
also said to

implement

the other.

---

