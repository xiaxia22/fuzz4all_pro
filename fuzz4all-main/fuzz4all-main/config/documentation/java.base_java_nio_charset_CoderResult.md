# Class CoderResult

**Source:** `java.base\java\nio\charset\CoderResult.html`

### Class Description

```java
public class
CoderResult

extends
Object
```

A description of the result state of a coder.

A charset coder, that is, either a decoder or an encoder, consumes bytes
(or characters) from an input buffer, translates them, and writes the
resulting characters (or bytes) to an output buffer. A coding process
terminates for one of four categories of reasons, which are described by
instances of this class:

- Underflow

is reported when there is no more input to be
processed, or there is insufficient input and additional input is
required. This condition is represented by the unique result object

UNDERFLOW

, whose

isUnderflow

method
returns

true

.
- Overflow

is reported when there is insufficient room
remaining in the output buffer. This condition is represented by the
unique result object

OVERFLOW

, whose

isOverflow

method returns

true

.
- A

malformed-input error

is reported when a sequence of
input units is not well-formed. Such errors are described by instances of
this class whose

isMalformed

method returns

true

and whose

length

method returns the length
of the malformed sequence. There is one unique instance of this class for
all malformed-input errors of a given length.
- An

unmappable-character error

is reported when a sequence
of input units denotes a character that cannot be represented in the
output charset. Such errors are described by instances of this class
whose

isUnmappable

method returns

true

and
whose

length

method returns the length of the input
sequence denoting the unmappable character. There is one unique instance
of this class for all unmappable-character errors of a given length.

For convenience, the

isError

method returns

true

for result objects that describe malformed-input and unmappable-character
errors but

false

for those that describe underflow or overflow
conditions.

**Since:** 1.4

---

### Field Details

#### public static final
CoderResult
UNDERFLOW

Result object indicating underflow, meaning that either the input buffer
has been completely consumed or, if the input buffer is not yet empty,
that additional input is required.

---

#### public static final
CoderResult
OVERFLOW

Result object indicating overflow, meaning that there is insufficient
room in the output buffer.

---

### Constructor Details

*No entries found.*

### Method Details

#### public
String
toString()

Returns a string describing this coder result.

**Overrides:**
- toString

in class

Object

**Returns:**
- A descriptive string

---

#### public boolean isUnderflow()

Tells whether or not this object describes an underflow condition.

**Returns:**
- true

if, and only if, this object denotes underflow

---

#### public boolean isOverflow()

Tells whether or not this object describes an overflow condition.

**Returns:**
- true

if, and only if, this object denotes overflow

---

#### public boolean isError()

Tells whether or not this object describes an error condition.

**Returns:**
- true

if, and only if, this object denotes either a
malformed-input error or an unmappable-character error

---

#### public boolean isMalformed()

Tells whether or not this object describes a malformed-input error.

**Returns:**
- true

if, and only if, this object denotes a
malformed-input error

---

#### public boolean isUnmappable()

Tells whether or not this object describes an unmappable-character
error.

**Returns:**
- true

if, and only if, this object denotes an
unmappable-character error

---

#### public int length()

Returns the length of the erroneous input described by this
object

(optional operation)

.

**Returns:**
- The length of the erroneous input, a positive integer

**Throws:**
- UnsupportedOperationException

- If this object does not describe an error condition, that is,
if the

isError

does not return

true

---

#### public static
CoderResult
malformedForLength​(int length)

Static factory method that returns the unique object describing a
malformed-input error of the given length.

**Parameters:**
- length

- The given length

**Returns:**
- The requested coder-result object

---

#### public static
CoderResult
unmappableForLength​(int length)

Static factory method that returns the unique result object describing
an unmappable-character error of the given length.

**Parameters:**
- length

- The given length

**Returns:**
- The requested coder-result object

---

#### public void throwException()
throws
CharacterCodingException

Throws an exception appropriate to the result described by this object.

**Throws:**
- BufferUnderflowException

- If this object is

UNDERFLOW
- BufferOverflowException

- If this object is

OVERFLOW
- MalformedInputException

- If this object represents a malformed-input error; the
exception's length value will be that of this object
- UnmappableCharacterException

- If this object represents an unmappable-character error; the
exceptions length value will be that of this object
- CharacterCodingException

---

### Additional Sections

#### Class CoderResult

java.lang.Object

- java.nio.charset.CoderResult

java.nio.charset.CoderResult

```java
public class
CoderResult

extends
Object
```

A description of the result state of a coder.

A charset coder, that is, either a decoder or an encoder, consumes bytes
(or characters) from an input buffer, translates them, and writes the
resulting characters (or bytes) to an output buffer. A coding process
terminates for one of four categories of reasons, which are described by
instances of this class:

