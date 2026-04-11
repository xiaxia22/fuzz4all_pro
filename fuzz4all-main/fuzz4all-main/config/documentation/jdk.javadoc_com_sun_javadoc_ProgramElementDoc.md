# Interface ProgramElementDoc

**Source:** `jdk.javadoc\com\sun\javadoc\ProgramElementDoc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ProgramElementDoc

extends
Doc
```

Represents a java program element: class, interface, field,
constructor, or method.
This is an abstract class dealing with information common to
these elements.

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ClassDoc
containingClass()

Get the containing class or interface of this program element.

**Returns:**
- a ClassDoc for this element's containing class or interface.
If this is a top-level class or interface, return null.

---

#### PackageDoc
containingPackage()

Get the package that this program element is contained in.

**Returns:**
- a PackageDoc for this element containing package.
If in the unnamed package, this PackageDoc will have the
name "".

---

#### String
qualifiedName()

Get the fully qualified name of this program element.
For example, for the class

java.util.Hashtable

,
return "java.util.Hashtable".

For the method

bar()

in class

Foo

in the unnamed package, return "Foo.bar".

**Returns:**
- the qualified name of the program element as a String.

---

#### int modifierSpecifier()

Get the modifier specifier integer.

**Returns:**
- Get the modifier specifier integer.

**See Also:**
- Modifier

---

#### String
modifiers()

Get modifiers string.
For example, for:

```java
public abstract int foo() { ... }
```

return "public abstract".
Annotations are not included.

**Returns:**
- "public abstract".

---

#### AnnotationDesc
[] annotations()

Get the annotations of this program element.
Return an empty array if there are none.

**Returns:**
- the annotations of this program element.

**Since:**
- 1.5

---

#### boolean isPublic()

Return true if this program element is public.

**Returns:**
- true if this program element is public.

---

#### boolean isProtected()

Return true if this program element is protected.

**Returns:**
- true if this program element is protected.

---

#### boolean isPrivate()

Return true if this program element is private.

**Returns:**
- true if this program element is private.

---

#### boolean isPackagePrivate()

Return true if this program element is package private.

**Returns:**
- true if this program element is package private.

---

#### boolean isStatic()

Return true if this program element is static.

**Returns:**
- true if this program element is static.

---

#### boolean isFinal()

Return true if this program element is final.

**Returns:**
- true if this program element is final.

---

### Additional Sections

#### Interface ProgramElementDoc

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

**All Known Subinterfaces:** AnnotationTypeDoc

,

AnnotationTypeElementDoc

,

ClassDoc

,

ConstructorDoc

,

ExecutableMemberDoc

,

FieldDoc

,

MemberDoc

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
ProgramElementDoc

extends
Doc
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a java program element: class, interface, field,
constructor, or method.
This is an abstract class dealing with information common to
these elements.

**See Also:** MemberDoc

,

ClassDoc

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

ProgramElementDoc

extends

Doc

Represents a java program element: class, interface, field,
constructor, or method.
This is an abstract class dealing with information common to
these elements.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

AnnotationDesc

[]

annotations

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.

ClassDoc

containingClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the containing class or interface of this program element.

PackageDoc

containingPackage

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package that this program element is contained in.

boolean

isFinal

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is final.

boolean

isPackagePrivate

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is package private.

boolean

isPrivate

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is private.

boolean

isProtected

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is protected.

boolean

isPublic

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is public.

boolean

isStatic

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is static.

String

modifiers

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get modifiers string.

int

modifierSpecifier

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the modifier specifier integer.

String

qualifiedName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the fully qualified name of this program element.

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

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

AnnotationDesc

[]

annotations

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.

ClassDoc

containingClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the containing class or interface of this program element.

PackageDoc

containingPackage

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package that this program element is contained in.

boolean

isFinal

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is final.

boolean

isPackagePrivate

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is package private.

boolean

isPrivate

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is private.

boolean

isProtected

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is protected.

boolean

isPublic

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is public.

boolean

isStatic

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is static.

String

modifiers

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get modifiers string.

int

modifierSpecifier

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the modifier specifier integer.

String

qualifiedName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the fully qualified name of this program element.

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

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.

Get the containing class or interface of this program element.

Get the package that this program element is contained in.

Return true if this program element is final.

Return true if this program element is package private.

Return true if this program element is private.

Return true if this program element is protected.

Return true if this program element is public.

Return true if this program element is static.

Get modifiers string.

Get the modifier specifier integer.

Get the fully qualified name of this program element.

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

============ METHOD DETAIL ==========

- Method Detail

- containingClass

```java
ClassDoc
containingClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the containing class or interface of this program element.

**Returns:** a ClassDoc for this element's containing class or interface.
If this is a top-level class or interface, return null.

- containingPackage

```java
PackageDoc
containingPackage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package that this program element is contained in.

**Returns:** a PackageDoc for this element containing package.
If in the unnamed package, this PackageDoc will have the
name "".

- qualifiedName

```java
String
qualifiedName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the fully qualified name of this program element.
For example, for the class

java.util.Hashtable

,
return "java.util.Hashtable".

For the method

bar()

in class

Foo

in the unnamed package, return "Foo.bar".

**Returns:** the qualified name of the program element as a String.

- modifierSpecifier

```java
int modifierSpecifier()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the modifier specifier integer.

**Returns:** Get the modifier specifier integer.
**See Also:** Modifier

- modifiers

```java
String
modifiers()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get modifiers string.
For example, for:

```java
public abstract int foo() { ... }
```

return "public abstract".
Annotations are not included.

**Returns:** "public abstract".

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.
Return an empty array if there are none.

**Returns:** the annotations of this program element.
**Since:** 1.5

- isPublic

```java
boolean isPublic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is public.

