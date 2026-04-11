# Interface ErrorListener

**Source:** `java.xml\javax\xml\transform\ErrorListener.html`

### Class Description

```java
public interface
ErrorListener
```

To provide customized error handling, implement this interface and
use the

setErrorListener

method to register an instance of the
implementation with the

Transformer

. The

Transformer

then reports all errors and warnings through this
interface.

If an application does

not

register its own custom

ErrorListener

, the default

ErrorListener

is used which reports all warnings and errors to

System.err

and does not throw any

Exception

s.
Applications are

strongly

encouraged to register and use

ErrorListener

s that insure proper behavior for warnings and
errors.

For transformation errors, a

Transformer

must use this
interface instead of throwing an

Exception

: it is up to the
application to decide whether to throw an

Exception

for
different types of errors and warnings. Note however that the

Transformer

is not required to continue with the transformation
after a call to

fatalError(TransformerException exception)

.

Transformer

s may use this mechanism to report XML parsing
errors as well as transformation errors.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void warning​(
TransformerException
exception)
throws
TransformerException

Receive notification of a warning.

Transformer

can use this method to report
conditions that are not errors or fatal errors. The default behaviour
is to take no action.

After invoking this method, the Transformer must continue with
the transformation. It should still be possible for the
application to process the document through to the end.

**Parameters:**
- exception

- The warning information encapsulated in a
transformer exception.

**Throws:**
- TransformerException

- if the application
chooses to discontinue the transformation.

**See Also:**
- TransformerException

---

#### void error​(
TransformerException
exception)
throws
TransformerException

Receive notification of a recoverable error.

The transformer must continue to try and provide normal transformation
after invoking this method. It should still be possible for the
application to process the document through to the end if no other errors
are encountered.

**Parameters:**
- exception

- The error information encapsulated in a
transformer exception.

**Throws:**
- TransformerException

- if the application
chooses to discontinue the transformation.

**See Also:**
- TransformerException

---

#### void fatalError​(
TransformerException
exception)
throws
TransformerException

Receive notification of a non-recoverable error.

The processor may choose to continue, but will not normally
proceed to a successful completion.

The method should throw an exception if it is unable to
process the error, or if it wishes execution to terminate
immediately. The processor will not necessarily honor this
request.

**Parameters:**
- exception

- The error information encapsulated in a

TransformerException

.

**Throws:**
- TransformerException

- if the application
chooses to discontinue the transformation.

**See Also:**
- TransformerException

---

### Additional Sections

#### Interface ErrorListener

```java
public interface
ErrorListener
```

To provide customized error handling, implement this interface and
use the

setErrorListener

method to register an instance of the
implementation with the

Transformer

. The

Transformer

then reports all errors and warnings through this
interface.

If an application does

not

register its own custom

ErrorListener

, the default

ErrorListener

is used which reports all warnings and errors to

System.err

and does not throw any

Exception

s.
Applications are

strongly

encouraged to register and use

ErrorListener

s that insure proper behavior for warnings and
errors.

For transformation errors, a

Transformer

must use this
interface instead of throwing an

Exception

: it is up to the
application to decide whether to throw an

Exception

for
different types of errors and warnings. Note however that the

Transformer

is not required to continue with the transformation
after a call to

fatalError(TransformerException exception)

.

Transformer

s may use this mechanism to report XML parsing
errors as well as transformation errors.

**Since:** 1.4

public interface

ErrorListener

To provide customized error handling, implement this interface and
use the

setErrorListener

method to register an instance of the
implementation with the

Transformer

. The

Transformer

then reports all errors and warnings through this
interface.

If an application does

not

register its own custom

ErrorListener

, the default

ErrorListener

is used which reports all warnings and errors to

System.err

and does not throw any

Exception

s.
Applications are

strongly

encouraged to register and use

ErrorListener

s that insure proper behavior for warnings and
errors.

For transformation errors, a

Transformer

must use this
interface instead of throwing an

Exception

: it is up to the
application to decide whether to throw an

Exception

for
different types of errors and warnings. Note however that the

Transformer

is not required to continue with the transformation
after a call to

fatalError(TransformerException exception)

.

Transformer

s may use this mechanism to report XML parsing
errors as well as transformation errors.

To provide customized error handling, implement this interface and
use the

setErrorListener

method to register an instance of the
implementation with the

Transformer

. The

Transformer

then reports all errors and warnings through this
interface.

If an application does

not

register its own custom

ErrorListener

, the default

ErrorListener

is used which reports all warnings and errors to

System.err

and does not throw any

Exception

s.
Applications are

strongly

encouraged to register and use

ErrorListener

s that insure proper behavior for warnings and
errors.

For transformation errors, a

Transformer

must use this
interface instead of throwing an

Exception

: it is up to the
application to decide whether to throw an

Exception

for
different types of errors and warnings. Note however that the

Transformer

is not required to continue with the transformation
after a call to

fatalError(TransformerException exception)

.

Transformer

s may use this mechanism to report XML parsing
errors as well as transformation errors.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

error

​(

TransformerException

exception)

Receive notification of a recoverable error.

void

fatalError

​(

TransformerException

exception)

Receive notification of a non-recoverable error.

void

warning

​(

TransformerException

exception)

Receive notification of a warning.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

error

​(

TransformerException

exception)

Receive notification of a recoverable error.

void

fatalError

​(

TransformerException

exception)

Receive notification of a non-recoverable error.

void

warning

​(

TransformerException

exception)

Receive notification of a warning.

---

#### Method Summary

Receive notification of a recoverable error.

Receive notification of a non-recoverable error.

Receive notification of a warning.

============ METHOD DETAIL ==========

- Method Detail

- warning

```java
void warning​(
TransformerException
exception)
throws
TransformerException
```

Receive notification of a warning.

