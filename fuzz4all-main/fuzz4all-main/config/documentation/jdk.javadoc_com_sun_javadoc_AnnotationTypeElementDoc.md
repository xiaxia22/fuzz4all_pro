# Interface AnnotationTypeElementDoc

**Source:** `jdk.javadoc\com\sun\javadoc\AnnotationTypeElementDoc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
AnnotationTypeElementDoc

extends
MethodDoc
```

Represents an element of an annotation type.

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

MethodDoc

,

ProgramElementDoc

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### AnnotationValue
defaultValue()

Returns the default value of this element.
Returns null if this element has no default.

**Returns:**
- the default value of this element.

---

### Additional Sections

#### Interface AnnotationTypeElementDoc

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

MethodDoc

,

ProgramElementDoc

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
AnnotationTypeElementDoc

extends
MethodDoc
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents an element of an annotation type.

**Since:** 1.5

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

AnnotationTypeElementDoc

extends

MethodDoc

Represents an element of an annotation type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

AnnotationValue

defaultValue

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the default value of this element.

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

MethodDoc

isAbstract

,

isDefault

,

overriddenClass

,

overriddenMethod

,

overriddenType

,

overrides

,

returnType

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

AnnotationValue

defaultValue

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the default value of this element.

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

MethodDoc

isAbstract

,

isDefault

,

overriddenClass

,

overriddenMethod

,

overriddenType

,

overrides

,

returnType

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

Returns the default value of this element.

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

MethodDoc

isAbstract

,

isDefault

,

overriddenClass

,

overriddenMethod

,

overriddenType

,

overrides

,

returnType

---

#### Methods declared in interface com.sun.javadoc. MethodDoc

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

- defaultValue

```java
AnnotationValue
defaultValue()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the default value of this element.
Returns null if this element has no default.

**Returns:** the default value of this element.

Method Detail

- defaultValue

```java
AnnotationValue
defaultValue()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the default value of this element.
Returns null if this element has no default.

**Returns:** the default value of this element.

---

#### Method Detail

defaultValue

```java
AnnotationValue
defaultValue()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the default value of this element.
Returns null if this element has no default.

**Returns:** the default value of this element.

---

#### defaultValue

AnnotationValue

defaultValue()

Returns the default value of this element.
Returns null if this element has no default.

---

