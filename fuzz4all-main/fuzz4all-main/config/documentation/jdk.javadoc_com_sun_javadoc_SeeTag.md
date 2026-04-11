# Interface SeeTag

**Source:** `jdk.javadoc\com\sun\javadoc\SeeTag.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
SeeTag

extends
Tag
```

Represents a user-defined cross-reference to related documentation.
The tag can reference a package, class or member, or can hold
plain text. (The plain text might be a reference
to something not online, such as a printed book, or be a hard-coded
HTML link.) The reference can either be inline with the comment,
using

{@link}

, or a separate block comment,
using

@see

.
Method

name()

returns "@link" (no curly braces) or
"@see", depending on the tag.
Method

kind()

returns "@see" for both tags.

**All Superinterfaces:** Tag

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
label()

Get the label of the

@see

tag.
Return null if no label is present.
For example, for:

@see String#trim() the trim method

return "the trim method".

**Returns:**
- "the trim method".

---

#### PackageDoc
referencedPackage()

Get the package doc when

@see

references only a package.
Return null if the package cannot be found, or if

@see

references any other element (class,
interface, field, constructor, method) or non-element.
For example, for:

@see java.lang

return the

PackageDoc

for

java.lang

.

**Returns:**
- the

PackageDoc

for

java.lang

.

---

#### String
referencedClassName()

Get the class or interface name of the

@see

reference.
The name is fully qualified if the name specified in the
original

@see

tag was fully qualified, or if the class
or interface can be found; otherwise it is unqualified.
If

@see

references only a package name, then return
the package name instead.
For example, for:

@see String#valueOf(java.lang.Object)

return "java.lang.String".
For "

@see java.lang

", return "java.lang".
Return null if

@see

references a non-element, such as

@see <a href="java.sun.com">

.

**Returns:**
- null if

@see

references a non-element, such as

@see <a href="java.sun.com">

.

---

#### ClassDoc
referencedClass()

Get the class doc referenced by the class name part of @see.
Return null if the class cannot be found.
For example, for:

@see String#valueOf(java.lang.Object)

return the

ClassDoc

for

java.lang.String

.

**Returns:**
- the

ClassDoc

for

java.lang.String

.

---

#### String
referencedMemberName()

Get the field, constructor or method substring of the

@see

reference. Return null if the reference is to any other
element or to any non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(String)

return "startsWith(String)".

**Returns:**
- "startsWith(String)".

---

#### MemberDoc
referencedMember()

Get the member doc for the field, constructor or method
referenced by

@see

. Return null if the member cannot
be found or if the reference is to any other element or to any
non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(java.lang.String)

return the

MethodDoc

for

startsWith

.

**Returns:**
- the

MethodDoc

for

startsWith

.

---

### Additional Sections

#### Interface SeeTag

**All Superinterfaces:** Tag

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
SeeTag

extends
Tag
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a user-defined cross-reference to related documentation.
The tag can reference a package, class or member, or can hold
plain text. (The plain text might be a reference
to something not online, such as a printed book, or be a hard-coded
HTML link.) The reference can either be inline with the comment,
using

{@link}

, or a separate block comment,
using

@see

.
Method

name()

returns "@link" (no curly braces) or
"@see", depending on the tag.
Method

kind()

returns "@see" for both tags.

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

SeeTag

extends

Tag

Represents a user-defined cross-reference to related documentation.
The tag can reference a package, class or member, or can hold
plain text. (The plain text might be a reference
to something not online, such as a printed book, or be a hard-coded
HTML link.) The reference can either be inline with the comment,
using

{@link}

, or a separate block comment,
using

@see

.
Method

name()

returns "@link" (no curly braces) or
"@see", depending on the tag.
Method

kind()

returns "@see" for both tags.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

String

label

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the label of the

@see

tag.

ClassDoc

referencedClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class doc referenced by the class name part of @see.

String

referencedClassName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class or interface name of the

@see

reference.

MemberDoc

referencedMember

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the member doc for the field, constructor or method
referenced by

@see

.

String

referencedMemberName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the field, constructor or method substring of the

@see

reference.

PackageDoc

referencedPackage

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package doc when

@see

references only a package.

- Methods declared in interface com.sun.javadoc.

Tag

firstSentenceTags

,

holder

,

inlineTags

,

kind

,

name

,

position

,

text

,

toString

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

String

label

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the label of the

@see

tag.

ClassDoc

referencedClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class doc referenced by the class name part of @see.

String

