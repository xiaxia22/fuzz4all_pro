# Class DOMException

**Source:** `java.xml\org\w3c\dom\DOMException.html`

### Class Description

```java
public class
DOMException

extends
RuntimeException
```

DOM operations only raise exceptions in "exceptional" circumstances, i.e.,
when an operation is impossible to perform (either for logical reasons,
because data is lost, or because the implementation has become unstable).
In general, DOM methods return specific error values in ordinary
processing situations, such as out-of-bound errors when using

NodeList

.

Implementations should raise other exceptions under other circumstances.
For example, implementations should raise an implementation-dependent
exception if a

null

argument is passed when

null

was not expected.

Some languages and object systems do not support the concept of
exceptions. For such systems, error conditions may be indicated using
native error reporting mechanisms. For some bindings, for example,
methods may return error codes similar to those listed in the
corresponding method descriptions.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public short code

*No description found.*

---

#### public static final short INDEX_SIZE_ERR

If index or size is negative, or greater than the allowed value.

**See Also:**
- Constant Field Values

---

#### public static final short DOMSTRING_SIZE_ERR

If the specified range of text does not fit into a

DOMString

.

**See Also:**
- Constant Field Values

---

#### public static final short HIERARCHY_REQUEST_ERR

If any

Node

is inserted somewhere it doesn't belong.

**See Also:**
- Constant Field Values

---

#### public static final short WRONG_DOCUMENT_ERR

If a

Node

is used in a different document than the one
that created it (that doesn't support it).

**See Also:**
- Constant Field Values

---

#### public static final short INVALID_CHARACTER_ERR

If an invalid or illegal character is specified, such as in an XML name.

**See Also:**
- Constant Field Values

---

#### public static final short NO_DATA_ALLOWED_ERR

If data is specified for a

Node

which does not support
data.

**See Also:**
- Constant Field Values

---

#### public static final short NO_MODIFICATION_ALLOWED_ERR

If an attempt is made to modify an object where modifications are not
allowed.

**See Also:**
- Constant Field Values

---

#### public static final short NOT_FOUND_ERR

If an attempt is made to reference a

Node

in a context
where it does not exist.

**See Also:**
- Constant Field Values

---

#### public static final short NOT_SUPPORTED_ERR

If the implementation does not support the requested type of object or
operation.

**See Also:**
- Constant Field Values

---

#### public static final short INUSE_ATTRIBUTE_ERR

If an attempt is made to add an attribute that is already in use
elsewhere.

**See Also:**
- Constant Field Values

---

#### public static final short INVALID_STATE_ERR

If an attempt is made to use an object that is not, or is no longer,
usable.

**See Also:**
- Constant Field Values

**Since:**
- 1.4, DOM Level 2

---

#### public static final short SYNTAX_ERR

If an invalid or illegal string is specified.

**See Also:**
- Constant Field Values

**Since:**
- 1.4, DOM Level 2

---

#### public static final short INVALID_MODIFICATION_ERR

If an attempt is made to modify the type of the underlying object.

**See Also:**
- Constant Field Values

**Since:**
- 1.4, DOM Level 2

---

#### public static final short NAMESPACE_ERR

If an attempt is made to create or change an object in a way which is
incorrect with regard to namespaces.

**See Also:**
- Constant Field Values

**Since:**
- 1.4, DOM Level 2

---

#### public static final short INVALID_ACCESS_ERR

If a parameter or an operation is not supported by the underlying
object.

**See Also:**
- Constant Field Values

**Since:**
- 1.4, DOM Level 2

---

#### public static final short VALIDATION_ERR

If a call to a method such as

insertBefore

or

removeChild

would make the

Node

invalid
with respect to "partial validity", this exception would be raised
and the operation would not be done. This code is used in [

DOM Level 3 Validation

]
. Refer to this specification for further information.

**See Also:**
- Constant Field Values

**Since:**
- 1.5, DOM Level 3

---

#### public static final short TYPE_MISMATCH_ERR

If the type of an object is incompatible with the expected type of the
parameter associated to the object.

**See Also:**
- Constant Field Values

**Since:**
- 1.5, DOM Level 3

---

### Constructor Details

#### public DOMException​(short code,

String
message)

*No description found.*

---

### Method Details

*No entries found.*

