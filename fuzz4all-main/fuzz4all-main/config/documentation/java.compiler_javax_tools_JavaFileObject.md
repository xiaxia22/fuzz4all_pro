# Interface JavaFileObject

**Source:** `java.compiler\javax\tools\JavaFileObject.html`

### Class Description

```java
public interface
JavaFileObject

extends
FileObject
```

File abstraction for tools operating on Java™ programming language
source and class files.

All methods in this interface might throw a SecurityException if
a security exception occurs.

Unless explicitly allowed, all methods in this interface might
throw a NullPointerException if given a

null

argument.

**All Superinterfaces:** FileObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### JavaFileObject.Kind
getKind()

Returns the kind of this file object.

**Returns:**
- the kind

---

#### boolean isNameCompatible​(
String
simpleName,

JavaFileObject.Kind
kind)

Checks if this file object is compatible with the specified
simple name and kind. A simple name is a single identifier
(not qualified) as defined in

The Java™ Language Specification

,
section 6.2 "Names and Identifiers".

**Parameters:**
- simpleName

- a simple name of a class
- kind

- a kind

**Returns:**
- true

if this file object is compatible; false
otherwise

---

#### NestingKind
getNestingKind()

Provides a hint about the nesting level of the class
represented by this file object. This method may return

NestingKind.MEMBER

to mean

NestingKind.LOCAL

or

NestingKind.ANONYMOUS

.
If the nesting level is not known or this file object does not
represent a class file this method returns

null

.

**Returns:**
- the nesting kind, or

null

if the nesting kind
is not known

---

#### Modifier
getAccessLevel()

Provides a hint about the access level of the class represented
by this file object. If the access level is not known or if
this file object does not represent a class file this method
returns

null

.

**Returns:**
- the access level

---

### Additional Sections

#### Interface JavaFileObject

**All Superinterfaces:** FileObject

**All Known Implementing Classes:** ForwardingJavaFileObject

,

SimpleJavaFileObject

```java
public interface
JavaFileObject

extends
FileObject
```

File abstraction for tools operating on Java™ programming language
source and class files.

All methods in this interface might throw a SecurityException if
a security exception occurs.

Unless explicitly allowed, all methods in this interface might
throw a NullPointerException if given a

null

argument.

**Since:** 1.6
**See Also:** JavaFileManager

public interface

JavaFileObject

extends

FileObject

File abstraction for tools operating on Java™ programming language
source and class files.

All methods in this interface might throw a SecurityException if
a security exception occurs.

Unless explicitly allowed, all methods in this interface might
throw a NullPointerException if given a

null

argument.

All methods in this interface might throw a SecurityException if
a security exception occurs.

Unless explicitly allowed, all methods in this interface might
throw a NullPointerException if given a

null

argument.

Unless explicitly allowed, all methods in this interface might
throw a NullPointerException if given a

null

argument.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

JavaFileObject.Kind

Kinds of JavaFileObjects.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Modifier

getAccessLevel

()

Provides a hint about the access level of the class represented
by this file object.

JavaFileObject.Kind

getKind

()

Returns the kind of this file object.

NestingKind

getNestingKind

()

Provides a hint about the nesting level of the class
represented by this file object.

boolean

isNameCompatible

​(

String

simpleName,

JavaFileObject.Kind

kind)

Checks if this file object is compatible with the specified
simple name and kind.

- Methods declared in interface javax.tools.

FileObject

delete

,

getCharContent

,

getLastModified

,

getName

,

openInputStream

,

openOutputStream

,

openReader

,

openWriter

,

toUri

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

JavaFileObject.Kind

Kinds of JavaFileObjects.

---

#### Nested Class Summary

Kinds of JavaFileObjects.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Modifier

getAccessLevel

()

Provides a hint about the access level of the class represented
by this file object.

JavaFileObject.Kind

getKind

()

Returns the kind of this file object.

NestingKind

getNestingKind

()

Provides a hint about the nesting level of the class
represented by this file object.

boolean

isNameCompatible

​(

String

simpleName,

JavaFileObject.Kind

kind)

Checks if this file object is compatible with the specified
simple name and kind.

- Methods declared in interface javax.tools.

FileObject

delete

,

getCharContent

,

getLastModified

,

getName

,

openInputStream

,

openOutputStream

,

openReader

,

openWriter

,

toUri

---

#### Method Summary

Provides a hint about the access level of the class represented
by this file object.

Returns the kind of this file object.

Provides a hint about the nesting level of the class
represented by this file object.

Checks if this file object is compatible with the specified
simple name and kind.

Methods declared in interface javax.tools.

FileObject

delete

,

getCharContent

,

getLastModified

,

getName

,

openInputStream

,

openOutputStream

,

openReader

,

openWriter

,

