# Interface DOMError

**Source:** `java.xml\org\w3c\dom\DOMError.html`

### Class Description

```java
public interface
DOMError
```

DOMError

is an interface that describes an error.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

---

### Field Details

#### static final short SEVERITY_WARNING

The severity of the error described by the

DOMError

is
warning. A

SEVERITY_WARNING

will not cause the
processing to stop, unless

DOMErrorHandler.handleError()

returns

false

.

**See Also:**
- Constant Field Values

---

#### static final short SEVERITY_ERROR

The severity of the error described by the

DOMError

is
error. A

SEVERITY_ERROR

may not cause the processing to
stop if the error can be recovered, unless

DOMErrorHandler.handleError()

returns

false

.

**See Also:**
- Constant Field Values

---

#### static final short SEVERITY_FATAL_ERROR

The severity of the error described by the

DOMError

is
fatal error. A

SEVERITY_FATAL_ERROR

will cause the
normal processing to stop. The return value of

DOMErrorHandler.handleError()

is ignored unless the
implementation chooses to continue, in which case the behavior
becomes undefined.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### short getSeverity()

The severity of the error, either

SEVERITY_WARNING

,

SEVERITY_ERROR

, or

SEVERITY_FATAL_ERROR

.

---

#### String
getMessage()

An implementation specific string describing the error that occurred.

---

#### String
getType()

A

DOMString

indicating which related data is expected in

relatedData

. Users should refer to the specification of
the error in order to find its

DOMString

type and

relatedData

definitions if any.

Note:

As an example,

Document.normalizeDocument()

does generate warnings when
the "split-cdata-sections" parameter is in use. Therefore, the method
generates a

SEVERITY_WARNING

with

type

"cdata-sections-splitted"

and the first

CDATASection

node in document order resulting from the
split is returned by the

relatedData

attribute.

---

#### Object
getRelatedException()

The related platform dependent exception if any.

---

#### Object
getRelatedData()

The related

DOMError.type

dependent data if any.

---

#### DOMLocator
getLocation()

The location of the error.

---

### Additional Sections

#### Interface DOMError

```java
public interface
DOMError
```

DOMError

is an interface that describes an error.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

public interface

DOMError

DOMError

is an interface that describes an error.

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

static short

SEVERITY_ERROR

The severity of the error described by the

DOMError

is
error.

static short

SEVERITY_FATAL_ERROR

The severity of the error described by the

DOMError

is
fatal error.

static short

SEVERITY_WARNING

The severity of the error described by the

DOMError

is
warning.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DOMLocator

getLocation

()

The location of the error.

String

getMessage

()

An implementation specific string describing the error that occurred.

Object

getRelatedData

()

The related

DOMError.type

dependent data if any.

Object

getRelatedException

()

The related platform dependent exception if any.

short

getSeverity

()

The severity of the error, either

SEVERITY_WARNING

,

SEVERITY_ERROR

, or

SEVERITY_FATAL_ERROR

.

String

getType

()

A

DOMString

indicating which related data is expected in

relatedData

.

Field Summary

Fields

Modifier and Type

Field

Description

static short

SEVERITY_ERROR

The severity of the error described by the

DOMError

is
error.

static short

SEVERITY_FATAL_ERROR

The severity of the error described by the

DOMError

is
fatal error.

static short

SEVERITY_WARNING

The severity of the error described by the

DOMError

is
warning.

---

#### Field Summary

The severity of the error described by the

DOMError

is
error.

The severity of the error described by the

DOMError

is
fatal error.

The severity of the error described by the

DOMError

is
warning.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DOMLocator

getLocation

()

The location of the error.

String

getMessage

()

An implementation specific string describing the error that occurred.

Object

getRelatedData

()

The related

DOMError.type

dependent data if any.

Object

getRelatedException

()

The related platform dependent exception if any.

short

getSeverity

()

The severity of the error, either

SEVERITY_WARNING

,

SEVERITY_ERROR

, or

SEVERITY_FATAL_ERROR

.

String

getType

()

A

DOMString

indicating which related data is expected in

relatedData

.

---

#### Method Summary

The location of the error.

An implementation specific string describing the error that occurred.

The related

DOMError.type

dependent data if any.

The related platform dependent exception if any.

The severity of the error, either

SEVERITY_WARNING

,

SEVERITY_ERROR

, or

SEVERITY_FATAL_ERROR