- Underflow

is reported when there is no more input to be
processed, or there is insufficient input and additional input is
required. This condition is represented by the unique result object

UNDERFLOW

, whose

isUnderflow

method
returns

true

.
- Overflow

is reported when there is insufficient room
remaining in the output buffer. This condition is represented by the
unique result object

OVERFLOW

, whose

isOverflow

method returns

true

.
- A

malformed-input error

is reported when a sequence of
input units is not well-formed. Such errors are described by instances of
this class whose

isMalformed

method returns

true

and whose

length

method returns the length
of the malformed sequence. There is one unique instance of this class for
all malformed-input errors of a given length.
- An

unmappable-character error

is reported when a sequence
of input units denotes a character that cannot be represented in the
output charset. Such errors are described by instances of this class
whose

isUnmappable

method returns

true

and
whose

length

method returns the length of the input
sequence denoting the unmappable character. There is one unique instance
of this class for all unmappable-character errors of a given length.

For convenience, the

isError

method returns

true

for result objects that describe malformed-input and unmappable-character
errors but

false

for those that describe underflow or overflow
conditions.

**Since:** 1.4

public class

CoderResult

extends

Object

A description of the result state of a coder.

A charset coder, that is, either a decoder or an encoder, consumes bytes
(or characters) from an input buffer, translates them, and writes the
resulting characters (or bytes) to an output buffer. A coding process
terminates for one of four categories of reasons, which are described by
instances of this class:

- Underflow

is reported when there is no more input to be
processed, or there is insufficient input and additional input is
required. This condition is represented by the unique result object

UNDERFLOW

, whose

isUnderflow

method
returns

true

.
- Overflow

is reported when there is insufficient room
remaining in the output buffer. This condition is represented by the
unique result object

OVERFLOW

, whose

isOverflow

method returns

true

.
- A

malformed-input error

is reported when a sequence of
input units is not well-formed. Such errors are described by instances of
this class whose

isMalformed

method returns

true

and whose

length

method returns the length
of the malformed sequence. There is one unique instance of this class for
all malformed-input errors of a given length.
- An

unmappable-character error

is reported when a sequence
of input units denotes a character that cannot be represented in the
output charset. Such errors are described by instances of this class
whose

isUnmappable

method returns

true

and
whose

length

method returns the length of the input
sequence denoting the unmappable character. There is one unique instance
of this class for all unmappable-character errors of a given length.

For convenience, the

isError

method returns

true

for result objects that describe malformed-input and unmappable-character
errors but

false

for those that describe underflow or overflow
conditions.

A charset coder, that is, either a decoder or an encoder, consumes bytes
(or characters) from an input buffer, translates them, and writes the
resulting characters (or bytes) to an output buffer. A coding process
terminates for one of four categories of reasons, which are described by
instances of this class:

- Underflow

is reported when there is no more input to be
processed, or there is insufficient input and additional input is
required. This condition is represented by the unique result object

UNDERFLOW

, whose

isUnderflow

method
returns

true

.
- Overflow

is reported when there is insufficient room
remaining in the output buffer. This condition is represented by the
unique result object

OVERFLOW

, whose

isOverflow

method returns

true

.
- A

malformed-input error

is reported when a sequence of
input units is not well-formed. Such errors are described by instances of
this class whose

isMalformed

method returns

true

and whose

length

method returns the length
of the malformed sequence. There is one unique instance of this class for
all malformed-input errors of a given length.
- An

unmappable-character error

is reported when a sequence
of input units denotes a character that cannot be represented in the
output charset. Such errors are described by instances of this class
whose

isUnmappable

method returns

true

and
whose

length

method returns the length of the input
sequence denoting the unmappable character. There is one unique instance
of this class for all unmappable-character errors of a given length.

For convenience, the

isError

method returns

true

for result objects that describe malformed-input and unmappable-character
errors but

false

for those that describe underflow or overflow
conditions.

Underflow

is reported when there is no more input to be
processed, or there is insufficient input and additional input is
required. This condition is represented by the unique result object

UNDERFLOW

, whose

isUnderflow

method
returns

true

.

Overflow

is reported when there is insufficient room
remaining in the output buffer. This condition is represented by the
unique result object

OVERFLOW

, whose

isOverflow

method returns

true

.

A

malformed-input error

is reported when a sequence of
input units is not well-formed. Such errors are described by instances of
this class whose

isMalformed

method returns

true

and whose

length

method returns the length
of the malformed sequence. There is one unique instance of this class for
all malformed-input errors of a given length.

An

unmappable-character error

