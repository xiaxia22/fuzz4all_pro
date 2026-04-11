# Class DeclarationSnippet

**Source:** `jdk.jshell\jdk\jshell\DeclarationSnippet.html`

### Class Description

```java
public abstract class
DeclarationSnippet

extends
PersistentSnippet
```

Grouping for all declaration Snippets: variable declarations
(

VarSnippet

), method declarations
(

MethodSnippet

), and type declarations
(

TypeDeclSnippet

).

Declaration snippets are unique in that they can be active
with unresolved references:

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

.
Unresolved references can be queried with

JShell.unresolvedDependencies(DeclarationSnippet)

.

DeclarationSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Direct Known Subclasses:** MethodSnippet

,

TypeDeclSnippet

,

VarSnippet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Class DeclarationSnippet

java.lang.Object

- jdk.jshell.Snippet
- - jdk.jshell.PersistentSnippet
- - jdk.jshell.DeclarationSnippet

jdk.jshell.Snippet

- jdk.jshell.PersistentSnippet
- - jdk.jshell.DeclarationSnippet

jdk.jshell.PersistentSnippet

- jdk.jshell.DeclarationSnippet

jdk.jshell.DeclarationSnippet

**Direct Known Subclasses:** MethodSnippet

,

TypeDeclSnippet

,

VarSnippet

```java
public abstract class
DeclarationSnippet

extends
PersistentSnippet
```

Grouping for all declaration Snippets: variable declarations
(

VarSnippet

), method declarations
(

MethodSnippet

), and type declarations
(

TypeDeclSnippet

).

Declaration snippets are unique in that they can be active
with unresolved references:

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

.
Unresolved references can be queried with

JShell.unresolvedDependencies(DeclarationSnippet)

.

DeclarationSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Since:** 9

public abstract class

DeclarationSnippet

extends

PersistentSnippet

Grouping for all declaration Snippets: variable declarations
(

VarSnippet

), method declarations
(

MethodSnippet

), and type declarations
(

TypeDeclSnippet

).

Declaration snippets are unique in that they can be active
with unresolved references:

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

.
Unresolved references can be queried with

JShell.unresolvedDependencies(DeclarationSnippet)

.

DeclarationSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

Declaration snippets are unique in that they can be active
with unresolved references:

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

.
Unresolved references can be queried with

JShell.unresolvedDependencies(DeclarationSnippet)

.

DeclarationSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

DeclarationSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class jdk.jshell.

Snippet

Snippet.Kind

,

Snippet.Status

,

Snippet.SubKind

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class jdk.jshell.

PersistentSnippet

name

- Methods declared in class jdk.jshell.

Snippet

id

,

kind

,

source

,

subKind

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

Nested Class Summary

- Nested classes/interfaces declared in class jdk.jshell.

Snippet

Snippet.Kind

,

Snippet.Status

,

Snippet.SubKind

---

#### Nested Class Summary

Nested classes/interfaces declared in class jdk.jshell.

Snippet

Snippet.Kind

,

Snippet.Status

,

Snippet.SubKind

---

#### Nested classes/interfaces declared in class jdk.jshell. Snippet

Method Summary

- Methods declared in class jdk.jshell.

PersistentSnippet

name

- Methods declared in class jdk.jshell.

Snippet

id

,

kind

,

source

,

subKind

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

Methods declared in class jdk.jshell.

PersistentSnippet

name

---

#### Methods declared in class jdk.jshell. PersistentSnippet

Methods declared in class jdk.jshell.

Snippet

id

,

kind

,

source

,

subKind

---

#### Methods declared in class jdk.jshell. Snippet

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