.

A

DOMString

indicating which related data is expected in

relatedData

.

============ FIELD DETAIL ===========

- Field Detail

- SEVERITY_WARNING

```java
static final short SEVERITY_WARNING
```

The severity of the error described by the

DOMError

is
warning. A

SEVERITY_WARNING

will not cause the
processing to stop, unless

DOMErrorHandler.handleError()

returns

false

.

**See Also:** Constant Field Values

- SEVERITY_ERROR

```java
static final short SEVERITY_ERROR
```

The severity of the error described by the

DOMError

is
error. A

SEVERITY_ERROR

may not cause the processing to
stop if the error can be recovered, unless

DOMErrorHandler.handleError()

returns

false

.

**See Also:** Constant Field Values

- SEVERITY_FATAL_ERROR

```java
static final short SEVERITY_FATAL_ERROR
```

The severity of the error described by the

DOMError

is
fatal error. A

SEVERITY_FATAL_ERROR

will cause the
normal processing to stop. The return value of

DOMErrorHandler.handleError()

is ignored unless the
implementation chooses to continue, in which case the behavior
becomes undefined.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getSeverity

```java
short getSeverity()
```

The severity of the error, either

SEVERITY_WARNING

,

SEVERITY_ERROR

, or

SEVERITY_FATAL_ERROR

.

- getMessage

```java
String
getMessage()
```

An implementation specific string describing the error that occurred.

- getType

```java
String
getType()
```

A

DOMString

indicating which related data is expected in

relatedData

. Users should refer to the specification of
the error in order to find its

DOMString

type and

relatedData

definitions if any.

Note:

As an example,

Document.normalizeDocument()

does generate warnings when
the "split-cdata-sections" parameter is in use. Therefore, the method
generates a

SEVERITY_WARNING

with

type

"cdata-sections-splitted"

and the first

CDATASection

node in document order resulting from the
split is returned by the

relatedData

attribute.

- getRelatedException

```java
Object
getRelatedException()
```

The related platform dependent exception if any.

- getRelatedData

```java
Object
getRelatedData()
```

The related

DOMError.type

dependent data if any.

- getLocation

```java
DOMLocator
getLocation()
```

The location of the error.

Field Detail

- SEVERITY_WARNING

```java
static final short SEVERITY_WARNING
```

The severity of the error described by the

DOMError

is
warning. A

SEVERITY_WARNING

will not cause the
processing to stop, unless

DOMErrorHandler.handleError()

returns

false

.

**See Also:** Constant Field Values

- SEVERITY_ERROR

```java
static final short SEVERITY_ERROR
```

The severity of the error described by the

DOMError

is
error. A

SEVERITY_ERROR

may not cause the processing to
stop if the error can be recovered, unless

DOMErrorHandler.handleError()

returns

false

.

**See Also:** Constant Field Values

- SEVERITY_FATAL_ERROR

```java
static final short SEVERITY_FATAL_ERROR
```

The severity of the error described by the

DOMError

is
fatal error. A

SEVERITY_FATAL_ERROR

will cause the
normal processing to stop. The return value of

DOMErrorHandler.handleError()

is ignored unless the
implementation chooses to continue, in which case the behavior
becomes undefined.

**See Also:** Constant Field Values

---

#### Field Detail

SEVERITY_WARNING

```java
static final short SEVERITY_WARNING
```

The severity of the error described by the

DOMError

is
warning. A

SEVERITY_WARNING

will not cause the
processing to stop, unless

DOMErrorHandler.handleError()

returns

false

.

**See Also:** Constant Field Values

---

#### SEVERITY_WARNING

static final short SEVERITY_WARNING

The severity of the error described by the

DOMError

is
warning. A

SEVERITY_WARNING

will not cause the
processing to stop, unless

DOMErrorHandler.handleError()

returns

false

.

SEVERITY_ERROR

```java
static final short SEVERITY_ERROR
```

The severity of the error described by the

DOMError

is
error. A

SEVERITY_ERROR

may not cause the processing to
stop if the error can be recovered, unless

DOMErrorHandler.handleError()

returns

false

.

**See Also:** Constant Field Values

---

#### SEVERITY_ERROR

static final short SEVERITY_ERROR

The severity of the error described by the

DOMError

is
error. A

SEVERITY_ERROR

may not cause the processing to
stop if the error can be recovered, unless

