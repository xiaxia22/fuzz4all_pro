# Class PersistentSnippet

**Source:** `jdk.jshell\jdk\jshell\PersistentSnippet.html`

### Class Description

```java
public abstract class
PersistentSnippet

extends
Snippet
```

Grouping for Snippets which persist and influence future code.
A persistent snippet can be

overwritten

with new input.

PersistentSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Direct Known Subclasses:** DeclarationSnippet

,

ImportSnippet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
name()

Name of the Snippet.

**Returns:**
- the name of the snippet.

---

### Additional Sections

#### Class PersistentSnippet

java.lang.Object

- jdk.jshell.Snippet
- - jdk.jshell.PersistentSnippet

jdk.jshell.Snippet

- jdk.jshell.PersistentSnippet

jdk.jshell.PersistentSnippet

**Direct Known Subclasses:** DeclarationSnippet

,

ImportSnippet

```java
public abstract class
PersistentSnippet

extends
Snippet
```

Grouping for Snippets which persist and influence future code.
A persistent snippet can be

overwritten

with new input.

PersistentSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Since:** 9

public abstract class

PersistentSnippet

extends

Snippet

Grouping for Snippets which persist and influence future code.
A persistent snippet can be

overwritten

with new input.

PersistentSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

PersistentSnippet

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

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

name

()

Name of the Snippet.

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

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

name

()

Name of the Snippet.

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

Name of the Snippet.

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

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- name

```java
public
String
name()
```

Name of the Snippet.

**Returns:** the name of the snippet.

Method Detail

- name

```java
public
String
name()
```

Name of the Snippet.

**Returns:** the name of the snippet.

---

#### Method Detail

name

```java
public
String
name()
```

Name of the Snippet.

**Returns:** the name of the snippet.

---

#### name

public

String

name()

Name of the Snippet.

---

