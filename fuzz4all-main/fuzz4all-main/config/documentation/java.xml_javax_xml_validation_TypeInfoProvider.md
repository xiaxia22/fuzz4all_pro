# Class TypeInfoProvider

**Source:** `java.xml\javax\xml\validation\TypeInfoProvider.html`

### Class Description

```java
public abstract class
TypeInfoProvider

extends
Object
```

This class provides access to the type information determined
by

ValidatorHandler

.

Some schema languages, such as W3C XML Schema, encourages a validator
to report the "type" it assigns to each attribute/element.
Those applications who wish to access this type information can invoke
methods defined on this "interface" to access such type information.

Implementation of this "interface" can be obtained through the

ValidatorHandler.getTypeInfoProvider()

method.

**Since:** 1.5
**See Also:** TypeInfo

---

### Field Details

*No entries found.*

### Constructor Details

#### protected TypeInfoProvider()

Constructor for the derived class.

The constructor does nothing.

---

### Method Details

#### public abstract
TypeInfo
getElementTypeInfo()

Returns the immutable

TypeInfo

object for the current
element.

The method may only be called by the startElement event
or the endElement event
of the

ContentHandler

that the application sets to
the

ValidatorHandler

.

When W3C XML Schema validation is being performed, in the
case where an element has a union type, the

TypeInfo

returned by a call to

getElementTypeInfo()

from the
startElement
event will be the union type. The

TypeInfo

returned by a call
from the endElement event will be the actual member type used
to validate the element.

**Returns:**
- An immutable

TypeInfo

object that represents the
type of the current element.
Note that the caller can keep references to the obtained

TypeInfo

longer than the callback scope.

Otherwise, this method returns
null if the validator is unable to
determine the type of the current element for some reason
(for example, if the validator is recovering from
an earlier error.)

**Throws:**
- IllegalStateException

- If this method is called from other

ContentHandler

methods.

---

#### public abstract
TypeInfo
getAttributeTypeInfo​(int index)

Returns the immutable

TypeInfo

object for the specified
attribute of the current element.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

**Parameters:**
- index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.

**Returns:**
- An immutable

TypeInfo

object that represents the
type of the specified attribute.
Note that the caller can keep references to the obtained

TypeInfo

longer than the callback scope.

Otherwise, this method returns
null if the validator is unable to
determine the type.

**Throws:**
- IndexOutOfBoundsException

- If the index is invalid.
- IllegalStateException

- If this method is called from other

ContentHandler

methods.

---

#### public abstract boolean isIdAttribute​(int index)

Returns

true

if the specified attribute is determined
to be ID.

Exacly how an attribute is "determined to be ID" is up to the
schema language. In case of W3C XML Schema, this means
that the actual type of the attribute is the built-in ID type
or its derived type.

A

DocumentBuilder

uses this information
to properly implement

Attr.isId()

.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

**Parameters:**
- index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.

**Returns:**
- true
if the type of the specified attribute is ID.

**Throws:**
- IndexOutOfBoundsException

- If the index is invalid.
- IllegalStateException

- If this method is called from other

ContentHandler

methods.

---

#### public abstract boolean isSpecified​(int index)

Returns

false

if the attribute was added by the validator.

This method provides information necessary for
a

DocumentBuilder

to determine what
the DOM tree should return from the

Attr.getSpecified()

method.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

A general guideline for validators is to return true if
the attribute was originally present in the pipeline, and
false if it was added by the validator.

**Parameters:**
- index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.

**Returns:**
- true

if the attribute was present before the validator
processes input.

false

if the attribute was added
by the validator.

**Throws:**
- IndexOutOfBoundsException

- If the index is invalid.
- IllegalStateException

- If this method is called from other

ContentHandler

methods.

---

### Additional Sections

#### Class TypeInfoProvider

java.lang.Object

- javax.xml.validation.TypeInfoProvider

javax.xml.validation.TypeInfoProvider

```java
public abstract class
TypeInfoProvider

extends
Object
```

This class provides access to the type information determined
by

ValidatorHandler

.

Some schema languages, such as W3C XML Schema, encourages a validator
to report the "type" it assigns to each attribute/element.
Those applications who wish to access this type information can invoke
methods defined on this "interface" to access such type information.

Implementation of this "interface" can be obtained through the

ValidatorHandler.getTypeInfoProvider()

method.

**Since:** 1.5
**See Also:** TypeInfo

public abstract class

TypeInfoProvider

extends