DOMErrorHandler.handleError()

returns

false

.

SEVERITY_FATAL_ERROR

```java
static final short SEVERITY_FATAL_ERROR
```

The severity of the error described by the

DOMError

is
fatal error. A

SEVERITY_FATAL_ERROR

will cause the
normal processing to stop. The return value of

DOMErrorHandler.handleError()

is ignored unless the
implementation chooses to continue, in which case the behavior
becomes undefined.

**See Also:** Constant Field Values

---

#### SEVERITY_FATAL_ERROR

static final short SEVERITY_FATAL_ERROR

The severity of the error described by the

DOMError

is
fatal error. A

SEVERITY_FATAL_ERROR

will cause the
normal processing to stop. The return value of

DOMErrorHandler.handleError()

is ignored unless the
implementation chooses to continue, in which case the behavior
becomes undefined.

Method Detail

- getSeverity

```java
short getSeverity()
```

The severity of the error, either

SEVERITY_WARNING

,

SEVERITY_ERROR

, or

SEVERITY_FATAL_ERROR

.

- getMessage

```java
String
getMessage()
```

An implementation specific string describing the error that occurred.

- getType

```java
String
getType()
```

A

DOMString

indicating which related data is expected in

relatedData

. Users should refer to the specification of
the error in order to find its

DOMString

type and

relatedData

definitions if any.

Note:

As an example,

Document.normalizeDocument()

does generate warnings when
the "split-cdata-sections" parameter is in use. Therefore, the method
generates a

SEVERITY_WARNING

with

type

"cdata-sections-splitted"

and the first

CDATASection

node in document order resulting from the
split is returned by the

relatedData

attribute.

- getRelatedException

```java
Object
getRelatedException()
```

The related platform dependent exception if any.

- getRelatedData

```java
Object
getRelatedData()
```

The related

DOMError.type

dependent data if any.

- getLocation

```java
DOMLocator
getLocation()
```

The location of the error.

---

#### Method Detail

getSeverity

```java
short getSeverity()
```

The severity of the error, either

SEVERITY_WARNING

,

SEVERITY_ERROR

, or

SEVERITY_FATAL_ERROR

.

---

#### getSeverity

short getSeverity()

The severity of the error, either

SEVERITY_WARNING

,

SEVERITY_ERROR

, or

SEVERITY_FATAL_ERROR

.

getMessage

```java
String
getMessage()
```

An implementation specific string describing the error that occurred.

---

#### getMessage

String

getMessage()

An implementation specific string describing the error that occurred.

getType

```java
String
getType()
```

A

DOMString

indicating which related data is expected in

relatedData

. Users should refer to the specification of
the error in order to find its

DOMString

type and

relatedData

definitions if any.

Note:

As an example,

Document.normalizeDocument()

does generate warnings when
the "split-cdata-sections" parameter is in use. Therefore, the method
generates a

SEVERITY_WARNING

with

type

"cdata-sections-splitted"

and the first

CDATASection

node in document order resulting from the
split is returned by the

relatedData

attribute.

---

#### getType

String

getType()

A

DOMString

indicating which related data is expected in

relatedData

. Users should refer to the specification of
the error in order to find its

DOMString

type and

relatedData

definitions if any.

Note:

As an example,

Document.normalizeDocument()

does generate warnings when
the "split-cdata-sections" parameter is in use. Therefore, the method
generates a

SEVERITY_WARNING

with

type

"cdata-sections-splitted"

and the first

CDATASection

node in document order resulting from the
split is returned by the

relatedData

attribute.

Note:

As an example,

Document.normalizeDocument()

does generate warnings when
the "split-cdata-sections" parameter is in use. Therefore, the method
generates a

SEVERITY_WARNING

with

type

"cdata-sections-splitted"

and the first

CDATASection

node in document order resulting from the
split is returned by the

relatedData

attribute.

getRelatedException

```java
Object
getRelatedException()
```

The related platform dependent exception if any.

---

#### getRelatedException

Object

getRelatedException()

The related platform dependent exception if any.

getRelatedData

```java
Object
getRelatedData()
```

The related

DOMError.type

dependent data if any.

---

#### getRelatedData

Object

getRelatedData()

The related

DOMError.type

dependent data if any.

getLocation

```java
DOMLocator
getLocation()
```

The location of the error.

---

#### getLocation

DOMLocator

getLocation()

The location of the error.

---