referencedClassName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class or interface name of the

@see

reference.

MemberDoc

referencedMember

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the member doc for the field, constructor or method
referenced by

@see

.

String

referencedMemberName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the field, constructor or method substring of the

@see

reference.

PackageDoc

referencedPackage

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package doc when

@see

references only a package.

- Methods declared in interface com.sun.javadoc.

Tag

firstSentenceTags

,

holder

,

inlineTags

,

kind

,

name

,

position

,

text

,

toString

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Get the label of the

@see

tag.

Get the class doc referenced by the class name part of @see.

Get the class or interface name of the

@see

reference.

Get the member doc for the field, constructor or method
referenced by

@see

.

Get the field, constructor or method substring of the

@see

reference.

Get the package doc when

@see

references only a package.

Methods declared in interface com.sun.javadoc.

Tag

firstSentenceTags

,

holder

,

inlineTags

,

kind

,

name

,

position

,

text

,

toString

---

#### Methods declared in interface com.sun.javadoc. Tag

============ METHOD DETAIL ==========

- Method Detail

- label

```java
String
label()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the label of the

@see

tag.
Return null if no label is present.
For example, for:

@see String#trim() the trim method

return "the trim method".

**Returns:** "the trim method".

- referencedPackage

```java
PackageDoc
referencedPackage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package doc when

@see

references only a package.
Return null if the package cannot be found, or if

@see

references any other element (class,
interface, field, constructor, method) or non-element.
For example, for:

@see java.lang

return the

PackageDoc

for

java.lang

.

**Returns:** the

PackageDoc

for

java.lang

.

- referencedClassName

```java
String
referencedClassName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class or interface name of the

@see

reference.
The name is fully qualified if the name specified in the
original

@see

tag was fully qualified, or if the class
or interface can be found; otherwise it is unqualified.
If

@see

references only a package name, then return
the package name instead.
For example, for:

@see String#valueOf(java.lang.Object)

return "java.lang.String".
For "

@see java.lang

", return "java.lang".
Return null if

@see

references a non-element, such as

@see <a href="java.sun.com">

.

**Returns:** null if

@see

references a non-element, such as

@see <a href="java.sun.com">

.

- referencedClass

```java
ClassDoc
referencedClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class doc referenced by the class name part of @see.
Return null if the class cannot be found.
For example, for:

@see String#valueOf(java.lang.Object)

return the

ClassDoc

for

java.lang.String

.

**Returns:** the

ClassDoc

for

java.lang.String

.

- referencedMemberName

```java
String
referencedMemberName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the field, constructor or method substring of the

@see

reference. Return null if the reference is to any other
element or to any non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(String)

return "startsWith(String)".

**Returns:** "startsWith(String)".

- referencedMember

```java
MemberDoc
referencedMember()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the member doc for the field, constructor or method
referenced by

@see

. Return null if the member cannot
be found or if the reference is to any other element or to any
non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(java.lang.String)

return the

MethodDoc

for

startsWith

.

**Returns:** the

MethodDoc

for

startsWith

.

Method Detail

- label

```java
String
label()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the label of the

@see

tag.
Return null if no label is present.
For example, for:

@see String#trim() the trim method

return "the trim method".

**Returns:** "the trim method".

- referencedPackage

```java
PackageDoc
referencedPackage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package doc when

@see

references only a package.
Return null if the package cannot be found, or if

@see

references any other element (class,
interface, field, constructor, method) or non-element.
For example, for:

@see java.lang

return the

PackageDoc

for

java.lang

.

**Returns:** the

PackageDoc

for

java.lang

.

- referencedClassName

```java
String
referencedClassName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class or interface name of the

@see

reference.
The name is fully qualified if the name specified in the
original

@see

tag was fully qualified, or if the class
or interface can be found; otherwise it is unqualified.
If

@see

references only a package name, then return
the package name instead.
For example, for:

@see String#valueOf(java.lang.Object)

return "java.lang.String".
For "

@see java.lang

", return "java.lang".
Return null if

@see

references a non-element, such as

@see <a href="java.sun.com">

.

**Returns:** null if

@see

references a non-element, such as

@see <a href="java.sun.com">

.

- referencedClass

```java
ClassDoc
referencedClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class doc referenced by the class name part of @see.
Return null if the class cannot be found.
For example, for:

@see String#valueOf(java.lang.Object)

return the

ClassDoc

for

java.lang.String

.

**Returns:** the

ClassDoc

for

java.lang.String

.

- referencedMemberName