is reported when a sequence
of input units denotes a character that cannot be represented in the
output charset. Such errors are described by instances of this class
whose

isUnmappable

method returns

true

and
whose

length

method returns the length of the input
sequence denoting the unmappable character. There is one unique instance
of this class for all unmappable-character errors of a given length.

Underflow

is reported when there is no more input to be
processed, or there is insufficient input and additional input is
required. This condition is represented by the unique result object

UNDERFLOW

, whose

isUnderflow

method
returns

true

.

Overflow

is reported when there is insufficient room
remaining in the output buffer. This condition is represented by the
unique result object

OVERFLOW

, whose

isOverflow

method returns

true

.

A

malformed-input error

is reported when a sequence of
input units is not well-formed. Such errors are described by instances of
this class whose

isMalformed

method returns

true

and whose

length

method returns the length
of the malformed sequence. There is one unique instance of this class for
all malformed-input errors of a given length.

An

unmappable-character error

is reported when a sequence
of input units denotes a character that cannot be represented in the
output charset. Such errors are described by instances of this class
whose

isUnmappable

method returns

true

and
whose

length

method returns the length of the input
sequence denoting the unmappable character. There is one unique instance
of this class for all unmappable-character errors of a given length.

For convenience, the

isError

method returns

true

for result objects that describe malformed-input and unmappable-character
errors but

false

for those that describe underflow or overflow
conditions.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

CoderResult

OVERFLOW

Result object indicating overflow, meaning that there is insufficient
room in the output buffer.

static

CoderResult

UNDERFLOW

Result object indicating underflow, meaning that either the input buffer
has been completely consumed or, if the input buffer is not yet empty,
that additional input is required.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isError

()

Tells whether or not this object describes an error condition.

boolean

isMalformed

()

Tells whether or not this object describes a malformed-input error.

boolean

isOverflow

()

Tells whether or not this object describes an overflow condition.

boolean

isUnderflow

()

Tells whether or not this object describes an underflow condition.

boolean

isUnmappable

()

Tells whether or not this object describes an unmappable-character
error.

int

length

()

Returns the length of the erroneous input described by this
object

(optional operation)

.

static

CoderResult

malformedForLength

​(int length)

Static factory method that returns the unique object describing a
malformed-input error of the given length.

void

throwException

()

Throws an exception appropriate to the result described by this object.

String

toString

()

Returns a string describing this coder result.

static

CoderResult

unmappableForLength

​(int length)

Static factory method that returns the unique result object describing
an unmappable-character error of the given length.

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

CoderResult

OVERFLOW

Result object indicating overflow, meaning that there is insufficient
room in the output buffer.

static

CoderResult

UNDERFLOW

Result object indicating underflow, meaning that either the input buffer
has been completely consumed or, if the input buffer is not yet empty,
that additional input is required.

---

#### Field Summary

Result object indicating overflow, meaning that there is insufficient
room in the output buffer.

Result object indicating underflow, meaning that either the input buffer
has been completely consumed or, if the input buffer is not yet empty,
that additional input is required.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isError

()

Tells whether or not this object describes an error condition.

boolean

isMalformed

()

Tells whether or not this object describes a malformed-input error.

boolean

isOverflow

()

Tells whether or not this object describes an overflow condition.

boolean

isUnderflow

()

Tells whether or not this object describes an underflow condition.

boolean

isUnmappable

()

Tells whether or not this object describes an unmappable-character
error.

int

length

()

Returns the length of the erroneous input described by this
object

(optional operation)

.

static

CoderResult

malformedForLength

​(int length)

Static factory method that returns the unique object describing a
malformed-input error of the given length.

void

throwException

()

Throws an exception appropriate to the result described by this object.

String

toString

()

Returns a string describing this coder result.

static

CoderResult

unmappableForLength

​(int length)

Static factory method that returns the unique result object describing
an unmappable-character error of the given length.

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

Tells whether or not this object describes an error condition.

Tells whether or not this object describes a malformed-input error.

Tells whether or not this object describes an overflow condition.

Tells whether or not this object describes an underflow condition.

Tells whether or not this object describes an unmappable-character
error.

Returns the length of the erroneous input described by this
object

(optional operation)

.

Static factory method that returns the unique object describing a
malformed-input error of the given length.

Throws an exception appropriate to the result described by this object.

Returns a string describing this coder result.

Static factory method that returns the unique result object describing
an unmappable-character error of the given length.

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

- UNDERFLOW

```java
public static final
CoderResult
UNDERFLOW
```

Result object indicating underflow, meaning that either the input buffer
has been completely consumed or, if the input buffer is not yet empty,
that additional input is required.

- OVERFLOW