**Returns:** true if this program element is public.

- isProtected

```java
boolean isProtected()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is protected.

**Returns:** true if this program element is protected.

- isPrivate

```java
boolean isPrivate()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is private.

**Returns:** true if this program element is private.

- isPackagePrivate

```java
boolean isPackagePrivate()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is package private.

**Returns:** true if this program element is package private.

- isStatic

```java
boolean isStatic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is static.

**Returns:** true if this program element is static.

- isFinal

```java
boolean isFinal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is final.

**Returns:** true if this program element is final.

Method Detail

- containingClass

```java
ClassDoc
containingClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the containing class or interface of this program element.

**Returns:** a ClassDoc for this element's containing class or interface.
If this is a top-level class or interface, return null.

- containingPackage

```java
PackageDoc
containingPackage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package that this program element is contained in.

**Returns:** a PackageDoc for this element containing package.
If in the unnamed package, this PackageDoc will have the
name "".

- qualifiedName

```java
String
qualifiedName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the fully qualified name of this program element.
For example, for the class

java.util.Hashtable

,
return "java.util.Hashtable".

For the method

bar()

in class

Foo

in the unnamed package, return "Foo.bar".

**Returns:** the qualified name of the program element as a String.

- modifierSpecifier

```java
int modifierSpecifier()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the modifier specifier integer.

**Returns:** Get the modifier specifier integer.
**See Also:** Modifier

- modifiers

```java
String
modifiers()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get modifiers string.
For example, for:

```java
public abstract int foo() { ... }
```

return "public abstract".
Annotations are not included.

**Returns:** "public abstract".

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.
Return an empty array if there are none.

**Returns:** the annotations of this program element.
**Since:** 1.5

- isPublic

```java
boolean isPublic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is public.

**Returns:** true if this program element is public.

- isProtected

```java
boolean isProtected()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is protected.

**Returns:** true if this program element is protected.

- isPrivate

```java
boolean isPrivate()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is private.

**Returns:** true if this program element is private.

- isPackagePrivate

```java
boolean isPackagePrivate()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is package private.

**Returns:** true if this program element is package private.

- isStatic

```java
boolean isStatic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is static.

**Returns:** true if this program element is static.

- isFinal

```java
boolean isFinal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is final.

**Returns:** true if this program element is final.

---

#### Method Detail

containingClass

```java
ClassDoc
containingClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the containing class or interface of this program element.

**Returns:** a ClassDoc for this element's containing class or interface.
If this is a top-level class or interface, return null.

---

#### containingClass

ClassDoc

containingClass()

Get the containing class or interface of this program element.

containingPackage

```java
PackageDoc
containingPackage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package that this program element is contained in.

**Returns:** a PackageDoc for this element containing package.
If in the unnamed package, this PackageDoc will have the
name "".

---

#### containingPackage

PackageDoc

containingPackage()

Get the package that this program element is contained in.

qualifiedName

```java
String
qualifiedName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the fully qualified name of this program element.
For example, for the class

java.util.Hashtable

,
return "java.util.Hashtable".

For the method

bar()

in class

Foo

in the unnamed package, return "Foo.bar".

**Returns:** the qualified name of the program element as a String.

---

#### qualifiedName

String

qualifiedName()

Get the fully qualified name of this program element.
For example, for the class

java.util.Hashtable

,
return "java.util.Hashtable".

For the method

bar()

in class

Foo

in the unnamed package, return "Foo.bar".

For the method

bar()

in class

Foo

in the unnamed package, return "Foo.bar".

modifierSpecifier

```java
int modifierSpecifier()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the modifier specifier integer.

**Returns:** Get the modifier specifier integer.
**See Also:** Modifier

---

#### modifierSpecifier

int modifierSpecifier()

Get the modifier specifier integer.

modifiers

```java
String
modifiers()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get modifiers string.
For example, for:

```java
public abstract int foo() { ... }
```

return "public abstract".
Annotations are not included.

**Returns:** "public abstract".

---

#### modifiers

String

modifiers()

Get modifiers string.
For example, for:

```java
public abstract int foo() { ... }
```

return "public abstract".
Annotations are not included.

public abstract int foo() { ... }

annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.
Return an empty array if there are none.

**Returns:** the annotations of this program element.
**Since:** 1.5

---

#### annotations

AnnotationDesc

[] annotations()

Get the annotations of this program element.
Return an empty array if there are none.

isPublic

```java
boolean isPublic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is public.

**Returns:** true if this program element is public.

---

#### isPublic

boolean isPublic()

Return true if this program element is public.

isProtected

```java
boolean isProtected()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is protected.

**Returns:** true if this program element is protected.

---

#### isProtected

boolean isProtected()

Return true if this program element is protected.

isPrivate

```java
boolean isPrivate()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is private.

**Returns:** true if this program element is private.

---

#### isPrivate

boolean isPrivate()

Return true if this program element is private.

isPackagePrivate

```java
boolean isPackagePrivate()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is package private.

**Returns:** true if this program element is package private.

---

#### isPackagePrivate

boolean isPackagePrivate()

Return true if this program element is package private.

isStatic

```java
boolean isStatic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is static.

**Returns:** true if this program element is static.

---

#### isStatic

boolean isStatic()

Return true if this program element is static.

isFinal

```java
boolean isFinal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this program element is final.

**Returns:** true if this program element is final.

---

#### isFinal

boolean isFinal()

Return true if this program element is final.

---