toUri

---

#### Methods declared in interface javax.tools. FileObject

============ METHOD DETAIL ==========

- Method Detail

- getKind

```java
JavaFileObject.Kind
getKind()
```

Returns the kind of this file object.

**Returns:** the kind

- isNameCompatible

```java
boolean isNameCompatible​(
String
simpleName,

JavaFileObject.Kind
kind)
```

Checks if this file object is compatible with the specified
simple name and kind. A simple name is a single identifier
(not qualified) as defined in

The Java™ Language Specification

,
section 6.2 "Names and Identifiers".

**Parameters:** simpleName

- a simple name of a class
**Parameters:** kind

- a kind
**Returns:** true

if this file object is compatible; false
otherwise

- getNestingKind

```java
NestingKind
getNestingKind()
```

Provides a hint about the nesting level of the class
represented by this file object. This method may return

NestingKind.MEMBER

to mean

NestingKind.LOCAL

or

NestingKind.ANONYMOUS

.
If the nesting level is not known or this file object does not
represent a class file this method returns

null

.

**Returns:** the nesting kind, or

null

if the nesting kind
is not known

- getAccessLevel

```java
Modifier
getAccessLevel()
```

Provides a hint about the access level of the class represented
by this file object. If the access level is not known or if
this file object does not represent a class file this method
returns

null

.

**Returns:** the access level

Method Detail

- getKind

```java
JavaFileObject.Kind
getKind()
```

Returns the kind of this file object.

**Returns:** the kind

- isNameCompatible

```java
boolean isNameCompatible​(
String
simpleName,

JavaFileObject.Kind
kind)
```

Checks if this file object is compatible with the specified
simple name and kind. A simple name is a single identifier
(not qualified) as defined in

The Java™ Language Specification

,
section 6.2 "Names and Identifiers".

**Parameters:** simpleName

- a simple name of a class
**Parameters:** kind

- a kind
**Returns:** true

if this file object is compatible; false
otherwise

- getNestingKind

```java
NestingKind
getNestingKind()
```

Provides a hint about the nesting level of the class
represented by this file object. This method may return

NestingKind.MEMBER

to mean

NestingKind.LOCAL

or

NestingKind.ANONYMOUS

.
If the nesting level is not known or this file object does not
represent a class file this method returns

null

.

**Returns:** the nesting kind, or

null

if the nesting kind
is not known

- getAccessLevel

```java
Modifier
getAccessLevel()
```

Provides a hint about the access level of the class represented
by this file object. If the access level is not known or if
this file object does not represent a class file this method
returns

null

.

**Returns:** the access level

---

#### Method Detail

getKind

```java
JavaFileObject.Kind
getKind()
```

Returns the kind of this file object.

**Returns:** the kind

---

#### getKind

JavaFileObject.Kind

getKind()

Returns the kind of this file object.

isNameCompatible

```java
boolean isNameCompatible​(
String
simpleName,

JavaFileObject.Kind
kind)
```

Checks if this file object is compatible with the specified
simple name and kind. A simple name is a single identifier
(not qualified) as defined in

The Java™ Language Specification

,
section 6.2 "Names and Identifiers".

**Parameters:** simpleName

- a simple name of a class
**Parameters:** kind

- a kind
**Returns:** true

if this file object is compatible; false
otherwise

---

#### isNameCompatible

boolean isNameCompatible​(

String

simpleName,

JavaFileObject.Kind

kind)

Checks if this file object is compatible with the specified
simple name and kind. A simple name is a single identifier
(not qualified) as defined in

The Java™ Language Specification

,
section 6.2 "Names and Identifiers".

getNestingKind

```java
NestingKind
getNestingKind()
```

Provides a hint about the nesting level of the class
represented by this file object. This method may return

NestingKind.MEMBER

to mean

NestingKind.LOCAL

or

NestingKind.ANONYMOUS

.
If the nesting level is not known or this file object does not
represent a class file this method returns

null

.

**Returns:** the nesting kind, or

null

if the nesting kind
is not known

---

#### getNestingKind

NestingKind

getNestingKind()

Provides a hint about the nesting level of the class
represented by this file object. This method may return

NestingKind.MEMBER

to mean

NestingKind.LOCAL

or

NestingKind.ANONYMOUS

.
If the nesting level is not known or this file object does not
represent a class file this method returns

null

.

getAccessLevel

```java
Modifier
getAccessLevel()
```

Provides a hint about the access level of the class represented
by this file object. If the access level is not known or if
this file object does not represent a class file this method
returns

null

.

**Returns:** the access level

---

#### getAccessLevel

Modifier

getAccessLevel()

Provides a hint about the access level of the class represented
by this file object. If the access level is not known or if
this file object does not represent a class file this method
returns

null

.

---

