# Interface ExecutableMemberDoc

**Source:** `jdk.javadoc\com\sun\javadoc\ExecutableMemberDoc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ExecutableMemberDoc

extends
MemberDoc
```

Represents a method or constructor of a java class.

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

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

#### ClassDoc
[] thrownExceptions()

Return exceptions this method or constructor throws.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

The

thrownExceptions

method cannot
accommodate certain generic type constructs. The

thrownExceptionTypes

method should be used
instead.

**Returns:**
- an array of ClassDoc[] representing the exceptions
thrown by this method.

**See Also:**
- thrownExceptionTypes()

---

#### Type
[] thrownExceptionTypes()

Return exceptions this method or constructor throws.

**Returns:**
- an array representing the exceptions thrown by this method.
Each array element is either a

ClassDoc

or a

TypeVariable

.

**Since:**
- 1.5

---

#### boolean isNative()

Return true if this method is native

**Returns:**
- true if this method is native

---

#### boolean isSynchronized()

Return true if this method is synchronized

**Returns:**
- true if this method is synchronized

---

#### boolean isVarArgs()

Return true if this method was declared to take a variable number
of arguments.

**Returns:**
- true if this method was declared to take a variable number of arguments.

**Since:**
- 1.5

---

#### Parameter
[] parameters()

Get argument information.

**Returns:**
- an array of Parameter, one element per argument
in the order the arguments are present.

**See Also:**
- Parameter

---

#### Type
receiverType()

Get the receiver type of this executable element.

**Returns:**
- the receiver type of this executable element.

**Since:**
- 1.8

---

#### ThrowsTag
[] throwsTags()

Return the throws tags in this method.

**Returns:**
- an array of ThrowTag containing all

@exception

and

@throws

tags.

---

#### ParamTag
[] paramTags()

Return the param tags in this method, excluding the type
parameter tags.

**Returns:**
- an array of ParamTag containing all

@param

tags
corresponding to the parameters of this method.

---

#### ParamTag
[] typeParamTags()

Return the type parameter tags in this method.

**Returns:**
- an array of ParamTag containing all

@param

tags
corresponding to the type parameters of this method.

**Since:**
- 1.5

---

#### String
signature()

Get the signature. It is the parameter list, type is qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(java.lang.String,int)

.

**Returns:**
- the parameter list where type is qualified.

---

#### String
flatSignature()

get flat signature. all types are not qualified.
return a String, which is the flat signiture of this member.
It is the parameter list, type is not qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(String, int)

.

**Returns:**
- a String, which is the flat signiture of this member.

---

#### TypeVariable
[] typeParameters()

Return the formal type parameters of this method or constructor.
Return an empty array if this method or constructor is not generic.

**Returns:**
- the formal type parameters of this method or constructor.

**Since:**
- 1.5

---

### Additional Sections

#### Interface ExecutableMemberDoc

**All Superinterfaces:** Comparable

<

Object

>

,

Doc

,

MemberDoc

,

ProgramElementDoc

**All Known Subinterfaces:** AnnotationTypeElementDoc

,

ConstructorDoc

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
ExecutableMemberDoc

extends
MemberDoc
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a method or constructor of a java class.

**Since:** 1.2

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

ExecutableMemberDoc

extends

MemberDoc

Represents a method or constructor of a java class.

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

flatSignature

()

Deprecated, for removal: This API element is subject to removal in a future version.

get flat signature.

boolean

isNative

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is native

boolean

isSynchronized

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is synchronized

boolean

isVarArgs

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method was declared to take a variable number
of arguments.

Parameter

[]

parameters

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get argument information.

ParamTag

[]

paramTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the param tags in this method, excluding the type
parameter tags.

Type

receiverType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the receiver type of this executable element.

String

signature

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the signature.

ClassDoc

[]

thrownExceptions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.

Type

[]

thrownExceptionTypes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.

ThrowsTag

[]

throwsTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the throws tags in this method.

TypeVariable

[]

typeParameters

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this method or constructor.

ParamTag

[]

typeParamTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags in this method.

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

String

flatSignature

()

Deprecated, for removal: This API element is subject to removal in a future version.

get flat signature.

boolean

isNative

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is native

boolean

isSynchronized

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is synchronized

boolean

isVarArgs

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method was declared to take a variable number
of arguments.

Parameter

[]

parameters

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get argument information.

ParamTag

[]

paramTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the param tags in this method, excluding the type
parameter tags.

Type

receiverType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the receiver type of this executable element.

String

signature

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the signature.

ClassDoc

[]

thrownExceptions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.

Type

[]

thrownExceptionTypes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.

ThrowsTag

[]

throwsTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the throws tags in this method.

TypeVariable

[]

typeParameters

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this method or constructor.

ParamTag

[]

typeParamTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags in this method.

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

get flat signature.

Return true if this method is native

Return true if this method is synchronized