### Additional Sections

#### Class DOMException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - org.w3c.dom.DOMException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - org.w3c.dom.DOMException

java.lang.Exception

- java.lang.RuntimeException
- - org.w3c.dom.DOMException

java.lang.RuntimeException

- org.w3c.dom.DOMException

org.w3c.dom.DOMException

**All Implemented Interfaces:** Serializable

```java
public class
DOMException

extends
RuntimeException
```

DOM operations only raise exceptions in "exceptional" circumstances, i.e.,
when an operation is impossible to perform (either for logical reasons,
because data is lost, or because the implementation has become unstable).
In general, DOM methods return specific error values in ordinary
processing situations, such as out-of-bound errors when using

NodeList

.

Implementations should raise other exceptions under other circumstances.
For example, implementations should raise an implementation-dependent
exception if a

null

argument is passed when

null

was not expected.

Some languages and object systems do not support the concept of
exceptions. For such systems, error conditions may be indicated using
native error reporting mechanisms. For some bindings, for example,
methods may return error codes similar to those listed in the
corresponding method descriptions.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**See Also:** Serialized Form

public class

DOMException

extends

RuntimeException

DOM operations only raise exceptions in "exceptional" circumstances, i.e.,
when an operation is impossible to perform (either for logical reasons,
because data is lost, or because the implementation has become unstable).
In general, DOM methods return specific error values in ordinary
processing situations, such as out-of-bound errors when using

NodeList

.

Implementations should raise other exceptions under other circumstances.
For example, implementations should raise an implementation-dependent
exception if a

null

argument is passed when

null

was not expected.

Some languages and object systems do not support the concept of
exceptions. For such systems, error conditions may be indicated using
native error reporting mechanisms. For some bindings, for example,
methods may return error codes similar to those listed in the
corresponding method descriptions.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

Implementations should raise other exceptions under other circumstances.
For example, implementations should raise an implementation-dependent
exception if a

null

argument is passed when

null

was not expected.

Some languages and object systems do not support the concept of
exceptions. For such systems, error conditions may be indicated using
native error reporting mechanisms. For some bindings, for example,
methods may return error codes similar to those listed in the
corresponding method descriptions.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

Some languages and object systems do not support the concept of
exceptions. For such systems, error conditions may be indicated using
native error reporting mechanisms. For some bindings, for example,
methods may return error codes similar to those listed in the
corresponding method descriptions.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

short

code

static short

DOMSTRING_SIZE_ERR

If the specified range of text does not fit into a

DOMString

.

static short

HIERARCHY_REQUEST_ERR

If any

Node

is inserted somewhere it doesn't belong.

static short

INDEX_SIZE_ERR

If index or size is negative, or greater than the allowed value.

static short

INUSE_ATTRIBUTE_ERR

If an attempt is made to add an attribute that is already in use
elsewhere.

static short

INVALID_ACCESS_ERR

If a parameter or an operation is not supported by the underlying
object.

static short

INVALID_CHARACTER_ERR

If an invalid or illegal character is specified, such as in an XML name.

static short

INVALID_MODIFICATION_ERR

If an attempt is made to modify the type of the underlying object.

static short

INVALID_STATE_ERR

If an attempt is made to use an object that is not, or is no longer,
usable.

static short

NAMESPACE_ERR

If an attempt is made to create or change an object in a way which is
incorrect with regard to namespaces.

static short

NO_DATA_ALLOWED_ERR

If data is specified for a

Node

which does not support
data.

static short

NO_MODIFICATION_ALLOWED_ERR

If an attempt is made to modify an object where modifications are not
allowed.

static short

NOT_FOUND_ERR

If an attempt is made to reference a

Node

in a context
where it does not exist.

static short

NOT_SUPPORTED_ERR

If the implementation does not support the requested type of object or
operation.

static short

SYNTAX_ERR

If an invalid or illegal string is specified.

static short

TYPE_MISMATCH_ERR

If the type of an object is incompatible with the expected type of the
parameter associated to the object.

static short

VALIDATION_ERR

If a call to a method such as

insertBefore

or

removeChild

would make the

Node

invalid
with respect to "partial validity", this exception would be raised
and the operation would not be done.

static short

WRONG_DOCUMENT_ERR

If a

Node