Object

This class provides access to the type information determined
by

ValidatorHandler

.

Some schema languages, such as W3C XML Schema, encourages a validator
to report the "type" it assigns to each attribute/element.
Those applications who wish to access this type information can invoke
methods defined on this "interface" to access such type information.

Implementation of this "interface" can be obtained through the

ValidatorHandler.getTypeInfoProvider()

method.

Some schema languages, such as W3C XML Schema, encourages a validator
to report the "type" it assigns to each attribute/element.
Those applications who wish to access this type information can invoke
methods defined on this "interface" to access such type information.

Implementation of this "interface" can be obtained through the

ValidatorHandler.getTypeInfoProvider()

method.

Implementation of this "interface" can be obtained through the

ValidatorHandler.getTypeInfoProvider()

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TypeInfoProvider

()

Constructor for the derived class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

TypeInfo

getAttributeTypeInfo

​(int index)

Returns the immutable

TypeInfo

object for the specified
attribute of the current element.

abstract

TypeInfo

getElementTypeInfo

()

Returns the immutable

TypeInfo

object for the current
element.

abstract boolean

isIdAttribute

​(int index)

Returns

true

if the specified attribute is determined
to be ID.

abstract boolean

isSpecified

​(int index)

Returns

false

if the attribute was added by the validator.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TypeInfoProvider

()

Constructor for the derived class.

---

#### Constructor Summary

Constructor for the derived class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

TypeInfo

getAttributeTypeInfo

​(int index)

Returns the immutable

TypeInfo

object for the specified
attribute of the current element.

abstract

TypeInfo

getElementTypeInfo

()

Returns the immutable

TypeInfo

object for the current
element.

abstract boolean

isIdAttribute

​(int index)

Returns

true

if the specified attribute is determined
to be ID.

abstract boolean

isSpecified

​(int index)

Returns

false

if the attribute was added by the validator.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the immutable

TypeInfo

object for the specified
attribute of the current element.

Returns the immutable

TypeInfo

object for the current
element.

Returns

true

if the specified attribute is determined
to be ID.

Returns

false

if the attribute was added by the validator.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TypeInfoProvider

```java
protected TypeInfoProvider()
```

Constructor for the derived class.

The constructor does nothing.

============ METHOD DETAIL ==========

- Method Detail

- getElementTypeInfo

```java
public abstract
TypeInfo
getElementTypeInfo()
```

Returns the immutable

TypeInfo

object for the current
element.

The method may only be called by the startElement event
or the endElement event
of the

ContentHandler

that the application sets to
the

ValidatorHandler

.

When W3C XML Schema validation is being performed, in the
case where an element has a union type, the

TypeInfo

returned by a call to

getElementTypeInfo()

from the
startElement
event will be the union type. The

TypeInfo

returned by a call
from the endElement event will be the actual member type used
to validate the element.

**Returns:** An immutable

TypeInfo

object that represents the
type of the current element.
Note that the caller can keep references to the obtained

TypeInfo

longer than the callback scope.

Otherwise, this method returns
null if the validator is unable to
determine the type of the current element for some reason
(for example, if the validator is recovering from
an earlier error.)
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

- getAttributeTypeInfo

```java
public abstract
TypeInfo
getAttributeTypeInfo​(int index)
```

Returns the immutable

TypeInfo

object for the specified
attribute of the current element.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

**Parameters:** index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.
**Returns:** An immutable

TypeInfo

object that represents the
type of the specified attribute.
Note that the caller can keep references to the obtained

TypeInfo

longer than the callback scope.

Otherwise, this method returns
null if the validator is unable to
determine the type.
**Throws:** IndexOutOfBoundsException

- If the index is invalid.
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

- isIdAttribute

```java
public abstract boolean isIdAttribute​(int index)
```

Returns

true

if the specified attribute is determined
to be ID.

Exacly how an attribute is "determined to be ID" is up to the
schema language. In case of W3C XML Schema, this means
that the actual type of the attribute is the built-in ID type
or its derived type.

A

DocumentBuilder

uses this information
to properly implement

Attr.isId()

.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

**Parameters:** index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.
**Returns:** true
if the type of the specified attribute is ID.
**Throws:** IndexOutOfBoundsException

- If the index is invalid.
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

- isSpecified

```java
public abstract boolean isSpecified​(int index)
```

Returns

false

if the attribute was added by the validator.

This method provides information necessary for
a

DocumentBuilder

to determine what
the DOM tree should return from the

