# Class EvalException

**Source:** `jdk.jshell\jdk\jshell\EvalException.html`

### Class Description

```java
public class
EvalException

extends
JShellException
```

Wraps an throwable thrown in the executing client.
An instance of

EvalException

can be returned in the

SnippetEvent.exception()

query.
The name of the throwable thrown is available from

getExceptionClassName()

.
Message and stack can be queried by methods on

Exception

.

Note that in stack trace frames representing JShell Snippets,

StackTraceElement.getFileName()

will return "#" followed by
the Snippet id and for snippets without a method name (for example an
expression)

StackTraceElement.getMethodName()

will be the
empty string.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getExceptionClassName()

Returns the name of the Throwable subclass which was thrown in the
executing client. Note this class may not be loaded in the controlling
process.
See

Class.getName()

for the format of the string.

**Returns:**
- the name of the exception class as a String

---

#### public
JShellException
getCause()

Returns the wrapped cause of the throwable in the executing client
represented by this

EvalException

or

null

if the cause is
nonexistent or unknown.

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause wrapped in a

EvalException

or

UnresolvedReferenceException

or return

null

if the cause
is nonexistent or unknown.

**Since:**
- 11

---

### Additional Sections

#### Class EvalException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - jdk.jshell.JShellException
- - jdk.jshell.EvalException

java.lang.Throwable

- java.lang.Exception
- - jdk.jshell.JShellException
- - jdk.jshell.EvalException

java.lang.Exception

- jdk.jshell.JShellException
- - jdk.jshell.EvalException

jdk.jshell.JShellException

- jdk.jshell.EvalException

jdk.jshell.EvalException

**All Implemented Interfaces:** Serializable

```java
public class
EvalException

extends
JShellException
```

Wraps an throwable thrown in the executing client.
An instance of

EvalException

can be returned in the

SnippetEvent.exception()

query.
The name of the throwable thrown is available from

getExceptionClassName()

.
Message and stack can be queried by methods on

Exception

.

Note that in stack trace frames representing JShell Snippets,

StackTraceElement.getFileName()

will return "#" followed by
the Snippet id and for snippets without a method name (for example an
expression)

StackTraceElement.getMethodName()

will be the
empty string.

**Since:** 9
**See Also:** Serialized Form

public class

EvalException

extends

JShellException

Wraps an throwable thrown in the executing client.
An instance of

EvalException

can be returned in the

SnippetEvent.exception()

query.
The name of the throwable thrown is available from

getExceptionClassName()

.
Message and stack can be queried by methods on

Exception

.

Note that in stack trace frames representing JShell Snippets,

StackTraceElement.getFileName()

will return "#" followed by
the Snippet id and for snippets without a method name (for example an
expression)

StackTraceElement.getMethodName()

will be the
empty string.

Note that in stack trace frames representing JShell Snippets,

StackTraceElement.getFileName()

will return "#" followed by
the Snippet id and for snippets without a method name (for example an
expression)

StackTraceElement.getMethodName()

will be the
empty string.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JShellException

getCause

()

Returns the wrapped cause of the throwable in the executing client
represented by this

EvalException

or

null

if the cause is
nonexistent or unknown.

String

getExceptionClassName

()

Returns the name of the Throwable subclass which was thrown in the
executing client.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JShellException

getCause

()

Returns the wrapped cause of the throwable in the executing client
represented by this

EvalException

or

null

if the cause is
nonexistent or unknown.

String

getExceptionClassName

()

Returns the name of the Throwable subclass which was thrown in the
executing client.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

Returns the wrapped cause of the throwable in the executing client
represented by this

EvalException

or

null

if the cause is
nonexistent or unknown.

Returns the name of the Throwable subclass which was thrown in the
executing client.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

============ METHOD DETAIL ==========

- Method Detail

- getExceptionClassName

```java
public
String
getExceptionClassName()
```

Returns the name of the Throwable subclass which was thrown in the
executing client. Note this class may not be loaded in the controlling
process.
See

Class.getName()

for the format of the string.

**Returns:** the name of the exception class as a String

- getCause

```java
public
JShellException
getCause()
```

Returns the wrapped cause of the throwable in the executing client
represented by this

EvalException

or

null

if the cause is
nonexistent or unknown.

**Overrides:** getCause

in class

Throwable
**Returns:** the cause wrapped in a

EvalException

or

UnresolvedReferenceException

or return

null

if the cause
is nonexistent or unknown.
**Since:** 11

Method Detail

- getExceptionClassName

```java
public
String
getExceptionClassName()
```

Returns the name of the Throwable subclass which was thrown in the
executing client. Note this class may not be loaded in the controlling
process.
See

Class.getName()

for the format of the string.

**Returns:** the name of the exception class as a String

- getCause

```java
public
JShellException
getCause()
```

Returns the wrapped cause of the throwable in the executing client
represented by this

EvalException

or

null

if the cause is
nonexistent or unknown.

**Overrides:** getCause

in class

Throwable
**Returns:** the cause wrapped in a

EvalException

or

UnresolvedReferenceException

or return

null

if the cause
is nonexistent or unknown.
**Since:** 11

---

#### Method Detail

getExceptionClassName

```java
public
String
getExceptionClassName()
```

Returns the name of the Throwable subclass which was thrown in the
executing client. Note this class may not be loaded in the controlling
process.
See

Class.getName()

for the format of the string.

**Returns:** the name of the exception class as a String

---

#### getExceptionClassName

public

String

getExceptionClassName()

Returns the name of the Throwable subclass which was thrown in the
executing client. Note this class may not be loaded in the controlling
process.
See

Class.getName()

for the format of the string.

getCause

```java
public
JShellException
getCause()
```

Returns the wrapped cause of the throwable in the executing client
represented by this

EvalException

or

null

if the cause is
nonexistent or unknown.

**Overrides:** getCause

in class

Throwable
**Returns:** the cause wrapped in a

EvalException

or

UnresolvedReferenceException

or return

null

if the cause
is nonexistent or unknown.
**Since:** 11

---

#### getCause

public

JShellException

getCause()

Returns the wrapped cause of the throwable in the executing client
represented by this

EvalException

or

null

if the cause is
nonexistent or unknown.

---