Return true if this method was declared to take a variable number
of arguments.

Get argument information.

Return the param tags in this method, excluding the type
parameter tags.

Get the receiver type of this executable element.

Get the signature.

Return exceptions this method or constructor throws.

Return the throws tags in this method.

Return the formal type parameters of this method or constructor.

Return the type parameter tags in this method.

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

- thrownExceptions

```java
ClassDoc
[] thrownExceptions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

The

thrownExceptions

method cannot
accommodate certain generic type constructs. The

thrownExceptionTypes

method should be used
instead.

**Returns:** an array of ClassDoc[] representing the exceptions
thrown by this method.
**See Also:** thrownExceptionTypes()

- thrownExceptionTypes

```java
Type
[] thrownExceptionTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.

**Returns:** an array representing the exceptions thrown by this method.
Each array element is either a

ClassDoc

or a

TypeVariable

.
**Since:** 1.5

- isNative

```java
boolean isNative()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is native

**Returns:** true if this method is native

- isSynchronized

```java
boolean isSynchronized()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is synchronized

**Returns:** true if this method is synchronized

- isVarArgs

```java
boolean isVarArgs()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method was declared to take a variable number
of arguments.

**Returns:** true if this method was declared to take a variable number of arguments.
**Since:** 1.5

- parameters

```java
Parameter
[] parameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get argument information.

**Returns:** an array of Parameter, one element per argument
in the order the arguments are present.
**See Also:** Parameter

- receiverType

```java
Type
receiverType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the receiver type of this executable element.

**Returns:** the receiver type of this executable element.
**Since:** 1.8

- throwsTags

```java
ThrowsTag
[] throwsTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the throws tags in this method.

**Returns:** an array of ThrowTag containing all

@exception

and

@throws

tags.

- paramTags

```java
ParamTag
[] paramTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the param tags in this method, excluding the type
parameter tags.

**Returns:** an array of ParamTag containing all

@param

tags
corresponding to the parameters of this method.

- typeParamTags

```java
ParamTag
[] typeParamTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags in this method.

**Returns:** an array of ParamTag containing all

@param

tags
corresponding to the type parameters of this method.
**Since:** 1.5

- signature

```java
String
signature()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the signature. It is the parameter list, type is qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(java.lang.String,int)

.

**Returns:** the parameter list where type is qualified.

- flatSignature

```java
String
flatSignature()
```

Deprecated, for removal: This API element is subject to removal in a future version.

get flat signature. all types are not qualified.
return a String, which is the flat signiture of this member.
It is the parameter list, type is not qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(String, int)

.

**Returns:** a String, which is the flat signiture of this member.

- typeParameters

```java
TypeVariable
[] typeParameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this method or constructor.
Return an empty array if this method or constructor is not generic.

**Returns:** the formal type parameters of this method or constructor.
**Since:** 1.5

Method Detail

- thrownExceptions

```java
ClassDoc
[] thrownExceptions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

The

thrownExceptions

method cannot
accommodate certain generic type constructs. The

thrownExceptionTypes

method should be used
instead.

**Returns:** an array of ClassDoc[] representing the exceptions
thrown by this method.
**See Also:** thrownExceptionTypes()

- thrownExceptionTypes

```java
Type
[] thrownExceptionTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.

**Returns:** an array representing the exceptions thrown by this method.
Each array element is either a

ClassDoc

or a

TypeVariable

.
**Since:** 1.5

- isNative

```java
boolean isNative()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is native

**Returns:** true if this method is native

- isSynchronized

```java
boolean isSynchronized()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is synchronized

**Returns:** true if this method is synchronized

- isVarArgs

```java
boolean isVarArgs()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method was declared to take a variable number
of arguments.

**Returns:** true if this method was declared to take a variable number of arguments.
**Since:** 1.5

- parameters

```java
Parameter
[] parameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get argument information.

**Returns:** an array of Parameter, one element per argument
in the order the arguments are present.
**See Also:** Parameter

- receiverType

```java
Type
receiverType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the receiver type of this executable element.

**Returns:** the receiver type of this executable element.
**Since:** 1.8

- throwsTags

```java
ThrowsTag
[] throwsTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the throws tags in this method.

**Returns:** an array of ThrowTag containing all

@exception

and

@throws

tags.

- paramTags

```java
ParamTag
[] paramTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the param tags in this method, excluding the type
parameter tags.

**Returns:** an array of ParamTag containing all

@param

tags
corresponding to the parameters of this method.

- typeParamTags

```java
ParamTag
[] typeParamTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags in this method.

**Returns:** an array of ParamTag containing all

@param

tags
corresponding to the type parameters of this method.
**Since:** 1.5

- signature