is used in a different document than the one
that created it (that doesn't support it).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DOMException

​(short code,

String

message)

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

short

code

static short

DOMSTRING_SIZE_ERR

If the specified range of text does not fit into a

DOMString

.

static short

HIERARCHY_REQUEST_ERR

If any

Node

is inserted somewhere it doesn't belong.

static short

INDEX_SIZE_ERR

If index or size is negative, or greater than the allowed value.

static short

INUSE_ATTRIBUTE_ERR

If an attempt is made to add an attribute that is already in use
elsewhere.

static short

INVALID_ACCESS_ERR

If a parameter or an operation is not supported by the underlying
object.

static short

INVALID_CHARACTER_ERR

If an invalid or illegal character is specified, such as in an XML name.

static short

INVALID_MODIFICATION_ERR

If an attempt is made to modify the type of the underlying object.

static short

INVALID_STATE_ERR

If an attempt is made to use an object that is not, or is no longer,
usable.

static short

NAMESPACE_ERR

If an attempt is made to create or change an object in a way which is
incorrect with regard to namespaces.

static short

NO_DATA_ALLOWED_ERR

If data is specified for a

Node

which does not support
data.

static short

NO_MODIFICATION_ALLOWED_ERR

If an attempt is made to modify an object where modifications are not
allowed.

static short

NOT_FOUND_ERR

If an attempt is made to reference a

Node

in a context
where it does not exist.

static short

NOT_SUPPORTED_ERR

If the implementation does not support the requested type of object or
operation.

static short

SYNTAX_ERR

If an invalid or illegal string is specified.

static short

TYPE_MISMATCH_ERR

If the type of an object is incompatible with the expected type of the
parameter associated to the object.

static short

VALIDATION_ERR

If a call to a method such as

insertBefore

or

removeChild

would make the

Node

invalid
with respect to "partial validity", this exception would be raised
and the operation would not be done.

static short

WRONG_DOCUMENT_ERR

If a

Node

is used in a different document than the one
that created it (that doesn't support it).

---

#### Field Summary

If the specified range of text does not fit into a

DOMString

.

If any

Node

is inserted somewhere it doesn't belong.

If index or size is negative, or greater than the allowed value.

If an attempt is made to add an attribute that is already in use
elsewhere.

If a parameter or an operation is not supported by the underlying
object.

If an invalid or illegal character is specified, such as in an XML name.

If an attempt is made to modify the type of the underlying object.

If an attempt is made to use an object that is not, or is no longer,
usable.

If an attempt is made to create or change an object in a way which is
incorrect with regard to namespaces.

If data is specified for a

Node

which does not support
data.

If an attempt is made to modify an object where modifications are not
allowed.

If an attempt is made to reference a

Node

in a context
where it does not exist.

If the implementation does not support the requested type of object or
operation.

If an invalid or illegal string is specified.

If the type of an object is incompatible with the expected type of the
parameter associated to the object.

If a call to a method such as

insertBefore

or

removeChild

would make the

Node

invalid
with respect to "partial validity", this exception would be raised
and the operation would not be done.

If a

Node

is used in a different document than the one
that created it (that doesn't support it).

Constructor Summary

Constructors

Constructor

Description

DOMException

​(short code,

String

message)

---

#### Constructor Summary

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- code

```java
public short code
```

- INDEX_SIZE_ERR

```java
public static final short INDEX_SIZE_ERR
```

If index or size is negative, or greater than the allowed value.

**See Also:** Constant Field Values

- DOMSTRING_SIZE_ERR

```java
public static final short DOMSTRING_SIZE_ERR
```

If the specified range of text does not fit into a

DOMString

.

**See Also:** Constant Field Values

- HIERARCHY_REQUEST_ERR

```java
public static final short HIERARCHY_REQUEST_ERR
```

If any

Node

is inserted somewhere it doesn't belong.

**See Also:** Constant Field Values

- WRONG_DOCUMENT_ERR

```java
public static final short WRONG_DOCUMENT_ERR
```

If a

Node

is used in a different document than the one
that created it (that doesn't support it).

**See Also:** Constant Field Values

- INVALID_CHARACTER_ERR

```java
public static final short INVALID_CHARACTER_ERR
```

If an invalid or illegal character is specified, such as in an XML name.

**See Also:** Constant Field Values

- NO_DATA_ALLOWED_ERR

```java
public static final short NO_DATA_ALLOWED_ERR
```

If data is specified for a

Node

which does not support
data.

**See Also:** Constant Field Values

- NO_MODIFICATION_ALLOWED_ERR

```java
public static final short NO_MODIFICATION_ALLOWED_ERR
```

If an attempt is made to modify an object where modifications are not
allowed.

**See Also:** Constant Field Values

- NOT_FOUND_ERR

```java
public static final short NOT_FOUND_ERR
```

If an attempt is made to reference a

Node

in a context
where it does not exist.

**See Also:** Constant Field Values

- NOT_SUPPORTED_ERR

```java
public static final short NOT_SUPPORTED_ERR
```

If the implementation does not support the requested type of object or
operation.

**See Also:** Constant Field Values

- INUSE_ATTRIBUTE_ERR

```java
public static final short INUSE_ATTRIBUTE_ERR
```

If an attempt is made to add an attribute that is already in use
elsewhere.

**See Also:** Constant Field Values

- INVALID_STATE_ERR

```java
public static final short INVALID_STATE_ERR
```

If an attempt is made to use an object that is not, or is no longer,
usable.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- SYNTAX_ERR

```java
public static final short SYNTAX_ERR
```

If an invalid or illegal string is specified.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- INVALID_MODIFICATION_ERR

```java
public static final short INVALID_MODIFICATION_ERR
```

If an attempt is made to modify the type of the underlying object.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- NAMESPACE_ERR

```java
public static final short NAMESPACE_ERR
```

If an attempt is made to create or change an object in a way which is
incorrect with regard to namespaces.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- INVALID_ACCESS_ERR

```java
public static final short INVALID_ACCESS_ERR
```

If a parameter or an operation is not supported by the underlying
object.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- VALIDATION_ERR

```java
public static final short VALIDATION_ERR
```

If a call to a method such as

insertBefore

or

removeChild

would make the

Node

invalid
with respect to "partial validity", this exception would be raised
and the operation would not be done. This code is used in [

DOM Level 3 Validation

]
. Refer to this specification for further information.

**Since:** 1.5, DOM Level 3
**See Also:** Constant Field Values

- TYPE_MISMATCH_ERR

```java
public static final short TYPE_MISMATCH_ERR
```

If the type of an object is incompatible with the expected type of the
parameter associated to the object.

**Since:** 1.5, DOM Level 3
**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DOMException

```java
public DOMException​(short code,

String
message)
```

Field Detail

- code

```java
public short code
```

- INDEX_SIZE_ERR

```java
public static final short INDEX_SIZE_ERR
```

If index or size is negative, or greater than the allowed value.

**See Also:** Constant Field Values

- DOMSTRING_SIZE_ERR

```java
public static final short DOMSTRING_SIZE_ERR
```

If the specified range of text does not fit into a

DOMString

.

**See Also:** Constant Field Values

- HIERARCHY_REQUEST_ERR

```java
public static final short HIERARCHY_REQUEST_ERR
```

If any

Node

is inserted somewhere it doesn't belong.

**See Also:** Constant Field Values

- WRONG_DOCUMENT_ERR

```java
public static final short WRONG_DOCUMENT_ERR
```

If a

Node

is used in a different document than the one
that created it (that doesn't support it).

**See Also:** Constant Field Values

- INVALID_CHARACTER_ERR

```java
public static final short INVALID_CHARACTER_ERR
```

If an invalid or illegal character is specified, such as in an XML name.

**See Also:** Constant Field Values

- NO_DATA_ALLOWED_ERR

```java
public static final short NO_DATA_ALLOWED_ERR
```

If data is specified for a

Node

which does not support
data.

**See Also:** Constant Field Values

- NO_MODIFICATION_ALLOWED_ERR

```java
public static final short NO_MODIFICATION_ALLOWED_ERR
```

If an attempt is made to modify an object where modifications are not
allowed.

**See Also:** Constant Field Values

- NOT_FOUND_ERR

```java
public static final short NOT_FOUND_ERR
```

If an attempt is made to reference a

Node

in a context
where it does not exist.

**See Also:** Constant Field Values

- NOT_SUPPORTED_ERR

```java
public static final short NOT_SUPPORTED_ERR
```

If the implementation does not support the requested type of object or
operation.

**See Also:** Constant Field Values

- INUSE_ATTRIBUTE_ERR

```java
public static final short INUSE_ATTRIBUTE_ERR
```

If an attempt is made to add an attribute that is already in use
elsewhere.

**See Also:** Constant Field Values

- INVALID_STATE_ERR

```java
public static final short INVALID_STATE_ERR
```

If an attempt is made to use an object that is not, or is no longer,
usable.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- SYNTAX_ERR

```java
public static final short SYNTAX_ERR
```

If an invalid or illegal string is specified.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- INVALID_MODIFICATION_ERR

```java
public static final short INVALID_MODIFICATION_ERR
```

If an attempt is made to modify the type of the underlying object.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- NAMESPACE_ERR

```java
public static final short NAMESPACE_ERR
```

If an attempt is made to create or change an object in a way which is
incorrect with regard to namespaces.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- INVALID_ACCESS_ERR

```java
public static final short INVALID_ACCESS_ERR
```

If a parameter or an operation is not supported by the underlying
object.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

- VALIDATION_ERR

```java
public static final short VALIDATION_ERR
```

If a call to a method such as

insertBefore

or

removeChild

would make the

Node

invalid
with respect to "partial validity", this exception would be raised
and the operation would not be done. This code is used in [

DOM Level 3 Validation

]
. Refer to this specification for further information.

**Since:** 1.5, DOM Level 3
**See Also:** Constant Field Values

- TYPE_MISMATCH_ERR

```java
public static final short TYPE_MISMATCH_ERR
```

If the type of an object is incompatible with the expected type of the
parameter associated to the object.

**Since:** 1.5, DOM Level 3
**See Also:** Constant Field Values

---

#### Field Detail

code

```java
public short code
```

---

#### code

public short code

INDEX_SIZE_ERR

```java
public static final short INDEX_SIZE_ERR
```

If index or size is negative, or greater than the allowed value.

**See Also:** Constant Field Values

---

#### INDEX_SIZE_ERR

public static final short INDEX_SIZE_ERR

If index or size is negative, or greater than the allowed value.

DOMSTRING_SIZE_ERR

```java
public static final short DOMSTRING_SIZE_ERR
```

If the specified range of text does not fit into a

DOMString

.

**See Also:** Constant Field Values

---

#### DOMSTRING_SIZE_ERR

public static final short DOMSTRING_SIZE_ERR

If the specified range of text does not fit into a

DOMString

.

HIERARCHY_REQUEST_ERR

```java
public static final short HIERARCHY_REQUEST_ERR
```

If any

Node

is inserted somewhere it doesn't belong.

**See Also:** Constant Field Values

---

#### HIERARCHY_REQUEST_ERR

public static final short HIERARCHY_REQUEST_ERR

If any

Node

is inserted somewhere it doesn't belong.

WRONG_DOCUMENT_ERR

```java
public static final short WRONG_DOCUMENT_ERR
```

If a

Node

is used in a different document than the one
that created it (that doesn't support it).

**See Also:** Constant Field Values

---

#### WRONG_DOCUMENT_ERR

public static final short WRONG_DOCUMENT_ERR

If a

Node

is used in a different document than the one
that created it (that doesn't support it).

INVALID_CHARACTER_ERR

```java
public static final short INVALID_CHARACTER_ERR
```

If an invalid or illegal character is specified, such as in an XML name.

**See Also:** Constant Field Values

---

#### INVALID_CHARACTER_ERR

public static final short INVALID_CHARACTER_ERR

If an invalid or illegal character is specified, such as in an XML name.

NO_DATA_ALLOWED_ERR

```java
public static final short NO_DATA_ALLOWED_ERR
```

If data is specified for a

Node

which does not support
data.

**See Also:** Constant Field Values

---

#### NO_DATA_ALLOWED_ERR

public static final short NO_DATA_ALLOWED_ERR

If data is specified for a

Node

which does not support
data.

NO_MODIFICATION_ALLOWED_ERR

```java
public static final short NO_MODIFICATION_ALLOWED_ERR
```

If an attempt is made to modify an object where modifications are not
allowed.

**See Also:** Constant Field Values

---

#### NO_MODIFICATION_ALLOWED_ERR

public static final short NO_MODIFICATION_ALLOWED_ERR

If an attempt is made to modify an object where modifications are not
allowed.

NOT_FOUND_ERR

```java
public static final short NOT_FOUND_ERR
```

If an attempt is made to reference a

Node

in a context
where it does not exist.

**See Also:** Constant Field Values

---

#### NOT_FOUND_ERR

public static final short NOT_FOUND_ERR

If an attempt is made to reference a

Node

in a context
where it does not exist.

NOT_SUPPORTED_ERR

```java
public static final short NOT_SUPPORTED_ERR
```

If the implementation does not support the requested type of object or
operation.

**See Also:** Constant Field Values

---

#### NOT_SUPPORTED_ERR

public static final short NOT_SUPPORTED_ERR

If the implementation does not support the requested type of object or
operation.

INUSE_ATTRIBUTE_ERR

```java
public static final short INUSE_ATTRIBUTE_ERR
```

If an attempt is made to add an attribute that is already in use
elsewhere.

**See Also:** Constant Field Values

---

#### INUSE_ATTRIBUTE_ERR

public static final short INUSE_ATTRIBUTE_ERR

If an attempt is made to add an attribute that is already in use
elsewhere.

INVALID_STATE_ERR

```java
public static final short INVALID_STATE_ERR
```

If an attempt is made to use an object that is not, or is no longer,
usable.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

---

#### INVALID_STATE_ERR

public static final short INVALID_STATE_ERR

If an attempt is made to use an object that is not, or is no longer,
usable.

SYNTAX_ERR

```java
public static final short SYNTAX_ERR
```

If an invalid or illegal string is specified.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

---

#### SYNTAX_ERR

public static final short SYNTAX_ERR

If an invalid or illegal string is specified.

INVALID_MODIFICATION_ERR

```java
public static final short INVALID_MODIFICATION_ERR
```

If an attempt is made to modify the type of the underlying object.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

---

#### INVALID_MODIFICATION_ERR

public static final short INVALID_MODIFICATION_ERR

If an attempt is made to modify the type of the underlying object.

NAMESPACE_ERR

```java
public static final short NAMESPACE_ERR
```

If an attempt is made to create or change an object in a way which is
incorrect with regard to namespaces.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

---

#### NAMESPACE_ERR

public static final short NAMESPACE_ERR

If an attempt is made to create or change an object in a way which is
incorrect with regard to namespaces.

INVALID_ACCESS_ERR

```java
public static final short INVALID_ACCESS_ERR
```

If a parameter or an operation is not supported by the underlying
object.

**Since:** 1.4, DOM Level 2
**See Also:** Constant Field Values

---

#### INVALID_ACCESS_ERR

public static final short INVALID_ACCESS_ERR

If a parameter or an operation is not supported by the underlying
object.

VALIDATION_ERR

```java
public static final short VALIDATION_ERR
```

If a call to a method such as

insertBefore

or

removeChild

would make the

Node

invalid
with respect to "partial validity", this exception would be raised
and the operation would not be done. This code is used in [

DOM Level 3 Validation

]
. Refer to this specification for further information.

**Since:** 1.5, DOM Level 3
**See Also:** Constant Field Values

---

#### VALIDATION_ERR

public static final short VALIDATION_ERR

If a call to a method such as

insertBefore

or

removeChild

would make the

Node

invalid
with respect to "partial validity", this exception would be raised
and the operation would not be done. This code is used in [

DOM Level 3 Validation

]
. Refer to this specification for further information.

TYPE_MISMATCH_ERR

```java
public static final short TYPE_MISMATCH_ERR
```

If the type of an object is incompatible with the expected type of the
parameter associated to the object.

**Since:** 1.5, DOM Level 3
**See Also:** Constant Field Values

---

#### TYPE_MISMATCH_ERR

public static final short TYPE_MISMATCH_ERR

If the type of an object is incompatible with the expected type of the
parameter associated to the object.

Constructor Detail

- DOMException

```java
public DOMException​(short code,

String
message)
```

---

#### Constructor Detail

DOMException

```java
public DOMException​(short code,

String
message)
```

---

#### DOMException

public DOMException​(short code,

String

message)

---

