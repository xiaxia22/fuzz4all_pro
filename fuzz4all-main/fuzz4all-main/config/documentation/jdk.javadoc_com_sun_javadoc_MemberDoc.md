# Interface MemberDoc

**Source:** `jdk.javadoc\com\sun\javadoc\MemberDoc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
MemberDoc

extends
ProgramElementDoc
```

Represents a member of a java class: field, constructor, or method.
This is an abstract class dealing with information common to
method, constructor and field members. Class members of a class
(innerclasses) are represented instead by ClassDoc.

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

ProgramElementDoc

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isSynthetic()

Returns true if this member was synthesized by the compiler.

**Returns:**
- true if this member was synthesized by the compiler.

---

### Additional Sections

#### Interface MemberDoc

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

ProgramElementDoc

**All Known Subinterfaces:** AnnotationTypeElementDoc

,

ConstructorDoc

,

ExecutableMemberDoc

,

FieldDoc

,

MethodDoc

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
MemberDoc

extends
ProgramElementDoc
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a member of a java class: field, constructor, or method.
This is an abstract class dealing with information common to
method, constructor and field members. Class members of a class
(innerclasses) are represented instead by ClassDoc.

**See Also:** MethodDoc

,

FieldDoc

,

ClassDoc

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

MemberDoc

extends

ProgramElementDoc

Represents a member of a java class: field, constructor, or method.
This is an abstract class dealing with information common to
method, constructor and field members. Class members of a class
(innerclasses) are represented instead by ClassDoc.

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

isSynthetic

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this member was synthesized by the compiler.

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

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

isSynthetic

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this member was synthesized by the compiler.

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

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this member was synthesized by the compiler.

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

============ METHOD DETAIL ==========

- Method Detail

- isSynthetic

```java
boolean isSynthetic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this member was synthesized by the compiler.

**Returns:** true if this member was synthesized by the compiler.

Method Detail

- isSynthetic

```java
boolean isSynthetic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this member was synthesized by the compiler.

**Returns:** true if this member was synthesized by the compiler.

---

#### Method Detail

isSynthetic

```java
boolean isSynthetic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if this member was synthesized by the compiler.

**Returns:** true if this member was synthesized by the compiler.

---

#### isSynthetic

boolean isSynthetic()

Returns true if this member was synthesized by the compiler.

---