```java
public static final
CoderResult
OVERFLOW
```

Result object indicating overflow, meaning that there is insufficient
room in the output buffer.

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Returns a string describing this coder result.

**Overrides:** toString

in class

Object
**Returns:** A descriptive string

- isUnderflow

```java
public boolean isUnderflow()
```

Tells whether or not this object describes an underflow condition.

**Returns:** true

if, and only if, this object denotes underflow

- isOverflow

```java
public boolean isOverflow()
```

Tells whether or not this object describes an overflow condition.

**Returns:** true

if, and only if, this object denotes overflow

- isError

```java
public boolean isError()
```

Tells whether or not this object describes an error condition.

**Returns:** true

if, and only if, this object denotes either a
malformed-input error or an unmappable-character error

- isMalformed

```java
public boolean isMalformed()
```

Tells whether or not this object describes a malformed-input error.

**Returns:** true

if, and only if, this object denotes a
malformed-input error

- isUnmappable

```java
public boolean isUnmappable()
```

Tells whether or not this object describes an unmappable-character
error.

**Returns:** true

if, and only if, this object denotes an
unmappable-character error

- length

```java
public int length()
```

Returns the length of the erroneous input described by this
object

(optional operation)

.

**Returns:** The length of the erroneous input, a positive integer
**Throws:** UnsupportedOperationException

- If this object does not describe an error condition, that is,
if the

isError

does not return

true

- malformedForLength

```java
public static
CoderResult
malformedForLength​(int length)
```

Static factory method that returns the unique object describing a
malformed-input error of the given length.

**Parameters:** length

- The given length
**Returns:** The requested coder-result object

- unmappableForLength

```java
public static
CoderResult
unmappableForLength​(int length)
```

Static factory method that returns the unique result object describing
an unmappable-character error of the given length.

**Parameters:** length

- The given length
**Returns:** The requested coder-result object

- throwException

```java
public void throwException()
throws
CharacterCodingException
```

Throws an exception appropriate to the result described by this object.

**Throws:** BufferUnderflowException

- If this object is

UNDERFLOW
**Throws:** BufferOverflowException

- If this object is

OVERFLOW
**Throws:** MalformedInputException

- If this object represents a malformed-input error; the
exception's length value will be that of this object
**Throws:** UnmappableCharacterException

- If this object represents an unmappable-character error; the
exceptions length value will be that of this object
**Throws:** CharacterCodingException

Field Detail

- UNDERFLOW

```java
public static final
CoderResult
UNDERFLOW
```

Result object indicating underflow, meaning that either the input buffer
has been completely consumed or, if the input buffer is not yet empty,
that additional input is required.

- OVERFLOW

```java
public static final
CoderResult
OVERFLOW
```

Result object indicating overflow, meaning that there is insufficient
room in the output buffer.

---

#### Field Detail

UNDERFLOW

```java
public static final
CoderResult
UNDERFLOW
```

Result object indicating underflow, meaning that either the input buffer
has been completely consumed or, if the input buffer is not yet empty,
that additional input is required.

---

#### UNDERFLOW

public static final

CoderResult

UNDERFLOW

Result object indicating underflow, meaning that either the input buffer
has been completely consumed or, if the input buffer is not yet empty,
that additional input is required.

OVERFLOW

```java
public static final
CoderResult
OVERFLOW
```

Result object indicating overflow, meaning that there is insufficient
room in the output buffer.

---

#### OVERFLOW

public static final

CoderResult

OVERFLOW

Result object indicating overflow, meaning that there is insufficient
room in the output buffer.

Method Detail

- toString

```java
public
String
toString()
```

Returns a string describing this coder result.

**Overrides:** toString

in class

Object
**Returns:** A descriptive string

- isUnderflow

```java
public boolean isUnderflow()
```

Tells whether or not this object describes an underflow condition.

**Returns:** true

if, and only if, this object denotes underflow

- isOverflow

```java
public boolean isOverflow()
```

Tells whether or not this object describes an overflow condition.

**Returns:** true

if, and only if, this object denotes overflow

- isError

```java
public boolean isError()
```

Tells whether or not this object describes an error condition.

**Returns:** true

if, and only if, this object denotes either a
malformed-input error or an unmappable-character error

- isMalformed

```java
public boolean isMalformed()
```

Tells whether or not this object describes a malformed-input error.

**Returns:** true

if, and only if, this object denotes a
malformed-input error

- isUnmappable

```java
public boolean isUnmappable()
```

Tells whether or not this object describes an unmappable-character
error.

**Returns:** true

if, and only if, this object denotes an
unmappable-character error

- length

```java
public int length()
```