Attr.getSpecified()

method.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

A general guideline for validators is to return true if
the attribute was originally present in the pipeline, and
false if it was added by the validator.

**Parameters:** index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.
**Returns:** true

if the attribute was present before the validator
processes input.

false

if the attribute was added
by the validator.
**Throws:** IndexOutOfBoundsException

- If the index is invalid.
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

Constructor Detail

- TypeInfoProvider

```java
protected TypeInfoProvider()
```

Constructor for the derived class.

The constructor does nothing.

---

#### Constructor Detail

TypeInfoProvider

```java
protected TypeInfoProvider()
```

Constructor for the derived class.

The constructor does nothing.

---

#### TypeInfoProvider

protected TypeInfoProvider()

Constructor for the derived class.

The constructor does nothing.

The constructor does nothing.

Method Detail

- getElementTypeInfo

```java
public abstract
TypeInfo
getElementTypeInfo()
```

Returns the immutable

TypeInfo

object for the current
element.

The method may only be called by the startElement event
or the endElement event
of the

ContentHandler

that the application sets to
the

ValidatorHandler

.

When W3C XML Schema validation is being performed, in the
case where an element has a union type, the

TypeInfo

returned by a call to

getElementTypeInfo()

from the
startElement
event will be the union type. The

TypeInfo

returned by a call
from the endElement event will be the actual member type used
to validate the element.

**Returns:** An immutable

TypeInfo

object that represents the
type of the current element.
Note that the caller can keep references to the obtained

TypeInfo

longer than the callback scope.

Otherwise, this method returns
null if the validator is unable to
determine the type of the current element for some reason
(for example, if the validator is recovering from
an earlier error.)
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

- getAttributeTypeInfo

```java
public abstract
TypeInfo
getAttributeTypeInfo​(int index)
```

Returns the immutable

TypeInfo

object for the specified
attribute of the current element.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

**Parameters:** index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.
**Returns:** An immutable

TypeInfo

object that represents the
type of the specified attribute.
Note that the caller can keep references to the obtained

TypeInfo

longer than the callback scope.

Otherwise, this method returns
null if the validator is unable to
determine the type.
**Throws:** IndexOutOfBoundsException

- If the index is invalid.
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

- isIdAttribute

```java
public abstract boolean isIdAttribute​(int index)
```

Returns

true

if the specified attribute is determined
to be ID.

Exacly how an attribute is "determined to be ID" is up to the
schema language. In case of W3C XML Schema, this means
that the actual type of the attribute is the built-in ID type
or its derived type.

A

DocumentBuilder

uses this information
to properly implement

Attr.isId()

.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

**Parameters:** index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.
**Returns:** true
if the type of the specified attribute is ID.
**Throws:** IndexOutOfBoundsException

- If the index is invalid.
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

- isSpecified

```java
public abstract boolean isSpecified​(int index)
```

Returns

false

if the attribute was added by the validator.

This method provides information necessary for
a

DocumentBuilder

to determine what
the DOM tree should return from the

Attr.getSpecified()

method.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

A general guideline for validators is to return true if
the attribute was originally present in the pipeline, and
false if it was added by the validator.

**Parameters:** index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.
**Returns:** true

if the attribute was present before the validator
processes input.

false

if the attribute was added
by the validator.
**Throws:** IndexOutOfBoundsException

- If the index is invalid.
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

---

#### Method Detail

getElementTypeInfo

```java
public abstract
TypeInfo
getElementTypeInfo()
```

Returns the immutable

TypeInfo

object for the current
element.

The method may only be called by the startElement event
or the endElement event
of the

ContentHandler

that the application sets to
the

ValidatorHandler

.

When W3C XML Schema validation is being performed, in the
case where an element has a union type, the

TypeInfo

returned by a call to

getElementTypeInfo()

from the
startElement
event will be the union type. The

TypeInfo

returned by a call
from the endElement event will be the actual member type used
to validate the element.

**Returns:** An immutable

TypeInfo

object that represents the
type of the current element.
Note that the caller can keep references to the obtained

TypeInfo

longer than the callback scope.

Otherwise, this method returns
null if the validator is unable to
determine the type of the current element for some reason
(for example, if the validator is recovering from
an earlier error.)
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

---

#### getElementTypeInfo

public abstract

TypeInfo

getElementTypeInfo()

Returns the immutable

TypeInfo

object for the current
element.

The method may only be called by the startElement event
or the endElement event
of the

