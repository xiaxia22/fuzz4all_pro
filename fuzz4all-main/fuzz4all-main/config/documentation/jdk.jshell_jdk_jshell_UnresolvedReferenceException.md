# Class UnresolvedReferenceException

**Source:** `jdk.jshell\jdk\jshell\UnresolvedReferenceException.html`

### Class Description

```java
public class
UnresolvedReferenceException

extends
JShellException
```

Exception reported on attempting to execute a

RECOVERABLE_DEFINED

snippet.

The stack can be queried by methods on

Exception

.
Note that in stack trace frames representing JShell Snippets,

StackTraceElement.getFileName()

will return "#" followed by
the Snippet id and for snippets without a method name (for example an
expression)

StackTraceElement.getName()

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
DeclarationSnippet
getSnippet()

Return the Snippet which has the unresolved reference(s).

**Returns:**
- the

Snippet

of the

RECOVERABLE_DEFINED

definition snippet.

---

### Additional Sections

#### Class UnresolvedReferenceException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - jdk.jshell.JShellException
- - jdk.jshell.UnresolvedReferenceException

java.lang.Throwable

- java.lang.Exception
- - jdk.jshell.JShellException
- - jdk.jshell.UnresolvedReferenceException

java.lang.Exception

- jdk.jshell.JShellException
- - jdk.jshell.UnresolvedReferenceException

jdk.jshell.JShellException

- jdk.jshell.UnresolvedReferenceException

jdk.jshell.UnresolvedReferenceException

**All Implemented Interfaces:** Serializable

```java
public class
UnresolvedReferenceException

extends
JShellException
```

Exception reported on attempting to execute a

RECOVERABLE_DEFINED

snippet.

The stack can be queried by methods on

Exception

.
Note that in stack trace frames representing JShell Snippets,

StackTraceElement.getFileName()

will return "#" followed by
the Snippet id and for snippets without a method name (for example an
expression)

StackTraceElement.getName()

will be the
empty string.

**Since:** 9
**See Also:** Serialized Form

public class

UnresolvedReferenceException

extends

JShellException

Exception reported on attempting to execute a

RECOVERABLE_DEFINED

snippet.

The stack can be queried by methods on

Exception

.
Note that in stack trace frames representing JShell Snippets,

StackTraceElement.getFileName()

will return "#" followed by
the Snippet id and for snippets without a method name (for example an
expression)

StackTraceElement.getName()

will be the
empty string.

The stack can be queried by methods on

Exception

.
Note that in stack trace frames representing JShell Snippets,

StackTraceElement.getFileName()

will return "#" followed by
the Snippet id and for snippets without a method name (for example an
expression)

StackTraceElement.getName()

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

DeclarationSnippet

getSnippet

()

Return the Snippet which has the unresolved reference(s).

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DeclarationSnippet

getSnippet

()

Return the Snippet which has the unresolved reference(s).

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

Return the Snippet which has the unresolved reference(s).

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

============ METHOD DETAIL ==========

- Method Detail

- getSnippet

```java
public
DeclarationSnippet
getSnippet()
```

Return the Snippet which has the unresolved reference(s).

**Returns:** the

Snippet

of the

RECOVERABLE_DEFINED

definition snippet.

Method Detail

- getSnippet

```java
public
DeclarationSnippet
getSnippet()
```

Return the Snippet which has the unresolved reference(s).

**Returns:** the

Snippet

of the

RECOVERABLE_DEFINED

definition snippet.

---

#### Method Detail

getSnippet

```java
public
DeclarationSnippet
getSnippet()
```

Return the Snippet which has the unresolved reference(s).

**Returns:** the

Snippet

of the

RECOVERABLE_DEFINED

definition snippet.

---

#### getSnippet

public

DeclarationSnippet

getSnippet()

Return the Snippet which has the unresolved reference(s).

---

