# Class CodingErrorAction

**Source:** `java.base\java\nio\charset\CodingErrorAction.html`

### Class Description

```java
public class
CodingErrorAction

extends
Object
```

A typesafe enumeration for coding-error actions.

Instances of this class are used to specify how malformed-input and
unmappable-character errors are to be handled by charset

decoders

and

encoders

.

**Since:** 1.4

---

### Field Details

#### public static final
CodingErrorAction
IGNORE

Action indicating that a coding error is to be handled by dropping the
erroneous input and resuming the coding operation.

---

#### public static final
CodingErrorAction
REPLACE

Action indicating that a coding error is to be handled by dropping the
erroneous input, appending the coder's replacement value to the output
buffer, and resuming the coding operation.

---

#### public static final
CodingErrorAction
REPORT

Action indicating that a coding error is to be reported, either by
returning a

CoderResult

object or by throwing a

CharacterCodingException

, whichever is appropriate for the method
implementing the coding process.

---

### Constructor Details

*No entries found.*

### Method Details

#### public
String
toString()

Returns a string describing this action.

**Overrides:**
- toString

in class

Object

**Returns:**
- A descriptive string

---

### Additional Sections

#### Class CodingErrorAction

java.lang.Object

- java.nio.charset.CodingErrorAction

java.nio.charset.CodingErrorAction

```java
public class
CodingErrorAction

extends
Object
```

A typesafe enumeration for coding-error actions.

Instances of this class are used to specify how malformed-input and
unmappable-character errors are to be handled by charset

decoders

and

encoders

.

**Since:** 1.4

public class

CodingErrorAction

extends

Object

A typesafe enumeration for coding-error actions.

Instances of this class are used to specify how malformed-input and
unmappable-character errors are to be handled by charset

decoders

and

encoders

.

Instances of this class are used to specify how malformed-input and
unmappable-character errors are to be handled by charset

decoders

and

encoders

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

CodingErrorAction

IGNORE

Action indicating that a coding error is to be handled by dropping the
erroneous input and resuming the coding operation.

static

CodingErrorAction

REPLACE

Action indicating that a coding error is to be handled by dropping the
erroneous input, appending the coder's replacement value to the output
buffer, and resuming the coding operation.

static

CodingErrorAction

REPORT

Action indicating that a coding error is to be reported, either by
returning a

CoderResult

object or by throwing a

CharacterCodingException

, whichever is appropriate for the method
implementing the coding process.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns a string describing this action.

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

static

CodingErrorAction

IGNORE

Action indicating that a coding error is to be handled by dropping the
erroneous input and resuming the coding operation.

static

CodingErrorAction

REPLACE

Action indicating that a coding error is to be handled by dropping the
erroneous input, appending the coder's replacement value to the output
buffer, and resuming the coding operation.

static

CodingErrorAction

REPORT

Action indicating that a coding error is to be reported, either by
returning a

CoderResult

object or by throwing a

CharacterCodingException

, whichever is appropriate for the method
implementing the coding process.

---

#### Field Summary

Action indicating that a coding error is to be handled by dropping the
erroneous input and resuming the coding operation.

Action indicating that a coding error is to be handled by dropping the
erroneous input, appending the coder's replacement value to the output
buffer, and resuming the coding operation.

Action indicating that a coding error is to be reported, either by
returning a

CoderResult

object or by throwing a

CharacterCodingException

, whichever is appropriate for the method
implementing the coding process.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns a string describing this action.

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

Returns a string describing this action.

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

- IGNORE

```java
public static final
CodingErrorAction
IGNORE
```

Action indicating that a coding error is to be handled by dropping the
erroneous input and resuming the coding operation.

- REPLACE

```java
public static final
CodingErrorAction
REPLACE
```

Action indicating that a coding error is to be handled by dropping the
erroneous input, appending the coder's replacement value to the output
buffer, and resuming the coding operation.

- REPORT

```java
public static final
CodingErrorAction
REPORT
```

Action indicating that a coding error is to be reported, either by
returning a

CoderResult

object or by throwing a

CharacterCodingException

, whichever is appropriate for the method
implementing the coding process.

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Returns a string describing this action.

**Overrides:** toString

in class

Object
**Returns:** A descriptive string

Field Detail

- IGNORE

```java
public static final
CodingErrorAction
IGNORE
```

Action indicating that a coding error is to be handled by dropping the
erroneous input and resuming the coding operation.

- REPLACE

```java
public static final
CodingErrorAction
REPLACE
```

Action indicating that a coding error is to be handled by dropping the
erroneous input, appending the coder's replacement value to the output
buffer, and resuming the coding operation.

- REPORT

```java
public static final
CodingErrorAction
REPORT
```

Action indicating that a coding error is to be reported, either by
returning a

CoderResult

object or by throwing a

CharacterCodingException

, whichever is appropriate for the method
implementing the coding process.

---

#### Field Detail

IGNORE

```java
public static final
CodingErrorAction
IGNORE
```

Action indicating that a coding error is to be handled by dropping the
erroneous input and resuming the coding operation.

---

#### IGNORE

public static final

CodingErrorAction

IGNORE

Action indicating that a coding error is to be handled by dropping the
erroneous input and resuming the coding operation.

REPLACE

```java
public static final
CodingErrorAction
REPLACE
```

Action indicating that a coding error is to be handled by dropping the
erroneous input, appending the coder's replacement value to the output
buffer, and resuming the coding operation.

---

#### REPLACE

public static final

CodingErrorAction

REPLACE

Action indicating that a coding error is to be handled by dropping the
erroneous input, appending the coder's replacement value to the output
buffer, and resuming the coding operation.

REPORT

```java
public static final
CodingErrorAction
REPORT
```

Action indicating that a coding error is to be reported, either by
returning a

CoderResult

object or by throwing a

CharacterCodingException

, whichever is appropriate for the method
implementing the coding process.

---

#### REPORT

public static final

CodingErrorAction

REPORT

Action indicating that a coding error is to be reported, either by
returning a

CoderResult

object or by throwing a

CharacterCodingException

, whichever is appropriate for the method
implementing the coding process.

Method Detail

- toString

```java
public
String
toString()
```

Returns a string describing this action.

**Overrides:** toString

in class

Object
**Returns:** A descriptive string

---

#### Method Detail

toString

```java
public
String
toString()
```

Returns a string describing this action.

**Overrides:** toString

in class

Object
**Returns:** A descriptive string

---

#### toString

public

String

toString()

Returns a string describing this action.

---