Transformer

can use this method to report
conditions that are not errors or fatal errors. The default behaviour
is to take no action.

After invoking this method, the Transformer must continue with
the transformation. It should still be possible for the
application to process the document through to the end.

**Parameters:** exception

- The warning information encapsulated in a
transformer exception.
**Throws:** TransformerException

- if the application
chooses to discontinue the transformation.
**See Also:** TransformerException

- error

```java
void error​(
TransformerException
exception)
throws
TransformerException
```

Receive notification of a recoverable error.

The transformer must continue to try and provide normal transformation
after invoking this method. It should still be possible for the
application to process the document through to the end if no other errors
are encountered.

**Parameters:** exception

- The error information encapsulated in a
transformer exception.
**Throws:** TransformerException

- if the application
chooses to discontinue the transformation.
**See Also:** TransformerException

- fatalError

```java
void fatalError​(
TransformerException
exception)
throws
TransformerException
```

Receive notification of a non-recoverable error.

The processor may choose to continue, but will not normally
proceed to a successful completion.

The method should throw an exception if it is unable to
process the error, or if it wishes execution to terminate
immediately. The processor will not necessarily honor this
request.

**Parameters:** exception

- The error information encapsulated in a

TransformerException

.
**Throws:** TransformerException

- if the application
chooses to discontinue the transformation.
**See Also:** TransformerException

Method Detail

- warning

```java
void warning​(
TransformerException
exception)
throws
TransformerException
```

Receive notification of a warning.

Transformer

can use this method to report
conditions that are not errors or fatal errors. The default behaviour
is to take no action.

After invoking this method, the Transformer must continue with
the transformation. It should still be possible for the
application to process the document through to the end.

**Parameters:** exception

- The warning information encapsulated in a
transformer exception.
**Throws:** TransformerException

- if the application
chooses to discontinue the transformation.
**See Also:** TransformerException

- error

```java
void error​(
TransformerException
exception)
throws
TransformerException
```

Receive notification of a recoverable error.

The transformer must continue to try and provide normal transformation
after invoking this method. It should still be possible for the
application to process the document through to the end if no other errors
are encountered.

**Parameters:** exception

- The error information encapsulated in a
transformer exception.
**Throws:** TransformerException

- if the application
chooses to discontinue the transformation.
**See Also:** TransformerException

- fatalError

```java
void fatalError​(
TransformerException
exception)
throws
TransformerException
```

Receive notification of a non-recoverable error.

The processor may choose to continue, but will not normally
proceed to a successful completion.

The method should throw an exception if it is unable to
process the error, or if it wishes execution to terminate
immediately. The processor will not necessarily honor this
request.

**Parameters:** exception

- The error information encapsulated in a

TransformerException

.
**Throws:** TransformerException

- if the application
chooses to discontinue the transformation.
**See Also:** TransformerException

---

#### Method Detail

warning

```java
void warning​(
TransformerException
exception)
throws
TransformerException
```

Receive notification of a warning.

Transformer

can use this method to report
conditions that are not errors or fatal errors. The default behaviour
is to take no action.

After invoking this method, the Transformer must continue with
the transformation. It should still be possible for the
application to process the document through to the end.

**Parameters:** exception

- The warning information encapsulated in a
transformer exception.
**Throws:** TransformerException

- if the application
chooses to discontinue the transformation.
**See Also:** TransformerException

---

#### warning

void warning​(

TransformerException

exception)
throws

TransformerException

Receive notification of a warning.

Transformer

can use this method to report
conditions that are not errors or fatal errors. The default behaviour
is to take no action.

After invoking this method, the Transformer must continue with
the transformation. It should still be possible for the
application to process the document through to the end.

Transformer

can use this method to report
conditions that are not errors or fatal errors. The default behaviour
is to take no action.

After invoking this method, the Transformer must continue with
the transformation. It should still be possible for the
application to process the document through to the end.

error

```java
void error​(
TransformerException
exception)
throws
TransformerException
```

Receive notification of a recoverable error.

The transformer must continue to try and provide normal transformation
after invoking this method. It should still be possible for the
application to process the document through to the end if no other errors
are encountered.

**Parameters:** exception

- The error information encapsulated in a
transformer exception.
**Throws:** TransformerException

- if the application
chooses to discontinue the transformation.
**See Also:** TransformerException

---

#### error

void error​(

TransformerException

exception)
throws

TransformerException

Receive notification of a recoverable error.

The transformer must continue to try and provide normal transformation
after invoking this method. It should still be possible for the
application to process the document through to the end if no other errors
are encountered.

The transformer must continue to try and provide normal transformation
after invoking this method. It should still be possible for the
application to process the document through to the end if no other errors
are encountered.

fatalError

```java
void fatalError​(
TransformerException
exception)
throws
TransformerException
```

Receive notification of a non-recoverable error.

The processor may choose to continue, but will not normally
proceed to a successful completion.

The method should throw an exception if it is unable to
process the error, or if it wishes execution to terminate
immediately. The processor will not necessarily honor this
request.

**Parameters:** exception

- The error information encapsulated in a

TransformerException

.
**Throws:** TransformerException

- if the application
chooses to discontinue the transformation.
**See Also:** TransformerException

---

#### fatalError

void fatalError​(

TransformerException

exception)
throws

TransformerException

Receive notification of a non-recoverable error.

The processor may choose to continue, but will not normally
proceed to a successful completion.

The method should throw an exception if it is unable to
process the error, or if it wishes execution to terminate
immediately. The processor will not necessarily honor this
request.

Receive notification of a non-recoverable error.

The processor may choose to continue, but will not normally
proceed to a successful completion.

The method should throw an exception if it is unable to
process the error, or if it wishes execution to terminate
immediately. The processor will not necessarily honor this
request.

---