ContentHandler

that the application sets to
the

ValidatorHandler

.

When W3C XML Schema validation is being performed, in the
case where an element has a union type, the

TypeInfo

returned by a call to

getElementTypeInfo()

from the
startElement
event will be the union type. The

TypeInfo

returned by a call
from the endElement event will be the actual member type used
to validate the element.

Returns the immutable

TypeInfo

object for the current
element.

The method may only be called by the startElement event
or the endElement event
of the

ContentHandler

that the application sets to
the

ValidatorHandler

.

When W3C XML Schema validation is being performed, in the
case where an element has a union type, the

TypeInfo

returned by a call to

getElementTypeInfo()

from the
startElement
event will be the union type. The

TypeInfo

returned by a call
from the endElement event will be the actual member type used
to validate the element.

getAttributeTypeInfo

```java
public abstract
TypeInfo
getAttributeTypeInfo​(int index)
```

Returns the immutable

TypeInfo

object for the specified
attribute of the current element.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

**Parameters:** index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.
**Returns:** An immutable

TypeInfo

object that represents the
type of the specified attribute.
Note that the caller can keep references to the obtained

TypeInfo

longer than the callback scope.

Otherwise, this method returns
null if the validator is unable to
determine the type.
**Throws:** IndexOutOfBoundsException

- If the index is invalid.
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

---

#### getAttributeTypeInfo

public abstract

TypeInfo

getAttributeTypeInfo​(int index)

Returns the immutable

TypeInfo

object for the specified
attribute of the current element.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

isIdAttribute

```java
public abstract boolean isIdAttribute​(int index)
```

Returns

true

if the specified attribute is determined
to be ID.

Exacly how an attribute is "determined to be ID" is up to the
schema language. In case of W3C XML Schema, this means
that the actual type of the attribute is the built-in ID type
or its derived type.

A

DocumentBuilder

uses this information
to properly implement

Attr.isId()

.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

**Parameters:** index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.
**Returns:** true
if the type of the specified attribute is ID.
**Throws:** IndexOutOfBoundsException

- If the index is invalid.
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

---

#### isIdAttribute

public abstract boolean isIdAttribute​(int index)

Returns

true

if the specified attribute is determined
to be ID.

Exacly how an attribute is "determined to be ID" is up to the
schema language. In case of W3C XML Schema, this means
that the actual type of the attribute is the built-in ID type
or its derived type.

A

DocumentBuilder

uses this information
to properly implement

Attr.isId()

.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

Exacly how an attribute is "determined to be ID" is up to the
schema language. In case of W3C XML Schema, this means
that the actual type of the attribute is the built-in ID type
or its derived type.

A

DocumentBuilder

uses this information
to properly implement

Attr.isId()

.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

A

DocumentBuilder

uses this information
to properly implement

Attr.isId()

.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

isSpecified

```java
public abstract boolean isSpecified​(int index)
```

Returns

false

if the attribute was added by the validator.

This method provides information necessary for
a

DocumentBuilder

to determine what
the DOM tree should return from the

Attr.getSpecified()

method.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

A general guideline for validators is to return true if
the attribute was originally present in the pipeline, and
false if it was added by the validator.

**Parameters:** index

- The index of the attribute. The same index for
the

Attributes

object passed to the

startElement

callback.
**Returns:** true

if the attribute was present before the validator
processes input.

false

if the attribute was added
by the validator.
**Throws:** IndexOutOfBoundsException

- If the index is invalid.
**Throws:** IllegalStateException

- If this method is called from other

ContentHandler

methods.

---

#### isSpecified

public abstract boolean isSpecified​(int index)

Returns

false

if the attribute was added by the validator.

This method provides information necessary for
a

DocumentBuilder

to determine what
the DOM tree should return from the

Attr.getSpecified()

method.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

A general guideline for validators is to return true if
the attribute was originally present in the pipeline, and
false if it was added by the validator.

This method provides information necessary for
a

DocumentBuilder

to determine what
the DOM tree should return from the

Attr.getSpecified()

method.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

A general guideline for validators is to return true if
the attribute was originally present in the pipeline, and
false if it was added by the validator.

The method may only be called by the startElement event of
the

ContentHandler

that the application sets to the

ValidatorHandler

.

A general guideline for validators is to return true if
the attribute was originally present in the pipeline, and
false if it was added by the validator.

A general guideline for validators is to return true if
the attribute was originally present in the pipeline, and
false if it was added by the validator.

---

