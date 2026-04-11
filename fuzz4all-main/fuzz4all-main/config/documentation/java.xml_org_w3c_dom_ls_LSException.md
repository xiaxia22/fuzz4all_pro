# Class LSException

**Source:** `java.xml\org\w3c\dom\ls\LSException.html`

### Class Description

```java
public class
LSException

extends
RuntimeException
```

Parser or write operations may throw an

LSException

if the
processing is stopped. The processing can be stopped due to a

DOMError

with a severity of

DOMError.SEVERITY_FATAL_ERROR

or a non recovered

DOMError.SEVERITY_ERROR

, or if

DOMErrorHandler.handleError()

returned

false

.

Note:

As suggested in the definition of the constants in the

DOMError

interface, a DOM implementation may choose to
continue after a fatal error, but the resulting DOM tree is then
implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public short code

*No description found.*

---

#### public static final short PARSE_ERR

If an attempt was made to load a document, or an XML Fragment, using

LSParser

and the processing has been stopped.

**See Also:**
- Constant Field Values

---

#### public static final short SERIALIZE_ERR

If an attempt was made to serialize a

Node

using

LSSerializer

and the processing has been stopped.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public LSException​(short code,

String
message)

*No description found.*

---

### Method Details

*No entries found.*

### Additional Sections

#### Class LSException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - org.w3c.dom.ls.LSException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - org.w3c.dom.ls.LSException

java.lang.Exception

- java.lang.RuntimeException
- - org.w3c.dom.ls.LSException

java.lang.RuntimeException

- org.w3c.dom.ls.LSException

org.w3c.dom.ls.LSException

**All Implemented Interfaces:** Serializable

```java
public class
LSException

extends
RuntimeException
```

Parser or write operations may throw an

LSException

if the
processing is stopped. The processing can be stopped due to a

DOMError

with a severity of

DOMError.SEVERITY_FATAL_ERROR

or a non recovered

DOMError.SEVERITY_ERROR

, or if

DOMErrorHandler.handleError()

returned

false

.

Note:

As suggested in the definition of the constants in the

DOMError

interface, a DOM implementation may choose to
continue after a fatal error, but the resulting DOM tree is then
implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

**Since:** 1.5
**See Also:** Serialized Form

public class

LSException

extends

RuntimeException

Parser or write operations may throw an

LSException

if the
processing is stopped. The processing can be stopped due to a

DOMError

with a severity of

DOMError.SEVERITY_FATAL_ERROR

or a non recovered

DOMError.SEVERITY_ERROR

, or if

DOMErrorHandler.handleError()

returned

false

.

Note:

As suggested in the definition of the constants in the

DOMError

interface, a DOM implementation may choose to
continue after a fatal error, but the resulting DOM tree is then
implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

Note:

As suggested in the definition of the constants in the

DOMError

interface, a DOM implementation may choose to
continue after a fatal error, but the resulting DOM tree is then
implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

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

PARSE_ERR

If an attempt was made to load a document, or an XML Fragment, using

LSParser

and the processing has been stopped.

static short

SERIALIZE_ERR

If an attempt was made to serialize a

Node

using

LSSerializer

and the processing has been stopped.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LSException

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

PARSE_ERR

If an attempt was made to load a document, or an XML Fragment, using

LSParser

and the processing has been stopped.

static short

SERIALIZE_ERR

If an attempt was made to serialize a

Node

using

LSSerializer

and the processing has been stopped.

---

#### Field Summary

If an attempt was made to load a document, or an XML Fragment, using

LSParser

and the processing has been stopped.

If an attempt was made to serialize a

Node

using

LSSerializer

and the processing has been stopped.

Constructor Summary

Constructors

Constructor

Description

LSException

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

- PARSE_ERR

```java
public static final short PARSE_ERR
```

If an attempt was made to load a document, or an XML Fragment, using

LSParser

and the processing has been stopped.

**See Also:** Constant Field Values

- SERIALIZE_ERR

```java
public static final short SERIALIZE_ERR
```

If an attempt was made to serialize a

Node

using

LSSerializer

and the processing has been stopped.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LSException

```java
public LSException​(short code,

String
message)
```

Field Detail

- code

```java
public short code
```

- PARSE_ERR

```java
public static final short PARSE_ERR
```

If an attempt was made to load a document, or an XML Fragment, using

LSParser

and the processing has been stopped.

**See Also:** Constant Field Values

- SERIALIZE_ERR

```java
public static final short SERIALIZE_ERR
```

If an attempt was made to serialize a

Node

using

LSSerializer

and the processing has been stopped.

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

PARSE_ERR

```java
public static final short PARSE_ERR
```

If an attempt was made to load a document, or an XML Fragment, using

LSParser

and the processing has been stopped.

**See Also:** Constant Field Values

---

#### PARSE_ERR

public static final short PARSE_ERR

If an attempt was made to load a document, or an XML Fragment, using

LSParser

and the processing has been stopped.

SERIALIZE_ERR

```java
public static final short SERIALIZE_ERR
```

If an attempt was made to serialize a

Node

using

LSSerializer

and the processing has been stopped.

**See Also:** Constant Field Values

---

#### SERIALIZE_ERR

public static final short SERIALIZE_ERR

If an attempt was made to serialize a

Node

using

LSSerializer

and the processing has been stopped.

Constructor Detail

- LSException

```java
public LSException​(short code,

String
message)
```

---

#### Constructor Detail

LSException

```java
public LSException​(short code,

String
message)
```

---

#### LSException

public LSException​(short code,

String

message)

---