```java
String
signature()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the signature. It is the parameter list, type is qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(java.lang.String,int)

.

**Returns:** the parameter list where type is qualified.

- flatSignature

```java
String
flatSignature()
```

Deprecated, for removal: This API element is subject to removal in a future version.

get flat signature. all types are not qualified.
return a String, which is the flat signiture of this member.
It is the parameter list, type is not qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(String, int)

.

**Returns:** a String, which is the flat signiture of this member.

- typeParameters

```java
TypeVariable
[] typeParameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this method or constructor.
Return an empty array if this method or constructor is not generic.

**Returns:** the formal type parameters of this method or constructor.
**Since:** 1.5

---

#### Method Detail

thrownExceptions

```java
ClassDoc
[] thrownExceptions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

The

thrownExceptions

method cannot
accommodate certain generic type constructs. The

thrownExceptionTypes

method should be used
instead.

**Returns:** an array of ClassDoc[] representing the exceptions
thrown by this method.
**See Also:** thrownExceptionTypes()

---

#### thrownExceptions

ClassDoc

[] thrownExceptions()

Return exceptions this method or constructor throws.
If the type of the exception is a type variable, return the

ClassDoc

of its erasure.

The

thrownExceptions

method cannot
accommodate certain generic type constructs. The

thrownExceptionTypes

method should be used
instead.

The

thrownExceptions

method cannot
accommodate certain generic type constructs. The

thrownExceptionTypes

method should be used
instead.

thrownExceptionTypes

```java
Type
[] thrownExceptionTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return exceptions this method or constructor throws.

**Returns:** an array representing the exceptions thrown by this method.
Each array element is either a

ClassDoc

or a

TypeVariable

.
**Since:** 1.5

---

#### thrownExceptionTypes

Type

[] thrownExceptionTypes()

Return exceptions this method or constructor throws.

isNative

```java
boolean isNative()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is native

**Returns:** true if this method is native

---

#### isNative

boolean isNative()

Return true if this method is native

isSynchronized

```java
boolean isSynchronized()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method is synchronized

**Returns:** true if this method is synchronized

---

#### isSynchronized

boolean isSynchronized()

Return true if this method is synchronized

isVarArgs

```java
boolean isVarArgs()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this method was declared to take a variable number
of arguments.

**Returns:** true if this method was declared to take a variable number of arguments.
**Since:** 1.5

---

#### isVarArgs

boolean isVarArgs()

Return true if this method was declared to take a variable number
of arguments.

parameters

```java
Parameter
[] parameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get argument information.

**Returns:** an array of Parameter, one element per argument
in the order the arguments are present.
**See Also:** Parameter

---

#### parameters

Parameter

[] parameters()

Get argument information.

receiverType

```java
Type
receiverType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the receiver type of this executable element.

**Returns:** the receiver type of this executable element.
**Since:** 1.8

---

#### receiverType

Type

receiverType()

Get the receiver type of this executable element.

throwsTags

```java
ThrowsTag
[] throwsTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the throws tags in this method.

**Returns:** an array of ThrowTag containing all

@exception

and

@throws

tags.

---

#### throwsTags

ThrowsTag

[] throwsTags()

Return the throws tags in this method.

paramTags

```java
ParamTag
[] paramTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the param tags in this method, excluding the type
parameter tags.

**Returns:** an array of ParamTag containing all

@param

tags
corresponding to the parameters of this method.

---

#### paramTags

ParamTag

[] paramTags()

Return the param tags in this method, excluding the type
parameter tags.

typeParamTags

```java
ParamTag
[] typeParamTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type parameter tags in this method.

**Returns:** an array of ParamTag containing all

@param

tags
corresponding to the type parameters of this method.
**Since:** 1.5

---

#### typeParamTags

ParamTag

[] typeParamTags()

Return the type parameter tags in this method.

signature

```java
String
signature()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the signature. It is the parameter list, type is qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(java.lang.String,int)

.

**Returns:** the parameter list where type is qualified.

---

#### signature

String

signature()

Get the signature. It is the parameter list, type is qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(java.lang.String,int)

.

flatSignature

```java
String
flatSignature()
```

Deprecated, for removal: This API element is subject to removal in a future version.

get flat signature. all types are not qualified.
return a String, which is the flat signiture of this member.
It is the parameter list, type is not qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(String, int)

.

**Returns:** a String, which is the flat signiture of this member.

---

#### flatSignature

String

flatSignature()

get flat signature. all types are not qualified.
return a String, which is the flat signiture of this member.
It is the parameter list, type is not qualified.
For instance, for a method

mymethod(String x, int y)

,
it will return

(String, int)

.

typeParameters

```java
TypeVariable
[] typeParameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the formal type parameters of this method or constructor.
Return an empty array if this method or constructor is not generic.

**Returns:** the formal type parameters of this method or constructor.
**Since:** 1.5

---

#### typeParameters

TypeVariable

[] typeParameters()

Return the formal type parameters of this method or constructor.
Return an empty array if this method or constructor is not generic.

---