```java
String
referencedMemberName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the field, constructor or method substring of the

@see

reference. Return null if the reference is to any other
element or to any non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(String)

return "startsWith(String)".

**Returns:** "startsWith(String)".

- referencedMember

```java
MemberDoc
referencedMember()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the member doc for the field, constructor or method
referenced by

@see

. Return null if the member cannot
be found or if the reference is to any other element or to any
non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(java.lang.String)

return the

MethodDoc

for

startsWith

.

**Returns:** the

MethodDoc

for

startsWith

.

---

#### Method Detail

label

```java
String
label()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the label of the

@see

tag.
Return null if no label is present.
For example, for:

@see String#trim() the trim method

return "the trim method".

**Returns:** "the trim method".

---

#### label

String

label()

Get the label of the

@see

tag.
Return null if no label is present.
For example, for:

@see String#trim() the trim method

return "the trim method".

@see String#trim() the trim method

referencedPackage

```java
PackageDoc
referencedPackage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the package doc when

@see

references only a package.
Return null if the package cannot be found, or if

@see

references any other element (class,
interface, field, constructor, method) or non-element.
For example, for:

@see java.lang

return the

PackageDoc

for

java.lang

.

**Returns:** the

PackageDoc

for

java.lang

.

---

#### referencedPackage

PackageDoc

referencedPackage()

Get the package doc when

@see

references only a package.
Return null if the package cannot be found, or if

@see

references any other element (class,
interface, field, constructor, method) or non-element.
For example, for:

@see java.lang

return the

PackageDoc

for

java.lang

.

@see java.lang

referencedClassName

```java
String
referencedClassName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class or interface name of the

@see

reference.
The name is fully qualified if the name specified in the
original

@see

tag was fully qualified, or if the class
or interface can be found; otherwise it is unqualified.
If

@see

references only a package name, then return
the package name instead.
For example, for:

@see String#valueOf(java.lang.Object)

return "java.lang.String".
For "

@see java.lang

", return "java.lang".
Return null if

@see

references a non-element, such as

@see <a href="java.sun.com">

.

**Returns:** null if

@see

references a non-element, such as

@see <a href="java.sun.com">

.

---

#### referencedClassName

String

referencedClassName()

Get the class or interface name of the

@see

reference.
The name is fully qualified if the name specified in the
original

@see

tag was fully qualified, or if the class
or interface can be found; otherwise it is unqualified.
If

@see

references only a package name, then return
the package name instead.
For example, for:

@see String#valueOf(java.lang.Object)

return "java.lang.String".
For "

@see java.lang

", return "java.lang".
Return null if

@see

references a non-element, such as

@see <a href="java.sun.com">

.

@see String#valueOf(java.lang.Object)

referencedClass

```java
ClassDoc
referencedClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the class doc referenced by the class name part of @see.
Return null if the class cannot be found.
For example, for:

@see String#valueOf(java.lang.Object)

return the

ClassDoc

for

java.lang.String

.

**Returns:** the

ClassDoc

for

java.lang.String

.

---

#### referencedClass

ClassDoc

referencedClass()

Get the class doc referenced by the class name part of @see.
Return null if the class cannot be found.
For example, for:

@see String#valueOf(java.lang.Object)

return the

ClassDoc

for

java.lang.String

.

@see String#valueOf(java.lang.Object)

referencedMemberName

```java
String
referencedMemberName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the field, constructor or method substring of the

@see

reference. Return null if the reference is to any other
element or to any non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(String)

return "startsWith(String)".

**Returns:** "startsWith(String)".

---

#### referencedMemberName

String

referencedMemberName()

Get the field, constructor or method substring of the

@see

reference. Return null if the reference is to any other
element or to any non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(String)

return "startsWith(String)".

@see String#startsWith(String)

referencedMember

```java
MemberDoc
referencedMember()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the member doc for the field, constructor or method
referenced by

@see

. Return null if the member cannot
be found or if the reference is to any other element or to any
non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(java.lang.String)

return the

MethodDoc

for

startsWith

.

**Returns:** the

MethodDoc

for

startsWith

.

---

#### referencedMember

MemberDoc

referencedMember()

Get the member doc for the field, constructor or method
referenced by

@see

. Return null if the member cannot
be found or if the reference is to any other element or to any
non-element.
References to member classes (nested classes) return null.
For example, for:

@see String#startsWith(java.lang.String)

return the

MethodDoc

for

startsWith

.

@see String#startsWith(java.lang.String)

---