Returns the length of the erroneous input described by this
object

(optional operation)

.

**Returns:** The length of the erroneous input, a positive integer
**Throws:** UnsupportedOperationException

- If this object does not describe an error condition, that is,
if the

isError

does not return

true

- malformedForLength

```java
public static
CoderResult
malformedForLength​(int length)
```

Static factory method that returns the unique object describing a
malformed-input error of the given length.

**Parameters:** length

- The given length
**Returns:** The requested coder-result object

- unmappableForLength

```java
public static
CoderResult
unmappableForLength​(int length)
```

Static factory method that returns the unique result object describing
an unmappable-character error of the given length.

**Parameters:** length

- The given length
**Returns:** The requested coder-result object

- throwException

```java
public void throwException()
throws
CharacterCodingException
```

Throws an exception appropriate to the result described by this object.

**Throws:** BufferUnderflowException

- If this object is

UNDERFLOW
**Throws:** BufferOverflowException

- If this object is

OVERFLOW
**Throws:** MalformedInputException

- If this object represents a malformed-input error; the
exception's length value will be that of this object
**Throws:** UnmappableCharacterException

- If this object represents an unmappable-character error; the
exceptions length value will be that of this object
**Throws:** CharacterCodingException

---

#### Method Detail

toString

```java
public
String
toString()
```

Returns a string describing this coder result.

**Overrides:** toString

in class

Object
**Returns:** A descriptive string

---

#### toString

public

String

toString()

Returns a string describing this coder result.

isUnderflow

```java
public boolean isUnderflow()
```

Tells whether or not this object describes an underflow condition.

**Returns:** true

if, and only if, this object denotes underflow

---

#### isUnderflow

public boolean isUnderflow()

Tells whether or not this object describes an underflow condition.

isOverflow

```java
public boolean isOverflow()
```

Tells whether or not this object describes an overflow condition.

**Returns:** true

if, and only if, this object denotes overflow

---

#### isOverflow

public boolean isOverflow()

Tells whether or not this object describes an overflow condition.

isError

```java
public boolean isError()
```

Tells whether or not this object describes an error condition.

**Returns:** true

if, and only if, this object denotes either a
malformed-input error or an unmappable-character error

---

#### isError

public boolean isError()

Tells whether or not this object describes an error condition.

isMalformed

```java
public boolean isMalformed()
```

Tells whether or not this object describes a malformed-input error.

**Returns:** true

if, and only if, this object denotes a
malformed-input error

---

#### isMalformed

public boolean isMalformed()

Tells whether or not this object describes a malformed-input error.

isUnmappable

```java
public boolean isUnmappable()
```

Tells whether or not this object describes an unmappable-character
error.

**Returns:** true

if, and only if, this object denotes an
unmappable-character error

---

#### isUnmappable

public boolean isUnmappable()

Tells whether or not this object describes an unmappable-character
error.

length

```java
public int length()
```

Returns the length of the erroneous input described by this
object

(optional operation)

.

**Returns:** The length of the erroneous input, a positive integer
**Throws:** UnsupportedOperationException

- If this object does not describe an error condition, that is,
if the

isError

does not return

true

---

#### length

public int length()

Returns the length of the erroneous input described by this
object

(optional operation)

.

malformedForLength

```java
public static
CoderResult
malformedForLength​(int length)
```

Static factory method that returns the unique object describing a
malformed-input error of the given length.

**Parameters:** length

- The given length
**Returns:** The requested coder-result object

---

#### malformedForLength

public static

CoderResult

malformedForLength​(int length)

Static factory method that returns the unique object describing a
malformed-input error of the given length.

unmappableForLength

```java
public static
CoderResult
unmappableForLength​(int length)
```

Static factory method that returns the unique result object describing
an unmappable-character error of the given length.

**Parameters:** length

- The given length
**Returns:** The requested coder-result object

---

#### unmappableForLength

public static

CoderResult

unmappableForLength​(int length)

Static factory method that returns the unique result object describing
an unmappable-character error of the given length.

throwException

```java
public void throwException()
throws
CharacterCodingException
```

Throws an exception appropriate to the result described by this object.

**Throws:** BufferUnderflowException

- If this object is

UNDERFLOW
**Throws:** BufferOverflowException

- If this object is

OVERFLOW
**Throws:** MalformedInputException

- If this object represents a malformed-input error; the
exception's length value will be that of this object
**Throws:** UnmappableCharacterException

- If this object represents an unmappable-character error; the
exceptions length value will be that of this object
**Throws:** CharacterCodingException

---

#### throwException

public void throwException()
throws

CharacterCodingException

Throws an exception appropriate to the result described by this object.

---

